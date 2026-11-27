"""Exact finite controls for actual centered-phase separation and realization."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json


def require(test, detail):
    if not test:
        raise ValueError(detail)


def step(q):
    numerator = 3 * q + 1
    gap = (numerator & -numerator).bit_length() - 1
    return gap, numerator >> gap


def carry(h):
    t = h - Fraction(1, 2)
    return (t.numerator - 1) // t.denominator


def centered(h):
    return h - carry(h) - Fraction(1, 2)


def scalar_table(bound):
    table = {1: Fraction(1)}
    for q in range(1, bound + 1, 2):
        trace = []
        while q not in table:
            require(len(trace) < 2000, 'unresolved finite trajectory')
            a, t = step(q)
            trace.append((q, a))
            q = t
        h = table[q]
        for start, a in reversed(trace):
            h = (a + h) / 3
            table[start] = h
    return table


def canonical_letter(q, table):
    a, t = step(q)
    return a + carry(table[t]) - 3 * carry(table[q])


def check_actual(table, counts):
    for q, h in table.items():
        a, t = step(q)
        b = canonical_letter(q, table)
        c, d = carry(h), carry(table[t])
        y, yp = centered(h), centered(table[t])
        require(1 <= b <= 3 and 0 < y < 1 and 3*y == b-1+yp, q)
        require(2**c <= q and a+d == b+3*c, q)
        require(2**(b+2*c)*Fraction(t, 2**d) == 3*Fraction(q, 2**c)+Fraction(1, 2**c), q)
        counts[f'actual_letter_{b}'] += 1
        if c and b == 1:
            counts['actual_one_steps_positive_carry'] += 1
        if c and not d and b == 1:
            counts['actual_one_steps_reset'] += 1
        for letter in (1, 3):
            end, length = q, 0
            while canonical_letter(end, table) == letter:
                end = step(end)[1]
                length += 1
                require(length <= len(table), q)
            if letter == 1:
                require(2**(length+1) <= q+1 and y*3**(length+1) > 1, q)
                if c == 0:
                    require((q+1) % 2**(length+1) == 0, q)
                else:
                    require(2**(length+c) <= q, q)
            else:
                require(4*8**length <= (5*q-1)*3**length, q)
                require((1-y)*3**(length+1) >= 1, q)
        # Check that the two nearest triadic grid distances use the actual
        # shifted scalar, retaining the distinct upper and lower remainders.
        end, digits = q, 0
        for n in range(10):
            rem = centered(table[end])
            require(3**n * y == digits+rem and 0 < rem < 1, q)
            require(2**n*(end+1) <= 3**n*(q+1), q)
            digits = 3*digits + canonical_letter(end, table)-1
            end = step(end)[1]
            counts['shifted_grid_cases'] += 1


def check_word(word):
    m = len(word)
    r = 0
    while 3**r < 8*(m+1):
        r += 1
    prescribed = word + (1,)*r
    q, modulus = 1, 2
    for a in reversed(prescribed):
        modulus <<= a
        q = (((q << a)-1)*pow(3, -1, modulus)) % modulus
    require(0 < q < 2**(sum(word)+r+1), word)
    end = q
    for a in prescribed:
        actual, end = step(end)
        require(actual == a, word)
    # The exact lower scalar bound is strict. The rational upper bound
    # substitutes bit_length for log2, with no convergence oracle.
    lo, hi = Fraction(1, 2), 1 + Fraction(end.bit_length(), 3)
    for a in reversed(prescribed[m:]):
        lo, hi = (a+lo)/3, (a+hi)/3
    require(lo >= Fraction(1, 2) and hi < Fraction(3, 2), word)
    for a in reversed(word):
        lo, hi = (a+lo)/3, (a+hi)/3
        require(lo >= Fraction(1, 2) and hi < Fraction(3, 2), word)
    return q


def check_sharpness():
    for k in range(2, 257):
        q = 2**k - 1
        end = q
        for i in range(k-1):
            require(end+1 == 2**(k-i)*3**i, k)
            a, end = step(end)
            require(a == 1, k)
        require(end == 2*3**(k-1)-1, k)
        bound = (Fraction(1, 2)+Fraction(end.bit_length(), 3))/3**(k-1)
        require(bound < 1 and bound <= 3*k*Fraction(1, 3**k), k)



def terminal_residue_table(m):
    modulus = 3**m
    lookup = {}
    for t in range(modulus):
        a, k = 2*t+1, 2-3*t+9*modulus
        numerator = (pow(2, a+2*k, 9*modulus) - pow(2, a, 9*modulus) - 3) % (9*modulus)
        require(numerator % 9 == 0, (m, t))
        residue = numerator // 9
        require(residue not in lookup, (m, residue))
        lookup[residue] = t
    require(len(lookup) == modulus, m)
    return lookup


def check_convergent_word(word, lookup):
    m = len(word)
    modulus = 3**m
    offset, binary, digits = 0, 1, 0
    for gap in word:
        offset = 3*offset+binary
        binary <<= gap
        digits = 3*digits+gap-1
    residue = (offset*pow(binary, -1, modulus)) % modulus
    t = lookup[residue]
    a, k = 2*t+1, 2-3*t+9*modulus
    z = (4**k-1)//3
    s = ((2**a)*z-1)//3
    require(s % modulus == residue and step(s) == (a, z) and step(z) == (2*k, 1), word)
    state, scalar = s, Fraction(3*a+2*k+1, 9)
    require(scalar == Fraction(8, 9)+2*modulus, word)
    for i in range(m-1, -1, -1):
        dest, next_scalar = state, scalar
        g = word[i]
        state, scalar = ((2**g)*state-1)//3, (g+scalar)/3
        require(step(state) == (g, dest) and state > 1, word)
        require(carry(scalar) == 2*3**i and g+carry(next_scalar)-3*carry(scalar) == g, word)
    require(centered(scalar) == (digits+Fraction(7, 18))/modulus, word)
    require(state.bit_length() <= sum(word)+5+18*modulus, word)
    return state.bit_length()


def check_two_step_fibers():
    cases = 0
    for d in range(1, 110):
        states = []
        for t in range(d):
            a, k = 2*t+1, 3*d-1-3*t
            z = (4**k-1)//3
            s = (2**a * z-1)//3
            require(step(s) == (a, z) and step(z) == (2*k, 1) and z > 1, (d, t))
            require(Fraction(3*a+2*k+1, 9) == Fraction(6*d+2, 9), (d, t))
            states.append(s)
        require(len(set(states)) == d, d)
        for modulus in (1, 3, 9, 27, 81, 243):
            hist = Counter(s % modulus for s in states)
            minimum = min(hist.values()) if len(hist) == modulus else 0
            require(max(hist.values())-minimum <= 1, (d, modulus))
            cases += 1
    return cases

def main():
    counts = Counter()
    table = scalar_table(3001)
    check_actual(table, counts)
    require(counts['actual_one_steps_positive_carry'] and counts['actual_one_steps_reset'], counts)
    largest = 0
    for m in range(1, 8):
        for w in product((1, 2, 3), repeat=m):
            largest = max(largest, check_word(w))
            counts['all_words_through_length_7'] += 1
    maxbits = 0
    for m in range(1, 10):
        lookup = terminal_residue_table(m)
        counts['terminal_permutation_cases'] += len(lookup)
        if m <= 7:
            for w in product((1, 2, 3), repeat=m):
                maxbits = max(maxbits, check_convergent_word(w, lookup))
                counts['convergent_prefix_witnesses'] += 1
    counts['largest_convergent_witness_bits'] = maxbits
    counts['two_step_fiber_modulus_checks'] = check_two_step_fibers()
    check_sharpness()
    print(json.dumps(dict(counts, distinct_actual_states=len(table), largest_constructed_source=largest,
                          sharpness_parameters=255), sort_keys=True))


if __name__ == '__main__':
    main()
