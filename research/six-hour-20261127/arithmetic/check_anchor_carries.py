"""Third-layer endpoint census using the independently replayed two-row transfer."""
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from unittest.mock import patch

import check_rival_pressure as pressure

ANCHOR = Fraction(1, 700)
LIMIT = 1636
require = pressure.require


def schedules():
    low, high = pressure.SLOPES
    log_two, log_three = pressure.log_bounds(3), pressure.log_bounds(2)
    require((1+low)*log_two[1] < log_three[0] < log_three[1] < (1+high)*log_two[0],
            "strict rotation enclosure")
    with patch.multiple(pressure, ANCHOR=ANCHOR, RETURN_LIMIT=LIMIT):
        floors, cuts = pressure.cuts(low)
        other_floors, other_cuts = pressure.cuts(high)
        mid = (low+high)/2
        coordinates = [x for x, _ in pressure.cuts(mid)[1]]
    require(floors == other_floors and [v for _, v in cuts] == [v for _, v in other_cuts]
            and LIMIT*(high-low) < ANCHOR, "stable clipped and unwrapped schedule")
    result = set()
    for a, b in zip(coordinates, coordinates[1:]):
        for phase in (a, (a+b)/2):
            letters = []
            for _ in range(LIMIT):
                letters.append(str(1+int(phase < mid)))
                phase = (phase-mid) % 1
                if phase < ANCHOR:
                    break
            else:
                raise ArithmeticError("uncovered return")
            result.add("".join(letters))
    require(sorted(map(len, result)) == [665, 971, 1636], "return coverage")
    return sorted(result, key=len)


def edge_ok(m, earlier, later):
    return all(1 <= m+x-y <= 2 for x, y in zip(earlier, later))


def endpoint_counts(first, last):
    left = []
    for k in range(3):
        quadruples = [x for x in product(range(2), repeat=4)
                      if edge_ok(first, x, (k,)*4) and sum(x[:2]) == sum(x[2:])]
        left.append([sum(sum(x[:2]) == j for x in quadruples) for j in range(3)])
    right = []
    for later in ((0, 0, 0, 0), (0, 1, 0, 1), (1, 1, 1, 1)):
        count = 0
        for x in product(range(3), repeat=4):
            c = [4 >> k for k in x]
            count += edge_ok(last, x, later) and (c[0]+c[1]-c[2]-c[3]) % 3 == 0
        right.append(count)
    return left, right


def contract(left, flat, right):
    return [sum(left[k][i]*flat[3*i+j]*right[j] for i in range(3) for j in range(3))
            for k in range(3)]


def literal(word, veto):
    # Enumerate separate actual one-copy paths, then count every ordered
    # quartet. Only the two positives use the veto, inside the trimmed block.
    reversed_veto = [(w[::-1], k) for w, k in veto.items()]
    estimates, nonzero = [], 0
    for k in range(3):
        paths = [(k, 0, 0, "", True)]
        for step, m in enumerate(map(int, word)):
            next_paths = []
            for later, offset, value, history, accepted in paths:
                for earlier in range(3 if step == len(word)-1 else 2):
                    a = m+earlier-later
                    if a not in (1, 2):
                        continue
                    new_history = history
                    valid = accepted
                    if 0 < step < len(word)-1:
                        new_history += str(a)
                        valid &= all(not new_history.endswith(w) or later > h
                                     for w, h in reversed_veto)
                    # Numerator terms encountered from the terminal end are
                    # 3^step times 2^(-sum of reverse increments) c(earlier).
                    mod = 3**len(word)
                    nxt = (value+3**step*pow(2, -offset-m, mod)*(4 >> earlier)) % mod
                    next_paths.append((earlier, offset+m, nxt, new_history, valid))
            paths = next_paths
        count = 0
        for a, b, c, d in product(paths, repeat=4):
            if a[4] and b[4] and (a[2]+b[2]-c[2]-d[2]) % mod == 0:
                count += 1
                if (4 >> a[0])+(4 >> b[0]) != (4 >> c[0])+(4 >> d[0]):
                    nonzero += 1
        estimates.append(count)
    return estimates, nonzero


def check():
    with patch.object(pressure, "MAX_LENGTH", 23):
        words, visits, states = pressure.forbidden_words()
    physical = pressure.actual_checks(words)
    machine = pressure.automaton(words)
    returns = schedules()
    toy = {"11": 0, "212": 1}
    short = ["2121", "21121", "22121"]
    matrices = pressure.execute([(0, pressure.automaton(toy), [w[1:-1] for w in short]),
                                 (1, machine, [w[1:-1] for w in returns])])
    require(len(matrices) == len(short)+len(returns) and all(len(m) == 9 for m in matrices),
            "all contracted matrices")
    fixtures = []
    for w, matrix in zip(short, matrices):
        left, right = endpoint_counts(int(w[0]), int(w[-1]))
        counts, carries = literal(w, toy)
        require(counts == contract(left, matrix, right) and carries > 0,
                "independent modular quartet and nonzero endpoint carry")
        fixtures.append({"reverse": w, "literal_counts": counts, "nonzero_carry": carries})
    record = []
    for w, matrix in zip(returns, matrices[len(short):]):
        left, right = endpoint_counts(int(w[0]), int(w[-1]))
        numerators = contract(left, matrix, right)
        require(max(numerators)*100 < 97*9*pressure.SCALE, "strict modular contraction")
        record.append({"length": len(w), "sha256": sha256(w.encode()).hexdigest(),
                       "entrance_counts": left, "earliest_counts": right,
                       "trimmed_scaled_matrix": matrix, "upper_numerators": numerators})
    require(97**100000 * 3**LIMIT < 100**100000, "per-letter bound")
    return {"anchor": str(ANCHOR), "context_length": 23, "states": states,
            "visits": visits, "forbidden_contexts": len(words), "actual_lifts": physical,
            "contexts_sha256": sha256("".join(f"{w} {k}\n" for w, k in sorted(words.items())).encode()).hexdigest(),
            "machine_states": len(machine[0]), "upper_denominator": 9*pressure.SCALE,
            "fixtures": fixtures, "returns": record, "per_edge_exponent": "99999/100000"}


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
