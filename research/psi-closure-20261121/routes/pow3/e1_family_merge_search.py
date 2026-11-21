#!/usr/bin/env python3
"""
E1 (EMPIRICAL): exact big-integer orbit-merge search among one-parameter exponential families.

Map: T(n) = n/2 (n even), (3n+1)/2 (n odd).
Families:  3-type (c*3^e + d)/g   and   2-type (c*2^a + d)/g   (only integer members).
For every member the T-orbit is followed while the value is >= 2^THR_BITS.  Values == 5 (mod 8)
are stored ("distinguished points"); an orbit that reaches a stored point has merged with the
orbit that stored it.  Union-find gives the classes "merged above 2^THR_BITS".
Finite computation: evidence, not proof.  Every structural link found here has to be proved
separately (see Pow3Families.lean).
"""
import sys, time
from collections import defaultdict, Counter
from math import gcd

THR_BITS = 44
THR = 1 << THR_BITS
E3 = (30, 92)
E2 = (48, 146)
EXT = 400

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
                hi = EXT if (c == 1 and abs(d) <= 1 and g == 1) else E3[1]
                for e in range(E3[0], hi+1):
                    v = c*3**e + d
                    if v % g: continue
                    mem.append((('3',c,d,g), e, v//g))
    for c in [1,3,5,7,9,11,13,15]:
        for d in range(-15, 16, 2):
            for g in (1,3,9,5,7):
                if g > 1 and gcd(c, abs(d)) % g == 0: continue
                hi = EXT if (c == 1 and abs(d) == 1 and g in (1,3)) else E2[1]
                for a in range(E2[0], hi+1):
                    v = c*2**a + d
                    if v % g: continue
                    mem.append((('2',c,d,g), a, v//g))
    return mem

SLOPES = [(1,1),(1,2),(2,1),(2,3),(3,2),(1,3),(3,1),(7,11),(11,7)]

def desc(es):
    es = sorted(set(es))
    if len(es) >= 3:
        d = es[1]-es[0]
        if all(es[i+1]-es[i] == d for i in range(len(es)-1)):
            return f"e={es[0]}..{es[-1]} step {d} (n={len(es)})"
    return "e in " + ",".join(map(str, es[:16])) + ("..." if len(es) > 16 else "") + f" (n={len(es)})"

def analyze(pairs, minc):
    out = []
    for p, q in SLOPES:
        cnt = defaultdict(list)
        for ef, eg in pairs:
            cnt[q*eg - p*ef].append(ef)
        for delta, lst in cnt.items():
            if len(set(lst)) >= minc:
                out.append((len(set(lst)), p, q, delta, lst))
    out.sort(key=lambda r: (-r[0], r[1], r[2], r[3]))
    return out

def main():
    t0 = time.time()
    mem = members()
    N = len(mem)
    fams = sorted(set(m[0] for m in mem))
    print(f"members: {N}  families: {len(fams)}  threshold: 2^{THR_BITS}")
    parent = list(range(N))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    seen = {}
    links = []
    steps = 0
    for idx in range(N):
        n = mem[idx][2]
        t = 0
        while n >= THR:
            if n & 7 == 5:
                hit = seen.get(n)
                if hit is not None:
                    links.append((idx, t, hit[0], hit[1], n.bit_length()))
                    a, b = find(idx), find(hit[0])
                    if a != b: parent[a] = b
                    break
                seen[n] = (idx, t)
            n = (3*n + 1) >> 1 if n & 1 else n >> 1
            t += 1
        steps += t
    print(f"orbit steps: {steps}  stored points: {len(seen)}  links: {len(links)}  time {time.time()-t0:.1f}s")
    comps = defaultdict(list)
    for i in range(N): comps[find(i)].append(i)
    multi = [v for v in comps.values() if len(v) > 1]
    print("classes with >=2 members:", len(multi), " largest:", max(len(v) for v in multi))
    print("class-size histogram (size:count):", sorted(Counter(len(v) for v in multi).items())[:40])
    rel = defaultdict(list)
    for comp in multi:
        for i in comp:
            fi, ei, _ = mem[i]
            for j in comp:
                if i == j: continue
                fj, ej, _ = mem[j]
                rel[(fi, fj)].append((ei, ej))
    # full table
    rows = []
    for (F, G), pairs in rel.items():
        for (cnt, p, q, delta, lst) in analyze(pairs, 5):
            rows.append((F, G, cnt, p, q, delta, desc(lst)))
    rows.sort(key=lambda r: (r[0], -r[2], r[1]))
    with open("e1_relations.tsv", "w") as fh:
        fh.write("# F\tG\tcount\trelation: q*e_G = p*e_F + delta\tp\tq\tdelta\texponents_of_F\n")
        for (F, G, cnt, p, q, delta, ds) in rows:
            fh.write(f"{fam_name(F)}\t{fam_name(G)}\t{cnt}\t{q}*eG={p}*eF{delta:+d}\t{p}\t{q}\t{delta}\t{ds}\n")
    print("relation rows (count>=5):", len(rows), "-> e1_relations.tsv")
    core = [('3',1,0,1), ('3',1,1,1), ('3',1,-1,1), ('2',1,-1,1), ('2',1,1,1), ('2',1,1,3)]
    for F in core:
        print(f"\n=== {fam_name(F)} ===")
        lines = [r for r in rows if r[0] == F]
        lines.sort(key=lambda r: -r[2])
        for (F_, G, cnt, p, q, delta, ds) in lines[:28]:
            print(f"  ~ {fam_name(G):<22} {q}*eG={p}*eF{delta:+d}  n={cnt:<4} {ds}")
        if len(lines) > 28: print(f"  ... {len(lines)-28} more rows in e1_relations.tsv")
    print("\n=== self-links (same family, different exponent), top rows ===")
    selfrows = [r for r in rows if r[0] == r[1]]
    selfrows.sort(key=lambda r: -r[2])
    for (F, G, cnt, p, q, delta, ds) in selfrows[:30]:
        print(f"  {fam_name(F):<22} {q}*e'={p}*e{delta:+d}  n={cnt:<4} {ds}")
    # P3 internal: every pair of distinct powers of three merged above threshold
    P3 = ('3',1,0,1)
    pp = sorted(set((min(a,b), max(a,b)) for (a,b) in rel.get((P3,P3), [])))
    print(f"\npairs (e,e') with 3^e ~ 3^e' merged above 2^{THR_BITS}, e,e' in [{E3[0]},{EXT}]: {len(pp)}")
    print("  ", pp[:60])
    with open("e1_pow3_classes.txt", "w") as fh:
        fh.write(f"# class (merged above 2^{THR_BITS}) of 3^e for e = {E3[0]}..{E3[1]}: other family members\n")
        for i in range(N):
            F, e, _ = mem[i]
            if F == P3 and e <= E3[1]:
                comp = comps[find(i)]
                others = sorted((fam_name(mem[j][0]), mem[j][1]) for j in comp if j != i)
                fh.write(f"3^{e}: " + "; ".join(f"{nm}@{ex}" for nm, ex in others) + "\n")
    print(f"total time {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
