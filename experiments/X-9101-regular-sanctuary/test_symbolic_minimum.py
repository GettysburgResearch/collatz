"""Tests for symbolic closure of the chosen minimum suffix-spine word."""

from __future__ import annotations

import copy
import importlib.util
import unittest

from automata import DFA
from odd_suffix_cegis import OddSuffixEncoding, OddSuffixSearchConfig
from symbolic_minimum import (
    _payload_digest,
    add_symbolic_minimum_closure,
    chosen_advancing_suffix,
    concrete_minimum_profile,
    gate_two_carry_certificate,
    run_audit,
    validate_audit,
    validate_suffix_normal_form,
)


HAS_Z3 = importlib.util.find_spec("z3") is not None


def reset_spine(state_count: int, gate: int) -> DFA:
    transitions: list[tuple[int, int]] = []
    for state in range(state_count - 1):
        advancing_bit = 0 if state == gate - 1 else 1
        transitions.append(
            (state + 1, 0) if advancing_bit == 0 else (0, state + 1)
        )
    transitions.append((0, gate))
    return DFA(tuple(transitions), frozenset({gate}), 0)


class SymbolicMinimumStructureTests(unittest.TestCase):
    def test_reset_spine_has_the_expected_chosen_word(self) -> None:
        dfa = reset_spine(7, 4)
        validate_suffix_normal_form(dfa, 4)
        suffix = chosen_advancing_suffix(dfa, 4)
        self.assertEqual(suffix, (1, 1, 1, 0, 1, 1, 1))
        profile = concrete_minimum_profile(dfa, 4)
        self.assertFalse(profile["accepted_by_symbolic_constraint"])
        self.assertEqual(profile["input_full_length"], 8)
        self.assertIn(profile["output_full_length"], (8, 9))

    def test_normal_form_validator_rejects_an_early_one_gate(self) -> None:
        dfa = reset_spine(6, 3)
        transitions = list(dfa.transitions)
        transitions[2] = (transitions[2][0], 3)
        malformed = DFA(tuple(transitions), dfa.accepting, dfa.start)
        with self.assertRaisesRegex(ValueError, "early one-transition"):
            validate_suffix_normal_form(malformed, 3)

    def test_gate_two_certificate_handles_small_boundary(self) -> None:
        q3 = gate_two_carry_certificate(3)
        q4 = gate_two_carry_certificate(4)
        self.assertEqual(q3["forced_spine_suffix_lsd"], "101")
        self.assertEqual(q3["forced_output_full_length"], 5)
        self.assertEqual(q4["forced_spine_suffix_lsd"], "1001")
        self.assertEqual(q4["forced_output_full_length"], 5)
        with self.assertRaises(ValueError):
            gate_two_carry_certificate(2)


@unittest.skipUnless(HAS_Z3, "optional z3-solver is not installed")
class SymbolicMinimumSolverTests(unittest.TestCase):
    def test_gate_two_is_unsat_for_small_state_counts(self) -> None:
        for state_count in range(3, 9):
            with self.subTest(state_count=state_count):
                encoding = OddSuffixEncoding(
                    OddSuffixSearchConfig(
                        state_count=state_count,
                        gate=2,
                        solver_seed=0,
                    )
                )
                add_symbolic_minimum_closure(encoding)
                self.assertEqual(encoding.solver.check(), encoding.z3.unsat)

    def test_sat_model_replays_the_symbolic_constraint_concretely(self) -> None:
        encoding = OddSuffixEncoding(
            OddSuffixSearchConfig(state_count=5, gate=3, solver_seed=0)
        )
        handles = add_symbolic_minimum_closure(encoding)
        self.assertEqual(len(handles.spine_bits), 4)
        self.assertEqual(encoding.solver.check(), encoding.z3.sat)
        candidate = encoding.extract_candidate(encoding.solver.model())
        profile = concrete_minimum_profile(candidate, 3)
        self.assertTrue(profile["accepted_by_symbolic_constraint"])
        self.assertIn(
            profile["path_class"],
            ("equal_length_all_advance", "one_bit_longer_one_stall"),
        )

    def test_small_audit_is_strict_and_tamper_evident(self) -> None:
        payload = run_audit(
            state_count=4,
            gate_min=2,
            gate_max=3,
            solver_seed=0,
            timeout_seconds=10.0,
        )
        aggregate = validate_audit(payload)
        self.assertEqual(
            aggregate["status_counts"],
            {"satisfiable_countermodel": 1, "solver_unsat": 1},
        )
        self.assertEqual(aggregate["exact_full_candidates"], 0)

        changed = copy.deepcopy(payload)
        changed["records"][0]["gate_two_carry_certificate"][
            "forced_output_full_length"
        ] += 1
        with self.assertRaisesRegex(ValueError, "payload digest mismatch"):
            validate_audit(changed)

        unsigned = dict(changed)
        del unsigned["payload_sha256"]
        changed["payload_sha256"] = _payload_digest(unsigned)
        with self.assertRaisesRegex(ValueError, "carry certificate mismatch"):
            validate_audit(changed)

        extra_field = copy.deepcopy(payload)
        extra_sat = next(
            record
            for record in extra_field["records"]
            if record["constraint_status"] == "satisfiable_countermodel"
        )
        extra_sat["candidate"]["unexpected"] = True
        unsigned = dict(extra_field)
        del unsigned["payload_sha256"]
        extra_field["payload_sha256"] = _payload_digest(unsigned)
        with self.assertRaisesRegex(ValueError, "candidate fields"):
            validate_audit(extra_field)

        noncanonical = copy.deepcopy(payload)
        noncanonical_sat = next(
            record
            for record in noncanonical["records"]
            if record["constraint_status"] == "satisfiable_countermodel"
        )
        noncanonical_sat["candidate"]["accepting"].append(
            noncanonical_sat["candidate"]["accepting"][0]
        )
        unsigned = dict(noncanonical)
        del unsigned["payload_sha256"]
        noncanonical["payload_sha256"] = _payload_digest(unsigned)
        with self.assertRaisesRegex(ValueError, "canonical DFA form"):
            validate_audit(noncanonical)

        wrong_scope = run_audit(
            state_count=4,
            gate_min=3,
            gate_max=3,
            solver_seed=0,
            timeout_seconds=10.0,
        )
        wrong_scope["scope"]["state_count"] += 1
        unsigned = dict(wrong_scope)
        del unsigned["payload_sha256"]
        wrong_scope["payload_sha256"] = _payload_digest(unsigned)
        with self.assertRaisesRegex(ValueError, "state count differs"):
            validate_audit(wrong_scope)


if __name__ == "__main__":
    unittest.main()
