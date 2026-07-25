"""Does the depth to reach coverage X^e scale like c(e)*log2(X)?  (O-6182 next attack)"""
import math

SC = [(10**6, 'results/coverage_1e6.txt'), (10**7, 'results/coverage_1e7.txt'),
      (10**8, 'results/coverage_1e8.txt'), (10**9, 'results/coverage_1e9.txt')]
EXP = [0.50, 0.70, 0.84, 0.90, 0.95, 0.99, 0.999]

tab = {}
for X, p in SC:
    try:
        rows = [l.split() for l in open(p) if not l.startswith('#')]
    except FileNotFoundError:
        continue
    data = [(int(r[0]), int(r[1])) for r in rows]
    tab[X] = (data, max(d for d, _ in data))

print(f"{'X':>12} {'log2 X':>8} " + " ".join(f"{'e='+str(e):>9}" for e in EXP) + f" {'full':>7}")
for X in sorted(tab):
    data, dmax = tab[X]
    row = []
    for e in EXP:
        t = X**e
        d = next((d for d, c in data if c >= t), None)
        row.append(f"{d:>9}" if d else f"{'-':>9}")
    print(f"{X:>12} {math.log2(X):>8.2f} " + " ".join(row) + f" {dmax:>7}")

print(f"\nnormalised c(e) = depth / log2(X):")
print(f"{'X':>12} " + " ".join(f"{'e='+str(e):>9}" for e in EXP) + f" {'full':>7}")
for X in sorted(tab):
    data, dmax = tab[X]
    lg = math.log2(X)
    row = []
    for e in EXP:
        t = X**e
        d = next((d for d, c in data if c >= t), None)
        row.append(f"{d/lg:>9.2f}" if d else f"{'-':>9}")
    print(f"{X:>12} " + " ".join(row) + f" {dmax/lg:>7.2f}")
print("\nIf c(e) is roughly constant down each column, depth ~ c(e) log2(X) and c(e) is an")
print("invariant of the problem; if it drifts, the scaling is not logarithmic.")
