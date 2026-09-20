# Universal finite synchronization and persistent-companion return budgets

**Status: PROPOSED pending independent mathematical review.** 2026-09-20.
Continuation of PR #127; programme #121. This packet contains a complete
classification of *uniform affine-family merging*, not a complete Collatz
proof or a universally successful selector for given positive sources.
No external priority claim is made.

Parent: #127, `f5e7ec9a23fa691d71a5a9f518cbff5529a5ea00`.
Parallel source read: #128, `edd48df6e9c678fa4a65b4ed8f41421dfc92518b`.
The gap and signed-template primitives below come from #127. The complete
one-step comparison grammar is credited to #128/AUA-002. The original
companion ladder comes from #125. These statements are re-derived here
where needed, without promoting their previous review status.

## 0. Conventions and the quantifiers that matter

Throughout,

    T(n)=n/2 if n is even; T(n)=(3n+1)/2 if n is odd.

This is the unabsorbed shortcut map; it continues through 1 -> 2 -> 1.
Positive witnesses remain positive ordinary integers. A word records the
chronological source parities. Different original arms retain their own
clocks. A merger T^A(n)=T^B(m), 0<m<n, excludes a *least* nonconvergent n.
It is not necessary that the displayed forward arm descend below n.

There are three distinct universal assertions in this packet:

* Every eligible finite list of affine forms, with any prescribed arithmetic
  class for their common parameter, admits a constructive uniform merger
  on a further nonempty positive progression (Sections 1--3).
* Every ladder depth admits one progression synchronizing ALL its rungs,
  and this lifts to smaller ORIGINAL companions (Section 4).
* Every hypothetical least counterexample obeys a finite visit budget for
  core-certified comparison catalogues, provided original companion clocks
  persist and strictly advance on their repeated visits (Section 5).

The first two assertions are existence of translated families. Neither
asserts that a given fixed parameter belongs to the constructed progression.
The third is genuinely about each fixed hypothetical least counterexample,
but does not prevent a permanent escape from the specified catalogues.

For a physical word w of length L and q odd bits,

    2^L T_w(x) = 3^q x + A_w.

Starting at A=0, an odd bit at position i replaces A by 3A+2^i; an even
bit leaves A unchanged. The unique legal source residue modulo 2^L is
-A_w*3^(-q). Endpoint integrality gives this entire finite parity cylinder:
induction on the successive bits proves necessity and sufficiency. Hence
polynomial word checks below certify whole progressions, not sample points.

## 1. UFS-001: a synchronous gate for EVERY monomial-slope pair

### 1.1 Credited positive-gap primitive

For every g>=1, the parent supplies M=2^ell and 0<B<M with words p,q
of length ell such that

    T^ell(B+M*t) = T^ell(B+M*t+g), every integer t>=0.       (1)

A short self-contained construction starts from g=1, B=4, M=8 and
p=001, q=100. Nonterminal gaps decrease as follows:

    g even          -> g/2,       lower/upper words 0 / 0;
    g=1 mod4, g>1   -> (3g+1)/4,  lower/upper words 10 / 01;
    g=3 mod4        -> (3g-1)/4,   lower/upper words 01 / 10.

The odd cases restrict the lower source to 1 mod4 and 2 mod4 respectively.
Given a smaller-gap residue B modulo M, their pullbacks are

    (4B-1)*3^(-1) mod 4M; (4B-2)*3^(-1) mod 4M.

The even pullback is 2B modulo 2M. These residues are positive, and the
words physically reach the smaller-gap cylinder. Each gap decreases, so
induction terminates. This particular construction also has M<=8g^7;
that parent bound is not claimed as a new result here. The general-family
construction below does NOT inherit a polynomial bound in family size.

### 1.2 Credited balanced signed-template primitive

Suppose a>=1 and c=3^a-b>2^a. Follow the actual signed trajectory of -c
only through its a-th even step. This is a FINITE template, not an assumed
negative-orbit convergence theorem.

Its magnitude cannot reach 1: after e<=a even steps it is at least c/2^e>1,
since odd steps increase every magnitude greater than 1. Every odd run is
finite, as h-1 is multiplied by 3/2 and therefore consumes its finite
2-adic valuation. Thus the a-th even step exists. Let the word have length
ell and endpoint -h, h>1. It has ell-a odd bits.

For d=2^ell*u-1, the positive pair (3^a*d+b,d) has these same two prefixes:

    (3^a*d+b,d) -> (3^ell*u-h, 3^ell*u-1),               (2)
    words: signed-template word / 1^ell.

Take u sufficiently large for positive sources. Modulo 2^ell, the first
source agrees with -c; the affine formula proves (2). Apply (1) to gap h-1
and solve 3^ell*u-h=B mod M. The inverse of 3^ell exists modulo M. This
produces a dyadic progression of d with an exact synchronous merger.

### 1.3 New total preconditioning: remove the c>2^a hypothesis

**Theorem UFS-001.** For every integer a>=0 and every integer b, an algorithm
constructs L>=0, M=2^L, R>=1 and two words of length L such that, for all t>=0,

    T^L(3^a*(R+M*t)+b) = T^L(R+M*t),                  (3)

with both sources positive. R may exceed M: the certificate is a positive
tail of a residue class, and no claim about earlier nonpositive members
is made. The trivial a=b=0 case allows L=0.

**Proof.** For a=0, b=0 is immediate; otherwise apply (1) to |b| and
orient or shift the lower endpoint as appropriate.

For a>=1, Section 1.2 already handles 3^a-b>2^a. In the complementary
case b>0. Choose s>=1 with 2^s>2b. Follow b for exactly s steps; let v be
that physical word, q its odd count, and B=T^s(b). On the progression
d=2^s*u, the words v and 0^s give

    (3^a*d+b,d) -> (3^(a+q)*u+B,u).                   (4)

It remains to prove that this new pair meets the old hypothesis. In the
affine formula for the path from b, divide by 3^q. If q_i denotes the
number of odd bits up through an odd position i, then q_i>=1, and

    B/3^q = b/2^s + sum_(odd i) 2^(i-s)/3^q_i
           <= b/2^s + (1-2^(-s))/3 < 5/6.

Writing A=a+q, this gives B/3^A<5/(6*3^a)<=5/18<1/3. Consequently

    3^A-B > (2/3)*3^A = 2*3^(A-1) >= 2^A.

Section 1.2 now applies to (3^A*u+B,u). Pull its dyadic progression back
through d=2^s*u and prepend the actual words in (4). All words, positivity
and endpoint equalities hold on the resulting whole progression. QED.

This removes every affine-type eligibility restriction. It does not remove
the final input congruence. The preconditioning costs O(log(b+1)) steps
when needed; no comparable total-cost claim is made for the signed template.

## 2. UFS-002: synchronize ANY finite family inside ANY arithmetic class

**Theorem UFS-002.** Let f_i(x)=3^a_i*x+b_i, 1<=i<=N, with a_i>=0 and
b_i arbitrary integers. Given any m>=1 and r in Z, an effective finite
construction supplies integers B>=1, M>=1, L>=0, K>=1, E>=1 and physical
words w_i of length L such that

    B=r mod m, m divides M,
    f_i(B+M*t)>0,
    T^L(f_i(B+M*t)) = K*t+E, every i and every t>=0.    (5)

Moreover, M=2^L*oddpart(m). Duplicate forms are permitted. A nonempty
singleton family is permitted. No assertion about the original parameter
r itself, or every x=r mod m, is included.

**Proof.** First write m=2^k*h, h odd. Choose B=r mod 2^k large enough
that every f_i(B) is positive, and parameterize x=B+2^k*t. Follow each
f_i(B) for k steps. Their full cylinders have endpoint forms

    3^e_i*t+c_i, e_i=a_i+number_of_odd_bits, c_i>0.

All words currently have length k. Suppose some initial subcollection has
already merged, including representative i=1, and add one new form j.
Orient this pair so e_hi>=e_lo. It is exactly

    (3^a*y+b,y),
    a=e_hi-e_lo, b=c_hi-3^a*c_lo,
    y=3^e_lo*t+c_lo.

Use UFS-001 to obtain y=R mod 2^ell with y>=R. The coefficient 3^e_lo is
odd, so this congruence has a solution t=t0 mod 2^ell. Increase t0 by a
multiple of 2^ell if necessary to satisfy y>=R, and substitute

    t=t0+2^ell*v, v>=0.

The two selected arms merge after ell further steps. Arms previously equal
remain equal because they use the same deterministic T. Every other arm
can also be advanced ell steps on its entire now-refined cylinder: its
coefficient is divisible by 2^ell. Every endpoint is again an affine form
with coefficient a power of three. Positivity persists. The accumulated
source modulus and common word length increase by factors 2^ell and ell.

At most N-1 such calls merge the whole family. No same-input Collatz
termination assertion is used in this finite induction: termination counts
how many forms have joined the common endpoint.

Finally impose the odd part h. The accumulated source modulus is 2^L,
which is invertible modulo h. Solve B+2^L*v0=r mod h and replace
v by v0+h*t. This preserves all physical words, makes M=2^L*h, and
ensures (5) in the originally prescribed arithmetic class. QED.

**Consequences.** Every finite integer offset pattern admits a synchronous
merging progression in every arithmetic progression. Every finite H ladder
has a SINGLE compatible gate, not unrelated pairwise gates. No finite
congruence class can by itself exclude the existence of such a translated
synchronizing family. This is not natural-density one or a fixed-source
entry theorem. Nested refinements may force their least positive roots
to grow without bound.

## 3. UFS-003: COMPLETE classification for arbitrary positive affine slopes

For A>=1 define its 6-free part

    D(A)=A/(2^v2(A)*3^v3(A)),

which is a positive integer coprime to 6.

**Theorem UFS-003.** Fix a nonempty finite family F_i(x)=A_i*x+B_i with
positive integer slopes A_i and arbitrary integer intercepts B_i. The
following are equivalent:

(a) All D(A_i) are equal.
(b) For EVERY m>=1 and r in Z, there are an effective progression x=B+M*t,
    t>=0, inside x=r mod m, and fixed physical words of possibly different
    lengths L_i, for which every F_i(x)>0 and all T^L_i(F_i(x)) agree.
(c) Such fixed-word mergers occur for infinitely many integer parameters x.

When these hold, the construction gives L_i=L+v2(A_i). In particular,
a uniform EQUAL-clock merger exists exactly when the 6-free parts are
equal AND all v2(A_i) are equal. More generally, any uniform merger must
satisfy L_i-L_j=v2(A_i)-v2(A_j).

**Necessity.** On a fixed word of length L_i and odd count q_i, the
coefficient of x at the endpoint is A_i*3^q_i/2^L_i. Equality on infinitely
many x is polynomial equality, hence these coefficients are equal.
Taking valuations at every prime other than 2 and 3 forces D(A_i)=D(A_j).
Taking v2 forces the displayed clock difference. This also forbids a
bounded-clock merger scheme on infinitely many parameters when the
6-free parts differ: finitely many clock/word choices contain an infinite
subfamily, to which the same coefficient argument applies.

**Sufficiency.** Let A_i=D*2^s_i*3^a_i with D common and odd. Begin as in
Section 2, with x=B+2^k*t inside the dyadic part of the requested class
and all sources positive. Follow arm i for k+s_i steps. Its entire cylinder
ends at

    D*3^e_i*t+c_i, e_i=a_i+odd_count, c_i>0.

The initial clocks differ by s_i but every endpoint has the same odd
cofactor D. Use exactly the finite gluing argument from Section 2. The
low-arm parameter is now y=D*3^e_lo*t+c_lo, whose coefficient is still
invertible modulo every power of two. Each new merging block has the same
length on every arm; thus their clock differences stay s_i-s_j. Impose
the odd part of the prescribed class at the end as before. QED.

**Controls.** The forms x and 2x admit uniform mergers with a one-step
clock difference, but cannot admit equal-clock uniform mergers. The forms
x and 5x cannot admit ANY uniform fixed-clock merger on an infinite
parameter set, even though individual numerical pairs can meet. This is
not evidence of individual divergence. Constant forms (slope zero) are
outside the theorem: treating arbitrary fixed positive integers as constant
forms would be an invalid attempted Collatz corollary.

The necessity generalizes the earlier clock-rigidity observation credited
to #124. The new construction supplies the converse for arbitrary
intercepts, arbitrary finite families and arbitrary initial arithmetic classes.
No comprehensive external priority audit has been performed.

## 4. UFS-004: ALL rungs can merge with one ORIGINAL source

Let H(C)=9C+2, so H^i(C)=9^i*C+(9^i-1)/4. UFS-002 supplies, for every J>=1,
one progression C=B+M*t and a common clock L synchronizing

    C, H(C), ..., H^J(C).                              (6)

For example, the implementation proves the whole-cylinder identity

    C=68719476736*t+9321819871,
    T^36(C)=T^36(H(C))=T^36(H^2(C))=T^36(H^3(C))
          =3486784401*t+472983464, t>=0.                (7)

Here M=2^36 and 3486784401=3^20. The respective words are

    111110010011111100001001111110000100
    101100000111111100001001111110000100
    110000111011100000000011111110000100
    100111011010010010110100000100000001

To lift (6), choose r>=2J, e=r-2J+1 and solve

    4C+1=3^e*u, u>0 odd,
    n=2^r*u-1.

This is compatible with the dyadic progression by CRT. For 0<=j<J let

    m_j=(n-(4^(j+1)-1)/3)/2.

Each m_j is a positive original integer with 2m_j<n. The physical prefix
words, already underlying #125's ladder, give

    T^(r+2)(n)=H^J(C),
    T^(r+1)(m_j)=H^(J-j-1)(C),                         (8)
    n prefix: 1^r 01;
    m_j prefix: 1 0^(2j) 1^(r-2j-2) 00.

The last exponent is nonnegative. Direct substitution in the affine
word formulas proves (8); in particular their source residues establish
all the claimed parities. Equivalently the successive parameters satisfy
C_j=9*C_(j+1)+2, since the odd exponents differ by two.

Appending (6) proves that n and ALL J smaller original companions reach
one common endpoint, at clocks r+2+L and r+1+L respectively. There is no
independent choice of incompatible gates for different companions.

### Entire displayed forward arm above its original source

Set K=L+2. If

    3^r >= 2^(r+K),                                   (9)

then every positive-time state of the displayed n arm is strictly above n.
The first r odd steps increase n to 3^r*u-1. Each of the remaining K steps
retains at least half its positive input, so every such state is at least

    (3^r*u-1)/2^K > 2^r*u-1=n.

For each fixed J, (9) holds for all sufficiently large r, independently of
the chosen progression member. No generic no-descent claim is made for
arbitrary extensions beyond the displayed words.

We can additionally impose u=2^(-r) mod3. To do so, with Q=3^(e+1), impose

    C=(3^e*2^(-r)-1)*4^(-1) mod Q,

where 2^(-r) is evaluated modulo 3. CRT with M gives infinitely many C.
Then 3|n. A positive multiple of three has no odd inverse under T; all
its depth-b predecessors are 2^b*n. Thus it has no smaller pure ancestor
at any depth, despite these two-sided lower-source mergers.

A J=3 example, with r=65, is

    n = 8589578070121890293264089612287,
    m_0 = 4294789035060945146632044806143,
    m_1 = 4294789035060945146632044806141,
    m_2 = 4294789035060945146632044806133.

All four meet at

    T^103(n)=T^102(m_0)=T^102(m_1)=T^102(m_2)
            =125193752075618272398493166850127569035.

The smallest positive-time value on the entire displayed n arm is
12884367105182835439896134418431>n, and 3|n. The large sizes illustrate
(8)--(9); they are not evidence of coverage of all original inputs.

## 5. UFS-005: fixed-source budgets, even with companion switching

### Core-certified comparisons

A relation R on positive ordered pairs is core-certified if, whenever one
coordinate is 1 or 2, the other coordinate has a proved trajectory to 1.
Coordinate exchange is allowed. It is enough to supply explicit finite
paths for the relevant partners.

For the H relation {(9C+2,C): C>=1}, the only possible partners of a
core coordinate are 11 and 20: the core coordinate cannot be 9C+2.
The needed certificates are

    11 ->17 ->26 ->13 ->20 ->10 ->5 ->8 ->4 ->2 ->1,
    20 ->10 ->5 ->8 ->4 ->2 ->1.

For a fixed chart (3^a*y+b,y), a>=0, its complete core-partner menu is

    3^a+b, 2*3^a+b,
    (1-b)/3^a, (2-b)/3^a when these are positive integers.       (10)

Keep only positive values. Proving those finitely many values converge
core-certifies the chart. The packet provides complete path witnesses for
all 455 charts 0<=a<=6, -32<=b<=32, with 438 distinct positive partners.
This finite computation is not an assertion about every affine chart.

### The fixed-source theorem

**Theorem UFS-005.** Fix a positive source n and a finite collection S of
positive convergent original companions. Let tau(m) be the first shortcut
time at which m reaches 1. Consider actual comparisons

    (T^A(n), T^B(m)), m in S,

in any specified core-certified catalogue, with either orientation. Assume
that, on successive visits assigned to the SAME original m, its clock B
is a strictly increasing nonnegative integer. If n does not reach 1, then

    every assigned B<tau(m),
    total number of catalogue visits <= sum_(m in S) tau(m).    (11)

No restriction on the intervening physical trajectories or chart changes
is needed. The clocks refer to the original sources, not to newly named
inflated states.

**Proof.** If B>=tau(m), the companion lies in {1,2}. Core certification
then says the other coordinate T^A(n) converges, which implies n converges,
a contradiction. For each fixed m there are only tau(m) distinct allowable
nonnegative clocks B<tau(m). Sum over the finite collection. QED.

For a hypothetical least counterexample n, every m<n converges by
minimality. Thus (11) applies even with S={1,...,n-1}. It also applies to
any selected subset, including the original companion ladder. In particular,
a fixed least counterexample cannot run forever through the old alternating
H returns, nor can it evade this fact by switching among finitely many
smaller original companions with persistent advancing clocks.

An explicit rank for charged visits is the number of unspent pairs
(m,b), 0<=b<tau(m). On a visit, spend that clock slot; each revisit to
m must use a strictly later slot. This is a *catalogue-visit* budget, not
a rank that decreases at every ordinary shortcut step. Under minimality,
all the tau(m) are finite and can in principle be computed by direct
simulation; no bound in terms of n alone is asserted.

There is also a root-dependent form requiring no separate finite ledger.
For a least counterexample n, every chart with

    2*3^a+|b| < n                                     (12)

is core-certified by minimality: every positive number in (10) is less
than n. Thus a persistent comparison with a converged smaller companion
must eventually leave this entire root-dependent chart region. This is
a necessary escape-height condition, not a prohibition of escape.

### What this settles and what it does not

This formalizes the fixed-companion observation from the preceding chat
and extends it to switching and core-certified chart catalogues. The
previous generic warning about infinite hard itineraries should not be
read as an additional open case for a least counterexample when its same
smaller original companion and advancing clock have been retained.

Arbitrarily long finite growing-return families from #123 remain valid:
the original sources, companions and their tau values vary with the
requested finite itinerary. Nothing here excludes an infinite itinerary
for an arbitrary positive pair whose convergence is not known.

Resetting a companion clock, endlessly reusing a spent slot, or replacing
m<n by a source known smaller only than a later inflated state invalidates
(11). An infinite family of uncertified new charts is not automatically
core-certified: its core partners may include arbitrary unknown sources.
Most importantly, a fixed least counterexample could make finitely many
catalogue visits and then escape permanently. This packet does not rule
out that remaining case.

## 6. Bounded successive-type procedure and exact evidence

The generator first preserves #127's exact selected procedure: #125's VL
returns followed by the three old normalized-escape gates. Only after a
parent OUTSIDE result does it examine the actual next 12 synchronous
steps, trying UFS-001 at each of the 13 visited charts. The exhaustive
single-step chart grammar, including the d=0 orientation exchange, is
credited to #128/AUA-002. Every accepted continuation retains both
original words and their orientation. An exhausted lookahead is OUTSIDE,
not proof that another certificate does not exist.

On the identical complete parameter range 1<=C<=65536:

    old VL mergers                         4366
    old EG mergers                           99
    additional actual successive-type      2091
    total mergers                          6556
    retained OUTSIDE                      58980
    return-stage budget exhaustion            0

The parent full-row hash was checked, and all 4465 parent certificates
retain their exact words and endpoints. These are outcomes of this
specified finite certificate language, not a convergence census or a
percentage of hypothetical counterexamples removed.

The complete deterministic new corpus has 70033 rows: 3707 entire affine
gates, 93 whole finite-family cylinders, 227 general-slope classification
cases (114 whole mergers and 113 uniform impossibility controls), 32
original simultaneous-ladder examples, 438 core-partner paths, and all
65536 comparison outcomes. Among the family tests is a single progression
synchronizing 256 consecutive offsets within each of four prescribed
classes. Such finite tests support implementation checks; the unbounded
statements have the proofs above.

The separately implemented verifier imports no generator/repository code.
It reconstructs entire word numerators and source congruences, all original
paths and source orders, the complete core menus, and every finite selector
decision. Its gap pullbacks use direct dyadic inverses, its templates iterate
signed integers, and its chart exponents are inferred from actual parities
with intercepts recomputed by subtraction. Normal, -O and -OO verifier
runs agree and reject 32 semantic/type/JSON controls. These are direct
mutated-row controls, not separately resealed full-corpus corruptions.
Generator runs normally and under -O produce identical corpus bytes.

No complete-checkout root validator, remote CI, Lean build, or independent
mathematical peer review was performed in this authoring pass. Direct Git
transport failed DNS. API publication and blob readback are different
from full-checkout validation. The generator's signed-template resource
ceiling is an explicit implementation exception, not an unproved theorem
cutoff or a silent successful outcome.

## 7. The remaining universal-input problem

The classification now says exactly WHICH affine configurations can have
uniform merging progressions, and supplies them inside every requested
arithmetic class. The remaining task is not to find a nonempty gate for
another monomial-slope type: all such types already have one.

For a fixed ordinary source, one must instead control the least positive
roots of successive compatible refinements, or prove a companion switch
lands on an actual gate while preserving the original-root inequality.
Section 5 shows that indefinitely recycling the core-certified catalogue
is not a valid escape for a least counterexample with persistent clocks;
the unresolved case is permanent departure after finitely many visits.

The distinction is substantive: x and x+1 synchronize on a progression
inside every residue class, yet the particular pair (1,2) never synchronizes
under raw T. Dense available gates do not compel entry by a specified
integer. Likewise compatible finite witnesses do not imply a bounded
ordinary root for all refinements. No such inference is used here.
