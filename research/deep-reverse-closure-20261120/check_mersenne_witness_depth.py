#!/usr/bin/env python3
"""Exact controls for W1--W2, using no witness-search implementation."""
from fractions import Fraction
import json


def need(ok, message):
    if not ok:
        raise ValueError(message)


def words_with_sum(total):
    if total == 0:
        yield ()
    else:
        for a in range(1, total+1):
            for suffix in words_with_sum(total-a):
                yield (a,)+suffix


def affine(word):
    A, D, m = 0, 1, 1
    for a in word:
        need(isinstance(a, int) and a >= 1, "inverse exponent must be positive")
        D = 2**a*D+m
        A += a
        m *= 3
    return A, D, m


def center(word):
    value = Fraction(7, 4)
    values = []
    for a in word:
        value = (2**a*value-1)/3
        if value.denominator != 1:
            return None
        need(value > 0, "nonpositive integral center state")
        values.append(int(value))
    return values


def small_A():
    tested = 0
    retained = []
    for A in range(2, 10):
        for word in words_with_sum(A):
            tested += 1
            values = center(word)
            if values is None:
                continue
            AA, D, m = affine(word)
            need(AA == A, "wrong inverse affine slope")
            endpoint = Fraction(11*2**(A-2)-D, m)
            need(endpoint == values[-1], "center affine reconstruction")
            slope = Fraction(2**(A+1), m)
            residue = (-D*pow(m, -1, 256)) % 256
            if slope <= Fraction(1024, 243) and residue in (65, 129, 193):
                retained.append(word)
                need(endpoint == 1, "low-A center exception")
    need(retained == [(2, 1, 2, 2, 2)], "unexpected cheap eligible center word")
    need(not set(range(1, 6)) & {65, 129, 193}, "high-A residue separation")
    return tested


def exponent_at_precision(H):
    need(H >= 5, "ternary precision below fixed progression")
    j, period = 0, 1
    for level in range(6, H+1):
        mod = 3**level
        candidates = [j+d*period for d in range(3)
                      if (4*pow(2, 119+162*(j+d*period), mod)-11) % mod == 0]
        need(len(candidates) == 1, "missing or nonunique ternary lift")
        j = candidates[0]
        period *= 3
    e = 119+162*j
    step = 162*period
    threshold = 4*H+11
    if e < threshold:
        e += ((threshold-e+step-1)//step)*step
    need(e % 162 == 119 and e >= threshold, "wrong ordinary exponent")
    need((4*pow(2, e, 3**H)-11) % 3**H == 0, "wrong ordinary ternary congruence")
    need(2**e > 1025*9**H, "slope/intercept separation bound")
    base = pow(2, 162, 3**H)
    need(pow(base, 3**(H-5), 3**H) == 1, "incorrect ternary subgroup order")
    if H > 5:
        need(pow(base, 3**(H-6), 3**H) != 1, "nonminimal ternary subgroup order")
    return e


def bounded_ordinary_control(H, e):
    maxA = 0
    while 243*2**(maxA+2) <= 1024*3**H:
        maxA += 1
    budget = maxA-H
    nodes = eligible = 0
    def walk(word, q, A, D, m):
        nonlocal nodes, eligible
        nodes += 1
        if q and 243*2**(A+1) <= 1024*m:
            residue = (-D*pow(m, -1, 256)) % 256
            if residue in (65, 129, 193):
                eligible += 1
                need(word == (2, 1, 2, 2, 2), "unexpected bounded-depth predecessor")
                need((A, D, m) == (9, 1165, 243), "original witness coefficients")
        if q == H:
            return
        for a in range(1, budget-(A-q)+2):
            next_A, next_D, next_m = A+a, 2**a*D+m, 3*m
            if (pow(2, next_A+e, next_m)-next_D) % next_m:
                continue
            walk(word+(a,), q+1, next_A, next_D, next_m)
    walk((), 0, 0, 1, 1)
    need(eligible == 1, "original witness missing or duplicated")
    return nodes, eligible


def precision_attempt():
    checked = 0
    for j in range(12):
        e = 119+162*j
        P = 2**e
        N = 4*P-11
        eta = 0
        Q = N
        while Q % 3 == 0:
            Q //= 3
            eta += 1
        need(eta >= 5, "initial ternary precision")
        Y = (512*P-1165)//243
        X = 2*Y-1
        h = eta-5
        v = Y
        for i in range(h+1):
            expected = Fraction(1)+Fraction(4,3)**i*(Y-1)
            need(v == expected, "precision-spending affine identity")
            if i:
                need(2*v-1 > X and v % 256 == 1, "height/binary guard was not lost")
            if i < h:
                need((4*v-1) % 3 == 0, "ineligible precision inverse")
                v = (4*v-1)//3
        need(v == 1+128*4**h*Q, "final precision quotient")
        need(v % 3 == (0 if Q % 3 == 1 else 2), "wrong precision exit branch")
        checked += 1
    return checked


def main():
    raw = 2**162-1
    valuation = 0
    while raw % 3 == 0:
        raw //= 3
        valuation += 1
    need(valuation == 5, "LTE base valuation")
    low_cases = small_A()
    lifts = []
    nodes = eligible = 0
    for H in range(5, 13):
        e = exponent_at_precision(H)
        lifts.append([H, e])
        if H <= 9:
            nn, ee = bounded_ordinary_control(H, e)
            nodes += nn
            eligible += ee
    print(json.dumps({
        "scope": "finite exact algebra and ordinary congruence controls for W1--W2; no all-depth witness selector",
        "low_total_exponent_words": low_cases,
        "ordinary_congruence_lifts": lifts,
        "bounded_inverse_nodes": nodes,
        "eligible_original_words": eligible,
        "strictly_cheaper_bounded_words": 0,
        "precision_spending_examples": precision_attempt(),
        "search_implementation_imported": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
