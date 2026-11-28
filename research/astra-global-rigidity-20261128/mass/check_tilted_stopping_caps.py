"""Integer certificates for the two conditional cycle-minimum exclusions.

The analytic moment premise and the decimal optimum are not tested here.
"""


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def odd_step(n):
    value = 3 * n + 1
    return value // (value & -value)


if __name__ == "__main__":
    require(10905 ** 8 < 2 * 10000 ** 8, "lower bound for 2^(1/8)")
    require(39 ** 9 * (2 * 10905 - 10000) ** 8 >
            3 * 40 ** 9 * 10000 ** 8, "s=9/8 minimum cap below 13")
    require(1259 ** 3 < 2 * 1000 ** 3, "lower bound for 2^(1/3)")
    require(27 ** 4 * (2 * 1259 - 1000) ** 3 >
            3 * 28 ** 4 * 1000 ** 3, "s=4/3 minimum cap below 9")
    edges = 0
    for n in range(1, 13, 2):
        seen = set()
        while n != 1:
            require(n not in seen, (n, "unexpected cycle"))
            seen.add(n)
            n = odd_step(n)
            edges += 1
    print("4 exact power inequalities; 6 possible odd minima;", edges,
          "actual odd departures to 1; no moment premise verified")
