#!/usr/bin/env python3
"""Exact lightweight checks for the fixed-height power-saving attack.

The script checks only finite arithmetic and small exhaustive interfaces used by
MZ-FH-001--005.  It is not a proof of fixed-height forward power saving and it
does not replay either external Lean development.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import sys

sys.set_int_max_str_digits(0)

CHECK_MAX_N = 16
NO_DESCENT_THRESHOLD = 6500
BETA_NUM = 19
BETA_DEN = 20
SLOPE_NUM = 6309
SLOPE_DEN = 10000


@dataclass(frozen=True)
class Row:
    depth: int
    ballot_words: int
    no_descent_roots: int
    cycle_lemma_classes_checked: int


def accelerated(n: int) -> int:
    if n < 0:
        raise ValueError("accelerated map expects n >= 0")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def word_root(bits: tuple[int, ...]) -> int:
    """Canonical residue in [0,2^N) realizing one parity word."""
    affine = 0
    odd_count = 0
    for k, bit in enumerate(bits):
        if bit:
            affine = 3 * affine + (1 << k)
            odd_count += 1
    modulus = 1 << len(bits)
    inv = pow(pow(3, odd_count), -1, modulus)
    return (-affine * inv) % modulus


def realizes(n: int, bits: tuple[int, ...]) -> bool:
    x = n
    for bit in bits:
        if x % 2 != bit:
            return False
        x = accelerated(x)
    return True


def ballot(bits: tuple[int, ...]) -> bool:
    odd_count = 0
    for k, bit in enumerate(bits, start=1):
        odd_count += bit
        if pow(3, odd_count) < (1 << k):
            return False
    return True


def no_descent(n: int, depth: int) -> bool:
    x = n
    for _ in range(depth):
        x = accelerated(x)
        if x < n:
            return False
    return True


def least_strict_supercritical_weight(depth: int) -> int:
    for q in range(depth + 1):
        if pow(3, q) > (1 << depth):
            return q
    raise AssertionError("no strict supercritical weight")


def rotations(bits: tuple[int, ...]):
    n = len(bits)
    for shift in range(n):
        yield bits[shift:] + bits[:shift]


def exact_inequalities() -> dict[str, bool]:
    # log(2)/log(3) > 6309/10000.
    alpha_floor = pow(3, 6309) < pow(2, 10000)

    # log(2)/log(3 + 1/6500) > 6309/10000.
    no_descent_floor = (
        pow(19501, 6309) < pow(2, 10000) * pow(6500, 6309)
    )

    # Chernoff base with z=6309/3691 is < 2^(19/20):
    # [(10000/3691)(3691/6309)^(6309/10000)]^10000 < 2^9500.
    entropy_enclosure = (
        pow(10000, 10000)
        < pow(2, 9500) * pow(3691, 3691) * pow(6309, 6309)
    )

    return {
        "alpha_gt_6309_over_10000": alpha_floor,
        "log2_over_log_3_plus_1_over_6500_gt_6309_over_10000": no_descent_floor,
        "chernoff_base_lt_2_pow_19_over_20": entropy_enclosure,
    }


def exhaustive_rows() -> list[Row]:
    rows: list[Row] = []
    for depth in range(1, CHECK_MAX_N + 1):
        seen_roots: set[int] = set()
        ballot_count = 0
        no_descent_count = 0
        for bits in itertools.product((0, 1), repeat=depth):
            root = word_root(bits)
            if root in seen_roots:
                raise AssertionError(f"duplicate root at depth {depth}: {root}")
            seen_roots.add(root)
            if not realizes(root, bits):
                raise AssertionError(f"root does not realize word at depth {depth}")
            if ballot(bits):
                ballot_count += 1
                if root == 0:
                    raise AssertionError("a ballot word had zero canonical root")
                if not no_descent(root, depth):
                    raise AssertionError("ballot root failed actual no-descent")

        if len(seen_roots) != 1 << depth:
            raise AssertionError("parity-cylinder bijection count failed")

        no_descent_count = sum(
            no_descent(n, depth) for n in range(1, 1 << depth)
        )

        q = least_strict_supercritical_weight(depth)
        cycle_classes: set[tuple[int, ...]] = set()
        checked_classes = 0
        for ones in itertools.combinations(range(depth), q):
            bits_list = [0] * depth
            for idx in ones:
                bits_list[idx] = 1
            bits = tuple(bits_list)
            canonical_class = min(rotations(bits))
            if canonical_class in cycle_classes:
                continue
            cycle_classes.add(canonical_class)
            checked_classes += 1
            if not any(ballot(rot) for rot in rotations(bits)):
                raise AssertionError(
                    f"cycle-lemma rotation failed at depth {depth}, q={q}"
                )

        rows.append(
            Row(
                depth=depth,
                ballot_words=ballot_count,
                no_descent_roots=no_descent_count,
                cycle_lemma_classes_checked=checked_classes,
            )
        )
    return rows


def exact_finite_bound_checks() -> list[dict[str, int | bool]]:
    out: list[dict[str, int | bool]] = []
    for depth in range(1, CHECK_MAX_N + 1):
        cutoff = 1 << depth
        count = sum(no_descent(n, depth) for n in range(1, cutoff + 1))
        excess = max(0, count - (NO_DESCENT_THRESHOLD - 1))
        # excess <= 2 X^(19/20), checked without floating point.
        inequality = pow(excess, 20) <= pow(2, 20) * pow(cutoff, 19)
        if not inequality:
            raise AssertionError(f"finite theorem check failed at X={cutoff}")
        out.append(
            {
                "cutoff": cutoff,
                "depth": depth,
                "no_descent_count": count,
                "exact_power_inequality": inequality,
            }
        )
    return out


def bootstrap_algebra() -> dict[str, str | bool]:
    # A hypothetical crossing-grade parameter point.  This verifies only the
    # algebra in MZ-FH-005, not the missing Collatz killed-set
    # decorrelation premise.
    r = Fraction(1, 2)
    local_saving = Fraction(3, 25)   # D = 0.12
    fiber_gain = Fraction(3, 50)     # delta = 0.06
    beta = Fraction(89, 100)         # 0.89
    inverse_gamma = Fraction(901, 1000)

    local_guard = beta > 1 - local_saving
    fiber_guard = beta > 1 - fiber_gain / (1 - r)
    crossing = beta < inverse_gamma
    exponent_gap = beta - (1 - r - fiber_gain + r * beta)

    if not (local_guard and fiber_guard and crossing and exponent_gap > 0):
        raise AssertionError("bootstrap sample algebra failed")

    return {
        "r": str(r),
        "D": str(local_saving),
        "delta": str(fiber_gain),
        "beta": str(beta),
        "inverse_gamma": str(inverse_gamma),
        "local_guard": local_guard,
        "fiber_guard": fiber_guard,
        "crosses_0_901": crossing,
        "recursive_exponent_gap": str(exponent_gap),
        "warning": "The parameter point is illustrative; no Collatz killed-set decorrelation certificate with these values is supplied.",
    }


def main() -> int:
    exact = exact_inequalities()
    if not all(exact.values()):
        raise AssertionError(f"exact inequality failed: {exact}")

    rows = exhaustive_rows()
    finite = exact_finite_bound_checks()
    bootstrap = bootstrap_algebra()

    payload = {
        "status": "finite checks passed; fixed-height power saving remains unproved",
        "scope": {
            "max_exhaustive_depth": CHECK_MAX_N,
            "does_not_prove": [
                "fixed-height forward power saving",
                "MZ-FH-005 killed-set decorrelation hypothesis",
                "SC*",
                "FC*",
                "the Collatz conjecture",
            ],
        },
        "constants": {
            "no_descent_small_range_cutoff": NO_DESCENT_THRESHOLD,
            "slope_floor": f"{SLOPE_NUM}/{SLOPE_DEN}",
            "proved_finite_exponent": f"{BETA_NUM}/{BETA_DEN}",
        },
        "exact_inequalities": exact,
        "exhaustive_rows": [asdict(row) for row in rows],
        "finite_bound_checks": finite,
        "bootstrap_algebra": bootstrap,
    }
    semantic = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["semantic_sha256"] = hashlib.sha256(semantic).hexdigest()

    output = Path(__file__).with_name("fixed-height-check-report.json")
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"all fixed-height attack checks passed: {payload['semantic_sha256']}")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
