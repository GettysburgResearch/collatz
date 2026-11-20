#!/usr/bin/env python3
"""Complete modular certificates for multiplication-by-three run escape.

This independent implementation uses upper run boundaries and complete
multiplication orbits. It does not import the adaptive-core implementation.
All counts and comparisons are exact integers. This certifies homogeneous
run escape, not unrestricted Collatz termination.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path


def require(value: bool, message: str) -> None:
    if not value:
        raise ValueError(message)


def run_count(n: int) -> int:
    require(n >= 0, "negative run-count argument")
    return (n & ~(n >> 1)).bit_count()


def certify(bits: int, cap: int, delta: int) -> dict:
    require(cap >= 1 and bits >= 2 * cap + 3, "insufficient precision")
    require(delta in (0, 1), "invalid shift")
    modulus = 1 << bits
    period = 1 << (bits - 2)
    maximum = 0
    witness = None
    good_count = 0
    cosets = []
    digest = hashlib.sha256()

    for seed in (1, 5):
        # Start at a bad state to count cyclic runs across the original seed.
        x = seed
        for _ in range(period):
            if run_count(x - delta) > cap:
                break
            x = (3 * x) % modulus
        else:
            raise ValueError("a whole odd coset avoids the target")
        anchor = x
        length = 0
        start = None
        coset_maximum = 0
        coset_good = 0
        for _ in range(period):
            x = (3 * x) % modulus
            good = run_count(x - delta) <= cap
            # The digest independently records all good/bad labels, in order.
            digest.update(bytes((int(good),)))
            if good:
                length += 1
                good_count += 1
                coset_good += 1
                if length == 1:
                    start = x
                if length > maximum:
                    maximum, witness = length, start
                coset_maximum = max(coset_maximum, length)
            else:
                length = 0
        require(x == anchor and length == 0, "incomplete cyclic traversal")
        cosets.append({"seed": seed, "bad_anchor": anchor,
                       "period": period, "good_residues": coset_good,
                       "maximum_wait": coset_maximum})

    require(witness is not None, "missing maximum witness")
    residue = witness
    trace = []
    for _ in range(maximum + 1):
        trace.append(run_count(residue - delta))
        residue = (3 * residue) % modulus
    require(all(r <= cap for r in trace[:-1]) and trace[-1] > cap,
            "maximum witness does not replay")
    return {"bits": bits, "cap": cap, "delta": delta,
            "checked_odd_residues": 2 * period,
            "good_residue_count": good_count,
            "maximum_modular_wait": maximum, "witness_residue": witness,
            "witness_run_trace": trace, "cosets": cosets,
            "ordered_good_bad_sha256": digest.hexdigest()}


def build_report(extended: bool) -> dict:
    # No use of XOR boundary count, unlike the separate core implementation.
    for n in range(1 << 16):
        expected = bin(n)[2:].count("01") + int(n > 0)
        require(run_count(n) == expected, "string run count disagrees")
    plans = [(20, cap) for cap in range(1, 7)]
    if extended:
        plans += [(24, cap) for cap in range(5, 9)]
    rows = [certify(bits, cap, delta)
            for bits, cap in plans for delta in (0, 1)]
    return {"schema": "collatz-homogeneous-run-hitting-v1",
            "scope": "all odd positive u, h_R(u,delta) <= modular maximum; delta=0,1",
            "not_claimed": "exact worst ordinary hitting times or unrestricted Collatz",
            "string_definition_checks": 1 << 16,
            "checked_states_including_repeated_cap_scans": sum(
                row["checked_odd_residues"] for row in rows),
            "rows": rows}


def compare(report: dict, reference: dict) -> None:
    require(report == reference, "regenerated modular report differs")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--extended", action="store_true",
                        help="also scan modulus 2^24 for caps 5 through 8")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()
    report = build_report(args.extended)
    if args.compare:
        reference = json.loads(args.compare.read_text(encoding="utf-8"))
        compare(report, reference)
        for key in ("maximum_modular_wait", "witness_residue", "ordered_good_bad_sha256"):
            changed = deepcopy(reference)
            old = changed["rows"][0][key]
            changed["rows"][0][key] = old + 1 if isinstance(old, int) else "corrupted"
            try:
                compare(report, changed)
            except ValueError:
                pass
            else:
                raise ValueError("a corrupted modular certificate was accepted")
    if args.output:
        require(not args.output.exists(), "refusing to overwrite frozen evidence")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n",
                               encoding="utf-8")
    print(json.dumps({"checked_states": report["checked_states_including_repeated_cap_scans"],
                      "maxima": [{"bits": r["bits"], "cap": r["cap"],
                                  "delta": r["delta"], "maximum": r["maximum_modular_wait"]}
                                 for r in report["rows"]]}, sort_keys=True))


if __name__ == "__main__":
    main()
