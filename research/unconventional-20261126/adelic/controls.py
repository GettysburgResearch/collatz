"""Exact finite checks for the periodic-window bounds, independent of Lean."""
from __future__ import annotations

from fractions import Fraction
from itertools import product
import json
from math import lcm
from random import Random


def require(test: bool, message: str) -> None:
    if not test:
        raise ArithmeticError(message)


def affine(word: str) -> tuple[int, int, int]:
    clock = len(word)
    grade = word.count('1')
    carry = sum(2**i * 3**word[i + 1:].count('1')
                for i, b in enumerate(word) if b == '1')
    return 2**clock, 3**grade, carry


def prescribed(word: str, value: Fraction) -> Fraction:
    for b in word:
        value = (3 * value + 1) / 2 if b == '1' else value / 2
    return value


def replay(word: str, start: int) -> list[int]:
    states = [start]
    for bit in word:
        x = states[-1]
        require(x % 2 == int(bit), 'incorrect ordinary parity')
        states.append((3 * x + 1) // 2 if bit == '1' else x // 2)
    return states


def positive_lift(word: str) -> int:
    modulus, multiplier, carry = affine(word)
    residue = (-carry * pow(multiplier, -1, modulus)) % modulus
    return residue or modulus


def encode(w: str, phase: int, n: int) -> str:
    return ''.join(w[(phase + i) % len(w)] for i in range(n))


def pin(w: str, phase: int) -> Fraction:
    n, m, c = affine(encode(w, phase, len(w)))
    return Fraction(c, n - m)


def v2(x: int) -> int:
    require(x != 0, 'v2(0)')
    x = abs(x)
    return (x & -x).bit_length() - 1


def integral(x: Fraction) -> int:
    require(x.denominator == 1, 'claimed integral numerator is fractional')
    return x.numerator


def shifted(word: str, D: int, z: Fraction, u: Fraction) -> int:
    n, m, c = affine(word)
    out = integral(D * (m * z + c - n * u))
    require(out == D * n * (prescribed(word, z) - u), 'cleared shift')
    return out


def exact_controls() -> dict:
    library = ('0', '1', '10', '101', '1110', '11000', '011101')
    phases = [(w, p, pin(w, p)) for w in library for p in range(len(w))]
    values = sorted({phase[2] for phase in phases})
    D = lcm(*(z.denominator for z in values))
    C1 = max(v2(integral(D * (z - u))) for z in values for u in values if z != u)
    C0 = 2 * max(abs(integral(D * z)) for z in values) + D
    require(D % 2 == 1, 'phase denominator is even')
    for w, p, z in phases:
        require(prescribed(encode(w, p, 1), z) == pin(w, p + 1), 'phase transition')
    cases = mismatch = inactive = 0
    # All hole words of length at most 7, every old phase and every new phase.
    for n in range(8):
        for bits in product('01', repeat=n):
            word = ''.join(bits)
            for w, p, z in phases:
                reference = encode(w, p, n)
                first = next((i for i in range(n) if word[i] != reference[i]), None)
                for u in values:
                    c = shifted(word, D, z, u)
                    require(abs(c) <= C0 * 3**n, 'archimedean hole bound')
                    if c:
                        require(0 <= v2(c) <= n + C1, 'valuation interval')
                    else:
                        inactive += 1
                    if first is not None:
                        require(c != 0 and v2(c) == first, 'first wrong shortcut')
                        mismatch += 1
                    cases += 1

    rng = Random(94628)
    telescope_count = fusion_count = 0
    for _ in range(2500):
        n_holes = rng.randrange(1, 7)
        refs = [rng.choice(phases)[:2] for _ in range(n_holes + 1)]
        good_lengths = [rng.randrange(11) for _ in refs]
        good = [encode(w, p, g) for (w, p), g in zip(refs, good_lengths)]
        holes = [''.join(rng.choice('01') for _ in range(rng.randrange(10)))
                 for _ in range(n_holes)]
        word = ''.join(g + h for g, h in zip(good, holes)) + good[-1]
        x = positive_lift(word) + rng.randrange(3) * 2**len(word)
        states = replay(word, x)
        q = states[-1]
        start_ref = pin(*refs[0])
        end_ref = pin(refs[-1][0], refs[-1][1] + good_lengths[-1])
        terms = [3**word.count('1') * integral(D * (x - start_ref))]
        starts, c_terms = [], []
        pos = 0
        for k, hole in enumerate(holes):
            pos += len(good[k])
            starts.append(pos)
            stop = pos + len(hole)
            w, phase = refs[k]
            z = pin(w, phase + len(good[k]))
            u = pin(*refs[k + 1])
            c = shifted(hole, D, z, u)
            c_terms.append(c)
            tail_multiplier = 3**word[stop:].count('1')
            terms.append(2**pos * tail_multiplier * c)
            # Direct per-hole relative comparison used in §3.
            b, d = states[pos], states[stop]
            beta = prescribed(hole, Fraction(0))
            ratio = abs(Fraction(terms[-1], D * 2**len(word) * q))
            require(ratio <= abs(z) / b + beta / d + abs(u) / d, 'real local bound')
            reciprocal = sum((Fraction(1, 3 * states[j]) for j in range(pos, stop)
                              if word[j] == '1'), Fraction(0))
            require(beta / d <= reciprocal, 'reciprocal distortion')
            pos = stop
        require(sum(terms) == (2**len(word)) * D * (q - end_ref), 'full telescope')
        telescope_count += 1
        for k in range(n_holes - 1):
            s1, s2 = starts[k], starts[k + 1]
            e1, e2 = s1 + len(holes[k]), s2 + len(holes[k + 1])
            w, p = refs[k]
            merged = shifted(word[s1:e2], D, pin(w, p + good_lengths[k]), pin(*refs[k + 2]))
            separated = (3**word[e1:e2].count('1') * c_terms[k]
                         + 2**(s2 - s1) * c_terms[k + 1])
            require(merged == separated, 'exact merged hole')
            fusion_count += 1

    max_clock = 512
    for L in (1, 2, 5, 31, 127, max_clock):
        states = replay('1' * L, 2**L - 1)
        require(states[-1] == 3**L - 1, 'sharp all-odd ordinary path')
        require(replay(('10' * L)[:L], 1)[-1] in (1, 2), 'small endpoint alternative')
    return {'common_phase_denominator': D, 'distinct_phases': len(values),
            'valuation_slack': C1, 'hole_cases': cases, 'wrong_bit_cases': mismatch,
            'zero_defect_cases': inactive, 'ordinary_window_telescopes': telescope_count,
            'neighboring_fusions': fusion_count, 'largest_sharpness_clock': max_clock}


if __name__ == '__main__':
    print(json.dumps(exact_controls(), indent=2, sort_keys=True))
