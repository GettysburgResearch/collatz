#!/usr/bin/env python3
"""X-0111: finite CRT Schottky automata (fixed modulus 2^A * 3^B).

Finite-state reformulation that avoids unbounded modulus demand:
states are residues mod M. Edges are shortcut steps or short blocks
compatible with the state. Parameter update on the cover n=M q+r is affine
in q. Search for:
  (1) SCCs where every simple cycle has parameter multiplier |α|>1
  (2) whether any ordinary positive lift follows an aperiodic infinite path
      with height→∞

Periodic expanding cycles are expected to yield negative/2-adic fixed points
(L-0103). The experiment hunts aperiodic acceptance with growth.
"""

from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def build_step_automaton(A: int) -> dict:
    """States mod 2^A; edges = one shortcut step with exact affine on q.

    n = 2^A q + r
    if r even: T(n) = 2^{A-1} q + r/2  → state r/2 mod 2^A needs care when A-1<A
    Actually T(n) = 2^{A-1} q + r/2, so write as 2^A q' + r' by splitting q.
    """
    M = 1 << A
    edges = []
    for r in range(M):
        if r % 2 == 0:
            # T = 2^{A-1} q + r/2. Let r2 = r/2. If we keep modulus M=2^A,
            # T = M*(q//2) + (2^{A-1}(q%2) + r2) when expressing...
            # Exact: T(n)= n/2 = 2^{A-1} q + r/2.
            # As AP with same M: only if we reparameterize.
            # dst residue of T(r) for q=0, but lift dependence:
            # For all q: T(M q + r) = (M/2) q + r/2 = M (q//2) + (M/2)(q%2) + r/2.
            # Multi-edges by parity of q — state machine on residue alone is NOT
            # closed without storing q mod 2. So enlarge or use M decreasing.
            #
            # Better: store state as residue mod M, and record alpha,beta for
            # map q |-> alpha q + beta into dst = (alpha q + beta) represented
            # as new_n = M * q_new + dst with q_new = alpha q + beta... wait.
            #
            # Standard trick: keep modulus fixed M, write
            # T(Mq+r) = α q + β exactly (not necessarily form M q'+r').
            # Then reduce: q' = (α q + β) // M, r' = (α q + β) % M — but q'
            # depends on q, not affine with constant r' unless α is multiple of M?
            #
            # For even r: α=M/2, β=r/2. Then α q + β = (M/2)q + r/2.
            # r' = ((M/2)q + r/2) mod M depends on q mod 2. Two edges.
            for qpar in (0, 1):
                # restrict to q ≡ qpar mod 2, reparameterize q=2t+qpar
                # T = (M/2)(2t+qpar) + r/2 = M t + (M/2)qpar + r/2
                dst = ((M // 2) * qpar + (r // 2)) % M
                # n' = M t + dst_val with dst_val = (M/2)qpar + r/2
                # t = (q - qpar)/2, so t = (1/2) q - qpar/2 → alpha=1/2 not integer on q.
                # On thinned line q=2t+qpar: n' = M t + ((M/2)qpar + r/2), α_t=1, β=0 for t→t?
                # height: n~M q, n'~ M t = M q/2, ratio 1/2.
                edges.append(
                    {
                        "src": r,
                        "dst": dst,
                        "kind": "even",
                        "qpar": qpar,
                        "alpha_on_t": 1,
                        "height_ratio": 0.5,
                        "mu_exact": "1/2",
                    }
                )
        else:
            # T = (3n+1)/2 = (3 M q + 3r +1)/2
            # Need 3r+1 even (r odd ⇒ ok). = (3M/2) q + (3r+1)/2
            # 3M/2 = 3*2^{A-1}. For A>=1.
            # Dependence on q mod 2 similarly if we want fixed M residue.
            for qpar in (0, 1):
                # q=2t+qpar
                # T = 3*2^{A-1} (2t+qpar) + (3r+1)/2 = 3*2^A t + 3*2^{A-1} qpar + (3r+1)/2
                # = M*(3t) + 3*2^{A-1} qpar + (3r+1)/2
                val0 = 3 * (1 << (A - 1)) * qpar + (3 * r + 1) // 2
                dst = val0 % M
                # n' = M*(3t) + val0 = M*(3t + val0//M) + dst
                # q_new = 3t + val0//M = 3*(q-qpar)/2 + val0//M
                # On t: alpha=3, height ~ n'/n ~ (3 M t)/(M*2t) = 3/2
                edges.append(
                    {
                        "src": r,
                        "dst": dst,
                        "kind": "odd",
                        "qpar": qpar,
                        "alpha_on_t": 3,
                        "height_ratio": 1.5,
                        "mu_exact": "3/2",
                    }
                )
    return {"A": A, "M": M, "edges": edges}


def cycle_alpha_products(auto: dict, max_len: int = 8) -> dict:
    """Enumerate simple cycles with product of height_ratio (heuristic)."""
    graph = defaultdict(list)
    for e in auto["edges"]:
        graph[e["src"]].append(e)
    cycles = []

    def dfs(start, node, path, prod, used):
        if len(path) >= max_len:
            return
        for e in graph[node]:
            # enforce qpar consistency weakly: ignore for heuristic census
            np = prod * e["height_ratio"]
            npath = path + [e]
            if e["dst"] == start and npath:
                kinds = "".join(x["kind"][0] for x in npath)
                cycles.append(
                    {
                        "kinds": kinds,
                        "len": len(npath),
                        "prod": np,
                        "geo": np ** (1 / len(npath)),
                        "start": start,
                    }
                )
            elif e["dst"] not in used:
                dfs(start, e["dst"], npath, np, used | {e["dst"]})

    for s in range(auto["M"]):
        dfs(s, s, [], 1.0, {s})
    # dedup by kinds+start
    uniq = {}
    for c in cycles:
        uniq[(c["start"], c["kinds"])] = c
    arr = list(uniq.values())
    expanding = [c for c in arr if c["prod"] > 1 + 1e-12]
    return {
        "raw": len(cycles),
        "uniq": len(arr),
        "expanding": len(expanding),
        "best": sorted(expanding, key=lambda c: -c["geo"])[:15],
        "note": "qpar branching ignored beyond edge labels; heuristic only",
    }


def block_automaton(A: int, Lmax: int) -> dict:
    """States mod 2^A; edges = supercritical words with L<=A enabled by residue."""
    M = 1 << A
    blocks = []
    for L in range(1, Lmax + 1):
        for mask in range(1 << L):
            word = format(mask, f"0{L}b")[::-1]
            a = word.count("1")
            if a == 0:
                continue
            N, Mm = 3**a, 1 << L
            if N <= Mm:
                continue
            # residue
            candidates = [0] if word[0] == "0" else [1]
            for k in range(1, L):
                lifted = []
                half = 1 << k
                for c in candidates:
                    for bit in (0, 1):
                        rr = c + bit * half
                        x = rr
                        ok = True
                        for i in range(k + 1):
                            if (x & 1) != int(word[i]):
                                ok = False
                                break
                            x = T(x)
                        if ok:
                            lifted.append(rr)
                candidates = lifted
            r = candidates[0]
            x = r
            for _ in range(L):
                x = T(x)
            blocks.append((word, L, a, r, x, Fraction(N, Mm), N, Mm))

    edges = []
    for word, L, a, r, s, mu, N, Mm in blocks:
        if L > A:
            continue
        src = r % M
        # Image of n=M q + src: only if src ≡ r mod 2^L. Since L<=A and src=r%M,
        # need r % 2^L == r % 2^L; for all q, n=M q + src ≡ src mod 2^L.
        # Enabled for all q iff src ≡ r (mod 2^L). True if src % 2^L == r % 2^L.
        if src % (1 << L) != r % (1 << L):
            continue
        # T^L(Mq+src) = T^L(Mq+r + (src-r)) — only equal to standard formula if src≡r mod 2^L.
        # If src=r (because r < 2^L <= M and src=r%M=r), OK when r < M.
        if src != r and not (r < M and src == r):
            # general: n = M q + src with src ≡ r mod 2^L ⇒ n = 2^L ((M/2^L)q + (src-r)/2^L) + r
            # = 2^L Q + r with Q=(M/2^L)q + (src-r)/2^L
            # T^L = N Q + s = N(M/2^L)q + N(src-r)/2^L + s
            pass
        if r >= M:
            continue
        if src != r:
            continue
        # T^L(Mq+r)= N q * (M/2^L)? Wait standard is T^L(2^L k + r)=N k +s.
        # Here n=M q + r = 2^L * ((M/2^L)q) + r, so k=(M/2^L)q, T^L=N(M/2^L)q + s.
        if M % (1 << L) != 0:
            continue
        alpha = N * (M // (1 << L))
        beta = s
        # n' = alpha q + beta. Reduce mod M: depends on q unless we keep affine cover.
        edges.append(
            {
                "src": r,
                "word": word,
                "mu": str(mu),
                "mu_f": float(mu),
                "alpha": alpha,
                "beta": beta,
                "L": L,
                "a": a,
                # dst for q=0:
                "dst0": beta % M,
            }
        )

    # Find cycles by dst0 heuristic (q=0 section) — incomplete but finds candidates
    graph = defaultdict(list)
    for e in edges:
        graph[e["src"]].append(e)

    cycles = []

    def dfs(start, node, path, mu_prod, depth):
        if depth > 5:
            return
        for e in graph.get(node, []):
            dst = e["dst0"]
            np = mu_prod * Fraction(e["mu"])
            npath = path + [e["word"]]
            if dst == start and npath:
                cycles.append({"words": npath, "mu_prod": str(np), "mu_f": float(np), "start": start})
            elif depth < 5:
                dfs(start, dst, npath, np, depth + 1)

    for s in list(graph.keys()):
        dfs(s, s, [], Fraction(1, 1), 0)
    uniq = {}
    for c in cycles:
        uniq[tuple(c["words"])] = c
    expanding = [c for c in uniq.values() if c["mu_f"] > 1]

    # Lift attempt: for each expanding cycle of words, compose and test integer periods
    lifts = []
    for c in expanding[:25]:
        concat = "".join(c["words"])
        # residue of concat
        candidates = [0] if concat[0] == "0" else [1]
        fail = False
        for k in range(1, len(concat)):
            lifted = []
            half = 1 << k
            for cc in candidates:
                for bit in (0, 1):
                    rr = cc + bit * half
                    x = rr
                    ok = True
                    for i in range(k + 1):
                        if (x & 1) != int(concat[i]):
                            ok = False
                            break
                        x = T(x)
                    if ok:
                        lifted.append(rr)
            candidates = lifted
            if not candidates:
                fail = True
                break
        if fail:
            continue
        r0 = candidates[0]
        L = len(concat)
        a = concat.count("1")
        # B
        ones = a
        seen = 0
        B = 0
        for j, bit in enumerate(concat):
            if bit == "1":
                seen += 1
                B += (1 << j) * (3 ** (ones - seen))
        M2 = 1 << L
        N = 3**a
        # iterate periods until residue fails
        best_steps = 0
        best_n = None
        for q in range(0, 1 << 12):
            n = M2 * q + r0
            m = n
            steps = 0
            while m % M2 == r0 and steps < 60:
                m = (N * m + B) // M2
                steps += 1
            if steps > best_steps:
                best_steps = steps
                best_n = n
        fp = Fraction(-B, N - M2) if N != M2 else None
        lifts.append(
            {
                "words": c["words"],
                "mu": str(Fraction(N, M2)),
                "r0": r0,
                "best_periods": best_steps,
                "best_n": best_n,
                "fixed_point": str(fp) if fp is not None else None,
                "fp_negative": fp < 0 if fp is not None else None,
            }
        )

    return {
        "A": A,
        "Lmax": Lmax,
        "edges": len(edges),
        "expanding_cycles": len(expanding),
        "examples": expanding[:10],
        "lifts": lifts[:15],
        "max_periods_over_lifts": max((L["best_periods"] for L in lifts), default=0),
        "all_fp_negative": all(L.get("fp_negative") for L in lifts) if lifts else None,
    }


def aperiodic_greedy_in_finite_states(A: int, n_max: int, steps: int) -> dict:
    """From seeds, follow supercritical L<=A blocks enabled by current n mod 2^A;
    forbid immediate period-1/2 word repetition when alternatives exist.
    """
    M = 1 << A
    # library
    lib = []
    for L in range(1, A + 1):
        for mask in range(1 << L):
            word = format(mask, f"0{L}b")[::-1]
            a = word.count("1")
            if a == 0:
                continue
            N, Mm = 3**a, 1 << L
            if N <= Mm:
                continue
            candidates = [0] if word[0] == "0" else [1]
            for k in range(1, L):
                lifted = []
                half = 1 << k
                for c in candidates:
                    for bit in (0, 1):
                        rr = c + bit * half
                        x = rr
                        ok = True
                        for i in range(k + 1):
                            if (x & 1) != int(word[i]):
                                ok = False
                                break
                            x = T(x)
                        if ok:
                            lifted.append(rr)
                candidates = lifted
            r = candidates[0]
            B = 0
            ones = a
            seen = 0
            for j, bit in enumerate(word):
                if bit == "1":
                    seen += 1
                    B += (1 << j) * (3 ** (ones - seen))
            lib.append((word, L, a, r, B, N, Mm))

    survivors = 0
    best = None
    for n0 in range(1, n_max + 1):
        n = n0
        hist = []
        ok = True
        for _ in range(steps):
            opts = []
            for word, L, a, r, B, N, Mm in lib:
                if n % Mm == r:
                    n2 = (N * n + B) // Mm
                    if n2 > 0:
                        opts.append((Fraction(N, Mm), word, n2))
            if not opts:
                ok = False
                break
            opts.sort(reverse=True)
            # prefer aperiodicity: avoid repeating last word if alternative
            chosen = None
            for cand in opts:
                if not hist or cand[1] != hist[-1] or len(opts) == 1:
                    chosen = cand
                    break
            if chosen is None:
                chosen = opts[0]
            hist.append(chosen[1])
            n = chosen[2]
        if ok and n > n0:
            survivors += 1
            growth = n / n0
            if best is None or growth > best["growth"]:
                best = {"n0": n0, "final": n, "growth": growth, "words": hist[:12]}
    return {"A": A, "n_max": n_max, "steps": steps, "survivors": survivors, "best": best}


def main() -> None:
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    step = build_step_automaton(6)
    cyc = cycle_alpha_products(step, max_len=6)
    blk = block_automaton(A=8, Lmax=8)
    greed = aperiodic_greedy_in_finite_states(A=8, n_max=4000, steps=25)
    greed2 = aperiodic_greedy_in_finite_states(A=10, n_max=3000, steps=30)
    summary = {
        "step_automaton_cycles": cyc,
        "block_automaton": blk,
        "greedy_A8": greed,
        "greedy_A10": greed2,
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        f"step aut expanding cycles~{cyc['expanding']} best_geo={cyc['best'][0]['geo'] if cyc['best'] else None}",
        f"block aut edges={blk['edges']} exp_cycles={blk['expanding_cycles']} max_periods={blk['max_periods_over_lifts']} all_fp_neg={blk['all_fp_negative']}",
        f"greedy A8 survivors={greed['survivors']} best={greed['best']}",
        f"greedy A10 survivors={greed2['survivors']} best={greed2['best']}",
    ]
    if blk["lifts"]:
        lines.append("lift examples:")
        for L in blk["lifts"][:5]:
            lines.append(
                f"  words={L['words']} periods={L['best_periods']} fp={L['fixed_point']} neg={L['fp_negative']}"
            )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
