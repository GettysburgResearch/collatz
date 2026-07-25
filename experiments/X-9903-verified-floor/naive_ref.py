#!/usr/bin/env python3
"""
X-9903 -- third, deliberately dumb reference implementation.
Agent: fable-02-p10

Python integers are arbitrary precision, so this is an unbounded-precision
implementation by construction: no overflow is possible, no guard is needed,
no sieve is used, no memoisation is used, no descent shortcut is used.  It
simply iterates C all the way to 1 and counts the steps.

Its only purpose is to be so obviously correct that agreement with the C
program is evidence about the C program.

Usage:  python3 naive_ref.py L      (default L = 100000)

Prints a digest that must match the C program's `naive`/`tst` digest on the
same range:  max sigma_C, its argmax, the max full-trajectory peak with its
argmax, and the checksum sum_{n=1..L} sigma_C(n).
"""
import sys


def sigma_and_peak(n):
    """Total C-stopping time of n and the maximum value on its C-trajectory."""
    x = n
    peak = n
    steps = 0
    while x != 1:
        if x % 2 == 1:
            x = 3 * x + 1
            if x > peak:
                peak = x
        else:
            x = x // 2
        steps += 1
        if steps > 1000000:
            raise SystemExit("step cap exceeded at n = %d" % n)
    return steps, peak


def main():
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
    maxs, args = 0, 0
    maxp, argp = 0, 0
    checksum = 0
    for n in range(1, L + 1):
        s, p = sigma_and_peak(n)
        checksum += s
        if s > maxs:
            maxs, args = s, n
        if p > maxp:
            maxp, argp = p, n
    print("PYTHON BIGINT NAIVE DIGEST")
    print("  L                        = %d" % L)
    print("  max sigma_C(n)           = %d  at n = %d" % (maxs, args))
    print("  max full-trajectory peak = %d  at n = %d" % (maxp, argp))
    print("  checksum sum sigma_C(n)  = %d" % checksum)


if __name__ == "__main__":
    main()
