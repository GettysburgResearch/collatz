"""Splice search.

Every symbolic EXIT configuration (X, w(k)) of the -5 block machine has
value of the exact form
        n(k) = (alpha * 8^k + beta) / d,     alpha, beta in Z, d in {1,7},
so 2-adically n(k) -> rho := beta/d as k -> infinity: the family follows
the parity trajectory of the rational TEMPLATE rho for ~3k steps while
the perturbation (alpha/d)*8^k is multiplied by 3^{#odd}/2^{#steps}.

By sign--criticality, the landing cycle of rho decides everything:
  * landing on a NEGATIVE cycle  => the tail keeps amplifying at
    supercritical density while the stored block lasts: a genuine
    second amplifier stage (the splice the route needs);
  * landing on a POSITIVE cycle  => subcritical sink (as in S6).

This script: (1) computes rho for every EXIT of the seed sweep,
(2) follows rho exactly to its landing cycle, (3) classifies, and
(4) reports the best composite loops (seed -> exit -> landing) with
exact odd/step counts, plus any negative landings found.
"""

from fractions import Fraction
from core import T, T_iter, is_odd
from blockmachine import (S5, PH, seed_sweep, derive, fmt, concretize)


def exit_value_form(X, segs):
    """n(k) = a8*8^k + b8 with a8, b8 Fractions (denominator | 7)."""
    k1, k2 = 60, 61
    q1 = Fraction(sum(d * 8 ** i for i, d in enumerate(concretize(segs, k1))))
    q2 = Fraction(sum(d * 8 ** i for i, d in enumerate(concretize(segs, k2))))
    a = (q2 - q1) / (8 ** k2 - 8 ** k1)
    b = q1 - a * 8 ** k1
    # config value n = 8 q - s_X
    A8, B8 = 8 * a, 8 * b - S5.s[X]
    # sanity at a third k
    k3 = 65
    q3 = Fraction(sum(d * 8 ** i for i, d in enumerate(concretize(segs, k3))))
    assert 8 * q3 - S5.s[X] == A8 * 8 ** k3 + B8
    # alpha may carry a power of 2 in its denominator (block offset shifts);
    # the template must have odd denominator to be a valid 2-adic rational.
    assert B8.denominator % 2 == 1
    assert (A8 * 8 ** k3).denominator % 2 == 1
    return A8, B8


def land(rho, cap=3000):
    """Follow the rational template rho to a cycle.
    Returns dict with transient length tau, odd count in transient,
    cycle tuple (canonical rotation), cycle length p, odd count a."""
    seen = {}
    x = rho
    seq = []
    while x not in seen:
        if len(seq) > cap:
            return None
        seen[x] = len(seq)
        seq.append(x)
        x = T(x)
    i = seen[x]
    trans, cyc = seq[:i], seq[i:]
    mn = min(range(len(cyc)), key=lambda j: cyc[j])
    cyc_canon = tuple(cyc[mn:] + cyc[:mn])
    return dict(tau=i, odd_trans=sum(1 for y in trans if is_odd(y)),
                cycle=cyc_canon, p=len(cyc),
                a=sum(1 for y in cyc if is_odd(y)),
                neg=cyc_canon[0] < 0)


def main():
    seeds, results = seed_sweep()
    exits = [(X, pref, v, suf, rec) for X, pref, v, suf, rec in results
             if rec['kind'] == 'EXIT']
    print(f"{len(exits)} EXIT configurations")

    from collections import Counter, defaultdict
    landings = Counter()
    neg_landings = []
    best = []
    templates = {}
    for X, pref, v, suf, rec in exits:
        Xe, segse = rec['X'], rec['segs']
        A8, B8 = exit_value_form(Xe, segse)
        rho = B8
        key = rho
        if key not in templates:
            templates[key] = land(rho)
        L = templates[key]
        if L is None:
            landings['DIVERGED?'] += 1
            neg_landings.append((X, pref, v, suf, rec, rho, None))
            continue
        cyc0 = L['cycle'][0]
        landings[(cyc0, L['p'], L['a'])] += 1
        if L['neg']:
            neg_landings.append((X, pref, v, suf, rec, rho, L))
        # composite loop bookkeeping: seed ->(3*steps macro)-> exit
        # ->(tau bridge steps)-> cycle entry.  In-system part has density
        # exactly 2/3; bridge has odd_trans/tau.
        S = 3 * rec['steps'] + L['tau']
        O = 2 * rec['steps'] + L['odd_trans']
        best.append((Fraction(O, S) if S else Fraction(0), S, O,
                     X, pref, v, suf, rec, rho, L))

    print("\n== landing cycles of exit templates ==")
    for key, cnt in landings.most_common():
        if key == 'DIVERGED?':
            print(f"  {cnt:6d}  no cycle within cap (investigate!)")
            continue
        c0, p, a = key
        sup = 3 ** a > 2 ** p
        print(f"  {cnt:6d}  cycle through {c0}  (p={p}, a={a}, "
              f"{'SUPERcritical/NEGATIVE' if sup else 'subcritical/positive'})")

    print(f"\n== negative landings: {len(neg_landings)} ==")
    for X, pref, v, suf, rec, rho, L in neg_landings[:20]:
        seed = [('d', d) for d in pref] + [('b', v, 0)] + \
               [('d', d) for d in suf]
        print(f"  seed {fmt(X, seed)}  exits {fmt(rec['X'], rec['segs'])}")
        print(f"      template rho = {rho}, lands {L}")

    # best composite densities (seed to cycle entry), need > log_3 2
    best.sort(key=lambda t: -t[0])
    print("\n== best composite (seed -> exit -> landing) densities ==")
    print("   (need > log_3 2 = 0.630929...; in-system part alone is 2/3)")
    shown = set()
    for dens, S, O, X, pref, v, suf, rec, rho, L in best[:1000]:
        sig = (rho, rec['steps'])
        if sig in shown:
            continue
        shown.add(sig)
        if len(shown) > 12:
            break
        seed = [('d', d) for d in pref] + [('b', v, 0)] + [('d', d) for d in suf]
        crit = "SUPER" if 3 ** O > 2 ** S else "sub"
        print(f"  {O:3d}/{S:3d} = {float(dens):.5f} ({crit})  "
              f"{fmt(X, seed)} -> rho={rho} -> cycle at {L['cycle'][0]} "
              f"(cycle density {L['a']}/{L['p']})")
    return exits, landings, neg_landings, best


if __name__ == '__main__':
    main()
