#!/usr/bin/env python3
"""Exact residue overlap between the 446 rays and the variable-clock half selector.

For n = n0 + 73728*t, the value T^3(n)+1 changes by 2^10*81*t.
If its base valuation R is at most 8, the short-diamond phase is fixed.
For R >= 9 the selected natural proportion is 1/2, by the valuation
partition and its vanishing divisibility tail. This script checks the finite
classification and the exact rational totals; the density argument is written
in AL27_HALF_ROUTE.md. It does not certify the remaining sources.
"""

from fractions import Fraction
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def short_fraction(n):
    a = (9*n + 13)//8
    require(8*a == 9*n + 13, "Nonintegral three-step endpoint")
    run = (a & -a).bit_length() - 1
    if run >= 9:
        return Fraction(1, 2)
    core = a >> run
    return Fraction(int(pow(3, run, 4)*core % 4 == 1))


def main():
    packet = json.loads(Path(__file__).with_name('al27_certificate.json').read_text())
    cells = set(range(27, 73728, 128))
    unresolved = set(packet['unresolved'])
    require(len(cells) == 576 and len(unresolved) == 130, "Unexpected partition size")
    require(unresolved <= cells, "Unresolved source outside the branch")
    covered = cells - unresolved
    total_half = sum((short_fraction(n) for n in cells), Fraction())
    new = sum((short_fraction(n) for n in unresolved), Fraction())
    partial = sorted(n for n in unresolved if short_fraction(n) == Fraction(1, 2))
    newly_whole = sorted(n for n in unresolved if short_fraction(n) == 1)
    expected = [1819,10011,22299,26395,34587,38683,46875,59163,63259,71451]
    require(total_half == 288, "Half-selector branch density disagrees")
    require(partial == expected and not newly_whole, "Unexpected overlap classification")
    require(new == 5, "Unexpected additional relative coverage")
    union = (len(covered) + new)/576
    require(union == Fraction(451, 576), "Incorrect union density")
    print(json.dumps({
        'status': 'PASS',
        'old_complete_cells': len(covered),
        'old_unresolved_cells': len(unresolved),
        'half_selector_relative_density': str(total_half/576),
        'newly_partial_cells': partial,
        'selected_fraction_in_each_new_partial_cell': '1/2',
        'old_unresolved_cells_still_wholly_uncovered': 120,
        'additional_relative_density': str(new/576),
        'combined_relative_density': str(union),
        'scope': 'Exact finite overlap plus the written natural-density partition; no universal convergence claim.'
    }, indent=2))


if __name__ == '__main__':
    main()
