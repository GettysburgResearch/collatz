#!/usr/bin/env python3
"""layers_numeric.py -- exact big-integer experiments for routes/layers.

Everything printed here is EMPIRICAL (finite computation). Nothing here is a proof.

T(n) = n/2 (n even), (3n+1)/2 (n odd);  S(c) = c/2 (c even), (3c-1)/2 (c odd).
rank(n) = number of odd T-steps on the orbit of n before its first visit to 1.
y_j = (4^j - 1)/3  (the odd numbers of rank 1 are y_j, j >= 2).

Part 1  brute-force check of the rank-0/1/2 parametrizations.
Part 2  exact iterate identities behind the layer families (asserted).
Part 3  S-orbits of 3^b+1, 3^b-1, 2*3^b-1: entry into the known 3x-1 cycles.
Part 4  hypothesis H at rank 1: merge classes of the two-parameter families against
        one-parameter exponential families (first orbit point below 2^40 as class label).
Part 5  rank 2 (three parameters): same test against one-parameter families and rank-1 families.
"""
import math
import sys
import time
from fractions import Fraction
from collections import defaultdict

T0 = time.time()


def T(n):
    return n >> 1 if not n & 1 else (3 * n + 1) >> 1


def S(c):
    return c >> 1 if not c & 1 else (3 * c - 1) >> 1


def Tit(t, n):
    for _ in range(t):
        n = n >> 1 if not n & 1 else (3 * n + 1) >> 1
    return n


def Sit(t, c):
    """(S^t(c), number of odd iterates among c, S c, ..., S^(t-1) c)."""
    o = 0
    for _ in range(t):
        if c & 1:
            o += 1
            c = (3 * c - 1) >> 1
        else:
            c >>= 1
    return c, o


def rank_capped(n, cap):
    r = 0
    while n != 1:
        if n & 1:
            r += 1
            if r > cap:
                return None
        n = n >> 1 if not n & 1 else (3 * n + 1) >> 1
    return r


def y(j):
    return (4 ** j - 1) // 3


CYC = [[1], [5, 7, 10], [17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34]]
CYCSET = {c: i for i, cy in enumerate(CYC) for c in cy}
for cy in CYC:
    for i, c in enumerate(cy):
        assert S(c) == cy[(i + 1) % len(cy)]

TH = 1 << 40      # class label = first orbit point below TH
MIN = 1 << 64     # only starts >= MIN are classified


def fp(n):
    while n >= TH:
        n = n >> 1 if not n & 1 else (3 * n + 1) >> 1
    return n


def orbit_dict(n):
    d = {}
    s = 0
    while n >= TH:
        d[n] = s
        n = n >> 1 if not n & 1 else (3 * n + 1) >> 1
        s += 1
    d[n] = s
    return d


def first_hit(n, d):
    s = 0
    while True:
        if n in d:
            return s, d[n], n
        if n < TH:
            return None
        n = n >> 1 if not n & 1 else (3 * n + 1) >> 1
        s += 1


def orbit_info(n):
    """point -> (steps, odd steps before it, least odd point before it)."""
    d = {}
    s = 0
    o = 0
    mu = None
    while True:
        d[n] = (s, o, mu)
        if n < TH:
            return d
        if n & 1:
            o += 1
            if mu is None or n < mu:
                mu = n
            n = (3 * n + 1) >> 1
        else:
            n >>= 1
        s += 1


def first_hit_info(n, d):
    s = 0
    o = 0
    mu = None
    while True:
        if n in d:
            return s, o, mu, d[n], n
        if n < TH:
            return None
        if n & 1:
            o += 1
            if mu is None or n < mu:
                mu = n
            n = (3 * n + 1) >> 1
        else:
            n >>= 1
        s += 1


def log(*a):
    print(*a)
    sys.stdout.flush()


# ----------------------------------------------------------------------------- Part 1
def part1(X=300000):
    log("== Part 1: parametrization of ranks 0,1,2 (brute force up to %d)" % X)
    brute = {0: set(), 1: set(), 2: set()}
    for x in range(1, X + 1):
        r = rank_capped(x, 2)
        if r is not None:
            brute[r].add(x)
    P0 = set()
    a = 0
    while 2 ** a <= X:
        P0.add(2 ** a)
        a += 1
    odd1 = [y(j) for j in range(2, 40)]
    P1 = set()
    for u in odd1:
        b = 0
        while 2 ** b * u <= X:
            P1.add(2 ** b * u)
            b += 1
    odd2 = []
    for yy in odd1:
        for e in range(1, 60):
            if (2 ** e * yy) % 3 == 1:
                u = (2 ** e * yy - 1) // 3
                if u % 2 == 1:
                    odd2.append(u)
    P2 = set()
    for u in odd2:
        b = 0
        while 2 ** b * u <= X:
            P2.add(2 ** b * u)
            b += 1
    ok = (brute[0] == P0, brute[1] == P1, brute[2] == P2)
    log("   rank0 == {2^a}: %s (%d);  rank1 == {2^b y_j, j>=2}: %s (%d);  "
        "rank2 == {2^b (2^e y_j - 1)/3}: %s (%d)" % (ok[0], len(P0), ok[1], len(P1), ok[2], len(P2)))
    assert all(ok)
    return odd1, odd2


# ----------------------------------------------------------------------------- Part 2
def part2(odd1, odd2):
    log("== Part 2: exact iterate identities (all asserted)")
    n_checks = 0
    # (a) T^b(3*2^b*u - 1) = 3^(b+1) u - 1
    for b in range(0, 14):
        for u in range(1, 200, 2):
            assert Tit(b, 3 * 2 ** b * u - 1) == 3 ** (b + 1) * u - 1
            n_checks += 1
    # (b) forward rank 1 landing: T^(b+2j)(2^b(4^j-1)-1) = 3^(b+o) - S^(2j)(3^b+1)
    for b in range(0, 40):
        for j in range(2, 40):
            N = 2 ** b * (4 ** j - 1) - 1
            assert Tit(b, N) == 3 ** b * 4 ** j - 3 ** b - 1
            c, o = Sit(2 * j, 3 ** b + 1)
            assert Tit(b + 2 * j, N) == 3 ** (b + o) - c
            n_checks += 1
    # (c) collapse: x = 3 mod 4  =>  T^2(x-1) = T^2(3x-1)
    for x in range(3, 4000, 4):
        assert Tit(2, x - 1) == Tit(2, 3 * x - 1)
        n_checks += 1
    #     hence F1(2n,j) ~ F1(2n+1,j), common point 9^(n+1) 2^(2j-3) - (9^(n+1)-1)/8
    for n in range(0, 20):
        for j in range(2, 30):
            A = 9 ** n * 4 ** j - 9 ** n - 1
            B = 3 ** (2 * n + 1) * 4 ** j - 3 ** (2 * n + 1) - 1
            common = 9 ** (n + 1) * 2 ** (2 * j - 3) - (9 ** (n + 1) - 1) // 8
            assert Tit(3, A) == common and Tit(3, B) == common
            n_checks += 1
    # (d) forward rank 2 landing
    for b in range(0, 16):
        for e in range(1, 20):
            for j in range(2, 14):
                yy = y(j)
                if (2 ** e * yy) % 3 != 1:
                    continue
                u = (2 ** e * yy - 1) // 3
                N = 3 * 2 ** b * u - 1
                assert Tit(b, N) == 3 ** b * 2 ** e * yy - (3 ** b + 1)
                ce, oe = Sit(e, 3 ** b + 1)
                k = b + oe
                assert Tit(b + e, N) == 3 ** k * yy - ce
                if k >= 1:
                    c2, o2 = Sit(2 * j, ce + 3 ** (k - 1))
                    assert Tit(b + e + 2 * j, N) == 3 ** (k - 1 + o2) - c2
                n_checks += 1
    # (e) reverse layers: m = (2^b u + 1)/3 with u odd of rank r
    for r, odds in ((0, [1]), (1, odd1[:12]), (2, [u for u in odd2 if u < 10 ** 12][:400])):
        for u in odds:
            for b in range(0, 16):
                if (2 ** b * u) % 3 != 2:
                    continue
                m = (2 ** b * u + 1) // 3
                if b >= 1:
                    assert m % 2 == 1 and T(m) == 2 ** (b - 1) * u + 1
                    i = (b - 1) // 2
                    if (b - 1) % 2 == 0:
                        assert u % 3 == 1
                        v = u
                    else:
                        assert u % 3 == 2
                        v = 2 * u
                    assert Tit(2 * i, 4 ** i * v + 1) == 3 ** i * v + 1
                else:
                    assert u % 3 == 2 and m % 2 == 0
                    if m % 8 == 2:
                        assert Tit(3, m) == (3 * m + 2) // 8
                n_checks += 1
    # reverse rank 1 families in S-unit form and their landings
    for k in range(0, 30):
        for n in range(4, 40, 3):
            N = 3 ** k * 4 ** n - (3 ** k - 1)
            assert N == 3 ** (k + 1) * y(n) + 1 and y(n) % 3 == 1
            c, o = Sit(2 * n, 3 ** k - 1)
            assert Tit(2 * n, N) == 3 ** (k + o) - c
            if k >= 1:
                assert T(3 ** k * y(n)) * 2 == 3 ** (k + 1) * y(n) + 1   # tripling form
            n_checks += 1
        for n in range(2, 40, 3):
            N = 3 ** k * 2 * 4 ** n - (2 * 3 ** k - 1)
            assert N == 3 ** (k + 1) * 2 * y(n) + 1 and y(n) % 3 == 2
            c, o = Sit(2 * n + 1, 2 * 3 ** k - 1)
            assert Tit(2 * n + 1, N) == 3 ** (k + o) - c
            n_checks += 1
    # even part of reverse rank 1: 9m = 4^(i+3)+2  =>  T^3(m) = (2*4^(i+1)+1)/3 ~ 3^i
    for i in range(2, 60, 3):
        m = (4 ** (i + 3) + 2) // 9
        assert 9 * m == 4 ** (i + 3) + 2
        J = (2 * 4 ** (i + 1) + 1) // 3
        assert Tit(3, m) == J and T(J) == 4 ** (i + 1) + 1
        assert Tit(2 * (i + 1), 4 ** (i + 1) + 1) == 3 ** (i + 1) + 1 == 2 * T(3 ** i)
        n_checks += 1
    # Mersenne parity collapse: 3^a - 1 ~ 3^(a+1) - 1 for odd a
    for a in range(1, 200, 2):
        assert Tit(3, 3 ** a - 1) == Tit(3, 3 ** (a + 1) - 1) == (3 ** (a + 1) - 1) // 8
        n_checks += 1
    log("   %d instances checked, no failure" % n_checks)


# ----------------------------------------------------------------------------- Part 3
def part3(BMAX=1000):
    log("== Part 3: S-orbits (3x-1 map) of the layer constants, b <= %d" % BMAX)
    res = {}
    for name, seed, b0 in (("3^b+1", lambda b: 3 ** b + 1, 0),
                           ("3^b-1", lambda b: 3 ** b - 1, 1),
                           ("2*3^b-1", lambda b: 2 * 3 ** b - 1, 0)):
        cnt = [0, 0, 0]
        fails = []
        ratios = []
        table = []
        for b in range(b0, BMAX + 1):
            c = seed(b)
            t = 0
            o = 0
            cap = 40 * b + 5000
            while (c > 136 or c not in CYCSET) and t < cap:
                if c & 1:
                    o += 1
                    c = (3 * c - 1) >> 1
                else:
                    c >>= 1
                t += 1
            if c <= 136 and c in CYCSET:
                cnt[CYCSET[c]] += 1
                table.append((b, t, o, c))
                if b >= 50:
                    ratios.append(t / b)
            else:
                fails.append(b)
        res[name] = table
        log("   seed %-9s: enters cycle{1}: %d, cycle{5,7,10}: %d, cycle{17,..}: %d, "
            "no known cycle within cap: %d" % (name, cnt[0], cnt[1], cnt[2], len(fails)))
        if ratios:
            log("      sigma/b for b>=50: min %.2f mean %.2f max %.2f" %
                (min(ratios), sum(ratios) / len(ratios), max(ratios)))
        log("      first rows (b, sigma, odd steps, entry point): " +
            " ".join("(%d,%d,%d,%d)" % r for r in table[:16]))
    log("   [%.1fs]" % (time.time() - T0))
    return res


# ----------------------------------------------------------------------------- Part 4
CONST3 = sorted(set(range(1, 41)) | {41, 55, 61, 68, 82, 91, 136})
CONST3SET = set(CONST3)


def build_one_param(K3MAX, K2MAX):
    fam = []
    for K in range(1, K3MAX + 1):
        p = 3 ** K
        for c in CONST3:
            if p - c >= MIN:
                fam.append(("3^K-%d" % c, K, p - c))
        for c in range(0, 11):
            if p + c >= MIN:
                fam.append(("3^K+%d" % c, K, p + c))
    for K in range(1, K2MAX + 1):
        p = 2 ** K
        for c in (-9, -7, -5, -3, -1, 1, 3, 5, 7, 9):
            if p + c >= MIN:
                fam.append(("2^K%+d" % c, K, p + c))
    return fam


def part4(BB=60, JJ=80, K3MAX=230, K2MAX=420):
    log("== Part 4: hypothesis H at rank 1 (box b,k <= %d, j,n <= %d; class label = first point < 2^40)"
        % (BB, JJ))
    one = build_one_param(K3MAX, K2MAX)
    cls = defaultdict(lambda: ([], []))   # fp -> (one-param members, two-param members)
    for lab, K, v in one:
        cls[fp(v)][0].append((lab, K, v))
    log("   one-parameter members classified: %d (%d labels)  [%.1fs]" %
        (len(one), len(set(l for l, _, _ in one)), time.time() - T0))

    two = []   # (family, p, q, value, prefix_len, landing_c, landing_K)
    for b in range(0, BB + 1):
        for j in range(2, JJ + 1):
            v = 3 ** b * 4 ** j - 3 ** b - 1
            c, o = Sit(2 * j, 3 ** b + 1)
            two.append(("F1", b, j, v, 2 * j, c, b + o))
    for k in range(1, BB + 1):
        for n in range(4, JJ + 1, 3):
            v = 3 ** k * 4 ** n - (3 ** k - 1)
            c, o = Sit(2 * n, 3 ** k - 1)
            two.append(("R1a", k, n, v, 2 * n, c, k + o))
    for k in range(0, BB + 1):
        for n in range(2, JJ + 1, 3):
            v = 3 ** k * 2 * 4 ** n - (2 * 3 ** k - 1)
            c, o = Sit(2 * n + 1, 2 * 3 ** k - 1)
            two.append(("R1b", k, n, v, 2 * n + 1, c, k + o))
    two = [m for m in two if m[3] >= MIN]
    for m in two:
        assert Tit(m[4], m[3]) == 3 ** m[6] - m[5]
        cls[fp(m[3])][1].append(m)
    log("   two-parameter members classified: %d  [%.1fs]" % (len(two), time.time() - T0))

    for famname in ("F1", "R1a", "R1b"):
        mem = [m for m in two if m[0] == famname]
        cyc = [m for m in mem if m[5] in CYCSET]
        small = [m for m in mem if m[5] in CONST3SET and m[5] not in CYCSET]
        gen = [m for m in mem if m[5] not in CONST3SET]
        log("   -- family %s: %d members; landing constant on an S-cycle: %d; small pre-cyclic (<=40): %d; "
            "generic (not listed): %d" % (famname, len(mem), len(cyc), len(small), len(gen)))
        # predicted merges (landing constant listed)
        good = bad = skipped = 0
        badlist = []
        for m in cyc + small:
            lab = "3^K-%d" % m[5]
            land = 3 ** m[6] - m[5]
            if m[6] > K3MAX or land < MIN:
                skipped += 1
                continue
            ones = cls[fp(m[3])][0]
            if any(l == lab and K == m[6] for l, K, _ in ones):
                good += 1
            else:
                bad += 1
                badlist.append(m[:3])
        log("      predicted landing 3^K-c found in the same class: %d, missing: %d %s, out of range: %d"
            % (good, bad, badlist[:5], skipped))
        # generic members: cost (bits of descent after the landing) of joining any one-parameter member
        bins = [(0, 8), (8, 16), (16, 24), (24, 32), (32, 48), (48, 64), (64, 10 ** 6)]
        stat = {bn: [] for bn in bins}
        nomerge = {bn: 0 for bn in bins}
        examples = []
        lem_n = lem_viol = lem_sync = lem_3fam = 0
        lem_tight = 0.0
        for m in gen:
            beta = m[5].bit_length()
            bn = next(x for x in bins if x[0] < beta <= x[1])
            ones = cls[fp(m[3])][0]
            best = None
            land = 3 ** m[6] - m[5]
            if ones:
                d = orbit_info(land)
                for lab, K, v in ones:
                    h = first_hit_info(v, d)
                    if h and (best is None or h[3][0] < best[3][3][0]):
                        best = (lab, K, v, h)
            if best is None:
                nomerge[bn] += 1
            else:
                lab, Kp, v, (sp, op, mup, (sl, ol, mul), pt) = best
                D = land.bit_length() - pt.bit_length()
                stat[bn].append((D, D - beta, sl))
                if len(examples) < 8 and beta > 16:
                    examples.append((m[1], m[2], m[6], beta, (lab, Kp, sp, sl, pt.bit_length()), D))
                # coalescence inequality: |ln(n/n') - (o'-o) ln 3 - (s-s') ln 2| <= max(o/(3 mu), o'/(3 mu'))
                R = Fraction(land * 3 ** ol * 2 ** sp, v * 3 ** op * 2 ** sl)
                x = R - 1
                lam = abs(math.log1p(float(x))) if abs(x) < Fraction(1, 2) else abs(math.log(float(R)))
                bound = max(ol / (3 * mul) if mul else 0.0, op / (3 * mup) if mup else 0.0)
                lem_n += 1
                if bound == 0.0 or lam > bound * (1 + 1e-9):
                    lem_viol += 1
                else:
                    lem_tight = max(lem_tight, lam / bound)
                if lab.startswith("3^K"):
                    lem_3fam += 1
                    if sl == sp and op - ol == m[6] - Kp:
                        lem_sync += 1
        log("      coalescence inequality on the %d merges: violations %d, max |Lambda|/bound = %.3f; "
            "merges with a 3^K'+-c' member: %d, of which same step count and odd-count gap K-K': %d"
            % (lem_n, lem_viol, lem_tight, lem_3fam, lem_sync))
        log("      generic members: cost of joining a one-parameter member (merge point >= 2^40),")
        log("      by beta = bits(landing constant c); D = bits(landing 3^K-c) - bits(merge point):")
        for bn in bins:
            st = stat[bn]
            hi = str(bn[1]) if bn[1] < 10 ** 6 else "inf"
            if st:
                Ds = sorted(x[0] for x in st)
                log("         beta in (%d,%s]: members %d, merged %d, D min/median/max = %d/%d/%d, "
                    "min(D-beta) = %d, merged with D < beta-8: %d"
                    % (bn[0], hi, len(st) + nomerge[bn], len(st), Ds[0], Ds[len(Ds) // 2], Ds[-1],
                       min(x[1] for x in st), sum(1 for x in st if x[1] < -8)))
            elif nomerge[bn]:
                log("         beta in (%d,%s]: members %d, merged 0" % (bn[0], hi, nomerge[bn]))
        for ex in examples:
            log("         e.g. (p,q)=(%d,%d) K=%d beta=%d merge(label,K',steps',steps after landing,bits)=%s D=%d" % ex)
        # internal structure of the generic part
        byfp = defaultdict(list)
        for m in gen:
            byfp[fp(m[3])].append(m)
        ndiff = 0
        for f, ms in byfp.items():
            if len(set((mm[6], mm[5]) for mm in ms)) > 1:
                ndiff += 1
        nland = len(set((m[6], m[5]) for m in gen))
        log("      generic members: %d, distinct landings (K,c): %d, distinct classes: %d, "
            "classes holding more than one landing: %d" % (len(gen), nland, len(byfp), ndiff))
        if famname == "F1":
            pairs = 0
            tot = 0
            genset = set((m[1], m[2]) for m in gen)
            fpmap = {(m[1], m[2]): fp(m[3]) for m in gen}
            for (b, j) in genset:
                if b % 2 == 0 and (b + 1, j) in genset:
                    tot += 1
                    if fpmap[(b, j)] == fpmap[(b + 1, j)]:
                        pairs += 1
            log("      parity fold F1(2n,j) ~ F1(2n+1,j): %d of %d generic pairs share a class" % (pairs, tot))
        # smooth detector on the unstructured tail of generic members
        M3 = 3 ** 25
        M2 = (1 << 40) - 1
        B = 200
        hits = []
        npts = 0
        for m in gen:
            if m[5].bit_length() < 24:
                continue
            n = Tit(m[4], m[3])
            s = m[4]
            while n >= MIN:
                npts += 1
                r3 = n % M3
                for dsh in (0, 1, 2):
                    rd = (r3 << dsh) % M3
                    if rd <= B or rd >= M3 - B:
                        hits.append((m[:3], s, "3-adic", dsh, rd if rd <= B else rd - M3))
                r2 = n & M2
                if r2 <= B or r2 >= M2 + 1 - B:
                    hits.append((m[:3], s, "2-adic", 0, r2 if r2 <= B else r2 - M2 - 1))
                n = n >> 1 if not n & 1 else (3 * n + 1) >> 1
                s += 1
        log("      tail detector on members with beta >= 24 (orbit points == small const mod 3^25 or mod 2^40, "
            "|const| <= %d): %d orbit points scanned, %d hits %s" % (B, npts, len(hits), hits[:6]))
    log("   [%.1fs]" % (time.time() - T0))
    return cls, two


# ----------------------------------------------------------------------------- Part 5
def part5(cls, two, B2=30, E2=30, J2=20):
    log("== Part 5: rank 2, F2(b,e,j) = 3^b 2^e y_j - (3^b+1), 2^e y_j = 1 mod 3 "
        "(box b<=%d, e<=%d, j<=%d)" % (B2, E2, J2))
    f1cls = defaultdict(list)
    for m in two:
        if m[0] == "F1":
            f1cls[fp(m[3])].append(m)
    mem = []
    for b in range(0, B2 + 1):
        for e in range(1, E2 + 1):
            for j in range(2, J2 + 1):
                yy = y(j)
                if (2 ** e * yy) % 3 != 1:
                    continue
                v = 3 ** b * 2 ** e * yy - (3 ** b + 1)
                if v < MIN:
                    continue
                ce, oe = Sit(e, 3 ** b + 1)
                k = b + oe
                if k < 1:
                    continue
                c2, o2 = Sit(2 * j, ce + 3 ** (k - 1))
                mem.append((b, e, j, v, ce, k, c2, k - 1 + o2))
    full = [m for m in mem if m[6] in CONST3SET]
    cone = [m for m in mem if m[6] not in CONST3SET and m[4] in CYCSET]
    gen = [m for m in mem if m[6] not in CONST3SET and m[4] not in CYCSET]
    log("   members: %d; landing constant listed (one-parameter): %d; first S-stage on a cycle but landing "
        "generic (two-parameter family 3^k y_j - c): %d; generic: %d" % (len(mem), len(full), len(cone), len(gen)))
    # cone members with ce == 1 must coincide with an F1 member along the orbit
    ok = miss = out = 0
    for m in cone:
        if m[4] != 1:
            continue
        b, e, j, v, ce, k = m[:6]
        target = 3 ** k * y(j) - 1
        assert Tit(e, v) == target
        if target < MIN or k - 1 > 60 or j > 80:
            out += 1
            continue
        if any(mm[1] == k - 1 and mm[2] == j for mm in f1cls.get(fp(v), [])):
            ok += 1
        else:
            miss += 1
    log("   cone members with first-stage constant 1: joined to F1(k-1,j) in class table: %d, missing: %d, "
        "out of the F1 box: %d" % (ok, miss, out))
    un1 = un2 = 0
    ex = []
    byfp = defaultdict(list)
    for m in gen:
        f = fp(m[3])
        byfp[f].append(m)
        if cls[f][0]:
            un1 += 1
            ex.append(("one-param", m[:3], cls[f][0][:2]))
        if f1cls.get(f):
            un2 += 1
            ex.append(("F1", m[:3], [mm[:3] for mm in f1cls[f]][:2]))
    sizes = defaultdict(int)
    difl = 0
    for f, ms in byfp.items():
        sizes[len(ms)] += 1
        if len(set((mm[7], mm[6]) for mm in ms)) > 1:
            difl += 1
    log("   generic members sharing a class with a one-parameter member: %d; with an F1 member: %d %s"
        % (un1, un2, ex[:6]))
    log("   generic members: %d, distinct classes: %d, class-size histogram: %s, "
        "classes with two different landings: %d" % (len(gen), len(byfp), dict(sorted(sizes.items())), difl))
    log("   [%.1fs]" % (time.time() - T0))


if __name__ == "__main__":
    odd1, odd2 = part1()
    part2(odd1, odd2)
    part3()
    cls, two = part4()
    part5(cls, two)
    log("done [%.1fs]" % (time.time() - T0))
