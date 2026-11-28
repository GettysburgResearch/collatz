"""Exact ordinary native path controls for the two adjacent padded words."""

from math import gcd, lcm


def require(test, label):
    if not test:
        raise ValueError(label)


def next_odd(x):
    z = 3 * x + 1
    a = (z & -z).bit_length() - 1
    return z >> a, a


def carry(valuations):
    c, clocks = 0, 0
    for a in valuations:
        c = 3 * c + (1 << clocks)
        clocks += a
    return c, clocks


def check_pair(x, y, word, d, r):
    t = len(word)
    x1, a = next_odd(x)
    y1, b = next_odd(y)
    n = sum(word) + d
    D = (1 << n) - 3**t
    if D <= 0:
        return None
    v = ((1 << d) - 1 - 3 * r) >> b
    d1 = d + a - b
    require(d1 > 0 and 0 < v < (1 << d), 'positive deficit and opposite defect')
    require(y1 == (x1 << d1) - v, 'consecutive crossing')
    require((v << b) + 3 * r == (1 << d) - 1, 'two defects')
    c, m = carry(word)
    c1, m1 = carry(word[1:] + [b])
    require(n - m == d and n - m1 == d1, 'equal padded clocks')
    require(c == D * x + (r << m) and c1 == D * x1 - (v << m1), 'true carries')
    q, q1 = D // gcd(D, c), D // gcd(D, c1)
    require(q == D // gcd(D, r) and q1 == D // gcd(D, v), 'complete denominators')
    require(gcd(D, (1 << d) - 1) % (D // lcm(q, q1)) == 0, 'common loss')
    if d == 3:
        require(q == D == q1, 'exact width-three-clock denominators')
    for weights, den in [(word[:-1] + [word[-1] + d], q),
                         ((word[1:] + [b])[:-1] + [b + d1], q1)]:
        if den * den > (1 << n):
            for h in range(1, t):
                require(t % h or weights != weights[:h] * (t // h), 'least period')
    return n, t, D, q, q1


def run():
    local = 0
    for d in range(3, 12):
        for r in range(1, ((1 << d) - 2) // 3 + 1, 2):
            for x in range(1, 80, 2):
                y = (x << d) + r
                x1, a = next_odd(x)
                y1, b = next_odd(y)
                v = ((1 << d) - 1 - 3 * r) >> b
                require(v > 0 and b < d and v % 2 == 1, 'opposite odd defect')
                require(y1 == (x1 << (d + a - b)) - v, 'local transition')
                require(((1 << d) - 1) % gcd(r, v) == 0, 'joint divisor')
                local += 1
    hits = set()
    total = 0
    for start in range(1, 2800, 2):
        x = start
        word = []
        clocks = 0
        c = 0
        for t in range(1, 32):
            x, a = next_odd(x)
            word.append(a)
            c = 3 * c + (1 << clocks)
            clocks += a
            require((x << clocks) == 3**t * start + c, 'ordinary native arc')
            for n in {(3**t).bit_length(), clocks + 2, max(1, clocks - 2)}:
                D = (1 << n) - 3**t
                if D <= 0:
                    continue
                e = clocks - n
                h = (x << max(e, 0)) - (start << max(-e, 0))
                require(gcd(c, D) == gcd(h, D), 'all-phase residue')
                total += 1
            if x <= start:
                continue
            d = (x // start).bit_length() - 1
            r = x - (start << d)
            if 0 < 3 * r < (1 << d) - 1:
                got = check_pair(start, x, word, d, r)
                if got:
                    hits.add((start, t, d, r, got[2]))
    require((47, 17, 3, 1, 5077565) in hits, 'ordinary 47 fixture')
    print(f'{local} local two-defect tests, {total} all-date residues, {len(hits)} native adjacent crossings')


if __name__ == '__main__':
    run()
