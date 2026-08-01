#!/usr/bin/env python3
"""Independent verifier for X-6912.

Uses one-bit canonical-pair lifting instead of modular inversion. This is a
bounded regression only, not an all-length theorem.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterator


def factor_prime_powers(n: int) -> list[int]:
    factors: list[int] = []
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            block = 1
            while n % divisor == 0:
                n //= divisor
                block *= divisor
            factors.append(block)
        divisor += 2
    if n > 1:
        factors.append(n)
    return factors


def crossing_weight(j: int) -> int | None:
    candidates = [q for q in range(j + 1) if 3**q < 2**j <= 2 * 3**q]
    return candidates[0] if candidates else None


def traverse(j: int, q: int) -> Iterator[tuple[str, int, int, int]]:
    """Yield word, A, canonical source and endpoint via pair lifting."""
    def dfs(
        pos: int,
        ones: int,
        P: int,
        Q: int,
        source: int,
        endpoint: int,
        prefix: str,
    ) -> Iterator[tuple[str, int, int, int]]:
        if pos == j - 1:
            if ones != q:
                return
            epsilon = endpoint & 1
            z = endpoint + epsilon * Q
            r2 = source + epsilon * P
            s2 = z // 2
            P2 = 2 * P
            A2 = P2 * s2 - Q * r2
            yield prefix + "0", A2, r2, s2
            return
        for bit in (0, 1):
            new_ones = ones + bit
            new_len = pos + 1
            if new_ones > q or new_ones + (j - 1 - new_len) < q:
                continue
            if 3**new_ones < 2**new_len:
                continue
            epsilon = (bit - endpoint) & 1
            z = endpoint + epsilon * Q
            r2 = source + epsilon * P
            s2 = (3 * z + 1) // 2 if bit else z // 2
            yield from dfs(
                pos + 1,
                new_ones,
                2 * P,
                3 * Q if bit else Q,
                r2,
                s2,
                prefix + str(bit),
            )
    yield from dfs(0, 0, 1, 1, 1, 1, "")


def mechanical_word(j: int, q: int) -> str:
    prefix = []
    old = 0
    for m in range(1, j):
        t = 0
        while 3**t < 2**m:
            t += 1
        prefix.append(str(t - old))
        old = t
    assert old == q
    return "".join(prefix) + "0"


def stats(word: str, mech: str) -> tuple[int, int, int]:
    a = [i for i, b in enumerate(word) if b == "1"]
    b = [i for i, c in enumerate(mech) if c == "1"]
    h = [y - x for x, y in zip(a, b)]
    return sum(x > 0 for x in h), sum(h), next(
        i for i, pair in enumerate(zip(word, mech)) if pair[0] != pair[1]
    )


def verify(data: dict) -> None:
    assert data["experiment_id"] == "X-6912"
    max_length = data["max_length"]
    expected_rows = {row["j"]: row for row in data["rows"]}
    first_failure = None
    total = 0
    failures = 0

    for j in range(2, max_length + 1):
        q = crossing_weight(j)
        if q is None:
            continue
        P, Q = 2**j, 3**q
        D = P - Q
        factors = factor_prime_powers(D) if D > 1 else []
        count = 0
        exceptions = []

        for word, A, source, endpoint in traverse(j, q):
            count += 1
            assert P * endpoint == Q * source + A
            displacement = endpoint - source
            if displacement >= 0 and not (j == 2 and source == endpoint == 1):
                failures += 1
            single = []
            local = []
            for F in factors:
                residue = (A * pow(Q, -1, F)) % F
                local.append({"modulus": F, "residue": residue})
                if F * P > A and residue * P >= A:
                    single.append(F)
            if factors and not single:
                best = None
                for mask in range(1, (1 << len(factors)) - 1):
                    components = [
                        factors[k] for k in range(len(factors)) if (mask >> k) & 1
                    ]
                    U = 1
                    for component in components:
                        U *= component
                    residue = (A * pow(Q, -1, U)) % U
                    if U * P > A and residue * P >= A:
                        item = (len(components), U, residue, components)
                        if best is None or item[:2] < best[:2]:
                            best = item
                mech = mechanical_word(j, q)
                support, area, first = stats(word, mech)
                exceptions.append(
                    {
                        "word": word,
                        "A": A,
                        "canonical_source": source,
                        "canonical_endpoint": endpoint,
                        "canonical_displacement": displacement,
                        "canonical_descent_defect": source - endpoint,
                        "threshold": {"numerator": A, "denominator": P},
                        "prime_power_residues": local,
                        "first_proper_block_witness": None if best is None else {
                            "factor_count": best[0],
                            "components": best[3],
                            "modulus": best[1],
                            "residue": best[2],
                        },
                        "displaced_support": support,
                        "integrated_displacement": area,
                        "first_departure": first,
                    }
                )

        total += count
        row = expected_rows[j]
        assert row == {
            "j": j,
            "q": q,
            "D": D,
            "prime_powers": factors,
            "word_count": count,
            "nontrivial_failures": 0,
            "no_single_prime_power_witness": len(exceptions),
        }
        if exceptions and first_failure is None:
            first_failure = {
                "j": j,
                "q": q,
                "D": D,
                "prime_powers": factors,
                "count": len(exceptions),
                "cases": exceptions,
            }

    assert total == data["total_first_crossing_words"]
    assert failures == data["nontrivial_canonical_failures"] == 0
    assert first_failure == data["first_single_prime_power_strategy_failure"]
    copy = dict(data)
    digest = copy.pop("semantic_sha256")
    payload = json.dumps(copy, sort_keys=True, separators=(",", ":")).encode()
    assert hashlib.sha256(payload).hexdigest() == digest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    verify(json.loads(args.result.read_text()))
    print("independent X-6912 verification passed")


if __name__ == "__main__":
    main()
