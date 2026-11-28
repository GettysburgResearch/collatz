"""Check physical rank spectra and complete denominator divisors with integers."""
from fractions import Fraction
from functools import cache
from math import gcd, lcm, prod
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def poly_remainder(coeffs, monic):
    work = list(coeffs)
    while len(work) >= len(monic):
        multiplier = work[-1]
        start = len(work) - len(monic)
        for k, coefficient in enumerate(monic):
            work[start + k] -= multiplier * coefficient
        require(work.pop() == 0, 'monic division')
    return work


@cache
def cyclotomic(n):
    poly = [-1] + [0] * (n - 1) + [1]
    for d in divisors(n)[:-1]:
        monic = cyclotomic(d)
        quot = [0] * (len(poly) - len(monic) + 1)
        for j in reversed(range(len(quot))):
            quot[j] = poly[j + len(monic) - 1]
            for k, coefficient in enumerate(monic):
                poly[j + k] -= quot[j] * coefficient
        require(not any(poly), 'exact cyclotomic division')
        poly = quot
    return tuple(poly)


def homogeneous(poly, a, b):
    deg = len(poly) - 1
    return sum(coef * a ** i * b ** (deg - i) for i, coef in enumerate(poly))


def primary_factors(n):
    primes = []
    for p in divisors(n)[1:]:
        if len(divisors(p)) == 2:
            q = p
            while n % (q * p) == 0:
                q *= p
            primes.append((p, q))
    return primes


def orbit(gaps, determinant):
    carry = date = 0
    for v in gaps:
        carry = 3 * carry + (1 << date)
        date += v
    z = carry
    least = largest = z
    minpos = 0
    for i, v in enumerate(gaps):
        if z < least:
            least, minpos = z, i
        largest = max(largest, z)
        require(z % 2 == 1 and (3 * z + determinant) % (1 << (v + 1)) == (1 << v),
                'true odd branch')
        z = (3 * z + determinant) >> v
    require(z == carry, 'closure')
    return carry, least, largest, minpos


def columns(gaps, a, b, g):
    result = [[0] * g for _ in range(b)]
    date = 0
    for i, gap in enumerate(gaps):
        rank = (i * a) % b
        delta = (i * a) // b - date
        require(-4 <= delta <= 4, 'finite fixture normalization')
        result[rank][i // b] = 1 << (4 - delta)
        date += gap
    return result


def active_orders(cols, g):
    return [k for k in divisors(g) if any(any(poly_remainder(col, cyclotomic(k))) for col in cols)]


def fixture(g, combined=False):
    # 485/306 is an upper convergent. Each changed column moves one native odd date.
    a, b = 485, 306
    slots = primary_factors(g)
    if combined:
        slots = [(g, g)]
    dates = []
    for i in range(g * b):
        rank, cell = i * a % b, i // b
        offset = 0
        for marker, (p, q) in enumerate(slots, 1):
            if rank == marker and cell % q < q // p:
                offset = 1
        dates.append(i * a // b - offset)
    dates.append(g * a)
    gaps = [y - x for x, y in zip(dates, dates[1:])]
    require(min(gaps) >= 1, 'ordered dates')
    determinant = (1 << (g * a)) - 3 ** (g * b)
    carry, minimum, maximum, minpos = orbit(gaps, determinant)
    check_orders = active_orders(columns(gaps, a, b, g), g)
    rotated = gaps[minpos:] + gaps[:minpos]
    cols = columns(rotated, a, b, g)
    active = active_orders(cols, g)
    require(active == check_orders and lcm(*active) == g, 'cyclic rank invariance and least period')
    if not combined:
        require(active == sorted({1} | {q for _, q in slots}), 'sharp primary mask')
    else:
        require(active == divisors(g), 'single point selector')
    scale = Fraction(1 << (a * g), 3 ** (b * g))
    require((scale * max(1, Fraction(maximum, 2 * minimum))) ** 4 < 2, 'true near-octave root')
    require(all(len(set(col)) <= 2 for col in cols), 'binary rank columns')
    A, B = 1 << a, 3 ** b
    factors = {k: homogeneous(cyclotomic(k), A, B) for k in divisors(g)}
    require(prod(factors.values()) == determinant, 'full homogeneous product')
    q = determinant // gcd(carry, determinant)
    inactive_product = prod(f for k, f in factors.items() if k not in active)
    upper = determinant // inactive_product
    require(carry % inactive_product == 0 and upper % q == 0, 'simultaneous inactive product')
    lower = prod(factors[k] // gcd(carry, factors[k]) for k in active)
    require(q % lower == 0, 'full active lower product including overlapping numerical factors')

    # Check the carry decomposition at the actual global minimum, over the whole determinant.
    v = pow(a, -1, b)
    u = (1 - v * a) // b
    W = A * pow(B, -1, determinant) % determinant
    X = pow(2, -u, determinant) * pow(3, -v, determinant) % determinant
    require(pow(X, b, determinant) * 2 % determinant == pow(W, v, determinant) and
            pow(X, a, determinant) * 3 % determinant == pow(W, -u, determinant),
            'two independent generators')
    evaluated = {}
    for col in {tuple(col) for col in cols}:
        val = 0
        for coef in reversed(col):
            val = (W * val + coef) % determinant
        evaluated[col] = val
    right = 0
    for r, col in enumerate(cols):
        right += pow(X, r, determinant) * pow(W, -(v * r // b), determinant) * evaluated[tuple(col)]
        right %= determinant
    require(right == minimum * 16 * pow(3, 1 - b * g, determinant) % determinant,
            'full composite rank identity')
    return {'g': g, 'h': a * g, 'active': active, 'degree': sum(len(cyclotomic(k)) - 1 for k in active),
            'q_bits': q.bit_length(), 'active_product_bits': upper.bit_length()}


def poly_product(polys):
    result = [1]
    for poly in polys:
        nxt = [0] * (len(result) + len(poly) - 1)
        for i, x in enumerate(result):
            for j, y in enumerate(poly):
                nxt[i + j] += x * y
        result = nxt
    return result


def all_binary_periods(g, orders):
    """Enumerate every binary row whose Fourier support is contained in orders."""
    recurrence = poly_product(cyclotomic(k) for k in orders)
    degree = len(recurrence) - 1
    require(degree <= g and recurrence[-1] == 1, 'cyclic monic recurrence')
    taps = [(j, -c) for j, c in enumerate(recurrence[:-1]) if c]
    joined = 1
    complete = 0
    for mask in range(1 << (degree - 1)):
        # A binary row or its complement starts with zero; their periods agree.
        values = [0] + [(mask >> j) & 1 for j in range(degree - 1)]
        for t in range(g - degree):
            next_bit = sum(c * values[t + j] for j, c in taps)
            if next_bit not in (0, 1):
                break
            values.append(next_bit)
        if len(values) != g:
            continue
        complete += 2
        least = next(k for k in divisors(g) if all(values[j] == values[j % k] for j in range(k, g)))
        joined = lcm(joined, least)
    return joined, complete


def exhaustive(g):
    """Rule out *any family* of binary rows below the claimed joint degree."""
    lower = 1 + sum(len(cyclotomic(q)) - 1 for _, q in primary_factors(g))
    divs = divisors(g)[1:]
    excluded = excluded_rows = 0
    for bits in range(1 << len(divs)):
        order_set = [1] + [d for j, d in enumerate(divs) if (bits >> j) & 1]
        degree = sum(len(cyclotomic(d)) - 1 for d in order_set)
        if degree >= lower or lcm(*order_set) != g:
            continue
        joined, rows = all_binary_periods(g, order_set)
        require(joined < g, 'no smaller active degree supports joint primitivity')
        excluded += 1
        excluded_rows += rows
    attaining = [1] + [q for _, q in primary_factors(g)]
    joined, attaining_rows = all_binary_periods(g, attaining)
    require(joined == g, 'all sharp support rows collectively give an actual least period')
    return {'g': g, 'minimum_degree': lower, 'smaller_candidate_subspaces': excluded,
            'binary_rows_in_smaller_subspaces': excluded_rows, 'binary_rows_in_sharp_subspace': attaining_rows}


def direct_binary_union(g):
    """Enumerate all binary words, then close their actual supports under union."""
    ds = divisors(g)
    weights = []
    for k in ds[1:]:
        basis = [poly_remainder([0] * j + [1], cyclotomic(k)) for j in range(g)]
        radix = 2 * sum(max(map(abs, vector), default=0) for vector in basis) + 2
        # Signed radix digits are bounded strictly below radix/2, so a zero
        # integer encodes exactly the zero algebraic remainder.
        weights.append([sum(c * radix ** j for j, c in enumerate(vector)) for vector in basis])
    evaluations = [0] * len(weights)
    masks = {1}
    last = 0
    for counter in range(1, 1 << g):
        word = counter ^ (counter >> 1)
        changed = word ^ last
        index = changed.bit_length() - 1
        sign = 1 if changed & word else -1
        support = 1
        for j, column in enumerate(weights):
            evaluations[j] += sign * column[index]
            if evaluations[j]:
                support |= 1 << (j + 1)
        masks.add(support)
        last = word
    unions = {1}
    for mask in masks:
        unions.update({existing | mask for existing in unions})
    degrees = []
    for mask in unions:
        selected = [k for j, k in enumerate(ds) if (mask >> j) & 1]
        if lcm(*selected) == g:
            degrees.append(sum(len(cyclotomic(k)) - 1 for k in selected))
    lower = 1 + sum(len(cyclotomic(q)) - 1 for _, q in primary_factors(g))
    require(min(degrees) == lower, 'direct all-words and all-column-unions minimum')
    return {'g': g, 'words': 1 << g, 'realized_supports': len(masks), 'joint_supports': len(unions),
            'minimum_degree': min(degrees)}


def main():
    rows = [fixture(g) for g in (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 30)]
    rows.extend(fixture(g, combined=True) for g in (4, 6, 12))
    tested_g = list(range(1, 19)) + [20, 21, 22, 24, 28, 30, 36, 40, 42, 60, 70, 84, 90, 105, 120, 210]
    print(json.dumps({'controls': rows, 'exhaustive_binary_spaces': [exhaustive(g) for g in tested_g],
                      'direct_all_binary_unions': [direct_binary_union(g) for g in range(1, 17)]}, indent=2))


if __name__ == '__main__':
    main()
