#!/usr/bin/env python3
"""X-0110: explicit 2-adic bit-budget ledger along accelerated walks.

Tracks a free parameter line n = M u + R through a sequence of blocks and
records, at each step:
  - tax: bits of 2-adic constraint imposed on u to enable the next word
  - transport: how the remaining parameter is mapped (odd unit vs not)
  - whether free 2-adic rank increases (true regeneration) or not

Hypothesis under test (toward L-0106): odd image moduli make residues
surjective in q, but when the current free parameter already lies in a
2^k-class, an odd unit transport preserves that k — no new free bits.
Each subsequent length-L word from an odd-step AP taxes exactly L bits.
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


def v2(n: int) -> int:
    if n == 0:
        return 10**9
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


@dataclass
class ParamLine:
    """n = M*u + R, with u free in Z>=0 (or further constrained externally)."""

    M: int
    R: int

    def __post_init__(self):
        self.R %= self.M


@dataclass
class Block:
    word: str
    L: int
    a: int
    B: int
    r: int

    @property
    def M2(self) -> int:
        return 1 << self.L

    @property
    def N(self) -> int:
        return 3**self.a


def make_block(word: str) -> Block:
    L = len(word)
    a = word.count("1")
    return Block(word, L, a, B_of(word), residue_of(word))


def enable_and_apply(line: ParamLine, b: Block) -> tuple[ParamLine, dict] | None:
    """Impose word residue on current AP; return image AP and ledger row."""
    # Solve M u + R ≡ r (mod 2^L)
    mod = b.M2
    A = line.M % mod
    c = (b.r - line.R) % mod
    g = gcd(A, mod)
    if c % g != 0:
        return None
    # solutions u ≡ u0 mod (mod/g)
    Ag, mg, cg = A // g, mod // g, c // g
    inv = pow(Ag, -1, mg)
    u0 = (cg * inv) % mg
    # thinned: u = mg * v + u0, n = M(mg v + u0) + R = (M*mg)v + (M*u0+R)
    M_thin = line.M * mg
    R_thin = line.M * u0 + line.R
    tax = v2(mg)  # 2-adic index bits charged to the free parameter
    # Apply affine: n' = (N n + B)/2^L
    # n = M_thin v + R_thin
    if (b.N * R_thin + b.B) % b.M2 != 0:
        return None
    if (b.N * M_thin) % b.M2 != 0:
        return None
    alpha = (b.N * M_thin) // b.M2
    beta = (b.N * R_thin + b.B) // b.M2
    # n' = alpha v + beta. Write as M' v' + R' with v'=v, M'=alpha, R'=beta
    # (or normalize). Free parameter still v; 2-adic freedom of v is unchanged
    # by representing n' this way. If we care about freedom in the integer n'
    # modulo powers of two: since M'=alpha = N * M_thin / 2^L,
    # v2(M') = v2(N)+v2(M_thin)-L = 0 + v2(M)+v2(mg)-L.
    image = ParamLine(alpha, beta)
    row = {
        "word": b.word,
        "mu": str(Fraction(b.N, b.M2)),
        "pre_M": line.M,
        "pre_R": line.R,
        "tax_bits": tax,
        "mg": mg,
        "M_thin": M_thin,
        "post_M": image.M,
        "post_R": image.R,
        "v2_pre_M": v2(line.M) if line.M else None,
        "v2_post_M": v2(image.M) if image.M else None,
        "post_M_odd": image.M % 2 == 1,
        "alpha_odd_unit_mod_high_2": image.M % 2 == 1,
    }
    return image, row


def ledger_for_schedule(words: list[str], start: ParamLine | None = None) -> dict:
    if start is None:
        start = ParamLine(1, 0)  # all positive integers
    line = start
    rows = []
    total_tax = 0
    for w in words:
        b = make_block(w)
        out = enable_and_apply(line, b)
        if out is None:
            return {
                "ok": False,
                "failed_at": w,
                "rows": rows,
                "total_tax_bits": total_tax,
            }
        line, row = out
        total_tax += row["tax_bits"]
        rows.append(row)
    return {
        "ok": True,
        "rows": rows,
        "total_tax_bits": total_tax,
        "final_M": line.M,
        "final_R": line.R,
        "sum_word_lengths": sum(len(w) for w in words),
    }


def prove_transport_samples() -> dict:
    """Empirically check: after a supercritical block from Z, post_M is odd;
    then a second block of length L taxes exactly L bits (mg=2^L).
    """
    samples = []
    words = ["1", "11", "101", "1111010", "1101110", "00001111111"]
    # build available
    built = []
    for L in range(1, 10):
        for mask in range(1 << L):
            w = format(mask, f"0{L}b")[::-1]
            if "1" in w:
                built.append(w)
    supers = []
    for w in built:
        b = make_block(w)
        if b.N > b.M2:
            supers.append(w)
    for w1 in ["1", "11", "101", "1111010"]:
        for w2 in supers[:40]:
            led = ledger_for_schedule([w1, w2])
            if not led["ok"]:
                continue
            tax1, tax2 = led["rows"][0]["tax_bits"], led["rows"][1]["tax_bits"]
            samples.append(
                {
                    "schedule": [w1, w2],
                    "tax1": tax1,
                    "tax2": tax2,
                    "len_w2": len(w2),
                    "tax2_equals_len_w2": tax2 == len(w2),
                    "post1_odd": led["rows"][0]["post_M_odd"],
                    "total_tax": led["total_tax_bits"],
                    "sum_lens": led["sum_word_lengths"],
                }
            )
            if len(samples) >= 30:
                break
        if len(samples) >= 30:
            break
    eq = sum(1 for s in samples if s["tax2_equals_len_w2"])
    return {
        "samples": samples[:15],
        "checked": len(samples),
        "tax2_equals_L_count": eq,
        "all_tax2_equals_L": eq == len(samples) and len(samples) > 0,
    }


def nested_intersection_demo() -> dict:
    """For the L-0104 pair, show ∩_N (2^{7N}Z+47) = {47} among integers,
    and that v2(n-47) bounds the number of alternations.
    """
    w1, w2 = "1111010", "1101110"
    # After k successful full pairs starting from free Z, tax should be 7*2*k? 
    # First w1 from Z: tax=7. Image odd M. Then w2: tax=7. Then w1: tax=7, etc.
    taxes = []
    for k in range(1, 6):
        sched = [w1, w2] * k
        led = ledger_for_schedule(sched)
        taxes.append(
            {
                "pairs": k,
                "ok": led["ok"],
                "total_tax": led.get("total_tax_bits"),
                "expected_min": 14 * k,
                "final_M_v2": v2(led["final_M"]) if led.get("ok") else None,
            }
        )
    # Integer survivors for depth
    survivors = []
    for n in range(47, 47 + (1 << 16), 1 << 7):
        # count alternations until fail
        m = n
        steps = 0
        while True:
            w = w1 if steps % 2 == 0 else w2
            b = make_block(w)
            if m % b.M2 != b.r:
                break
            m = (b.N * m + b.B) // b.M2
            steps += 1
            if steps > 40:
                break
        if steps >= 2:
            survivors.append(
                {
                    "n": n,
                    "steps": steps,
                    "v2_n_minus_47": v2(n - 47) if n != 47 else None,
                    "steps_le_v2_budget": steps <= (v2(n - 47) // 7 if n != 47 else 10**9),
                }
            )
        if len(survivors) >= 12:
            break
    return {"pair_tax_table": taxes, "survivor_budget_relation": survivors}


def main() -> None:
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    transport = prove_transport_samples()
    nested = nested_intersection_demo()
    # canonical ledgers
    demos = {
        "from_Z_then_mild": ledger_for_schedule(["1", "101", "1"]),
        "drain_pair_3": ledger_for_schedule(["1111010", "1101110"] * 3),
    }
    summary = {
        "transport_law": transport,
        "nested": nested,
        "demos": demos,
        "conclusion": (
            "From Z, first block of length L taxes L bits and yields an odd-step "
            "image AP. Every subsequent block of length L' then taxes exactly L' "
            "bits (mg=2^{L'}). Odd image moduli do not increase free 2-adic "
            "parameter rank. Total tax along a schedule equals total parity length "
            "when starting from Z and never meeting a pre-aligned 2-power port."
        ),
    }
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        summary["conclusion"],
        f"transport checks: {transport['tax2_equals_L_count']}/{transport['checked']} "
        f"have tax2==L (all={transport['all_tax2_equals_L']})",
        "pair tax table:",
    ]
    for row in nested["pair_tax_table"]:
        lines.append(f"  pairs={row['pairs']} tax={row['total_tax']} ok={row['ok']}")
    lines.append("survivor vs v2 budget samples:")
    for s in nested["survivor_budget_relation"][:6]:
        lines.append(
            f"  n={s['n']} steps={s['steps']} v2(n-47)={s['v2_n_minus_47']} "
            f"bounded={s['steps_le_v2_budget']}"
        )
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
