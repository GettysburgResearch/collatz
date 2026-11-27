"""Uniform bounds for the actual location of two-sided native CRT addresses."""
from fractions import Fraction
from itertools import product
from math import isqrt
from operator import add
from pathlib import Path
import json

from check_period_gap import (
    AboveLog, GAIN_DEN, GAIN_NUM, STRIP_DEN, STRIP_NUM, ceil_div, require,
)

# Increasing primitive odd period as in the frozen PERIOD_CONTROLS.json.
# Circle bins, combined depth, and normalized rank bin [a/12, (a+1)/12).
TESTS = (
    (2048, 46, 13), (4096, 49, 22), (512, 46, 13), (1024, 49, 22),
    (512, 48, 20), (512, 49, 22), (512, 50, 13), (512, 51, 15),
    (512, 51, 15), (1024, 53, 20), (2048, 54, 19), (4096, 56, 13),
    (512, 54, 19), (1024, 57, 19), (512, 57, 19), (512, 59, 22),
    (1024, 61, 15), (1024, 66, 13), (2048, 73, 22), (8192, 77, 22),
    (4096, 80, 13), (2048, 82, 22), (1024, 83, 22), (16384, 90, 13),
    (32768, 100, 22),
)


def allowed(j, grade, a, b, backwards):
    three, two = 3**j, 1 << grade
    if backwards:
        return ((a+1)*two >= b*three
                and a*two*STRIP_DEN <= b*three*STRIP_NUM)
    return (a*three*STRIP_DEN <= b*two*STRIP_NUM
            and (a+1)*three*GAIN_NUM >= b*two*GAIN_DEN)


def transitions(depth, a, b, backwards):
    layers = []
    old = {0}
    for j in range(1, depth+1):
        moves = [(v, v+e) for v in sorted(old) for e in (1, 2)
                 if allowed(j, v+e, a, b, backwards)]
        layers.append(moves)
        old = {w for _, w in moves}
    return layers


def angular_increment(j, before, after, p3, p2, backwards):
    if backwards:
        return (3**(j-1)*pow(p2*(1 << after), -1, p3) % p3, p3)
    return (-(1 << before)*pow(p3*3**j, -1, p2) % p2, p2)


def histogram(layers, p3, p2, size, backwards):
    # The constant half-turn of the future address is immaterial to the peak.
    row = {0: [1] + [0]*(size-1)}
    for j, moves in enumerate(layers, start=1):
        nxt = {}
        for v, w in moves:
            num, den = angular_increment(j, v, w, p3, p2, backwards)
            offset = size*num//den
            source = row[v]
            rotated = source[-offset:] + source[:-offset] if offset else source
            nxt[w] = list(map(add, nxt[w], rotated)) if w in nxt else rotated
        row = nxt
    return row


def moments(buckets):
    total = sum(buckets)
    variance = len(buckets)*sum(x*x for x in buckets)-total*total
    require(variance >= 0, "centered second moment")
    return total, variance


def interval_cap(left, right, width, modulus, depth):
    """Bound any interval of integer starts of the given rational width."""
    size = len(left)
    require(size == len(right), "common quantization")
    n, v = moments(left)
    m, w = moments(right)
    peak = (n*m+isqrt(v*w))//size
    bins = (size*width)//modulus+depth+2
    return peak*bins


def band_cap(a, b, size, k, f, height):
    past = transitions(k, a, b, True)
    future = transitions(f, a, b, False)
    total = 0
    p3 = 3**k
    for grade in sorted({w for _, w in future[-1]}):
        p2 = 1 << (grade+1)
        past_rows = histogram(past, p3, p2, size, True)
        left = list(map(sum, zip(*past_rows.values())))
        right = histogram(future, p3, p2, size, False)[grade]
        total += interval_cap(left, right, Fraction(height, b), p3*p2, k+f)
    return total


def literal_addresses(layers, p3, p2, size, backwards):
    """Independent exact affine recurrence for short words, including carries."""
    out = {}
    depth = len(layers)
    for word in product((1, 2), repeat=depth):
        grade = carry = bucket = 0
        for j, e in enumerate(word, start=1):
            v, w = grade, grade+e
            if (v, w) not in layers[j-1]:
                break
            if backwards:
                carry = (1 << e)*carry+3**(j-1)
            else:
                carry = 3*carry+(1 << v)
            num, den = angular_increment(j, v, w, p3, p2, backwards)
            bucket += size*num//den
            grade = w
        else:
            if backwards:
                residue = carry*pow(1 << grade, -1, p3) % p3
            else:
                residue = ((1 << grade)-carry)*pow(3**depth, -1, p2) % p2
            out.setdefault(grade, []).append((residue, bucket % size))
    return out


def short_checks():
    k, f, a, b, size = 3, 4, 3, 2, 73
    past, future = transitions(k, a, b, True), transitions(f, a, b, False)
    examined = 0
    for grade in sorted({w for _, w in future[-1]}):
        p3, p2 = 3**k, 1 << (grade+1)
        modulus = p3*p2
        prev = literal_addresses(past, p3, p2, size, True)
        nexts = literal_addresses(future, p3, p2, size, False)[grade]
        l = list(map(sum, zip(*histogram(past, p3, p2, size, True).values())))
        r = histogram(future, p3, p2, size, False)[grade]
        direct_l, direct_r = [0]*size, [0]*size
        exact = [0]*modulus
        for res, slot in (item for row in prev.values() for item in row):
            direct_l[slot] += 1
            for rem, pos in nexts:
                x = next(i for i in range(rem, modulus, p2) if i % p3 == res)
                # The true second address includes a half-turn.
                error = (Fraction(size*x, modulus)-slot-pos-Fraction(size, 2)) % size
                require(error < k+f, "joint angular enclosure")
                exact[x] += 1
                examined += 1
        for _, pos in nexts:
            direct_r[pos] += 1
        require((direct_l, direct_r) == (l, r), "literal histogram")
        prefix = [0]
        for v in exact*3:
            prefix.append(prefix[-1]+v)
        for width in (1, 17, modulus//3, modulus+13):
            cap = interval_cap(l, r, Fraction(width), modulus, k+f)
            maximum = max(prefix[t+width]-prefix[t] for t in range(modulus))
            require(maximum <= cap, "literal interval population")
    return examined


def checks():
    log = AboveLog()
    archive = Path(__file__).with_name("PERIOD_CONTROLS.json")
    pairs = json.loads(archive.read_text())["ordinary_joint_pairs"]
    require(len(pairs) == len(TESTS) == 25, "complete finite input")
    require(pairs == sorted(pairs, key=lambda pair: pair[1]), "period order")
    results = []
    for (h, p), (size, depth, a) in zip(pairs, TESTS):
        slope = Fraction(h, p)
        lowest_eps, highest_eps = slope-log.upper, slope-log.lower
        require(0 < lowest_eps <= highest_eps, "slope orientation")
        high = ceil_div(7*lowest_eps.denominator, 20*lowest_eps.numerator)
        low = max(1 << 71, (1/highest_eps-8)//16)
        require(1000 <= p <= low//100 and low <= high, "physical onset")
        cap = 0
        for j in range(3):
            b = 12 >> j
            if a*STRIP_DEN <= b*STRIP_NUM:
                cap += band_cap(a, b, size, depth//2, depth-depth//2, high)
        need = Fraction(2884*p, 1000*(2*a+1))-Fraction(p*p, low)-2
        demand = ceil_div(need.numerator, need.denominator)
        require(cap < demand, "physical rank interval overfull")
        results.append({"odd_period": p, "clock": h, "circle_bins": size,
                        "odd_window": depth, "rank_index_over_12": a,
                        "upper_population": cap, "lower_population": demand})
    return {"control_word_pairs": short_checks(), "excluded": results,
            "period_upper_limit_tested": "10^1000"}


if __name__ == "__main__":
    print(json.dumps(checks(), indent=2))
