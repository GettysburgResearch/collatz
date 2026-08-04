#!/usr/bin/env python3
"""X-0127: typed multi-block concatenated cycle sieve.

Search structured families of chronological words built by concatenating short
affine blocks:

  1. All concatenations of k∈{2,3} short library blocks with total L≤Lmax,
     overall subcritical, exact integrality of n=B/(2^L-3^a).
  2. Supercritical+subcritical "sandwich" pairs (growth then descent) with
     overall subcritical — the natural multi-block cycle shape.
  3. Pure powers u^k of a short seed u, overall subcritical.

Hits with n>2 and verified itinerary are K-candidates.
"""

from __future__ import annotations

import json
from itertools import product
from math import log
from pathlib import Path


def B_of(word: str) -> int:
    ones = word.count("1")
    seen = 0
    total = 0
    for j, bit in enumerate(word):
        if bit == "1":
            seen += 1
            total += (1 << j) * (3 ** (ones - seen))
    return total


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def follows_cycle(n: int, word: str) -> bool:
    x = n
    for bit in word:
        if str(x & 1) != bit:
            return False
        x = T(x)
    return x == n


def density(word: str) -> float:
    return word.count("1") / len(word) if word else 0.0


LOG32 = log(2) / log(3)


def classify(word: str) -> str:
    d = density(word)
    if d > LOG32 + 1e-15:
        return "super"
    if d < LOG32 - 1e-15:
        return "sub"
    return "critical"


def check_word(word: str) -> dict | None:
    L = len(word)
    a = word.count("1")
    if a == 0:
        return None
    den = (1 << L) - 3**a
    if den <= 0:
        return None  # not positive-cycle regime
    B = B_of(word)
    if B % den != 0:
        return None
    n = B // den
    if n <= 2:
        return {"word": word, "n": n, "trivial": True, "verified": follows_cycle(n, word)}
    ok = follows_cycle(n, word)
    return {
        "word": word,
        "L": L,
        "a": a,
        "n": n,
        "trivial": False,
        "verified": ok,
    }


def short_library(Lmax: int = 6) -> list[str]:
    lib = []
    for L in range(1, Lmax + 1):
        for mask in range(1 << L):
            w = format(mask, f"0{L}b")[::-1]
            if "1" in w:
                lib.append(w)
    return lib


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)

    lib = short_library(5)
    by_type = {"super": [], "sub": [], "critical": []}
    for w in lib:
        by_type[classify(w)].append(w)

    checked = 0
    hits = []
    trivial_hits = []
    family_stats = {
        "concat2": {"checked": 0, "divisible": 0},
        "concat3": {"checked": 0, "divisible": 0},
        "sandwich": {"checked": 0, "divisible": 0},
        "powers": {"checked": 0, "divisible": 0},
    }

    # 1) all 2-block concatenations with total L <= 14
    for u, v in product(lib, lib):
        w = u + v
        if len(w) > 14:
            continue
        family_stats["concat2"]["checked"] += 1
        checked += 1
        rec = check_word(w)
        if rec:
            family_stats["concat2"]["divisible"] += 1
            (trivial_hits if rec.get("trivial") else hits).append(
                {**rec, "family": "concat2", "parts": [u, v]}
            )

    # 2) 3-block concatenations with total L <= 12
    short3 = [w for w in lib if len(w) <= 4]
    for u, v, z in product(short3, short3, short3):
        w = u + v + z
        if len(w) > 12:
            continue
        family_stats["concat3"]["checked"] += 1
        checked += 1
        rec = check_word(w)
        if rec:
            family_stats["concat3"]["divisible"] += 1
            (trivial_hits if rec.get("trivial") else hits).append(
                {**rec, "family": "concat3", "parts": [u, v, z]}
            )

    # 3) sandwich: super then sub, overall subcritical, L<=16
    for u in by_type["super"]:
        for v in by_type["sub"]:
            w = u + v
            if len(w) > 16:
                continue
            if classify(w) != "sub":
                continue
            family_stats["sandwich"]["checked"] += 1
            checked += 1
            rec = check_word(w)
            if rec:
                family_stats["sandwich"]["divisible"] += 1
                (trivial_hits if rec.get("trivial") else hits).append(
                    {**rec, "family": "sandwich", "parts": [u, v]}
                )
            # also sub then super
            w2 = v + u
            if len(w2) <= 16 and classify(w2) == "sub":
                family_stats["sandwich"]["checked"] += 1
                checked += 1
                rec2 = check_word(w2)
                if rec2:
                    family_stats["sandwich"]["divisible"] += 1
                    (trivial_hits if rec2.get("trivial") else hits).append(
                        {**rec2, "family": "sandwich", "parts": [v, u]}
                    )

    # 4) powers u^k
    for u in lib:
        for k in range(2, 12):
            w = u * k
            if len(w) > 18:
                break
            if classify(w) != "sub":
                continue
            family_stats["powers"]["checked"] += 1
            checked += 1
            rec = check_word(w)
            if rec:
                family_stats["powers"]["divisible"] += 1
                (trivial_hits if rec.get("trivial") else hits).append(
                    {**rec, "family": "powers", "parts": [u], "k": k}
                )

    # dedupe by word
    def dedupe(rows):
        seen = set()
        out = []
        for r in rows:
            if r["word"] in seen:
                continue
            seen.add(r["word"])
            out.append(r)
        return out

    hits = dedupe(hits)
    trivial_hits = dedupe(trivial_hits)
    verified_nontrivial = [h for h in hits if h.get("verified")]

    summary = {
        "checked": checked,
        "family_stats": family_stats,
        "lib_sizes": {k: len(v) for k, v in by_type.items()},
        "nontrivial_hits": hits,
        "verified_nontrivial": verified_nontrivial,
        "trivial_hits_count": len(trivial_hits),
        "trivial_examples": trivial_hits[:20],
        "conclusion": (
            "Typed multi-block cycle sieve over short concatenations, "
            "super/sub sandwiches, and powers; nontrivial verified hits "
            "would be K-candidates."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"checked={checked} nontrivial={len(hits)} verified_nontrivial={len(verified_nontrivial)} trivial={len(trivial_hits)}",
    ]
    for fam, st in family_stats.items():
        lines.append(f"  {fam}: checked={st['checked']} divisible={st['divisible']}")
    for h in verified_nontrivial[:10]:
        lines.append(f"  HIT n={h['n']} word={h['word']} family={h['family']}")
    if not verified_nontrivial:
        lines.append("  (no verified nontrivial positive cycles in scanned families)")
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
