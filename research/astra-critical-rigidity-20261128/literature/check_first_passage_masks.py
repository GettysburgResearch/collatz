"""Exact small native first-passage word fixtures for logarithmic square masks."""
from fractions import Fraction
from hashlib import sha256
import json


def require(condition, context):
    if not condition:
        raise ArithmeticError(context)


def literal_replay(gaps):
    modulus = 3 ** len(gaps)
    total = 0
    res = 0
    for i, gap in enumerate(reversed(gaps)):
        total += gap
        res = (res + 3**i * pow(2, -total, modulus)) % modulus
    terminal = res + modulus * (3 + res % 2)
    seed = terminal
    for gap in reversed(gaps):
        seed, rem = divmod((seed << gap) - 1, 3)
        require(not rem and seed > 0 and seed % 2, ("inverse", gaps))
    y = seed
    for gap in gaps:
        triple = 3 * y + 1
        require((triple & -triple) == 1 << gap, ("valuation", gaps))
        y = triple >> gap
    require(y == terminal, ("true terminal", gaps))
    return res


def small_stop(level, depth):
    words = []
    failed_tail = Fraction()
    censored = Fraction()

    def visit(gaps, total):
        nonlocal failed_tail, censored
        k = len(gaps)
        gain = Fraction(3**k, 2**total)
        require(gain >= 1, "a dead prefix was continued")
        if gain >= level:
            require(gain < Fraction(3, 2) * level, "terminal tilt overshoot")
            words.append((gaps, total))
            return
        if k == depth:
            censored += Fraction(1, 2**total)
            return
        gap = 1
        while 3 ** (k + 1) > 2 ** (total + gap):
            visit(gaps + (gap,), total + gap)
            gap += 1
        # All larger next gaps end this excursion at once.
        failed_tail += Fraction(1, 2 ** (total + gap - 1))

    visit((), 0)
    fair = sum((Fraction(1, 2**s) for _, s in words), Fraction())
    tilted = sum((Fraction(3 ** len(v), 4**s) for v, s in words), Fraction())
    volume = sum((Fraction(1, 3 ** len(v)) for v, _ in words), Fraction())
    require(fair + failed_tail + censored == 1, "prefix-free probabilities")
    require(fair <= 1 / level and volume <= fair / level, "full cylinder cost")
    require(level * fair <= tilted < Fraction(3, 2) * level * fair,
            "reverse stopped likelihood")
    residues = [literal_replay(v) for v, _ in words]
    return {"L": str(level), "depth_cap": depth, "words": len(words),
            "fair_mass": str(fair), "tilted_mass": str(tilted),
            "sum_cylinder_volumes": str(volume),
            "residue_digest": sha256(str(residues).encode()).hexdigest()}


def envelope_checks():
    profiles = (lambda j: 1 + j.bit_length().bit_length() // 3,
                lambda j: 3 if j < 2**31 else 10**12,
                lambda j: 1 + j // 7)
    count = 0
    for w in profiles:
        b = [1]
        for e in range(1, 122):
            b.append(min(b[-1] + 1, w(1 << (e - 1))))
        for e in range(4, 120):
            for j in (1 << e, (1 << (e + 1)) - 1):
                for other in (e - 1, e, e + 1):
                    require(Fraction(b[other], 2**other) <= Fraction(4 * w(j), j),
                            ("stage envelope", e, j, other))
                    count += 1
    return count


if __name__ == "__main__":
    fixtures = [small_stop(Fraction(n, d), k)
                for n, d, k in ((3, 2, 6), (2, 1, 8), (3, 1, 10), (7, 2, 12))]
    print(json.dumps({"finite_prefix_free_stopping_trees": fixtures,
                      "neighbor_comparisons": envelope_checks()}, sort_keys=True, indent=2))
