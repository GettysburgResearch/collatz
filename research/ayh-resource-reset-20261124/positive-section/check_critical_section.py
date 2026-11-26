"""Exact bounded replay of the quarter reduction for the positive shortcut map."""

import json


CUTOFF = 250_000
EXPECTED_BANDS = [1092, 546, 3990, 2185, 1092, 546, 273, 1994]


def require(test, context):
    if not test:
        raise RuntimeError(context)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def data(n):
    height = n.bit_length() - 1
    number = 3 * n + 1
    odd = number
    valuation = 0
    while odd % 2 == 0:
        odd //= 2
        valuation += 1
    marked = (height + 1) * (n - (1 << height)) <= 70 * (1 << height)
    return height, valuation, odd, marked, 5 * valuation - height - 1


def main():
    bands = [0] * 8
    endpoints = {}
    reductions = 0
    total = 0
    for n in range(1, CUTOFF + 1, 2):
        d, e, u, marked, surplus = data(n)
        if not marked or surplus < 0:
            continue
        total += 1
        actual = n
        for _ in range(e):
            actual = step(actual)
        require(actual == u and u % 2 == 1, ("odd endpoint", n))
        if n == 1:
            require(surplus == 9 and u == 1, "base case")
            continue
        if surplus < 8:
            require(u not in endpoints, ("repeated band endpoint", u, n))
            endpoints[u] = n
            bands[surplus] += 1
            continue
        reductions += 1
        y = n
        while y > 1 and surplus >= 8:
            m = (y - 1) // 4
            nd, ne, nu, nm, ns = data(m)
            require((y % 8, m % 2) == (5, 1) and 0 < m < y, ("domain", y, m))
            require(step((y - 1) // 2) == m, ("half-size partner", y, m))
            require(step(m) == step(step(step(y))), ("physical merger", y, m))
            require((nd, ne, nu, nm, ns) == (d - 2, e - 2, u, True, surplus - 8),
                    ("mark, valuation, or endpoint", y, m))
            y, d, e, surplus = m, nd, ne, ns
        require(y == 1 or 0 <= surplus <= 7, ("termination of reduction", n, y))
    require(bands == EXPECTED_BANDS, ("per-surplus counts", bands))
    require(reductions == 6090 and total == 17809 and len(endpoints) == 11718,
            ("census totals", reductions, total, len(endpoints)))
    print(json.dumps({"positive_odd_inputs_up_to": CUTOFF, "marked_power_sources": total,
                      "quarter_reducible_sources": reductions, "critical_sources": sum(bands),
                      "distinct_critical_odd_endpoints": len(endpoints),
                      "counts_for_surplus_0_through_7": bands}, indent=2))


if __name__ == "__main__":
    main()
