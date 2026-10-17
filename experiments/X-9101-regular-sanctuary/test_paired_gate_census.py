"""Adversarial tests for the compact paired-gate census wrapper."""

from __future__ import annotations

import json
import math
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from paired_gate_census import (
    INCOMPLETE_DISCLAIMER,
    SCHEMA,
    _aggregate,
    _atomic_json_write,
    _classification,
    _seal_partition,
    _seal_wrapper,
    _sha256_object,
    outside_in_schedule,
    run_census,
    validate_census,
)
from spine_cegis import BANK_SCHEMA, BANK_SEMANTICS, SCHEMA as SPINE_SCHEMA


def _write_empty_shortcut_bank(path: Path) -> None:
    payload: dict[str, object] = {
        "schema": BANK_SCHEMA,
        "program": "exact-floor-spine-cegis",
        "semantics": BANK_SEMANTICS,
        "source": {
            "checkpoint_sha256": "0" * 64,
            "checkpoint_schema": SPINE_SCHEMA,
            "logical_signature": {
                "state_count": 5,
                "gate": 0,
                "force_zero_loop": True,
                "force_11_prefix": True,
                "solver_seed": 0,
            },
            "status": "running",
            "locally_learned_implications": 0,
            "inherited_imported_implications": 0,
        },
        "implication_count": 0,
        "implications_sha256": _sha256_object([]),
        "implications": [],
    }
    payload["bank_sha256"] = _sha256_object(payload)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


class PairedGateCensusPureTests(unittest.TestCase):
    def test_atomic_writer_retries_a_transient_windows_lock(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "wrapper.json"
            real_replace = os.replace
            calls = 0

            def transient_replace(source: str, target: str | Path) -> None:
                nonlocal calls
                calls += 1
                if calls == 1:
                    raise PermissionError("transient indexer lock")
                real_replace(source, target)

            with mock.patch(
                "paired_gate_census.os.replace", side_effect=transient_replace
            ), mock.patch("paired_gate_census.time.sleep"):
                _atomic_json_write(output, {"ok": True})

            self.assertEqual(calls, 2)
            self.assertEqual(
                json.loads(output.read_text(encoding="utf-8")), {"ok": True}
            )

    def test_outside_in_schedule_and_parameter_boundaries(self) -> None:
        self.assertEqual(outside_in_schedule(2, 2), [2])
        self.assertEqual(outside_in_schedule(2, 6), [2, 6, 3, 5, 4])
        self.assertEqual(outside_in_schedule(2, 7), [2, 7, 3, 6, 4, 5])
        with self.assertRaises(ValueError):
            outside_in_schedule(3, 2)
        with self.assertRaises(ValueError):
            run_census(
                bank_path=Path("missing.json"),
                output_path=Path("unused.json"),
                suffix_state_count=5,
                raw_state_count=5,
                first_suffix_gate=2,
                last_suffix_gate=2,
                workers=1,
            )

    def test_status_classification_is_explicitly_bounded(self) -> None:
        self.assertEqual(
            _classification("model_limit", 1),
            ("bounded_model_quota", True),
        )
        self.assertEqual(
            _classification("time_limit", 0),
            ("zero_model_stall", True),
        )
        self.assertEqual(
            _classification("solver_unknown", 2),
            ("bounded_incomplete", True),
        )
        self.assertEqual(
            _classification("solver_unsat", 0),
            ("solver_unsat_without_independent_proof", True),
        )
        self.assertEqual(
            _classification("verified_candidate", 1),
            ("verified_candidate", False),
        )


try:
    import z3  # type: ignore[import-not-found]  # noqa: F401

    HAVE_Z3 = True
except ImportError:
    HAVE_Z3 = False


@unittest.skipUnless(HAVE_Z3, "paired census synthesis requires z3-solver")
class PairedGateCensusSynthesisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temporary = tempfile.TemporaryDirectory()
        root = Path(cls.temporary.name)
        cls.bank = root / "empty-bank.json"
        cls.wrapper = root / "paired-census.json"
        _write_empty_shortcut_bank(cls.bank)
        cls.result = run_census(
            bank_path=cls.bank,
            output_path=cls.wrapper,
            suffix_state_count=5,
            raw_state_count=6,
            first_suffix_gate=2,
            last_suffix_gate=3,
            solver_seed=0,
            model_quota=1,
            watchdog_seconds=10.0,
            workers=2,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temporary.cleanup()

    def _fresh_data(self) -> dict[str, object]:
        return json.loads(self.wrapper.read_text(encoding="utf-8"))

    def test_parallel_wave_is_compact_ordered_atomic_and_strictly_valid(self) -> None:
        data = self._fresh_data()
        self.assertEqual(data["schema"], SCHEMA)
        self.assertEqual(data["status"], "complete")
        self.assertEqual(data["disclaimer"], INCOMPLETE_DISCLAIMER)
        self.assertEqual(
            data["plan"]["outside_in_suffix_gate_order"], [2, 3]
        )
        self.assertEqual(
            [item["task_index"] for item in data["partitions"]],
            [0, 1, 2, 3],
        )
        self.assertEqual(data["baseline"]["raw_implication_count"], 0)
        self.assertEqual(data["baseline"]["suffix_implication_count"], 0)
        self.assertFalse(Path(data["baseline"]["shortcut_bank_path"]).is_absolute())
        self.assertIn(
            "independent_check.py",
            data["environment"]["implementation_sha256"],
        )
        for partition in data["partitions"]:
            self.assertNotIn("imported_implications", partition)
        raw_bytes = self.wrapper.read_bytes()
        self.assertTrue(raw_bytes.endswith(b"\n"))
        self.assertNotIn(b"\r\n", raw_bytes)
        report = validate_census(self.wrapper)
        self.assertTrue(report["valid"])
        self.assertEqual(report["partitions_validated"], 4)
        self.assertEqual(report["models_reverified"], 4)
        self.assertGreater(report["local_implications_recomputed"], 0)

    def test_validation_never_instantiates_z3(self) -> None:
        with mock.patch(
            "spine_cegis._require_z3",
            side_effect=AssertionError("validator attempted to instantiate Z3"),
        ), mock.patch(
            "odd_suffix_cegis._require_z3",
            side_effect=AssertionError("validator attempted to instantiate Z3"),
        ):
            report = validate_census(self.wrapper)
        self.assertTrue(report["valid"])

    def test_resealed_verification_tampering_is_caught_by_exact_replay(self) -> None:
        data = self._fresh_data()
        partition = data["partitions"][0]
        partition["model_records"][0]["verification"]["relation_edges"] += 1
        data["partitions"][0] = _seal_partition(partition)
        data["aggregate"] = _aggregate(
            data["partitions"], data["plan"]["partition_count"]
        )
        data = _seal_wrapper(data)
        bad = self.wrapper.parent / "bad-verification.json"
        bad.write_text(
            json.dumps(data, indent=2, sort_keys=True, allow_nan=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        with self.assertRaisesRegex(ValueError, "verification disagrees"):
            validate_census(bad)

    def test_strict_root_and_nonfinite_json_are_rejected(self) -> None:
        extra = self._fresh_data()
        extra["unexpected"] = True
        bad_extra = self.wrapper.parent / "bad-extra.json"
        bad_extra.write_text(json.dumps(extra), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "wrapper fields"):
            validate_census(bad_extra)

        bad_nan = self.wrapper.parent / "bad-nan.json"
        bad_nan.write_text('{"elapsed": NaN}', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "nonfinite JSON"):
            validate_census(bad_nan)

        bad_duplicate = self.wrapper.parent / "bad-duplicate.json"
        bad_duplicate.write_text('{"schema": 1, "schema": 2}', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "duplicate JSON"):
            validate_census(bad_duplicate)

    def test_payload_and_semantic_digests_have_distinct_volatility(self) -> None:
        data = self._fresh_data()
        original_semantic = data["partitions"][0]["semantic_sha256"]
        original_payload = data["partitions"][0]["payload_sha256"]
        data["partitions"][0]["external_wall_seconds"] += 0.25
        resealed = _seal_partition(data["partitions"][0])
        self.assertEqual(resealed["semantic_sha256"], original_semantic)
        self.assertNotEqual(resealed["payload_sha256"], original_payload)

    def test_two_model_quota_preserves_replayable_batch_history(self) -> None:
        output = self.wrapper.parent / "two-model-census.json"
        result = run_census(
            bank_path=self.bank,
            output_path=output,
            suffix_state_count=5,
            raw_state_count=6,
            first_suffix_gate=2,
            last_suffix_gate=2,
            solver_seed=0,
            model_quota=2,
            watchdog_seconds=10.0,
            workers=1,
        )
        self.assertEqual(result["aggregate"]["models_checked"], 4)
        for partition in result["partitions"]:
            self.assertEqual(partition["models_checked"], 2)
            self.assertEqual(len(partition["model_records"]), 2)
            self.assertEqual(partition["status"], "model_limit")
        report = validate_census(output)
        self.assertEqual(report["models_reverified"], 4)

    def test_resealed_baseline_identity_tampering_is_rejected(self) -> None:
        data = self._fresh_data()
        data["baseline"]["bank_file_sha256"] = "f" * 64
        data = _seal_wrapper(data)
        bad = self.wrapper.parent / "bad-baseline.json"
        bad.write_text(
            json.dumps(data, indent=2, sort_keys=True, allow_nan=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        with self.assertRaisesRegex(ValueError, "baseline identity"):
            validate_census(bad)


if __name__ == "__main__":
    unittest.main()
