"""Finite ordinary controls for the row transport and timed predictor."""

from collections import Counter


def require(ok, message):
    if not ok:
        raise ValueError(message)


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def iterate(n, clocks):
    for _ in range(clocks):
        n = step(n)
    return n


def ternary_row(h, r):
    """Lift the entire progression using a single odd inverse per ternary digit."""
    p, clocks = r, 0
    for _ in range(h):
        exponent = next(e for e in range(1, 7) if (2**e * p) % 9 == 4)
        p = (2**exponent * p - 1) // 3
        clocks += exponent
    return clocks, p


def test_rows():
    rows = 0
    for h in range(1, 8):
        for r in range(1, 3**h):
            if r % 3 == 0:
                continue
            clocks, p = ternary_row(h, r)
            require(0 < p < 2**clocks and clocks <= 6 * h, (h, r, clocks, p))
            for n in (0, 1, 17, 63, 2**79 + 5):
                require(iterate(2**clocks * n + p, clocks) == 3**h * n + r,
                        (h, r, n))
            rows += 1
    return rows


def predict(n, target):
    """Visit the initial state and its next seven times bitlength shortcut iterates."""
    require(n > 0 and target > 0, "positive arguments required")
    for clock in range(7 * n.bit_length() + 1):
        if n == target:
            return clock
        n = step(n)
    return None


def test_predictor():
    count = Counter()
    for source in range(1, 20001):
        n = source
        reference = {}
        # All controls in this fixed range terminate. Guard a changed step function.
        for clock in range(1000):
            if n in (1, 5, 85):
                reference.setdefault(n, clock)
            if n == 1:
                break
            n = step(n)
        else:
            raise ValueError(("unresolved finite control", source))
        for target in (1, 5, 85):
            observed = predict(source, target)
            expected = reference.get(target)
            if expected is not None and expected > 7 * source.bit_length():
                expected = None
                count[target] += 1
            require(observed == expected, (source, target, observed, expected))
    return count


if __name__ == "__main__":
    print("ternary-unit rows verified through depth 7:", test_rows())
    print("finite true hits exceeding the cutoff by target:", dict(sorted(test_predictor().items())))
