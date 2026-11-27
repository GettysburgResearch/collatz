"""Independently compare the interval checker with exact geometric periods."""

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("interval_report", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.interval_report.read_text())
    scale = int(data["scale"])
    assert data["status"] == "PASS" and scale == 2**88
    assert data["precision_bits"] == 88 and data["tail_terms"] == 112
    assert [row["depth"] for row in data["rows"]] == list(range(1, 15))
    old = [Fraction(1)]
    checks = []
    for depth in range(1, 6):
        modulus = 3**depth
        exponent_period = 2 * 3**(depth - 1)
        powers = [pow(2, e, modulus) for e in range(1, exponent_period + 1)]
        new = []
        for residue in range(modulus):
            if residue % 3 == 0:
                new.append(Fraction(0))
                continue
            value = Fraction(0)
            for exponent, power in enumerate(powers, 1):
                numerator = power * residue - 1
                if numerator % 3 == 0:
                    value += Fraction(3, 2**exponent) * old[(numerator // 3) % len(old)]
            new.append(value / (1 - Fraction(1, 2**exponent_period)))
        delta = [(new[y % modulus] - old[y % len(old)]) / y
                 for y in range(1, 2 * modulus, 2)]
        signed, absolute = sum(delta), sum(map(abs, delta))
        row = data["rows"][depth - 1]
        for prefix, exact in [("signed", signed), ("absolute", absolute)]:
            lower = Fraction(int(row[prefix + "_lower_numerator"]), scale)
            upper = Fraction(int(row[prefix + "_upper_numerator"]), scale)
            assert lower <= exact <= upper
        checks.append({"depth": depth, "signed_exact": str(signed),
                       "absolute_exact": str(absolute), "passed": True})
        old = new
    last = data["rows"][-1]
    assert int(last["signed_lower_numerator"]) > 0
    assert data["signed_depth_14_positive"] is True
    result = {
        "status": "PASS",
        "scope": "Exact full-period Fraction formulas through depth five independently confirm the C++ recurrence enclosures. The positive sign at depth fourteen uses the C++ integer enclosure proof and computation, not a full rational-law reconstruction at that depth.",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "interval_report_sha256": hashlib.sha256(args.interval_report.read_bytes()).hexdigest(),
        "independent_exact_checks": checks,
        "depth_fourteen_sign_verified_from_integer_bound": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print("PASS: five independent exact laws; positive depth-fourteen interval.")


if __name__ == "__main__":
    main()
