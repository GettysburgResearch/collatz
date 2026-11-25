"""Bounded all-exponent controls and exact fixed-cofactor ordinary certificates."""


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def run(x, length):
    """Return endpoint, odd count, affine offset using literal shortcut steps."""
    count = offset = 0
    for clock in range(length):
        if x % 2:
            count += 1
            offset = 3 * offset + (1 << clock)
            x = (3 * x + 1) // 2
        else:
            x //= 2
    return x, count, offset


def check_language():
    states = {(0, -1)}
    first = {}
    witnesses = 0
    for clock in range(14):
        carries = {c for _, c in states}
        require({c for c in carries if c < 0} == {-(1 << i) for i in range(clock + 1)},
                "negative carry shape")
        for carry in carries:
            first.setdefault(carry, clock)
            if carry > 0 and carry % 2:
                require(first[carry] <= (carry + 3).bit_length(), "positive deadline")
        for n in range(1, 19):
            peak = 3**n - 1
            endpoint, actual, offset = run(peak, clock)
            expected = offset - 3**actual
            require((actual, expected) in states, "missing physical word")
            for p, c in states:
                value, rem = divmod(3**(n + p) + c, 1 << clock)
                if rem:
                    continue
                require(value == endpoint and p == actual and c == expected, "illegal realization")
                witnesses += 1
        states = states | {(p + 1, 3*c + (1 << clock)) for p, c in states}
    return witnesses


def parameters(d, e):
    k = d // 3
    return (d, d + 4, 1) if e == 22 else (2*k, 3*k + 3, 5)


def certificate(v, e, h, shift):
    """Use only residues of ordinary starting values and exact affine carries."""
    d = (v & -v).bit_length() - 1
    b, beta, a = parameters(d, e)
    degree = 2*v*e
    target = degree + shift
    total = h + beta
    mask = 1 << total
    raw = pow(3, degree, mask)
    unit, rem = divmod(raw - 1, 1 << beta)
    require(rem == 0, "unit precision")
    _, p, D = run(3**b*unit - a, h)
    _, target_count, target_offset = run(pow(3, target, mask) - 1, total)
    c = (1 << beta) * (D - a*3**p) - 3**(b+p)
    require(v % 27 == 4 and 0 < target < 66*v - 5, "earlier source")
    require(shift + target_count == b + p, "slope mismatch")
    require(c == target_offset - 3**target_count, "carry mismatch")
    return p, target_count


def literal():
    tests = [(166, 22, 3, 1), (220, 21, 131, 9), (274, 21, 24, -3),
             (328, 22, 3, 1), (436, 21, 189, 5), (544, 21, 71, 3)]
    for v, e, h, shift in tests:
        certificate(v, e, h, shift)
        d = (v & -v).bit_length() - 1
        b, beta, a = parameters(d, e)
        start = 3**b * ((3**(2*v*e)-1) >> beta) - a
        n = 2*v*e + shift
        peak = 3**n - 1
        require(run(start, h)[0] == run(peak, h + beta)[0], "literal postpeak merger")
        require(run(2**n-1, n)[0] == peak, "literal ascent")
    return len(tests)


def fixed():
    fixtures = [(20, 21, 209, 3), (38, 21, 144, 1), (38, 22, 130, 11),
                (56, 22, 183, 27), (74, 21, 89, 7), (110, 21, 160, 11),
                (128, 21, 49, 21), (164, 21, 117, 17), (182, 21, 132, 25),
                (200, 21, 56, 23), (236, 21, 46, 25)]
    for d, e, h, shift in fixtures:
        certificate(1 << d, e, h, shift)
    for u in [0, 27, 54, 27*137, 27*(2**64+17)]:
        v = (1 << 128) * (1 + (u << 49))
        require(certificate(v, 21, 49, 21) == (25, 88), "fixed family")
    mod = 1 << 180
    R = 357515049256705
    require(pow(3, 42 << 128, mod) == 1 + (R << 131), "first modular square")
    require(pow(3, 42 << 177, mod) == 1, "second modular square")
    a = run(4*3**84*R - 5, 49)
    b = run(3**21*((R << 131) + 1) - 1, 178)
    require(a[0] == b[0] == 25769221349192892822098750098086840813219442152713792,
            "affine representative endpoint")
    require(a[1] == 25 and b[1] == 88, "affine representative counts")
    return len(fixtures)


if __name__ == "__main__":
    print(f"{check_language()} physical language controls, {literal()} literal source mergers, "
          f"{fixed()} preassigned binary-power certificates, 5 fixed-class controls passed.")
