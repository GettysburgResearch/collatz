"""Build exact marked first-arrival pairs and independently replay both arms."""

from hashlib import sha256


def check(condition, message):
    if not condition:
        raise ValueError(message)


def step(value):
    return value // 2 if value % 2 == 0 else (3 * value + 1) // 2


def first(start, target, horizon):
    value, odd = start, 0
    for clock in range(horizon + 1):
        if value == target:
            return clock, odd
        if clock < horizon:
            check(value > target, "literal flight stays above the target")
            odd += value % 2
            value = step(value)
    return None


def child(parent, degree, lower=20):
    carry = {2: 7, 3: 37}[degree]
    denominator = 3**degree
    for exponent in range(lower, lower + 2 * denominator):
        numerator = (parent << exponent) - carry
        candidate, remainder = divmod(numerator, denominator)
        if remainder == 0 and candidate % 3:
            check(candidate > 256 * parent, "native first-visit size guard")
            return candidate, exponent
    raise ValueError("primitive-root bank exhausted")


def route(waypoint, precision, residue, clock):
    period = 54 * 3**precision
    check(clock >= period + 11 and waypoint % 3, "two-macro inputs")
    for exponent in range(6, period + 6):
        numerator = (waypoint << clock) - 63 - (7 << exponent)
        source, remainder = divmod(numerator, 81)
        if remainder == 0 and source % 3**precision == residue % 3**precision:
            check(source % 64 == 49 and clock - exponent >= 6, "native address")
            return source, exponent
    raise ValueError("two-macro period exhausted")


def magnitude_digest(value):
    data = value.to_bytes((value.bit_length() + 7) // 8, "big")
    return sha256(data).hexdigest()


def marked_example(target, precision, residue, time_mod, time_class, grade_mod, grade_class, lo):
    fixed = 54 * 3**precision + 11
    current, elapsed, count = target, 0, 0
    for depth in range(400):
        if (4 + count) % grade_mod == grade_class:
            estimate = lo.bit_length() - current.bit_length() - fixed + 7
            for padding in range(max(0, estimate - 4), max(0, estimate + 5)):
                total = fixed + elapsed + padding
                if total % time_mod != time_class:
                    continue
                start, split = route(current << padding, precision, residue, fixed)
                if lo <= start and 16 * start <= 17 * lo:
                    first_arm = first(start, target, total)
                    second_arm = first(5 * start, 5 * target, total)
                    check(first_arm == second_arm == (total, count + 4), "both literal first arrivals")
                    check((total % time_mod, (count + 4) % grade_mod) == (time_class, grade_class), "marks")
                    check(start % 3**precision == residue % 3**precision, "source trits")
                    return depth, split, padding, total, count + 4, magnitude_digest(start)
        for degree in [2] * (grade_mod - 1) + [3]:
            current, additional = child(current, degree)
            elapsed += additional
            count += degree
    raise ValueError("finite fixture depth budget exhausted")


def primitive_records(limit):
    # Each unmerged cylinder has unequal counted endpoints. A common-zero
    # run has length at most 2*limit+4, since an integer carry of size at
    # most 5*3**limit is divided by two at every such step.
    states = [(1, 1, 2, 8, 1, 1)]
    records = {}
    while states:
        height, residue, left, right, grade, companion_grade = states.pop()
        if grade == companion_grade and right == 5 * left:
            records.setdefault(grade, []).append((height, residue))
            continue
        check(height <= 2 * limit * (2 * limit + 5) + 1, "primitive clock bound")
        for bit in (0, 1):
            first_input = left + bit * 3**grade
            second_input = right + bit * 5 * 3**companion_grade
            new_grade = grade + first_input % 2
            new_companion = companion_grade + second_input % 2
            if max(new_grade, new_companion) <= limit:
                states.append(
                    (height + 1, residue + bit * 2**height, step(first_input), step(second_input),
                     new_grade, new_companion)
                )
    return records


def main():
    examples = [
        (1, 1, 2, 3, 1, 2, 0, 11 << 8192),
        (7, 2, 4, 4, 3, 3, 2, 19 << 8192),
        (26, 1, 0, 5, 2, 2, 1, 13 << 8192),
    ]
    expected = {
        1: (8392, 124, "eb058c33dea40144716c4fb2f65ce10ddb3621f3fe9401f67a122a90a2ff3373"),
        7: (9043, 536, "a4236f98f698fa5074e608c7834d60b9feb079c7cd6fad732fb9861dbbd03894"),
        26: (8237, 29, "0698259a66444e59caa57a3a5cd7b4ebcb625bfbedb852c760a1d014fcbd9496"),
    }
    for target, *parameters in examples:
        depth, split, padding, clock, grade, digest = marked_example(target, *parameters)
        check((clock, grade, digest) == expected[target], "pinned physical source and result")
        print(f"PASS target={target} depth={depth} split={split} padding={padding} clock={clock} "
              f"grade={grade} source_sha256={digest}")
    records = primitive_records(5)
    check(records[2] == [(6, 49)] and records[3] == [(8, 65)], "minimal two and three grade records")
    check({g: len(row) for g, row in records.items()} == {2: 1, 3: 1, 4: 5, 5: 15},
          "complete low-grade first-return record enumeration")
    print("PASS all primitive records through grade 5 on both arms")


if __name__ == "__main__":
    main()
