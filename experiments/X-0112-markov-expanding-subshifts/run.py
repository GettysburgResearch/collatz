#!/usr/bin/env python3
"""X-0112: expanding Markov subshifts on residues mod 2^A.

Because each state enables at most one length-L word (bijection residues↔words),
a finite CRT Schottky automaton with L≤A is essentially a subshift of the
deterministic shortcut graph on Z/2^A Z. This experiment:

1) builds the full shortcut graph mod 2^A;
2) searches for strongly connected edge-subsets where every simple cycle has
   odd-density > log(2)/log(3) (hence supercritical concatenation);
3) enumerates ordinary integers in cylinders of those subsets up to a bound
   and checks survival length / divergence.

Links the ping-pong packet back to classical Markov / digit-transfer survivors.
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


LOG2_OVER_LOG3 = math.log(2) / math.log(3)


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def build_graph(A: int):
    M = 1 << A
    succ = {}
    for r in range(M):
        succ[r] = T(r) % M
    return M, succ


def cycle_odd_density(cycle_states, succ) -> float:
    """Odd density along the unique path of length len(cycle)."""
    odds = 0
    for s in cycle_states:
        if s % 2 == 1:
            odds += 1
    return odds / len(cycle_states)


def find_simple_cycles(succ, max_len: int):
    M = len(succ)
    cycles = []

    def dfs(start, node, path, used):
        if len(path) > max_len:
            return
        nxt = succ[node]
        if nxt == start and path:
            cycles.append(path + [nxt])
        elif nxt not in used and len(path) < max_len:
            dfs(start, nxt, path + [nxt], used | {nxt})

    for s in range(M):
        dfs(s, s, [s], {s})
    # normalize rotation
    uniq = {}
    for c in cycles:
        body = c[:-1]
        # rotate to min
        k = body.index(min(body))
        rot = tuple(body[k:] + body[:k])
        uniq[rot] = rot
    return list(uniq.values())


def supercritical_cycles(A: int, max_len: int):
    M, succ = build_graph(A)
    cycles = find_simple_cycles(succ, max_len=max_len)
    out = []
    for c in cycles:
        dens = cycle_odd_density(c, succ)
        if dens > LOG2_OVER_LOG3 + 1e-15:
            out.append(
                {
                    "states": list(c),
                    "len": len(c),
                    "odd_density": dens,
                    "mu": float(Fraction(3 ** sum(s % 2 for s in c), 1 << len(c))),
                }
            )
    out.sort(key=lambda x: -x["odd_density"])
    return {"A": A, "cycles_total": len(cycles), "supercritical": out[:30], "count_super": len(out)}


def survivors_in_cylinder(A: int, allowed_parity_fn, n_max: int, steps: int):
    """Count n<=n_max whose first `steps` parities all lie in an allowed set
    depending on current residue mod 2^A — here allowed means we only keep
    numbers that always take odd steps when odd density is required... 

    Simpler probe: follow Collatz and require that the residue path stays inside
    a chosen subset S of states that induces only supercritical cycles.
    """
    M, succ = build_graph(A)
    # Pick S = all odd residues (aggressive expanding attempt)
    S_odd = {r for r in range(M) if r % 2 == 1}
    # Also S = full set control
    results = {}
    for name, S in [("odds_only", S_odd), ("full", set(range(M)))]:
        stay = 0
        grow = 0
        best = None
        for n0 in range(1, n_max + 1):
            n = n0
            ok = True
            for _ in range(steps):
                if (n % M) not in S:
                    ok = False
                    break
                n = T(n)
            if ok:
                stay += 1
                if n > n0:
                    grow += 1
                    if best is None or n / n0 > best["growth"]:
                        best = {"n0": n0, "final": n, "growth": n / n0}
        results[name] = {"stay": stay, "grow": grow, "best": best}
    return results


def odd_run_death(n_max: int, max_odd_run: int = 40):
    """All-odd itinerary is the most expanding; positive integers cannot stay
    odd forever (every odd maps to (3n+1)/2 which is even when n≡1 mod 4? 
    actually (3n+1)/2 can be odd). Known that infinite all-odd => n=-1.
    Empirically measure maximal odd run lengths for n<=n_max.
    """
    best = (0, None)
    hist = defaultdict(int)
    for n0 in range(1, n_max + 1, 2):
        n = n0
        run = 0
        while n % 2 == 1 and run < max_odd_run:
            n = T(n)
            run += 1
        hist[run] += 1
        if run > best[0]:
            best = (run, n0)
    return {"best_run": best, "histogram": dict(sorted(hist.items())[:20])}


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    cyc6 = supercritical_cycles(6, max_len=6)
    cyc8 = supercritical_cycles(8, max_len=8)
    surv = survivors_in_cylinder(8, None, n_max=5000, steps=20)
    odds = odd_run_death(5000)
    summary = {
        "threshold": LOG2_OVER_LOG3,
        "cycles_A6": cyc6,
        "cycles_A8": {"count_super": cyc8["count_super"], "top": cyc8["supercritical"][:10]},
        "survivors": surv,
        "odd_runs": odds,
        "structural_note": (
            "Residues mod 2^L biject with length-L words, so finite CRT Schottky "
            "with L<=A is a subshift of the deterministic shortcut graph. "
            "Expanding certificates reduce to Markov subsets with odd-density "
            "> log2/log3 — the classical supercritical subshift problem."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["structural_note"],
        f"threshold log2/log3={LOG2_OVER_LOG3:.6f}",
        f"A=6 supercritical simple cycles={cyc6['count_super']} / {cyc6['cycles_total']}",
        f"A=8 supercritical simple cycles={cyc8['count_super']}",
        f"survivors stay odds_only={surv['odds_only']['stay']} grow={surv['odds_only']['grow']} best={surv['odds_only']['best']}",
        f"survivors stay full={surv['full']['stay']} grow={surv['full']['grow']}",
        f"best odd run={odds['best_run']}",
    ]
    if cyc6["supercritical"]:
        lines.append("top A6 super cycles:")
        for c in cyc6["supercritical"][:5]:
            lines.append(f"  dens={c['odd_density']:.4f} mu={c['mu']:.4f} states={c['states']}")
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
