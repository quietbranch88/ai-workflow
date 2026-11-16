# Follow-up review and scan audit

## 2026-11-16 — Reconciliation and scope

- User authorized independent review/security scan, in-scope fixes and GitHub
  push/PR after verification. No merge or production action is authorized.
- Authoritative GitHub readback found PR #40 already merged on 2026-11-15 at
  1a8f6188c13107024378a7b3c4d7d29ff592ed32, head ebe9d7478c3e4128385bda44fc8a95921b91017c.
  Do not duplicate that PR or attribute its merge to this run.
- Re-anchor this follow-up to main 1a8f6188 on a separate feature branch.
- Fresh read-only reviewer covered c6e6887..ebe9d74: IR-01 (P2, confirmed/open),
  indentation-only valid checkbox is rejected; IR-02 (P3, confirmed/open),
  lowercase generic types and formatting tags are falsely rejected as filler.
  Existing TODO/list-marker fixes were checked as counterevidence, not reopened.
- These are correctness issues, not confirmed vulnerabilities. Review expected
  grammar/observable CLI results rather than copying implementation into tests.
- New tests on merged main: 15 methods ran, 8 assertion failures. Only whitespace
  or the meaningful evidence value differed from passing controls.
- Existing Codex Security scan 0479032d-4b0b-494a-9622-976bbc2f2312 remains bound
  to historical c6e6887..8821dcf; never relabel it as a scan of this new branch.
- Tool setup: PyPI bandit==1.8.6, wheel-only, task-local venv. Python 3.15 lacks
  a compatible PyYAML wheel, so retry with the bundled Python 3.12 runtime;
  no global installation, source build, credential access or config change.

## Fix verification and review follow-up

- IR-01: accept the same leading space/tab prefix as the existing checkbox parser.
- IR-02: do not treat directly adjacent generic arguments as template slots;
  recognise common formatting tags. This remains a documented heuristic, not
  a universal HTML/type parser or semantic evidence proof.
- Same new tests after the fix: 15 test methods passed; no assertions weakened.
- Independent read-only follow-up: 21 CLI probes passed, including indentation,
  lowercase generics, formatting tags and negative filler controls. IR-01/02
  are confirmed/fixed in that scope. Validator SHA-256:
  0162bc8fd4920b680f98d636f05f3b63e7ce8499fd89813b4c4da481b834456b.
- `python3 -m unittest discover -s tests -v`: 113 tests passed in 38.537 seconds.
  This includes the existing legacy/WIP/revision/private-record regression suite.
- Bandit 1.8.6 scans of main and corrected validator completed without scanner
  errors. Both report the identical 9 Low findings (B404 x1, B607 x4, B603 x4)
  at existing subprocess imports/call sites; 0 new result signatures and no
  Medium/High result. Exit 1 reflects baseline warnings, not a clean exit claim.
  Reviewed argv-only Git calls and unchanged original-object/private-path controls;
  Verify remains data, not executed. No newly reachable dangerous sink identified.
- Gitleaks 8.24.3 (official release checksum verified) directory scan completed
  with exit 0 and no leaks. A committed-range scan is recorded after commit.
- No project dependencies or lockfile changed; dependency advisory audit is not
  asserted. Python 3.12 tool venv and generated reports stay outside the repo.
- Historical Codex Security diff scan completed with no security findings for
  c6e6887..8821dcf only. Its immutable report is not evidence of a scan of this
  newer branch; current source is covered by the independent review, Bandit,
  Gitleaks and explicit changed-boundary inspection above.

## Prepared delivery

- Follow-up target is main, branch fix/verification-map-valid-content-20261116.
  The original PR #40 is already merged; no duplicate PR is needed.
- Local checks and PR metadata are ready. Push/PR creation and hosted CI are
  pending until actual provider receipts are obtained. No merge is authorized.

## Confirmed publication receipts

- `python3 scripts/check_close_the_loop.py` with explicit main/HEAD refs and
  committed-range Ship validation both passed with zero warnings before push.
- Gitleaks 8.24.3 outgoing range main..0ee6f19: exit 0, one commit scanned,
  no leaks. Directory scan also had no leaks.
- `git push -u github fix/verification-map-valid-content-20261116` succeeded;
  GitHub ref readback confirmed 0ee6f1958dc0638ad9731b9a4feea8aaf3b7f883.
- PR #41 created and read back as OPEN against main:
  https://github.com/quietbranch88/ai-workflow/pull/41
- This receipt-only commit changes no executable source or tests. Follow the
  PR's live check results for its final head, not the historical creation snapshot.
  No merge, deployment, repository setting change or plugin activation occurred.
