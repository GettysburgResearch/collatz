"""Exact finite controls for unrestricted odd-segment triple-product separation."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from math import prod


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def clocks(word):
    times = [0]
    for a in word:
        times.append(times[-1] + a)
    return times


def offsets(times, m):
    return [sum((F(3 ** (m - 1 - j), 2 ** (times[m-1] - times[j]))
                 for j in range(i, m)), F()) for i in range(m + 1)]


def coefficients(roots):
    result = [1]
    for root in roots:
        result = [old + new for old, new in zip(result + [0], [0] + [-root*r for r in result])]
    return result


def verify_aligned(word, a, b):
    times = clocks(word)
    k = len(a)
    counts = [a.count(i) - b.count(i) for i in range(len(times))]
    m = max(i for i, c in enumerate(counts) if c)
    require(sum(i*c for i, c in enumerate(counts)) == 0, 'index alignment')
    require(sum(t*c for t, c in zip(times, counts)) == 0, 'clock alignment')
    s = offsets(times, m)
    first = sum(c*v for c, v in zip(counts, s))
    if counts[m] % 3 == 0:
        return first
    L = len(word)
    M = 2*L + (2*k*L - 1).bit_length()
    prefix = F()
    for j in range(m):
        E = times[m-1] - times[m-1-j]
        d = sum(counts[:m-j])
        prefix += F(d * 3**j, 2**E)
        scaled = prefix * 2**E
        require(scaled.denominator == 1 and scaled.numerator % 3 == -counts[m]*2**E % 3,
                'prefix congruence')
    require(first == prefix and abs(first) >= F(1, 2**(L*M+1)), 'gap lower bound')
    return first


def all_aligned(word, k):
    times = clocks(word)
    buckets = defaultdict(list)
    pairs = 0
    for multiset in combinations_with_replacement(range(len(times)), k):
        key = sum(multiset), sum(times[i] for i in multiset)
        for previous in buckets[key]:
            verify_aligned(word, previous, multiset)
            pairs += 1
        buckets[key].append(multiset)
    return pairs


def high_path(word):
    times = clocks(word)
    L = len(word)
    H = 2 ** (8*(L+1)**2)
    mod = 2 ** (times[-1]+1)
    carry = sum(3**(L-1-j) * 2**times[j] for j in range(L))
    seed = ((2**times[-1]-carry) * pow(3**L, -1, mod)) % mod + mod*H
    states = [seed]
    for a in word:
        y = 3*states[-1]+1
        require((y & -y) == 2**a, 'native valuation')
        states.append(y // 2**a)
    require(min(states) > H, 'high real fixture')
    values = [prod(states[i] for i in inds)
              for inds in combinations_with_replacement(range(L+1), 3)]
    require(len(values) == len(set(values)), 'high real triple products')
    return len(values)


def main():
    pairs = sum(all_aligned(w, 3) for L in range(2, 6) for w in product((1, 2, 3), repeat=L))
    fixtures = [(1, 1, 1, 1, 1, 1, 1), (199, 1, 2, 199, 1, 2),
                (1, 501, 2, 1, 501, 2), (211, 97, 1, 211, 97, 1),
                (1, 2, 3, 1, 2, 1001)]
    pairs += sum(all_aligned(w, 3) for w in fixtures)
    high = sum(high_path(w) for w in fixtures)
    word = (1, 2, 2, 2, 1, 1, 2)
    a, b = (0, 0, 7, 7, 7), (1, 4, 4, 6, 6)
    require(verify_aligned(word, a, b) == 0, 'Paper 163 first-correction cancellation')
    s = offsets(clocks(word), len(word))
    A, B = (coefficients([s[i] for i in inds]) for inds in (a,b))
    require(A[1] == B[1] and A[2] != B[2], 'Paper 163 second correction')
    low = [245, 23, 35, 53, 5]
    require(all((3*x+1)//((3*x+1) & -(3*x+1)) == y for x,y in zip(low,low[1:])), 'low path')
    require(low[0]*low[-1]*low[1] == low[2]**2*low[1], 'low triple collision')
    print(f'{pairs} aligned triple comparisons, {high} high native products, higher and lower controls passed')


if __name__ == '__main__':
    main()
