#!/usr/bin/env python3
"""Pre-push guard for tracked or explicitly local-only living-tier docs.

Enforces workflow.md's close-the-loop rule mechanically: if the commits being
pushed change code but touch neither `.spec/**` nor `devlog.md` / `todo.md`,
the push is rejected with a reminder.

Default tracked-policy scope rules:
- Only enforces in repos that follow the discipline (a `.spec/` dir exists).
- Doc-only pushes always pass.
- Only `.spec/**/current.md`, `.spec/**/tasks.md`, `devlog.md`, and `todo.md`
  count as living-tier evidence; historical audit/ADR files do not.
- An unresolved comparison range fails visibly instead of silently passing.
- Escape hatches: `git push --no-verify`, or `CLOSE_THE_LOOP=skip git push`.

Explicit local-only policy checks the named local ticket and rejects private
records in the index or outgoing commits, even for doc-only pushes. It does not
use CLOSE_THE_LOOP=skip. These are local safeguards, not hosted enforcement.

Wire-up (pre-commit framework, pre-push stage) — see pre-commit.template.yaml.
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
from validate_workflow_docs import emit_report, validate_workflow_documents  # noqa: E402

ZEROS = "0" * 40
PROJECT_LIVING_PATHS = {"devlog.md", "todo.md"}
SPEC_LIVING_BASENAMES = {"current.md", "tasks.md"}


def git(*args, input=None):
    return subprocess.run(
        ["git", *args], input=input, capture_output=True, text=True
    )


def resolve_range():
    """Return the outgoing comparison range, or None so the guard fails closed."""
    from_ref = os.environ.get("PRE_COMMIT_FROM_REF") or ""
    to_ref = os.environ.get("PRE_COMMIT_TO_REF") or "HEAD"

    if not from_ref or from_ref == ZEROS:
        # New branch: compare against the default branch if we can find one.
        for candidate in ("origin/HEAD", "origin/main", "origin/master"):
            base = git("merge-base", candidate, to_ref)
            if base.returncode == 0 and base.stdout.strip():
                return base.stdout.strip(), to_ref
        return None  # caller reports the unresolved range and refuses the push

    return from_ref, to_ref


def changed_files(from_ref, to_ref):
    diff = git("diff", "--name-only", f"{from_ref}..{to_ref}")
    if diff.returncode != 0:
        return None
    return [line.strip() for line in diff.stdout.splitlines() if line.strip()]


def is_living_doc(path):
    p = path.replace("\\", "/")
    basename = p.rsplit("/", 1)[-1].lower()
    return (
        (p.startswith(".spec/") and basename in SPEC_LIVING_BASENAMES)
        or p.lower() in PROJECT_LIVING_PATHS
    )


def is_doc(path):
    return is_living_doc(path) or path.lower().endswith(".md")


def validate_private_history(revisions):
    """Reject private records even when a later outgoing commit removes them."""
    commits = git("rev-list", "--stdin", input="\n".join(revisions) + "\n")
    if commits.returncode:
        sys.stderr.write("close-the-loop: unable to inspect outgoing commits\n")
        return False
    for commit in commits.stdout.splitlines():
        tree = git("ls-tree", "-r", "--name-only", commit, "--", ".spec")
        if tree.returncode or tree.stdout:
            sys.stderr.write("close-the-loop: private records in an outgoing commit or unreadable tree\n")
            return False
    return True


def native_push_revisions(remote, stream):
    """Consume every native pre-push update; pre-commit exposes only one pair."""
    updates = []
    for line in stream.splitlines():
        fields = line.split()
        if len(fields) != 4 or any(
            not re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", fields[index])
            for index in (1, 3)
        ):
            sys.stderr.write("close-the-loop: invalid native pre-push input\n")
            return None
        _, local_sha, _, remote_sha = fields
        if local_sha.strip("0"):
            updates.append((local_sha, remote_sha))
    if not updates:
        return []

    remote_tips = []
    if any(not old.strip("0") for _, old in updates):
        # A new ref has no old SHA. Use current advertised refs, not a possibly
        # stale local origin/HEAD that can hide unpublished private history.
        advertised = git("ls-remote", "--refs", "--", remote)
        if advertised.returncode:
            sys.stderr.write("close-the-loop: unable to inspect remote refs\n")
            return None
        for line in advertised.stdout.splitlines():
            sha = line.split()[0]
            if not re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", sha):
                sys.stderr.write("close-the-loop: invalid remote object ID\n")
                return None
            if git("cat-file", "-e", f"{sha}^{{commit}}").returncode == 0:
                remote_tips.append(sha)

    ranges = []
    for local_sha, remote_sha in updates:
        # Check the tip even when the same object is already advertised elsewhere.
        tree = git("ls-tree", "-r", "--name-only", local_sha, "--", ".spec")
        if tree.returncode or tree.stdout:
            sys.stderr.write("close-the-loop: private records in an outgoing commit or unreadable tree\n")
            return None
        excluded = [remote_sha] if remote_sha.strip("0") else remote_tips
        ranges.append([local_sha, *(f"^{sha}" for sha in excluded)])
    return ranges


def main(spec_policy="tracked", ticket=None, native=False, remote=None):
    if spec_policy == "local-only":
        # Privacy policy must not be disabled by the legacy tracked-doc escape hatch.
        if not native or not remote:
            sys.stderr.write("close-the-loop: local-only requires the native pre-push hook; "
                             "pre-commit does not expose every pushed ref\n")
            return 1
        ranges = native_push_revisions(remote, sys.stdin.read())
        if ranges is None or any(not validate_private_history(revisions) for revisions in ranges):
            return 1
        report = validate_workflow_documents(Path.cwd(), [], "wip",
                                             spec_policy="local-only", ticket=ticket)
        emit_report(report)
        return 0 if report.ok else 1
    if os.environ.get("CLOSE_THE_LOOP", "").lower() == "skip":
        return 0
    if not os.path.isdir(".spec"):
        return 0

    resolved = resolve_range()
    if resolved is None:
        sys.stderr.write(
            "close-the-loop: unable to resolve the outgoing comparison range; "
            "refusing to treat this push as verified.\n"
            "Set PRE_COMMIT_FROM_REF/PRE_COMMIT_TO_REF or fetch origin/HEAD, "
            "then retry. Intentional exception: CLOSE_THE_LOOP=skip git push\n"
        )
        return 1
    files = changed_files(*resolved)
    if files is None:
        sys.stderr.write(
            "close-the-loop: git diff failed for the outgoing comparison "
            "range; refusing to pass silently.\n"
        )
        return 1
    if not files:
        return 0

    code = [f for f in files if not is_doc(f)]
    if not code:
        return 0
    if not any(is_living_doc(f) for f in files):
        sys.stderr.write(
            "close-the-loop: this push changes code but no living-tier doc.\n"
            "workflow.md requires updating, in the SAME PR:\n"
            "  .spec/<ticket>/{current.md,tasks.md}\n"
            "  devlog.md (newest-on-top entry) and todo.md\n"
            f"Code files pushed without docs ({len(code)}): {', '.join(code[:5])}"
            f"{' …' if len(code) > 5 else ''}\n"
            "Intentional? CLOSE_THE_LOOP=skip git push   (or git push --no-verify)\n"
        )
        return 1

    report = validate_workflow_documents(os.getcwd(), files, "wip")
    emit_report(report)
    if not report.ok:
        sys.stderr.write(
            "close-the-loop: living-doc structure is invalid. This guard still "
            "cannot prove semantic correctness.\n"
        )
        return 1
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec-policy", choices=("tracked", "local-only"), default="tracked")
    parser.add_argument("--ticket", default=os.environ.get("WORKFLOW_TICKET"))
    parser.add_argument("--native-pre-push", action="store_true")
    parser.add_argument("remote_name", nargs="?")
    parser.add_argument("remote_url", nargs="?")
    args = parser.parse_args()
    sys.exit(main(args.spec_policy, args.ticket, args.native_pre_push, args.remote_url))
