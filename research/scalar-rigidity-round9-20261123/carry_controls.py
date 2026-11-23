#!/usr/bin/env python3
"""Exact ordinary/candidate controls for CARRY_RETURN.md.

Finite candidate carry paths are not claimed to equal the actual infinite
scalar. No proof check uses floating point, Python assert, or a carry cap.
"""

from collections import Counter
from fractions import Fraction
import json


class Checks:
    def __init__(self):
        self.counts = Counter()

    def require(self, condition, category):
        if not condition:
            raise RuntimeError(category)
        self.counts[category] += 1


def valuation(n, prime=2):
    if n <= 0:
        raise ValueError("positive valuation argument required")
    if prime == 2:
        return (n & -n).bit_length() - 1
    result = 0
    while n % prime == 0:
        n //= prime
        result += 1
    return result


def odd_step(q):
    if q <= 0 or q % 2 == 0:
        raise ValueError("positive odd source required")
    value = 3 * q + 1
    gap = valuation(value)
    return value >> gap, gap


def replay(q, word, checks):
    states = [q]
    for expected in word:
        successor, actual = odd_step(states[-1])
        checks.require(actual == expected, "literal ordinary gap replay")
        checks.require((1 << actual) * successor == 3 * states[-1] + 1,
                       "complete ordinary edge equation")
        states.append(successor)
    return states


def ordinary_source(word, checks):
    """Construct a positive cylinder member, then verify its literal word."""
    coefficient, constant, clock = 1, 0, 0
    for gap in word:
        constant = 3 * constant + (1 << clock)
        coefficient *= 3
        clock += gap
    modulus = 1 << (clock + 1)
    residue = (((1 << clock) - constant) * pow(coefficient, -1, modulus)) % modulus
    # One full period above the least residue keeps all source states >1.
    q = residue + modulus
    states = replay(q, word, checks)
    checks.require(all(x >= 3 for x in states), "positive nonterminal cylinder member")
    checks.require((1 << clock) * states[-1] == coefficient * q + constant,
                   "complete cylinder affine equation")
    return states


def candidate_values(word, checks):
    values = [7]
    for gap in word:
        values.append(3 * values[-1] - 8 * gap)
    checks.require(values[-1] == 7 and all(H > 4 for H in values),
                   "closed positive denominator-eight candidate")
    checks.require(all(H % 8 == (7 if i % 2 == 0 else 5)
                       for i, H in enumerate(values)), "exact alternating candidate phase")
    return values


def check_paid_word(word, checks):
    values = candidate_values(word, checks)
    checks.require(len(word) % 2 == 0 and word[0] == 1 and values[1] == 13,
                   "paid high entry")
    first_low = next(i for i in range(1, len(values)) if values[i] in (5, 7))
    checks.require(first_low == len(word) or
                   (first_low == len(word) - 1 and values[first_low] == 5 and word[-1] == 1),
                   "minimal first low return and forced normalization")
    carries = [(H - (7 if i % 2 == 0 else 5)) // 8
               for i, H in enumerate(values)]
    ell = len(word) // 2
    total_carry = sum(carries[:-1])
    checks.require(sum(word) == 3 * ell + 2 * total_carry,
                   "complete normalized carry clock")
    checks.require(total_carry >= (1 if ell == 1 else 2 * ell - 2),
                   "first-return integer carry lower bound")
    states = ordinary_source(word, checks)
    normalized = [Fraction(q, 1 << k) for q, k in zip(states, carries)]
    for i, (q, successor) in enumerate(zip(normalized, normalized[1:])):
        b, k = (2 if i % 2 == 0 else 1), carries[i]
        expected = 3 * q / (1 << (b + 2 * k)) + Fraction(1, 1 << (b + 3 * k))
        checks.require(successor == expected, "exact carry-normalized ordinary equation")
        if k >= 1:
            upper = 3 * q / (1 << (b + 2)) + Fraction(1, 1 << (b + 3))
            checks.require(successor <= upper, "unbounded carry unit envelope")
    x, r = states[0], states[-1]
    checks.require(Fraction(r) <= Fraction(9 * x + 5, 32) <= Fraction(x, 3),
                   "all-paid-return P majorant")
    if ell >= 2:
        checks.require(Fraction(r) <= Fraction(81 * x + 605, 1024) < Fraction(9 * x + 5, 32),
                       "strict longer-excursion affine majorant")
        checks.require(Fraction(r, x) <= Fraction(25, 18)**ell / 4**total_carry
                       <= Fraction(625, 5184), "independent complete physical clock bound")
    return {"odd_steps": len(word), "clock": sum(word),
            "maximum_carry": max(carries), "source_bits": x.bit_length()}


def one_return(q):
    """Total one-return transformer for a supplied candidate h(q)=7/8.

    A 'return' is an equality-preserving finite prefix, not acceptance of the
    infinite candidate. A 'reject' disproves that candidate by the note's gates.
    """
    if q <= 0 or q % 2 == 0:
        raise ValueError("positive odd candidate source required")
    initial = q
    if q == 1:
        return {"status": "reject", "reason": "one", "steps": 0}
    shifted = valuation(q + 7)
    if shifted % 3 != 1:
        return {"status": "reject", "reason": "shifted valuation", "steps": 0}
    m = (shifted - 1) // 3
    budget = 2 * (q + 7).bit_length() + 1
    H, high_seen = 7, False
    states, values, gaps = [q], [H], []
    for _ in range(budget):
        if q == 1:
            return {"status": "reject", "reason": "one", "steps": len(gaps)}
        if H <= 4:
            return {"status": "reject", "reason": "lower guard", "steps": len(gaps)}
        if 3 * H > 8 * q.bit_length() + 24:
            return {"status": "reject", "reason": "upper guard", "steps": len(gaps)}
        q, gap = odd_step(q)
        H = 3 * H - 8 * gap
        gaps.append(gap)
        states.append(q)
        values.append(H)
        high_seen = high_seen or H >= 13
        if H == 7 and high_seen and q != 1:
            return {"status": "return", "initial": initial, "endpoint": q,
                    "steps": len(gaps), "budget": budget, "low_pairs": m,
                    "states": states, "values": values, "gaps": gaps}
    return {"status": "reject", "reason": "finite return budget", "steps": len(gaps)}


def actual_scalar(q, checks):
    """Finite control only: complete the specified actual ordinary trajectory."""
    gaps = []
    while q != 1 and len(gaps) < 20_000:
        q, gap = odd_step(q)
        gaps.append(gap)
    checks.require(q == 1, "selected actual scalar tail completed")
    h = Fraction(1)
    for gap in reversed(gaps):
        h = (gap + h) / 3
    return h


def reduce_supplied_candidate(q, a, r):
    """Reduce a/(8*3^r) to a triadic dispatch, rejection, or a 7/8 candidate."""
    if q <= 0 or q % 2 == 0 or r < 0:
        raise ValueError("positive odd source and nonnegative denominator exponent required")
    phase = a % 8
    if phase == 0:
        return {"status": "triadic_dispatch", "steps": 0}
    if phase not in (5, 7):
        return {"status": "reject", "reason": "excluded complete phase", "steps": 0}
    candidate = Fraction(a, 8 * 3**r)
    budget = 2*r + q.bit_length() + 1
    gaps = []

    def violates_guard():
        return q == 1 or candidate <= Fraction(1, 2) or 3*candidate > q.bit_length()+3

    for _ in range(r):
        if violates_guard():
            return {"status": "reject", "reason": "necessary scalar guard", "steps": len(gaps)}
        q, gap = odd_step(q)
        candidate = 3*candidate - gap
        gaps.append(gap)
    cleared = 8*candidate
    if cleared.denominator != 1 or cleared.numerator % 8 != phase:
        raise RuntimeError("exact ternary clearing failed")
    # At most bl(q_r) high transitions and one forced low transition.
    tail_budget = q.bit_length() + 1
    for tail_step in range(tail_budget + 1):
        if violates_guard():
            return {"status": "reject", "reason": "necessary scalar guard", "steps": len(gaps)}
        if candidate == Fraction(7, 8):
            return {"status": "seven_eighths_candidate", "endpoint": q,
                    "steps": len(gaps), "budget": budget, "gaps": gaps}
        if tail_step == tail_budget:
            break
        q, gap = odd_step(q)
        candidate = 3*candidate - gap
        gaps.append(gap)
    return {"status": "reject", "reason": "finite reduction budget", "steps": len(gaps)}


def run_checks():
    checks = Checks()
    block_rows = []
    for m in range(33):
        D = 9 ** (m + 1)
        u0 = 13 * pow(D, -1, 32) % 32
        checks.require(u0 == [5, 29, 21, 13][m % 4], "complete P source residue period")
        for z in [0, 1, 7]:
            u = u0 + 32 * z
            q = (1 << (3 * m + 1)) * u - 7
            r = (D * u - 29) // 16
            states = replay(q, [2, 1] * m + [1, 4], checks)
            checks.require(states[-1] == r, "complete L-power-P source and endpoint class")
            slope = Fraction(D, 1 << (3 * m + 5))
            checks.require(r == slope * (q + 7) - Fraction(29, 16),
                           "full affine endpoint including additive term")
            checks.require((r < q) == (m <= 10) and (r > q) == (m >= 11),
                           "sharp ten-eleven physical threshold")
        if m in [0, 1, 10, 11, 32]:
            block_rows.append({"m": m, "u0": u0,
                               "direction": "descent" if m <= 10 else "expansion"})

    paid_words = []
    # Long unit-carry excursions, with either parity of the first low return.
    for t in range(9):
        paid_words.append([1] + [3, 4] * t + [4])
        paid_words.append([1] + [3, 4] * t + [3, 5, 1])
    # Exponentially large carries are created by repeated literal gap-one steps.
    for t in range(1, 8):
        word = [1] * (t + 1)
        H = 3 ** (t + 2) + 4
        next_phase = 7 if (len(word) + 1) % 2 == 0 else 5
        word.append((3 * H - next_phase) // 8)
        if next_phase == 5:
            word.append(1)
        paid_words.append(word)
    paid_rows = [check_paid_word(word, checks) for word in paid_words]
    for word in paid_words:
        for m in range(13):
            states = ordinary_source([2, 1] * m + word, checks)
            q, x, r = states[0], states[2 * m], states[-1]
            checks.require(valuation(q + 7) == 3 * m + 1,
                           "exact unpaid length before arbitrary carry excursion")
            checks.require(Fraction(r) <= Fraction(9 * x + 5, 32),
                           "arbitrary paid excursion after exact L prefix")
            if m <= 10:
                checks.require(r < q, "all-carry short-prefix descent")

    decisions = Counter()
    return_examples = []
    maximum_steps = 0
    for q in range(1, 1 << 15, 2):
        result = one_return(q)
        maximum_steps = max(maximum_steps, result["steps"])
        if result["status"] == "reject":
            decisions["reject: " + result["reason"]] += 1
            continue
        decisions["return"] += 1
        n, m, r = result["steps"], result["low_pairs"], result["endpoint"]
        checks.require(n <= result["budget"] and n % 2 == 0,
                       "finite normalized one-return budget")
        checks.require(result["gaps"][:2*m] == [2, 1] * m,
                       "transformer uses literal unpaid prefix")
        checks.require(result["values"][2*m+1] == 13,
                       "transformer actual high-entry clock")
        x = result["states"][2*m]
        checks.require(Fraction(r) <= Fraction(9*x+5, 32),
                       "returned candidate path satisfies all-carry majorant")
        checks.require(r < q, "all returned small sources strictly decrease")
        if len(return_examples) < 24:
            return_examples.append(result)
    for result in return_examples:
        q, r, n = result["initial"], result["endpoint"], result["steps"]
        hq, hr = actual_scalar(q, checks), actual_scalar(r, checks)
        checks.require(hq - Fraction(7, 8) == (hr - Fraction(7, 8)) / 3**n,
                       "actual scalar equality transport on finite candidate return")
        checks.require(hq != Fraction(7, 8), "completed examples are not exact seven-eighths sources")

    reductions = Counter()
    for q in [3, 5, 7, 9, 11, 27, 31, 41, 85, 457]:
        for r in range(4):
            for a in [1, 2, 3, 4, 6, 8, 13, 15, 5*3**r, 7*3**r]:
                result = reduce_supplied_candidate(q, a, r)
                reductions[result["status"]] += 1
                if result["status"] == "seven_eighths_candidate":
                    checks.require(result["steps"] <= result["budget"],
                                   "bounded supplied denominator-eight reduction")
                    t = Fraction(a, 8*3**r)
                    endpoint = q
                    for gap in result["gaps"]:
                        endpoint, actual = odd_step(endpoint)
                        checks.require(actual == gap, "literal supplied-candidate reduction prefix")
                        t = 3*t-gap
                    checks.require(t == Fraction(7, 8) and endpoint == result["endpoint"],
                                   "exact supplied-candidate reduction endpoint")
                    hq, hr = actual_scalar(q, checks), actual_scalar(endpoint, checks)
                    checks.require(hq-Fraction(a, 8*3**r) ==
                                   (hr-Fraction(7, 8))/3**result["steps"],
                                   "actual scalar transport for unreduced supplied candidates")

    # Actual inverse words, followed by controls showing the three gates coexist.
    for z in range(12):
        q = 18*z + 11
        p = (8*q - 7)//9
        checks.require(0 < p < q and replay(p, [2, 1], checks)[-1] == q,
                       "smaller literal inverse-L source")
    D = 3**24
    residue = (-29 * pow(16, -1, D)) % D
    if residue % 2 == 0:
        residue += D
    for j in range(6):
        q = residue + 2*D*j
        u = (16*q + 29)//D
        p = (1 << 34)*u - 7
        checks.require(0 < p < q and replay(p, [2, 1]*11 + [1, 4], checks)[-1] == q,
                       "smaller literal inverse-eleven-L-P source")
    compatible_gates = []
    for j in range(8):
        q = (1 << 34)*(1+18*j) - 7
        checks.require(valuation(q+7) == 34 and q % 9 == 0 and valuation(16*q+29, 3) == 0,
                       "binary and ternary gates retain ordinary integer freedom")
        result = one_return(q)
        compatible_gates.append({"j": j, "source": q, "one_return_status": result["status"],
                                 "steps": result["steps"]})

    return {
        "status": "PASS",
        "scope": "finite ordinary prefixes and candidate carries; all-time scalar equality is not assumed",
        "exact_checks": sum(checks.counts.values()),
        "checks_by_category": dict(sorted(checks.counts.items())),
        "sharp_threshold_rows": block_rows,
        "paid_excursion_cases": len(paid_rows),
        "largest_tested_carry": max(row["maximum_carry"] for row in paid_rows),
        "largest_paid_source_bits": max(row["source_bits"] for row in paid_rows),
        "candidate_ordinary_sources": 1 << 14,
        "one_return_decisions": dict(sorted(decisions.items())),
        "maximum_candidate_odd_steps": maximum_steps,
        "exact_actual_scalar_transport_examples": len(return_examples),
        "supplied_candidate_reductions": dict(sorted(reductions.items())),
        "compatible_gate_examples": compatible_gates,
        "unproved": "termination of repeated returns after arbitrarily long low prefixes at one fixed positive ordinary source",
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), sort_keys=True, indent=2))
