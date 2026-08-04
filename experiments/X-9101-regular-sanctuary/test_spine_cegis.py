"""Tests for the optional exact-floor spine CEGIS prototype."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from automata import shortest_canonical_word
from spine_cegis import (
    BANK_SCHEMA,
    INCOMPLETE_DISCLAIMER,
    LearnedImplication,
    SCHEMA,
    SpineEncoding,
    SpineSearchConfig,
    _bank_payload_digest,
    _canonical_json_bytes,
    _is_timeout_reason,
    _sha256_bytes,
    diagnostic_config,
    export_implication_bank,
    load_implication_bank,
    load_checkpoint,
    run_spine_cegis,
)
from transducer import shortcut_transducer
from verify import verify_candidate as exact_verify_candidate


HAS_Z3 = importlib.util.find_spec("z3") is not None


class SpineConfigurationTests(unittest.TestCase):
    def test_rejects_incoherent_options(self) -> None:
        with self.assertRaises(ValueError):
            SpineSearchConfig(state_count=1)
        with self.assertRaises(ValueError):
            SpineSearchConfig(state_count=5, gate=5)
        with self.assertRaises(ValueError):
            SpineSearchConfig(
                state_count=5,
                force_zero_loop=False,
                force_11_prefix=True,
            )
        with self.assertRaises(ValueError):
            SpineSearchConfig(state_count=2, force_11_prefix=True)
        with self.assertRaises(ValueError):
            SpineSearchConfig(state_count=5, max_models=0)
        for bad_limit in (float("nan"), float("inf"), True, "10"):
            with self.subTest(bad_limit=bad_limit):
                with self.assertRaises(ValueError):
                    SpineSearchConfig(
                        state_count=5,
                        time_limit_seconds=bad_limit,  # type: ignore[arg-type]
                    )
        self.assertTrue(_is_timeout_reason("timeout"))
        self.assertTrue(_is_timeout_reason("canceled"))
        self.assertTrue(_is_timeout_reason("resource CANCELED by timeout"))
        self.assertFalse(_is_timeout_reason("incomplete theory"))

    def test_limits_do_not_change_resume_signature(self) -> None:
        left = SpineSearchConfig(
            state_count=5,
            solver_seed=7,
            max_models=1,
            time_limit_seconds=1.0,
        )
        right = SpineSearchConfig(
            state_count=5,
            solver_seed=7,
            max_models=100,
            time_limit_seconds=100.0,
        )
        self.assertEqual(left.logical_signature(), right.logical_signature())

    def test_frozen_v2_scout_still_exports_as_a_portable_bank(self) -> None:
        source = (
            Path(__file__).with_name("results") / "spine-q72-gate0-scout.json"
        )
        frozen = json.loads(source.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as directory:
            bank_path = Path(directory) / "q72-bank.json"
            export_implication_bank(source, bank_path)
            bank = load_implication_bank(bank_path)

        self.assertEqual(
            len(bank.implications), frozen["learned_implications_cumulative"]
        )
        self.assertEqual(
            bank.provenance["source_logical_signature"],
            frozen["logical_signature"],
        )


@unittest.skipUnless(HAS_Z3, "optional z3-solver is not installed")
class SpineCegisTests(unittest.TestCase):
    def test_prefix_trie_batch_asserts_the_same_clauses(self) -> None:
        config = SpineSearchConfig(state_count=5, gate=3, solver_seed=3)
        implications = (
            LearnedImplication((1, 1, 0, 1), (1, 0, 1)),
            LearnedImplication((1, 1, 1, 1), (1, 0, 0, 1)),
        )
        sequential = SpineEncoding(config)
        baseline = len(sequential.solver.assertions())
        for implication in implications:
            sequential.add_implication(implication)
        batched = SpineEncoding(config)
        batched.add_implications_batch(implications)

        self.assertEqual(
            [str(item) for item in sequential.solver.assertions()[baseline:]],
            [str(item) for item in batched.solver.assertions()[baseline:]],
        )

    def test_symbolic_model_obeys_complete_spine_normal_form(self) -> None:
        config = SpineSearchConfig(state_count=5, solver_seed=3)
        encoding = SpineEncoding(config)
        self.assertEqual(encoding.solver.check(), encoding.z3.sat)
        candidate = encoding.extract_candidate(encoding.solver.model())

        self.assertEqual(candidate.transitions[0], (0, 1))
        self.assertEqual(candidate.transitions[1][1], 2)
        self.assertNotEqual(candidate.transitions[1][0], 2)
        gate = next(iter(candidate.accepting))
        self.assertEqual(candidate.transitions[-1][1], gate)
        for state in range(candidate.state_count - 1):
            self.assertLessEqual(candidate.transitions[state][0], state + 1)
            self.assertLessEqual(candidate.transitions[state][1], state + 1)
            self.assertIn(state + 1, candidate.transitions[state])
            self.assertNotEqual(candidate.transitions[state][1], gate)

        witness = shortest_canonical_word(candidate)
        self.assertIsNotNone(witness)
        self.assertEqual(len(witness), config.state_count)

    def test_diagnostic_checks_every_model_and_never_relearns_violation(self) -> None:
        config = diagnostic_config(seed=0)
        with patch(
            "spine_cegis.verify_candidate", wraps=exact_verify_candidate
        ) as checker:
            result = run_spine_cegis(config)

        self.assertEqual(result["status"], "solver_unsat")
        self.assertGreater(result["models_checked"], 0)
        self.assertEqual(checker.call_count, result["models_checked"])
        self.assertFalse(result["bounded_or_incomplete"])
        self.assertFalse(result["independently_checkable_unsat_proof_emitted"])
        learned_pairs = {
            (item["input_lsd"], item["output_lsd"])
            for item in result["learned_implications"]
        }
        self.assertEqual(len(learned_pairs), len(result["learned_implications"]))
        self.assertEqual(
            sum(batch["new_implications"] for batch in result["batch_history"]),
            len(result["learned_implications"]),
        )

    def test_model_limit_batches_multiple_endpoint_violations(self) -> None:
        config = SpineSearchConfig(
            state_count=6,
            solver_seed=11,
            max_models=1,
            time_limit_seconds=10.0,
        )
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "checkpoint.json"
            result = run_spine_cegis(config, checkpoint_path=checkpoint)
            frozen = json.loads(checkpoint.read_text(encoding="utf-8"))

            self.assertEqual(result["status"], "model_limit")
            self.assertEqual(frozen["schema"], SCHEMA)
            self.assertTrue(frozen["bounded_or_incomplete"])
            self.assertEqual(frozen["disclaimer"], INCOMPLETE_DISCLAIMER)
            self.assertFalse(
                frozen["independently_checkable_unsat_proof_emitted"]
            )
            learned = load_checkpoint(checkpoint, config)
            self.assertEqual(len(frozen["batch_history"]), 1)
            batch = frozen["batch_history"][0]
            self.assertGreater(batch["violating_endpoint_pairs"], 1)
            self.assertEqual(
                batch["new_implications"], batch["violating_endpoint_pairs"]
            )
            self.assertEqual(len(learned), batch["new_implications"])
            self.assertEqual(
                learned[0].output_word,
                shortcut_transducer().transduce(learned[0].input_word),
            )

    def test_resume_records_cumulative_and_this_run_counts(self) -> None:
        config = SpineSearchConfig(
            state_count=6,
            solver_seed=13,
            max_models=1,
            time_limit_seconds=10.0,
        )
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "checkpoint.json"
            first = run_spine_cegis(config, checkpoint_path=checkpoint)
            second = run_spine_cegis(
                config,
                checkpoint_path=checkpoint,
                resume_path=checkpoint,
            )

            self.assertEqual(first["models_checked_cumulative"], 1)
            self.assertEqual(second["models_checked_this_run"], 1)
            self.assertEqual(second["models_checked_cumulative"], 2)
            self.assertTrue(second["resumed"])
            self.assertEqual(second["resume_source"], checkpoint.name)
            self.assertEqual(
                second["learned_implications_before_run"],
                first["learned_implications_cumulative"],
            )
            self.assertGreater(second["learned_implications_this_run"], 0)
            self.assertEqual(
                second["batches_before_run"], first["batches_cumulative"]
            )

    def test_portable_bank_crosses_gate_without_importing_accounting(self) -> None:
        source_config = SpineSearchConfig(
            state_count=6,
            gate=0,
            solver_seed=17,
            max_models=1,
            time_limit_seconds=10.0,
        )
        target_config = SpineSearchConfig(
            state_count=6,
            gate=3,
            solver_seed=19,
            max_models=1,
            time_limit_seconds=10.0,
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_checkpoint = root / "gate-0.json"
            bank_path = root / "portable-bank.json"
            target_checkpoint = root / "gate-3.json"
            source_result = run_spine_cegis(
                source_config, checkpoint_path=source_checkpoint
            )
            exported = export_implication_bank(source_checkpoint, bank_path)
            bank = load_implication_bank(bank_path)

            self.assertEqual(exported["schema"], BANK_SCHEMA)
            self.assertGreater(source_result["models_checked_cumulative"], 0)
            self.assertGreater(len(bank.implications), 0)
            self.assertEqual(
                bank.provenance["source_logical_signature"]["gate"], 0
            )

            target = run_spine_cegis(
                target_config,
                checkpoint_path=target_checkpoint,
                implication_bank_paths=(bank_path,),
            )
            self.assertEqual(target["config"]["gate"], 3)
            self.assertEqual(target["models_checked_before_run"], 0)
            self.assertEqual(
                target["models_checked_cumulative"],
                target["models_checked_this_run"],
            )
            self.assertEqual(target["batches_before_run"], 0)
            self.assertEqual(
                target["imported_implications_cumulative"], len(bank.implications)
            )
            self.assertEqual(
                target["imported_implications_this_run"], len(bank.implications)
            )
            self.assertEqual(
                target["enforced_implications_cumulative"],
                target["learned_implications_cumulative"]
                + target["imported_implications_cumulative"],
            )
            self.assertEqual(
                len(load_checkpoint(target_checkpoint, target_config)),
                target["enforced_implications_cumulative"],
            )
            provenance = target["implication_bank_imports"][0]
            self.assertEqual(provenance["source_logical_signature"]["gate"], 0)
            self.assertEqual(provenance["new_implications"], len(bank.implications))

            unfixed = run_spine_cegis(
                SpineSearchConfig(
                    state_count=6,
                    gate=None,
                    solver_seed=31,
                    max_models=1,
                    time_limit_seconds=10.0,
                ),
                implication_bank_paths=(bank_path,),
            )
            self.assertIsNone(unfixed["config"]["gate"])
            self.assertEqual(
                unfixed["imported_implications_cumulative"],
                len(bank.implications),
            )

            # Imported clauses are embedded separately, so resume needs neither
            # the source checkpoint nor the portable bank file.
            source_checkpoint.unlink()
            bank_path.unlink()
            resumed = run_spine_cegis(
                target_config,
                resume_path=target_checkpoint,
            )
            self.assertEqual(
                resumed["imported_implications_before_run"], len(bank.implications)
            )
            self.assertEqual(resumed["imported_implications_this_run"], 0)

    def test_implication_bank_rejects_integrity_exactness_and_provenance_tampering(
        self,
    ) -> None:
        config = SpineSearchConfig(
            state_count=6,
            gate=0,
            solver_seed=23,
            max_models=1,
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            checkpoint = root / "checkpoint.json"
            bank_path = root / "bank.json"
            run_spine_cegis(config, checkpoint_path=checkpoint)
            export_implication_bank(checkpoint, bank_path)
            original = json.loads(bank_path.read_text(encoding="utf-8"))

            broken_integrity = json.loads(json.dumps(original))
            broken_integrity["source"]["status"] = "solver_unsat"
            bad_integrity = root / "bad-integrity.json"
            bad_integrity.write_text(json.dumps(broken_integrity), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "payload digest mismatch"):
                load_implication_bank(bad_integrity)

            # Recompute both public digests so validation reaches the semantic
            # w -> T(w) check rather than stopping at the integrity envelope.
            wrong_image = json.loads(json.dumps(original))
            wrong_image["implications"][0]["output_lsd"] = "1"
            wrong_image["implications_sha256"] = _sha256_bytes(
                _canonical_json_bytes(wrong_image["implications"])
            )
            unsigned = dict(wrong_image)
            del unsigned["bank_sha256"]
            wrong_image["bank_sha256"] = _bank_payload_digest(unsigned)
            bad_image = root / "bad-image.json"
            bad_image.write_text(json.dumps(wrong_image), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "exact T image"):
                load_implication_bank(bad_image)

            bad_provenance = json.loads(json.dumps(original))
            bad_provenance["source"]["logical_signature"]["gate"] = 99
            unsigned = dict(bad_provenance)
            del unsigned["bank_sha256"]
            bad_provenance["bank_sha256"] = _bank_payload_digest(unsigned)
            bad_source = root / "bad-provenance.json"
            bad_source.write_text(json.dumps(bad_provenance), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "provenance gate"):
                load_implication_bank(bad_source)

    def test_v2_checkpoint_without_bank_fields_remains_loadable(self) -> None:
        config = SpineSearchConfig(
            state_count=5,
            solver_seed=29,
            max_models=1,
        )
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "checkpoint.json"
            run_spine_cegis(config, checkpoint_path=checkpoint)
            legacy = json.loads(checkpoint.read_text(encoding="utf-8"))
            for field in (
                "imported_implications_before_run",
                "imported_implications_this_run",
                "imported_implications_cumulative",
                "imported_implications",
                "enforced_implications_cumulative",
                "implication_bank_imports",
            ):
                legacy.pop(field)
            checkpoint.write_text(json.dumps(legacy), encoding="utf-8")
            self.assertGreater(len(load_checkpoint(checkpoint, config)), 0)

    def test_checkpoint_rejects_mismatched_partition(self) -> None:
        config = SpineSearchConfig(
            state_count=5,
            solver_seed=1,
            max_models=1,
        )
        other = SpineSearchConfig(
            state_count=5,
            gate=0,
            solver_seed=1,
            max_models=1,
        )
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "checkpoint.json"
            run_spine_cegis(config, checkpoint_path=checkpoint)
            with self.assertRaises(ValueError):
                load_checkpoint(checkpoint, other)

            original = json.loads(checkpoint.read_text(encoding="utf-8"))
            tampered_config = json.loads(json.dumps(original))
            tampered_config["config"]["gate"] = 0
            bad_config = Path(directory) / "bad-displayed-config.json"
            bad_config.write_text(json.dumps(tampered_config), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "displayed config"):
                load_checkpoint(bad_config, config)

            nonfinite = json.loads(json.dumps(original))
            nonfinite["elapsed_seconds_cumulative"] = float("nan")
            bad_elapsed = Path(directory) / "bad-elapsed.json"
            bad_elapsed.write_text(json.dumps(nonfinite), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "elapsed time"):
                load_checkpoint(bad_elapsed, config)

            fixed_checkpoint = Path(directory) / "fixed-gate.json"
            run_spine_cegis(other, checkpoint_path=fixed_checkpoint)
            fixed = json.loads(fixed_checkpoint.read_text(encoding="utf-8"))
            fixed["batch_history"][0]["gate"] = 3
            fixed_checkpoint.write_text(json.dumps(fixed), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "fixed partition"):
                load_checkpoint(fixed_checkpoint, other)

    def test_checkpoint_rejects_nonstring_nonbinary_and_noncanonical_words(
        self,
    ) -> None:
        config = SpineSearchConfig(
            state_count=5,
            solver_seed=2,
            max_models=1,
        )
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "checkpoint.json"
            run_spine_cegis(config, checkpoint_path=checkpoint)
            original = json.loads(checkpoint.read_text(encoding="utf-8"))
            cases = (
                ("input_lsd", 101),
                ("input_lsd", "12"),
                ("input_lsd", "10"),
                ("output_lsd", None),
                ("output_lsd", "02"),
                ("output_lsd", "10"),
            )
            for index, (field, value) in enumerate(cases):
                with self.subTest(field=field, value=value):
                    tampered = json.loads(json.dumps(original))
                    tampered["learned_implications"][0][field] = value
                    bad = Path(directory) / f"bad-{index}.json"
                    bad.write_text(json.dumps(tampered), encoding="utf-8")
                    with self.assertRaises(ValueError):
                        load_checkpoint(bad, config)


if __name__ == "__main__":
    unittest.main()
