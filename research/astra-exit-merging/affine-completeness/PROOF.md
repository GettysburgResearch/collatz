# All-source return liveness and a complete affine-shadow existence criterion

**ACS-001--005: PROPOSED pending independent mathematical review.**
Date: 2026-09-20. Programme: issue #121. Parent: PR #128 at
`edd48df6e9c678fa4a65b4ed8f41421dfc92518b`.

This pass answers two different questions, without conflating their quantifiers.

* For **every hypothetical least positive counterexample**, the existing
  fixed-companion return process must escape in finite time. Its possible
  infinite hard-return branch is already incompatible with minimality. This
  includes the enlarged valuation language of #125, not only #123.
* For **every finite collection of nonconstant integer affine source families**,
  we classify exactly when fixed physical words can merge the whole collection
  on an infinite parameter set. The criterion is equality of the slopes after
  removing all factors of two and three. When it holds, a terminating compiler
  constructs such a merger inside **any specified arithmetic progression**.

The first result is pointwise in the original source but uses least-counterexample
minimality. The second is unconditional and complete as a classification of
uniform affine templates, but constructs a **subprogression**, not a merger for
an arbitrary prescribed parameter. Neither proves Collatz. In particular, a
compiler choosing new parameter digits is not an actual-orbit termination proof.

Use raw shortcut T(x)=x/2 for positive even x and (3x+1)/2 for positive odd x.
Raw T continues through 1 -> 2 -> 1. Each original source has its own physical
clock. All actual witnesses are positive ordinary integers. Negative constants
in symbolic affine expressions are allowed only with an explicit positive-source
threshold; they are not negative trajectories used as positive witnesses.

For a chronological parity word w of length l and q odd bits,

    2^l T_w(x)=3^q x+A_w.

The ordinary legality cylinder is x=-A_w*3^(-q) mod 2^l. This elementary
interface, the first odd-run entry, the H return, and the fixed-gap compiler
are credited in SOURCES_AND_LIMITS.md. They are restated where needed.

## 1. ACS-001: no infinite hard returns at a least counterexample

### 1.1 A general physical-clock lemma

Suppose m is a positive source whose first visit to 1 is at time sigma(m).
Then T^t(m) belongs to {1,2} for every t>=sigma(m).

Consequently, there cannot be infinitely many strictly increasing physical
clocks t_j with T^(t_j)(m)>=3. More generally, for a finite pool of convergent
positive sources S, suppose every use of m in S reads a state at least 3 and
its recorded clock strictly increases on successive uses. The total number
of such uses is at most

    sum_(m in S) sigma(m),

or sum max(0,sigma(m)-b_m) when each clock starts at b_m. This is just the
number of available integer clocks below the first visit to 1. It does NOT
permit resetting a clock on reuse or replacing an old source by an unbounded
stream of new sources. It is a mathematical finiteness bound, not a known
numerical bound in n unless the stopping times have separately been supplied.

For a hypothetical least nonconvergent N, every source 1<=m<N converges.
The lemma therefore applies to every fixed finite pool of smaller ORIGINAL
companions, and even to adaptive selection from ALL sources 1<=m<N, because
that whole pool is finite. A conservative bound from clock zero is

    sum_(1<=m<N) sigma(m).

Thus switching repeatedly among different smaller shadows cannot evade the
finiteness argument, provided each shadow keeps its own nonresetting clock.
The condition that the used checkpoint lies outside the core is essential.
Knowing that this budget exists does not produce the required legal transition
or a merger when a shadow reaches the core. No convergence assumption about
N, numerical uniform stopping-time bound, or effective all-N selector is used.

### 1.2 The old H return already has this property

Write H(C)=9C+2. The #123 transition admits C only when

    r=v2(C+2)-1>=3,   C=2^(r+1)b-2, b positive odd.

After r+3 steps on each arm it either merges (H(C),C), or returns to
(D,H(D)) with D=(3^(r-1)b-1)/4. The return exchanges the two original arms.
The physical words are supplied in #123 and recalled in the experiment.

Every admitted parameter satisfies C>=14, so BOTH coordinates at the start
of every admitted stage are at least 14. Both original clocks advance by
at least six. Thus an infinite sequence of admitted hard returns would make
BOTH original sources nonconvergent: a source that ever reached 1 could not
keep appearing at these checkpoints. This is an unconditional implication
for every positive starting pair supporting the displayed comparison.

If one original companion m converges, and its entry clock is b0, at most

    ceil(max(0,sigma(m)-b0)/6)                            (1)

hard-return stages can be completed. Indeed the starting clock of stage j
is at least b0+6j and must be below sigma(m). A terminating merging stage
can be counted with the same starting-clock bound. This is conservative:
some earlier states already equal 2 and are also inadmissible.

No decrease of C or any proposed rank was used. In particular the r>=8
expanding returns do not obstruct this argument. Arbitrarily long finite
constructions change their source and companion; their companion stopping
times need not be bounded uniformly.

### 1.3 The enlarged #125 valuation language is finite for the same reason

Its two entrance guards are

    A: v2(3C-2)=2k+3, k>=0;
    B: v2(3C-1)=2k+4, k>=0.                              (2)

For A put b=(3C-2)/2^(2k+3), D=(3^(k+1)b+1)/2. The bridge words
00(01)^k00 / 01(10)^k11 end at (D,3D+2).
For B put b=(3C-1)/2^(2k+4), D=(3^(k+2)b+1)/2. The words
100(01)^k00 / 110(10)^k11 give the same type.

Read s=v2(D+1), z=3^s(D+1)/2^s. Append

    1^s01 / 1^s00 if z=3 mod4: merge at (3z-1)/4;
    1^s00 / 1^s01 if z=1 mod4: return to (C',H(C')),
                                      C'=(z-1)/4>0.       (3)

These are the source-qualified identities VL-003/004, not new identities.
They have equal finite clocks and exchange roles on a hard return.
Every admitted C is at least 14: checking C=1,...,13 gives no guard in (2),
or solve the displayed congruences. Every complete stage has at least six
steps on each arm. Hence exactly the same proof and bound (1) apply.
The experiment reconstructs both bridge paths from the raw map, independently
of the generator's formulas.

The important conclusion is NOT an unconditional exclusion of every positive
C with an infinite return itinerary. It is that such an itinerary cannot
arise with a convergent fixed companion, hence cannot arise in the
least-counterexample comparison below.

### 1.4 A finite escape is forced for EVERY hypothetical least counterexample

A least nonconvergent N>1 is odd and 3 mod4: the other cases descend in one
or two steps. Write N=2^r u-1 with r>=2 and u positive odd, and set
m=(N-1)/2<N. The credited first odd-run identity gives either a merger, or

    T^(r+2)(N)=H(C), T^(r+1)(m)=C,
    C=(3^(r-1)u-1)/4>0, C=2 mod3.                       (4)

A merger is impossible under the least-counterexample hypothesis. Follow
#125's actual valuation returns with this same m and these same clocks.
A merging exit again contradicts minimality. Infinite returns are excluded
by 1.3 because m converges. Therefore the process must reach a finite escape
with

    C>0, C=2 mod3,
    NOT [v2(3C-2) is odd and >=3],
    NOT [v2(3C-1) is even and >=4].                       (5)

The ternary condition is preserved: in either bridge D=2 mod3. Thus
3 divides D+1 and also divides z in (3), so C'=(z-1)/4=2 mod3.

The original-root restriction is still present. With an even number of
role swaps, the original N-arm is H(C), so 9C+2>=N. With an odd number,
it is C, so C>=N. Every original N-iterate is at least N by minimality.
A locally smaller companion after this escape need not be below N.

For the shorter #123-only process, the corresponding finite escape has
v2(C+2)<=3 and C=2 mod3; equivalently it lies in one of the four disjoint
classes

    C=5 mod6,  C=8 mod12,  C=2 mod24,  C=38 mod48.         (6)

The stronger exclusion (5) is the useful current target. It still contains
unbounded classes; it is not a finite list of numerical exceptions.

**What changes for the research programme.** One need not invent a global
rank for infinite iterations of the present hard-return rules. That case
is already disposed of in a least-counterexample proof. The work left is
what happens at the actual finite escapes (5), with clocks and original
source order retained. This observation is elementary, but removes a
logically unnecessary global obligation from this specific route.

## 2. ACS-002: a terminating synchronizer for EVERY integer affine chart

For every d>=0 and b in Z, there are computable equal-length words F,G and
one dyadic residue c modulo 2^ell such that

    T^ell(3^d y+b)=T^ell(y)                              (7)

for every y in that residue class for which both source values are positive.
A first positive representative is explicitly computable. No inequality
3^d-b>2^d, negative cycle, or signed stopping-time premise is needed.

Let B=|b|+3^d, R=bitlength(B). One possible compiler satisfies

    ell <= d(R+2)+6R+3.                                 (8)

This bounds word construction, not the time until a prescribed input's
actual parameter falls in a successful class.

### 2.1 Three controlled reductions

At a chart (3^d y+b,y) with d>0 use:

| Chart condition | Impose on y | Words on the two arms | New chart parameters |
|---|---|---|---|
| b even and nonzero | y even | 0 / 0 | d, b/2 |
| b odd | y odd | 0 / 1 | d-1, (b-3^(d-1))/2 |
| b=0 | y odd | 1 / 1 | d, (1-3^d)/2 |

These are selected rows of the exhaustive grammar in #128, with parity
choices used to construct a gate. They are NOT freely selectable at a fixed
y: there the actual parity dictates the row. All divisions and word parities
follow immediately from the table.

After a b=0 step, b becomes a nonzero negative integer. Halve a nonzero even
b until odd, then use the second row to reduce d. Therefore exactly d such
exponent reductions reach a constant-gap chart. The b=0 case is essential:
blindly halving zero would create a false nontermination in the compiler.

For a direct bound, use P=|b|+3^d at the start of one exponent-reduction
block. If b is nonzero, its preparatory halvings do not increase P and the
odd-intercept step gives

    P_new <= |b|/2 + 3^(d-1)/2 + 3^(d-1) = P/2.

If b=0, the one preparatory odd step increases P to less than 3P/2; after
any intervening halvings and the exponent reduction, P_new<3P/4.
Thus P at the beginnings of these blocks never exceeds its initial B.
At most R halvings, one possible zero-intercept step, and one exponent
reduction are used per block. This gives at most d(R+2) prefix steps.

### 2.2 Finish any signed constant gap

At d=0, b=0 is already a merger. Otherwise let g=|b| and order the pair so
the larger coordinate is lower+g. Use the credited #128/#127 gap compiler:

    g even:              g -> g/2,           cost 1;
    g=1 mod4, g>1:       g -> (3g+1)/4,      cost 2;
    g=3 mod4:            g -> (3g-1)/4,      cost 2;
    g=1: lower=4 mod8, words 100/001,         cost 3.

The odd cases impose lower=1 mod4 and lower=2 mod4, respectively.
Every nonterminal step has g_new-1 <= (3/4)(g-1).
As (4/3)^3>2 and g<=B, at most 3R such stages suffice; their words have
length at most 6R+3. Exchanging the two words when b<0 preserves original
source labels. This proves (8).

### 2.3 Why all the requested parities can be realized simultaneously

After a prescribed finite word of length j, the current lower coordinate
is (3^q y+A)/2^j. The prefix fixes one y residue modulo 2^j. The two lifts
modulo 2^(j+1) change this coordinate by the odd number 3^q, so exactly one
lift supplies either requested next parity. Equivalently, each new lower
congruence can be pulled back using the inverse of an odd coefficient.
The gap compiler's guards have the same property. Hence the completed word
pair has one consistent residue class for y, never an empty set of formal
constraints. Choosing y sufficiently far along that progression ensures
both starting values are positive, and then all physical intermediate
values are positive.

The full affine identities are

    q_G-q_F=d,   3^(q_F)b+A_F=A_G,

and the source residues of F,G are compatible under x=3^d y+b. The verifier
checks these statements on whole progressions, not only sampled values.

Example outside #127's condition: d=2,b=20 has 3^d-b=-11, but on

    y=16t+12,
    T^4(9y+20)=T^4(y)=9t+8,
    words 0000 / 0011.                                  (9)

No negative-source argument is needed. Conversely a familiar output is
C=128t+59 for H(C), already published as VL-006. Reproducing that gate is
credited as an overlap, not a new result.

## 3. ACS-003: complete classification of finite affine shadow collections

Let s>=2 and

    f_i(t)=A_i t+B_i,  A_i positive integers, B_i integers.

Define the factor remaining after deleting all twos and threes,

    core_6(A)=A / (2^v2(A) * 3^v3(A)).

The following are equivalent:

1. Fixed finite physical words w_i send all f_i(t) to the same endpoint for
   infinitely many integer parameters t where the sources are positive.
2. core_6(A_i) is the same for every i; equivalently A_i/A_j is a rational
   product of integer powers of 2 and 3 for every pair i,j.
3. For EVERY arithmetic progression t=a mod M, M>=1, an explicitly
   computable nonempty subprogression t=t0+M*2^K h, h>=0, has all sources
   positive and has fixed words w_i merging ALL of them simultaneously.

The compiler returns t0,K,the words, their independent clocks, and the
common affine endpoint as a function of h. This is a full existence
classification for nonconstant affine templates, not only for periodic
shadows, a finite menu, selected signs of B_i, or dyadic starting progressions.

### Necessity and forced clock differences

Write l_i=|w_i| and q_i for its odd count. Equality for infinitely many t
makes the affine endpoint expressions identical. Comparing their slopes,

    3^(q_i) A_i / 2^(l_i) = 3^(q_j) A_j / 2^(l_j).

It follows that their core_6 values agree, and necessarily

    l_i-l_j = v2(A_i)-v2(A_j),
    q_i-q_j = v3(A_j)-v3(A_i).                           (10)

The pairwise necessity is the earlier AAC-001 clock-rigidity observation.
The sufficiency and simultaneous construction below are the extension.

If the core values disagree, fixed words can yield at most one parameter
for that particular word tuple, because the endpoint difference has a
nonzero slope. This does NOT rule out isolated mergers, parameter-dependent
unbounded words, or convergence of every individual member. For example
5t+1 and t+1 have incompatible cores but coincide at t=0.

### Sufficiency for a pair on an arbitrary prescribed progression

Substitute t=a+Mz. The two positive slopes are now A_1 M,A_2 M and still
have equal core_6. For a current affine expression Pz+Q with even P, its
next parity is the constant Q mod2 for every integer z. Apply exactly v2(P)
physical steps, following these forced bits. The coefficient becomes odd;
there is no choice of parameter or convergence premise here.

Do this separately on the two arms. Their new odd slopes differ by an
integer power of 3 after possibly exchanging their labels. Thus the pair
has exactly the form

    (3^d Y+b,Y),   Y=Pz+Q with P odd,

with integer b and d>=0. Apply ACS-002. Its dyadic guard on Y pulls back to
one residue for z because P is odd. Substituting this residue gives a
subprogression of the original a mod M. Appending the two compiler words
proves a uniform merger. Restrict its first representative until both
original source values are positive. Physical iteration then supplies all
intermediate positivity automatically.

### Simultaneous sufficiency for any finite collection

Merge the first two families. All their retained original paths now share
one affine endpoint. Compare that common endpoint to the third family;
its slope ratio is still a product of powers of 2 and 3, since every
previous operation multiplied slopes only by 3 or divided by 2 and any
parameter refinement multiplied every slope by the same power of 2.

Use the pair construction again. Refine the SAME global parameter
progression, and append the same new word to every already merged arm.
This preserves all earlier equalities. Induction handles the whole finite
collection. Every refinement is dyadic relative to the initially specified
M, and every step is a finite computation. At the end, advance the first
parameter along the final progression far enough to make every source
positive. No incompatible independently chosen parameter values are combined.

This proves (2)=>(3); (3)=>(1) is immediate. The construction is implemented
for arbitrary finite input lists, not merely pairs.

### Examples

For every h>=0, put t=205+256h. Then

    T^11(8t-5)=T^10(4t-1)=T^8(3t-5)=81h+65.            (11)

At h=0 the three sources are 1635,819,610. The two companions are smaller
than the first original source for every h. This example demonstrates
SIMULTANEOUS synchronization, not new global coverage of the burst family.

The same three templates can be compiled while preserving t=7 mod24:
choose t=6127+12288h. Their clocks are 15/14/12 and their common endpoint is
2187h+1091. The factor 3 in the required initial modulus is not discarded.

For t=387+2048h,

    T^11(t+1)=T^11(t+2)=T^11(t+3)=T^11(t+4)=243h+47.    (12)

A four-template example with common core 5 and unequal slopes uses
5t+1,30t-19,90t+7,180t on a subprogression of t=17 mod40. Its complete
words and exact affine endpoints are retained in the corpus. These examples
are outputs of the general compiler, not an asserted optimal atlas.

## 4. ACS-004: no permanent arithmetic-progression failure region

For any compatible affine collection in ACS-003, no arithmetic progression
can consist entirely of positive parameters on which that collection never
merges by any fixed word tuple: each progression contains a uniform
simultaneous merger subprogression. This rules out a whole congruence class
as a permanent barrier for this affine template collection.

In particular, inside EVERY dyadic parameter cylinder there is a smaller
cylinder of simultaneous success. The uniform-merger set is open and dense
in the 2-adic parameter space (with positive ordinary tails on its cylinders).
This is a topological statement, not a Haar-measure-one theorem or an
ordinary-integer covering theorem. No Hausdorff dimension or density saving
is inferred from density in this topological sense.

It also matters that the claim concerns the union over arbitrary finite
words. A fixed finite atlas can certainly have an entire unresolved
progression at its cutoff; later words may cut a hole in it. The construction
can work within such a specified cell without erasing its earlier failure
record, but it generally changes the selected parameter.

**Pointwise countercontrol.** The compatible templates t+2,t+1 at t=0 give
the pair (2,1), which never merges at equal times. Nevertheless every
progression t=0 mod2^J contains a subprogression where those templates do
merge synchronously. For J=3 one output is t=48 mod128, length seven.
The fixed integer t=0 remains outside that new gate. This explicitly blocks
the invalid inference 'success in every neighborhood implies success of
the given ordinary point.'

## 5. ACS-005: what this does and does not accomplish for all positive integers

The pointwise universal conclusion of this pass is (5): every hypothetical
least positive counterexample has a finite escape from the two existing
valuation return languages, with the SAME smaller original companion,
nonresetting clocks, the ternary restriction, and the source-height
inequality preserved. The infinite-return issue is not an additional
unproved premise for that least-counterexample route.

The unconditional algebraic classification is ACS-003. It proves that
2-and-3 slope compatibility is both necessary and sufficient for uniform
finite affine-template merging; it supplies simultaneous witnesses in any
prescribed congruence class. The former restriction 3^d-b>2^d in the
parallel #127 sufficient construction is unnecessary for this new compiler.
That older theorem and its positive-source examples remain valid unchanged.

These results still do NOT prove that a particular fixed escape parameter
in (5) lies in a gate, or that some smaller original companion at that
parameter has a merger. ACS-002's controlled parity choice constructs a
residue class; it is not a legal choice at a fixed integer whose parity is
already determined. Constant source families (all slopes zero) are outside
ACS-003: their coalescence question is not resolved by coefficient comparison.

No convergence-density claim, no full Collatz solution, no independent
mathematical acceptance, and no external priority claim is made. The fixed
pair 3003/999 retains its opposite raw core phases; the different-companion
certificate from #124 is not contradicted or re-proved by pretending that
this pair merges synchronously.

The next genuinely global task is a POINTWISE restart or companion-switch
rule at the finite escapes (5), with original source order and physical
clock accounting. The clock lemma shows what a closed rule system would
need for liveness: if it keeps using a finite pool of smaller companions,
it cannot reset their clocks and must account honestly for a companion
reaching the core. The affine compiler supplies available templates, not
that missing closure rule. Enlarging the template list alone is no longer
the correct definition of progress toward an all-input theorem.
