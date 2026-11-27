"""Exact finite circle-mesh and fixed ordinary prefix identities."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def mesh_controls():
    counts = Counter()
    for p in range(2, 7):
        for word in product((1, 2, 3), repeat=p):
            A = sum(word)
            dates = [0]
            for e in word * 2:
                dates.append(dates[-1] + e)
            phi = [i * A - p * dates[i] for i in range(p)]
            w = max(phi) - min(phi)
            require(w <= p * (A - p), "one-sided cyclic cap")
            lo = phi.index(min(phi))
            phi = phi[lo:] + phi[:lo]
            peak = phi.index(max(phi))
            for v in range(1, p):
                counts["lags"] += 1
                cost = sum(abs(phi[(i + v) % p] - phi[i]) for i in range(p))
                B = [dates[i + v] - dates[i] for i in range(p)]
                for u, freq in Counter(B).items():
                    m = p - freq
                    require(cost <= p * m * (2 * A - p), "defect shift cost")
                    counts["common_clock_choices"] += 1
                for K in range(1, p + 1):
                    samples = [(k * v % p, k) for k in range(K + 1)]
                    distinct = sorted(set(point for point, _ in samples))
                    largest = max((point - distinct[i-1]) % p or p
                                  for i, point in enumerate(distinct))
                    for r in range(1, p + 1):
                        g, k = min(((peak-r-point) % p, k) for point, k in samples)
                        require(g <= largest, "sample mesh")
                        require(r * (w - (r+g) * (A-p)) <= k * cost, "finite mesh")
                        counts["mesh_intervals"] += 1
    return dict(sorted(counts.items()))


def prefix_controls(source, N):
    x = [source]
    dates = [0]
    prod = [Fraction(1)]
    for i in range(N):
        num = 3 * x[-1] + 1
        e = (num & -num).bit_length() - 1
        prod.append(prod[-1] * Fraction(num, num - 1))
        dates.append(dates[-1] + e)
        x.append(num >> e)
    require(len(set(x)) == len(x), "prefix must actually be injective")
    for i in range(N + 1):
        left = Fraction(x[i], source) ** N / Fraction(x[N], source) ** i
        phi = i * dates[N] - N * dates[i]
        right = Fraction(2) ** phi * prod[i] ** N / prod[N] ** i
        require(left == right, "actual endpoint line and reciprocal remainder")
    return {"source": source, "odd_edges": N, "native_clock": dates[N],
            "actual_endpoint": x[N], "largest_state": max(x)}


if __name__ == "__main__":
    print(json.dumps({"mesh": mesh_controls(),
                      "actual_prefixes": [prefix_controls(27, 25), prefix_controls(31, 30),
                                          prefix_controls(6171, 40)]}, indent=2))
