#!/usr/bin/env python3
"""Whole-source signed drift control for one explicit ordinary input.

Standalone standard-library implementation. Every logarithm is enclosed by
integer interval arithmetic and an explicit atanh-series remainder. Every
omitted original source is covered analytically. No floating-point number is
used to decide the signs.
"""

from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import json


SCALE = 10**32
TERMS = 32
SOURCE_CUTOFF = 262144
INITIAL_DRIFT_CUTOFF = 256
RETURN_INDEX = 9


def require(condition, message):
    if not condition:
        raise ValueError(message)


def ceildiv(a, b):
    return -((-a) // b)


def atanh_log_interval(a, b):
    """Enclose 2*atanh(a/b), 0<=a/b<=1/3, in SCALE units."""
    require(0 <= 3 * a <= b, "atanh argument outside certified range")
    z_lo, z_hi = SCALE * a // b, ceildiv(SCALE * a, b)
    z2_lo = z_lo * z_lo // SCALE
    z2_hi = ceildiv(z_hi * z_hi, SCALE)
    p_lo, p_hi = z_lo, z_hi
    lo = hi = 0
    for j in range(TERMS):
        lo += 2 * p_lo // (2 * j + 1)
        hi += ceildiv(2 * p_hi, 2 * j + 1)
        p_lo = p_lo * z2_lo // SCALE
        p_hi = ceildiv(p_hi * z2_hi, SCALE)
    # 2*z^(2M+1)/((2M+1)*(1-z²)) <= 9/(4*(2M+1)*3^(2M+1)).
    hi += ceildiv(9 * SCALE, 4 * (2 * TERMS + 1) * 3**(2 * TERMS + 1))
    return lo, hi


LOG2 = atanh_log_interval(1, 3)


def log_interval(a, b=1):
    """Enclose log(a/b) for a/b>=1, in SCALE units."""
    require(a >= b > 0, "log argument below one")
    k = a.bit_length() - b.bit_length()
    if a < b * (1 << k):
        k -= 1
    require(k >= 0, "unexpected negative binary scale")
    d = b * (1 << k)
    require(d <= a < 2 * d, "binary log normalization")
    lo, hi = atanh_log_interval(a - d, a + d)
    return lo + k * LOG2[0], hi + k * LOG2[1]


def loglog_shift_interval(rank_value):
    """Enclose 1+log(log(rank_value+6)) for rank_value>=1."""
    require(rank_value >= 1, "positive rank required")
    lo1, hi1 = log_interval(rank_value + 6)
    require(lo1 > SCALE, "inner log must exceed one")
    lo2, _ = log_interval(lo1, SCALE)
    _, hi2 = log_interval(hi1, SCALE)
    return SCALE + lo2, SCALE + hi2


def v(n, p):
    require(n != 0, "zero valuation")
    n = abs(n)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


@lru_cache(None)
def rank(n):
    if n == 1:
        return 0
    h = v(2 * n + 1, 3)
    modes = {0, 1, 2}
    if h >= 3:
        modes.add(h)
    values = []
    for a in modes:
        z = 3**a * (n + 1) - 2**a * (2 * n + 1)
        require(z != 0, "unexpected zero rank component")
        values.append(z * z // 3**v(z, 3))
    result = min(values)
    require(n - 1 <= result <= n * n, "proper-rank interface")
    return result


@lru_cache(None)
def acceleration(n):
    require(n > 1, "absorbed acceleration source")
    a = 0 if n % 2 == 0 else v(n + 1, 2)
    d, c = 3**a - 2**(a + 1), 3**a - 2**a
    z = d * n + c
    k = v(z, 2) // (a + 1)
    require(k >= 1, "empty physical acceleration")
    out_z = 3**(a * k) * (z // 2**((a + 1) * k))
    require((out_z - c) % d == 0, "nonintegral affine endpoint")
    endpoint = (out_z - c) // d
    physical = n
    for _ in range(k):
        for _ in range(a):
            require(physical % 2, "wrong odd bit")
            physical = (3 * physical + 1) // 2
        require(physical % 2 == 0, "wrong even bit")
        physical //= 2
    require(endpoint == physical and endpoint >= 1, "physical replay mismatch")
    require(endpoint + 5 <= (n + 5)**3, "height bound")
    require(rank(endpoint) + 6 <= (rank(n) + 6)**6, "logarithmic-domain bound")
    return endpoint


@lru_cache(None)
def safe(n):
    return 4 * rank(acceleration(n)) <= rank(n)


@lru_cache(None)
def return_map(n):
    require(n > 1 and not safe(n), "unsafe source required")
    current = acceleration(n)
    while current > 1 and safe(current):
        before = rank(current)
        current = acceleration(current)
        require(4 * rank(current) <= before, "safe descent failed")
    require(rank(current) + 6 <= (rank(n) + 6)**6, "return-domain bound")
    return current


@lru_cache(None)
def psi_interval(n):
    return (0, 0) if n == 1 else loglog_shift_interval(rank(n))


def weighted_drift_interval(distribution):
    total_lo = total_hi = 0
    for n, (mass_lo, mass_hi) in distribution.items():
        target = return_map(n)
        p_lo, p_hi = psi_interval(n)
        q_lo, q_hi = psi_interval(target)
        d_lo, d_hi = q_lo - p_hi, q_hi - p_lo
        products = (mass_lo * d_lo, mass_lo * d_hi,
                    mass_hi * d_lo, mass_hi * d_hi)
        total_lo += min(products)
        total_hi += max(products)
    return Fraction(total_lo, SCALE**2), Fraction(total_hi, SCALE**2)


def original_distribution(limit):
    result = {}
    for n in range(2, limit + 1):
        if not safe(n):
            denominator = n * (n + 1)
            result[n] = (SCALE // denominator, ceildiv(SCALE, denominator))
    return result


def transport(distribution):
    result = {}
    for n, (lo, hi) in distribution.items():
        target = return_map(n)
        if target > 1:
            previous = result.get(target, (0, 0))
            result[target] = (previous[0] + lo, previous[1] + hi)
    return result


LOG6 = log_interval(6)


def original_tail_energy_upper(limit):
    m = limit + 1
    _, g_hi = loglog_shift_interval(m * m)
    log_m_lo, _ = log_interval(m)
    return Fraction(g_hi, SCALE * m) + Fraction(SCALE, m * log_m_lo)


def complete_drift_interval(finite_interval, cutoff, return_index):
    negative_tail = original_tail_energy_upper(cutoff) + Fraction(return_index * LOG6[1], SCALE * (cutoff + 1))
    positive_tail = Fraction(LOG6[1], SCALE * (cutoff + 1))
    return finite_interval[0] - negative_tail, finite_interval[1] + positive_tail


def decimal_enclosure(lo, hi, digits=12):
    scale = 10**digits
    low = (lo.numerator * scale) // lo.denominator
    high = ceildiv(hi.numerator * scale, hi.denominator)
    def render(value):
        sign = "-" if value < 0 else ""
        value = abs(value)
        return f"{sign}{value // scale}.{value % scale:0{digits}d}"
    return [render(low), render(high)]


def main():
    initial_partial = weighted_drift_interval(original_distribution(INITIAL_DRIFT_CUTOFF))
    initial_complete = complete_drift_interval(initial_partial, INITIAL_DRIFT_CUTOFF, 0)
    require(initial_complete[1] < 0, "initial full-source drift is not certified negative")

    current = original_distribution(SOURCE_CUTOFF)
    initial_state_count = len(current)
    for _ in range(RETURN_INDEX):
        current = transport(current)
    late_partial = weighted_drift_interval(current)
    late_complete = complete_drift_interval(late_partial, SOURCE_CUTOFF, RETURN_INDEX)
    require(late_complete[0] > 0, "transported full-source drift is not certified positive")

    retained_mass_lower = Fraction(sum(pair[0] for pair in current.values()), SCALE)
    # m0<=sum_(n>=2)1/[n(n+1)]=1/2 and D0<0 imply mean fresh drift <=2D0.
    covariance_lower = late_complete[0] - 2 * initial_complete[1] * retained_mass_lower
    require(covariance_lower > 0, "transport covariance lower bound")
    witness = [27]
    for _ in range(10):
        witness.append(return_map(witness[-1]))
    require(witness == [27, 31, 121, 91, 103, 175, 445, 334, 167, 319, 1822], "carrier witness changed")
    require(319 in current, "missing accumulated carrier")
    amplification_lower = Fraction(current[319][0] * 319 * 320, SCALE)

    result = {
        "status": "PASS",
        "scope": "whole-source signs for the explicit fixed f0; two specified return times only; no all-time decay claim",
        "input": "f0(u)=1/[u(u+1)] on U; zero elsewhere",
        "initial_complete_drift_interval": decimal_enclosure(*initial_complete),
        "return_9_to_10_complete_drift_interval": decimal_enclosure(*late_complete),
        "finite_part_return_9_to_10_interval": decimal_enclosure(*late_partial),
        "transport_covariance_lower_bound": decimal_enclosure(covariance_lower, covariance_lower)[0],
        "return_9_retained_mass_lower_bound": decimal_enclosure(retained_mass_lower, retained_mass_lower)[0],
        "carrier_319_density_amplification_lower_bound": decimal_enclosure(amplification_lower, amplification_lower)[0],
        "carrier_original_path": witness,
        "initial_drift_source_cutoff": INITIAL_DRIFT_CUTOFF,
        "transported_drift_source_cutoff": SOURCE_CUTOFF,
        "initial_unsafe_states_under_larger_cutoff": initial_state_count,
        "return_9_distinct_retained_endpoints": len(current),
        "integer_interval_scale": str(SCALE),
        "atanh_terms": TERMS,
        "tail_proof": "sum f_tail<=1/(M+1); psi-tail<=g(M+1)/(M+1)+1/[(M+1)log(M+1)]; actual j-return additive bound",
    }
    here = Path(__file__).resolve().parent
    result["source_sha256"] = {name: sha256((here / name).read_bytes()).hexdigest()
                               for name in ["check_transported_drift.py", "FIXED_SOURCE_DRIFT.md"]}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
