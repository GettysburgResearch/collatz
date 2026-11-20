#!/usr/bin/env python3
"""Exact all-lift coefficient checks and bounded ordinary replays.

The rational renewal certificate covers every ternary unit residue, with an
analytic geometric bound for every omitted inverse exponent and two-run length.
It does not verify full Collatz or finite energy of the uncovered complement.
"""
from fractions import Fraction
from functools import lru_cache
import hashlib
import json

S_EXP = Fraction(21, 25)
ROUND_DEN = 10**12
TINY = Fraction(1, 2**160)
LIMIT = Fraction(249, 250)
# name, source prefix, target prefix, minimum final source exponent, extendable
SEEDS = (
    ('A', (2,), (5,), 4, True),
    ('B', (1, 1, 1), (1, 2, 5), 6, False),
    ('C', (1, 1, 2), (1, 5, 1), 4, False),
    ('D', (1, 1, 4), (1, 3, 5), 4, True),
    ('E', (3, 1, 1, 4), (2, 4, 1, 5), 4, True),
    ('F', (2, 1, 1, 4), (3, 2, 1, 5), 4, True),
    ('G', (3, 1, 1, 2), (2, 4, 3, 1), 4, False),
    ('H', (2, 1, 1, 2), (3, 2, 3, 1), 4, False),
)
# For inverse-fiber estimates, A uses the empty stem and a nonempty two-run.
STEMS = (('A', (), 1), ('D', (1, 1, 4), 0),
         ('E', (3, 1, 1, 4), 0), ('F', (2, 1, 1, 4), 0))
FIXED = tuple(row for row in SEEDS if not row[4])


def require(condition, message):
    if not condition:
        raise ValueError(message)


def v2(n):
    require(n > 0, 'positive valuation input')
    return (n & -n).bit_length() - 1


@lru_cache(None)
def correction(prefix):
    """Correction for the word prefix+(b,), independent of final b."""
    p = len(prefix) + 1
    total = 0
    position = 0
    for j in range(p):
        total += 3**(p - 1 - j) * 2**position
        if j < len(prefix):
            position += prefix[j]
    return total


def decode(c, p):
    """Unique positive odd-position prefix with correction c, if it exists."""
    require(type(c) is int and c > 0 and type(p) is int and p >= 1,
            'decode domain')
    prefix = []
    for exponent in range(p - 1, 0, -1):
        remainder = c - 3**exponent
        if remainder <= 0 or remainder % 2:
            return None
        a = v2(remainder)
        prefix.append(a)
        c = remainder >> a
    return tuple(prefix) if c == 1 else None


def extended(row, r):
    name, source, target, bmin, extendable = row
    require(type(r) is int and r >= 0 and (extendable or r == 0),
            'extension domain')
    if r == 0:
        return source, target, bmin
    require(sum(target) - sum(source) == 3 and target[-1] >= 2,
            'extension hypotheses')
    return (source + (2,)*r,
            target[:-1] + (target[-1] - 1,) + (2,)*(r-1) + (3,),
            bmin)


def inverse(endpoint, word):
    require(type(endpoint) is int and endpoint > 0 and endpoint % 2,
            'positive odd inverse endpoint')
    n = endpoint
    for a in reversed(word):
        require(type(a) is int and a >= 1, 'positive integer exponent')
        numerator = (n << a) - 1
        require(numerator % 3 == 0, 'nonintegral inverse')
        n = numerator // 3
        require(n > 0 and n % 2, 'positive odd inverse output')
    return n


def replay(n, word, endpoint, first_hit=False):
    require(n > 0 and n % 2, 'positive odd replay source')
    for a in word:
        require(not first_hit or n != 1, 'not a first-hit word')
        numerator = 3*n + 1
        require(v2(numerator) == a, 'wrong exact valuation')
        n = numerator >> a
    require(n == endpoint, 'wrong endpoint')


@lru_cache(None)
def log2_mod_3(q, k):
    require(k >= 1 and 0 < q < 3**k and q % 3, 'discrete-log domain')
    if k == 1:
        return 0 if q == 1 else 1
    old_modulus = 3**(k-1)
    e = log2_mod_3(q % old_modulus, k-1)
    old_order = 2*3**(k-2)
    candidates = [e+j*old_order for j in range(3)
                  if pow(2, e+j*old_order, 3**k) == q]
    require(len(candidates) == 1, 'unique ternary digit lift')
    return candidates[0]


def first_congruent_exponent(q, prefix, bmin, available_digits):
    p, offset = len(prefix)+1, sum(prefix)
    used = min(p, available_digits)
    modulus = 3**used
    order = 2*3**(used-1)
    residue = correction(prefix) * pow(q, -1, modulus) % modulus
    b = (log2_mod_3(residue, used) - offset) % order
    if b < bmin:
        b += ((bmin-b+order-1)//order)*order
    # If the first legal inverse is divisible by 3, it cannot be a source.
    if p < available_digits:
        high_modulus = 3**(p+1)
        if (pow(2, offset+b, high_modulus)*q - correction(prefix)) % high_modulus == 0:
            b += 2*3**(p-1)
    return b


@lru_cache(None)
def power_upper(value):
    """Rational upper enclosure of value^(21/25), proved by integers."""
    require(isinstance(value, Fraction) and 0 < value <= 1, 'power domain')
    rhs = ROUND_DEN**25 * value.numerator**21
    denominator_power = value.denominator**21
    low, high = 0, ROUND_DEN
    while low+1 < high:
        middle = (low+high)//2
        if middle**25 * denominator_power >= rhs:
            high = middle
        else:
            low = middle
    require(high**25 * denominator_power >= rhs, 'power enclosure')
    require(low**25 * denominator_power < rhs, 'power lower witness')
    return Fraction(high, ROUND_DEN)


def geometric_upper(period):
    # 2^(-period*21/25) <= 2^(-floor(period*21/25)).
    exponent = min((period*21)//25, 160)
    require(exponent >= 1, 'geometric exponent')
    return 1 / (1 - Fraction(1, 2**exponent))


def finite_weight(q, k, prefix, bmin):
    p, offset, c = len(prefix)+1, sum(prefix), correction(prefix)
    b = first_congruent_exponent(q, prefix, bmin, k)
    clock = offset+b
    # Here C < 2^(clock-1) and 3^p < 2^(2p), so the ratio is
    # < 2^(1+2p-clock) <= 2^-200. Its 21/25 power is <= 2^-168.
    if clock >= max(c.bit_length()+1, 2*p+201):
        power = TINY
    else:
        ratio = Fraction(5*3**p, 5*2**clock-c)
        power = power_upper(ratio)
    return power * geometric_upper(2*3**(p-1))


def tail_weight(q, k, stem):
    # For r>=k, integrality implies q*2^(b-2)=1 mod3^k.
    order = 2*3**(k-1)
    b = (2-log2_mod_3(q, k)) % order
    if b < 4:
        b += ((4-b+order-1)//order)*order
    length, offset = len(stem), sum(stem)
    if b >= 2*(length+1)+210:
        power = TINY
    else:
        ratio = Fraction(5*3**(length+1), 2**offset*(5*2**b-4))
        power = power_upper(ratio)
    gamma = power_upper(Fraction(3, 4))
    return (power * gamma**k / (1-gamma)
            * geometric_upper(2*3**k))


def pressure_bound(q, k):
    require(k >= 5 and 0 < q < 3**k and q % 3, 'pressure cell domain')
    bound = Fraction(0)
    for _, stem, first_r in STEMS:
        for r in range(first_r, k):
            bound += finite_weight(q, k, stem+(2,)*r, 4)
        bound += tail_weight(q, k, stem)
    for _, prefix, _, bmin, _ in FIXED:
        bound += finite_weight(q, k, prefix, bmin)
    return bound


def pressure_certificate():
    # The starting cells are all units modulo 3^5. Replacing a cell by
    # its three ternary lifts preserves a disjoint exhaustive cover.
    pending = [(q, 5) for q in range(1, 3**5) if q % 3]
    leaves = []
    splits = []
    while pending:
        q, k = pending.pop()
        upper = pressure_bound(q, k)
        if upper < LIMIT:
            leaves.append((q, k, upper))
        else:
            require(k < 20, 'unclosed pressure cell')
            splits.append((q, k))
            pending.extend((q+j*3**k, k+1) for j in range(3))
    require(sum(Fraction(1, 3**k) for _, k, _ in leaves) == Fraction(2, 3),
            'complete normalized residue mass')
    require(len(leaves) == 162 + 2*len(splits), 'tree leaf accounting')
    return sorted(leaves), sorted(splits)


def parse_block(word, start):
    # The eight families are prefix-disjoint, including their variable runs.
    found = []
    for row in SEEDS:
        _, base, _, _, can_extend = row
        if tuple(word[start:start+len(base)]) != base:
            continue
        r = 0
        position = start+len(base)
        if can_extend:
            while position < len(word) and word[position] == 2:
                r += 1
                position += 1
        source, target, bmin = extended(row, r)
        if position < len(word) and word[position] >= bmin:
            b = word[position]
            delta = sum(target)-sum(source)
            found.append((position+1, target+(b-delta,)))
    require(len(found) <= 1, 'ambiguous block parse')
    return found[0] if found else None


def compile_certificate(x, word):
    replay(x, word, 1, first_hit=True)
    position = 0
    output = ()
    while position < len(word):
        block = parse_block(word, position)
        if block is None:
            return {'status': 'UNRESOLVED'}
        position, new_word = block
        output += new_word
    output += (4,)
    replay(5*x, output, 1, first_hit=True)
    return {'status': 'CERTIFIED', 'word': output}


def main():
    algebra = 0
    ordinary = 0
    compiled = 0
    for row in SEEDS:
        for r in range(9 if row[4] else 1):
            prefix, target, bmin = extended(row, r)
            require(correction(target) == 5*correction(prefix), 'correction identity')
            require(decode(5*correction(prefix), len(prefix)+1) == target,
                    'complete decoding identity')
            require(sum(target)-sum(prefix) == bmin-1 or
                    (bmin == 4 and sum(target)-sum(prefix) == 3), 'final positivity')
            algebra += 1
            if r > 3:
                continue
            for q in range(1, 102, 2):
                if q % 3 == 0:
                    continue
                p = len(prefix)+1
                b = first_congruent_exponent(q, prefix, bmin, p+1)
                source_word = prefix+(b,)
                target_word = target+(b-sum(target)+sum(prefix),)
                x = inverse(q, source_word)
                require(x % 3 != 0, 'source unit guard')
                require(inverse(5*q, target_word) == 5*x, 'paired inverse')
                replay(x, source_word, q)
                replay(5*x, target_word, 5*q)
                require(3*q <= x, 'common smaller endpoint bound')
                ordinary += 1
                if q == 1:
                    result = compile_certificate(x, source_word)
                    require(result['status'] == 'CERTIFIED', 'single block compiler')
                    compiled += 1
    # Build eight complete multi-block certificates from their endpoint back.
    for shift in range(8):
        word = ()
        x = 1
        for index in range(8):
            row = SEEDS[(index+shift) % len(SEEDS)]
            prefix, _, bmin = extended(row, index % 3 if row[4] else 0)
            b = first_congruent_exponent(x, prefix, bmin, len(prefix)+2)
            block = prefix+(b,)
            x = inverse(x, block)
            word = block+word
        result = compile_certificate(x, word)
        require(result['status'] == 'CERTIFIED', 'composed compiler')
        require(len(result['word']) == len(word)+1, 'exact odd-count transport')
        require(sum(result['word']) == sum(word)+4, 'exact shortcut clock')
        compiled += 1
    require(compile_certificate(5, (4,))['status'] == 'UNRESOLVED',
            'known unresolved source')
    rejected = 0
    for action in (lambda: replay(5, (3,), 1, True),
                   lambda: inverse(1, (0,)),
                   lambda: extended(SEEDS[1], 1),
                   lambda: inverse(1, (1,))):
        try:
            action()
        except ValueError:
            rejected += 1
        else:
            raise ValueError('damaged control accepted')
    parts = [Fraction(1, 24), Fraction(1, 256), Fraction(1, 128),
             Fraction(1, 384), Fraction(1, 3072), Fraction(1, 1536),
             Fraction(1, 1024), Fraction(1, 512)]
    require(sum(parts) == Fraction(23, 384), 'cylinder density')
    leaves, splits = pressure_certificate()
    max_cell = max(leaves, key=lambda item: item[2])
    max_upper = max_cell[2]
    envelope = Fraction(996, 1000)
    require(max_upper < envelope, 'reported stronger rounded bound')
    serialized_cells = json.dumps([(q, k, str(v)) for q, k, v in leaves],
                                  separators=(',', ':')).encode()
    report = {
        'status': 'PASS',
        'scope': 'complete residue pressure certificate; bounded ordinary replays; no full Collatz proof',
        'algebraic_instances': algebra,
        'paired_ordinary_replays': ordinary,
        'complete_certificate_compilations': compiled,
        'rejected_malformed_controls': rejected,
        'unresolved_valid_control': {'source': 5, 'word': [4]},
        'relative_unit_density': '23/384',
        'renewal_exponent': '21/25',
        'renewal_coefficient': '249/250',
        'pressure_certificate': {
            'initial_modulus': 243,
            'initial_cells': 162,
            'terminal_cells': len(leaves),
            'split_cells': splits,
            'largest_ternary_depth': max(k for _, k, _ in leaves),
            'normalized_cover_mass': '2/3',
            'maximum_cell': {'residue': max_cell[0], 'depth': max_cell[1]},
            'strict_maximum_upper_envelope': '249/250',
            'exact_cells_sha256': hashlib.sha256(serialized_cells).hexdigest(),
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
