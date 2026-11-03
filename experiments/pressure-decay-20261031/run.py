"""Exact finite regressions for proposed pressure-decay results; not a Collatz proof."""
from __future__ import annotations
import argparse
import hashlib
import json
from bisect import bisect_right
from fractions import Fraction as Q
from pathlib import Path


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def enc(q: Q) -> list[int]:
    return [q.numerator, q.denominator]


def blob(obj: object) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode()


def step(n: int, p: int = 3) -> tuple[int, int]:
    need(type(n) is int and n > 0 and n % 2 == 1, "positive odd source required")
    y = p * n + 1
    a = (y & -y).bit_length() - 1
    return y >> a, a


def trace(n: int) -> dict[int, Q]:
    result: dict[int, Q] = {}
    j = Q(1)
    while n not in result:
        need(len(result) < 10000 and n.bit_length() < 100000, "trace resource cap")
        result[n] = j
        n, a = step(n)
        j *= Q(3, 1 << a)
    need(n == 1, "this finite bank did not close at the known cycle")
    return result


def bank(cutoff: int) -> tuple[dict, list]:
    profile: dict[int, Q] = {}
    boundary: dict[int, Q] = {}
    scales = [1 << k for k in range(17)]
    path_checks = 0
    odd_records = 0
    for x in range(1, cutoff + 1, 2):
        path = trace(x)
        ordered = sorted(path)
        for y in scales:
            count = bisect_right(ordered, y)
            need(count**40 <= 5**40 * y**39, "finite-path packing regression")
            path_checks += 1
        for t, j in path.items():
            profile[t] = profile.get(t, Q(0)) + j * j
            need(j * x <= t, "first-hit upper weight")
            value = path[1] / j
            need(t not in boundary or boundary[t] == value, "inconsistent target-one weight")
            boundary[t] = value
            odd_records += 1
    edge_checks = 0
    for n, value in boundary.items():
        endpoint, a = step(n)
        residual = value - Q(3, 1 << a) * boundary[endpoint]
        need(residual == (Q(1, 4) if n == 1 else 0), "Dirichlet/eigenvector distinction")
        edge_checks += 1
    rows = [[t, *enc(value)] for t, value in sorted(profile.items())]
    means = []
    precision = 1 << 60
    for y in scales:
        selected = [(t, h) for t, h in profile.items() if t <= y]
        low = sum((h * precision // (t * t)) for t, h in selected)
        upper = Q(low + len(selected), precision)
        need((4 * upper)**40 <= 25**40 * y**39, "mean-bound regression")
        means.append([y, low, len(selected)])
    return {
        "cutoff": cutoff, "sources": (cutoff + 1) // 2,
        "odd_records": odd_records, "profile_entries": len(rows),
        "max_target": max(profile), "packing_checks": path_checks,
        "dirichlet_edges": edge_checks, "root_residual": [1, 4],
        "profile_sha256": hashlib.sha256(blob(rows)).hexdigest(),
        "mean_floor_bits": 60, "mean_rows": means,
        "uniform_missing_source_error": [1, 2 * (cutoff + 1)],
    }, rows


def shadows() -> tuple[list, list]:
    simple = []
    for m in range(1, 33):
        for k in range(1, 25):
            source = 2 * m * 2**k - 1
            target = 2 * m * 3**k - 1
            n = source
            for _ in range(k):
                n, a = step(n)
                need(a == 1, "shadow valuation")
            need(n == target, "shadow endpoint")
            simple.append([m, k, source, target, 3**k, 2**k])
    powers = []
    for m in range(1, 33):
        for k in (1, 2, 4):
            for p, d in ((0, 1), (1, 2), (1, 1), (3, 2), (7, 4), (15, 8)):
                for u in range(1, 16385):
                    x, t = 2 * m * u * 2**k - 1, 2 * m * u * 3**k - 1
                    if 9**(k*d) * x**p > 4**(k*d) * t**p:
                        powers.append([m, k, p, d, u, x, t])
                        break
                else:
                    raise ValueError("power-witness resource cap")
    return simple, powers


def norm_tests() -> list:
    rows = []
    for seed in range(1, 33):
        total = Q(0)
        partial = Q(0)
        tail = Q(0)
        for t in range(1, 128, 2):
            f = Q((seed * 37 + t * 11) % 19 - 9, 7)
            coefficient = (Q(0), Q(3, 5), Q(12, 5))[t % 3]
            total += coefficient * f * f
            if t % 3:
                start = 2 if t % 3 == 1 else 1
                for a in range(start, 19, 2):
                    x = ((1 << a) * t - 1) // 3
                    endpoint, actual = step(x)
                    need((endpoint, actual) == (t, a), "inverse branch replay")
                    partial += Q(9, 4**a) * f * f
                first = 20 if start == 2 else 19
                tail += Q(9 * 16, 15 * 4**first) * f * f
        need(total == partial + tail, "infinite-preimage norm identity")
        rows.append([seed, enc(total), enc(partial), enc(tail)])
    return rows


def controls() -> dict:
    toys = []
    for r in range(1, 81):
        t = 2**r - 1
        value = sum((Q(4**j, t*t) for j in range(r)), Q(0))
        need(value == Q(4**r - 1, 3*t*t), "toy pressure")
        toys.append([r, *enc(value)])
    cycles = []
    for p, orbit in ((3, [1]), (5, [13, 33, 83])):
        derivative = Q(1)
        for i, n in enumerate(orbit):
            endpoint, a = step(n, p)
            need(endpoint == orbit[(i+1) % len(orbit)], "cycle endpoint")
            derivative *= Q(p, 1 << a)
        need(0 < derivative < 1, "positive-cycle discount")
        cycles.append([p, orbit, enc(derivative)])
    return {"toy": toys, "cycles": cycles}



def energy() -> dict:
    """Finite-clock exact arithmetic; dyadic enclosures avoid huge common denominators."""
    cutoff, horizon, bits = 4095, 40, 80
    precision = 1 << bits
    states = list(range(1, cutoff + 1, 2))
    weights = [Q(1) for _ in states]  # J_q^2
    seen_one = [n == 1 for n in states]
    maximum = cutoff
    rows = []
    previous_low = None
    spike = None
    for clock in range(horizon + 1):
        populations: dict[int, Q] = {}
        e_low = 0
        for index, (t, weight) in enumerate(zip(states, weights)):
            e_low += (weight * precision // (t * t))
            populations[t] = populations.get(t, Q(0)) + weight
            if clock == 32 and index == 13:
                need(t == 3077, "source-27 moment endpoint")
                # J is positive; the stored square suffices for the moment lower bound.
                lower = weight * weight / (t * t)
                need(lower > 13, "source-27 moment excursion")
                spike = [27, clock, t, enc(weight), enc(lower)]
        s_low = sum((weight * weight * precision // (t * t))
                    for t, weight in populations.items())
        e_upper = Q(e_low + len(states), precision)
        s_upper = Q(s_low + len(populations), precision)
        if previous_low is not None:
            need(e_upper < Q(previous_low, precision), "finite-clock energy decrease")
        previous_low = e_low
        theta = e_upper + Q(1, 2 * (cutoff + 1))
        moment_upper = 2 * s_upper + Q(12, 5)**clock / (cutoff + 1)
        rows.append([clock, e_low, s_low, len(populations), maximum,
                     sum(not done for done in seen_one), enc(theta), enc(moment_upper)])
        if clock == horizon:
            break
        for index, t in enumerate(states):
            endpoint, a = step(t)
            old = weights[index] / (t*t)
            new_weight = weights[index] * Q(9, 4**a)
            new = new_weight / (endpoint*endpoint)
            loss = weights[index] * Q(6*t+1, t*t*(3*t+1)**2)
            need(old - new == loss > 0, "exact energy decrement")
            weights[index] = new_weight
            states[index] = endpoint
            seen_one[index] |= endpoint == 1
            maximum = max(maximum, endpoint)
    need(spike is not None, "moment excursion inventory")
    return {"cutoff": cutoff, "horizon": horizon, "dyadic_bits": bits,
            "source_count": len(states), "rows": rows, "spike": spike,
            "decrement_checks": len(states)*horizon}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    summary, profile = bank(4095)
    simple, powers = shadows()
    result = {
        "schema": "pressure-decay-20261031/v2", "status": "FINITE_REGRESSIONS_ONLY",
        "parent": "6bee3183ff7f29f2e20ca88ab94bc7745c1af602",
        "bank": summary, "shadows": simple, "power_barriers": powers,
        "norms": norm_tests(), "controls": controls(), "energy": energy(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(blob(result))
    args.output.with_suffix(args.output.suffix + ".profile.json").write_bytes(blob(profile))
    print(json.dumps({"status": "PASS", "checks_sha256": hashlib.sha256(blob(result)).hexdigest(),
                      "bank": summary, "shadow_rows": len(simple), "power_rows": len(powers), "energy_clocks": len(result["energy"]["rows"])}, sort_keys=True))


if __name__ == "__main__":
    main()
