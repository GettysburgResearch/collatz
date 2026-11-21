#!/usr/bin/env python3
"""
E1 (EMPIRICAL): exact big-integer search for exponent-parametrized identities
T^a(F(i)) = T^b(G(j)) among one-parameter exponential families.

Map: T(n) = n/2 (n even), (3n+1)/2 (n odd).
Families:  3-type (c*3^e + d)/g   and   2-type (c*2^a + d)/g   (integer members only).
Window: a 3-type member is followed for K3 steps, a 2-type member with exponent a for a + K3
steps (its 2-adically structured phase lasts about a steps).  Two members are linked when their
windows share a value; the pair is recorded with the exact step counts of the first common value.
A relation  q*e_G = p*e_F + delta  with step signature (t_F - s_F, t_G - s_G) (s = exponent for
2-type, 0 for 3-type) is REPORTED only if it holds for EVERY tested exponent of a residue class
r mod M (M <= 32, at least 3 exponents) with the same signature.

Why a window and not "merged somewhere": a first version of this script linked members whose
orbits merged anywhere above 2^44.  That criterion is useless here: for e in [30,400] about 74% of
the pairs (3^e, 3^(e+1)) already coalesce above 2^44 (273 of 370), and one class had 1694 members.
Coalescence of two given orbits is a finite fact about two numbers; it is not an identity in e.

Finite computation: evidence, not proof.  The identities used later are proved in Pow3Families.lean.
"""
import sys, time
from collections import defaultdict
from math import gcd

K3 = 16
E3 = (30, 125)
E2 = (48, 143)

def fam_name(f):
    t, c, d, g = f
    b = '3^e' if t == '3' else '2^a'
    s = f"{c}*{b}" if c != 1 else b
    if d > 0: s += f"+{d}"
    elif d < 0: s += f"{d}"
    if g != 1: s = f"({s})/{g}"
    return s

def members():
    mem = []
    for c in [1,2,4,5,7,8,10,11,13,14,16]:
        for d in range(-16, 17):
            if c % 2 == 0 and d % 2 == 0: continue
            for g in (1,5,7):
                if g > 1 and gcd(c, abs(d)) % g == 0: continue
                for e in range(E3[0], E3[1]+1):
                    v = c*3**e + d
                    if v % g: continue
                    mem.append((('3',c,d,g), e, v//g))
    for c in [1,3,5,7,9,11,13,15]:
        for d in range(-15, 16, 2):
            for g in (1,3,9,5,7):
                if g > 1 and gcd(c, abs(d)) % g == 0: continue
                for a in range(E2[0], E2[1]+1):
                    v = c*2**a + d
                    if v % g: continue
                    mem.append((('2',c,d,g), a, v//g))
    return mem

SL = {('3','3'): [(1,1)], ('2','2'): [(1,1)],
      ('2','3'): [(1,1),(1,2),(2,3),(1,3),(7,11)],
      ('3','2'): [(1,1),(2,1),(3,2),(3,1),(11,7)]}

def main():
    t0 = time.time()
    mem = members()
    N = len(mem)
    exps = defaultdict(set)
    for f, e, v in mem: exps[f].add(e)
    print(f"members: {N}  families: {len(exps)}  K3={K3}  3-type e in {E3}, 2-type a in {E2}")
    d = {}
    for idx, (f, e, v) in enumerate(mem):
        K = K3 if f[0] == '3' else e + K3
        n = v
        base = idx << 12
        for t in range(K + 1):
            cur = d.get(n)
            if cur is None: d[n] = base | t
            elif type(cur) is int: d[n] = [cur, base | t]
            else: cur.append(base | t)
            n = (3*n + 1) >> 1 if n & 1 else n >> 1
    print(f"stored values: {len(d)}  time {time.time()-t0:.1f}s")
    pm = {}
    for v, cur in d.items():
        if type(cur) is list:
            L = len(cur)
            for x in range(L):
                cx = cur[x]; ix = cx >> 12; tx = cx & 4095
                for y in range(x+1, L):
                    cy = cur[y]; iy = cy >> 12; ty = cy & 4095
                    old = pm.get((ix, iy))
                    if old is None or tx < old[0]: pm[(ix, iy)] = (tx, ty)
    del d
    print(f"linked pairs: {len(pm)}  time {time.time()-t0:.1f}s")
    rel = defaultdict(set)
    for (i, j), (ti, tj) in pm.items():
        for (a, ta, b, tb) in ((i, ti, j, tj), (j, tj, i, ti)):
            F, eF, _ = mem[a]; G, eG, _ = mem[b]
            sa = ta - (eF if F[0] == '2' else 0)
            sb = tb - (eG if G[0] == '2' else 0)
            for (p, q) in SL[(F[0], G[0])]:
                rel[(F, G, p, q, q*eG - p*eF, sa, sb)].add(eF)
    rows = []
    for key, es in rel.items():
        if len(es) < 3: continue
        F, G, p, q, delta, sa, sb = key
        cand = sorted(exps[F])
        def partner_ok(e):
            x = p*e + delta
            return x % q == 0 and (x//q) in exps[G] and not (F == G and x//q == e)
        done = []
        for M in (1,2,4,8,16,32):
            for r in range(M):
                if any(r % M0 == r0 for (r0, M0) in done): continue
                ex = [e for e in cand if e % M == r and partner_ok(e)]
                if len(ex) >= 3 and all(e in es for e in ex):
                    done.append((r, M))
                    rows.append((F, G, p, q, delta, sa, sb, r, M, len(ex)))
    print(f"uniform relations (every tested exponent of a class mod M<=32, constant signature): {len(rows)}")
    bytype = defaultdict(int)
    for r in rows: bytype[(r[0][0], r[1][0], r[8])] += 1
    print("  count by (type F, type G, modulus):", sorted(bytype.items()))
    core = [('3',1,0,1), ('3',1,1,1), ('3',1,-1,1), ('2',1,-1,1), ('2',1,1,1), ('2',1,1,3)]
    core_ext = core + [('3',2,1,1), ('3',2,-1,1), ('3',4,1,1), ('3',4,-1,1), ('3',1,2,1), ('3',1,-2,1),
                       ('2',1,-1,3), ('2',3,1,1), ('2',3,-1,1)]
    def fmt(r):
        F, G, p, q, delta, sa, sb, res, M, n = r
        rel_s = (f"e_G = e_F{delta:+d}" if (p, q) == (1, 1) else f"{q}*e_G = {p}*e_F{delta:+d}")
        return (f"{fam_name(F):<10} ~ {fam_name(G):<10} {rel_s:<18} e_F = {res:>2} mod {M:<2} "
                f"steps(F,G)=({'a' if F[0]=='2' else ''}{sa:+d},{'a' if G[0]=='2' else ''}{sb:+d})  n={n}")
    # Output is deliberately compact: counts, plus the relations among a short list of core families.
    for F in core:
        mine = [r for r in rows if r[0] == F]
        cnt = defaultdict(int)
        for r in mine: cnt[(r[1][0], r[8])] += 1
        print(f"\n=== {fam_name(F)} : {len(mine)} uniform relations; by (type of G, modulus): {sorted(cnt.items())}")
        cc = [r for r in mine if r[1] in core_ext]
        cc.sort(key=lambda r: (r[8], r[1][0], fam_name(r[1]), r[4], r[7]))
        for r in cc[:40]:
            print("  " + fmt(r))
        if len(cc) > 40: print(f"  ... {len(cc)-40} more core-core rows")
    selfr = [r for r in rows if r[0] == r[1]]
    cnt = defaultdict(int)
    for r in selfr: cnt[(r[0][0], r[8])] += 1
    print(f"\n=== same family, different exponent: {len(selfr)} uniform rows; by (type, modulus): {sorted(cnt.items())}")
    for r in sorted([r for r in selfr if r[0] in core_ext], key=lambda r: (r[8], fam_name(r[0]), r[4], r[7])):
        print("  " + fmt(r))
    known = {('2',1,-1,3), ('2',3,-3,9)}      # (2^a-1)/3 = (4^j-1)/3 for even a: T of it is a power of two
    kk = [r for r in rows if (r[0] in core and r[1] in known) or (r[1] in core and r[0] in known)]
    print(f"\nuniform relations between a core family and (2^a-1)/3 (trivially in C): {len(kk)}")
    print("note: four 2-type labels duplicate others: (3*2^a+-3)/9 = (2^a+-1)/3, (3*2^a+-15)/9 = (2^a+-5)/3")
    print(f"total time {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
