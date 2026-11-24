"""Finite replay of the source-fixed clock inequality and constructive families."""
from collections import defaultdict

def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2

def valuation(x, prime):
    value = 0
    while x % prime == 0:
        value += 1
        x //= prime
    return value

def crt_dyadic_ternary(a, binary_modulus, ternary_modulus):
    return ternary_modulus * (a * pow(ternary_modulus, -1, binary_modulus) % binary_modulus)

def verify_small(source_limit=1500, competing_clock=20):
    earlier = defaultdict(list)
    mergers = comparison_sources = active_triples = 0
    sharp_excess = set()
    for n in range(1, source_limit + 1):
        b_max = valuation(n + 1, 2)
        e = valuation(n, 3)
        y = n
        for b in range(b_max + 1):
            for x, a, p in earlier[y]:
                mergers += 1
                if not (x < n and p > b + e and (a > b + e)):
                    raise ArithmeticError('control failed: x < n and p > b + e and (a > b + e)')
                if b > 0 and e > 0:
                    active_triples += 1
                if p == b + e + 1 and b > 0:
                    sharp_excess.add(e)
            y = step(y)
        y, p = (n, 0)
        for a in range(competing_clock + 1):
            earlier[y].append((n, a, p))
            p += y % 2
            y = step(y)
        comparison_sources += 1
    return dict(sources=comparison_sources, competing_clock=competing_clock, strictly_smaller_mergers=mergers, mergers_with_both_b_and_e_positive=active_triples, exact_one_odd_step_excess_for_v3=sorted(sharp_excess))

def verify_families():
    progressions = 0
    for H in range(1, 121):
        s = 0
        while 2 ** (H + s) < 3 ** H:
            s += 1
        if not 2 ** (H + s - 1) < 3 ** H < 2 ** (H + s):
            raise ArithmeticError('control failed: 2 ** (H + s - 1) < 3 ** H < 2 ** (H + s)')
        modulus = 2 ** (H + s)
        residue = 2 ** H * pow(3 ** H, -1, 2 ** s) - 1
        n = crt_dyadic_ternary(residue, modulus, 3 ** H)
        if not 3 ** H <= n < 2 * 9 ** H:
            raise ArithmeticError('control failed: 3 ** H <= n < 2 * 9 ** H')
        for j in range(3):
            source = n + j * modulus * 3 ** H
            y = source
            for a in range(H + s):
                if not y >= source:
                    raise ArithmeticError('control failed: y >= source')
                if not (y % 2 == 1) == (a < H):
                    raise ArithmeticError('control failed: (y % 2 == 1) == (a < H)')
                y = step(y)
            if not 0 < y < source:
                raise ArithmeticError('control failed: 0 < y < source')
            progressions += 1
    for t in (1, 5, 7, 11, 13):
        for H in range(1, 5):
            modulus = 3 ** (2 * H)
            target = (3 ** H * pow(2 ** H, -1, modulus) - 1) % modulus
            r = next((r for r in range(1, 2 * 3 ** (2 * H - 1) + 1) if pow(2, r, modulus) * t % modulus == target))
            j = (2 ** r * t + 1) // 3 ** H
            n = 2 ** H * j - 1
            if not (n % 3 ** H == 0 and n % 2 ** H == 2 ** H - 1):
                raise ArithmeticError('control failed: n % 3 ** H == 0 and n % 2 ** H == 2 ** H - 1')
            y = n
            for b in range(H):
                if not y % 2:
                    raise ArithmeticError('control failed: y % 2')
                y = step(y)
            if not (y == 2 ** r * t and y // 2 ** r == t):
                raise ArithmeticError('control failed: y == 2 ** r * t and y // 2 ** r == t')
    return dict(descending_sources=progressions, H_range=[1, 120], target_basin_sources=20)
if __name__ == '__main__':
    print(verify_small())
    print(verify_families())
