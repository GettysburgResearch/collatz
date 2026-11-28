"""Exact ordinary first clocks, both orders of floor/target, and mark fibres."""

from collections import Counter
from fractions import Fraction
from functools import cache


def require(condition):
    if not condition:
        raise ValueError("finite clock or mark identity failed")


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


@cache
def path(n):
    # Store one full terminal cycle when its first observed site is reached.
    visited = set()
    states = []
    while n not in visited:
        visited.add(n)
        states.append(n)
        n = step(n)
        require(len(states) < 10_000)
    return tuple(states)


@cache
def first_floor(n, floor):
    return next(i for i, v in enumerate(path(n)) if v % 2 and v <= floor)


@cache
def first_hit(n, y):
    return path(n).index(y)


def main():
    targets = {1, 3, 5, 7, 11, 13, 17, 23, 31, 41, 47, 53, 71, 101, 161}
    mesh = 37
    floor_ranks = (1, 2, 3, 4, 5, 6)
    clock_checks = Counter()
    cells = Counter()

    for n in range(1024, 4096):
        states = path(n)
        landings = [(2**k, first_floor(n, 2**k)) for k in floor_ranks]
        odd_count = 0
        correction = Fraction(1)
        for t, y in enumerate(states):
            if y in targets:
                for floor, arrival in landings:
                    if t >= arrival:
                        centre = first_hit(states[arrival], y)
                        order = "at or after"
                    else:
                        centre = -first_floor(y, floor)
                        order = "before"
                    require(t - arrival == centre)
                    clock_checks[order] += 1
                exact = Fraction(n * 3**odd_count, y * 2**t)
                require(exact == correction)
                cell = (exact.numerator * mesh) // exact.denominator
                cells[y, t, odd_count, cell] += 1
            if y % 2:
                odd_count += 1
                correction *= Fraction(3 * y, 3 * y + 1)

    for (y, t, p, _), count in cells.items():
        # Width in the original n coordinate of a mark cell at a fixed (t,p).
        width = Fraction(y * 2**t, mesh * 3**p)
        require(count <= 1 + width.numerator // width.denominator)
    require(min(clock_checks.values()) > 100)
    print("two-order checks", dict(sorted(clock_checks.items())))
    print("exact marked source visits", sum(cells.values()))
    print("nonempty physical clock/grade/mark cells", len(cells))


if __name__ == "__main__":
    main()
