"""Exact finite counts supporting the ordinary predecessor-minimum density theorem."""

from fractions import Fraction


def first_crossing_counts(maximum, threshold=Fraction(1)):
    # At terminal depth j a first crossing must have total A <= floor(j log2 3).
    cap = (3**maximum).bit_length() - 1
    surviving = [0] * (cap + 1)
    surviving[0] = 1
    counts = []
    for depth in range(1, maximum + 1):
        scaled = 3**depth * threshold.numerator // threshold.denominator
        boundary = scaled.bit_length() - 1
        current = [0] * (cap + 1)
        partial_sum = 0
        for total in range(1, cap + 1):
            partial_sum += surviving[total - 1]
            current[total] = partial_sum
        counts.append(sum(current[: boundary + 1]))
        current[: boundary + 1] = [0] * (boundary + 1)
        surviving = current
    return counts


def exact_crossing_residues(maximum):
    # Store the least excess sum(a_i-1) at each inverse depth. Larger costs
    # can never reach a coefficient crossing by the final horizon.
    excess_cap = (3**maximum).bit_length() - 1 - maximum
    missing = excess_cap + 1
    minimum = bytearray([0])
    hits = bytearray([0])
    for depth in range(1, maximum + 1):
        old_modulus = len(minimum)
        modulus = 3 * old_modulus
        updated = bytearray([missing]) * modulus
        for valuation in range(1, excess_cap + 2):
            scale = 1 << valuation
            first_residue = 1 if valuation % 2 == 0 else 2
            # All legal residues are first_residue + 3i. Their inverse
            # residues advance by scale on the smaller ring.
            offset = (scale * first_residue - 1) // 3
            for index in range(old_modulus):
                residue = first_residue + 3 * index
                cost = valuation - 1 + minimum[(offset + scale * index) % old_modulus]
                if cost < updated[residue]:
                    updated[residue] = cost
        hits *= 3
        boundary = (3**depth).bit_length() - 1 - depth
        for residue, cost in enumerate(updated):
            if cost <= boundary:
                hits[residue] = 1
        minimum = updated
    return hits


def census(maximum, hits):
    # Ascending starts give first ordinary occurrence. All old forward suffixes
    # have already been explored. End at a known path to 1 in this finite run.
    seen = {1}
    smaller = 0
    differing = 0
    for start in range(1, maximum + 1, 2):
        has_smaller = start != 1 and start in seen
        smaller += has_smaller
        finite_hit = bool(hits[start % len(hits)])
        assert not finite_hit or has_smaller
        differing += has_smaller and not finite_hit
        path = set()
        current = start
        while current not in seen:
            assert current not in path
            path.add(current)
            following = 3 * current + 1
            current = following // (following & -following)
        seen.update(path)
    return smaller, differing


def main():
    depth = 512
    counts = first_crossing_counts(depth)
    total = sum((Fraction(count, 3**j) for j, count in enumerate(counts, 1)), Fraction())
    assert total < Fraction(517161, 10**6)
    ratio = Fraction(97, 100)
    assert 3**8 < (6 * ratio) ** 5
    beyond = ratio ** (depth + 1) / (1 - ratio)
    assert total + beyond < Fraction(517167, 10**6)
    print("Certified union bound through infinity: below 517167/1000000.")

    split = [Fraction(2, 3), Fraction(7, 10), Fraction(3, 4), Fraction(1)]
    for left, right in zip(split, split[1:]):
        threshold_counts = first_crossing_counts(depth, right)
        raw_upper = sum(
            (Fraction(count, 3**j) for j, count in enumerate(threshold_counts, 1)),
            beyond,
        )
        assert raw_upper <= Fraction(467, 500) * left**2
    print("All ratio thresholds: Haar crossing mass <= (467/500) theta^2.")

    prefix_depth = 12
    hits = exact_crossing_residues(prefix_depth)
    lower = Fraction(sum(hits), len(hits))
    rest = sum((Fraction(counts[j - 1], 3**j) for j in range(prefix_depth + 1, depth + 1)), Fraction())
    upper = lower + rest + beyond
    print("First-cross union at depth 12:", sum(hits), "/", len(hits))
    # Bound the limiting no-smaller density using directed rational rounding.
    lo = (1 - upper) * 10**6
    hi = (1 - lower) * 10**6
    print("Odd-root density lies in [%d,%d]/1000000." % (lo.numerator // lo.denominator, -(-hi.numerator // hi.denominator)))
    print("Among 50000 odd starts <=100000, smaller predecessor / beyond depth-12 screen:", census(100000, hits))


if __name__ == "__main__":
    main()
