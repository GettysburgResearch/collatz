"""Exact lower populations and pair collisions in the full physical mask.

This is a finite certificate for the moment-method boundary in
FULL_MASK_MOMENTS.md, not a cycle-exclusion certificate.
"""
from collections import Counter
from itertools import product
from pathlib import Path
from fractions import Fraction
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'arithmetic'))
from check_strip_energy import schedules


STATES = {
    b: [q for q in product(range(4-b), repeat=4)
        if sorted(q[:2]) == sorted(q[2:])]
    for b in (1, 2)
}
INCOMING = {
    (b, c): [[i for i, old in enumerate(STATES[b])
              if all(b+old[j]-new[j] in (1, 2) for j in range(4))]
             for new in STATES[c]]
    for b, c in product((1, 2), repeat=2)
}


def demand(ok, message):
    if not ok:
        raise ArithmeticError(message)


def population_row(word, initial):
    row = [int(i == initial) for i in range(4-word[0])]
    for b, c in zip(word, word[1:]):
        row = [sum(count for old, count in enumerate(row)
                   if b+old-new in (1, 2)) for new in range(4-c)]
    return row


def pair_row(word, initial):
    row = [int(q == (initial,)*4) for q in STATES[word[0]]]
    for b, c in zip(word, word[1:]):
        row = [sum(row[i] for i in incoming) for incoming in INCOMING[b, c]]
    return [row[STATES[word[-1]].index((k,)*4)]
            for k in range(4-word[-1])]


def literal_rows(word, initial):
    paths = [(initial,)]
    for b, c in zip(word, word[1:]):
        paths = [p+(new,) for p in paths for new in range(4-c)
                 if b+p[-1]-new in (1, 2)]
    populations, energies = [], []
    for terminal in range(4-word[-1]):
        selected = [p for p in paths if p[-1] == terminal]
        signatures = Counter(tuple(tuple(sorted((x, y))) for x, y in zip(a, b))
                             for a in selected for b in selected)
        populations.append(len(selected))
        energies.append(sum(v*v for v in signatures.values()))
    return populations, energies


def run():
    literal_cuts = 0
    for word in schedules(8):
        for initial in range(4-word[0]):
            populations, energies = literal_rows(word, initial)
            demand(populations == population_row(word, initial),
                   ('literal population', word, initial))
            demand(energies == pair_row(word, initial),
                   ('literal pair signatures', word, initial))
            literal_cuts += len(populations)

    length = 512
    words = schedules(length)
    minimum_population = None
    minimum_energy = None
    cut_cases = 0
    for word in words:
        for initial in range(4-word[0]):
            populations = population_row(word, initial)
            energies = pair_row(word, initial)
            for p, e in zip(populations, energies):
                minimum_population = p if minimum_population is None else min(minimum_population, p)
                minimum_energy = e if minimum_energy is None else min(minimum_energy, e)
                cut_cases += 1
    demand(len(words) == 514 and cut_cases == 2908,
           ('all mechanical phase cells and cut layers', len(words), cut_cases))
    demand(minimum_population**100 > 3**(47*length), '47/100 population lower rate')
    demand(minimum_energy**100 > 3**(109*length), '109/100 fourth-moment lower rate')

    # These affine inequalities cover every real q in the indicated intervals.
    # Endpoints suffice; the last interval also needs a positive slope.
    rate = Fraction(1, 3) + Fraction(1, 30000)
    switch = Fraction(61, 18)
    pieces = [
        (Fraction(1), Fraction(2), Fraction(47, 100), -Fraction(47, 100)),
        (Fraction(2), switch, Fraction(47, 200), Fraction(0)),
        (switch, Fraction(4), Fraction(12, 25), -Fraction(83, 100)),
        (Fraction(4), Fraction(5), Fraction(109, 400), Fraction(0)),
        (Fraction(5), None, Fraction(47, 100), -Fraction(1)),
    ]
    budgets = []
    for lo, hi, slope, intercept in pieces:
        gap = lambda q: slope*q + intercept - rate*(q-1)
        demand(gap(lo) >= 0, ('left budget', lo))
        if hi is not None:
            demand(gap(hi) >= 0, ('right budget', hi))
        else:
            demand(slope > rate, 'infinite-tail budget slope')
        budgets.append({'left': str(lo), 'right': None if hi is None else str(hi),
                        'slope': str(slope), 'intercept': str(intercept),
                        'left_margin': str(gap(lo)),
                        'right_margin': None if hi is None else str(gap(hi))})

    return {
        'scope': 'Full unweighted physical mask; individual absolute moments only',
        'literal_eight_step_cut_checks': literal_cuts,
        'odd_steps': length, 'phase_schedules': len(words), 'fixed_cut_cases': cut_cases,
        'minimum_fixed_cut_population': minimum_population,
        'minimum_fixed_cut_coordinate_pair_energy': minimum_energy,
        'certified_population_lower_base3': '47/100',
        'certified_pair_energy_lower_base3': '109/100',
        'population_upper_input': '../arithmetic/check_rank_support.py: 12/25 per native binary clock',
        'moment_rate_per_q_minus_one': str(rate), 'affine_budgets': budgets,
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
