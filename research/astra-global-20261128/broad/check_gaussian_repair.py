"""Solve each normalized finite Gaussian system and check its reduced denominator."""

from fractions import Fraction
from math import prod


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def solve(matrix, rhs):
    n = len(rhs)
    rows = [row + [value] for row, value in zip(matrix, rhs)]
    for k in range(n):
        pivot = next((r for r in range(k, n) if rows[r][k]), None)
        require(pivot is not None, "singular interpolation matrix")
        rows[pivot], rows[k] = rows[k], rows[pivot]
        pivot_value = rows[k][k]
        rows[k] = [z / pivot_value for z in rows[k]]
        for r in range(n):
            if r != k:
                ratio = rows[r][k]
                rows[r] = [z - ratio * y for z, y in zip(rows[r], rows[k])]
    return [row[-1] for row in rows]


def outside_six(number):
    require(number > 0, "denominator")
    for prime in (2, 3):
        while number % prime == 0:
            number //= prime
    return number


def main():
    beta = Fraction(2, 3)
    cases = 0
    rows_checked = 0
    max_denom_bits = 0
    for h in (2, 4, 6, 10):
        x = beta ** (h // 2)
        for n in range(2, 10):
            matrix = [[x ** ((i - k) ** 2) for k in range(n)] for i in range(n)]
            flat_rhs = [-x ** ((n - i) ** 2) for i in range(n)]
            flat = solve(matrix, flat_rhs)
            require(flat[-1] == -x * sum(x ** (2 * j) for j in range(n)), "flat subleading coefficient")
            perturbed_rhs = flat_rhs[:]
            perturbed_rhs[0] *= beta
            new = solve(matrix, perturbed_rhs)
            denominator = prod(1 - x ** (2 * d) for d in range(1, n))
            correction = (1 - beta) * (-1) ** (n - 1) * x ** (n ** 2 + n - 1) / denominator
            require(new[-1] == flat[-1] + correction, "rank-one repair")
            exact_denominator = prod(3 ** (h * d) - 2 ** (h * d) for d in range(1, n))
            require(outside_six(new[-1].denominator) == exact_denominator, "reduced denominator outside six")
            for i, row in enumerate(matrix):
                require(sum(a * b for a, b in zip(row, new)) == perturbed_rhs[i], "repaired cancellation")
                rows_checked += 1
            max_denom_bits = max(max_denom_bits, exact_denominator.bit_length())
            cases += 1
    print(f"Gaussian systems={cases}, repaired rows={rows_checked}, largest outside-six denominator bits={max_denom_bits}")


if __name__ == "__main__":
    main()
