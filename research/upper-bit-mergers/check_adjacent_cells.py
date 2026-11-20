"""Classify fixed native word lifts of two adjacent Collatz comparisons."""

from check import step, walk


def classify(target_scale, depth_limit):
    """Return all (scale, lower intercept) pairs, checking exhaustion."""
    target_clock = (target_scale & -target_scale).bit_length() - 1
    targets = {}
    for base in (1, 2):
        endpoint, odds = walk(base, target_clock)
        targets[endpoint] = (target_scale >> target_clock) * 3**odds
    assert targets[2] == 3 * targets[1]
    max_odds = 0
    power = targets[2]
    while power % 3 == 0:
        max_odds += 1
        power //= 3
    # A state records the canonical residue, both endpoints, and odd counts.
    active = [(0, 0, 1, 0, 0)]
    matches = set()
    visited = 0
    for clock in range(depth_limit):
        next_active = []
        for residue, left, right, left_odds, right_odds in active:
            visited += 1
            if {left, right} == {1, 2}:
                slope_numerator = targets[left] << clock
                scale, remainder = divmod(slope_numerator, 3**left_odds)
                if remainder == 0 and scale * 3**right_odds == targets[right] << clock:
                    matches.add((scale, residue))
            for bit in (0, 1):
                x = left + bit * 3**left_odds
                y = right + bit * 3**right_odds
                p = left_odds + x % 2
                q = right_odds + y % 2
                x, y = step(x), step(y)
                if max(p, q) > max_odds or (p == q and x == y):
                    continue
                next_active.append((residue + (bit << clock), x, y, p, q))
        active = next_active
    if active:
        raise AssertionError("The claimed depth leaves unchecked prefixes")
    return visited, matches


if __name__ == "__main__":
    for scale, depth, nodes, count, optimum, residues in (
        (54, 16, 333, 13, 1024, {16, 21, 23}),
        (3456, 35, 34146, 60, 2**23, {6464}),
    ):
        visited, matches = classify(scale, depth)
        highest = max(coefficient for coefficient, _ in matches)
        winners = {residue for coefficient, residue in matches if coefficient == highest}
        if (visited, len(matches), highest, winners) != (nodes, count, optimum, residues):
            raise AssertionError((scale, visited, len(matches), highest, winners))
        print(f"Target scale {scale}: {visited} prefixes, {len(matches)} certificates, "
              f"largest scale {highest}, lower intercepts {sorted(winners)}")
