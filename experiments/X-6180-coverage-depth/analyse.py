"""X-6180 analysis: at what backward-tree depth does coverage reach a given exponent?"""
import math
import sys


def main(path, X=10**8):
    rows = [l.split() for l in open(path) if not l.startswith('#')]
    data = [(int(r[0]), int(r[1])) for r in rows]
    lX = math.log(X)
    print(f"X = {X:,};  every n <= X reaches 1, deepest at d = {data[-1][0]} shortcut steps\n")
    print("depth at which the backward tree from 1 first covers X^e integers below X:")
    print(f"  {'exponent e':>11} {'target count':>16} {'depth d':>9} {'d / log2(X)':>12}")
    for e in (0.50, 0.70, 0.84, 0.90, 0.95, 0.99, 0.999, 1.0):
        tgt = X**e
        d = next((d for d, c in data if c >= tgt), None)
        if d is None:
            print(f"  {e:>11.3f} {tgt:>16.0f} {'not reached':>9}")
        else:
            print(f"  {e:>11.3f} {tgt:>16.0f} {d:>9} {d/math.log2(X):>12.2f}")
    print()
    print("coverage fraction by depth:")
    print(f"  {'d':>5} {'coverage':>14} {'fraction':>12} {'log(cov)/log(X)':>16}")
    for d, c in data:
        if d % 60 == 0 or d == data[-1][0]:
            print(f"  {d:>5} {c:>14,} {c/X:>12.9f} {math.log(c)/lX:>16.5f}")
    # tail: how much depth is spent on the last sliver
    for frac in (0.99, 0.999, 0.9999, 0.999999):
        d = next((d for d, c in data if c >= frac*X), None)
        print(f"  first depth with coverage >= {frac:>9.6f} of X : d = {d}")
    print(f"\n  the last {X - max(c for _, c in data if _ <= 300):,} integers below X "
          f"(of {X:,}) need depth > 300")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "results/coverage_1e8.txt")
