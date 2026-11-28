"""Finite controls for the complete ternary grid and its true landing clocks."""

from collections import Counter
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(x):
    if x.numerator % 2:
        return (3 * x + 1) / 2
    return x / 2


def candidate_word(d, q, length):
    word = 0
    # A common odd denominator works before and after clearing.
    for index in range(length):
        if d % 2:
            word |= 1 << index
            d = (3 * d + q) // 2
        else:
            d //= 2
    return word


def check_residue_cells():
    triples = 0
    counts = 0
    nonuniform_cells = 0
    for h in range(1, 6):
        q = 3**h
        units = [m for m in range(1, q) if m % 3]
        for date in (0, 1, 4, 9):
            inverse = pow(2, -date, q)
            residues = [inverse * m % q for m in units]
            require(sorted(residues) == units, "incomplete ternary permutation")
            for floor in (0, 1, 2, 5):
                for length in range(1, 2 * h + 3):
                    hist = Counter(candidate_word(floor * q + r, q, length)
                                   for r in residues)
                    dyadic = 1 << length
                    require(sum(hist.values()) == len(units), "lost candidates")
                    ceiling = (q + dyadic - 1) // dyadic
                    require(max(hist.values()) <= ceiling, "grid atom cap")
                    if dyadic > q:
                        nonuniform_cells += 1
                    triples += 1
                    counts += len(hist)
    return {"grid_tables": triples, "occupied_word_cells": counts,
            "tables_beyond_one_ternary_interval_of_dyadic_classes": nonuniform_cells}


def check_orbits(n):
    powers = [3**i for i in range(n + 1)]
    q = powers[-1]
    histogram = Counter()
    dates = 0
    exact_steps = 0
    high_prefixes = 0
    block_ledgers = 0
    for m in range(1, q):
        if not m % 3:
            continue
        h, d, t, twopow = n, m, 0, 1
        levels = [h]
        excursion_odds = 0
        excursion_len = 0
        exact = Fraction(m, q) if n <= 5 or m % 997 == 1 else None
        while h:
            old_q = powers[h]
            require(twopow * d % old_q == m % old_q, "time-level congruence")
            require(0 < d <= q and d % 3 != 0, "reduced numerator height")
            k, r = divmod(d, old_q)
            require(0 < r < old_q and k * old_q + r == d, "floor lift")
            if d <= 2 * old_q:
                excursion_odds = 0
                excursion_len = 0
            odd = d % 2
            if odd:
                h -= 1
                d = (d + powers[h]) // 2
            else:
                d //= 2
            t += 1
            twopow <<= 1
            levels.append(h)
            excursion_len += 1
            excursion_odds += odd
            if d > 2 * powers[h]:
                require(2**(excursion_len + excursion_odds + 1)
                        < 7**(excursion_odds + 1), "high excursion odds")
                high_prefixes += 1
            if exact is not None:
                exact = shortcut(exact)
                require(exact == Fraction(d, powers[h]), "raw Fraction replay")
                exact_steps += 1
        require(t <= n * (1 + q.bit_length()), "finite clock horizon")
        # Independently compare each native block with the denominator loss.
        date = 0
        excess = 0
        while levels[date] >= 3 and date + levels[date] <= t:
            height = levels[date]
            end = date + height
            g = sum(a - b for a, b in zip(levels[date:end], levels[date + 1:end + 1]))
            require(g == height - levels[end], "native block grade")
            excess += height - 2 * g
            date = end
            block_ledgers += 1
        require(t - 2 * n == excess + (t - date) - 2 * levels[date],
                "stopped clock identity")
        histogram[t] += 1
        dates += t
    total = sum(histogram.values())
    require(total == 2 * q // 3, "full source grid")
    cumulative = 0
    quantiles = {}
    for value, count in sorted(histogram.items()):
        cumulative += count
        for per_mille in (10, 500, 990):
            if cumulative * 1000 >= total * per_mille:
                quantiles.setdefault(str(per_mille), value)
    return {
        "n": n, "sources": total, "dates": dates, "exact_fraction_steps": exact_steps,
        "high_excursion_prefixes": high_prefixes, "stopped_block_ledgers": block_ledgers,
        "min": min(histogram), "max": max(histogram), "quantiles_per_mille": quantiles,
    }


if __name__ == "__main__":
    print(json.dumps({"cells": check_residue_cells(),
                      "complete_grids": [check_orbits(n) for n in range(1, 10)]},
                     sort_keys=True, indent=2))
