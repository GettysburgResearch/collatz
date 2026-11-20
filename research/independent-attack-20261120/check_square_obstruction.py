"""An exact open-box obstruction to the powered-block cone comparisons.

This verifies a region of abstract necessary inequalities, not a family
of Collatz cycles.  It is independent of the cubic-descent checker.
"""

from fractions import Fraction as F


LOWER = F(1054, 665)
UPPER = F(485, 306)
CENTER = (F(1, 2), F(1, 2), F(1))
RADIUS = F(1, 100)
ONE, *GAINS = [tuple(F(i == j) for i in range(4)) for j in range(4)]


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def mul(a, scalar):
    return tuple(scalar * x for x in a)


def sub(a, b):
    return add(a, mul(b, -1))


def value(a, point=CENTER):
    return a[0] + sum(x * y for x, y in zip(a[1:], point))


def extrema(a, radius=RADIUS):
    error = radius * sum(abs(x) for x in a[1:])
    return value(a) - error, value(a) + error


def forms(c):
    gamma = c - 1
    heights = [ONE]
    costs = []
    for gain in GAINS:
        costs.append(sub(heights[-1], mul(gain, (2-c) / gamma)))
        heights.append(add(heights[-1], mul(gain, 2)))
    drop = mul(sub(heights[-1], ONE), F(1, 2))
    descent_cost = add(drop, mul(ONE, 1-c/gamma))
    floor = 2*c/gamma - 1
    domain = GAINS + costs + [sub(heights[-1], mul(ONE, floor))]

    tests = []
    for i in range(3):
        for j in range(i + 1, 3):
            for k in (1, 2):
                charge = add(mul(costs[i], k), costs[j])
                savings = (mul(GAINS[i], k), GAINS[j],
                           mul(heights[i+1], 1/c))
                tests.append((f"rise {i+1} to rise {j+1}, k={k}",
                              tuple(sub(s, charge) for s in savings)))
        for k in (1, 2):
            for ell in (1, 2):
                charge = add(mul(costs[i], k), mul(descent_cost, ell))
                savings = (mul(GAINS[i], k), mul(drop, ell),
                           mul(heights[i+1], 1/c))
                tests.append((f"rise {i+1} to descent, k={k}, ell={ell}",
                              tuple(sub(s, charge) for s in savings)))

    total_charge = mul(descent_cost, 2)
    for cost in costs:
        total_charge = add(total_charge, mul(cost, 2))
    full_margin = sub(heights[-1], total_charge)
    return domain, tests, full_margin


def failure_certificate(margins, radius=RADIUS):
    """Return a margin that is strictly negative everywhere in the box."""
    eligible = [(extrema(m, radius)[1], index)
                for index, m in enumerate(margins)
                if extrema(m, radius)[1] < 0]
    return min(eligible) if eligible else None


def main():
    require(3**665 > 2**1054, "lower bound for log2(3)")
    require(3**306 < 2**485, "upper bound for log2(3)")
    require(F(1) < LOWER < UPPER < F(2), "logarithm bracket")

    # Domain requirements become weaker as c grows, and all charged
    # comparison margins become smaller.  LOWER is therefore the
    # strongest endpoint for this obstruction, as proved in the note.
    domain, tests, full_margin = forms(LOWER)
    domain_margin = min(extrema(row)[0] for row in domain)
    require(domain_margin > 0, "whole box lies in the strict domain")
    failure_gaps = []
    for tag, margins in tests:
        certificate = failure_certificate(margins)
        require(certificate is not None, f"unexcluded comparison: {tag}")
        maximum, _ = certificate
        failure_gaps.append(-maximum)
    require(extrema(full_margin)[1] < 0, "full displacement margin fails")

    # A larger box crosses a domain face, so domain feasibility must fail.
    require(any(extrema(row, F(1))[0] < 0 for row in domain),
            "oversized-box mutation must be rejected")
    # Erasing multiplier charges would falsely turn a comparison into
    # a success.  Our failure checker must not certify that mutation.
    charge_free = (GAINS[0], GAINS[1], mul(add(ONE, mul(GAINS[0], 2)), 1/LOWER))
    require(failure_certificate(charge_free) is None,
            "zero-charge mutation must not be certified as a failure")

    print("logarithm interval:", LOWER, "< log2(3) <", UPPER)
    print("center:", tuple(map(str, CENTER)), "radius:", RADIUS)
    print("strict domain margin:", domain_margin)
    print("failed charge comparisons:", len(tests))
    print("weakest certified charge-failure gap:", min(failure_gaps))
    print("full displacement maximum margin:", extrema(full_margin)[1])
    print("negative controls: oversized box rejected; zero-charge mutation rejected")
    print("PASS: whole rational box survives all stated square-descent comparisons")


if __name__ == "__main__":
    main()
