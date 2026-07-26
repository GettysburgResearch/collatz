#!/usr/bin/env python3
"""Unit, regression, and small-tail differential tests for X-8256."""
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("x8256_run", HERE / "run.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load run.py")
RUN = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = RUN
SPEC.loader.exec_module(RUN)


class ConstantsAndRegressionTests(unittest.TestCase):
    def test_constants_are_derived_from_source_identities(self) -> None:
        constants = RUN.audit_constants()
        self.assertEqual(constants["D9"], 68_332_056_247)
        self.assertEqual(constants["omega"], 37_933_813_917)
        self.assertEqual(constants["a"], 215_072_362)
        self.assertEqual(constants["b"], 38_148_886_279)
        self.assertEqual(RUN.B - RUN.A, RUN.OMEGA)
        self.assertEqual((1 << 36) * RUN.A - RUN.NINE9 * RUN.B, 1)

    def test_regression_against_x8251_frozen_rows(self) -> None:
        source_path = (
            HERE.parent
            / "X-8251-nine-b-synchronizer"
            / "results"
            / "canonical.json"
        )
        source = json.loads(source_path.read_text(encoding="utf-8"))
        self.assertEqual(
            source["constants"],
            {
                "D9": RUN.D9,
                "D9_factorization": [7, 13, 19, 37, 163, 6553],
                "a": RUN.A,
                "b": RUN.B,
                "b_minus_a": RUN.OMEGA,
                "omega": RUN.OMEGA,
            },
        )
        for sample in source["samples"]:
            row = RUN.branch(int(sample["run"]))
            canonical_output = (
                row.multiplier * row.residue + row.toll
            ) // row.radix
            self.assertEqual(row.height, sample["radix_bits"])
            self.assertEqual(str(row.residue), sample["xi"])
            self.assertEqual(str(row.toll), sample["toll"])
            self.assertEqual(row.multiplier.bit_length(), sample["multiplier_bits"])
            self.assertEqual(str(canonical_output), sample["canonical_output"])

    def test_high_prefix_regression_from_l8253(self) -> None:
        prefix = 598_051_932_619_127_473_212_326_704_339_812_739_814
        modulus = 1 << 132
        for label in range(44, 81):
            self.assertEqual(RUN.branch(label).residue % modulus, prefix)
        self.assertEqual(
            RUN.v2(RUN.branch(44).residue - RUN.branch(45).residue),
            132,
        )


class ExactBoundTests(unittest.TestCase):
    def test_root_bound_is_exact_integer_bound(self) -> None:
        cap = 1 << 512
        self.assertEqual(RUN.exact_label_upper(0, 1, cap - 1), 180)

    def test_bound_dominates_bruteforce_valuations(self) -> None:
        cases = [
            (0, 1, 4095),
            (123_456, 17, 8191),
            (-RUN.A, RUN.NINE9, 2047),
        ]
        for C, P, qmax in cases:
            upper = RUN.exact_label_upper(C, P, qmax)
            for q in range(qmax + 1):
                y = RUN.NINE9 * (C + P * q) + RUN.A
                if y:
                    self.assertLessEqual(RUN.v2(y) // 3, upper)


class TransportDifferentialTests(unittest.TestCase):
    def test_bruteforce_twelve_bit_quotient_windows(self) -> None:
        """Compare transport to every q in three actual 12-bit tail windows."""
        first = RUN.branch(44)
        first_output = (
            first.multiplier * first.residue + first.toll
        ) // first.radix
        window_size = 1 << 12

        for target in (44, 45, 64):
            target_row = RUN.branch(target)
            absolute_rho = (
                (target_row.residue - first_output)
                * pow(first.multiplier, -1, target_row.radix)
            ) % target_row.radix
            window_start = max(0, absolute_rho - window_size // 2)
            theta = first.residue + first.radix * window_start
            current = first_output + first.multiplier * window_start
            initial = RUN.InitialState(
                theta=theta,
                K=first.radix,
                C=current,
                P=first.multiplier,
                q_max=window_size - 1,
            )
            cap = theta + first.radix * window_size
            nodes, _ = RUN.transported_closure(
                cap_exclusive=cap,
                minimum_label=44,
                initial=initial,
                max_transitions=1,
            )

            transported = [
                (nodes[i].label, nodes[i].rho, nodes[i].C)
                for i in nodes[0].children
            ]
            brute: list[tuple[int, int, int]] = []
            for q in range(window_size):
                x = current + first.multiplier * q
                label = RUN.intrinsic_label(x, minimum=44)
                if label is not None:
                    xp = RUN.centered_step(x, label)
                    self.assertIsNotNone(xp)
                    brute.append((label, q, int(xp)))
            brute.sort()
            self.assertEqual(transported, brute)
            self.assertIn(target, [entry[0] for entry in brute])

    def test_default_closure_regression(self) -> None:
        canonical, trie = RUN.build_default_outputs()
        self.assertEqual(canonical["counts"]["nodes_including_root"], 1936)
        self.assertEqual(canonical["counts"]["retained_edges"], 1935)
        self.assertEqual(canonical["counts"]["candidate_labels_tested"], 269000)
        self.assertEqual(canonical["counts"]["dead_end_branch_nodes"], 1866)
        self.assertEqual(canonical["counts"]["exit_terminals"], 1936)
        self.assertEqual(canonical["counts"]["survivor_terminals"], 0)
        self.assertEqual(
            canonical["tree"]["depth_histogram"],
            {"0": 1, "1": 116, "2": 1801, "3": 18},
        )
        self.assertEqual(
            canonical["result"]["maximum_consecutive_defined_labels_at_least_44"],
            3,
        )
        self.assertEqual(canonical["result"]["length_four_prefixes"], 0)
        self.assertTrue(trie["prefix_free_terminal_words"])
        self.assertEqual(trie["survivor_terminals"], [])


if __name__ == "__main__":
    unittest.main()
