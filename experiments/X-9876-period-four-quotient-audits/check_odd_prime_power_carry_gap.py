#!/usr/bin/env python3
"""Finite audit of the exact carry identity and strict phi gap."""


def primes(n):
    out = []
    for p in range(3, n + 1, 2):
        if all(p % d for d in range(3, int(p**0.5) + 1, 2)):
            out.append(p)
    return out


def W(n, p):
    ans = 0
    for r in range(1, n + 1):
        t, w = r, 1
        while t % p == 0:
            t //= p
            w *= p
        ans += w
    return ans


def carry_value(u, p, k):
    digits = []
    n = u
    while len(digits) < k:
        digits.append(n % p)
        n //= p
    carry = 1
    value = 0
    for i, digit in enumerate(digits):
        total = 2 * digit + carry
        carry = total // p
        if i + 1 < k:
            value += carry * p**i
    assert carry == 0
    return (p - 1) * value


def main(max_u=500):
    cases = 0
    for u in range(1, max_u + 1):
        N = 2 * u + 1
        for p in primes(N):
            pk, k = p, 1
            while pk <= N:
                pk *= p
                k += 1
            v0 = W(N, p) - 2 * W(u, p) - 1
            assert v0 == carry_value(u, p, k)
            assert 2 * v0 + 1 < pk // p * (p - 1)
            cases += 1
    print(f"PASS: exact carry formula and strict phi gap in {cases} cases")


if __name__ == "__main__":
    main()


