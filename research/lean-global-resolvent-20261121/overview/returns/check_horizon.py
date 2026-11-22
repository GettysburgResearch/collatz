"""Exact finite control for the checkpoint 13 whole-source debt attempt.

This checks integer arithmetic, not the universal FloorIntervalStep.
Canonical words omit terminal gap-2 padding at the fixed odd state 1.
"""

from collections import deque
import json


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def grade(e, word):
    return tuple(sorted(([2 * e + 1] if e else []) + [2 * a for a in word], reverse=True))


def path(n, clock):
    values = [n]
    for _ in range(clock):
        values.append(step(values[-1]))
    return values


# Every complete word with exactly one gap 4 consists of a <=3 inverse
# path from 5, then the gap 4 to 1, then optional terminal gap-2 padding.
# Explicit closure of this small inverse cluster proves enumeration complete.
words = {5: (4,)}
queue = deque([5])
edges = {}
while queue:
    n = queue.popleft()
    edges[n] = []
    for a in range(1, 4):
        numerator = (1 << a) * n - 1
        if numerator % 3 == 0:
            predecessor = numerator // 3
            assert predecessor > 0 and predecessor % 2 == 1
            edges[n].append((a, predecessor))
            if predecessor not in words:
                words[predecessor] = (a,) + words[n]
                queue.append(predecessor)
assert set(words) == {3, 5, 7, 9, 11, 13, 17, 19, 25, 29, 33, 45, 51, 77, 205, 273}

t, q, e = 3711, 273, 3
word = words[q]
assert word == (2, 3, 3, 3, 1, 2, 3, 4)
A, S, G = sum(word), q << e, grade(e, word)
sources = [(1 << k, grade(k, ())) for k in range(4)]
sources += [(n << k, grade(k, w)) for n, w in words.items() for k in range(4)]
assert max(n for n, g in sources if g < G) == 1640
assert max(n for n, g in sources if g <= G) == S == 2184
assert S + 1 < t <= 2 * S + 1
assert 1105 < t and t % 4 == 3 and 2 * A < t
assert all(3 ** i < 2 ** sum(word[:i]) for i in range(1, len(word) + 1))

source = path(q, A)
powered_source = path(S, e + A)
target = path(t, e + A)
assert source[-1] == powered_source[-1] == 1
assert max(powered_source[1:]) <= (t - 1) // 2
assert min(target) == t
assert target[A] == 76196

source_odds = target_odds = 0
debt = []
for j in range(A + 1):
    assert target_odds >= source_odds
    c = 3 ** (target_odds - source_odds)
    debt.append((j, c, target[j] - c * source[j]))
    if j < A:
        source_odds += source[j] % 2
        target_odds += target[j] % 2

value, first_descent = t, 0
while value >= t:
    value = step(value)
    first_descent += 1
assert (first_descent, value) == (37, 2543)

print(json.dumps({
    "target": t, "source": S, "odd_source": q, "initial_halvings": e,
    "word": word, "grade": G, "odd_source_clock": A,
    "powered_source_clock": e + A, "lower_grade_maximum": 1640,
    "target_at_source_clock": target[A], "target_at_powered_source_clock": target[e + A],
    "first_descent_clock": first_descent, "first_descent_value": value,
    "source_odd_count": source_odds, "target_odd_count": target_odds,
    "terminal_multiplier": debt[-1][1], "terminal_debt": debt[-1][2],
    "one_four_inverse_edges": edges,
    "status": "Finite horizon control only; not a counterexample to FloorIntervalStep."
}, indent=2))
