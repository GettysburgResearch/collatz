"""Exact uniform bounds for normalized reverse four-copy carries."""
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement, product
from fractions import Fraction
import json

DEN = 1_000_000
SLOPE = 1_584_962
# name, block length, known mod-3 carry precision, width in millionths,
# largest clean exponent, numerator/denominator of a strict source exponent.
CASES = (
    ("bounded_binary", 256, 27, 2_420_000, 2, 3, 8),
)


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


@lru_cache(None)
def end_states(width):
    pair = list(combinations_with_replacement(range(width), 2))
    return tuple(left+right for left in pair for right in pair)


@lru_cache(None)
def transition(old_width, new_width, advance, trits, max_e):
    """One entry per four terminal layers and known signed carry residue."""
    old = {state: i for i, state in enumerate(end_states(old_width))}
    table = []
    for end in end_states(new_width):
        options = [[x for x in range(old_width) if 1 <= advance+y-x <= max_e]
                   for y in end]
        predecessors = Counter()
        for a, b, c, d in product(*options):
            index = old[tuple(sorted((a, b))+sorted((c, d)))]
            digit = (1 << a)+(1 << b)-(1 << c)-(1 << d)
            predecessors[index, digit] += 1
        for residue in range(trits):
            branches = []
            for next_trit in range(3):
                carry = (residue+next_trit*trits) << advance
                branch = tuple((g*trits+((carry+digit)//3 % trits), multiplicity)
                               for (g, digit), multiplicity in predecessors.items()
                               if (carry+digit) % 3 == 0)
                branches.append(branch)
            # Equal next-trit alternatives have the same upper bound.
            table.append(tuple(dict.fromkeys(branches)))
    return tuple(table)


def propagate(values, table):
    return [max(sum(values[i]*count for i, count in branch) for branch in branches)
            for branches in table]


def schedule(point, n, width):
    """point is the intercept in units 1/(2*DEN)."""
    rows = []
    for j in range(n+1):
        phase = point+2*j*SLOPE
        low = -(-phase//(2*DEN))
        top = (phase+2*width)//(2*DEN)
        rows.append((low, top-low+1))
    return rows


def path_labels(point, n, width):
    rows = schedule(point, n, width)
    labels = [(rows[0][1],)]
    for (low, size), (later, new_size) in zip(rows, rows[1:]):
        labels.append((size, new_size, later-low))
    return labels


def envelope(n, trits, width, max_e):
    cuts = sorted({0, DEN} | {(-j*SLOPE) % DEN for j in range(n+1)}
                  | {(-j*SLOPE-width) % DEN for j in range(n+1)})
    points = {2*x for x in cuts[:-1]} | {x+y for x, y in zip(cuts, cuts[1:])}
    # A common prefix of row shapes has exactly the same counting vector.
    tree = {}
    for point in sorted(points):
        node = tree
        for label in path_labels(point, n, width):
            node = node.setdefault(label, {})
    number = 0
    largest = 0

    def visit(subtree, values):
        nonlocal number, largest
        if not subtree:
            number += 1
            largest = max(largest, max(values))
        for label, child in subtree.items():
            table = transition(*label, trits, max_e)
            visit(child, propagate(values, table))

    for (start_width,), child in tree.items():
        visit(child, [1]*(len(end_states(start_width))*trits))
    return len(points), number, largest


def literal_checks():
    tested = 0
    for point, width, max_e in ((155000, 2420000, 2), (61001, 1587000, 3)):
        n, trits = 6, 9
        rows = schedule(point, n, width)
        first, last = rows[0][0], rows[-1][0]
        carries = Counter()
        for word in product(range(1, max_e+1), repeat=n):
            grade, affine = first, 0
            for j, e in enumerate(word):
                affine = 3*affine+(1 << (grade-first))
                grade += e
                lo, size = rows[j+1]
                if not lo <= grade < lo+size:
                    break
            else:
                if grade == last:
                    carries[affine] += 1
        sums = Counter()
        for x, nx in carries.items():
            for y, ny in carries.items():
                sums[x+y] += nx*ny
        energy = sum(v*v for v in sums.values())
        # Independently propagate exact signed carries from the fixed endpoint.
        exact = {((0, 0, 0, 0), 0): 1}
        for j in range(n, 0, -1):
            before, old_size = rows[j-1]
            after = rows[j][0]
            advance = after-before
            nxt = Counter()
            for (end, carry), count in exact.items():
                opts = [[x for x in range(old_size) if 1 <= advance+y-x <= max_e]
                        for y in end]
                for states in product(*opts):
                    a, b, c, d = states
                    v = (carry << advance)+(1 << a)+(1 << b)-(1 << c)-(1 << d)
                    if v % 3 == 0:
                        nxt[states, v//3] += count
            exact = nxt
        require(exact.get(((0, 0, 0, 0), 0), 0) == energy and energy > 0,
                "literal ordinary energy equals exact reverse decoding")
        vec = [1]*(len(end_states(rows[0][1]))*trits)
        for (lo, w), (hi, q) in zip(rows, rows[1:]):
            vec = propagate(vec, transition(w, q, hi-lo, trits, max_e))
        require(vec[0] >= sum(exact.values()), "known-zero residue upper bound")
        tested += energy
    return tested


# Width 4963/2500 leaves a strict asymptotic margin above log2(3959/1000).
CAP = Fraction(4963, 2500)-1
RETURN_LIMIT = 147
SLOPE_LOWER = Fraction(58_496_250, 100_000_000)
SLOPE_UPPER = Fraction(58_496_251, 100_000_000)


def log_bounds(reciprocal):
    x = Fraction(1, reciprocal)
    lower = 2*sum(x**(2*i+1)/(2*i+1) for i in range(40))
    return lower, lower+2*x**81/(81*(1-x*x))


def return_cuts(alpha):
    cuts = [(Fraction(0), ("start", 0, 0)), (Fraction(1), ("stop", 0, 0))]
    for j in range(RETURN_LIMIT+1):
        for kind, value in (("integer", 0), ("width", CAP)):
            if j == 0 and kind == "integer":
                continue
            raw = value-j*alpha
            base = raw//1
            cuts.append((raw-base, (kind, j, base)))
    cuts.sort()
    require(len({pos for pos, _ in cuts}) == len(cuts), "distinct rank cuts")
    return cuts


def first_return(alpha, phase):
    starts_forced = phase > CAP
    low, middle, high = 1, 0, 0
    for length in range(1, RETURN_LIMIT+1):
        phase += alpha
        if phase >= 1:
            phase -= 1
            low, middle, high = low, 4*low+middle, low+middle+high
        else:
            low, middle, high = low+middle+high, middle+4*high, high
        if phase > CAP:
            return length, low if starts_forced else None
    raise ArithmeticError("uncovered return phase")


def upper_log_scaled(value, scale):
    # Least j with value**scale <= 3**j, including value=1.
    low, high = -1, value.bit_length()*scale
    power = value**scale
    while high-low > 1:
        mid = (low+high)//2
        if power <= 3**mid:
            high = mid
        else:
            low = mid
    return high


def frequency_certificate():
    ln2, ln3 = log_bounds(3), log_bounds(2)
    require((1+SLOPE_LOWER)*ln2[1] < ln3[0] and
            ln3[1] < (1+SLOPE_UPPER)*ln2[0], "rotation slope")
    require((1 << 4963)*1000**2500 > 3959**2500, "physical width")
    slopes = (SLOPE_LOWER, SLOPE_UPPER)
    extreme = [return_cuts(a) for a in slopes]
    require([v for _, v in extreme[0]] == [v for _, v in extreme[1]],
            "stable return arrangement")
    mid = sum(slopes)/2
    cuts = [x for x, _ in return_cuts(mid)]
    measures = [Counter(), Counter()]
    boundary_types = set()
    longest_initial = 0
    for i, (a, b) in enumerate(zip(cuts, cuts[1:])):
        for pos in (a, (a+b)/2):
            length, energy = first_return(mid, pos)
            if energy is None:
                longest_initial = max(longest_initial, length)
            else:
                boundary_types.add((length, energy))
                if pos != a:
                    for arrangement, mass in zip(extreme, measures):
                        mass[length, energy] += arrangement[i+1][0]-arrangement[i][0]

    require({n for n, _ in boundary_types} == {53, 94, 147}, "return lengths")
    scale = 1000
    logs = {key: upper_log_scaled(key[1], scale) for key in boundary_types}
    upper = []
    for mass in measures:
        require(sum(n*w for (n, _), w in mass.items()) == 1, "return-time mass")
        bound = sum(logs[key]*w for key, w in mass.items())/scale
        require(bound < Fraction(99_999, 100_000), "mean energy margin")
        upper.append(str(bound))

    records = []
    for n, energy in sorted(boundary_types):
        key = (n, energy)
        records.append({"length": n, "energy": energy, "upper_log3_times_1000": logs[key],
                        "phase_measure_at_slope_endpoints": [str(q[key]) for q in measures]})
    return {"physical_ratio": "3959/1000", "width": str(CAP+1),
            "return_limit": RETURN_LIMIT, "longest_initial_delay": longest_initial,
            "cells_including_boundaries": 2*(len(cuts)-1), "returns": records,
            "mean_log3_upper_at_slope_endpoints": upper,
            "strict_log3_energy_exponent": "99999/100000"}


def checks():
    # Exact rational slope enclosure and real-width margins. For a block of
    # at most 256 sites the slope replacement costs <256/10^6 binary units.
    require(1 << SLOPE < 3**DEN < 1 << (SLOPE+1), "clock slope")
    require((1 << 2419)*3**1000 > 16**1000, "wide physical width")
    rows = []
    for name, n, trits, width, max_e, num, den in CASES:
        points, types, value = envelope(n, trits, width, max_e)
        require(value**den < 3**(3*num*n), "strict energy exponent")
        rows.append({"family": name, "odd_block": n, "carry_modulus": trits,
                     "strip_width_millionths": width, "maximum_gap": max_e,
                     "intercepts_tested": points, "different_row_schedules": types,
                     "maximum_quadruple_count": value,
                     "strict_source_exponent": [num, den]})
    return {"literal_energy_sum": literal_checks(), "wide_band": rows[0],
            "sparse_binary_band": frequency_certificate()}


if __name__ == "__main__":
    print(json.dumps(checks(), indent=2))
