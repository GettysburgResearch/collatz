"""Exact finite controls for the marked all-grade argument.

The cap applies to each displayed gap. Terminal rho_1 is kept exact.
All guards remain active under python -O. No asymptotic estimate is inferred.
"""

from collections import defaultdict
from fractions import Fraction as Q
from functools import cache
import json


GAP_CAP = 6
MAX_GRADE = 3


def require(test, message):
    if not test:
        raise ValueError(message)


def odd_rep(r, modulus):
    r %= modulus
    return r if r % 2 else r + modulus


def edges(z):
    for gap in range(1, GAP_CAP + 1):
        numerator = 2**gap * z - 1
        if numerator % 3 == 0:
            yield gap, numerator // 3


@cache
def words(z, length):
    if length == 0:
        return ((0, Q(0), z),)
    paths = []
    for gap, parent in edges(z):
        for clock, intercept, source in words(parent, length - 1):
            paths.append((gap + clock, (1 + 3 * intercept) / 2**gap, source))
    return tuple(paths)


def minmax_norm(first, second):
    bins = defaultdict(Q)
    for mass, sign in ((first, 1), (second, -1)):
        for site, value in mass.items():
            bins[site] += sign * value
    largest = Q(0)
    current = Q(0)
    for site in sorted(bins, reverse=True):
        current += bins[site]
        largest = max(largest, abs(current))
    return largest


@cache
def measure(z, length):
    atoms = defaultdict(Q)
    for clock, intercept, source in words(z, length):
        require(z == intercept + Q(3**length * source, 2**clock), 'affine word')
        atoms[intercept] += Q(3**length * (source % 3), 2**clock)
    return dict(atoms)


@cache
def size(z, depth):
    modulus = 3**(depth + 2)
    root = odd_rep(z, modulus)
    return minmax_norm(measure(root, depth + 1), measure(root, depth))


@cache
def atom_size(z, length):
    return max(measure(odd_rep(z, 3**(length + 1)), length).values(), default=Q(0))


def frozen_measure(z, length, freeze):
    atoms = defaultdict(Q)
    for clock, intercept, parent in words(z, freeze):
        atoms[intercept] += Q(3**freeze, 2**clock) * sum(measure(parent, length - freeze).values())
    return atoms


def by_residue_checks():
    controls = []
    for depth in range(MAX_GRADE + 1):
        q = 3**(depth + 2)
        k = depth // 2
        frozen_total = Q(0)
        mean_difference = Q(0)
        difference_total = Q(0)
        spacing_count = 0
        for r in range(q):
            z = odd_rep(r, q)
            for length in (depth, depth + 1):
                require(measure(z, length) == measure(z + 2 * q, length), 'periodicity')
                clocks = defaultdict(list)
                for total, intercept, source in words(z, length):
                    if source % 3:
                        clocks[total].append((intercept, source))
                for total, atoms in clocks.items():
                    step = Q(3**length, 2**total)
                    sites = sorted(x for x, _ in atoms)
                    for left, right in zip(sites, sites[1:]):
                        require(right - left >= step, 'fixed-clock source spacing')
                        spacing_count += 1
                next_atom = atom_size(z, length + 1)
                atom_bound = sum(Q(3, 2**e) * atom_size(x, length) for e, x in edges(z))
                require(next_atom <= atom_bound, 'largest atom transport')
            difference_total += size(z, depth)
            upper = frozen_measure(z, depth + 1, k)
            lower = frozen_measure(z, depth, k)
            frozen_total += minmax_norm(upper, lower)
            shorter = depth - k
            density = sum(measure(z, shorter + 1).values()) - sum(measure(z, shorter).values())
            mean_difference += abs(density)
        prefix_prob = sum(Q(1, 2**e) for e in range(1, GAP_CAP + 1)) ** k
        require(frozen_total <= prefix_prob * mean_difference, 'frozen mean contraction')
        controls.append({
            'grade': depth, 'odd_representatives': q, 'spacing_pairs': spacing_count,
            'period_average_marked_norm': str(difference_total / q),
            'frozen_average': str(frozen_total / q),
            'frozen_average_upper': str(prefix_prob * mean_difference / q),
        })
    return controls


def flux_checks():
    controls = []
    for depth in range(MAX_GRADE + 1):
        q = 3**(depth + 2)
        mean = sum(size(odd_rep(r, q), depth) for r in range(q)) / q
        b_old = sum(size(x, depth) / x for x in range(1, q + 1, 2))
        paid = sum(size(x, depth) / (x * (3 * x + 1)) for x in range(1, q + 1, 2))
        b_new = Q(0)
        incoming = defaultdict(Q)
        seen = defaultdict(set)
        interior = Q(0)
        edge_count = 0
        for z in range(1, 3 * q + 1, 2):
            b_new += size(z, depth + 1) / z
            row = Q(0)
            for e, x in edges(z):
                actual = 3 * x + 1
                require(actual % 2**e == 0 and actual % 2**(e + 1) != 0, 'physical exponent')
                weight = Q(3, 2**e * z)
                require(weight == Q(1, x) - Q(1, x * (3 * x + 1)), 'harmonic loss')
                row += weight * size(x, depth)
                edge_count += 1
                if x <= q:
                    interior += weight * size(x, depth)
                else:
                    require(x % q not in seen[e], 'exterior residue injection')
                    seen[e].add(x % q)
                    incoming[e] += weight * size(x, depth)
            require(size(z, depth + 1) / z <= row, 'physical CDF transport')
        require(all(v <= mean for v in incoming.values()), 'one exponent uses one residue period')
        influx = sum(incoming.values(), Q(0))
        require(interior <= b_old - paid, 'interior pays stopped loss')
        require(b_new + paid <= b_old + influx, 'moving cutoff flux')
        controls.append({
            'grade': depth, 'physical_edges': edge_count,
            'exterior_residue_pairs': sum(len(v) for v in seen.values()),
            'maximum_fixed_exponent_fraction_of_mean': str(max(incoming.values(), default=Q(0)) / mean),
            'moving_cutoff_inequality': True,
        })
    return controls


def main():
    out = {
        'scope': 'per-gap capped original inverse words with exact terminal selector; all checks use fractions',
        'gap_cap': GAP_CAP,
        'residue_checks': by_residue_checks(),
        'flux_checks': flux_checks(),
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
