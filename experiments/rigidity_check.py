"""Numeric confirmation of the schema-rigidity theorem.

THEOREM (single-parameter schema rigidity; proof in ../RIGIDITY.md).
Let N(k) = (sum_i alpha_i 2^{m_i k} + beta)/d  (exp-poly values: exactly
the value forms of RLE word families with block lengths affine in k),
positive and increasing, Delta >= 1.  Then there is NO S(k) >= 1 with
    T^{S(k)}(N(k)) = N(k+Delta)   for all large k,
provided the derivation respects its fuel  S(k) <= v2(N(k) - beta/d).

This script searches small parameter ranges for counterexamples to the
theorem (there must be none), and also exhibits CONTRACTING identities
(Delta <= -1), which DO exist -- showing the search is not vacuous.
"""

from fractions import Fraction
from core import T_iter

found_expanding = []
found_contracting = []

def v2(x):
    x = Fraction(x)
    n = x.numerator
    if n == 0:
        return 10 ** 9
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v

KS = list(range(8, 14))          # test window for k
for d in (1, 7, 5, 3):
    for m in (1, 2, 3):
        for alpha in range(1, 10):
            for beta in range(-40, 41):
                # N(k) = (alpha*2^{mk} + beta)/d must be a positive integer
                Ns = {}
                ok = True
                for k in range(min(KS) - 2, max(KS) + 3):
                    num = alpha * 2 ** (m * k) + beta
                    if num <= 0 or num % d:
                        ok = False
                        break
                    Ns[k] = num // d
                if not ok:
                    continue
                for Delta in (1, 2, -1, -2):
                    # is there S(k) with T^{S(k)}(N(k)) = N(k+Delta),
                    # S <= fuel, for all k in KS?
                    good = True
                    Ss = []
                    for k in KS:
                        fuel = m * k + v2(Fraction(alpha, d))
                        tgt = Ns.get(k + Delta)
                        if tgt is None:
                            good = False
                            break
                        x = Ns[k]
                        S = None
                        for s in range(1, fuel + 1):
                            x2, _ = T_iter(Ns[k], s)
                            if x2 == tgt:
                                S = s
                                break
                        if S is None:
                            good = False
                            break
                        Ss.append(S)
                    if good:
                        rec = (d, m, alpha, beta, Delta, Ss)
                        if Delta >= 1:
                            found_expanding.append(rec)
                        else:
                            found_contracting.append(rec)

print(f"expanding identities found (theorem says 0): {len(found_expanding)}")
for r in found_expanding:
    print("  !!", r)
print(f"contracting identities found (expected >0): {len(found_contracting)}")
for d, m, alpha, beta, Delta, Ss in found_contracting[:10]:
    print(f"   N(k)=({alpha}*2^{{{m}k}}{beta:+d})/{d}, Delta={Delta}, S(k)={Ss}")

assert not found_expanding, "RIGIDITY THEOREM CONTRADICTED -- investigate!"
print("\nOK: no expanding single-parameter schema identity in range.")

# ----------------------------------------------------------------------
# Lemmas A, B, B' used in the rigidity proof (RIGIDITY.md section 0)
# ----------------------------------------------------------------------
import random
random.seed(42)
okA = okB = okBp = True
for _ in range(20000):
    n = random.randrange(1, 10 ** 12)
    S = random.randrange(1, 50)
    m, par = T_iter(n, S)
    A = sum(par)
    c = 2 ** S * m - 3 ** A * n
    okA &= c >= 0
    okB &= c <= S * 3 ** max(S - 1, 0)
    if c > 0:
        rt = max(Fraction(3 ** (A - sum(par[:j])), 2 ** (S - j))
                 for j in range(S + 1))
        okBp &= Fraction(c, 2 ** S) <= Fraction(S, 2) * rt
print("Lemma A (c >= 0):", "PASS" if okA else "FAIL")
print("Lemma B (c <= S*3^{S-1}):", "PASS" if okB else "FAIL")
print("Lemma B' (c/2^S <= (S/2)*max suffix multiplier):",
      "PASS" if okBp else "FAIL")
assert okA and okB and okBp
