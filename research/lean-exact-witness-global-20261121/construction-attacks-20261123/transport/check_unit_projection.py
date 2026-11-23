#!/usr/bin/env python3
"""Exact finite controls for the full-source projection, not escape simulation."""
from collections import defaultdict, deque
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def shortcut(n):
    require(n > 0, "positive ordinary input")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def projection(n):
    require(n > 0, "positive projection input")
    m, a = n, 0
    while m % 2 == 0:
        m //= 2
        a += 1
    if m % 3:
        return m, a
    u, e = 3 * m + 1, 0
    while u % 2 == 0:
        u //= 2
        e += 1
    return u, a + e


def trace(n, steps):
    out = [n]
    for _ in range(steps):
        out.append(shortcut(out[-1]))
    return out


def ancestors(root, depth):
    require(root > 0 and root % 2 == 1 and root % 3, "unit target")
    clocks = {root: 0}
    work = deque([root])
    while work:
        u = work.popleft()
        k = clocks[u]
        if k == depth:
            continue
        parents = [2 * u]
        if (2 * u - 1) % 3 == 0:
            m = (2 * u - 1) // 3
            if m > 0 and m % 2:
                parents.append(m)
        for n in parents:
            require(shortcut(n) == u, "actual inverse shortcut edge")
            if n not in clocks:
                clocks[n] = k + 1
                work.append(n)
    return clocks


def weight(n):
    return Q(1, n * n)


def run():
    c2 = (1 + Q(25, 9) / (1 - Q(1, 4096))) / (1 - Q(1, 4))
    require(c2 < 6, "explicit inverse-square constant")
    roots = [1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 41, 65, 85]
    roots += [64 * q + 21 for q in [1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 41]]
    roots = sorted(set(roots))
    pools = atoms = suffix_steps = nonunit_sources = 0
    largest_fiber = 0
    source_sums = []
    for root in roots:
        clocks = ancestors(root, 16)
        fibers = defaultdict(list)
        for n, k in clocks.items():
            u, h = projection(n)
            require(u > 0 and u % 2 == 1 and u % 3, "projected unit")
            require(h <= k, "projection is before the same target")
            path = trace(n, k)
            require(path[h] == u and path[-1] == root, "literal prefix and suffix")
            require(3 * u <= 5 * n, "sharp height factor")
            fibers[u].append(n)
            suffix_steps += k - h
            atoms += 1
            m = n
            while m % 2 == 0:
                m //= 2
            nonunit_sources += m % 3 == 0
        for u, sources in fibers.items():
            require(sum(map(weight, sources), Q(0)) <= c2 * weight(u), "finite fiber budget")
            largest_fiber = max(largest_fiber, len(sources))
        full_mass = sum(map(weight, clocks), Q(0))
        image_mass = sum(map(weight, fibers), Q(0))
        require(full_mass <= c2 * image_mass, "finite deduplicated mass consumer")
        ratio = full_mass / image_mass
        source_sums.append(dict(root=root, sources=len(clocks), unit_images=len(fibers),
                                exact_ratio_sha256=sha256(str(ratio).encode()).hexdigest(),
                                ratio_display=round(float(ratio), 10)))
        pools += 1

    # Complete finite rectangles of the two exact source families. This
    # independently checks the fiber parameterization and pressure multiplier.
    rectangles = rectangle_atoms = 0
    table = {1: 6, 2: 5, 4: 4, 5: 1, 7: 2, 8: 3}
    max_inverse_power_ratio = Q(0)
    max_pressure_ratio = Q(0)
    for u in range(1, 602, 2):
        if u % 3 == 0:
            continue
        e0 = table[u % 9]
        require(pow(2, e0, 9) * u % 9 == 1, "nonunit exponent table")
        require(sum(pow(2, e, 9) * u % 9 == 1 for e in range(1, 7)) == 1,
                "unique nonunit base exponent")
        actual = {}
        pressure_mass = Q(0)
        geo_a = sum((Q(1, 4) ** a for a in range(7)), Q(0))
        geo_b = sum((Q(1, 4096) ** b for b in range(4)), Q(0))
        for a in range(7):
            n = (1 << a) * u
            require(n not in actual, "disjoint first fiber family")
            actual[n] = (a, None)
            pressure_mass += Q(1, 4) ** a
            for b in range(4):
                e = e0 + 6 * b
                m = ((1 << e) * u - 1) // 3
                require(m > 0 and m % 2 and m % 3 == 0, "nonunit odd parent")
                require(3 * m + 1 == (1 << e) * u, "exact odd edge")
                m0 = ((1 << e0) * u - 1) // 3
                require(m == 64 ** b * m0 + (64 ** b - 1) // 3,
                        "complete sibling recurrence")
                require(5 * m0 >= 3 * u and m >= 64 ** b * m0, "fiber height")
                n = (1 << a) * m
                require(n not in actual, "no duplicate two-parameter fiber")
                actual[n] = (a, e)
                pressure_mass += Q(1, 4) ** a * Q(3, 1 << e) ** 2
        for n, (a, e) in actual.items():
            v, h = projection(n)
            require(v == u and h == a + (0 if e is None else e), "exact complete fiber clock")
            require(trace(n, h)[-1] == u, "actual complete fiber realization")
        square_mass = sum(map(weight, actual), Q(0)) / weight(u)
        expected_pressure = geo_a * (1 + Q(3, 1 << e0) ** 2 * geo_b)
        require(pressure_mass == expected_pressure, "exact pressure rectangle factor")
        require(square_mass <= c2, "complete rectangle power mass")
        pressure_upper = (1 + Q(9, 4) / (1 - Q(1, 4096))) / (1 - Q(1, 4))
        require(pressure_mass <= pressure_upper, "uniform exact pressure multiplier")
        max_inverse_power_ratio = max(max_inverse_power_ratio, square_mass)
        max_pressure_ratio = max(max_pressure_ratio, pressure_mass)
        rectangles += 1
        rectangle_atoms += len(actual)

    # Exact failed strengthenings, not putative escaping examples.
    controls = []
    require(projection(3) == (5, 1) and 5 > 3, "projection can increase height")
    controls.append("height factor 1 rejected by 3 -> 5")
    dyadic = [5 * 2 ** a for a in range(20)]
    require(len({projection(n)[0] for n in dyadic}) == 1, "unweighted collision control")
    controls.append("bounded unweighted multiplicity rejected by a dyadic fiber")
    require(sum(map(weight, dyadic), Q(0)) > weight(5), "dropping dyadic multiplicity fails")
    controls.append("omitted dyadic weights rejected")
    require(projection(75) == (113, 1) and trace(75, 3) == [75, 113, 170, 85],
            "nonunit source reaches unchanged unit target")
    controls.append("lost nonunit source rejected by 75 -> 113 -> 170 -> 85")
    require(projection(21) == (1, 6), "nonunit odd prefix must be completed")
    controls.append("one shortcut step is not the full odd projection: 21 -> 1 takes 6")

    base = Path(__file__).resolve().parent
    sources = {name: sha256((base / name).read_bytes()).hexdigest()
               for name in ["FULL_SOURCE_FINITE_CERTIFICATE.md", "UnitProjection.lean",
                            "check_unit_projection.py"]}
    return dict(scope="finite actual ordinary predecessor and exact weighted-fiber controls; no escape simulation",
                sources=sources, full_predecessor_pools=pools, actual_source_atoms=atoms,
                actual_projected_suffix_steps=suffix_steps, sources_with_nonunit_odd_part=nonunit_sources,
                largest_observed_fiber=largest_fiber, complete_fiber_rectangles=rectangles,
                complete_rectangle_atoms=rectangle_atoms, inverse_square_constant=str(c2),
                largest_finite_inverse_power_ratio=str(max_inverse_power_ratio),
                largest_finite_pressure_ratio=str(max_pressure_ratio),
                failed_strengthening_controls=controls, sample_pool_records=source_sums[:5])


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
