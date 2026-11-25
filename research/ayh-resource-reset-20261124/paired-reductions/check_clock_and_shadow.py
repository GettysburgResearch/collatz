"""Independent finite arithmetic for the pointwise clock and ternary transfer."""
from collections import Counter
import argparse
import json
from math import comb
from pathlib import Path


def require(test, label):
    if not test:
        raise ValueError(label)


def shortcut(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def check(bank):
    max_first_hit = (0, 1)
    max_first_drop = (0, 1)
    for n in range(1, 2720):
        x = n
        hit = 0
        drop = None
        while x != 1:
            x = shortcut(x)
            hit += 1
            if x < n and drop is None:
                drop = hit
            require(hit <= 132, "small trajectory exceeded the replay budget")
        max_first_hit = max(max_first_hit, (hit, n))
        if n > 1:
            max_first_drop = max(max_first_drop, (drop, n))
    require(max_first_drop[0] == 81 and max_first_hit[0] == 132, "small cutoff")
    for B, p, h in [(226, 620, 984), (2720, 646, 1024)]:
        require((3 * B + 1) ** p < B**p * 2**h, "successful cutoff")
        require((3 * B - 2) ** p >= (B - 1) ** p * 2**h, "preceding cutoff")
        require(3 ** (p + 1) >= 2**h, "reverse cutoff")
    period = 3**10
    coverage = set()
    for row in json.loads(bank.read_text()):
        step = 3 ** (row["depth"] - 4)
        cells = set(range(row["index"], period, step))
        require(cells.isdisjoint(coverage), "overlapping existing ternary certificate")
        coverage.update(cells)
    require(len(coverage) == 1000, "existing certificate population")
    m = 1
    counts = Counter()
    covered = 0
    one_row = []
    for t in range(period):
        counts[m] += 1
        covered += m in coverage
        if m % 2187 == 181:
            one_row.append(t)
        m = (262144 * m + 165053) % period
    require(len(counts) == period and max(counts.values()) == 1 and m == 1, "permutation")
    require(covered == 1000, "pullback population")
    require(one_row == list(range(2034, period, 2187)), "exact explicit rescue progression")
    parity = []
    x = 17
    for _ in range(4):
        parity.append(x % 2)
        x = shortcut(x)
    require(parity == [1, 0, 1, 0], "fixed leading word")
    tail = sum(comb(1020, k) for k in range(619, 1021))
    require(tail << 37 < 2**1020 < tail << 38, "binomial tail")
    return {
        "small_ordinary_sources": [1, 2719],
        "max_first_drop_with_one_witness": max_first_drop,
        "max_first_hit_with_one_witness": max_first_hit,
        "least_floor_for_count_620_factor_2pow40": 226,
        "least_floor_for_count_plus_exponent_646": 2720,
        "eligible_least_defect_tail_exact": f"{tail}/{2**1020}",
        "eligible_least_defect_tail_decimal": tail / 2**1020,
        "prior_ternary_bank_rows": len(json.loads(bank.read_text())),
        "shadow_t_period_checked": period,
        "prior_ternary_bank_covered_t": covered,
        "prior_ternary_bank_uncovered_t": period-covered,
        "third_query_t_residue_mod_2187": one_row[0],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bank", type=Path)
    args = parser.parse_args()
    print(json.dumps(check(args.bank), indent=2))
