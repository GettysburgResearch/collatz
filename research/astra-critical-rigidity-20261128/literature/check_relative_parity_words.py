"""Exact finite conditional and product-law checks on unaligned integer intervals."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path


def require(condition, explanation):
    if not condition:
        raise ArithmeticError(explanation)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


@lru_cache(maxsize=None)
def terminal(n):
    # Actual first native entrance into the fixed finite set [1,23].
    for _ in range(1000):
        if n <= 23:
            return n
        n = step(n)
    raise ArithmeticError("finite terminal fixture did not enter the set")


def word(n, t):
    bits = []
    for _ in range(t):
        bits.append(n % 2)
        n = step(n)
    return tuple(bits)


def total_variation(left, right):
    left_mass = sum(left.values())
    right_mass = sum(right.values())
    return sum(abs(Fraction(left[x], left_mass) - Fraction(right[x], right_mass))
               for x in set(left) | set(right)) / 2


def fixture(start, length, t):
    size = 2**t
    residues = tuple(range(size))
    table = [word(r, t) for r in residues]
    require(len(set(table)) == size, "word permutation")
    lo = (start + size - 1) // size
    hi = (start + length) // size
    require(hi > lo, "complete integer blocks exist")
    starts = range(start, start + length)
    for n in starts:
        require(table[n % size] == word(n, t), "true native word")
    full_law = Counter(terminal(n) for n in starts)
    trimmed = Counter(terminal(n) for n in range(lo * size, hi * size))
    total_disagreement = 0
    joint = Counter()
    for m in range(lo, hi):
        block = [terminal(m * size + r) for r in residues]
        hist = Counter(block)
        for r, label in enumerate(block):
            joint[table[r], label] += 1
            total_disagreement += size - hist[label]
    product = Counter({(v, z): count for v in table for z, count in trimmed.items()})
    joint_distance = total_variation(joint, product)
    require(joint_distance <= Fraction(total_disagreement, (hi - lo) * size**2),
            "whole-word product coupling")
    selected = ({0}, {size - 1}, set(residues), {r for r in residues if sum(table[r]) == t // 2},
                {r for r in residues if table[r][0] and table[r][-1]})
    tests = []
    for family in selected:
        seen = Counter(terminal(n) for n in starts if n % size in family)
        count = sum(seen.values())
        require(abs(count * size - length * len(family)) <= 2 * size * len(family),
                "relative word mass in two partial blocks")
        one = Counter()
        other = Counter()
        disagreement = 0
        for m in range(lo, hi):
            block = [terminal(m * size + r) for r in residues]
            hist = Counter(block)
            for r in family:
                one[block[r]] += 1
                other.update(hist)
                disagreement += size - hist[block[r]]
        require(other == Counter({z: len(family) * freq for z, freq in trimmed.items()}),
                "conditional resampling preserves the other label")
        require(total_variation(one, other) <= Fraction(disagreement, sum(other.values())),
                "conditional coupling bound")
        tests.append({"residues": len(family), "actual_word_count": count,
                      "label_tv_from_interval": str(total_variation(seen, full_law))})
    return {"start": start, "length": length, "word_length": t,
            "trimmed_joint_tv": str(joint_distance), "word_families": tests}


if __name__ == "__main__":
    note = Path(__file__).with_name("RELATIVE_PARITY_WORD_EQUIPARTITION.md")
    print(json.dumps({"source_sha256": sha256(note.read_bytes()).hexdigest(),
                      "finite_intervals": [fixture(*case) for case in
                                           ((1, 95, 3), (417, 771, 4), (17003, 1053, 5),
                                            (518713, 2319, 6))],
                      "scope": "exact counts, empirical baselines and coupling inequalities only"},
                     sort_keys=True, indent=2))
