#!/usr/bin/env python3
"""Exact boundary controls for UC-D; no all-word census or Collatz claim."""
import json
from math import gcd, prod


def require(condition, message):
    if not condition:
        raise ValueError(message)


def smooth_part(n):
    require(n > 0, "nonzero cross-carry gcd")
    answer = 1
    for prime in (2, 3):
        while n % prime == 0:
            answer *= prime
            n //= prime
    return answer


def word_data(word):
    require(word and set(word) <= {"0", "1"}, "nonempty binary word")
    carry = 0
    for j, bit in enumerate(word):
        if bit == "1":
            carry = 3 * carry + 2**j
    return 3**word.count("1"), 2**len(word), carry


def check_cycle(states, blocks, asserted_denominator=None):
    """Blocks here may be abstract affine maps; that scope is explicit."""
    require(len(states) == len(blocks) > 1, "one block per edge")
    require(len(set(states)) > 1, "nonconstant cycle")
    for i, (P, Q, C) in enumerate(blocks):
        require(P > 0 and Q > P and C >= 0, "contracting positive block")
        require(Q * states[(i + 1) % len(states)] == P * states[i] + C,
                "literal edge")
    require(any(P % 3 == 0 for P, Q, C in blocks), "odd reference block")
    d = [Q - P for P, Q, C in blocks]
    E = [[d[i] * blocks[j][2] - d[j] * blocks[i][2]
          for j in range(len(blocks))] for i in range(len(blocks))]
    G = 0
    for row in E:
        for entry in row:
            G = gcd(G, abs(entry))
    s = smooth_part(G)
    D = prod(Q for P, Q, C in blocks) - prod(P for P, Q, C in blocks)
    require(gcd(D, 6) == 1, "complete determinant unit")
    if asserted_denominator is not None:
        require(D == asserted_denominator, "whole denominator retained")
    ref = next(i for i, (P, Q, C) in enumerate(blocks) if P % 3 == 0)
    a = (blocks[ref][2] * pow(d[ref], -1, s)) % s
    require(all((d[i] * a - blocks[i][2]) % s == 0
                for i in range(len(blocks))), "common fixed residue")
    require(all((x - a) % s == 0 for x in states), "ordinary boundary lattice")
    m = min(states)
    entering = next(i for i, x in enumerate(states)
                    if x > m and states[(i + 1) % len(states)] == m)
    leaving = next(i for i, x in enumerate(states)
                   if x == m and states[(i + 1) % len(states)] > m)
    alpha = (states[entering] - m) // s
    beta = (states[(leaving + 1) % len(states)] - m) // s
    Pi, Qi, _ = blocks[entering]
    Pj, Qj, _ = blocks[leaving]
    threshold = Qi * Qj - Pi * Pj
    require(alpha >= 1 and beta >= 1, "minimum plateau entrances")
    require(E[entering][leaving] ==
            s * (d[entering] * Qj * beta + d[leaving] * Pi * alpha),
            "exact two-edge elimination")
    require(E[entering][leaving] >= s * threshold, "pair denominator capacity")
    return {"states": states, "blocks": blocks, "complete_D": D,
            "smooth_lattice": s, "corner": [entering, leaving],
            "cross_carry": E[entering][leaving], "capacity": s * threshold}


def rejected(call):
    try:
        call()
    except ValueError:
        return True
    return False


def main():
    controls = 0
    shapes = [(3, 4), (9, 16), (1, 4), (27, 32)]
    for pattern in ([0, 1], [0, 0, 3, 1], [0, 2, 0, 1, 3]):
        for scale in (1, 6, 64, 729):
            xs = [1 + scale * (1000 + p) for p in pattern]
            maps = []
            for i, x in enumerate(xs):
                P, Q = shapes[i % len(shapes)]
                maps.append((P, Q, Q * xs[(i + 1) % len(xs)] - P * x))
            check_cycle(xs, maps)
            controls += 1

    sharp = check_cycle([4, 3], [(3, 4, 0), (3, 8, 23)])
    require(sharp["cross_carry"] == sharp["capacity"] == 23,
            "strict threshold is necessary")

    sparse_controls = 0
    for u, t in (("11101010", "1"), ("10", "110"), ("11110001", "001")):
        P, Q, C = word_data(u)
        R, S, B = word_data(t)
        require(Q > P, "contracting base word")
        E = (Q-P)*B-(S-R)*C
        require(E != 0, "distinct fixed expressions")
        for k in (0, 1, 2, 7, 19):
            Pk, Qk, Ck = word_data(u*k+t)
            require((P, Q, C) == word_data(u), "base unchanged")
            require(Pk == R*P**k and Qk == S*Q**k, "full shape")
            require((Q-P)*Ck-(Qk-Pk)*C == Q**k*E,
                    "sparse-defect complete commutator")
            sparse_controls += 1

    bad = [
        rejected(lambda: check_cycle([1, 2], [(3, 2, 1), (1, 2, 0)])),
        rejected(lambda: check_cycle([4, 3], [(3, 4, 0), (3, 8, 24)])),
        rejected(lambda: check_cycle([4, 3], [(3, 4, 0), (3, 8, 23)], 1)),
    ]
    require(all(bad), "invalid hypotheses and mutations rejected")
    print(json.dumps({
        "status": "PASS", "scope": "finite exact controls of a written theorem",
        "abstract_affine_cycles_not_collatz": controls,
        "includes_pure_even_reference_variant": True,
        "includes_repeated_minimum_plateaus": True,
        "sharp_abstract_unequal_cycle_not_collatz": sharp,
        "literal_sparse_defect_controls": sparse_controls,
        "rejected_controls": len(bad),
        "unrestricted_Collatz": "OPEN",
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
