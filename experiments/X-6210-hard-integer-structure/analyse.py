"""Are the hardest integers structured?  Residues, parity, density, and 2-adic profile."""
import math
from collections import Counter

hard = []
for l in open('results/hard_300.txt'):
    n, d = l.split()
    hard.append((int(n), int(d)))
N = len(hard)
X = 10**8
print(f"{N} integers <= {X:,} with total stopping time >= 300  (density {N/X:.3e})\n")

print("residue distribution vs. uniform expectation:")
for M in (2, 3, 4, 6, 8, 9, 16, 5, 7):
    c = Counter(n % M for n, _ in hard)
    exp = N/M
    dev = max(abs(c[r]-exp)/exp for r in range(M) if True)
    top = sorted(c.items(), key=lambda kv: -kv[1])[:4]
    print(f"  mod {M:>2}: max relative deviation {dev:6.3f}   most common: "
          + ", ".join(f"{r}:{v}({v/N:.3f})" for r, v in top))

print("\nspecial structure checks:")
odd = sum(1 for n, _ in hard if n % 2)
print(f"  odd: {odd}/{N} = {odd/N:.4f}   (a hard even n forces n/2 hard, so evens are inherited)")
div3 = sum(1 for n, _ in hard if n % 3 == 0)
print(f"  divisible by 3: {div3}/{N} = {div3/N:.4f}  (after one odd step the orbit avoids"
      f" multiples of 3, so these can only be starts)")

print("\ntop 12 by stopping time:")
for n, d in sorted(hard, key=lambda t: -t[1])[:12]:
    f = []
    m = n
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23):
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        if e:
            f.append(f"{p}^{e}" if e > 1 else str(p))
    fac = "*".join(f) + (f"*{m}" if m > 1 else "") if (f or m > 1) else str(n)
    print(f"  {n:>12}  delay {d:>4}   = {fac}")

print("\ndoubling structure: how many hard n are 2*(another hard n)?")
S = {n for n, _ in hard}
dbl = sum(1 for n in S if n % 2 == 0 and n//2 in S)
print(f"  {dbl}/{N} = {dbl/N:.4f}")
print("\ngap structure of the odd hard integers (are they clustered?):")
oddn = sorted(n for n, _ in hard if n % 2)
gaps = [oddn[i+1]-oddn[i] for i in range(len(oddn)-1)]
print(f"  {len(oddn)} odd values, mean gap {sum(gaps)/len(gaps):.0f}, "
      f"median gap {sorted(gaps)[len(gaps)//2]}, min {min(gaps)}, max {max(gaps)}")
print(f"  expected mean gap if uniform among odds: {X/len(oddn)/2*2:.0f}")
