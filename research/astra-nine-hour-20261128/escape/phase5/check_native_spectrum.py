"""Finite exact controls for shortcut clock quotients and native boundary flux."""

from fractions import Fraction as Q
from math import comb


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def trace(n, length):
    odd = 0
    result = []
    for t in range(length + 1):
        result.append((n, t, odd))
        odd += n % 2
        n = step(n)
    return result


def first_one_clock(n):
    t = 0
    odds = 0
    while n != 1:
        odds += n % 2
        n = step(n)
        t += 1
        require(t <= 300, "finite test range exceeded")
    return t - 2 * odds


def check_meetings():
    dates = 0
    for ref in (1, 3, 5, 9, 19, 27):
        by_state = {}
        for value, j, grade in trace(ref, 90):
            by_state.setdefault(value, []).append((j, grade))
        for n in range(1, 129):
            difference = first_one_clock(n) - first_one_clock(ref)
            for value, s, p in trace(n, 90):
                for j, q in by_state.get(value, ()):
                    require(s - j - 2 * (p - q) == difference, "lap quotient")
                    dates += 1
    return dates


def check_flux():
    coordinates = 0
    for modulus in range(2, 10):
        label = [0] + [first_one_clock(n) % modulus for n in range(1, 129)]
        for N in range(1, 81):
            end = Q(2 * N, 3)
            integrated = [Q(0) for _ in range(modulus)]
            flux = integrated.copy()
            for n in range(1, int(end) + 1):
                integrated[label[n]] += Q(1, n) - 1 / end
            for y in range(1, int(end / 2) + 1):
                integrated[(label[y] + 1) % modulus] -= Q(1, 2 * y) - 1 / end
            for y in range(1, N + 1):
                idx = (label[y] - 1) % modulus
                integrated[idx] -= Q(1, 2 * y) - Q(1, 3) / end
                active = int(y % 3 == 2)
                flux[idx] += (Q(3 * active, 2 * y - 1) - Q(1, 2 * y)
                              - (active - Q(1, 3)) / end)
            require(integrated == flux, "direct physical integral versus boundary sum")
            coordinates += modulus
    return coordinates


def check_source_recursions():
    coordinates = 0
    for modulus in range(2, 10):
        label = [0] + [first_one_clock(n) % modulus for n in range(1, 257)]
        for j in range(1, 321):
            # Include both sides of each physical and ideal floor discontinuity.
            Y = Q(j, 3)
            native = [0] * modulus
            residual = native.copy()
            for n in range(1, int(Y) + 1):
                native[label[n]] += 3
            for y in range(1, int(Y / 2) + 1):
                native[(label[y] + 1) % modulus] -= 3
            for y in range(1, int(3 * Y / 2) + 1):
                idx = (label[y] - 1) % modulus
                native[idx] -= 1
                residual[idx] -= 1
            for y in range(2, int((3 * Y + 1) / 2) + 1, 3):
                residual[(label[y] - 1) % modulus] += 3
            require(native == residual, "direct native count versus trit residual")
            coordinates += modulus
    return coordinates


def check_smoothing():
    for j in range(257):
        weights = [0] + [comb(j, k) for k in range(j + 1)] + [0]
        variation = sum(abs(x - y) for x, y in zip(weights, weights[1:]))
        require(variation == 2 * max(weights), "binomial translation variation")
    return 257


if __name__ == "__main__":
    print("PASS", check_meetings(), "native meeting comparisons,",
          check_source_recursions(), "source-recurrence coordinates,",
          check_flux(), "integrated flux coordinates,",
          check_smoothing(), "binomial shift identities")
