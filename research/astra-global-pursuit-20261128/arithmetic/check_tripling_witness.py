"""Exact arithmetic controls for the local tripling witness formulas."""

from collections import Counter


def check(condition):
    if not condition:
        raise RuntimeError("tripling witness control failed")


def shortcut(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def split(n):
    h = v = 0
    while n % 2 == 0:
        n //= 2
        h += 1
    while n % 3 == 0:
        n //= 3
        v += 1
    return h, v, n


def negative_entrance(r, d):
    # Store the numerator over the current formal denominator 3^d.
    u = -r
    while d:
        if u % 2:
            d -= 1
            u = (u + 3**d) // 2
        else:
            u //= 2
    return u


class VisitFive:
    """Real ordinary control with the single exceptional departure 5 -> 8."""

    def __init__(self):
        self.values = {1: False, 5: True}

    def __call__(self, n):
        path = []
        while n not in self.values:
            path.append(n)
            check(len(path) < 10000)
            n = shortcut(n)
        answer = self.values[n]
        for vertex in path:
            self.values[vertex] = answer
        return answer


def witness(f, n):
    m = n
    bits = []
    for depth in range(11):
        check(f(m) != f(m + 1))
        if m % 6 == 3:
            return m, "child"
        left = f(2 * m) != f(2 * m + 1)
        if len(bits) >= 2 and bits[-2:] == [1, 1]:
            s = m // 4 + 1
            case = "right"
            break
        if depth == 6 and bits == [0] * 6:
            s = n
            case = "left"
            break
        bits.append(0 if left else 1)
        m = 2 * m + bits[-1]
    else:
        raise RuntimeError("address exceeded its guaranteed depth")
    h, v, a = split(s)
    if f(s) != f(a):
        for exponent in range(v):
            q = a * 3**exponent
            if f(q) != f(3 * q):
                return 3 * q, case + "-chain"
        raise RuntimeError("missing change on the tripling chain")
    if case == "left":
        k = next(k for k in range(h + 2 * v + 2, h + 2 * v + 8)
                 if (2**k * a) % 9 == 1)
        return (2**k * a - 1) // 3, case
    k = next(k for k in (h + v + 1, h + v + 2) if (2**k * a) % 3 == 1)
    return 2**k * a - 1, case


def main():
    phases = 0
    for d in range(1, 11):
        modulus = 3**d
        zero = set()
        for r in range(1, modulus):
            if r % 3:
                phases += 1
                if negative_entrance(r, d) == 0:
                    zero.add(r)
        check(zero == {modulus - 2**d, modulus - 2 ** (d - 1)})

    f = VisitFive()
    cases = Counter()
    for n in range(2048, 32768):
        if f(n) == f(n + 1):
            continue
        p, kind = witness(f, n)
        check(p % 6 == 3 and f(p) != f(p // 3))
        _, v, _ = split(n)
        check(p * 3**v <= 2**13 * (n + 1) * 4**v)
        cases[kind] += 1
    check(set(cases) == {"child", "right", "left", "right-chain", "left-chain"})
    print(f"{phases} signed ternary phases; {sum(cases.values())} ordinary witnesses")
    print(dict(sorted(cases.items())))


if __name__ == "__main__":
    main()
