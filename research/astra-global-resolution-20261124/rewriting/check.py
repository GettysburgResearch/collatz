"""Replay the directed single-return certificate on whole affine progressions."""

import json
import math
import re
from collections import Counter
from fractions import Fraction
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_rows(source):
    route = source.split("private def route : Nat → Nat → String\n", 1)[1]
    route = route.split("\nprivate def dropRow", 1)[0]
    rows = {}
    modulus = None
    for line in route.splitlines():
        if not line.strip() or line.strip() == '| _, _ => ""':
            continue
        if line.strip() == '| _ => ""':
            modulus = None
            continue
        group = re.fullmatch(r"  \| ([0-9]+), b => match b with", line)
        if group:
            require(modulus is None, "unterminated modulus group")
            modulus = int(group[1])
            continue
        leaf = re.fullmatch(r'    \| ([0-9]+) => "([DhitS]+)"', line)
        require(modulus is not None and leaf is not None, f"unrecognized row {line!r}")
        base = int(leaf[1])
        row = (modulus, base)
        require(2 <= base <= modulus + 1, f"{row} skips its first positive input above 1")
        require(row not in rows, f"duplicate leaf {row}")
        rows[row] = leaf[2]
    require(modulus is None and rows, "incomplete certificate")
    return rows


def apply_letter(letter, slope, base, location):
    # Work with the integer numerator and denominator of each actual move.
    # In addition to integral outputs, enforce the forward or inverse source domain.
    rules = {
        "h": (2, 0, 1, 0, 2),
        "D": (1, 0, 2, 0, 1),
        "t": (2, 1, 3, 1, 2),
        "i": (3, 2, 2, -1, 3),
        "S": (8, 7, 9, 1, 8),
    }
    domain, residue, multiplier, offset, divisor = rules[letter]
    require(slope % domain == 0 and base % domain == residue, f"source domain at {location}")
    a, ar = divmod(multiplier * slope, divisor)
    b, br = divmod(multiplier * base + offset, divisor)
    require(ar == br == 0 and a > 0 and b > 0, f"nonintegral or nonpositive at {location}")
    return a, b


def replay(rows):
    period = math.lcm(*(modulus for modulus, _ in rows))
    cover = bytearray(period)
    terminal = Fraction(0)
    jump = Fraction(0)
    jump_witness = None
    above_source = 0
    jumps = 0
    letters = Counter()
    level_counts = Counter()
    for (modulus, base), word in rows.items():
        start = base % modulus
        require(not any(cover[start::modulus]), f"overlapping class {(modulus, base)}")
        cover[start::modulus] = b"\x01" * (period // modulus)
        level_counts[modulus] += 1
        a, b = modulus, base
        leaf_jump = Fraction(0)
        for position, letter in enumerate(word, 1):
            letters[letter] += 1
            if letter == "S":
                jumps += 1
                for limit, ratio in (("base", Fraction(b, base)), ("infinity", Fraction(a, modulus))):
                    leaf_jump = max(leaf_jump, ratio)
                    if ratio > jump:
                        jump = ratio
                        jump_witness = {
                            "modulus": modulus,
                            "base": base,
                            "letter": position,
                            "ratio_at": limit,
                            "jump_slope": a,
                            "jump_base": b,
                        }
            a, b = apply_letter(letter, a, b, (modulus, base, position))
        above_source += int(leaf_jump > 1)
        require(a <= modulus and 0 < b < base, f"failed strict descent for {(modulus, base)}")
        terminal = max(terminal, Fraction(a, modulus), Fraction(b, base))
    require(all(cover), "uncovered residue")
    require(len(rows) == 291 and sum(letters.values()) == 3483, "unexpected certificate size")
    require(terminal == Fraction(118, 123), "terminal height bound changed")
    require(jump == Fraction(20970919, 122875), "maximum jump input changed")
    return {
        "complete_residue_period": period,
        "leaves": len(rows),
        "leaves_by_modulus": dict(sorted(level_counts.items())),
        "distinct_words": len(set(rows.values())),
        "longest_word": max(map(len, rows.values())),
        "total_letters": sum(letters.values()),
        "letters": dict(sorted(letters.items())),
        "total_quotient_jumps": jumps,
        "leaves_with_jump_above_source": above_source,
        "largest_terminal_ratio": str(terminal),
        "largest_quotient_jump_source_ratio": str(jump),
        "largest_quotient_jump_source_witness": jump_witness,
    }


if __name__ == "__main__":
    source = Path(__file__).with_name("SingleReturn.lean").read_text(encoding="utf-8")
    print(json.dumps(replay(read_rows(source)), sort_keys=True, indent=2))
