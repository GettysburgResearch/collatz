#!/usr/bin/env python3
"""Exact finite certificate for the four-A, 88-clock paired router.

No random sampling or floating point arithmetic is used. The claim is
coverage of a finite residue space, not fixed-target central pressure.
"""

from collections import Counter
import argparse
import hashlib
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def shortcut(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def compositions(total):
    for a in range(6, total - 17):
        for b in range(6, total - a - 11):
            for c in range(6, total - a - b - 5):
                yield (a, b, c, total - a - b - c)


def carry_of_word(word):
    carry, grade = 0, 0
    for clock, bit in enumerate(word):
        if bit == "1":
            carry = 3 * carry + 2**clock
            grade += 1
    return carry, grade


def build(total, verify_word):
    modulus = 3**8
    fine = 3 * modulus
    by_class = {}
    seen_carries = set()
    words = 0
    for exponents in compositions(total):
        a, b, c, d = exponents
        require(min(exponents) >= 6 and sum(exponents) == total, "composition")
        carry = 7 * (9**3 + 9**2 * 2**a + 9 * 2**(a+b) + 2**(a+b+c))
        if verify_word:
            word = "".join("101000" + "0" * (e-6) for e in exponents)
            require(carry_of_word(word) == (carry, 8), "independent parity carry")
            require(len(word) == total, "clock")
        require(carry not in seen_carries, "fixed-clock carry injectivity")
        seen_carries.add(carry)
        require(55 * carry <= 7 * 2**total, "real offset cap 7/55")
        residue = carry % modulus
        lift = (carry % fine) // modulus
        require(residue % 3 != 0, "carry unit")
        by_class.setdefault(residue, {}).setdefault(lift, (exponents, carry))
        words += 1
    return by_class, words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    h, p = 88, 8
    m, fine = 3**p, 3**(p+1)
    bank, words = build(h, True)
    units = [a for a in range(m) if a % 3]
    require(len(units) == 4374, "unit count")
    require(all(len(bank.get(a, {})) >= 2 for a in units), "two lifts per coarse carry")
    lift_histogram = dict(sorted(Counter(len(bank[a]) for a in units).items()))

    selections = []
    paths = 0
    for r in range(fine):
        if r % 3 == 0:
            continue
        target_residue = (2**h * r) % fine
        candidates = bank[target_residue % m]
        exponents, carry = next(value for lift, value in sorted(candidates.items())
                                if value[1] % fine != target_residue)
        require((target_residue - carry) % m == 0, "coarse inverse divisibility")
        require((target_residue - carry) % fine != 0, "unit inverse exclusion")
        q = r if r % 2 else r + fine
        x = (2**h * q - carry) // m
        require(m*x + carry == 2**h*q, "whole inverse equation")
        require(x > 0 and x % 2 == 1 and x % 3 != 0, "positive odd unit source")
        left, right = x, 5*x
        odd_left = odd_right = 0
        for length in exponents:
            first_return = None
            block_left = block_right = 0
            require(left % 2 == 1 and right == 5*left, "marked block entry")
            for clock in range(1, length+1):
                bl, br = left % 2, right % 2
                block_left += bl
                block_right += br
                odd_left += bl
                odd_right += br
                left, right = shortcut(left), shortcut(right)
                require(left > 0 and right > 0, "positive physical path")
                if first_return is None and block_left == block_right and right == 5*left:
                    first_return = clock
            require(first_return == 6, "first positive joint root")
            require(block_left == block_right == 2 and left % 2 == 1, "block count and sentinel")
        require((left, right, odd_left, odd_right) == (q, 5*q, p, p), "literal paired landing")
        selections.append([r, list(exponents), str(carry)])
        paths += 2

    smaller, smaller_words = build(87, False)
    missing = [a for a in units if len(smaller.get(a, {})) < 2]
    require(missing == [1732], "87-clock negative control")
    canonical = json.dumps(selections, separators=(",", ":")).encode()
    result = {
        "scope": "Complete finite residue certificate for four padded A blocks; no central-row or Collatz proof",
        "clock": h, "odd_count": p, "blocks": 4,
        "compositions": words, "coarse_modulus": m, "fine_modulus": fine,
        "coarse_unit_classes": len(units), "fine_unit_classes": len(selections),
        "fine_lift_count_histogram": lift_histogram,
        "literal_arm_paths": paths, "literal_shortcut_steps": paths*h,
        "selector_sha256": hashlib.sha256(canonical).hexdigest(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "negative_control": {"clock": 87, "compositions": smaller_words,
                             "coarse_carry_classes_missing_two_lifts": missing},
    }
    rendered = json.dumps(result, indent=2) + "\n"
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
