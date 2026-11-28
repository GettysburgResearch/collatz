"""Replay native clocks without using reach-one information."""

def require(test, message):
    if not test:
        raise AssertionError(message)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def trace(x, initial_level, horizon):
    lower, upper = x, 3**initial_level * x
    lower_count = upper_count = upper_carry = 0
    first_tie = first_overtake = first_merge = None
    first_tie_count = None
    for t in range(horizon + 1):
        level = initial_level + upper_count - lower_count
        if level < 0 and first_overtake is None:
            first_overtake = t
        if t and first_overtake is None:
            require(upper < 3**level * lower, (x, initial_level, t, "strict order"))
        if level == 0 and first_tie is None:
            first_tie = (t, lower, upper)
            gap = lower - upper
            # Twice the native gap exceeds four times the upper affine offset.
            require((2 * gap - 1) * 2**t >= 4 * upper_carry,
                    (x, initial_level, t, "first-tie carry"))
            first_tie_count = lower_count
        if level == 0 and lower == upper:
            require(first_overtake is not None, (x, initial_level, t, "overtake"))
            suffix_length = t - first_tie[0]
            suffix_odds = lower_count - first_tie_count
            suffix_evens = suffix_length - suffix_odds
            gap = first_tie[1] - first_tie[2]
            require(3**suffix_odds * gap <= (2**suffix_evens - 1) *
                    (3**suffix_odds - 2**suffix_odds),
                    (x, initial_level, t, "post-tie carry range"))
            first_merge = (t, lower)
            break
        low_bit, high_bit = lower % 2, upper % 2
        upper_carry = 3**high_bit * upper_carry + high_bit * 2**t
        lower_count += low_bit
        upper_count += high_bit
        lower, upper = step(lower), step(upper)
    return first_tie, first_overtake, first_merge


def main():
    sample = trace(545, 1, 20)
    require(sample == ((5, 461, 460), 6, (8, 173)), sample)
    print("Canonical example (first equal grade, first overtake, counted merger):", sample)
    for s in range(1, 5):
        ties = overtakes = mergers = 0
        for x in range(1, 8192, 2):
            tie, overtake, merge = trace(x, s, 192)
            ties += tie is not None
            overtakes += overtake is not None
            mergers += merge is not None
        print(f"s={s}, 4096 odd starts, 192 clocks: "
              f"{ties} first ties, {overtakes} overtakes, {mergers} counted mergers")


if __name__ == "__main__":
    main()
