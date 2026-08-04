#!/usr/bin/env python3
"""X-0103: integer port / inverse-block graph search for height-expanding walks.

Builds a graph whose nodes are residue ports (mod 2^L for various L) and whose
edges are accelerated Collatz blocks that map port to port with exact affine
parameter updates. Searches for multi-port cycles or strongly connected
components with net height expansion — candidate integer Schottky skeletons.

Also implements a creative variant: **projective ping-pong on log-scale
displacement** between distinct mildly supercritical forward maps, looking for
alternating words with monotone log-growth on explicit arithmetic progressions.
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
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


def follow(n: int, L: int) -> tuple[str, int]:
    bits = []
    x = n
    for _ in range(L):
        bits.append(str(x & 1))
        x = T(x)
    return "".join(bits), x


def residue_of(word: str) -> int:
    L = len(word)
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
    return candidates[0]


@dataclass(frozen=True)
class Block:
    word: str
    L: int
    a: int
    B: int
    r: int
    s: int
    mu: Fraction

    @property
    def M(self) -> int:
        return 1 << self.L

    @property
    def N(self) -> int:
        return 3**self.a


def make_block(word: str) -> Block:
    L = len(word)
    a = word.count("1")
    B = B_of(word)
    r = residue_of(word)
    _, s = follow(r, L)
    return Block(word, L, a, B, r, s, Fraction(3**a, 1 << L))


def apply_block(n: int, b: Block) -> int | None:
    if n % b.M != b.r:
        return None
    # T^L(n) = (3^a n + B)/2^L
    return (b.N * n + b.B) // b.M


@dataclass(frozen=True)
class Port:
    L: int
    r: int

    @property
    def M(self) -> int:
        return 1 << self.L


@dataclass(frozen=True)
class Transition:
    src: Port
    dst: Port
    word: str
    # n = M q + r  ->  T^L(n) = N q + s = M' q' + r'
    # so N q + s ≡ r' (mod M') and q' = (N q + s - r')/M'
    alpha: int  # q' = alpha q + beta
    beta: int
    N: int
    M: int
    expand: bool  # N > M roughly height expand when q large


def transition_from_block(b: Block, dst: Port) -> Transition | None:
    """Edge from port of b to dst if the image affine lands in dst for all large q."""
    src = Port(b.L, b.r)
    # T^L(Mq+r) = Nq + s
    # Need Nq + s = M_d * q' + r_d for some affine q'=alpha q + beta, all large q.
    # So Nq + s ≡ r_d (mod M_d) for all q ⇒ N ≡ 0 (mod gcd? ) actually need
    # Nq + s - r_d divisible by M_d for all q ⇒ M_d | N and M_d | (s-r_d),
    # then alpha = N/M_d, beta = (s-r_d)/M_d.
    Md = dst.M
    if b.N % Md != 0:
        return None
    if (b.s - dst.r) % Md != 0:
        return None
    alpha = b.N // Md
    beta = (b.s - dst.r) // Md
    # For q large, q' = alpha q + beta >= 0 automatically if alpha > 0
    if alpha <= 0:
        return None
    expand = b.N > b.M  # supercritical block
    return Transition(src, dst, b.word, alpha, beta, b.N, b.M, expand)


def height_ratio(tr: Transition) -> float:
    # asymptotic n' / n ~ (N/M) * (M/M') wait:
    # n = M q, n' = M' (alpha q) = M' (N/M') q = N q ≈ (N/M) n
    return tr.N / tr.M


def search_ports(Lmax: int) -> dict:
    blocks = []
    for L in range(1, Lmax + 1):
        for mask in range(1 << L):
            word = format(mask, f"0{L}b")[::-1]
            if "1" not in word:
                continue
            blocks.append(make_block(word))

    ports = sorted({Port(b.L, b.r) for b in blocks}, key=lambda p: (p.L, p.r))
    # Transitions: from each block's native port to every port with compatible modulus
    transitions: list[Transition] = []
    for b in blocks:
        for dst in ports:
            # limit fan-out: only dst with L <= Lmax and not huge mismatch
            if dst.L > Lmax:
                continue
            tr = transition_from_block(b, dst)
            if tr is not None:
                transitions.append(tr)

    # Graph adjacency
    graph = defaultdict(list)
    for tr in transitions:
        graph[tr.src].append(tr)

    # Find expanding self-loops and 2-cycles
    expanding_self = []
    for tr in transitions:
        if tr.src == tr.dst and tr.expand and tr.alpha >= 1:
            # q' = alpha q + beta >= q for large q needs alpha > 1 or (alpha==1 and beta>=0)
            if tr.alpha > 1 or (tr.alpha == 1 and tr.beta >= 0):
                expanding_self.append(
                    {
                        "port": f"mod {tr.src.M} r={tr.src.r}",
                        "word": tr.word,
                        "alpha": tr.alpha,
                        "beta": tr.beta,
                        "N/M": f"{tr.N}/{tr.M}",
                        "height_ratio": height_ratio(tr),
                    }
                )

    two_cycles = []
    # Index transitions by src
    by_src = defaultdict(list)
    for tr in transitions:
        by_src[tr.src].append(tr)

    checked = 0
    for tr1 in transitions:
        if not tr1.expand:
            continue
        for tr2 in by_src[tr1.dst]:
            if tr2.dst != tr1.src:
                continue
            checked += 1
            # composed q -> alpha2(alpha1 q + beta1) + beta2
            A = tr2.alpha * tr1.alpha
            B = tr2.alpha * tr1.beta + tr2.beta
            net_ratio = height_ratio(tr1) * height_ratio(tr2)
            if A > 1 or (A == 1 and B >= 0):
                # distinct words / ports for nontriviality
                if tr1.word != tr2.word or tr1.src != tr1.dst:
                    two_cycles.append(
                        {
                            "port1": f"mod {tr1.src.M} r={tr1.src.r}",
                            "port2": f"mod {tr1.dst.M} r={tr1.dst.r}",
                            "word1": tr1.word,
                            "word2": tr2.word,
                            "compose_alpha": A,
                            "compose_beta": B,
                            "net_height_ratio": net_ratio,
                            "both_expand": tr1.expand and tr2.expand,
                        }
                    )
            if len(two_cycles) >= 50:
                break
        if len(two_cycles) >= 50:
            break

    # Creative variant: forward alternating growth on a single arithmetic progression
    # using two words with SAME modulus (same L) but different residues — impossible
    # for one n. Instead: search residue-changing walks of length 2..4 with net mu>1
    # and verify on concrete seeds.
    seed_hits = []
    for tr1, tr2 in zip(transitions, transitions[1:]):
        pass

    # Concrete seed search: start from n in 1..N0, apply any compatible supercritical
    # block greedily whenever available; see if we can survive S steps with growth.
    # This is exploratory, not a certificate.
    greedy_stats = greedy_supercritical_walks(blocks, n_max=5000, steps=30)

    # Analyze self-loops: an expanding self-loop means H(q)=alpha q+beta on one port.
    # Infinite iteration from finite q0 gives divergence IF every iterate stays in port
    # — which it does by construction. BUT the parity itinerary is then purely periodic
    # (word repeated), which yields a rational fixed point / 2-adic cycle, not a new
    # positive divergent orbit unless the seed is already that divergent thing.
    # Record this trap explicitly.
    periodic_trap = []
    for item in expanding_self[:20]:
        # fixed point of q -> alpha q + beta: q = beta/(1-alpha) if alpha!=1
        alpha, beta = item["alpha"], item["beta"]
        if alpha != 1:
            # n = M q + r with q = beta/(1-alpha)
            # forward map on n is multiplication by N/M plus const — fixed point negative
            periodic_trap.append(
                {
                    **item,
                    "note": "pure self-loop ⇒ periodic word ⇒ not an aperiodic integer Schottky walk",
                }
            )

    # Look for SCC-like pairs with BOTH transitions expanding and ports DISTINCT
    distinct_expanding_two_cycles = [
        c for c in two_cycles if c["port1"] != c["port2"] and c["both_expand"] and c["compose_alpha"] > 1
    ]

    return {
        "Lmax": Lmax,
        "blocks": len(blocks),
        "ports": len(ports),
        "transitions": len(transitions),
        "expanding_self_loops": len(expanding_self),
        "expanding_self_loop_examples": expanding_self[:15],
        "two_cycle_candidates_checked": checked,
        "two_cycle_hits": len(two_cycles),
        "two_cycle_examples": two_cycles[:20],
        "distinct_expanding_two_cycles": len(distinct_expanding_two_cycles),
        "distinct_expanding_two_cycle_examples": distinct_expanding_two_cycles[:20],
        "periodic_trap_examples": periodic_trap[:10],
        "greedy_walks": greedy_stats,
    }


def greedy_supercritical_walks(blocks: list[Block], n_max: int, steps: int) -> dict:
    super_blocks = [b for b in blocks if b.N > b.M]
    # index by residue mod M — multiple M
    by_mod: dict[int, list[Block]] = defaultdict(list)
    for b in super_blocks:
        by_mod[b.M].append(b)

    survivors = 0
    best_growth = 1.0
    best_trace = None
    for n0 in range(1, n_max + 1):
        n = n0
        trace = []
        ok = True
        for _ in range(steps):
            applied = False
            # try larger blocks first
            for M in sorted(by_mod.keys(), reverse=True):
                r = n % M
                for b in by_mod[M]:
                    if b.r == r:
                        n = apply_block(n, b)
                        trace.append(b.word)
                        applied = True
                        break
                if applied:
                    break
            if not applied or n is None or n <= 0:
                ok = False
                break
        if ok and n > n0:
            survivors += 1
            growth = n / n0
            if growth > best_growth:
                best_growth = growth
                best_trace = {"n0": n0, "n_final": n, "growth": growth, "words": trace[:10]}
    return {
        "n_max": n_max,
        "steps": steps,
        "survivors_with_growth": survivors,
        "best": best_trace,
    }


def projective_displacement_experiment(Lmax: int = 10) -> dict:
    """Creative probe: treat log-displacements a*log3 - L*log2 as vectors and
    ask whether two mildly supercritical displacements can alternate while an
    explicit integer seed realizes both residue constraints in turn.

    This is a speculative reformulation of 2-port search in log coordinates.
    """
    mild = []
    for L in range(1, Lmax + 1):
        for mask in range(1 << L):
            word = format(mask, f"0{L}b")[::-1]
            a = word.count("1")
            if a == 0:
                continue
            mu = Fraction(3**a, 1 << L)
            if 1 < mu <= Fraction(3, 2):
                mild.append(make_block(word))

    # Try pairs with distinct L or residues; seek n that follows w1 then lands
    # in residue of w2, etc., for several alternations.
    alternations_found = []
    for b1, b2 in zip(mild, mild[1:]):
        # brute seeds
        for n0 in range(1, 20000):
            n = n0
            ok = True
            depths = []
            for i in range(6):
                b = b1 if i % 2 == 0 else b2
                if n % b.M != b.r:
                    ok = False
                    break
                n = (b.N * n + b.B) // b.M
                depths.append(n)
            if ok and depths[-1] > n0 * 2:
                alternations_found.append(
                    {
                        "n0": n0,
                        "word1": b1.word,
                        "word2": b2.word,
                        "final": depths[-1],
                        "growth": depths[-1] / n0,
                    }
                )
                break
        if len(alternations_found) >= 10:
            break

    return {
        "mild_blocks": len(mild),
        "alternation_hits": len(alternations_found),
        "examples": alternations_found,
    }


def main() -> None:
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    summary = search_ports(Lmax=9)
    proj = projective_displacement_experiment(Lmax=9)
    summary["projective_probe"] = proj
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        f"Lmax={summary['Lmax']}",
        f"blocks={summary['blocks']} ports={summary['ports']} transitions={summary['transitions']}",
        f"expanding self-loops={summary['expanding_self_loops']}",
        f"two-cycle hits={summary['two_cycle_hits']}",
        f"distinct expanding two-cycles={summary['distinct_expanding_two_cycles']}",
        f"greedy survivors={summary['greedy_walks']['survivors_with_growth']} best={summary['greedy_walks']['best']}",
        f"projective alternation hits={proj['alternation_hits']}",
        "",
        "distinct expanding two-cycle examples:",
    ]
    for c in summary["distinct_expanding_two_cycle_examples"][:10]:
        lines.append(
            f"  {c['port1']} --{c['word1']}--> {c['port2']} --{c['word2']}--> "
            f"compose α={c['compose_alpha']} β={c['compose_beta']} net~{c['net_height_ratio']:.4f}"
        )
    if proj["examples"]:
        lines.append("projective examples:")
        for e in proj["examples"][:5]:
            lines.append(
                f"  n0={e['n0']} words={e['word1']}/{e['word2']} growth={e['growth']:.3f}"
            )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
