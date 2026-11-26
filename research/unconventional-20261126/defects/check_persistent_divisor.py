#!/usr/bin/env python3
"""Exact checks for common boundary factors and physical multi-reset CRT paths."""
from fractions import Fraction
from math import gcd, prod
import json


def check(ok, message):
    if not ok:
        raise ArithmeticError(message)


def v2(n):
    check(n > 0, "invalid positive valuation")
    return (n & -n).bit_length() - 1


def rough6(n):
    n >>= v2(n)
    while n % 3 == 0:
        n //= 3
    return n


def block(x):
    t = v2(x + 1)
    w = (x + 1) >> t
    m = 3 ** t * w - 1
    b = v2(m)
    return t, b, m >> b


def path_data(x, r):
    states = [x]
    rises, excesses = [], []
    for _ in range(r):
        t, b, z = block(states[-1])
        rises.append(t)
        excesses.append(b)
        states.append(z)
    return states, rises, excesses


def certificate(states, rises, excesses):
    y = [x + 1 for x in states]
    g = gcd(*(z >> v2(z) for z in y))
    full = gcd(*y)
    T, B, t0 = sum(rises), sum(excesses), rises[0]
    coords = [(3 ** T) * (y[0] >> t0) // g]
    plain_cores = [(y[0] >> t0) // g]
    D_prev = T_prev = 0
    for j, (t, b) in enumerate(zip(rises, excesses)):
        check(((1 << b) - 1) % g == 0, "common factor lost at a block")
        v = ((1 << b) - 1) // g
        coords.append(3 ** (T - T_prev - t) * (1 << (D_prev + t - t0)) * v)
        plain_cores.append(v)
        check(
            (y[j + 1] << (t + b)) == 3 ** t * y[j] + ((1 << b) - 1) * (1 << t),
            "physical block bank",
        )
        D_prev += t + b
        T_prev += t
    total = sum(coords)
    check(total == (y[-1] << (T + B - t0)) // g, "positive integer sum")
    check(all(v > 0 for v in coords) and coords[0] % 2 == 1, "nondegeneracy or odd root")
    check(v2(total) == T + B - t0 + v2(y[-1]), "terminal valuation")
    check(
        prod(rough6(v) for v in coords) == prod(rough6(v) for v in plain_cores),
        "product of three-place coordinate norms",
    )
    check(
        prod(plain_cores) * (g ** (len(rises) + 1)) < (y[0] >> t0) * (1 << B),
        "multiplicity of the persistent factor",
    )
    check(full == g << min(v2(v) for v in y), "full integer gcd")
    return g


def residue_for_word(word):
    residue = current = 0
    free_slope = 1
    for index, bit in enumerate(word):
        lift = (current % 2) ^ bit
        residue += lift << index
        current += lift * free_slope
        check(current % 2 == bit, "binary cylinder split")
        if bit:
            current = (3 * current + 1) // 2
            free_slope *= 3
        else:
            current //= 2
    return residue


def first_one(x, limit=1000000):
    for tick in range(limit + 1):
        if x == 1:
            return tick
        x = (3 * x + 1) // 2 if x % 2 else x // 2
    raise ArithmeticError("actual first-hit verification exceeded its cap")


def threshold_time(r, b, n, d):
    if (r + 1) * n <= d:
        return 0
    def holds(t):
        return 3 ** (d * t) >= 1 << (n * t + ((r + 1) * n - d) * b)
    low, high = 0, 1
    while not holds(high):
        low, high = high, high * 2
    while high - low > 1:
        mid = (low + high) // 2
        if holds(mid):
            high = mid
        else:
            low = mid
    return high


def example(r, b, n, d):
    total = threshold_time(r, b, n, d) + 16 * r
    target_rises = [total // r + int(i < total % r) for i in range(r)]
    target = []
    for t in target_rises:
        target.extend([1] * t + [0] * b)
    target.append(1)
    binary = 1 << len(target)
    residue = residue_for_word(target)
    g = (1 << b) - 1
    odd_modulus = 3 * g
    # g is 1 mod 3 for odd b, so g-1 is the joint numerical residue.
    other = ((g - 1 - residue) * pow(binary, -1, odd_modulus)) % odd_modulus
    x = residue + binary * other + binary * odd_modulus
    check(x % 6 == 3, "sharpness source is not an odd triple")
    states, rises, excesses = path_data(x, r)
    check(rises == target_rises and excesses == [b] * r, "exact block endpoints")
    check(certificate(states, rises, excesses) == g, "sharpness common gcd")
    check(states[-1] ** d >= (x + 1) ** n, "sharpness terminal floor")
    result = {
        "r": r, "b": b, "sigma": str(Fraction(n, d)), "T": sum(rises),
        "initial_bits": x.bit_length(), "terminal_bits": states[-1].bit_length(),
        "odd_gcd_bits": g.bit_length(),
    }
    if n == d:
        y = x
        for bit in target[:-1]:
            check(y % 2 == bit, "physical protected parity mismatch")
            y = (3 * y + 1) // 2 if bit else y // 2
            check(y > x, "physical shortcut below its required protected floor")
        check(y == states[-1], "physical shortcut landing mismatch")
        result["checked_protected_shortcuts"] = len(target) - 1
        if b <= 127:
            result["first_one_shortcut_triple"] = first_one(x)
            result["first_one_shortcut_cofactor"] = first_one(x // 3)
    return result


def full_gcd_example(r, c, n, d):
    def large_enough(t):
        return n <= d or 3 ** (d*t) >= 1 << (n*t + (n-d)*c)
    low, high = 0, 1
    while not large_enough(high):
        low, high = high, 2*high
    while high-low > 1:
        middle = (low+high)//2
        if large_enough(middle):
            high = middle
        else:
            low = middle
    rise_total = max(r*c, high)+128*r
    rises = [rise_total//r+int(j<rise_total%r) for j in range(r)]
    word = []
    for t in rises:
        word.extend([1]*t+[0])
    word.extend([1]*c+[0])
    residue = residue_for_word(word)
    binary = 1 << len(word)
    multiplier = (-residue * pow(binary, -1, 3)) % 3
    x = residue + binary * (multiplier+3)
    states, actual_rises, excesses = path_data(x, r)
    check(x%6 == 3 and actual_rises == rises and excesses == [1]*r, "full-gcd exact blocks")
    check(v2(states[-1]+1) == c, "exact terminal ascent")
    check(gcd(*(z+1 for z in states)) == 1 << c, "sharp full gcd")
    check(certificate(states, rises, excesses) == 1, "purely dyadic gcd")
    check(states[-1]**d >= (x+1)**n, "full-gcd landing lower bound")
    return {"r": r, "c": c, "sigma": str(Fraction(n,d)), "T": sum(rises),
            "initial_bits": x.bit_length(), "terminal_bits": states[-1].bit_length()}


def main():
    cases = 0
    max_full = 0
    for x in range(1, 4096, 2):
        states, rises, excesses = path_data(x, 12)
        for r in [1, 2, 3, 4, 6, 9, 12]:
            certificate(states[:r+1], rises[:r], excesses[:r])
            max_full = max(max_full, gcd(*(z + 1 for z in states[:r+1])))
            cases += 1
    canonical = []
    for r in [2, 3, 5, 8]:
        for b in [7, 31, 127]:
            for n, d in [(1, r + 1), (1, 1), (5, 4)]:
                canonical.append(example(r, b, n, d))
    print(json.dumps({
        "scope": "Exact integer algebra and physical trajectories. No finite test proves the asymptotic Subspace estimate.",
        "all_small_shifted_paths": cases, "small_start_bound": 4095,
        "largest_full_gcd_among_tested_windows": max_full, "sharp_families": canonical,
        "full_gcd_families": [full_gcd_example(r,c,n,d) for r in [2,5]
                              for c in [7,31,127] for n,d in [(1,1),(4,3),(3,2)]],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
