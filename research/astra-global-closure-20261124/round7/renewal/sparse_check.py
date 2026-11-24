"""Finite exact controls for ordered odd-position edits. Safe under Python -O."""

import json
from collections import defaultdict
from itertools import combinations


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def carry(positions):
    value = 0
    for i in positions:
        value = 3 * value + (1 << i)
    return value


def literal_positions(x, e):
    out = []
    for i in range(e):
        if x % 2:
            out.append(i)
            x = (3 * x + 1) // 2
        else:
            x //= 2
    return tuple(out), x


def sharp_example(j):
    power = 3**j
    e, p = 16 * power, 8 * power
    one = tuple(i if i <= j else i + 2 * power for i in range(p))
    two = tuple(i if i < j else i + 2 * power for i in range(p))
    c1, c2 = carry(one), carry(two)
    B, P = 2**e, 3**p
    require(one[0] == two[0] == 0 and one[-1] < e and two[-1] < e, "positive odd start")
    require(sum(x != y for x, y in zip(one, two)) == 1 and two[j]-one[j] == 2*power,
            "one ordered change")
    require((c1-c2) % P == 0 and 2 * max(c1, c2) < B, "fine congruence and offset")
    r = c1 * pow(B, -1, P) % P
    require(r % 3 != 0, "terminal class")
    # Skip the single prohibited lift of each word and choose an odd representative.
    for lift in range(3):
        q = r + P * lift
        if q % 2 == 0:
            q += 3*P
        x, y = (B*q-c1)//P, (B*q-c2)//P
        if x % 3 and y % 3:
            require(min(x, y) > 0 and x != y and x % 2 == y % 2 == 1, "ordinary starts")
            require(literal_positions(x, e) == (one, q), "first fixed-target path")
            require(literal_positions(y, e) == (two, q), "second fixed-target path")
            return {"changed_rank": j, "weight": p, "clock": e, "displacement": 2*power,
                    "positive_target_bits": q.bit_length()}
    raise ArithmeticError("no simultaneous legal lift")


def main():
    comparisons = accepted = cluster_checks = 0
    for e in range(2, 15):
        for p in range(2, e + 1):
            P = 3**p
            groups = defaultdict(list)
            for suffix in combinations(range(1, e), p-1):
                word = (0, *suffix)
                C = carry(word)
                groups[C % P].append(word)
                for j in range(1, p):
                    stop = word[j+1] if j+1 < p else e
                    for d in range(word[j]+1, stop):
                        other_c = C + 3**(p-1-j) * ((1 << d) - (1 << word[j]))
                        admissible = (other_c - C) % P == 0
                        require(admissible == ((d - word[j]) % (2*3**j) == 0),
                                "one-move equivalence")
                        comparisons += 1
                        accepted += int(admissible)
            for values in groups.values():
                for w, v in combinations(values, 2):
                    moved = [j for j in range(p) if w[j] != v[j]]
                    if not 1 <= len(moved) <= 3:
                        continue
                    J = moved[-1]
                    for a, j in enumerate(moved):
                        tail = sum(3**(J-i) * ((1 << w[i]) - (1 << v[i]))
                                   for i in moved[a:])
                        exponent = J+1 if a == 0 else J-moved[a-1]
                        require(tail != 0 and tail % 3**exponent == 0, "retained rank tail")
                        cluster_checks += 1
    require(comparisons > accepted > 0 and cluster_checks > 0, "vacuous census")
    return {"status": "PASS", "max_census_clock": 14, "one_move_comparisons": comparisons,
            "accepted_one_moves": accepted, "nonzero_divisible_rank_tails": cluster_checks,
            "sharp_examples": [sharp_example(j) for j in range(1, 6)]}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
