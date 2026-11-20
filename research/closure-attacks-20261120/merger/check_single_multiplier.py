#!/usr/bin/env python3
"""Exact all-lift checking of M5-002; M5 calls remain explicit assumptions."""

from collections import Counter
import json


MODULUS = 480


def require(condition, message):
    if not condition:
        raise ValueError(message)


def add(x, c):
    return x[0], x[1] + c


def mul(x, c):
    return c * x[0], c * x[1]


def div(x, c):
    require(x[0] % c == 0 and x[1] % c == 0, ("nonintegral", x, c))
    return x[0] // c, x[1] // c


def value(x, k):
    return x[0] * k + x[1]


def residue(x, m):
    require(x[0] % m == 0, ("variable residue", x, m))
    return x[1] % m


class Path:
    def __init__(self, r):
        require(r % 3 != 0, ("source not a unit", r))
        self.source = MODULUS, r
        self.current = self.source
        self.minimum = 1 if r == 1 else 0
        self.vertices = [self.source]
        self.queries = []
        self.steps = []

    def legal(self, x):
        require(x[0] >= 0 and value(x, self.minimum) > 0, ("nonpositive", x))
        require(residue(x, 3) != 0, ("nonunit", x))

    def edge(self, kind, y):
        x = self.current
        self.legal(x)
        self.legal(y)
        if kind == "half":
            require(x == mul(y, 2), (kind, x, y))
        elif kind == "odd":
            require(residue(x, 2) == 1, (kind, x))
            require(mul(y, 2) == add(mul(x, 3), 1), (kind, x, y))
        elif kind == "odd_inverse":
            require(residue(y, 2) == 1, (kind, y))
            require(mul(x, 2) == add(mul(y, 3), 1), (kind, x, y))
        elif kind == "M5":
            if y == mul(x, 5):
                base = x
            else:
                require(x == mul(y, 5), (kind, x, y))
                base = y
            self.legal(base)
            self.queries.append(base)
        else:
            raise ValueError(("unknown edge", kind))
        self.steps.append(kind)
        self.current = y
        self.vertices.append(y)

    def half(self):
        self.edge("half", div(self.current, 2))

    def odd(self):
        self.edge("odd", div(add(mul(self.current, 3), 1), 2))

    def divide_five(self):
        self.edge("M5", div(self.current, 5))

    def c5(self):
        n = self.current
        require(residue(n, 4) == 3, ("C5 domain", n))
        self.edge("M5", mul(n, 5))
        self.odd()
        self.odd()
        self.divide_five()
        require(self.current == div(add(mul(n, 9), 1), 4), ("C5 output", n))

    def bounded(self, x, multiple, offset=0):
        difference = add(self.source, 0)
        difference = multiple * difference[0] - x[0], multiple * difference[1] + offset - x[1]
        require(difference[0] >= 0 and value(difference, self.minimum) >= 0,
                ("failed height bound", self.source, x, multiple, offset))

    def finish(self, branch):
        n, q = self.source, self.current
        difference = n[0] - q[0], n[1] - q[1]
        require(difference[0] >= 0 and value(difference, self.minimum) >= 1,
                ("not strictly decreasing", n, q))
        self.bounded(mul(q, 32), 27, 23)
        require(len(self.queries) <= 3, ("too many queries", n, self.queries))
        for query in self.queries:
            self.bounded(query, 3)
        for vertex in self.vertices:
            self.bounded(vertex, 15)
        return {"residue": n[1], "branch": branch, "output": q,
                "M5_queries": self.queries, "ordinary_edges":
                sum(step != "M5" for step in self.steps)}


def certificate(r):
    path = Path(r)
    if r % 2 == 0:
        path.half()
        return path.finish("even")
    if r % 5 == 0:
        path.divide_five()
        return path.finish("five")
    if r % 4 == 1:
        path.odd()
        path.half()
        return path.finish("one_mod_four")
    if r % 8 == 7:
        path.c5()
        path.half()
        path.edge("odd_inverse", div(add(mul(path.current, 2), -1), 3))
        return path.finish("seven_mod_eight")
    require(r % 8 == 3, ("uncovered binary case", r))
    if r % 5 == 3:
        path.odd()
        path.divide_five()
        return path.finish("three_mod_five")
    if r % 5 == 1:
        path.c5()
        path.divide_five()
        return path.finish("one_mod_five")
    if r % 5 == 4:
        path.c5()
        path.odd()
        path.divide_five()
        return path.finish("four_mod_five")
    require(r % 5 == 2, ("uncovered quinary case", r))
    path.odd()
    path.odd()
    path.half()
    v = path.current
    require(residue(v, 15) == 1, ("last-unit class", v))
    if residue(v, 2) == 0:
        path.half()
        return path.finish("last_even")
    if residue(v, 4) == 1:
        path.odd()
        path.half()
        return path.finish("last_one_mod_four")
    require(residue(v, 4) == 3, ("uncovered final parity", v))
    path.c5()
    path.divide_five()
    return path.finish("last_three_mod_four")


def main():
    rows = [certificate(r) for r in range(MODULUS) if r % 3]
    require(len(rows) == 320, "cell count")
    # Explicitly preserve the larger-query failure of numeric query induction.
    n, p = (40, 11), (90, 25)
    require(p[0] > n[0] and p[1] > n[1], "missing growing query control")
    require(p == div(add(mul(n, 9), 1), 4), "growing-query identity")
    report = {
        "status": "PASS",
        "normalization": "positive shortcut Collatz; independent merger clocks",
        "scope": "exact affine all-lift verification; M5 is an unproved supplied law",
        "modulus": MODULUS,
        "ternary_unit_cells": len(rows),
        "branch_counts": dict(sorted(Counter(row["branch"] for row in rows).items())),
        "max_M5_calls_per_stage": max(len(row["M5_queries"]) for row in rows),
        "query_height_bound": "3*n",
        "abstract_path_vertex_bound": "15*n",
        "descent_bound": "q <= (27*n+23)/32 < n",
        "growing_query_control": "n=40*k+11 in U requires p=90*k+25 > n in this path",
        "unproved": "actual M5(x) merger certificates for every fixed odd ternary unit x",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
