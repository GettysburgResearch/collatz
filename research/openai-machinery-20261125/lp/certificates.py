"""Exact finite potential or Farkas certificates, with ordinary Collatz witnesses.

This implements a difference-constraints specialization, not OpenAI's new
strongly polynomial general LP algorithm. All certificate checks use integers.
The finite graph must be supplied with its own coverage theorem before a
potential can imply anything about all positive integers.
"""

import json
from collections import Counter
from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class Edge:
    source: int
    target: int
    cost: int
    ordinary: int | None = None
    endpoint: int | None = None
    gap: int | None = None


def odd_step(n):
    if type(n) is not int or n <= 0 or n % 2 == 0:
        raise ValueError("need a positive odd ordinary source")
    v = 3 * n + 1
    e = (v & -v).bit_length() - 1
    return v >> e, e


def verify_ordinary(edges, modulus=None):
    if modulus is not None and (type(modulus) is not int or modulus <= 0):
        raise ValueError("need a positive integer modulus")
    for edge in edges:
        if any(type(v) is not int for v in (edge.source, edge.target, edge.cost,
                                           edge.ordinary, edge.endpoint, edge.gap)):
            raise ValueError("missing or inexact ordinary witness")
        y, e = odd_step(edge.ordinary)
        if (y, e, edge.cost) != (edge.endpoint, edge.gap, 8 - 5 * e):
            raise ValueError("false ordinary edge or cost")
        projected = (edge.ordinary, y) if modulus is None else (
            edge.ordinary % modulus, y % modulus)
        if (edge.source, edge.target) != projected:
            raise ValueError("source/endpoint projection mismatch")


def verify_certificate(vertices, edges, certificate):
    vertices = set(vertices)
    if any(type(v) is not int for v in vertices) or any(
        type(v) is not int for e in edges for v in (e.source, e.target, e.cost)
    ):
        raise ValueError("vertices and edge data must be exact integers")
    if any(e.source not in vertices or e.target not in vertices for e in edges):
        raise ValueError("missing vertex")
    if certificate["kind"] == "potential":
        p = {int(k): v for k, v in certificate["values"].items()}
        if set(p) != vertices or any(type(v) is not int for v in p.values()):
            raise ValueError("potential domain or exact type")
        if any(p[e.target] - p[e.source] > -e.cost for e in edges):
            raise ValueError("violated potential inequality")
    elif certificate["kind"] == "obstruction":
        y = certificate["multipliers"]
        if len(y) != len(edges) or any(type(v) is not int or v < 0 for v in y):
            raise ValueError("invalid multiplier")
        balance = Counter()
        gain = 0
        for e, v in zip(edges, y):
            balance[e.target] += v
            balance[e.source] -= v
            gain += v * e.cost
        if any(balance.values()) or gain <= 0:
            raise ValueError("not a positive balanced circulation")
        if type(certificate["total_cost"]) is not int or gain != certificate["total_cost"]:
            raise ValueError("wrong objective")
    else:
        raise ValueError("unknown certificate")


def solve(vertices, edges):
    """Bellman-Ford, retaining an exact dual circulation on a negative cycle."""
    vertices = list(vertices)
    if any(type(v) is not int for v in vertices) or any(
        type(v) is not int for e in edges for v in (e.source, e.target, e.cost)
    ) or any(e.source not in vertices or e.target not in vertices for e in edges):
        raise ValueError("invalid exact finite graph")
    p = {v: 0 for v in vertices}
    if not vertices:
        answer = {"kind": "potential", "values": {}}
        verify_certificate(vertices, edges, answer)
        return answer
    previous = {}
    changed = None
    for _ in vertices:
        changed = None
        for i, edge in enumerate(edges):
            candidate = p[edge.source] - edge.cost
            if p[edge.target] > candidate:
                p[edge.target] = candidate
                previous[edge.target] = i
                changed = edge.target
        if changed is None:
            answer = {"kind": "potential", "values": p}
            verify_certificate(vertices, edges, answer)
            return answer
    current = changed
    for _ in vertices:
        current = edges[previous[current]].source
    start = current
    y = [0] * len(edges)
    while True:
        i = previous[current]
        y[i] += 1
        current = edges[i].source
        if current == start:
            break
    answer = {
        "kind": "obstruction",
        "multipliers": y,
        "total_cost": sum(e.cost * v for e, v in zip(edges, y)),
    }
    verify_certificate(vertices, edges, answer)
    return answer


def ordinary_path(start):
    edges = []
    current = start
    seen = set()
    while current != 1:
        if current in seen:
            raise ValueError("unexpected nontrivial cycle in finite control")
        seen.add(current)
        target, gap = odd_step(current)
        edges.append(Edge(current, target, 8 - 5 * gap, current, target, gap))
        current = target
    return edges


def residue_graph(modulus):
    """A finite bank of actual edges suffices to obstruct the full ansatz.

    This does NOT claim all transition coverage. Infeasibility of a subsystem
    implies infeasibility of any larger system containing its exact edges.
    """
    records = {}
    for n in range(1, 4 * modulus + 1, 2):
        if n == 1 or n % 3 == 0:
            continue
        target, gap = odd_step(n)
        key = (n % modulus, target % modulus, gap)
        records.setdefault(key, Edge(*key[:2], 8 - 5 * gap, n, target, gap))
    edges = list(records.values())
    vertices = sorted({v for e in edges for v in (e.source, e.target)})
    verify_ordinary(edges, modulus)
    return vertices, edges


def must_reject(vertices, edges, candidate):
    try:
        verify_certificate(vertices, edges, candidate)
    except ValueError:
        return
    raise RuntimeError("invalid certificate was accepted")


def main():
    report = {"scope": "finite exact certificates; no global coverage", "paths": [], "residues": []}
    for start in (3, 7, 27):
        edges = ordinary_path(start)
        verify_ordinary(edges)
        vertices = sorted({v for e in edges for v in (e.source, e.target)})
        certificate = solve(vertices, edges)
        if certificate["kind"] != "potential":
            raise RuntimeError("acyclic ordinary path should admit a potential")
        report["paths"].append({"start": start, "edges": len(edges), "certificate": certificate})
    for modulus in (6, 18, 54, 162, 486):
        vertices, edges = residue_graph(modulus)
        certificate = solve(vertices, edges)
        if certificate["kind"] != "obstruction":
            raise RuntimeError("ordinary self-loop should obstruct the residue ansatz")
        active = [{"edge": asdict(e), "weight": y} for e, y in zip(edges, certificate["multipliers"]) if y]
        report["residues"].append({"modulus": modulus, "vertices": len(vertices),
            "edges": len(edges), "active_certificate": active, "total_cost": certificate["total_cost"]})
        broken = dict(certificate, multipliers=[0] * len(edges))
        must_reject(vertices, edges, broken)
        broken = dict(certificate, total_cost=certificate["total_cost"] + 1)
        must_reject(vertices, edges, broken)
        broken = dict(certificate, multipliers=[-v for v in certificate["multipliers"]])
        must_reject(vertices, edges, broken)
    report["rejected_mutations"] = 15
    empty = solve([], [])
    verify_certificate([], [], empty)
    must_reject([0], [], {"kind": "potential", "values": {0: True}})
    must_reject([0], [Edge(0, 0, 0.5)],
                {"kind": "obstruction", "multipliers": [1], "total_cost": 0.5})
    must_reject([0], [Edge(0, 0, 1)],
                {"kind": "obstruction", "multipliers": [1], "total_cost": True})
    for false_edge in (Edge(99, 77, 3, 3, 5, 1), Edge(3, 5, 3.0, 3, 5, 1)):
        try:
            verify_ordinary([false_edge])
        except ValueError:
            pass
        else:
            raise RuntimeError("invalid ordinary projection or exact type was accepted")
    report["boundary_checks"] = {
        "empty_graph": empty,
        "rejected_inexact_or_misprojected": 5,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
