#!/usr/bin/env python3
"""Actual-gap paid returns for a supplied complete rational phase.

A return preserves an equality; it does not accept the infinite candidate.
All checks are exact and stay active under optimized Python.
"""

from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import json


class Checks:
    def __init__(self):
        self.counts = Counter()

    def require(self, condition, category):
        if not condition:
            raise RuntimeError(category)
        self.counts[category] += 1


def valuation(value):
    value = abs(value)
    if not value:
        raise ValueError("nonzero binary valuation argument required")
    return (value & -value).bit_length() - 1


def odd_step(q):
    if q <= 0 or q % 2 == 0:
        raise ValueError("positive odd source required")
    value = 3 * q + 1
    gap = valuation(value)
    return value >> gap, gap


def minimum_lift(x):
    fraction = x % 1
    return fraction + (fraction <= F(1, 2))


def affine(word):
    constant = clock = 0
    for gap in word:
        constant = 3 * constant + (1 << clock)
        clock += gap
    return 3**len(word), constant, clock


@lru_cache(None)
def phase_data(p):
    p = F(p)
    if not F(1, 2) < p <= F(3, 2) or p.denominator % 3 == 0:
        raise ValueError("canonical rational phase with denominator coprime to three required")
    phases, word, current = [], [], p
    while not phases or current != p:
        phases.append(current)
        successor = minimum_lift(3 * current)
        gap = 3 * current - successor
        if gap.denominator != 1 or not 1 <= gap <= 3:
            raise RuntimeError("canonical phase charge failed")
        word.append(int(gap))
        current = successor
        if len(word) > p.denominator:
            raise RuntimeError("finite phase cycle failed to close")
    coefficient, constant, clock = affine(word)
    return tuple(phases), tuple(word), constant, coefficient - (1 << clock), clock


def first_departure(word, t):
    index = clock = 0
    while clock + word[index % len(word)] < t:
        clock += word[index % len(word)]
        index += 1
    b = word[index % len(word)]
    return index, clock, b, t == clock + b


def paid_upper(x, b):
    if b == 2:
        return F(9 * x + 5, 32)
    if b == 3:
        return F(9 * x + 7, 64)
    raise ValueError("paid entry requires canonical charge two or three")


def one_return(source, phase):
    """Total reject/cycle/paid-return procedure for h(source)=phase.

All transitions use the actual ordinary map. A returned phase equality
is equivalent to the original one, whether or not either is true.
"""
    if source <= 0 or source % 2 == 0:
        raise ValueError("positive odd source required")
    phase = F(phase)
    phases, word, constant, signed_d, period_clock = phase_data(phase)
    if source == 1 and phase != 1:
        return {"status": "reject", "reason": "known endpoint scalar", "steps": 0}
    difference = signed_d * source + constant
    if difference == 0:
        q = source
        for expected in word:
            q, gap = odd_step(q)
            if gap != expected:
                raise RuntimeError("canonical cycle verification failed")
        if q != source:
            raise RuntimeError("canonical cycle endpoint failed")
        return {"status": "canonical_cycle", "source": source,
                "phase": phase, "steps": len(word), "gaps": list(word)}
    t = valuation(difference)
    zero_length, zero_clock, entry_b, endpoint_gate = first_departure(word, t)
    budget = source.bit_length() + 2 * t
    if endpoint_gate:
        return {"status": "reject", "reason": "first-departure valuation gate",
                "steps": 0, "budget": budget, "valuation": t}
    q, candidate, high_seen = source, phase, False
    states, candidates, carries, gaps = [], [], [], []
    entry_source = entry_carry = None
    for clock in range(budget + 1):
        current_phase = phases[clock % len(phases)]
        carry = candidate - current_phase
        if q == 1 and candidate != 1:
            return {"status": "reject", "reason": "known endpoint scalar",
                    "steps": clock, "budget": budget}
        if candidate <= F(1, 2) or 3 * candidate > q.bit_length() + 3:
            return {"status": "reject", "reason": "necessary scalar guard",
                    "steps": clock, "budget": budget}
        if carry.denominator != 1 or carry < 0:
            return {"status": "reject", "reason": "canonical carry guard",
                    "steps": clock, "budget": budget}
        k = int(carry)
        states.append(q)
        candidates.append(candidate)
        carries.append(k)
        if high_seen and k == 0:
            return {"status": "return", "source": source, "initial_phase": phase,
                    "endpoint": q, "endpoint_phase": current_phase,
                    "steps": clock, "budget": budget, "valuation": t,
                    "zero_steps": zero_length, "zero_clock": zero_clock,
                    "entry_b": entry_b, "entry_source": entry_source,
                    "entry_carry": entry_carry,
                    "affine_upper": paid_upper(entry_source, entry_b),
                    "states": states, "candidates": candidates,
                    "carries": carries, "gaps": gaps}
        if clock == budget:
            return {"status": "reject", "reason": "finite paid-return budget",
                    "steps": clock, "budget": budget}
        successor, gap = odd_step(q)
        next_candidate = 3 * candidate - gap
        next_carry = next_candidate - phases[(clock + 1) % len(phases)]
        if not high_seen and next_carry >= 1:
            high_seen = True
            entry_source, entry_carry = q, int(next_carry)
        q, candidate = successor, next_candidate
        gaps.append(gap)
    raise RuntimeError("unreachable return loop exit")


def ordinary_source(word, checks):
    coefficient, constant, clock = affine(word)
    modulus = 1 << (clock + 1)
    residue = (((1 << clock) - constant) * pow(coefficient, -1, modulus)) % modulus
    source, q = residue + modulus, residue + modulus
    states = [q]
    for expected in word:
        q, gap = odd_step(q)
        checks.require(gap == expected, "complete literal ordinary cylinder valuation")
        states.append(q)
    checks.require(all(q >= 3 for q in states), "nonterminal positive ordinary cylinder states")
    checks.require((1 << clock) * states[-1] == coefficient * source + constant,
                   "complete cylinder affine equation")
    return states


def actual_scalar(q):
    gaps = []
    while q != 1:
        q, gap = odd_step(q)
        gaps.append(gap)
        if len(gaps) > 20000:
            raise RuntimeError("selected completed scalar replay cap")
    h = F(1)
    for gap in reversed(gaps):
        h = (gap + h) / 3
    return h


def run_checks():
    checks = Checks()
    phases = [F(1), F(3, 2), F(6, 5), F(5, 8), F(7, 8),
              F(7, 13), F(61, 121), F(729, 1456)]
    decisions = Counter()
    return_samples = []
    for p in phases:
        ps, word, constant, signed_d, total = phase_data(p)
        checks.require(all(F(1, 2) < z <= F(3, 2) for z in ps),
                       "complete canonical phase endpoints")
        checks.require(signed_d % 2 == constant % 2 == 1 and signed_d != 0,
                       "complete signed periodic denominator")
        for source in range(1, 2048, 2):
            result = one_return(source, p)
            decisions[result["status"]] += 1
            if result["status"] == "reject":
                checks.require(result["steps"] <= result.get("budget", 0),
                               "total rejection respects supplied source budget")
                continue
            if result["status"] == "canonical_cycle":
                checks.require(source == 1 and p == 1,
                               "checked standard canonical cycle branch")
                continue
            checks.require(result["steps"] <= result["budget"],
                           "actual paid return respects linear source budget")
            checks.require(F(result["endpoint"]) <= result["affine_upper"],
                           "universal arbitrary-phase paid affine upper bound")
            checks.require(result["zero_steps"] <= result["valuation"] - 1,
                           "fixed-source valuation pays zero-carry run")
            for q, h, k in zip(result["states"], result["candidates"], result["carries"]):
                y = F(q, 1 << k)
                checks.require(y >= 1, "necessary scalar guard supplies normalized lower rank")
                if k:
                    checks.require(3 * k <= q.bit_length() + 1,
                                   "integral carry bound from scalar guard")
            for i, (q, q_next) in enumerate(zip(result["states"], result["states"][1:])):
                k, next_k = result["carries"][i:i + 2]
                y, next_y = F(q, 1 << k), F(q_next, 1 << next_k)
                b = word[i % len(word)]
                checks.require(next_y == 3 * y / (1 << (b + 2 * k)) +
                               F(1, 1 << (b + 3 * k)),
                               "exact complete normalized physical step")
                if k:
                    checks.require(next_y <= F(7, 16) * y,
                                   "every high step contracts finite guarded rank")
            if len(return_samples) < 40:
                return_samples.append(result)
    for result in return_samples:
        hq = actual_scalar(result["source"])
        hr = actual_scalar(result["endpoint"])
        checks.require(hq - result["initial_phase"] ==
                       (hr - result["endpoint_phase"]) / 3**result["steps"],
                       "actual scalar equality transport on returned finite prefix")

    paid_paths = maximum_carry = 0
    for p in [F(7, 8), F(11, 13), F(3, 2), F(1) + F(1, 1456)]:
        ps, canonical, _, _, _ = phase_data(p)
        if canonical[0] < 2:
            raise RuntimeError("paid-word fixture must permit entry")
        for growing in (False, True):
            for length in range(7):
                word = [canonical[0] - 1]
                carries = [0, 1]
                k = 1
                for j in range(length):
                    b = canonical[len(word) % len(canonical)]
                    next_k = b + 3 * k - 1 if growing else 1
                    word.append(b + 3 * k - next_k)
                    carries.append(next_k)
                    k = next_k
                b = canonical[len(word) % len(canonical)]
                word.append(b + 3 * k)
                carries.append(0)
                states = ordinary_source(word, checks)
                candidate = p
                for i, q in enumerate(states):
                    checks.require(candidate == ps[i % len(ps)] + carries[i],
                                   "complete arbitrary high candidate path")
                    checks.require(3 * candidate <= q.bit_length() + 3,
                                   "large ordinary source funds every candidate guard")
                    if i < len(word):
                        candidate = 3 * candidate - word[i]
                result = one_return(states[0], p)
                checks.require(result["status"] == "return" and
                               result["endpoint"] == states[-1] and
                               result["gaps"] == word,
                               "total transformer reconstructs arbitrary high excursion")
                checks.require(F(states[-1]) <= paid_upper(states[0], canonical[0]),
                               "unbounded-carry paid envelope on actual ordinary word")
                paid_paths += 1
                maximum_carry = max(maximum_carry, max(carries))

    w = [1] * 6 + [2] * 5 + [3]
    v = [1] * 7 + [5] + [2] * 3 + [3]
    p = F(729, 1456)
    _, canonical, cnum, d, a = phase_data(p)
    checks.require(list(canonical) == w and (cnum, d, a) == (700273, 7153, 19),
                   "sharp composite phase full canonical data")
    checks.require(affine(v) == (531441, 1227505, 21),
                   "complete paid composite phase word")
    allowed, clock = set(), 0
    for b in w:
        allowed.update(range(clock + 1, clock + b))
        clock += b
    checks.require(allowed == {7, 9, 11, 13, 15, 17, 18},
                   "exact denominator-1456 first-departure gate")
    R, c = F(531441, 524288), F(700273, 7153)
    kappa = F(-2838855001, 117194752)
    alpha = lambda m: R**(m + 1) / 4
    checks.require(alpha(101) < 1 < alpha(102),
                   "exact composite phase slope threshold")
    checks.require(alpha(101) * (17958 + c) + kappa < 17958,
                   "complete affine threshold retains additive cost")
    checks.require(alpha(1) * (3 + c) + kappa < 3 and c + kappa > 0,
                   "small-prefix descent and all-later expansion signs")
    checks.require(F((1 << 45) - 700273, 7153) > 17958,
                   "fixed-source valuation funds full threshold source height")
    composite_rows = []
    for m in [0, 1, 2, 10, 50, 100, 101, 102, 103]:
        word = w * m + v
        states = ordinary_source(word, checks)
        source, endpoint = states[0], states[-1]
        checks.require(valuation(7153 * source + 700273) == 19 * m + 7,
                       "literal full-family ordinary valuation class")
        checks.require(F(endpoint) == alpha(m) * (source + c) + kappa,
                       "complete same-phase composite endpoint identity")
        checks.require((endpoint < source) == (m <= 101) and
                       (endpoint > source) == (m >= 102),
                       "sharp complete composite return descent-expansion threshold")
        result = one_return(source, p)
        checks.require(result["status"] == "return" and
                       result["steps"] == 12 * m + 8,
                       "first paid low return occurs before optional phase completion")
        checks.require(result["steps"] <= 3 * source.bit_length() + 26,
                       "sharp composite phase explicit bit-length return budget")
        composite_rows.append({"m": m, "source_bits": source.bit_length(),
                               "whole_word_steps": len(word),
                               "first_paid_return_steps": result["steps"],
                               "direction": "descent" if endpoint < source else "expansion"})

    return {"status": "PASS", "exact_checks": sum(checks.counts.values()),
            "checks_by_category": dict(sorted(checks.counts.items())),
            "supplied_phase_source_cases": len(phases) * 1024,
            "transformer_outcomes": dict(sorted(decisions.items())),
            "actual_scalar_transport_cases": len(return_samples),
            "arbitrary_paid_paths": paid_paths, "largest_tested_carry": maximum_carry,
            "sharp_composite_family": composite_rows,
            "scope": "literal ordinary finite paths and total supplied-phase transformers; returns preserve equality without accepting it",
            "unproved": "termination or exclusion of repeated paid returns from one fixed positive ordinary source"}


if __name__ == "__main__":
    print(json.dumps(run_checks(), sort_keys=True, indent=2))
