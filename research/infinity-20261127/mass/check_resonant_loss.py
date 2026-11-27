"""Exact controls for the three suffixes, native lift and ordinary death clock."""
from fractions import Fraction
from itertools import accumulate
from math import comb
import json

def demand(condition, detail):
    if not condition:
        raise ValueError(detail)


def odd_step(x):
    value = 3*x + 1
    exponent = (value & -value).bit_length() - 1
    return exponent, value >> exponent


def follow(x, count):
    gaps = []
    for _ in range(count):
        e, x = odd_step(x)
        gaps.append(e)
    return gaps, x


def passing(es):
    return all(4*clock <= 7*i for i, clock in enumerate(accumulate(es), 1))


def carry(es):
    total, value = 0, 0
    for e in es:
        value = 3*value + (1 << total)
        total += e
    return value


def leaf_replay():
    q = 1 << 56
    words = [
        [1]*31 + [25],
        [1]*27 + [22, 1, 2, 2, 2],
        [1, 2, 2, 2]*8,
    ]
    cs = [carry(w) for w in words]
    demand(cs == [1853015893884545, 58710943741132417, 150865148058652885],
           "suffix carries")
    for w, c in zip(words, cs):
        demand(len(w) == 32 and sum(w) == 56 and passing(w), "suffix gate")
        formula = sum(3**(31-i) * 2**a for i, a in enumerate([0]+list(accumulate(w))[:-1]))
        demand(c == formula, "expanded carry")

    gaps = [b-a for a, b in zip(cs, cs[1:]+[cs[0]+4*q])]
    demand(max(gaps) < 31*q//16, "closed circular coverage")
    # Probe both sides of all phase boundaries and the wrap, respecting parity.
    probes = {1, 4*q-1}
    for c in cs:
        for span in (q//16, 2*q):
            probes.update((c+span+r) % (4*q) for r in (-4, -2, 0, 2, 4))
    for k in (55, 56, 67, 128, 1024):
        factor = pow(3, 1 << k, 4*q)
        demand((2*factor) % (4*q) == 2, "resonance")
        for t in probes:
            a = (q-t) % (4*q)
            witnesses = []
            for c in cs:
                j = ((t-c) % (4*q))//2
                if q//32 <= j < q:
                    demand((a+c+2*factor*j) % (4*q) == q, "selected endpoint")
                    witnesses.append(j)
            demand(witnesses, "phase uncovered")
    # Literal affordable trajectories. These controls exercise the full
    # principal lift even at depths where the dyadic resonance is unavailable.
    actual = 0
    for start in (1, 3, 7, 27, 31, 47, 73, 127, 255, 511):
        for p in (0, 1, 4, 8, 16):
            initial, y = follow(start, p)
            A = sum(initial)
            m = start % (1 << (A+1))
            initial, y = follow(m, p)
            for w, c in zip(words, cs):
                numer = q - 3**32*y - c
                demand(numer % 2 == 0, "lift parity")
                j = (numer//2 * pow(3, -(p+32), q)) % q
                source = m + (1 << (A+1))*j
                ws, z = follow(source, p+32)
                demand(ws == initial+w and source < 1 << (A+57), "literal principal")
                demand(q*z == 3**32*y+c+2*3**(p+32)*j, "literal endpoint")
                demand((odd_step(z)[0] >= 2) == (z % 4 == 1), "literal next exponent")
                actual += 1
    return dict(carries=cs, circular_gaps=gaps, modulus=q, odd_phases=len(probes),
                literal_small_prefix_suffix_paths=actual)


def gate_replay():
    # Two independent clocks: geometric letters versus binary increments.
    rows = []
    for n in (4, 8, 12):
        ab = 7*n//4
        counts = {0: 1}
        for i in range(1, n+1):
            next_counts = {}
            for t, c in counts.items():
                for e in range(1, 7*i//4-t+1):
                    next_counts[t+e] = next_counts.get(t+e, 0)+c
            counts = next_counts
        levels = {(0, 0): 1}
        for E in range(1, ab+1):
            for ones in range(n+1):
                if 7*ones >= 4*E:
                    levels[E, ones] = levels.get((E-1, ones), 0)+levels.get((E-1, ones-1), 0)
        demand(counts == {E:levels[E,n] for E in range(n,ab+1)}, "binary / odd gate")
        P = sum((Fraction(c, 1<<E) for E,c in counts.items()), Fraction(0))
        demand(n*counts[ab] >= comb(ab-1,n-1), "rotation lower bound")
        rows.append(dict(odd_depth=n, boundary_words=counts[ab], probability=str(P)))
    return rows


if __name__ == "__main__":
    print(json.dumps(dict(local=leaf_replay(), original_gate=gate_replay()),
                     sort_keys=True, indent=2))
