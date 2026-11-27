"""Replay precise arithmetic for every cyclic one/two-swap presentation through length 15."""

from collections import Counter
from itertools import product
from math import gcd


def require(condition, reason):
    if not condition:
        raise AssertionError(reason)


def rotate(word, shift):
    return word[shift:] + word[:shift]


def numerator(word):
    intercept = 0
    for i, bit in enumerate(word):
        if bit:
            intercept = 3 * intercept + (1 << i)
    return intercept


def divisors(word):
    n = len(word)
    raw = (1 << n) - 3 ** sum(word)
    cancelled = gcd(raw, numerator(word))
    return raw, cancelled, raw // cancelled


def neighbors(word):
    n = len(word)
    for edge, left in enumerate(word):
        right = (edge + 1) % n
        if left != word[right]:
            moved = list(word)
            moved[edge], moved[right] = moved[right], moved[edge]
            yield edge, tuple(moved)


def classify(word, shift, edges, counts):
    n = len(word)
    weight = sum(word)
    raw, cancelled, denom = divisors(word)
    target = rotate(word, shift)
    require(divisors(target) == (raw, cancelled, denom), "rotation gcd")
    if len(edges) == 1:
        require(cancelled == 1, "one swap")
        counts["single"] += 1
        return
    p, q = edges
    require(p != q and n > 2, "same edge undone")
    cut = next(i for i in range(n) if (i - 1) % n not in edges)
    source = rotate(word, cut)
    target = rotate(target, cut)
    p, q = sorted(((p - cut) % n, (q - cut) % n))
    if q == p + 1:
        triple = source[p:q + 2]
        overlap_type = sum(triple)
        require(overlap_type in (1, 2), "overlap triple")
        factor = 3 if overlap_type == 1 else 5
        require(factor % cancelled == 0, "overlap cancellation")
        counts["overlapping" + str(overlap_type)] += 1
        return
    a = q - p
    vpart = sum(source[p:q])
    sign = 1 if source[p] == source[q] else -1
    difference = abs(3 ** vpart + sign * (1 << a))
    require(difference % cancelled == 0, "factored affine difference")
    local_unit = (1 << p) * 3 ** (weight - sum(source[:q]) - 1)
    require(abs(numerator(source) - numerator(target)) == local_unit * difference,
            "exact affine difference")
    g = gcd(n, shift)
    if sign == 1:
        delta = n * vpart - weight * a
        require(g <= 2 and gcd(n, weight) <= 2, "same direction gcd")
        require(0 < abs(delta) <= 3 * n, "same direction resonance")
        k = 2 * abs(delta)
        require(pow(2, k, cancelled) == 1 % cancelled
                and pow(3, k, cancelled) == 1 % cancelled, "BCZ gcd reduction")
        counts["same direction"] += 1
        return
    m = n // g
    require(g >= 2 and a % g == 0 and weight % m == 0, "opposite rows")
    ell = a // g
    v = weight // m
    require(vpart == ell * v, "equal row weights")
    t = 1 << g
    b = 3 ** v
    r = gcd(m, ell)
    root = t ** r - b ** r
    require(root % cancelled == 0, "whole cancelled divisor")
    require(denom % (raw // root) == 0 and denom ** 2 > (1 << n),
            "whole geometric quotient")
    counts["opposite direction"] += 1


def exhaust(max_n):
    counts = Counter()
    necklaces = 0
    for n in range(2, max_n + 1):
        for word in product(range(2), repeat=n):
            if not 0 < sum(word) or 3 ** sum(word) >= (1 << n):
                continue
            rotations = {rotate(word, h): h for h in range(n)}
            if len(rotations) != n or min(rotations) != word:
                continue
            necklaces += 1
            for first, step in neighbors(word):
                if step in rotations and step != word:
                    classify(word, rotations[step], (first,), counts)
                for second, final in neighbors(step):
                    if final in rotations and final != word:
                        classify(word, rotations[final], (first, second), counts)
    for group in ("single", "overlapping1", "overlapping2", "same direction", "opposite direction"):
        require(counts[group] > 0, "empty presentation class " + group)
    print("primitive positive necklaces", necklaces, "at lengths 2 through", max_n)
    print("presentations", sorted(counts.items()))


def sharp_family(g, v, k, critical):
    a = (1,) * v + (0,) * (g - v)
    bword = a[:v - 1] + (0, 1) + a[v + 1:]
    word = a * k + bword * k
    n = len(word)
    target = rotate(word, g)
    positive = [i for i in range(n) if target[i] > word[i]]
    require(len(positive) == 2 and 2 * (positive[1] - positive[0]) != n, "primitive certificate")
    raw, cancelled, denom = divisors(word)
    t, b = 1 << g, 3 ** v
    factor = t ** k + b ** k
    require(denom % factor == 0 and (t - b) * factor % denom == 0, "sharp sandwich")
    require(raw // cancelled == denom, "reduced denominator")
    if critical:
        require(3 ** (2 * k * v) < (1 << n) < 3 ** (2 * k * v + 1), "critical weight")
    return n, denom.bit_length()


def critical_k(g, v):
    """Compute floor((g log_3(2)-v)^(-1/2)) using only integers."""
    require((1 << g) > 3 ** v, "lower convergent required")
    def permitted(k):
        return (1 << (g * k * k)) <= 3 ** (v * k * k + 1)
    low, high = 0, 1
    while permitted(high):
        low, high = high, 2 * high
    while high - low > 1:
        middle = (low + high) // 2
        if permitted(middle):
            low = middle
        else:
            high = middle
    return low


if __name__ == "__main__":
    exhaust(15)
    for k in range(1, 21):
        n, bits = sharp_family(2, 1, k, False)
        require(bits == (4 ** k + 3 ** k).bit_length(), "fixed row")
    print("fixed rows give d=4^k+3^k through k=20")
    for g, v in ((8, 5), (65, 41), (485, 306)):
        k = critical_k(g, v)
        n, bits = sharp_family(g, v, k, True)
        print("critical template", (g, v), "repeats", k, "length", n, "denominator bits", bits)
