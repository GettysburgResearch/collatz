#!/usr/bin/env python3
"""Exact source-persistent entropy and saturated-capacity checks.

Map and outward logarithm arithmetic adapt the author's PR157 checker at
64361ecca770092d6c8242dc6211e38818af2e50; this is not an independent replay
of that prior program. New finite claims are in occupation.md.
No floating-point verification gates, external packages, or convergence
assumption are used. Uncomputed ORIGINAL sources have explicit tail bounds.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from functools import cache
from hashlib import sha256
from math import gcd
from pathlib import Path
import json


S = 10**30
STATS = defaultdict(int)


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def up(a, b):
    need(b > 0, "positive denominator required")
    return -((-a) // b)


def val(n, p):
    n = abs(n)
    need(n > 0, "zero valuation")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


@cache
def rank(n):
    if n == 1:
        return 0
    h = val(2 * n + 1, 3)
    modes = (0, 1, 2, h) if h >= 3 else (0, 1, 2)
    result = []
    for a in modes:
        z = (3**a - 2**(a + 1)) * n + 3**a - 2**a
        result.append(z * z // 3 ** val(z, 3))
    answer = min(result)
    need(n - 1 <= answer <= n * n, "rank bounds failed")
    return answer


@cache
def accel(n):
    if n == 1:
        return 1
    a = 0 if n % 2 == 0 else val(n + 1, 2)
    d, c = 3**a - 2**(a + 1), 3**a - 2**a
    z = d * n + c
    k = val(z, 2) // (a + 1)
    need(k >= 1, "empty acceleration")
    numerator, denominator = z * 3 ** (a * k), 2 ** ((a + 1) * k)
    need(numerator % denominator == 0, "A affine division")
    zz = numerator // denominator
    need((zz - c) % d == 0, "A endpoint division")
    result = (zz - c) // d
    actual = n
    for _ in range(k):
        for position in range(a + 1):
            odd = position < a
            need(bool(actual & 1) == odd, "A physical parity")
            actual = (3 * actual + 1) // 2 if odd else actual // 2
            STATS["physical_shortcut_edges"] += 1
            STATS["maximum_physical_state"] = max(STATS["maximum_physical_state"], actual)
    need(actual == result, "A physical endpoint")
    STATS["physically_replayed_A_words"] += 1
    return result


@cache
def unsafe(n):
    return n > 1 and 4 * rank(accel(n)) > rank(n)


@cache
def ret(n):
    if n == 1:
        return 1
    need(unsafe(n), "B source is not unsafe")
    current = accel(n)
    while current > 1 and not unsafe(current):
        following = accel(current)
        need(4 * rank(following) <= rank(current), "safe step rank drop")
        current = following
        STATS["safe_A_steps_inside_B"] += 1
    if current > 1:
        need(rank(current) + 6 <= (rank(n) + 6) ** 6, "return height budget")
    STATS["actual_B_edges"] += 1
    return current


def times(x, y):
    need(x[0] >= 0 and y[0] >= 0, "positive interval multiplication")
    return x[0] * y[0] // S, up(x[1] * y[1], S)


def log_unit(n, d):
    need(0 <= 3 * n <= d, "atanh normalization")
    z = S * n // d, up(S * n, d)
    z2, power = times(z, z), z
    lo = hi = 0
    for r in range(32):
        lo += power[0] // (2 * r + 1)
        hi += up(power[1], 2 * r + 1)
        power = times(power, z2)
    return 2 * lo, 2 * hi + up(9 * S, 4 * 65 * 3**65)


LN2 = log_unit(1, 3)


def logarithm(a, b=1):
    need(a > 0 and b > 0, "logarithm domain")
    k = a.bit_length() - b.bit_length()
    below = a < (b << k) if k >= 0 else (a << (-k)) < b
    if below:
        k -= 1
    n, d = (a, b << k) if k >= 0 else (a << (-k), b)
    need(d <= n < 2 * d, "logarithm range")
    lo, hi = log_unit(n - d, n + d)
    return (lo + k * LN2[0], hi + k * LN2[1]) if k >= 0 else (lo + k * LN2[1], hi + k * LN2[0])


@cache
def psi_rank(r):
    inner = logarithm(r + 6)
    return S + logarithm(inner[0], S)[0], S + logarithm(inner[1], S)[1]


@cache
def reciprocal_psi(n):
    lo, hi = psi_rank(rank(n))
    need(lo > 0, "positive psi")
    return S * S // hi, up(S * S, lo)


def entropy_atom_at(x):
    if x == 0:
        return 0, 0
    lo, hi = logarithm(x, S)
    need(hi < 0, "entropy mass must be below one")
    return x * (-hi) // S, up(x * (-lo), S)


def entropy(masses):
    lo = hi = 0
    for a, b in masses.values():
        need(0 <= a <= b and 3 * b < S, "entropy monotonicity domain")
        lo += entropy_atom_at(a)[0]
        hi += entropy_atom_at(b)[1]
    return lo, hi


def decimal(n, places=12):
    sign = "-" if n < 0 else ""
    n = abs(n)
    base = 10**places
    return f"{sign}{n // base}.{n % base:0{places}d}"


def record(interval, denominator=S):
    a, b = interval
    return {"decimal_enclosure": [decimal(a * 10**12 // denominator),
                                  decimal(up(b * 10**12, denominator))],
            "lower_numerator": str(a), "upper_numerator": str(b),
            "denominator": str(denominator)}


def information_check(starts, masses, clock):
    total_lo = total_hi = 0
    for u in starts:
        current = u
        for _ in range(clock):
            current = ret(current)
        mass = masses[current]
        denominator = u * (u + 1)
        log_lo = logarithm(mass[0] * denominator, S)[0]
        log_hi = logarithm(mass[1] * denominator, S)[1]
        need(log_hi >= 0, "carrier contains its original atom")
        value = times((S // denominator, up(S, denominator)), (max(0, log_lo), log_hi))
        total_lo += value[0]
        total_hi += value[1]
    return total_lo, total_hi


def entropy_run(cutoff, horizon):
    starts = [n for n in range(2, cutoff + 1) if unsafe(n)]
    initial = {n: (S // (n * (n + 1)), up(S, n * (n + 1))) for n in starts}
    mass_lo = sum(a for a, _ in initial.values())
    mass_hi = sum(b for _, b in initial.values())
    mass_tail = up(S, cutoff + 1)
    need(3 * (mass_hi + mass_tail) < S and logarithm(3)[0] > S,
         "full source entropy monotonicity certificate")
    tail_entropy = up(2 * (logarithm(cutoff + 2)[1] + S), cutoff + 1)
    star = psi_rank(1)
    one_charge_tail = up(S * S, (cutoff + 1) * star[0])
    s0 = entropy(initial)
    budget_upper = s0[1] + tail_entropy - entropy_atom_at(mass_lo)[0]
    masses, old_entropy = initial, s0
    cumulative = (0, 0)
    rows = []
    info = None
    for j in range(horizon):
        charge_lo = charge_hi = 0
        following = {}
        for n, weight in masses.items():
            if n > 1:
                lo, hi = times(weight, reciprocal_psi(n))
                charge_lo += lo
                charge_hi += hi
            y = ret(n)
            a, b = following.get(y, (0, 0))
            following[y] = a + weight[0], b + weight[1]
        next_entropy = entropy(following)
        finite_drop = old_entropy[0] - next_entropy[1], old_entropy[1] - next_entropy[0]
        full_drop = max(0, finite_drop[0] - tail_entropy), finite_drop[1] + tail_entropy
        gap = charge_lo - full_drop[1], charge_hi + one_charge_tail - full_drop[0]
        cumulative = cumulative[0] + charge_lo, cumulative[1] + charge_hi
        if j in (0, 1, 2, 4, 8, 9, horizon - 1):
            rows.append({"return_index": j,
                         "whole_source_reciprocal_psi_charge": record((charge_lo, charge_hi + one_charge_tail)),
                         "whole_source_entropy_drop": record(full_drop),
                         "charge_minus_entropy_drop": record(gap),
                         "finite_carriers_including_cemetery": len(masses)})
        if j == 8:
            need(gap[0] > 0, "whole-source unit-price obstruction not certified")
            direct = information_check(starts, following, 9)
            difference = s0[0] - next_entropy[1], s0[1] - next_entropy[0]
            need(max(direct[0], difference[0]) <= min(direct[1], difference[1]),
                 "finite information/entropy identity mismatch")
            info = {"original_atoms": len(starts), "return_clock": 9,
                    "direct_source_information": record(direct),
                    "entropy_difference": record(difference), "intervals_overlap": True}
        masses, old_entropy = following, next_entropy
    mixture_controls = []
    need(unsafe(3) and ret(3) == 1, "actual one-atom full-support control")
    for coefficient in (1, 10, 100, 1000):
        k = coefficient.bit_length() + 16
        power = 2**k
        # H(normalized f0)<48; h(epsilon)<=epsilon(log(1/epsilon)+1).
        entropy_upper = up(k * LN2[1] + 49 * S, power)
        charge_lower = (power - 1) * S * S // (power * psi_rank(rank(3))[1])
        gap = charge_lower - coefficient * entropy_upper
        need(gap > 0, "full-support input entropy control failed")
        mixture_controls.append({"coefficient": coefficient, "epsilon": f"1/{power}",
                                 "charge_minus_scaled_entropy_lower": record((gap, gap))})
    return {"original_source_cutoff": cutoff, "unsafe_original_sources": len(starts),
            "return_horizon": horizon, "whole_source_initial_mass": record((mass_lo, mass_hi + mass_tail)),
            "whole_source_initial_entropy": record((s0[0], s0[1] + tail_entropy)),
            "omitted_original_source_entropy_upper": record((0, tail_entropy)),
            "all_time_total_coalescence_information_upper": record((0, budget_upper)),
            "whole_source_finite_G": record((cumulative[0], cumulative[1] + horizon * one_charge_tail)),
            "rows": rows, "finite_information_identity": info,
            "other_full_support_input_controls": mixture_controls}


def capacity_run(cutoff, horizon):
    denominator = 1
    for n in range(2, cutoff + 2):
        denominator = denominator // gcd(denominator, n) * n
    need(denominator % (cutoff + 1) == 0, "capacity tail denominator")
    starts = [n for n in range(2, cutoff + 1) if unsafe(n)]
    initial = {u: denominator // (u * (u + 1)) for u in starts}
    for u, weight in initial.items():
        need(weight * u * (u + 1) == denominator, "exact initial atom denominator")
    capacity = defaultdict(int)
    unresolved = cycles = longest = visits = 0
    for u, weight in initial.items():
        current, seen = u, set()
        for _ in range(horizon):
            if current == 1 or current in seen:
                break
            seen.add(current)
            capacity[current] += weight
            visits += 1
            current = ret(current)
        longest = max(longest, len(seen))
        if current == 1:
            pass
        elif current in seen:
            cycles += 1
        else:
            unresolved += weight
    error = unresolved + denominator // (cutoff + 1)
    need(unresolved == 0 and cycles == 0, "default finite capacity source scope changed")
    incoming = defaultdict(int)
    incoming_powers = {p: defaultdict(int) for p in (2, 3, 4)}
    for x, value in capacity.items():
        y = ret(x)
        if y > 1:
            incoming[y] += value
            for p in incoming_powers:
                incoming_powers[p][y] += value**p
    flow_checks = power_checks = 0
    for y, value in capacity.items():
        need(value == initial.get(y, 0) + incoming[y], "exact first-hit flow identity")
        flow_checks += 1
        for p, values in incoming_powers.items():
            need(values[y] <= value**p, "convex capacity supersolution")
            if y in initial:
                need(values[y] < value**p, "strict source convexity")
            power_checks += 1
    x, y = 31, 121
    need(ret(x) == y and rank(x) == 144 and rank(y) == 1764, "known-convergent witness edge")
    lower_x, upper_y = capacity[x], capacity[y] + error
    need(lower_x**2 * y > upper_y**2 * x, "all-s weighted capacity failure")
    need(lower_x**5 * denominator**2 > 5000 * upper_y**7,
         "all-c compactified capacity failure")
    witness_path, current = [], x
    while current != 1:
        need(current not in witness_path, "witness unexpectedly cycles")
        witness_path.append(current)
        current = ret(current)
    witness_path.append(1)
    # A finite positive Poisson repair on the certified path starting at 121.
    # Its coefficient 150 dominates total mass of w_1=A(y)/y by OCC-003.
    patch = {n: 150 for n in witness_path[1:-1]}
    patch_defect = dict(patch)
    for n, value in patch.items():
        endpoint = ret(n)
        if endpoint > 1:
            patch_defect[endpoint] = patch_defect.get(endpoint, 0) - value
    need({n: value for n, value in patch_defect.items() if value} == {121: 150},
         "finite positive Poisson repair")
    bound_x = Fraction(capacity[x], denominator), Fraction(capacity[x] + error, denominator)
    bound_y = Fraction(capacity[y], denominator), Fraction(capacity[y] + error, denominator)

    def rational_pair(bounds):
        return {"lower": f"{bounds[0].numerator}/{bounds[0].denominator}",
                "upper": f"{bounds[1].numerator}/{bounds[1].denominator}",
                "decimal_enclosure": [decimal(bounds[0].numerator * 10**12 // bounds[0].denominator),
                                      decimal(up(bounds[1].numerator * 10**12, bounds[1].denominator))]}

    return {"original_source_cutoff": cutoff, "return_horizon": horizon,
            "unsafe_original_sources": len(starts), "complete_distinct_state_carrier": len(capacity),
            "first_hit_visits": visits, "longest_source_path": longest,
            "unresolved_original_mass_numerator": str(unresolved), "detected_cycle_sources": cycles,
            "common_denominator_bitlength": denominator.bit_length(),
            "exact_flow_identities": flow_checks, "exact_convex_power_checks": power_checks,
            "uniform_whole_source_capacity_error": f"1/{cutoff + 1}",
            "finite_positive_repair": {"defect_source": 121, "defect_coefficient": 150,
                                       "support_size": len(patch), "total_mass": sum(patch.values()),
                                       "I_minus_H_patch_equals_150_delta_121": True},
            "witness": {"source": x, "endpoint": y, "known_convergent_B_path": witness_path,
                        "source_capacity": rational_pair(bound_x), "endpoint_capacity": rational_pair(bound_y),
                        "A_source_squared_times_endpoint_exceeds_A_endpoint_squared_times_source": True,
                        "A_source_power5_over_A_endpoint_power7_exceeds": 5000,
                        "weighted_family_failure_range": "every real s>=1/2",
                        "bitlength_power_family_failure_range": "every real c>1"}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entropy-cutoff", type=int, default=65536)
    parser.add_argument("--entropy-returns", type=int, default=16)
    parser.add_argument("--capacity-cutoff", type=int, default=8192)
    parser.add_argument("--capacity-returns", type=int, default=64)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--compare", type=Path)
    args = parser.parse_args()
    need(args.entropy_returns >= 9 and args.capacity_returns >= 1, "declared return scope")
    entropy_result = entropy_run(args.entropy_cutoff, args.entropy_returns)
    capacity_result = capacity_run(args.capacity_cutoff, args.capacity_returns)
    report = {"status": "PASS", "schema": "creative-occupation-v1",
              "claims": ["OCC-001", "OCC-002", "OCC-003", "OCC-004"],
              "source_pins": {"main": "ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a",
                              "PR152": "2391a9c1e4a7f77233b951d2eb6da92e76652e7c",
                              "PR153": "eb04a5d79020cefa0ba46794095b5766c5ff66a4",
                              "PR157": "64361ecca770092d6c8242dc6211e38818af2e50"},
              "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "entropy": entropy_result, "capacity": capacity_result,
              "physical_replay": dict(sorted(STATS.items())),
              "limits": ["All-time coalescence budget does not upper-bound reciprocal-psi occupation without a new arithmetic estimate.",
                         "Saturated capacity counts each original source at most once at an endpoint; it is not time occupation.",
                         "First-hit flow supersolutions are stated off periodic states.",
                         "Both candidate-weight failures include every omitted original source analytically.",
                         "No global Collatz conclusion, all-time orbit witness, or asymptotic extrapolation is claimed."]}
    if args.compare:
        need(json.loads(args.compare.read_text(encoding="utf-8")) == report, "frozen report mismatch")
    if args.output:
        args.output.write_text(json.dumps(report, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "entropy_sources": entropy_result["unsafe_original_sources"],
                      "capacity_sources": capacity_result["unsafe_original_sources"],
                      "flow_identities": capacity_result["exact_flow_identities"],
                      "convex_power_checks": capacity_result["exact_convex_power_checks"],
                      "actual_B_edges": STATS["actual_B_edges"]}, sort_keys=True))


if __name__ == "__main__":
    main()
