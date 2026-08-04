"""Adversarial tests for the conditional odd-suffix CEGIS search."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from automata import (
    decode_lsd,
    encode_lsd,
    finite_language_dfa,
    shortest_canonical_word,
)
from odd_core import lift_odd_suffix_dfa_to_shortcut, odd_part
from odd_suffix_cegis import (
    INCOMPLETE_DISCLAIMER,
    NORMALIZED_DIGEST_SERIALIZATION,
    SCHEMA,
    OddSuffixEncoding,
    OddSuffixSearchConfig,
    SuffixImplication,
    diagnostic_config,
    load_checkpoint,
    run_odd_suffix_cegis,
    suffix_implication_digest,
    suffix_to_odd_dfa,
    translate_shortcut_implication_bank,
    verify_suffix_candidate,
)
from spine_cegis import (
    ImplicationBank,
    LearnedImplication,
    SpineSearchConfig,
    export_implication_bank,
    run_spine_cegis,
)
from verify import verify_candidate as exact_verify_candidate


HAS_Z3 = importlib.util.find_spec("z3") is not None


class OddSuffixStructureTests(unittest.TestCase):
    @staticmethod
    def frozen_shortcut_bank() -> Path:
        return (
            Path(__file__).resolve().parent
            / "results"
            / "spine-q72-gate0-bank.json"
        )

    def test_configuration_rejects_out_of_scope_and_nonfinite_values(self) -> None:
        bad_configs = (
            {"state_count": 2},
            {"state_count": True},
            {"gate": 1},
            {"gate": 71},
            {"gate": False},
            {"odd_offset": 0},
            {"solver_seed": -1},
            {"max_models": 0},
            {"max_models": 1.5},
            {"time_limit_seconds": float("nan")},
            {"time_limit_seconds": float("inf")},
            {"time_limit_seconds": True},
        )
        for kwargs in bad_configs:
            with self.subTest(kwargs=kwargs):
                with self.assertRaises(ValueError):
                    OddSuffixSearchConfig(**kwargs)  # type: ignore[arg-type]

    def test_suffix_and_shortcut_lifts_consume_marker_without_a_step(self) -> None:
        # A accepts suffixes 01 and 11, so O_A is exactly {101,111} = {5,7}.
        suffix = finite_language_dfa(("01", "11"))
        odd = suffix_to_odd_dfa(suffix)
        lifted = lift_odd_suffix_dfa_to_shortcut(suffix)

        for value in range(1, 2_000):
            odd_expected = value in (5, 7)
            self.assertEqual(
                odd.accepts_canonical(encode_lsd(value)), odd_expected, value
            )
            lift_expected = odd_part(value) in (5, 7)
            self.assertEqual(
                lifted.accepts_canonical(encode_lsd(value)), lift_expected, value
            )

    def test_minus_one_cycle_passes_both_exact_verifiers(self) -> None:
        suffix = finite_language_dfa(("01", "11"))
        odd_result, lift_result, odd, lifted = verify_suffix_candidate(
            suffix, odd_offset=-1
        )
        self.assertTrue(odd_result.valid, odd_result.to_dict())
        self.assertTrue(lift_result.valid, lift_result.to_dict())
        self.assertEqual(
            OddSuffixSearchConfig(odd_offset=-1).odd_offset,
            -1,
        )
        self.assertEqual(decode_lsd(odd_result.accepted_witness), 5)
        self.assertEqual(decode_lsd(lift_result.accepted_witness), 5)
        self.assertEqual(odd.state_count, suffix.state_count + 2)
        self.assertEqual(lifted.state_count, suffix.state_count + 1)

    def test_all_frozen_shortcut_clauses_normalize_exactly(self) -> None:
        translated = translate_shortcut_implication_bank(
            self.frozen_shortcut_bank()
        )
        self.assertEqual(len(translated.implications), 213)
        self.assertEqual(translated.provenance["source_implications"], 213)
        self.assertEqual(translated.provenance["tautologies_skipped"], 0)
        self.assertEqual(translated.provenance["duplicates_skipped"], 0)
        self.assertEqual(translated.provenance["inputs_with_low_zeros"], 0)
        self.assertEqual(translated.provenance["outputs_with_low_zeros"], 44)
        self.assertEqual(
            translated.provenance["outputs_with_multiple_low_zeros"], 2
        )
        self.assertEqual(
            translated.provenance["normalized_implications_sha256"],
            "ea4dc231df8840bfe8369702b45b2bc1ba4f6bdc9a158da170b8c8a0bf8ce1cc",
        )
        self.assertEqual(
            translated.provenance["normalized_digest_serialization"],
            NORMALIZED_DIGEST_SERIALIZATION,
        )
        self.assertEqual(
            suffix_implication_digest(translated.implications),
            translated.provenance["normalized_implications_sha256"],
        )

        # At least one frozen output has more than one low zero.  Removing just
        # one bit would be wrong; the imported suffix uses the complete odd part.
        raw = json.loads(self.frozen_shortcut_bank().read_text(encoding="utf-8"))
        item = next(
            entry for entry in raw["implications"] if entry["output_lsd"].startswith("00")
        )
        expected = (
            item["input_lsd"].lstrip("0")[1:],
            item["output_lsd"].lstrip("0")[1:],
        )
        imported_pairs = {
            (
                "".join(map(str, implication.input_suffix)),
                "".join(map(str, implication.output_suffix)),
            )
            for implication in translated.implications
        }
        self.assertIn(expected, imported_pairs)
        self.assertNotEqual(expected[1], item["output_lsd"][1:])

    def test_shortcut_bank_integrity_tampering_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            bad = Path(directory) / "tampered-bank.json"
            data = json.loads(
                self.frozen_shortcut_bank().read_text(encoding="utf-8")
            )
            data["implications"][0]["output_lsd"] = "1"
            bad.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "payload digest mismatch"):
                translate_shortcut_implication_bank(bad)

    def test_even_shortcut_step_becomes_saturation_identity(self) -> None:
        # 6 -> 3 preserves odd part 3.  A saturated language gives both values
        # the same membership, so this exact even step contributes no U clause.
        fake = ImplicationBank(
            (LearnedImplication(encode_lsd(6), encode_lsd(3)),),
            "0" * 64,
            {
                "bank_file_sha256": "1" * 64,
                "source_checkpoint_sha256": "2" * 64,
                "source_status": "time_limit",
                "declared_implications": 1,
            },
        )
        with patch(
            "odd_suffix_cegis.load_shortcut_implication_bank",
            return_value=fake,
        ):
            translated = translate_shortcut_implication_bank(
                Path("unused-bank.json")
            )
        self.assertEqual(translated.implications, ())
        self.assertEqual(translated.provenance["inputs_with_low_zeros"], 1)
        self.assertEqual(translated.provenance["tautologies_skipped"], 1)


@unittest.skipUnless(HAS_Z3, "optional z3-solver is not installed")
class OddSuffixCegisTests(unittest.TestCase):
    def make_small_shortcut_bank(self, root: Path) -> Path:
        checkpoint = root / "source-checkpoint.json"
        bank = root / "source-bank.json"
        run_spine_cegis(
            SpineSearchConfig(
                state_count=5,
                solver_seed=31,
                max_models=1,
                time_limit_seconds=10.0,
            ),
            checkpoint_path=checkpoint,
        )
        export_implication_bank(checkpoint, bank)
        return bank

    def test_prefix_trie_batch_asserts_the_same_clauses(self) -> None:
        config = OddSuffixSearchConfig(state_count=6, gate=3, solver_seed=3)
        implications = (
            SuffixImplication((1, 0, 1), (0, 1)),
            SuffixImplication((1, 1, 0, 1), (0, 0, 1)),
        )
        sequential = OddSuffixEncoding(config)
        baseline = len(sequential.solver.assertions())
        for implication in implications:
            sequential.add_implication(implication)
        batched = OddSuffixEncoding(config)
        batched.add_implications_batch(implications)

        self.assertEqual(
            [str(item) for item in sequential.solver.assertions()[baseline:]],
            [str(item) for item in batched.solver.assertions()[baseline:]],
        )

    def test_symbolic_model_obeys_complete_suffix_normal_form(self) -> None:
        config = OddSuffixSearchConfig(state_count=6, gate=3, solver_seed=3)
        encoding = OddSuffixEncoding(config)
        self.assertEqual(encoding.solver.check(), encoding.z3.sat)
        candidate = encoding.extract_candidate(encoding.solver.model())

        self.assertEqual(candidate.accepting, frozenset({3}))
        self.assertEqual(candidate.transitions[0][1], 1)
        self.assertNotEqual(candidate.transitions[0][0], 1)
        self.assertEqual(candidate.transitions[-1][1], 3)
        for state in range(candidate.state_count - 1):
            self.assertLessEqual(candidate.transitions[state][0], state + 1)
            self.assertLessEqual(candidate.transitions[state][1], state + 1)
            self.assertIn(state + 1, candidate.transitions[state])
            self.assertNotEqual(candidate.transitions[state][1], 3)

        suffix_witness = shortest_canonical_word(candidate)
        self.assertIsNotNone(suffix_witness)
        self.assertEqual(len(suffix_witness), config.state_count)
        full_witness = shortest_canonical_word(suffix_to_odd_dfa(candidate))
        self.assertIsNotNone(full_witness)
        self.assertEqual(len(full_witness), config.state_count + 1)

    def test_diagnostic_checks_every_model_and_learns_exact_suffix_images(self) -> None:
        config = diagnostic_config(seed=0)
        with patch(
            "odd_suffix_cegis.verify_candidate", wraps=exact_verify_candidate
        ) as checker:
            result = run_odd_suffix_cegis(config)

        self.assertEqual(result["status"], "solver_unsat")
        self.assertGreater(result["models_checked"], 0)
        # No positive model occurs in the diagnostic, so each proposal invokes
        # exactly the odd-core oracle once and never reaches the lift oracle.
        self.assertEqual(checker.call_count, result["models_checked"])
        self.assertFalse(result["bounded_or_incomplete"])
        learned = {
            (item["input_suffix_lsd"], item["output_suffix_lsd"])
            for item in result["learned_implications"]
        }
        self.assertEqual(len(learned), len(result["learned_implications"]))
        self.assertEqual(
            sum(batch["new_implications"] for batch in result["batch_history"]),
            len(learned),
        )

    def test_model_limit_checkpoint_is_bounded_and_resumable(self) -> None:
        config = OddSuffixSearchConfig(
            state_count=6,
            gate=2,
            solver_seed=11,
            max_models=1,
            time_limit_seconds=10.0,
        )
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "checkpoint.json"
            first = run_odd_suffix_cegis(config, checkpoint_path=checkpoint)
            frozen = json.loads(checkpoint.read_text(encoding="utf-8"))

            self.assertEqual(first["status"], "model_limit")
            self.assertEqual(frozen["schema"], SCHEMA)
            self.assertTrue(frozen["bounded_or_incomplete"])
            self.assertEqual(frozen["disclaimer"], INCOMPLETE_DISCLAIMER)
            self.assertIn("runs atomically", frozen["disclaimer"])
            self.assertGreater(len(load_checkpoint(checkpoint, config)), 0)

            second = run_odd_suffix_cegis(
                config,
                checkpoint_path=checkpoint,
                resume_path=checkpoint,
            )
            self.assertTrue(second["resumed"])
            self.assertEqual(second["models_checked_this_run"], 1)
            self.assertEqual(second["models_checked_cumulative"], 2)
            self.assertEqual(
                second["learned_implications_before_run"],
                first["learned_implications_cumulative"],
            )
            self.assertGreater(second["learned_implications_this_run"], 0)

    def test_checkpoint_rejects_partition_metadata_and_image_tampering(self) -> None:
        config = OddSuffixSearchConfig(
            state_count=6,
            gate=2,
            solver_seed=17,
            max_models=1,
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            checkpoint = root / "checkpoint.json"
            run_odd_suffix_cegis(config, checkpoint_path=checkpoint)
            original = json.loads(checkpoint.read_text(encoding="utf-8"))

            other_gate = OddSuffixSearchConfig(
                state_count=6,
                gate=3,
                solver_seed=17,
                max_models=1,
            )
            with self.assertRaisesRegex(ValueError, "logical configuration"):
                load_checkpoint(checkpoint, other_gate)

            displayed = json.loads(json.dumps(original))
            displayed["config"]["gate"] = 3
            bad_display = root / "bad-display.json"
            bad_display.write_text(json.dumps(displayed), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "displayed config"):
                load_checkpoint(bad_display, config)

            nonfinite = json.loads(json.dumps(original))
            nonfinite["elapsed_seconds_cumulative"] = float("nan")
            bad_elapsed = root / "bad-elapsed.json"
            bad_elapsed.write_text(json.dumps(nonfinite), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "elapsed time"):
                load_checkpoint(bad_elapsed, config)

            wrong_image = json.loads(json.dumps(original))
            wrong_image["learned_implications"][0]["output_suffix_lsd"] = ""
            bad_image = root / "bad-image.json"
            bad_image.write_text(json.dumps(wrong_image), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "exact U image"):
                load_checkpoint(bad_image, config)

            malformed = json.loads(json.dumps(original))
            malformed["learned_implications"][0]["input_suffix_lsd"] = "10"
            bad_suffix = root / "bad-suffix.json"
            bad_suffix.write_text(json.dumps(malformed), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "terminal 1"):
                load_checkpoint(bad_suffix, config)

    def test_imported_and_local_ledgers_resume_without_source_bank(self) -> None:
        config = OddSuffixSearchConfig(
            state_count=5,
            gate=2,
            solver_seed=37,
            max_models=1,
            time_limit_seconds=10.0,
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bank = self.make_small_shortcut_bank(root)
            checkpoint = root / "odd-checkpoint.json"
            first = run_odd_suffix_cegis(
                config,
                checkpoint_path=checkpoint,
                shortcut_bank_path=bank,
            )
            imported = first["imported_implications_cumulative"]
            self.assertGreater(imported, 0)
            self.assertEqual(first["imported_implications_before_run"], 0)
            self.assertEqual(first["imported_implications_this_run"], imported)
            self.assertEqual(
                first["enforced_implications_cumulative"],
                imported + first["learned_implications_cumulative"],
            )
            self.assertEqual(len(first["shortcut_bank_imports"]), 1)
            self.assertEqual(
                first["shortcut_bank_imports"][0]["source_path"], bank.name
            )

            bank.unlink()
            second = run_odd_suffix_cegis(
                config,
                checkpoint_path=checkpoint,
                resume_path=checkpoint,
            )
            self.assertTrue(second["resumed"])
            self.assertEqual(second["resume_source"], checkpoint.name)
            self.assertEqual(second["imported_implications_before_run"], imported)
            self.assertEqual(second["imported_implications_this_run"], 0)
            self.assertEqual(second["imported_implications_cumulative"], imported)
            self.assertGreaterEqual(
                second["learned_implications_cumulative"],
                first["learned_implications_cumulative"],
            )
            self.assertEqual(
                len(load_checkpoint(checkpoint, config)),
                second["enforced_implications_cumulative"],
            )

    def test_import_metadata_and_map_mismatch_are_rejected(self) -> None:
        config = OddSuffixSearchConfig(
            state_count=5,
            gate=2,
            solver_seed=41,
            max_models=1,
            time_limit_seconds=10.0,
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bank = self.make_small_shortcut_bank(root)
            checkpoint = root / "odd-checkpoint.json"
            run_odd_suffix_cegis(
                config,
                checkpoint_path=checkpoint,
                shortcut_bank_path=bank,
            )
            original = json.loads(checkpoint.read_text(encoding="utf-8"))

            bad_digest_data = json.loads(json.dumps(original))
            bad_digest_data["shortcut_bank_imports"][0][
                "normalized_implications_sha256"
            ] = "0" * 64
            bad_digest = root / "bad-normalized-digest.json"
            bad_digest.write_text(json.dumps(bad_digest_data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "normalized digest mismatch"):
                load_checkpoint(bad_digest, config)

            bad_count_data = json.loads(json.dumps(original))
            bad_count_data["shortcut_bank_imports"][0][
                "inputs_with_low_zeros"
            ] = 10**6
            bad_count = root / "bad-valuation-count.json"
            bad_count.write_text(json.dumps(bad_count_data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "valuation count"):
                load_checkpoint(bad_count, config)

            minus_config = OddSuffixSearchConfig(
                state_count=5,
                gate=2,
                odd_offset=-1,
                max_models=1,
            )
            with self.assertRaisesRegex(ValueError, r"only for odd_offset=\+1"):
                run_odd_suffix_cegis(
                    minus_config,
                    shortcut_bank_path=bank,
                )

            with self.assertRaisesRegex(ValueError, "do not supply"):
                run_odd_suffix_cegis(
                    config,
                    resume_path=checkpoint,
                    shortcut_bank_path=bank,
                )


if __name__ == "__main__":
    unittest.main()
