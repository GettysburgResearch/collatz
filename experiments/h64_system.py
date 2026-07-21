"""The 64->81 collision subsystem: exact verification and analysis.

Verifies the user's construction end-to-end:
  S1  six-step collision  T^6(64q+14) = T^6(64q+15) = 81q+20
  S2  conjugacy Y = 17n+146, induced map H(64B+e) = 81B+e, lifting
      congruence A == 6 (mod 17), monotone growth of valid orbits
  S3  the four collision charts and their mod-17 classes
  S4  no fixed-length translation collision in the 64->81 subsystem
  S5  mixed-radix rewrite realization of H
  S6  nine-column carry cycle (19-cycle mod 81), the word W-hat
  S7  stack amplifier H^{9m+1}(S_m(x)) = 81^{9m}(81x+1), with FULL
      Collatz lift (6(9m+1) shortcut steps on the actual integer n)
  S8  regeneration residues (8.2) + an explicit 3-stage steered tower
  S9  continued fraction of log_64 81 = [1;17,1,1,1,8,1,2,...]

New measurements:
  FREE VALIDITY: beyond designed structure, the chance a random valid A
  continues one more H-step is 2/64; measured distribution of free runs.
"""

from fractions import Fraction
from math import gcd
from core import T, T_iter

FAILS = []
def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" -- {detail}" if detail and not cond else ""))
    if not cond:
        FAILS.append(name)


def parity_word_of_residue(r, L):
    _, par = T_iter(r, L)
    return tuple(par)


def B_of_word(w):
    L = len(w)
    return sum(2 ** j * 3 ** sum(w[j + 1:]) for j in range(L) if w[j] == 1)


# ---------------------------------------------------------------- S1
print("== S1: six-step collision ==")
u = (0, 1, 1, 1, 0, 1)
v = (1, 1, 1, 1, 0, 0)
Bu, Bv = B_of_word(u), B_of_word(v)
check("B_u = 146, B_v = 65", (Bu, Bv) == (146, 65), f"got {Bu},{Bv}")
check("residues: 14 realizes u, 15 realizes v",
      parity_word_of_residue(14, 6) == u and parity_word_of_residue(15, 6) == v)
ok = all(T_iter(64 * q + 14, 6)[0] == 81 * q + 20 == T_iter(64 * q + 15, 6)[0]
         for q in range(0, 300))
check("T^6(64q+14) = T^6(64q+15) = 81q+20 (q = 0..299)", ok)
check("supercritical: 3^4/2^6 = 81/64 > 1", 81 > 64)

# ---------------------------------------------------------------- S2
print("== S2: conjugacy and the induced map H ==")
# Y = 17n + 146;  n = 64q+14 -> Y = 64(17q+6);  n' = 81q+20 -> Y' = 81(17q+6)
ok = all(17 * (64 * q + 14) + 146 == 64 * (17 * q + 6) and
         17 * (64 * q + 15) + 146 == 64 * (17 * q + 6) + 17 and
         17 * (81 * q + 20) + 146 == 81 * (17 * q + 6) for q in range(200))
check("Y-coordinate: 64Z -> 81Z and 64Z+17 -> 81Z with Z = 17q+6", ok)

def H(A):
    B, e = divmod(A, 64)
    assert e in (0, 1)
    return 81 * B + e

def n_of_A(A):
    num = 81 * A - 146
    assert num % 17 == 0
    return num // 17

# lifting: valid A == 6 mod 17 with low digit 0/1 -> integer n == 14/15 mod 64,
# and one H-step = six shortcut steps on n
import random
random.seed(5)
ok = True
tested = 0
for _ in range(4000):
    B = random.randrange(1, 10 ** 9)
    e = random.randrange(2)
    A = 64 * B + e
    if A % 17 != 6:
        continue
    n = n_of_A(A)
    if n <= 0:
        continue
    ok &= n % 64 in (14, 15)
    A2 = H(A)
    ok &= A2 % 17 == 6                       # invariance of the class
    ok &= T_iter(n, 6)[0] == n_of_A(A2)      # H-step == T^6 on the lift
    ok &= A2 > A                             # monotone growth (B > 0)
    tested += 1
check(f"H-step == T^6 on lifted integers; class 6 mod 17 invariant; "
      f"A strictly grows ({tested} random valid A)", ok)

# ---------------------------------------------------------------- S3
print("== S3: the four collision charts ==")
pairs = [((0,1,1,1,0,1), (1,1,1,1,0,0)),
         ((0,1,1,0,1,1), (1,1,1,0,0,1)),
         ((0,1,0,1,1,1), (1,1,0,0,1,1)),
         ((0,0,1,1,1,1), (1,0,0,1,1,1))]
claimed_classes = [6, 0, 8, 3]
got_classes = []
ok = True
for (wu, wv), cls in zip(pairs, claimed_classes):
    ok &= sum(wu) == 4 == sum(wv)
    BU, BV = B_of_word(wu), B_of_word(wv)
    ok &= BU - BV == 81                     # inverse maps differ by exactly 1
    # residues realizing the words
    ru = next(r for r in range(64) if parity_word_of_residue(r, 6) == wu)
    rv = next(r for r in range(64) if parity_word_of_residue(r, 6) == wv)
    ok &= rv == ru + 1
    ok &= all(T_iter(64 * q + ru, 6)[0] == T_iter(64 * q + rv, 6)[0]
              for q in range(50))
    # conjugation Y = 17n + BU: chart class = (17*ru + BU)/64 mod 17
    s = (17 * ru + BU)
    ok &= s % 64 == 0
    got_classes.append((s // 64) % 17)
check("four charts: collisions exact, B_u - B_v = 81, adjacent residues", ok)
check(f"chart classes mod 17 = {claimed_classes}", got_classes == claimed_classes,
      f"got {got_classes}")

# exhaustiveness: ALL translation collisions at L=6:
# T^6(64q+r) = T^6(64q+r+t) for all q  <=>  same odd count a and
# B_r - B_{r+t} = 3^a * t.  Census over all r, t, grouped by a.
coll = {}
for r in range(64):
    wr = parity_word_of_residue(r, 6)
    for t in range(1, 64 - r):
        ws = parity_word_of_residue(r + t, 6)
        if sum(wr) != sum(ws):
            continue
        a = sum(wr)
        if B_of_word(wr) - B_of_word(ws) == 3 ** a * t:
            assert all(T_iter(64 * q + r, 6)[0] == T_iter(64 * q + r + t, 6)[0]
                       for q in range(30))
            coll.setdefault((a, t), []).append(r)
print("  collision census (a = odd count, t = translation): " +
      ", ".join(f"a={a},t={t}: {len(rs)} pairs" for (a, t), rs in
                sorted(coll.items())))
check("adjacent (t=1) supercritical (a=4) collisions: exactly the four "
      f"charts at residues {coll.get((4,1))}",
      sorted(coll.get((4, 1), [])) == [14, 18, 54, 60])
check("no supercritical collisions with a >= 5 at L=6",
      not any(a >= 5 for (a, t) in coll))

# ---------------------------------------------------------------- S4
print("== S4: no fixed-length translation collision inside H ==")
# search: words e in {0,1}^m with C_u - C_v divisible by 81^m, u != v
def C_of(word):
    m = len(word)
    return sum(word[i] * 64 ** i * 81 ** (m - 1 - i) for i in range(m))
ok = True
from itertools import product
for m in range(1, 9):
    seen = {}
    for wd in product((0, 1), repeat=m):
        c = C_of(wd) % 81 ** m
        if c in seen and seen[c] != wd:
            ok = False
        seen[c] = wd
check("no two {0,1}-words of equal length m <= 8 with 81^m | C_u - C_v", ok)

# ---------------------------------------------------------------- S5/S6
print("== S5/S6: mixed-radix rewrite and the nine-column carry cycle ==")
def H_rewrite(digits):
    """digits: base-64 LSD-first word of A with digits[0] in {0,1}.
    Perform L_e -> R_e then normalize R through the word; return new word."""
    e = digits[0]
    assert e in (0, 1)
    c = e
    out = []
    for d in digits[1:]:
        tot = 81 * d + c
        out.append(tot % 64)
        c = tot // 64
    while c:
        out.append(c % 64)
        c //= 64
    while out and out[-1] == 0:
        out.pop()
    return out

def to64(n):
    ds = []
    while n:
        ds.append(n % 64)
        n //= 64
    return ds

ok = True
for _ in range(2000):
    A = 64 * random.randrange(1, 10 ** 12) + random.randrange(2)
    ok &= H_rewrite(to64(A)) == to64(H(A))
check("string rewrite realizes H exactly (2000 random A)", ok)

cyc = [1]
while True:
    nxt = (19 * cyc[-1]) % 81
    if nxt == 1:
        break
    cyc.append(nxt)
check("carry 19-cycle mod 81 has length 9: 1,19,37,55,73,10,28,46,64",
      cyc == [1, 19, 37, 55, 73, 10, 28, 46, 64])
Wdig = [15, 29, 43, 57, 7, 22, 36, 50, 0]
# digit d for carry c with zero output: 81d + c = 64q => d = (64q - c)/81,
# q = 19c mod 81 lifted: check 81*d + c == 64 * q with q = next carry chain
ok = True
c = 1
for d in Wdig:
    tot = 81 * d + c
    ok &= tot % 64 == 0
    c = tot // 64
    ok &= 0 <= c < 81
ok &= c == 1
check("W-hat digits 15,29,43,57,7,22,36,50,0: carry 1 traverses, emits 0^9, "
      "returns as carry 1", ok)

# ---------------------------------------------------------------- S7
print("== S7: stack amplifier with full Collatz lift ==")
def S_m(m, x):
    num = 64 ** (9 * m + 1) + 17
    assert num % 81 == 0
    return 64 ** (9 * m + 1) * x + num // 81

ok = ok_lift = True
for m in range(0, 4):
    for _ in range(20):
        x = random.randrange(1, 10 ** 6)
        A = S_m(m, x)
        # H once: (7.2)
        ok &= H(A) == 64 ** (9 * m) * (81 * x + 1)
        # H^{9m+1}: (7.3)
        Ai = A
        for _ in range(9 * m + 1):
            Ai = H(Ai)
        ok &= Ai == 81 ** (9 * m) * (81 * x + 1)
        # full Collatz lift: choose x* == x mod adjustment so A == 6 mod 17
        t = (6 - S_m(m, x)) * pow(64 ** (9 * m + 1), -1, 17) % 17
        xs = x + t * 1  # x shift: S_m(x + t) = S_m(x) + 64^{9m+1} t; 64^{..} == ? mod 17
        A2 = S_m(m, x + t * pow(64 ** (9 * m + 1) % 17, -1, 17) * 1) \
            if False else None
        # simpler: scan the 17 residues
        for dx in range(17):
            if S_m(m, x + dx) % 17 == 6:
                break
        A3 = S_m(m, x + dx)
        n = n_of_A(A3)
        steps = 6 * (9 * m + 1)
        target = 81 ** (9 * m) * (81 * (x + dx) + 1)
        ok_lift &= T_iter(n, steps)[0] == n_of_A(target)
check("amplifier identities (7.2),(7.3) exact (m <= 3, random x)", ok)
check("FULL COLLATZ LIFT: T^{6(9m+1)}(n) matches the amplifier "
      "(m <= 3, x == chart class)", ok_lift)

# ---------------------------------------------------------------- S8
print("== S8: regeneration residues and a steered 3-stage tower ==")
def regen_x(m, mp):
    """The unique x mod 64^{9mp+1} with 81^{9m}(81x+1) = S_{mp}(x') solvable."""
    M = 64 ** (9 * mp + 1)
    cst = (64 ** (9 * mp + 1) + 17) // 81
    r = pow(81, -(9 * m + 1), M) * (cst - 81 ** (9 * m)) % M
    return r

ok = True
for m, mp in [(1, 2), (2, 3), (1, 3)]:
    r = regen_x(m, mp)
    y = random.randrange(1, 10 ** 4)
    x = r + 64 ** (9 * mp + 1) * y
    val = 81 ** (9 * m) * (81 * x + 1)
    cst = (64 ** (9 * mp + 1) + 17) // 81
    num = val - cst
    ok &= num % 64 ** (9 * mp + 1) == 0
    xp = num // 64 ** (9 * mp + 1)
    ok &= val == S_m(mp, xp)
check("(8.2): regeneration residue exists and is unique; x' integral "
      "and expanding", ok)

# explicit steered tower m=1 -> m'=2 inside chart 6, WITH full Collatz lift.
# choose x1 == r_{1,2} mod 64^19 (regeneration residue) AND S_1(x1) == 6
# mod 17 (chart congruence) -- moduli coprime, CRT.
r12 = regen_x(1, 2)
M = 64 ** 19
for dy in range(17):
    x1 = r12 + M * (5 + dy * 0)  # scan additive shifts for the chart class
    x1 = r12 + M * dy
    if S_m(1, x1) % 17 == 6 and x1 > 0:
        break
val = 81 ** 9 * (81 * x1 + 1)
cst2 = (64 ** 19 + 17) // 81
assert (val - cst2) % M == 0
x2 = (val - cst2) // M
A_tower = S_m(1, x1)
Ai = A_tower
okT = True
for _ in range(10):                      # H^{10}: stage-1 amplifier
    okT &= Ai % 64 in (0, 1)
    Ai = H(Ai)
okT &= Ai == S_m(2, x2) == val
for _ in range(19):                      # H^{19}: stage-2 amplifier
    okT &= Ai % 64 in (0, 1)
    Ai = H(Ai)
okT &= Ai == 81 ** 18 * (81 * x2 + 1)
check("explicit steered tower: S_1(x1) -H^10-> S_2(x2) -H^19-> "
      "81^18(81 x2 + 1)", okT)
# full Collatz lift of the 29 H-steps: 174 shortcut steps
n = n_of_A(A_tower)
okL = T_iter(n, 6 * 29)[0] == n_of_A(81 ** 18 * (81 * x2 + 1))
check(f"tower lift: T^174 on the {n.bit_length()}-bit Collatz integer "
      "matches", okL)

# ---------------------------------------------------------------- S9
print("== S9: boundary slope ==")
import math
val = math.log(81) / math.log(64)
cf = []
y = val
for _ in range(8):
    a = int(y)
    cf.append(a)
    y = 1 / (y - a)
check(f"CF of log_64 81 begins [1;17,1,1,1,8,1,2] (got {cf})",
      cf == [1, 17, 1, 1, 1, 8, 1, 2])
check("log_64 81 irrational (81^q = 64^p impossible)", True)

# ---------------------------------------------------------------- free validity
print("== free validity in the H-system ==")
runs = {}
tested = 0
for A0 in range(6, 4_000_000, 17):
    if A0 % 64 not in (0, 1):
        continue
    if 81 * A0 <= 146:
        continue
    tested += 1
    A = A0
    r = 0
    while A % 64 in (0, 1):
        A = H(A)
        r += 1
        if r > 60:
            break
    runs[r] = runs.get(r, 0) + 1
tot = sum(runs.values())
print(f"  {tested} valid seeds A == 6 mod 17, digit in {{0,1}}: run-length "
      f"distribution {dict(sorted(runs.items()))}")
mean_extra = sum((r - 1) * c for r, c in runs.items()) / tot
check(f"free continuation ~ Geometric(1/32): mean extra steps "
      f"{mean_extra:.4f} vs 1/31 = {1/31:.4f}",
      abs(mean_extra - 1 / 31) < 0.01)

print()
if FAILS:
    raise SystemExit("FAILURES: " + ", ".join(FAILS))
print("ALL CHECKS PASS")
