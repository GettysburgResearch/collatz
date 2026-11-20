#!/usr/bin/env python3
"""Small exact regressions for PRIMITIVE_TRACE.md; no all-clock conclusion."""

from fractions import Fraction as F
from itertools import product
import json


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def odd_representative(residue, modulus):
    residue %= modulus
    return residue if residue % 2 else residue + modulus


def odd_step(n):
    value = 3 * n + 1
    gap = 0
    while value % 2 == 0:
        gap += 1
        value //= 2
    return value, gap


def word_data(word):
    coefficient, constant, binary = 1, 0, 1
    for gap in word:
        coefficient *= 3
        constant = 3 * constant + binary
        binary *= 2**gap
    endpoint = odd_representative(
        constant * pow(binary, -1, coefficient), coefficient
    )
    source, remainder = divmod(binary * endpoint - constant, coefficient)
    require(remainder == 0, "canonical source integrality")
    return source, endpoint, coefficient, binary, constant


def replay_words():
    counts = {"words": 0, "ordinary_lifts": 0, "inverse_one_chains": 0}
    for q in range(5):
        for word in product(range(1, 7), repeat=q):
            source, endpoint, ternary, binary, constant = word_data(word)
            require(0 < source < 2 * binary and source % 2, "binary minimum")
            require(0 < endpoint < 2 * ternary and endpoint % 2, "ternary minimum")
            require(binary * endpoint == ternary * source + constant, "affine identity")
            require(endpoint >= F(ternary + constant, binary), "positive-source cutoff")
            for lift in range(4):
                value = source + 2 * binary * lift
                gaps = []
                for _ in word:
                    value, gap = odd_step(value)
                    gaps.append(gap)
                require(tuple(gaps) == word, "direct ordinary valuation replay")
                require(value == endpoint + 2 * ternary * lift, "endpoint lift")
                counts["ordinary_lifts"] += 1
            counts["words"] += 1
    for h in range(1, 41):
        value = 2 * 3**h - 1
        for _ in range(h):
            require((2 * value - 1) % 3 == 0, "inverse-one integrality")
            value = (2 * value - 1) // 3
            require(value > 0 and value % 2, "inverse-one positivity and parity")
        require(value == 2 ** (h + 1) - 1, "inverse-one endpoint")
        counts["inverse_one_chains"] += 1
    return counts


def exact_columns():
    columns = [{0: F(1)}]
    rows = []
    for q in range(6):
        modulus = 3**q
        if q:
            previous = columns[-1]
            period = 2 * 3 ** (q - 1)
            require(pow(2, period, modulus) == 1, "binary order witness")
            require(all(pow(2, d, modulus) != 1 for d in range(1, period)),
                    "binary order minimality in finite regression")
            denominator = 1 - F(1, 2 ** (4 * period))
            current = {}
            for residue in range(modulus):
                endpoint = odd_representative(residue, modulus)
                value = F(0)
                for gap in range(1, period + 1):
                    predecessor_numerator = 2**gap * endpoint - 1
                    if predecessor_numerator % 3 == 0:
                        predecessor = predecessor_numerator // 3
                        value += F(81, 2 ** (4 * gap)) * previous[
                            predecessor % (modulus // 3)
                        ]
                current[residue] = value / denominator
            columns.append(current)
        current = columns[q]
        mass = sum(current.values(), F(0))
        require(mass == F(27, 5) ** q, "exact period mass")
        require(all(value >= 0 for value in current.values()), "positive columns")
        if q:
            require(all(value == 0 for r, value in current.items() if r % 3 == 0),
                    "ternary-unit support")
        head = sum((value / odd_representative(r, modulus) ** 2
                    for r, value in current.items()), F(0))
        quartic = sum((value / odd_representative(r, modulus) ** 4
                       for r, value in current.items()), F(0))
        require(quartic <= F(11, 10), "coarse quartic source budget check")
        rows.append({"q": q, "period_mass": str(mass), "head": str(head),
                     "head_decimal_display_only": float(head),
                     "nonprimitive_geometric_factor": str(F(3, 5) ** q)})

    # Independent word enumeration is a lower sum, never called a complete
    # infinite-gap computation. Its exact omitted mass agrees with the
    # geometric word mass and is nonnegative in every endpoint column.
    for q in range(1, 4):
        modulus = 3**q
        truncated = {r: F(0) for r in range(modulus)}
        for word in product(range(1, 7), repeat=q):
            _, endpoint, ternary, binary, _ = word_data(word)
            truncated[endpoint % modulus] += F(ternary, binary) ** 4
        require(all(columns[q][r] >= truncated[r] for r in range(modulus)),
                "independent word lower sum")
        gap_mass = sum((F(81, 2 ** (4 * a)) for a in range(1, 7)), F(0))
        require(sum(truncated.values(), F(0)) == gap_mass**q, "truncated word mass")
        omitted = sum((columns[q][r] - truncated[r] for r in range(modulus)), F(0))
        require(omitted == F(27, 5) ** q - gap_mass**q, "exact omitted gap mass")

    # A source-wise check uses the physical accelerated map, independently
    # of the inverse-column recurrence.
    physical = 0
    for source in range(1, 501, 2):
        endpoint, weight = source, F(1)
        for q in range(6):
            require(columns[q][endpoint % (3**q)] >= weight**4,
                    "actual source contribution is present in its column")
            endpoint, gap = odd_step(endpoint)
            weight *= F(3, 2**gap)
            physical += 1
    return rows, physical


def model_identities():
    rows = []
    for q in range(21):
        beta_mean = sum((F(1, 3) * F(7, 9) ** j for j in range(q)), F(0))
        require(beta_mean == F(3, 2) * (1 - F(7, 9) ** q), "cutoff model mean")
        require(F(1, 1) / (1 + beta_mean) >= F(2, 5), "Jensen coefficient")
        # The coefficient identity behind the two-sided tail bound.
        require(F(27, 5) ** q / (3**q) ** 2 == F(3, 5) ** q,
                "nonprimitive geometric coefficient")
        rows.append({"q": q, "beta_mean": str(beta_mean)})
    return rows


def main():
    counts = replay_words()
    rows, counts["physical_source_clock_checks"] = exact_columns()
    model = model_identities()
    result = {
        "status": "exact finite regression passed; all-clock moment bound remains open",
        "scope": {
            "map": "accelerated positive odd Collatz map U",
            "state_space": "all positive odd integers, counting measure, no killing",
            "columns": "complete infinite-gap inverse columns through q=5",
            "word_replay": "length at most 4, each gap from 1 through 6, lifts 0 through 3",
            "no_claims": ["quadratic P_q bound", "power-saving tripling boundary upper bound",
                          "exclusion of nontrivial positive cycles", "Collatz proof"]
        },
        "counts": counts,
        "complete_heads": rows,
        "cutoff_model_mean_checks": len(model),
    }
    serialized = json.dumps(result, sort_keys=True, indent=2) + "\n"
    print(serialized, end="")


if __name__ == "__main__":
    main()
