#!/usr/bin/env python3
"""X-0132: scheduled depth-dip + repair policy (fuel path).

Allow v2(n+17) to hit 0 during a supercritical burst, then spend a budget of
mild excursions to repair depth, and repeat. Ask whether net bit-length can
climb by ≥10 across multiple dip/repair epochs while ending each epoch at
depth ≥ D0.
"""

from __future__ import annotations

import json
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
    candidates = [0] if word[0] == "0" else [1]
    for k in range(1, len(word)):
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
    return (3**a * n + B_of(word)) // (1 << L)


def v2(n: int) -> int:
    if n == 0:
        return 10**9
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def follows(n: int, word: str) -> bool:
    x = n
    for bit in word:
        if (x & 1) != int(bit):
            return False
        x = T(x)
    return True


def main():
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)

    template = "11110111000"
    target = -17
    grow_alphabet = ["1", "11", "111", "1111", "1011", "1101", "11111"]
    repair_alphabet = ["0", "00", "000", "10", "010", "0010", "0001", "1000"]
    D0 = 3
    EPOCHS = 8
    REPAIR_BUDGET = 6

    seeds = []
    for m in (11, 22, 33):
        prefix = (template * ((m + 10) // 11 + 2))[:m]
        rt = residue_of(prefix)
        for q in range(0, 30):
            n = (1 << m) * q + rt
            if n > 0:
                seeds.append(n)

    records = []
    success = []
    for n0 in seeds[:90]:
        n = n0
        path = []
        start_bits = n0.bit_length()
        epoch_ok = 0
        for ep in range(EPOCHS):
            # GROW burst: take best expanding move admissible
            grew = False
            for w in grow_alphabet:
                if follows(n, w):
                    n2 = apply_word(n, w)
                    if n2 > n:
                        n = n2
                        path.append(("grow", w, v2(n - target), n))
                        grew = True
                        break
            if not grew:
                break
            # REPAIR phase
            repaired = False
            for _ in range(REPAIR_BUDGET):
                if v2(n - target) >= D0:
                    repaired = True
                    break
                best = None
                for w in repair_alphabet:
                    if not follows(n, w):
                        continue
                    n2 = apply_word(n, w)
                    if n2 <= 0:
                        continue
                    d2 = v2(n2 - target)
                    # prefer depth gain; allow shrink
                    key = (d2, -abs(n2))
                    if best is None or key > best[0]:
                        best = (key, w, n2, d2)
                if best is None:
                    break
                _, w, n2, d2 = best
                n = n2
                path.append(("repair", w, d2, n))
            if v2(n - target) >= D0:
                epoch_ok += 1
                repaired = True
            else:
                break
        bit_gain = n.bit_length() - start_bits
        rec = {
            "seed": n0,
            "final": n,
            "epochs_completed": epoch_ok,
            "bit_gain": bit_gain,
            "final_depth": v2(n - target),
            "path_len": len(path),
            "path_head": path[:12],
        }
        records.append(rec)
        if epoch_ok >= 4 and bit_gain >= 10:
            success.append(rec)

    best = sorted(records, key=lambda r: (-r["epochs_completed"], -r["bit_gain"]))
    summary = {
        "D0": D0,
        "epochs_target": EPOCHS,
        "seeds": len(records),
        "success_4epochs_plus10bits": len(success),
        "best": best[:20],
        "max_epochs": best[0]["epochs_completed"] if best else 0,
        "max_bit_gain": max((r["bit_gain"] for r in records), default=0),
        "conclusion": (
            "Scheduled dip/repair epochs on -17: require ≥4 epochs ending at "
            f"depth≥{D0} with +10 bit gain for a fuel-engine hit."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"seeds={len(records)} success={len(success)} "
        f"max_epochs={summary['max_epochs']} max_bit_gain={summary['max_bit_gain']}",
    ]
    for r in best[:8]:
        lines.append(
            f"  epochs={r['epochs_completed']} bit_gain={r['bit_gain']} "
            f"final_depth={r['final_depth']} final={r['final']}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
