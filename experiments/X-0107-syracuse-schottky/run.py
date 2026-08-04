#!/usr/bin/env python3
"""X-0107: Schottky search on the odd Syracuse map.

S(m) = (3m+1)/2^{v2(3m+1)} for odd positive m.
Inverse branches: for each valuation k>=1,
  m = (2^k * t - 1)/3  must be a positive odd integer, i.e. 2^k t ≡ 1 (mod 3),
  t odd positive.

A Syracuse Schottky pair would be two nonempty sets of odd residues / intervals
with disjoint inverse-branch ping-pong and guaranteed odd-kernel growth.

This script:
1) classifies inverse branches by valuation k;
2) searches modular domains mod 3^p for disjoint branch images;
3) probes whether a finite set of k's can support an expanding automaton on
   odd residues mod M.
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import gcd
from pathlib import Path


def v2(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0)")
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def S(m: int) -> int:
    assert m % 2 == 1 and m > 0
    return (3 * m + 1) // (1 << v2(3 * m + 1))


def inverse_branch(k: int, t: int) -> int | None:
    """Preimage under valuation-k Syracuse branch ending at odd t."""
    assert t % 2 == 1 and t > 0 and k >= 1
    num = (1 << k) * t - 1
    if num % 3 != 0:
        return None
    m = num // 3
    if m > 0 and m % 2 == 1 and S(m) == t and v2(3 * m + 1) == k:
        return m
    return None


def branch_affine(k: int) -> tuple[Fraction, Fraction] | None:
    """m = (2^k / 3) t - 1/3, when defined on the admissible AP of t."""
    return Fraction(1 << k, 3), Fraction(-1, 3)


def admissible_t_mod(k: int, modulus: int) -> list[int]:
    """Odd t mod modulus with 2^k t ≡ 1 (mod 3). Also filter those that can lift."""
    out = []
    for t in range(1, modulus, 2):
        if ((1 << k) * t - 1) % 3 == 0:
            out.append(t)
    return out


def modular_pingpong_search(Kmax: int, mod: int) -> dict:
    """For pairs of valuations k1,k2, see if inverse images of {odd residues}
    land in disjoint residue sets mod `mod` with expansion 2^{k}/3 > 1.
    """
    expanding_ks = [k for k in range(1, Kmax + 1) if (1 << k) > 3]
    hits = []
    for i, k1 in enumerate(expanding_ks):
        for k2 in expanding_ks[i + 1 :]:
            # Image sets of the full odd set under inverse branches are the
            # admissible preimages. Compute residues of preimages for many t.
            set1 = set()
            set2 = set()
            for t in range(1, mod * 4, 2):
                m1 = inverse_branch(k1, t)
                m2 = inverse_branch(k2, t)
                if m1 is not None:
                    set1.add(m1 % mod)
                if m2 is not None:
                    set2.add(m2 % mod)
            inter = set1 & set2
            if set1 and set2 and not inter:
                hits.append(
                    {
                        "k1": k1,
                        "k2": k2,
                        "mod": mod,
                        "|set1|": len(set1),
                        "|set2|": len(set2),
                        "mu1": str(Fraction(1 << k1, 3)),
                        "mu2": str(Fraction(1 << k2, 3)),
                    }
                )
    # Also record typical overlaps
    overlaps = []
    for k1 in expanding_ks[:6]:
        for k2 in expanding_ks[:6]:
            if k2 <= k1:
                continue
            set1=set(); set2=set()
            for t in range(1, mod*4, 2):
                m1=inverse_branch(k1,t); m2=inverse_branch(k2,t)
                if m1 is not None: set1.add(m1%mod)
                if m2 is not None: set2.add(m2%mod)
            overlaps.append({
                "k1":k1,"k2":k2,
                "overlap": len(set1&set2),
                "u1":len(set1),"u2":len(set2),
            })
    return {
        "expanding_ks": expanding_ks,
        "disjoint_hits": hits,
        "overlap_table": overlaps,
    }


def automaton_on_odds(M: int, Kmax: int, depth_search: int = 12) -> dict:
    """States: odd residues mod M. Edges: Syracuse steps with v2=k in 1..Kmax.
    Edge expands the odd kernel asymptotically when 2^k > 3.
    """
    odds = [r for r in range(M) if r % 2 == 1]
    edges = []
    for r in odds:
        # lift representative r, apply S, see k
        # Exact on AP: m=M q + r (q even or odd to keep m odd — M even ⇒ q any with r odd)
        # Use concrete probe over q=0..20
        ks = set()
        dsts = set()
        for q in range(0, 40):
            m = M * q + r
            if m % 2 == 0 or m <= 0:
                continue
            k = v2(3 * m + 1)
            if 1 <= k <= Kmax:
                ks.add(k)
                dsts.add(S(m) % M)
        for k in ks:
            expanding = (1 << k) > 3
            # destination not unique — record multi-edges
            for q in range(0, 40):
                m = M * q + r
                if m % 2 == 0 or m <= 0:
                    continue
                if v2(3 * m + 1) == k:
                    edges.append(
                        {
                            "src": r,
                            "dst": S(m) % M,
                            "k": k,
                            "expanding": expanding,
                            "sample_m": m,
                        }
                    )
                    break

    # Unique edges by (src,dst,k)
    uniq = {}
    for e in edges:
        uniq[(e["src"], e["dst"], e["k"])] = e
    edges_u = list(uniq.values())
    expanding_edges = [e for e in edges_u if e["expanding"]]

    # Search for a cycle using only expanding edges
    graph = {}
    for e in expanding_edges:
        graph.setdefault(e["src"], []).append(e)

    cycles = []

    def dfs(start, node, path, depth):
        if depth > depth_search:
            return
        for e in graph.get(node, []):
            np = path + [e]
            if e["dst"] == start and np:
                cycles.append(np)
            elif depth < depth_search:
                dfs(start, e["dst"], np, depth + 1)

    for s in list(graph.keys()):
        dfs(s, s, [], 0)

    # dedup by k-sequence
    seen=set(); cyc_u=[]
    for c in cycles:
        key=tuple((e["k"], e["dst"]) for e in c)
        if key not in seen:
            seen.add(key); cyc_u.append(c)

    examples=[]
    for c in cyc_u[:20]:
        examples.append({
            "ks":[e["k"] for e in c],
            "states":[c[0]["src"]]+[e["dst"] for e in c],
            "sample_start": c[0]["sample_m"],
        })

    # Try to lift an expanding cycle to an integer odd seed following those k's
    lifted=[]
    for c in cyc_u[:30]:
        ks=[e["k"] for e in c]
        # brute odd seeds
        for m0 in range(1, 5000, 2):
            m=m0
            ok=True
            for k in ks*3:  # three periods
                if v2(3*m+1)!=k:
                    ok=False; break
                m=S(m)
            if ok and m>m0:
                lifted.append({"m0":m0,"final":m,"ks":ks,"growth":m/m0})
                break

    return {
        "M": M,
        "edges": len(edges_u),
        "expanding_edges": len(expanding_edges),
        "expanding_cycles": len(cyc_u),
        "examples": examples[:10],
        "lifted_periodic_k_schedules": lifted[:10],
        "lifted_count": len(lifted),
    }


def main() -> None:
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    ping = modular_pingpong_search(Kmax=10, mod=27)
    auto = automaton_on_odds(M=16, Kmax=8)
    auto2 = automaton_on_odds(M=32, Kmax=8)
    summary = {"modular_pingpong_mod27": ping, "auto_mod16": auto, "auto_mod32": auto2}
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        f"expanding valuations={ping['expanding_ks']}",
        f"disjoint modular hits mod27={len(ping['disjoint_hits'])}",
        f"auto mod16: edges={auto['edges']} exp_edges={auto['expanding_edges']} exp_cycles={auto['expanding_cycles']} lifted={auto['lifted_count']}",
        f"auto mod32: edges={auto2['edges']} exp_edges={auto2['expanding_edges']} exp_cycles={auto2['expanding_cycles']} lifted={auto2['lifted_count']}",
    ]
    if ping["disjoint_hits"]:
        lines.append("DISJOINT HITS:")
        lines.extend(str(h) for h in ping["disjoint_hits"][:10])
    else:
        lines.append("overlap samples:")
        for o in ping["overlap_table"][:8]:
            lines.append(f"  k={o['k1']},{o['k2']} overlap={o['overlap']} sizes={o['u1']}/{o['u2']}")
    if auto["lifted_periodic_k_schedules"]:
        lines.append("lifted schedules:")
        for L in auto["lifted_periodic_k_schedules"][:5]:
            lines.append(str(L))
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
