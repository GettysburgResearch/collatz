"""Independent sparse integral-polynomial replay at frozen period-ten schedules."""

from collections import defaultdict


def potential(index, pulse):
    return int(index % 10 in pulse)


def stack_exponents(drift, start, pulse, stop):
    height = start
    total = 0
    output = [total]
    init_difference = potential(0, pulse) - potential(-1, pulse)
    assert init_difference == potential(0, pulse) == 0
    for j in range(1, stop + 1):
        increment = drift + potential(j, pulse) - 2 * potential(j - 1, pulse) + potential(j - 2, pulse)
        assert increment >= 1
        height += increment
        total += 9 * height + 1
        output.append(total)
    return output


def denominator_terms(n, delay, A, B):
    # Keys in the auxiliary product are (Y degree, q degree).
    auxiliary = {(0, 0): 1}
    for factor in range(n):
        update = defaultdict(int)
        for (k, q_degree), coefficient in auxiliary.items():
            for h in range(10):
                update[k + h, q_degree + (delay + factor) * h] += coefficient * (-1) ** h
        auxiliary = update
    return [
        (k, A * (q_degree - k * (k + 1) // 2) + B * k, coefficient)
        for (k, q_degree), coefficient in auxiliary.items() if coefficient
    ]


def test_case(n, drift, start, pulse):
    delay, degree = 37 * n // 2, 9 * n
    A, B = 9 * drift, 9 * start + 1 + 9 * drift
    first = delay + n
    native = stack_exponents(drift, start, pulse, first + 4)
    for j, E in enumerate(native):
        assert E == A * j * (j - 1) // 2 + B * j + 9 * potential(j, pulse)
    terms = denominator_terms(n, delay, A, B)
    height_cap = A * (delay * (delay - 1) // 2 + 9 * n * (n - 1) // 2) + B * delay + 9
    assert all(0 <= E <= height_cap for _, E, _ in terms)
    assert [(k, c) for k, E, c in terms if E == 0] == [(0, 1)]
    balanced = pulse == {1, 2}
    smallest = []
    failed_window = 0
    for j in range(len(native)):
        coefficients = defaultdict(int)
        for k, E, coefficient in terms:
            if k <= j:
                coefficients[E + native[j - k]] += coefficient
        nonzero = {e: c for e, c in coefficients.items() if c}
        if j < delay:
            assert not nonzero or max(nonzero) <= height_cap
        elif j < first:
            if balanced:
                assert not nonzero
            else:
                failed_window += bool(nonzero)
        elif balanced:
            e = min(nonzero)
            expected = A * (j * (j - 1) // 2 - degree * (j - delay) + 9 * n * (n - 1) // 2)
            expected += B * j + 9 * potential(j - degree, pulse)
            assert e == expected and abs(nonzero[e]) == 1
            smallest.append(e)
    if balanced:
        assert all(a < b for a, b in zip(smallest, smallest[1:]))
    else:
        assert failed_window
    return len(native)


if __name__ == "__main__":
    probes = sum(test_case(n, d, m, {1, 2}) for n in (2, 4) for d, m in [(2, 0), (4, 3)])
    adverse = test_case(2, 3, 0, {1})
    assert 64**93 > 81**88 and 88 * 297 - 93 * 281 == 3
    print(f"Checked {probes} balanced coefficient polynomials and {adverse} adverse controls.")
