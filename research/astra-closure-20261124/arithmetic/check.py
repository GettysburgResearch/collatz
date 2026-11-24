"""Exact finite controls for the mountain equations and signed unit tuple."""
from itertools import accumulate
from math import gcd


def require(condition, explanation):
    if not condition:
        raise ArithmeticError(explanation)


def v2(n):
    return (n & -n).bit_length() - 1


def mountain(x):
    k = v2(x + 1)
    peak = 3**k * ((x + 1) >> k) - 1
    ell = v2(peak)
    y = peak >> ell
    require(ell > 0 and y % 2 and peak > x, ("peak", x))
    value = x
    for _ in range(k):
        require(value % 2 == 1, ("odd", value))
        value = (3 * value + 1) // 2
    require(value == peak and 2**ell * y == value, ("clock", x))
    return k, ell, y


def subsetsums(terms):
    sums = [0]
    for term in terms:
        sums += [s + term for s in sums]
    return sums


def replay_windows():
    windows = high = low_terminal = 0
    for source in range(1, 2500, 2):
        path = [source]
        odd_runs, even_runs = [], []
        for h in range(1, 5):
            k, ell, target = mountain(path[-1])
            path.append(target)
            odd_runs.append(k)
            even_runs.append(ell)
            p = list(accumulate(odd_runs, initial=0))
            a = list(accumulate((u + v for u, v in zip(odd_runs, even_runs)), initial=0))
            atoms = []
            for i in range(h):
                atoms.extend((2**a[i] * 3**(p[-1] - p[i]),
                              -(2**(a[i] + odd_runs[i]) * 3**(p[-1] - p[i+1]))))
            left, right = 3**p[-1] * source, 2**a[-1] * target
            require(left + sum(atoms) == right, ("carry", path))
            require(len({v2(abs(term)) for term in atoms}) == 2*h, ("separation", path))
            require(subsetsums(atoms).count(0) == 1, ("atoms", path))
            if min(path[:-1]) > 8*h:
                require(sum(map(abs, atoms)) < left, ("dominance", path))
                require(subsetsums([left, *atoms, -right]).count(0) == 2, ("tuple", path))
                high += 1
                low_terminal += int(target <= 8*h)
            windows += 1
    return windows, high, low_terminal


def replay_powers():
    tested = 0
    for base in range(3, 301, 2):
        for exponent in range(1, 36):
            x = base**exponent
            k, ell, y = mountain(x)
            require(2**k <= base+1, ("power-clock", base, exponent))
            require((3**k - 2**k) % gcd(x, y) == 0, ("common divisor", base, exponent))
            if k >= 2:
                require(3**k <= (2**k-1)**2 and 3**k-2**k < base**2,
                        ("carry bound", base, exponent))
            if exponent == 1:
                require(y < base**2, ("base successor", base))
            if y % base == 0:
                t, z = 0, y
                while z % base == 0:
                    t, z = t+1, z//base
                if z == 1:
                    require(t == 1 and exponent % 2 == 1, ("dependent", base, exponent))
            tested += 1
    return tested


def replay_rounding():
    # U and W are exact powers. Negative W modulo U is the unique candidate c.
    u = w = 1
    for k in range(1, 4097):
        u *= 2
        w *= 3
        c = (-w) % u
        require(0 < c < u and (w+c) % u == 0, ("rounding", k))
        if k >= 2:
            require(u*c >= w, ("unexpected near power", k))
    return 4095


if __name__ == "__main__":
    n, high, low_target = replay_windows()
    print(f"{n} exact windows, {high} nondegenerate high-entry tuples, "
          f"{low_target} of them with a low terminal value")
    print(f"{replay_powers()} ordinary power starts checked")
    print(f"{replay_rounding()} candidate exponents excluded by the exact rounding filter")
