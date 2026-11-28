"""Exact finite-period moments and ordinary-source atoms for VARIATION_PROFILE.md."""
from collections import defaultdict
from fractions import Fraction
import hashlib
import json


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def advance_moment(row, power):
    q = len(row)
    period = 2 * q
    modulus = 3 * q
    divisor = (1 << (power * period)) - 1
    weights = [Fraction(3**power * (1 << (power * (period - e))), divisor)
               for e in range(1, period + 1)]
    newrow = []
    for residue in range(modulus):
        total = Fraction(0)
        u = residue
        for weight in weights:
            u = 2 * u % modulus
            if u % 3 == 1:
                total += weight * row[(u - 1) // 3]
        newrow.append(total)
    return newrow


def moment_check():
    summaries = []
    digest = hashlib.sha256()
    for power in (1, 2, 3):
        row = [Fraction(t**power) for t in range(3)]
        base = Fraction(1 + 2**power, 3)
        ratio = Fraction(3**(power - 1), 2**power - 1)
        for depth in range(5):
            average = sum(row, Fraction(0)) / len(row)
            require(average == base * ratio**depth, 'period-moment formula')
            summaries.append([power, depth, len(row), str(average)])
            for value in row:
                digest.update(f'{power},{depth},{value}\n'.encode())
            if depth < 4:
                row = advance_moment(row, power)
    return summaries, digest.hexdigest()


def physical_check():
    # The restriction on x belongs to this second, physical test only.
    rows = defaultdict(dict)
    edges = atoms = 0
    digest = hashlib.sha256()
    for x in range(1, 1024, 2):
        if x % 3 == 0:
            continue
        y, clock = x, 0
        survival = Fraction(1)
        for depth in range(13):
            mark = Fraction(3**depth * x, 2**clock * y)
            weight = Fraction(3**depth * (x % 3), 2**clock * y)
            require(mark == survival, 'original relative mark')
            require(weight == Fraction(x % 3, x) * survival, 'harmonic atom')
            target = rows[(y, depth)]
            require(mark not in target, 'two finite-grade sources share a mark')
            target[mark] = weight
            digest.update(f'{x},{depth},{clock},{y},{mark},{weight}\n'.encode())
            atoms += 1
            if depth < 12:
                n = 3 * y + 1
                gap = (n & -n).bit_length() - 1
                next_y = n >> gap
                survival *= Fraction(3 * y, n)
                y, clock = next_y, clock + gap
                edges += 1
    comparisons = 0
    for (y, depth), atoms_at_y in rows.items():
        successor = rows.get((y, depth + 1))
        if successor is not None:
            require(atoms_at_y.keys().isdisjoint(successor),
                    'adjacent grades at an ordinary target share a positive atom')
            comparisons += 1
    return {'ordinary_atoms': atoms, 'ordinary_edges': edges,
            'nonempty_adjacent_comparisons': comparisons,
            'atom_digest_sha256': digest.hexdigest()}


def main():
    moments, digest = moment_check()
    data = {'exact_period_moments_p_depth_period_mean': moments,
            'period_digest_sha256': digest, **physical_check()}
    print(json.dumps(data, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
