#!/usr/bin/env python3
"""Exact checks for L-0009, L-0010, and T-0007."""

from __future__ import annotations

from itertools import product


def B(word: tuple[int, ...]) -> int:
    total = sum(word)
    seen = 0
    out = 0
    for j, bit in enumerate(word):
        if bit:
            seen += 1
            out += (1 << j) * 3 ** (total - seen)
    return out


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def trace(n: int, length: int) -> tuple[tuple[int, ...], int]:
    bits = []
    x = n
    for _ in range(length):
        bits.append(x & 1)
        x = T(x)
    return tuple(bits), x


def prefix_family(b: int) -> list[tuple[int, ...]]:
    words = []
    for x in product((0, 1), repeat=b):
        missing = b - sum(x)
        high = (1,) * missing + (0,) * (b - missing)
        u = tuple(x) + high
        assert len(u) == 2 * b and sum(u) == b
        words.append(u)
    return words


def correction_code(b: int) -> list[tuple[int, ...]]:
    prefixes = prefix_family(b)
    p = b + 1
    modulus = 3**p
    period = 2 * 3 ** (p - 1)
    target = 1
    table = {pow(2, j, modulus): j for j in range(period)}
    assert len(table) == period
    words = []
    for u in prefixes:
        rhs = ((target - 3 * B(u)) * pow(pow(2, len(u), modulus), -1, modulus)) % modulus
        assert rhs % 3 != 0
        j = table[rhs]
        suffix = tuple(1 if t == j else 0 for t in range(period))
        w = u + suffix
        assert sum(w) == b + 1
        assert B(w) % modulus == target
        words.append(w)
    assert len(set(words)) == 2**b
    return words


def crt(a: int, m: int, b: int, n: int) -> int:
    # x=a mod m, x=b mod n, gcd(m,n)=1
    return (a + m * (((b - a) * pow(m, -1, n)) % n)) % (m * n)


def verify_b(b: int) -> tuple[int, int, int]:
    prefixes = prefix_family(b)
    residues = {B(u) % (1 << b) for u in prefixes}
    assert residues == set(range(1 << b))

    words = correction_code(b)
    L = len(words[0])
    a = b + 1
    mod3 = 3**a
    signature = (pow(2, -L, mod3) * B(words[0])) % mod3
    assert all((pow(2, -L, mod3) * B(w)) % mod3 == signature for w in words)

    # Select a positive common root with the shared signature.
    y = signature + mod3
    starts = [(2**L * y - B(w)) // mod3 for w in words]
    assert all(n >= 0 for n in starts)
    assert {n % (1 << b) for n in starts} == set(range(1 << b))
    for w, n in zip(words, starts):
        got_word, output = trace(n, L)
        assert got_word == w
        assert output == y

    # Append the shortest forced odd tail making the block supercritical.
    k = 1
    while 3 ** (a + k) <= 2 ** (L + k):
        k += 1
    root = crt(signature, mod3, -1 % (1 << k), 1 << k)
    root += mod3 * (1 << k)  # positive representative safely above all B/2^L bounds
    full_starts = [(2**L * root - B(w)) // mod3 for w in words]
    assert {n % (1 << b) for n in full_starts} == set(range(1 << b))
    for w, n in zip(words, full_starts):
        prefix_word, mid = trace(n, L)
        tail_word, _ = trace(mid, k)
        assert prefix_word == w
        assert tail_word == (1,) * k
    ratio_num = 3 ** (a + k)
    ratio_den = 2 ** (L + k)
    assert ratio_den < ratio_num <= 3 * ratio_den // 2 + 1
    return L, k, len(words)


def main() -> None:
    for b in range(1, 6):
        L, k, size = verify_b(b)
        print(f"b={b} branches={size} core_length={L} tail={k} projection=complete")
    print("all dyadic-projection checks passed")


if __name__ == "__main__":
    main()
