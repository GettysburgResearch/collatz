#!/usr/bin/env python3
"""Bounded exact-integer checks of the new finite identities and actual words.

The Lean proof handles the finite arithmetic generally. This checker is a
small check on the Collatz word indexing, endpoint projection, and the
integer scaling in the written collision bound. It is not an escape test.
"""

from collections import Counter
from fractions import Fraction
import json
from math import comb


def require(ok, message):
    if not ok:
        raise ValueError(message)


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def orbit(start, limit=256):
    states, gaps, seen = [start], [], {start}
    while len(gaps) < limit:
        z = 3 * states[-1] + 1
        g = (z & -z).bit_length() - 1
        y = z >> g
        if y in seen:
            break
        gaps.append(g)
        states.append(y)
        seen.add(y)
    return states, gaps


def ceil_log3(h):
    m, p = 0, 1
    while p < h:
        p *= 3
        m += 1
    return m


def main():
    identity_cases = 0
    for m in range(1, 25):
        for k in range(0, 81):
            q1 = sum((k - s) * choose(s - 1, m - 1) for s in range(m, k))
            q2 = sum((k - s) ** 2 * choose(s - 1, m - 1) for s in range(m, k))
            require(q1 == choose(k, m + 1), 'Failed check: q1 == choose(k, m + 1)')
            require(q2 == choose(k, m + 1) + 2 * choose(k, m + 2), 'Failed check: q2 == choose(k, m + 1) + 2 * choose(k, m + 2)')
            identity_cases += 1

    orbit_cases = 0
    distinct_word_cases = 0
    for start in range(1, 512, 2):
        states0, gaps0 = orbit(start)
        n0 = len(gaps0)
        for n in sorted({n0, *[r for r in (8, 16, 32, 64, 128, 256) if r <= n0]}):
            if n == 0:
                continue
            states, gaps = states0[: n + 1], gaps0[:n]
            h = max(states) + 1
            height_m = ceil_log3(h)
            for m in sorted({r for r in (1, 2, 4, 8, height_m) if 1 <= r <= n}):
                words = [tuple(gaps[j - m : j]) for j in range(m, n + 1)]
                word_counts = Counter(words)
                residues = Counter(q % (3**m) for q in states[m:])
                length = n - m + 1
                cost = sum(sum(w) for w in words)
                full_budget = m * sum(gaps)
                require(cost <= full_budget, 'Failed check: cost <= full_budget')
                for word, q in zip(words, states[m:]):
                    a = c = 0
                    for g in word:
                        c = 3 * c + (1 << a)
                        a += g
                    require(((1 << a) * q - c) % (3**m) == 0, 'Failed check: ((1 << a) * q - c) % (3**m) == 0')

                k = (full_budget + length - 1) // length + 1
                q2 = choose(k, m + 1) + 2 * choose(k, m + 2)
                word_collision_numerator = sum(x*x for x in word_counts.values())
                residue_collision_numerator = sum(x*x for x in residues.values())
                require((k*length-full_budget)**2 <= q2*word_collision_numerator, 'Failed check: (k*length-full_budget)**2 <= q2*word_collision_numerator')
                require(word_collision_numerator <= residue_collision_numerator, 'Failed check: word_collision_numerator <= residue_collision_numerator')

                # The original 0..n endpoint window pays exactly its size ratio.
                all_residues = Counter(q % (3**m) for q in states)
                original_collision = Fraction(sum(x*x for x in all_residues.values()), (n+1)**2)
                tail_lower = Fraction((k*length-full_budget)**2, q2*(n+1)**2)
                require(original_collision >= tail_lower, 'Failed check: original_collision >= tail_lower')

                if 3**m >= h:
                    require(len(word_counts) == length, 'Failed check: len(word_counts) == length')
                    require(all(x == 1 for x in word_counts.values()), 'Failed check: all(x == 1 for x in word_counts.values())')
                    require(k*length <= full_budget + choose(k, m+1), 'Failed check: k*length <= full_budget + choose(k, m+1)')
                    distinct_word_cases += 1
                orbit_cases += 1

    return {
        "status": "passed",
        "identity_cases": identity_cases,
        "actual_word_windows": orbit_cases,
        "distinct_word_height_cases": distinct_word_cases,
        "source_range": "positive odd starts 1..511",
        "max_odd_steps": 256,
        "arithmetic": "exact integers and rational numbers",
        "scope": "finite identities, original-source word indexing and collision projection; no asymptotic or escape certification",
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
