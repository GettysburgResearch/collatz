#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from fractions import Fraction

P = 3**12
Q = 2**19
DELTA = P - Q
A = tuple(7 * (2 ** (15 - 3 * i)) * (3 ** (2 * i)) for i in range(6))
A_SET = set(A)


def egcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def solve_triple(ai: int, aj: int, ak: int) -> list[tuple[int, int, int]]:
    """Solve u*ai+v*aj=ak with 0<u*Q+v*P<Q exactly."""
    g, x, y = egcd(ai, aj)
    if ak % g:
        return []

    multiplier = ak // g
    u0 = x * multiplier
    v0 = y * multiplier
    du = aj // g
    dv = -ai // g

    l0 = u0 * Q + v0 * P
    dl = du * Q + dv * P
    assert dl != 0

    if dl > 0:
        lower = (-l0) // dl + 1
        upper = ceil_fraction(Fraction(Q - l0, dl)) - 1
    else:
        lower = (Q - l0) // dl + 1
        upper = ceil_fraction(Fraction(-l0, dl)) - 1

    result: list[tuple[int, int, int]] = []
    for parameter in range(lower, upper + 1):
        u = u0 + du * parameter
        v = v0 + dv * parameter
        contraction_numerator = u * Q + v * P
        assert 0 < contraction_numerator < Q
        assert u * ai + v * aj == ak
        result.append((u, v, contraction_numerator))
    return result


def continued_fraction(value: Fraction) -> list[int]:
    result: list[int] = []
    while value.denominator != 1:
        integer_part = value.numerator // value.denominator
        result.append(integer_part)
        value = 1 / (value - integer_part)
    result.append(value.numerator)
    return result


def convergents(values: list[int]) -> list[tuple[int, int, int]]:
    p_minus_2, p_minus_1 = 0, 1
    q_minus_2, q_minus_1 = 1, 0
    result: list[tuple[int, int, int]] = []
    for value in values:
        p = value * p_minus_1 + p_minus_2
        q = value * q_minus_1 + q_minus_2
        result.append((p, q, p * Q - q * P))
        p_minus_2, p_minus_1 = p_minus_1, p
        q_minus_2, q_minus_1 = q_minus_1, q
    return result


def semantic_digest(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    forms: dict[tuple[int, int], list[tuple[int, int, int, int]]] = defaultdict(list)
    for i, ai in enumerate(A):
        for j, aj in enumerate(A):
            for k, ak in enumerate(A):
                for u, v, contraction_numerator in solve_triple(ai, aj, ak):
                    forms[(u, v)].append((i, j, k, contraction_numerator))

    diagonal: list[dict] = []
    adjacent: list[dict] = []
    other: list[dict] = []
    for (u, v), hits in sorted(forms.items()):
        edges = sorted({(i, j, k) for i, j, k, _ in hits})
        if u + v == 1 and edges == [(i, i, i) for i in range(6)]:
            diagonal.append(
                {
                    "u": u,
                    "v": v,
                    "lambda_numerator": u * Q + v * P,
                }
            )
        elif (u, v) in {(-8, 8), (-9, 9)}:
            adjacent.append({"u": u, "v": v, "edge_outputs": edges})
        else:
            other.append({"u": u, "v": v, "edge_outputs": edges})

    assert len(forms) == 75
    assert {(row["u"], row["v"]) for row in diagonal} == {
        (t + 1, -t) for t in range(1, 74)
    }
    assert len(diagonal) == 73
    assert {(row["u"], row["v"]) for row in adjacent} == {(-8, 8), (-9, 9)}
    assert not other

    cf = continued_fraction(Fraction(P, Q))
    convergent_rows: list[dict] = []
    for p, q, signed_remainder in convergents(cf):
        if signed_remainder > 0:
            hits = [
                (i, j, A.index(p * A[i] - q * A[j]))
                for i in range(6)
                for j in range(6)
                if p * A[i] - q * A[j] in A_SET
            ]
        elif signed_remainder < 0:
            hits = [
                (i, j, A.index(q * A[j] - p * A[i]))
                for i in range(6)
                for j in range(6)
                if q * A[j] - p * A[i] in A_SET
            ]
        else:
            hits = []
        convergent_rows.append(
            {
                "p": p,
                "q": q,
                "signed_remainder": signed_remainder,
                "allowed_hits": hits,
            }
        )

    assert cf == [1, 73, 3, 2, 1, 1, 1, 23, 2, 5]
    assert convergent_rows[1]["allowed_hits"] == [(i, i, i) for i in range(6)]
    assert all(
        not row["allowed_hits"]
        for index, row in enumerate(convergent_rows)
        if index != 1
    )

    payload = {
        "schema_version": 1,
        "experiment_id": "X-7301",
        "status": "EXACT FINITE CLASSIFICATION / NO COUNTEREXAMPLE",
        "constants": {
            "P": P,
            "Q": Q,
            "Delta": DELTA,
            "digits": list(A),
        },
        "contracting_forms": {
            "total": len(forms),
            "diagonal_family_count": len(diagonal),
            "diagonal_parameter_range": [1, 73],
            "diagonal_forms": sorted(diagonal, key=lambda row: row["u"]),
            "adjacent_forms": adjacent,
            "other_forms": other,
        },
        "continued_fraction": {
            "P_over_Q": cf,
            "convergents": convergent_rows,
        },
        "interpretation": {
            "proved": [
                "all integer two-point filters z_n=u*x_n+v*x_(n+1) with 0<u+v*P/Q<1 and at least one legal output digit are classified",
                "the only forms supporting an infinite edge path are the 73 diagonal forms, whose paths are constant-type",
                "the only non-diagonal forms are (-8,8) and (-9,9), supported on the finite adjacent-ascent chain 0->1->...->5",
                "the complete continued-fraction Euclidean ladder has only the 74/73 diagonal hit",
            ],
            "not_proved": [
                "boundedness or divergence of m_n",
                "an ordinary infinite root",
                "a Collatz counterexample",
            ],
        },
    }
    payload["semantic_sha256"] = semantic_digest(payload)
    print(json.dumps(payload, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
