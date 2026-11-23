#!/usr/bin/env python3
"""Exact ordinary return-tower controls; no actual scalar rationality assumed."""

from collections import Counter
from fractions import Fraction
import json


A = 9**12
BINARY = 2**38
DISTANCE = A-BINARY
CONSTANT = 7*A-29*2**34
R_WORD = [2, 1]*11+[1, 4]
LAMBDA = Fraction(9, 8)
RHO = Fraction(9, 32)+Fraction(83, 2**38)


class Checks:
    def __init__(self):
        self.counts = Counter()

    def require(self, value, category):
        if not value:
            raise RuntimeError(category)
        self.counts[category] += 1


def v2(n):
    if n <= 0:
        raise ValueError("positive valuation argument required")
    return (n & -n).bit_length()-1


def odd_step(q):
    if q <= 0 or q % 2 == 0:
        raise ValueError("positive odd source required")
    value = 3*q+1
    gap = v2(value)
    return value >> gap, gap


def replay(q, word, checks):
    states = [q]
    for expected in word:
        q, gap = odd_step(q)
        checks.require(gap == expected, "literal ordinary tower gap")
        states.append(q)
    return states


def center(q):
    return DISTANCE*q+CONSTANT


def repetition_count(q):
    return (v2(center(q))-1)//38


def complete_affine(word):
    odd_power, constant, clock = 1, 0, 0
    for gap in word:
        constant = 3*constant+(1 << clock)
        odd_power *= 3
        clock += gap
    return odd_power, constant, clock


def cylinder_source(word):
    odd_power, constant, clock = complete_affine(word)
    modulus = 1 << (clock+1)
    residue = (((1 << clock)-constant)*pow(odd_power, -1, modulus)) % modulus
    return residue+modulus


def check_tower_boundaries(boundaries, low_lengths, checks, use_small_rho=False):
    initial = boundaries[0]+7
    source_bits = initial.bit_length()
    charge = 0
    upper = Fraction(initial)
    small_upper = Fraction(initial)
    for j, m in enumerate(low_lengths):
        X, X_next = boundaries[j]+7, boundaries[j+1]+7
        checks.require(v2(X) == 3*m+1, "exact next unpaid shifted valuation")
        checks.require(X <= upper, "cumulative arbitrary-return shifted product")
        checks.require((1 << (3*m+1)) <= X, "next-run ordinary size requirement")
        checks.require(15*m < 5*(source_bits-1)+charge,
                       "integer height-to-low-run budget")
        checks.require(3*15**j*m < (source_bits-1)*16**j,
                       "source-dependent exponential low-run bound")
        one_step = Fraction(9, 32)*LAMBDA**m*X+Fraction(83, 16)
        checks.require(X_next <= one_step, "complete shifted return with additive constant")
        upper *= Fraction(4, 5)*LAMBDA**m
        checks.require(X_next <= upper, "next cumulative arbitrary-return bound")
        if use_small_rho:
            checks.require(X >= 2**34, "explicit source floor for sharpened paid factor")
            small_upper *= RHO*LAMBDA**m
            checks.require(X_next <= small_upper, "sharpened source-floor product")
        charge += m


def construct_flat_tower(T, checks):
    if T < 2:
        raise ValueError("at least two R words retain a constant valuation at compared endpoints")
    K, G, s = 24*T, 38*T, 24*T+6
    denominator = A**T
    numerator_constant = CONSTANT*(A**T-BINARY**T)//DISTANCE
    checks.require(numerator_constant*DISTANCE == CONSTANT*(A**T-BINARY**T),
                   "integral full repeated affine constant")
    residue = ((2**G+numerator_constant)*pow(pow(2, G+s, denominator), -1, denominator)) % denominator
    checks.require(0 < residue < denominator, "nonzero terminal source congruence")
    t = residue if residue % 2 else residue+denominator
    checks.require(0 < t < 2*denominator and t % 2 == 1, "unique odd terminal representative")
    r = (1 << s)*t-1
    numerator = (1 << G)*r-numerator_constant
    checks.require(numerator % denominator == 0, "exact finite tower source integrality")
    q = numerator//denominator
    checks.require(0 < q < (1 << (62*T+7)) and q % 2 == 1,
                   "positive ordinary source with linear bit bound")
    states = replay(q, R_WORD*T, checks)
    checks.require(states[-1] == r, "complete prescribed tower endpoint")
    boundaries = states[::24]
    checks.require(len(boundaries) == T+1, "complete return boundary count")
    for j in range(T):
        x, y = boundaries[j:j+2]
        checks.require(BINARY*y == A*x+CONSTANT, "full expanding return affine equation")
        checks.require(y > x, "strict actual physical growth at every return")
        checks.require(BINARY*center(y) == A*center(x), "integer affine-center transport")
        checks.require(v2(center(y)) == v2(center(x))-38,
                       "exact integer repetition rank decrement")
        checks.require(v2(x+7) == 34, "constant shifted valuation before every R")
    checks.require(v2(r+7) == 1 and v2(center(r)) == 1, "terminal break in the constant return type")
    checks.require(v2(center(q)) == 38*T+1 and repetition_count(q) == T,
                   "exact maximal constant-return count")
    checks.require(T <= (center(q).bit_length()-2)//38, "fixed-source repetition height budget")
    next_state, next_gap = odd_step(r)
    checks.require(next_gap != R_WORD[0] and next_state > 0,
                   "no additional constant return at the endpoint")

    tail = replay(r, [1]*(s-1), checks)
    v = 2*3**(s-1)*t-1
    checks.require(tail[-1] == v and v < (1 << (2*(s+K))),
                   "complete actual gap-one tail and height bound")
    checks.require(32*K+108 < 3**(K+6), "exact actual scalar tail comparison")
    lower_tail = Fraction(1, 2)
    upper_tail = lower_tail+Fraction(8*K+27, 6*3**(K+5))
    bit_upper = lower_tail+(Fraction(v.bit_length()+3, 3)-lower_tail)/3**(s-1)
    checks.require(lower_tail < bit_upper <= upper_tail < Fraction(5, 8),
                   "unconditional actual tail scalar enclosure")
    intervals = []
    for j in range(T+1):
        scalar_denominator = 3**(24*(T-j))
        lo = Fraction(7, 8)+(lower_tail-Fraction(7, 8))/scalar_denominator
        hi = Fraction(7, 8)+(upper_tail-Fraction(7, 8))/scalar_denominator
        intervals.append((lo, hi))
        checks.require(Fraction(1, 2) <= lo < hi < Fraction(7, 8),
                       "actual boundary scalar interval below exceptional phase")
    for j in range(T):
        lo, hi = intervals[j]
        lo_next, hi_next = intervals[j+1]
        checks.require(lo > hi_next, "strict actual scalar decrease between returns")
        checks.require(Fraction(boundaries[j+1], 1)/hi_next > Fraction(boundaries[j], 1)/lo,
                       "strict actual q-over-h increase from disjoint enclosures")
        if j < T-1:
            checks.require(v2(boundaries[j]+7) == v2(boundaries[j+1]+7) == 34,
                           "valuation correction unchanged at both compared endpoints")
    check_tower_boundaries(boundaries, [11]*T, checks, use_small_rho=True)
    return {"prescribed_returns": T, "constant_valuation_comparisons": T-1,
            "source_bits": q.bit_length(), "source_bit_bound": 62*T+7,
            "initial_center_valuation": v2(center(q)),
            "compared_endpoint_source_ratio_floor": boundaries[T-1]//q,
            "odd_prefix_steps": K, "tail_gap_one_steps": s-1}


def run_checks():
    checks = Checks()
    checks.require((A, BINARY, DISTANCE, CONSTANT) ==
                   (282429536481, 274877906944, 7551629537, 1478790549031),
                   "exact expanding-return constants")
    checks.require(LAMBDA**5 < 2 and RHO*LAMBDA**10 < 1 < RHO*LAMBDA**11,
                   "exact growth and paid-budget comparisons")

    rank_rows = []
    for desired in [1, 2, 33, 34, 35, 38, 39, 40, 76, 77, 78, 114, 115, 153, 381]:
        modulus = 1 << (desired+1)
        q = (((1 << desired)-CONSTANT)*pow(DISTANCE, -1, modulus)) % modulus
        checks.require(q > 0 and q % 2 == 1 and v2(center(q)) == desired,
                       "exact chosen repetition-rank source")
        count = repetition_count(q)
        endpoint = replay(q, R_WORD*count, checks)[-1]
        checks.require(count == (desired-1)//38 and v2(center(endpoint)) == desired-38*count,
                       "maximal repetition rank at boundary cases")
        current, matched = endpoint, True
        for expected in R_WORD:
            current, gap = odd_step(current)
            if gap != expected:
                matched = False
                break
        checks.require(not matched, "next complete R word fails after maximal count")
        rank_rows.append({"valuation": desired, "returns": count})

    # Distinct first carry excursions, including large integer carry candidates.
    paid_words = [[1, 4], [1, 3, 5, 1], [1, 3, 4, 3, 4, 4],
                  [1, 1, 11, 1], [1, 1, 1, 31]]
    for word in paid_words:
        H, values = 7, [7]
        for gap in word:
            H = 3*H-8*gap
            values.append(H)
        first_low = next(i for i in range(1, len(values)) if values[i] in (5, 7))
        checks.require(values[1] == 13 and values[-1] == 7 and all(H > 4 for H in values),
                       "positive first-excursion candidate phases")
        checks.require(first_low == len(word) or
                       (first_low == len(word)-1 and values[first_low] == 5 and word[-1] == 1),
                       "first paid return with correct low normalization")
    mixed_schedules = [[0, 11, 1, 3, 15, 0, 7], [1, 2, 4, 8, 16, 32],
                       [11, 11, 10, 12, 0, 20, 2, 1]]
    for schedule_number, schedule in enumerate(mixed_schedules):
        words = [[2, 1]*m+paid_words[(i+schedule_number) % len(paid_words)]
                 for i, m in enumerate(schedule)]
        full_word = [gap for word in words for gap in word]
        q = cylinder_source(full_word)
        boundaries = [q]
        H = 7
        for word in words:
            states = replay(boundaries[-1], word, checks)
            for gap in word:
                H = 3*H-8*gap
                checks.require(H > 4, "positive candidate carries in mixed ordinary tower")
            checks.require(H == 7, "closed candidate return in mixed ordinary tower")
            boundaries.append(states[-1])
        check_tower_boundaries(boundaries, schedule, checks)

    tower_rows = [construct_flat_tower(T, checks) for T in [2, 3, 4, 8, 16, 32, 64, 128, 256]]
    return {
        "status": "PASS",
        "scope": "finite ordinary towers with unconditional real scalar enclosures; no exact seven-eighths realization",
        "exact_checks": sum(checks.counts.values()),
        "checks_by_category": dict(sorted(checks.counts.items())),
        "repetition_rank_boundary_cases": rank_rows,
        "mixed_arbitrary_paid_towers": len(mixed_schedules),
        "actual_flat_valuation_towers": tower_rows,
        "unproved": "a rank that cannot reset indefinitely across changing actual return types at one fixed positive ordinary source",
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), sort_keys=True, indent=2))
