"""Analysis for X-6135: compare the measured universal floor mu_L with the exact
binomial-tail density and with the dimension prediction of T-6131."""
import math
import sys
from math import comb, log2

ALPHA = math.log(2) / math.log(3)


def H2(p):
    return -p*log2(p) - (1-p)*log2(1-p)


def load(path):
    out = []
    for line in open(path):
        if line.startswith('#'):
            continue
        L, need, mu, _ = line.split()
        out.append((int(L), int(need), int(mu)))
    return out


def slope(pairs):
    n = len(pairs)
    sx = sum(a for a, _ in pairs); sy = sum(b for _, b in pairs)
    sxx = sum(a*a for a, _ in pairs); sxy = sum(a*b for a, b in pairs)
    return (n*sxy - sx*sy) / (n*sxx - sx*sx)


def main(path):
    data = load(path)
    Lmax = data[-1][0]
    lo = max(20, Lmax//2)
    print(f"alpha = log2/log3 = {ALPHA:.12f}")
    print(f"H_2(alpha)        = {H2(ALPHA):.12f}")
    print(f"codimension       = {1-H2(ALPHA):.12f}   (T-6131(c))")
    print(f"deepest exact level: L = {Lmax}\n")
    print(f"{'L':>5} {'need':>5} {'mu_L':>12} {'log2 mu_L':>10} {'1/p_L exact':>14} {'mu_L*p_L':>10}")
    step = max(1, Lmax//12)
    for L, need, mu in data:
        if L % step:
            continue
        p = sum(comb(L, j) for j in range(need, L+1)) / 2**L
        print(f"{L:>5} {need:>5} {mu:>12} {log2(mu):>10.2f} {1/p:>14.1f} {mu*p:>10.2f}")

    tail = [(L, log2(mu)) for L, _, mu in data if L >= lo]
    tailp = [(L, -log2(sum(comb(L, j) for j in range(need, L+1)) / 2**L))
             for L, need, _ in data if L >= lo]
    print(f"\nlocal slopes over L in [{lo}, {Lmax}]:")
    print(f"  measured   d log2(mu_L)/dL          = {slope(tail):.5f}")
    print(f"  exact tail d log2(1/p_L)/dL         = {slope(tailp):.5f}")
    print(f"  asymptotic 1 - H_2(alpha)           = {1-H2(ALPHA):.5f}")

    runs = {}
    for L, _, mu in data:
        runs.setdefault(mu, []).append(L)
    longest = max(runs.items(), key=lambda kv: len(kv[1]))
    print(f"\nlongest run of a single floor value: x = {longest[0]} is mu_L for "
          f"L in [{longest[1][0]}, {longest[1][-1]}] ({len(longest[1])} depths)")

    print("\ncomparison with the six-branch chart (X-6110), per Collatz step:")
    fit = slope(tail)
    for N, m in [(8, 181625992579115023082252809688279976000),
                 (12, 83301137368103499460139839972641009013711852735287572369408),
                 (16, 4629285799073801695890071893291563216294381998435632568233291338101143197194568)]:
        L = 19*N
        floor_est = 2**(fit*L + (log2(data[-1][2]) - fit*Lmax))
        print(f"  N={N:>2}  L={L:>3}   six-branch m_N = 2^{log2(m):>6.1f}   "
              f"universal floor ~ 2^{log2(floor_est):>5.1f}   ratio ~ 2^{log2(m/floor_est):>6.1f}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "results/floor.txt")
