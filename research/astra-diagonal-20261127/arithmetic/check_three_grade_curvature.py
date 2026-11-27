"""Finite induction on the correctly ordered high-rank return calendar."""

from fractions import Fraction
from functools import cache
from itertools import product
import json


# (second difference, first residue modulo four, middle residue modulo four)
EXCEPTIONS = frozenset({
    (1, 1, 1), (1, 2, 1), (2, 2, 1),
    (3, 1, 2), (3, 2, 2), (4, 2, 2),
})
HIGH_CAP = 128


def phi(n):
    return (3 * n + (n & -n)) // 2


def high_return(n, kind):
    lowbit = n & -n
    if lowbit not in (1, 2):
        return None
    if kind == "S":
        numerator = 3 * n + lowbit
        if numerator % 4:
            return None
        out = numerator // 4
        if (out & -out) not in (lowbit, lowbit // 2):
            return None
        return out
    assert kind == "D"
    middle = phi(n)
    middle_lowbit = middle & -middle
    if middle_lowbit not in (lowbit, 2 * lowbit):
        return None
    numerator = 3 * middle + middle_lowbit
    if numerator % 4:
        return None
    out = numerator // 4
    last_lowbit = out & -out
    if last_lowbit not in (1, 2) or 2 * last_lowbit not in (
        middle_lowbit, 2 * middle_lowbit
    ):
        return None
    return out


def curvature(values):
    return values[0] - 2 * values[1] + values[2]


@cache
def transitions(state, column_words):
    h, first, middle = state
    # Endpoint slope denominators are 4, 8, and 32 respectively.
    endpoint_denominator = {"S": 4, "D": 8, "DS": 32, "SD": 32}[column_words[0]]
    modulus = 4 * endpoint_denominator
    outputs = set()
    for i, j in product(range(0, modulus, 4), repeat=2):
        x = 4096 + first + i
        y = 4096 + middle + j
        inputs = (x, y, 2*y-x+h)
        assert min(inputs) > 0
        row_ends = []
        unwrapped_middle = []
        for initial, word in zip(inputs, column_words):
            current = initial
            for k, letter in enumerate(word):
                current = high_return(current, letter)
                if current is None:
                    break
                if len(word) == 2 and k == 0:
                    # The SD side crosses the high interval's upper seam.
                    unwrapped_middle.append(phi(current) if letter == "S" else current)
            if current is None:
                break
            row_ends.append(current)
        if len(row_ends) != 3:
            continue
        mid_h = curvature(unwrapped_middle) if unwrapped_middle else None
        outputs.add((curvature(row_ends), row_ends[0] % 4, row_ends[1] % 4, mid_h))
    return frozenset(outputs)


def protected(state):
    return state[0] > 0 and state not in EXCEPTIONS


def propagate(states, columns):
    targets = set()
    for state in states:
        for h, x, y, mid_h in transitions(state, columns):
            assert h > 0 and (mid_h is None or mid_h > 0), (state, columns, h, mid_h)
            targets.add((h, x, y))
    return targets


def verify_block(block):
    initial_count = 0
    all_states = set()
    for h in range(1, HIGH_CAP):
        for x, y in product((1, 2, 3), repeat=2):
            if (2*y-x+h) % 4 == 0 or not protected((h, x, y)):
                continue
            initial_count += 1
            all_states.add((h, x, y))
    step_sizes = []
    for columns in block:
        all_states = propagate(all_states, columns)
        step_sizes.append(len(all_states))
    assert all(map(protected, all_states))
    return dict(initial=initial_count, step_sizes=step_sizes)


def main():
    # Each ordinary/composite transition and composite middle has
    # H_out >= 3*H_in/4 - 4 while H_in >= 0.
    lower = Fraction(HIGH_CAP)
    lower_bounds = []
    for _ in range(6):
        lower = 3*lower/4 - 4
        lower_bounds.append(str(lower))
        assert lower > 4
    S, D = ("S",) * 3, ("D",) * 3
    left = ("DS", "DS", "SD")
    right = ("DS", "SD", "SD")
    blocks = {
        "ordinary_SDD": (S,D,D),
        "ordinary_SDDD": (S,D,D,D),
        "left_seam": (S,D,D,left,D,D),
        "right_seam": (S,D,D,right,D,D),
    }
    # The bound for both composite carries uses only the exact finite
    # sets of single-column three-ordinary-step carries.
    carries = {}
    for word in ("DS", "SD"):
        c = set()
        for n in range(128, 256):
            m = high_return(n, word[0])
            if m is not None:
                out = high_return(m, word[1])
                if out is not None:
                    c.add(32*out-27*n)
        carries[word] = sorted(c)
    assert carries["DS"] == [23,29,37,38,46,58]
    assert carries["SD"] == [29,37,38,46,58,74]
    print(json.dumps(dict(
        exceptions=sorted(EXCEPTIONS),
        cap=HIGH_CAP,
        scalar_lower_bounds=lower_bounds,
        seam_carries=carries,
        blocks={name: verify_block(block) for name, block in blocks.items()},
    ), indent=2))


if __name__ == "__main__":
    main()
