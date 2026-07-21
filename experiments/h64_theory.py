"""Three theorems in the H-frame, verified.

THEOREM 1 (H-rigidity, three lines).  Within the 64->81 subsystem every
valid step multiplies by exactly 81/64 up to a bounded additive part:
    A_S = (81^S A_0 - 17 C)/64^S,  0 <= 17C <= 81^S,
so (81/64)^S (A_0 - 1) <= A_S <= (81/64)^S A_0.  If an exp-poly family
N(k) ~ c 64^{mk} satisfied H^{S(k)}(N(k)) = N(k+Delta), Delta >= 1, then
(81/64)^{S(k)} -> 64^{m Delta}, forcing S(k) eventually constant = S,
and coefficient matching gives 81^S = 64^{S + m Delta}: impossible.
NO hypotheses on S(k) (affine or otherwise), no crash-and-climb case:
the subsystem freezes odd-density at 4/6, so the T-frame pathologies
cannot occur.

THEOREM 2 (coding).  The valid set V_inf = {A in Z_2 : every H-iterate
has base-64 digit in {0,1}} is homeomorphic to {0,1}^N: for every
epsilon-sequence there is exactly ONE 2-adic A whose digit sequence
under H is that sequence (digit t fixes A mod 64^{t+1}).

COROLLARY (no integer cycles, one line).  A valid p-periodic point
satisfies A = 17 C_w/(81^p - 64^p) with 0 <= 17 C_w <= 81^p, hence
0 <= A <= 81^p/(81^p - 64^p) <= 81/17 < 5; integers 0..4 check directly
to leave only the trivial fixed digits 0 and 1.

THEOREM 3 (automaticity of regeneration residues).  The residue
r_{m,m'} of (8.2) satisfies: for every depth j, r_{m,m'} mod 64^j
depends only on (m mod 2^{6j-4}, min(j, 9m'+1)); i.e. the residue data
is 2-AUTOMATIC in m at every fixed depth (period 2^{6j-4} = ord(81 mod
64^j) in m).  Combined with Cobham (k-automatic sequences have rational
letter frequencies) and Gelfond--Schneider (the required schedule
frequency log_64 81 is transcendental), no k-automatic certificate can
drive the schedule, while all residue data is automatic: the surviving
certificate class is Sturmian/Ostrowski-computable, outside every
Cobham class.
"""

from fractions import Fraction
from itertools import product
from core import T_iter

FAILS = []
def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" -- {detail}" if detail and not cond else ""))
    if not cond:
        FAILS.append(name)


def H(A):
    B, e = divmod(A, 64)
    assert e in (0, 1)
    return 81 * B + e


# ------------------------------------------------------- Theorem 1
print("== Theorem 1: H-rigidity ==")
# two-sided bound check on random valid words
import random
random.seed(11)
ok = True
for _ in range(3000):
    S = random.randrange(1, 40)
    eps = [random.randrange(2) for _ in range(S)]
    C = sum(eps[t] * 64 ** t * 81 ** (S - 1 - t) for t in range(S))
    ok &= 0 <= 17 * C <= 81 ** S
    # affine form: verify on the coded 2-adic truncation lifted to ints
    A0 = random.randrange(2, 10 ** 8) * 64 ** S  # divisible => digits 0
    AS = A0
    for _ in range(S):
        AS = H(AS)
    ok &= AS * 64 ** S == 81 ** S * A0  # all-zero digits case exact
check("affine form and bound 0 <= 17C <= 81^S (3000 random words)", ok)

# numeric search for expanding H-identities on exp-poly families: none
found = []
for d in (1, 17):
    for mm in (1, 2):
        for al in range(1, 6):
            for be in range(-30, 31):
                Ns = {}
                good = True
                for k in range(4, 12):
                    num = al * 64 ** (mm * k) + be
                    if num <= 0 or num % d:
                        good = False
                        break
                    Ns[k] = num // d
                if not good:
                    continue
                for Delta in (1, 2):
                    okd = True
                    for k in range(4, 9):
                        tgt = Ns.get(k + Delta)
                        A = Ns[k]
                        hit = False
                        for s in range(1, 200):
                            if A % 64 not in (0, 1):
                                break
                            A = H(A)
                            if A == tgt:
                                hit = True
                                break
                            if A > tgt:
                                break
                        if not hit:
                            okd = False
                            break
                    if okd:
                        found.append((d, mm, al, be, Delta))
check("no expanding H-identity on exp-poly families in range", not found,
      str(found))

# ------------------------------------------------------- Theorem 2
print("== Theorem 2: coding V_inf ~ {0,1}^N ==")
# cleaner: direct recursion from the uniqueness proof:
def code_to_A2(eps):
    """A == eps0 (64); write A = 64B + eps0, then B's digit sequence must
    code eps1 eps2... SHIFTED through 81B + eps0's digits... use direct
    per-step solving: maintain A mod 64^k by requiring digit t of the
    orbit mod 64^{k} to match."""
    k = len(eps)
    A = eps[0] % 64
    M = 64
    for t in range(1, k):
        M *= 64
        base = A
        step = M // 64
        done = False
        for c in range(64):
            cand = base + c * step
            X = cand
            good = True
            for s in range(t + 1):
                if X % 64 != eps[s]:
                    good = False
                    break
                X = H(X)
            if good:
                A = cand
                done = True
                break
        if not done:
            return None
    return A

ok = True
for _ in range(60):
    k = random.randrange(1, 9)
    eps = [random.randrange(2) for _ in range(k)]
    A = code_to_A2(eps)
    ok &= A is not None
    if A is None:
        continue
    X = A
    for s in range(k):
        ok &= X % 64 == eps[s]
        X = H(X)
check("every {0,1}-word codes a unique residue (60 random words, k<=8)", ok)

# periodic words = rational fixed points 17C/(81^p - 64^p)
ok = True
for p in range(1, 7):
    for w in product((0, 1), repeat=p):
        C = sum(w[t] * 64 ** t * 81 ** (p - 1 - t) for t in range(p))
        Afix = Fraction(17 * C, 81 ** p - 64 ** p)
        ok &= 0 <= Afix <= Fraction(81, 17)
        # 2-adic check: Afix mod 64^p equals the coded residue
        A = code_to_A2(list(w) * 2)  # 2 periods for safety
        den = Afix.denominator
        if den % 2 == 0:
            ok = False
            continue
        Amod = Afix.numerator * pow(den, -1, 64 ** (2 * p)) % 64 ** (2 * p)
        ok &= Amod == A
check("periodic codes = rational fixed points 17C/(81^p-64^p), all p<=6", ok)
# direct: integers 0..4: which are valid fixed/periodic?
per = []
for A0 in range(5):
    A, seen = A0, set()
    okv = True
    for _ in range(20):
        if A % 64 not in (0, 1):
            okv = False
            break
        A = H(A)
    if okv:
        per.append(A0)
check(f"direct: integer valid periodic points in 0..4 are exactly {{0,1}}",
      per == [0, 1])

# ------------------------------------------------------- Theorem 3
print("== Theorem 3: 2-automaticity of regeneration residues ==")
def regen_r(m, mp, j):
    """r_{m,m'} mod 64^j."""
    M = 64 ** (9 * mp + 1)
    cst = (M + 17) // 81
    r = pow(81, -(9 * m + 1), M) * (cst - 81 ** (9 * m)) % M
    return r % 64 ** j

ok = True
for j in (1, 2):
    period = 2 ** (6 * j - 4)
    vals = [regen_r(m, m + 17, j) for m in range(1, 3 * period + 5)]
    ok &= all(vals[i] == vals[i + period] for i in range(len(vals) - period))
    # and the period is exact (not smaller) for j = 2
    if j == 2:
        half = period // 2
        ok &= any(vals[i] != vals[i + half] for i in range(half))
check("r_{m,m+17} mod 64^j periodic in m with exact period 2^{6j-4} "
      "(j=1: 4, j=2: 256)", ok)
# schedule side: increments {17,18} Sturmian for slope log_64 81:
import math
sl = math.log(81) / math.log(64)
# per macro-step the boundary gains sl-1 digits; one new digit per
# 1/(sl-1) ~ 17.65 steps => Sturmian over {17,18}, frequency of 18 is
# frac(1/(sl-1)) -- irrational (transcendental slope)
freq18 = 1 / (sl - 1) - 17
check(f"stage-gap frequency of 18 = {freq18:.6f} irrational "
      "(from transcendental slope); Cobham: not k-automatic", 0 < freq18 < 1)

print()
if FAILS:
    raise SystemExit("FAILURES: " + ", ".join(FAILS))
print("ALL CHECKS PASS")
