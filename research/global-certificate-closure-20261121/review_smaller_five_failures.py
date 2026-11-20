#!/usr/bin/env python3
"""Independent binary-cylinder and finite-base replay of SMALLER_FIVE_FAILURES.

No functions are imported from the author's checker. Universal short-word
legality is checked on the full binary cylinder needed by each word.
"""

from fractions import Fraction
from pathlib import Path
import hashlib
import json


HERE = Path(__file__).resolve().parent
SOURCE = (HERE if (HERE / "SMALLER_FIVE_FAILURES.md").exists()
          else HERE.parent / "agent_global_reverse_20261121")
H = 176106


def need(ok, why):
    if not ok:
        raise ValueError(why)


def step(n):
    need(n > 0, "nonpositive ordinary state")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def valuation(n):
    need(n > 0, "nonpositive valuation argument")
    return (n & -n).bit_length() - 1


def whole_cylinder_word(start_slope, start_offset, word, endpoint):
    """All actual integral starts alpha*2^e+beta, e>=119, share these bits."""
    clock = sum(word)
    modulus = 2 ** (clock + 1)
    alpha, beta = Fraction(start_slope), Fraction(start_offset)
    need(alpha.denominator % 2 and beta.denominator % 2, "even start denominator")
    need(119 >= clock + 1, "binary cylinder not uniform on exponent family")
    test = (beta.numerator * pow(beta.denominator, -1, modulus)) % modulus
    test += modulus
    for letter in word:
        need(valuation(3 * test + 1) == letter, "wrong exact cylinder exponent")
        test = (3 * test + 1) >> letter
        alpha, beta = 3 * alpha / 2 ** letter, (3 * beta + 1) / 2 ** letter
    need((alpha, beta) == endpoint, "wrong affine endpoint")


def cycle(offset, clock, parities, multiplier):
    offset = Fraction(offset)
    modulus = 2 ** clock
    start = offset.numerator * pow(offset.denominator, -1, modulus) % modulus
    start += modulus
    alpha, beta = Fraction(1), Fraction(0)
    seen = []
    for _ in range(clock):
        odd = start % 2
        seen.append(odd)
        if odd:
            alpha, beta = 3 * alpha / 2, (3 * beta + 1) / 2
        else:
            alpha, beta = alpha / 2, beta / 2
        start = step(start)
    need(seen == parities, "wrong cycle cylinder parities")
    need(alpha == multiplier and alpha * offset + beta == offset,
         "rational offset is not fixed by the declared affine cycle")


def upper(exponent):
    numerator = 1024 * 2 ** exponent - 2573
    need(numerator % 243 == 0, "upper family is not integral")
    return numerator // 243


def main():
    whole_cylinder_word(Fraction(32, 135), Fraction(-61, 135),
                        [4, 1, 2, 1, 1, 2, 1], (Fraction(81, 640), Fraction(19, 5)))
    whole_cylinder_word(Fraction(128, 405), Fraction(-271, 405),
                        [3, 2, 1, 4], (Fraction(1, 40), Fraction(1, 5)))
    whole_cylinder_word(Fraction(32, 27), Fraction(-61, 27),
                        [2, 1, 2], (Fraction(1), Fraction(-1)))
    whole_cylinder_word(Fraction(128, 81), Fraction(-271, 81),
                        [2, 2, 1, 2], (Fraction(1), Fraction(-1)))
    cycle(Fraction(1, 5), 3, [1, 0, 0], Fraction(3, 8))
    cycle(Fraction(19, 5), 5, [1, 1, 1, 0, 0], Fraction(27, 32))
    need(pow(2, 119, 243) * 4 % 243 == 11, "wrong base ternary residue")
    need(pow(2, 162, 243) == 1, "ternary progression does not persist")
    need(pow(2, 119, 5) == 3 and pow(2, 281, 5) == 2,
         "wrong mod-five phase selection")
    need(pow(2, 324, 5) == 1, "mod-five phases do not persist")
    need(H * (3 ** 59 + 1) < upper(119), "successor-five base failed")
    need(H * 3 ** 92 < upper(281), "fast source base failed")
    need(H ** 5 * 3 ** 1329 < upper(443) ** 5, "slow source base failed")
    need(20 ** 5 * 32 ** 4 < 3 ** 33, "slow residual bound failed")
    need(3 ** 81 < 2 ** 162 and 3 ** 108 < 2 ** 324
         and 3 ** 972 < 2 ** 1620, "induction growth inequality failed")
    certificate = json.loads((SOURCE / "base_119_ordinary_prefix.json").read_text())
    values = certificate["ordinary_values"]
    need(len(values) == 137, "base evidence has wrong length")
    q = (32 * 2 ** 119 - 61) // 135
    need(values[0] == q == certificate["five_source"], "base evidence starts elsewhere")
    need(all(step(x) == y for x, y in zip(values, values[1:])),
         "base evidence contains a false ordinary transition")
    need(values[-1] == certificate["endpoint"] == 9900175581272098130203189984031,
         "base evidence has wrong endpoint")
    need(H * values[-1] < upper(119), "base evidence does not enter same initial interval")
    need(Fraction(10126085, 23) / 13 == Fraction(10126085, 299) > 1,
         "joint cost comparison changed")
    files = ("SMALLER_FIVE_FAILURES.md", "check_smaller_five_failures.py",
             "base_119_ordinary_prefix.json")
    print(json.dumps({
        "status": "PASS",
        "scope": "SF1-SF4, exact paths/guards/bases; H2 imported at its stated pin; no full Collatz proof",
        "independent_binary_cylinder_prefixes": 4,
        "independent_rational_cycles": 2,
        "stored_base_transitions_verified": len(values) - 1,
        "input_sha256": {name: hashlib.sha256((SOURCE / name).read_bytes()).hexdigest()
                         for name in files},
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
