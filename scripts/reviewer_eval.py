#!/usr/bin/env python3
"""Export answer-free review packets or score independently adjudicated reports.

No model calls, candidate execution, semantic judge or automatic merge decisions.
"""
import argparse
import hashlib
import json
import shutil
import statistics
from pathlib import Path


DATA = Path(__file__).resolve().parents[1] / "evals" / "reviewer"
METADATA = ("model", "model_configuration", "harness", "prompt_revision",
            "tools_permissions", "budgets", "environment", "adjudicator")


def dataset_digest():
    digest = hashlib.sha256()
    for path in sorted([DATA / "oracle.json", *(DATA / "cases").rglob("*.md"),
                        *(DATA / "cases").rglob("*.py")]):
        digest.update(path.relative_to(DATA).as_posix().encode() + b"\0")
        digest.update(path.read_bytes() + b"\0")
    return digest.hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def export(destination):
    # A new directory prevents accidentally mixing prior answers into a packet.
    destination.mkdir(parents=True, exist_ok=False)
    oracle = json.loads((DATA / "oracle.json").read_text(encoding="utf-8"))
    for case_id in oracle["cases"]:
        packet = destination / case_id
        packet.mkdir()
        for name in ("CONTRACT.md", "candidate.py"):
            shutil.copyfile(DATA / "cases" / case_id / name, packet / name)
    return {"dataset_digest": dataset_digest(), "cases": list(oracle["cases"])}


def score(record):
    require(isinstance(record, dict), "Record must be an object")
    oracle = json.loads((DATA / "oracle.json").read_text(encoding="utf-8"))
    cases = oracle["cases"]
    require(record.get("schema_version") == 1, "Unsupported record schema")
    require(record.get("dataset_digest") == dataset_digest(), "Dataset digest mismatch")
    require(record.get("kind") in ("model-review", "synthetic"), "Missing run kind")
    metadata = record.get("metadata", {})
    require(isinstance(metadata, dict) and all(nonempty(metadata.get(k)) for k in METADATA),
            "All metadata fields must be nonempty strings; record unknowns explicitly")
    trials = record.get("trials")
    require(type(trials) is int and trials > 0, "trials must be a positive integer")
    results = record.get("results")
    require(isinstance(results, list), "results must be a list")
    seen = set()
    totals = dict(completed=0, infrastructure_errors=0, expected_defects=0,
                  detected_defects=0, false_positive_findings=0, duplicate_matches=0,
                  clean_cases=0, clean_cases_with_false_alarm=0, unassessed_defects=0)
    rounds = []
    per_case = []
    for result in results:
        require(isinstance(result, dict), "Each result must be an object")
        case_id, trial = result.get("case_id"), result.get("trial")
        require(isinstance(case_id, str) and case_id in cases, "Unknown case")
        require(type(trial) is int and 1 <= trial <= trials, "Invalid trial")
        key = (case_id, trial)
        require(key not in seen, "Duplicate case/trial")
        seen.add(key)
        count = result.get("rounds")
        require(type(count) is int and count >= 0, "Invalid round count")
        findings = result.get("findings")
        require(isinstance(findings, list), "findings must be a list")
        expected = set(cases[case_id]["defects"])
        status = result.get("status")
        if status == "infrastructure_error":
            require(nonempty(result.get("error")) and not findings,
                    "Infrastructure errors need a reason and no scored findings")
            totals["infrastructure_errors"] += 1
            totals["unassessed_defects"] += len(expected)
            per_case.append(dict(case_id=case_id, trial=trial, status=status))
            continue
        require(status == "completed" and count >= 1 and nonempty(result.get("raw_report")),
                "Completed reviews need rounds >= 1 and their raw report")
        totals["completed"] += 1
        totals["expected_defects"] += len(expected)
        rounds.append(count)
        matched, finding_ids = set(), set()
        false_positives = 0
        for finding in findings:
            require(isinstance(finding, dict), "Finding must be an object")
            fid = finding.get("id")
            require(nonempty(fid) and fid not in finding_ids, "Invalid/duplicate finding ID")
            finding_ids.add(fid)
            require(nonempty(finding.get("reason")), "Adjudication needs evidence/reason")
            require("defect_id" in finding, "Missing adjudication")
            defect = finding["defect_id"]
            if defect is None:
                false_positives += 1
            else:
                require(isinstance(defect, str) and defect in expected,
                        "Adjudication names a defect outside this case")
                if defect in matched:
                    totals["duplicate_matches"] += 1
                matched.add(defect)
        totals["detected_defects"] += len(matched)
        totals["false_positive_findings"] += false_positives
        if not expected:
            totals["clean_cases"] += 1
            totals["clean_cases_with_false_alarm"] += int(false_positives > 0)
        per_case.append(dict(case_id=case_id, trial=trial, status=status,
                             detected=sorted(matched), missed=sorted(expected - matched),
                             false_positive_findings=false_positives, rounds=count))
    require(len(seen) == len(cases) * trials,
            "Every case/trial needs a result, including infrastructure errors")
    totals["missed_defects"] = totals["expected_defects"] - totals["detected_defects"]
    return {"kind": record["kind"], "dataset_digest": record["dataset_digest"],
            "metadata": metadata, "trials": trials, "scheduled": len(seen), **totals,
            "recall_on_completed": (totals["detected_defects"] / totals["expected_defects"]
                                    if totals["expected_defects"] else None),
            "clean_case_false_alarm_rate": (totals["clean_cases_with_false_alarm"] /
                                           totals["clean_cases"] if totals["clean_cases"] else None),
            "mean_rounds_completed": statistics.mean(rounds) if rounds else None,
            "max_rounds_completed": max(rounds) if rounds else None,
            "per_case": per_case}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("export").add_argument("destination", type=Path)
    commands.add_parser("score").add_argument("record", type=Path)
    args = parser.parse_args()
    try:
        result = (export(args.destination) if args.command == "export" else
                  score(json.loads(args.record.read_text(encoding="utf-8"))))
    except (ValueError, OSError, TypeError) as exc:
        parser.exit(2, f"reviewer-eval: {exc}\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
