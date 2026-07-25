"""X-6200 — localise the coverage deficit.

The backward tree from 1 is a genuine tree (each n has the unique parent T(n)), with mean
branching 4/3 (branching.py). So a depth-d tree has ~(4/3)^d nodes, and if none were wasted
the depth needed to cover X^e integers below X would be

    c_naive(e) = e * ln2/ln(4/3) = 2.409421 * e     (in units of log2 X).

Since the tree has no duplicates, the ONLY loss is nodes exceeding X. The gap between measured
c(e) and c_naive(e) is therefore exactly the coverage deficit, and this file locates where it
switches on.
"""
import math

C = math.log(2)/math.log(4/3)
rows = [l.split() for l in open('results/coverage_1e8_fine.txt') if not l.startswith('#')]
data = [(int(r[0]), int(r[1])) for r in rows]
X = 10**8
lg = math.log2(X)

print(f"X = {X:,},  c_naive(e) = {C:.6f} * e\n")
print(f"{'e':>7} {'depth d':>9} {'c(e)=d/log2X':>13} {'c_naive(e)':>11} {'ratio':>7} {'deficit':>9}")
for e in (0.30, 0.50, 0.60, 0.70, 0.75, 0.80, 0.84, 0.88, 0.90, 0.95, 0.99, 0.999):
    t = X**e
    d = next((d for d, c in data if c >= t), None)
    if d is None:
        continue
    cm, cn = d/lg, C*e
    print(f"{e:>7.3f} {d:>9} {cm:>13.3f} {cn:>11.3f} {cm/cn:>7.3f} {cm-cn:>9.3f}")

print("\nper-depth growth ratio coverage(d)/coverage(d-1), against the branching factor 4/3:")
print(f"{'d':>5} {'coverage':>13} {'ratio':>8} {'vs 4/3':>8} {'log(cov)/log(X)':>16}")
prev = None
for d, c in data:
    if prev and d % 8 == 0 and d <= 200:
        r = c/prev_c
        print(f"{d:>5} {c:>13,} {r:>8.4f} {r/(4/3):>8.3f} {math.log(c)/math.log(X):>16.4f}")
    prev, prev_c = d, c

# where does the per-depth ratio first fall below 4/3 in a sustained way?
first = None
for i in range(3, len(data)-3):
    d, c = data[i]
    _, cp = data[i-1]
    if cp and c/cp < 4/3:
        window = [data[j][1]/data[j-1][1] for j in range(i, min(i+8, len(data))) if data[j-1][1]]
        if window and max(window) < 4/3:
            first = d
            break
print(f"\nper-depth growth first falls permanently below 4/3 at d = {first} "
      f"(= {first/lg:.2f} log2 X), where coverage = X^{math.log(dict(data)[first])/math.log(X):.3f}")
