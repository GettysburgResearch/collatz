"""Replay exact finite source-shell identities on literal positive integer paths."""

from fractions import Fraction
from itertools import combinations
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def odd_step(n):
    numerator = 3 * n + 1
    exponent = (numerator & -numerator).bit_length() - 1
    return exponent, numerator >> exponent


def compositions(total, parts):
    if total < parts:
        return
    for cuts in combinations(range(1, total), parts - 1):
        bounds = (0, *cuts, total)
        yield [y - x for x, y in zip(bounds, bounds[1:])]


def residue_ledger():
    """Count literal offset classes for all compositions at small central clocks."""
    ledger = []
    for n in range(2, 9):
        s = 2 * n
        words = tuple(compositions(s, n))
        for k in (1, 2):
            modulus = 3 ** (n + k)
            inverse = pow(2**s, -1, modulus)
            offsets = set()
            for word in words:
                numerator, clock = 0, 0
                for e in word:
                    numerator = 3 * numerator + 2**clock
                    clock += e
                offsets.add(numerator * inverse % modulus)
            require(len(offsets) <= len(words), "offset class count exceeds word count")
            require(all(r % 3 for r in offsets), "nonunit ternary offset residue")
            ledger.append(dict(depth=n, extra=k, words=len(words), offset_classes=len(offsets),
                               unit_classes=2 * modulus // 3))
    return ledger


def run():
    shell_count = 0
    simple_count = 0
    min_center_ratio = Fraction(1)
    max_center_ratio = Fraction(0)
    for a in range(5, 102, 2):
        if a % 3 == 0:
            continue
        qi, clock = a, 0
        visited = {a}
        for i in range(1, 5):
            ei, qi = odd_step(qi)
            clock += ei
            if qi in visited:
                break
            visited.add(qi)
            for e in range(2, 10):
                numerator = 2**e * a - 1
                if numerator % 3 or (t := numerator // 3) % 3 == 0:
                    continue
                require(odd_step(t) == (e, a), "inverse gap does not land at the gate")
                for n in range(1, 5):
                    b = n + i + 1
                    s = 2 * b - clock - e
                    if s < n:
                        continue
                    scale = Fraction(3**n, 2**s)
                    center = Fraction(a * 2**e, 3 * scale)
                    require(center == a * Fraction(3**i, 2**clock) * Fraction(4, 3) ** b,
                            "inconsistent source interval center")
                    for letters in compositions(s, n):
                        x = t
                        states = [t]
                        for v in letters:
                            value = 2**v * x - 1
                            if value % 3:
                                break
                            x = value // 3
                            if x % 3 == 0:
                                break
                            states.append(x)
                        else:
                            beta = t - scale * x
                            require(beta >= 0, "negative affine prefix offset")
                            require(1 - Fraction(x, center) == (1 + 3 * beta) / (2**e * a),
                                    "source interval identity failed")
                            min_center_ratio = min(min_center_ratio, Fraction(x, center))
                            max_center_ratio = max(max_center_ratio, Fraction(x, center))
                            shell_count += 1
                            if len(set(states) | visited) == b + 1:
                                require(1 - Fraction(x, qi) / Fraction(4, 3) ** b >= Fraction(1, 3 * a + 1),
                                        "simple path falls below the required relative carry")
                                simple_count += 1
    require(simple_count > 0, "no simple high-carry path was checked")
    return dict(residue_ledger=residue_ledger(), shell_identities=shell_count, simple_high_carry_paths=simple_count,
                minimum_source_to_center=str(min_center_ratio),
                maximum_source_to_center=str(max_center_ratio))


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
