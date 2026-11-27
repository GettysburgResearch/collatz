"""Build paths from one to every positive integer with canonical directed arrows."""
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path

import check_canonical_paths as paths

HERE = Path(__file__).resolve().parent
require = paths.require

# Descending from n. A zero traverses 3w -> w with w = 1 modulo 16.
TREE = (
    (
        (
            (
                (
                    [0],
                    (
                        [1, 2, 2],
                        [1, 2, 1, -3, -7, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, 1, 1, 2, 1, -3, -1, -1, -7, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, -5, -1, 0, 2, 2, 1, -3, -1, 0, 2, 8],
                    ),
                ),
                (
                    (
                        (
                            [1, 1, 2, 1, -3, -1, -7, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, 1, 1, 1, 2, 1, -3, -1, -1, -1, -7, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, -5, -1, 0, 2, 2, 1, -3, -1, 0, 2, 9],
                            (
                                (
                                    [1, 1, 2, 2, 1, -3, -1, 0, 2],
                                    [1, 1, 2, 2, 2],
                                ),
                                [1, 1, 2, 3],
                            ),
                        ),
                        [1, 1, 3],
                    ),
                    (
                        [1, 1, 1, -7, -3, -1, -3, -1, 0, 2, 4, 1, 1, 1, 3, 2, 1, -3, -1, -5, -1, 0, 2, 2, 1, -3, -1, 0, 2, 5, -1, -3, -3, -1, 0, 2, 3, 6],
                        (
                            (
                                (
                                    [1, -3, -8, -1, 0, -3, -1, 0, 2, 3, 1, 2, 1, 1, 1, 2, 2, -4, -1, -1, -1, -5, -1, 0, 2, 2, 1, -3, -1, 0, 2, 7],
                                    [1, 1, -7, -1, -1, -2, -3, -3, -1, 0, 2, 3, -1, 0, 2, 5],
                                    [1, -3, -2, -3, -3, -3, -1, 0, 2, 3, 3, 3],
                                ),
                                [1, -3, -2, -3, -3, -1, 0, 2, 3, 3],
                                [1, -3, -2, -9, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, 1, 2, 1, -3, -1, -1, -3, -1, 0, 2, 5, 3],
                            ),
                            [1, -5, -1, -5, -1, 0, 2, 2, 1, -3, -1, 0, 2, 5],
                            [1, -3, -2, -3, -1, 0, 2, 3],
                        ),
                        (
                            [1, -5, -7, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, -5, -1, 0, 2, 2, 1, -3, -1, 0, 2, 6],
                            [1, 1, -7, -1, -3, -1, 0, 2, 4, 1, -3, -3, -1, 0, 2, 3, 3, 6],
                            [1, -5, -1, -3, -1, 0, 2, 4],
                        ),
                    ),
                ),
            ),
            (
                [1, -5, -3, -1, 0, 2, 3, 2, 1, 1, -7, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, -5, -1, 0, 2, 2, 1, -3, -1, 0, 2, 6],
                (
                    [1, -11, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, 1, 2, 2, 1, -3, -1, 0, 2, 3, -5, -3, -1, 0, 2, 3, 2, 1, 1, -7, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, -5, -1, 0, 2, 2, 1, -3, -1, 0, -3, -1, 0, 2, 3, 1, 3, 1, -7, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, -5, -1, 0, 2, 2, 1, -3, -1, 0, 2, 6],
                    [1, 1, -5, -2, -3, -1, 0, 2, 3, 1, 3, 1, -7, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, -5, -1, 0, 2, 2, 1, -3, -1, 0, 2, 7],
                ),
                [1, -11, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, 1, 2, 2, -4, -1, -1, -3, -1, 0, 2, 5, 2, 1, 1, -7, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, -5, -1, 0, 2, 2, 1, -3, -1, 0, 2, 6],
            ),
            [1, -5, -1, 0, 2, 2, 1, -3, -1, 0, 2, 4],
        ),
        (
            (
                [1, -3, -3, -1, 0, 2, 3],
                [1, -9, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, 1, 2, 1, -3, -1, -7, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, -5, -1, 0, 2, 2, 1, -3, -1, 0, 2, 7],
                [1, -9, -1, 0, 2, 2, 1, -3, -1, 0, 2, 3, 1, 2, 1, -3, -1, -1, -3, -1, 0, 2, 5],
            ),
            [1, -3, -1, 0],
            [-2, -1],
        ),
        [-1],
    ),
    [2],
)


def leaves(tree, root=(2, 3)):
    a, b = root
    if isinstance(tree, list):
        yield a, b, tree
        return
    require(isinstance(tree, tuple) and len(tree) in (2, 3), "complete radix node")
    for i, sub in enumerate(tree):
        yield from leaves(sub, (len(tree)*a, b+i*a))


def replay(a, b, word):
    """Reconstruct the affine row at every individual edge."""
    A, B = a, b
    vertices = [(A, B)]
    charges = []
    for e in word:
        if e == 0:
            require(A % 48 == 0 and B % 48 == 3, "charge head")
            A, B = A//3, B//3
            require(A % 16 == 0 and B % 16 == 1, "charge cofactor")
            vertices.append((A, B))
            charges.append((A, B))
            continue
        if e < 0:
            mult = 2**(-e)
            require(A*mult % 3 == 0 and (B*mult-1) % 3 == 0, "inverse integral row")
            lo = A*mult//3, (B*mult-1)//3
        else:
            lo = A, B
        u, v = lo
        trace = [lo]
        for j in range(abs(e)):
            require(u % 2 == 0 and v % 2 == int(j == 0), "fixed ordinary block")
            u, v = (3*u//2, (3*v+1)//2) if v % 2 else (u//2, v//2)
            require(min(u, v) > 0, "positive affine vertex")
            trace.append((u, v))
        if e < 0:
            require(trace[-1] == (A, B), "actual inverse block ends at its original input")
            trace.reverse()
        A, B = trace[-1]
        vertices.extend(trace[1:])
    require(A <= a and 0 < B < b, "whole positive strict descent")
    return vertices, charges


def outward_path(n):
    """Return an actual directed path from 1 to n."""
    require(n > 0, "positive target")
    parts = []
    while n > 1:
        if n % 2 == 0:
            parts.append([(n//2, n, False)])
            n //= 2
            continue
        tree, t, a, b = TREE, (n-3)//2, 2, 3
        while not isinstance(tree, list):
            m = len(tree)
            t, i = divmod(t, m)
            tree, (a, b) = tree[i], (m*a, b+i*a)
        rows, _ = replay(a, b, tree)
        vals = [A*t+B for A, B in rows]
        require(vals[0] == n, "original integer")
        part = []
        for u, v in zip(reversed(vals[1:]), reversed(vals[:-1])):
            if v == 3*u and u % 16 == 1:
                part.extend(paths.canonical_tripling(u))
            else:
                require(paths.first.shortcut(u) == v or paths.first.shortcut(v) == u,
                        "reversed ordinary edge")
                part.append((u, v, False))
        parts.append(part)
        n = vals[-1]
    return [edge for part in reversed(parts) for edge in part]


def controls():
    local = paths.local_edges(paths.PLAN, (1, 17), [(1, 17)])
    ratios = []
    heights = []
    sources = []
    original_length = expanded_length = num_charges = 0
    count = Counter()
    mass = Fraction(0)
    for a, b, word in leaves(TREE):
        vertices, charges = replay(a, b, word)
        mass += Fraction(2, a)
        def ratio(row):
            return max(Fraction(row[0], a), Fraction(row[1], b))
        ratios.append(ratio(vertices[-1]))
        heights.extend(map(ratio, vertices))
        sources.extend(map(ratio, charges))
        k = len(charges)
        count[k] += 1
        num_charges = max(num_charges, k)
        original_length = max(original_length, len(vertices)-1)
        expanded_length = max(expanded_length, len(vertices)-1+k*(local-1))
    require(mass == 1 and 2*max(ratios)**14 <= 1, "full cover and geometric contraction")
    metrics = paths.bank.main()
    local_height = max(Fraction(s) for s in
                       metrics["suprema_over_physical_rows_relative_to_original_1mod16_source"].values())
    cap = max(heights)
    src = max(sources)
    height = max(cap, src*local_height)
    result = {
        "odd_leaves": sum(count.values()), "odd_leaf_mass": str(mass),
        "leaf_distribution_by_number_of_reverse_charges": {str(i): count[i] for i in sorted(count)},
        "first_stage_contraction": str(max(ratios)), "first_stage_height": str(cap),
        "first_stage_source_ceiling": str(src), "max_first_stage_edges": original_length,
        "max_reverse_charges": num_charges, "single_expanded_descent_edges": expanded_length,
        "coefficient_per_ceiling_log2": 14*expanded_length,
        "global_canonical_source_ceiling": str(src*metrics["binary_to_canonical_budget"]),
        "global_vertex_ceiling": str(height), "literal_paths": [],
    }
    for n in (1, 2, 27, 43, 1479, 2**99-1, 5**54+2):
        route = outward_path(n)
        u, peak, count_c = 1, 1, 0
        for l, r, c in route:
            require(l == u and r > 0, "connected positive outward route")
            if c:
                require(l % 48 == 17 and r == 3*l and l <= src*4096*n, "canonical arrow")
                count_c += 1
            else:
                require(paths.first.shortcut(l) == r or paths.first.shortcut(r) == l, "ordinary traversal")
            u, peak = r, max(peak, r)
        require(u == n and peak <= height*n, "true target below vertex cap")
        require(len(route) <= 14*expanded_length*(n-1).bit_length(), "logarithmic length")
        result["literal_paths"].append(dict(target=str(n), edges=len(route), maximum=str(peak),
                                            canonical_arrows=count_c))
    return result


if __name__ == "__main__":
    result = controls()
    archive = HERE/"CANONICAL_CONNECTION_CONTROLS.json"
    if archive.exists():
        require(result == json.loads(archive.read_text()), "archived controls differ")
    print(json.dumps(result, indent=2, sort_keys=True))
