"""Specified exact controls for the signed-shadow/triadic-dual bridge.

This checks two members of a proved family and the full forced carry.
It does not search for, or rule out, other complementary candidates.
"""

from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(x):
    require(x.denominator % 2 == 1, "actual rational state needs odd denominator")
    return (3 * x + 1) / 2 if x.numerator % 2 else x / 2


def valuation_two(n):
    require(n != 0, "zero has no finite valuation")
    n = abs(n)
    return (n & -n).bit_length() - 1


def paired_table():
    z, dual = Fraction(-3239, 729), Fraction(-734, 81)
    rows = []
    for clock in range(11):
        require((z.numerator + dual.numerator) % 2 == 1,
                "signed pair lost complementary parity")
        rows.append({"clock": clock, "shadow": str(z), "dual": str(dual)})
        if clock < 10:
            z, dual = shortcut(z), shortcut(dual)
    require((z, dual) == (Fraction(-1), Fraction(0)), "wrong fixed pair")
    require(shortcut(z) == z and shortcut(dual) == dual, "pair is not fixed")
    return rows


def family_control(h):
    b = 341 + 486 * h
    x, rem = divmod((1 << (b + 11)) - 7207, 729)
    require(rem == 0 and x > 0 and x % 512 == 257, "invalid complete source")
    require(729 * x + 7207 == 1 << (b + 11), "source identity")
    y = (x + 1) // 2
    require(729 * y == (1 << (b + 10)) - 3239, "target identity")
    N, r, a = max(1, y.bit_length()), 4, -734
    L = max(1, max(1, abs(a), 3 ** r).bit_length())
    H = 8 * N + (9 * r + 8) * L + 2
    require((N, L, H) == (b + 1, 10, 8 * b + 450), "candidate height budget")
    first_mismatch = None
    n, candidate = y, Fraction(a, 3 ** r)
    # Carry R_i = 3^b_i*a + 3^r*D_i, retaining the full ordered word.
    carry = a
    complementary_odd_count = 0
    checkpoints = []
    for i in range(H):
        bit = 1 - n % 2
        if candidate.numerator % 2 != bit and first_mismatch is None:
            first_mismatch = i
        carry = 3 ** bit * carry + (3 ** r) * bit * (1 << i)
        complementary_odd_count += bit
        n = (3 * n + 1) // 2 if n % 2 else n // 2
        candidate = shortcut(candidate)
        clock = i + 1
        if clock == b + 10:
            require(carry == 0 and candidate == 0, "wrong end of exact agreement")
        if clock > b + 10:
            require(valuation_two(carry) == b + 10, "forced carry valuation changed")
        if clock in (b + 11, H):
            checkpoints.append({"clock": clock, "carry_binary_valuation": valuation_two(carry),
                                "required_divisibility_holds": carry % (1 << clock) == 0})
    require(first_mismatch == b + 10, "first opposite-parity mismatch")
    require(carry % (1 << H) != 0, "candidate unexpectedly passed its horizon")
    return {"h": h, "b": b, "input_odd_length": 6, "input_residue": x % 512,
            "target_bit_length": N, "candidate_numerator": a,
            "candidate_denominator_exponent": r, "candidate_height_bits": L,
            "required_horizon": H, "first_parity_mismatch": first_mismatch,
            "complementary_odd_count_at_horizon": complementary_odd_count,
            "forced_carry_checks": checkpoints,
            "scope": "failure of this candidate only; no assertion about other candidates"}


def main():
    print(json.dumps({"schema": "collatz-triadic-bridge-controls/v1",
                      "scope": "fixed rational pair and two exact family members; no candidate census",
                      "paired_table": paired_table(),
                      "families": [family_control(h) for h in (0, 1)]}, indent=2))


if __name__ == "__main__":
    main()
