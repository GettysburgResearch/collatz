#!/usr/bin/env python3
"""Exact controls for scalar separation and the literature counterexample.

The scalar is evaluated only after a finite literal replay reaches one.
The logarithmic sign is certified by an exact rational lower bound.
"""

from fractions import Fraction
import json

from germ_bridge_controls import Checks, candidate_decision, odd_step, scalars
from germ_bridge_controls import ternary_exponent, trajectory


def run_checks():
    checks = Checks()
    candidate_count = rejection_count = transition_count = 0
    decisions = {"endpoint": 0, "lower": 0, "upper": 0}
    for source in range(1, 256, 2):
        states, gaps = trajectory(source)
        actual = scalars(gaps)
        h0 = actual[0]
        exponent = ternary_exponent(h0.denominator)
        candidates = {(h0.numerator, exponent),
                      (9 * h0.numerator, exponent + 2), (-1, 0)}
        for r in range(7):
            floor = (h0 * 3**r).__floor__()
            candidates.update((a, r) for a in (floor - 1, floor, floor + 1))
        for a, r in sorted(candidates):
            candidate_count += 1
            initial = Fraction(a, 3**r)
            t = initial
            budget = 4 * r + 3 * source.bit_length()
            accepted, used, returned_budget, _ = candidate_decision(source, a, r)
            checks.require(returned_budget == budget, "independent candidate budget")
            checks.require(accepted == (initial == h0), "candidate equality on known ordinary source")
            for clock, q in enumerate(states):
                d = 3**max(r - clock, 0)
                n = t * d
                checks.require(n.denominator == 1, "unreduced candidate lattice")
                checks.require(actual[clock] - t == 3**clock * (h0 - initial),
                               "exact discrepancy transport")
                reason = None
                if q == 1:
                    reason = "endpoint"
                    if t != 1:
                        checks.require(abs(actual[clock] - t) >= Fraction(1, d),
                                       "endpoint mismatch lattice margin")
                elif 2 * t < 1:
                    reason = "lower"
                    checks.require(abs(actual[clock] - t) >= Fraction(1, 2 * d),
                                   "lower rejection lattice margin")
                elif 3 * t > q.bit_length() + 3:
                    reason = "upper"
                    checks.require(abs(actual[clock] - t) >= Fraction(1, 3 * d),
                                   "upper rejection lattice margin")
                if reason is not None:
                    decisions[reason] += 1
                    checks.require(clock == used and clock <= budget,
                                   "independent decision clock agrees")
                    if not accepted:
                        rejection_count += 1
                        checks.require(abs(h0 - initial) >= Fraction(1, 3**(budget + 1)),
                                       "source-specific triadic separation")
                        checks.require(clock + max(r - clock, 0) <= budget,
                                       "transported denominator exponent within budget")
                    break
                checks.require(clock < budget, "decision occurs before exhausted budget")
                successor, gap = odd_step(q)
                checks.require(successor == states[clock + 1] and gap == gaps[clock],
                               "literal source retained in candidate trace")
                t = 3 * t - gap
                transition_count += 1
            else:
                raise RuntimeError("finite trace exhausted without decision")

    states, gaps = trajectory(7)
    checks.require(states == [7, 11, 17, 13, 5, 1] and gaps == [1, 1, 2, 3, 4],
                   "literal literature counterexample orbit")
    alpha = Fraction(1, 4)
    terminal = Fraction(2) / (1 - alpha)
    discounted = [terminal]
    for gap in reversed(gaps):
        discounted.append(gap + alpha * discounted[-1])
    discounted.reverse()
    direct = sum((alpha**i * gap for i, gap in enumerate(gaps)), Fraction())
    direct += alpha**len(gaps) * terminal
    checks.require(discounted[0] == direct == Fraction(553, 384),
                   "complete discounted sum at seven")
    checks.require(discounted[1] == Fraction(169, 96),
                   "complete discounted sum at eleven")
    correction = Fraction(7, 10) * (discounted[1] - discounted[0])
    checks.require(correction == Fraction(287, 1280),
                   "exact literature potential correction")
    positive_lower_bound = Fraction(4, 11) - correction
    checks.require(positive_lower_bound > 0,
                   "strict positive rational lower bound for claimed descent")
    return {
        "status": "PASS",
        "scope": "bounded exact scalar-separation controls and one actual counterexample to an external uniform-descent lemma",
        "sources": 128,
        "candidate_decisions": candidate_count,
        "incorrect_candidates": rejection_count,
        "candidate_trace_transitions": transition_count,
        "decisions_by_kind": decisions,
        "exact_checks": sum(checks.counts.values()),
        "checks_by_category": dict(sorted(checks.counts.items())),
        "literature_counterexample": {
            "source": 7, "successor": 11,
            "discounted_sum_at_source": str(discounted[0]),
            "discounted_sum_at_successor": str(discounted[1]),
            "logarithmic_change": "log(11/7)-287/1280",
            "certified_positive_lower_bound": str(positive_lower_bound),
        },
        "unproved": "a successful triadic approximation satisfying the sufficient precision bound for every ordinary source",
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), sort_keys=True, indent=2))
