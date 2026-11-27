"""Exact, dependency-free controls for the mixed-root slope obstruction."""

from fractions import Fraction as F
import json


def check(condition, message):
    if not condition:
        raise ValueError(message)


def valuation_congruent(x, residue, prime):
    return (x.numerator - residue * x.denominator) % prime == 0


def edges(x, y):
    odd = not valuation_congruent(x, 0, 2)
    a, b = (F(3, 2), F(1, 2)) if odd else (F(1, 2), F(0))
    yield "F", a * x + b, a * y + b, a
    yield "E", 2 * x, 2 * y, F(2)
    if valuation_congruent(y, 2, 3):
        yield "O", (2 * x - 1) / 3, (2 * y - 1) / 3, F(2, 3)


def inspect_ball(n, radius):
    """Explore all distinct endpoint/slope pairs, comparing every permitted edge."""
    states = {(F(-1), F(1), n, F(1))}
    seen = states.copy()
    inspected = 0
    for _ in range(radius):
        following = set()
        for x, y, z, slope in states:
            signed = list(edges(x, y))
            physical = list(edges(F(z), F(z)))
            check([a[0] for a in signed] == [a[0] for a in physical], "legality")
            for (name, u, v, p), (_, t, _, q) in zip(signed, physical):
                check(p == q and t.denominator == 1, name)
                final = slope * p
                check(final >= 1 and v - u == 2 * final, "slope")
                following.add((u, v, int(t), final))
                inspected += 1
        states = following - seen
        seen.update(following)
    return len(seen), inspected


def least_root(r):
    mod2, mod3 = 2**r, 3**r
    return 1 + mod3 * ((-2 * pow(mod3, -1, mod2)) % mod2)


def discrete_log_2_3power(target, k):
    j = int(target % 3 == 2)
    for i in range(1, k):
        period = 2 * 3 ** (i - 1)
        lifts = [j + t * period for t in range(3)]
        j = next(a for a in lifts if pow(2, a, 3 ** (i + 1)) == target % 3 ** (i + 1))
    return j


def good_control(r):
    modulus = 3 ** (2 * r)
    target = (3**r * pow(2, 1 - r, modulus) - 1) % modulus
    j = discrete_log_2_3power(target, 2 * r) + 2 * 3 ** (2 * r - 1)
    y = 1 << j
    n = ((y + 1) << r) // (3**r) - 1
    check((n + 1) % (2**r) == 0 and (n - 1) % (3**r) == 0, "CRT")
    z = n
    for _ in range(r):
        check(z % 2 == 1, "odd prefix")
        z = (3 * z + 1) // 2
    check(z == y, "power-of-two endpoint")
    return {"radius": r, "j": j, "source_bits": n.bit_length()}


def backward_tables(depth):
    # 2^k times maximum incoming forward slope over all ancestors of depth <= k.
    tables = [[1]]
    for k in range(1, depth + 1):
        prior = tables[-1]
        m = len(prior)
        row = []
        for y in range(3 * m):
            value = max(2**k, prior[(2 * y) % m])
            if y % 3 == 2:
                value = max(value, 3 * prior[((2 * y - 1) // 3) % m])
            row.append(value)
        tables.append(row)
    return tables


def survives(n, r, tables):
    j, odd, y = 0, 0, n
    while j <= r:
        table = tables[r - j]
        if 3**odd * 2 ** (r - j) < 2**j * table[y % len(table)]:
            return False
        odd += y % 2
        y = (3 * y + 1) // 2 if y % 2 else y // 2
        j += 1
    return True


def main():
    depth = 11
    tables = backward_tables(depth)
    layers = []
    for r in range(1, depth + 1):
        n = least_root(r)
        check(0 < n <= 6**r, "least positive CRT representative")
        check(survives(n, r, tables), "backward dynamic program")
        vertices, edges_checked = inspect_ball(n, r)
        row = {"radius": r, "least_CRT_root": n, "vertices": vertices,
               "edges_checked": edges_checked}
        if r <= 7:
            row["surviving_residues_mod_6^r"] = sum(
                survives(z, r, tables) for z in range(1, 6**r + 1)
            )
        layers.append(row)
    print(json.dumps({"mixed_ball": layers,
                      "explicit_good": [good_control(r) for r in range(1, 8)]},
                     indent=2))


if __name__ == "__main__":
    main()
