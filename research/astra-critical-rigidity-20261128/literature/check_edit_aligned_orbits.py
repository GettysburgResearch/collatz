"""Exact arithmetic for two native Collatz clocks with alignment gaps."""

from collections import Counter
from fractions import Fraction
from itertools import groupby


def require(condition, reason):
    if not condition:
        raise ArithmeticError(reason)


def vtwo(n):
    return (abs(n) & -abs(n)).bit_length() - 1


def places_three(n):
    count = 0
    while n % 3 == 0:
        n //= 3
        count += 1
    return count


def dyadic(power):
    return Fraction(2**power) if power >= 0 else Fraction(1, 2 ** -power)


def letter(y, q, clock):
    if clock == "raw":
        b = y % 2
        return (b, 1, b)
    require(y % 2 == 1, "odd physical input")
    e = vtwo(3 * y + q)
    return (e, e, 1)


def step(y, q, move):
    if move is None:
        return y
    _, d, g = move
    num = 3**g * y + g * q
    require(num % (1 << d) == 0, "physical integrality")
    return num // (1 << d)


def make_columns(pair, q, clock, policy):
    states = [pair]
    columns = []
    for i in range(44):
        first, second = (letter(y, q, clock) for y in states[-1])
        if policy and (i + 2 * policy) % 17 == 3:
            first = None
        elif policy and (i + 3 * policy) % 19 == 7:
            second = None
        end = tuple(step(y, q, move) for y, move in zip(states[-1], (first, second)))
        if end[0] == end[1] or any(y * pair[0] <= 0 for y in end):
            break
        states.append(end)
        columns.append((first, second))
    return states, columns


def is_match(pair):
    a, b = pair
    return a is not None and b is not None and a[0] == b[0]


def physical_blocks(columns):
    groups = []
    for matching, indexed in groupby(enumerate(columns), key=lambda entry: is_match(entry[1])):
        positions = [i for i, _ in indexed]
        if matching:
            middle = len(positions) // 2
            # Mimic a split on macroscopic runs without making a field-rank claim.
            if len(positions) >= 5:
                groups += [positions[:middle], positions[middle:]]
            else:
                groups.append(positions)
        else:
            groups += [[i] for i in positions]
    return groups


def carry(moves):
    d, g, value = 0, 0, 0
    for move in moves:
        if move is None:
            continue
        _, ds, gs = move
        value = 3**gs * value + gs * (1 << d)
        d += ds
        g += gs
    return d, g, value


def replay(pair, q, clock, policy, counts):
    states, columns = make_columns(pair, q, clock, policy)
    if len(columns) < 3:
        return
    counts["paths"] += 1
    counts[clock] += 1
    counts["negative_paths"] += pair[0] < 0
    counts["columns"] += len(columns)
    counts["indels"] += sum(a is None or b is None for a, b in columns)
    counts["substitutions"] += sum(a is not None and b is not None and a[0] != b[0]
                                   for a, b in columns)
    subblocks = physical_blocks(columns)
    divis, grades, weight = [0, 0], [0, 0], 0
    partial = [Fraction(v) for v in pair]
    carry_product = 1
    block_cost = 1
    for positions in subblocks:
        start, end = positions[0], positions[-1] + 1
        inputs, outputs = states[start], states[end]
        run = is_match(columns[start])
        data = [carry([columns[i][j] for i in positions]) for j in range(2)]
        common_grade = sum(max(m[2] if m is not None else 0 for m in columns[i])
                           for i in positions)
        old_divis = divis.copy()
        weight += common_grade
        for j, (d, g, c) in enumerate(data):
            require((1 << d) * outputs[j] == 3**g * inputs[j] + q * c, "raw affine carry")
            divis[j] += d
            grades[j] += g
        c = max(a[2] for a in data)
        if run:
            require(data[0] == data[1], "matching block")
            require((inputs[1] - inputs[0]) % (1 << data[0][0]) == 0,
                    "true-start difference divisor")
        else:
            require(len(positions) == 1 and c in (0, 1), "defect carry")
        if c:
            require(c % 3, "ternary-unit carry")
            coordinate = Fraction(q * c * (1 << old_divis[0]), 3**weight)
            require(places_three(coordinate.numerator) - places_three(coordinate.denominator)
                    == -weight, "ternary weight")
            norm_two = dyadic(vtwo(coordinate.denominator) - vtwo(coordinate.numerator))
            require(abs(coordinate) * norm_two ==
                    Fraction(q * c, (1 << vtwo(c)) * 3**weight), "two-place product")
            counts["even_carries"] += c % 2 == 0
            for j in range(2):
                if data[j][2]:
                    require(data[j][2] == c, "one available shared carry")
                    coefficient = dyadic(old_divis[j] - old_divis[0]) * 3 ** (weight - grades[j])
                    partial[j] += coefficient * coordinate
                else:
                    counts["one_sided_forms"] += 1
            carry_product *= q * c
            block_cost *= q * ((1 + q) * (common_grade + 1) if run else 1)
        else:
            counts["carry_free_blocks"] += 1
        for j in range(2):
            require(partial[j] == Fraction((1 << divis[j]) * outputs[j], 3 ** grades[j]),
                    "normalized physical telescope")
        counts["unequal_grade_cuts"] += grades[0] != grades[1]
        counts["unequal_dyadic_cuts"] += divis[0] != divis[1]

    start_envelope = max(map(abs, pair)) + q
    end_envelope = max(map(abs, states[-1])) + q
    require(carry_product * end_envelope <=
            3**weight * Fraction(3, 2)**weight * start_envelope * block_cost,
            "single-envelope carry product")
    counts["graded_columns"] += weight


def main():
    counts = Counter()
    for sign in (1, -1):
        for q in (1, 5, 7, 11):
            for base in (17, 27, 41, 73, 127, 255):
                for shift in (4, 9, 15):
                    pair = sign * base, sign * (base + (1 << shift))
                    for policy in (0, 1, 3):
                        for clock in ("raw", "odd"):
                            replay(pair, q, clock, policy, counts)
    require(counts["paths"] > 500 and counts["even_carries"] > 100, "coverage of both clocks")
    require(min(counts[key] for key in ("indels", "carry_free_blocks",
                                        "one_sided_forms", "unequal_grade_cuts")) > 500,
            "asynchronous and empty-coordinate controls")
    for name, total in sorted(counts.items()):
        print(name, total)


if __name__ == "__main__":
    main()
