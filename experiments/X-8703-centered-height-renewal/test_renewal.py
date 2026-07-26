#!/usr/bin/env python3
"""Tests for the exact X-8703 centered height-renewal atlas."""
from __future__ import annotations

import ast
import copy
import importlib.util
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_module(name: str, filename: str):
    specification = importlib.util.spec_from_file_location(name, HERE / filename)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


build = load_module("x8703_build", "build.py")
verify = load_module("x8703_verify", "verify.py")


def forced_step(B: int, e: int) -> tuple[int, int] | None:
    answers = []
    for next_e in (0, 1):
        numerator = 81 * B + e - next_e
        if numerator % 64 == 0:
            answers.append((numerator // 64, next_e))
    if len(answers) > 1:
        raise AssertionError("the forced transition is not deterministic")
    return answers[0] if answers else None


def first_crossing_within(
    B: int, e: int, height: int, horizon: int
) -> tuple[int, str] | None:
    for t in range(1, horizon + 1):
        result = forced_step(B, e)
        if result is None:
            return None
        B, e = result
        if B >= height:
            return t, e
    return None


class ExactFormulaTests(unittest.TestCase):
    def test_iterated_formula_and_direct_recurrence(self) -> None:
        height = 64**5
        for t in range(1, 6):
            for number in range(1 << (t + 1)):
                record = build.derive_word_record(height, t, number)
                bits = tuple(int(bit) for bit in record["word"])
                direct_D = [0]
                for j in range(1, t + 1):
                    direct_D.append(
                        sum(
                            81 ** (j - 1 - i)
                            * 64**i
                            * (bits[i] - bits[i + 1])
                            for i in range(j)
                        )
                    )
                self.assertEqual(record["D"], direct_D)
                self.assertEqual(
                    (81**t * record["r"] + direct_D[t]) % (64**t), 0
                )

                B = record["r"]
                replay = [B]
                for j in range(t):
                    numerator = 81 * B + bits[j] - bits[j + 1]
                    self.assertEqual(numerator % 64, 0)
                    B = numerator // 64
                    replay.append(B)
                self.assertEqual(replay, record["c"])

                q = 3
                affine = build.replay_values(record, q)
                B = record["r"] + 64**t * q
                self.assertEqual(B, affine[0])
                for j in range(t):
                    result = forced_step(B, bits[j])
                    self.assertIsNotNone(result)
                    B, next_e = result  # type: ignore[misc]
                    self.assertEqual(next_e, bits[j + 1])
                    self.assertEqual(B, affine[j + 1])

    def test_exact_ceil_and_strict_upper_boundary(self) -> None:
        cases = [
            (-129, 64, -2),
            (-128, 64, -2),
            (-65, 64, -1),
            (-64, 64, -1),
            (-63, 64, 0),
            (-1, 64, 0),
            (0, 64, 0),
            (1, 64, 1),
            (63, 64, 1),
            (64, 64, 1),
            (65, 64, 2),
        ]
        for numerator, denominator, expected in cases:
            with self.subTest(numerator=numerator):
                self.assertEqual(build.ceil_div(numerator, denominator), expected)
                self.assertEqual(verify.ceiling(numerator, denominator), expected)
                for q in range(expected - 2, expected + 3):
                    self.assertEqual(
                        q * denominator < numerator,
                        q < expected,
                        "q < U must be equivalent to q < ceil(U)",
                    )

    def test_interval_endpoints_and_first_crossing(self) -> None:
        height = 64**3
        retained = 0
        for t in range(1, 7):
            for number in range(1 << (t + 1)):
                record = build.derive_word_record(height, t, number)
                interval = record["integer_Q"]
                if interval["count"] == 0:
                    continue
                retained += 1
                start = interval["start_inclusive"]
                stop = interval["stop_exclusive"]
                for q in (start, stop - 1):
                    values = build.replay_values(record, q)
                    self.assertEqual(
                        build.failed_inequalities(height, values, t), []
                    )
                    self.assertEqual(build.first_crossing(height, values), t)
                    bits = tuple(int(bit) for bit in record["word"])
                    for j in range(t):
                        self.assertEqual(
                            64 * values[j + 1],
                            81 * values[j] + bits[j] - bits[j + 1],
                        )
                below = build.replay_values(record, start - 1)
                above = build.replay_values(record, stop)
                self.assertTrue(build.failed_inequalities(height, below, t))
                self.assertTrue(build.failed_inequalities(height, above, t))
        self.assertGreater(retained, 0)


class BoundAndPartitionTests(unittest.TestCase):
    def test_uniform_eighteen_step_bound_constants(self) -> None:
        data = build.elementary_bound_data()
        self.assertEqual(data["steps"], 18)
        self.assertEqual(data["control_error_lower"], -(81**17))
        self.assertEqual(data["branchwise_positive_step_minimum"], 4)
        self.assertEqual(data["large_height_threshold"], 11)
        self.assertGreater(81**18 - 64**19, 0)
        self.assertGreater(
            11 * (81**18 - 64**19) - 64 * 81**17,
            0,
        )

        for j in range(1, 19):
            expanded_minimum = -sum(
                17 * 81 ** (j - 1 - i) * 64 ** (i - 1)
                for i in range(1, j)
            ) - 64 ** (j - 1)
            self.assertEqual(expanded_minimum, -(81 ** (j - 1)))

        # Exact differences in the three positive legal branches.
        differences = []
        for quotient in range(6):
            if quotient:
                differences.append(17 * quotient)
            differences.extend((17 * quotient + 4, 17 * quotient + 13))
        self.assertEqual(min(differences), 4)
        self.assertEqual(verify.bound_constants(), data)

    def test_bounded_atlas_is_a_deterministic_partition(self) -> None:
        """Exhaustively compare the atlas and direct dynamics on a small band."""
        height = 64**2
        horizon = 4
        atlas: dict[tuple[int, int], tuple[int, str]] = {}
        for t in range(1, horizon + 1):
            for number in range(1 << (t + 1)):
                record = build.derive_word_record(height, t, number)
                start = record["integer_Q"]["start_inclusive"]
                stop = record["integer_Q"]["stop_exclusive"]
                e0 = int(record["word"][0])
                for q in range(start, stop):
                    B0 = record["r"] + 64**t * q
                    key = (B0, e0)
                    self.assertNotIn(key, atlas)
                    atlas[key] = (t, record["word"][-1])

        direct: dict[tuple[int, int], tuple[int, str]] = {}
        band_start = build.ceil_div(height, 64)
        for B0 in range(band_start, height):
            for e0 in (0, 1):
                answer = first_crossing_within(B0, e0, height, horizon)
                if answer is not None:
                    t, terminal_e = answer
                    direct[(B0, e0)] = (t, str(terminal_e))
        self.assertEqual(atlas, direct)
        self.assertEqual(len(atlas), 53)


class ReproducibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.small = build.build_certificate(64**2, 4)

    def test_verifier_is_independent_and_accepts_certificate(self) -> None:
        syntax = ast.parse((HERE / "verify.py").read_text(encoding="utf-8"))
        imported = {
            alias.name
            for node in ast.walk(syntax)
            if isinstance(node, (ast.Import, ast.ImportFrom))
            for alias in node.names
        }
        self.assertNotIn("build", imported)
        summary = verify.verify_certificate_data(copy.deepcopy(self.small))
        self.assertEqual(summary["total_words"], 60)
        self.assertEqual(summary["retained_charts"], 4)
        self.assertEqual(summary["represented_seed_states"], 53)

    def test_digest_stability(self) -> None:
        again = build.build_certificate(64**2, 4)
        self.assertEqual(self.small, again)
        self.assertEqual(
            self.small["semantic_digest"],
            verify.sha(self.small["semantic"]),
        )

    def test_tamper_resistance_even_if_digests_are_rewritten(self) -> None:
        tampered = copy.deepcopy(self.small)
        tampered["semantic"]["enumeration"]["depths"][0][
            "represented_seed_states"
        ] += 1
        tampered["semantic_digest"] = verify.sha(tampered["semantic"])
        artifact_input = {
            "semantic": tampered["semantic"],
            "semantic_digest": tampered["semantic_digest"],
            "provenance": tampered["provenance"],
        }
        tampered["artifact_digest"] = verify.sha(artifact_input)
        with self.assertRaisesRegex(
            verify.VerificationError, "independent semantic reconstruction"
        ):
            verify.verify_certificate_data(tampered)

    def test_raw_digest_and_boundary_tampering_are_rejected(self) -> None:
        bad_digest = copy.deepcopy(self.small)
        bad_digest["semantic_digest"] = "0" * 64
        with self.assertRaisesRegex(verify.VerificationError, "semantic digest"):
            verify.verify_certificate_data(bad_digest)

        bad_boundary = copy.deepcopy(self.small)
        bad_boundary["semantic"]["representatives"][0]["first_lexicographic"][
            "boundary_replay"
        ][1]["B"][0] += 1
        bad_boundary["semantic_digest"] = verify.sha(bad_boundary["semantic"])
        artifact_input = {
            "semantic": bad_boundary["semantic"],
            "semantic_digest": bad_boundary["semantic_digest"],
            "provenance": bad_boundary["provenance"],
        }
        bad_boundary["artifact_digest"] = verify.sha(artifact_input)
        with self.assertRaisesRegex(
            verify.VerificationError, "independent semantic reconstruction"
        ):
            verify.verify_certificate_data(bad_boundary)


if __name__ == "__main__":
    unittest.main()
