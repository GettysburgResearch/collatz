"""Finite checks of the arithmetic inputs to the ordinary trace calculation."""
from fractions import Fraction as Q
import hashlib
import json
from math import comb


def require(test, message):
    if not test:
        raise RuntimeError(message)


def odd_step(x):
    y = 3 * x + 1
    e = (y & -y).bit_length() - 1
    return y >> e, e


def folded_rows(depth):
    rows = [[Q(1)]]
    for k in range(depth):
        prev = rows[-1]
        m = 3 * len(prev)
        period = 2 * len(prev)
        common = (1 << period) - 1
        weight = [Q(3 * (1 << (period - e)), common) for e in range(1, period + 1)]
        row = [Q(0)] * m
        # Push a source residue forward by each folded choice for e.
        inv2 = pow(2, -1, m)
        factor = 1
        for w in weight:
            factor = factor * inv2 % m
            for x, value in enumerate(prev):
                row[(3 * x + 1) * factor % m] += w * value
        require(sum(row) == m and min(row) >= 0, 'period mass')
        # Separately resolve the one-bit recursion on every target.
        for a in range(m):
            rhs = row[2*a % m] / 2
            if 2*a % 3 == 1:
                rhs += 3 * prev[((2*a - 1)//3) % len(prev)] / 2
            require(rhs == row[a], 'one-bit recursion')
        rows.append(row)
    return rows


def first_return(a, n):
    x = a
    d = 0
    for k in range(1, n+1):
        x, e = odd_step(x)
        d += e
        if x == a:
            return k, Q(3**k, 2**d)
    return None


def first_hit_row(rows, a, n):
    ret = first_return(a, n)
    value = rows[n][a % len(rows[n])]
    if ret:
        k, mult = ret
        value -= mult * rows[n-k][a % len(rows[n-k])]
    return value


def literal_words(a, k, max_gap):
    frontier = [(a, 0, False)]
    for j in range(k):
        new = []
        for y, d, returned in frontier:
            for e in range(1, max_gap+1):
                numerator = (y << e) - 1
                if numerator % 3:
                    continue
                x = numerator // 3
                require(x > 0 and (x & 1) and odd_step(x) == (y, e), 'literal inverse')
                new.append((x, d + e, returned or x == a))
        frontier = new
    # x itself being a on a positive-length path is excluded too.
    require(len({x for x, _, _ in frontier}) == len(frontier), 'one source, one word')
    raw = sum(Q(3**k, 2**d) for _, d, _ in frontier)
    first = sum(Q(3**k, 2**d) for _, d, returned in frontier if not returned)
    return raw, first, len(frontier)


def main():
    rows = folded_rows(5)
    roots = list(range(1, 48, 2))
    literal_count = 0
    for root in roots:
        for k in range(1, 5):
            raw, first, count = literal_words(root, k, 12)
            literal_count += count
            exact = rows[k][root % len(rows[k])]
            exact_first = first_hit_row(rows, root, k)
            tail = Q(3**k*k, 2**12)  # Union bound for at least one gap > 12.
            require(0 <= exact - raw <= tail, 'ordinary raw enclosure')
            require(0 <= exact_first - first <= tail, 'ordinary first-hit enclosure')

    comparisons = 0
    for root in roots:
        x = root
        multiplier = Q(1)
        for length in range(1, 5):
            x, e = odd_step(x)
            multiplier *= Q(3, 2**e)
            for k in range(1, 6-length):
                lhs = rows[k+length][x % len(rows[k+length])]
                rhs = multiplier * rows[k][root % len(rows[k])]
                require(lhs >= rhs, 'distinguished finite path')
                comparisons += 1

    summaries = []
    for n in range(1, 6):
        cutoff = 3**n
        u = [first_hit_row(rows, a, n)/a for a in range(1, cutoff+1, 2)]
        v = [sum(first_hit_row(rows, a, k) for k in range(1, n+1))/(a*n)
             for a in range(1, cutoff+1, 2)]
        require(all(value >= 0 for value in u+v), 'nonnegative first-hit mass')
        # Check the exact negative-binomial clock bound used in (3).
        tail_prob = 1 - sum(Q(comb(d-1, n-1), 2**d) for d in range(n, 8*n+1))
        require(3**n*tail_prob <= (6*Q(3,4)**8)**n, 'large exponent bound')
        serialized = '|'.join(map(str, u+v)).encode()
        summaries.append({'depth':n, 'period':cutoff,
                          'first_and_averaged_sha256':hashlib.sha256(serialized).hexdigest()})
    print(json.dumps({'positive_odd_roots':len(roots),
                      'literal_odd_paths':literal_count,
                      'finite_path_lower_comparisons':comparisons,
                      'periodic_and_first_hit_rows':summaries}, indent=2))


if __name__ == '__main__':
    main()
