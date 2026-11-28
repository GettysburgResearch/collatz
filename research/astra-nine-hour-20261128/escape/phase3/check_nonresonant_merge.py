"""Check finite same-clock cone certificates and rational profile integrals."""

import json
from fractions import Fraction


def require(condition, detail):
    if not condition:
        raise AssertionError(detail)


def native_rows(largest, horizon):
    rows = {}
    products_checked = 0
    for start in range(1, largest + 1):
        state = start
        grade = 0
        correction = Fraction(1)
        path = []
        for tick in range(horizon + 1):
            require(
                correction * 3**grade * start == 2**tick * state,
                ("affine product", start, tick),
            )
            path.append((state, correction))
            products_checked += 1
            if state % 2:
                correction *= Fraction(3 * state + 1, 3 * state)
                state = (3 * state + 1) // 2
                grade += 1
            else:
                state //= 2
        rows[start] = path
    return rows, products_checked


def cone_checks():
    largest_base = 128
    horizon = 96
    rows, product_checks = native_rows(6 * largest_base, horizon)
    cone_meets = 0
    fivefold_meets = 0
    pairs = 0
    for start in range(1, largest_base + 1):
        for partner in range(4 * start, 6 * start + 1):
            pairs += 1
            # Largest c allowed by 3*c*x <= y and c*y <= 9*x.
            floor = min(Fraction(partner, 3 * start), Fraction(9 * start, partner))
            require(floor >= Fraction(4, 3), ("cone", start, partner))
            for tick, (first, second) in enumerate(zip(rows[start], rows[partner])):
                if first[0] != second[0]:
                    continue
                cone_meets += 1
                require(
                    max(first[1], second[1]) >= floor,
                    ("same-clock correction", start, partner, tick),
                )
                if partner == 5 * start:
                    fivefold_meets += 1
                    require(floor == Fraction(5, 3), ("fivefold", start))
    require(fivefold_meets > 0, "empty fivefold control")
    return {
        "base_starts": largest_base,
        "horizon": horizon,
        "trajectory_product_identities": product_checks,
        "distinct_source_pairs": pairs,
        "potential_pair_dates": pairs * (horizon + 1),
        "same_clock_dates": cone_meets,
        "fivefold_same_clock_dates": fivefold_meets,
    }


def profile_checks():
    # Integrate in v = 3^theta. On each interval away from a jump,
    # A(theta,u)/v is a rational constant for rational u.
    marks = sorted({Fraction(n, d) for d in range(1, 35) for n in range(1, d + 1)})
    powers = [Fraction(3) ** k for k in range(-5, 3)]
    pieces = 0
    for mark in marks:
        cuts = sorted({Fraction(1), Fraction(3)} | {
            power / mark for power in powers if 1 < power / mark < 3
        })
        total = Fraction(0)
        for lower, upper in zip(cuts, cuts[1:]):
            middle = (lower + upper) / 2
            leading_power = next(power for power in powers if power >= middle * mark)
            coefficient = Fraction(3, 2) / leading_power
            total += coefficient * (upper - lower)
            value = middle * coefficient
            require(Fraction(1, 2) <= mark * value <= Fraction(3, 2), ("bounds", mark))
            pieces += 1
        require(total == 1 / mark, ("circle integral", mark, total))
    return {"rational_marks": len(marks), "integrated_rational_pieces": pieces}


if __name__ == "__main__":
    print(json.dumps({"cone": cone_checks(), "profile": profile_checks()}, sort_keys=True))
