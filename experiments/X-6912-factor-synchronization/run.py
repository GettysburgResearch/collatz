#!/usr/bin/env python3
"""X-6912: finite regression for complete-factor displacement synchronization.

This is a bounded exact experiment. It does not prove FC* at arbitrary length.
All proof decisions use Python integers.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterator


def factor_prime_powers(n: int) -> list[int]:
    out: list[int] = []
    p = 3
    while p * p <= n:
        if n % p == 0:
            pe = 1
            while n % p == 0:
                n //= p
                pe *= p
            out.append(pe)
        p += 2
    if n > 1:
        out.append(n)
    return out


def crossing_weight(j: int) -> int | None:
    for q in range(j + 1):
        if 3**q < 2**j and 3**q >= 2 ** (j - 1):
            return q
    return None


def words(j: int, q: int) -> Iterator[tuple[str, int]]:
    """Yield valid words and affine numerators by recursive prefix construction."""
    def visit(pos: int, ones: int, numerator: int, prefix: list[str]) -> Iterator[tuple[str, int]]:
        if pos == j - 1:
            if ones == q:
                yield "".join(prefix) + "0", numerator
            return
        for bit in (0, 1):
            new_ones = ones + bit
            next_pos = pos + 1
            if new_ones > q or new_ones + (j - 1 - next_pos) < q:
                continue
            if 3**new_ones < 2**next_pos:
                continue
            new_num = 3 * numerator + 2**pos if bit else numerator
            yield from visit(next_pos, new_ones, new_num, prefix + [str(bit)])
    yield from visit(0, 0, 0, [])


def mechanical_word(j: int, q: int) -> str:
    # Exact ceiling test: ceil(alpha*m) is the least t with 3^t >= 2^m.
    bits: list[str] = []
    ones = 0
    for m in range(1, j):
        target = 0
        while 3**target < 2**m:
            target += 1
        bits.append(str(target - ones))
        ones = target
    assert ones == q
    return "".join(bits) + "0"


def displacement_stats(word: str, mech: str) -> tuple[int, int, int]:
    pv = [i for i, b in enumerate(word) if b == "1"]
    pm = [i for i, b in enumerate(mech) if b == "1"]
    heights = [u - v for v, u in zip(pv, pm)]
    support = sum(h > 0 for h in heights)
    area = sum(heights)
    first = next(i for i, (a, b) in enumerate(zip(word, mech)) if a != b)
    return support, area, first


def build(max_length: int) -> dict:
    rows: list[dict] = []
    first_failure: dict | None = None
    total_words = 0
    nontrivial_failures = 0

    for j in range(2, max_length + 1):
        q = crossing_weight(j)
        if q is None:
            continue
        P, Q = 2**j, 3**q
        D = P - Q
        prime_powers = factor_prime_powers(D) if D > 1 else []
        count = 0
        local_failures: list[dict] = []

        for word, A in words(j, q):
            count += 1
            r = (-A * pow(Q, -1, P)) % P
            if r == 0:
                r = P
            s = (Q * r + A) // P
            displacement = s - r
            if displacement >= 0 and not (j == 2 and r == s == 1):
                nontrivial_failures += 1

            single_witness = False
            local = []
            for F in prime_powers:
                residue = (A * pow(Q, -1, F)) % F
                local.append({"modulus": F, "residue": residue})
                if F * P > A and residue * P >= A:
                    single_witness = True

            if prime_powers and not single_witness:
                block_witness = None
                t = len(prime_powers)
                for mask in range(1, (1 << t) - 1):
                    components = [prime_powers[k] for k in range(t) if (mask >> k) & 1]
                    U = 1
                    for component in components:
                        U *= component
                    residue = (A * pow(Q, -1, U)) % U
                    if U * P > A and residue * P >= A:
                        candidate = {
                            "factor_count": len(components),
                            "components": components,
                            "modulus": U,
                            "residue": residue,
                        }
                        if block_witness is None or (
                            candidate["factor_count"], candidate["modulus"]
                        ) < (
                            block_witness["factor_count"], block_witness["modulus"]
                        ):
                            block_witness = candidate
                mech = mechanical_word(j, q)
                support, area, first = displacement_stats(word, mech)
                local_failures.append(
                    {
                        "word": word,
                        "A": A,
                        "canonical_source": r,
                        "canonical_endpoint": s,
                        "canonical_displacement": displacement,
                        "canonical_descent_defect": r - s,
                        "threshold": {"numerator": A, "denominator": P},
                        "prime_power_residues": local,
                        "first_proper_block_witness": block_witness,
                        "displaced_support": support,
                        "integrated_displacement": area,
                        "first_departure": first,
                    }
                )

        total_words += count
        rows.append(
            {
                "j": j,
                "q": q,
                "D": D,
                "prime_powers": prime_powers,
                "word_count": count,
                "nontrivial_failures": 0,
                "no_single_prime_power_witness": len(local_failures),
            }
        )
        if local_failures and first_failure is None:
            first_failure = {
                "j": j,
                "q": q,
                "D": D,
                "prime_powers": prime_powers,
                "count": len(local_failures),
                "cases": local_failures,
            }

    result = {
        "experiment_id": "X-6912",
        "status": "EXACT FINITE REGRESSION / NOT AN ALL-j PROOF",
        "max_length": max_length,
        "valid_lengths": [row["j"] for row in rows],
        "total_first_crossing_words": total_words,
        "nontrivial_canonical_failures": nontrivial_failures,
        "rows": rows,
        "first_single_prime_power_strategy_failure": first_failure,
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["semantic_sha256"] = hashlib.sha256(payload).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-length", type=int, default=27)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()
    result = build(args.max_length)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.check_results:
        expected = args.check_results.read_text()
        if text != expected:
            raise SystemExit("result mismatch")
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
