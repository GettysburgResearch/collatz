"""Rational entropy margin and independently enumerated finite first-hit controls."""

from fractions import Fraction
from functools import lru_cache
import json


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def log_bounds(x, n=96):
    """Bounds from 2 atanh((x-1)/(x+1)), for x >= 1."""
    t = (x - 1) / (x + 1)
    low = 2 * sum(t ** (2 * j + 1) / (2 * j + 1) for j in range(n))
    error = 2 * t ** (2 * n + 1) / ((2 * n + 1) * (1 - t * t))
    return low, low + error


@lru_cache(None)
def odd_step(x):
    raw = 3 * x + 1
    e = (raw & -raw).bit_length() - 1
    return e, raw >> e


def actual_path(x):
    visited = []
    seen = set()
    while x != 1:
        require(x not in seen, "bounded census cycle")
        seen.add(x)
        visited.append(x)
        _, x = odd_step(x)
    return visited + [1]


@lru_cache(None)
def is_principal_passing(x, n):
    start = x
    total = 0
    for j in range(1, n + 1):
        e, x = odd_step(x)
        total += e
        if 4 * total > 7 * j:
            return False
    return start < (1 << (total + 1))


def run():
    a = Fraction(1001, 1000)
    l2, u2 = log_bounds(Fraction(2))
    l3, u3 = log_bounds(Fraction(3))
    l7, u7 = log_bounds(Fraction(7))
    lm, um = log_bounds(Fraction(4, 3))
    # H(4/7) = (log(7) - 8 log(2)/7 - 3 log(3)/7) / log(2).
    hz_lo = (l7 - 8 * u2 / 7 - 3 * u3 / 7) / u2
    hz_hi = (u7 - 8 * l2 / 7 - 3 * l3 / 7) / l2
    scale = 2 * (a**3 - 1)
    gap_lo = 1 - hz_hi
    gap_hi = 1 - hz_lo
    k_lo, k_hi = scale * l2 / um, scale * u2 / lm
    require(Fraction(144709, 10**7) < k_lo < k_hi < Fraction(144711, 10**7), "kappa")
    require(Fraction(147718, 10**7) < gap_lo < gap_hi < Fraction(147720, 10**7), "dimension")
    require((a**3 - 1) / lm < Fraction(11, 1000), "short local horizon")
    paths = [actual_path(x) for x in range(1, 2000, 2)]
    date_controls = {}
    for n in (4, 8, 16, 32, 64, 128, 256):
        hits = [next((x for x in path if is_principal_passing(x, n)), None) for path in paths]
        date_controls[n] = {"finite_landings": sum(x is not None for x in hits),
                            "distinct_finite_landings": len(set(hits) - {None})}
    require(date_controls[256]["finite_landings"] == 0, "tested finite paths eventually fail")
    return {"odd_sources_checked_through": 1999, "source_count": len(paths),
            "joint_local_margin_lower_bound": "0.0003007",
            "log_series_terms": 96, "finite_gates": date_controls}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
