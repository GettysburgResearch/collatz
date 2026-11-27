"""Exact finite controls for the independent-product meeting bound."""

from collections import deque
from fractions import Fraction
from itertools import combinations, product
from math import gcd


if not __debug__:
    raise RuntimeError("The exact finite controls require Python assertions. Run without -O or -OO.")


def solve_linear(rows, rhs):
    size = len(rows)
    matrix = [list(map(Fraction, row)) + [Fraction(value)] for row, value in zip(rows, rhs)]
    for column in range(size):
        pivot = next(i for i in range(column, size) if matrix[i][column])
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        divisor = matrix[column][column]
        matrix[column] = [entry / divisor for entry in matrix[column]]
        for i in range(size):
            if i == column or not matrix[i][column]:
                continue
            factor = matrix[i][column]
            matrix[i] = [a - factor * b for a, b in zip(matrix[i], matrix[column])]
    return [row[-1] for row in matrix]


def closed_classes(table):
    reached = []
    for start in range(len(table)):
        seen = {start}
        todo = [start]
        while todo:
            for nxt in table[todo.pop()]:
                if nxt not in seen:
                    seen.add(nxt)
                    todo.append(nxt)
        reached.append(seen)
    classes = set()
    for state, seen in enumerate(reached):
        if all(state in reached[other] for other in seen):
            classes.add(tuple(sorted(seen)))
    return sorted(classes)


def check_class(table, vertices):
    base, size = len(table[0]), len(table)
    row = {v: {w: Fraction(table[v].count(w), base) for w in vertices} for v in vertices}
    root = vertices[0]
    distance = {root: 0}
    queue = deque([root])
    while queue:
        v = queue.popleft()
        for w in table[v]:
            if w not in distance:
                distance[w] = distance[v] + 1
                queue.append(w)
    period = 0
    for v in vertices:
        for w in table[v]:
            period = gcd(period, distance[v] + 1 - distance[w])
    assert period >= 1
    matrix = [[int(v == w) - row[v][w] for v in vertices] for w in vertices[:-1]]
    pi = dict(zip(vertices, solve_linear(matrix + [[1] * len(vertices)], [0] * len(matrix) + [1])))
    assert min(pi.values()) >= Fraction(1, size * base ** (size - 1))
    for phase in range(period):
        assert sum(pi[v] for v in vertices if distance[v] % period == phase) == Fraction(1, period)

    # Check the edge-hitting inequality independently by first-step equations.
    for target in vertices:
        rest = [v for v in vertices if v != target]
        rows = [[int(v == w) - row[v][w] for w in rest] for v in rest]
        hitting = dict(zip(rest, solve_linear(rows, [1] * len(rest))))
        for v in rest:
            if row[v][target]:
                assert hitting[v] <= 1 / (pi[v] * row[v][target])

    pairs = [(v, w) for v, w in product(vertices, repeat=2) if (distance[v] - distance[w]) % period == 0]
    mu = {(v, w): period * pi[v] * pi[w] for v, w in pairs}
    assert sum(mu.values()) == 1
    incoming = dict.fromkeys(pairs, Fraction(0))
    for (v, w), probability in mu.items():
        for a in set(table[v]):
            for b in set(table[w]):
                flow = probability * row[v][a] * row[w][b]
                assert flow >= Fraction(1, size ** 2 * base ** (2 * size))
                incoming[a, b] += flow
    assert incoming == mu

    # Equal-phase pair hitting times can be solved on unordered pairs by symmetry.
    live = [(v, w) for v, w in combinations(vertices, 2) if (v, w) in mu]
    rows = []
    for pair in live:
        v, w = pair
        rows.append([
            int(pair == (a, b)) - row[v][a] * row[w][b] - row[v][b] * row[w][a]
            for a, b in live
        ])
    hitting = solve_linear(rows, [1] * len(live))
    largest = max(hitting, default=Fraction(0))
    assert largest <= size ** 4 * base ** (2 * size)
    return period, len(live), largest


def main():
    count = classes = live_pairs = 0
    worst = Fraction(0)
    for size in (1, 2, 3):
        for digits in product(range(size), repeat=2 * size):
            table = [digits[i : i + 2] for i in range(0, len(digits), 2)]
            count += 1
            for cls in closed_classes(table):
                _, pairs, largest = check_class(table, cls)
                classes += 1
                live_pairs += pairs
                worst = max(worst, largest)
    print(f"binary tables={count} recurrent classes={classes} unordered live pairs={live_pairs} max mean={worst}")

    examples = {
        "periodic_four": [(2, 3), (2, 3), (0, 1), (0, 1)],
        "delayed_phase_eight": [(i + 1, i + 1) for i in range(7)] + [(0, 1)],
        "ternary_reset_five": [(0, 0, min(i + 1, 4)) for i in range(5)],
    }
    for name, table in examples.items():
        period, pairs, largest = check_class(table, tuple(range(len(table))))
        print(f"{name} period={period} unordered live pairs={pairs} max mean={largest}")


if __name__ == "__main__":
    main()
