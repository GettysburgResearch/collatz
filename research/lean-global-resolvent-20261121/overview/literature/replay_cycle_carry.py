"""Independent exact replay of the cycle programs and terminal congruences.

The infinite ordinary-source realizability theorem is in Lean. The terminal
exponents below are too large to materialize 2**h; this checker therefore
checks their exact integer congruences with modular exponentiation. It does
not label these modular checks as literal positive-orbit replays.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

PIN_WORD = (1, 1, 4, 1, 1, 1, 2)


def correction(word: tuple[int, ...]) -> int:
    c, b = 0, 0
    for a in word:
        c = 3 * c + 2**b
        b += a
    return c


def compiler(word: tuple[int, ...]) -> tuple[int, int, str]:
    s, b, c = len(word) + 1, sum(word), correction(word)
    p = 3**s - 2 ** (b + 1) - 6 * c
    branches: list[str] = []
    while s or (p and p % 2 == 0):
        if p % 2:
            assert s > 0
            s -= 1
            p = (p + 3**s) // 2
            branches.append("O")
        else:
            assert p
            p //= 2
            branches.append("E")
    return len(branches), p, "".join(branches)


def signed_pin_entrance() -> str:
    n, branches = -81, []
    while n != -5:
        branches.append("O" if n % 2 else "E")
        n = (3 * n + 1) // 2 if n % 2 else n // 2
    assert len(branches) == 15 and branches.count("O") == 7
    return "".join(branches)


def terminal_exponent(s: int, c: int = 122) -> int:
    """Construct an even exponent solving 2**h == -c mod 3**s."""
    assert s >= 1 and c % 3 == 2
    h, modulus, period = 2, 3, 2
    assert (pow(2, h, modulus) + c) % modulus == 0
    for _ in range(1, s):
        modulus *= 3
        candidates = [h + j * period for j in range(3)]
        passing = [v for v in candidates if (pow(2, v, modulus) + c) % modulus == 0]
        assert len(passing) == 1
        h = passing[0]
        period *= 3
    assert (pow(2, h, 3**s) + c) % (3**s) == 0
    return h


def main() -> dict:
    entrance = signed_pin_entrance()
    checked = 0
    for d in range(129):
        word = PIN_WORD * (2 * d + 12)
        b, s = sum(word), len(word) + 1
        clock, carry, branches = compiler(word)
        assert b == 22 * d + 132 and s == 14 * d + 85
        assert clock == 21 * d + 132 and b - clock == d
        assert carry == 244 * 2**d - 5 > 0
        assert carry % 2 == 1
        assert branches == entrance + "OOE" * (7 * d + 39)
        assert correction(word) + 41 * 2**b == 41 * 3 ** (s - 1)
        checked += 1
    realizations = []
    for d in range(13):
        s, b = 14 * d + 85, 22 * d + 132
        h = terminal_exponent(s)
        assert h >= b + 3
        realizations.append({"deficit": d, "ternary_precision": s,
                             "terminal_exponent": str(h),
                             "terminal_exponent_digits": len(str(h)),
                             "terminal_grade_bound": b + 3})
    # The coefficient identity also retains arbitrary suffixes.
    tails = [(), (1,), (2,), (3,), (4,), (1, 2, 3), (4, 1, 1, 2, 2, 1, 2, 4, 4, 4)]
    prefix_checks = 0
    for k in range(20):
        for tail in tails:
            sv = len(tail) + 1
            pv = 3**sv - 2 ** (sum(tail) + 1) - 6 * correction(tail)
            coefficient = pv + 81 * 3**sv
            w = PIN_WORD * k + tail
            p = 3 ** (len(w) + 1) - 2 ** (sum(w) + 1) - 6 * correction(w)
            assert p == coefficient * 2 ** (11 * k) - 81 * 3 ** (7 * k + sv)
            prefix_checks += 1
    return {"exact_compiler_programs": checked,
            "arbitrary_suffix_affine_checks": prefix_checks,
            "integer_terminal_congruences": realizations,
            "scope": "Finite exact compiler and congruence replay. Infinite ordinary-source statements are kernel-proved in Lean."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = main()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items()
                      if key != "integer_terminal_congruences"}, indent=2))
