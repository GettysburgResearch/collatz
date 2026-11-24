"""Finite parts of the all-buffer, all-paid-run reset classification."""
from fractions import Fraction


def demand(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def clocks(word: str) -> tuple[int, int, int]:
    length = odds = carry = 0
    for symbol in word:
        width, offset = {"L": (3, 7), "P": (5, 5)}[symbol]
        carry = 9 * carry + (1 << length) * offset
        length += width
        odds += 2
    return length, odds, carry


def reset_word(multiplier: Fraction, source: str) -> str | None:
    length, odds, carry = clocks(source)
    correction = multiplier * (carry - 7 * 3**odds + 7 * 2**length) + 7 * (3**odds - 2**length)
    if correction.denominator != 1:
        return None
    modulus = 2**length
    start = -int(correction) * pow(3**odds, -1, modulus) % modulus
    value = start
    parity = []
    for _ in range(length):
        parity.append(value % 2)
        value = (3 * value + 1) // 2 if value % 2 else value // 2
    if sum(parity) == odds and value * modulus == 3**odds * start + correction:
        return "".join(map(str, parity))
    return None


def signed_orbit(start: Fraction) -> tuple[int, list[Fraction]]:
    seq = []
    seen = {}
    value = start
    while value not in seen:
        demand(value.denominator % 2 == 1, "formal starting point must be 2-integral")
        seen[value] = len(seq)
        seq.append(value)
        value = (3 * value + 1) / 2 if value.numerator % 2 else value / 2
    return seen[value], seq[seen[value]:]


def verify_controller(numerator: int, d: int, expected: tuple[int, int]) -> None:
    multiplier = Fraction(numerator, 2**d)
    k = (d + 1) // 3
    h = d - 1
    anchor = multiplier * Fraction(166, 23)
    initial = anchor * Fraction(8, 9)**k - 7
    terminal = anchor - 7
    target = 2**h * 23 * terminal
    demand(target.denominator == 1, "terminal clearing")
    preperiod, cycle = signed_orbit(initial)
    demand((preperiod, len(cycle)) == expected, "wrong cycle")
    demand(3*k + 15 - h >= preperiod, "insufficient forced clocks at s=3")
    for point in cycle:
        scaled = 23 * point
        demand(scaled.denominator == 1, "cycle denominator")
        possible = {int(scaled)}
        for j in range(h):
            possible |= {3 * value + 23 * 2**j for value in possible}
        demand(target not in possible, "formal suffix reached the designated terminal")
    for s in (1, 2):
        demand(reset_word(multiplier, "L"*k + "P"*s) is not None, "positive exception")
    for gap in range(k):
        word = "L"*k + "P" + "L"*gap + "P"
        demand((reset_word(multiplier, word) is not None) == (gap != 3), "isolated pair gap")
    print(f"M={numerator} k={k} h={h} preperiod={preperiod} period={len(cycle)} "
          f"first_cycle={cycle[0]} terminal_numerator={target}")


if __name__ == "__main__":
    verify_controller(5583, 12, (12, 43))
    verify_controller(72873, 16, (14, 5))
