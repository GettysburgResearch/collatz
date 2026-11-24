"""Exact first-crossing carry envelope and a short independent word enumeration."""

from argparse import ArgumentParser


def envelope(max_odds):
    ternary = 1
    carry = 0
    maximum = 0
    maximizing_odds = 0
    maximizing_length = 1
    small = {0: 0}
    for odd_count in range(1, max_odds + 1):
        # ternary = 3^(odd_count-1) before the update.
        largest_next_position = ternary.bit_length() - 1
        carry = 3 * carry + (1 << largest_next_position)
        ternary *= 3
        length = ternary.bit_length()
        denominator = (1 << length) - ternary
        floor_center = carry // denominator
        if floor_center > maximum:
            maximum = floor_center
            maximizing_odds = odd_count
            maximizing_length = length
        if length <= 18:
            small[odd_count] = carry
    return maximum, maximizing_odds, maximizing_length, small


def direct_small(max_length=18):
    """Grow every prefix to its first strict crossing or the finite horizon."""
    stack = [(0, 0, 1, 0)]
    maxima = {}
    count = 0
    while stack:
        length, odds, ternary, carry = stack.pop()
        if ternary < (1 << length):
            maxima[odds] = max(carry, maxima.get(odds, 0))
            count += 1
        elif length < max_length:
            stack.append((length + 1, odds, ternary, carry))
            stack.append((length + 1, odds + 1, 3 * ternary, 3 * carry + (1 << length)))
    return maxima, count


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--max-odds', type=int, default=47_467)
    args = parser.parse_args()
    if args.max_odds < 0:
        parser.error('--max-odds must be nonnegative')
    maximum, odds, length, small = envelope(args.max_odds)
    maxima, count = direct_small()
    if small != {k: v for k, v in maxima.items() if k <= args.max_odds}:
        raise ArithmeticError('disagreement with independent short-word enumeration')
    next_length = (3 ** (args.max_odds + 1)).bit_length()
    print(f'first-crossing upper weight {args.max_odds}')
    print(f'maximum floor center {maximum} first attained at weight {odds}, length {length}')
    print(f'length at next weight {next_length}')
    print(f'independently enumerated {count} first crossings through length 18')


if __name__ == '__main__':
    main()
