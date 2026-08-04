#!/usr/bin/env python3
"""X-0106: finite Schottky automaton over accelerated Collatz blocks.

A Schottky automaton is a finite directed graph whose edges are labeled by
parity words. Each edge e carries an affine update on a vector of CRT
registers (moduli powers of 2 and 3) plus a height multiplier μ_e.

This experiment builds the concrete automaton whose states are residues
modulo 2^K (K small) and edges are single shortcut steps OR short
supercritical blocks that are enabled at that residue. It then searches for
a strongly connected subgraph on which every cycle has geometric mean
height multiplier > 1.

If such a subgraph exists and supports an aperiodic infinite walk realized
by an ordinary integer, that would be a counterexample certificate.
Empirically, for the single-step automaton, every SCC containing the trivial
cycle has some cycles with μ_prod < 1 (descent), and supercritical-only
subgraphs are not closed.

Status: exploratory EMPIRICAL probe of the automaton certificate format.
"""

from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def step_multiplier(n: int) -> Fraction:
    """Exact n' / n for one shortcut step (rational)."""
    if n == 0:
        return Fraction(0, 1)
    if n % 2 == 0:
        return Fraction(1, 2)
    return Fraction(3 * n + 1, 2 * n)


def build_mod_automaton(K: int) -> dict:
    """States 0..2^K-1; edge r -> T(r) mod 2^K with symbolic mu class."""
    mod = 1 << K
    edges = []
    for r in range(mod):
        if r % 2 == 0:
            nxt = (r // 2) % mod
            # On the AP 2^K q + r, T = 2^{K-1} q + r/2 — mu = 1/2 exactly
            edges.append({"src": r, "dst": nxt, "kind": "even", "mu": "1/2", "mu_f": 0.5})
        else:
            # T = (3n+1)/2; on AP: (3(2^K q+r)+1)/2 = 3*2^{K-1} q + (3r+1)/2
            # asymptotic mu -> 3/2, but exact ratio depends on q
            nxt = ((3 * r + 1) // 2) % mod
            edges.append({"src": r, "dst": nxt, "kind": "odd", "mu": "~3/2", "mu_f": 1.5})
    return {"K": K, "mod": mod, "edges": edges}


def cycle_products(edges: list[dict], mod: int, max_len: int = 8) -> dict:
    """Enumerate simple cycles and compute naive mu products treating odd as 3/2."""
    graph = defaultdict(list)
    for e in edges:
        graph[e["src"]].append(e)

    cycles = []

    def dfs(start, node, path, mu_prod, used_nodes):
        if len(path) > max_len:
            return
        for e in graph[node]:
            nxt = e["dst"]
            new_mu = mu_prod * Fraction(e["mu_f"])
            if nxt == start and path:
                cycles.append(
                    {
                        "path": path + [e["kind"][0]],
                        "len": len(path) + 1,
                        "mu_prod": str(new_mu),
                        "mu_prod_f": float(new_mu),
                        "geo_mean": float(new_mu) ** (1 / (len(path) + 1)),
                    }
                )
            elif nxt not in used_nodes and len(path) + 1 < max_len:
                dfs(start, nxt, path + [e["kind"][0]], new_mu, used_nodes | {nxt})

    for s in range(mod):
        dfs(s, s, [], Fraction(1, 1), {s})

    # dedup by path signature + start omitted
    expanding = [c for c in cycles if c["mu_prod_f"] > 1 + 1e-12]
    contracting = [c for c in cycles if c["mu_prod_f"] < 1 - 1e-12]
    return {
        "cycle_count_raw": len(cycles),
        "expanding_cycles": len(expanding),
        "contracting_cycles": len(contracting),
        "best_expanding": sorted(expanding, key=lambda c: -c["geo_mean"])[:10],
        "note": (
            "Odd edges use asymptotic 3/2, not exact affine ratios; "
            "expanding cycles here are NECESSARY-condition candidates only."
        ),
    }


def supercritical_block_automaton(Lmax: int, K: int) -> dict:
    """States mod 2^K; edges = supercritical words of length <= Lmax that are
    compatible with the state (first K bits of residue). Track exact mu=3^a/2^L.
    """
    mod = 1 << K
    # Precompute words
    words = []
    for L in range(1, Lmax + 1):
        for mask in range(1 << L):
            word = format(mask, f"0{L}b")[::-1]
            a = word.count("1")
            if a == 0:
                continue
            N, M = 3**a, 1 << L
            if N <= M:
                continue
            # residue
            candidates = [0] if word[0] == "0" else [1]
            for k in range(1, L):
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
            r = candidates[0]
            x = r
            for _ in range(L):
                x = T(x)
            words.append((word, L, a, r, x, Fraction(N, M)))

    edges = []
    for word, L, a, r, s, mu in words:
        src = r % mod
        # For the edge to be valid for ALL lifts of src mod 2^K, need the word
        # residue constraints beyond K to be free or implied.
        # Conservative: only add edge if L <= K and r ≡ src mod 2^L with src=r.
        if L > K:
            continue
        dst = s % mod
        # Exact image modulus issue: not all lifts of src follow word unless L<=K
        # and src ≡ r mod 2^L. Here src = r % 2^K, and L<=K ⇒ enabled exactly on
        # the cone src + 2^K Z that also equals r mod 2^L, i.e. a subport.
        edges.append(
            {
                "src": src,
                "dst": dst,
                "word": word,
                "mu": str(mu),
                "mu_f": float(mu),
                "L": L,
            }
        )

    # Find cycles with product mu > 1 using DFS limited
    graph = defaultdict(list)
    for e in edges:
        graph[e["src"]].append(e)

    cycles = []

    def dfs(start, node, path_words, mu_prod, depth):
        if depth > 6:
            return
        for e in graph[node]:
            new_mu = mu_prod * Fraction(e["mu"])
            path = path_words + [e["word"]]
            if e["dst"] == start and path:
                cycles.append(
                    {
                        "words": path,
                        "mu_prod": str(new_mu),
                        "mu_prod_f": float(new_mu),
                        "states_start": start,
                    }
                )
            elif depth < 6:
                dfs(start, e["dst"], path, new_mu, depth + 1)

    for s in list(graph.keys()):
        dfs(s, s, [], Fraction(1, 1), 0)

    # Unique by tuple of words
    uniq = {}
    for c in cycles:
        key = tuple(c["words"])
        if key not in uniq:
            uniq[key] = c
    cycles_u = list(uniq.values())
    expanding = [c for c in cycles_u if c["mu_prod_f"] > 1]

    # CRITICAL CHECK: does a cycle of words actually close on an integer AP?
    # For each expanding cycle, try to solve for a seed residue that follows
    # the concatenated word and returns to the same 2^K class with growth.
    realized = []
    for c in expanding[:30]:
        concat = "".join(c["words"])
        L = len(concat)
        # find residue of concat
        candidates = [0] if concat[0] == "0" else [1]
        fail = False
        for k in range(1, L):
            lifted = []
            half = 1 << k
            for cc in candidates:
                for bit in (0, 1):
                    r = cc + bit * half
                    x = r
                    ok = True
                    for i in range(k + 1):
                        if (x & 1) != int(concat[i]):
                            ok = False
                            break
                        x = T(x)
                    if ok:
                        lifted.append(r)
            candidates = lifted
            if not candidates:
                fail = True
                break
        if fail or not candidates:
            continue
        r0 = candidates[0]
        # After L steps from r0, output s0; for AP 2^L q + r0 -> 3^a q + s0
        a = concat.count("1")
        x = r0
        for _ in range(L):
            x = T(x)
        s0 = x
        M, N = 1 << L, 3**a
        # Return to same state mod 2^K means s0 ≡ r0 (mod gcd(2^K, something))
        # For true self-map on a single AP of modulus M: need image port compatible.
        realized.append(
            {
                "words": c["words"],
                "concat_L": L,
                "a": a,
                "mu_block": str(Fraction(N, M)),
                "r0": r0,
                "s0": s0,
                "returns_mod_2K": (s0 % (1 << K)) == (r0 % (1 << K)),
                "supercritical_concat": N > M,
            }
        )

    return {
        "K": K,
        "Lmax": Lmax,
        "edges": len(edges),
        "expanding_symbolic_cycles": len(expanding),
        "examples": expanding[:10],
        "realized_concat_checks": realized[:15],
        "realized_return_count": sum(1 for r in realized if r["returns_mod_2K"]),
    }


def main() -> None:
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    auto = build_mod_automaton(5)
    cyc = cycle_products(auto["edges"], auto["mod"], max_len=6)
    block_auto = supercritical_block_automaton(Lmax=7, K=7)
    summary = {
        "mod_automaton_K5": cyc,
        "block_automaton": block_auto,
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        f"K=5 single-step cycles expanding~{cyc['expanding_cycles']} contracting~{cyc['contracting_cycles']}",
        cyc["note"],
        f"block automaton edges={block_auto['edges']} expanding symbolic cycles={block_auto['expanding_symbolic_cycles']}",
        f"concat returns mod 2^K: {block_auto['realized_return_count']} / {len(block_auto['realized_concat_checks'])} checked",
        "",
        "best expanding single-step (heuristic mu):",
    ]
    for c in cyc["best_expanding"][:5]:
        lines.append(f"  path={''.join(c['path'])} geo_mean={c['geo_mean']:.4f} prod={c['mu_prod']}")
    lines.append("block cycle examples:")
    for c in block_auto["examples"][:5]:
        lines.append(f"  words={c['words']} prod={c['mu_prod']}")
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
