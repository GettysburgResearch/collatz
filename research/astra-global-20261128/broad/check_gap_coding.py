"""Small exact controls for gap numerators, finite regeneration, and source costs."""

from collections import Counter, defaultdict
from functools import cache
from itertools import combinations, product
from math import comb


def require(condition, message):
    if not condition:
        raise ValueError(message)


def compositions(n, maximum):
    for cuts in combinations(range(1, maximum + 1), n):
        yield tuple(v - u for u, v in zip((0,) + cuts[:-1], cuts))


def numerator(word):
    value = 0
    for j, e in enumerate(word):
        value = (1 << e) * value + 3**j
    return value


def source(word, terminal, modulus):
    return (3 ** len(word) * terminal + numerator(word)) * pow(2, -sum(word), modulus) % modulus


def step(x, e):
    q, r = divmod((x << e) - 1, 3)
    require(r == 0 and q % 3, 'illegal inverse edge')
    return q


def recover(word):
    n, s, c = len(word), sum(word), numerator(word)
    backwards = []
    while n > 1:
        v = c - 3 ** (n - 1)
        require(v > 0, 'missing odd factor')
        e = (v & -v).bit_length() - 1
        require(e > 0, 'nonpositive recovered gap')
        backwards.append(e)
        n, s, c = n - 1, s - e, v >> e
    require(c == 1 and s > 0, 'base numerator')
    return (s,) + tuple(reversed(backwards))


def numerator_control():
    checked = bins = 0
    for n in range(1, 7):
        q = 3**n
        fibers = defaultdict(list)
        for w in compositions(n, 15):
            c, s = numerator(w), sum(w)
            require(recover(w) == w, 'word recovery')
            require(c == sum(3**j * (1 << sum(w[j + 1:])) for j in range(n)), 'affine numerator')
            fibers[s, c % q].append(c // q)
            for y in (1, 2):
                x = source(w, y, 3 * q)
                if x % 2 == 0:
                    x += 3 * q
                current = x
                for e in w:
                    current = step(current, e)
                require((x << s) == q * current + c and current % 3 == y, 'physical source lift')
            checked += 1
        for quotients in fibers.values():
            require(len(quotients) == len(set(quotients)), 'residue-bin collision')
            for lo in set(quotients):
                require(sum(lo <= j < lo + 3 for j in quotients) <= 3, 'three-bin bound')
                bins += 1
    return checked, bins


def regeneration_control():
    # A finite one-letter routing fixture. The universal theorem uses a much
    # longer fixed-total route at mean two, from Weaver--Wren Theorem 8.
    word = (1, 2)
    u, k = 1, len(word)
    depth = k + 2
    q = 3**depth
    target = source(word, u, q // 3)
    plans = {}
    for cell in range(u, q, 3):
        gap = next(e for e in range(1, 2 * q // 3 + 1) if ((cell << e) - 1) % q == 3 * target)
        plans[cell] = (gap,) + word
    phases = len(word) + 1
    starts, ends, departures, arrivals = (Counter() for _ in range(4))
    edges = Counter()
    for x in range(u, q * 3**phases, 3):
        state = x
        starts[state % q] += 1
        for e in plans[x % q]:
            departures[state % q] += 1
            edges[state % q, e] += 1
            state = step(state, e)
            arrivals[state % q] += 1
        ends[state % q] += 1
    require(ends == starts and arrivals == departures, 'stationary finite flow')
    # Markovize the occupations, then independently expose each of the three
    # children of a row. The occupation remains invariant at depth `depth`.
    fresh = Counter()
    for (r, e), mass in edges.items():
        for trit in range(3):
            fresh[step(r + trit * q, e) % q] += mass
    require(fresh == Counter({r: 3 * v for r, v in departures.items()}), 'rolling fresh-trit law')
    return len(plans), len(edges), sum(ends.values())


@cache
def min_cost(n, x):
    if n == 0:
        return 0
    require(0 < x < 3 ** (n + 1) and x % 3, 'source unit out of range')
    # A legal gap <=4 exists in every row: no cost-minimizer can exceed 4n.
    return min(e + min_cost(n - 1, (((x << e) - 1) // 3) % 3**n)
               for e in range(1, 4 * n + 1) if ((x << e) - 1) % 9 in (3, 6))


def spectrum_control():
    words = []
    cells = set()
    for w in compositions(3, 6):
        r = source(w, 0, 27)
        if r not in cells:
            words.append(w)
            cells.add(r)
    q = 3**6
    concatenated = [left + right for left, right in product(words, repeat=2)]
    require(len({source(w, 0, q) for w in concatenated}) == len(words)**2, 'block separation')
    tests = 0
    for n in range(1, 7):
        mod = 3 ** (n + 1)
        counts = defaultdict(set)
        for r in range(1, mod):
            if r % 3 == 0:
                continue
            cost = min_cost(n, r)
            previous = min_cost(n - 1, r % (mod // 3))
            require(1 <= cost - previous <= 4, 'cost increments')
            counts[cost].add(r % (mod // 3))
            x = 2 * mod + r + (mod if r % 2 == 0 else 0)
            require(2 * mod <= x <= 4 * mod and x % 2 == 1, 'ordinary octave representative')
            require(min_cost(n, x % mod) == cost, 'octave cost')
            tests += 1
        for t in sorted(counts):
            cheap = set().union(*(v for s, v in counts.items() if s <= t))
            require(len(cheap) <= comb(t, n), 'composition upper bound')
    return len(words), len(concatenated), tests


if __name__ == '__main__':
    print('numerator words and residue-bin checks', *numerator_control())
    print('regenerative rows, occupied edges, lifts', *regeneration_control())
    print('separated words, concatenations, source-depth checks', *spectrum_control())
