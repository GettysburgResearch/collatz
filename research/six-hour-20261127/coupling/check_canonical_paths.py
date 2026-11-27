"""Construct true capped canonical paths from integers and check uniform constants."""
from collections import deque
from fractions import Fraction
import json
from pathlib import Path

import check_global_return as first
import check_optimized_bank as bank

HERE = Path(__file__).resolve().parent
PLAN, _ = bank.read_plan((HERE/"OptimizedBank.lean").read_text())
TABLE = first.rows()
require = bank.require


def ordinary_walk(left, right):
    a, b = bank.orbit(left), bank.orbit(right)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                return a[:i+1] + list(reversed(b[:j]))
    raise ValueError(("no physical merger", left, right))


def local_edges(plan, src, history, parameter=None, graph=None):
    """Return an edge-occurrence upper bound, or populate one actual graph."""
    op, *args = plan
    cur = history[-1]

    def add(left, right, directed=False):
        if graph is not None:
            sample = lambda row: row[0]+parameter*(row[1]-row[0])
            l, r = sample(left), sample(right)
            if directed:
                require(l % 48 == 17 and r == 3*l, "actual canonical edge")
            else:
                require(first.shortcut(l) == r or first.shortcut(r) == l, "actual ordinary edge")
            graph.setdefault(l, {})[r] = directed
            if not directed:
                graph.setdefault(r, {})[l] = False

    def connect(left, right):
        walk = ordinary_walk(left, right)
        for a, b in zip(walk, walk[1:]):
            add(a, b)
        return len(walk)-1

    def linear(row, k, c=0):
        return bank.lin(row, k, c)

    if op in (".split2", ".split3"):
        m = len(args)
        def child(i):
            sub = lambda r: bank.restrict(r, m, i)
            value = None if parameter is None else parameter//m
            return local_edges(args[i], sub(src), [sub(r) for r in history], value, graph)
        if parameter is not None:
            return child(parameter % m)
        return max(child(i) for i in range(m))

    if op == ".unit":
        nxt = tuple((4*x-1)//3 for x in cur)
        edges = connect(cur, nxt) + connect(linear(cur, 3), linear(nxt, 3))
        return edges + local_edges(args[0], src, history+[nxt], parameter, graph)

    if op == ".nonunit":
        u = tuple(x//3 for x in cur)
        l, r = linear(u, 16, 1), linear(u, 32, 1)
        edges = connect(cur, l) + connect(linear(l, 3), r) + connect(linear(r, 3), linear(cur, 3))
        return edges + sum(local_edges(sub, src, history+[v], parameter, graph)
                           for sub, v in zip(args, (l, r), strict=True))

    index, word = args
    q = history[-1-index]
    if not word:
        add(q, linear(q, 3), directed=True)
        return 1
    total = 0
    for ch in word:
        if ch == "M":
            y, target = bank.ordinary(q), linear(q, 3)
            add(q, y)
            add(y, linear(y, 3), directed=True)
            total += 2 + connect(linear(y, 3), target)
        else:
            if ch == "D":
                target = linear(q, 2)
            elif ch == "I":
                target = tuple((2*x-1)//3 for x in q)
            else:
                target = bank.ordinary(q)
            add(q, target)
            total += 1
        q = target
    return total


def canonical_tripling(w):
    require(w > 0 and w % 16 == 1, "first-stage source")
    graph = {}
    r = (1, 17)
    local_edges(PLAN, r, [r], (w-1)//16, graph)
    prev = {w: None}
    queue = deque([w])
    while queue and 3*w not in prev:
        u = queue.popleft()
        for v in graph.get(u, {}):
            if v not in prev:
                prev[v] = u
                queue.append(v)
    require(3*w in prev, "directed path from original source to its triple")
    u, path = 3*w, []
    while u != w:
        v = prev[u]
        path.append((v, u, graph[v][u]))
        u = v
    return list(reversed(path))


def blocks(n):
    if n % 2 == 0:
        return [(n, n//2, False)]
    for a, b, _, word in TABLE:
        if n < b or (n-b) % a:
            continue
        u, edges = n, []
        for e in word:
            if e == 0:
                edges.extend(canonical_tripling(u))
                u *= 3
            else:
                v = u if e > 0 else (2**(-e)*u-1)//3
                seq = [v]
                for _ in range(abs(e)):
                    seq.append(first.shortcut(seq[-1]))
                if e < 0:
                    seq.reverse()
                require(seq[0] == u, "inverse block meeting")
                edges.extend((x, y, False) for x, y in zip(seq, seq[1:]))
                u = seq[-1]
        require(0 < u < n, "positive descent")
        return edges
    raise ValueError(("no descent leaf", n))


def path_to_one(n):
    require(n > 0, "positive input")
    path = []
    while n != 1:
        step = blocks(n)
        path.extend(step)
        n = step[-1][1]
    return path


def controls():
    opt = bank.main()
    maxima = opt["suprema_over_physical_rows_relative_to_original_1mod16_source"]
    second_height = max(map(Fraction, maxima.values()))
    local_budget = local_edges(PLAN, (1, 17), [(1, 17)])
    contraction = Fraction(1, 2)
    physical_max = Fraction(1)
    stage_length = plain_length = 1
    charge_count = 0
    for a, b, _, word in TABLE:
        A, B = a, b
        length = 0
        for op in word:
            if op == 0:
                A, B = 3*A, 3*B
                vertices = [(A, B)]
                length += local_budget
            else:
                if op > 0:
                    X, Y, u, v = 3*A//2**op, (3*B+1)//2**op, A, B
                else:
                    X, Y = A*2**(-op)//3, (B*2**(-op)-1)//3
                    u, v = X, Y
                vertices = [(u, v)]
                for _ in range(abs(op)):
                    u, v = (3*u//2, (3*v+1)//2) if v % 2 else (u//2, v//2)
                    vertices.append((u, v))
                A, B = X, Y
                length += abs(op)
            for u, v in vertices:
                physical_max = max(physical_max, Fraction(u, a), Fraction(v, b))
        contraction = max(contraction, Fraction(A, a), Fraction(B, b))
        stage_length = max(stage_length, length)
        plain_length = max(plain_length, sum(abs(op) if op else 1 for op in word))
        charge_count = max(charge_count, word.count(0))
    require(contraction < 1 and 2*contraction**14 <= 1, "strict uniform contraction")
    height = max(physical_max, 24*second_height)
    result = {
        "max_first_stage_contraction": str(contraction),
        "max_first_stage_physical_height_factor": str(physical_max),
        "local_tripling_edge_bound": local_budget,
        "max_initial_descent_edges_before_charge_replacement": plain_length,
        "max_initial_charges_in_one_descent": charge_count,
        "single_descent_edge_bound": stage_length,
        "edge_bound_per_ceiling_log2_of_input": 14*stage_length,
        "global_height_factor": str(height),
        "global_integer_height_factor": -(-height.numerator//height.denominator),
        "global_canonical_source_factor": 98304,
        "literal_paths": [],
    }
    for n in [1, 2, 27, 871, 1215655, 2**127-1, 3**88+2]:
        route = path_to_one(n)
        u, charge, peak = n, 0, n
        for l, r, directed in route:
            require(l == u and r > 0, "connected positive path")
            if directed:
                require(l % 48 == 17 and r == 3*l and l <= 98304*n, "scoped charge")
                charge += 1
            else:
                require(first.shortcut(l) == r or first.shortcut(r) == l, "ordinary edge")
            u, peak = r, max(peak, r)
        require(u == 1 and peak <= height*n, "bounded return to one")
        require(len(route) <= 14*stage_length*(n-1).bit_length(), "logarithmic length")
        result["literal_paths"].append(dict(input=str(n), edges=len(route),
                                             canonical_charges=charge, maximum=str(peak)))
    return result


if __name__ == "__main__":
    result = controls()
    archive = HERE/"CANONICAL_PATH_CONTROLS.json"
    if archive.exists():
        require(result == json.loads(archive.read_text()), "archived controls differ")
    print(json.dumps(result, indent=2, sort_keys=True))
