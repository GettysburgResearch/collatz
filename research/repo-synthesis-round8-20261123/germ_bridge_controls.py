#!/usr/bin/env python3
"""Exact finite controls for the center-one scalar criterion.

The actual scalar is computed only for sources explicitly replayed to one.
All checks use integers/fractions and remain active under Python -O.
"""

from collections import Counter
from fractions import Fraction
import json


class Checks:
    def __init__(self):
        self.counts = Counter()

    def require(self, condition, category):
        if not condition:
            raise RuntimeError(category)
        self.counts[category] += 1


def odd_step(q):
    if q <= 0 or q % 2 == 0:
        raise RuntimeError("odd source domain")
    value = 3 * q + 1
    gap = (value & -value).bit_length() - 1
    return value >> gap, gap


def trajectory(q):
    states, gaps = [q], []
    while states[-1] != 1:
        if len(gaps) >= 2000:
            raise RuntimeError("finite orbit replay cap")
        successor, gap = odd_step(states[-1])
        states.append(successor)
        gaps.append(gap)
    return states, gaps


def scalars(gaps):
    values = [Fraction(1)]
    for gap in reversed(gaps):
        values.append((gap + values[-1]) / 3)
    return list(reversed(values))


def ternary_exponent(denominator):
    result = 0
    while denominator % 3 == 0:
        denominator //= 3
        result += 1
    if denominator != 1:
        raise RuntimeError("nontriadic denominator in known convergent scalar")
    return result


def candidate_decision(q, numerator, exponent):
    """Total exact recognizer for a supplied candidate a/3^r.

    Termination within the displayed budget is proved in GERM_BRIDGE.md.
    Rejection does not reject convergence of q.
    """
    if q <= 0 or q % 2 == 0 or exponent < 0:
        raise RuntimeError("invalid candidate input")
    budget = 4 * exponent + 3 * q.bit_length()
    scalar = Fraction(numerator, 3**exponent)
    for clock in range(budget + 1):
        if q == 1:
            return scalar == 1, clock, budget, "standard endpoint"
        if 2 * scalar < 1 or 3 * scalar > q.bit_length() + 3:
            return False, clock, budget, "actual scalar bound failed"
        if clock == budget:
            raise RuntimeError("candidate exceeded its proved finite budget")
        q, gap = odd_step(q)
        scalar = 3 * scalar - gap
    raise RuntimeError("unreachable candidate loop exit")


def run_checks():
    checks = Checks()
    sources = sorted(set(range(1, 256, 2)) |
                     {6171, 77031, 837799} |
                     {(2**(6 * k + 2) - 1) // 3 for k in range(11)})
    ordinary_steps = candidate_tests = max_candidate_steps = 0
    fixtures = []
    for source in sources:
        states, gaps = trajectory(source)
        values = scalars(gaps)
        ordinary_steps += len(gaps)
        initial = values[0]
        exponent = ternary_exponent(initial.denominator)
        checks.require(len(gaps) <= 4 * exponent + 3 * source.bit_length(),
                       "actual stopping time within scalar denominator budget")
        position = 0
        direct_derivative = Fraction(0)
        partial_gap = Fraction(0)
        for i, (q, h) in enumerate(zip(states, values)):
            checks.require(h >= Fraction(1, 2), "unconditional scalar lower")
            checks.require(3 * h <= q.bit_length() + 3,
                           "unconditional exact bitlength upper")
            checks.require(ternary_exponent(h.denominator) == max(exponent - i, 0),
                           "exact scalar denominator clock")
            checks.require(initial == partial_gap + h / 3**i,
                           "same-source exact discounted tail identity")
            checks.require(partial_gap + Fraction(1, 2 * 3**i) <= initial,
                           "finite real enclosure lower")
            checks.require(initial <= partial_gap + Fraction(q.bit_length() + 3, 3**(i + 1)),
                           "finite real enclosure upper")
            checks.require((1 << position) * q <= source * 4**i,
                           "complete actual positive-source clock bound")
            if i < len(gaps):
                successor, gap = odd_step(q)
                checks.require(successor == states[i + 1] and gap == gaps[i],
                               "literal actual odd transition")
                checks.require(values[i + 1] == 3 * h - gap,
                               "actual scalar recurrence")
                direct_derivative += Fraction(position, 3**(i + 1))
                partial_gap += Fraction(gap, 3**(i + 1))
                position += gap
                if h.denominator == 1 and values[i + 1].denominator == 1:
                    h_int, next_int = int(h), int(values[i + 1])
                    potential = Fraction(q - 1, 2**h_int - 1)
                    next_potential = Fraction(successor - 1, 2**next_int - 1)
                    checks.require(next_potential <= Fraction(3, 4) * potential,
                                   "actual integer-stage three-quarter contraction")
                    checks.require(h_int <= q.bit_length() - 1,
                                   "nonterminal integral scalar guard")
                    checks.require(potential >= 1,
                                   "nonterminal integer-stage positive potential")
        direct_derivative += Fraction(position + 1, 2 * 3**len(gaps))
        checks.require(2 * direct_derivative == initial,
                       "independent actual center-one derivative identity")

        candidates = {(initial.numerator, exponent),
                      (initial.numerator - 1, exponent),
                      (initial.numerator + 1, exponent), (0, 0), (-1, 0)}
        for r in range(min(exponent + 1, 5)):
            floor = (initial * 3**r).__floor__()
            candidates.update({(floor, r), (floor + 1, r)})
        for numerator, r in sorted(candidates):
            accepted, used, budget, reason = candidate_decision(source, numerator, r)
            checks.require(accepted == (Fraction(numerator, 3**r) == initial),
                           "finite candidate decision agrees with independent exact scalar")
            checks.require(used <= budget, "candidate decision respects finite budget")
            candidate_tests += 1
            max_candidate_steps = max(max_candidate_steps, used)
        if source in (1, 3, 5, 7, 27, 85, 5461, 837799):
            fixtures.append({"source": source, "h": str(initial),
                             "reduced_ternary_exponent": exponent,
                             "actual_odd_steps_to_one": len(gaps),
                             "candidate_budget": 4 * exponent + 3 * source.bit_length()})

    # This does not assume a candidate scalar is actual.  It separately
    # checks the polynomial contraction on every positive integer candidate
    # in a small range whose literal next charge remains positive.
    algebra_cases = 0
    for q in range(3, 512, 2):
        successor, gap = odd_step(q)
        for h in range(1, 9):
            next_h = 3 * h - gap
            if next_h < 1:
                continue
            checks.require(
                4 * (successor - 1) * (2**h - 1)
                <= 3 * (q - 1) * (2**next_h - 1),
                "literal polynomial contraction for positive integer candidate",
            )
            algebra_cases += 1

    for k in range(11):
        q = (2**(6 * k + 2) - 1) // 3
        states, gaps = trajectory(q)
        checks.require(scalars(gaps)[0] == 2 * k + 1,
                       "explicit integral scalar source family")

    checks.require(Fraction(3, 4)**3 < Fraction(1, 2),
                   "exact three-step binary contraction")
    return {
        "status": "PASS",
        "scope": "exact finite controls on explicitly convergent ordinary sources and supplied candidates",
        "sources": len(sources), "literal_odd_steps": ordinary_steps,
        "candidate_decisions": candidate_tests,
        "maximum_candidate_transitions": max_candidate_steps,
        "additional_polynomial_cases": algebra_cases,
        "exact_checks": sum(checks.counts.values()),
        "checks_by_category": dict(sorted(checks.counts.items())),
        "fixtures": fixtures,
        "unproved": "triadic rationality of the actual center-one derivative for every fixed ordinary source",
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), sort_keys=True, indent=2))
