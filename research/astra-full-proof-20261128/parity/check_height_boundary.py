"""Cross-check finite Collatz harmonic densities, signed transport and least residues."""

from fractions import Fraction


def require(condition):
    if not condition:
        raise RuntimeError("finite height boundary identity failed")


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def source_data(n, depth):
    q, correction = 0, Fraction(1)
    for _ in range(depth):
        if n % 2:
            q += 1
            correction *= Fraction(3 * n + 1, 3 * n)
        n = step(n)
    return n, q, correction


def finite_densities(max_depth):
    tables = [[Fraction(1)]]
    for t in range(max_depth):
        old = tables[-1]
        period = len(old)
        new = []
        for y in range(3 * period):
            value = old[(2 * y) % period] / 2
            if y % 3 == 2:
                value += Fraction(3, 2) * old[((2 * y - 1) // 3) % period]
            new.append(value)
        require(sum(new) == len(new))
        tables.append(new)
    return tables


def main():
    depth_limit, cap = 7, 24
    tables = finite_densities(depth_limit)
    checks = 0
    for t, table in enumerate(tables):
        inverse = [Fraction()] * (cap + 1)
        for x in range(1, 2**t * cap + 1):
            y, _, correction = source_data(x, t)
            if y <= cap:
                inverse[y] += 1 / (x * correction)
        for y in range(1, cap + 1):
            require(inverse[y] == table[y % len(table)] / y)
            checks += 1
        from_sources, from_least_residues = Fraction(), Fraction()
        for n in range(1, 2**t + 1):
            y, q, correction = source_data(n, t)
            require(1 <= y <= 3**q)
            from_sources += 1 / (n * correction)
            from_least_residues += Fraction(3**q, y * 2**t)
        require(from_sources == from_least_residues)
    print(f"Verified {checks} exact inverse harmonic weights and all {depth_limit + 1} native moment sums.")


if __name__ == "__main__":
    main()
