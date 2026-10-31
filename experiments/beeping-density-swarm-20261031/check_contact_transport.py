#!/usr/bin/env python3
"""Exact bounded replay of contact-transport claims; not a Collatz solver."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from pathlib import Path


def need(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(label)


def T(n: int) -> int:
    if n < 1:
        raise ValueError("positive integer required")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def v3(n: int) -> int:
    if n <= 0:
        raise ValueError("nonzero absolute value required")
    result = 0
    while n % 3 == 0:
        n //= 3
        result += 1
    return result


def g(d: int) -> int:
    if d == 0:
        raise ValueError("zero displacement omitted")
    return d * d // 3 ** v3(abs(d))


@lru_cache(None)
def gamma(n: int) -> int:
    """Direct full source-only cutoff, without the previous early exit."""
    if n < 1:
        raise ValueError("positive source required")
    if n == 1:
        return 0
    result, state, power = g(n), n, 1
    for _ in range(1, n.bit_length()):
        state, power = T(state), 4 * power
        if state != n:
            result = min(result, power * g(state - n))
    return result


@lru_cache(None)
def phi(n: int) -> int:
    """A horizon based only on the initial Gamma, not the evolving maximum."""
    if n == 1:
        return 0
    initial = gamma(n)
    three, four, state, result = 1, 1, n, initial
    while True:
        result = max(result, (gamma(state) + three - 1) // three)
        if state == 1 or three * (n + 1) ** 2 <= four * initial:
            return result
        state, three, four = T(state), 3 * three, 4 * four


def contact(n: int) -> bool:
    return n >= 2 and phi(n) == gamma(n)


@lru_cache(None)
def arc(x: int) -> tuple[int, ...]:
    if not contact(x):
        raise ValueError("contact source required")
    u = T(x)
    if u == 1 or contact(u):
        return (x, u)
    three = four = 1
    limit = 0
    while four * (phi(u) - 1) <= three * (u + 1) ** 2:
        limit, three, four = limit + 1, 3 * three, 4 * four
    result = [x]
    z = u
    for _ in range(limit + 1):
        result.append(z)
        if z == 1 or contact(z):
            return tuple(result)
        z = T(z)
    raise RuntimeError("proved contact exit clock violated")


def predecessors(n: int) -> tuple[int, ...]:
    result = [2 * n]
    if n % 3 == 2:
        odd = (2 * n - 1) // 3
        if odd > 1:
            result.append(odd)
    return tuple(result)


@lru_cache(None)
def incoming_contacts(n: int) -> tuple[tuple[int, int], ...]:
    """Complete positive-time contact ancestors before another contact."""
    P = phi(n)
    D, power = 0, 1
    while power < P:
        D, power = D + 1, 3 * power
    stack = [(n, 0)]
    leaves = {}
    while stack:
        state, depth = stack.pop()
        for x in predecessors(state):
            d = depth + 1
            need(d <= D, "complete inverse depth bound")
            need(x <= 2 * ((P + 3 ** (d - 1) - 1) // 3 ** (d - 1)),
                 "complete inverse height bound")
            if contact(x):
                need(x not in leaves, "duplicate deterministic ancestor")
                leaves[x] = d
            else:
                need(phi(x) == (phi(state) + 2) // 3 < phi(state),
                     "inverse noncontact Bellman equality")
                stack.append((x, d))
    return tuple(sorted(leaves.items()))


@lru_cache(None)
def lift(n: int) -> F:
    if contact(n):
        return F(1, phi(n))
    return sum((F(1, phi(x)) for x, _ in incoming_contacts(n)), F(0))


def polynomial_square(a: F, b: F, factor: F) -> tuple[F, F, F]:
    return factor * a * a, 2 * factor * a * b, factor * b * b


def evaluate(poly: tuple[F, F, F], n: int) -> F:
    a, b, c = poly
    return a * n * n + b * n + c


def positive_from(poly: tuple[F, F, F], n: int) -> bool:
    a, b, _ = poly
    return a >= 0 and 2 * a * n + b >= 0 and evaluate(poly, n) >= 0


def template_certificate() -> dict:
    result = []
    for base, winning, offset, expected_tau, expected_q, expected_D in (
        (115, 3, 5, 23, 10, 3), (173, 1, 1, 22, 9, 4)
    ):
        state, q, rows, tau, q_tau = base, 0, [], None, None
        for j in range(1, 26):
            q += state % 2
            state = T(state)
            if state == 1 and tau is None:
                tau, q_tau = j, q
            c = F(3 ** q, 2 ** j)
            delta = F(state) - c * base
            valuation = v3(abs(state - base))
            leading = F((3 ** q - 2 ** j) ** 2, 3 ** valuation)
            if j <= 23 and j != winning:
                need(leading >= F(25, 27), "short-prefix leading gap")
                need(abs(c - 1) >= F(1, 8), "short-prefix slope gap")
                need(0 <= delta < 3, "short-prefix offset bound")
            if j == winning:
                actual = polynomial_square(c - 1, delta, F(4 ** j, 3 ** valuation))
                expected = polynomial_square(F(1), F(offset), F(1, 3))
                need(actual == expected, "winning polynomial identity")
            if j >= 24:
                need(state in (1, 2) and c <= F(1, 2) and 0 <= delta <= 2,
                     "eventual template tail bounds")
            rows.append({"j": j, "state": state, "odd_count": q,
                         "displacement_v3": valuation, "slope": str(c),
                         "offset": str(delta), "leading": str(leading)})
        need(tau == expected_tau and q_tau == expected_q, "literal template hitting time")
        D = max(row["displacement_v3"] for row in rows)
        need(D == expected_D, "complete template valuation cap")
        need(v3(base - 1) <= D and v3(base - 2) <= D, "tail valuation cap")
        result.append({"base": base, "first_hit_one": tau, "odd_count_to_one": q_tau,
                       "displacement_v3_cap": D, "winning_prefix": winning,
                       "rows": rows})
    B12 = F(3, 2) ** 8 * (F(1, 3) * F(3, 4) ** 12 + F(1, 81) * F(1, 4) ** 12)
    need(B12 < F(1, 2), "all-long-prefix base inequality")
    need(F(3, 4) ** 5 < F(1, 3), "envelope universal tail bound")

    # Six witness polynomials, reconstructed from the actual first seven states.
    states, slopes, offsets = [115], [F(1)], [F(0)]
    for _ in range(7):
        b, c, d = states[-1], slopes[-1], offsets[-1]
        if b % 2:
            states.append(T(b)); slopes.append(F(3, 2) * c); offsets.append((3 * d + 1) / 2)
        else:
            states.append(T(b)); slopes.append(c / 2); offsets.append(d / 2)
    expected = [
        polynomial_square(F(1), F(5), F(1, 3)),
        polynomial_square(F(1), F(1), F(3, 4)),
        polynomial_square(F(5), F(1), F(1, 16)),
        polynomial_square(F(5), F(1), F(1, 64)),
        polynomial_square(F(1), F(13), F(9, 256)),
        polynomial_square(F(9), F(-11), F(3, 1024)),
    ]
    for j, length in enumerate((3, 1, 3, 3, 3, 2)):
        valuation = v3(abs(states[j + length] - states[j]))
        actual = polynomial_square(slopes[j + length] - slopes[j],
                                   offsets[j + length] - offsets[j],
                                   F(4 ** length, 3 ** valuation))
        need(actual == expected[j], "local envelope witness polynomial")
        need(valuation < 5, "valuation stable on 243-cylinder")
    comparisons = 0
    for root in (0, 1):
        for j in range(1, 5):
            difference = tuple(expected[root][i] - expected[root + j][i] / 3 ** j
                               for i in range(3))
            need(positive_from(difference, 115), "all-n envelope polynomial inequality")
            comparisons += 1
    return {"templates": result, "B12": str(B12),
            "exact_envelope_polynomial_comparisons": comparisons,
            "six_witness_polynomials": [[str(x) for x in p] for p in expected]}


def odd_family() -> dict:
    parameters = list(range(12, 81)) + [96, 128]
    samples = []
    for k in parameters:
        n = 243 * 4 ** k + 115
        y = T(n)
        need(n % 2 == y % 2 == 1 and n % 3 and y % 3, "odd unit family")
        first, second = (n + 5) ** 2 // 3, (y + 1) ** 2 // 3
        need(gamma(n) == phi(n) == first, "exact source rank formula")
        need(gamma(y) == phi(y) == second, "exact endpoint rank formula")
        need(arc(n) == (n, y), "literal one-step contact return")
        need(F(second, first) == F(9, 4) * F(n + 1, n + 5) ** 2,
             "exact amplification formula")
        if k in (12, 16, 32, 64, 128):
            samples.append({"k": k, "source": str(n), "endpoint": str(y),
                            "source_phi": str(first), "endpoint_phi": str(second),
                            "ratio": str(F(second, first))})
    return {"parameters": parameters, "instances": len(parameters), "samples": samples,
            "scope": "bounded replay of the all-k proof, not inference from samples"}


def unbounded_family() -> dict:
    parameters = list(range(10, 65)) + [80, 100, 128]
    samples = []
    largest_clock = 0
    for h in parameters:
        m = 3 ** h
        need(not contact(m), "power-of-three seed noncontact")
        r, x = 1, 2 * m
        while not contact(x):
            r, x = r + 1, 2 * x
            need(3 ** (r - 1) < phi(m), "finite dyadic contact search bound")
        trace = arc(x)
        y, clock = trace[-1], len(trace) - 1
        need(clock >= r + 1 and y > 1, "seed lies before first return")
        need(phi(m) <= 12 ** r * m, "dyadic contact lower-clock inequality")
        need(phi(y) - 1 >= 3 ** r * (2 ** (r - 1) * m - 1), "amplification proof inequality")
        need(3 * 2 ** r * phi(y) > 3 ** r * phi(x), "rank ratio lower bound")
        need(all((z + 1) ** 2 >= m for z in trace), "whole arc escapes any fixed core")
        largest_clock = max(largest_clock, clock)
        if h in (10, 16, 32, 64, 128):
            samples.append({"h": h, "dyadic_depth": r, "return_clock": clock,
                            "source": str(x), "endpoint": str(y),
                            "ratio": str(F(phi(y), phi(x)))})
    return {"parameters": parameters, "instances": len(parameters),
            "largest_checked_return_clock": largest_clock, "samples": samples}


def lift_replay() -> dict:
    target_limit = 48
    source_limit = 2 * max(phi(n) for n in range(2, target_limit + 1))
    forward = defaultdict(F)
    contact_sources = 0
    for x in range(2, source_limit + 1):
        if not contact(x):
            continue
        contact_sources += 1
        trace = arc(x)
        r = len(trace) - 1
        if r > 2:
            need(2 * 4 ** (r - 2) <= 9 * (x + 1) * 3 ** (r - 2),
                 "exact logarithmic return-clock bound")
        for z in trace[:-1]:
            if z <= target_limit:
                forward[z] += F(1, phi(x))
    positive = 0
    pointwise = 0
    for n in range(2, target_limit + 1):
        value = lift(n)
        need(value == forward[n], "complete forward/inverse occupation agreement")
        need(value > 0, "strict positive lift")
        positive += 1
        incoming = sum((lift(p) for p in predecessors(n)), F(0))
        if contact(n):
            row = sum((F(1, phi(x)) for x, _ in incoming_contacts(n)), F(0))
            need(incoming == row, "contact residual agrees with complete row")
        else:
            need(incoming == value, "exact noncontact flow balance")
        pointwise += 1
    return {"target_limit": target_limit, "proved_complete_source_limit": source_limit,
            "contact_sources_traversed": contact_sources,
            "strictly_positive_target_values": positive,
            "pointwise_residual_checks": pointwise,
            "source_cutoff_justification": "every contact ancestor of a target n is <=2 Phi(n)"}


def finite_population_residual() -> dict:
    population = {x: F(1, 2 ** x) for x in range(2, 257) if contact(x)}
    occupation, contact_image = defaultdict(F), defaultdict(F)
    expected_total = F(0)
    visited = 0
    for x, mass in population.items():
        trace = arc(x)
        expected_total += (len(trace) - 1) * mass
        for z in trace[:-1]:
            occupation[z] += mass
            visited += 1
        if trace[-1] > 1:
            contact_image[trace[-1]] += mass
    image = defaultdict(F)
    for n, mass in occupation.items():
        if T(n) > 1:
            image[T(n)] += mass
    support = set(occupation) | set(image) | set(population) | set(contact_image)
    for n in support:
        need(occupation[n] - image[n] == population.get(n, F(0)) - contact_image[n],
             "whole finite-population Poisson residual")
    total = sum(occupation.values(), F(0))
    need(total == expected_total, "exact clock mass identity")
    return {"contact_population": len(population), "literal_arc_visits": visited,
            "residual_support": len(support), "occupation_total": str(total),
            "clock_weight_total": str(expected_total)}


def run() -> dict:
    payload = {"schema": "contact-transport-bounded-replay/v1", "status": "PASS",
               "scope": "exact finite certificates and bounded examples; universal claims rely on the companion proofs; no Collatz or formal-assistant proof",
               "template_certificate": template_certificate(),
               "odd_contact_family": odd_family(),
               "unbounded_return_family": unbounded_family(),
               "occupation_lift": lift_replay(),
               "finite_population": finite_population_residual()}
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return {"payload": payload, "semantic_sha256": hashlib.sha256(canonical).hexdigest()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    p = result["payload"]
    print(json.dumps({"status": "PASS", "semantic_sha256": result["semantic_sha256"],
                      "odd_family_instances": p["odd_contact_family"]["instances"],
                      "unbounded_family_instances": p["unbounded_return_family"]["instances"],
                      "occupation_targets": p["occupation_lift"]["strictly_positive_target_values"],
                      "complete_contact_sources": p["occupation_lift"]["contact_sources_traversed"]}))
