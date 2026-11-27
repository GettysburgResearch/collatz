"""Exact finite checks for sparse signed terminal carries and ordinary lifts."""

import json
from fractions import Fraction
from itertools import combinations
from math import gcd, prod


def require(test, message):
    if not test:
        raise ValueError(message)


def trace(x, steps):
    bits = []
    for _ in range(steps):
        bit = x % 2
        bits.append(bit)
        x = (3 * x + 1 if bit else x) // 2
    return bits, x


def row(bits):
    a, q, c = 1, 1, 0
    for bit in bits:
        c = 3**bit * c + bit * a
        a *= 2
        q *= 3**bit
    return a, q, c


def root_atoms(blocks):
    """Represent each repeated carry by two signed terms before composition."""
    total_odds = sum(sum(root) * d for root, d in blocks)
    future_odds = total_odds
    prefix_length = 0
    atoms = []
    for root, d in blocks:
        a, q, c = row(root)
        future_odds -= sum(root) * d
        if c and d:
            coeff = Fraction(c, a - q)
            atoms.append((coeff, prefix_length + len(root) * d, future_odds))
            atoms.append((-coeff, prefix_length, future_odds + sum(root) * d))
        prefix_length += len(root) * d
    return atoms


def first_zero(columns):
    for size in range(1, len(columns) + 1):
        for group in combinations(range(len(columns)), size):
            if sum(columns[i][0] for i in group) == 0:
                return set(group)
    return None


def outside(value, primes):
    value = abs(value)
    require(value > 0, "outside part of zero")
    for prime in primes:
        if prime == 2:
            value //= value & -value
        else:
            while value % prime == 0:
                value //= prime
    return value


def verify_tuple(x, p, t, r, length, odds, atoms, totals):
    d = prod(coeff.denominator for coeff, _, _ in atoms)
    z0 = d * 3 ** (p + odds) * t
    right = [(d * r * 2**length, d * r, 0),
             (-d * x * 3**odds, d * x, odds)]
    for coeff, u, v in atoms:
        b = d * coeff
        require(b.denominator == 1, "coefficient denominator")
        right.append((-int(b) * 2**u * 3**v, abs(int(b)), v))
    require(sum(value for value, _, _ in right) == z0, "ordinary displaced row")
    require(z0 > 0, "positive ordinary displacement")
    while (group := first_zero(right)) is not None:
        totals["pruned_zero_subsums"] += 1
        right = [col for i, col in enumerate(right) if i not in group]
    require(bool(right) and sum(value for value, _, _ in right) == z0, "pruning")
    complete = [z0] + [-value for value, _, _ in right]
    require(sum(complete) == 0, "complete relation")
    for size in range(1, len(complete)):
        require(all(sum(group) for group in combinations(complete, size)),
                "proper zero subsum after pruning")
    g = gcd(*complete)
    primitive = [abs(value) // g for value in complete]
    require(gcd(*primitive) == 1, "primitive content")
    if g > 1:
        totals["nontrivial_contents"] += 1
    if (g % 2 == 0) and (g % 3 == 0):
        totals["contents_divisible_by_six"] += 1
    V = primitive[0]
    H = max(primitive)
    R = prod(b for _, b, _ in right)
    for primes in [(2, 3), (2, 3, 5, 7, 11)]:
        P = prod(outside(value, primes) for value in primitive)
        require((V * R) % P == 0, "outside parts do not divide stripped columns")
        for _, _, v in right:
            lhs = 3 ** (p + odds) * P
            rhs = 3**v * V * R
            require(rhs % lhs == 0, "exact primitive pivot divisibility")
            require(lhs <= 3**v * H * R, "projective bound")
            totals["exact_pivot_divisibilities"] += 1
    totals["signed_physical_tuples"] += 1


def two_run(n, k, d, totals):
    bits, x = trace(n, k)
    p = sum(bits)
    modulus = 3 ** (p + d)
    target = (3**d * (x + 1) * pow(2**d, -1, modulus) - 1) % modulus
    residue = 1
    period = 2 * 3 ** (p + d - 1)
    for j in range(period):
        if residue == target:
            break
        residue = 2 * residue % modulus
    else:
        raise ValueError("missing power of two")
    while j == 0 or 2**d * ((2**j + 1) // 3**d) - 1 <= max(x, 1):
        j += period
    z, remainder = divmod(2**j + 1, 3**d)
    require(remainder == 0 and z % 2 == 1, "integral odd parameter")
    y = 2**d * z - 1
    t, remainder = divmod(y - x, 3**p)
    require(remainder == 0 and t > 0, "positive lift")
    m = n + 2**k * t
    actual_bits, actual = trace(m, k)
    require(actual_bits == bits and actual == y and m > 2**k, "anchored prefix")
    for i in range(d):
        require(actual == 2 ** (d-i) * 3**i * z - 1 and actual % 2 == 1,
                "literal odd run")
        actual = (3 * actual + 1) // 2
    require(actual == 2**j, "dyadic endpoint")
    if j <= 5000:
        trailing, end = trace(actual, j)
        require(end == 1 and not any(trailing), "actual halving suffix")
        totals["physically_iterated_halving_suffixes"] += 1
    atoms = root_atoms([([1], d), ([0], j)])
    verify_tuple(x, p, t, 1, d+j, d, atoms, totals)
    totals["two_run_first_hits"] += 1
    return {"n": n, "k": k, "p": p, "odd_tail": d, "even_tail": j,
            "lift_quotient_bits": t.bit_length()}


def main():
    totals = dict.fromkeys(["pruned_zero_subsums", "nontrivial_contents",
                            "contents_divisible_by_six", "signed_physical_tuples",
                            "exact_pivot_divisibilities", "two_run_first_hits",
                            "physically_iterated_halving_suffixes", "rational_root_coefficients"], 0)
    for n in (1, 2, 5, 7, 27, 97):
        for k in range(2, 10):
            bits, x = trace(n, k)
            p = sum(bits)
            require(2**k*x <= 4**p*n and 3**k*x <= 2**k*3**p*n,
                    "physical height estimate")
            for t in (1, 2, 6, 35):
                lift_bits, lifted = trace(n+2**k*t, k)
                require(bits == lift_bits and lifted == x+3**p*t, "physical lift")
                for length in (3, 7, 11):
                    suffix, r = trace(lifted, length)
                    h = sum(suffix)
                    a, q, carry = row(suffix)
                    require(a*r == q*lifted+carry, "terminal row")
                    cut = length // 2
                    atoms = root_atoms([(suffix[:cut], 1), (suffix[cut:], 1)])
                    require(sum(c*2**u*3**v for c, u, v in atoms) == carry,
                            "moving root expansion")
                    if any(c.denominator > 1 for c, _, _ in atoms):
                        totals["rational_root_coefficients"] += 1
                    # The additional genuine zero subsum exercises signed pruning
                    # and a nontrivial common denominator at both small primes.
                    atoms.extend([(Fraction(5, 6), 2, h), (Fraction(-5, 6), 2, h)])
                    verify_tuple(x, p, t, r, length, h, atoms, totals)
    examples = []
    for n in (1, 5, 27):
        for k in range(1, 7):
            for d in sorted({1, k, 3}):
                result = two_run(n, k, d, totals)
                if n == 27 and k == d and k in (3, 5, 6):
                    examples.append(result)
    require(all(totals.values()), "a required class of controls was missed")
    print(json.dumps({"scope": "finite ordinary identities and exact primitive divisibility",
                      "counts": totals, "two_run_examples": examples},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
