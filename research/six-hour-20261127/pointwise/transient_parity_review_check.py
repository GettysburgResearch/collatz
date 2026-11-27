"""Independent exact tests for actual windows, binary basin lifts and square births."""

from collections import Counter
from itertools import product, combinations
from math import isqrt
import json


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def selfpower(n):
    return n ** n if n else 1


def window_tests():
    trials = 0
    nontrivial = 0
    largest = 0
    for seed in range(25, 405, 7):
        states = []
        x = seed
        while x not in states and len(states) < 85:
            states.append(x)
            x = step(x)
        bits = [x % 2 for x in states]
        for m in (3, 5, 7, 9):
            if m > len(states):
                continue
            for h in sorted({1, m // 2, m - 1}):
                D = sum(a != b for a, b in zip(bits, bits[h:]))
                for base in (0, 17, 69, states[len(states) // 2]):
                    indices = [i for i in range(len(states) - m + 1)
                               if base <= states[i] < base + (1 << m)]
                    a = len(indices)
                    if not a:
                        continue
                    pairs = Counter((bits[i + j - h], bits[i + j])
                                    for i in indices for j in range(h, m))
                    counts = [pairs[u, v] for u in (0, 1) for v in (0, 1)]
                    u0, u1 = counts[0] + counts[1], counts[2] + counts[3]
                    diff = counts[1] + counts[2]
                    total = a * (m - h)
                    pair_power = 1
                    for f in counts:
                        pair_power *= selfpower(f)
                    marginal_power = selfpower(u0) * selfpower(u1)
                    assert selfpower(a) * pair_power <= (1 << (a * h)) * marginal_power
                    assert selfpower(total) * pair_power >= (
                        selfpower(diff) * selfpower(total - diff) * marginal_power)
                    assert diff <= D * (m - h)
                    assert len({tuple(bits[i:i + m]) for i in indices}) == a
                    trials += 1
                    nontrivial += a >= 2
                    largest = max(largest, a)
    return dict(trials=trials, at_least_two=nontrivial, largest=largest)


def lifts():
    clocks = Counter()
    maximum = 0
    all_exponents = {}
    for q in range(9):
        mod = 3 ** (q + 1)
        residues = {}
        y = 1
        for i in range(1, 3 ** q + 1):
            y = (4 * y) % mod
            residues[y] = i
        assert len(residues) == 3 ** q
        all_exponents[q] = residues
    for n in range(9):
        for w in product(range(2), repeat=n):
            q = sum(w)
            d = sum((1 << i) * 3 ** sum(w[i + 1:]) for i in range(n) if w[i])
            mod = 3 ** q
            residue = (d * pow(1 << n, -1, mod)) % mod
            l = all_exponents[q][1 + 3 * residue]
            y = (4 ** l - 1) // 3
            u, rem = divmod((y << n) - d, mod)
            assert rem == 0 and u > 0
            for bit in w:
                assert u % 2 == bit
                u = step(u)
            assert u == y and 3 * y + 1 == 1 << (2 * l)
            clocks[n] += 1
            maximum = max(maximum, l)
    return dict(by_length=dict(clocks), largest_terminal_exponent=maximum)


def births():
    K = 32
    seed = terminal = 1
    q = t = 0
    forced = 0
    types = Counter()
    last_date = 0
    for j in range(1, 1300):
        # isqrt(floor(log2(j+1))) equals floor(sqrt(log2(j+1))).
        L = 1 + isqrt((j + 1).bit_length() - 1)
        end = t + L
        target = q
        threshold = (1 << end) * (K + end) ** 2
        while 3 ** target * K * K < threshold:
            target += 1
        k = target - q
        assert 0 <= k <= L
        arrangements = list(combinations(range(L), k))
        ordinal = types[L, k]
        locations = arrangements[ordinal % len(arrangements)]
        types[L, k] += 1
        word = [int(i in locations) for i in range(L)]
        if 3 ** q <= (1 << end):
            word.sort(reverse=True)
        elif j == isqrt(j) ** 2 and 0 < k < L:
            desired = 1 - terminal % 2
            if desired != word[0]:
                z = word.index(desired)
                word[0], word[z] = word[z], word[0]
            assert (word[0] != terminal % 2)
            forced += 1
            last_date = t
        for b in word:
            if terminal % 2 != b:
                seed += 1 << t
                terminal += 3 ** q
            terminal = step(terminal)
            q += b
            t += 1
            assert 3 ** q > (1 << t)
            assert 1 <= seed <= (1 << t)
        assert q == target
    assert seed > (1 << last_date)
    return dict(blocks=1299, bits=t, ones=q, forced_square_births=forced,
                last_forced_at=last_date, canonical_seed_bits=seed.bit_length())


if __name__ == '__main__':
    print(json.dumps(dict(windows=window_tests(), basin=lifts(), birth=births()), indent=2))
