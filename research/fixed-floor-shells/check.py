"""Exact finite witnesses for FS-001 and FS-002. Run with python -B check.py."""

from collections import Counter


def shortcut(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def advance(n, steps):
    for _ in range(steps):
        n = shortcut(n)
    return n


def odd_core(n):
    return n // (n & -n)


def unit_recode(n):
    m = odd_core(n)
    if n % 3:
        return n
    assert advance(4 * m + 1, 3) == shortcut(m)
    return (n // m) * (4 * m + 1)


def inverse(z, k):
    n, remainder = divmod((z << k) - 1, 3)
    assert remainder == 0 and n % 2 and advance(n, k) == z
    return n


def legal_exp(z, precision, choices):
    modulus = 3**precision
    residue = (modulus - 1) // 2
    solutions = [
        k for k in choices if ((z << k) - (3 * residue + 1)) % (3 * modulus) == 0
    ]
    assert len(solutions) == 1
    return solutions[0]


def check_recoding():
    fibers = Counter()
    for n in range(1, 10001):
        u = unit_recode(n)
        k = 1 if u % 3 == 2 else 2
        y = inverse(u, k)
        assert 3 * y <= 20 * n
        fibers[y] += 1
    assert max(fibers.values()) <= 4
    return max(fibers.values())


def check_lifts():
    total = 0
    for precision in range(1, 5):
        modulus = 3**precision
        period = 2 * modulus // 3
        for u in range(1, 3 * modulus + 1):
            if u % 3 == 0:
                continue
            exponent = legal_exp(u, precision, range(1, 3 * period + 1))
            first = inverse(u, exponent)
            z = first
            accumulated = 0
            for j in range(1, 13):
                k = legal_exp(z, precision, (period, 2 * period, 3 * period))
                z = inverse(z, k)
                assert z % modulus == (modulus - 1) // 2
                accumulated += k
                scaled = z * 3**j
                assert (first - 1) << accumulated <= scaled <= first << accumulated
                total += 1
    return total


def check_shells():
    # The two-offset gate x=4+8t, x+1=5+8t has common endpoint 2+3t.
    total = 0
    max_depth = 0
    for n in range(25, 126):
        u = unit_recode(n)
        first = inverse(u, legal_exp(u, 1, range(1, 7)))
        for endpoint in (2**1024, 3**646, 5**442):
            z = first
            for j in range(151):
                # Find smallest k>=0 in the permitted parity with x>=endpoint.
                k = max(1, endpoint.bit_length() - z.bit_length() - 6) | 1
                while True:
                    t, remainder = divmod((z << k) - 2, 3)
                    assert remainder == 0
                    x = 4 + 8 * t
                    if x >= endpoint:
                        break
                    k += 2
                if 20 * (x + 1) <= 21 * endpoint:
                    joined = advance(x, 3)
                    assert joined == advance(x + 1, 3) == z << k
                    start = odd_core(joined)
                    for _ in range(j):
                        start = odd_core(3 * start + 1)
                    assert start == first
                    max_depth = max(max_depth, j)
                    total += 1
                    break
                z = inverse(z, legal_exp(z, 1, (2, 4, 6)))
            else:
                raise AssertionError((n, endpoint))
    return total, max_depth


def check_terminal_lift():
    total = 0
    for precision in range(1, 5):
        modulus = 3**precision
        period = 2 * modulus // 3
        exponent_to_residue = {
            pow(2, k, 3 * modulus): k for k in range(3 * period)
        }
        for y in (1, 5, 7, 29, 35, 97):
            for e in range(1, modulus):
                if e % 3 == 0:
                    continue
                for prescribed in (3 * period, 3 * period + 1, 16 * period + 5):
                    start = prescribed - 3 * period
                    residue = ((y << prescribed) - 3 * e) % (3 * modulus)
                    k = start + (exponent_to_residue[residue] - start) % (3 * period)
                    z = inverse(y, prescribed - k)
                    gate_endpoint = z << k
                    assert gate_endpoint % modulus == e
                    assert odd_core(3 * odd_core(gate_endpoint) + 1) == y
                    total += 1
    return total


if __name__ == "__main__":
    print("FS-001 max odd recoding fiber for n<=10000:", check_recoding())
    print("FS-002 exact legal rotation steps:", check_lifts())
    print("FS-002 exact two-point shell witnesses and max depth:", check_shells())
    print("FS-004 prescribed exponents reconstructed:", check_terminal_lift())
