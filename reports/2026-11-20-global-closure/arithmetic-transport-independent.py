#!/usr/bin/env python3
"""Independent physical-return and exact-source-mass review of transport.

The logarithm enclosure implementation is reused only after a separate written
audit of its analytic remainder and rounding. Rank/A/B and source transport
are reconstructed here, without importing the author's arithmetic formulas
for A endpoints or its interval mass transport. This is bounded evidence.
"""

from collections import defaultdict
from fractions import Fraction
from functools import cache
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "experiments/global_closure_transport.py"
EXPECTED_TARGET = "68e74e13aa3ebf7aaeef743dcbcd9a06216f349a4c65af8cf703a3eea20d3d83"
CUTOFF = 512
HORIZON = 32
RANK_INPUTS = set()
A_INPUTS = set()
B_INPUTS = set()
COUNTS = defaultdict(int)


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


def shortcut(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


@cache
def reference_rank(n):
    RANK_INPUTS.add(n)
    if n == 1:
        return 0
    temp = 2 * n + 1
    h = 0
    while temp % 3 == 0:
        temp //= 3
        h += 1
    values = []
    # Includes all source-qualified minimizing modes, plus extra modes.
    for a in range(max(8, h + 4) + 1):
        z = (3 ** a - 2 ** (a + 1)) * n + 3 ** a - 2 ** a
        check(z != 0, "unexpected zero component above 1")
        three_part = 1
        while z % (three_part * 3) == 0:
            three_part *= 3
        values.append(z * z // three_part)
    return min(values)


@cache
def reference_a(n):
    A_INPUTS.add(n)
    if n == 1:
        return 1
    probe = n
    odd_count = 0
    while probe % 2:
        probe = shortcut(probe)
        odd_count += 1
    word = [1] * odd_count + [0]
    current = n
    copies = 0
    while current != 1:
        trial = current
        legal = True
        for bit in word:
            if trial % 2 != bit:
                legal = False
                break
            trial = shortcut(trial)
        if not legal:
            break
        current = trial
        copies += 1
        COUNTS["accepted_physical_shortcut_edges"] += len(word)
        check(copies < 10000, "bounded reviewer guard exhausted")
    check(copies > 0, "empty physical acceleration")
    return current


@cache
def reference_unsafe(n):
    return n > 1 and 4 * reference_rank(reference_a(n)) > reference_rank(n)


@cache
def reference_b(n):
    B_INPUTS.add(n)
    check(reference_unsafe(n), "unsafe source required")
    current = reference_a(n)
    safe_steps = 0
    while current != 1 and not reference_unsafe(current):
        following = reference_a(current)
        check(4 * reference_rank(following) <= reference_rank(current), "safe rank descent")
        current = following
        safe_steps += 1
        check(safe_steps < 10000, "bounded safe reviewer guard exhausted")
    COUNTS["accepted_safe_a_steps"] += safe_steps
    return current


def main():
    check(sha256(TARGET.read_bytes()).hexdigest() == EXPECTED_TARGET, "reviewed checker changed")
    spec = importlib.util.spec_from_file_location("reviewed_transport", TARGET)
    author = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(author)
    result = author.run(CUTOFF, HORIZON)
    scale = author.SCALE
    rows = {r["horizon"]: r for r in result["functional_enclosures"]}
    starts = [n for n in range(2, CUTOFF + 1) if reference_unsafe(n)]
    mass = {n: Fraction(1, n * (n + 1)) for n in starts}
    original_mass = sum(mass.values(), Fraction(0))
    killed_mass = Fraction(0)
    accumulated_low = Fraction(0)
    accumulated_high = Fraction(0)
    checkpoints_checked = []
    for j in range(HORIZON):
        for n, weight in mass.items():
            lo, hi = author.reciprocal_psi(n)
            accumulated_low += weight * Fraction(lo, scale)
            accumulated_high += weight * Fraction(hi, scale)
        if j + 1 in rows:
            row = rows[j + 1]
            recorded = row["finite_source_G"]
            check(Fraction(int(recorded["lower_scaled"]), scale) <= accumulated_low,
                  "author lower interval exceeds independent exact-weight lower bound")
            check(accumulated_high <= Fraction(int(recorded["upper_scaled"]), scale),
                  "author upper interval misses independent exact-weight upper bound")
            check(row["finite_source_carriers_at_last_observation"] == len(mass),
                  "carrier count mismatch")
            tail_lo, _ = author.psi_from_rank(1)
            exact_tail_upper = Fraction((j + 1) * scale, (CUTOFF + 1) * tail_lo)
            tail_record = row["omitted_original_source_tail_upper"]
            check(exact_tail_upper <= Fraction(int(tail_record["upper_scaled"]), scale),
                  "source-tail upper bound rounded inwards")
            checkpoints_checked.append(j + 1)
        following = defaultdict(Fraction)
        for n, weight in mass.items():
            endpoint = reference_b(n)
            if endpoint == 1:
                killed_mass += weight
            else:
                following[endpoint] += weight
        mass = dict(following)
        check(sum(mass.values(), Fraction(0)) + killed_mass == original_mass,
              "original-source mass was not conserved until killing")
    for n in RANK_INPUTS:
        check(reference_rank(n) == author.rank(n), "rank mismatch")
    for n in A_INPUTS:
        check(reference_a(n) == author.accel(n), "physical acceleration mismatch")
    for n in B_INPUTS:
        check(reference_b(n) == author.actual_return(n), "actual return mismatch")
    receipt = {
        "status": "PASS",
        "scope": "independent bounded physical A/B reconstruction and exact rational original-source mass; audited author logarithm intervals reused",
        "reviewed_checker_sha256": EXPECTED_TARGET,
        "source_cutoff": CUTOFF,
        "return_horizon": HORIZON,
        "unsafe_sources": len(starts),
        "rank_inputs_compared": len(RANK_INPUTS),
        "physical_accelerations_compared": len(A_INPUTS),
        "actual_returns_compared": len(B_INPUTS),
        "functional_and_source_tail_checkpoints": checkpoints_checked,
        "final_surviving_carriers": len(mass),
        "exact_mass_conservation_horizons": HORIZON,
        "physical_counts": dict(sorted(COUNTS.items())),
        "limitations": [
            "Rank minimizer reduction remains qualified to the pinned source proof.",
            "No global Green upper bound or cycle exclusion is inferred.",
            "The author's logarithm routine was algebraically reviewed and reused; it is not claimed independently reimplemented here."
        ],
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
