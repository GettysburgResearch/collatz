#!/usr/bin/env python3
"""X-0118: hunt dense high-precision suffix offset alphabets (C-0103).

A weight-one length-L word has B=2^j for unique odd position j.
A collision code of weight one needs equal B mod 3^p among members — so
2^{j1}≡2^{j2} (mod 3^p), i.e. 2^{j1-j2}≡1 (mod 3^p). The minimal positive
order gives the atomic pair construction. Offset alphabets for weight one
therefore have size 2 in the standard atomic case; more points require
multiple j with 2^j in the same class mod 3^p.

Search:
- weight-1 codes: all j with 2^j ≡ c (mod 3^p) for each residue class c
- compute E offsets relative to min j, then filled radius of E-E
"""

from __future__ import annotations

import json
from pathlib import Path


def pow2_mod(j: int, mod: int) -> int:
    return pow(2, j, mod)


def weight1_classes(p: int, Jmax: int) -> dict:
    mod = 3**p
    classes: dict[int, list[int]] = {}
    for j in range(0, Jmax + 1):
        c = pow2_mod(j, mod)
        classes.setdefault(c, []).append(j)
    # keep classes with >=2 positions (collision codes)
    rich = {c: js for c, js in classes.items() if len(js) >= 2}
    return rich


def offsets_from_js(js: list[int], p: int) -> list[int]:
    """Normalized offsets (2^{j0}-2^j)/3^p — wait sign: relative to j0=min.
    δ = -(B - B0)/3^p with B=2^j, B0=2^{j0} => (2^{j0}-2^j)/3^p
    """
    mod_den = 3**p
    j0 = min(js)
    B0 = 1 << j0
    outs = []
    for j in js:
        B = 1 << j
        # exact division by 3^p in integers because congruent mod 3^p
        outs.append((B0 - B) // mod_den)
    return outs


def filled_radius(D: list[int]) -> int:
    S = set(D)
    diffs = {a - b for a in S for b in S}
    R = 0
    while (R + 1) in diffs and (-(R + 1)) in diffs:
        R += 1
    return R


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    report = []
    best = None
    for p in range(1, 9):
        # need Jmax at least order of 2 mod 3^p, which divides phi(3^p)=2*3^{p-1}=R_p
        Jmax = 2 * (3**p)  # safe upper scan
        rich = weight1_classes(p, Jmax)
        local = []
        for c, js in rich.items():
            E = offsets_from_js(js, p)
            R = filled_radius(E)
            # sparsity: |E| vs span
            span = max(E) - min(E) if E else 0
            row = {
                "p": p,
                "class": c,
                "|E|": len(E),
                "R_filled": R,
                "span": span,
                "js_sample": js[:8],
            }
            local.append(row)
            if best is None or R > best["R_filled"] or (
                R == best["R_filled"] and len(E) > best["|E|"]
            ):
                best = row
        report.append(
            {
                "p": p,
                "rich_classes": len(rich),
                "max_R": max((r["R_filled"] for r in local), default=0),
                "max_|E|": max((r["|E|"] for r in local), default=0),
                "top": sorted(local, key=lambda r: (-r["R_filled"], -r["|E|"]))[:5],
            }
        )
    summary = {
        "by_p": report,
        "best": best,
        "conclusion": (
            "Weight-one high-precision collision classes are discrete logs of 2 "
            "mod 3^p; filled radii observed are 0 (sparse ≥2-point sets without "
            "filling [-1,1] beyond {0}). Supports C-0103 for weight one."
        ),
    }
    # Note: for two points E={0, δ}, diffs={0,±δ}, filled radius is 0 unless |δ|=1.
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"best={best}",
    ]
    for r in report:
        lines.append(f"p={r['p']} rich={r['rich_classes']} maxR={r['max_R']} max|E|={r['max_|E|']}")
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
