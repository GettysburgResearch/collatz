#!/usr/bin/env python3
"""Exact certificate for the all-repetition two-pulse exclusion T-8255.

The sole external dependency is the quoted n=2 Matveev lower bound already
recorded for T-8202. Everything after that bound is checked using exact Python
integers and Fraction interval arithmetic.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Sequence

sys.set_int_max_str_digits(0)
TERMS = 180
MATVEEV_C2 = 2**32


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if not self.lo < self.hi:
            raise ValueError("invalid interval")


def sha_fraction(x: Fraction) -> str:
    return hashlib.sha256(f"{x.numerator}/{x.denominator}".encode()).hexdigest()


def dec_floor(x: Fraction, digits: int = 18) -> str:
    sign = "-" if x < 0 else ""
    x = abs(x)
    scale = 10**digits
    n = x.numerator * scale // x.denominator
    q, r = divmod(n, scale)
    return f"{sign}{q}.{r:0{digits}d}"


def atanh_interval(z: Fraction, terms: int = TERMS) -> Interval:
    if not Fraction(0) <= z < 1:
        raise ValueError("atanh domain")
    s = Fraction(0)
    zpow = z
    z2 = z * z
    for j in range(terms):
        s += 2 * zpow / (2 * j + 1)
        zpow *= z2
    tail = 2 * zpow / ((2 * terms + 1) * (1 - z2))
    return Interval(s, s + tail)


def log_interval(x: Fraction, terms: int = TERMS) -> Interval:
    if x <= 0:
        raise ValueError("log domain")
    if x == 2:
        return atanh_interval(Fraction(1, 3), terms)
    m = x.numerator.bit_length() - x.denominator.bit_length()
    y = x / (2**m) if m >= 0 else x * (2 ** (-m))
    while y < 1:
        m -= 1
        y *= 2
    while y >= 2:
        m += 1
        y /= 2
    z = (y - 1) / (y + 1)
    core = atanh_interval(z, terms)
    l2 = atanh_interval(Fraction(1, 3), terms)
    if m >= 0:
        return Interval(m * l2.lo + core.lo, m * l2.hi + core.hi)
    return Interval(m * l2.hi + core.lo, m * l2.lo + core.hi)


LOG2 = log_interval(Fraction(2))
LOG3 = log_interval(Fraction(3))


def log_int(n: int) -> Interval:
    return log_interval(Fraction(n))


def alpha_interval(A: int, k: int) -> Interval:
    lo = (k * LOG3.lo - A * LOG2.hi) / LOG2.hi
    hi = (k * LOG3.hi - A * LOG2.lo) / LOG2.lo
    if lo <= 0:
        raise AssertionError("alpha not positive")
    return Interval(lo, hi)


def cf_rows(alpha: Interval, stop_q: int) -> list[dict[str, int | str]]:
    lo, hi = alpha.lo, alpha.hi
    p2, p1 = 0, 1
    q2, q1 = 1, 0
    out: list[dict[str, int | str]] = []
    for idx in range(256):
        a0 = lo.numerator // lo.denominator
        a1 = hi.numerator // hi.denominator
        if a0 != a1:
            raise AssertionError(f"CF interval unresolved at row {idx}")
        a = a0
        p = a * p1 + p2
        q = a * q1 + q2
        value = Fraction(p, q)
        if value < alpha.lo:
            side = "below"
        elif value > alpha.hi:
            side = "above"
        else:
            raise AssertionError("convergent inside unresolved interval")
        out.append({"index": idx, "partial_quotient": a, "p": p, "q": q, "side": side})
        if q > stop_q:
            return out
        lo, hi = 1 / (hi - a), 1 / (lo - a)
        p2, p1 = p1, p
        q2, q1 = q1, q
    raise AssertionError("CF did not pass cutoff")


def effective_rate(A: int, k: int) -> Interval:
    half = Fraction(k, 2)
    return Interval(A * LOG2.lo - half * LOG3.hi, A * LOG2.hi - half * LOG3.lo)


def matveev_cutoff(A: int, k: int, cmax: int, M: int) -> dict[str, object]:
    rate = effective_rate(A, k)
    if rate.lo <= 0:
        raise AssertionError("effective decay rate not positive")
    K = Interval(MATVEEV_C2 * LOG2.lo * LOG3.lo, MATVEEV_C2 * LOG2.hi * LOG3.hi)
    logc = log_int(2 * cmax)
    logB = log_int(k * M + 1)
    margin = M * rate.lo - logc.hi - K.hi * (1 + logB.hi)
    deriv = rate.lo - K.hi * Fraction(k, k * M + 1)
    if margin <= 0 or deriv <= 0:
        raise AssertionError("Matveev cutoff not certified")
    if M * rate.lo <= logc.hi:
        raise AssertionError("Lambda<1 not certified at cutoff")
    return {
        "cutoff": M,
        "margin_decimal_lower": dec_floor(margin, 12),
        "margin_sha256": sha_fraction(margin),
        "derivative_decimal_lower": dec_floor(deriv, 18),
        "derivative_sha256": sha_fraction(deriv),
    }


def legendre_certificate(A: int, k: int, cmax: int, r0: int) -> dict[str, object]:
    U = 2**A
    lhs = 4 * cmax * r0 * 3 ** ((k * r0) // 2)
    rhs = Fraction(U**r0) * LOG2.lo
    if not rhs > lhs:
        raise AssertionError("Legendre threshold fails")
    max_ratio = Fraction(2 * 3 ** ((k + 1) // 2), U)
    if not max_ratio < 1:
        raise AssertionError("Legendre ratio not decreasing")
    return {
        "first_r": r0,
        "margin_decimal_lower": dec_floor(rhs - lhs, 12),
        "margin_sha256": sha_fraction(rhs - lhs),
        "uniform_ratio_upper": f"{max_ratio.numerator}/{max_ratio.denominator}",
    }


def comparison_certificate(A: int, k: int, cmax: int, p: int, q: int, qnext: int) -> dict[str, object]:
    rhs_int = 4 * cmax * (q + qnext)
    margin = A * q * LOG2.lo - ((k * q) // 2) * LOG3.hi - log_int(rhs_int).hi
    if margin <= 0:
        raise AssertionError(f"candidate q={q} not rejected")
    return {
        "p": p,
        "q": q,
        "q_next": qnext,
        "floor_kq_over_2": (k * q) // 2,
        "all_positive_multiples_rejected": True,
        "log_margin_decimal_lower": dec_floor(margin, 12),
        "log_margin_sha256": sha_fraction(margin),
    }


def v2(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0)")
    n = abs(n)
    return (n & -n).bit_length() - 1


def prefix_sums(word: Sequence[int]) -> list[int]:
    out = [0]
    for a in word:
        out.append(out[-1] + a)
    return out


def numerator(word: Sequence[int]) -> int:
    pref = prefix_sums(word)
    n = len(word)
    return sum(3 ** (n - 1 - j) * 2 ** pref[j] for j in range(n))


def rotate(word: Sequence[int], s: int) -> tuple[int, ...]:
    s %= len(word)
    return tuple(word[s:]) + tuple(word[:s])


def negative_orbit(word: Sequence[int]) -> tuple[int, list[int], list[int]]:
    pref = prefix_sums(word)
    D = 2 ** pref[-1] - 3 ** len(word)
    C = numerator(word)
    if C % D:
        raise AssertionError("nonintegral base cycle")
    z = C // D
    if z >= 0 or z % 2 == 0:
        raise AssertionError("not negative odd cycle")
    states = [z]
    cur = z
    for a in word:
        raw = 3 * cur + 1
        if v2(raw) != a:
            raise AssertionError("base valuation mismatch")
        cur = raw // 2**a
        states.append(cur)
    if cur != z:
        raise AssertionError("base cycle does not close")
    return z, states, pref


def scan_small(base: tuple[int, ...], rmax: int) -> dict[str, object]:
    packets = candidates = identities = 0
    hits: list[dict[str, object]] = []
    transcript = hashlib.sha256()
    for r in range(1, rmax + 1):
        for rot in range(len(base)):
            primitive = rotate(base, rot)
            word = primitive * r
            _, states, pref = negative_orbit(word)
            U = 2 ** pref[-1]
            Q = 3 ** len(word)
            for gap in range(1, len(word) // 2 + 1):
                S = sum(word[1 : gap + 1])
                alpha = (-states[1]) * 3**gap
                beta = (-states[gap + 1]) * 2**S
                gamma = alpha - beta
                if not (alpha > 0 and beta > 0 and gamma > 0 and alpha == beta + gamma):
                    raise AssertionError("coefficient sign/telescope failure")
                c = Q * beta - U * alpha
                d = Q * gamma
                Xcap = (2 * abs(c) + d + Q) // (2 * U)
                packets += 1
                X = 2
                while X <= Xcap:
                    J = U * (X * gamma - alpha) + beta * Q
                    Mcap = (abs(J) + Q) // (U * X)
                    M = 2
                    while M <= Mcap:
                        D = U * X * M - Q
                        if D > 0:
                            candidates += 1
                            R = X * (beta * M + gamma) - alpha
                            K = Q * (beta * M + gamma) - U * M * alpha
                            J2 = U * (X * gamma - alpha) + beta * Q
                            if U * M * R - (beta * M + gamma) * D != K:
                                raise AssertionError("K identity")
                            if U * X * R - beta * X * D != X * J2:
                                raise AssertionError("J identity")
                            if (R % D == 0) != (K % D == 0) or (R % D == 0) != (J2 % D == 0):
                                raise AssertionError("divisibility equivalence")
                            identities += 2
                            if R % D == 0:
                                d1 = X.bit_length() - 1
                                d2 = M.bit_length() - 1
                                pulsed = list(word)
                                pulsed[0] += d1
                                pulsed[gap] += d2
                                C2 = numerator(pulsed)
                                D2 = 2 ** sum(pulsed) - 3 ** len(pulsed)
                                if D2 != D or C2 % D2:
                                    raise AssertionError("hit reconstruction")
                                n = C2 // D2
                                cur = n
                                for a in pulsed:
                                    raw = 3 * cur + 1
                                    if v2(raw) != a:
                                        raise AssertionError("hit replay valuation")
                                    cur = raw // 2**a
                                if cur != n:
                                    raise AssertionError("hit replay closure")
                                hits.append({"r": r, "rotation": rot, "gap": gap, "d1": d1, "d2": d2, "n": n, "word": pulsed, "D": D})
                            transcript.update(f"{r}|{rot}|{gap}|{X}|{M}\n".encode())
                        M *= 2
                    X *= 2
    return {
        "rmax": rmax,
        "packets": packets,
        "positive_denominator_candidates": candidates,
        "eliminant_identities": identities,
        "hits": hits,
        "transcript_sha256": transcript.hexdigest(),
    }


CASES = (
    {"name": "negative-three-cycle", "base": (1, 2), "A": 3, "k": 2, "cmax": 7, "cutoff": 100_000_000_000, "legendre_r": 6, "small_r": 5},
    {"name": "negative-eleven-cycle", "base": (1, 1, 1, 2, 1, 1, 4), "A": 11, "k": 7, "cmax": 91, "cutoff": 25_000_000_000, "legendre_r": 2, "small_r": 1},
)


def build_payload() -> dict[str, object]:
    output = []
    total_rows = total_rejected = 0
    master = hashlib.sha256()
    for spec in CASES:
        A = int(spec["A"])
        k = int(spec["k"])
        c = int(spec["cmax"])
        cutoff = int(spec["cutoff"])
        alpha = alpha_interval(A, k)
        rows = cf_rows(alpha, cutoff)
        mat = matveev_cutoff(A, k, c, cutoff)
        leg = legendre_certificate(A, k, c, int(spec["legendre_r"]))
        rejected = []
        exceptional = []
        for idx, row in enumerate(rows[:-1]):
            q = int(row["q"])
            p = int(row["p"])
            if row["side"] != "above" or q >= cutoff:
                continue
            qnext = int(rows[idx + 1]["q"])
            if spec["name"] == "negative-three-cycle" and (p, q) == (1, 5):
                lhs = 1 - Fraction(59049, 65536) ** 2
                rhs = 7 * Fraction(3, 8) ** 10
                margin = lhs - rhs
                if margin <= 0:
                    raise AssertionError("q=5 exceptional row not rejected")
                exceptional.append({"p": 1, "q": 5, "minimum_multiple_m": 2, "exact_margin_numerator": margin.numerator, "exact_margin_denominator": margin.denominator, "all_m_at_least_2_rejected": True})
            else:
                rejected.append(comparison_certificate(A, k, c, p, q, qnext))
        small = scan_small(tuple(spec["base"]), int(spec["small_r"]))
        case = {
            "name": spec["name"],
            "A": A,
            "k": k,
            "cmax": c,
            "alpha_interval": {"lo_sha256": sha_fraction(alpha.lo), "hi_sha256": sha_fraction(alpha.hi)},
            "matveev": mat,
            "legendre": leg,
            "continued_fraction_rows": rows,
            "uniform_candidate_rejections": rejected,
            "exceptional_rows": exceptional,
            "small_exact_scan": small,
        }
        output.append(case)
        total_rows += len(rows)
        total_rejected += len(rejected) + len(exceptional)
        master.update(json.dumps(case, sort_keys=True, separators=(",", ":")).encode())
    all_hits = [h for case in output for h in case["small_exact_scan"]["hits"]]
    if len(all_hits) != 1 or all_hits[0]["n"] != 1 or all_hits[0]["word"] != [2, 2, 2, 2]:
        raise AssertionError("unexpected hit set")
    return {
        "experiment_id": "X-8255",
        "status": "exact finite certificate; T-8255 remains PROPOSED / SOURCE-DEPENDENT",
        "cases": output,
        "totals": {"continued_fraction_rows": total_rows, "primitive_upper_rows_rejected": total_rejected, "nontrivial_hits": 0, "trivial_hits": 1},
        "master_transcript_sha256": master.hexdigest(),
    }


def stable(payload: dict[str, object]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write-results", type=Path)
    group.add_argument("--check-results", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    text = stable(payload)
    target = args.write_results or args.check_results
    if args.write_results:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        print(f"wrote {target}")
    else:
        if target.read_text(encoding="utf-8") != text:
            raise SystemExit("result mismatch")
        print("frozen result verified")
    print(json.dumps(payload["totals"], sort_keys=True))
    print(payload["master_transcript_sha256"])


if __name__ == "__main__":
    main()
