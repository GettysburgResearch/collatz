"""Adversarial tests for X-9102's parametric reset-spine decision."""

from __future__ import annotations

import copy
import json
import tempfile
import unittest
from itertools import product
from pathlib import Path

from check_result import (
    Family as CheckerFamily,
    _independent_trace,
    _load_strict,
    check_payload,
)
from symbolic_closure import (
    BDD,
    Family,
    _materialize_candidate,
    _sha256_value,
    build_result,
    classify_gate,
    compact_guarded_parametric_witness,
    guarded_closure_fixed_point,
    guarded_parametric_witness,
)


class DecisionDiagramTests(unittest.TestCase):
    def test_reduced_diagram_counts_and_models(self) -> None:
        manager = BDD(4)
        x0 = manager.literal(0)
        x1 = manager.literal(1)
        formula = manager.disjunction(
            manager.conjunction(x0, x1),
            manager.conjunction(manager.negate(x0), x1),
        )
        self.assertEqual(formula, x1)
        self.assertEqual(manager.model_count(formula), 8)
        model = manager.pick_model(formula)
        self.assertIsNotNone(model)
        self.assertEqual(model[1], 1)  # type: ignore[index]
        self.assertEqual(
            manager.structural_digest(manager.TRUE),
            "dd82ce80ace3118921c768215569c33c5739c0401055d7d80814f7dbd20b81c6",
        )

    def test_family_validation_is_strict(self) -> None:
        bad = (
            lambda: Family.create(2, 2),
            lambda: Family.create(True, 2),
            lambda: Family.create(5, 1),
            lambda: Family.create(5, 5),
            lambda: Family.create(5, False),
        )
        for call in bad:
            with self.subTest(call=call):
                with self.assertRaises(ValueError):
                    call()


class SmallExhaustiveDifferentialTests(unittest.TestCase):
    def test_q3_through_q8_against_every_materialized_x9101_dfa(self) -> None:
        checked_assignments = 0
        for q in range(3, 9):
            for gate in range(2, q):
                family = Family.create(q, gate)
                record = classify_gate(q, gate)
                self.assertEqual(record["status"], "UNSAT", (q, gate))
                self.assertEqual(
                    record["guarded_reachability"][
                        "closure_violation_assignments"
                    ],
                    1 << (q - 3),
                )

                # This is the literal least-reachability product, not the
                # compact factor proof used at q=71.
                explicit, manager, accepted, bad = guarded_parametric_witness(
                    q, gate
                )
                self.assertEqual(
                    manager.model_count(accepted), 1 << (q - 3)
                )
                self.assertEqual(manager.model_count(bad), 1 << (q - 3))
                self.assertEqual(
                    explicit["closure_violation_assignments"], 1 << (q - 3)
                )

                for assignment in product((0, 1), repeat=q - 3):
                    checked_assignments += 1
                    _, lifted, materialized = _materialize_candidate(
                        family, assignment
                    )
                    verification = materialized["x9101_verify_candidate"]
                    self.assertFalse(verification["valid"], (q, gate, assignment))
                    self.assertEqual(
                        verification["reason"],
                        "language is not forward invariant",
                    )
                    labels = family.labels_from_assignment(assignment)
                    witness = (1,) + labels + (1,)
                    self.assertTrue(lifted.accepts_canonical(witness))

                    # The existing X-9101 verifier's shortest closure witness
                    # is exactly the parametric word certified by X-9102.
                    observed = verification["closure_input_lsd"]
                    self.assertEqual(
                        observed,
                        "".join(str(bit) for bit in witness),
                        (q, gate, assignment),
                    )
        self.assertEqual(checked_assignments, 321)

    def test_full_fixed_point_agrees_on_small_families(self) -> None:
        for q in range(3, 7):
            for gate in range(2, q):
                result = guarded_closure_fixed_point(
                    q,
                    gate,
                    node_limit=1_000_000,
                    update_limit=1_000_000,
                )
                self.assertEqual(result["status"], "UNSAT", (q, gate))
                self.assertEqual(result["bad_assignments"], 1 << (q - 3))

    def test_one_q71_materialization_per_active_gate_is_rejected(self) -> None:
        for gate in range(3, 71):
            family = Family.create(71, gate)
            _, _, materialized = _materialize_candidate(family, (0,) * 68)
            verification = materialized["x9101_verify_candidate"]
            self.assertFalse(verification["valid"], gate)
            self.assertEqual(
                verification["reason"], "language is not forward invariant"
            )

    def test_compact_and_explicit_guarded_traces_have_same_coverage(self) -> None:
        for q in range(3, 9):
            for gate in range(2, q):
                compact = compact_guarded_parametric_witness(q, gate)
                explicit, _, _, _ = guarded_parametric_witness(q, gate)
                independent = _independent_trace(CheckerFamily(q, gate))
                for field in (
                    "accepted_input_assignments",
                    "closure_violation_assignments",
                    "parameter_assignments",
                ):
                    self.assertEqual(compact[field], explicit[field])
                    self.assertEqual(explicit[field], independent[field])
                self.assertTrue(compact["terminal_flush_included"])


class IndependentArtifactCheckerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = build_result(q=8, gate_min=2, gate_max=7)

    def _reseal(self, payload: dict[str, object]) -> None:
        unsigned = dict(payload)
        unsigned.pop("result_sha256", None)
        payload["result_sha256"] = _sha256_value(unsigned)

    def test_independent_checker_reconstructs_all_proofs(self) -> None:
        receipt = check_payload(self.payload)
        self.assertEqual(receipt["status"], "independently_verified")
        self.assertEqual(
            receipt["status_counts"],
            {"SAT": 0, "UNSAT": 6, "UNKNOWN": 0},
        )
        self.assertEqual(receipt["unsat_proofs_checked"], 6)

    def test_digest_and_resealed_semantic_tampering_are_rejected(self) -> None:
        changed = copy.deepcopy(self.payload)
        changed["records"][0]["guarded_reachability"][
            "closure_violation_assignments"
        ] -= 1
        with self.assertRaisesRegex(ValueError, "result digest mismatch"):
            check_payload(changed)

        self._reseal(changed)
        with self.assertRaisesRegex(ValueError, "guarded trace differs"):
            check_payload(changed)

        changed = copy.deepcopy(self.payload)
        changed["records"][0]["proof"]["alignment_cases"][0][
            "equation_solution_m"
        ] = 1
        self._reseal(changed)
        with self.assertRaisesRegex(ValueError, "factor-alignment proof"):
            check_payload(changed)

        changed = copy.deepcopy(self.payload)
        changed["backend"]["cnf_emitted"] = True
        changed["backend"]["cnf_sha256"] = "0" * 64
        self._reseal(changed)
        with self.assertRaisesRegex(ValueError, "backend contract"):
            check_payload(changed)

    def test_strict_json_rejects_duplicates_and_nonfinite_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                _load_strict(duplicate)
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":NaN}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "nonstandard JSON"):
                _load_strict(nonfinite)

    def test_result_generation_is_deterministic(self) -> None:
        second = build_result(q=8, gate_min=2, gate_max=7)
        self.assertEqual(second, self.payload)
        self.assertEqual(
            self.payload["result_sha256"],
            "2ea50e670912ae547fce508503d14585f9e6ca9928ecf151b6e0fbf23aa39a5b",
        )


if __name__ == "__main__":
    unittest.main()
