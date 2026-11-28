"""Exact finite controls for the phase changes and their actual capture clock."""
from collections import Counter
from functools import lru_cache
import hashlib
import json
from math import gcd


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def step(n):
    return (3 * n + 1) // 2 if n % 2 else n // 2


def oddpart(n):
    return n // (n & -n)


def local_floor(n, b, q, numerator, denominator):
    """Exact floor of b*q*log2(n) and a strict rational fractional-part test."""
    base = n ** (b * q)
    integer = base.bit_length() - 1
    selected = base ** denominator < (1 << (denominator * integer + numerator))
    return integer % (2 * b), selected


def grid_controls(b):
    q0, q1, q2 = 1, 1 + 2 * b, (1 + 2 * b) ** 2
    denominator = 16 * b * q2
    total = 0

    def label(i, q, q_next, s):
        value = (i * b * q) // denominator
        partial = i * b * q % denominator
        if 16 * partial < s * denominator:
            value = (i * b * q_next) // denominator
        return value % (2 * b)

    for first, second in ((q0, q1), (q1, q2)):
        period = 2 * denominator // first
        for s in range(17):
            values = [label(i, first, second, s) for i in range(period)]
            require(set(Counter(values).values()) == {period // (2 * b)}, "balance")
            for i, a in enumerate(values):
                delta = denominator // (b * first)
                require(values[(i + delta) % period] == (a + 1) % (2 * b),
                        ("label translation", b, first, s, i))
                total += 1
    seam = 0
    terms = (q0, q1, q2)
    for index in range(2 * denominator):
        # Both selectors must choose the middle pattern along the whole seam.
        frac0 = (index * b * q0) % denominator
        frac1 = (index * b * q1) % denominator
        if 16 * frac0 >= 14 * denominator or 16 * frac1 < 2 * denominator:
            continue
        for s0 in (14, 15, 16):
            for s1 in (0, 1, 2):
                a = label(index, terms[0], terms[1], s0)
                c = label(index, terms[1], terms[2], s1)
                require(a == c, ("two-stage seam", b, index, s0, s1))
                seam += 1
    return total, seam


def map_controls(b, last):
    targets = (3, 5, 7, 9)[:b]
    cycle = {q: i for i, q in enumerate(targets)}
    cycle.update({2 * q: i + b for i, q in enumerate(targets)})
    vertices = {label: n for n, label in cycle.items()}
    q1 = 1 + 2 * b

    @lru_cache(None)
    def phase(n):
        odd = oddpart(n)
        v = (n // odd).bit_length() - 1
        if odd in targets:
            return (targets.index(odd) + b * v) % (2 * b)
        scale = odd.bit_length() - 1
        if scale < 6:
            first, second, s = 1, q1, scale
        else:
            first, second, s = q1, q1 * q1, min(6, scale - 6)
        label, selected = local_floor(n, b, first, s, 6)
        if selected:
            label = local_floor(n, b, second, 0, 1)[0]
        return label

    @lru_cache(None)
    def retained_above(n):
        current = n
        for _ in range(n.bit_length()):
            current = step(current)
            if current < n:
                return False
        return True

    @lru_cache(None)
    def modified(n):
        if n % 2 == 0:
            return n // 2
        if n in targets:
            return 2 * n
        target = vertices[(phase(n) - b) % (2 * b)]
        ordinary = step(n)
        if retained_above(n):
            return target if target != ordinary else 4 * target
        return ordinary if phase(ordinary) == (phase(n) - b) % (2 * b) else target

    digest = hashlib.sha256()
    routes = Counter()
    denominator_checks = 0
    tables = []
    for n in range(1, last + 1):
        original = [n]
        while original[-1] != 1:
            require(len(original) < 500, ("true trajectory timeout", n))
            original.append(step(original[-1]))
        tau = len(original) - 1
        require(all(y > 1 for y in original[:tau]), ("true minimum", n))
        first_change = next((j for j, y in enumerate(original) if modified(y) != step(y)), None)
        require(first_change is not None and first_change <= tau, ("true first change", n))
        current = n
        t = 0
        while current not in cycle:
            following = modified(current)
            require(phase(following) == (phase(current) - b) % (2 * b), "phase advance")
            if current % 2 == 0:
                require(following == current // 2, "halving")
            if t <= first_change:
                require(current == original[t], ("shared prefix", n, t))
            current = following
            t += 1
            require(t <= first_change + 3, ("capture clock", n))
        require(first_change - 1 <= t <= first_change + 3, ("clock bounds", n))
        require(cycle[current] == (phase(n) - b * t) % (2 * b), "phase at entry")
        require(modified(modified(current)) == current, "genuine two-cycle")
        require(phase(2 * n) == (phase(n) + b) % (2 * b), "doubling")
        routes[t - first_change] += 1
        tables.append((phase(n), current, t))
        digest.update(f"{n} {tau} {first_change} {t} {current}\n".encode())
        denominator_checks += 1

    # Compare every pair of independent sources in an explicit small box.
    samples = list(range(1, 97))
    for _ in range(700):
        samples = [modified(n) for n in samples]
    for i, first in enumerate(samples):
        for j, second in enumerate(samples):
            require((first == second) == (tables[i][0] == tables[j][0]),
                    ("synchronous quotient", b, i, j))
    return {"prefixes": denominator_checks, "capture_minus_discrepancy": dict(sorted(routes.items())),
            "ordered_pairs": len(samples) ** 2, "trace_sha256": digest.hexdigest()}


def run():
    scenarios = {}
    for b in (2, 3, 4):
        balanced, seam = grid_controls(b)
        record = map_controls(b, 4096)
        record.update(exact_pattern_translations=balanced, seam_equalities=seam)
        scenarios[str(b)] = record
    return {"scope": "Finite complete positive paths, local first-drop tests, exact selectors and seam identities. Finite schedules do not verify the asymptotic Fourier selection or Brownian estimate.",
            "scenarios": scenarios}


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True, indent=2))
