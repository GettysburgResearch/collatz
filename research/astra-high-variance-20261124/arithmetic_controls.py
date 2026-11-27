"""Exact finite controls for raw clocks, dyadic padding, and inverse phases."""
from fractions import Fraction


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def trace(value: int, length: int) -> tuple[int, int]:
    odd_count = 0
    for _ in range(length):
        odd = value % 2
        odd_count += odd
        value = (3 * value + 1) // 2 if odd else value // 2
    return value, odd_count


def script_length(parameter: int, budget: int) -> int | None:
    length = 0
    for depth in range(budget + 1):
        if parameter % 4 == 2:
            return length + 2
        if depth == budget:
            break
        if parameter % 2:
            parameter = 3 * (parameter // 2) + 2
            length += 1
        elif parameter % 64 == 56:
            parameter = 9 * (parameter // 64) + 8
            length += 6
        else:
            break
    return None


def marked(value: int) -> bool:
    octave = value.bit_length() - 1
    return value % 2 == 1 and (octave + 1) * (value - 2**octave) <= 70 * 2**octave


def source_clock_controls() -> tuple[int, int]:
    accepted = 0
    padded = 0
    for n in range(3, 100_000, 2):
        valuation = ((n + 1) & -(n + 1)).bit_length() - 1
        k = valuation - 1
        v = (n + 1) >> valuation
        length = script_length(3**k * v - 1, n.bit_length())
        if length is None:
            continue
        x = (n - 1) // 2
        check(trace(x, k + length) == trace(n, k + 1 + length), "source trace")
        accepted += 1
    for d in range(4, 121):
        n = 2**d + 3
        s = (n - 1) // 2
        check(marked(n) and marked(s), "nearby marks")
        check(trace(n, 4) == trace(2 * s, 4), "one-unit padded clocks")
        padded += 1
    return accepted, padded


def inverse_controls() -> int:
    paths = 0
    for root in (1, 5, 7, 11, 13, 17):
        frontier = [(root, 0, Fraction(0))]
        for depth in range(5):
            following = []
            for value, total, offset in frontier:
                choices = [e for e in range(3, 15) if (2**e * value) % 9 in (4, 7)]
                check(len(choices) == 4, "four inverse choices")
                check(all(e <= b for e, b in zip(choices, (6, 8, 12, 14))), "digit bounds")
                last_upper = None
                for e in reversed(choices):
                    low = Fraction(1, 2**e)
                    high = Fraction(8, 5) * low
                    if last_upper is not None:
                        check(low - last_upper >= Fraction(3, 5 * 2**14), "sibling gap")
                    last_upper = high
                    child = (2**e * value - 1) // 3
                    E = total + e
                    D = offset + Fraction(3**depth, 2**E)
                    check(child % 2 == 1 and 3 * child + 1 == 2**e * value, "exact inverse")
                    check(root - D == Fraction(3 ** (depth + 1) * child, 2**E), "amplitude")
                    following.append((child, E, D))
                    paths += 1
            frontier = following
    return paths


if __name__ == "__main__":
    accepted, padded = source_clock_controls()
    print(f"accepted physical source pairs: {accepted}")
    print(f"unit-separation padded pairs: {padded}")
    print(f"exact inverse prefixes: {inverse_controls()}")
