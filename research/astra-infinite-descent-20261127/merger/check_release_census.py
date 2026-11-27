"""Resolve every cofactor residue through a fixed number of postrelease steps."""

import hashlib
from functools import lru_cache

from check_finite_patterns import check, trace
from check_fixed_mersenne import charges


def release_profiles(valuations, extra, costs):
    """For each normalized pair of exact postrelease affine functions, retain its largest saving."""
    high = max(valuations)
    powers = [1]
    for _ in range(high + extra + 2):
        powers.append(3 * powers[-1])
    out = {j: {} for j in valuations}
    for gap in range(1, high + extra):
        num = 1 - powers[gap + 1]
        odd = 0
        saving = gap - costs[((10 - gap) // 2) % 81]
        for clock in range(1, high + 1):
            if num % 2:
                if odd <= gap:
                    num += powers[gap - odd]
                else:
                    num = 3 * num + 1
                odd += 1
            num //= 2
            credit = odd - gap - 1
            if clock in out and gap < clock + extra and abs(credit) <= extra:
                sig = (credit, num)
                if sig not in out[clock] or out[clock][sig][0] < saving:
                    out[clock][sig] = (saving, gap)
    return out


@lru_cache(None)
def hits(extra, credit, signed):
    """All odd U modulo 2^extra supporting equal affine slopes and a common ordinary endpoint."""
    mod = 1 << extra
    good = 0
    scale = 3 ** abs(credit)
    inv = pow(scale, -1, mod)
    for u in range(1, mod, 2):
        if credit >= 0:
            top = u
            low = scale * top + signed
        else:
            low = (u + signed) * inv % mod
            if scale * low < signed:
                low += mod * ((signed - scale * low + mod * scale - 1) // (mod * scale))
            top = scale * low - signed
        check(top >= 0 and low >= 0 and top % mod == u, "ordinary profile representative")
        z, a = trace(top, extra)
        other, b = trace(low, extra)
        if z == other and a == b + credit:
            good |= 1 << (u // 2)
    return good


def results(profiles, extra):
    total = paid = first_any = first_paid = 0
    counts = []
    fixed = []
    for j, records in sorted(profiles.items()):
        mask = priced = 0
        for (credit, signed), (saving, _) in records.items():
            if abs(credit) > extra:
                continue
            found = hits(extra, credit, signed)
            mask |= found
            if saving >= 0:
                priced |= found
        a, b = mask.bit_count(), priced.bit_count()
        upper = (pow(3, 12 << (j - 4), 1 << (j + extra)) - 1) >> j
        fa = mask >> (upper // 2) & 1
        fb = priced >> (upper // 2) & 1
        fixed.append((j, fa, fb))
        counts.append((j, a, b))
        total += a
        paid += b
        first_any += fa
        first_paid += fb
    data = (counts, fixed)
    return (extra, sum(a > 0 for _, a, _ in counts), sum(b > 0 for _, _, b in counts),
            total, paid, first_any, first_paid, max(a for _, a, _ in counts),
            hashlib.sha256(repr(data).encode('ascii')).hexdigest())


def main():
    vals = [18 * k + 4 for k in range(1, 193)]
    costs = charges()
    profiles = release_profiles(vals, 12, costs)
    expected = [
        (1, 0, 0, 0, 0, 0, 0, 0, "9b2736fae34fa1edf57752c72ee223b07026983deefa0bc53232531a1c6cf8d9"),
        (3, 5, 3, 5, 3, 0, 0, 1, "897769b49f976eebc2895e26b84536119cd3d2aa8efdcbb7cf1dd6864bb35e9d"),
        (6, 10, 6, 88, 52, 0, 0, 15, "833e4cfea22f380607949f77e12fb3492239829b4a945d5fb1e2d4aeb49f973b"),
        (9, 44, 26, 1004, 556, 0, 0, 128, "7e84f11df74551bf9ef71b82a219255f79e58e9f00de2391e9159b3cdf0e0fec"),
        (12, 73, 55, 10566, 5736, 1, 1, 1073, "9be50fceb371a67a682cfcad28c962ca0d7d3bbab8e190773981b7875d37b709"),
    ]
    for row in expected:
        actual = results(profiles, row[0])
        check(actual == row, "complete valuation census")
        print(actual, flush=True)


if __name__ == "__main__":
    main()
