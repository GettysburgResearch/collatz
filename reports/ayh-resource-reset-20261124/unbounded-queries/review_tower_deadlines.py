"""Independent ordinary affine checks of the first asynchronous tower deadline."""


def word(initial, horizon):
    value = initial
    count = offset = 0
    steps = []
    for clock in range(horizon + 1):
        steps.append((count, offset, value))
        parity = value % 2
        count += parity
        offset = 3**parity * offset + parity * 2**clock
        value = (3**parity * value + parity) // 2
    return steps


def review(horizon):
    period = 1 << (horizon - 2)
    left_count, _, left_terminal = word(17, horizon)[-1]
    right_count, _, right_terminal = word(51, horizon)[-1]
    if left_count != right_count or (left_terminal, right_terminal) != (1, 1):
        raise ValueError("base return")

    def suffix_residue(multiplier):
        high = (pow(3, period * multiplier, 1 << (horizon + 5)) - 1) >> horizon
        return high * 17 * 3**left_count % 32

    multiplier = next(u for u in range(1, 33) if suffix_residue(u) == 5)
    rank = period * multiplier
    ceiling = horizon + 5
    representative = pow(3, rank, 1 << ceiling)
    lower = word(17 * representative, ceiling)
    upper = word(51 * representative, ceiling)
    meetings = []
    for i, (p, lower_offset, _) in enumerate(lower):
        for j, (q, upper_offset, _) in enumerate(upper):
            slope = 17 * 3**p * 2**j - 51 * 3**q * 2**i
            offset = lower_offset * 2**j - upper_offset * 2**i
            if abs(offset).bit_length() >= rank:
                raise ValueError("ordinary power separation")
            if (slope, offset) == (0, 0):
                meetings.append((i, j))
    first = min(max(i, j) for i, j in meetings)
    if first != ceiling or (ceiling, ceiling) not in meetings:
        raise ValueError("unexpected first meeting")
    return horizon, rank, first


if __name__ == "__main__":
    print([review(horizon) for horizon in range(17, 40, 2)])
