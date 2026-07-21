"""Differential tests for the regular-preimage verification route."""

from __future__ import annotations

import itertools
import unittest

from automata import DFA, finite_language_dfa, transition_skeletons
from independent_check import verify_candidate_via_preimage
from search import known_3n_minus_1_cycle
from transducer import SubsequentialTransducer, shortcut_transducer
from verify import verify_candidate


class IndependentPreimageCheckerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.standard = shortcut_transducer(+1)

    def assert_agrees(self, candidate: DFA, transducer=None) -> None:
        machine = self.standard if transducer is None else transducer
        primary = verify_candidate(candidate, machine)
        second = verify_candidate_via_preimage(candidate, machine)
        self.assertEqual(primary.valid, second.valid)
        self.assertEqual(primary.reason, second.reason)
        self.assertEqual(primary.accepted_witness, second.accepted_witness)
        if second.reason == "language is not forward invariant":
            self.assertIsNotNone(second.closure_input)
            self.assertIsNotNone(second.closure_output)
            self.assertEqual(primary.closure_input, second.closure_input)
            self.assertEqual(primary.closure_output, second.closure_output)
            self.assertTrue(candidate.accepts_canonical(second.closure_input))
            self.assertFalse(candidate.accepts_canonical(second.closure_output))

    def test_exhaustive_labeled_dfas_through_two_states(self) -> None:
        for state_count in (1, 2):
            for skeleton in transition_skeletons(state_count):
                for mask in range(1 << state_count):
                    accepting = {
                        state
                        for state in range(state_count)
                        if mask & (1 << state)
                    }
                    with self.subTest(
                        states=state_count,
                        transitions=skeleton.transitions,
                        mask=mask,
                    ):
                        self.assert_agrees(skeleton.with_accepting(accepting))

    def test_exhaustive_labeled_three_state_dfas(self) -> None:
        # All 729 labeled transition skeletons and all eight acceptance masks.
        for skeleton in transition_skeletons(3):
            for mask in range(8):
                accepting = {
                    state for state in range(3) if mask & (1 << state)
                }
                self.assert_agrees(skeleton.with_accepting(accepting))

    def test_primary_positive_control(self) -> None:
        control = known_3n_minus_1_cycle()
        self.assert_agrees(control, shortcut_transducer(-1))
        result = verify_candidate_via_preimage(control, shortcut_transducer(-1))
        self.assertTrue(result.valid)

    def test_long_singleton_violation_is_exact(self) -> None:
        value = (1 << 200) + 12345
        word = tuple(int(bit) for bit in reversed(bin(value)[2:]))
        candidate = finite_language_dfa((word,))
        self.assert_agrees(candidate)
        result = verify_candidate_via_preimage(candidate, self.standard)
        self.assertEqual(result.closure_input, word)

    def test_rejects_noncanonical_forbidden_metadata(self) -> None:
        candidate = DFA(((0, 0),), frozenset({0}))
        with self.assertRaises(ValueError):
            verify_candidate_via_preimage(
                candidate, self.standard, forbidden_words=("10",)
            )

    def test_rejects_partial_transducer_outside_candidate_language(self) -> None:
        candidate = finite_language_dfa(("001",))  # {4}
        transitions = {
            (0, 0): (1, (0,)),
            (0, 1): (2, (1,)),
            (1, 0): (1, (0,)),
            (1, 1): (1, (1,)),
            (2, 0): (2, (0,)),
            (2, 1): (2, (1,)),
        }
        partial = SubsequentialTransducer(
            "partial_odd_branch",
            3,
            0,
            transitions,
            {1: ()},
        )
        with self.assertRaisesRegex(AssertionError, "no terminal output"):
            verify_candidate_via_preimage(candidate, partial)

    def test_rejects_noncanonical_output_outside_candidate_language(self) -> None:
        candidate = finite_language_dfa(("001",))  # {4}
        transitions = {
            (0, 0): (1, (0,)),
            (0, 1): (2, (1,)),
            (1, 0): (1, (0,)),
            (1, 1): (1, (1,)),
            (2, 0): (2, (0,)),
            (2, 1): (2, (1,)),
        }
        malformed = SubsequentialTransducer(
            "noncanonical_odd_branch",
            3,
            0,
            transitions,
            {1: (), 2: (0,)},
        )
        with self.assertRaisesRegex(AssertionError, "noncanonical output"):
            verify_candidate_via_preimage(candidate, malformed)


if __name__ == "__main__":
    unittest.main()
