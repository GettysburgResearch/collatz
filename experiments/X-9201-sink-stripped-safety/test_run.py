#!/usr/bin/env python3
"""Adversarial tests for X-9201."""

from __future__ import annotations

import unittest
from collections import deque

from run import (
    audit_depth,
    build_safety_dfa,
    direct_avoids,
    encode_lsd,
    forbidden_levels,
    shortcut_preimages,
    strongly_connected_components,
)


class ReverseTreeTests(unittest.TestCase):
    def test_lsd_encoding(self) -> None:
        self.assertEqual(encode_lsd(1), (1,))
        self.assertEqual(encode_lsd(2), (0, 1))
        self.assertEqual(encode_lsd(5), (1, 0, 1))
        with self.assertRaises(ValueError):
            encode_lsd(0)

    def test_exact_preimages(self) -> None:
        self.assertEqual(shortcut_preimages(1), frozenset({2}))
        self.assertEqual(shortcut_preimages(2), frozenset({1, 4}))
        self.assertEqual(shortcut_preimages(5), frozenset({3, 10}))

    def test_first_forbidden_levels(self) -> None:
        levels = forbidden_levels(3)
        self.assertEqual(levels[0], frozenset({1, 2}))
        self.assertEqual(levels[1], frozenset({1, 2, 4}))
        self.assertEqual(levels[2], frozenset({1, 2, 4, 8}))
        self.assertEqual(levels[3], frozenset({1, 2, 4, 5, 8, 16}))

    def test_direct_membership_matches_reverse_tree(self) -> None:
        for depth, forbidden in enumerate(forbidden_levels(8)):
            for value in range(1, 4097):
                self.assertEqual(
                    direct_avoids(value, depth),
                    value not in forbidden,
                    (depth, value),
                )


class AutomatonTests(unittest.TestCase):
    def test_raw_noncanonical_words_are_rejected(self) -> None:
        dfa = build_safety_dfa(frozenset({1, 2})).dfa
        for word in ((), (0,), (1, 0), (0, 0), (1, 1, 0)):
            self.assertFalse(dfa.accepts_word(word), word)
        self.assertTrue(dfa.accepts_word((1, 0, 1)))

    def test_membership_matches_direct_iteration(self) -> None:
        for depth, forbidden in enumerate(forbidden_levels(8)):
            dfa = build_safety_dfa(forbidden).dfa
            for value in range(1, 4097):
                self.assertEqual(
                    dfa.accepts_value(value),
                    direct_avoids(value, depth),
                    (depth, value),
                )

    def test_independently_reproduces_draft_baseline_counts(self) -> None:
        expected = [
            4,
            5,
            6,
            8,
            9,
            12,
            15,
            18,
            21,
            30,
            36,
            42,
            46,
            54,
            63,
            75,
            92,
            116,
            143,
            179,
            217,
        ]
        observed = [
            build_safety_dfa(forbidden).dfa.state_count
            for forbidden in forbidden_levels(20)
        ]
        self.assertEqual(observed, expected)

    def test_only_cycle_is_two_state_tail(self) -> None:
        for forbidden in forbidden_levels(20):
            safety = build_safety_dfa(forbidden)
            components = strongly_connected_components(safety.dfa)
            cyclic = [
                component
                for component in components
                if len(component) > 1
                or any(
                    safety.dfa.transitions[state][bit] == state
                    for state in component
                    for bit in (0, 1)
                )
            ]
            self.assertEqual(len(cyclic), 1)
            self.assertEqual(cyclic[0], safety.tail_states)

    def test_tail_stripped_graph_is_acyclic_by_kahn_algorithm(self) -> None:
        for forbidden in forbidden_levels(20):
            safety = build_safety_dfa(forbidden)
            boundary = set(range(safety.dfa.state_count)) - set(safety.tail_states)
            indegree = {state: 0 for state in boundary}
            for state in boundary:
                for target in set(safety.dfa.transitions[state]):
                    if target in boundary:
                        indegree[target] += 1
            queue = deque(
                state for state in sorted(boundary) if indegree[state] == 0
            )
            removed = 0
            while queue:
                state = queue.popleft()
                removed += 1
                for target in set(safety.dfa.transitions[state]):
                    if target in boundary:
                        indegree[target] -= 1
                        if indegree[target] == 0:
                            queue.append(target)
            self.assertEqual(removed, len(boundary))

    def test_explicit_nonclosure_witness_at_every_depth(self) -> None:
        for depth, forbidden in enumerate(forbidden_levels(20)):
            row = audit_depth(depth, forbidden)
            witness = row["one_step_nonclosure_witness"]
            self.assertEqual(witness["input"], 1 << (depth + 2))
            self.assertEqual(witness["output"], 1 << (depth + 1))

    def test_every_number_above_reverse_tree_maximum_is_accepted(self) -> None:
        for forbidden in forbidden_levels(12):
            dfa = build_safety_dfa(forbidden).dfa
            maximum = max(forbidden)
            for value in range(maximum + 1, maximum + 257):
                self.assertTrue(dfa.accepts_value(value), value)


if __name__ == "__main__":
    unittest.main()
