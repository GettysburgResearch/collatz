"""Finite coefficient, rank/module, and transported-population research adapters.

Definitions pinned to research/integrated/CONVENTIONS.md and pass4/
MOVING_GHOST_RANK.md at ab7a62c. No monotonicity, return-control, or coverage
conjecture is treated as an invariant. All experiment sources are positive.
"""
from __future__ import annotations

from collections import Counter

try:
    from .core import Budget, Cancelled, TimedOut, bounded_int, parse_integer, orbit, valuation2, plot_log2
    from .pairs import fields
except ImportError:
    from core import Budget, Cancelled, TimedOut, bounded_int, parse_integer, orbit, valuation2, plot_log2
    from pairs import fields

RANK_SOURCE = "research/astra-three-routes/pass4/MOVING_GHOST_RANK.md"


def v3(n: int) -> int:
    n = abs(n)
    if n == 0:
        raise ValueError("v3(0) is not a finite integer.")
    exponent = 0
    while n % 3 == 0:
        n //= 3
        exponent += 1
    return exponent


def component(n: int, a: int) -> int:
    z = 3 ** a * (n + 1) - 2 ** a * (2 * n + 1)
    return z * z // 3 ** v3(z) if z else 0


def ranks(n: int) -> dict:
    if n <= 0:
        raise ValueError("Ranks require a positive integer.")
    h = v3(2 * n + 1)
    indices = [0, 1, 2] + ([h] if h >= 3 else [])
    values = [(a, component(n, a)) for a in indices]
    moving = min(v for _, v in values)
    section = (2 * n + 1) ** 2 // 3 ** h
    return {"moving": str(moving), "section": str(section), "h": h,
            "minimizers": [a for a, v in values if v == moving],
            "components": [{"a": a, "value": str(v)} for a, v in values]}


def module_step(n: int) -> dict:
    """Exact maximal (1^a 0)^k module. Absorbed 1 has zero elapsed clocks."""
    if n == 1:
        return {"endpoint": 1, "a": None, "k": 0, "shortcut_cost": 0, "raw_cost": 0}
    if n < 1:
        raise ValueError("Module source must be positive.")
    a = valuation2(n + 1) if n & 1 else 0
    q, p = 3 ** a, 2 ** (a + 1)
    d, c = q - p, q - 2 ** a
    z = d * n + c
    k = valuation2(abs(z)) // (a + 1)
    new_z = q ** k * (z // p ** k)
    numerator = new_z - c
    if k < 1 or numerator % d:
        raise ArithmeticError("Module integrality check failed.")
    endpoint = numerator // d
    if endpoint <= 0:
        raise ArithmeticError("Module positivity check failed.")
    return {"endpoint": endpoint, "a": a, "k": k,
            "shortcut_cost": k * (a + 1), "raw_cost": k * (2 * a + 1)}


def module_trace(seed: int, count: int, max_bits: int, budget: Budget) -> dict:
    n, raw_clock, shortcut_clock = seed, 0, 0
    rows, status = [], "module_limit"
    for i in range(count + 1):
        budget.check()
        rank = ranks(n)
        row = {"i": i, "n": str(n), "raw": raw_clock, "shortcut": shortcut_clock, **rank}
        rows.append(row)
        if n == 1:
            status = "reached_one"
            break
        if i == count:
            break
        step = module_step(n)
        m = step["endpoint"]
        # Bounds here apply to module endpoints, NOT every omitted intermediate.
        if m.bit_length() > max_bits:
            status = "endpoint_bit_limit"
            break
        next_rank = ranks(m)
        r, s = int(rank["moving"]), int(next_rank["moving"])
        row.update(a=step["a"], repetitions=step["k"], next=str(m),
                   quarter_safe=4 * s <= r, nonincreasing=s <= r,
                   shortcut_cost=step["shortcut_cost"], raw_cost=step["raw_cost"])
        n = m
        raw_clock += step["raw_cost"]
        shortcut_clock += step["shortcut_cost"]
    return {"rows": rows, "status": status, "map": "maximal_word_module",
            "scope": "Exact module endpoints/clocks and rank comparisons. Endpoint bit cap is not a bound on hidden raw peaks. Quarter-safe and nonincreasing are distinct tests; no unsafe-return theorem is assumed."}


def research_config(request: dict) -> dict:
    fields(request, {"seed", "steps", "modules", "max_bits"})
    n = parse_integer(request.get("seed", "27"))
    bits = bounded_int(request.get("max_bits", 1024), "max_bits", 8, 1024)
    if n.bit_length() > bits:
        raise ValueError("Research adapters cap sources at 1024 bits; the pair desk supports larger integers.")
    return {"kind": "research", "seed": str(n), "max_bits": bits,
            "steps": bounded_int(request.get("steps", 128), "steps", 1, 512),
            "modules": bounded_int(request.get("modules", 32), "modules", 1, 128)}


def research(config: dict, budget: Budget) -> dict:
    trace = orbit({**config, "map": "shortcut"}, budget)
    a, b, denominator, q = 1, 0, 1, 0
    points = []
    coefficient_first, physical_first = None, None
    seed = int(config["seed"])
    for row in trace["rows"]:
        budget.check()
        k, n = row["i"], int(row["n"])
        if a * seed + b != denominator * n:
            raise ArithmeticError("Affine replay mismatch.")
        coefficient = a < denominator
        physical = n < seed
        if k and coefficient and coefficient_first is None:
            coefficient_first = k
        if k and physical and physical_first is None:
            physical_first = k
        rank = ranks(n)
        points.append({**row, "odd_count": q, "multiplier_numerator": str(a),
                       "denominator": str(denominator), "affine_B": str(b),
                       "D": str(denominator - a), "displacement": str(n - seed),
                       "coefficient_below_one": coefficient, "physical_descent": physical,
                       "log2_coefficient": plot_log2(a) - k, **rank})
        if row["parity"]:
            a, b, q = 3 * a, 3 * b + denominator, q + 1
        denominator *= 2
    return {"rows": points, "status": trace["status"], "map": "shortcut",
            "first_coefficient_crossing": coefficient_first, "first_physical_descent": physical_first,
            "modules": module_trace(seed, config["modules"], config["max_bits"], budget),
            "definitions": {"section": "P(n)=(2n+1)^2/3^v3(2n+1)",
                            "moving": "R*(n)=min(R0,R1,R2,Rh), adding h=v3(2n+1) only if h>=3",
                            "affine": "2^k T^k(n0) = 3^q n0 + B; B = (2^k-3^q)n0 + 2^k(T^k(n0)-n0)",
                            "rank_source": RANK_SOURCE},
            "scope": "Exact finite identities and named ranks; P and R* are different. Neither is universally decreasing. Coefficient contraction is not silently substituted for physical descent."}


def transport_config(request: dict) -> dict:
    fields(request, {"seed", "stride", "count", "rounds", "floor", "map", "max_bits", "modulus"})
    seed = parse_integer(request.get("seed", "1"))
    stride = parse_integer(request.get("stride", "1"))
    count = bounded_int(request.get("count", 64), "count", 1, 128)
    bits = bounded_int(request.get("max_bits", 512), "max_bits", 8, 1024)
    if (seed + stride * (count - 1)).bit_length() > bits:
        raise ValueError("A population source exceeds max_bits.")
    mode = request.get("map", "shortcut")
    if mode not in ("shortcut", "module"):
        raise ValueError("Transport clock must be shortcut or module.")
    floor = parse_integer(request.get("floor", "1"))
    if mode == "module" and floor != 1:
        raise ValueError("Module transport supports floor=1 only: arbitrary floors could be crossed inside a hidden module.")
    return {"kind": "transport", "seed": str(seed), "stride": str(stride), "count": count,
            "max_bits": bits, "map": mode, "floor": str(floor),
            "rounds": bounded_int(request.get("rounds", 24), "rounds", 1, 64),
            "modulus": bounded_int(request.get("modulus", 16), "modulus", 2, 64)}


def transport(config: dict, budget: Budget) -> dict:
    seed, stride, floor = int(config["seed"]), int(config["stride"]), int(config["floor"])
    population = [{"source": str(seed + j * stride), "n": seed + j * stride,
                   "status": "killed" if seed + j * stride <= floor else "alive", "raw": 0, "clock": 0}
                  for j in range(config["count"])]
    frames, interruption = [], None
    try:
        for t in range(config["rounds"] + 1):
            budget.check()
            endpoints = Counter(p["n"] for p in population if p["status"] == "alive")
            counts = Counter(p["status"] for p in population)
            histogram = [0] * config["modulus"]
            rank_mass = 0
            quarter = nonincreasing = membership_unknown = 0
            for n, weight in endpoints.items():
                budget.check()
                histogram[n % config["modulus"]] += weight
                rank_n = int(ranks(n)["moving"])
                rank_mass += rank_n * weight
                if config["map"] == "module":
                    next_n = module_step(n)["endpoint"]
                    if next_n.bit_length() > config["max_bits"]:
                        membership_unknown += weight
                    else:
                        rank_next = int(ranks(next_n)["moving"])
                        quarter += weight if 4 * rank_next <= rank_n else 0
                        nonincreasing += weight if rank_next <= rank_n else 0
            frames.append({"time": t, "alive": counts["alive"], "killed": counts["killed"],
                           "unresolved": counts["unresolved"], "distinct_endpoints": len(endpoints),
                           "residues": histogram, "moving_rank_mass": str(rank_mass),
                           "quarter_safe_weight": quarter if config["map"] == "module" else None,
                           "nonincreasing_weight": nonincreasing if config["map"] == "module" else None,
                           "membership_unresolved_weight": membership_unknown if config["map"] == "module" else None,
                           "endpoints": [{"n": str(n), "weight": weight} for n, weight in sorted(endpoints.items())]})
            if t == config["rounds"]:
                break
            # Commit a whole frame atomically. An interruption retains the previous population.
            next_population = []
            for p in population:
                budget.check()
                p = dict(p)
                if p["status"] == "alive":
                    n = p["n"]
                    if config["map"] == "module":
                        step = module_step(n)
                        nxt, raw, peak = step["endpoint"], step["raw_cost"], step["endpoint"]
                    else:
                        nxt = (3 * n + 1) // 2 if n & 1 else n // 2
                        raw, peak = (2, 3 * n + 1) if n & 1 else (1, n)
                    if peak.bit_length() > config["max_bits"]:
                        p["status"] = "unresolved"
                    else:
                        p.update(n=nxt, raw=p["raw"] + raw, clock=p["clock"] + 1,
                                 status="killed" if nxt <= floor else "alive")
                next_population.append(p)
            population = next_population
            budget.progress({"unit": config["map"] + " rounds", "completed": t + 1, "total": config["rounds"]})
    except (Cancelled, TimedOut) as exc:
        interruption = "cancelled" if isinstance(exc, Cancelled) else "timed_out"
    # Last committed frame is authoritative; population may have advanced once before a frame check.
    return {"frames": frames, "count": config["count"], "interruption": interruption,
            "map": config["map"], "floor": str(floor),
            "scope": "Uniform source weights are transported, not resampled; merged endpoints retain multiplicity. At each completed frame alive + killed + unresolved = initial count. Killed means a represented value <= floor. Module floor is fixed to 1. Endpoint-limited module work does not bound hidden raw peaks. Residue laws normalized on survivors are conditional populations, not fresh independent shells."}
