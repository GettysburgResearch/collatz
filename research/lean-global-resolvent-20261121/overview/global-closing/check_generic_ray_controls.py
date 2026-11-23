#!/usr/bin/env python3
"""Exact finite controls for the sparse insertion proof, not an iid simulation."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import random


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def endpoint_ok(n: int, total: int, inserted: int, sign: int) -> bool:
    if sign == 1:
        return 3 ** (n + inserted) >= (1 << (total + inserted)) * (n + 1) ** 3
    return 3 ** (n + inserted) * (n + 1) ** 3 <= 1 << (total + 2 * inserted)


def regulate(raw: list[int], sign: int) -> tuple[list[int], list[int]]:
    require(sign in (-1, 1), "invalid regulator sign")
    require(all(isinstance(g, int) and g >= 1 for g in raw), "invalid raw gaps")
    output: list[int] = []
    counts: list[int] = []
    total = inserted = 0
    gap = 1 if sign == 1 else 2
    for n, g in enumerate(raw, 1):
        total += g
        old = inserted
        while not endpoint_ok(n, total, inserted, sign):
            inserted += 1
        output.extend([gap] * (inserted - old))
        output.append(g)
        counts.append(inserted)
    return output, counts


def verify_regulation(raw: list[int], sign: int, output: list[int], counts: list[int]) -> dict:
    require(len(counts) == len(raw), "wrong number of raw endpoints")
    gap = 1 if sign == 1 else 2
    j = total = raw_total = old = 0
    positive = sign == 1
    for n, (g, inserted) in enumerate(zip(raw, counts), 1):
        require(inserted >= old, "regulator decreased")
        raw_total += g
        require(endpoint_ok(n, raw_total, inserted, sign), "endpoint barrier failed")
        if inserted > old:
            require(not endpoint_ok(n, raw_total, inserted - 1, sign), "nonminimal new record")
        for _ in range(inserted - old):
            require(j < len(output) and output[j] == gap, "wrong inserted gap")
            j += 1
            total += gap
            if positive:
                require(3**j >= (1 << total) * n**3, "positive interstitial barrier failed")
                require(3**j > 1 << total, "origin is not a strict minimum")
            else:
                require(3**j * n**3 <= 1 << total, "negative interstitial barrier failed")
                require(3**j < 1 << total, "origin is not a strict maximum")
        require(j < len(output) and output[j] == g, "wrong raw gap")
        j += 1
        total += g
        require(total == raw_total + gap * inserted, "first-moment identity failed")
        require(j == n + inserted, "clock identity failed")
        if positive:
            require(3**j >= (1 << total) * (n + 1) ** 3, "positive endpoint bound failed")
        else:
            require(3**j * (n + 1) ** 3 <= 1 << total, "negative endpoint bound failed")
        old = inserted
    require(j == len(output), "unaccounted output suffix")
    return {"raw_length": len(raw), "output_length": j, "inserted": old,
            "raw_total_gap": raw_total, "output_total_gap": total,
            "sign": sign, "all_clock_barriers": True, "record_minimality": True}


def blocks(word: list[int], r: int) -> Counter:
    return Counter(tuple(word[i:i+r]) for i in range(max(0, len(word) - r + 1)))


def verify_block_counts(raw: list[int], output: list[int], inserted: int) -> None:
    for r in range(1, 6):
        left, right = blocks(raw, r), blocks(output, r)
        for pattern in left.keys() | right.keys():
            require(abs(left[pattern] - right[pattern]) <= (2*r - 1) * inserted,
                    "deletion block-count bound failed")


def literal_gaps(source: int, expected: list[int]) -> list[int]:
    require(source > 0 and source % 2 == 1, "source must be positive odd")
    q = source
    states = [q]
    for g in expected:
        numerator = 3*q + 1
        actual = (numerator & -numerator).bit_length() - 1
        require(actual == g, "ordinary source realizes a wrong valuation")
        q = numerator >> g
        require(q > 0 and q % 2 == 1, "ordinary endpoint is not positive odd")
        states.append(q)
    return states


def finite_realizer(gaps: list[int], floor: int) -> dict:
    total = carry = 0
    for g in gaps:
        carry = 3*carry + (1 << total)
        total += g
    length = len(gaps)
    modulus = 1 << (total + 1)
    residue = (((1 << total) - carry) * pow(3**length, -1, modulus)) % modulus
    # At most L(L+1)/2 values can have a repeated state. Raising the lift
    # first ensures all states exceed the requested floor as well.
    source = residue + (floor + 1) * modulus
    for _ in range(length * (length + 1) // 2 + 1):
        states = literal_gaps(source, gaps)
        if min(states) > floor and len(set(states)) == len(states):
            break
        source += modulus
    else:
        raise ValueError("finite affine collision avoidance failed")
    require((3**length * source + carry) == (1 << total) * states[-1],
            "complete affine identity failed")
    # The 2-adic truncation includes j=L: that term records an odd tail.
    code = 0
    partial = 0
    for j in range(length + 1):
        code -= (1 << partial) * pow(3**(j+1), -1, modulus)
        if j < length:
            partial += gaps[j]
    require(code % modulus == residue, "2-adic code and carry residue disagree")
    return {"prefix_length": length, "total_gap": total, "source": str(source),
            "source_bits": source.bit_length(), "floor": floor,
            "minimum_state": str(min(states)), "all_states_distinct": True,
            "exact_gap_valuations": True, "code_matches_carry_residue": True}


def verify_series_orientation(gaps: list[int]) -> dict:
    total = 0
    inverse = Fraction(1, 3)
    forward = Fraction(0)
    chis = [Fraction(1)]
    for j, g in enumerate(gaps, 1):
        total += g
        chi = Fraction(3**j, 1 << total)
        chis.append(chi)
        inverse += 1 / (3 * chi)
        forward += chi / 3
    require(inverse == sum((Fraction(1, 3*x) for x in chis), Fraction(0)),
            "inverse series orientation failed")
    require(forward == sum((x / 3 for x in chis[1:]), Fraction(0)),
            "reversed series orientation failed")
    require(inverse != forward, "fixture must distinguish the two series")
    # Check forward real affine identity at each clock, with the finite
    # inverse sum stopping BEFORE that clock.
    q0 = Fraction(7)
    q = q0
    tail = Fraction(0)
    for j, g in enumerate(gaps):
        tail += 1 / (3 * chis[j])
        q = (3*q + 1) / (1 << g)
        require(q == chis[j+1] * (q0 + tail), "real affine orientation failed")
    return {"tested_length": len(gaps), "two_series_distinguished": True,
            "real_affine_identity": True}


def must_reject(action, label: str) -> str:
    try:
        action()
    except ValueError:
        return label
    raise ValueError("damaged control was accepted: " + label)


def main() -> None:
    rng = random.Random(20261123)
    # A rational 5/8 geometric sampler is ONLY a reproducible finite fixture.
    # It is not the theorem's irrational-parameter iid input, and its
    # infinite extension is not claimed to have a sublinear regulator.
    finite_random = []
    for _ in range(256):
        g = 1
        while rng.randrange(8) >= 5:
            g += 1
        finite_random.append(g)
    fixtures = {
        "spikes": [1, 17, 1, 2, 1, 1, 23, 1, 2, 9, 1, 1],
        "alternating": [1, 2] * 64,
        "finite_rational_sampler": finite_random,
    }
    rows = []
    for name, raw in fixtures.items():
        for sign in (1, -1):
            out, counts = regulate(raw, sign)
            row = verify_regulation(raw, sign, out, counts)
            verify_block_counts(raw, out, counts[-1])
            row.update({"fixture": name, "block_count_lengths_checked": [1, 2, 3, 4, 5],
                        "finite_realizer": finite_realizer(out[:24], 1000),
                        "series_orientation": verify_series_orientation(out[:24])})
            rows.append(row)
    raw = [1, 17, 1, 2]
    out, counts = regulate(raw, 1)
    damaged = out.copy()
    damaged[0] = 2
    wrong_counts = counts.copy()
    wrong_counts[0] -= 1
    controls = [
        must_reject(lambda: verify_regulation(raw, 1, damaged, counts), "wrong inserted gap"),
        must_reject(lambda: verify_regulation(raw, 1, out, wrong_counts), "missing needed insertion"),
        must_reject(lambda: verify_regulation(raw, -1, out, counts), "swapped pressure sign"),
        must_reject(lambda: literal_gaps(1, [1]), "wrong ordinary realizer"),
    ]
    require(11**11 < 15**10, "explicit nonatomic entropy margin failed")
    here = Path(__file__).resolve().parent
    note = here / "GENERIC_RAY_CONSTRUCTION.md"
    result = {
        "schema": "collatz-generic-ray-finite-controls/v1",
        "status": "PASS",
        "scope": "Finite exact algebra only; asymptotic theorem is the written proof.",
        "proof_sha256": hashlib.sha256(note.read_bytes()).hexdigest(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "raw_fixture_warning": "Finite rational sampler is not the critical iid theorem law.",
        "cases": rows,
        "damaged_controls_rejected": controls,
        "nonatomic_margin": {"left": str(11**11), "right": str(15**10), "strict": True},
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
