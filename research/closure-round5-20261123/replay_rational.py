#!/usr/bin/env python3
"""Bounded exact checks for the supplied rational-candidate recognizer.

The oracle computes known finite ordinary trajectories to 1 and pulls the
complementary value 2 backward with Fraction arithmetic. It does not reuse
the recognizer's event or clock logic. These checks are finite controls,
not evidence that every original source converges.
"""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json

import verify_rational as recognizer


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def ordinary_oracle(n, step_limit=10000):
    """Independently follow one positive source to 1 within a stated cap."""
    trajectory = [n]
    seen = {n}
    while trajectory[-1] != 1:
        require(len(trajectory) - 1 < step_limit, "oracle step cap exceeded")
        x = trajectory[-1]
        y = (3 * x + 1) // 2 if x % 2 else x // 2
        require(y not in seen, "oracle repeated a state before the first 1")
        trajectory.append(y)
        seen.add(y)
    value = Fraction(2)
    for x in reversed(trajectory[:-1]):
        value = 2 * value if x % 2 else (2 * value - 1) / 3
    return trajectory, value


def pull_back(trajectory, terminal):
    value = Fraction(terminal)
    for x in reversed(trajectory[:-1]):
        value = 2 * value if x % 2 else (2 * value - 1) / 3
    return value


def rational_step(value):
    """Exact rational map, with parity taken after Fraction reduction."""
    return (3 * value + 1) / 2 if value.numerator % 2 else value / 2


def inspect_trace(result, original_trajectory):
    trace = result["paired_trace"]
    require(len(trace) == result["ordinary_steps_executed"] + 1,
            "trace length disagrees with executed transitions")
    require(trace[0]["ordinary"] == result["original_source"],
            "trace changed its original source")
    require(Fraction(trace[0]["numerator"], trace[0]["denominator"]) ==
            Fraction(result["candidate_numerator"], result["candidate_denominator"]),
            "trace changed the supplied rational")
    drops = 0
    edges = 0
    for i, state in enumerate(trace):
        require(state["clock"] == i, "trace skipped a state clock")
        require(state["ordinary"] == original_trajectory[i],
                "trace differs from the independent ordinary trajectory")
        q = state["denominator"]
        require(q > 0 and q % 2 == 1, "trace denominator is not positive odd")
        if i + 1 == len(trace):
            continue
        following = trace[i + 1]
        require(state["ordinary"] % 2 != state["numerator"] % 2,
                "recognizer continued after a failed parity test")
        value = Fraction(state["numerator"], q)
        expected = rational_step(value)
        require(Fraction(following["numerator"], following["denominator"]) == expected,
                "trace rational edge is not the literal map")
        if result["method"] == "mixed" and state["numerator"] % 2 and q % 3 == 0:
            require(following["denominator"] == q // 3,
                    "mixed trace did not remove exactly one denominator factor of three")
            drops += 1
        else:
            require(following["denominator"] == q,
                    "trace changed a fixed denominator or exhausted at the wrong branch")
        edges += 1
    return edges, drops


def run_checks():
    strategies = ("auto", "general", "mixed")
    source_values = list(range(1, 513)) + [6171, 77031, 837799]
    oracles = {n: ordinary_oracle(n) for n in source_values}
    events = Counter()
    methods = Counter()
    decisions = Counter()

    def check_candidate(n, a, q, strategy, with_trace=False):
        trajectory, true_dual = oracles[n]
        expected = Fraction(a, q) == true_dual
        result = recognizer.verify_rational(n, a, q, strategy, with_trace)
        require(result["accepted"] == expected,
                "candidate decision differs from independent backward oracle")
        require(0 <= result["ordinary_steps_executed"] < result["state_clock_budget"],
                "candidate decision exceeded its strict state-clock budget")
        require(Fraction(result["reduced_numerator"], result["reduced_denominator"]) ==
                Fraction(a, q), "normalization changed candidate value")
        require(result["original_source"] == n, "candidate result changed the source")
        events[result["event"]] += 1
        methods[result["method"]] += 1
        decisions["accepted" if result["accepted"] else "rejected"] += 1
        if with_trace:
            return result, inspect_trace(result, trajectory)
        return result

    known_candidate_checks = 0
    for n in source_values:
        _, dual = oracles[n]
        a, q = dual.numerator, dual.denominator
        # Multiplying by 15 tests both removable three- and nonthree-parts.
        # Adding 256 retains eight initial 2-adic bits, unlike a parity flip.
        candidates = ((a, q), (15 * a, 15 * q), (a + 256, q))
        for numerator, denominator in candidates:
            for strategy in strategies:
                check_candidate(n, numerator, denominator, strategy)
                known_candidate_checks += 1

    grid_checks = 0
    for n in range(1, 41):
        for q in range(1, 16, 2):
            for a in range(-16, 17):
                for strategy in strategies:
                    check_candidate(n, a, q, strategy)
                    grid_checks += 1

    pullback_candidates = 0
    pullback_decisions = 0
    pullback_prefix_edges = 0
    paired_trace_edges = 0
    mixed_three_drops = 0
    residual_denominators = set()
    terminals = (Fraction(1, 5), Fraction(-1, 7), Fraction(11, 5))
    for n in (3, 7, 27, 97, 6171):
        trajectory, true_dual = oracles[n]
        tau = len(trajectory) - 1
        prefix_lengths = sorted({1, min(3, tau - 1), min(8, tau - 1), tau // 2})
        for length in prefix_lengths:
            require(0 < length < tau, "selected prefix is not a nonempty proper prefix")
            prefix = trajectory[:length + 1]
            for terminal in terminals:
                candidate = pull_back(prefix, terminal)
                require(candidate != true_dual, "nontriadic terminal unexpectedly became exact")
                q0 = candidate.denominator
                while q0 % 3 == 0:
                    q0 //= 3
                require(q0 > 1, "pullback lost its residual nonthree denominator")
                residual_denominators.add(q0)
                # Check the entire intended prefix independently, even if the
                # recognizer soundly rejects sooner at a repeated numerator.
                value = candidate
                for x in prefix[:-1]:
                    require(x % 2 != value.numerator % 2,
                            "backward pullback did not impose the prescribed opposite parity")
                    value = rational_step(value)
                    pullback_prefix_edges += 1
                require(value == terminal, "backward pullback did not recover its exact terminal")
                pullback_candidates += 1
                for strategy in strategies:
                    _, (edges, drops) = check_candidate(
                        n, candidate.numerator, candidate.denominator,
                        strategy, with_trace=True)
                    paired_trace_edges += edges
                    mixed_three_drops += drops
                    pullback_decisions += 1
    require(mixed_three_drops > 0, "mixed denominator exhaustion was not exercised")
    require(residual_denominators == {5, 7}, "unexpected residual denominator coverage")

    repeated_rejections = []
    for n, a, q in ((3, 0, 1), (10, 1, 1)):
        for strategy in strategies:
            result, (edges, drops) = check_candidate(n, a, q, strategy, with_trace=True)
            require(result["event"] == "repeated_small_numerator" and not result["accepted"],
                    "designated repeated-small rejection was not reached")
            require(result["previous_ordinary"] != result["repeated_ordinary"],
                    "repeated-small rejection did not retain distinct original states")
            paired_trace_edges += edges
            mixed_three_drops += drops
            repeated_rejections.append({
                "source": n, "numerator": a, "denominator": q,
                "strategy": strategy, "event_clock": result["ordinary_steps_executed"],
                "earlier_ordinary": result["previous_ordinary"],
                "later_ordinary": result["repeated_ordinary"],
            })

    invalid_inputs = (
        ((0, 1, 1), {}, ValueError),
        ((-3, 1, 1), {}, ValueError),
        ((3, 1, 0), {}, ValueError),
        ((3, 1, 2), {}, ValueError),
        ((3, 1, -3), {}, ValueError),
        ((True, 1, 1), {}, TypeError),
        ((3, False, 1), {}, TypeError),
        ((3, 1, True), {}, TypeError),
        ((3.0, 1, 1), {}, TypeError),
        ((3, 1.5, 1), {}, TypeError),
        ((3, 1, 3.0), {}, TypeError),
        ((3, 1, 1), {"strategy": "invalid"}, ValueError),
    )
    for args, kwargs, expected_error in invalid_inputs:
        try:
            recognizer.verify_rational(*args, **kwargs)
        except expected_error:
            pass
        else:
            raise RuntimeError("invalid input was accepted")

    large_single_checks = 0
    large_pair_checks = 0
    for q in range(1, 32, 2):
        for x in range(2, 65):
            for w in range(-4 * q - 8, 4 * q + 9):
                if abs(w) <= q or x % 2 == w % 2:
                    continue
                x1 = (3 * x + 1) // 2 if x % 2 else x // 2
                w1 = (3 * w + q) // 2 if w % 2 else w // 2
                v0 = x * max(1, abs(w))
                v1 = x1 * max(1, abs(w1))
                require(w1 != 0 and v1 <= v0, "large single-step nonincrease failed")
                large_single_checks += 1
                if x1 < 2 or abs(w1) <= q or x1 % 2 == w1 % 2:
                    continue
                x2 = (3 * x1 + 1) // 2 if x1 % 2 else x1 // 2
                w2 = (3 * w1 + q) // 2 if w1 % 2 else w1 // 2
                v2 = x2 * max(1, abs(w2))
                require(8 * v2 <= 7 * v0, "uniform two-large-step contraction failed")
                large_pair_checks += 1
    require(large_pair_checks > 0, "no consecutive-large compatible pair was sampled")

    original_one_countercontrols = []
    for q in range(3, 32, 2):
        x0, w0 = 1, 2 * q + 4
        x1, w1 = 2, q + 2
        x2, w2 = 1, 2 * q + 3
        require(x0 % 2 != w0 % 2 and x1 % 2 != w1 % 2,
                "original-one control is not two compatible steps")
        require(w0 > q and w1 > q, "original-one control did not stay large")
        require(2 * w1 == w0 and 2 * w2 == 3 * w1 + q,
                "original-one control uses an incorrect numerator edge")
        require(8 * x2 * w2 > 7 * x0 * w0,
                "original-one control did not refute the unguarded contraction")
        original_one_countercontrols.append({"q": q, "two_step_ratio": str(Fraction(w2, w0))})

    for q in range(1, 65):
        product = Fraction(1)
        for k in range(1, q + 1):
            product *= 1 + Fraction(q, k)
        require(product == comb(2 * q, q), "central binomial charge identity failed")
        require(product ** 2 <= 16 ** q, "signed distinct-value charge bound failed")

    return {
        "schema": "collatz-round5-rational-replay/v1",
        "scope": "bounded exact controls with a separate known-convergent backward oracle",
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "verifier_sha256": sha256(Path(recognizer.__file__).read_bytes()).hexdigest(),
        "oracle_sources": len(source_values),
        "oracle_step_cap": 10000,
        "largest_observed_oracle_stopping_time": max(len(x[0]) - 1 for x in oracles.values()),
        "known_exact_unreduced_perturbed_checks": known_candidate_checks,
        "late_perturbation_numerator_increment": 256,
        "bounded_grid": {"sources": [1, 40], "odd_denominators": [1, 15],
                         "numerators": [-16, 16], "checks": grid_checks},
        "nontriadic_pullbacks": {"candidates": pullback_candidates,
                                 "decisions": pullback_decisions,
                                 "prescribed_prefix_edges": pullback_prefix_edges,
                                 "residual_denominators": sorted(residual_denominators)},
        "paired_trace_edges": paired_trace_edges,
        "mixed_three_exhaustions_checked": mixed_three_drops,
        "repeated_small_rejections": repeated_rejections,
        "invalid_inputs_rejected": len(invalid_inputs),
        "large_single_step_checks": large_single_checks,
        "large_two_step_checks": large_pair_checks,
        "original_one_countercontrols": original_one_countercontrols,
        "central_binomial_product_checks": 64,
        "decision_counts": dict(sorted(decisions.items())),
        "event_counts": dict(sorted(events.items())),
        "method_counts": dict(sorted(methods.items())),
        "nontrivial_ordinary_repeated_pair_acceptance_exercised": False,
        "success": True,
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
