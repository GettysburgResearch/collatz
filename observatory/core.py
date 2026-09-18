"""Exact, bounded mathematical kernel for Collatz Observatory 0.1.

All unbounded integers cross the JSON boundary as decimal strings. No eval,
floats in arithmetic decisions, external packages, or imported proof claims.
"""
from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
from hashlib import sha256
from math import log2
from pathlib import Path
import re
import threading
import time
from typing import Any, Callable

VERSION = "0.1.0"
BASELINE = "ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a"
LIMITS = {"max_bits": 8192, "max_steps": 20000, "family_count": 512,
          "family_work": 1000000, "word_length": 512, "inverse_nodes": 256,
          "digit_budget": 1500000, "wall_seconds": 15}
MAPS = {"raw": "n/2 if even; 3n+1 if odd",
        "shortcut": "n/2 if even; (3n+1)/2 if odd",
        "odd": "(3n+1)/2^v2(3n+1); positive odd sources only"}


class Cancelled(Exception):
    pass


class TimedOut(Exception):
    pass


class Budget:
    def __init__(self, event: threading.Event | None = None,
                 progress: Callable[[dict], None] | None = None,
                 seconds: float = LIMITS["wall_seconds"]):
        self.event = event or threading.Event()
        self.deadline = time.monotonic() + seconds
        self.progress = progress or (lambda _: None)

    def check(self) -> None:
        if self.event.is_set():
            raise Cancelled("Cancelled by the caller; no conclusion about the orbit.")
        if time.monotonic() > self.deadline:
            raise TimedOut("Wall-time budget exhausted; no mathematical conclusion.")


def bounded_int(value: Any, name: str, low: int, high: int) -> int:
    if type(value) is not int or not low <= value <= high:
        raise ValueError(f"{name} must be an integer in [{low}, {high}].")
    return value


def parse_integer(value: Any) -> int:
    """Positive decimal, binary, or the bounded grammar 2^k[+/-decimal]."""
    if not isinstance(value, str) or len(value) > 2600:
        raise ValueError("An exact seed must be a string of at most 2600 characters.")
    text = value.strip()
    power = re.fullmatch(r"2\^(\d{1,4})(?:([+-])(\d{1,2500}))?", text)
    if power:
        exponent = bounded_int(int(power[1]), "exponent", 0, LIMITS["max_bits"] - 1)
        offset = int(power[3] or "0")
        n = (1 << exponent) + (-offset if power[2] == "-" else offset)
    elif re.fullmatch(r"0b[01]{1,2500}", text):
        n = int(text[2:], 2)
    elif re.fullmatch(r"[0-9]{1,2500}", text):
        n = int(text, 10)
    else:
        raise ValueError("Use positive decimal, 0b binary, or 2^k+offset / 2^k-offset. No code expressions.")
    if n <= 0 or n.bit_length() > LIMITS["max_bits"]:
        raise ValueError(f"Seed must be positive and at most {LIMITS['max_bits']} bits.")
    return n


def normalize_request(request: Any) -> dict:
    if not isinstance(request, dict):
        raise ValueError("Request must be a JSON object.")
    kind = request.get("kind")
    if kind not in ("orbit", "family", "word", "inverse"):
        raise ValueError("kind must be orbit, family, word, or inverse.")
    allowed = {"orbit": {"kind", "seed", "map", "steps", "max_bits"},
               "family": {"kind", "seed", "map", "steps", "max_bits", "count", "stride"},
               "word": {"kind", "word"},
               "inverse": {"kind", "seed", "depth", "nodes"}}[kind]
    if set(request) - allowed:
        raise ValueError("Unknown request fields: " + ", ".join(sorted(set(request) - allowed)))
    if kind == "word":
        word = request.get("word")
        if not isinstance(word, str) or not re.fullmatch(r"[01]{1,512}", word):
            raise ValueError("word must contain 1–512 binary digits; clock is shortcut.")
        return {"kind": kind, "word": word}
    seed = parse_integer(request.get("seed", "27"))
    out = {"kind": kind, "seed": str(seed)}
    if kind == "inverse":
        out.update(depth=bounded_int(request.get("depth", 6), "depth", 0, 12),
                   nodes=bounded_int(request.get("nodes", 128), "nodes", 1, LIMITS["inverse_nodes"]))
        return out
    mode = request.get("map", "shortcut")
    if mode not in MAPS:
        raise ValueError("Unknown map.")
    if mode == "odd" and seed % 2 == 0:
        raise ValueError("The odd-to-odd map requires an odd seed; no implicit normalization.")
    bits = bounded_int(request.get("max_bits", 8192), "max_bits", 8, 8192)
    if seed.bit_length() > bits:
        raise ValueError("The seed already exceeds max_bits.")
    steps = bounded_int(request.get("steps", 2000), "steps", 1, LIMITS["max_steps"])
    out.update(map=mode, steps=steps, max_bits=bits)
    if kind == "family":
        count = bounded_int(request.get("count", 128), "count", 1, LIMITS["family_count"])
        stride = parse_integer(request.get("stride", "1"))
        if mode == "odd" and count > 1 and stride % 2:
            raise ValueError("Odd-to-odd families need an even stride.")
        if count * steps > LIMITS["family_work"]:
            raise ValueError("count × steps must not exceed 1,000,000.")
        if (seed + (count - 1) * stride).bit_length() > bits:
            raise ValueError("The last family source exceeds max_bits.")
        out.update(count=count, stride=str(stride))
    return out


def valuation2(n: int) -> int:
    if n <= 0:
        raise ValueError("valuation2 expects a positive integer.")
    return (n & -n).bit_length() - 1


def plot_log2(n: int) -> float:
    """Approximate DISPLAY coordinate; never a predicate or integer identity."""
    shift = max(0, n.bit_length() - 53)
    return log2(n >> shift) + shift


def transition(n: int, mode: str) -> tuple[int, int, int]:
    """Next displayed state, raw clock cost, maximum along the raw segment."""
    if n % 2 == 0:
        if mode == "odd":
            raise ValueError("Odd-to-odd input is even.")
        return n // 2, 1, n
    high = 3 * n + 1
    if mode == "raw":
        return high, 1, high
    if mode == "shortcut":
        return high // 2, 2, high
    if mode == "odd":
        v = valuation2(high)
        return high >> v, 1 + v, high
    raise ValueError("Unknown map.")


def orbit(config: dict, budget: Budget, retain: bool = True) -> dict:
    seed, mode = int(config["seed"]), config["map"]
    n, raw, peak, raw_peak, peak_step = seed, 0, seed, seed, 0
    first_descent, cycle_entry, digit_count = None, None, 0
    rows, seen = [], {}
    status = "step_limit"
    for i in range(config["steps"] + 1):
        budget.check()
        if i % 128 == 0:
            budget.progress({"unit": "steps", "completed": i, "total": config["steps"]})
        if retain:
            text = str(n)
            rows.append({"i": i, "raw": raw, "n": text, "bits": n.bit_length(),
                         "log2": plot_log2(n), "parity": n & 1})
            digit_count += len(text)
        if n > peak:
            peak, peak_step = n, i
        if n < seed and first_descent is None:
            first_descent = i
        if n == 1:
            status = "reached_one"
            break
        if n in seen:
            cycle_entry, status = seen[n], "cycle"
            break
        seen[n] = i
        if i == config["steps"]:
            break
        if retain and digit_count >= LIMITS["digit_budget"]:
            status = "storage_limit"
            break
        nxt, cost, segment_peak = transition(n, mode)
        # Includes hidden 3n+1 intermediates in accelerated maps.
        if segment_peak.bit_length() > config["max_bits"]:
            status = "bit_limit"
            break
        raw_peak = max(raw_peak, segment_peak)
        n, raw = nxt, raw + cost
    return {"seed": str(seed), "map": mode, "status": status, "steps": i,
            "raw_steps": raw, "terminal": str(n), "peak": str(peak),
            "peak_log2": plot_log2(peak), "peak_step": peak_step,
            "raw_peak": str(raw_peak), "first_descent": first_descent,
            "cycle_entry": cycle_entry, "rows": rows,
            "coverage": "Exact finite orbit; stopped at 1, repeat, or stated resource limit."}


def family(config: dict, budget: Budget) -> dict:
    members = []
    seed, stride = int(config["seed"]), int(config["stride"])
    for j in range(config["count"]):
        budget.check()
        item = orbit({**config, "seed": str(seed + j * stride)}, budget, retain=False)
        item.pop("rows")
        item["offset"] = j
        members.append(item)
        budget.progress({"unit": "sources", "completed": j + 1, "total": config["count"]})
    return {"members": members, "counts": dict(Counter(x["status"] for x in members)),
            "population": "All requested sources seed + j*stride; uniform counting, not logarithmic sampling.",
            "map": config["map"], "count": len(members)}


def fraction_text(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def word_analysis(config: dict, budget: Budget) -> dict:
    word = config["word"]
    a, s, prefixes = 0, 0, []
    for j, bit in enumerate(word):
        budget.check()
        if bit == "1":
            a, s = 3 * a + (1 << j), s + 1
        modulus = 1 << (j + 1)
        residue = (-a * pow(3 ** s, -1, modulus)) % modulus
        least = residue or modulus  # positive representative, not canonical zero
        prefixes.append({"length": j + 1, "residue": str(residue), "modulus": str(modulus),
                         "least": str(least), "log2": plot_log2(least)})
    length, denominator = len(word), (1 << len(word)) - 3 ** s
    candidate = Fraction(a, denominator)
    x, replay, legal = candidate, [], True
    for bit in word:
        budget.check()
        # For rationals with odd denominator, parity is numerator parity.
        parity = x.numerator & 1
        legal = legal and x.denominator % 2 == 1 and parity == int(bit)
        replay.append({"value": fraction_text(x), "parity": parity})
        x = (3 * x + 1) / 2 if bit == "1" else x / 2
    legal = legal and x == candidate
    is_integer = candidate.denominator == 1
    if not legal:
        classification = "replay_failed_not_a_cycle"
    elif not is_integer:
        classification = "rational_noninteger"
    elif candidate > 0:
        classification = ("trivial_positive_cycle" if all(r["value"] in ("1", "2") for r in replay)
                          else "positive_integer_cycle")
    elif candidate < 0:
        classification = "signed_integer_cycle"
    else:
        classification = "zero_outside_positive_domain"
    primitive = next(k for k in range(1, length + 1) if length % k == 0 and word == word[:k] * (length // k))
    return {"word": word, "map": "shortcut", "length": length, "ones": s, "A": str(a),
            "D": str(denominator), "candidate": fraction_text(candidate),
            "numerator": str(candidate.numerator), "denominator": str(candidate.denominator),
            "full_denominator_divides": a % abs(denominator) == 0,
            "classification": classification, "replay_legal": legal, "replay": replay,
            "primitive_word_length": primitive, "prefixes": prefixes,
            "residue": prefixes[-1]["residue"], "modulus": prefixes[-1]["modulus"],
            "least_positive": prefixes[-1]["least"],
            "scope": "One finite word and its exact rational periodic candidate; not all-word exclusion."}


def inverse(config: dict, budget: Budget) -> dict:
    root = int(config["seed"])
    nodes, edges = {root: 0}, []
    queue = deque([root])
    truncated = False
    while queue:
        budget.check()
        target = queue.popleft()
        depth = nodes[target]
        if depth >= config["depth"]:
            continue
        predecessors = [2 * target]
        if (2 * target - 1) % 3 == 0:
            candidate = (2 * target - 1) // 3
            if candidate > 0 and candidate % 2:
                predecessors.append(candidate)
        for source in predecessors:
            if source.bit_length() > LIMITS["max_bits"]:
                truncated = True
                continue
            if source not in nodes:
                if len(nodes) >= config["nodes"]:
                    truncated = True
                    continue
                nodes[source] = depth + 1
                queue.append(source)
            edges.append({"source": str(source), "target": str(target)})
    return {"root": str(root), "map": "shortcut", "depth": config["depth"], "truncated": truncated,
            "nodes": [{"n": str(n), "depth": d} for n, d in nodes.items()], "edges": edges,
            "scope": "Distinct positive states, minimum inverse depths, exact source→target edges; finite depth only."}


OPERATIONS = {"orbit": orbit, "family": family, "word": word_analysis, "inverse": inverse}


def execute(request: Any, budget: Budget | None = None) -> dict:
    config = normalize_request(request)
    result = OPERATIONS[config["kind"]](config, budget or Budget())
    return {"schema": "collatz-result/v1", "version": VERSION, "request": config,
            "kernel_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
            "baseline": BASELINE, "result": result}
