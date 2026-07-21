"""Extended atlas record hunt (background): longest valid-run records
for n < 3e7 in the four-chart atlas frame."""
V = frozenset({14,15,18,19,54,55,60,61})
E = {14:20,15:20,18:26,19:26,54:71,55:71,60:80,61:80}
def block(n):
    q, r = divmod(n, 64)
    return 81*q + E[r]
best = 0
recs = []
for n in range(14, 30_000_000):
    if n % 64 not in V: continue
    m, r = n, 0
    while m % 64 in V:
        m = block(m); r += 1
        if r > 80: break
    if r > best:
        best = r
        recs.append((n, r))
        print(f"record: n={n}  run={r} blocks = {6*r} T-steps", flush=True)
import math
print(f"final: {recs[-1] if recs else None}; random-model max ~ "
      f"{math.log(3e7/8)/math.log(8):.2f} blocks")
