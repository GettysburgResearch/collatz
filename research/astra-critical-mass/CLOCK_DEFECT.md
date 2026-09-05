# Sixth pass: unequal-clock reduction and the ternary precision budget

Agent: `astra-critical-mass-01` (GPT-6 Pro). Date: 2026-09-05.
Frozen parent: PR #90 at `908fdca1fe21456f8c6d476b31b74c8552670395`.

**All new theorem-level claims are PROPOSED pending independent review.**
The full merging cover, basin-stability implication, Green bound, signed
budget, and Collatz remain OPEN. No earlier proof or artifact is amended.

This pass attacks the phase obstruction rather than assuming the homogeneous
quotient must synchronize. It obtains an unequal-clock rank reduction for
859 using a different source, with an infinite upward progression and a sharp
ternary-depth guard. A compact compiler certifies 263 sufficient prefix rules
on the depth-two residual, covering 15980 of its 16384 dyadic branches at
modulus 2^18. The other 404 branches remain explicit.

The structural result is a converse to the preceding cancellation mechanism:
when 3^h(n) >= 12^M, EVERY lower-rank merging diagram with both clocks <=M
must be synchronous homogeneous ternary stripping. This applies to all
ordinary merging witnesses, not just a finite affine dictionary. A constructed
family has minimum diagram cost of order h(n), with an explicit finite
adaptive upper certificate. Thus small fixed clock menus are not a complete
escape from the phase obstruction.

## 0. Definitions and claim map

Use the shortcut map T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n. For all
positive integers, including ternary depth zero, set

    z(n)=2n+1,   h(n)=v3(z(n)),   P(n)=z(n)^2/3^h(n).

P is a positive integer and P(n)>=2n+1. Two ordinary sources merge when
T^r(n)=T^s(x) for finite nonnegative r,s. Empty words and clock zero are allowed.
A merging diagram is a reduction only when x>0 and P(x)<P(n).

A minimum-P exceptional integer would contradict any complete family of such
reductions. The elementary argument and normalization are in
[REMAINDER_CANCELLATION.md](REMAINDER_CANCELLATION.md) and
[MINIMUM_RANK.md](MINIMUM_RANK.md). This pass does not assume the residual is
empty. It does not label a smaller quotient as a merger without physical paths.

| Claim | Result | Boundary |
|---|---|---|
| T-ASTRA-030 | Complete short-clock classification at high ternary precision | Does not exclude longer or adaptive diagrams |
| C-ASTRA-031 | An ordinary family whose minimum merging-clock cost is Theta(h) | A family-local result, not a global complexity bound |
| L-ASTRA-032 | Exact frozen-defect rank-ray criterion | No generic valuation substituted on an unfrozen branch |
| T-ASTRA-033 | An unequal-clock reduction through 859, valid on an infinite progression | Its same-word extension to h>=3 increases rank |
| T-ASTRA-034 | Certified removal of 15980/16384 dyadic branches of the prior h=2 residual | 404 branches and all higher-depth residuals remain |
| X-ASTRA-006 | Separate physical, affine, CRT, and coverage reconstructions | Same-author implementations, not mathematical acceptance |

## 1. T-ASTRA-030: small-clock lowering must cancel exactly

For a parity word v of length r and odd count q_v, write

    T_v(n)=(3^q_v n+A_v)/2^r,
    B_v=2A_v+2^r-3^q_v.

The shifted identity is

    2^r z(T_v(n))=3^q_v z(n)+B_v.                         (1.1)

For the empty word B=0. Every nonempty word has B odd and

    2^r-1 <= B <= 3^r-2^r.                              (1.2)

Appending bit b at depth i replaces B by 3^b B+2^i, proving these facts by
induction. The same identity and elementary parity-cylinder bijectivity
were proved in the fifth packet; they are restated for a self-contained
clock comparison, not claimed as newly discovered affine formulas.

Suppose actual positive integers satisfy T_v(n)=T_w(x), with lengths r,s.
Set d=min(r,s), M=max(r,s), and define the integer clock defect

    D = 2^(s-d) B_v - 2^(r-d) B_w.

Then exactly

    2^(r-d) 3^q_w z(x) = 2^(s-d) 3^q_v z(n)+D.          (1.3)

If M>=1, then

    |D| <= 3^M-2^M < 3^M.                              (1.4)

For r>=s, D is the difference of B_v and 2^(r-s)B_w. Both are nonnegative
and at most 3^r-2^r; the latter bound uses
2^(r-s)3^s <= 3^r. The other ordering is symmetric. This is a bound on a
difference of two nonnegative quantities, not their sum.

### Theorem

Let M>=1 and H=h(n). Assume

    3^H >= 12^M,             r,s <= M.                  (1.5)

If D is nonzero, then

    P(x) > (4/3) P(n).                                  (1.6)

Consequently, every lower-rank diagram under (1.5) satisfies

    r=s>=1,   B_v=B_w,   p=q_w-q_v>0,
    z(n)=3^p z(x),        P(x)=3^(-p)P(n).               (1.7)

In particular no genuinely unequal-clock lower-rank diagram exists in this
regime. The result is uniform in x, the parity words, and their actual values.

### Proof

We may use the declared clock cap M in (1.4), even if both words are shorter.
If D!=0, put delta=v3(D)<=M-1. Condition (1.5) implies H>=M+1. In (1.3),
the source term has valuation H+q_v>delta. Since the denominator's ternary
valuation is q_w, ordinary integrality gives

    h(x)=delta-q_w >=0.                                 (1.8)

There is no unexamined cancellation at this step. Let

    a=2^(s-d)3^q_v,          b=2^(r-d)3^q_w.

Because z(n)>=3^H, a>=1, and |D|<3^M,

    z(x)/z(n) > (a/b)(1-3^(M-H)) >= (2/3)(a/b).

Therefore

    P(x)/P(n)
      > (4/9) 4^(s-r) 3^(H+2q_v-q_w-delta)
      >= (4/9) 4^(-M) 3^(H-M+1)
      >= 4/3.                                          (1.9)

The middle inequality uses q_w<=s, q_v>=0, delta<=M-1 and
4^(s-r)3^(-q_w)>=4^(-r)(4/3)^s>=4^(-M).
The last is (1.5). This proves (1.6).

If a diagram lowers rank, D=0. One empty and one nonempty word cannot give
D=0; both empty imply x=n. With both nonempty, B_v and B_w are odd, so
2^(s-d)B_v=2^(r-d)B_w forces r=s. Equation (1.3) then says
z(x)=3^(q_v-q_w)z(n). Its rank ratio is exactly 3^(q_v-q_w), so lowering
requires p=q_w-q_v>0. Ordinary integrality forces p<=H. QED.

### Scope and algorithmic use

The previous shared-remainder condition was sufficient. This theorem makes
that mechanism exhaustive in the short-clock/high-precision regime. For
M below the budget in (1.5), a search need only inspect exact cancellations;
changing the finite affine offset or choosing another cheaper source cannot
produce a nonzero-defect reduction there.

For a nonhomogeneous rank-lowering diagram, necessarily

    max(r,s) > h(n) log(3)/log(12).                      (1.10)

This is a necessary clock cost, not a sufficient existence theorem. All
comparisons in the implementation use integer powers, not approximate logs.

## 2. C-ASTRA-031: a total adaptive certificate with a necessary linear clock cost

Define C(n) as the minimum of max(r,s) over all finite positive ordinary
merging diagrams that lower P; set C(n)=infinity if there is none.

For every integer H>=3 there are infinitely many positive n with

    h(n)=H,                 v2(n+1)=4H.

Indeed combine, for either e=1 or e=2,

    n == 2^(4H)-1 mod 2^(4H+1),
    2n+1 == e*3^H mod 3^(H+1).                          (2.1)

The moduli are coprime; adding positive multiples gives ordinary integers.
Let M_H be the largest integer with 12^M_H<=3^H. For every such source,

    M_H+1 <= C(n) <= 4H+1.                              (2.2)

Thus the minimum clock cost on this family is Theta(H).

For the lower bound, the first M_H parities of n are all odd. If a lower-rank
diagram had both clocks <=M_H, T-ASTRA-030 would force r=s and q_w>q_v=r,
which is impossible for a length-r word. This excludes every candidate x,
not only the finite inverse examples checked computationally.

For the upper bound, the actual word 1^(4H)0 reaches

    y=(3^(4H)(n+1)/2^(4H)-1)/2.

The initial odd run has exactly 4H steps and the next step is even. Since
n=1 mod 3, the odd factor (n+1)/2^(4H) is a 3-unit and h(y)=4H. Directly,

    P(y)/P(n) = (243/256)^H ((n+1)/(2n+1))^2
              < (243/256)^H <1.                        (2.3)

This is a finite forward diagram of length 4H+1. The odd-run identity is
credited to the earlier packets; the new content here is its combination
with a lower bound against ALL shorter two-sided diagrams.

No single n is asserted to resist every finite horizon. The sources vary
with H. This does not contradict Collatz: the family has the explicit rank
reduction (2.3), not necessarily a supplied complete path to 1.

## 3. L-ASTRA-032: a frozen nonzero defect can still give a whole rank-reducing ray

Equation (1.3) is also a constructive interface below the rigidity threshold.
If delta=v3(D)<H+q_v and an ordinary diagram exists, then h(x)=delta-q_w is
fixed. Its shifted source has the form

    z(x)=alpha*z(n)+beta,   alpha>0,
    alpha=2^(s-r)3^(q_v-q_w).

Suppose a progression preserves the words, source depth H, and integrality.
For all its positive members the rank ratio is

    3^(H-h(x)) (alpha+beta/z(n))^2.                      (3.1)

If it is strictly below one at the least positive source and its limiting
value 3^(H-h(x))*alpha^2 is strictly below one, it remains below one on the
whole upward progression. The inner positive ratio is monotone toward alpha;
it stays between its first value and its limit. Positivity of the first
witness and alpha guarantees positivity thereafter.

This is the same limiting-ratio principle as T-ASTRA-024, now with the
ternary depth read exactly from the clock defect. It is NOT an assertion
that every finite successful diagram extends to an infinite family.

### The two certificate shapes compiled in this pass

Fix H=2 and an odd source word v of length j. Its dyadic source residue is
r mod 2^j. The exact depth condition is n=4 or 22 mod 27.

For a forward reduction x=T_v(n), take D=B_v, delta=v3(D), and require

    delta<q_v+2,             h(x)=delta,
    limiting ratio = 3^(2+2q_v-delta)/4^j <1.            (3.2)

For an unequal-clock reduction T_v(n)=T(x), take

    D=B_v-2^(j-1),           delta=v3(D),
    1<=delta<q_v+2,          h(x)=delta-1,
    limiting ratio = 3^(1+2q_v-delta)/4^(j-1) <1.        (3.3)

The compiler additionally requires an even, positive number of trailing
zeros in v. An odd step's endpoint is 2 mod 3; an even number of subsequent
halvings preserves that class. Hence T_v(n)=2 mod 3, and the distinct odd
predecessor x=(2T_v(n)-1)/3 is integral. Requiring at least two trailing
zeros prevents merely undoing the last odd step.

For each word, find the smaller of its two positive CRT bases for n=4,22
mod 27. Replay it physically, require x>=1 and P(x)<P(n), and check (3.2) or
(3.3). The worst first value and limiting value prove the entire ray, for
BOTH ternary unit classes. Words with an unfrozen valuation are skipped,
not assigned an average or generic depth. The witnesses' words and positive
integer values are retained by the separate checker.

## 4. T-ASTRA-033: the old phase obstruction has a different cheaper merger

For v=1101110101011100, the affine data are

    j=16, q_v=10, A_v=132845, B_v=272177.

For w=1, B_w=1 and q_w=1. The defect is

    D=272177-32768=239409=27*8867,

where 8867 is a 3-unit. Thus, for every n with h(n)>=2 that realizes v,

    x=(19683n+33359)/32768,
    z(x)=(19683z(n)+79803)/32768,
    h(x)=2,
    T^16(n)=T(x).                                      (4.1)

The source residue for v is 859 mod 65536. At exact depth two, (3.1) proves
this entire explicit progression:

    n_t=859+1769472t,
    x_t=517+1062882t,
    T^16(n_t)=T(x_t)=776+1594323t,
    P(x_t)<(3/8)P(n_t),                  t>=0.           (4.2)

The initial ratio is (115/191)^2=13225/36481<3/8. The limiting ratio is
(19683/32768)^2=387420489/1073741824, smaller than the initial one. All
source and witness depths are two, and both words are preserved by the
increments. This needs no computation of either total stopping time.

The preceding phase counterexample was the fixed quotient 859=9*95+4.
The new witness is 517, not 95. Consequently the fixed-quotient unequal-clock
obstruction is respected, not evaded by a change in terminology. At t=0
this diagram uses 17 total steps instead of the earlier 34+7 meeting with 95.
The new witness has higher rank than 95 but still strictly lower than 859.
No claim is made that this is the shortest possible diagram.

### Sharp failure of the same formula at higher ternary depth

The condition h(n)=2 cannot be removed. In the same dyadic source cylinder,
if h(n)>=3, formula (4.1) still gives a positive physical witness with h(x)=2,
but the positive affine defect gives

    P(x)/P(n) > 3^(h(n)-2) (19683/32768)^2 >1,           (4.3)

since 3*387420489>1073741824. Thus the same words now INCREASE rank.
The checker preserves high-depth countertests rather than promoting a
depth-two rule into an all-depth reduction.

## 5. T-ASTRA-034: a certified compression of the earlier depth-two residual

T-ASTRA-021 reduced a minimum-rank exceptional state with h=2 to

    n=139,427,571,859,1003 mod 1296.                      (5.1)

Equivalently, its dyadic part is n=11 mod 16 and its ternary part is one of
4,22,31,49,58 mod 81. Every n=11 mod 16 starts with the physical word 1101.

The new compiler starts there. At lengths 4,...,18 it attempts the forward
rule (3.2), then the odd-predecessor rule (3.3). A successful prefix is
removed; otherwise both next parity lifts are retained. Every accepted row
is justified by L-ASTRA-032, not by a finite sample extrapolation.

The exact certificate contains 263 prefix-free rules:

    192 forward rules;
     71 unequal-clock odd-predecessor rules.

At modulus 2^18 they cover 15980 of the 16384 classes that are 11 mod 16, leaving
404 explicit binary residues. Therefore, intersecting with the five ternary
conditions in (5.1), the remaining depth-two minimum-rank candidates occupy
exactly 2020 classes modulo

    81*2^18 = 21,233,664.                               (5.2)

This removes 15980/16384=97.5341796875% of the DYADIC BRANCHES of that earlier
residual by proved infinite-family reductions. It is not a statistical
success rate, not a percentage of Collatz solved, and not a coverage theorem
for higher ternary depth. Every remaining ordinary member is labelled
unresolved. The first residual in (5.1) under the new rules is 16987; no
nonconvergence claim is made for it.

The 404 residues and all 263 full rules are reconstructed by either checker;
use --full-output to materialize them. Their Cartesian CRT product with
{4,22,31,49,58} mod 81 defines (5.2) without ambiguous omissions. The compiler
is exhaustive only for its two stated certificate shapes and finite depth,
not for every possible merging diagram. Earlier proof packets can have
other reductions on some of this remaining set.

## 6. What this attempt tried to close, and the first unsupported step

The intended escape from the previous synchronized quotient barrier was to
allow unequal clocks and different cheaper sources. The positive rule (4.2)
and the 263-rule corpus show that this genuinely helps. The clock theorem
also shows why a bounded list of such repairs cannot handle arbitrary
ternary depth: below its necessary precision budget, every successful diagram
is forced back into exact homogeneous cancellation.

The constructed family in Section 2 makes this a necessary cost rather than
an abstract warning: its minimum diagram clock is bounded both below and
above by positive multiples of its ternary depth. A complete selector must
have genuinely unbounded depth, while preserving its ordinary replay.

**Q-ASTRA-003 is still OPEN.** The missing theorem is a total, terminating
selection of a lower-rank merging diagram for every residual source. Neither
an iteration of the finite cover nor a linear clock bound for all sources
is proved. In particular no recursion on the 404 remaining binary classes,
or on all h>=3 residuals, is asserted closed. Extending the finite table
without an all-length argument would not prove the conjecture.

## 7. Validation and sources

The [experiment](../../experiments/X-ASTRA-006-clock-defect/README.md) has two
separately written standard-library programs. The generator uses affine word
composition and direct inverse trees. The verifier reconstructs source words
by literal physical iteration, compares two inputs for affine slopes, uses
backward rational word maps to enumerate inverse candidates, and uses extended
Euclid rather than modular pow for CRT. Both have the same author.

The full reconstruction includes 263 rules, 404 residual binary classes, 2104
ordinary ray replays, 32 high-precision cases covering 5864 exact diagram pairs,
24 cost-family cases with 3048 actual forward steps, and 13 named/depth-guard
cases. Twelve lower-rank pairs in the rigidity tests exist and are all exact
homogeneous cancellations, so that check is not wholly vacuous. Eight
resealed corrupt reports are rejected after independent reconstruction.

The all-parameter theorems are proved above, not inferred from these samples.
The local code uses explicit checks, not Python assertions disabled by -O.
No outside theorem, high-range convergence computation, Lean build, or
repository-wide validator is a proof dependency.

Provenance: the shared B formula and global normalization are from the fifth
packet; the general progression-lifting principle and previous residual are
from the fourth; the original section and rank are credited there to PR #91
at b8c88843726ee7ac11cf91323c69bf911ca50706. Their acceptance statuses are not
changed here. A contextual primary-source abstract consulted on 2026-09-05 was
Applegate and Lagarias, *The 3x+1 Semigroup*, arXiv:math/0411140v2,
https://arxiv.org/abs/math/0411140v2 . Its multiplicative semigroup theorem is
not imported as an orbit-merging or parity-guard theorem. No PDF or external
formalization was audited in this pass. No broad external priority claim is made.
