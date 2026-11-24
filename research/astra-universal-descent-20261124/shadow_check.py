"""Finite controls for the ordinary two-clock construction in shadow.md."""
from fractions import Fraction

def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2

def trace(x, length):
    out = [x]
    for _ in range(length):
        out.append(step(out[-1]))
    return out

def guard_controls():
    for h in range(21):
        d = h + 4
        modulus = 3 ** d
        unit = -pow(2 ** (2 * h + 1), -1, modulus) % modulus
        for a in (1, 8, 17):
            u2 = -pow(3 ** h, -1, 2 ** a) % 2 ** a
            u = unit + modulus * ((u2 - unit) * pow(modulus, -1, 2 ** a) % 2 ** a)
            n = 3 ** h * u
            m = 2 ** (d + 1) * ((1 + 2 * 4 ** h * u) // modulus) - 1
            path = trace(m, d + 2 * (h + 1) + 1)
            if not ((n + 1) % 2 ** a == 0 and 0 < m < n):
                raise RuntimeError('Check failed at source line 28: (n + 1) % 2 ** a == 0 and 0 < m < n')
            if not [x % 2 for x in path[:-1]] == [1] * d + [1, 0] * (h + 1) + [0]:
                raise RuntimeError('Check failed at source line 29: [x % 2 for x in path[:-1]] == [1] * d + [1, 0] * (h + 1) + [0]')
            if not path[-1] == step(n):
                raise RuntimeError('Check failed at source line 30: path[-1] == step(n)')
    print('63 exact positive certificates, h=0..20, a=1,8,17')

def small_shadows():
    bound, clock = (500, 16)
    paths = [trace(n, clock) for n in range(bound + 1)]
    targets = {}
    for m in range(1, bound + 1):
        k = 0
        for b, end in enumerate(paths[m]):
            targets.setdefault(end, []).append((m, b, k))
            k += end % 2
    checked = first = 0
    for n in range(2, bound + 1):
        u, h = (n, 0)
        while u % 3 == 0:
            u //= 3
            h += 1
        for a, end in enumerate(paths[n]):
            if (n + 1) % 2 ** a:
                break
            for m, b, k in targets[end]:
                if m >= n:
                    continue
                checked += 1
                if not (b > a and k > a + h):
                    raise RuntimeError('Check failed at source line 56: b > a and k > a + h')
                if n > 3 and n % 8 == 3:
                    delta, height = (n - 3, 0)
                    while delta % 3 == 0:
                        delta //= 3
                        height += 1
                    if not k > a + height:
                        raise RuntimeError('Check failed at source line 62: k > a + height')
                if k == a + h + 1:
                    first += 1
                    if not (h == 0 and b == a + 1 and (3 * m == 2 * n - 1)):
                        raise RuntimeError('Check failed at source line 65: h == 0 and b == a + 1 and (3 * m == 2 * n - 1)')
    print(f'{checked} smaller diagrams, {first} first-tier, n≤{bound}, both clocks≤{clock}')

def first_endpoint_inversion():
    """Reconstruct the signed denominator-clearing and physical tail in S5."""
    cap = 90
    paths = [trace(m, cap) for m in range(350)]
    checked = 0
    for n in range(3, 350, 6):
        h, u = (0, n)
        while u % 3 == 0:
            h += 1
            u //= 3
        endpoint = step(n)
        for m in range(1, n):
            path = paths[m]
            if endpoint not in path:
                continue
            for b, x in enumerate(path):
                if x != endpoint:
                    continue
                bits = [y % 2 for y in path[:b]]
                d = sum(bits) - 1 - h
                if not (d >= 1 and bits[-1] == 0):
                    raise RuntimeError('Check failed at source line 89: d >= 1 and bits[-1] == 0')
                C = k = s = 0
                for bit in bits:
                    if bit:
                        C = 3 * C + 2 ** s
                        k += 1
                    s += 1
                    if k == d:
                        break
                p = b - 1 - s
                v = m - Fraction(2 ** (b - 1) * u, 3 ** d)
                rr = (3 ** d * v + C) / 2 ** s
                if not (rr.denominator == 1 and 0 < rr < 2 * Fraction(3, 2) ** d):
                    raise RuntimeError('Check failed at source line 101: rr.denominator == 1 and 0 < rr < 2 * Fraction(3, 2) ** d')
                tail = trace(int(rr), p)
                if not tail[-1] == 1:
                    raise RuntimeError('Check failed at source line 103: tail[-1] == 1')
                if not sum((y % 2 for y in tail[:-1])) == h + 1:
                    raise RuntimeError('Check failed at source line 104: sum((y % 2 for y in tail[:-1])) == h + 1')
                if not 3 ** d * m == 2 ** s * (rr + 2 ** p * u) - C:
                    raise RuntimeError('Check failed at source line 105: 3 ** d * m == 2 ** s * (rr + 2 ** p * u) - C')
                checked += 1
    print(f'{checked} complete first-endpoint inversions, odd 3|n<350, clocks≤90')

def escape_budget(d):
    cutoff = 2 * Fraction(3, 2) ** d
    limit = (cutoff.numerator - 1) // cutoff.denominator
    best = 0
    for r in range(1, limit + 1):
        x, balance = (r, 0)
        while x != 1:
            balance += 1 if x % 2 else -1
            best = max(best, balance)
            x = step(x)
        best = max(best, balance + 1)
    h = 1
    while 2 ** (h + 1) < 2 * cutoff or 2 ** max(0, 2 * h + d + 2 - best) < 2 * 3 ** (h + d):
        h += 1
    return (limit, best, h)
if __name__ == '__main__':
    guard_controls()
    small_shadows()
    first_endpoint_inversion()
    for d in (1, 2, 4, 8, 12, 16):
        print('d, r_max, B_d, sufficient h:', d, *escape_budget(d))
