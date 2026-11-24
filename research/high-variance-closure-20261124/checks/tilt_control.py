"""Exact finite tilted adjacent-grid checks at s = 3/2."""


def step(value):
    return (3 * value + 1) // 2 if value % 2 else value // 2


def nonnegative_quadratic(a, b):
    """Whether a + b sqrt(3) is nonnegative."""
    if b >= 0:
        return a >= 0 or 3 * b*b >= a*a
    return a >= 0 and a*a >= 3 * b*b


def run(k):
    width = 2**k
    start = (2 * 3**k // width + 1) * width
    total = [0, 0]
    failures = [0, 0]
    no_count_return = [0, 0]
    for n in range(start, start + width):
        x, y = n + 1, n
        j, ell = 0, 0
        ever_equal = False
        returned = False
        for _ in range(k):
            j += x % 2
            ell += y % 2
            x, y = step(x), step(y)
            ever_equal |= x == y
            returned |= j == ell
        weight = 3**(j//2)
        total[j%2] += weight
        if not ever_equal:
            failures[j%2] += weight
        if not returned:
            if ever_equal:
                raise ValueError("unequal-count finite meeting above bound")
            no_count_return[j%2] += weight
    # (2 - sqrt(3)) * (a + b sqrt(3)).
    a, b = total
    for count in [failures, no_count_return]:
        if not nonnegative_quadratic(count[0] - (2*a-3*b), count[1] - (2*b-a)):
            raise ValueError("tilted failure bound violated")


if __name__ == '__main__':
    for horizon in range(1, 14):
        run(horizon)
    print("16,382 adjacent ordinary pairs on 13 complete grids; exact Q(sqrt(3)) directional failure bound")
