"""Exact first-moment and winding replay on two explicit affine prototypes."""

from math import gcd, prod


LOW = ((6, 1), (6, 5), (12, 7), (6, 2), (18, 14))
HIGH = ((6, 1), (6, 5), (12, 8))


def shortcut(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def winding_factors(proto, parameter):
    odd = [u * parameter + v for u, v in proto if v % 2]
    return prod(odd), prod(3 * n + 1 for n in odd)


def check():
    # 52*(5,3)+75*(3,2)=(485,306), a positive near-critical pair.
    prototypes = [LOW] * 52 + [HIGH] * 75
    length = sum(map(len, prototypes))
    odd_count = sum(v % 2 for shape in prototypes for _, v in shape)
    assert (length, odd_count) == (485, 306) and gcd(length, odd_count) == 1

    def initial_ratio(base):
        factors = [winding_factors(shape, base + 2 * i)
                   for i, shape in enumerate(prototypes)]
        return (2**length * prod(x for x, _ in factors),
                prod(y for _, y in factors))

    low, high = 1, 2
    while True:
        num, den = initial_ratio(high)
        if num >= den:
            break
        low, high = high, 2 * high
    while high - low > 1:
        mid = (low + high) // 2
        num, den = initial_ratio(mid)
        if num < den:
            low = mid
        else:
            high = mid

    params = [low + 2 * i for i in range(len(prototypes))]
    num, den = initial_ratio(low)
    for i, shape in enumerate(prototypes):
        old_n, old_d = winding_factors(shape, params[i])
        new_n, new_d = winding_factors(shape, params[i] + 1)
        num, den = num // old_n * new_n, den // old_d * new_d
        params[i] += 1
        if num >= den:
            break
    assert 0 <= (num - den) * low**2 < den

    states = [u * t + v for shape, t in zip(prototypes, params)
              for u, v in shape]
    successors = [shortcut(n) for n in states]
    assert len(set(states)) == length
    assert all(n > 0 and n % 3 != 0 for n in states)
    assert sum(states) == sum(successors)
    assert set(states) != set(successors)
    # The two lists have equal cardinality and first moment, hence their
    # even-exponent defect vanishes to order at least two at z=1.
    odd = [n for n in states if n % 2]
    assert (2**length * prod(odd), prod(3 * n + 1 for n in odd)) == (num, den)
    print(f"PASS {length} distinct sources, {odd_count} odd, exact first moment, "
          f"multiplicative winding residual below 1/{low}², unequal successors.")


if __name__ == "__main__":
    check()
