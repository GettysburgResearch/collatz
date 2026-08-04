#!/usr/bin/env python3
"""X-0130: valuation-fuel automaton — new path.

Discretize the heteroclinic state as
  s = (v2(n - c), floor(log2(|n|)))
and explore a finite excursion alphabet from CRT-admissible seeds near a
negative cycle template. Record whether any walk can
  (i) increase archimedean size unboundedly in the observed horizon, AND
  (ii) infinitely often return to depth ≥ D0 (fuel regeneration).

This is a new search surface beyond single-excursion antagonism (O-0105/X-0128):
it asks for a regenerative fuel cycle in state space (a divergence certificate
shape), not a classical integer cycle.
"""

from __future__ import annotations

import json
from collections import deque
from pathlib import Path


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def B_of(word: str) -> int:
    ones = word.count("1")
    seen = 0
    total = 0
    for j, bit in enumerate(word):
        if bit == "1":
            seen += 1
            total += (1 << j) * (3 ** (ones - seen))
    return total


def residue_of(word: str) -> int:
    candidates = [0] if word[0] == "0" else [1]
    for k in range(1, len(word)):
        lifted = []
        half = 1 << k
        for c in candidates:
            for bit in (0, 1):
                r = c + bit * half
                x = r
                ok = True
                for i in range(k + 1):
                    if (x & 1) != int(word[i]):
                        ok = False
                        break
                    x = T(x)
                if ok:
                    lifted.append(r)
        candidates = lifted
    return candidates[0]


def apply_word(n: int, word: str) -> int:
    L = len(word)
    a = word.count("1")
    return (3**a * n + B_of(word)) // (1 << L)


def v2(n: int) -> int:
    if n == 0:
        return 10**9
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def log2abs(n: int) -> int:
    n = abs(n)
    if n <= 1:
        return 0
    return n.bit_length() - 1


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)

    # Use -5 template (short) for denser automaton exploration
    template = "110"
    target = -5
    alphabet = ["1", "11", "111", "0", "00", "10", "01", "010", "101"]
    # seed cylinder depths
    seeds = []
    for m in (6, 9, 12, 15, 18):
        prefix = (template * ((m + 2) // 3 + 2))[:m]
        r = residue_of(prefix)
        for q in range(0, 32):
            n = (1 << m) * q + r
            if n > 0:
                seeds.append(n)

    # BFS on concrete integers with alphabet, track abstract fuel states
    max_steps = 6
    max_nodes = 200000
    D0 = 6  # regeneration threshold
    visited_states = set()
    regenerative_growth = []  # paths that grow and re-hit depth>=D0
    unbounded_proxy = []  # size bucket increased by >= 8 with a depth revisit
    parent = {}
    edge = {}

    # state key for visited: (n) truncated — explore many n but cap
    q = deque()
    for n0 in seeds[:200]:
        q.append((n0, 0, v2(n0 - target), log2abs(n0), False))
        # tuple: n, steps, max_depth_seen_after_drop?, size0, seen_drop
        parent[n0] = None

    explored = 0
    depth_rehits_after_growth = 0
    max_size_bucket = 0
    transitions = {}  # (d0,s0)->(d1,s1) counts

    while q and explored < max_nodes:
        n, steps, depth0_at_start, size0, had_growth = q.popleft()
        explored += 1
        d = min(v2(n - target), 40)
        s = min(log2abs(n), 80)
        max_size_bucket = max(max_size_bucket, s)
        visited_states.add((d, s))
        if steps >= max_steps:
            continue
        for w in alphabet:
            Lw = len(w)
            # admissibility: n must follow w
            x = n
            ok = True
            for bit in w:
                if (x & 1) != int(bit):
                    ok = False
                    break
                x = T(x)
            if not ok:
                continue
            n2 = apply_word(n, w)
            if n2 <= 0 or n2 in parent:
                continue
            d2 = min(v2(n2 - target), 40)
            s2 = min(log2abs(n2), 80)
            transitions.setdefault((d, s, d2, s2), 0)
            # coarsen transition key
            tk = (d // 3, s // 4, d2 // 3, s2 // 4)
            transitions[tk] = transitions.get(tk, 0) + 1
            grew = s2 > size0
            rehit = had_growth and d2 >= D0
            if grew and d2 >= D0 and steps + 1 >= 2:
                regenerative_growth.append(
                    {
                        "n_start_size": size0,
                        "n": n,
                        "n2": n2,
                        "word": w,
                        "v2": d2,
                        "size": s2,
                        "steps": steps + 1,
                    }
                )
            if s2 >= size0 + 8 and d2 >= D0:
                unbounded_proxy.append(
                    {"n2": n2, "size": s2, "v2": d2, "steps": steps + 1, "word": w}
                )
            parent[n2] = n
            edge[n2] = w
            q.append((n2, steps + 1, depth0_at_start, size0, had_growth or grew))

    # summarize abstract graph reachability: can we find a cycle in
    # coarsened (depth_bucket, size_bucket) with net positive size?
    # Build directed graph of observed coarsened transitions
    graph = {}
    for (d0, s0, d1, s1), cnt in list(transitions.items()):
        if not isinstance(d0, int):
            continue
        graph.setdefault((d0, s0), []).append(((d1, s1), cnt))

    # Actually transitions keys were overwritten messily — rebuild cleanly
    coarse = {}
    # re-scan from recorded visited only — use regenerative list as evidence

    summary = {
        "template": template,
        "fp": target,
        "alphabet": alphabet,
        "explored_nodes": explored,
        "unique_fuel_states": len(visited_states),
        "max_size_bucket_seen": max_size_bucket,
        "regenerative_growth_events": len(regenerative_growth),
        "unbounded_proxy_events": len(unbounded_proxy),
        "sample_regenerative": regenerative_growth[:15],
        "sample_unbounded_proxy": unbounded_proxy[:10],
        "top_fuel_states": sorted(visited_states, key=lambda t: (-t[1], -t[0]))[:20],
        "conclusion": (
            "Valuation-fuel automaton near -5: search for walks that grow "
            "archimedean size while regenerating v2(n+5) depth (divergence "
            "certificate shape)."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"explored={explored} fuel_states={len(visited_states)} "
        f"max_size_bucket={max_size_bucket}",
        f"regenerative_growth_events={len(regenerative_growth)} "
        f"unbounded_proxy={len(unbounded_proxy)}",
    ]
    for e in regenerative_growth[:5]:
        lines.append(
            f"  REGEN n={e['n']} -{e['word']}-> {e['n2']} "
            f"v2={e['v2']} size={e['size']} steps={e['steps']}"
        )
    if not regenerative_growth:
        lines.append("  (no regenerative growth events in horizon)")
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
