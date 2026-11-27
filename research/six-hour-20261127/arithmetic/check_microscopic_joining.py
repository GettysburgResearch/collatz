"""Exact one-copy pressure supplement for the full-width rank-gap joining."""
from fractions import Fraction
from hashlib import sha256
import json

from check_anchor_carries import require, schedules


def path_counts(word):
    totals = []
    for terminal in range(3):
        counts = [int(k == terminal) for k in range(3)]
        for m in map(int, word):
            counts = [sum(count for later, count in enumerate(counts)
                          if x <= 3-m and 1 <= m+x-later <= 2) for x in range(3)]
        totals.append(sum(counts))
    return totals


def check():
    records = []
    for word in schedules():
        totals = path_counts(word)
        require(max(totals)**250 < 2**(189*len(word)), "uniform single-history pressure")
        records.append({"length": len(word), "reverse_sha256": sha256(word.encode()).hexdigest(),
                        "path_counts": totals})
    require(3**12 > 2**19 and Fraction(19, 24)-Fraction(189, 250) > Fraction(1, 30)
            and Fraction(19, 25)-Fraction(189, 250) == Fraction(1, 250), "entropy margins")
    require(300**300 < 2**10*299**299, "binary prediction error")
    return {"return_paths": records, "single_entropy_upper": "189/250",
            "microscopic_conditional_entropy_lower_strict": "1/30",
            "twelfth_power_conditional_entropy_lower_strict": "1/250",
            "microscopic_prediction_error_strict": "1/300"}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
