#!/usr/bin/env python3
"""Independent positive-sum check of the finite spectral witnesses.

Only the author's tree producer is reused. Acceptance independently checks
the ordinary edges and uses root leakage + internal loss + external fibers,
rather than the author's cancellation formula. Infinite quantifiers remain
in the written proof. Every numerical comparison is rational.
"""

from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import runpy


def require(condition, message):
    if not condition:
        raise ValueError(message)


def replay(tree, k):
    root = ((1 << (3 ** (k - 1) + 1)) - 1) // 3
    require(tree["root"] == root, "incorrect explicit root")
    rows = tree["rows"]
    require(len(rows) == 512, "unexpected support size")
    states = {}
    gaps = {}
    for n, parent, depth in rows:
        require(all(type(x) is int for x in (n, parent, depth)), "integer row")
        require(n > 1 and n % 2 == 1 and depth >= 0, "ordinary domain")
        require(n not in states, "duplicate state")
        raw = 3 * n + 1
        gap = (raw & -raw).bit_length() - 1
        require(gap >= 1 and raw >> gap == parent, "literal edge failed")
        states[n] = (parent, depth)
        gaps[n] = gap
    require(states.get(root) == (1, 0), "root leakage must go to 1")
    for n, (parent, depth) in states.items():
        if n != root:
            require(parent in states, "missing internal parent")
            require(depth == states[parent][1] + 1, "depth does not decrease")
    return root, states, gaps


def full_column(target, s):
    if target % 3 == 0:
        return Fraction(0)
    first_gap = 2 if target % 3 == 1 else 1
    ratio = Fraction(1, 2 ** (4 * s))
    return Fraction(3 ** (2 * s), 2 ** (2 * s * first_gap)) / (1 - ratio)


def positive_residual(root, states, gaps, s):
    scale = 1 << 128
    mass_floor = 0
    # The scaled root contribution is exactly one.
    residual_floor = scale
    residual_upper = scale
    inside_columns = {n: Fraction(0) for n in states}
    for n, (parent, _) in states.items():
        if parent in states:
            inside_columns[parent] += Fraction(3, 2 ** gaps[n]) ** (2 * s)

    def enclose_positive(term):
        require(term >= 0, "negative contribution in positive decomposition")
        lower = (scale * term.numerator) // term.denominator
        return lower, lower + 1

    external_nonzero = 0
    for n in states:
        weight = Fraction(root, n) ** (2 * s)
        lower, _ = enclose_positive(weight)
        mass_floor += lower
        if n != root:
            loss = (1 - Fraction(3 * n, 3 * n + 1) ** s) ** 2 * weight
            lower, upper = enclose_positive(loss)
            residual_floor += lower
            residual_upper += upper
        outside = full_column(n, s) - inside_columns[n]
        external_nonzero += outside > 0
        lower, upper = enclose_positive(outside * weight)
        residual_floor += lower
        residual_upper += upper
    require(mass_floor > 0, "zero lower mass")
    return {
        "s": s,
        "squared_residual_lower": str(Fraction(residual_floor, mass_floor + len(states))),
        "squared_residual_upper": str(Fraction(residual_upper, mass_floor)),
        "nonzero_external_fiber_terms": external_nonzero,
    }


def main():
    producer = Path(__file__).with_name("check_ordinary_spectrum.py")
    require(
        sha256(producer.read_bytes()).hexdigest()
        == "395beaf29efeb7f66b88e346d04451e04b089cad63ee8b434c6ac9806feba0d4",
        "producer differs from the frozen reviewed bytes",
    )
    build = runpy.run_path(str(producer))["build_tree"]
    bounds = {
        (6, 1): Fraction(93, 1000), (6, 2): Fraction(16, 1000),
        (8, 1): Fraction(41, 1000), (8, 2): Fraction(31, 10000),
    }
    cases = []
    for k in (6, 8):
        root, states, gaps = replay(build(k, 512), k)
        support = "".join(
            f"{n:x}:{parent:x}:{depth}\n"
            for n, (parent, depth) in sorted(states.items())
        )
        for s in (1, 2):
            result = positive_residual(root, states, gaps, s)
            bound = bounds[k, s]
            require(Fraction(result["squared_residual_upper"]) < bound ** 2,
                    "independent rational residual bound failed")
            result.update({
                "k": k,
                "states": len(states),
                "support_sha256": sha256(support.encode("ascii")).hexdigest(),
                "strict_norm_bound": str(bound),
                "all_unit_complex_phases": True,
            })
            cases.append(result)
    print(json.dumps({
        "status": "PASS",
        "method": "positive root/internal/external decomposition with outward rational bounds",
        "producer_reuse": "only build_tree; no author verification or residual routine is called",
        "scope": "finite ordinary convergent supports only; no Collatz closure",
        "cases": cases,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
