#!/usr/bin/env python3
"""Decide a supplied odd-denominator rational Collatz parity complement.

Mathematical interface: TRIADIC_CONSTRUCTION.md, Sections 6 and 7.
This decides one candidate. It does not select a successful rational for
every source, and acceptance of a general denominator need not exclude a
nontrivial ordinary cycle. All arithmetic and decisions are exact.
"""

import argparse
from fractions import Fraction
import json


def shortcut(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def verify_rational(n, a, q, strategy="auto", include_trace=False):
    """Recognize a/q = Omega(n), using a proved finite state-clock budget.

    auto uses the specialized triadic stopping bound when available;
    otherwise it chooses the smaller general or mixed bound. general
    holds the reduced denominator fixed. mixed removes each factor of
    three as it is exhausted by the literal compatible pair dynamics.
    """
    if not all(isinstance(v, int) and not isinstance(v, bool) for v in (n, a, q)):
        raise TypeError("n, a and q must be integers")
    if n <= 0 or q <= 0 or q % 2 == 0:
        raise ValueError("n must be positive and q must be positive and odd")
    if strategy not in ("auto", "general", "mixed"):
        raise ValueError("strategy must be auto, general or mixed")

    candidate = Fraction(a, q)
    numerator, denominator = candidate.numerator, candidate.denominator
    r, q0 = 0, denominator
    while q0 % 3 == 0:
        r += 1
        q0 //= 3
    bits_product = (n * max(1, abs(numerator))).bit_length()
    bits_initial = max(1, abs(numerator), denominator).bit_length()
    general_bound = 14 * bits_product + 60 * denominator + 18
    mixed_bound = (14 * n.bit_length() + (15 * r + 14) * bits_initial
                   + 60 * q0 + 18)
    if strategy == "auto":
        mode = "triadic" if q0 == 1 else ("mixed" if mixed_bound < general_bound else "general")
    else:
        mode = strategy
    bound = (3 * (r + 1) if mode == "triadic" else
             mixed_bound if mode == "mixed" else general_bound)

    result = {
        "schema": "collatz-rational-candidate/v1",
        "original_source": n,
        "candidate_numerator": a,
        "candidate_denominator": q,
        "reduced_numerator": numerator,
        "reduced_denominator": denominator,
        "three_exponent": r,
        "residual_denominator": q0,
        "method": mode,
        "state_clock_budget": bound,
        "scope": "Exact recognition of this supplied rational candidate only.",
    }
    x, w, current_q = n, numerator, denominator
    small_seen = {}
    trace = []

    def finish(accepted, event, clock, **extra):
        result.update(accepted=accepted, event=event,
                      ordinary_steps_executed=clock, **extra)
        if include_trace:
            result["paired_trace"] = trace
        return result

    for clock in range(bound):
        if include_trace:
            trace.append({"clock": clock, "ordinary": x,
                          "numerator": w, "denominator": current_q})
        if (x % 2) == (w % 2):
            return finish(False, "parity_mismatch", clock)
        if x == 1:
            return finish(w == 2 * current_q, "ordinary_one_exact_comparison", clock,
                          ordinary_stopping_time=clock)

        # While a three-part is being exhausted, the current denominator
        # changes. The mixed proof starts its visited-value charge only
        # when the residual denominator has been reached.
        recording = mode != "mixed" or current_q % 3 != 0
        if recording and abs(w) <= current_q:
            if w in small_seen:
                old_x, old_clock = small_seen[w]
                equal = x == old_x
                return finish(equal, "repeated_small_numerator", clock,
                              previous_clock=old_clock,
                              previous_ordinary=old_x,
                              repeated_ordinary=x,
                              pair_period=clock - old_clock if equal else None)
            small_seen[w] = (x, clock)

        if clock + 1 == bound:
            break
        x = shortcut(x)
        odd_numerator = bool(w % 2)
        w = (3 * w + current_q) // 2 if odd_numerator else w // 2
        if mode == "mixed" and odd_numerator and current_q % 3 == 0:
            if w % 3:
                raise ArithmeticError("Exact denominator exhaustion failed")
            w //= 3
            current_q //= 3

    if mode == "triadic":
        # An exact reduced triadic dual would have forced the first 1
        # strictly before this clock bound. Finite parity matching alone
        # is not a successful certificate.
        return finish(False, "triadic_stopping_budget_exhausted", bound - 1)
    raise ArithmeticError("Compatible pair exceeded the proved event budget")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int, help="positive ordinary source")
    parser.add_argument("a", type=int, help="signed candidate numerator")
    parser.add_argument("q", type=int, help="positive odd candidate denominator")
    parser.add_argument("--strategy", choices=("auto", "general", "mixed"), default="auto")
    parser.add_argument("--include-trace", action="store_true")
    args = parser.parse_args()
    print(json.dumps(verify_rational(args.n, args.a, args.q,
                                     args.strategy, args.include_trace),
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
