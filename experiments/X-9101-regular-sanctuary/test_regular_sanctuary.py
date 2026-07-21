from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest

from automata import (
    DFA,
    canonical_positive_dfa,
    decode_lsd,
    empty_dfa,
    encode_lsd,
    finite_language_dfa,
    is_canonical_positive,
    shortest_canonical_word,
    threshold_core_dfa,
    transition_skeletons,
    universal_dfa,
    word_text,
)
from search import known_3n_minus_1_cycle
from transducer import (
    CARRY_2,
    SubsequentialTransducer,
    direct_shortcut,
    shortcut_transducer,
)
from verify import (
    closure_counterexample,
    direct_avoids,
    maximal_safe_kernel,
    preimage_dfa,
    safety_approximant,
    terminal_relation,
    verify_candidate,
)


class EncodingTests(unittest.TestCase):
    def test_round_trip(self) -> None:
        for value in range(1, 10_000):
            word = encode_lsd(value)
            self.assertTrue(is_canonical_positive(word))
            self.assertEqual(decode_lsd(word), value)

    def test_exact_orientation(self) -> None:
        self.assertEqual(encode_lsd(1), (1,))
        self.assertEqual(encode_lsd(2), (0, 1))
        self.assertEqual(encode_lsd(5), (1, 0, 1))
        self.assertEqual(decode_lsd("0001"), 8)

    def test_reject_noncanonical(self) -> None:
        for word in ("", "0", "10", "100"):
            with self.assertRaises(ValueError):
                decode_lsd(word)
        with self.assertRaises(ValueError):
            encode_lsd(0)


class DFATests(unittest.TestCase):
    def test_constructor_rejects_incomplete_table(self) -> None:
        with self.assertRaises(ValueError):
            DFA(((0,),), frozenset())  # type: ignore[arg-type]

    def test_certificate_requires_orientation(self) -> None:
        data = universal_dfa().to_dict()
        data["bit_order"] = "msd_first"
        with self.assertRaises(ValueError):
            DFA.from_dict(data)

    def test_certificate_round_trip(self) -> None:
        original = finite_language_dfa(("101", "111", "0101"))
        encoded = json.loads(json.dumps(original.to_dict()))
        self.assertEqual(DFA.from_dict(encoded), original)

    def test_certificate_rejects_coercible_nonintegers(self) -> None:
        base = universal_dfa().to_dict()
        mutations = []
        for field, value in (
            ("start", "0"),
            ("start", False),
            ("accepting", [0.0]),
            ("alphabet", [False, True]),
            ("transitions", [[0, "0"]]),
        ):
            mutated = dict(base)
            mutated[field] = value
            mutations.append(mutated)
        for mutated in mutations:
            with self.subTest(mutated=mutated):
                with self.assertRaises(ValueError):
                    DFA.from_dict(mutated)

    def test_finite_language_and_minimization(self) -> None:
        dfa = finite_language_dfa(("101", "111", "0101"))
        for word in ("101", "111", "0101"):
            self.assertTrue(dfa.accepts_canonical(word))
        for word in ("1", "01", "11", "1011"):
            self.assertFalse(dfa.accepts_canonical(word))

    def test_shortest_witness_is_canonical(self) -> None:
        witness = shortest_canonical_word(canonical_positive_dfa())
        self.assertEqual(witness, (1,))


class TransducerTests(unittest.TestCase):
    def test_standard_against_integer_arithmetic(self) -> None:
        machine = shortcut_transducer(+1)
        for value in range(1, 20_000):
            observed = decode_lsd(machine.transduce(encode_lsd(value)))
            self.assertEqual(observed, direct_shortcut(value, +1))

    def test_minus_one_against_integer_arithmetic(self) -> None:
        machine = shortcut_transducer(-1)
        for value in range(1, 20_000):
            observed = decode_lsd(machine.transduce(encode_lsd(value)))
            self.assertEqual(observed, direct_shortcut(value, -1))

    def test_boundary_outputs(self) -> None:
        machine = shortcut_transducer(+1)
        expected = {
            "1": "01",
            "01": "1",
            "11": "101",
            "101": "0001",
            "111": "1101",
            "0001": "001",
        }
        for source, target in expected.items():
            self.assertEqual(word_text(machine.transduce(source)), target)

    def test_wrong_terminal_carry_is_detected(self) -> None:
        good = shortcut_transducer(+1)
        terminals = dict(good.terminal_outputs)
        terminals[CARRY_2] = (1, 0)
        bad = SubsequentialTransducer(
            "corrupt", good.state_count, good.start, good.transitions, terminals
        )
        with self.assertRaises(AssertionError):
            terminal_relation(universal_dfa(), bad)

    def test_missing_terminal_output_is_detected(self) -> None:
        good = shortcut_transducer(+1)
        bad = SubsequentialTransducer(
            "partial", good.state_count, good.start, good.transitions, {}
        )
        with self.assertRaises(AssertionError):
            terminal_relation(universal_dfa(), bad)


class VerificationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.standard = shortcut_transducer(+1)
        self.control = shortcut_transducer(-1)

    def test_all_positive_is_closed_but_unsafe(self) -> None:
        all_raw = universal_dfa()
        self.assertIsNone(closure_counterexample(all_raw, self.standard))
        result = verify_candidate(all_raw, self.standard)
        self.assertFalse(result.valid)
        self.assertIn("trivial-cycle", result.reason)

    def test_trivial_cycle_is_closed_but_unsafe(self) -> None:
        cycle = finite_language_dfa(("1", "01"))
        self.assertIsNone(closure_counterexample(cycle, self.standard))
        self.assertFalse(verify_candidate(cycle, self.standard).valid)

    def test_empty_language_fails(self) -> None:
        result = verify_candidate(empty_dfa(), self.standard)
        self.assertFalse(result.valid)
        self.assertIn("empty", result.reason)

    def test_noncanonical_raw_alias_is_semantically_empty(self) -> None:
        alias_only = finite_language_dfa(("10",))
        result = verify_candidate(alias_only, self.standard)
        self.assertFalse(result.valid)
        self.assertIn("empty", result.reason)

    def test_closure_counterexample_is_exact(self) -> None:
        singleton = finite_language_dfa(("11",))
        source, target = closure_counterexample(singleton, self.standard)  # type: ignore[misc]
        self.assertEqual(source, (1, 1))
        self.assertEqual(target, (1, 0, 1))

    def test_closure_counterexample_is_globally_shortest(self) -> None:
        # Reviewer regression: endpoint-state ordering returned 111 before 11.
        dfa = DFA(((0, 1), (0, 2), (0, 0)), frozenset({0, 2}))
        source, target = closure_counterexample(dfa, self.standard)  # type: ignore[misc]
        self.assertEqual(source, (1, 1))
        self.assertEqual(target, (1, 0, 1))

    def test_3n_minus_1_positive_control(self) -> None:
        cycle = known_3n_minus_1_cycle()
        result = verify_candidate(cycle, self.control)
        self.assertTrue(result.valid, result)
        values = {decode_lsd(word) for word in ("101", "111", "0101")}
        self.assertEqual(values, {5, 7, 10})

    def test_no_sampling_cutoff(self) -> None:
        huge = (1 << 200) + 1
        singleton = finite_language_dfa((encode_lsd(huge),))
        counterexample = closure_counterexample(singleton, self.standard)
        self.assertIsNotNone(counterexample)
        source, target = counterexample  # type: ignore[misc]
        self.assertEqual(decode_lsd(source), huge)
        self.assertEqual(decode_lsd(target), direct_shortcut(huge, +1))

    def test_maximal_kernel_matches_all_acceptance_masks(self) -> None:
        for skeleton in transition_skeletons(2):
            relation = terminal_relation(skeleton, self.standard)
            kernel = maximal_safe_kernel(skeleton, self.standard)
            forbidden_states = {skeleton.run("1"), skeleton.run("01")}
            for mask in range(1 << skeleton.state_count):
                accepting = {
                    state
                    for state in range(skeleton.state_count)
                    if mask & (1 << state)
                }
                safe = not (accepting & forbidden_states) and all(
                    source not in accepting or target in accepting
                    for source, target in relation.edges
                )
                if safe:
                    self.assertTrue(accepting <= kernel.safe_states)
            self.assertFalse(kernel.safe_states & forbidden_states)
            self.assertTrue(
                all(
                    source not in kernel.safe_states or target in kernel.safe_states
                    for source, target in relation.edges
                )
            )

    def test_small_standard_kernels_are_empty(self) -> None:
        for state_count in (1, 2):
            for skeleton in transition_skeletons(state_count):
                self.assertFalse(
                    maximal_safe_kernel(skeleton, self.standard).nonempty
                )

    def test_threshold_forbids_early_acceptance(self) -> None:
        expanded, early = threshold_core_dfa(universal_dfa(), 5)
        saturated = expanded.with_accepting(
            set(range(expanded.state_count)) - set(early)
        )
        witness = shortest_canonical_word(saturated)
        self.assertIsNotNone(witness)
        self.assertEqual(len(witness), 5)  # type: ignore[arg-type]

    def test_short_witness_bound_on_all_small_skeletons_and_masks(self) -> None:
        for state_count in (1, 2, 3):
            for skeleton in transition_skeletons(state_count):
                for mask in range(1 << state_count):
                    candidate = skeleton.with_accepting(
                        state
                        for state in range(state_count)
                        if mask & (1 << state)
                    )
                    witness = shortest_canonical_word(candidate)
                    if witness is not None:
                        self.assertLessEqual(len(witness), state_count)


class CertificateCLITests(unittest.TestCase):
    def test_nonstandard_map_requires_explicit_opt_in(self) -> None:
        directory = Path(__file__).resolve().parent
        command = [
            sys.executable,
            "-B",
            str(directory / "check_certificate.py"),
            str(directory / "results" / "control-3n-minus-1.json"),
        ]
        rejected = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertNotEqual(rejected.returncode, 0)
        accepted = subprocess.run(
            command + ["--allow-nonstandard-control"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(accepted.returncode, 0, accepted.stderr)
        payload = json.loads(accepted.stdout)
        self.assertEqual(payload["map"], "shortcut_3n_minus_1")
        self.assertEqual(
            payload["certificate_schema"], "regular-sanctuary-certificate-v1"
        )
        self.assertTrue(payload["verification"]["valid"])


class ApproximationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.machine = shortcut_transducer(+1)

    def test_preimage_against_direct_arithmetic(self) -> None:
        target = finite_language_dfa((encode_lsd(5), encode_lsd(8)))
        preimage = preimage_dfa(self.machine, target)
        for value in range(1, 1_000):
            observed = preimage.accepts_raw(encode_lsd(value))
            expected = direct_shortcut(value, +1) in (5, 8)
            self.assertEqual(observed, expected, value)

    def test_safety_approximants_against_iteration(self) -> None:
        for depth in range(7):
            dfa = safety_approximant(self.machine, depth)
            for value in range(1, 2_000):
                observed = dfa.accepts_canonical(encode_lsd(value))
                expected = direct_avoids(
                    value,
                    depth,
                    lambda number: direct_shortcut(number, +1),
                )
                self.assertEqual(observed, expected, (depth, value))


if __name__ == "__main__":
    unittest.main(verbosity=2)
