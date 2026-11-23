#!/usr/bin/env python3
"""Decide a supplied triadic parity dual with a linear ordinary clock.

Mathematical interface: TRIADIC_RIGIDITY.md. This decides the particular
candidate a/3^r for n; it does not select a sufficient r for every n.
The finite ordinary orbit and exact backward equality are both required.
"""

import argparse
from fractions import Fraction
import json


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def backward_dual(orbit):
    """The unique complementary dual of a supplied path ending at 1."""
    if not orbit or orbit[0] <= 0 or orbit[-1] != 1:
        raise ValueError("a positive ordinary path ending at 1 is required")
    if any(step(x) != y for x, y in zip(orbit, orbit[1:])):
        raise ValueError("the supplied path contains an invalid ordinary step")
    value = Fraction(2)
    for x in reversed(orbit[:-1]):
        value = 2 * value if x % 2 else (2 * value - 1) / 3
    return value


def verify_triadic(n, a, r, include_orbit=False):
    """Return whether a/3^r is the exact all-time parity complement of n.

    The reduced exponent may be smaller than r. The strict stopping bound
    is tau < 3(r+1), so at most 3(r+1)-1 ordinary transitions are needed.
    A short matched parity prefix alone is not the acceptance condition.
    """
    if not all(isinstance(v, int) and not isinstance(v, bool) for v in (n, a, r)):
        raise TypeError("n, a and r must be integers")
    if n <= 0 or r < 0:
        raise ValueError("n must be positive and r must be nonnegative")
    clock_bound = 3 * (r + 1)
    orbit = [n]
    while orbit[-1] != 1 and len(orbit) < clock_bound:
        orbit.append(step(orbit[-1]))
    result = {
        "schema": "collatz-triadic-candidate/v1",
        "original_source": n,
        "candidate_numerator": a,
        "candidate_denominator_exponent": r,
        "strict_stopping_bound": clock_bound,
        "ordinary_steps_executed": len(orbit) - 1,
    }
    if orbit[-1] != 1:
        result.update({
            "accepted": False,
            "reason": "The ordinary orbit did not reach 1 before the candidate's necessary stopping bound.",
            "scope": "Rejects this denominator budget; makes no assertion about later convergence.",
        })
    else:
        dual = backward_dual(orbit)
        accepted = a * dual.denominator == dual.numerator * (3 ** r)
        result.update({
            "accepted": accepted,
            "reason": ("Exact backward dual equality verified."
                       if accepted else "The candidate differs from the exact backward dual."),
            "ordinary_stopping_time": len(orbit) - 1,
            "exact_dual_numerator": dual.numerator,
            "exact_dual_denominator": dual.denominator,
            "scope": "A supplied candidate and its original ordinary source only.",
        })
    if include_orbit:
        result["ordinary_orbit"] = orbit
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int, help="positive ordinary source")
    parser.add_argument("a", type=int, help="signed candidate numerator")
    parser.add_argument("r", type=int, help="nonnegative power of three in the candidate denominator")
    parser.add_argument("--include-orbit", action="store_true")
    args = parser.parse_args()
    result = verify_triadic(args.n, args.a, args.r, args.include_orbit)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
