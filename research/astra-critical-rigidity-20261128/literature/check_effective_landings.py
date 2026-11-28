"""Exact finite controls for level counting, packet transport and the determinant cutoff."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
import json
import math


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def vprime(x, prime):
    if isinstance(x, Fraction):
        return vprime(x.numerator, prime) - vprime(x.denominator, prime)
    if x == 0:
        raise ValueError("Zero has no finite valuation")
    count = 0
    while x % prime == 0:
        x //= prime
        count += 1
    return count


def determinant(rows, absolute_terms=False):
    n = len(rows)
    total = 0
    for perm in permutations(range(n)):
        term = math.prod(rows[i][perm[i]] for i in range(n))
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        total += abs(term) if absolute_terms else (-1) ** inversions * term
    return total


def pivot_columns(rows):
    if not rows:
        return []
    matrix = [list(map(Fraction, row)) for row in rows]
    rank = 0
    pivots = []
    for j in range(len(matrix[0])):
        i = next((i for i in range(rank, len(matrix)) if matrix[i][j]), None)
        if i is None:
            continue
        matrix[i], matrix[rank] = matrix[rank], matrix[i]
        pivot = matrix[rank][j]
        for i in range(rank + 1, len(matrix)):
            if matrix[i][j]:
                scale = matrix[i][j] / pivot
                matrix[i] = [a - scale * b for a, b in zip(matrix[i], matrix[rank])]
        pivots.append(j)
        rank += 1
        if rank == len(matrix):
            break
    return pivots


def physical_packets(n, stats):
    """All moving windows with up to five odd letters on the full small positive grid."""
    powers = [3**h for h in range(n + 1)]
    distinct = set()
    for source in range(1, 3**n + 1):
        if source % 3 == 0:
            continue
        h, u, time = n, source, 0
        marks = []
        while h:
            wait = (u & -u).bit_length() - 1
            u >>= wait
            time += wait
            require(u % 3 != 0 and 0 < u <= powers[n], "odd-unit bound")
            marks.append((h, u, time))
            u = (u + powers[h - 1]) // 2
            time += 1
            h -= 1
        marks.append((0, u, time))
        stats["positive_sources"] += 1
        for start in range(n):
            h, u, first = marks[start]
            carry = 0
            for k in range(1, min(5, n - start) + 1):
                t = marks[start + k - 1][2] - first
                carry += powers[h - k] << t
                _, v, end = marks[start + k]
                d = end - first
                require(u + carry == v << d, "full physical packet transport")
                stats["transport_checks"] += 1
                if d >= 2*n:
                    times = tuple(marks[i][2] - first for i in range(start, start + k))
                    distinct.add((h, u, times, d))
    return distinct


def check_box(rows, threshold, stats):
    """Check every reduced bordered determinant against the exact dyadic ledger."""
    pure = [row[2] for row in rows]
    J = pivot_columns(pure)
    r = len(J)
    chosen = [[z[j] for j in J] for z in pure]
    I = pivot_columns(list(zip(*chosen)))
    basis = [chosen[i] for i in I]
    delta = determinant(basis)
    require(delta != 0, "basis minor")
    u_on_basis = [rows[i][1] for i in I]
    numerators = [determinant([line[:j] + [u_on_basis[i]] + line[j+1:]
                              for i, line in enumerate(basis)]) for j in range(r)]
    if r < len(pure[0]):
        stats["boxes_with_pure_column_dependence"] += 1
    certified = True
    for i, (_, u, _) in enumerate(rows):
        if i in I:
            continue
        augmented = [[rows[j][1], *chosen[j]] for j in [*I, i]]
        minor = determinant(augmented)
        require((delta * minor) % (1 << threshold) == 0, "cleared determinant divisibility")
        stats["bordered_minor_checks"] += 1
        if abs(delta) * determinant(augmented, absolute_terms=True) < 1 << threshold:
            require(minor == 0, "height forces vanishing")
            stats["individual_height_cutoffs"] += 1
        else:
            certified = False
    if len(rows) > r and certified:
        for (h, u, z), lin in zip(rows, chosen):
            require(sum(a*b for a, b in zip(numerators, lin)) == delta*u, "numerator in pure span")
        stats["nontrivial_certified_boxes"] += 1
        stats["certified_boxes_with_distinct_levels"] += int(len({row[0] for row in rows}) > 1)


def check_physical(stats):
    for n in range(5, 11):
        packets = physical_packets(n, stats)
        stats["distinct_long_physical_packets"] += len(packets)
        for width in (2, 3, 5):
            boxes = defaultdict(list)
            for h, u, times, d in sorted(packets):
                k = len(times)
                H = k + (h-k)//width*width
                starts = tuple(t//width*width for t in times)
                z = tuple(3**(h-H) << (t-s) for t, s in zip(times, starts))
                coeff = tuple(3**(H-i) << s for i, s in enumerate(starts, 1))
                require((u + sum(c*x for c,x in zip(coeff, z))) % (1 << d) == 0,
                        "normalized common coefficients")
                boxes[k, H, starts].append((h, u, z))
            for rows in boxes.values():
                check_box(rows, 2*n, stats)


def check_moving_level_model(stats):
    # An exact integral matrix exercising the rank-deficient, varying-level case.
    # This tests the algebra separately from the complete physical-grid enumeration.
    threshold = 40
    modulus = 1 << threshold
    row_coefficients = (-2 * pow(9, -1, modulus), -pow(9, -1, modulus)-1, 1)
    rows = []
    for exponent in (0, 1, 4, 6):
        value = Fraction(2 + 2**exponent, 9)
        level_shift = -vprime(value, 3)
        factor = 3**level_shift
        u = value * factor
        require(u.denominator == 1 and vprime(u, 3) == 0, "exact model source level")
        z = (factor, factor << exponent, factor << exponent)
        require((u.numerator + sum(a*x for a,x in zip(row_coefficients,z))) % modulus == 0,
                "fixed model coefficients")
        rows.append((level_shift, u.numerator, z))
    model = Counter()
    check_box(rows, threshold, model)
    require(model["certified_boxes_with_distinct_levels"] == 1, "distinct-level certificate")
    stats["synthetic_certified_distinct_levels"] = len({row[0] for row in rows})


def check_valuation_boxes(stats):
    """Use rational moving coefficients chosen to enforce high and exact-zero rows."""
    for prime, base in ((3, 2), (5, 2), (2, 3)):
        for r in (2, 3, 4):
            T = 7
            for width in (1, 2):
                for c in ([1, *([0] * (r-2)), -base**3 + prime**55],
                          [1, *([0] * (r-2)), -base**3],
                          [Fraction(1, prime**4), *([1] * (r-2)), Fraction(-1, prime**4)]):
                    shift = min(vprime(x, prime) for x in c if x)
                    normalized = [Fraction(x) / (Fraction(prime)**shift) for x in c]
                    high = defaultdict(set)
                    unit = prime**(1 + (math.factorial(r) * base**(r*width)).bit_length())
                    for a in product(range(T + 1), repeat=r):
                        value = sum(x * base**j for x, j in zip(normalized, a))
                        if not value:
                            stats["exact_zero_values_omitted"] += 1
                            continue
                        stats["finite_valuation_rows"] += 1
                        if vprime(value, prime) < vprime(unit, prime):
                            continue
                        rel = tuple(i - a[0] for i in a)
                        lower = tuple(t//width*width for t in rel)
                        row = tuple(base**(i-j) for i,j in zip(rel, lower))
                        high[lower].add(row)
                    for rows in high.values():
                        require(len(pivot_columns(rows)) < r, "high-valuation rational rank drop")
                        stats["nonempty_high_valuation_boxes"] += 1
                        stats["multirow_high_valuation_boxes"] += int(len(rows) > 1)


def main():
    stats = Counter()
    check_physical(stats)
    check_valuation_boxes(stats)
    check_moving_level_model(stats)
    for name in ("nontrivial_certified_boxes", "bordered_minor_checks",
                 "multirow_high_valuation_boxes", "boxes_with_pure_column_dependence"):
        require(stats[name] > 0, name)
    print(json.dumps(dict(sorted(stats.items())), indent=2))


if __name__ == "__main__":
    main()
