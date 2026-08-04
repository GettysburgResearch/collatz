#!/usr/bin/env python3
"""X-0129: meet-in-the-middle constructive cycle builder.

For subcritical (L,a) near log3(2), search for ones-sets with
B(ones) ≡ 0 (mod 2^L - 3^a) by splitting positions into two halves and
matching partial B-contributions in a hash map.

This is a constructive CRT/modular path beyond uniform random sampling
(X-0126): if a hit exists in the scanned (L,a), MITM finds it (for full
coverage of each half's combinations when binom allows).
"""

from __future__ import annotations

import json
from itertools import combinations
from math import comb, log
from pathlib import Path


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def B_from_ones(ones: tuple[int, ...], L: int, a: int | None = None) -> int:
    if a is None:
        a = len(ones)
    ones_set = set(ones)
    seen = 0
    total = 0
    for j in range(L):
        if j in ones_set:
            seen += 1
            total += (1 << j) * (3 ** (a - seen))
    return total


def follows(n: int, ones: tuple[int, ...], L: int) -> bool:
    ones_set = set(ones)
    x = n
    for j in range(L):
        bit = 1 if j in ones_set else 0
        if (x & 1) != bit:
            return False
        x = T(x)
    return x == n


def mitm_search(L: int, a: int, max_half_binom: int = 200000) -> dict:
    den = (1 << L) - 3**a
    if den <= 0:
        return {"L": L, "a": a, "status": "not_subcritical"}
    positions = list(range(L))
    # split positions
    mid = L // 2
    left_pos = positions[:mid]
    right_pos = positions[mid:]
    hits = []
    # distribute ones: k on left, a-k on right
    maps_built = 0
    pairs_checked = 0
    mode = "mitm"
    for k in range(max(0, a - len(right_pos)), min(a, len(left_pos)) + 1):
        if comb(len(left_pos), k) > max_half_binom:
            mode = "mitm_truncated"
            continue
        if comb(len(right_pos), a - k) > max_half_binom:
            mode = "mitm_truncated"
            continue
        # For fixed total a, B depends on chronological order of ALL ones.
        # Partial B on a half is not independent of the other half's ones count
        # before/after — so we use a corrected split:
        # enumerate left ones-sets fully; for each, the contribution of left
        # positions depends on how many ones appear on the right that are
        # "after" in the global count... Actually B formula:
        #   B = sum_{ones j} 2^j * 3^{a - rank(j)}
        # where rank(j) is 1-based index of j among ones in order.
        # So left contribution depends on how many ones are on the left before
        # each left one, AND the total a (for the exponent), but NOT on right
        # ones' positions — wait: rank is global among all ones. So for a left
        # position j, rank(j) = (# left ones ≤ j) + (# right ones < j).
        # Since right positions are all ≥ mid > j for left j, (# right ones < j)=0.
        # So left ranks depend only on left ones! Left contribution:
        #   B_left = sum 2^j * 3^{a - rank_left(j)}
        # Right contribution: for right j, rank(j) = k + rank_among_right(j).
        #   B_right = sum 2^j * 3^{a - (k + rank_right(j))}
        # Both depend on k and a but are independent across the split. Good.
        left_map: dict[int, list[tuple[int, ...]]] = {}
        for left in combinations(left_pos, k):
            Bl = B_from_ones(left, L, a)  # uses global a; ranks among left only
            # verify: B_from_ones with only left ones uses ranks among those ones
            # which matches rank_left. Exponent uses a - rank — correct.
            left_map.setdefault(Bl % den, []).append(left)
        maps_built += 1
        for right in combinations(right_pos, a - k):
            # B_right with ranks offset by k: equivalent to computing B on right
            # ones alone with total ones a and ranks starting at k+1.
            # B_from_ones(right, L, a) treats ranks among right-only as 1..,
            # but we need ranks k+1, k+2, ...
            # Fix: B_right = sum 2^j * 3^{a - (k + r)} = 3^{-k} * sum 2^j * 3^{a - r}
            # vs B_from_ones(right,L,a) = sum 2^j * 3^{a - r}
            # So B_right = B_from_ones(right,L,a) // 3^k  if exponents work...
            # a - (k+r) = (a-r) - k, so multiply by 3^{-k}:
            # B_right = B_from_ones(right, L, a) // (3**k) only if exact.
            Br_raw = B_from_ones(right, L, a)
            # Each term is 2^j * 3^{a-r}; we need 2^j * 3^{a-k-r} = term / 3^k
            if Br_raw % (3**k) != 0:
                # Should always be divisible since each exponent a-r >= a-(a-k)=k
                # max r is a-k, so a-r >= k. Yes.
                raise RuntimeError("unexpected non-divisibility")
            Br = Br_raw // (3**k)
            need = (-Br) % den
            pairs_checked += 1
            if need not in left_map:
                continue
            for left in left_map[need]:
                ones = tuple(sorted(left + right))
                B = B_from_ones(ones, L, a)
                if B % den != 0:
                    continue
                n = B // den
                if n > 2 and follows(n, ones, L):
                    hits.append({"ones": ones, "n": n, "B": B})
                elif n in (1, 2) and follows(n, ones, L):
                    hits.append({"ones": ones, "n": n, "B": B, "trivial": True})
    return {
        "L": L,
        "a": a,
        "den": den,
        "binom": comb(L, a),
        "mode": mode,
        "maps_built": maps_built,
        "pairs_checked": pairs_checked,
        "hits": hits,
        "nontrivial_hits": [h for h in hits if not h.get("trivial")],
    }


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)

    # Push beyond X-0126 sampling: full MITM on larger convergent L
    # log3(2) convergent-ish denominators include 19,30,49,...
    targets = []
    for L in [16, 17, 19, 20, 24, 29, 30, 37, 41, 49]:
        amax = int(L * log(2) / log(3))
        for a in {amax, max(1, amax - 1), max(1, amax - 2)}:
            if 3**a < (1 << L):
                targets.append((L, a))

    rows = []
    for L, a in targets:
        # larger L may truncate extreme k halves; middle k still covered
        cap = 400000 if L <= 30 else 250000
        rows.append(mitm_search(L, a, max_half_binom=cap))

    nont = [r for r in rows if r.get("nontrivial_hits")]
    summary = {
        "rows": rows,
        "nontrivial_configs": nont,
        "total_nontrivial": sum(len(r.get("nontrivial_hits", [])) for r in rows),
        "total_trivial_hits": sum(
            len([h for h in r.get("hits", []) if h.get("trivial")]) for r in rows
        ),
        "conclusion": (
            "MITM modular cycle builder near log3(2) convergents; "
            "nontrivial hits would be K-candidates."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"configs={len(rows)} nontrivial_configs={len(nont)} "
        f"total_nontrivial={summary['total_nontrivial']}",
    ]
    for r in rows:
        lines.append(
            f"L={r['L']} a={r['a']} mode={r.get('mode')} "
            f"pairs={r.get('pairs_checked')} hits={len(r.get('hits', []))} "
            f"nont={len(r.get('nontrivial_hits', []))}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
