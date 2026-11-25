"""Exact finite checks for the unrestricted rank-two reduction."""
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import cache
from pathlib import Path
import json


B = 2**40
CUT = 1600
GRID = 486
PERIODS = {1: (1, 1), 5: (3, 2), 17: (11, 7)}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def step(n, denominator=1):
    return (3*n + denominator)//2 if n % 2 else n//2


@cache
def period(rank):
    length = 2*3**rank
    denominator = 3**(rank+1)
    residues = {pow(2, i, denominator): i for i in range(length)}
    require(len(residues) == length and pow(2, length, denominator) == 1, rank)
    return residues


@dataclass(frozen=True)
class Chart:
    rank: int
    numerator: int
    denominator: int
    upper_last: int
    upper_class: int
    center: int
    entry: int
    odds: int


@cache
def chart(gaps):
    rank = len(gaps)+1
    denominator = 3**(rank+1)
    c, last = 1, 0
    for gap in gaps:
        require(gap >= 1, gaps)
        last += gap
        c = 3*c + 2**last
    upper = -c
    times = []
    for j in range(last+1):
        if upper % 2:
            times.append(j)
        upper = step(upper, denominator//3)
    expected = [0]
    for gap in gaps:
        expected.append(expected[-1]+gap)
    require(upper == 0 and expected == times, ('upper', gaps))
    numerator, odds = -c, 0
    for i in range(CUT):
        if numerator in {-denominator, -5*denominator, -17*denominator}:
            center = -numerator//denominator
            p, o = PERIODS[center]
            end, count = numerator, 0
            for _ in range(p):
                count += end % 2
                end = step(end, denominator)
            require(end == numerator and count == o, center)
            return Chart(rank, c, denominator, last, period(rank)[c % denominator],
                         center, i, odds)
        if numerator >= 0:
            return None
        odds += numerator % 2
        numerator = step(numerator, denominator)
    raise ValueError(('unclassified negative center', gaps))


def check_short(e):
    """Each positive odd source with two supplied odds is exhausted by e,H."""
    c = 3+2**e
    checked = 0
    max_clock = 0
    upper_class = period(2)[c % 27]
    for H in range(upper_class, CUT, 18):
        if H <= e or (1 << H) <= c:
            continue
        z, rem = divmod((1 << H)-c, 27)
        u, rem2 = divmod(9*z+1, 2**e)
        require(rem == rem2 == 0 and z%2 == u%2 == 1 and
                3*u+1 == 2**(H-e), (e, H, z))
        n = z
        j = 0
        while n != 1 and B*n >= z and j < 100000:
            n = step(n)
            j += 1
        require(n == 1 or B*n < z, ('short lower', e, H, j))
        checked += 1
        max_clock = max(max_clock, j)
    return checked, max_clock


def drop_reason(e):
    """A strict comparison at CUT and a positive leading difference imply
    the same comparison after replacing 2^CUT by any larger 2^H."""
    c = 3+2**e
    a, q = -c, 0
    U = 2**CUT
    for j in range(CUT+1):
        # 27 T^j z = a + 2^(H-j) 3^q.
        if 2**j > B*3**q and B*(a+(U >> j)*3**q) < U-c:
            return 'physical drop'
        q += a % 2
        a = step(a, 27)
    row = chart((e,))
    require(row is not None, e)
    if row.center == 1:
        shift = row.entry-row.odds+3
        require(shift >= 0, e)
        if (1 << shift) > 27*B and 27*B*((U >> shift)-1) < U-c:
            # At H, the lower reaches 3^(H-shift)-1, which has
            # the ordinary ancestor 2^(H-shift)-1.
            return 'Mersenne ancestor'
    return 'compare'


def wider_periods(old, new):
    """Return delta and the exponent classes it covers. All comparisons
    are uniform beyond CUT, including positivity and legality at both clocks."""
    require(old.center == new.center, (old, new))
    p, o = PERIODS[old.center]
    num = old.odds-3 - new.odds+new.rank+1
    require(num % o == 0, (old, new))
    dk = num//o
    delta = new.entry-old.entry+p*dk
    up, down = 2**max(delta, 0), 2**max(-delta, 0)
    require(up*27 < down*new.denominator, ('leading height', old, new))
    # Compare both physical sources with the denominators cleared at CUT.
    U = 2**CUT
    require(27*(up*U-down*new.numerator) <
            down*new.denominator*(U-old.numerator), ('height intercept', old, new))
    require(CUT+delta > new.upper_last and (U*up)//down > new.numerator,
            ('positive upper', old, new))
    k = (CUT-old.entry)//p
    require(k+dk >= 0 and old.odds+o*k >= 3, ('first admissible lap', old, new))
    return {H for H in range(GRID)
            if H % 18 == old.upper_class
            and (H+delta) % (2*3**new.rank) == new.upper_class}


def main():
    require(4**101 > 9*B*(1+3**100)+1, 'long first gap threshold')
    total, longest = 0, 0
    by_reason = Counter()
    residual = {}
    for e in range(1, 202):
        n, j = check_short(e)
        total += n
        longest = max(longest, j)
        reason = drop_reason(e)
        by_reason[reason] += 1
        if reason == 'compare':
            row = chart((e,))
            residual[e] = {H for H in range(GRID) if H % 18 == row.upper_class}
    original_rows = len(residual)
    witnesses = json.loads(Path(__file__).with_name('competitors.json').read_text())
    for e, gaps in witnesses:
        require(e in residual and 1 <= len(gaps) <= 4, ('witness', e, gaps))
        old, new = chart((e,)), chart(tuple(gaps))
        require(old is not None and new is not None, gaps)
        covered = wider_periods(old, new)
        require(bool(residual[e] & covered), ('unused witness', e, gaps))
        residual[e] -= covered
    residual = {e: sorted(rows) for e, rows in residual.items() if rows}
    print(json.dumps({
        'height_factor': B, 'finite_clock_cutoff': CUT,
        'first_gaps_checked': 201, 'finite_rank_two_sources': total,
        'maximum_observed_lower_clock_to_hit_or_drop': longest,
        'long_clock_first_gap_counts': by_reason, 'chart_pairs': len(witnesses),
        'grid': GRID, 'admissible_before_chart_comparison': original_rows*(GRID//18),
        'remaining_pair_count': sum(map(len, residual.values())),
        'remaining_H_mod_486_by_e': residual
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
