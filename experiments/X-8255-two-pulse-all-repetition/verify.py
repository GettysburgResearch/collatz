#!/usr/bin/env python3
"""Independent reconstruction of the X-8255 frozen certificate.

This verifier imports no author-side module. It independently rebuilds logarithm
intervals, continued fractions, the analytic rejection rows, and the complete
small-repetition two-pulse scan, then compares the resulting object to JSON.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

sys.set_int_max_str_digits(0)
NTERMS = 180
C2 = 1 << 32


def fdigest(x: Fraction) -> str:
    return hashlib.sha256((str(x.numerator) + "/" + str(x.denominator)).encode()).hexdigest()


def floor_decimal(x: Fraction, n: int) -> str:
    sign = "-" if x < 0 else ""
    x = abs(x)
    scale = 10**n
    z = x.numerator * scale // x.denominator
    return f"{sign}{z // scale}.{z % scale:0{n}d}"


def log_bounds_integer(n: int) -> tuple[Fraction, Fraction]:
    if n <= 0:
        raise AssertionError
    if n == 2:
        y = Fraction(1, 3)
        s = Fraction(0)
        yp = y
        y2 = y * y
        for j in range(NTERMS):
            s += 2 * yp / (2 * j + 1)
            yp *= y2
        return s, s + 2 * yp / ((2 * NTERMS + 1) * (1 - y2))
    shift = n.bit_length() - 1
    mant = Fraction(n, 1 << shift)
    z = (mant - 1) / (mant + 1)
    s = Fraction(0)
    zp = z
    z2 = z * z
    for j in range(NTERMS):
        s += 2 * zp / (2 * j + 1)
        zp *= z2
    tail = 2 * zp / ((2 * NTERMS + 1) * (1 - z2))
    l2lo, l2hi = log_bounds_integer(2)
    return shift * l2lo + s, shift * l2hi + s + tail


L2 = log_bounds_integer(2)
L3 = log_bounds_integer(3)


def alpha_bounds(A: int, k: int) -> tuple[Fraction, Fraction]:
    return ((k * L3[0] - A * L2[1]) / L2[1], (k * L3[1] - A * L2[0]) / L2[0])


def continued_fraction(lo: Fraction, hi: Fraction, limit: int):
    original_lo, original_hi = lo, hi
    pp, pc = 0, 1
    qp, qc = 1, 0
    rows = []
    for idx in range(256):
        a = lo.numerator // lo.denominator
        if a != hi.numerator // hi.denominator:
            raise AssertionError("ambiguous CF")
        p = a * pc + pp
        q = a * qc + qp
        f = Fraction(p, q)
        side = "below" if f < original_lo else "above" if f > original_hi else None
        if side is None:
            raise AssertionError("CF value unresolved")
        rows.append({"index": idx, "partial_quotient": a, "p": p, "q": q, "side": side})
        if q > limit:
            return rows
        lo, hi = 1 / (hi - a), 1 / (lo - a)
        pp, pc = pc, p
        qp, qc = qc, q
    raise AssertionError("CF limit")


def interval_log_product(A: int, k: int) -> tuple[Fraction, Fraction]:
    return A * L2[0] - Fraction(k, 2) * L3[1], A * L2[1] - Fraction(k, 2) * L3[0]


def cutoff_record(A: int, k: int, c: int, M: int):
    rate = interval_log_product(A, k)
    Khi = C2 * L2[1] * L3[1]
    _, chi = log_bounds_integer(2 * c)
    _, bhi = log_bounds_integer(k * M + 1)
    margin = M * rate[0] - chi - Khi * (1 + bhi)
    derivative = rate[0] - Khi * Fraction(k, k * M + 1)
    assert margin > 0 and derivative > 0 and M * rate[0] > chi
    return {
        "cutoff": M,
        "margin_decimal_lower": floor_decimal(margin, 12),
        "margin_sha256": fdigest(margin),
        "derivative_decimal_lower": floor_decimal(derivative, 18),
        "derivative_sha256": fdigest(derivative),
    }


def legendre_record(A: int, k: int, c: int, r: int):
    left = 4 * c * r * 3 ** ((k * r) // 2)
    right = (2 ** (A * r)) * L2[0]
    margin = right - left
    assert margin > 0
    ratio = Fraction(2 * 3 ** ((k + 1) // 2), 2**A)
    assert ratio < 1
    return {
        "first_r": r,
        "margin_decimal_lower": floor_decimal(margin, 12),
        "margin_sha256": fdigest(margin),
        "uniform_ratio_upper": f"{ratio.numerator}/{ratio.denominator}",
    }


def reject_record(A: int, k: int, c: int, p: int, q: int, qn: int):
    rhs = 4 * c * (q + qn)
    _, logrھs_hi = log_bounds_integer(rhs)
    margin = A * q * L2[0] - ((k * q) // 2) * L3[1] - logrھs_hi
    assert margin > 0
    return {
        "p": p,
        "q": q,
        "q_next": qn,
        "floor_kq_over_2": (k * q) // 2,
        "all_positive_multiples_rejected": True,
        "log_margin_decimal_lower": floor_decimal(margin, 12),
        "log_margin_sha256": fdigest(margin),
    }


def ord2(x: int) -> int:
    if x == 0:
        raise AssertionError
    x = abs(x)
    n = 0
    while x % 2 == 0:
        n += 1
        x //= 2
    return n


def psums(w):
    total = 0
    out = [0]
    for a in w:
        total += a
        out.append(total)
    return out


def affine_num(w):
    p = psums(w)
    n = len(w)
    return sum(pow(3, n - 1 - j) * pow(2, p[j]) for j in range(n))


def rot(w, j):
    j %= len(w)
    return tuple(w[j:]) + tuple(w[:j])


def base_cycle(w):
    p = psums(w)
    den = pow(2, p[-1]) - pow(3, len(w))
    num = affine_num(w)
    assert num % den == 0
    z = num // den
    assert z < 0 and z % 2
    states = [z]
    for a in w:
        raw = 3 * z + 1
        assert ord2(raw) == a
        z = raw // pow(2, a)
        states.append(z)
    assert z == states[0]
    return states, p


def finite_scan(base, rmax):
    packet_count = positive_count = bezout_count = 0
    found = []
    digest = hashlib.sha256()
    for rep in range(1, rmax + 1):
        for shift in range(len(base)):
            seq = rot(base, shift) * rep
            states, pref = base_cycle(seq)
            U = pow(2, pref[-1])
            Q = pow(3, len(seq))
            for gap in range(1, len(seq) // 2 + 1):
                sval = sum(seq[1 : gap + 1])
                aa = (-states[1]) * pow(3, gap)
                bb = (-states[gap + 1]) * pow(2, sval)
                gg = aa - bb
                assert aa == bb + gg and min(aa, bb, gg) > 0
                c = Q * bb - U * aa
                d = Q * gg
                xcap = (2 * abs(c) + d + Q) // (2 * U)
                packet_count += 1
                x = 2
                while x <= xcap:
                    jj = U * (x * gg - aa) + bb * Q
                    mcap = (abs(jj) + Q) // (U * x)
                    m = 2
                    while m <= mcap:
                        den = U * x * m - Q
                        if den > 0:
                            positive_count += 1
                            rr = x * (bb * m + gg) - aa
                            kk = Q * (bb * m + gg) - U * m * aa
                            jj2 = U * (x * gg - aa) + bb * Q
                            assert U * m * rr - (bb * m + gg) * den == kk
                            assert U * x * rr - bb * x * den == x * jj2
                            assert (rr % den == 0) == (kk % den == 0) == (jj2 % den == 0)
                            bezout_count += 2
                            if rr % den == 0:
                                d1 = x.bit_length() - 1
                                d2 = m.bit_length() - 1
                                trial = list(seq)
                                trial[0] += d1
                                trial[gap] += d2
                                D = pow(2, sum(trial)) - pow(3, len(trial))
                                C = affine_num(trial)
                                assert D == den and C % D == 0
                                start = C // D
                                cur = start
                                for a in trial:
                                    raw = 3 * cur + 1
                                    assert ord2(raw) == a
                                    cur = raw // pow(2, a)
                                assert cur == start
                                found.append({"r": rep, "rotation": shift, "gap": gap, "d1": d1, "d2": d2, "n": start, "word": trial, "D": D})
                            digest.update(f"{rep}|{shift}|{gap}|{x}|{m}\n".encode())
                        m *= 2
                    x *= 2
    return {
        "rmax": rmax,
        "packets": packet_count,
        "positive_denominator_candidates": positive_count,
        "eliminant_identities": bezout_count,
        "hits": found,
        "transcript_sha256": digest.hexdigest(),
    }


SPECS = (
    ("negative-three-cycle", (1, 2), 3, 2, 7, 100_000_000_000, 6, 5),
    ("negative-eleven-cycle", (1, 1, 1, 2, 1, 1, 4), 11, 7, 91, 25_000_000_000, 2, 1),
)


def reconstruct():
    cases = []
    row_total = reject_total = 0
    master = hashlib.sha256()
    for name, base, A, k, c, cutoff, legendre_r, small_r in SPECS:
        bounds = alpha_bounds(A, k)
        rows = continued_fraction(*bounds, cutoff)
        rejections = []
        exceptions = []
        for i, row in enumerate(rows[:-1]):
            if row["side"] != "above" or int(row["q"]) >= cutoff:
                continue
            p = int(row["p"])
            q = int(row["q"])
            qnext = int(rows[i + 1]["q"])
            if name == "negative-three-cycle" and (p, q) == (1, 5):
                margin = 1 - Fraction(59049, 65536) ** 2 - 7 * Fraction(3, 8) ** 10
                assert margin > 0
                exceptions.append({"p": 1, "q": 5, "minimum_multiple_m": 2, "exact_margin_numerator": margin.numerator, "exact_margin_denominator": margin.denominator, "all_m_at_least_2_rejected": True})
            else:
                rejections.append(reject_record(A, k, c, p, q, qnext))
        item = {
            "name": name,
            "A": A,
            "k": k,
            "cmax": c,
            "alpha_interval": {"lo_sha256": fdigest(bounds[0]), "hi_sha256": fdigest(bounds[1])},
            "matveev": cutoff_record(A, k, c, cutoff),
            "legendre": legendre_record(A, k, c, legendre_r),
            "continued_fraction_rows": rows,
            "uniform_candidate_rejections": rejections,
            "exceptional_rows": exceptions,
            "small_exact_scan": finite_scan(base, small_r),
        }
        cases.append(item)
        row_total += len(rows)
        reject_total += len(rejections) + len(exceptions)
        master.update(json.dumps(item, sort_keys=True, separators=(",", ":")).encode())
    hits = [h for case in cases for h in case["small_exact_scan"]["hits"]]
    assert len(hits) == 1 and hits[0]["n"] == 1 and hits[0]["word"] == [2, 2, 2, 2]
    return {
        "experiment_id": "X-8255",
        "status": "exact finite certificate; T-8255 remains PROPOSED / SOURCE-DEPENDENT",
        "cases": cases,
        "totals": {"continued_fraction_rows": row_total, "primitive_upper_rows_rejected": reject_total, "nontrivial_hits": 0, "trivial_hits": 1},
        "master_transcript_sha256": master.hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path)
    args = parser.parse_args()
    frozen = json.loads(args.artifact.read_text(encoding="utf-8"))
    rebuilt = reconstruct()
    if frozen != rebuilt:
        raise SystemExit("independent reconstruction mismatch")
    print("independent reconstruction matches")
    print(json.dumps(rebuilt["totals"], sort_keys=True))
    print(rebuilt["master_transcript_sha256"])


if __name__ == "__main__":
    main()
