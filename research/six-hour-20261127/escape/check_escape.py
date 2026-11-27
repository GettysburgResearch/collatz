"""Exact ternary densities, certified dyadic sieve and prediction controls."""
import json
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb

SCALE = 10**18
B_NUM, B_DEN = 13, 8


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def odd_step(x):
    z = 3*x + 1
    e = (z & -z).bit_length() - 1
    return z >> e, e


def words_and_residues(depth):
    """Backwards ternary prefixes, including all budget checks."""
    states = [(0, 0)]
    modulus = 1
    for length in range(1, depth + 1):
        parent = modulus
        modulus *= 3
        nxt = []
        for total, residue in states:
            for e in range(1, B_NUM*length//B_DEN - total + 1):
                new_total = total + e
                # Reversed gaps append 3^(length-1)/2^new_total to the offset.
                # Keep exact fractions until the final precision is known.
                nxt.append((new_total, residue + Fraction(parent, 2**new_total)))
        states = nxt
    cells = {int(v.numerator * pow(v.denominator, -1, modulus)) % modulus
             for _, v in states}
    require(len(cells) <= comb(B_NUM*depth//B_DEN, depth), "incoming count")
    return cells


def density_step(prev, den):
    """Double around the entire unit cycle and solve the periodic recurrence."""
    q = 3*len(prev)
    length = 2*q//3
    order = [1]
    for _ in range(1, length):
        order.append(2*order[-1] % q)
    require(len(set(order)) == length and 2*order[-1] % q == 1, "doubling order")
    source = [prev[((2*r-1)//3) % len(prev)] if r % 3 == 2 else 0 for r in order]
    factor = (1 << length) - 1
    n = 0
    for v in source:
        n = 2*n + 3*v
    initial = n
    nxt = [0]*q
    for r, v in zip(order, source):
        nxt[r] = n
        n = 2*n - 3*factor*v
    outden = den*factor
    require(n == initial and min(nxt) == 0 and sum(nxt) == q*outden, "density mass")
    return nxt, outden


def independent_step(prev, den):
    """Sum all original geometric final-gap period classes explicitly."""
    q = 3*len(prev)
    period = 2*q//3
    factor = (1 << period) - 1
    mass = [0]*q
    for a, n in enumerate(prev):
        x = 3*a + 1
        for e in range(1, period + 1):
            x = x * pow(2, -1, q) % q
            mass[x] += 3*n*(1 << (period-e))
    return mass, den*factor


def forward_sieves(x, limit):
    elapsed = 0
    marks = []
    for i in range(1, limit + 1):
        x, e = odd_step(x)
        elapsed += e
        marks.append(B_DEN*elapsed <= B_NUM*i and (not marks or marks[-1]))
    return marks


def predict_two_gap(z, r):
    word = []
    for _ in range(r):
        if z % 3 == 0:
            return None
        e = 1 if z % 3 == 2 else 2
        word.append(e)
        z = ((1 << e)*z - 1)//3
    return tuple(word)


def sampled_layer(k, nums, den, cells):
    q = len(nums)
    by_cell = {(d, r): defaultdict(lambda: defaultdict(int))
               for d in range(1, min(5, k)+1) for r in (1, 2)}
    masks = (2, 8, 32)
    forward = dict.fromkeys(masks, 0)
    weight_sum = 0
    digest = sha256()
    for y in range(1, 2*q, 2):
        a = nums[y % q]
        b = den*y
        weight = (SCALE*a*a)//(b*(a+b))
        weight_sum += weight
        byte_count = max(1, (weight.bit_length()+7)//8)
        digest.update(byte_count.to_bytes(4, 'big'))
        digest.update(weight.to_bytes(byte_count, 'big'))
        marks = forward_sieves(y, masks[-1])
        for m in masks:
            if marks[m-1]:
                forward[m] += weight
        z = y
        word = []
        for r in (1, 2):
            z, e = odd_step(z)
            word.insert(0, e)
            if max(word) <= 2:
                require(predict_two_gap(z % 3**r, r) == tuple(word), "two-gap decoder")
            for d in range(1, min(5, k)+1):
                t = z % 3**d
                if t in cells[d]:
                    by_cell[d, r][t][tuple(word)] += weight
    results = []
    for (d, r), counts in by_cell.items():
        mass = sum(sum(group.values()) for group in counts.values())
        loss = sum(sum(group.values()) - max(group.values()) for group in counts.values())
        results.append([d, r, mass, loss])
    return {"k": k, "odd_representatives": q, "floor_sum": weight_sum,
            "floor_vector_sha256": digest.hexdigest(),
            "forward_floor_sums": forward, "prediction_d_r_mass_loss": results}


def route(word, h):
    anchors = {1}
    for _ in range(h):
        anchors = {((1 << e)*a-1)//3 for a in anchors for e in range(1, 7)
                   if ((1 << e)*a) % 9 in (4, 7)}
    require(len(anchors) == 2**h, "anchor count")
    q = 3**len(word)
    residue = 0
    for e in word:
        residue = ((3*residue + 1)*pow(2, -e, q)) % q
    terminals = set()
    for a in anchors:
        routing = next(e for e in range(1, 2*q+1) if (1 << e)*a % (3*q) == 3*residue+1)
        z = ((1 << routing)*a-1)//3
        y = z
        for e in reversed(word):
            t = (1 << e)*y-1
            require(t > 0 and t % 3 == 0, "word admissibility")
            y = t//3
        for e in word:
            y, actual = odd_step(y)
            require(actual == e, "true routed gap")
        require(y == z and odd_step(z) == (a, routing), "routed target")
        require(predict_two_gap(z % q, len(word)) == tuple(reversed(word)), "routed decode")
        terminals.add(z)
    require(len(terminals) == len(anchors), "distinct lifts")
    return max(z.bit_length() for z in terminals)


def main():
    require(2**13 > 3**8 and 13**13 < 3**8 * 8**8 * 5**5, "sieve parameter")
    cells = {d: words_and_residues(d) for d in range(1, 6)}
    for d in range(2, 6):
        require({r % (3**(d-1)) for r in cells[d]} <= cells[d-1], "nested targets")
    rows = []
    prev, den = [1], 1
    for k in range(1, 9):
        nums, newden = density_step(prev, den)
        if k <= 4:
            require((nums, newden) == independent_step(prev, den), "independent geometric sum")
        rows.append(sampled_layer(k, nums, newden, cells))
        prev, den = nums, newden
    biggest = max(route(w, 5) for w in product((1, 2), repeat=4))
    print(json.dumps({"scope": "finite source-weighted controls only",
                      "budget": [B_NUM, B_DEN], "scale": SCALE,
                      "interval": "unscaled subset totals and Bayes errors lie between the displayed floor sum/scale and (floor sum+3^k)/scale; divide by k for M_k",
                      "J_cell_counts": {d: len(s) for d, s in cells.items()},
                      "routed_length_four_words": 16, "distinct_lifts_per_word": 32,
                      "largest_routed_terminal_bits": biggest, "layers": rows}, indent=2))


if __name__ == "__main__":
    main()
