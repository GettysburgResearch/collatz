"""Exact independent checks for the quadratic-residue physical cycle theorem."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json
from math import gcd
from random import Random


def check(test, label):
    if not test:
        raise ValueError(label)


def carry(word):
    value = 0
    for i, bit in enumerate(word):
        if bit:
            value = 3 * value + (1 << i)
    return value


def rotate(word, first):
    return word[first:] + word[:first]


def distance(word, shift):
    return sum(a != b for a, b in zip(word, rotate(word, shift)))


def paley(n):
    residues = {i * i % n for i in range(1, n)}
    return [int(i in residues) for i in range(n)]


def blocks(length, weight):
    entries = []
    for places in combinations(range(length), weight):
        ones = set(places)
        bits = [int(i in ones) for i in range(length)]
        entries.append((bits, carry(bits)))
    return entries


def resultant_binomial(p, q, u, coeffs):
    """P^deg times norm, by multiplication in Q[X]/(X^u-Q/P)."""
    coeffs = {i: c for i, c in coeffs.items() if c}
    check(bool(coeffs), 'zero polynomial')
    degree = max(coeffs)
    matrix = [[Fraction(0) for _ in range(u)] for _ in range(u)]
    base = Fraction(q, p)
    for j in range(u):
        for exponent, coefficient in coeffs.items():
            power, rem = divmod(exponent + j, u)
            matrix[rem][j] += coefficient * base ** power
    determinant = Fraction(1)
    for i in range(u):
        j = next((j for j in range(i, u) if matrix[j][i]), None)
        if j is None:
            return 0
        if i != j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            determinant = -determinant
        pivot = matrix[i][i]
        determinant *= pivot
        for k in range(i + 1, u):
            scale = matrix[k][i] / pivot
            for col in range(i + 1, u):
                matrix[k][col] -= scale * matrix[i][col]
    resultant = p ** degree * determinant
    check(resultant.denominator == 1, 'resultant failed to be integral')
    return resultant.numerator


def exact_unaltered(counts):
    for n in (7, 11, 19, 23, 31):
        labels = paley(n)
        check(all(distance(labels, v) == (n + 1)//2 for v in range(1, n)),
              'wrong Paley shift correlations')
        for length in range(2, 8):
            q = 2**length
            for weight in range(1, length):
                p = 3**weight
                if p >= q:
                    continue
                entries = blocks(length, weight)
                S = (q**n - p**n) // (q - p)
                weights = [q**i * p**(n-1-i) for i in range(n)]
                select = sum(v for v, label in zip(weights, labels) if label)
                for (u, c0), (v, c1) in combinations(entries, 2):
                    total = c0*S + (c1-c0)*select
                    g = gcd(S, total)
                    check(g == gcd(S, c1-c0), 'exact template gcd')
                    counts['unaltered_template_pairs'] += 1
                    counts['unaltered_nonunit_gcd'] += int(g > 1)
                    if counts['unaltered_template_pairs'] % 197 == 0:
                        word = [bit for x in labels for bit in (v if x else u)]
                        check(carry(word) == total, 'direct raw carry')
                        counts['unaltered_direct_bit_replays'] += 1


def damaged(counts):
    rng = Random(245711)
    receipts = []
    cases = ((2, 1), (4, 2), (5, 3), (6, 2), (7, 3), (8, 5), (10, 5))
    menus = {pair: blocks(*pair) for pair in cases}
    for index in range(720):
        length, weight = cases[index % len(cases)]
        n = (7, 11, 19, 23, 31)[index % 5]
        q, p = 2**length, 3**weight
        c = (n+1)//4
        S = (q**n-p**n)//(q-p)
        labels = paley(n)
        (u0, c0), (u1, c1) = rng.sample(menus[length, weight], 2)
        delta = c1-c0
        counts['N_divides_carry_difference'] += int(delta % n == 0)
        base = [bit for lab in labels for bit in (u1 if lab else u0)]
        changed = base.copy()
        r = 1 + index % 2
        starts = []
        lengths = []
        errors = []
        occupied = set()
        for _ in range(r):
            h = rng.randrange(1, 4)
            choices = [a for a in range(n) if all((a+j)%n not in occupied for j in range(h))]
            a = rng.choice(choices)
            occupied.update((a+j)%n for j in range(h))
            positions = [(a*length+i) % len(base) for i in range(length*h)]
            before = [base[i] for i in positions]
            after = before.copy()
            rng.shuffle(after)
            for i, bit in zip(positions, after):
                changed[i] = bit
            counts['wraparound_intervals'] += int(a+h>n)
            counts['intervals_with_changed_cell_weights'] += int(any(
                sum(after[i:i+length]) != weight for i in range(0, len(after), length)))
            starts.append(a)
            lengths.append(h)
            errors.append(carry(after)-carry(before))
        H = max(lengths)
        B = delta * p**(H-1)
        E = [j*p**(H-h) for j, h in zip(errors, lengths)]
        C = carry(rotate(changed, starts[0]*length))
        g = gcd(S, C)
        d = (q**n-p**n)//gcd(q**n-p**n, C)
        check(d % (S//g) == 0, 'full original denominator')
        t = q * pow(p, -1, g) % g
        period = sum(pow(t, i, g) for i in range(n) if labels[i])
        check((B*period + sum(e * pow(t, a, g) for e, a in zip(E, starts))) % g == 0,
              'rotated common-cut physical carry')
        check((period*period+period+c) % g == 0, 'quadratic relation')
        def signed(s):
            return (s+n//2)%n - n//2
        K = 3 if 3**r < n else 2
        k, shifts = min(((j, [signed(j*a) for a in starts]) for j in range(1, K**r+1)),
                        key=lambda pair: max(map(abs, pair[1])))
        check(K*max(map(abs, shifts)) < n, 'simultaneous short multiple')
        T = max(map(abs, shifts))
        poly = Counter({2*T: c*B*B})
        for e, s in zip(E, shifts):
            poly[2*T+s] -= B*e
            for f, j in zip(E, shifts):
                poly[2*T+s+j] += e*f
        z = pow(t, pow(k, -1, n), g)
        check(sum(v*pow(z, i, g) for i, v in poly.items()) % g == 0, 'modular root')
        value = abs(resultant_binomial(p, q, k, poly))
        norm = sum(abs(v) for v in poly.values())
        degree = max(i for i, v in poly.items() if v)
        check(value and value % g == 0 and value <= q**degree * norm**k, 'nonzero resultant')
        check(max(map(abs, [B]+E)) <= 3**(H*length), 'clock normalization')
        check(norm <= (r*r+r+c)*3**(2*H*length), 'coefficient height')
        counts['damaged_resultants'] += 1
        counts['damaged_nonunit_gcd'] += int(g > 1)
        counts['negative_short_exponents'] += int(any(s < 0 for s in shifts))
        if g > 1 and len(receipts) < 6:
            receipts.append(dict(N=n, L=length, weight=weight, starts=starts,
                                 lengths=lengths, g=g, denominator_bits=d.bit_length(),
                                 resultant_bits=value.bit_length()))
    return receipts


def actual_shifts(counts):
    for n in (7, 11, 19, 23, 31, 43, 47, 59, 67, 71):
        labels = paley(n)
        for u0 in ([0, 1], [1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0, 1]):
            u1 = rotate(u0, 1)
            word = [bit for x in labels for bit in (u1 if x else u0)]
            for h in range(1, len(word)):
                v = h % len(u0)
                lower = (n+1)*distance(u0, v)//4 if v else (n+1)*distance(u0, 1)//2
                check(distance(word, h) >= lower, 'physical-shift lower bound')
                counts['physical_rotations'] += 1


def main():
    counts = Counter()
    exact_unaltered(counts)
    witnesses = damaged(counts)
    actual_shifts(counts)
    print(json.dumps({'scope':'Exact finite controls; no unknown ordinary cycle tested.',
                      'counts':dict(sorted(counts.items())),
                      'nontrivial_gcd_examples':witnesses}, indent=2))


if __name__ == '__main__':
    main()
