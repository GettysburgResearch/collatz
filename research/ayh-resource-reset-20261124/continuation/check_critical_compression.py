"""Replay the exact critical compression and its two physical clocks on fixed fibers."""
from collections import Counter
import json
from random import Random


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def orbit(x, clock):
    for _ in range(clock):
        x = step(x)
    return x


def valuation(n):
    return (n & -n).bit_length() - 1


def exact_critical(n):
    d = n.bit_length() - 1
    e = valuation(3 * n + 1)
    return n % 2 == 1 and 0 <= 5 * e - d - 1 <= 7 and (d + 1) * (n - 2**d) <= 70 * 2**d


def check(n, d, e, H, u_start, u_last):
    require(exact_critical(n), "input outside critical fiber")
    u = (3 * n + 1) >> e
    require(orbit(n, e) == u, "first factorization fails")
    x, h, p = u, 0, 0
    while h - p < H and h < 3 * H:
        p += x % 2
        h += 1
        x = step(x)
    if h - p != H:
        return "even_step_deadline"
    a = (-u) % (2**h)
    t = (u + a) >> h
    r = a
    for _ in range(h):
        r = (3 * r - 1) // 2 if r % 2 else r // 2
    require(x == 3**p * t - r and 1 <= r <= 3**p, "mirror identity fails")
    g = next(g for g in (1, 2, 3) if (2**p * g - a + 1) % 3 == 0)
    v = (t - g) * 2**p - 1
    require(v % 3 == u % 3 and 0 < u - (v << H) <= 4 * 2**(3 * H), "compression fails")
    k = H // 8
    f = e - 2 * k
    m = ((v << f) - 1) // 3
    require((v << f) == 3 * m + 1 and m * 2**(10 * k) < n, "critical inverse fails")
    if m < 2**(d - 10 * k):
        return "lower_edge"
    require(exact_critical(m) and m.bit_length() - 1 == d - 10*k, "partner outside exact fiber")
    require(valuation(3 * m + 1) == f, "partner exponent not exact")
    require(5*f - m.bit_length() == 5*e - n.bit_length(), "surplus changed")
    require(orbit(m, f) == v, "partner prefix misses endpoint")
    y = orbit(v, p)
    require(y == 3**p * (t-g) - 1 and y-x == r - 3**p*g - 1, "fixed gap fails")
    spacing = 3 * 2**h
    cell_size = 1 + (u - u_start) // spacing + (u_last - u) // spacing
    budget = cell_size.bit_length() - 1
    for b in range(budget + 1):
        if x == y:
            require(orbit(n, e+h+b) == orbit(m, f+p+b) == x, "two paths did not meet")
            return "smaller_critical_partner"
        x, y = step(x), step(y)
    return "pair_deadline"


def main():
    rng = Random(20261124)
    rows = []
    for e, H in ((24, 8), (48, 16), (80, 24), (128, 32)):
        counts = Counter()
        for surplus in range(8):
            d = 5*e - 1 - surplus
            require(12 * H <= d, "sample violates height hypothesis")
            n_start = 2**d
            n_end = n_start + 70 * n_start // (d+1)
            u_lo = (3*n_start + 1 + 2**e - 1) >> e
            u_hi = (3*n_end + 1) >> e
            u_start = u_lo + (((1 if e%2 == 0 else 5) - u_lo) % 6)
            fiber_size = 1 + (u_hi-u_start) // 6
            u_last = u_start + 6*(fiber_size-1)
            for j in [0, 1, fiber_size-1] + [rng.randrange(fiber_size) for _ in range(125)]:
                u = u_start + 6*j
                n = ((u << e)-1) // 3
                counts[check(n, d, e, H, u_start, u_last)] += 1
        rows.append({"valuation": e, "even_steps": H, "counts": dict(sorted(counts.items()))})
    require(all(row["counts"].get("smaller_critical_partner", 0) for row in rows), "no positive controls")
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
