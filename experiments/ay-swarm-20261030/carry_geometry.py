#!/usr/bin/env python3
"""Exact carry-chamber identities and compressed Collatz/SRS macros.

Run lengths, like all arithmetic here, are arbitrary precision integers. The
compressed macro does O(number of input runs) state transitions, not O(bit length).
It proves no universal termination claim. All checks use explicit exceptions so
that the same checks execute under python -O.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def odd_step(n):
    require(type(n) is int and n > 0 and n % 2 == 1, "positive odd integer required")
    m = 3 * n + 1
    return m // (m & -m)


def trailing_ones(n):
    x = n + 1
    return (x & -x).bit_length() - 1


def runs_lsb(n):
    require(type(n) is int and n > 0, "positive integer required")
    runs = []
    for bit in bin(n)[:1:-1]:
        append_run(runs, int(bit), 1)
    return runs


def append_run(runs, bit, length):
    if length == 0:
        return
    require(bit in (0, 1) and type(length) is int and length > 0,
            "invalid run")
    if runs and runs[-1][0] == bit:
        runs[-1] = (bit, runs[-1][1] + length)
    else:
        runs.append((bit, length))


def run_value(runs):
    shift = 0
    value = 0
    for bit, length in runs:
        if bit:
            value += ((1 << length) - 1) << shift
        shift += length
    return value


def run_popcount(runs):
    return sum(length for bit, length in runs if bit)


def run_rank(runs):
    s = run_popcount(runs)
    require(runs and runs[0][0] == 1 and runs[-1][0] == 1,
            "canonical odd runs required")
    r = runs[0][1]
    return s * (s - 1) // 2 + r


def flux(runs):
    """P,M,O and signed flux using run lengths truncated at two.

    state is the carry after the preceding constant run. At the first run
    it is 1, supplied by the odd source and the +1 in 3n+1.
    """
    require(runs and runs[0][0] == 1 and runs[-1][0] == 1,
            "canonical odd runs required")
    state = 1
    debit = credit = opening = 0
    for bit, length in runs:
        if bit == 0 and length >= 2 and state == 1:
            opening += 1
        if length == 1:
            debit += int(bit == 1 and state == 0)
            credit += int(bit == 0 and state == 1)
        else:
            state = bit
    return {"P": debit, "M": credit, "O": opening,
            "defect": debit - credit, "ag": credit + opening}


def guarded(runs):
    d = flux(runs)["defect"]
    return d < 0 or (d == 0 and runs[0][1] >= 2)


def carry_reference(n):
    """Independent schoolbook bit-addition reference for 3n+1."""
    previous_bit = 0
    carry = 1
    occupancy = 0
    reconstructed = 0
    for i in range(n.bit_length() + 2):
        bit = (n >> i) & 1
        z = bit + previous_bit + carry
        reconstructed |= (z % 2) << i
        carry = z // 2
        occupancy += carry
        previous_bit = bit
    require(reconstructed == 3 * n + 1 and carry == 0,
            "schoolbook reconstruction failed")
    return occupancy


def compressed_macro(runs):
    """Canonical odd SRS macro followed by all even shortcut steps.

    Returns the shortcut and accelerated output runs and exact counts of the
    eleven SRS rules. Counts for normalization to U include the additional ad
    steps. n=1 is deliberately terminal, not assigned the arithmetic 1-cycle.
    """
    require(runs and runs[0][0] == 1 and runs[-1][0] == 1,
            "canonical odd runs required")
    if runs == [(1, 1)]:
        return {"T_runs": runs[:], "U_runs": runs[:], "rules": {},
                "terminated": True}
    internal = list(runs)
    # Delete the represented leading 1 (c) and final odd bit (b).
    first_bit, first_length = internal[0]
    internal[0] = (first_bit, first_length - 1)
    last_bit, last_length = internal[-1]
    internal[-1] = (last_bit, last_length - 1)
    internal = [(b, length) for b, length in internal if length]
    ternary = 2
    out = []
    counts = Counter({"bd": 1})
    for bit, length in internal:
        remaining = length
        # On a constant bit, the three-state transducer reaches its stable
        # state (0 for bit 0, 2 for bit 1) in at most two transitions.
        for _ in range(min(2, remaining)):
            rule = "ab"[bit] + "efg"[ternary]
            counts[rule] += 1
            z = 3 * bit + ternary
            append_run(out, z % 2, 1)
            ternary = z // 2
            remaining -= 1
        if remaining:
            require(ternary == 2 * bit, "constant-run stabilization failed")
            counts["ab"[bit] + "efg"[ternary]] += remaining
            append_run(out, bit, remaining)
    counts["c" + "efg"[ternary]] += 1
    # ce/cf/cg represent 3,4,5, respectively, at the high boundary.
    for bit, length in runs_lsb(3 + ternary):
        append_run(out, bit, length)
    shortcut = out[:]
    if out and out[0][0] == 0:
        counts["ad"] += out[0][1]
        out = out[1:]
    return {"T_runs": shortcut, "U_runs": out,
            "rules": dict(sorted(counts.items())), "terminated": False}


def feature_row(n):
    s = n.bit_count()
    C = carry_reference(n)
    return {"n": n, "U": odd_step(n), "s": s,
            "z": n.bit_length() + 1 - C, "r": trailing_ones(n)}


def run_checks(max_n=65535):
    odd_count = (max_n + 1) // 2
    safe = unsafe = no00 = shielded = 0
    first_unsafe = []
    for n in range(1, max_n + 1, 2):
        rr = runs_lsb(n)
        f = flux(rr)
        u = odd_step(n)
        require(u.bit_count() - n.bit_count() == f["defect"],
                f"run flux at {n}")
        C = carry_reference(n)
        require(u.bit_count() == 2 * n.bit_count() + 1 - C,
                f"carry occupancy at {n}")
        actual_guard = run_rank(runs_lsb(u)) < run_rank(rr)
        require(actual_guard == guarded(rr), f"maximal guard at {n}")
        macro = compressed_macro(rr)
        require(run_value(macro["U_runs"]) == u, f"compressed U at {n}")
        if n > 1:
            require(run_value(macro["T_runs"]) == (3 * n + 1) // 2,
                    f"compressed T at {n}")
            require(macro["rules"].get("ag", 0) == f["ag"],
                    f"critical-event count at {n}")
        if actual_guard:
            safe += 1
        else:
            unsafe += 1
            if n > 1 and len(first_unsafe) < 12:
                first_unsafe.append(n)
        if n > 1 and "00" not in bin(n)[2:]:
            no00 += 1
            require(actual_guard, f"no00 guard at {n}")
        # A concrete regular sublanguage of the one-counter exact guard.
        if n > 1 and f["P"] == 0 and (f["M"] > 0 or rr[0][1] >= 2):
            shielded += 1
            require(actual_guard, f"regular carry guard at {n}")

    # All run skeletons with <= 11 runs, each run short or long, retaining
    # their exact length-2 representative and the input's two end boundaries.
    skeletons = 0
    for count in range(1, 12, 2):
        for lengths in product((1, 2), repeat=count):
            rr = [(1 - (i % 2), length) for i, length in enumerate(lengths)]
            n = run_value(rr)
            f = flux(rr)
            macro = compressed_macro(rr)
            require(run_value(macro["U_runs"]) == odd_step(n),
                    "skeleton macro")
            require(run_popcount(macro["U_runs"]) - run_popcount(rr) == f["defect"],
                    "skeleton flux")
            skeletons += 1

    # Constant-run arithmetic with exponents too large to expand as integers.
    huge = 10 ** 80
    enormous = [
        [(1, huge)],
        [(1, 1), (0, huge), (1, 1)],
        [(1, huge), (0, huge + 1), (1, huge + 2)],
        [(1, 1), (0, 2), (1, huge), (0, 1), (1, huge + 3)],
    ]
    huge_receipts = []
    for rr in enormous:
        macro = compressed_macro(rr)
        f = flux(rr)
        require(run_popcount(macro["U_runs"]) - run_popcount(rr) == f["defect"],
                "enormous run flux")
        require(macro["rules"].get("ag", 0) == f["ag"],
                "enormous critical-event count")
        huge_receipts.append({"input_runs": rr, "U_runs": macro["U_runs"],
                              "flux": f, "rule_counts": macro["rules"]})

    paired = []
    for m in range(1, 257):
        n = 1 + 8 * ((4 ** m - 1) // 3)
        neighbor = n + 6
        require((3 * n + 1) // 2 == (1 << (2 * m + 2)) - 2,
                "dense paired output")
        require((3 * neighbor + 1) // 2 == (1 << (2 * m + 2)) + 7,
                "sparse paired output")
        require(odd_step(n) == (1 << (2 * m + 1)) - 1,
                "paired odd output")
        require(flux(runs_lsb(n)) == {"P": m, "M": 0, "O": 1,
                                            "defect": m, "ag": 1},
                "unbounded debt from one event")
        if m in (1, 2, 4, 16, 256):
            paired.append({"m": m, "source_bit_length": n.bit_length(),
                           "source_popcount": n.bit_count(),
                           "output_popcount": odd_step(n).bit_count(),
                           "neighbor_output_popcount": odd_step(neighbor).bit_count(),
                           "ag": 1})

    # Exact affine-feature obstruction data: 3->5, 9->7, 11->17.
    obstruction = [{"source": feature_row(n), "target": feature_row(odd_step(n))}
                   for n in (3, 9, 11)]
    return {
        "status": "PASS",
        "scope": "exact bounded checks and parameterized identity checks; no universal termination claim",
        "max_n": max_n, "odd_sources": odd_count,
        "rank_decrease_sources": safe, "rank_non_decrease_sources": unsafe,
        "no00_sources_above_one": no00,
        "regular_carry_guard_sources_above_one": shielded,
        "first_non_decrease_sources_above_one": first_unsafe,
        "run_skeletons": skeletons,
        "paired_family_parameters_checked": 256,
        "paired_examples": paired,
        "enormous_run_checks": huge_receipts,
        "affine_obstruction": obstruction,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=65535)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    require(args.max_n >= 1 and args.max_n % 2 == 1, "max-n must be positive odd")
    result = run_checks(args.max_n)
    encoded = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")


if __name__ == "__main__":
    main()
