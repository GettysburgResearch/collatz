#!/usr/bin/env python3
"""Replay ordinary trajectories, word carries, and the protected decoder controls."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json


ROWS = (
    (12_977_607, 25_165_824, 4_933_001, 9_565_938,
     ((3, 1), (1, 1), (1, 1), (1, 2), (4, 2), (3, 2)),
     ((1, 1), (1, 1), (1, 2), (3, 2), (3, 1), (4, 2))),
    (73_870_594_215, 103_079_215_104, 404_800_088_233, 564_859_072_962,
     ((3, 1), (2, 1), (5, 1), (1, 1), (1, 1), (1, 1), (1, 2), (5, 2), (4, 1)),
     ((1, 1), (1, 1), (2, 1), (3, 1), (1, 2), (1, 1), (5, 2), (4, 1), (5, 1))),
)


def require(test, why):
    if not test:
        raise RuntimeError(why)


def word(labels):
    return tuple(v for t, b in labels for v in (1,) * t + (0,) * b)


def record(bits):
    carry = count = 0
    gain = Fraction(1)
    minimum = None
    for i, bit in enumerate(bits):
        if bit:
            carry = 3 * carry + (1 << i)
            count += 1
        gain *= Fraction(3 if bit else 1, 2)
        minimum = gain if minimum is None else min(minimum, gain)
    return carry, count, minimum


def visit(x, bits):
    states = [x]
    for bit in bits:
        require(x % 2 == bit, "physical parity mismatch")
        x = (3 * x + 1 if bit else x) // 2
        states.append(x)
    return states


def row_control(row):
    x, step, end, end_step, u, v = row
    require(sorted(u) == sorted(v) and u != v, "multiset mismatch")
    wu, wv = word(u), word(v)
    nu, p, minimum = record(wu)
    nv, q, _ = record(wv)
    require(len(wu) == len(wv) and p == q and nv - nu == 6 * 3**p, "bad carry")
    require(step % (2 ** (len(wu) + 1)) == 0, "terminal parity not fixed")
    require(3**p * step == 2**len(wu) * end_step, "affine slope mismatch")
    require(x % 3 == step % 3 == 0, "ternary progression mismatch")
    for k in (0, 1, 2, 3, 13, 127, 2**127 + 7):
        source = x + step * k
        upper, lower = visit(source, wu), visit(source - 6, wv)
        require(upper[-1] == lower[-1] == end + end_step*k, "terminal mismatch")
        require(upper[-1] % 2 == 1, "incomplete final block")
        require(all(3*(y+1) >= source+1 for y in upper), "floor lost")
        if len(u) == 9:
            require(min(upper[1:]) > source, "strict rise lost")
    return {
        "block_count": len(u), "clock": len(wu), "odd_departures": p,
        "shifted_carries": [n + 2**len(wu) - 3**p for n in (nu, nv)],
        "minimum_nonempty_prefix_gain": str(minimum),
        "base_terminal": end, "terminal_increment": end_step,
        "base_upper_boundaries": [upper for i, upper in enumerate(visit(x, wu))
                                  if i in {sum(a+b for a, b in u[:j]) for j in range(len(u)+1)}],
    }


def dictionary_control():
    dictionary = ((3, 1), (4, 2))
    signatures = set()
    for indices in product(range(2), repeat=8):
        labels = tuple(dictionary[j] for j in indices)
        bits = word(labels)
        n, p, minimum = record(bits)
        require(minimum > 1, "coded dictionary lost strict rise")
        key = (tuple(sorted(Counter(labels).items())), n % (3**p))
        require(key not in signatures, "distinct permutations share terminal residue")
        signatures.add(key)
        modulus = 1 << (len(bits) + 1)
        residue = ((2**len(bits) - n) * pow(3**p, -1, modulus)) % modulus
        x = residue + modulus*((-residue * pow(modulus, -1, 3)) % 3)
        state = visit(x, bits)[-1]
        require(state % 2 == 1 and x % 3 == 0, "positive realization")
        for t, b in reversed(labels):
            recovered = (3, 1) if state % 3 == 1 else (4, 2)
            require(recovered == (t, b), "inverse label mismatch")
            up, remainder = divmod((2**b * state + 1) * 2**t, 3**t)
            require(remainder == 0, "fractional predecessor")
            state = up - 1
        require(state == x, "wrong reconstructed original source")
    return {"depth": 8, "distinct_multiset_residue_pairs": len(signatures)}


def main():
    print(json.dumps({"rows": [row_control(row) for row in ROWS],
                      "reverse_decoding": dictionary_control()}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
