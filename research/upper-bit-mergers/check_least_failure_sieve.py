"""Enumerate sparse dyadic test sets and check the exponent-lifting certificates."""

from check_deep_reverse_basin import CERTIFICATES


def retained_indices(depth):
    """Yield the retained indices in [2**depth, 2**(depth+1)), in parity-word order."""
    modulus = 1 << depth
    inverse_27 = pow(27, -1, modulus)
    stack = [(0, 1, 0)]
    while stack:
        length, odd_factor, offset = stack.pop()
        if (odd_factor << 16) < (1 << length):
            continue
        if length == depth:
            start = -offset * pow(odd_factor, -1, modulus)
            index = modulus + (start - 1) * inverse_27 % modulus
            if index % 4:
                yield index
            continue
        stack.append((length + 1, odd_factor, offset))
        stack.append((length + 1, 3 * odd_factor, 3 * offset + (1 << length)))


def first_cut(index):
    """Return the actual orbit value at the first failing prefix, if there is one."""
    value = 27 * index + 1
    odd_factor = 1
    for length in range(1, index.bit_length()):
        if value % 2:
            odd_factor *= 3
            value = (3 * value + 1) // 2
        else:
            value //= 2
        if (odd_factor << 16) < (1 << length):
            return value
    return None


def directly_retained(index):
    return index % 4 != 0 and first_cut(index) is None


def descent_dependencies(index):
    """Return smaller comparison indices for a discarded eligible index."""
    if index <= 0 or index % 4 == 0:
        raise ValueError("expected a positive index not divisible by four")
    value = first_cut(index)
    if value is None:
        raise ValueError("the index is retained")
    while value % 2 == 0:
        value //= 2
    if value % 3 == 0:
        value = (3 * value + 1) // 2
    dependencies = []
    while value > 1:
        if value % 2 == 0:
            value //= 2
            continue
        start = value
        word = next(word for modulus, residue, word in CERTIFICATES
                    if start % modulus == residue)
        for token in word.split():
            if token == "M":
                if value % 18 != 9:
                    raise AssertionError("ineligible tripling")
                h = value // 9
                dependencies.extend((h, 2 * h))
                value *= 3
            elif token.startswith("S"):
                value, remainder = divmod(3 * value + 1, 1 << int(token[1:]))
                if remainder:
                    raise AssertionError("nonintegral forward step")
            else:
                value, remainder = divmod((value << int(token[1:])) - 1, 3)
                if remainder or not value % 2:
                    raise AssertionError("invalid inverse step")
        if not 0 < 25 * value <= 24 * start or not value % 3:
            raise AssertionError("failed unit descent")
    if any(8 * (128 * j + 1) >= 5 * (128 * index + 1) for j in dependencies):
        raise AssertionError("conditional upper start exceeds bound")
    return dependencies


def check_exponent_progression(first, spacing):
    """Lift the exponent one ternary digit at a time without constructing 2**e."""
    if first % 162 != 119 or spacing <= 0 or spacing % 162:
        raise ValueError("progression is outside the rank-five family")
    depth = 1
    while pow(2, spacing, 3 ** (depth + 1)) == 1:
        depth += 1
    # One representative suffices to choose the first depth inverse exponents.
    representative = pow(2, first, 3**depth) - 1
    scale, offset = 1, 0
    for used in range(depth):
        shift = 1 if representative % 3 == 2 else 2
        if used + 1 < depth and (representative << shift) % 9 == 1:
            shift += 2
        numerator = (representative << shift) - 1
        if numerator % 3:
            raise AssertionError("nonintegral inverse prefix")
        representative = numerator // 3
        scale <<= shift
        offset = (offset << shift) + 3**used

    length = 5 * depth + 30
    target = 3**depth
    lift = 0
    for digit in range(length):
        modulus = target * 3 ** (digit + 1)
        options = []
        for next_digit in range(3):
            candidate = lift + next_digit * 3**digit
            value = pow(2, first + spacing * candidate, modulus) - 1
            if (scale * value - offset + target) % modulus == 0:
                options.append(candidate)
        if len(options) != 1:
            raise AssertionError("expected a unique ternary lift")
        lift = options[0]
    if 176106 * scale * 2**length >= 3 ** (depth + length):
        raise AssertionError("insufficient contraction")


def main():
    for depth in range(18):
        lower = 1 << depth
        direct = {k for k in range(lower, 2 * lower) if directly_retained(k)}
        generated = list(retained_indices(depth))
        if len(generated) != len(direct) or set(generated) != direct:
            raise AssertionError(("dyadic enumeration mismatch", depth))
    # A pruning boundary above 16 bits, checked without exhaustively scanning a large block.
    if directly_retained((1 << 19) + (-pow(27, -1, 1 << 18)) % (1 << 18)):
        raise AssertionError("all-even prefix should be pruned")
    dependency_count = 0
    for unit in (23, 43, 55, 811):
        shift = next(s for s in range(24, 42) if (unit << s) % 27 == 1)
        dependency_count += len(descent_dependencies(((unit << shift) - 1) // 27))
    if dependency_count == 0:
        raise AssertionError("no directed comparison exercised")
    for j in range(5):
        power = 1 << (119 + 162 * j)
        index, remainder = divmod(8 * power - 22, 243)
        if remainder or not directly_retained(index):
            raise AssertionError("rank-five index pruned")
    if pow(2, 119, 243) != 185:
        raise AssertionError("wrong ternary center")
    for first, spacing in [(119, 162), (281, 324), (767, 1458), (605, 1134)]:
        check_exponent_progression(first, spacing)
    print(f"Dyadic enumeration, {dependency_count} smaller comparisons, "
          "Mersenne survivors and four exact ternary subprogressions passed.")


if __name__ == "__main__":
    main()
