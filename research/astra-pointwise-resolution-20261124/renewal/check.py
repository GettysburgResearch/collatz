"""Fresh exact controls for the fixed-total route and residual fusion cylinder."""

import json


def require(claim, message):
    if not claim:
        raise ValueError(message)


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def build_logs():
    modulus = 3**7
    powers = {pow(2, v, modulus): v for v in range(2, 1460)}
    require(len(powers) == 1458, "incomplete cycle")
    require(set(powers) == {i for i in range(modulus) if i % 3}, "missing unit")
    return powers


def router(source, total, depth, exponents):
    y = source
    gaps = []
    for _ in range(depth - 2):
        e = next(e for e in range(2, 7) if ((1 << e) * y - 1) % 9 in (3, 6))
        y = ((1 << e) * y - 1) // 3
        gaps.append(e)
    remaining = total - sum(gaps)
    v = exponents[(pow(2, remaining, 3**7) * y - 3 - 9 * 47) % 3**7]
    u = remaining - v
    require(u >= 2, "inadmissible total")
    gaps.extend([u, v])
    for e in (u, v):
        numerator = (1 << e) * y - 1
        require(numerator % 9 in (3, 6), "nonunit inverse")
        y = numerator // 3
    return y, gaps



def four_odd_step_cut():
    scale = 10_000
    weights = {}
    for e in range(2, 21):
        lo, hi = 0, scale + 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if mid**5 * 2**(2 * e) <= 9 * scale**5:
                lo = mid
            else:
                hi = mid
        weights[e] = lo
    counts = [0, 1, 1]
    minima = []
    for _ in range(4):
        modulus = len(counts)
        next_counts = []
        for r in range(3 * modulus):
            count = 0
            if r % 3:
                for e, weight in weights.items():
                    n = (1 << e) * r - 1
                    if n % 3 == 0:
                        count += weight * counts[(n // 3) % modulus]
            next_counts.append(count)
        counts = next_counts
        minima.append(min(x for i, x in enumerate(counts) if i % 3))
    require(minima[-1] == 10_261_932_046_877_717 > scale**4, "cut mass below one")
    return minima


def main():
    logs = build_logs()
    routes = 0
    gap_checks = 0
    for source in range(1, 2 * 3**7, 2):
        if source % 3 == 0:
            continue
        for depth in (2, 3, 8):
            for extra in (0, 19):
                total = 1461 + 6 * (depth - 2) + extra
                m, gaps = router(source, total, depth, logs)
                require(m % 243 == 47 and m >= source, "terminal mismatch")
                require(len(gaps) == depth and sum(gaps) == total, "wrong clocks")
                k = 64 * ((m - 47) // 243) + 12
                a, b = 9 * k + 2, 81 * k + 20
                for _ in range(6):
                    a, b = step(a), step(b)
                require(a == b == m, "residual arms failed to merge")
                z = m
                for e in reversed(gaps):
                    n = 3 * z + 1
                    require((n & -n) == 1 << e, "wrong physical odd valuation")
                    z = n >> e
                    require(z >= source and z % 2 == 1 and z % 3, "illegal return")
                    gap_checks += 1
                require(z == source, "wrong original unit")
                routes += 1
    print(json.dumps({
        "ternary_units_checked": len(logs),
        "minimum_inverse_cut_numerators": four_odd_step_cut(),
        "complete_routes": routes,
        "physical_odd_steps": gap_checks,
        "initial_arms_per_route": 2,
        "shortcut_fusion_clock": 6,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
