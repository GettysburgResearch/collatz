#!/usr/bin/env python3
"""Exact finite checks for ORDINARY_ESSENTIAL_SPECTRUM.md.

No orbit-convergence oracle and no floating-point acceptance are used.
The producer enumerates inverse trees. The verifier independently replays
each ordinary forward edge and includes every off-support predecessor via
the exact column sums. The theorem's infinite quantifiers remain written
proofs, not claims of this finite script.
"""

from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from heapq import heappop, heappush
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, minimum: int, label: str) -> None:
    require(type(value) is int and value >= minimum, label)


def odd_step(n: int) -> tuple[int, int]:
    integer(n, 1, "positive integer state required")
    require(n % 2 == 1, "odd state required")
    t = 3 * n + 1
    a = 0
    while t % 2 == 0:
        t //= 2
        a += 1
    return t, a


def root_data(k: int) -> tuple[int, int, int, int]:
    integer(k, 2, "root parameter k>=2 required")
    h = 3 ** (k - 1)
    numerator = (1 << h) + 1
    require(numerator % (3**k) == 0, "root LTE divisibility")
    m = numerator // (3**k)
    n = (1 << k) * m - 1
    root = 2 * 3 ** (k - 1) * m - 1
    require(root == ((1 << (h + 1)) - 1) // 3, "root formulas differ")
    return h, m, n, root


def build_tree(k: int, count: int) -> dict:
    """Producer: lowest currently undiscovered inverse vertex first."""
    integer(count, 1, "nonempty finite tree required")
    _, _, _, root = root_data(k)
    rows = [(root, 1, 0)]
    depth = {root: 0}
    queue: list[tuple[int, int, int]] = []

    def first_child(parent: int) -> None:
        if parent % 3:
            gap = 2 if parent % 3 == 1 else 1
            child = ((1 << gap) * parent - 1) // 3
            heappush(queue, (child, parent, gap))

    first_child(root)
    while len(rows) < count:
        require(bool(queue), "unexpected exhausted inverse tree")
        child, parent, gap = heappop(queue)
        require(child not in depth, "producer duplicated a vertex")
        depth[child] = depth[parent] + 1
        rows.append((child, parent, depth[child]))
        gap += 2
        sibling = ((1 << gap) * parent - 1) // 3
        heappush(queue, (sibling, parent, gap))
        first_child(child)
    return {"k": k, "root": root, "rows": rows}


def verify_tree(tree: dict) -> dict[int, tuple[int, int]]:
    """Verifier: recompute all parents with raw 3n+1 and division by 2."""
    require(type(tree) is dict, "tree object required")
    integer(tree.get("k"), 2, "invalid root parameter")
    integer(tree.get("root"), 1, "invalid root")
    _, _, _, expected = root_data(tree["k"])
    require(tree["root"] == expected, "root does not match parameter")
    rows = tree.get("rows")
    require(type(rows) is list and len(rows) > 0, "empty support")
    states: dict[int, tuple[int, int]] = {}
    for row in rows:
        require(type(row) in (list, tuple) and len(row) == 3, "bad row")
        n, parent, depth = row
        integer(n, 1, "bad vertex")
        integer(parent, 1, "bad parent")
        integer(depth, 0, "bad depth")
        require(n % 2 == 1 and parent % 2 == 1, "even vertex or parent")
        require(n not in states, "duplicate vertex")
        states[n] = (parent, depth)
    root = tree["root"]
    require(root in states, "root missing from support")
    require(states[root] == (1, 0), "bad root depth or parent")
    require(1 not in states, "support includes absorbing cycle state")
    for n, (parent, depth) in states.items():
        image, _ = odd_step(n)
        require(image == parent, "wrong ordinary parent")
        if n == root:
            require(image == 1, "root fails immediate convergence")
        else:
            require(parent in states, "support is not forward closed")
            require(depth == states[parent][1] + 1, "wrong first-hit depth")
    return states


def column(n: int, s: int) -> Fraction:
    integer(s, 1, "positive operator exponent required")
    require(s in (1, 2), "only s=1,2 are certified")
    if n % 3 == 0:
        return Fraction(0)
    # Derived independently as a geometric series over the legal parity.
    a0 = 2 if n % 3 == 1 else 1
    first = Fraction(3 ** (2 * s), 2 ** (2 * s * a0))
    return first / (1 - Fraction(1, 2 ** (4 * s)))


def residual_enclosure(tree: dict, s: int, precision: int = 128) -> dict:
    states = verify_tree(tree)
    integer(precision, 32, "precision too small")
    integer(s, 1, "invalid operator exponent")
    require(s in (1, 2), "unsupported operator exponent")
    scale = 1 << precision
    root_power = tree["root"] ** (2 * s)
    mass_floor = column_floor = cross_floor = 0
    for n, (_, depth) in states.items():
        denominator = n ** (2 * s)
        mass_floor += (scale * root_power) // denominator
        z = column(n, s)
        column_floor += (scale * root_power * z.numerator) // (
            z.denominator * denominator
        )
        if depth:
            # c(n)^s*(root/n)^(2s), after exact cancellation.
            cross_floor += (scale * root_power * 3**s) // (
                n**s * (3 * n + 1) ** s
            )
    count = len(states)
    # Every floor is <= its summand < floor+1. C+M-2E is the
    # full infinite residual, including all off-support predecessors.
    numerator_upper = column_floor + mass_floor + 2 * count - 2 * cross_floor
    numerator_lower = max(
        0, column_floor + mass_floor - 2 * (cross_floor + count - 1)
    )
    require(mass_floor > 0 and numerator_upper >= 0, "invalid norm interval")
    return {
        "s": s,
        "precision_bits": precision,
        "squared_lower_numerator": str(numerator_lower),
        "squared_lower_denominator": str(mass_floor + count),
        "squared_upper_numerator": str(numerator_upper),
        "squared_upper_denominator": str(mass_floor),
    }


def prove_norm_bound(interval: dict, bound: Fraction) -> None:
    require(bound > 0, "positive norm bound required")
    numerator = int(interval["squared_upper_numerator"])
    denominator = int(interval["squared_upper_denominator"])
    require(
        numerator * bound.denominator**2 < denominator * bound.numerator**2,
        "claimed rational norm bound failed",
    )


def support_digest(tree: dict) -> str:
    lines = (
        f"{n:x}:{parent:x}:{depth}\n"
        for n, parent, depth in sorted(tree["rows"])
    )
    return sha256("".join(lines).encode("ascii")).hexdigest()


def check_root_arithmetic() -> dict:
    edges = 0
    previous = 0
    for k in range(2, 11):
        h, m, n, root = root_data(k)
        require(m % 2 == 1 and m % 3 == 1, "wrong root quotient units")
        require(root > previous, "roots not distinct")
        previous = root
        state = n
        for j in range(k - 1):
            expected = 2 ** (k - j) * 3**j * m - 1
            require(state == expected, "spine formula mismatch")
            state, gap = odd_step(state)
            require(gap == 1, "spine valuation is not one")
            edges += 1
        require(state == root, "spine missed its root")
        image, gap = odd_step(root)
        require(image == 1 and gap == h + 1, "root does not hit one")
        require(n * 3 ** (k - 1) < root * 2 ** (k - 1), "ratio bound")
        edges += 1
    return {"root_parameters": [2, 10], "exact_edges": edges}


def check_small_full_residual() -> dict:
    # This known two-state tree gives a short rational certificate whose
    # external predecessor contribution is too large to silently omit.
    tree = {"k": 2, "root": 5, "rows": [(5, 1, 0), (3, 5, 1)]}
    states = verify_tree(tree)
    ratios = []
    for s in (1, 2):
        mass = sum((Fraction(1, n ** (2 * s)) for n in states), Fraction(0))
        full = sum(
            ((1 + column(n, s)) * Fraction(1, n ** (2 * s)) for n in states),
            Fraction(0),
        )
        for n, (_, depth) in states.items():
            if depth:
                full -= 2 * Fraction(3 * n, 3 * n + 1) ** s / n ** (2 * s)
        ratio = full / mass
        if s == 1:
            require(ratio == Fraction(53, 170), "tiny full-column certificate")
        interval = residual_enclosure(tree, s)
        lower = Fraction(
            int(interval["squared_lower_numerator"]),
            int(interval["squared_lower_denominator"]),
        )
        upper = Fraction(
            int(interval["squared_upper_numerator"]),
            int(interval["squared_upper_denominator"]),
        )
        require(lower <= ratio <= upper, "outward interval misses exact ratio")
        ratios.append({"s": s, "squared_ratio": str(ratio)})
    return {"support": [3, 5], "exact_squared_ratios": ratios}


def check_smoothing_arithmetic() -> dict:
    cases = 0
    for k in range(4, 21):
        n = (4**k - 1) // 3
        m = n + 2
        tn, tm = n, m
        rn = rm = Fraction(1)
        for q in range(k):
            if q:
                require(
                    rn == Fraction(4**k - 1, 4**k) * Fraction(3, 4) ** (q - 1),
                    "one-hit product mismatch",
                )
            if q >= 3:
                require(tm == 3 ** (q - 1) * 4 ** (k - q) + 1, "nearby path formula")
                require(
                    rm == Fraction(4**k + 5, 1) / (4**k + 3 * Fraction(4, 3) ** q),
                    "nearby finite product mismatch",
                )
            cases += 1
            rn *= Fraction(3 * tn, 3 * tn + 1)
            rm *= Fraction(3 * tm, 3 * tm + 1)
            tn, _ = odd_step(tn)
            tm, _ = odd_step(tm)
    for z in (Fraction(1, 2), Fraction(3, 4), Fraction(7, 8), Fraction(15, 16)):
        left = 1 - (1 - z) * (1 + z / (1 - 3 * z / 4))
        require(left == z * z / (4 - 3 * z), "Abel oscillation algebra")
    return {"finite_product_pairs": cases, "Abel_parameters": 4}


def check_compact_constants() -> dict:
    require(16 < 255, "K1 residue-one tail")
    require(1600 < 9 * 255, "K1 residue-two tail")
    require(32**2 < 9 * 4095, "K2 residue-one tail")
    require(1600**2 < 27**2 * 4095, "K2 residue-two tail")
    for s, expected in ((1, (Fraction(3, 5), Fraction(12, 5))),
                        (2, (Fraction(27, 85), Fraction(432, 85)))):
        require(column(1, s) == expected[0], "column residue one")
        require(column(5, s) == expected[1], "column residue two")
        require(column(3, s) == 0, "nonunit target column")
    return {"global_tail_constant_squared_checks": 4, "full_columns": 6}


def check_negative_controls(tree: dict) -> list[str]:
    controls = []

    def rejected(name, operation):
        try:
            operation()
        except ValueError:
            controls.append(name)
        else:
            raise ValueError("negative control accepted: " + name)

    bad = deepcopy(tree)
    bad["rows"].append(bad["rows"][0])
    rejected("duplicate vertex", lambda: verify_tree(bad))
    bad = deepcopy(tree)
    n, parent, depth = bad["rows"][1]
    bad["rows"][1] = (n, parent + 2, depth)
    rejected("false ordinary parent", lambda: verify_tree(bad))
    bad = deepcopy(tree)
    n, parent, depth = bad["rows"][1]
    bad["rows"][1] = (n, parent, depth + 1)
    rejected("incorrect phase depth", lambda: verify_tree(bad))
    bad = deepcopy(tree)
    bad["rows"] = bad["rows"][1:]
    rejected("missing root", lambda: verify_tree(bad))
    bad = deepcopy(tree)
    bad["rows"] = []
    rejected("empty support", lambda: verify_tree(bad))
    bad = deepcopy(tree)
    n, parent, depth = bad["rows"][1]
    bad["rows"][1] = (n + 1, parent, depth)
    rejected("even state", lambda: verify_tree(bad))
    rejected("unsupported operator exponent", lambda: residual_enclosure(tree, 3))
    rejected("Boolean root parameter", lambda: root_data(True))
    return controls


def main() -> None:
    witnesses = []
    tree_for_controls = None
    bounds = {
        (6, 1): Fraction(93, 1000), (6, 2): Fraction(16, 1000),
        (8, 1): Fraction(41, 1000), (8, 2): Fraction(31, 10000),
    }
    for k in (6, 8):
        tree = build_tree(k, 512)
        states = verify_tree(tree)
        record = {
            "k": k, "vertices": len(states),
            "algorithm": "least-discovered-inverse-vertex-v1",
            "root_bit_length": tree["root"].bit_length(),
            "max_depth": max(depth for _, depth in states.values()),
            "support_sha256": support_digest(tree),
            "all_unit_complex_phases": True,
            "residual_certificates": [],
        }
        for s in (1, 2):
            interval = residual_enclosure(tree, s)
            bound = bounds[k, s]
            prove_norm_bound(interval, bound)
            interval["strict_norm_upper_bound"] = str(bound)
            record["residual_certificates"].append(interval)
        witnesses.append(record)
        tree_for_controls = tree
    report = {
        "status": "PASS finite exact certificate checks; no Collatz closure",
        "root_arithmetic": check_root_arithmetic(),
        "compact_comparison": check_compact_constants(),
        "small_full_residual": check_small_full_residual(),
        "witnesses": witnesses,
        "smoothing_boundary": check_smoothing_arithmetic(),
        "rejected_controls": check_negative_controls(tree_for_controls),
        "limits": [
            "The infinite essential-spectrum statement uses the written proof.",
            "All certified support vertices reach1; no escape is inferred.",
            "No all-clock D_q upper bound or extra-cycle exclusion is proved.",
        ],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
