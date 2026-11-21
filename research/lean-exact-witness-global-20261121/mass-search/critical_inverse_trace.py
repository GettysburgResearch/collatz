#!/usr/bin/env python3
"""Exact finite-quotient replay for the critical positive-integer trace.

This computes the complete cylinder law on Z/(3**k) at the geometric gap
law P(a)=3/4**a, using the period of 2 modulo 3**k. All arithmetic is exact.
It checks finite identities, not the all-depth theorem or Collatz convergence.
"""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import argparse
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def critical_level(previous, k):
    modulus = 3 ** k
    lower = modulus // 3
    require(len(previous) == lower, 'incorrect preceding level')
    period = 2 * lower
    require(pow(2, period, modulus) == 1, 'incorrect modular period')
    denominator = 4 ** period - 1
    powers = []
    for a in range(1, period + 1):
        powers.append((pow(2, a, modulus), Fraction(9 * 4 ** (period - a), denominator)))
    values = []
    for n in range(modulus):
        value = Fraction(0)
        for power, weight in powers:
            residue = power * n % modulus
            if residue % 3 == 1:
                value += weight * previous[(residue - 1) // 3]
        values.append(value)
    require(sum(values) == modulus, 'cylinder law is not normalized')
    for n, value in enumerate(values):
        right = values[2 * n % modulus]
        if n % 3 == 2:
            right += 9 * previous[((2 * n - 1) // 3) % lower]
        require(4 * value == right, 'exact transfer identity failed')
        require(value >= 0, 'negative cylinder mass')
        if n % 3 == 0:
            require(value == 0, 'nonunit has a positive odd-predecessor mass')
    require(values[-1] >= Fraction(9, 4) ** k, 'negative fixed-point lower bound failed')
    return values


def negative_residual_example():
    source = 27
    parent = 2308
    trace = [source]
    odd_count = 0
    for _ in range(45):
        n = trace[-1]
        if n % 2:
            trace.append((3 * n + 1) // 2)
            odd_count += 1
        else:
            trace.append(n // 2)
    require(trace[-1] == 2 * parent and odd_count == 33, 'ordinary prefix mismatch')
    weight = Fraction(3 ** (2 * odd_count), 2 ** 90)
    threshold = Fraction(4 * (2 * parent + 1) ** 2, 4 * parent + 3)
    gap = 9235 * 3 ** 66 - 85266756 * 2 ** 90
    require(gap > 0 and weight > threshold, 'exact negative residual inequality failed')
    require(source < parent, 'the finite surplus packet does not give a smaller merger')
    return dict(parent=parent, predecessor=source, endpoint=trace[-1],
                shortcut_clock=45, odd_inputs=odd_count, ordinary_trace=trace,
                single_source_green_weight=str(weight), drift_threshold=str(threshold),
                integer_inequality='9235*3^66 > 85266756*2^90',
                positive_integer_difference=str(gap),
                conclusion='Raw W_2 drift is negative here; the same finite packet gives the smaller ordinary merger 27.',
                scope='Does not exclude a finite-core repair, a different weight, or supply global closure.')


def replay(max_depth):
    require(isinstance(max_depth, int) and 1 <= max_depth <= 6,
            'this finite replay accepts depths one through six')
    levels = [[Fraction(1)]]
    summaries = []
    for k in range(1, max_depth + 1):
        values = critical_level(levels[-1], k)
        levels.append(values)
        encoded = '\n'.join(str(v) for v in values).encode()
        summaries.append(dict(depth=k, ternary_modulus=3 ** k,
                              complete_residue_count=len(values),
                              density_sum=str(sum(values)),
                              vector_sha256=sha256(encoded).hexdigest(),
                              density_at_positive_one=str(values[1]),
                              density_at_negative_one=str(values[-1]),
                              negative_one_lower_bound=str(Fraction(9, 4) ** k)))
    targets = []
    for n in (1, 2, 3, 5, 7, 11, 27, 53, 81, 127):
        partial = sum(level[n % len(level)] for level in levels[1:])
        uniform_bound = Fraction(2 * n * n * (3 * n + 1) ** 2, 6 * n + 1)
        require(partial <= uniform_bound, 'finite trace exceeds the proved general bound')
        targets.append(dict(ordinary_target=n, finite_trace_sum=str(partial),
                            all_depth_upper_bound=str(uniform_bound)))
    return dict(status='PASS: exact finite quotient replay; not a Collatz proof',
                gap_law='P(a)=3/4^a, for every positive integer a',
                density='F_k(n)=3^k P(S_k congruent to n mod3^k)',
                max_depth=max_depth, levels=summaries, fixed_positive_targets=targets,
                exact_negative_residual=negative_residual_example(),
                all_depth_theorem_evidence='paper proof in SECTION_MASS_ATTACK.md; not inferred from this replay',
                warning='The negative residue -1 at each modulus is one fixed 3-adic target; its positive representatives change with k.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--depth', type=int, default=4)
    parser.add_argument('--receipt')
    args = parser.parse_args()
    result = replay(args.depth)
    result['source_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.receipt:
        Path(args.receipt).write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
