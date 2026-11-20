#!/usr/bin/env python3
"""Exact repair of the TWO supplied v3 point certificates; v2 matrix audit.

Standard library only.  Decimal JSON multipliers are read as exact rationals.
Logarithms and exponentials are outward integer intervals with proved series
remainders.  No LP solver, NumPy, threshold scan, or floating point decision is
used.  A finite list of exact matrix reconstructions accompanies the general
column-sum proof in FARKAS_DIRICHLET_AUDIT.md.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


SCALE = 10 ** 50
VECTOR_SCALE = 10 ** 10
LOG_TERMS = 64
EXP_TERMS = 80


def ceildiv(a, b):
    return -((-a) // b)


def atanh_log(a, b):
    """Enclose 2*atanh(a/b) in SCALE units, for 0<=a/b<=1/3."""
    require(0 <= 3 * a <= b, 'verification condition failed at source line 33')
    zlo, zhi = SCALE * a // b, ceildiv(SCALE * a, b)
    zzlo = zlo * zlo // SCALE
    zzhi = ceildiv(zhi * zhi, SCALE)
    plo, phi = zlo, zhi
    lo = hi = 0
    for j in range(LOG_TERMS):
        lo += 2 * plo // (2 * j + 1)
        hi += ceildiv(2 * phi, 2 * j + 1)
        plo = plo * zzlo // SCALE
        phi = ceildiv(phi * zzhi, SCALE)
    hi += ceildiv(9 * SCALE,
                  4 * (2 * LOG_TERMS + 1) * 3 ** (2 * LOG_TERMS + 1))
    return lo, hi


LOG2 = atanh_log(1, 3)


def logarithm(a, b=1):
    """Enclose log(a/b) for a>=b>0 by binary normalization."""
    require(a >= b > 0, 'verification condition failed at source line 54')
    k = a.bit_length() - b.bit_length()
    if a < b * (1 << k):
        k -= 1
    require(k >= 0, 'verification condition failed at source line 58')
    d = b * (1 << k)
    require(d <= a < 2 * d, 'verification condition failed at source line 60')
    lo, hi = atanh_log(a - d, a + d)
    return lo + k * LOG2[0], hi + k * LOG2[1]


def exp_negative(xlo, xhi):
    """Enclose exp(-x) for x in [xlo/SCALE,xhi/SCALE] subset [0,2]."""
    require(0 <= xlo <= xhi <= 2 * SCALE, 'verification condition failed at source line 67')
    tlo = thi = SCALE
    lo = hi = SCALE
    for j in range(1, EXP_TERMS + 1):
        tlo = tlo * xlo // (SCALE * j)
        thi = ceildiv(thi * xhi, SCALE * j)
        lo += tlo
        hi += thi
    # For 0<=x<=2 and N>=2, the omitted positive Taylor tail is bounded by
    # 2 * 2^(N+1)/(N+1)! because all subsequent term ratios are <=1/2.
    hi += ceildiv(SCALE * 2 ** (EXP_TERMS + 2), factorial(EXP_TERMS + 1))
    return SCALE * SCALE // hi, ceildiv(SCALE * SCALE, lo)


def negative_power(a, b, s):
    lo, hi = logarithm(a, b)
    xlo = lo * s.numerator // s.denominator
    xhi = ceildiv(hi * s.numerator, s.denominator)
    return exp_negative(xlo, xhi)


def coeffs(cert):
    r = int(cert["r"])
    m, p = 3 ** r, 3 ** (r - 1)
    require(cert["modulus"] == m, 'verification condition failed at source line 91')
    u = [F(v) for v in cert["u"]]
    w = [F(v) for v in cert["w"]]
    require(len(u) == m and len(w) == 2 * p + 1, 'verification condition failed at source line 94')
    require(all(v >= 0 for v in u) and w[-1] == -1, 'verification condition failed at source line 95')
    require(all((v * VECTOR_SCALE).denominator == 1 for v in u + w), 'verification condition failed at source line 96')
    ui = [int(v * VECTOR_SCALE) for v in u]
    wi = [int(v * VECTOR_SCALE) for v in w]
    inv2 = pow(2, -1, m)
    # Every coordinate is C+A*2^-s+B*3^-s+D*(2/3)^s.
    # The identity (2/3)^s*2^-s=3^-s is used exactly.
    out = [[wi[-1], 0, 0, 0] for _ in range(m)]
    for a in range(m):
        out[a][0] -= ui[a]
        out[a * inv2 % m][1] += ui[a]
    for k in range(p):
        out[3 * k + 2][0] += wi[k]
        b = (2 * k + 1) % p
        for lift in range(3):
            a = b + lift * p
            out[a][3] -= wi[k]
            out[a * inv2 % m][2] += wi[k]
    for b in range(p):
        out[3 * b][0] += wi[p + b]
        for lift in range(3):
            out[b + lift * p][2] -= wi[p + b]
    return out, u, w


def interval_residual(row, powers):
    lo = hi = row[0] * SCALE
    for coefficient, (vlo, vhi) in zip(row[1:], powers):
        if coefficient >= 0:
            lo += coefficient * vlo
            hi += coefficient * vhi
        else:
            lo += coefficient * vhi
            hi += coefficient * vlo
    return lo, hi


def decimal_bound(numerator, denominator, digits, upper=False):
    scale = 10 ** digits
    n = (ceildiv(numerator * scale, denominator) if upper
         else numerator * scale // denominator)
    sign = "-" if n < 0 else ""
    n = abs(n)
    return f"{sign}{n // scale}.{n % scale:0{digits}d}"


def check_point(name, cert):
    coefficients, u, w = coeffs(cert)
    s = F(cert["s"])
    require((int(cert["r"]), s) in {(4, F(21, 25)), (6, F(913, 1000))}, 'verification condition failed at source line 144')
    powers = [negative_power(2, 1, s), negative_power(3, 1, s),
              negative_power(3, 2, s)]
    residuals = [interval_residual(row, powers) for row in coefficients]
    minimum_lower = min(x[0] for x in residuals)
    minimum_upper = min(x[1] for x in residuals)
    require(minimum_lower > 0, 'verification condition failed at source line 150')
    denominator = VECTOR_SCALE * SCALE
    # The SAME exported multipliers cannot certify the feasible s=1 system.
    s1 = [F(row[0]) + F(row[1], 2) + F(row[2], 3) + F(2 * row[3], 3)
          for row in coefficients]
    m = 3 ** int(cert["r"])
    require(min(s1) < 0, 'verification condition failed at source line 156')
    require(sum(s1) / (m * VECTOR_SCALE) == -1 - sum(u) / (2 * m), 'verification condition failed at source line 157')
    coefficient_hash = sha256(json.dumps(coefficients, separators=(",", ":")).encode()).hexdigest()
    return {
        "name": name, "r": int(cert["r"]), "modulus": m, "s_exact": str(s),
        "all_u_nonnegative": True, "normalization_multiplier_exact": str(w[-1]),
        "residual_coordinates": len(residuals),
        "minimum_residual_lower": decimal_bound(minimum_lower, denominator, 18),
        "minimum_residual_upper": decimal_bound(minimum_upper, denominator, 18, True),
        "minimum_residual_exact_integer_interval": [minimum_lower, minimum_upper],
        "residual_interval_denominator": denominator,
        "coefficient_integer_matrix_sha256": coefficient_hash,
        "negative_control_same_dual_rejected_at_s1": True,
        "scope": "One supplied rational exponent only; no all-s interval or r8 claim.",
    }


def uniform_primal(r):
    m, p = 3 ** r, 3 ** (r - 1)
    unit = F(1, m)
    require(-unit + F(1, 2) * unit < 0, 'verification condition failed at source line 176')
    for _ in range(p):
        require(unit - F(2, 3) * 3 * (unit - F(1, 2) * unit) == 0, 'verification condition failed at source line 178')
        require(unit - F(1, 3) * 3 * unit == 0, 'verification condition failed at source line 179')
    require(m * unit == 1, 'verification condition failed at source line 180')
    return {"r": r, "s": "1", "uniform_entry": str(unit),
            "inequality_residual": str(-unit / 2), "all_equalities_exact": True}


def matrix_column_replay():
    cases = []
    for r in (1, 2, 4):
        m = 3 ** r
        states = [u for u in range(m) if u % 3]
        for gap in range(1, 13):
            counts = {v: 0 for v in states}
            witnesses = {}
            for u in states:
                if (2 ** gap * u) % 3 != 1:
                    continue
                for lift in range(3):
                    target = ((2 ** gap * (u + lift * m) - 1) // 3) % m
                    if target % 3:
                        counts[target] += 1
                        witnesses[target] = (u, lift)
            require(set(counts.values()) == {1}, 'verification condition failed at source line 201')
            for target in states:
                source = ((3 * target + 1) * pow(2 ** gap, -1, 3 * m)) % (3 * m)
                require(witnesses[target] == (source % m, source // m), 'verification condition failed at source line 204')
            cases.append({"r": r, "gap": gap, "unit_states": len(states),
                          "every_target_column_count": 1})
    g = 4
    lambda1 = sum(F(1, 2 ** j) for j in range(1, g + 1))
    lambda3 = sum(F(9, 2 ** (3 * j)) for j in range(1, g + 1))
    require(lambda1 == 1 - F(1, 2 ** g), 'verification condition failed at source line 210')
    require(lambda3 == F(9, 7) * (1 - F(1, 8 ** g)), 'verification condition failed at source line 211')
    require(lambda3 > lambda1, 'verification condition failed at source line 212')
    # A concrete positive odd source exposes the hidden-lift averaging.
    require(7 % 3 == 1 and (4 * 7 - 1) // 3 == 9 and 9 % 3 == 0, 'verification condition failed at source line 214')
    modeled_lifts = [((4 * (1 + 3 * c) - 1) // 3) % 3 for c in range(3)]
    require(modeled_lifts == [1, 2, 0], 'verification condition failed at source line 216')
    return {
        "column_incidence_cases": cases,
        "exact_spectral_formula": "rho(L_r,G(s)) = 3^(s-1) sum_{g=1}^G 2^(-g*s)",
        "modulus_independent": True,
        "global_monotonicity_negative_control": {
            "G": g, "rho_at_s1": str(lambda1), "rho_at_s3": str(lambda3),
            "rho_s3_greater_than_rho_s1": True},
        "infinite_gap_formula": "rho(L_r,infinity(s)) = 3^(s-1)/(2^s-1)",
        "infinite_gap_values": {"s1": "1", "s3": "9/7"},
        "ordinary_source_7_gap2": {"inverse_endpoint": 9,
            "endpoint_excluded_by_unit_restriction": True,
            "averaged_model_from_source_class_1_has_two_unit_lifts": True},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificates", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    raw = args.certificates.read_bytes()
    data = json.loads(raw, parse_float=F)
    require(set(data) == {"r4_s0840", "r6_s0913"}, 'verification condition failed at source line 239')
    points = [check_point(name, data[name]) for name in sorted(data)]
    receipt = {
        "status": "PASS",
        "scope": "Two supplied point certificates rigorously repaired; exact v2 "
                 "averaged-matrix structure and negative controls checked. "
                 "No threshold scan, all-s LP theorem, or Collatz proof.",
        "certificate_file_sha256": sha256(raw).hexdigest(),
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "audit_note_sha256": sha256(Path(__file__).with_name(
            "FARKAS_DIRICHLET_AUDIT.md").read_bytes()).hexdigest(),
        "arithmetic": {"fixed_integer_scale": SCALE, "decimal_vector_scale": VECTOR_SCALE,
                       "log_terms": LOG_TERMS, "positive_exp_terms": EXP_TERMS,
                       "outward_rounding": True, "floating_point_used": False,
                       "solver_used": False},
        "point_certificates": points,
        "uniform_primal_negative_controls": [uniform_primal(4), uniform_primal(6)],
        "averaged_matrix": matrix_column_replay(),
    }
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(json.dumps({
        "status": receipt["status"], "scope": receipt["scope"],
        "certificate_file_sha256": receipt["certificate_file_sha256"],
        "checker_sha256": receipt["checker_sha256"],
        "points": [{k: v for k, v in p.items() if k not in
                    ("minimum_residual_exact_integer_interval", "residual_interval_denominator")}
                   for p in points],
        "column_incidence_cases": len(receipt["averaged_matrix"]["column_incidence_cases"]),
        "matrix_global_monotonicity_negative_control":
            receipt["averaged_matrix"]["global_monotonicity_negative_control"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
