"""Verify the O13 Frostman and O14 point-disk controls from the O9 table."""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


def verify(source):
    data = source.read_bytes()
    digest = sha256(data).hexdigest()
    if digest != "91170eb02223527b842d0e06d8370ba6e8278f71f5a108f33075660de54dae88":
        raise ValueError("Unrecognized O9 table")
    original = [int(line) for line in data.splitlines()]
    modulus = 3**10
    if len(original) != modulus or min(original) <= 0:
        raise ArithmeticError("The table must be strictly positive")
    unit = [x if r % 3 else 0 for r, x in enumerate(original)]
    unit_values = [x for x in unit if x]
    lower, upper = min(unit_values), max(unit_values)
    if (lower, upper) != (71736705115, 99999999999):
        raise ArithmeticError("Unit extrema differ")
    alpha = Fraction(207384761192, 93324220975)
    beta = Fraction(5516102802, 2482245023)
    minimizers = set()
    for a in range(3 * modulus):
        r = a % modulus
        even = 2 * a % modulus
        low = 6 * unit[even]
        high = 6 * original[even]
        if a % 3 == 2:
            odd = (2 * a - 1) // 3 % modulus
            low += 2 * unit[odd]
            high += 2 * original[odd]
        if low * alpha.denominator < 3 * unit[r] * alpha.numerator:
            raise ArithmeticError(f"Lower bound failed at {a}")
        if high * beta.denominator > 3 * original[r] * beta.numerator:
            raise ArithmeticError(f"Upper bound failed at {a}")
        if unit[r] and low * alpha.denominator == 3 * unit[r] * alpha.numerator:
            minimizers.add(r)
    if 3995 not in minimizers:
        raise ArithmeticError("The recorded extremizing residue is missing")
    t = Fraction(20, 9)
    e = (beta - t) * upper / (lower * (t - 2))
    atanh = 2 * sum(Fraction(1, (2*j+1) * 2**(2*j+1)) for j in range(4))
    if not atanh > Fraction(109, 100) or not e < Fraction(109, 100) * Fraction(64, 10**7):
        raise ArithmeticError("Frostman rounding failed")
    if Fraction(149070337, 10**8)**2 >= alpha:
        raise ArithmeticError("Point-disk rounding failed")
    return dict(digest=digest, lifted_residues=3*modulus, unit_min=lower,
                unit_max=upper, lower_squared=str(alpha), upper_squared=str(beta),
                minimizing_residues=sorted(minimizers), frostman_excess_bound=str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("vector", type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(args.vector), indent=2))
