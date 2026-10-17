"""Adversarial tests for the reset-pattern spine audit."""

from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
from unittest.mock import patch

from automata import encode_lsd
from odd_core import direct_fully_accelerated_odd, odd_core_transducer
from reset_spine import (
    SCIENTIFIC_Q,
    SEMANTIC_DIGEST_SERIALIZATION,
    _sha256_value,
    build_audit,
    contains_reset_pattern,
    first_uncovered_reset_labels,
    indexed_reset_labels,
    least_odd_image_formula,
    least_odd_integer,
    least_suffix_word,
    main,
    normal_form_checks,
    reset_pattern_dfa,
    reset_pattern_word,
    reset_spine_dfa,
    reset_spine_labels,
    targeted_implication,
    validate_audit,
)


class ResetPatternConstructionTests(unittest.TestCase):
    def test_parameters_and_patterns_are_strictly_validated(self) -> None:
        bad_calls = (
            lambda: reset_spine_labels(2, 1),
            lambda: reset_spine_labels(True, 2),
            lambda: reset_spine_labels(4, 1),
            lambda: reset_spine_labels(4, 4),
            lambda: reset_spine_labels(4, False),
            lambda: reset_pattern_dfa(4, 2, (1, 0)),
            lambda: reset_pattern_dfa(4, 2, (0, 0, 1)),
            lambda: reset_pattern_dfa(4, 2, (1, 1, 0)),
            lambda: reset_pattern_dfa(4, 2, (1, 0, True)),
            lambda: indexed_reset_labels(4, 2, -1),
            lambda: indexed_reset_labels(4, 2, 2),
            lambda: indexed_reset_labels(4, 2, True),
            lambda: contains_reset_pattern(4, 2, (1, 0, 1), (1, 0)),
            lambda: contains_reset_pattern(4, 2, (1, 0, 1), (1, True, 1)),
            lambda: first_uncovered_reset_labels(4, 2, ((1, 0),)),
        )
        for call in bad_calls:
            with self.subTest(call=call):
                with self.assertRaises(ValueError):
                    call()

    def test_every_small_pattern_satisfies_normal_form_and_factor_theorem(
        self,
    ) -> None:
        for q in range(3, 8):
            for h in range(2, q):
                seen: set[tuple[int, ...]] = set()
                for index in range(1 << (q - 3)):
                    labels = indexed_reset_labels(q, h, index)
                    pattern = reset_pattern_word(q, h, labels)
                    seen.add(pattern)
                    dfa = reset_pattern_dfa(q, h, labels)
                    self.assertTrue(
                        all(normal_form_checks(dfa, q, h, labels).values()),
                        (q, h, labels),
                    )
                    for length in range(q + 4):
                        for suffix in product((0, 1), repeat=length):
                            if suffix and suffix[-1] != 1:
                                continue
                            accepted = dfa.run(suffix) == h
                            if length < q:
                                self.assertFalse(accepted, (q, h, labels, suffix))
                            if accepted:
                                self.assertTrue(
                                    contains_reset_pattern(q, h, labels, suffix),
                                    (q, h, labels, suffix),
                                )
                self.assertEqual(len(seen), 1 << (q - 3))

    def test_required_factor_need_not_be_the_terminal_window(self) -> None:
        dfa = reset_pattern_dfa(3, 2, (1, 0))
        suffix = (1, 0, 1, 1)
        self.assertEqual(dfa.run(suffix), 2)
        self.assertTrue(contains_reset_pattern(3, 2, (1, 0), suffix))
        self.assertEqual(suffix[-3:], (0, 1, 1))
        self.assertNotEqual(suffix[-3:], reset_pattern_word(3, 2, (1, 0)))

    def test_constructive_factor_pigeonhole_boundary(self) -> None:
        q, h = 5, 3
        patterns = [
            reset_pattern_word(q, h, indexed_reset_labels(q, h, index))
            for index in range(1 << (q - 3))
        ]
        labels = first_uncovered_reset_labels(q, h, patterns[:-1])
        self.assertEqual(reset_pattern_word(q, h, labels), patterns[-1])
        with self.assertRaisesRegex(ValueError, "too many distinct factors"):
            first_uncovered_reset_labels(q, h, patterns)

    def test_distinguished_formula_and_exact_image_at_boundaries(self) -> None:
        q = SCIENTIFIC_Q
        for h in (2, q - 1):
            with self.subTest(gate=h):
                labels = reset_spine_labels(q, h)
                suffix = least_suffix_word(q, h)
                m = least_odd_integer(q, h)
                image = least_odd_image_formula(q, h)
                implication = targeted_implication(q, h)
                self.assertEqual(suffix, labels + (1,))
                self.assertEqual(encode_lsd(m), (1,) + suffix)
                self.assertEqual(direct_fully_accelerated_odd(m), image)
                self.assertEqual(
                    odd_core_transducer().transduce((1,) + suffix),
                    encode_lsd(image),
                )
                self.assertEqual(implication.input_suffix, suffix)
                self.assertEqual(
                    (1,) + implication.output_suffix, encode_lsd(image)
                )
                dfa = reset_spine_dfa(q, h)
                self.assertEqual(dfa.run(implication.input_suffix), h)
                self.assertNotEqual(dfa.run(implication.output_suffix), h)


class ScientificResetSpineAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        forbidden = AssertionError("the reset audit must not invoke Z3")
        with patch("odd_suffix_cegis._require_z3", side_effect=forbidden), patch(
            "spine_cegis._require_z3", side_effect=forbidden
        ):
            cls.audit = build_audit()

    def test_frozen_corpus_and_canonical_digest(self) -> None:
        semantic = self.audit["semantic"]
        corpus = semantic["corpus"]
        self.assertEqual(corpus["imported_implications"], 213)
        self.assertEqual(corpus["local_implications"], 11)
        self.assertEqual(corpus["combined_implications"], 224)
        self.assertEqual(corpus["antecedents_shorter_than_q"], 0)
        self.assertEqual(corpus["length_q_factor_occurrences"], 2170)
        self.assertEqual(corpus["distinct_imported_length_q_factors"], 1662)
        self.assertEqual(corpus["distinct_local_length_q_factors"], 30)
        self.assertEqual(corpus["distinct_combined_length_q_factors"], 1692)
        self.assertEqual(corpus["distinct_imported_terminal_q_windows"], 187)
        self.assertEqual(corpus["distinct_local_terminal_q_windows"], 8)
        self.assertEqual(corpus["distinct_combined_terminal_q_windows"], 195)
        self.assertEqual(corpus["minimum_imported_terminal_window_zeros"], 2)
        self.assertEqual(corpus["minimum_local_terminal_window_zeros"], 7)
        self.assertEqual(
            self.audit["semantic_sha256"],
            "7851e9d0888e20e631206e66e2b373f69df3fb31f7bf45aeb92a04847d293e16",
        )
        self.assertEqual(
            self.audit["semantic_sha256"], _sha256_value(self.audit["semantic"])
        )
        self.assertEqual(
            self.audit["semantic_digest_serialization"],
            SEMANTIC_DIGEST_SERIALIZATION,
        )

    def test_all_fixed_spines_are_exactly_rejected_and_bank_blind(self) -> None:
        records = self.audit["semantic"]["gate_records"]
        self.assertEqual([item["gate"] for item in records], list(range(2, 71)))
        for item in records:
            self.assertTrue(all(item["normal_form_checks"].values()))
            self.assertEqual(item["active_imported_antecedents"], 0)
            self.assertEqual(item["active_local_antecedents"], 0)
            self.assertEqual(item["least_odd_image_bit_length"], 73)
            self.assertEqual(
                item["least_odd_image_zero_positions"],
                [item["gate"] - 1, item["gate"], 71],
            )
            for field in ("odd_verification", "shortcut_lift_verification"):
                result = item[field]
                self.assertFalse(result["valid"])
                self.assertEqual(
                    result["reason"], "language is not forward invariant"
                )
                self.assertEqual(
                    result["closure_input_lsd"], result["accepted_witness_lsd"]
                )

    def test_69_exact_clauses_still_leave_every_gate_open(self) -> None:
        semantic = self.audit["semantic"]
        targeted = semantic["targeted_implications"]
        self.assertEqual(len(targeted), 69)
        self.assertEqual([item["gate"] for item in targeted], list(range(2, 71)))
        self.assertEqual(semantic["targeted_overlap_with_frozen_corpus"], 0)
        self.assertEqual(
            semantic["targeted_antecedent_factor_overlap_with_frozen_corpus"],
            1,
        )

        bound = semantic["concrete_factor_bound"]
        self.assertEqual(
            bound["necessary_distinct_length_q_factors_per_fixed_gate"],
            1 << 68,
        )
        self.assertEqual(bound["frozen_distinct_length_q_factors"], 1692)
        self.assertEqual(bound["fixed_targeted_implications_added"], 69)
        self.assertEqual(bound["augmented_distinct_length_q_factors"], 1760)
        self.assertTrue(bound["scope_excludes_symbolic_transition_cube_clauses"])
        records = bound["gate_evasion_records"]
        self.assertEqual([item["gate"] for item in records], list(range(2, 71)))
        for item in records:
            self.assertEqual(item["active_frozen_antecedents"], 0)
            self.assertEqual(item["active_targeted_antecedents"], 0)
            self.assertTrue(all(item["normal_form_checks"].values()))
            self.assertEqual(
                item["classification"], "FINITE_CLAUSE_EVASION_WITNESS_ONLY"
            )
        self.assertEqual(semantic["conclusion"]["reported_sanctuaries"], 0)
        self.assertEqual(
            semantic["conclusion"][
                "gates_eliminated_by_augmented_concrete_clauses"
            ],
            0,
        )

    def test_strict_round_trip_and_semantic_tampering(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            valid = root / "valid.json"
            valid.write_text(
                json.dumps(self.audit, sort_keys=True, allow_nan=False),
                encoding="utf-8",
            )
            with patch("reset_spine.build_audit", return_value=self.audit):
                receipt = validate_audit(valid)
            self.assertEqual(receipt["status"], "valid")

            tampered = json.loads(valid.read_text(encoding="utf-8"))
            tampered["semantic"]["q"] = 70
            bad_digest = root / "bad-digest.json"
            bad_digest.write_text(json.dumps(tampered), encoding="utf-8")
            with patch("reset_spine.build_audit", return_value=self.audit):
                with self.assertRaisesRegex(ValueError, "digest mismatch"):
                    validate_audit(bad_digest)

            tampered["semantic_sha256"] = _sha256_value(tampered["semantic"])
            recomputed_tamper = root / "recomputed-tamper.json"
            recomputed_tamper.write_text(json.dumps(tampered), encoding="utf-8")
            with patch("reset_spine.build_audit", return_value=self.audit):
                with self.assertRaisesRegex(ValueError, "exact recomputation"):
                    validate_audit(recomputed_tamper)

            extra = json.loads(valid.read_text(encoding="utf-8"))
            extra["unexpected"] = True
            extra_path = root / "extra.json"
            extra_path.write_text(json.dumps(extra), encoding="utf-8")
            with patch("reset_spine.build_audit", return_value=self.audit):
                with self.assertRaisesRegex(ValueError, "root is malformed"):
                    validate_audit(extra_path)

            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"semantic": NaN}', encoding="utf-8")
            with patch("reset_spine.build_audit", return_value=self.audit):
                with self.assertRaisesRegex(ValueError, "nonstandard JSON"):
                    validate_audit(nonfinite)

    def test_cli_writes_and_validates_strict_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "audit.json"
            output = io.StringIO()
            with patch("reset_spine.build_audit", return_value=self.audit), redirect_stdout(
                output
            ):
                self.assertEqual(main(["--output", str(path)]), 0)
            self.assertEqual(json.loads(output.getvalue())["status"], "written")
            self.assertEqual(
                json.loads(path.read_text(encoding="utf-8")), self.audit
            )

            output = io.StringIO()
            with patch("reset_spine.build_audit", return_value=self.audit), redirect_stdout(
                output
            ):
                self.assertEqual(main(["--validate", str(path)]), 0)
            receipt = json.loads(output.getvalue())
            self.assertEqual(receipt["status"], "valid")
            self.assertEqual(receipt["semantic_sha256"], self.audit["semantic_sha256"])


if __name__ == "__main__":
    unittest.main()
