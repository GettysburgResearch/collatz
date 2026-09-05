#!/usr/bin/env python3
"""Exact audit of the general distinguished-block floor and carry lemma."""


def primes(limit):
    out = []
    for n in range(3, limit + 1, 2):
        if all(n % d for d in range(3, int(n**0.5) + 1, 2)):
            out.append(n)
    return out


def weight(n, p):
    ans = 0
    for j in range(1, n + 1):
        t, w = j, 1
        while t % p == 0:
            t //= p
            w *= p
        ans += w
    return ans


def block_weight(u, b, m, p):
    return (
        weight((2 * u + 1) // m, p)
        - weight(u // m, p)
        - weight((u - b) // m, p)
        - weight((2 * b + 1) // m, p)
        + 2 * weight(b // m, p)
    )


def carry_weight(B, delta, p, a):
    carry = delta
    value = 0
    n = B
    for i in range(a):
        digit = n % p
        n //= p
        carry = (2 * digit + carry) // p
        if i + 1 < a:
            value += carry * p**i
    assert n == 0 and carry == 0
    return (p - 1) * value


def main(max_m=64, max_u=256):
    cases = 0
    for m in range(1, max_m + 1):
        for u in range(max_u + 1):
            B, r = divmod(u, m)
            delta = (2 * r + 1) // m
            assert delta in (0, 1)
            b = 0 if delta == 0 else m // 2
            assert b <= u
            R = r - b
            assert 0 <= R < m

            anti = (
                m % 2 == 0
                and R % 2 == 1
                and (2 * b + R + 1 - m // 2) % m == 0
            )
            predicted = m % 4 == 0 and r in (m // 2 - 1, m - 1)
            assert anti == predicted, (m, u, r, b, R)

            for p in primes(31):
                if m % p == 0:
                    continue
                A = 2 * B + delta
                pa, a = p, 1
                while pa <= A:
                    pa *= p
                    a += 1
                direct = block_weight(u, b, m, p)
                collapsed = weight(A, p) - 2 * weight(B, p) - delta
                carried = carry_weight(B, delta, p, a)
                assert direct == collapsed == carried
                assert 2 * direct + 1 < (p - 1) * p ** (a - 1)
                cases += 1

    print(f"PASS: distinguished floors, residual states, and carry gap in {cases} cases")
    print(f"PASS: complementary state classification for m<= {max_m}, u<= {max_u}")


if __name__ == "__main__":
    main()


