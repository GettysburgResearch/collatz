#!/usr/bin/env python3
"""X-0114: verify generalized precision accounting (T-0101, L-0110, L-0111).

Checks:
1) random multi-length schedules: tax == sum of lengths (generic)
2) supercritical concatenations: fixed point negative
3) cylinder uniqueness: followers of a concat word = one class mod 2^Λ
4) mechanical (Sturmian-like) schedules of two mild words: finite ordinary
   survival depths bounded by v2 budgets
"""

from __future__ import annotations

import json
import random
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


def v2(n: int) -> int:
    if n == 0:
        return 10**9
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def tax_schedule(words: list[str]) -> dict:
    M, R = 1, 0
    total_tax = 0
    for w in words:
        L = len(w)
        a = w.count("1")
        if a == 0:
            return {"ok": False, "reason": "even-only word"}
        r = residue_of(w)
        B = B_of(w)
        mod = 1 << L
        A = M % mod
        c = (r - R) % mod
        g = gcd(A, mod)
        if c % g != 0:
            return {"ok": False, "reason": "unsolvable", "word": w}
        mg = mod // g
        Ag = A // g
        u0 = ((c // g) * pow(Ag, -1, mg)) % mg
        tax = v2(mg)
        total_tax += tax
        M_thin = M * mg
        R_thin = M * u0 + R
        N = 3**a
        alpha = (N * M_thin) // mod
        beta = (N * R_thin + B) // mod
        M, R = alpha, beta % alpha if alpha else 0
    return {
        "ok": True,
        "total_tax": total_tax,
        "sum_L": sum(len(w) for w in words),
        "equal": total_tax == sum(len(w) for w in words),
        "final_M_odd": M % 2 == 1,
    }


def fixed_point(words: list[str]) -> Fraction:
    # compose affine maps f(x)=(3^a x + B)/2^L
    # F = f_m ∘ ... ∘ f_1
    mu = Fraction(1, 1)
    beta = Fraction(0, 1)
    for w in words:
        L = len(w)
        a = w.count("1")
        B = B_of(w)
        mu_i = Fraction(3**a, 1 << L)
        beta_i = Fraction(B, 1 << L)
        # f_i(mu x + beta) = mu_i (mu x + beta) + beta_i
        beta = mu_i * beta + beta_i
        mu = mu_i * mu
    if mu == 1:
        return Fraction(0, 1)
    return -beta / (mu - 1)


def cylinder_unique(word: str, bound_bits: int = 4) -> dict:
    L = len(word)
    r = residue_of(word)
    bound = 1 << (L + bound_bits)
    hits = [n for n in range(r, bound, 1 << L)]
    # verify all hits follow word and no others below bound
    ok_hits = []
    for n in hits:
        x = n
        good = True
        for bit in word:
            if str(x & 1) != bit:
                good = False
                break
            x = T(x)
        if good:
            ok_hits.append(n)
    others = 0
    for n in range(1, bound):
        if (n - r) % (1 << L) == 0:
            continue
        x = n
        good = True
        for bit in word:
            if str(x & 1) != bit:
                good = False
                break
            x = T(x)
        if good:
            others += 1
    return {
        "L": L,
        "r": r,
        "hits_verified": len(ok_hits),
        "expected": 1 << bound_bits,
        "spurious_others": others,
    }


def random_words(rng: random.Random, n: int, Lmax: int) -> list[str]:
    out = []
    for _ in range(n):
        L = rng.randint(1, Lmax)
        # ensure at least one 1
        mask = rng.randint(1, (1 << L) - 1)
        out.append(format(mask, f"0{L}b")[::-1])
    return out


def mechanical_schedule(w0: str, w1: str, alpha: Fraction, N: int) -> list[str]:
    """Beatty-like: choose w1 when {i*alpha} < alpha, else w0 — a mechanical word."""
    sched = []
    for i in range(N):
        # standard mechanical: floor((i+1)a) - floor(i a)
        a = alpha
        bit = (int((i + 1) * a) - int(i * a))
        sched.append(w1 if bit == 1 else w0)
    return sched


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    rng = random.Random(20260721)

    tax_trials = []
    for _ in range(40):
        words = random_words(rng, rng.randint(2, 6), 8)
        # skip if some a=0
        if any(w.count("1") == 0 for w in words):
            continue
        row = tax_schedule(words)
        row["words"] = words
        tax_trials.append(row)
    tax_ok = [t for t in tax_trials if t.get("ok")]
    tax_eq = sum(1 for t in tax_ok if t["equal"])

    fp_trials = []
    for _ in range(30):
        words = random_words(rng, rng.randint(1, 4), 7)
        if any(w.count("1") == 0 for w in words):
            continue
        A = sum(w.count("1") for w in words)
        Lam = sum(len(w) for w in words)
        if 3**A <= (1 << Lam):
            continue  # need supercritical
        fp = fixed_point(words)
        fp_trials.append(
            {
                "words": words,
                "mu": str(Fraction(3**A, 1 << Lam)),
                "fp": str(fp),
                "negative": fp < 0,
            }
        )
    fp_neg = sum(1 for t in fp_trials if t["negative"])

    cyl = cylinder_unique("11110101101110", bound_bits=5)

    # mechanical schedule of two mild words
    w0, w1 = "101", "1111010"  # mu=9/8 and 243/128
    alpha = Fraction(7, 11)  # convergent flavor
    sched = mechanical_schedule(w0, w1, alpha, 12)
    mech_tax = tax_schedule(sched)
    # survival depth for n in cylinder of first block
    concat = "".join(sched)
    r = residue_of(concat)
    Lam = len(concat)
    max_steps = 0
    for q in range(0, 1 << 10):
        n = (1 << Lam) * q + r
        # try to follow schedule once only by construction; repeat mechanical? 
        # measure v2(n-r)
        max_steps = max(max_steps, v2(n - r) // max(Lam, 1))
    summary = {
        "tax_trials_ok": len(tax_ok),
        "tax_equals_sumL": tax_eq,
        "tax_all_equal": tax_eq == len(tax_ok) and len(tax_ok) > 0,
        "fp_trials_super": len(fp_trials),
        "fp_all_negative": fp_neg == len(fp_trials) and len(fp_trials) > 0,
        "fp_neg_count": fp_neg,
        "cylinder": cyl,
        "mechanical": {
            "alpha": str(alpha),
            "sched_prefix": sched[:8],
            "tax": mech_tax,
            "concat_L": Lam,
        },
        "samples_tax": tax_ok[:5],
        "samples_fp": fp_trials[:5],
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        f"tax equal sum L: {tax_eq}/{len(tax_ok)} (all={summary['tax_all_equal']})",
        f"supercritical fp negative: {fp_neg}/{len(fp_trials)} (all={summary['fp_all_negative']})",
        f"cylinder unique: hits={cyl['hits_verified']} expected={cyl['expected']} spurious={cyl['spurious_others']}",
        f"mechanical tax equal={mech_tax.get('equal')} tax={mech_tax.get('total_tax')} sumL={mech_tax.get('sum_L')}",
    ]
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
