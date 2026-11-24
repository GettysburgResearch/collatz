"""Finite checks of both quantifiers, the positive formula, and the CRT family."""
import json


def walk(x, steps):
    odds = 0
    for _ in range(steps):
        if x % 2:
            x = (3 * x + 1) // 2
            odds += 1
        else:
            x //= 2
    return x, odds


def inverse_layer(n, h, excess):
    """All smaller ordinary witnesses of exact odd excess at an all-odd prefix."""
    if n <= 1 or h < 0 or excess < 1 or (n + 1) % (2 ** h):
        raise ValueError("requires an all-odd prefix and positive excess")
    target, _ = walk(n, h)
    a = h + excess
    maximum_t = h + 2 * excess - 1
    stack = [(target, 0, 0)]
    witnesses = []
    while stack:
        z, t, used = stack.pop()
        if used == a and z < n:
            witnesses.append((z, t, used))
        if t == maximum_t or a - used > maximum_t - t:
            continue
        stack.append((2 * z, t + 1, used))
        if used < a and z % 3 == 2:
            stack.append(((2 * z - 1) // 3, t + 1, used + 1))
    return sorted(witnesses)


def small_anchor_bound(excess):
    maximum = 2 * 3 ** excess // 2 ** excess - 1
    maximum_odds = 0
    for z in range(1, maximum + 1):
        y, odds = z, 0
        for _ in range(10000):
            if y == 1:
                break
            y, p = walk(y, 1)
            odds += p
        else:
            raise ArithmeticError(f"unfinished first hit for {z}")
        maximum_odds = max(odds, maximum_odds)
    return dict(E=excess, M=maximum, D=maximum_odds,
                sufficient_A=5 * maximum_odds + 4 * excess + 3)


def progression(A, H):
    B = 3 ** (A - 1)
    k = 2 * B
    r = 2 ** H * pow(3, -H, 4) - 1
    modulus = 2 ** (B + H + 2)
    u = (1 + 2 ** B * r) * pow(3, -k, modulus) % modulus
    return B, k, u, modulus


def require(value):
    if not value:
        raise ArithmeticError("two-anchor verification failed")


def check():
    pairs = targets = positive = examples = 0
    limit = 900
    # Enumerate all smaller sources through t=32 once per source.
    paths = [[walk(x, t) for t in range(33)] for x in range(limit)]
    for n in range(3, limit, 2):
        H = ((n + 1) & -(n + 1)).bit_length() - 1
        M = (n + 1) >> H
        if pow(3, H, 4) * M % 4 == 1:
            require(walk((n - 1) // 2, H + 1) == walk(n, H + 2)
                    == ((3 ** H * M - 1) // 4, H))
            positive += 1
        A, residue = 0, n - 1
        while residue % 3 == 0:
            A += 1
            residue //= 3
        if A == 0:
            continue
        hits = dict(walk(n, h) for h in range(H + 1 + int(H >= 2)))
        targets += 1
        for x in range(1, n):
            for y, a in paths[x]:
                if y in hits:
                    require(a > hits[y] + A)
                    pairs += 1

    for H in range(2, 8):
        for A in range(1, 5):
            B, k, u, period = progression(A, H)
            step = 2 ** (H + 2) * 3 ** k
            d = max(80, step.bit_length() + 16)
            first = (3 ** k * u - 1) >> B
            lift = max(0, (2 ** d - first + step - 1) // step)
            u += period * lift
            n = (3 ** k * u - 1) >> B
            x = (2 ** k * u) - 1
            require(n % 3 ** A == 1 and n % 2 ** H == 2 ** H - 1)
            require(walk(x, k + B) == (n, k) and x < n)
            require(walk((n - 1) // 2, H + 1) == walk(n, H + 2))
            require(2 ** d <= n < 2 ** (d + 1)
                    and (d + 1) * (n - 2 ** d) <= 70 * 2 ** d)
            examples += 1
    B, k, u, _ = progression(2, 2)
    n = (3 ** k * u - 1) >> B
    for h in range(3):
        for excess in range(1, 7):
            layer = inverse_layer(n, h, excess)
            require(excess > 2 or not layer)
            require(all(walk(x, t) == (walk(n, h)[0], a)
                        for x, t, a in layer))
    all_layers = [inverse_layer(n, 0, excess) for excess in range(1, 7)]
    require((2 ** k * u - 1, k + B, k) in all_layers[-1])
    first_s = next(i for i, layer in enumerate(all_layers, 1) if layer)
    return dict(max_source_exclusive=limit, max_inverse_clock=32,
                obstruction_sources=targets, actual_meetings_checked=pairs,
                positive_selectors=positive, narrowing_band_examples=examples,
                additive_overhead=small_anchor_bound(16),
                A2_H2=dict(n=(3 ** k * u - 1) >> B, predecessor=2 ** k * u - 1,
                           odds=k, final_halvings=B, minimum_clock_zero_odds=first_s,
                           first_layer=all_layers[first_s-1]))


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
