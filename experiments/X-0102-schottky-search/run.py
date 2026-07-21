#!/usr/bin/env python3
"""X-0102: search for real Schottky systems among supercritical inverse branches.

For pairs/triples of supercritical words, try to find a positive interval I
on which the inverse branches form a classical IFS ping-pong (into-itself,
disjoint images, uniform contraction).

Status intent: EMPIRICAL search. A hit would be promoted carefully; absence of
hits up to a bound is not a nonexistence proof.
"""

from __future__ import annotations

import itertools
import json
import math
from dataclasses import dataclass
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


@dataclass(frozen=True)
class InvBranch:
    word: str
    L: int
    a: int
    B: int
    mu: Fraction  # forward slope
    inv_slope: Fraction
    beta: Fraction
    tau: Fraction
    fp: Fraction
    residue: int

    def g(self, y: Fraction) -> Fraction:
        return (y - self.beta) / self.mu

    def g_interval(self, A: Fraction, B: Fraction) -> tuple[Fraction, Fraction]:
        # g is increasing
        lo, hi = self.g(A), self.g(B)
        return (lo, hi) if lo <= hi else (hi, lo)


def build(word: str) -> InvBranch | None:
    L = len(word)
    a = word.count("1")
    if a == 0:
        return None
    B = B_of(word)
    mu = Fraction(3**a, 1 << L)
    if mu <= 1:
        return None
    beta = Fraction(B, 1 << L)
    fp = Fraction(-B, 3**a - (1 << L))
    return InvBranch(
        word=word,
        L=L,
        a=a,
        B=B,
        mu=mu,
        inv_slope=Fraction(1 << L, 3**a),
        beta=beta,
        tau=beta,
        fp=fp,
        residue=residue_of(word),
    )


def words_up_to(Lmax: int):
    for L in range(1, Lmax + 1):
        for mask in range(1 << L):
            yield format(mask, f"0{L}b")[::-1]


def intervals_disjoint_separated(
    ints: list[tuple[Fraction, Fraction]], gamma: Fraction
) -> bool:
    for (a1, b1), (a2, b2) in itertools.combinations(ints, 2):
        # distance between closed intervals
        if b1 < a2:
            dist = a2 - b1
        elif b2 < a1:
            dist = a1 - b2
        else:
            return False
        if dist < gamma:
            return False
    return True


def try_interval_for(
    branches: list[InvBranch], A: Fraction, B: Fraction, gamma: Fraction
) -> dict | None:
    if A <= 0 or B <= A:
        return None
    images = []
    for br in branches:
        lo, hi = br.g_interval(A, B)
        if lo <= 0:
            return None
        if lo < A or hi > B:
            return None
        images.append((lo, hi))
    if not intervals_disjoint_separated(images, gamma):
        return None
    kappa = max(br.inv_slope for br in branches)
    return {
        "I": [str(A), str(B)],
        "gamma": str(gamma),
        "kappa": str(kappa),
        "words": [br.word for br in branches],
        "mu": [str(br.mu) for br in branches],
        "images": [[str(lo), str(hi)] for lo, hi in images],
        "taus": [str(br.tau) for br in branches],
        "fps": [str(br.fp) for br in branches],
    }


def candidate_intervals(branches: list[InvBranch]) -> list[tuple[Fraction, Fraction]]:
    """Heuristic positive intervals above all positivity thresholds."""
    tau_max = max(br.tau for br in branches)
    # Need I subset (tau_max, ∞) roughly, but also g(I) subset I.
    # For contraction toward negative fp, g maps [A,B] to a left-shifted interval.
    # Mildly supercritical branches have inv_slope ~ 1, so need large A.
    outs = []
    for A in [
        tau_max + Fraction(1, 1),
        tau_max + Fraction(2, 1),
        tau_max + Fraction(5, 1),
        tau_max + Fraction(10, 1),
        tau_max * 2 + Fraction(1, 1),
        tau_max * 3 + Fraction(1, 1),
        Fraction(10, 1),
        Fraction(100, 1),
        Fraction(1000, 1),
        Fraction(10**6, 1),
        Fraction(10**9, 1),
    ]:
        if A <= tau_max:
            A = tau_max + 1
        for width_factor in [Fraction(1, 10), Fraction(1, 2), Fraction(1, 1), Fraction(2, 1), Fraction(5, 1)]:
            # Width relative to displacement scale
            w = max(Fraction(1, 1), A * width_factor * Fraction(1, 100))
            # Also try widths from contraction gap
            outs.append((A, A + w))
            outs.append((A, A + max(Fraction(1, 1), A // 1000)))
            outs.append((A, A + max(Fraction(1, 1), A // 100)))
            outs.append((A, 2 * A))
    # Dedup
    uniq = []
    seen = set()
    for I in outs:
        key = (I[0], I[1])
        if key not in seen and I[1] > I[0]:
            seen.add(key)
            uniq.append(I)
    return uniq


def analytic_obstruction_note(branches: list[InvBranch]) -> str:
    """Record a structural reason pairs often fail.

    Each g maps toward a negative fixed point, so on a positive interval
    g([A,B]) = [g(A), g(B)] lies to the left of [A,B] whenever
    g(B) < B, i.e. B > fp (always for B>0>fp) and the right endpoint moves left:
    g(B) - B = (B - beta)/mu - B = B(1/mu - 1) - beta/mu < 0 since mu>1.
    Thus g(B) < B always. For g(A) >= A one needs A <= g(A), i.e.
    A <= (A - beta)/mu, impossible for A > 0 because that rearranges to
    A(mu - 1) <= -beta < 0.
    Conclusion: NO supercritical inverse branch can map a positive interval
    into itself — the left endpoint condition A <= g(A) fails for all A>0.
    """
    br = branches[0]
    # Demonstrate A <= g(A) fails
    return (
        "OBSTRUCTION: for supercritical mu>1 and beta>0, g(A)-A = "
        "A(1/mu-1) - beta/mu < 0 for every A>0; hence g(I) is never a subset "
        f"of I subset (0,∞). Sample word={br.word}, mu={br.mu}, beta={br.beta}."
    )


def search(Lmax: int) -> dict:
    branches = []
    for w in words_up_to(Lmax):
        br = build(w)
        if br is not None:
            branches.append(br)
    # Prefer mild supercritical
    branches.sort(key=lambda b: float(b.mu))
    mild = [b for b in branches if b.mu <= Fraction(3, 2)]
    pool = mild if len(mild) >= 2 else branches[:200]

    hits = []
    tested_pairs = 0
    gamma = Fraction(1, 1000)

    # Pair search with heuristic intervals
    for brs in itertools.combinations(pool[:80], 2):
        tested_pairs += 1
        for A, B in candidate_intervals(list(brs)):
            hit = try_interval_for(list(brs), A, B, gamma)
            if hit:
                hits.append(hit)
                break
        if len(hits) >= 5:
            break

    # Triple search (smaller pool)
    tested_triples = 0
    for brs in itertools.combinations(pool[:30], 3):
        tested_triples += 1
        for A, B in candidate_intervals(list(brs))[:20]:
            hit = try_interval_for(list(brs), A, B, gamma)
            if hit:
                hits.append(hit)
                break
        if len(hits) >= 8:
            break

    obstruction = analytic_obstruction_note(pool[:1] or branches[:1])

    # Verify obstruction numerically on many samples
    obstruction_checks = 0
    obstruction_failures = 0
    for br in pool[:100]:
        for A in [Fraction(1, 1), Fraction(10, 1), br.tau + 1, Fraction(10**6, 1)]:
            if A <= 0:
                continue
            obstruction_checks += 1
            if br.g(A) >= A:
                obstruction_failures += 1

    return {
        "Lmax": Lmax,
        "supercritical_branches": len(branches),
        "mild_pool": len(mild),
        "tested_pairs": tested_pairs,
        "tested_triples": tested_triples,
        "hits": hits,
        "hit_count": len(hits),
        "analytic_obstruction": obstruction,
        "obstruction_checks": obstruction_checks,
        "obstruction_counterexamples_to_claim": obstruction_failures,
    }


def main() -> None:
    root = Path(__file__).resolve().parent
    results = root / "results"
    results.mkdir(exist_ok=True)
    summary = search(Lmax=12)
    (results / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    lines = [
        f"Lmax={summary['Lmax']}",
        f"supercritical branches={summary['supercritical_branches']}",
        f"mild pool={summary['mild_pool']}",
        f"tested pairs={summary['tested_pairs']} triples={summary['tested_triples']}",
        f"hits={summary['hit_count']}",
        f"obstruction checks={summary['obstruction_checks']} counterexamples={summary['obstruction_counterexamples_to_claim']}",
        "",
        summary["analytic_obstruction"],
    ]
    if summary["hits"]:
        lines.append("HITS:")
        lines.append(json.dumps(summary["hits"], indent=2))
    (results / "summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
