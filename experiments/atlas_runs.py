"""Unified four-chart atlas: validity, transitions, free-run statistics.
See H64.md addendum.  V = residues mod 64 where a supercritical 6-step
collision block applies; continuation probability 8/64 per block."""
from core import T_iter
import random, math

V = {14, 15, 18, 19, 54, 55, 60, 61}
assert all(sum(T_iter(64 * 1000 + r, 6)[1]) == 4 for r in V)
outs = {r: T_iter(64 * 7 + r, 6)[0] - 81 * 7 for r in sorted(V)}
assert outs == {14: 20, 15: 20, 18: 26, 19: 26, 54: 71, 55: 71,
                60: 80, 61: 80}
assert all(sum(1 for qr in range(64) if (81 * qr + outs[r]) % 64 in V) == 8
           for r in V)
print("atlas structure verified: 8 valid residues, 8/64 transitions, a=4")

random.seed(9)
runs = {}
N = 300000
for _ in range(N):
    n = random.randrange(1, 10 ** 12)
    n = (n - n % 64) + random.choice(sorted(V))
    r = 0
    while n % 64 in V:
        n, _ = T_iter(n, 6)
        r += 1
        if r > 40:
            break
    runs[r] = runs.get(r, 0) + 1
mean_extra = sum((r - 1) * c for r, c in runs.items()) / N
print("free runs:", dict(sorted(runs.items())), f"mean {mean_extra:.4f} "
      f"vs 1/7 = {1/7:.4f}")
assert abs(mean_extra - 1 / 7) < 0.01

best = (0, None)
for n in range(15, 3_000_000):
    if n % 64 not in V:
        continue
    m, r = n, 0
    while m % 64 in V:
        m, _ = T_iter(m, 6)
        r += 1
        if r > 60:
            break
    if r > best[0]:
        best = (r, n)
print(f"record run n<3e6: {best[0]} blocks at n={best[1]} "
      f"(random-model max ~{math.log(3e6/8)/math.log(8):.1f})")
