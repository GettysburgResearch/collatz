"""Independent integer replay of the descent table, swapped row, and deletion path."""

from collections import Counter
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def run(n, count):
    for _ in range(count):
        n = step(n)
    return n


def table(n):
    if n % 2 == 0:
        return "even", n // 2, None, step(n), n // 2
    if n % 3 == 0:
        z = n // 3
        return "multiple", z, z, 3 * z, n
    if n % 3 == 2:
        z = (2 * n - 1) // 3
        return "two", z, None, step(z), n
    if n % 9 == 4:
        z = (8 * n - 5) // 9
        return "four", z, None, run(z, 3), n
    if n % 9 == 7:
        z = (4 * n - 1) // 9
        return "seven", z, z, run(3 * z, 2), n
    z = (8 * n + 1) // 9
    return "one", z, z, run(3 * z, 4), step(n)


def check():
    counts = Counter()
    for n in range(2, 100002):
        case, z, query, left, right = table(n)
        counts[case] += 1
        require(0 < z < n and left == right, (n, "descent"))
        if query is not None:
            require(query % 2 == 1 and 9 * query <= 8 * n + 1, (n, "query"))
    samples = [*range(4096), 10**50]
    for t in samples:
        q, x = 3007 + 4374 * t, 2815 + 4096 * t
        require(run(x, 12) == step(3 * q), (t, "swapped first endpoint"))
        require(run(3 * x, 12) == step(q), (t, "swapped second endpoint"))
        require(0 < x < q and x % 2 == 1 and q % 2 == 1, (t, "source"))
        require((x % 3 != 0) == (t % 3 != 2), (t, "unit"))
        base, f, ff = 1 + 486 * t, 1 + 432 * t, 1 + 384 * t
        require(run(3 * f, 4) == step(base), (t, "first comparison"))
        require(run(3 * ff, 4) == step(f), (t, "second comparison"))
        require(run(ff, 6) == 1 + 162 * t, (t, "digit endpoint"))
        require(run(3 * (8 * t + 7), 3) == step(6 * t + 5), (t, "seven"))
    return {"descent_cases": dict(sorted(counts.items())), "affine_samples": len(samples)}


if __name__ == "__main__":
    print(json.dumps(check(), sort_keys=True))
