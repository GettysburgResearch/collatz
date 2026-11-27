"""Check finite cylinder transfer, its Taylor cancellations, and pressure barriers exactly."""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path


def require(test, text):
    if not test:
        raise ValueError(text)


def unit_classes(modulus):
    return [a for a in range(1, modulus) if a % 3]


def branch_rows(modulus):
    """For each parent mod 3*modulus, give the inverse exponent for each unit child."""
    period = 2 * modulus
    next_modulus = 3 * modulus
    logs = {pow(2, e, next_modulus): e for e in range(1, period + 1)}
    require(len(logs) == period, "two did not generate the required unit group")
    children = unit_classes(modulus)
    rows = {}
    for z in unit_classes(next_modulus):
        inverse = pow(z, -1, next_modulus)
        rows[z] = [logs[(3 * x + 1) * inverse % next_modulus] for x in children]
        require(len(set(rows[z])) == len(children), "two children shared an exponent")
        require(all(((z << e) - 1) // 3 % modulus == x for x, e in zip(children, rows[z])),
                "integer inverse residue mismatch")
    return children, rows


def regular_transfer(values, modulus, tail):
    children, rows = branch_rows(modulus)
    period = 2 * modulus
    weights = [None] + [3 * (1 - tail) * tail ** (e - 1) / (1 - tail ** period)
                         for e in range(1, period + 1)]
    next_values = {z: sum(values[x] * weights[e] for x, e in zip(children, es))
                   for z, es in rows.items()}
    require(sum(next_values.values()) == 3 * sum(values.values()), "unit Haar not preserved")
    return next_values


def series_multiply(a, b):
    return [sum(a[j] * b[i-j] for j in range(i + 1)) for i in range(len(a))]


def series_divide(a, b):
    """Quotient of truncated rational power series with invertible constant."""
    answer = []
    for i in range(len(a)):
        answer.append((a[i] - sum(answer[j] * b[i-j] for j in range(i))) / b[0])
    return answer


def jet_transfer(values, modulus, order):
    children, rows = branch_rows(modulus)
    period = 2 * modulus
    # p=1-exp(-t). The grouped branch weight is 3(1-p)^(e-1) / sum(1-p)^i.
    # The denominator coefficient is (-1)^k * binom(period,k+1) by hockey-stick.
    den = [Fraction((-1) ** k * comb(period, k+1)) for k in range(order+1)]
    weights = {}
    for e in range(1, period+1):
        num = [Fraction(3 * (-1) ** k * comb(e-1, k)) for k in range(order+1)]
        weights[e] = series_divide(num, den)
    next_values = {}
    for z, exponents in rows.items():
        jet = [Fraction(0)] * (order + 1)
        for x, e in zip(children, exponents):
            for i, value in enumerate(series_multiply(values[x], weights[e])):
                jet[i] += value
        next_values[z] = jet
    for k in range(order+1):
        require(sum(j[k] for j in next_values.values()) == 3 * sum(j[k] for j in values.values()),
                "Taylor coefficient of the Haar mean changed")
    return next_values


def rational_bounds():
    tail = Fraction(99, 100)
    modulus = 3
    values = {z: Fraction(1) for z in unit_classes(modulus)}
    reports = []
    for m in range(3):
        after = regular_transfer(values, modulus, tail)
        ratios = [v / values[z % modulus] for z, v in after.items()]
        low, high = min(ratios), max(ratios)
        require(low <= 1 <= high, "bad positive barriers")
        # Independently consume all bounds one more step.
        extra = regular_transfer(after, 3 * modulus, tail)
        for z, v in extra.items():
            h = values[z % modulus]
            require(low ** 2 * h <= v <= high ** 2 * h, "two-step positive barrier failed")
        margin = max(abs(1-low), abs(high-1))
        reports.append({"correction_depth": m, "parent_classes": len(after),
                        "two_step_children": len(extra),
                        "relative_error_below": str(Fraction(1, 1 // margin)),
                        "ratio_sha256": sha256(repr((low,high)).encode()).hexdigest()})
        modulus *= 3
        values = after
    return reports


def taylor_cancellations():
    order = 4
    modulus = 3
    values = {z: [Fraction(1)] + [Fraction(0)] * order for z in unit_classes(modulus)}
    reports = []
    for m in range(4):
        after = jet_transfer(values, modulus, order)
        first = []
        for z, jet in after.items():
            delta = [a - b for a, b in zip(jet, values[z % modulus])]
            require(all(c == 0 for c in delta[:m+1]), "defect jet starts too early")
            first.append(delta[m+1])
        require(any(v != 0 for v in first), "leading finite coefficient unexpectedly zero")
        reports.append({"correction_depth": m, "root_classes": len(after),
                        "zero_jet_through_order": m, "leading_supremum": str(max(map(abs,first)))})
        modulus *= 3
        values = after
    return reports


def report():
    return {"parameter_for_rational_action": "1/100", "finite_positive_bounds": rational_bounds(),
            "exact_jet_cancellations": taylor_cancellations()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    output = json.dumps(report(), sort_keys=True, indent=2) + "\n"
    if args.check:
        require(output == Path(__file__).with_name("PRESSURE_CONTROLS.json").read_text(),
                "finite pressure report changed")
    print(output, end="")
