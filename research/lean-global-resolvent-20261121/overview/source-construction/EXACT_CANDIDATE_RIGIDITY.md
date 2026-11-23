# An accepted finite triadic certificate is the exact all-time dual

23 November 2026. **PROVED:** the checkpoint-16 certificate forces the
supplied candidate itself onto the standard complementary cycle. It
therefore proves all-time compatibility of that same candidate. The
universal construction of an accepted candidate remains **OPEN**.

This strengthens the conclusion of checkpoint 16 without strengthening
its finite hypothesis. It arose while trying to construct a small
complementary residue, rather than assuming an all-time dual.

## 1. The finite hypothesis and strengthened conclusion

Use the shortcut map T(x)=x/2 on even integers and (3x+1)/2 on odd
integers. Fix n>0, signed a, and r>=0. Keep the same deterministic paired
trajectory as the preceding packet: its represented dual is w_j/3^r_j,
with one denominator factor cancelled at each original-even step while
the exponent is positive. Lowest terms are not required.

Put

    F(r)=product_(0<=j<r)(1+3^j),
    B=n*max(1,|a|)*F(r),
    E=bl(B),
    H=9E+1.

Assume the first H complementary-parity tests pass. Then there exists
a clock tau<=8E at which

    x_tau=1,
    w_tau=2*3^r_tau.

From that clock onward the represented dual is exactly opposite to the
standard original cycle 1,2. Thus all subsequent parity tests pass for
the same original candidate a/3^r. In particular,

    first H tests pass  <=>  all tests pass.

The H on the left is still computed from that very candidate's height.
There is no statement that any candidate exists for every n.

The Lean module `lean/TriadicCertificateRigidity.lean` proves the exact
paired hit and this finite-to-all-time implication. It does not require
a definition or algebraicity assumption for the 2-adic autoconjugacy.

## 2. The original first hit occurs by 8E

Suppose there is no original hit through clock 8E. If the numerator
remains nonzero, the previous eight-step contraction halves the positive
integer potential

    P_j=x_j |w_j| F(r_j)

E times, contradicting P_0<=B<2^E. Hence the numerator first becomes zero
at some j<=8E. For j>0 the preceding zero-entry lemma gives

    0<x_j+1<=P_(j-1)<=B<2^E.

For an initially zero numerator, use n+1<=2^E instead. The remaining
H-j>=E+1 passed tests force the original coordinate to take odd steps,
and hence 2^(E+1) divides x_j+1. This contradicts the displayed height
bound. Therefore the first original hit tau is at most 8E.

The zero-tail reserve is needed to exclude a zero branch; it does not
postpone the original hit to 9E+1.

## 3. The remaining finite tests identify the terminal dual exactly

The potential is nonincreasing before the first hit, including a zero
state if one had occurred. Therefore

    |w_tau| F(r_tau)<=B,
    r_tau<=r.

The elementary weight inequality is

    1+3^j<=2F(j)                 (j>=0).

Also B>=2F(r) for every accepted positive-input certificate. This is
immediate for n>=2. If n=1, the first test forces a even. The case a=0
fails the second test at (2,0,r), so |a|>=2 and the same bound follows.

Set d_tau=w_tau-2*3^r_tau. Multiplying the triangle bound by F(r_tau)
and using both inequalities above gives

    |d_tau|<=2B<2^(E+1).

More explicitly, |w_tau|F<=B and 2F<=B give

    (|w_tau|+2*3^r_tau)F
      <=B+B*3^r_tau
      <=2BF.

Now follow the original 1,2 cycle. At a state x in {1,2}, define the
integer defect

    d=w-(3-x)3^r.

At each compatible step one has either

    2d'=d,

or, only on the original-even branch at denominator exponent zero,

    2d'=3d.

Consequently L consecutive tests on that cycle force 2^L to divide its
initial defect, since three is odd. There are at least E+1 tests after
tau. Thus 2^(E+1) divides d_tau while |d_tau|<2^(E+1), forcing d_tau=0.

Once this exact paired state is reached, its future is the standard
opposite cycle. This is an explicit invariant of the deterministic
integer state rules, including unreduced representations.

## 4. Written arithmetic consequences for accepted candidates

The following consequences are written mathematics, not additional
theorems included in the current Lean module.

Because the finite hypothesis now supplies the all-time paired orbit,
the initial rational is the parity-complement value Omega(n). This
follows either from the uniqueness in the published autoconjugacy
construction or by pulling the standard terminal dual backward through
the same finite original word. Hence two accepted representations for
one n represent the same rational number.

Write that value in lowest terms as a_*/3^r_*. For n>2, let b_tau count
the original even steps before its first hit. The forced terminal segment
4,2,1 and denominator persistence give

    r_*=b_tau-1.

The exact affine identity at the first hit yields

    n*3^(tau-r_*-1)<=2^tau,

and thus

    tau <= [(r_*+1) log3-log n]/log(3/2).

Equality is possible for powers of two, whose first-hit word has no odd
input. It is strict when that word has an odd input. This is a bound
on the actual first hit after the full finite hypothesis has been
discharged, not a numerator-free finite compatibility hypothesis.

For n outside {1,2,4}, the accepted candidate is negative. Its first
negative-to-positive crossing is the exact pair

    (8,-1/9) -> (4,1/3),

followed by (2,1) and (1,2). The arbitrary-target crossing construction
in `CARRY_CONSTRUCTION_ATTACK.md` therefore cannot use an arbitrary
terminal dual and still pass its own full height horizon. Shorter local
continuations remain possible, exactly as that construction states.

## 5. What this changes in the attempted construction

The finite arithmetic search cannot succeed through a small-height
candidate that merely shadows a long initial segment and later departs
from the correct dual. Every accepted candidate already equals the exact
dual and admits indefinite continuation. This is a stronger conclusion
from the existing finite budget, and it makes the candidate's denominator
an actual first-hit clock parameter after reduction.

The next missing estimate is unchanged in substance: construct one
accepted candidate from each fixed positive n. Terminal interpolation
must still meet its extra 3-adic congruence, and the positive-sector reset
sum in the companion attempt note still has no sufficient source-specific
upper bound. No universal ordinary convergence claim follows without
that construction.

## 6. Exact dependencies and verification scope

The copied `TriadicAmortizedBudget.lean` and `TriadicDualClosure.lean` are
unchanged checkpoint-16 dependencies at PR176 commit
`fb402404deb810bd8e32e596993739bb5a6967d1`. The latter is itself the
unchanged PR178 source pinned by that checkpoint. The new theorem proves
its finite-to-all-time conclusion directly; it does not invoke the older
all-time convergence theorem to supply an unproved premise.

The new Lean source has `autoImplicit false`; compilation treats warnings
as errors. The complete new-declaration inventory and axiom audit are
recorded with the execution receipt. The finite exact tests cover the
signed and zero cases and deliberately failing terminal defects. These
checks supplement the symbolic proof; they do not establish candidate
existence by enumeration.

Monks--Yazinski, *The autoconjugacy of the 3x+1 function*, defines Omega
as the unique point with complementary parity sequence:
https://monks.scranton.edu/files/pubs/AutoConjV13.pdf.
That published interpretation is used only for the written corollaries;
the formal finite theorem is stated in the repository's literal integer
trajectory language.
