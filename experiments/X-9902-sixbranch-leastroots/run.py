#!/usr/bin/env python3
# X-9902 -- six-branch chart least roots: exact m_N (N <= 10) and beam upper bounds
# u_N (N <= 60) for the deterministic chart x_{n+1} = ceil(P x_n / Q), digit
# a_n = Q x_{n+1} - P x_n, digit alphabet A = {7 * 3^(2i) * 2^(15-3i) : i = 0..5}.
# Agent: fable-02-p7. Python 3 stdlib only; every arithmetic decision is exact.
# Associated: issue #58; forward-ref claim L-9916; experiment ID X-9902.
#
# Exactness notes (proofs in README.md):
#  - each digit word w in A^N corresponds to a unique residue class r_w mod Q^N
#    (P is odd, hence a unit mod Q^N); S_N is the disjoint union of these 6^N classes;
#  - least representatives are monotone along lifts: r_{w a} = r_w + Q^{|w|} t,
#    t in [0, Q), so r_{w a} >= r_w  ("roots only grow");
#  - theta-certificate: if every level-9 node with r <= theta is extended to level 10
#    and the resulting minimum Mhat satisfies Mhat <= theta, then m_10 = Mhat exactly.
import time, math, os, random

P = 3 ** 12                    # 531441
Q = 2 ** 19                    # 524288
MASK = Q - 1
SH = 19
A = [7 * 3 ** (2 * i) * 2 ** (15 - 3 * i) for i in range(6)]
Aset = set(A)
POSTED = {1: 6472, 2: 1908874353, 3: 44906374791168, 4: 275202518480529950784,
          8: 181625992579115023082252809688279976000}
OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
os.makedirs(OUTDIR, exist_ok=True)
LOG = []
def say(*parts):
    line = " ".join(str(p) for p in parts)
    print(line, flush=True)
    LOG.append(line)

def log10_big(v):
    s = str(v)
    lead = s[:15]
    return (len(s) - len(lead)) + math.log10(int(lead))

# ---------------------------------------------------------------- chart replay
def replay_digits(x, N):
    """The first N digits of the deterministic chart started at x (exact)."""
    ds = []
    for _ in range(N):
        y = P * x
        xn = -(-y // Q)                       # ceil(P x / Q)
        ds.append(Q * xn - y)
        x = xn
    return ds

def certify(x, N):
    """x in S_N?  (mandatory certification for every reported element)"""
    return all(d in Aset for d in replay_digits(x, N))

# ------------------------------------------------------- incremental lift BFS
def level1():
    invP = pow(P, -1, Q)
    out = []
    for al in A:
        r = ((Q - al) * invP) % Q             # r = -al * P^{-1} mod Q, al < Q
        assert r != 0
        assert (P * r + al) % Q == 0
        out.append((r, (P * r + al) >> SH))   # (least rep, exact iterate x_1)
    return out

def extend_level(nodes, n, check=False):
    """All 6-digit extensions of level-n nodes (r < Q^n, s = x_n from x_0 = r)."""
    Qn = Q ** n
    Pn = P ** n
    inv = pow(P, -(n + 1), Q)
    out = []
    for r, s in nodes:
        base = P * s
        for al in A:
            b = (base + al) & MASK
            t = ((Q - b) * inv) & MASK        # t = -(P s + al) P^{-(n+1)} mod Q
            x = s + t * Pn                    # x_n after lifting x_0 by Q^n t
            y = P * x + al
            if check:
                assert y & MASK == 0, (r, al)
            out.append((r + t * Qn, y >> SH))
    return out

def validate_sample(nodes, n, k, seed=12345):
    """Replay-check k random nodes of a level: digits in A^n and iterate match."""
    rnd = random.Random(seed)
    for r, s in rnd.sample(nodes, min(k, len(nodes))):
        assert certify(r, n), (n, r)
        x = r
        for _ in range(n):
            x = -(-P * x // Q)
        assert x == s, (n, r)

t_start = time.time()
say("X-9902 run.py -- P = 3^12 =", P, ", Q = 2^19 =", Q)
say("digits A =", A)
say("null-model slope log10(Q/6) = %.6f ; log10(Q) = %.6f" %
    (math.log10(Q / 6), math.log10(Q)))
say("")

# ---- validation gate 0: independent direct-formula enumeration for N <= 3 ---
say("== validation gates ==")
from itertools import product
def direct_level_residues(N):
    QN = Q ** N
    invPN = pow(P, -N, QN)
    out = []
    for w in product(A, repeat=N):
        Ssum = sum(pow(P, N - 1 - i) * Q ** i * al for i, al in enumerate(w))
        r = (-Ssum * invPN) % QN
        out.append(QN if r == 0 else r)
    return out

first = next(x for x in range(1, 10 ** 5) if replay_digits(x, 1)[0] in Aset)
assert first == POSTED[1]
say("gate: brute scan x=1.. gives least x with a_0 in A ->", first, "== posted m_1: PASS")

# ---- build levels 1..8 by incremental lift, recording m_N -------------------
t0 = time.time()
lev = level1()
mN = {1: min(r for r, _ in lev)}
saved_r = {1: sorted(r for r, _ in lev)}
for n in range(1, 8):
    lev = extend_level(lev, n, check=(n <= 3))
    mN[n + 1] = min(r for r, _ in lev)
    if n + 1 <= 4:
        saved_r[n + 1] = sorted(r for r, _ in lev)
say("built levels 1..8 by incremental lift: %d nodes at level 8, %.1f s"
    % (len(lev), time.time() - t0))

for N in (1, 2, 3):
    assert saved_r[N] == sorted(direct_level_residues(N)), N
say("gate: lift recurrence == direct per-word formula (FULL residue multiset), N=1..3: PASS")
assert mN[4] == min(direct_level_residues(4))
say("gate: min agreement with direct formula at N=4: PASS")
for N, v in POSTED.items():
    if N <= 8:
        assert mN[N] == v, (N, mN[N], v)
say("gate: posted m_1, m_2, m_3, m_4, m_8 all reproduced: PASS")
for N in range(1, 9):
    assert certify(mN[N], N), N
say("gate: every m_N (N<=8) certified by exact digit replay: PASS")
validate_sample(lev, 8, 200)
say("gate: 200 random level-8 nodes replay-certified (digits + iterate): PASS")
say("")

# ---- task 1a: m_9 exact by streaming the 6-way extension of level 8 ---------
# ---- task 1b: m_10 exact by theta-thresholded survivors (proof in README) ---
t0 = time.time()
theta = Q ** 9 // 20                          # survivor threshold (a-priori choice)
Q8 = Q ** 8
P8 = P ** 8
inv9 = pow(P, -9, Q)
attempt = 0
while True:
    attempt += 1
    m9 = None
    survivors = []
    for r, s in lev:
        base = P * s
        for al in A:
            b = (base + al) & MASK
            t = ((Q - b) * inv9) & MASK
            r9 = r + t * Q8
            if m9 is None or r9 < m9:
                x = s + t * P8
                y = P * x + al
                assert y & MASK == 0
                m9 = r9
            if r9 <= theta:
                x = s + t * P8
                y = P * x + al
                assert y & MASK == 0
                survivors.append((r9, y >> SH))
    say("stream 8->9: full 6^9 = %d extensions, %.1f s; survivors (r <= theta=Q^9/%d): %d"
        % (6 * len(lev), time.time() - t0, Q ** 9 // theta, len(survivors)))
    mN[9] = m9

    # level 10 from survivors
    Q9 = Q ** 9
    P9 = P ** 9
    inv10 = pow(P, -10, Q)
    m10 = None
    for r, s in survivors:
        base = P * s
        for al in A:
            b = (base + al) & MASK
            t = ((Q - b) * inv10) & MASK
            r10 = r + t * Q9
            if m10 is None or r10 < m10:
                m10 = r10
    if m10 is not None and m10 <= theta:
        mN[10] = m10
        say("theta-certificate: Mhat = m_10 <= theta holds -> m_10 is EXACT")
        break
    theta *= 8                                # graceful exact retry (never expected)
    say("theta-certificate FAILED; retrying with theta *= 8 (attempt %d)" % (attempt + 1))
    assert attempt < 4, "aborting m_10 attempt"

assert mN[9] >= mN[8] and mN[10] >= mN[9]     # monotone sanity
assert certify(mN[9], 9) and certify(mN[10], 10)
say("m_9  =", mN[9])
say("m_10 =", mN[10])
say("m_9, m_10 certified by exact digit replay: PASS   (t = %.1f s)" % (time.time() - t0))
say("")

# ---- task 2: beam probe for small (certified, non-minimal) u_N, N up to 60 --
say("== beam probe (upper bounds u_N; deterministic; NOT minima) ==")
SAMPLES = [10, 15, 20, 30, 40, 60]
BEAMS = [1, 64, 1024]
t0 = time.time()
uN = {}
for K in BEAMS:
    levb = sorted(level1())[:K]
    got = {}
    for n in range(1, 60):
        nxt = extend_level(levb, n)
        nxt.sort(key=lambda p: p[0])
        levb = nxt[:K]
        if n + 1 in SAMPLES:
            got[n + 1] = levb[0][0]
    for N, u in got.items():
        assert certify(u, N), (K, N)          # mandatory certification
    uN[K] = got
    say("beam K=%4d: certified u_N at N=%s  (%.1f s)" % (K, SAMPLES, time.time() - t0))
say("")

# ---- stall criterion --------------------------------------------------------
stall = False
for K in BEAMS:
    seq = [uN[K][N] for N in SAMPLES]
    for i in range(len(seq) - 2):
        if seq[i] >= seq[i + 1] >= seq[i + 2]:
            stall = True
            say("STALL SIGNAL at K=%d, N=%s: dumping word prefix and residue" %
                (K, SAMPLES[i:i + 3]))
            say("  residue:", seq[i + 2], " word:", replay_digits(seq[i + 2], SAMPLES[i + 2]))
if not stall:
    say("stall criterion (u_N non-increasing over 3 consecutive sampled N): NOT triggered")
say("")

# ---- fits and table ---------------------------------------------------------
def fit_slope(pairs):
    n = len(pairs)
    sx = sum(p[0] for p in pairs); sy = sum(p[1] for p in pairs)
    sxx = sum(p[0] * p[0] for p in pairs); sxy = sum(p[0] * p[1] for p in pairs)
    return (n * sxy - sx * sy) / (n * sxx - sx * sx)

rows = []
rows.append("X-9902 results table  (P = 3^12, Q = 2^19, |A| = 6)")
rows.append("")
rows.append("exact least roots m_N  (N = 1..10; N<=4 and N=8 are the posted validation gates)")
rows.append(f"{'N':>3} | {'log10 m_N':>10} | m_N")
for N in range(1, 11):
    rows.append(f"{N:>3} | {log10_big(mN[N]):>10.4f} | {mN[N]}")
slope_m = fit_slope([(N, log10_big(mN[N])) for N in range(1, 11)])
rows.append("")
rows.append("fit slope of log10 m_N vs N (N=1..10):  %.4f" % slope_m)
rows.append("null-model slope log10(Q/6):            %.4f" % math.log10(Q / 6))
rows.append("")
rows.append("beam upper bounds u_N (certified elements of S_N; NOT minima)")
rows.append(f"{'N':>3} | " + " | ".join(f"log10 u_N (K={K})" for K in BEAMS))
for N in SAMPLES:
    rows.append(f"{N:>3} | " + " | ".join(f"{log10_big(uN[K][N]):>16.4f}" for K in BEAMS))
for K in BEAMS:
    s = fit_slope([(N, log10_big(uN[K][N])) for N in SAMPLES])
    rows.append("fit slope log10 u_N vs N, K=%4d:  %.4f   (log10 Q = %.4f)"
                % (K, s, math.log10(Q)))
rows.append("")
rows.append("calibration at N=10: u_10/m_10 = %.3g (K=1), %.3g (K=64), %.3g (K=1024)"
            % tuple(uN[K][10] / mN[10] for K in BEAMS))
rows.append("stall signal: %s" % ("TRIGGERED (see log)" if stall else "none"))
for line in rows:
    say(line)

with open(os.path.join(OUTDIR, "table.txt"), "w") as f:
    f.write("\n".join(rows) + "\n")
with open(os.path.join(OUTDIR, "uN_values.txt"), "w") as f:
    f.write("# X-9902 certified beam elements u_N of S_N (full integers)\n")
    for K in BEAMS:
        for N in SAMPLES:
            f.write(f"K={K} N={N} u={uN[K][N]}\n")
with open(os.path.join(OUTDIR, "mN_values.txt"), "w") as f:
    f.write("# X-9902 exact least roots m_N = min S_N (full integers)\n")
    for N in range(1, 11):
        f.write(f"N={N} m={mN[N]}\n")
with open(os.path.join(OUTDIR, "run_log.txt"), "w") as f:
    f.write("\n".join(LOG) + "\n")
say("")
say("total runtime: %.1f s" % (time.time() - t_start))
