"""
Barrier Falsification Harness for GettysburgResearch/collatz [PR #149 / STATE.md].
Tests any candidate Collatz invariant/predicate against known non-Z^+ obstructions:
  1. Negative integer cycles (-1, -5, -17)
  2. The STATE.md '1110' negative rational ghost (-19/11)
  3. PR #149-style positive noninteger rational cycles in Z_2 cap Z_3 (23/5, 19/5, 211/13, 259/13)
"""
import json
from fractions import Fraction


def T_rational(x: Fraction) -> Fraction:
    """Exact 2-adic shortcut Collatz map on Z_(2) = {a/b : b odd}."""
    assert x.denominator % 2 == 1, f"Not in Z_(2): {x}"
    if x.numerator % 2 == 0:
        return x / 2
    return (3 * x + 1) / 2


def verify_cycle(x0: Fraction, expected_period: int):
    cur = x0
    orbit = [str(cur)]
    for _ in range(expected_period):
        cur = T_rational(cur)
        orbit.append(str(cur))
    return {
        "x0": str(x0),
        "positive": (x0 > 0),
        "in_Z2_cap_Z3": (x0.denominator % 2 != 0 and x0.denominator % 3 != 0),
        "is_integer": (x0.denominator == 1),
        "expected_period": expected_period,
        "closes_exactly": (cur == x0),
        "orbit_preview": orbit[:min(6, len(orbit))]
    }


def main():
    obstructions = [
        ("trivial_positive_cycle", Fraction(1, 1), 2),
        ("neg_int_cycle_1", Fraction(-1, 1), 1),
        ("neg_int_cycle_5", Fraction(-5, 1), 3),
        ("neg_int_cycle_17", Fraction(-17, 1), 11),
        ("state_md_1110_ghost", Fraction(-19, 11), 4),
        ("pr149_pos_rational_11010", Fraction(23, 5), 5),
        ("pr149_pos_rational_11100", Fraction(19, 5), 5),
        ("pr149_pos_rational_11111000", Fraction(211, 13), 8),
        ("pr149_pos_rational_11110010", Fraction(259, 13), 8),
    ]
    report = {}
    all_ok = True
    for name, x0, per in obstructions:
        res = verify_cycle(x0, per)
        report[name] = res
        if not res["closes_exactly"]:
            all_ok = False
    print(json.dumps({"all_obstructions_verified": all_ok, "cases": report}, indent=2))
    assert all_ok, "One or more obstruction cycles failed to close!"


if __name__ == "__main__":
    main()
