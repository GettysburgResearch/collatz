#!/usr/bin/env python3
"""Regression and adversarial tests for X-8260."""
from __future__ import annotations

import gzip
import importlib.util
import json
import sys
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUTHOR = load_module("x8260_author_tests", "run.py")
INDEPENDENT = load_module("x8260_independent_tests", "verify.py")


class ThreePulseCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload, cls.raw, cls.compressed = AUTHOR.build_bundle()

    def test_largest_gap_normalization_and_tie_rule(self) -> None:
        self.assertEqual(
            AUTHOR.normalize_three_support(2, 6, 0, (0, 2, 4)),
            (0, 2, 4),
        )
        self.assertEqual(
            AUTHOR.normalize_three_support(2, 6, 1, (1, 3, 5)),
            (0, 2, 4),
        )
        p11 = AUTHOR.FAMILIES[1]
        keys, coverage = AUTHOR.normalized_packet_keys(p11, 1)
        self.assertEqual(len(keys), 35)
        self.assertEqual(coverage["raw_rotation_support_configurations"], 245)
        self.assertEqual(coverage["primitive_rotations"], list(range(7)))
        self.assertLessEqual(
            coverage["maximum_p3"], coverage["floor_2kr_over_3"]
        )

    def test_known_reduced_resultant_packet(self) -> None:
        p3 = AUTHOR.FAMILIES[0]
        packet = AUTHOR.compile_packet(p3, 3, (0, 2, 4))
        self.assertEqual(packet.weights, (567, 504, 448))
        self.assertEqual(packet.coefficients, (-567, 63, 56, 448))
        self.assertEqual(packet.caps, (1374, 1347, 1324))
        self.assertEqual(packet.max_heights, (10, 10, 10))

    def test_analytic_boundary_rows(self) -> None:
        p3 = self.payload["analytic_reduction"][0]
        p11 = self.payload["analytic_reduction"][1]
        self.assertEqual(
            [row["r"] for row in p3["transition_rejections"]],
            [4, 5, 6, 7, 8, 9],
        )
        self.assertEqual(
            [row["r"] for row in p11["transition_rejections"]], [2]
        )
        exceptional = p3["exceptional_rows"]
        self.assertEqual(len(exceptional), 1)
        self.assertEqual(exceptional[0]["minimum_multiple_m"], 3)
        self.assertTrue(exceptional[0]["all_m_at_least_3_rejected"])

    def test_frozen_bundle_and_independent_reconstruction(self) -> None:
        canonical = json.loads(
            (HERE / "results" / "canonical.json").read_text(encoding="utf-8")
        )
        compressed = (HERE / "results" / "finite-tuples.jsonl.gz").read_bytes()
        self.assertEqual(self.payload, canonical)
        self.assertEqual(self.compressed, compressed)
        self.assertEqual(gzip.decompress(compressed), self.raw)
        self.assertEqual(
            INDEPENDENT.reconstruct(self.raw, self.compressed), self.payload
        )
        self.assertEqual(self.payload["totals"]["finite_tuples"], 53_808)
        self.assertEqual(self.payload["totals"]["nontrivial_hits"], 0)
        self.assertEqual(self.payload["totals"]["trivial_hits"], 1)

    def test_tuple_transcript_tampering_is_detected(self) -> None:
        lines = self.raw.splitlines()
        record = json.loads(lines[1])
        record[5] += 1
        lines[1] = json.dumps(record, separators=(",", ":")).encode("ascii")
        tampered = b"\n".join(lines) + b"\n"
        with self.assertRaises(AssertionError):
            INDEPENDENT.rebuild_finite(tampered)


if __name__ == "__main__":
    unittest.main()
