#!/usr/bin/env python3
"""Check all-input certificates for CR-002 as exact affine identities.

The input in cell r is n = 480*k+r, with k >= 0, except r=1 uses
k >= 1 because n=1 is the induction base. No Collatz orbit census is used.
"""

from collections import Counter
import json


if not __debug__:
    raise SystemExit("Run without -O: certificate checks require assertions.")


MODULUS = 480


def add(x, value):
    return x[0], x[1] + value


def mul(x, value):
    return x[0] * value, x[1] * value


def exact_div(x, value):
    assert x[0] % value == 0 and x[1] % value == 0, (x, value)
    return x[0] // value, x[1] // value


def residue(x, modulus):
    assert x[0] % modulus == 0, (x, modulus)
    return x[1] % modulus


def at(x, k):
    return x[0] * k + x[1]


class Certificate:
    def __init__(self, r):
        self.source = (MODULUS, r)
        self.k_min = 1 if r == 1 else 0
        self.current = self.source
        self.steps = []

    def positive(self, x):
        assert x[0] >= 0 and at(x, self.k_min) >= 1, x

    def edge(self, law, x, y):
        assert x == self.current
        self.positive(x)
        self.positive(y)
        if law.startswith("A"):
            p = int(law[1:])
            assert p in (2, 3, 5)
            assert x == mul(y, p) or y == mul(x, p)
        else:
            scale = {"B": 3, "C": 9, "D": 15}[law]
            if y == add(mul(x, scale), 1):
                base = x
            else:
                assert x == add(mul(y, scale), 1)
                base = y
            assert residue(base, 2) == 1
            if law == "B":
                assert residue(base, 3) in (1, 2)
            if law == "C":
                assert residue(base, 4) == 3
        self.steps.append((law, x, y))
        self.current = y
        return y

    def scale(self, p):
        return self.edge(f"A{p}", self.current, mul(self.current, p))

    def divide(self, divisor):
        for p in (2, 3, 5):
            while divisor % p == 0:
                self.edge(f"A{p}", self.current, exact_div(self.current, p))
                divisor //= p
        assert divisor == 1
        return self.current

    def forward(self, law):
        scale = {"B": 3, "C": 9, "D": 15}[law]
        return self.edge(law, self.current, add(mul(self.current, scale), 1))

    def backward(self, law):
        scale = {"B": 3, "C": 9, "D": 15}[law]
        return self.edge(law, self.current, exact_div(add(self.current, -1), scale))

    def finish(self, branch):
        n, q = self.source, self.current
        # Both linear coefficients and the minimum allowed k prove each
        # inequality for every later integer k, not just for a sample.
        assert n[0] - q[0] >= 0
        assert at(n, self.k_min) - at(q, self.k_min) >= 1
        bound = (27 * n[0] - 32 * q[0], 27 * n[1] + 23 - 32 * q[1])
        assert bound[0] >= 0 and at(bound, self.k_min) >= 0
        self.positive(q)
        return branch


def build(r):
    c = Certificate(r)
    n = c.source
    for p in (2, 3, 5):
        if residue(n, p) == 0:
            c.divide(p)
            return c, c.finish(f"factor_{p}")

    assert residue(n, 2) == 1 and residue(n, 3) != 0 and residue(n, 5) != 0
    if residue(n, 4) == 1:
        c.forward("B")
        c.divide(4)
        return c, c.finish("one_mod_four")

    if residue(n, 8) == 7:
        c.forward("C")
        c.divide(4)
        c.backward("B")
        return c, c.finish("seven_mod_eight")

    assert residue(n, 8) == 3
    if residue(n, 5) == 3:
        c.forward("B")
        c.divide(10)
        return c, c.finish("three_mod_five")

    if residue(n, 5) == 1:
        c.forward("C")
        c.divide(20)
        return c, c.finish("one_mod_five")

    if residue(n, 5) == 4:
        c.forward("C")
        p = c.divide(4)
        assert residue(p, 2) == 1 and residue(p, 3) != 0 and residue(p, 5) == 3
        c.forward("B")
        c.divide(10)
        return c, c.finish("four_mod_five")

    assert residue(n, 5) == 2
    if residue(n, 3) == 2:
        for _ in range(3):
            c.scale(2)
        c.backward("D")
        return c, c.finish("inverse_fifteen")

    assert residue(n, 120) == 67
    c.forward("B")
    u = c.divide(2)
    assert residue(u, 4) == 1 and residue(u, 3) != 0
    c.forward("B")
    v = c.divide(4)
    assert residue(v, 15) == 1
    if residue(v, 2) == 0:
        c.divide(2)
        return c, c.finish("last_even")
    if residue(v, 4) == 1:
        c.forward("B")
        c.divide(4)
        return c, c.finish("last_one_mod_four")
    assert residue(v, 4) == 3
    c.forward("C")
    c.divide(20)
    return c, c.finish("last_three_mod_four")


def main():
    branches = Counter()
    laws = Counter()
    max_steps = 0
    for r in range(1, MODULUS + 1):
        certificate, branch = build(r)
        branches[branch] += 1
        laws.update(law for law, _, _ in certificate.steps)
        max_steps = max(max_steps, len(certificate.steps))
    assert sum(branches.values()) == MODULUS
    print(json.dumps({
        "status": "PASS",
        "claim": "CR-002 conditional arithmetic rigidity",
        "symbolic_residue_cells": MODULUS,
        "ordinary_input_coverage": "Every n>1; unrestricted positive affine lifts",
        "maximum_primitive_law_applications_per_reduction": max_steps,
        "strict_descent_and_uniform_bound": True,
        "branch_cell_counts": dict(sorted(branches.items())),
        "primitive_law_counts": dict(sorted(laws.items())),
        "proves_restricted_merger_hypothesis_E": False,
        "proves_unconditional_Collatz": False,
    }, indent=2))


if __name__ == "__main__":
    main()
