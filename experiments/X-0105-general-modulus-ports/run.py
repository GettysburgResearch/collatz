#!/usr/bin/env python3
"""X-0105: integer Schottky search with general-modulus ports.

Ports are arithmetic progressions n = M q + r for arbitrary M>=1, not only
powers of two. An accelerated word applies when the progression can be thinned
to meet the word's residue constraint mod 2^L; the image is again an AP.

This is the corrected integer specialization of D-0102 after observing that
power-of-two destination ports admit no universal transitions (3^a is odd).
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
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

    @property
    def M2(self) -> int:
        return 1 << self.L

    @property
    def N(self) -> int:
        return 3**self.a

    @property
    def mu(self) -> Fraction:
        return Fraction(self.N, self.M2)


@dataclass(frozen=True)
class Port:
    M: int
    r: int

    def __post_init__(self):
        object.__setattr__(self, "r", self.r % self.M)


@dataclass(frozen=True)
class Edge:
    src: Port
    dst: Port
    word: str
    # parameter map q |-> alpha q + beta on the THINNED source progression
    # source thinning: n = M_thin * u + r_thin, with M_thin multiple of src.M
    M_thin: int
    r_thin: int
    alpha: int
    beta: int

    @property
    def height_ratio(self) -> Fraction:
        # n ~ M_thin u, n' ~ dst.M * (alpha u) = dst.M * alpha / M_thin * n
        return Fraction(self.dst.M * self.alpha, self.M_thin)


def make_blocks(Lmax: int) -> list[Block]:
    blocks = []
    for L in range(1, Lmax + 1):
        for mask in range(1 << L):
            word = format(mask, f"0{L}b")[::-1]
            a = word.count("1")
            if a == 0:
                continue
            B = B_of(word)
            r = residue_of(word)
            # s = T^L(r)
            x = r
            for _ in range(L):
                x = T(x)
            blocks.append(Block(word, L, a, B, r, x))
    return blocks


def solve_congruence(M: int, r: int, mod: int, target: int):
    """Solve M q + r ≡ target (mod mod). Return (M_thin, r_thin) for q-parameter u,
    where q = (mod/g) u + q0, n = M q + r = (M mod/g) u + (M q0 + r).
    Or None if impossible.
    """
    # M q ≡ target - r (mod mod)
    A = M % mod
    b = (target - r) % mod
    g = gcd(A, mod)
    if b % g != 0:
        return None
    # Solve (A/g) q ≡ (b/g) (mod mod/g)
    Ag, mg, bg = A // g, mod // g, b // g
    inv = pow(Ag, -1, mg)
    q0 = (bg * inv) % mg
    # q = mg * u + q0
    M_thin = M * mg
    r_thin = M * q0 + r
    return M_thin, r_thin % M_thin, mg, q0


def edge_apply(block: Block, src: Port) -> Edge | None:
    """Thin src to meet block residue; image becomes an AP port."""
    sol = solve_congruence(src.M, src.r, block.M2, block.r)
    if sol is None:
        return None
    M_thin, r_thin, mg, q0 = sol
    # n = M_thin u + r_thin
    # T^L(n) = (N n + B)/M2 = (N M_thin / M2) u + (N r_thin + B)/M2
    if (block.N * r_thin + block.B) % block.M2 != 0:
        return None
    if (block.N * M_thin) % block.M2 != 0:
        # May still hold for all u if N*M_thin / M2 is integer — check
        return None
    alpha = (block.N * M_thin) // block.M2
    beta = (block.N * r_thin + block.B) // block.M2
    # Image AP: n' = alpha u + beta = alpha (u) + beta, as port (alpha, beta) if we
    # write n' = alpha * u + beta. That's Port(M=alpha, r=beta) with parameter u,
    # but only if we treat step-1 in u. Equivalently Port(gcd?).
    # Standard: n' runs over alpha u + beta, so M_dst = alpha, r_dst = beta % alpha? 
    # Careful: as u runs over Z>=0, n' = alpha u + beta is AP with modulus |alpha|.
    if alpha <= 0:
        return None
    dst = Port(alpha, beta % alpha) if alpha else None
    # Wait: n' = alpha u + beta, modulus alpha, residue beta mod alpha — yes Port(alpha, beta%alpha)
    # But then parameter u maps as identity: n' = alpha u + (beta%alpha) + alpha*floor...
    # Actually beta = alpha*k + (beta%alpha), so n' = alpha (u+k) + (beta%alpha).
    # Reparameterize u' = u + k, alpha'=1? Better keep dst = Port(M=alpha, r=beta%alpha)
    # and parameter map u |-> u + k with k = beta // alpha, so new edge alpha_param=1, beta_param=k.
    # For height, n' ~ alpha u, n ~ M_thin u, ratio alpha/M_thin = N/M2 = mu. Good.
    k = beta // alpha
    r_dst = beta % alpha
    dst = Port(alpha, r_dst)
    return Edge(src, dst, block.word, M_thin, r_thin, 1, k)


def build_seed_ports(blocks: list[Block]) -> list[Port]:
    ports = []
    for b in blocks:
        ports.append(Port(b.M2, b.r))  # native 2-power ports
        ports.append(Port(b.N, b.s % b.N))  # native image 3-power ports
    # unique
    return sorted(set(ports), key=lambda p: (p.M, p.r))


def search(Lmax: int) -> dict:
    blocks = make_blocks(Lmax)
    ports = build_seed_ports(blocks)
    # Also include unit port
    ports = sorted(set(ports + [Port(1, 0)]), key=lambda p: (p.M, p.r))

    edges: list[Edge] = []
    for src in ports:
        for b in blocks:
            e = edge_apply(b, src)
            if e is not None:
                edges.append(e)

    # Expanding edges: height ratio > 1
    expanding = [e for e in edges if e.height_ratio > 1]

    # Build graph on ports appearing as src/dst
    by_src: dict[Port, list[Edge]] = {}
    for e in edges:
        by_src.setdefault(e.src, []).append(e)

    # Search 2-cycles with net height > 1 and distinct ports
    two = []
    for e1 in expanding:
        for e2 in by_src.get(e1.dst, []):
            if e2.dst != e1.src:
                continue
            # compose parameter maps on thinned lattices is delicate; use height ratios
            net = e1.height_ratio * e2.height_ratio
            if net > 1 and e1.src != e1.dst:
                two.append(
                    {
                        "src": f"{e1.src.M}Z+{e1.src.r}",
                        "mid": f"{e1.dst.M}Z+{e1.dst.r}",
                        "word1": e1.word,
                        "word2": e2.word,
                        "ratio1": str(e1.height_ratio),
                        "ratio2": str(e2.height_ratio),
                        "net": str(net),
                        "thin1": f"{e1.M_thin}Z+{e1.r_thin}",
                        "thin2": f"{e2.M_thin}Z+{e2.r_thin}",
                    }
                )
            if len(two) >= 40:
                break
        if len(two) >= 40:
            break

    # Verify concrete seeds for top candidates
    verified = []
    for cand in two[:20]:
        # parse thin1
        # Find the edge objects again
        pass

    concrete = verify_concrete_alternators(blocks, max_n=20000, rounds=8)

    return {
        "Lmax": Lmax,
        "blocks": len(blocks),
        "ports": len(ports),
        "edges": len(edges),
        "expanding_edges": len(expanding),
        "two_cycle_candidates": len(two),
        "two_cycle_examples": two[:15],
        "concrete_alternators": concrete,
    }


def verify_concrete_alternators(blocks: list[Block], max_n: int, rounds: int) -> dict:
    """Search pairs of blocks (possibly different L) and seeds that alternate
    for `rounds` rounds with net growth, without requiring universal AP closure.
    This produces EMPIRICAL finite shadows of integer Schottky walks.
    """
    supers = [b for b in blocks if b.N > b.M2]
    supers.sort(key=lambda b: float(Fraction(b.N, b.M2)))
    hits = []
    tested_pairs = 0
    for i, b1 in enumerate(supers[:80]):
        for b2 in supers[i + 1 : i + 40]:
            tested_pairs += 1
            for n0 in range(1, max_n + 1):
                n = n0
                ok = True
                for r in range(rounds):
                    b = b1 if r % 2 == 0 else b2
                    if n % b.M2 != b.r:
                        ok = False
                        break
                    n = (b.N * n + b.B) // b.M2
                if ok and n > n0:
                    hits.append(
                        {
                            "n0": n0,
                            "final": n,
                            "growth": n / n0,
                            "word1": b1.word,
                            "word2": b2.word,
                            "mu1": str(Fraction(b1.N, b1.M2)),
                            "mu2": str(Fraction(b2.N, b2.M2)),
                            "rounds": rounds,
                        }
                    )
                    break
            if len(hits) >= 15:
                return {"tested_pairs": tested_pairs, "hits": hits}
    return {"tested_pairs": tested_pairs, "hits": hits}


def main() -> None:
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    summary = search(Lmax=8)
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        f"Lmax={summary['Lmax']}",
        f"blocks={summary['blocks']} ports={summary['ports']} edges={summary['edges']}",
        f"expanding edges={summary['expanding_edges']}",
        f"two-cycle candidates={summary['two_cycle_candidates']}",
        f"concrete alternator hits={len(summary['concrete_alternators']['hits'])} "
        f"(tested pairs={summary['concrete_alternators']['tested_pairs']})",
        "",
        "two-cycle examples:",
    ]
    for c in summary["two_cycle_examples"][:8]:
        lines.append(
            f"  {c['src']} -{c['word1']}-> {c['mid']} -{c['word2']}-> net={c['net']}"
        )
    lines.append("concrete hits:")
    for h in summary["concrete_alternators"]["hits"][:8]:
        lines.append(
            f"  n0={h['n0']} -> {h['final']} growth={h['growth']:.3f} "
            f"words={h['word1']}/{h['word2']} mu={h['mu1']}/{h['mu2']}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
