#!/usr/bin/env python3
"""X-0108: hunt precision-regenerating transitions with odd destination moduli.

L-0105 kills pure power-of-two image ports. This experiment looks for edges
  port (M,r) --w--> port (M',r')
where M' is divisible by an odd integer (typically 3^b), and the thinning
congruence modulo 2^{L} leaves free binary parameters — i.e. the solution
modulus for q is odd, not a positive power of two.

Such an edge would be a candidate precision-regeneration gadget.
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


def make_blocks(Lmax: int) -> list[Block]:
    out = []
    for L in range(1, Lmax + 1):
        for mask in range(1 << L):
            word = format(mask, f"0{L}b")[::-1]
            a = word.count("1")
            if a == 0:
                continue
            r = residue_of(word)
            x = r
            for _ in range(L):
                x = T(x)
            out.append(Block(word, L, a, B_of(word), r, x))
    return out


def v2(n: int) -> int:
    if n == 0:
        return 10**9
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def analyze_image_ports(blocks: list[Block]) -> dict:
    """For each block, the unrestricted image port is M'=3^a, r'=s.
    Starting from native 2^L port, the enabling constraint is free on that port
    (by definition). The image is exactly the AP 3^a q + s — modulus odd!

    Question: can we chain odd-modulus ports so that the NEXT word's 2-power
    constraint thins only the odd part (index odd) rather than consuming bits?
    That would require the current modulus M (odd) and the constraint mod 2^L
    to interact via CRT: solutions have step lcm(M,2^L)/M = 2^L, so parameter
    step is still 2^L — drain returns when leaving an odd port via a word.
    """
    notes = []
    regen_candidates = []
    for b in blocks:
        # Native: M=2^L, image modulus N=3^a (odd). This CREATE odd modulus.
        # Precision in 2-adic sense: image AP has step 3^a, which is odd, so
        # residues mod 2^k are SURJECTIVE as q varies — free binary digits!
        # That is regeneration: after one block, n' = 3^a q + s runs through
        # all residue classes mod 2^k.
        regen_candidates.append(
            {
                "word": b.word,
                "mu": str(Fraction(b.N, b.M2)),
                "image_modulus": b.N,
                "image_mod_odd": b.N % 2 == 1,
                "covers_all_mod_2k": True,  # because step odd
                "supercritical": b.N > b.M2,
            }
        )
    supers = [c for c in regen_candidates if c["supercritical"]]
    # Chain test: start n=2^L q + r, apply b1 to get 3^a q + s (odd step).
    # Then apply b2 requiring residue r2 mod 2^{L2}: since image hits all
    # classes, there EXISTS q mod 2^{L2} working — thinning index 2^{L2} on q.
    # Net 2-adic precision vs start: start had free q on Z; after enabling b2,
    # q in a class mod 2^{L2}. Same drain! Regeneration of residues ≠ free
    # parameters after the next constraint.
    notes.append(
        "Odd image moduli make residues mod 2^k surjective (regenerate "
        "residues), but imposing the next word constraint still selects an "
        "index-2^{L'} sublattice of the parameter line (L-0105 again)."
    )
    # Look for a DIFFERENT regeneration: destination constraint of odd modulus
    # on an odd-step AP that is automatically satisfied (cofiniteness).
    auto = []
    for b in blocks:
        # Image n' = N q + s. Impose n' ≡ r_odd (mod M_odd) with M_odd odd.
        # N q + s ≡ r_odd (mod M_odd) for ALL q iff M_odd|N and M_odd|(s-r_odd).
        for b2 in blocks:
            Mod = b2.N  # odd
            # Can the image of b lie entirely in a single class mod Mod?
            if b.N % Mod == 0 and (b.s - (b2.s % Mod)) % Mod == 0:
                auto.append(
                    {
                        "word": b.word,
                        "target_mod": Mod,
                        "target_r": b2.s % Mod,
                        "mu": str(Fraction(b.N, b.M2)),
                        "auto_contained": True,
                    }
                )
            if len(auto) >= 20:
                break
        if len(auto) >= 20:
            break

    # More systematic: for each b, factor — image contained in mod 3^j class?
    contained = []
    for b in [x for x in blocks if x.N > x.M2][:200]:
        for j in range(1, b.a + 1):
            Mod = 3**j
            # N q + s mod Mod = (3^a q + s) mod 3^j. If a>=j, N≡0, so constant s mod Mod.
            if b.a >= j:
                contained.append(
                    {
                        "word": b.word,
                        "mod": Mod,
                        "constant_residue": b.s % Mod,
                        "mu": str(Fraction(b.N, b.M2)),
                        "note": "image AP is CONSTANT mod 3^j for j<=a; odd-port auto edge",
                    }
                )
                break
    return {
        "blocks": len(blocks),
        "supercritical_with_odd_image": len(supers),
        "notes": notes,
        "auto_odd_containment_examples": auto[:10],
        "constant_mod_3j_examples": contained[:15],
        "interpretation": (
            "Every supercritical block regenerates 2-adic residue coverage in "
            "its image AP (odd step), AND simultaneously collapses to a "
            "constant class mod 3^j for j<=a. Precision regeneration in the "
            "2-adic direction is real at the residue level, but L-0105 still "
            "taxes parameters when the next edge needs a 2-power port. The "
            "open constructive move is to stay inside odd-modulus ports long "
            "enough to expand height without re-entering 2-power constraints, "
            "or to buy more binary digits than each tax consumes."
        ),
    }


def odd_port_walk_search(blocks: list[Block], max_n: int = 3000) -> dict:
    """Try walks that prefer blocks whose current n already satisfies residue,
    scoring by whether image increases v3-structure. Empirical only.
    """
    supers = [b for b in blocks if b.N > b.M2]
    best = None
    long = 0
    for n0 in range(1, max_n + 1):
        n = n0
        steps = 0
        for _ in range(40):
            opts = [b for b in supers if n % b.M2 == b.r]
            if not opts:
                break
            # choose maximal mu
            opts.sort(key=lambda b: Fraction(b.N, b.M2), reverse=True)
            b = opts[0]
            n = (b.N * n + b.B) // b.M2
            steps += 1
        if steps > long:
            long = steps
            best = {"n0": n0, "steps": steps, "final": n}
    return {"max_n": max_n, "longest_super_only_walk": best}


def main() -> None:
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    blocks = make_blocks(8)
    analysis = analyze_image_ports(blocks)
    walks = odd_port_walk_search(blocks)
    summary = {**analysis, "walks": walks}
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        f"blocks={analysis['blocks']} supercritical odd-image={analysis['supercritical_with_odd_image']}",
        analysis["interpretation"],
        f"longest super-only walk={walks['longest_super_only_walk']}",
        f"constant mod 3^j examples={len(analysis['constant_mod_3j_examples'])}",
    ]
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
