"""Verify the Lyapunov certificate and independently compute inverse minima."""
import json

PHASES = ((17, 0, 0), (25, 1, 1), (37, 2, 2), (55, 3, 3),
          (41, 4, 5), (61, 5, 6), (91, 6, 7))
TRAPPED = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18,
           19, 20, 22, 24, 26, 27, 28, 29, 30, 32, 35, 36, 40, 43, 52, 64}
EXPONENTS = {17: 0, 21: 2, 23: 3, 25: 4, 31: 6, 33: 7, 34: 7, 37: 8,
             41: 9, 46: 10, 49: 11, 55: 12, 61: 13, 68: 14, 73: 15,
             82: 16, 91: 17, 109: 19, 122: 20, 136: 21, 163: 23, 244: 27}


def require(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def reflected(n):
    return (3*n - 1)//2 if n % 2 else n//2


def potential(n):
    return 170**7 << EXPONENTS[n] if n in EXPONENTS else (9*n)**7


def exact_minimum(target, budget):
    """All exponents, via the universal lower bound for later ancestors."""
    minimum = target
    def visit(n, remaining):
        nonlocal minimum
        minimum = min(minimum, n)
        if not remaining or n % 3 == 0:
            return
        exponent = 2 if n % 3 == 1 else 1
        numerator = n << exponent
        while True:
            parent = (numerator-1)//3
            # Any ancestor y in r more odd departures obeys
            # 3^r (y+1) >= 2^r (parent+1).
            if (parent+1) << (remaining-1) >= (minimum+1)*3**(remaining-1):
                return
            visit(parent, remaining-1)
            numerator *= 4
    visit(target, budget)
    return minimum


def main():
    require(all(reflected(n) in TRAPPED for n in TRAPPED), "trap closure")
    for n in range(245):
        require(potential(n) >= (9*n)**7, ("potential floor", n))
        if n not in TRAPPED:
            require(2048**(n % 2)*potential(n) <= 128*potential(reflected(n)),
                    ("edge", n))
    require(110**7 >= 2048*37**7, "tail threshold")
    require(2048*100**7 > 297**7, "six extra odd departures")
    require(54*99**6 > 50*100**6, "margin")
    for t, a, h in PHASES:
        n = 17
        q = 0
        for _ in range(h):
            q += n % 2
            n = reflected(n)
        require((n,q) == (t,a), ("cycle", t))
        require(128**h * potential(t) == 2048**a * 170**7, ("phase", t))
    comparisons = 0
    sample = {}
    for depth in range(7, 19):
        for t, a, h in PHASES:
            k = (depth-a)//7
            p = 7*k+a
            H = 11*k+h
            for z in (1, 2, 3, 5, 17):
                target = 2*3**depth*z-t
                expected = (2**(H+1))*3**(depth-p)*z-17
                actual = exact_minimum(target, depth)
                require(actual == expected, (depth, t, z, expected, actual))
                comparisons += 1
                if depth == 14 and z == 1:
                    sample[str(t)] = [target, actual]
    print(json.dumps({"certificate_edge_checks": 245-len(TRAPPED),
                      "override_count": len(EXPONENTS),
                      "trapped_count": len(TRAPPED),
                      "odd_budget_range": [7, 18],
                      "cofactors": [1, 2, 3, 5, 17],
                      "unbounded_exponent_minima_checked": comparisons,
                      "rank14_z1_target_and_minimum": sample},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
