#!/usr/bin/env python3
"""Exact finite ordinary masses, support replay, and rational prefix regression."""
from __future__ import annotations
from fractions import Fraction
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)


def shortcut(x: int) -> int:
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def weight(x: int) -> Fraction:
    return Fraction(9 if x % 2 else 1, 4)


def finite_mass(height: int) -> list[Fraction]:
    edges = [[] for _ in range(height + 1)]
    for source in range(1, height + 1):
        target = shortcut(source)
        if target <= height:
            edges[source].append((target, source))
            edges[target].append((source, source))
    out = [Fraction(0) for _ in edges]
    seen = set()
    for vertex in range(1, height + 1):
        if vertex in seen:
            continue
        component = {vertex}
        work = [vertex]
        while work:
            for neighbor, _ in edges[work.pop()]:
                if neighbor not in component:
                    component.add(neighbor)
                    work.append(neighbor)
        seen.update(component)
        if 1 in component:
            continue
        sequence = []
        position = {}
        tip = vertex
        while tip <= height and tip not in position:
            position[tip] = len(sequence)
            sequence.append(tip)
            tip = shortcut(tip)
        cut = min(sequence[position[tip]:]) if tip <= height else None
        root = cut if cut is not None else min(component)
        out[root] = Fraction(1, 4 ** (root-1).bit_length())
        known = {root}
        work = [root]
        while work:
            u = work.pop()
            for v, src in edges[u]:
                if src == cut or v in known:
                    continue
                out[v] = out[u] / weight(src) if u == src else out[u] * weight(src)
                known.add(v)
                work.append(v)
        require(known == component, "weight propagation covers the entire component")
        for u in component:
            v = shortcut(u)
            if v <= height and u != cut:
                require(out[u] == weight(u) * out[v], "retained physical edge weight")
    return out


def directly_resolves(n: int, H: int) -> bool:
    seen = set()
    while n <= H and n not in seen:
        if n == 1:
            return True
        seen.add(n)
        n = shortcut(n)
    return False


def recurrence_order(a: list[Fraction]) -> int:
    """Berlekamp–Massey over Q, with an independent substitution check."""
    C = [Fraction(1)]
    previous = [Fraction(1)]
    L = 0
    delay = 1
    pivot = Fraction(1)
    for n, value in enumerate(a):
        residual = value + sum(C[j]*a[n-j] for j in range(1, min(len(C), L+1)))
        if residual == 0:
            delay += 1
            continue
        old = C.copy()
        multiplier = residual/pivot
        C.extend([Fraction(0)] * max(0, len(previous)+delay-len(C)))
        for j, entry in enumerate(previous):
            C[delay+j] -= multiplier*entry
        if 2*L <= n:
            L = n+1-L
            previous = old
            pivot = residual
            delay = 1
        else:
            delay += 1
    require(all(a[n]+sum(C[j]*a[n-j] for j in range(1, min(len(C), L+1))) == 0
                for n in range(L, len(a))), "returned recurrence fits every prescribed index")
    return L


def main() -> None:
    rows = []
    for H in (15, 31, 63, 127, 255, 511, 2047, 8191):
        mass = finite_mass(H)
        for n in range(1,H+1):
            require((mass[n] == 0) == directly_resolves(n,H), "exact finite support")
            if 2*n <= H:
                require(4*mass[2*n] == mass[n], "finite dyadic section identity")
        for N in (15,31,63):
            if N > H:
                continue
            packet=mass[:N+1]
            unresolved=[n for n in range(1,N+1) if packet[n]]
            order=recurrence_order(packet)
            require((4*order > N+2) if unresolved else order == 0, "finite recurrence gap")
            rows.append({'height':H,'prefix_end':N,'first_unresolved':min(unresolved,default=None),
                         'unresolved_count':len(unresolved),'rational_recurrence_order':order})
    print(json.dumps(rows,indent=2))

if __name__ == '__main__':
    main()
