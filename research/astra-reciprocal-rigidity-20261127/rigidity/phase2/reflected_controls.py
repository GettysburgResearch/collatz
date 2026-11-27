#!/usr/bin/env python3
"""Exact weighted norm, signed-tree, and known terminating excitation controls."""
from decimal import Decimal, localcontext
from fractions import Fraction
import json


def require(value, message):
    if not value:
        raise RuntimeError(message)


def reflected_layers(max_evens):
    row = {1}
    counts = [1]
    for even_count in range(1, max_evens+1):
        next_row = set()
        for parent in row:
            x = 2*parent
            while True:
                require(x not in next_row, "Duplicate reflected first-hit path")
                require(x <= 2**even_count, "Reflected height bound failed")
                next_row.add(x)
                if x % 3 != 1:
                    break
                x = (2*x+1)//3
                if x == 1:
                    break
        row = next_row
        counts.append(len(row))
    return counts


def depth_masses(max_depth, p):
    base = 9**p
    values = [1]
    signed = {1: 0}
    maxima = []
    for k in range(1, max_depth+1):
        previous_modulus = 3**(k-1)
        current_modulus = 3*previous_modulus
        values = [
            values[2*y % previous_modulus]
            + (base * values[((2*y-1)//3) % previous_modulus] if y % 3 == 2 else 0)
            for y in range(current_modulus)
        ]
        new_signed = {}
        for y, even_count in signed.items():
            new_signed[2*y] = even_count+1
            if y % 3 == 1:
                x = (2*y+1)//3
                require(x not in new_signed, "Reflected inverse branches collided")
                new_signed[x] = even_count
        signed = new_signed
        maximum = max(values)
        signed_mass = sum(base**(k-j) for j in signed.values())
        maximizers = [r for r,v in enumerate(values) if v == maximum]
        require(maximizers == [current_modulus-1], "Maximizing ternary residue differs")
        require(signed_mass == maximum, "Signed reflected tree missed the exact mass")
        maxima.append(maximum)
    return maxima


def shortcut(n):
    return n//2 if n % 2 == 0 else (3*n+1)//2


def known_excursions():
    out = []
    for k in range(1, 8):
        power = 1+3**k
        q = (2**power-1)//3
        require((q+1) % 3**k == 0, "Ternary target precision failed")
        t = (q+1)//3**k
        x = 2**k*t-1
        cursor = x
        for i in range(k):
            require(cursor == 3**i * 2**(k-i)*t-1, "All-odd affine discrepancy")
            require(cursor % 2 == 1 and cursor < q, "Premature root hit or parity mismatch")
            cursor = shortcut(cursor)
        require(cursor == q and shortcut(q) == 2**(power-1), "Physical target mismatch")
        for _ in range(power):
            cursor = shortcut(cursor)
        require(cursor == 1, "First-hit target trajectory failed")
        ratio = Fraction(9,4)**k
        out.append({"k": k, "q_bit_length": q.bit_length(), "x_bit_length": x.bit_length(),
                    "q_to_one_steps": power, "amplification": str(ratio)})
    return out


def main():
    counts = reflected_layers(26)
    limit = sum((Fraction(m,9**j) for j,m in enumerate(counts)), Fraction(0))
    ratio = Fraction(2,9)
    error = ratio**len(counts)/(1-ratio)
    with localcontext() as ctx:
        ctx.prec = 35
        decimal = lambda q: str(Decimal(q.numerator)/Decimal(q.denominator))
        bounds = [decimal(limit), decimal(limit+error)]
    results = {
        "reflected_first_hit_counts_by_even_count": counts,
        "p1_normalized_limit_rational_bounds": [str(limit),str(limit+error)],
        "p1_normalized_limit_decimal_approximations": bounds,
        "maxima_scaled_by_9_to_pk_depths_1_to_10": {
            str(p): depth_masses(10,p) for p in (1,2)
        },
        "known_terminating_all_odd_excursions": known_excursions(),
    }
    print(json.dumps(results,indent=2))


if __name__ == "__main__":
    main()
