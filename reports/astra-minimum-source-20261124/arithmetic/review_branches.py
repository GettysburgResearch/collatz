"""Independent positive-integer controls for the two reviewed conditional branches."""


def require(ok):
    if not ok:
        raise ArithmeticError('ordinary path or branch identity failed')


def itinerary(n, h):
    bits = []
    for _ in range(h):
        bits.append(n & 1)
        n = (3 * n + 1) >> 1 if n & 1 else n >> 1
    return n, bits


def count_surviving_shapes():
    seen = 0
    for q in range(1, 500000, 2):
        n = 3 * q
        if n % 27 or (n + 1) % 8:
            continue
        m = ((n + 1) & -(n + 1)).bit_length() - 1
        a = (n + 1) >> m
        if 3**m * a % 4 != 3:
            continue
        w, h = n, 0
        while w % 3 == 0:
            w //= 3
            h += 1
        z = (w << h) - 1
        u = (3**(m - 1) * a - 1) // 4
        require(0 < z < q and itinerary(z, h)[0] == n - 1)
        require(u % 9 == 2 and ((4 * u + 1) // 9) == 3**(m - 3) * a)
        require(a % 3 != 0 and (8 * (1 << (m - 3)) * a - 1) == n)
        require(itinerary(n - 1, m)[0] == 4 * u)
        require(itinerary(n, m + 2)[0] == 9 * u + 2)
        require(itinerary(n, m + 2)[0] == itinerary(2 * n + 1, m + 3)[0])
        seen += 1
    return seen


def check_exit():
    a0, b0 = itinerary(1322, 8), itinerary(146, 8)
    require(a0 == (47, [0, 1, 0, 0, 0, 0, 0, 1]))
    require(b0 == (47, [0, 1, 0, 1, 1, 1, 0, 0]))
    seen = 0
    for a in range(2, 102):
        residue = 147 * pow(3**(a - 2), -1, 256) % 256
        b = next(v for v in (residue, residue + 256, residue + 512) if ((1 << a) * v) % 3 == 1)
        for v in (b, b + 768, b + 768 * 10**12):
            n = (1 << a) * v - 1
            q, t = n // 3, (3**(a - 2) * v - 147) // 256
            z = (1 << (a - 2)) * v - 1
            require(n == 3 * q and 0 < z < q)
            require(itinerary(n, a + 8)[0] == 47 + 81 * t == itinerary(z, a + 6)[0])
            seen += 1
    return seen


if __name__ == '__main__':
    print(f'Canonical shapes {count_surviving_shapes()}, complementary exit lifts {check_exit()}')
