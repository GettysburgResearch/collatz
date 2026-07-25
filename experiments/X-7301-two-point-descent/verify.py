#!/usr/bin/env python3
from __future__ import annotations

import json
import sys

P = 3**12
Q = 2**19
A = tuple(7 * (2 ** (15 - 3 * i)) * (3 ** (2 * i)) for i in range(6))


def ceiling_division(a: int, b: int) -> int:
    return -((-a) // b)


def independent_hits() -> dict[tuple[int, int], list[tuple[int, int, int, int]]]:
    """Independent elimination of u followed by direct enumeration of v."""
    forms: dict[tuple[int, int], list[tuple[int, int, int, int]]] = {}
    for i, ai in enumerate(A):
        for j, aj in enumerate(A):
            coefficient = P * ai - Q * aj
            assert coefficient != 0
            for k, ak in enumerate(A):
                constant = ak * Q

                # 0 < constant + coefficient*v < Q*ai.
                if coefficient > 0:
                    lower = (-constant) // coefficient + 1
                    upper = ceiling_division(Q * ai - constant, coefficient) - 1
                else:
                    lower = (Q * ai - constant) // coefficient + 1
                    upper = ceiling_division(-constant, coefficient) - 1

                for v in range(lower, upper + 1):
                    numerator = ak - v * aj
                    if numerator % ai:
                        continue
                    u = numerator // ai
                    contraction_numerator = u * Q + v * P
                    assert 0 < contraction_numerator < Q
                    forms.setdefault((u, v), []).append(
                        (i, j, k, contraction_numerator)
                    )
    return forms


def main(path: str) -> None:
    with open(path, encoding="utf-8") as source:
        payload = json.load(source)

    assert payload["constants"]["P"] == P
    assert payload["constants"]["Q"] == Q
    assert payload["constants"]["digits"] == list(A)

    forms = independent_hits()
    assert len(forms) == 75

    diagonal = {(t + 1, -t) for t in range(1, 74)}
    assert diagonal.issubset(forms)
    for pair in diagonal:
        assert sorted((i, j, k) for i, j, k, _ in forms[pair]) == [
            (i, i, i) for i in range(6)
        ]

    assert sorted(set(forms) - diagonal) == [(-9, 9), (-8, 8)]
    assert sorted((i, j, k) for i, j, k, _ in forms[(-8, 8)]) == [
        (i, i + 1, i) for i in range(5)
    ]
    assert sorted((i, j, k) for i, j, k, _ in forms[(-9, 9)]) == [
        (i, i + 1, i + 1) for i in range(5)
    ]

    continued_fraction = payload["continued_fraction"]
    assert continued_fraction["P_over_Q"] == [1, 73, 3, 2, 1, 1, 1, 23, 2, 5]
    rows = continued_fraction["convergents"]
    assert rows[1]["allowed_hits"] == [[i, i, i] for i in range(6)]
    assert all(
        not row["allowed_hits"]
        for index, row in enumerate(rows)
        if index != 1
    )

    print("independent X-7301 classification checks passed")


if __name__ == "__main__":
    main(sys.argv[1])
