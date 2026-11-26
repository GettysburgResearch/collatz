"""Exact finite controls for the ascent optimizer, gate, and rank-two obstructions."""

import argparse
import json
from functools import cache


def require(test, message):
    if not test:
        raise ValueError(message)


def step(x):
    return (3 * x + 1) // 2 if x & 1 else x // 2


def visit(x, clocks):
    path = [x]
    for _ in range(clocks):
        path.append(step(path[-1]))
    return path


def first_hit(x):
    path = [x]
    while path[-1] != 1:
        require(len(path) < 100_000, f"explicit first-hit control timed out at {x}")
        path.append(step(path[-1]))
    return path


def odd_count(path):
    return sum(x % 2 for x in path[:-1])


def potential(m):
    return {2: 5, 4: 18, 7: 50}.get(m, m * m)


def compressed_word(m, count, clocks):
    """Search all words with at most clocks and exactly count more odd inverses."""
    if count == 0:
        return ()
    if m % 3 == 0:
        return None
    # A completion starts at absolute magnitude at least 2, so P(source) >= 4.
    if 4**clocks * potential(m) < 4 * 8**count:
        return None
    first = 2 if m % 3 == 2 else 1
    for e in range(first, clocks - count + 2, 2):
        nxt = ((m << e) + 1) // 3
        tail = compressed_word(nxt, count - 1, clocks - e)
        if tail is not None:
            return (e,) + tail
    return None


@cache
def optimal(count):
    if not count:
        return 0, ()
    lower = optimal(count - 1)[0] + 1
    for clocks in range(lower, 6 * count + 1):
        word = compressed_word(2, count, clocks)
        if word is not None:
            require(sum(word) == clocks, "first feasible budget was not used")
            return clocks, word
    raise ValueError("no signed word below proved constructive upper bound")


def minimum_magnitudes(magnitude, count, clocks):
    """All endpoints at the exact clock, including unsuccessful recursive branches."""
    if not count:
        if not clocks:
            yield magnitude
        return
    if magnitude % 3 == 0 or 4**clocks * potential(magnitude) < 4 * 8**count:
        return
    first = 2 if magnitude % 3 == 2 else 1
    for e in range(first, clocks - count + 2, 2):
        yield from minimum_magnitudes(((magnitude << e) + 1) // 3, count - 1, clocks - e)


def cofactor_classes(r, clocks):
    k = penalty(r, clocks)
    modulus = 3**k
    inverse = pow(2 ** (clocks + 1), -1, modulus)
    magnitudes = sorted(minimum_magnitudes(2, r, clocks))
    residues = sorted((m - 1) * inverse % modulus for m in magnitudes)
    require(len(set(residues)) == len(magnitudes), "optimal roots should have distinct classes")
    require(len(residues) * 2**k < modulus, "frequency bound")
    return {"all_minimizing_magnitudes": magnitudes, "optimal_cofactor_modulus": modulus,
            "optimal_cofactor_residues": residues}


def test_supplied_cofactors():
    r = 1
    clocks, _ = optimal(r)
    k = penalty(r, clocks)
    classes = cofactor_classes(r, clocks)
    hits = []
    for a in range(1, 251):
        apex = 3 * a - 1
        found = False
        for w in range(1, 2*a - 1):
            cost = 0
            u = w
            while cost <= r+k:
                cost += u % 2
                v = step(u)
                if v == apex and u == 2*apex and cost == r+k:
                    found = True
                    break
                u = v
            if found:
                break
        predicted = (a % (3**k)) in classes["optimal_cofactor_residues"]
        require(predicted == found, "exhaustive supplied cofactor test disagrees")
        if found:
            hits.append(a)
    return {"r": r, "all_supplied_cofactors_through": 250, "attaining_cofactors": hits}


def independent_clocks(max_count):
    """No pruning, no compressed odd edges, no use of P, clock-by-clock."""
    layer = [(2, 0)]
    minima = {}
    clocks = 0
    while len(minima) != max_count:
        next_layer = []
        for m, count in layer:
            if 0 < count <= max_count:
                minima.setdefault(count, clocks)
            next_layer.append((2 * m, count))
            if m % 3 == 1:
                next_layer.append(((2 * m + 1) // 3, count + 1))
        layer = next_layer
        clocks += 1
    return minima


def penalty(r, clocks):
    k = 0
    while 3**k <= 2 ** (k + clocks + 1 - r):
        k += 1
    return k


def ascent_example(r, clocks, word, *, power_apex=False):
    s = 2
    for e in word:
        require(((s << e) + 1) % 3 == 0, "illegal negative inverse")
        s = ((s << e) + 1) // 3
    signed_path = visit(-s, clocks)
    require(signed_path[-1] == -2 and odd_count(signed_path) == r, "signed word did not replay")
    k = penalty(r, clocks)
    modulus = 3**k
    a0 = ((s - 1) * pow(2 ** (clocks + 1), -1, modulus)) % modulus
    if power_apex:
        target = 3**r * a0 - 1
        # Lift the ordinary discrete logarithm one ternary digit at a time.
        height = 1
        period = 2
        for depth in range(2, r + k + 1):
            power = 3**depth
            height = next(h for h in (height, height + period, height + 2 * period)
                          if pow(2, h, power) == target % power)
            period *= 3
        if height < clocks + k + r + 2:
            height += period
        a = (2**height + 1) // 3**r
    else:
        a = a0 + modulus
    apex = 3**r * a - 1
    start = 2**r * a - 1
    visitor = 2**k * ((2 ** (clocks + 1) * a - s + 1) // modulus) - 1
    require(0 < visitor < start, "matched source missed strict order")
    trail = visit(visitor, k + clocks + 1)
    ramp = visit(start, r)
    require(trail[-1] == apex == ramp[-1], "mismatched physical apex")
    require(trail[-2] == 2 * apex and odd_count(trail) == k + r, "physical edge or cost")
    if power_apex:
        require(apex == 2**height, "apex not required power")
        require(all(v > 1 and v % 2 for v in ramp[:-1]), "native nonterminal site")
        require(not set(trail[:-1]).intersection(ramp), "unexpected earlier native intersection")
        return {"r": r, "power_of_two_exponent": height, "start_bits": start.bit_length(),
                "visitor_bits": visitor.bit_length(), "first_native_intersection": r, "odds": k + r}
    return {"r": r, "clock": clocks, "signed_magnitude": s, "extra_odds": k,
            "minimum_odds": r + k, "inverse_gaps": word}


def supplied_controls():
    j = 11
    z = (2 ** (j + 7) - 271) // 81
    lower = first_hit(z)
    upper = first_hit(3 * z)
    peak = 3**j - 1
    native = first_hit(peak)
    require(lower[7] == 2**j - 1 and lower[7 + j] == peak, "hard family prefix")
    require((len(upper) - 1, odd_count(upper)) == (7 + j, 3), "hard family upper")
    require(max(lower) < 3**18 + 1, "rank-two all-height separation")
    charge = 2 * (j + odd_count(native)) - len(native) + 1
    rank2 = []
    s = 18
    while 4**s <= 2 ** (charge + 1) * 3**s:
        w = (32 * 4**s - 5) // 27
        lo = first_hit(w)
        hi = first_hit(3 * w)
        lower_prefix = lo[:len(hi)]
        require(lo[5] == 4**s + 1 and lower_prefix[-1] == 3**s + 1, "rank-two exact pair path")
        require(min(lower_prefix) == 3**s + 1, "rank-two upper deadline minimum")
        require((len(hi) - 1, odd_count(hi)) == (2 * s + 5, 2), "rank-two upper")
        tail = first_hit(3**s + 1)
        other_charge = 2 * (s + odd_count(tail)) - len(tail) + 1
        require(other_charge != charge, "countercontrol has unexpected augmented link")
        rank2.append({"s": s, "postpeak_first_hit": len(tail) - 1,
                      "postpeak_odd_count": odd_count(tail), "charge": other_charge})
        s += 27
    return {"hard_parent": z, "lower_hit": len(lower) - 1, "lower_maximum": max(lower),
            "upper_hit": len(upper) - 1, "upper_odds": odd_count(upper),
            "postpeak_hit": len(native) - 1, "postpeak_odds": odd_count(native),
            "charge": charge, "rank_two_surviving_charge_bound": rank2,
            "first_excluded_s": s}


def supplied_ascent():
    r = 11
    native = visit(2**r - 1, r)
    locations = {v: i for i, v in enumerate(native)}
    hits = {}
    for w in range(1, native[0]):
        trail = first_hit(w)
        overlaps = [(locations[v], h) for h, v in enumerate(trail) if v in locations]
        if not overlaps:
            continue
        i, h = min(overlaps)
        require(i == 0 or (h > 0 and trail[h - 1] == 2 * native[i]), "off-ascent origin")
        cost = odd_count(trail[:h + 1])
        if i > 0:
            require(cost >= i + penalty(i, optimal(i)[0]), "physical lower bound failed")
        entry = hits.setdefault(i, {"sources": 0, "w": w, "minimum_odds": cost})
        entry["sources"] += 1
        if cost < entry["minimum_odds"]:
            entry.update(w=w, minimum_odds=cost)
    return {"r": r, "a": 1, "source_limit_exclusive": native[0], "by_first_native_clock": hits}


PHASE_ROWS = (
    (17, 51, 1, 126), (23, 147, 0, 80), (24, 90, 10, 1074),
    (25, 71, 7, 752), (26, 62, 11, 1158), (27, 121, 1, 164),
    (28, 124, 9, 990), (29, 81, 9, 962), (30, 168, 1, 192),
    (31, 59, 3, 328), (33, 163, 4, 496), (37, 47, 8, 832),
    (48, 78, 8, 844),
)


def phase_controls():
    for root, period, odds in ((-5, 3, 2), (-17, 11, 7)):
        trail = visit(root, period)
        require(trail[-1] == root and odd_count(trail) == odds, "signed lap")
    result = []
    for e, first, m0, n0 in PHASE_ROWS:
        h0 = first + 162*m0
        row = {"third_odd_gap": e, "first_upper_clock": first, "base_m": m0,
               "base_upper_clock": h0, "base_exponent": n0}
        for t in (0, 1, 2):
            h, n = h0 + 1782*t, n0 + 1134*t
            z, rem = divmod(2**h - 15 - 2**(e+2), 81)
            require(not rem and z % 48 == 17, "canonical phase source")
            hi = visit(3*z, h)
            require(hi[-1] == 1 and 1 not in hi[:-1], "certified first upper hit")
            require([i for i, u in enumerate(hi[:-1]) if u % 2] == [0, 1, 2+e], "upper gap")
            lo = visit(z, h)
            require(lo[-1] == 3**n-17 and odd_count(lo) == n+4, "lower actual phase")
            k = n//2 - 1
            w = 2**(3*k+1) - 5
            arriving = visit(w, 3*k+1)
            require(arriving[-1] == 3**(n-1)-7, "explicit smaller visitor")
            require(visit(arriving[-1], 3)[-1] == visit(lo[-1], 3)[-1], "cross-phase merger")
            if t:
                require(2**40*w < z, "lowest-height contradiction at larger parameter")
            else:
                require(2**40*(w+5) < 2**81*z, "uniform advancing height margin")
                if 2**40*w >= z:
                    row["exceptional_base_first_hit"] = len(first_hit(z))-1
        if m0 >= 11:
            z = (2**first - 15 - 2**(e+2)) // 81
            row["preceding_same_class_first_hit"] = len(first_hit(z))-1
        result.append(row)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-odds", type=int, default=32)
    args = parser.parse_args()
    require(1 <= args.max_odds <= 100, "choose 1 <= --max-odds <= 100")
    independent = independent_clocks(11)
    rows = []
    for r in range(1, args.max_odds + 1):
        clocks, word = optimal(r)
        if r in independent:
            require(clocks == independent[r], "independent breadth search disagrees")
        rows.append(ascent_example(r, clocks, word) | cofactor_classes(r, clocks))
    result = {"ascent_optima": rows, "independent_unpruned_clocks": independent,
              "ordinary_power_apex_examples": [ascent_example(r, *optimal(r), power_apex=True)
                                              for r in (1, 2)],
              "supplied_ascent": supplied_ascent(), "upper_certificate_controls": supplied_controls(),
              "supplied_optimum_classes": test_supplied_cofactors(), "rank_three_phase_rows": phase_controls()}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
