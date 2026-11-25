"""Reconstruct the frozen 41-gap rational control using integer arithmetic."""

from fractions import Fraction
from math import gcd


WORD = tuple(map(int, "12112212212212121212212121221221212121222"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    p, h = len(WORD), sum(WORD)
    numerator, elapsed = 0, 0
    for a in WORD:
        numerator = 3 * numerator + 2**elapsed
        elapsed += a
    denominator = 2**h - 3**p
    seed = Fraction(numerator, denominator)
    d = seed.denominator
    x = seed
    odd, physical, parity = [], [], []
    for a in WORD:
        require(x.denominator == d and x.numerator % 2 == 1, "odd phase")
        odd.append(x)
        physical.append(x)
        parity.append(1)
        x = (3 * x + 1) / 2
        for _ in range(a - 1):
            require(x.denominator == d and x.numerator % 2 == 0, "even phase")
            physical.append(x)
            parity.append(0)
            x /= 2
    require(x == seed and len(set(odd)) == p, "primitive return")
    s = min(odd)
    rows = []
    for x in odd:
        j = (x >= 2 * s) + (x >= 4 * s)
        t = 4 * d * x / 2**j
        require(s <= x / 2**j < 2 * s and t.denominator == 1, "octave")
        rows.append((int(t), 4 // 2**j))
    ordered = sorted(rows)
    z = [entry for entry, _ in ordered]
    c = [correction for _, correction in ordered]
    require(len(set(z)) == p, "distinct ordered phases")
    rank = {entry: i for i, entry in enumerate(z)}
    for i, (entry, correction) in enumerate(rows):
        r = rank[entry]
        octave, target = divmod(r + h, p)
        require((2**octave) * z[target] == 3 * entry + d * correction,
                "lifted rank recurrence")
        require(target == rank[rows[(i + 1) % p][0]], "rank shift")
    gaps = [b - a for a, b in zip(z, z[1:] + [2 * z[0]])]
    extended = c + [2 * c[0]]
    changes = [i for i in range(p) if extended[i] != extended[i + 1]]
    require(sum(gaps) == 4 * d * s, "telescoping")
    for r, gap in enumerate(gaps):
        octave, target = divmod(r + h, p)
        require((2**octave) * gaps[target]
                == 3 * gap + d * (extended[r + 1] - extended[r]),
                "gap recurrence including seam")
    # One lap tests every past length. The signed sum grows by
    # 5*p - 3*h > 0 on every extra complete lap.
    require(5 * p > 3 * h, "positive record drift")
    records = [i for i in range(h) if all(
        sum(5 * parity[(i - j) % h] - 3 for j in range(1, k + 1)) > 0
        for k in range(1, h + 1))]
    high_odd = sum(x > 2 * s for x in odd)
    high_physical = sum(x > 2 * s for x in physical)
    high_records = sum(physical[i] > 2 * s for i in records)
    B = len(changes)
    budget = [3**k * max(p - k * B, 0) for k in range((p + B - 1) // B + 1)]
    require((p, h, B, high_odd, high_physical, len(records), high_records)
            == (41, 65, 7, 7, 30, 9, 9), "control statistics")
    require(max(budget) == 1458 and max(budget) < 4 * s, "ordinary-scale inequality")
    require(gcd(numerator, denominator) == 19 and d > 1, "complete denominator")
    print(f"p={p} h={h} s={s} reduced_denominator={d} sorted_changes={B}")
    print(f"high_odd={high_odd} high_physical={high_physical} "
          f"strict_records={len(records)} high_strict_records={high_records}")
    print(f"budget_for_k_0_through_{len(budget)-1}={budget}; all later values are zero")


def constructed_control():
    """One exact example following the free-rank construction."""
    p, h = 306, 485
    j = [int(0 < r <= p // 3 and r % 2 == 1) for r in range(p)]
    order = [(i * h) % p for i in range(p)]
    word = []
    carry, elapsed = 0, 0
    for r in order:
        octave, target = divmod(r + h, p)
        a = octave + j[r] - j[target]
        require(a in (1, 2), "constructed valuation")
        word.append(a)
        carry = 3 * carry + 2**elapsed
        elapsed += a
    require(elapsed == h, "constructed lap clock")
    s = Fraction(carry, 2**h - 3**p)
    x = s
    mantissas, physical, parity = {}, [], []
    for r, a in zip(order, word):
        require(x.denominator == s.denominator and x.numerator % 2 == 1,
                "constructed odd phase")
        mantissas[r] = x / 2**j[r]
        physical.append(x)
        parity.append(1)
        x = (3*x + 1) / 2
        if a == 2:
            require(x.numerator % 2 == 0, "constructed even phase")
            physical.append(x)
            parity.append(0)
            x /= 2
    require(x == s and s.denominator > 1, "constructed nonordinary return")
    dyadic = [mantissas[r] for r in range(p)] + [2*s]
    require(all(a < b for a, b in zip(dyadic, dyadic[1:])), "constructed dyadic order")
    ternary = [x if x < 3*s else x/3 for x in physical]
    ranks = {v: i for i, v in enumerate(sorted(ternary))}
    require(len(ranks) == h and all(s <= v < 3*s and ranks[v] == -i*p % h
                                    for i, v in enumerate(ternary)), "constructed ternary order")
    changes = 1 + sum(a != b for a, b in zip(j, j[1:]))
    high_records = 0
    for i, x in enumerate(physical):
        score = 0
        for k in range(1, h+1):
            score += 5*parity[(i-k) % h] - 3
            if score <= 0:
                break
        else:
            high_records += int(x > 2*s)
    require(sum(j) == 51 and changes == 103 and high_records > 0, "constructed counts")
    print(f"constructed p={p} h={h} sorted_changes={changes} high_odd={sum(j)} "
          f"high_strict_records={high_records} reduced_denominator_bits={s.denominator.bit_length()}")


if __name__ == "__main__":
    main()
    constructed_control()
