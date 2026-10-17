#!/usr/bin/env python3
"""Exact audit for the H renewal one-counter normal form.

Finite computation only.  It verifies the canonical type cylinders and
transition decoder in a bounded type box, enumerates the nondecreasing
("refund") edge graph, and searches the canonical edge roots for consecutive
refund transitions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path

sys.setrecursionlimit(100_000)


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 requires a positive integer")
    return (n & -n).bit_length() - 1


@dataclass(frozen=True)
class TypeData:
    a: int
    R: int
    b: int
    q_plus_one: int
    modulus: int
    x0: int
    u0: int
    y0: int
    x_slope: int
    u_slope: int
    y_slope: int


@dataclass(frozen=True)
class EdgeData:
    eta: int
    q: int
    zeta: int
    amp: int


def type_data(a: int, R: int, b: int) -> TypeData:
    d = 3 * R + 2 * b
    two_modulus = 1 << (d + 1)
    coefficient = 9**R * 3**a
    rhs = (1 << d) + 8**R - 9**R
    residue_two = rhs * pow(coefficient, -1, two_modulus) % two_modulus
    x0 = next(
        residue_two + t * two_modulus
        for t in range(3)
        if (residue_two + t * two_modulus) % 3 == 2
    )
    modulus = 3 * two_modulus
    numerator_u = 3**a * x0 + 1
    assert numerator_u % 8**R == 0
    u0 = numerator_u // 8**R
    numerator_y = 9**R * u0 - 1
    assert numerator_y % 4**b == 0
    y0 = numerator_y // 4**b
    assert x0 % 6 == 5
    assert u0 % 4 == 1
    assert y0 % 6 == 5
    return TypeData(
        a=a,
        R=R,
        b=b,
        q_plus_one=d + 1,
        modulus=modulus,
        x0=x0,
        u0=u0,
        y0=y0,
        x_slope=modulus,
        u_slope=2 ** (2 * b + 1) * 3 ** (a + 1),
        y_slope=2 * 3 ** (2 * R + a + 1),
    )


def edge_data(source: TypeData, target: TypeData) -> EdgeData:
    assert source.b == target.a
    q = 3 * target.R + 2 * target.b
    modulus = 1 << q
    odd_amp = 3 ** (2 * source.R + source.a)
    eta = ((target.x0 - source.y0) // 6) * pow(odd_amp, -1, modulus)
    eta %= modulus
    numerator = source.y0 + source.y_slope * eta - target.x0
    assert numerator % target.modulus == 0
    zeta = numerator // target.modulus
    assert zeta >= 0
    return EdgeData(eta=eta, q=q, zeta=zeta, amp=odd_amp)


def direct_transition(source: TypeData, k: int) -> tuple[tuple[int, int, int], int] | None:
    X = source.x0 + source.x_slope * k
    first = 3**source.a * X + 1
    valuation = v2(first)
    if valuation % 3:
        return None
    R = valuation // 3
    U = first >> valuation
    if R <= 0 or U % 4 != 1:
        return None
    second = 9**R * U - 1
    valuation_two = v2(second)
    if valuation_two % 2:
        return None
    b = valuation_two // 2
    Y = second >> valuation_two
    if b <= 0 or Y % 6 != 5:
        return None

    next_first = 3**b * Y + 1
    next_valuation = v2(next_first)
    if next_valuation % 3:
        return None
    S = next_valuation // 3
    U_next = next_first >> next_valuation
    if S <= 0 or U_next % 4 != 1:
        return None
    next_second = 9**S * U_next - 1
    next_v2 = v2(next_second)
    if next_v2 % 2:
        return None
    c = next_v2 // 2
    if c <= 0:
        return None

    target = type_data(b, S, c)
    difference = Y - target.x0
    if difference < 0 or difference % target.modulus:
        return None
    return (b, S, c), difference // target.modulus


def is_refund(edge: EdgeData) -> bool:
    return edge.amp >= (1 << edge.q) and edge.zeta >= edge.eta


def strongly_connected_components(
    nodes: list[tuple[int, int, int]],
    graph: dict[tuple[int, int, int], list[tuple[tuple[int, int, int], EdgeData]]],
) -> list[list[tuple[int, int, int]]]:
    index: dict[tuple[int, int, int], int] = {}
    low: dict[tuple[int, int, int], int] = {}
    stack: list[tuple[int, int, int]] = []
    on_stack: set[tuple[int, int, int]] = set()
    components: list[list[tuple[int, int, int]]] = []

    def visit(v: tuple[int, int, int]) -> None:
        index[v] = low[v] = len(index)
        stack.append(v)
        on_stack.add(v)
        for w, _ in graph.get(v, []):
            if w not in index:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            component: list[tuple[int, int, int]] = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                component.append(w)
                if w == v:
                    break
            components.append(component)

    for node in nodes:
        if node not in index:
            visit(node)
    return components


@dataclass(frozen=True)
class Summary:
    max_type: int
    types: int
    transition_cylinders: int
    refund_edges: int
    refund_self_loops: int
    zero_increment_refund_edges: int
    refund_sccs: int
    largest_refund_scc: int
    refund_scc_size_histogram: dict[str, int]
    finite_kraft_numerator: int
    finite_kraft_denominator: int
    full_kraft_numerator: int
    full_kraft_denominator: int
    maximum_canonical_refund_chain: int
    maximizing_start_type: tuple[int, int, int]
    maximizing_start_k: int
    maximizing_initial_X: int
    maximizing_initial_U: int
    maximizing_initial_Y: int
    maximizing_initial_p: int
    maximizing_initial_n: int
    maximizing_exit_type: tuple[int, int, int]
    maximizing_exit_k: int
    maximizing_trajectory: list[dict[str, object]]
    digest_sha256: str


def audit(max_type: int) -> Summary:
    types = {
        (a, R, b): type_data(a, R, b)
        for a in range(1, max_type + 1)
        for R in range(1, max_type + 1)
        for b in range(1, max_type + 1)
    }
    graph: dict[tuple[int, int, int], list[tuple[tuple[int, int, int], EdgeData]]] = defaultdict(list)
    all_edges: list[tuple[tuple[int, int, int], tuple[int, int, int], EdgeData]] = []
    refund_roots: list[tuple[tuple[int, int, int], int]] = []

    for source_id, source in types.items():
        for S in range(1, max_type + 1):
            for c in range(1, max_type + 1):
                target_id = (source.b, S, c)
                target = types[target_id]
                edge = edge_data(source, target)
                all_edges.append((source_id, target_id, edge))

                # Check the exact affine decoder at two different tail values.
                for tail in (0, 7):
                    k = edge.eta + (1 << edge.q) * tail
                    transition = direct_transition(source, k)
                    assert transition is not None
                    decoded_id, decoded_k = transition
                    assert decoded_id == target_id
                    assert decoded_k == edge.zeta + edge.amp * tail

                if is_refund(edge):
                    graph[source_id].append((target_id, edge))
                    refund_roots.append((source_id, edge.eta))

    refund_self_loops = sum(
        1 for source_id, target_id, _ in all_edges
        if source_id == target_id and any(
            w == target_id and is_refund(edge)
            for w, edge in graph.get(source_id, [])
        )
    )
    # The expression above counts a self-loop once for its unique target row.
    zero_increment_refund_edges = sum(
        1 for _, _, edge in all_edges if is_refund(edge) and edge.zeta == edge.eta
    )

    components = strongly_connected_components(list(types), graph)
    cyclic = [
        component
        for component in components
        if len(component) > 1
        or any(w == component[0] for w, _ in graph.get(component[0], []))
    ]

    best_chain: list[dict[str, object]] = []
    best_start = ((1, 1, 1), 0)
    for source_id, k0 in refund_roots:
        state = source_id
        k = k0
        chain: list[dict[str, object]] = []
        for _ in range(50):
            transition = direct_transition(types[state], k)
            if transition is None:
                break
            target_id, next_k = transition
            edge = edge_data(types[state], type_data(*target_id))
            if not is_refund(edge):
                break
            chain.append(
                {
                    "source": state,
                    "k": k,
                    "target": target_id,
                    "next_k": next_k,
                    "eta": edge.eta,
                    "q": edge.q,
                    "zeta": edge.zeta,
                    "amp": edge.amp,
                }
            )
            state, k = target_id, next_k
        if len(chain) > len(best_chain):
            best_chain = chain
            best_start = (source_id, k0)

    start_type, start_k = best_start
    start_data = types[start_type]
    start_X = start_data.x0 + start_data.x_slope * start_k
    start_U = start_data.u0 + start_data.u_slope * start_k
    start_Y = start_data.y0 + start_data.y_slope * start_k
    start_p = (1 << (3 * start_type[1] + 2)) * start_U
    assert (start_p - 4) % 3 == 0
    start_n = (start_p - 4) // 3
    exit_type = start_type
    exit_k = start_k
    for row in best_chain:
        exit_type = tuple(row["target"])
        exit_k = int(row["next_k"])
    assert direct_transition(type_data(*exit_type), exit_k) is None

    finite_kraft = sum(
        Fraction(1, 1 << (3 * S + 2 * c))
        for S in range(1, max_type + 1)
        for c in range(1, max_type + 1)
    )
    full_kraft = Fraction(1, 21)

    payload = {
        "max_type": max_type,
        "types": len(types),
        "transition_cylinders": len(all_edges),
        "refund_edges": len(refund_roots),
        "refund_self_loops": refund_self_loops,
        "zero_increment_refund_edges": zero_increment_refund_edges,
        "refund_scc_sizes": sorted(len(component) for component in cyclic),
        "finite_kraft": [finite_kraft.numerator, finite_kraft.denominator],
        "best_start": [list(best_start[0]), best_start[1]],
        "best_initial": [start_X, start_U, start_Y, start_p, start_n],
        "best_exit": [list(exit_type), exit_k],
        "best_chain": best_chain,
    }
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    histogram = Counter(len(component) for component in cyclic)
    return Summary(
        max_type=max_type,
        types=len(types),
        transition_cylinders=len(all_edges),
        refund_edges=len(refund_roots),
        refund_self_loops=refund_self_loops,
        zero_increment_refund_edges=zero_increment_refund_edges,
        refund_sccs=len(cyclic),
        largest_refund_scc=max(map(len, cyclic), default=0),
        refund_scc_size_histogram={str(k): histogram[k] for k in sorted(histogram)},
        finite_kraft_numerator=finite_kraft.numerator,
        finite_kraft_denominator=finite_kraft.denominator,
        full_kraft_numerator=full_kraft.numerator,
        full_kraft_denominator=full_kraft.denominator,
        maximum_canonical_refund_chain=len(best_chain),
        maximizing_start_type=best_start[0],
        maximizing_start_k=best_start[1],
        maximizing_initial_X=start_X,
        maximizing_initial_U=start_U,
        maximizing_initial_Y=start_Y,
        maximizing_initial_p=start_p,
        maximizing_initial_n=start_n,
        maximizing_exit_type=exit_type,
        maximizing_exit_k=exit_k,
        maximizing_trajectory=best_chain,
        digest_sha256=digest,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-type", type=int, default=12)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_type < 1:
        raise SystemExit("max-type must be positive")
    summary = audit(args.max_type)
    rendered = json.dumps(asdict(summary), indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
