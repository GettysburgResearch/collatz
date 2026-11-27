"""Compare ordinary odd rows, fixed-prefix continuations, and exact gap-word counts."""

from math import log, log2


def cutoff(n):
    return (((n + 1) * 3 ** (6 * n)).bit_length() - 1) // 6


def odd_history(x, n):
    """Return the successive physical gap lengths starting at this ordinary odd x."""
    gaps = []
    for _ in range(n):
        value = 3 * x + 1
        gap = (value & -value).bit_length() - 1
        gaps.append(gap)
        x = value >> gap
    return gaps


def exact_count(prefix, n):
    """Conditional passing-row numerator, over 2**(H(n)-sum(prefix)) lifts."""
    elapsed = 0
    for j, gap in enumerate(prefix, 1):
        elapsed += gap
        if gap < 1 or elapsed > cutoff(j):
            raise ValueError("the supplied prefix must miss all its cuts")
    counts = [0] * elapsed + [1]
    for j in range(len(prefix) + 1, n + 1):
        updated = [0]
        total = 0
        for s in range(1, cutoff(j) + 1):
            if s - 1 < len(counts):
                total += counts[s - 1]
            updated.append(total)
        counts = updated
    top = cutoff(n)
    return sum(c << (top - s) for s, c in enumerate(counts)), 1 << (top - elapsed)


def direct_count(prefix, n, offset, stride):
    failed = 0
    matched = 0
    bounds = [cutoff(j) for j in range(1, n + 1)]
    for index in range(1 << cutoff(n)):
        gaps = odd_history(2 * (offset + stride * index) + 1, n)
        if gaps[:len(prefix)] != prefix:
            continue
        matched += 1
        elapsed = 0
        for gap, bound in zip(gaps, bounds):
            elapsed += gap
            if elapsed > bound:
                break
        else:
            failed += 1
    return failed, matched


def main():
    checks = 0
    for n in range(2, 9):
        for prefix in ([], [1], [1, 2]):
            for offset, stride in ((0, 1), (2, 3), (17, 81)):
                observed = direct_count(prefix, n, offset, stride)
                expected = exact_count(prefix, n)
                if observed != expected:
                    raise ArithmeticError((prefix, n, offset, stride, observed, expected))
                checks += 1
    print(f"{checks} complete ordinary-row and fixed-prefix comparisons passed")
    mu = log2(3)
    p = 1 / mu
    r = 1 - p
    tilt = -log(2 * r)
    log_rho = log(r / p) + tilt * mu
    kappa = tilt / (6 * log(2))
    print(f"rho={2 ** (log_rho / log(2)):.9f} kappa={kappa:.9f}")
    for n in (8, 32, 128, 512):
        num, den = exact_count([], n)
        print(f"n={n} H={cutoff(n)} log2(normalized ratio)="
              f"{log2(num)-log2(den)-n*log_rho/log(2)+(1.5-kappa)*log2(n):.5f}")


if __name__ == "__main__":
    main()
