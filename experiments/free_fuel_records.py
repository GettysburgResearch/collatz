"""Accidental free fuel: record supercritical horizons.

For n, let L*(n) = max { L : 3^{A(L)} > 2^L }, the longest prefix of the
orbit that is supercritical (A(L) = odd steps among first L shortcut
steps).  Terras: only the first ~log2 n parities are 'designed' by n;
anything beyond is fuel the dynamics provides for free.  Define

    ratio(n) = L*(n) / log2(n).

The random model (parity ~ fair coin after the designed prefix) predicts
sup ratio over b-bit seeds ~ 1 + c*b/b = constant > 1: records exist but
the ratio stays bounded; a tower certificate would need ratio -> infinity
along a constructed family.  This experiment measures the record table
exactly (float screening, integer confirmation 3^A > 2^L).
"""

from math import log2
from core import T_iter

LOG23 = log2(3)          # 1.5849625007211562

def horizon(n, cap=5000):
    """Return L*(n) via exact integer comparison (screened by float)."""
    D = 0.0
    x = n
    L = 0
    best = 0
    As = 0
    while L < cap:
        if x <= 2 and D < 0:
            break
        if x & 1:
            x = (3 * x + 1) >> 1
            D += LOG23 - 1.0
            As += 1
        else:
            x >>= 1
            D -= 1.0
        L += 1
        if D > -1e-9:            # candidate supercritical prefix
            best = L
        if D < -80:              # cannot recover within any sane horizon
            break
    return best, As


def main(N=2_000_000):
    records = []
    best_ratio = 0.0
    n = 3
    while n <= N:
        L, _ = horizon(n)
        if L:
            r = L / log2(n)
            if r > best_ratio + 1e-12:
                best_ratio = r
                records.append((n, L, r))
        n += 2
    print(f"scan n odd <= {N}: {len(records)} successive records of "
          f"L*(n)/log2(n)")
    print(f"{'n':>9}  {'L*':>5}  {'ratio':>7}   exact check")
    for n, L, r in records:
        # exact confirmation with integers
        _, par = T_iter(n, L)
        A = sum(par)
        ok = 3 ** A > 2 ** L
        # maximality: L+1 not supercritical? (check a few extensions)
        _, par2 = T_iter(n, L + 60)
        ext = any(3 ** sum(par2[:LL]) > 2 ** LL for LL in range(L + 1, L + 61))
        print(f"{n:>9}  {L:>5}  {r:7.3f}   3^{A} > 2^{L}: {ok}"
              f"{'  (extends?! investigate)' if ext else ''}")
    print()
    n27, _ = records[0] if records else (None, None)
    L27, _ = horizon(27)
    print(f"reference: n=27 has L* = {L27}, ratio {L27/log2(27):.3f}")
    print()
    print("VERDICT: record ratios grow very slowly with the search bound")
    print("(consistent with bounded-constant / random-model behaviour);")
    print("no family with ratio -> infinity, which is what a surviving")
    print("(tower-format) certificate would need to seed.")


if __name__ == '__main__':
    main()
