"""Compare symbolic Hellinger weights with complete grids of positive ordinary pairs."""

from collections import defaultdict
from fractions import Fraction
from json import dumps
from math import isqrt


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def valuation(n):
    n = abs(n)
    require(n != 0, 'zero has no finite dyadic valuation')
    return (n & -n).bit_length() - 1


def edge(rank, carry, lower):
    upper = lower ^ (carry % 2)
    new_rank = rank + upper - lower
    power = max(0, -new_rank) + upper - max(0, -rank)
    numerator = (3 ** power * carry
                 + 3 ** max(0, -new_rank) * upper
                 - 3 ** max(0, new_rank) * lower)
    require(numerator % 2 == 0, 'symbolic edge has a half-integral carry')
    return new_rank, numerator // 2, upper


def factor(lower, upper, odd, even):
    return (odd if lower else even) if lower == upper else isqrt(odd * even)


def symbolic(depth, odd, even):
    distribution = {(1, -1): 1}
    rows = []
    for _ in range(depth):
        following = defaultdict(int)
        for (rank, carry), total in distribution.items():
            for lower in (0, 1):
                out_rank, out_carry, upper = edge(rank, carry, lower)
                if out_carry == 0:
                    require(out_rank == 0, 'nonzero rank merging in symbolic chart')
                    continue
                following[out_rank, out_carry] += total * factor(lower, upper, odd, even)
        distribution = following
        rows.append((sum(distribution.values()), distribution.get((1, -1), 0)))
    return rows


def physical(depth, odd, even):
    """Use ordinary integer dynamics, without using symbolic edges for the count."""
    grid = 2 ** depth
    base = 3 ** (depth + 2) * grid
    rows = [[0, 0] for _ in range(depth)]
    hold_cases = set()
    for residue in range(grid):
        lower = base + residue
        upper = 3 * lower - 1
        a, b, rank, carry, total = 0, 1, 1, -1, 1
        for h in range(depth):
            e, f = lower % 2, upper % 2
            require(e ^ f == carry % 2, 'mismatch was not predictable')
            next_lower = (3 ** e * lower + e) // 2
            next_upper = (3 ** f * upper + f) // 2
            a_next, b_next = a + e, b + f
            next_rank = b_next - a_next
            next_carry = (3 ** max(0, -next_rank) * next_upper
                          - 3 ** max(0, next_rank) * next_lower)
            old_min, new_min = min(a, b), min(a_next, b_next)
            d = Fraction(carry, 3 ** abs(rank))
            d_next = Fraction(next_carry, 3 ** abs(next_rank))
            error = (Fraction(f, 3 ** (b_next - new_min))
                     - Fraction(e, 3 ** (a_next - new_min)))
            require(abs(error) <= 1 and 2 * d_next == 3 ** (new_min - old_min) * d + error,
                    'ordinary normalized recurrence failed')
            if e == f and rank == 0:
                require(2 * next_carry == 3 ** e * carry and valuation(next_carry) == valuation(carry) - 1,
                        'rank-zero dyadic countdown failed')
                hold_cases.add('zero-rank')
            if e == f and rank != 0:
                cutoff = valuation(3 ** abs(rank) - 1)
                options = [edge(rank, carry, bit)[1] for bit in (0, 1)]
                if valuation(carry) < cutoff:
                    require(all(valuation(c) == valuation(carry) - 1 for c in options), 'shallow hold')
                    hold_cases.add('shallow')
                else:
                    require(any(valuation(c) == cutoff - 1 for c in options), 'deep hold')
                    hold_cases.add('deep')
            if next_carry == 0:
                require(next_rank == 0 and next_lower == next_upper, 'ordinary germ merger')
                break
            require(next_lower != next_upper, 'base representative too small')
            total *= factor(e, f, odd, even)
            rows[h][0] += total
            if (next_rank, next_carry) == (1, -1):
                rows[h][1] += total
            lower, upper = next_lower, next_upper
            a, b, rank, carry = a_next, b_next, next_rank, next_carry
    require(hold_cases == {'zero-rank', 'shallow', 'deep'}, 'incomplete holding-case coverage')
    result = []
    for h, row in enumerate(rows, 1):
        copies = 2 ** (depth - h)
        require(all(v % copies == 0 for v in row), 'incomplete physical prefix multiplicity')
        result.append(tuple(v // copies for v in row))
    return result


def main():
    outputs = []
    for odd, even, depth in [(25, 16, 15), (9, 16, 12), (16, 9, 12)]:
        require(isqrt(odd * even) ** 2 == odd * even, 'nonintegral Hellinger numerator')
        first = symbolic(depth, odd, even)
        second = physical(depth, odd, even)
        require(first == second, 'Hellinger propagation differs from ordinary grid')
        outputs.append({'q': f'{odd}/{odd+even}', 'depth': depth, 'ordinary_sources': 2**depth,
                        'surviving_numerator': first[-1][0], 'return_numerator': first[-1][1],
                        'denominator': (odd + even)**depth})
    print(dumps({'scope': 'all physical prefix lengths through each reported depth', 'runs': outputs}, indent=2))


if __name__ == '__main__':
    main()
