#!/usr/bin/env python3
"""Exact controls for the unrestricted-cycle attempt. No exclusion claim."""
from fractions import Fraction
from math import gcd
import json

def require(condition, message):
    if not condition:
        raise ValueError(message)


def numerator(word):
    s = 0
    total = 0
    p = len(word)
    for i, e in enumerate(word):
        require(e >= 1, 'e >= 1')
        total += 3 ** (p - 1 - i) * 2 ** s
        s += e
    return total

def v2(x):
    require(x > 0, 'x > 0')
    return (x & -x).bit_length() - 1

def inspect(word):
    p, A = (len(word), sum(word))
    D, C = (2 ** A - 3 ** p, numerator(word))
    require(D > 0 and gcd(D, 6) == 1, 'D > 0 and gcd(D, 6) == 1')
    q = Fraction(C, D)
    q0 = q
    rational_states = []
    lambdas = []
    for i, e in enumerate(word):
        require(q > 0 and q.numerator % 2 == q.denominator % 2 == 1, 'q > 0 and q.numerator % 2 == q.denominator % 2 == 1')
        rational_states.append(q)
        lambdas.append(3 * q / (3 * q + 1))
        q = (3 * q + 1) / 2 ** e
        rotation = word[i + 1:] + word[:i + 1]
        require(q == Fraction(numerator(rotation), D), 'q == Fraction(numerator(rotation), D)')
    require(q == q0, 'q == q0')
    rho = Fraction(1)
    for factor in lambdas:
        rho *= factor
    require(rho == Fraction(3 ** p, 2 ** A), 'rho == Fraction(3 ** p, 2 ** A)')
    modulus = 2 ** (A + 1)
    source = C * pow(D, -1, modulus) % modulus
    require(source > 0 and source % 2 == 1, 'source > 0 and source % 2 == 1')
    endpoint = source
    for e in word:
        require(v2(3 * endpoint + 1) == e, 'v2(3 * endpoint + 1) == e')
        endpoint = (3 * endpoint + 1) // 2 ** e
        require(endpoint > 0 and endpoint % 2 == 1, 'endpoint > 0 and endpoint % 2 == 1')
    require(2 ** A * (endpoint - source) == C - D * source, '2 ** A * (endpoint - source) == C - D * source')
    transfer_checks = 0
    for j in range(1, p):
        if word[j] >= 2:
            changed = list(word)
            changed[j] -= 1
            changed[j - 1] += 1
            delta = numerator(changed) - C
            require(delta == 3 ** (p - 1 - j) * 2 ** sum(word[:j]), 'delta == 3 ** (p - 1 - j) * 2 ** sum(word[:j])')
            require(gcd(delta, D) == 1, 'gcd(delta, D) == 1')
            transfer_checks += 1
    return {'word': word, 'odd_period': p, 'valuation_total': A, 'full_denominator': str(D), 'full_numerator': str(C), 'gcd': str(gcd(C, D)), 'rational_minimum': str(min(rational_states)), 'integer_cycle': C % D == 0, 'one_original_integer_source': str(source), 'actual_endpoint_after_word': str(endpoint), 'original_source_returns': endpoint == source, 'exact_unit_transfer_checks': transfer_checks}
words = [[2, 2], [1, 2, 2], [1, 1, 3, 2]]
words.append([65 * (i + 1) // 41 - 65 * i // 41 for i in range(41)])
rows = [inspect(word) for word in words]
require(rows[0]['integer_cycle'] and rows[0]['original_source_returns'], "rows[0]['integer_cycle'] and rows[0]['original_source_returns']")
require(all((not row['integer_cycle'] for row in rows[1:])), "all((not row['integer_cycle'] for row in rows[1:]))")
require(all((not row['original_source_returns'] for row in rows[1:])), "all((not row['original_source_returns'] for row in rows[1:]))")
require(numerator([3, 1]) == 11 and numerator([2, 2]) == 7, 'numerator([3, 1]) == 11 and numerator([2, 2]) == 7')
require(11 % 7 != 0, '11 % 7 != 0')
out = {'claim': 'Finite exact controls only; no arbitrary-cycle exclusion', 'rows': rows}
print(json.dumps(out, indent=2))
