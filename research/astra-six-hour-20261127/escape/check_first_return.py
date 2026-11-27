"""Check the first-hit cells, defect transport, and stationary loss budget."""

from argparse import ArgumentParser
from array import array
from collections import defaultdict
from fractions import Fraction
from math import ceil

from check_linear_trace import EXTRA, SCALE, enumerated_level, fixed_level


def validate_cells(max_depth=11, max_clock=24, source_cap=40000):
    cells = {(0, 0): [1]}
    forward = defaultdict(set)
    for depth in range(max_depth):
        for clock in range(max_clock + 1):
            for source in cells.get((depth, clock), []):
                for gap in range(1, max_clock - clock + 1):
                    numerator = (source << gap) - 1
                    if numerator % 3:
                        continue
                    parent = numerator // 3
                    if parent == 1:
                        assert (depth, clock, source, gap) == (0, 0, 1, 2)
                        continue
                    next_clock = clock + gap
                    cells.setdefault((depth + 1, next_clock), []).append(parent)
                    old_defect = Fraction(source * 3**depth, 2**clock)
                    new_defect = Fraction(parent * 3**(depth + 1), 2**next_clock)
                    assert old_defect - new_defect == Fraction(3**depth, 2**next_clock)
    for source in range(1, source_cap + 1, 2):
        current, depth, clock = source, 0, 0
        while current != 1 and depth < max_depth and clock < max_clock:
            numerator = 3 * current + 1
            gap = (numerator & -numerator).bit_length() - 1
            current = numerator >> gap
            depth += 1
            clock += gap
        if current == 1 and clock <= max_clock:
            forward[depth, clock].add(source)
    for cell in cells.keys() | forward.keys():
        row = cells.get(cell, [])
        assert len(row) == len(set(row))
        assert {x for x in row if x <= source_cap} == forward[cell]
    return sum(len(row) for row in cells.values()), sum(map(len, forward.values()))


def kappa_enclosure(terms=12):
    partial = sum(Fraction(1, (2*j+1)*7**(2*j+1)) for j in range(terms))
    tail = Fraction(49, 48*(2*terms+1)*7**(2*terms+1))
    return partial, partial + tail


def loss_bounds(row, depth, target_terms=100000):
    q = len(row)
    periods = max(1, ceil(target_terms / q))
    terms = periods * q
    rounded = 0
    for x in range(1, 2*terms, 2):
        rounded += (row[x % q] << EXTRA) // (x*(3*x+1))
    denominator = SCALE << EXTRA
    lower = Fraction(rounded, denominator)
    # The exact odd reciprocal kernel sums to less than one. At period
    # m>=periods use x>=2qm and the exact residue mass q.
    density_error = 3 * (2**depth-1)
    tail = Fraction(periods+1, 12*q*periods**2)
    upper = lower + Fraction(terms, denominator) + Fraction(density_error, SCALE) + tail
    return lower, upper


def outward(value, direction):
    scale = 10**9
    integer = (value.numerator*scale) // value.denominator
    if direction == "up" and value.numerator*scale % value.denominator:
        integer += 1
    return f"{integer//scale}.{integer%scale:09d}"


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--depth", type=int, default=14)
    args = parser.parse_args()
    if not 0 <= args.depth <= 16:
        parser.error("depth must be between zero and sixteen")
    total, checked = validate_cells()
    print(f"# exact inverse cells contain {total} sources; {checked} match the independent forward range")
    kappa_lo, kappa_hi = kappa_enclosure()
    print("depth\tlower_loss\tupper_loss\tcompared_to_log_4_3_over_2\texact_density")
    row = array("Q", [SCALE])
    numerators, denominator = [1], 1
    signs = {}
    for depth in range(args.depth + 1):
        if depth:
            row = fixed_level(row, depth)
            if depth <= 5:
                numerators, denominator = enumerated_level(numerators, denominator)
        if depth <= 5:
            for residue, estimate in enumerate(row):
                actual = Fraction(SCALE*len(row)*numerators[residue], denominator)
                assert 0 <= actual-estimate <= 3*(2**depth-1)
        lower, upper = loss_bounds(row, depth)
        sign = "above" if lower > kappa_hi else "below" if upper < kappa_lo else "overlap"
        signs[depth] = sign
        print(depth, outward(lower, "down"), outward(upper, "up"), sign,
              "yes" if depth <= 5 else "not_run", sep="\t", flush=True)
    if args.depth >= 13:
        assert (signs[12], signs[13]) == ("above", "below")


if __name__ == "__main__":
    main()
