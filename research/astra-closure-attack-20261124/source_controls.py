"""Exact tests of the fixed-source identities; no numerical Subspace Theorem claim."""
from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import product
from math import gcd, lcm, prod
import json


def require(test, message):
    if not test:
        raise ValueError(message)


def actual_prefix(q, length):
    states, prefixes = [q], [0]
    for _ in range(length):
        x = 3*states[-1]+1
        gap = (x & -x).bit_length()-1
        states.append(x >> gap)
        prefixes.append(prefixes[-1]+gap)
    return states, prefixes


def outside(value, primes):
    value = abs(value)
    for p in primes:
        while value % p == 0:
            value //= p
    return value


def check_affine(x, k, counts):
    q, prefix = actual_prefix(x, k)
    terms = [3**k*x]+[3**(k-1-i)*2**prefix[i] for i in range(k)]
    maximum = 2**prefix[k]*q[k]
    require(sum(terms) == maximum and min(terms) > 0, ('affine', x, k))
    require(reduce(gcd, terms+[maximum]) == 1, ('primitive', x, k))
    require(Fraction(terms[0], terms[1]) == 3*x, ('start recovery', x, k))
    for primes in ((2, 3), (2, 3, 7), (2, 3, 5, 7, 13)):
        require(prod(outside(t, primes) for t in terms+[maximum]) ==
                outside(x, primes)*outside(q[-1], primes), ('outside mass', x, k))
        counts['outside_product_identities'] += 1
    require(sum(Fraction(t, maximum) for t in terms) == 1, ('unit equation', x, k))
    require(maximum % 3 != 0 and Fraction(maximum, 3**k).denominator == 3**k,
            ('reduced denominator', x, k))
    counts['primitive_positive_tuples'] += 1


def record_window(q, prefix, n, m, track, counts):
    y = 2**prefix[m]*(q[m]-track[-1])
    earlier = 3**(m-n)*2**prefix[n]*(q[n]-track[0])
    atoms = []
    for i in range(n, m):
        a = prefix[i+1]-prefix[i]
        t, u = track[i-n:i-n+2]
        if 3*t+1 == 2**a*u:
            counts['matched_virtual_edges'] += 1
            continue
        for coefficient, binary in ((3*t+1, prefix[i]), (-u, prefix[i+1])):
            if coefficient:
                atoms.append((binary, i, coefficient))
    scaled = [coefficient*2**binary*3**(m-i-1) for binary, i, coefficient in atoms]
    require(y-sum(scaled) == earlier, ('virtual telescope', q[0], n, m, track))
    require(all(abs(j-i) <= abs(d-b)+1 for b,i,_ in atoms for d,j,_ in atoms),
            ('time/clock separation', q[0], n, m))
    # Group close clock exponents as in the subsequence extraction, but
    # with a finite threshold just to exercise the level and ratio identity.
    grouped = []
    for binary,i,c in sorted(atoms, key=lambda entry: entry[0]):
        if not grouped or binary-grouped[-1][-1][0] > 2:
            grouped.append([])
        grouped[-1].append((binary,i,c))
    combined = []
    for cluster in grouped:
        b0, i0, _ = cluster[0]
        multiplier = sum(c*2**(b-b0)*Fraction(3)**(i0-i) for b,i,c in cluster)
        combined.append(multiplier*2**b0*3**(m-i0-1))
    require(sum(combined) == sum(scaled), 'cluster consolidation')
    counts['virtual_windows'] += 1
    counts['deleted_zero_clusters'] += sum(term == 0 for term in combined)



def check_unit_decomposition(q, prefix, n, m, counts):
    local = [3**(m-i-1) * 2**(prefix[i]-prefix[n]) for i in range(n, m)]
    length = m-n
    carry = 2**(prefix[m]-prefix[n])*q[m] - 3**length*q[n]
    require(carry == sum(local), ('local carry', n, m))
    # Include rational atoms with genuine denominators and allow nontrivial
    # P-smooth common factors in the primitive integer tuple.
    for repetitions, smooth_scale in ((2, 5), (3, 7), (6, 11)):
        atoms = [Fraction(smooth_scale*t, repetitions) for t in local for _ in range(repetitions)]
        c = smooth_scale*carry
        require(sum(atoms) == c and min(atoms) > 0, ('positive unit sum', n, m))
        den = lcm(*(u.denominator for u in atoms))
        cleared = [int(den*u) for u in atoms]
        common = reduce(gcd, cleared)
        require(gcd(common, den) == 1 and c % common == 0, ('least denominator', n, m))
        primitive = [t//common for t in cleared] + [-(den*c//common)]
        require(reduce(gcd, primitive) == 1 and sum(primitive) == 0, 'primitive rational tuple')
        require(max(map(abs, primitive)) == den*(c//common), 'primitive height')
        primes = (2, 3, 5, 7, 11)
        require(prod(outside(t, primes) for t in primitive) == outside(c//common, primes), 'outside units')
        virtual_sum = sum(Fraction(2**prefix[n], 3**m)*v/smooth_scale for v in atoms)
        require(virtual_sum == Fraction(2**prefix[m]*q[m], 3**m)-Fraction(2**prefix[n]*q[n], 3**n),
                ('two real normalizations', q[0], n, m))
        counts['positive_rational_carry_presentations'] += 1


def check_signed_controls(counts):
    # The fixed cycle has a two-term signed S-unit witness at every length,
    # even though positive S-unit length is unbounded by the external theorem.
    for length in range(1, 257):
        positive, negative = 4**length, 3**length
        carry = positive-negative
        require(sum(Fraction(t,positive) for t in (negative,carry)) == 1, length)
        require(Fraction(positive+negative, carry) <= 7, length)
        require(Fraction(carry,positive) == 1-Fraction(3,4)**length, length)
        counts['signed_cycle_controls'] += 1
    # Primitive signed presentations must retain a denominator/height cost;
    # exact zero subsums would invalidate Evertse and have to be removed.
    for exp in range(1, 11):
        terms = [Fraction(3**exp, 2), -Fraction(1, 2)]
        c = sum(terms)
        require(c.denominator == 1 and c>0, exp)
        den = lcm(*(t.denominator for t in terms))
        cleared = [int(t*den) for t in terms]
        common = reduce(gcd, map(abs, cleared))
        primitive = [v//common for v in cleared]+[-den*int(c)//common]
        require(max(map(abs,primitive)) == den*max([c]+list(map(abs,terms)))/common, exp)
        require(prod(outside(v,(2,3)) for v in primitive) == outside(int(c)//common,(2,3)), exp)
        counts['pruned_signed_tuple_controls'] += 1

def main():
    c = Counter()
    for x in range(1, 1000, 2):
        for k in range(1, 10):
            check_affine(x, k, c)
    for x in (1, 3, 5, 27, 97, 2**42-1):
        q, prefix = actual_prefix(x, 24)
        for j in range(8):
            for k in range(1, 12):
                check_unit_decomposition(q, prefix, j, j+k, c)
    menu = [Fraction(-1), Fraction(1), Fraction(5, 7), Fraction(-1, 3), Fraction(0)]
    for x in (1, 3, 7, 27, 31, 2**8-1, 2**44-1):
        q, prefix = actual_prefix(x, 30)
        for n,m in ((0,3),(4,7),(12,15)):
            for track in product(menu, repeat=m-n+1):
                record_window(q, prefix, n, m, track, c)
    require(c['deleted_zero_clusters'] > 0 and c['matched_virtual_edges'] > 0, c)
    # Exhibits the failure of any dimension-independent bound that also
    # covers repeated orbits, not an exceptional infinite injective example.
    for k in range(1, 257):
        q, prefix = actual_prefix(1, k)
        value = q[-1]*2**prefix[-1]
        require(value == 4**k and outside(q[0]*q[-1], (2,3)) == 1, k)
        c['growing_dimension_cycle_controls'] += 1
    check_signed_controls(c)
    print(json.dumps(dict(c), sort_keys=True))


if __name__ == '__main__':
    main()
