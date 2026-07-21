#!/usr/bin/env python3
"""X-0101: census of affine Collatz blocks (exact integers / rationals).

Recomputes affine data for every chronological parity word of length <= Lmax,
verifies the affine iterate formula on the word's residue class, and records
supercritical / near-critical statistics used by the Schottky search.
"""

from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path


def T(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative for this census")
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def B_of(word: str) -> int:
    ones = word.count("1")
    seen = 0
    total = 0
    for j, bit in enumerate(word):
        if bit == "1":
            seen += 1
            total += (1 << j) * (3 ** (ones - seen))
        elif bit != "0":
            raise ValueError(bit)
    return total


def residue_of(word: str) -> int:
    """Unique residue mod 2^L realizing the chronological parity word."""
    L = len(word)
    # Solve successive constraints by building from the first bit.
    # r mod 2 determines t0; after each T, next parity is determined.
    # Easiest exact method: test all residues (L small) — replaced below by
    # constructive lift for speed.
    mod = 1 << L
    # Constructive: start with candidates mod 2, lift bit by bit.
    candidates = [0, 1]
    if word[0] == "0":
        candidates = [0]
    else:
        candidates = [1]
    for k in range(1, L):
        lifted = []
        half = 1 << k
        need = int(word[k])
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
        if not candidates:
            raise RuntimeError(f"no residue for {word}")
    # Unique mod 2^L
    assert len(candidates) == 1, (word, candidates)
    return candidates[0] % mod


def follow(n: int, L: int) -> tuple[str, int]:
    bits = []
    x = n
    for _ in range(L):
        bits.append(str(x & 1))
        x = T(x)
    return "".join(bits), x


@dataclass(frozen=True)
class Block:
    word: str
    L: int
    a: int
    B: int
    residue: int
    s: int
    mu_num: int
    mu_den: int
    supercritical: bool
    log_mu: float
    fp: str  # Fraction as string
    tau: str

    @property
    def mu(self) -> Fraction:
        return Fraction(self.mu_num, self.mu_den)


def build_block(word: str) -> Block:
    L = len(word)
    a = word.count("1")
    B = B_of(word)
    r = residue_of(word)
    got_word, s = follow(r, L)
    assert got_word == word, (word, got_word, r)
    # Affine check
    assert (3**a * r + B) == s * (1 << L)
    mu_num = 3**a
    mu_den = 1 << L
    supercritical = mu_num > mu_den
    log_mu = a * math.log(3) - L * math.log(2)
    if mu_num != mu_den:
        fp = Fraction(-B, mu_num - mu_den)
    else:
        fp = Fraction(0, 1)  # sentinel unused
    tau = Fraction(B, mu_den)
    return Block(
        word=word,
        L=L,
        a=a,
        B=B,
        residue=r,
        s=s,
        mu_num=mu_num,
        mu_den=mu_den,
        supercritical=supercritical,
        log_mu=log_mu,
        fp=str(fp),
        tau=str(tau),
    )


def all_words(L: int):
    for mask in range(1 << L):
        yield format(mask, f"0{L}b")[::-1]  # chronological: bit0 = LSB of mask


def census(Lmax: int) -> dict:
    blocks: list[Block] = []
    verified = 0
    for L in range(1, Lmax + 1):
        for word in all_words(L):
            b = build_block(word)
            blocks.append(b)
            # lift check for q=0..3
            M = 1 << L
            for q in range(4):
                n = M * q + b.residue
                w2, out = follow(n, L)
                assert w2 == word
                assert out == (3**b.a * n + b.B) // M
                verified += 1

    super_blocks = [b for b in blocks if b.supercritical]
    super_blocks.sort(key=lambda b: (abs(b.log_mu), b.L, b.word))

    mild = [
        b
        for b in super_blocks
        if 0 < b.log_mu <= math.log(1.5)  # mu in (1, 1.5]
    ]

    summary = {
        "Lmax": Lmax,
        "total_words": len(blocks),
        "affine_lift_checks": verified,
        "supercritical_count": len(super_blocks),
        "mild_supercritical_mu_le_1_5": len(mild),
        "smallest_log_mu_supercritical": [
            {
                "word": b.word,
                "L": b.L,
                "a": b.a,
                "mu": f"{b.mu_num}/{b.mu_den}",
                "log_mu": b.log_mu,
                "residue": b.residue,
                "B": b.B,
                "fp": b.fp,
                "tau": b.tau,
            }
            for b in super_blocks[:25]
        ],
        "mild_examples": [
            {
                "word": b.word,
                "L": b.L,
                "a": b.a,
                "mu": f"{b.mu_num}/{b.mu_den}",
                "log_mu": b.log_mu,
                "residue": b.residue,
                "tau": b.tau,
                "fp": b.fp,
            }
            for b in mild[:40]
        ],
    }
    return summary


def main() -> None:
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    summary = census(Lmax=14)
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        f"Lmax = {summary['Lmax']}",
        f"total words = {summary['total_words']}",
        f"affine lift checks = {summary['affine_lift_checks']}",
        f"supercritical = {summary['supercritical_count']}",
        f"mild supercritical (mu<=1.5) = {summary['mild_supercritical_mu_le_1_5']}",
        "",
        "smallest log_mu supercritical:",
    ]
    for row in summary["smallest_log_mu_supercritical"][:15]:
        lines.append(
            f"  L={row['L']} a={row['a']} mu={row['mu']} log_mu={row['log_mu']:.6f} word={row['word']}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
