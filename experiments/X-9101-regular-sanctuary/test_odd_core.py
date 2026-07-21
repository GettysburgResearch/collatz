"""Focused tests for the odd-core regular-sanctuary tooling."""

from __future__ import annotations

import unittest

from automata import (
    DFA,
    decode_lsd,
    encode_lsd,
    finite_language_dfa,
    product_dfa,
    transition_skeletons,
    universal_dfa,
)
from odd_core import (
    direct_fully_accelerated_odd,
    direct_odd_core_map,
    lift_odd_dfa_to_shortcut,
    lift_odd_suffix_dfa_to_shortcut,
    odd_core_transducer,
    odd_part,
    transduce_odd_word,
)
from transducer import direct_shortcut, shortcut_transducer
from verify import closure_counterexample, verify_candidate


class OddCoreArithmeticTests(unittest.TestCase):
    def setUp(self) -> None:
        self.machine = odd_core_transducer()

    def test_exhaustive_odd_arithmetic(self) -> None:
        for value in range(1, 100_000, 2):
            observed = decode_lsd(self.machine.transduce(encode_lsd(value)))
            self.assertEqual(observed, direct_fully_accelerated_odd(value), value)

    def test_totalized_transducer_uses_the_odd_part(self) -> None:
        for value in range(1, 20_000):
            observed = decode_lsd(self.machine.transduce(encode_lsd(value)))
            self.assertEqual(observed, direct_odd_core_map(value), value)

    def test_minus_one_positive_control_arithmetic(self) -> None:
        machine = odd_core_transducer(-1)
        for value in range(1, 20_000, 2):
            observed = decode_lsd(machine.transduce(encode_lsd(value)))
            expected = direct_fully_accelerated_odd(value, -1)
            self.assertEqual(observed, expected, value)

        self.assertEqual(decode_lsd(transduce_odd_word("101", odd_offset=-1)), 7)
        self.assertEqual(decode_lsd(transduce_odd_word("111", odd_offset=-1)), 5)

    def test_named_edge_cases(self) -> None:
        expected = {
            1: 1,
            3: 5,
            5: 1,
            7: 11,
            27: 41,
        }
        for value, image in expected.items():
            self.assertEqual(direct_fully_accelerated_odd(value), image)
            self.assertEqual(
                decode_lsd(transduce_odd_word(encode_lsd(value))), image
            )

    def test_long_suppressed_zero_run(self) -> None:
        # 3*m + 1 = 2**200, so all 199 low zeros of the shortcut image
        # disappear under full acceleration.
        value = ((1 << 200) - 1) // 3
        self.assertEqual(value % 2, 1)
        self.assertEqual(self.machine.transduce(encode_lsd(value)), (1,))

        # The totalized machine also skips arbitrarily many input low zeros.
        even_value = (1 << 150) * 5
        self.assertEqual(self.machine.transduce(encode_lsd(even_value)), (1,))

    def test_domain_and_canonicality_errors(self) -> None:
        for value in (0, -1, 2, 10):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    direct_fully_accelerated_odd(value)

        for value in (0, -1):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    odd_part(value)

        for word in ((), "", "0", "10"):
            with self.subTest(word=word):
                with self.assertRaises(ValueError):
                    self.machine.transduce(word)

        for word in ("01", "001", "011"):
            with self.subTest(word=word):
                with self.assertRaises(ValueError):
                    transduce_odd_word(word)

        for offset in (-3, 0, 3):
            with self.subTest(offset=offset):
                with self.assertRaises(ValueError):
                    odd_core_transducer(offset)
                with self.assertRaises(ValueError):
                    direct_fully_accelerated_odd(3, offset)


class OddCoreLiftTests(unittest.TestCase):
    def test_exact_closure_equivalence_on_every_two_state_dfa(self) -> None:
        # This is an exact finite-product comparison, not arithmetic sampling.
        # The domain DFA restricts the odd-side checker to canonical words that
        # begin with an LSD one.  The standard side receives only the 0* lift.
        odd_canonical = DFA(
            ((3, 1), (2, 1), (2, 1), (3, 3)),
            frozenset({1}),
        )
        odd_machine = odd_core_transducer()
        standard_machine = shortcut_transducer()

        for skeleton in transition_skeletons(2):
            for mask in range(1 << skeleton.state_count):
                accepting = frozenset(
                    state
                    for state in range(skeleton.state_count)
                    if mask & (1 << state)
                )
                odd_dfa = skeleton.with_accepting(accepting)
                restricted = product_dfa(odd_dfa, odd_canonical).minimized()
                lifted = lift_odd_dfa_to_shortcut(odd_dfa)

                odd_closed = (
                    closure_counterexample(restricted, odd_machine) is None
                )
                lifted_closed = (
                    closure_counterexample(lifted, standard_machine) is None
                )
                self.assertEqual(
                    odd_closed,
                    lifted_closed,
                    (skeleton.transitions, sorted(accepting)),
                )

    def test_lift_accepts_exactly_by_odd_part(self) -> None:
        odd_dfa = finite_language_dfa(("1", "11", "101", "1011"))
        lifted = lift_odd_dfa_to_shortcut(odd_dfa)

        for value in range(1, 10_000):
            expected = odd_dfa.accepts_canonical(encode_lsd(odd_part(value)))
            observed = lifted.accepts_canonical(encode_lsd(value))
            self.assertEqual(observed, expected, value)

    def test_universal_odd_language_lifts_to_all_positives(self) -> None:
        lifted = lift_odd_dfa_to_shortcut(universal_dfa())
        for value in range(1, 10_000):
            self.assertTrue(lifted.accepts_canonical(encode_lsd(value)), value)

        # The lifted language is exactly closed under the standard shortcut
        # map, but the existing verifier correctly rejects its unsafe words.
        standard = shortcut_transducer()
        self.assertIsNone(closure_counterexample(lifted, standard))
        result = verify_candidate(lifted, standard)
        self.assertFalse(result.valid)
        self.assertEqual(
            result.reason,
            "semantic language contains a forbidden trivial-cycle word",
        )

    def test_u_invariant_finite_language_lifts_to_t_invariant_language(self) -> None:
        # U(1)=1 and U(5)=1.  Thus O={1,5} is U-invariant, and its
        # power-of-two cone is exactly T-invariant (although deliberately
        # unsafe, so it is not a Collatz sanctuary).
        odd_dfa = finite_language_dfa(("1", "101"))
        lifted = lift_odd_dfa_to_shortcut(odd_dfa)
        self.assertIsNone(closure_counterexample(lifted, shortcut_transducer()))

    def test_minus_one_cycle_is_an_end_to_end_positive_control(self) -> None:
        # Under fully accelerated 3n-1, 5 -> 7 -> 5.  Lifting the odd cycle
        # gives {2**k*5, 2**k*7}, which the unchanged shortcut verifier proves
        # safe and exactly forward invariant for the nonstandard control map.
        odd_dfa = finite_language_dfa(("101", "111"))
        for value in (5, 7):
            image = direct_fully_accelerated_odd(value, -1)
            self.assertTrue(odd_dfa.accepts_canonical(encode_lsd(image)))

        lifted = lift_odd_dfa_to_shortcut(odd_dfa)
        result = verify_candidate(lifted, shortcut_transducer(-1))
        self.assertTrue(result.valid, result.to_dict())
        self.assertEqual(decode_lsd(result.accepted_witness), 5)

    def test_noninvariant_odd_language_yields_standard_closure_witness(self) -> None:
        # U(3)=5, so O={3} is not invariant.  Its lift contains every
        # 3*2**k, and the existing standard checker exposes 3 -> 5.
        odd_dfa = finite_language_dfa(("11",))
        lifted = lift_odd_dfa_to_shortcut(odd_dfa)
        result = verify_candidate(lifted, shortcut_transducer())
        self.assertFalse(result.valid)
        self.assertEqual(result.reason, "language is not forward invariant")
        self.assertEqual(decode_lsd(result.closure_input), 3)
        self.assertEqual(decode_lsd(result.closure_output), 5)

    def test_lifted_membership_is_preserved_by_even_shortcut_steps(self) -> None:
        odd_dfa = finite_language_dfa(("11", "101", "111"))
        lifted = lift_odd_dfa_to_shortcut(odd_dfa)
        for value in range(2, 20_000, 2):
            word = encode_lsd(value)
            if lifted.accepts_canonical(word):
                image = direct_shortcut(value)
                self.assertTrue(
                    lifted.accepts_canonical(encode_lsd(image)),
                    (value, image),
                )


class OddSuffixLiftTests(unittest.TestCase):
    def test_suffix_lift_accepts_exactly_by_stripped_odd_word(self) -> None:
        suffix_dfa = finite_language_dfa(("1", "01", "101"))
        lifted = lift_odd_suffix_dfa_to_shortcut(suffix_dfa)
        self.assertEqual(lifted.state_count, suffix_dfa.state_count + 1)

        for value in range(1, 10_000):
            odd_word = encode_lsd(odd_part(value))
            expected = suffix_dfa.accepts_raw(odd_word[1:])
            observed = lifted.accepts_canonical(encode_lsd(value))
            self.assertEqual(observed, expected, value)

    def test_accepting_empty_suffix_exposes_trivial_cycle(self) -> None:
        suffix_dfa = universal_dfa()
        lifted = lift_odd_suffix_dfa_to_shortcut(suffix_dfa)
        result = verify_candidate(lifted, shortcut_transducer())
        self.assertFalse(result.valid)
        self.assertEqual(
            result.reason,
            "semantic language contains a forbidden trivial-cycle word",
        )
        self.assertTrue(lifted.accepts_canonical(encode_lsd(1)))
        self.assertTrue(lifted.accepts_canonical(encode_lsd(2)))

    def test_minus_one_suffix_cycle_is_a_positive_control(self) -> None:
        # Full odd words 101 and 111 become suffixes 01 and 11.
        suffix_dfa = finite_language_dfa(("01", "11"))
        lifted = lift_odd_suffix_dfa_to_shortcut(suffix_dfa)
        result = verify_candidate(lifted, shortcut_transducer(-1))
        self.assertTrue(result.valid, result.to_dict())
        self.assertEqual(decode_lsd(result.accepted_witness), 5)


if __name__ == "__main__":
    unittest.main()
