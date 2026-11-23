#!/usr/bin/env python3
"""Exact finite controls for actual CRT scalar approximation and carry freedom."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json


class Checks:
    def __init__(self):
        self.counts = Counter()

    def need(self, condition, category):
        if not condition:
            raise RuntimeError(category)
        self.counts[category] += 1


def cylinder(word):
    clock = carry = 0
    for gap in word:
        carry = 3 * carry + 2**clock
        clock += gap
    modulus = 2**(clock + 1)
    residue = ((2**clock - carry) * pow(3**len(word), -1, modulus)) % modulus
    return residue, modulus, clock, carry


def realize(word, modulus, residue, checks):
    rho, binary_modulus, clock, carry = cylinder(word)
    multiple = 0 if modulus == 1 else ((residue - rho) * pow(binary_modulus, -1, modulus)) % modulus
    source = rho + binary_modulus * multiple
    checks.need(0 < source < modulus * binary_modulus and source % 2 == 1,
                'positive odd complete CRT representative')
    checks.need(source % modulus == residue % modulus,
                'prescribed odd source congruence')
    checks.need((3**len(word) * source + carry) % binary_modulus == 2**clock,
                'complete terminal-odd cylinder congruence')
    q = source
    states = [q]
    prefix_clock = prefix_carry = 0
    for expected in word:
        value = 3 * q + 1
        actual = (value & -value).bit_length() - 1
        checks.need(actual == expected, 'literal actual gap matches cylinder')
        q = value // 2**actual
        checks.need(q > 0 and q % 2 == 1, 'positive odd actual endpoint')
        prefix_carry = 3 * prefix_carry + 2**prefix_clock
        prefix_clock += expected
        states.append(q)
        checks.need(3**(len(states)-1) * source + prefix_carry == 2**prefix_clock * q,
                    'complete physical prefix identity')
    checks.need(q < (2 * modulus + 1) * 3**len(word),
                'endpoint height independent of supplied gap sizes')
    checks.need(source.bit_length() <= clock + modulus.bit_length() + 1,
                'CRT source bit-length payment')
    return source, q, states


def partial_scalar(word):
    return sum((F(gap, 3**(i+1)) for i, gap in enumerate(word)), F())


def enclosure(word, endpoint):
    p = partial_scalar(word)
    denominator = 3**len(word)
    return (p + F(1, 2 * denominator),
            p + F(endpoint.bit_length() + 3, 3 * denominator))


def target_word(target, length):
    shifted = target - F(1, 2)
    integer = shifted.__floor__()
    remainder = shifted - integer
    word = []
    for i in range(length):
        remainder *= 3
        digit = remainder.__floor__()
        remainder -= digit
        word.append(1 + digit + (3 * integer if i == 0 else 0))
    return integer, word, F(1, 2) + remainder


def run_checks():
    checks = Checks()
    approximation_cases = carry_cases = actual_steps = 0
    targets = [F(1,2), F(5,8), F(7,8), F(1), F(13,8), F(3), F(22,7)]
    congruences = [(1,0),(3,0),(3,1),(3,2),(5,3),(7,5),(9,4),(15,0),(31,17),(81,80)]
    lengths = [1,2,3,4,8,16,32]
    for target in targets:
        for modulus, residue in congruences:
            for length in lengths:
                integer, word, tail = target_word(target, length)
                checks.need(all(g >= 1 for g in word), 'positive target gap digits')
                checks.need(F(1,2) <= tail <= F(3,2), 'normalized target scalar tail')
                checks.need(partial_scalar(word) + tail / 3**length == target,
                            'exact target prefix and tail')
                source, endpoint, _ = realize(word, modulus, residue, checks)
                bound = F(4*length + 2*modulus.bit_length() + 5, 6 * 3**length)
                lo, hi = enclosure(word, endpoint)
                checks.need(max(abs(lo-target), abs(hi-target)) <= bound,
                            'unconditional enclosure certifies target approximation')
                checks.need(source.bit_length() <= 3*length + 3*integer + modulus.bit_length() + 1,
                            'linear source height for supplied target')
                approximation_cases += 1
                actual_steps += length

    words = [list(bits) for length in range(1,7) for bits in product((0,1), repeat=length)]
    words += [[int(j > 0 and j & (j-1) == 0) for j in range(length)]
              for length in (16,32,64,128)]
    for bits in words:
        gaps = [g for bit in bits for g in (2-bit,1+3*bit)]
        n = len(bits)
        checks.need(sum(gaps) == 3*n + 2*sum(bits), 'complete binary carry clock')
        checks.need(partial_scalar(gaps) + F(7,8*9**n) == F(7,8),
                    'arbitrary finite carry word has exact symbolic scalar')
        candidate = F(7,8)
        for i, gap in enumerate(gaps):
            candidate = 3*candidate-gap
            expected = F(5,8)+bits[i//2] if i%2 == 0 else F(7,8)
            checks.need(candidate == expected, 'bounded candidate scalar transport')
        modulus, residue = (9,4) if n%2 else (5,3)
        source, endpoint, _ = realize(gaps, modulus, residue, checks)
        lo, hi = enclosure(gaps, endpoint)
        bound = F(32*n+8*modulus.bit_length()+11,24*9**n)
        checks.need(max(abs(lo-F(7,8)),abs(hi-F(7,8))) <= bound,
                    'actual finite carry realization shadows seven eighths')
        carry_cases += 1
        actual_steps += 2*n

    return {'status':'PASS',
            'scope':'finite actual ordinary CRT realizations and unconditional scalar enclosures; no terminating-tail assumption',
            'target_approximation_cases':approximation_cases,
            'binary_carry_cases':carry_cases,
            'actual_odd_transitions':actual_steps,
            'exact_checks':sum(checks.counts.values()),
            'checks_by_category':dict(sorted(checks.counts.items())),
            'unproved':'arithmetic or periodicity of the actual scalar carries for one arbitrary fixed positive ordinary source'}


if __name__ == '__main__':
    print(json.dumps(run_checks(),sort_keys=True,indent=2))
