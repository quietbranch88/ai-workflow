import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


EVAL = load(ROOT / "scripts/reviewer_eval.py", "reviewer_eval")


def sample():
    record = dict(schema_version=1, kind="synthetic", dataset_digest=EVAL.dataset_digest(),
                  metadata={key: "synthetic scorer test; no model" for key in EVAL.METADATA},
                  trials=1, results=[])
    for index in range(1, 5):
        record["results"].append(dict(case_id=f"case-{index:02}", trial=1,
                                      status="completed", rounds=1,
                                      raw_report="Synthetic report, no actionable findings.", findings=[]))
    return record


class ReferenceBehaviorTests(unittest.TestCase):
    def candidate(self, case):
        return load(EVAL.DATA / "cases" / case / "candidate.py", case)

    def test_installer_pair_against_no_write_contract(self):
        bad, good = (self.candidate(c) for c in ("case-01", "case-03"))
        for mode in ("instal", "check", "restore"):
            observed = []
            bad.sync(mode, lambda: observed.append("backup"), lambda: observed.append("write"))
            self.assertEqual(["write"], observed, "Historical defect must still reproduce")
            observed = []
            if mode == "check":
                self.assertEqual(0, good.sync(mode, lambda: observed.append("backup"),
                                              lambda: observed.append("write")))
            else:
                with self.assertRaises(ValueError):
                    good.sync(mode, lambda: observed.append("backup"), lambda: observed.append("write"))
            self.assertEqual([], observed)
        for candidate in (bad, good):
            observed = []
            self.assertEqual(0, candidate.sync("install", lambda: observed.append("backup"),
                                               lambda: observed.append("write")))
            self.assertEqual(["backup", "write"], observed)

    def test_acceptance_pair_against_quality_warning_contract(self):
        bad, good = (self.candidate(c) for c in ("case-04", "case-02"))
        for text in ("Observable:\nEnvironment: \nVerify:\t", "prose Observable: Environment: Verify:"):
            self.assertEqual((0, []), bad.check(text), "Historical defect must still reproduce")
            self.assertEqual((0, ["Observable", "Environment", "Verify"]), good.check(text))
        self.assertEqual((0, []), good.check("\u00a0Observable: result\nEnvironment: fixture\nVerify: test"))
        for prefix in ("-", "prose ", "-- "):
            self.assertEqual((0, ["Observable"]), good.check(prefix + "Observable: result\nEnvironment: local\nVerify: test"))
        for prefix in ("", " ", "\t", "\u00a0", "- ", "\t-\t"):
            self.assertEqual((0, []), good.check(prefix + "Observable: result\nEnvironment: local\nVerify: test"))
        for separator in ("\n", "\r\n"):
            text = separator.join(["- observable: result", " Environment: fixture", "Verify: test"])
            for candidate in (bad, good):
                self.assertEqual((0, []), candidate.check(text))
        self.assertEqual((0, []), good.check("Observable:\nObservable: result\nEnvironment: local\nVerify: test"))
        self.assertEqual((0, ["Verify"]), good.check("Observable: result\nEnvironment: fixture"))


class ScorerTests(unittest.TestCase):
    def test_hand_calculated_mixed_outcomes_and_cli(self):
        record = sample()
        record["results"][0]["findings"] = [
            dict(id="f1", defect_id="mode-dispatch", reason="check calls write"),
            dict(id="f2", defect_id="mode-dispatch", reason="same class for unknown mode")]
        record["results"][1]["findings"] = [dict(id="f1", defect_id=None, reason="invented defect")]
        record["results"][1]["rounds"] = 2
        record["results"][2].update(status="infrastructure_error", error="worker unavailable", rounds=0)
        record["results"][3]["rounds"] = 3
        result = EVAL.score(record)
        self.assertEqual((3, 1, 1, 1, 1, 1), tuple(result[k] for k in (
            "completed", "infrastructure_errors", "detected_defects", "missed_defects",
            "false_positive_findings", "duplicate_matches")))
        self.assertEqual(0.5, result["recall_on_completed"])
        self.assertEqual(1.0, result["clean_case_false_alarm_rate"])
        self.assertEqual(2, result["mean_rounds_completed"])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "record.json"
            path.write_text(json.dumps(record))
            process = subprocess.run([sys.executable, str(ROOT / "scripts/reviewer_eval.py"),
                                      "score", str(path)], capture_output=True, text=True, check=True)
            self.assertEqual(result, json.loads(process.stdout))

    def test_clean_and_infrastructure_only_runs_do_not_invent_recall(self):
        record = sample()
        for index in (0, 3):
            record["results"][index].update(status="infrastructure_error", error="timeout", rounds=0)
        result = EVAL.score(record)
        self.assertIsNone(result["recall_on_completed"])
        self.assertEqual(2, result["unassessed_defects"])
        self.assertEqual(0, result["clean_case_false_alarm_rate"])
        for result in record["results"]:
            result.update(status="infrastructure_error", error="timeout", rounds=0)
        result = EVAL.score(record)
        self.assertIsNone(result["mean_rounds_completed"])
        self.assertIsNone(result["clean_case_false_alarm_rate"])

    def test_records_reject_omissions_duplicates_contamination_and_bad_adjudication(self):
        mutations = [
            lambda r: r["results"].pop(),
            lambda r: r["results"].append(copy.deepcopy(r["results"][0])),
            lambda r: r.update(dataset_digest="old"),
            lambda r: r["results"][0].update(rounds=True),
            lambda r: r["results"][0].update(raw_report=" "),
            lambda r: r["metadata"].update(adjudicator=""),
            lambda r: r["results"][1].update(findings=[dict(id="x", defect_id="mode-dispatch", reason="wrong case")]),
            lambda r: r["results"][0].update(findings=[dict(id="x", reason="missing adjudication")]),
            lambda r: r["results"][0].update(findings=[dict(id="x", defect_id=None, reason=" ")]),
            lambda r: r["results"][0].update(status="infrastructure_error", error="timeout",
                                           findings=[dict(id="x", defect_id="mode-dispatch", reason="partial")]),
        ]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                record = sample()
                mutate(record)
                with self.assertRaises(ValueError):
                    EVAL.score(record)
        with self.assertRaises(ValueError):
            EVAL.score([])

    def test_export_excludes_oracles_and_refuses_existing_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "packets"
            result = EVAL.export(destination)
            self.assertEqual(EVAL.dataset_digest(), result["dataset_digest"])
            self.assertEqual(8, len([p for p in destination.rglob("*") if p.is_file()]))
            self.assertFalse((destination / "oracle.json").exists())
            self.assertEqual({"CONTRACT.md", "candidate.py"}, {p.name for p in destination.rglob("*") if p.is_file()})
            with self.assertRaises(FileExistsError):
                EVAL.export(destination)


if __name__ == "__main__":
    unittest.main()
