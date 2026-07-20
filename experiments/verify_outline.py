"""Exact verification of every claim in the symbolic-rewrite outline
(sections 1-7).  All checks are exact integer/rational arithmetic.

Run:  python3 verify_outline.py
Each check prints PASS/FAIL; any FAIL raises at the end.
"""

from fractions import Fraction
from core import (T, T_iter, is_odd, value_word, to_word, radix_replace,
                  CycleSystem, CYC_M1, CYC_M5, CYC_M17, cycle_check)

FAILS = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f"  -- {detail}" if detail and not cond else ""))
    if not cond:
        FAILS.append((name, detail))


# ======================================================================
# S1. exact binary/ternary rewrite system
# ======================================================================
print("== S1: binary/ternary rewrite system ==")

b = lambda i: (lambda x: 2 * x + i)
t = lambda j: (lambda x: 3 * x + j)

ok = all(T(b(0)(x)) == x for x in range(200))
ok &= all(T(b(1)(x)) == t(2)(x) for x in range(200))
check("S1.branches  T(b0 x)=x, T(b1 x)=t2 x", ok)

# push-through rules t_j b_i -> b_{(3i+j)%2} t_{(3i+j)//2}
ok = True
table = {}
for j in range(3):
    for i in range(2):
        i2, j2 = (3 * i + j) % 2, (3 * i + j) // 2
        table[(j, i)] = (i2, j2)
        ok &= all(t(j)(b(i)(x)) == b(i2)(t(j2)(x)) for x in range(100))
claimed = {(0, 0): (0, 0), (0, 1): (1, 1), (1, 0): (1, 0),
           (1, 1): (0, 2), (2, 0): (0, 1), (2, 1): (1, 2)}
check("S1.push-through rules (all 6)", ok and table == claimed)

# high end: value of '#' is 0 (empty word); t_j # has value j
ok = (t(0)(0) == 0) and (t(1)(0) == b(1)(0)) and (t(2)(0) == b(0)(b(1)(0)))
check("S1.high-end rules t0#->#, t1#->b1#, t2#->b0b1#", ok)

# one round = one shortcut step, on canonical words (exhaustive small check)
def round_step(word):
    """word: LSD-first binary digits.  Delete b0, or b1 -> t2 then
    normalize the ternary digit to the top.  Returns new binary word."""
    if not word:
        return None
    if word[0] == 0:
        return word[1:]
    # replace by t2 at position 0 acting on rest
    rest = list(word[1:])
    j = 2
    out = []
    for i in rest:
        i2, j2 = (3 * i + j) % 2, (3 * i + j) // 2
        out.append(i2)
        j = j2
    # t_j # at top
    if j == 1:
        out.append(1)
    elif j == 2:
        out += [0, 1]
    return out

ok = True
for n in range(1, 4000):
    w = to_word(n, 2)
    w2 = round_step(w)
    ok &= value_word(w2, 2) == T(n)
check("S1.one round == one shortcut step (n=1..3999)", ok)

# ======================================================================
# S2. radix-replacement theorem
# ======================================================================
print("== S2: radix replacement ==")
ok = True
uniq_ok = True
for L in range(1, 13):
    for r in range(2 ** L):
        a, c, par = radix_replace(L, r)
        ok &= (0 <= c < 3 ** a) and a == sum(par)
        # verify on two x values (affine identity => two points suffice)
        for x in (0, 1, 7, 10 ** 6):
            got, _ = T_iter(2 ** L * x + r, L)
            ok &= got == 3 ** a * x + c
check("S2.radix-replacement T^L(2^L x + r) = 3^a x + c, L<=12, all r", ok)

# Terras-style bijection: r -> parity word is a bijection for each L
for L in (1, 2, 3, 8, 11):
    words = set()
    for r in range(2 ** L):
        _, _, par = radix_replace(L, r)
        words.add(tuple(par))
    check(f"S2.parity words distinct (bijection) L={L}", len(words) == 2 ** L)

# ======================================================================
# S3. negative three-cycle amplifier
# ======================================================================
print("== S3: -5 cycle system ==")
check("cycles are cycles", cycle_check())

ok = all(T_iter(8 * q - 5, 3)[0] == 9 * q - 5 for q in range(-50, 51))
ok &= all(T_iter(8 * q - 7, 3)[0] == 9 * q - 7 for q in range(-50, 51))
ok &= all(T_iter(8 * q - 10, 3)[0] == 9 * q - 10 for q in range(-50, 51))
check("S3.three identities T^3(8q-s)=9q-s, s in {5,7,10}", ok)

sysc = CycleSystem(CYC_M5, names=['A', 'B', 'C'])
# claimed state rule table: (X, r) -> (Y, c)
A, B, C = 0, 1, 2
claimed_rules = {
    (A, 0): (A, 0), (A, 3): (C, 4), (A, 6): (B, 7),
    (B, 0): (B, 0), (B, 2): (A, 2), (B, 5): (C, 6),
    (C, 0): (C, 0), (C, 3): (B, 3), (C, 5): (A, 5),
}
check("S3.state rules match compiler", sysc.rules == claimed_rules,
      f"compiler produced {sysc.rules}")

# normalization rule N_c O_r semantics + macro step == 3 shortcut steps
import random
random.seed(1)
ok = True
for _ in range(400):
    X = random.randrange(3)
    w = [random.randrange(8) for _ in range(random.randrange(1, 9))]
    if w[-1] == 0:
        w[-1] = 1
    n = sysc.config_value(X, w)
    if n <= 0:
        continue
    out = sysc.macro_step(X, w)
    m, _ = T_iter(n, 3)
    if out is not None:
        Y, w2 = out
        ok &= m == sysc.config_value(Y, w2)
check("S3.macro step == exactly 3 shortcut steps (400 random configs)", ok)

# q' - q = (q + s_Y - s_X)/8 > 0 for q>5 whenever transition exists
ok = True
for (X, r), (Y, c) in sysc.rules.items():
    for x in range(0, 60):
        q = 8 * x + r
        qp = (9 * q + sysc.s[Y] - sysc.s[X]) // 8
        assert (9 * q + sysc.s[Y] - sysc.s[X]) % 8 == 0
        if q > 5:
            ok &= qp > q
check("S3.growth q'>q for q>5 in the subsystem", ok)

# ======================================================================
# S4. growth gadget  A 6^{k+1} => B 5^k 7 => C 3^{k-1} 5 0 1 => B 6^{k-2} 0 6 1 1
# ======================================================================
print("== S4: growth gadget ==")
ok = True
for k in range(2, 30):
    w0 = [6] * (k + 1)
    st = (A, w0)
    n0 = sysc.config_value(*st)
    st = sysc.macro_step(*st)
    ok &= st is not None and st[0] == B and st[1] == [5] * k + [7]
    st = sysc.macro_step(*st)
    ok &= st is not None and st[0] == C and st[1] == [3] * (k - 1) + [5, 0, 1]
    st = sysc.macro_step(*st)
    ok &= st is not None and st[0] == B and st[1] == [6] * (k - 2) + [0, 6, 1, 1]
    # and the whole thing is exactly 9 shortcut steps
    m, par = T_iter(n0, 9)
    ok &= m == sysc.config_value(*st)
check("S4.gadget chain exact for k=2..29 (9 shortcut steps)", ok)

# next low digit is 6 in state B and B O_6 is not a rule
check("S4.B6 exits the subsystem", (B, 6) not in sysc.rules)

# ======================================================================
# S5. bridge lemma and 24-step combined identity
# ======================================================================
print("== S5: bridge lemma ==")

def octal_word_B_bridge(m):
    return [6] * m + [0, 6, 1, 1]

ok_q = all(value_word(octal_word_B_bridge(m), 8) == (4374 * 8 ** m - 6) // 7
           and (4374 * 8 ** m - 6) % 7 == 0 for m in range(1, 20))
check("S5.q_m = (4374*8^m - 6)/7", ok_q)

ok_n = all(8 * value_word(octal_word_B_bridge(m), 8) - 7
           == (3 ** 7 * 2 ** (3 * m + 4) - 97) // 7 for m in range(1, 20))
check("S5.n_m = (3^7 2^{3m+4} - 97)/7", ok_n)

# 2-adic template -97/7: first 15 parities and trajectory
x = Fraction(-97, 7)
traj = [x]
for _ in range(15):
    x = T(x)
    traj.append(x)
claimed_par = [1,0,1,1,1,1,1,1,0,0,0,0,0,1,1]
_, par = T_iter(Fraction(-97, 7), 15)
check("S5.parity word of -97/7 is 101111110000011",
      par == claimed_par, f"got {par}")
check("S5.template trajectory passes -142/7, -71/7, -103/7 ... -43/7",
      traj[1] == Fraction(-142, 7) and traj[2] == Fraction(-71, 7)
      and traj[3] == Fraction(-103, 7) and traj[15] == Fraction(-43, 7))
check("S5.nine odd steps in the window", sum(claimed_par) == 9)

# the bridge: B 6^m 0 6 1 1 # =(15)=> A 1^{m-5} 7 6 4 5 2 7 6 5 #
ok = True
for m in range(5, 26):
    n = 8 * value_word(octal_word_B_bridge(m), 8) - 7
    got, par = T_iter(n, 15)
    ok &= par == claimed_par
    target_word = [1] * (m - 5) + [7, 6, 4, 5, 2, 7, 6, 5]
    ok &= got == 8 * value_word(target_word, 8) - 5
    r = m - 5
    ok &= got == (3 ** 16 * 2 ** (3 * r + 4) - 43) // 7
check("S5.bridge lemma exact for m=5..25", ok)

# sharpness: the 15 template parities need 2^15 | perturbation, i.e.
# 3m+4 >= 15, i.e. m >= 4 (the user's m>=5 is what makes the OUTPUT
# word 1^{m-5}... exist as a word; the value identity holds from m=4).
n4 = 8 * value_word(octal_word_B_bridge(4), 8) - 7
_, par4 = T_iter(n4, 15)
got4 = T_iter(n4, 15)[0]
check("S5.m=4 still follows template (value identity holds, r=-1)",
      par4 == claimed_par and got4 == (3 ** 16 * 2 ** 1 - 43) // 7)
n3 = 8 * value_word(octal_word_B_bridge(3), 8) - 7
_, par3 = T_iter(n3, 15)
check("S5.m=3 deviates (sharpness at m=3)", par3 != claimed_par,
      f"m=3 parities {par3}")

# combined 24-step identity for k >= 7
ok = True
for k in range(7, 28):
    Nk = 8 * value_word([6] * (k + 1), 8) - 5
    ok &= Nk == (48 * 8 ** (k + 1) - 83) // 7
    got, par = T_iter(Nk, 24)
    Mk = 8 * value_word([1] * (k - 7) + [7, 6, 4, 5, 2, 7, 6, 5], 8) - 5
    ok &= got == Mk
    ok &= Mk == (3 ** 16 * 2 ** (3 * k - 17) - 43) // 7
    ok &= sum(par) == 15
check("S5.24-step identity A6^{k+1} => A1^{k-7}76452765, 15 odd, k=7..27", ok)

check("S5.multiplier 3^15/2^24 < 1 < 3^16/2^24",
      3 ** 15 < 2 ** 24 < 3 ** 16)
check("S5.density 15/24 < log_3 2 (i.e. 3^15 < 2^24... equivalent)",
      3 ** 15 < 2 ** 24)  # 15/24 > log32 <=> 3^15 > 2^24

# ======================================================================
# S6. where the repeated block goes
# ======================================================================
print("== S6: positive rational sink ==")

x, par = T_iter(Fraction(-43, 7), 14)
check("S6.T^14(-43/7) = 5/7 with 6 odd steps",
      x == Fraction(5, 7) and sum(par) == 6, f"got {x}, odd={sum(par)}")

cyc = [Fraction(5, 7)]
for _ in range(4):
    cyc.append(T(cyc[-1]))
check("S6.cycle 5/7 -> 11/7 -> 20/7 -> 10/7 -> 5/7, parity 1100",
      cyc == [Fraction(5,7), Fraction(11,7), Fraction(20,7),
              Fraction(10,7), Fraction(5,7)])

ok = True
for r in range(4, 12):
    u = (3 ** 16 * 2 ** (3 * r + 4) - 43)
    assert u % 7 == 0
    u //= 7
    got, _ = T_iter(u, 14)
    ok &= got == (3 ** 22 * 2 ** (3 * r - 10) + 5) // 7
    for j in range(0, (3 * r - 10) // 4 + 1):
        if 4 * j <= 3 * r - 10:
            gj, _ = T_iter(u, 14 + 4 * j)
            ok &= gj == (3 ** (22 + 2 * j) * 2 ** (3 * r - 10 - 4 * j) + 5) // 7
check("S6.T^{14+4j}(u_r) = (3^{22+2j} 2^{3r-10-4j} + 5)/7", ok)

# ======================================================================
# S7. periodic phase schedules cannot work
# ======================================================================
print("== S7: periodic obstruction ==")

# |q| <= 5 bound + direct check: enumerate all (X, q) with |q| <= 100,
# follow subsystem transitions, find all cycles.
def sub_step(X, q):
    r = q % 8
    if (X, r) not in sysc.rules:
        return None
    Y, c = sysc.rules[(X, r)]
    return Y, (9 * q + sysc.s[Y] - sysc.s[X]) // 8

cycles_found = set()
for X0 in range(3):
    for q0 in range(-100, 101):
        st = (X0, q0)
        seen = []
        while st is not None and st not in seen and abs(st[1]) <= 10 ** 6:
            seen.append(st)
            st = sub_step(*st)
        if st in seen:
            i = seen.index(st)
            cyc_states = tuple(sorted(set(seen[i:])))
            cycles_found.add(cyc_states)
allq = sorted({q for cycs in cycles_found for (_, q) in cycs})
check("S7.only subsystem cycles have q=0 (the negative cycle itself)",
      allq == [0], f"cycle q values {allq}")

# ======================================================================
print()
if FAILS:
    print(f"{len(FAILS)} FAILURES:")
    for name, d in FAILS:
        print("  -", name, d)
    raise SystemExit(1)
print("ALL CHECKS PASS")
