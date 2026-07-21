#!/usr/bin/env python3
"""X-0122: heteroclinic path starter — congruence destruction under excursions.

Fix a 2-adic cycle template (periodic word), take deep neighborhoods
n ≡ c mod 2^m, apply a supercritical excursion word, measure surviving
2-adic depth toward the template and archimedean growth.

Labels: EMPIRICAL probe of directions/D-HETEROCLINIC-*.md
"""

from __future__ import annotations

import json
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


def apply_word(n: int, word: str) -> int:
    L = len(word)
    a = word.count("1")
    B = B_of(word)
    return (3**a * n + B) // (1 << L)


def v2_diff(n: int, c: int) -> int:
    d = n - c
    if d == 0:
        return 10**9
    v = 0
    while d % 2 == 0:
        d //= 2
        v += 1
    return v


def template_point(word: str) -> Fraction:
    """2-adic/rational fixed point of periodic word (may be negative)."""
    L = len(word)
    a = word.count("1")
    B = B_of(word)
    return Fraction(-B, 3**a - (1 << L)) if 3**a != (1 << L) else Fraction(0)


def excursion_probe(template: str, excursion: str, depths: list[int]) -> dict:
    """c = residue of template repeated to cover depth; actually use fp rounded?
    Better: integer approximations: n = fp + k*2^m in the 2-adic sense is hard
    for negative fp. Use the native residue cylinder of template^k instead.
    """
    # Build deep cylinder for template repeated
    tw = template
    rows = []
    for m in depths:
        # need length >= m bits of constraint: repeat template
        reps = (m + len(tw) - 1) // len(tw)
        prefix = (tw * reps)[:m]
        # followers of prefix: n ≡ r mod 2^m
        # compute r by residue_of for the prefix word — only if prefix is exact word
        # For m not multiple of |tw|, use residue of tw*reps then reduce — actually
        # chronological prefix of length m of tw^ω.
        r = 0
        # construct residue bit by bit from template stream
        # Standard: the unique r mod 2^m with first m parities = prefix
        r = residue_of(prefix)
        # sample several lifts
        best = None
        for q in range(0, 64):
            n0 = (1 << m) * q + r
            if n0 <= 0:
                continue
            # apply excursion if compatible else skip
            er = residue_of(excursion)
            if n0 % (1 << len(excursion)) != er:
                # try CRT merge: need n0 already in excursion class — usually not
                continue
            n1 = apply_word(n0, excursion)
            growth = n1 / n0 if n0 else None
            # surviving depth toward template: v2 of distance to cylinder after return?
            # measure v2(n1 - r) relative to same r? wrong.
            # measure how many template periods fit after excursion
            x = n1
            periods = 0
            L = len(tw)
            tr = residue_of(tw)
            while x % (1 << L) == tr and periods < 40:
                x = apply_word(x, tw)
                periods += 1
            rec = {
                "m": m,
                "q": q,
                "n0": n0,
                "n1": n1,
                "growth": growth,
                "template_periods_after": periods,
            }
            if best is None or periods > best["template_periods_after"]:
                best = rec
        rows.append(
            {
                "m": m,
                "prefix": prefix,
                "r": r,
                "compatible_excursions_found": best is not None,
                "best": best,
                "note": "compatibility of deep template cylinder with excursion residue is rare",
            }
        )
    return {"template": template, "excursion": excursion, "rows": rows}


def crt_gluing_probe(template: str, excursion: str, m: int) -> dict:
    """Solve CRT: n ≡ r_template_prefix (mod 2^m) and n ≡ r_exc (mod 2^{Le}).
    Then apply excursion and measure growth + return depth.
    """
    Le = len(excursion)
    reps = (m + len(template) - 1) // len(template)
    prefix = (template * reps)[:m]
    rt = residue_of(prefix)
    re = residue_of(excursion)
    # CRT mod 2^max
    M1, M2 = 1 << m, 1 << Le
    # n ≡ rt mod M1, n ≡ re mod M2. If m>=Le, need rt ≡ re mod M2.
    if m >= Le:
        if rt % M2 != re % M2:
            return {"ok": False, "reason": "incompatible cylinders", "m": m}
        mod = M1
        r = rt
    else:
        # standard CRT for powers of 2: stronger modulus wins if compatible
        if re % M1 != rt % M1:
            return {"ok": False, "reason": "incompatible", "m": m}
        mod = M2
        r = re
    # sample
    outcomes = []
    Lt = len(template)
    tr = residue_of(template)
    for q in range(0, 32):
        n0 = mod * q + r
        if n0 <= 0:
            continue
        if n0 % (1 << Le) != re:
            continue
        n1 = apply_word(n0, excursion)
        # return depth
        x = n1
        periods = 0
        while x % (1 << Lt) == tr and periods < 60:
            x = apply_word(x, template)
            periods += 1
        outcomes.append(
            {
                "n0": n0,
                "n1": n1,
                "growth": n1 / n0,
                "periods_after": periods,
                "v2_n1_minus_tr": v2_diff(n1, tr) if n1 != tr else None,
            }
        )
    return {
        "ok": True,
        "m": m,
        "mod": mod,
        "r": r,
        "outcomes": outcomes[:10],
        "max_periods_after": max((o["periods_after"] for o in outcomes), default=0),
        "max_growth": max((o["growth"] for o in outcomes), default=None),
    }


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    # templates: (10) related, (100) classic, all-odd short
    templates = ["10", "100", "1"]
    excursions = ["1111010", "11", "101", "1111"]
    glues = []
    for tw in templates:
        fp = template_point(tw)
        for ex in excursions:
            for m in (8, 12, 16, 20):
                g = crt_gluing_probe(tw, ex, m)
                g["template"] = tw
                g["excursion"] = ex
                g["fp"] = str(fp)
                glues.append(g)
    # summarize destruction: periods_after vs m
    usable = [g for g in glues if g.get("ok") and g.get("max_growth") and g["max_growth"] > 1]
    summary = {
        "glues": glues,
        "usable_growth_cases": len(usable),
        "best_usable": sorted(
            usable, key=lambda g: (-(g.get("max_periods_after") or 0), -(g.get("max_growth") or 0))
        )[:15],
        "conclusion": (
            "Deep template cylinders rarely remain compatible with supercritical "
            "excursions; when CRT gluing works, post-excursion template periods "
            "are the congruence-destruction metric."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"usable growth cases={len(usable)} / {len(glues)}",
    ]
    for g in summary["best_usable"][:8]:
        lines.append(
            f"  tpl={g['template']} exc={g['excursion']} m={g['m']} "
            f"periods_after={g['max_periods_after']} growth={g['max_growth']:.3f}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
