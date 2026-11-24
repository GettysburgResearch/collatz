#!/usr/bin/env python3
"""Exact same-source controls for finite Taylor-jet transport.

All jets are computed only for explicitly replayed sources that reach one.
No finite check is used as a proof of universal rationality or convergence.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb
import json


ORDER = 11
SOURCES = tuple(range(1, 65)) + (85, 6171, 77031, 837799)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def shortcut(value: int) -> int:
    return (3 * value + 1) // 2 if value % 2 else value // 2


def orbit_to_one(source: int) -> list[int]:
    require(source > 0, "source must be a positive ordinary integer")
    states = [source]
    while states[-1] != 1:
        require(len(states) <= 10000, f"replay cap reached for {source}")
        states.append(shortcut(states[-1]))
    return states


def standard_jet(order: int) -> tuple[Fraction, ...]:
    # The literal standard itinerary has B_1(z)=1/(3-z^2).
    coefficients = [Fraction(-1)]
    for j in range(1, order + 1):
        coefficients.append(
            -4 * coefficients[j - 1]
            - (coefficients[j - 2] if j >= 2 else 0)
        )
    return tuple(coefficients)


def source_jets(states: list[int], order: int) -> list[tuple[Fraction, ...]]:
    jets = [standard_jet(order)]
    for value in reversed(states[:-1]):
        tail = jets[-1]
        e = value % 2
        scale = 3**e
        head = [Fraction(e + 2 * tail[0], scale)]
        for j in range(1, order + 1):
            head.append((2 * tail[j] + tail[j - 1]) / scale)
        jets.append(tuple(head))
    return list(reversed(jets))


def ternary_denominator_exponent(value: Fraction) -> int:
    denominator = value.denominator
    exponent = 0
    while denominator % 3 == 0:
        exponent += 1
        denominator //= 3
    require(denominator == 1, "coefficient has a nonternary denominator")
    return exponent


def jet_exponent(jet: tuple[Fraction, ...], order: int) -> int:
    return max(ternary_denominator_exponent(c) for c in jet[: order + 1])


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def direct_carry(bits: list[int], j: int) -> int:
    odd_count = sum(bits)
    prefix_odd = 0
    result = 0
    for k, e in enumerate(bits):
        prefix_odd += e
        result += e * choose(k, j) * 2**k * 3 ** (odd_count - prefix_odd)
    return result


def run_checks() -> dict[str, object]:
    totals = {
        "sources": len(SOURCES),
        "jet_order": ORDER,
        "actual_prefixes": 0,
        "coefficient_prefix_identities": 0,
        "direct_carry_identities": 0,
        "coefficient_step_identities": 0,
        "exact_denominator_clock_checks": 0,
        "integral_tail_coefficients_checked": 0,
        "maximum_shortcut_steps": 0,
        "maximum_initial_ternary_exponent": 0,
    }
    witness_85 = None
    for source in SOURCES:
        states = orbit_to_one(source)
        jets = source_jets(states, ORDER)
        bits = [value % 2 for value in states[:-1]]
        initial_exponents = [jet_exponent(jets[0], r) for r in range(ORDER + 1)]
        totals["maximum_shortcut_steps"] = max(
            totals["maximum_shortcut_steps"], len(bits)
        )
        totals["maximum_initial_ternary_exponent"] = max(
            totals["maximum_initial_ternary_exponent"], initial_exponents[-1]
        )
        if source == 85:
            witness_85 = jets[0][1]
        carries = [0] * (ORDER + 1)
        odd_count = 0
        direct_indices = {0, 1, len(bits) // 2, len(bits)}
        for n, (value, jet) in enumerate(zip(states, jets)):
            totals["actual_prefixes"] += 1
            require(jet[0] == -value, f"wrong actual constant: {source}, {n}")
            require(
                all(c.denominator % 2 for c in jet),
                f"binary integrality failed: {source}, {n}",
            )
            for r in range(ORDER + 1):
                exponent = jet_exponent(jet, r)
                require(
                    exponent == max(initial_exponents[r] - odd_count, 0),
                    f"exact denominator clock failed: {source}, {n}, {r}",
                )
                totals["exact_denominator_clock_checks"] += 1
                if odd_count >= initial_exponents[r]:
                    require(
                        all(c.denominator == 1 for c in jet[: r + 1]),
                        f"integer jet clearing failed: {source}, {n}, {r}",
                    )
                    totals["integral_tail_coefficients_checked"] += r + 1
            for j in range(ORDER + 1):
                left = 2**j * 3**odd_count * jets[0][j] - carries[j]
                right = 2**n * sum(
                    (choose(n, j - i) * 2**i * jet[i] for i in range(j + 1)),
                    Fraction(0),
                )
                require(left == right, f"prefix identity failed: {source}, {n}, {j}")
                totals["coefficient_prefix_identities"] += 1
                if n in direct_indices:
                    require(
                        carries[j] == direct_carry(bits[:n], j),
                        f"direct carry identity failed: {source}, {n}, {j}",
                    )
                    totals["direct_carry_identities"] += 1
            if n < len(bits):
                e = bits[n]
                next_jet = jets[n + 1]
                require(
                    2 * next_jet[0] == 3**e * jet[0] - e,
                    f"constant step identity failed: {source}, {n}",
                )
                totals["coefficient_step_identities"] += 1
                for j in range(1, ORDER + 1):
                    require(
                        2 * next_jet[j] == 3**e * jet[j] - next_jet[j - 1],
                        f"step identity failed: {source}, {n}, {j}",
                    )
                    totals["coefficient_step_identities"] += 1
                for j in range(ORDER + 1):
                    carries[j] = 3**e * carries[j] + e * choose(n, j) * 2**n
                odd_count += e
        require(states[-1] == 1, "source was not explicitly replayed to one")
    require(witness_85 == 0, "the derivative-zero countercontrol changed")
    return {
        "status": "pass",
        "scope": "finite exact replay on explicitly convergent ordinary sources",
        "totals": totals,
        "derivative_zero_countercontrol": {"source": 85, "c1": str(witness_85)},
        "unproved": "rationality of the actual Taylor germ for an arbitrary positive source",
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), sort_keys=True, indent=2))
