#!/usr/bin/env python3
"""Independent exact finite checks for the affine-section proof packet.

No imported author modules, floating arithmetic, random simulation, or
assert statements are used. The unbounded recurrence and expectation
claims are proved in the notes, not certified by this finite grid.
"""

from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


class CheckFailure(RuntimeError):
    pass


def need(condition, message):
    if not condition:
        raise CheckFailure(message)


def shortcut(n):
    need(isinstance(n, int) and n > 0, "positive ordinary input required")
    return (3 * n + 1) // 2 if n % 2 else n // 2


def parity(q):
    q = Q(q)
    need(q.denominator % 2 == 1, "binary parity requires odd denominator")
    return q.numerator % 2


def slope(k):
    return 5 * Q(3) ** k


def lattice(k, c):
    return (Q(c) * 3 ** max(0, -k)).denominator == 1


def section_step(k, c, epsilon):
    need(epsilon in (0, 1) and lattice(k, c), "invalid section input")
    eta = (epsilon + parity(c)) % 2
    next_k = k + eta - epsilon
    next_c = (3 ** eta * c + eta - slope(next_k) * epsilon) / 2
    need(lattice(next_k, next_c), "lattice preservation failed")
    return next_k, next_c, eta


def normalized_step(k, D, epsilon):
    need(isinstance(D, int) and epsilon in (0, 1), "invalid normalized state")
    eta = (epsilon + D) % 2
    t = k + eta - epsilon
    exponent = max(-t, 0) + eta - max(-k, 0)
    need(exponent >= 0, "negative exponent in normalized update")
    numerator = (3 ** exponent * D + 3 ** max(-t, 0) * eta
                 - 5 * 3 ** max(t, 0) * epsilon)
    need(numerator % 2 == 0, "nonintegral normalized update")
    return t, numerator // 2


def valuation_two(q):
    q = Q(q)
    if not q:
        return None
    n = abs(q.numerator)
    d = q.denominator
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    while d % 2 == 0:
        d //= 2
        v -= 1
    return v


def root_control(k, D):
    """Reconstruct PR146's integer-state control, independently."""
    bits = []

    def bit(epsilon):
        nonlocal k, D
        k, D = normalized_step(k, D, epsilon)
        bits.append(epsilon)
        need(len(bits) < 10000, "finite grid control unexpectedly long")

    original_level = abs(k)
    while k:
        old_level = abs(k)
        start = len(bits)
        if D % 2 == 0:
            v = valuation_two(D)
            vc = 1 if k % 2 else 2
            if v is None or v > vc:
                bit(1)
            while D % 2 == 0:
                bit(0)
        bit(1 if k > 0 else 0)
        need(abs(k) == old_level - 1, "control failed to lower level")
        need(len(bits) - start <= 3, "level control exceeded three bits")
    need(len(bits) <= 3 * original_level, "level-removal bound failed")

    while D:
        old_D = D
        if D % 2 == 0:
            bit(0)
        elif D == -3:
            for epsilon in (1, 1, 0, 1, 0, 0, 0):
                bit(epsilon)
        else:
            bit(1)
            need(k == -1 and D != 0, "zero-level excursion entry failed")
            while D % 2 == 0:
                bit(0)
            bit(0)
        need(k == 0, "offset control did not return to level zero")
        need(abs(D) < abs(old_D), "offset control failed strict descent")
    return bits


def ordinary_checks():
    h = 12
    vectors = set()
    transitions = 0
    for n in range(1, 2 ** h + 1):
        x, y = n, 5 * n
        k, c = 0, Q(0)
        vector = []
        for _ in range(h):
            epsilon = x % 2
            vector.append(epsilon)
            next_k, next_c, eta = section_step(k, c, epsilon)
            need(eta == y % 2, "target parity mismatch")
            x, y = shortcut(x), shortcut(y)
            need(y == slope(next_k) * x + next_c, "ordinary affine identity failed")
            k, c = next_k, next_c
            transitions += 1
        vectors.add(tuple(vector))
    need(len(vectors) == 2 ** h, "finite parity/residue bijection failed")
    return {"prefix_length": h, "ordinary_sources": 2 ** h,
            "literal_paired_transitions": transitions,
            "distinct_source_parity_vectors": len(vectors)}


def section_grid_checks():
    states = 0
    paths = 0
    transitions = 0
    min_variance = None
    longest_control = 0
    for k in range(-12, 13):
        need(valuation_two(slope(k) - 1) == (1 if k % 2 else 2),
             "slope valuation identity failed")
        for m in range(-48, 49):
            c = Q(m, 3 ** max(0, -k))
            states += 1
            need(lattice(k, c), "grid state outside lattice")
            deltas = []
            for bits in product((0, 1), repeat=3):
                current_k, current_c = k, c
                for epsilon in bits:
                    old_lambda = slope(current_k)
                    next_k, next_c, eta = section_step(current_k, current_c, epsilon)
                    new_lambda = slope(next_k)
                    old_D = current_c * 3 ** max(-current_k, 0)
                    need(old_D.denominator == 1, "normalized grid offset not integer")
                    nk, nD = normalized_step(current_k, int(old_D), epsilon)
                    need(nk == next_k and nD == next_c * 3 ** max(-next_k, 0),
                         "two independently implemented updates disagree")
                    A = Q(3 ** eta) * (1 + old_lambda) / (2 * (1 + new_lambda))
                    need(Q(1, 2) <= A <= Q(3, 2), "carry multiplier out of range")
                    r = abs(current_c) / (1 + old_lambda)
                    next_r = abs(next_c) / (1 + new_lambda)
                    need(next_r <= A * r + Q(1, 2), "fractional carry precursor failed")
                    if parity(current_c):
                        a0 = 3 * (1 + old_lambda) / (2 * (1 + 3 * old_lambda))
                        a1 = 3 * (1 + old_lambda) / (2 * (3 + old_lambda))
                        need(1 / a0 + 1 / a1 == Q(8, 3), "reciprocal-sum identity failed")
                    current_k, current_c = next_k, next_c
                    transitions += 1
                deltas.append(current_k - k)
                paths += 1
            need(sum(deltas) == 0, "three-step martingale mean failed")
            need(max(map(abs, deltas)) <= 3, "three-step increment bound failed")
            variance = sum(Q(delta * delta, 8) for delta in deltas)
            need(variance >= Q(1, 4), "uniform three-step variance failed")
            min_variance = variance if min_variance is None else min(min_variance, variance)

            bits = root_control(k, m)
            check_k, check_c = k, c
            for epsilon in bits:
                check_k, check_c, _ = section_step(check_k, check_c, epsilon)
            need((check_k, check_c) == (0, 0), "root control did not reach the root")
            longest_control = max(longest_control, len(bits))
    return {"states": states, "three_bit_paths": paths,
            "checked_state_transitions": transitions,
            "minimum_three_step_variance": str(min_variance),
            "independent_root_controls": states,
            "maximum_control_length_in_grid": longest_control}


def constant_checks():
    checks = 0

    def exact(condition, message):
        nonlocal checks
        need(condition, message)
        checks += 1

    # rho^2=(2+sqrt(3))/4; all squared quantities are positive.
    threshold = 4 * Q(97, 100) ** 2 - 2
    exact(threshold > 0 and threshold ** 2 > 3, "rho < 97/100 failed")
    exact(Q(71, 100) ** 2 > Q(1, 2), "sqrt additive constant failed")
    M = Q(1000, 997)
    a = Q(97, 100) ** 3
    b = Q(71, 100) * (1 + Q(97, 100) + Q(97, 100) ** 2)
    exact(M * a == Q(912673, 997000), "Ma identity failed")
    exact(M * a < Q(23, 25), "Ma contraction failed")
    exact(M * b == Q(2066739, 997000), "Mb identity failed")
    exact(M * b < Q(211, 100), "Mb bound failed")
    exact(Q(3, 20) / M - Q(211, 10000) == Q(2569, 20000),
          "outer log/carry coefficient failed")
    exact(Q(2569, 20000) > Q(1, 8), "outer strict drift margin failed")
    exact(10 ** 6 + 2003 ** 2 == 5012009, "inner denominator failed")
    margin = (Q(25000000, 1250) - Q(211, 10000)) / 5012009
    exact(margin == Q(199999789, 50120090000), "inner drift identity failed")
    exact(margin > Q(3, 1000), "inner strict drift margin failed")
    exact(Q(3, 2) ** 5 / 2 ** 3 == Q(243, 256) < 1,
          "Chernoff exponential factor failed")
    exact(32 > 27, "positive log inverse-slope margin failed")
    return {"exact_comparisons": checks,
            "scope": "algebraic constants only; calculus and infinite-time proof are in notes"}


def phase_checks():
    def orbit(n):
        result = [n]
        while result[-1] != 1:
            need(len(result) < 10000, "literal control orbit exceeded finite bound")
            result.append(shortcut(result[-1]))
        return result

    a, b = orbit(85), orbit(425)
    need(len(a) - 1 == 8 and len(b) - 1 == 39, "85/425 first-hit clocks failed")
    need([i for i, value in enumerate(b) if value == 5] == [35],
         "425 target-five clock failed")
    x = 85
    for _ in range(35):
        x = shortcut(x)
    need(x == 2, "source phase at target-five clock failed")
    x, y, k, c = 5, 25, 0, Q(0)
    for _ in range(12):
        k, c, eta = section_step(k, c, x % 2)
        need(eta == y % 2, "point equality control target bit failed")
        x, y = shortcut(x), shortcut(y)
    need((x, y, k, c) == (1, 5, 1, -10), "isolated ratio equality control failed")
    return {"tau_85": len(a) - 1, "tau_425": len(b) - 1,
            "unique_425_hit_of_5": 35, "85_at_clock_35": 2,
            "point_equality_control": {"source": 5, "clock": 12,
                                       "endpoints": [x, y], "section": [k, str(c)]}}


def negative_controls():
    rejected = 0
    for bad in (Q(1, 2), Q(3, 8)):
        try:
            parity(bad)
        except CheckFailure:
            rejected += 1
        else:
            raise CheckFailure("invalid binary parity denominator accepted")
    for n in (0, -1):
        try:
            shortcut(n)
        except CheckFailure:
            rejected += 1
        else:
            raise CheckFailure("nonpositive ordinary state accepted")
    # Deliberately omit the relative-slope correction at an odd/odd step.
    k, c, eta = section_step(0, Q(0), 1)
    wrong_c = Q(eta, 2)
    need(wrong_c != c and shortcut(5) != slope(k) * shortcut(1) + wrong_c,
         "mutated affine update escaped the negative control")
    rejected += 1
    return {"rejected_invalid_or_mutated_controls": rejected}


def main():
    folder = Path(__file__).resolve().parent
    report = {"status": "PASS", "evidence": "bounded exact arithmetic",
              "ordinary": ordinary_checks(), "state_grid": section_grid_checks(),
              "constants": constant_checks(), "phase_controls": phase_checks(),
              "negative_controls": negative_controls(),
              "notes_sha256": {name: sha256((folder / name).read_bytes()).hexdigest()
                               for name in ("AFFINE_SECTION_RECURRENCE.md",
                                            "AFFINE_SECTION_ROOT_RETURN.md")},
              "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
              "not_computationally_proved": [
                  "almost-sure recurrence", "infinite expected return time",
                  "infinite subcritical average pressure", "ordinary Collatz convergence"]}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
