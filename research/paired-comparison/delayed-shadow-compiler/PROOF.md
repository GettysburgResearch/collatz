# Delayed shadows: all intercepts, all dyadic cells, and permanent isolated meetings

**DS-001--006: PROPOSED pending independent mathematical review.**
Date: 2026-09-20. This is an additive research continuation, not a complete
Collatz proof, independent acceptance, or an external priority claim.

The strongest universal statement is DS-004: every dyadic input cell contains
an explicitly constructible uniform merger subcell for the FIXED comparison
(H(C),C), H(C)=9C+2. DS-005 proves why this cannot be promoted to fixed-input
coverage: ordinary positive parameters that actually merge can permanently
lie outside every finite uniform merger cylinder. Both results hold together.

## Conventions and provenance

T is the unabsorbed shortcut map: T(n)=n/2 for even n and (3n+1)/2 for odd n.
In particular 1 <-> 2. All certificate sources and arms are positive ordinary
integers. Signed T is used only to compile a provably finite word. A word
lists actual source parities chronologically. Comparison tails are synchronous;
original source prefixes retain their independent clocks and immutable roots.
A uniform cylinder means a fixed finite pair of words valid on an entire
power-of-two progression, not individual successes at varying times.

The preceding in-chat packet was published separately as PR #129:
`9d362511343c97790d42808c363b090a3342b45f`, branch
`research/anchored-r-bridges-20260920`, tree
`aa595f5728bee49aca04459d073dcbd8e721d97a`. Its AR-001--006 are in
`research/paired-comparison/anchored-returns/PROOF.md`. This continuation
is a separate child commit; it does not amend those source bytes or statuses.

Read dependencies and parallel work:

* #125 `081dd4fb8af75b3b237a5eb4cef28b84bb5329be`,
  `research/paired-comparison/valuation-ladder/PROOF.md`: VL forced H-entry,
  valuation returns, original-source ladder, first-exit CRT lifts.
* #127 `f5e7ec9a23fa691d71a5a9f518cbff5529a5ea00`,
  `research/paired-comparison/escape-gaps/PROOF.md`: EG-002 all-gap compiler,
  EG-003 balanced finite negative shadows under 3^a-b>2^a, EG-004/005 type
  gates and exponent lifts. All-gap existence and signed balancing are credited.
* #128 `edd48df6e9c678fa4a65b4ed8f41421dfc92518b`,
  `research/astra-exit-merging/universal-shadow-atlas/PROOF.md`, sections 1--4:
  universal entrance, countable affine-pair grammar, another all-gap compiler,
  and a smaller-shadow subfamily inside every finite parity template.
  Its grammar and bounded atlas already distinguish isolated from uniform
  meetings. DS-005 adds an all-future exclusion criterion, not priority for
  noticing isolated points. DS-004 keeps the same affine comparison rather
  than selecting a different shadow source for each prescribed prefix.
* Earlier source pins remain #124 `1d4dfc103055648def3db73860778a383a91ea3c`
  and #126 `7e996feb24cc5d8579d75b39e0b909ffc03b3bcb`.

Main was `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Main, source branches,
scientific statuses, workflows, settings and licensing are unchanged.
No analytic, density, rank-transport, or external formalization theorem is a
premise. The public literature check was not a comprehensive priority audit.

## DS-001. A long-block all-gap compiler with a smaller modulus exponent

For EVERY integer g>=1 there are an explicit power of two M=2^ell, a residue
0<B<M, and words w,z of length ell with the same odd count such that

    T^ell(Mt+B)=T^ell(Mt+B+g), every integer t>=0.           (1)

Let

    p = log(8)/log(8/3) = 2.120085157834271... .

For g>=2 our long-block construction satisfies

    M <= 16 (g-1)^p,
    ell <= 4 + p log_2(g-1).                              (2)

For g=1 take M=8, B=4, words 001/100. This is a quantitative improvement
of the already-published all-gap existence theorem, not a new claim of its
priority. #127 gives M<=8g^7. #128 gives ell<=2K+3 with K the least positive
integer satisfying (4/3)^K>g-1; that corresponds to the stronger-than-seven
polynomial exponent log(4)/log(4/3), approximately 4.819. The exponent in
(2) improves both guarantees. It bounds one supplied progression, not the
unknown total density of successful pairs and not Collatz convergence density.

### Physical long blocks and inverse pullbacks

The inverse of a delayed odd word 0^j1 sends an endpoint z to

    (2^(j+1)z-2^j)/3,

whereas the inverse of 10^j sends z to

    (2^(j+1)z-1)/3.                                      (3)

When their numerators are divisible by three, these are actual positive
paths with exactly the indicated parities. In the first expression the
source has exactly j factors of two, and in the second it is odd; the
subsequent j halvings follow from 3x+1=2^(j+1)z.

For even g=2h, double both sources of the h certificate and prefix 0 on
both arms. Thus M(g)=2M(h).

For odd g=1 mod4, g>1, put

    j=v2(3g+1)>=2, h=((3g+1)/2^j-1)/2.

If h=0, use M=2^(j+1), B=2^j and the words 0^j1 / 10^j.
Here g=(2^j-1)/3 and both endpoints are 3t+2.
Otherwise take the h certificate for (z,z+h), where z=B_h+M_h t.
Choose t in one class modulo three so that z=2 mod3. Define

    x=(2^(j+1)z-2^j)/3,
    y=(2^(j+1)(z+h)-1)/3.

Then y-x=g and the prefixes 0^j1 / 10^j reach the h pair. Appending its
words proves (1). Both integrality conditions follow from 3g+1=2^j(2h+1).

For odd g=3 mod4, except the special base g=3, put

    j=v2(3g-1)>=2, h=((3g-1)/2^j+1)/2.

Choose the h certificate parameter z so that 2^(j+1)z=1 mod3, and set

    x=(2^(j+1)z-1)/3,
    y=(2^(j+1)(z+h)-2^j)/3.

Now y-x=g, and the prefixes 10^j / 0^j1 reach (z,z+h). Again the second
integrality condition follows from the gap equation. Each odd pullback has
modulus 2^(j+1)M_h: restricting t=t0+3v cancels its denominator three.
Taking t0 in {0,1,2} makes the new residue strictly between zero and that
modulus. Thus every v>=0 is a positive ordinary realization.

In every nonterminal case 1<=h<g. The recursion is therefore finite. Use
for g=3 the explicit base M=64, B=10, words 010001/100100, endpoint 9t+2.
This small special case improves the constant in (2). Implementation uses
iterative descent/unwind, without a Python recursion-depth restriction.

### Proof of the bound

For either long odd branch with h>=2, direct substitution gives

    h-1 <= 3(g-1)/2^(j+1).

Since j>=2, p>1 and 8(3/8)^p=1,

    2^(j+1) [3/2^(j+1)]^p <= 1.

The induction M_h<=16(h-1)^p therefore proves (2) on that branch. On an
even branch h>=2, use 2(h-1)^p <= (2h-1)^p; g=2 has M=16 directly.
The base g=3 has M=64<=16*2^p because p>2.
If h=0 then g>=5 and M=6g+2<=16(g-1)^p. The remaining h=1 can occur
only in the second odd branch; apart from the special g=3 it has g>=5,
2^j=3g-1 and M=16(3g-1)<=16(g-1)^2<=16(g-1)^p.
This completes the induction using exact inequalities, not fitted data.

For executable integer-only checks we use the weaker consequence
M^4<=16^4(g-1)^9. Indeed p<9/4, since 3^9<8^5. This is clearly labeled
as a consequence, not a numerical verification of the sharper logarithmic
exponent. The proof supplies that sharper bound for all gaps.

Example g=23: the retained short-block compiler gives M=16384,B=6166;
the new long-block compiler gives M=4096,B=3253. Thus the new supplied
progression has four times the density for this example.
The implementation also retains a long-block variant whose gap-one base is
M=32,B=5, words 10001/01100. Its analogous constant is 64, not the constant
16 asserted for the main variant. Old and alternate gates are kept because
smaller guaranteed modulus does not imply containment of successful inputs.

## DS-002. Delayed signed seeds handle every affine intercept

Fix ANY integers a>=1 and b. For EVERY k>=0 satisfying

    (3^a-2^a)2^k > b,                                    (4)

one can explicitly construct a dyadic progression of positive d with
EXACT v2(d)=k, on all of which (3^a d+b,d) merges synchronously by fixed
finite words. Such k always exist, and all sufficiently large k satisfy (4).
There is no remaining restriction on the intercept b.

### Finite stopping without a negative-orbit conjecture

Set c=3^a 2^k-b>2^(a+k). Starting from -c, follow signed T until precisely
a+k even steps have occurred. Write L for that time and -h for its endpoint.
Before and including this stopping event, the magnitude is at least
c/2^(a+k)>1: on magnitudes z>1 an odd step is (3z-1)/2>=z, while an even
step halves. Thus the path cannot reach -1. Each block of odd steps is
finite, because (3z-1)/2-1=3(z-1)/2 consumes one unit of v2(z-1) at each
odd step. Hence every required next even step occurs. Therefore L is finite,
L>=a+k>k, and h>1. No convergence or periodicity assertion about negative
orbits was used.

Use the delayed lower seed -2^k, whose exact length-L word is 0^k1^(L-k)
and whose endpoint is -1. For

    d=2^L u-2^k,

lift both signed templates by the positive parameter u. Their endpoints are

    3^a d+b  --upper word--> 3^(L-k)u-h,
    d         --lower word--> 3^(L-k)u-1.                (5)

For every prefix time i<L, the lifted-versus-signed difference is an even
integer 3^q 2^(L-i)u, with the additional initial factor 3^a on the upper
arm. This proves all prefix parities. At time L the coefficients balance
because the upper word has L-a-k odd steps and the lower has L-k.
Also v2(d)=k exactly, since L>k. Choosing a sufficiently positive ordinary
u makes both starting values positive and hence every actual forward state
positive.

The remaining gap in (5) is h-1. Apply DS-001 with its lower residue B and
modulus M, and impose

    3^(L-k)u-h = B mod M.

Odd invertibility gives one residue for u. After a positive tail shift this
produces a whole progression in d of modulus 2^L M, with all original
parities and the desired merger. The two complete words have equal lengths
and odd counts differing by exactly a, as their coefficients require.

This extends #127's seed k=0 and guard 3^a-b>2^a. The additional delayed
seed is what makes every intercept eligible. It does not assert that a
fixed preassigned d belongs to the newly constructed progression.

### A second finite seed retained by the selector

The lower seed -3*2^k follows 0^k100 to -1, with k+2 even steps. Whenever

    (3^(a+1)-2^(a+2))2^k > b,

start the upper signed arm at -(3^(a+1)2^k-b), and stop after a+k+2 even
steps. The same proof gives a finite L>=k+3 and h>1. Set

    d=2^L u-3*2^k.

The lower word is 0^k1001^(L-k-3), with L-k-2 odd steps. Both endpoint
coefficients become 3^(L-k-2), and their gap is again h-1. All remaining
arguments are identical. The coefficient 3^(a+1)-2^(a+2) is positive for
a>=1, so all sufficiently large k work for this seed too.

A concrete previously ineligible intercept is a=1,b=10. Seed one with k=4
has c=38, L=9, h=5, and produces

    d=16384t+11760,
    T^14(3d+10)=T^14(d)=729t+524, every t>=0,
    words 01001011000001 / 00001111100100.               (6)

The negative word is only a compiler template. It is not an infinite
positive witness, a prescribed future for an arbitrary source, or a proof
of convergence of any negative trajectory.

## DS-003. Every H-parameter valuation has strict original-source families

For H(C)=9C+2, take a=2,b=2. Both delayed-seed guards hold for EVERY k>=0:
5*2^k>2 and 11*2^k>2. Consequently for every exact valuation v2(C)=k,
including every odd valuation, an explicit whole H-merging progression exists.
This extends the earlier 4-adic even-valuation escape families. It does not
claim that every C at that valuation is successful.

These families lift to ORIGINAL sources, with unbounded first odd-run length,
and can keep the entire displayed forward arm above its original source.
Let C=B+Mt be any one such whole H cylinder, with complete upper word w of
length ell. For its j-th prefix let q_j be the odd count, and define the
positive rational number

    gamma = min_(0<=j<=ell) 9*3^q_j/2^j.

Every upper prefix value, as an affine function of C, has this prefix slope
and a positive constant term. Thus it is at least gamma*C.
Choose ANY r>=2 such that

    gamma*3^(r-1) > 8*2^r.                               (7)

All sufficiently large r satisfy (7). CRT imposes

    4C+1=3^(r-1)u, u positive odd,
    2^r u=1 mod3,                                       (8)

inside the dyadic C cylinder. To see compatibility, impose
4C+1=3^(r-1)*(2^r)^(-1) mod3^r; the moduli M and 3^r are coprime.
There are infinitely many positive C obeying it. Set

    n=2^r u-1, m=(n-3)/4.

The hard odd-run entrance and compressed first companion from AR-005 give

    T^(r+2)(n)=H(C), T^r(m)=C, 0<4m<n.

Append the fixed cylinder words:

    T^(r+2+ell)(n)=T^(r+ell)(m).                         (9)

For the strict bound, 3^(r-1)u>=2 and hence
C=(3^(r-1)u-1)/4 >= 3^(r-1)u/8. Equations (7) and (8) give gamma*C>2^r u>n.
The initial odd run strictly increases. The intervening even-step value
(3^r u-1)/2 also exceeds n for r>=2. Thus EVERY positive-time original state
through (9) exceeds n, not just the final state.
Moreover 3|n. An odd pure predecessor of any multiple of three would require
(2n-1)/3 integral; iterated even predecessors remain multiples of three.
So the only pure ancestors are 2^j n, and none is smaller, at any depth.

For every k, and every sufficiently large r depending on its chosen cylinder,
this is an infinite original-source exclusion family. The companion is below
n/4. No convergence assumption was used to construct the certificates;
least-counterexample minimality is used only to interpret their exclusion.

Example at the newly handled odd valuation k=3:

    C=32768t+14584,
    T^15(H(C))=T^15(C)=2187t+974,
    words 010011000010001 / 000111110100100.

A CRT lift with r=16 gives

    n=23855300607, m=5963825151,
    T^33(n)=T^31(m)=87149046638,
    min_(1<=j<=33)T^j(n)=35782950911>n,
    3|n and 4m<n.

Every parameter of this k=3 cylinder fails the parent's initial admission
guards: it is even with valuation at least two, so the old even valuation
bridge does not apply, while the parent's two new R bridges require odd C.

## DS-004. Every prescribed dyadic input cell contains a uniform H merger

For EVERY positive integer C and EVERY precision P>=0, a terminating
construction supplies B>C and M=2^ell such that

    B=C mod2^P, 2^P divides M,
    T^ell(H(B+Mt))=T^ell(B+Mt), every integer t>=0.        (10)

The words and all parameters are explicit, and their first P steps are the
actual first P parities of the fixed pair (H(C),C). In particular every
residue class modulo every power of two contains a whole merger subcell.

### Proof: normalize the actual finite prefix, then compile its intercept

Follow the actual pair for exactly P steps, with words w,z, odd counts q_w,
q_z, and endpoints x,y. For parameter C+2^P t, the SAME physical prefixes
have endpoints

    3^(2+q_w)t+x, 3^q_z t+y.                             (11)

This follows from the affine word formula, since the input perturbations
are 9*2^P t and 2^P t. All intermediate perturbations are even before the
P-th step, so both prefix words remain physical.

If the two exponents in (11) are equal, their gap is constant. If x=y they
already agree uniformly; otherwise DS-001 compiles |x-y|. Its lower-source
congruence is solvable in t because the common coefficient is odd. Choose
t in a positive tail of that residue and append the compiler words.

If the exponents are unequal, let s be the smaller exponent, let a>=1 be
their difference, and write D=3^s t+v for the smaller-coefficient arm.
The other arm is 3^a D+b, with b an arbitrary integer determined by (11).
No sign or size restriction on b can be assumed here. Choose k large enough
for DS-002 and obtain a whole merger progression

    D=d+Kj, K a power of two.

CRT solves d+Kj=v mod3^s, since K is coprime to 3^s. Write
j=j0+3^s h, giving t=t0+Kh. Move j0 along this progression until t0>0.
Both arms are now positive actual continuations of the original prefixes.
Their union of prefix and tail words has length ell=P+log_2 K, and the
resulting original parameters are

    B=C+2^P t0, M=2^P K.

Orient the two appended tail words by coefficient size, while retaining
which original arm each belongs to. This proves (10). Every component
terminates: P is finite, a suitable k exists, DS-002's signed stopping time
is proved finite, DS-001 strictly reduces an integer gap, and CRT is finite.
No ordinary orbit is assumed to converge during this construction.

The same proof works for ANY fixed affine type (3^a C+b,C), a>=0, with both
chosen starting values positive: replace the initial exponent two by a.
Every residue class has such a positive representative even when b<0.
The implemented all-cell corpus specializes this general argument to H.

### Quantifier and comparison boundaries

DS-004 preserves the FIXED H relationship and works inside any prescribed
cell. It is stronger than exhibiting one gate for each named comparison type.
It is distinct from #128's finite-word subfamily theorem, which selects its
own odd-spine companion rather than retaining this fixed H pair.
In 2-adic language, the union of all uniform H-merger cylinders is open and
dense. This does not assert measure one, natural density one, or membership
of every ordinary integer. The construction generally changes C to B>C;
it cannot replace the actual comparison parameter by B in a least-source
argument. Its information about arbitrarily fine neighborhoods must not be
read as a successful selector for their common center.

The next theorem proves that some positive ordinary centers really are
excluded forever from this entire uniform-cylinder language, even though
nearby cells always contain successes.

## DS-005. First-meeting coefficient imbalance is a permanent obstruction

Let the positive pair (H(C),C) have a first synchronous meeting at time L.
Write q_H,q_C for the odd counts on its two actual words through that time.
Then precisely one of the following holds:

* q_C-q_H=2: those finite words already yield a uniform H-merger cylinder
  containing C, by equality of their affine slopes and their equality at C.
* q_C-q_H!=2: NO uniform finite synchronous H-merger cylinder containing C
  exists at ANY depth, not merely through a tested horizon.

Proof. On a common dyadic refinement, a finite word applied to H(C) has
coefficient 9*3^q_H/2^L in C; the lower has 3^q_C/2^L. A uniform identity
requires equality of these coefficients, hence q_C-q_H=2. In the balanced
case, equality at C also forces equality of the constant terms, proving
the entire cylinder. In the unbalanced case there is no earlier meeting by
definition. After the first meeting both actual trajectories are identical,
so future simultaneous odd counts increase equally: their difference never
changes. No later depth can have the required coefficient balance. Any
putative uniform merger progression through C may be refined modulo its
word-length power of two, where the actual words at C are fixed; the same
necessary coefficient condition applies. QED.

For a general affine type (3^a C+b,C), the same criterion is q_C-q_H=a.
The result concerns FIXED finite synchronous word/cylinder certificates.
It does not exclude a progression whose members meet at different unbounded
times, a different original companion, or a different source-clock relation.

Exact examples, checked by literal first-meeting replay:

| C | H(C) | First time | Common value | q_H | q_C | Classification |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 11 | 9 | 2 | 4 | 5 | isolated only |
| 7 | 65 | 18 | 2 | 8 | 9 | isolated only |
| 17 | 155 | 54 | 2 | 30 | 26 | isolated only |
| 71 | 641 | 64 | 2 | 31 | 37 | isolated only |
| 439 | 3953 | 9 | 209 | 3 | 5 | uniform |
| 735 | 6617 | 10 | 524 | 4 | 6 | uniform |

In particular C=17 and 71 are both 2 mod3, the necessary congruence of the
least-counterexample H entrance. These are genuine positive ordinary points,
not merely nonordinary 2-adic completions. Their meeting is not disputed;
the coefficient criterion proves they can NEVER be captured by a finite
uniform H-merger cylinder. The parallel atlas's finite isolated records are
consistent with this all-future distinction.

Applying DS-004 at every P around any of these isolated centers constructs
uniform merger cylinders arbitrarily close to that center, necessarily
excluding the center itself. The corpus includes 16 such explicit
neighborhoods, at four depths around each of C=1,7,17,71.
It also includes a gate inside C=2 mod2^256. The center C=2 never merges
synchronously: (20,2) reaches (2,1) after five common steps and remains in
opposite core phases. That finite identity and deterministic continuation
rule out every later meeting; a putative earlier meeting would persist.
Thus even arbitrarily precise initial agreement cannot silently erase the
fixed-source and clock requirements.

This is a concrete reason a complete H-only selector cannot consist solely
of more finite uniform merger cylinders. A broader approach must retain
individual certificates or valid original-companion/clock changes, or use
an argument that bypasses this fixed-H language altogether. It is not a
claim that the Collatz conjecture is false or that other architectures fail.

## DS-006. The fixed-anchor lemma extends to a finite persistent portfolio

Let A be a finite collection of positive original sources, each reaching 1.
For m in A let tau(m) be its first entry time into {1,2}. Consider a schedule
of observations (m,b) with m in A, b>=0, such that T^b(m)>2 and no ordered
pair (m,b) is charged twice. Then there are at most

    sum_(m in A) tau(m)

such observations. Indeed for each fixed m they require b<tau(m), because
{1,2} is forward invariant. Counting the available finite pairs proves the
bound. This is an elementary finite-resource argument, not a computable
uniform upper estimate for the stopping times of unproved sources.

Under least-counterexample minimality, any portfolio of original companions
below the fixed n is finite and every member reaches 1. Therefore a comparison
procedure whose hypothetical infinite continuation forces infinitely many
FRESH above-core observations from that portfolio is impossible. This extends
AR-001 beyond one fixed companion and permits switching between the finitely
many compressed ladder sources, or even among all sources below fixed n.

The persistent-observation hypothesis matters. Resetting an anchor clock and
reusing the same observation is not fresh. A new smaller companion of a much
larger intermediate state need not be below the original n. Administrative
coordinate swaps are not actual arm-order reversals. The procedure must
prove that its infinite continuation forces these physical observations;
this lemma does not establish escape-completeness or that forcing property
for an arbitrary countable comparison grammar. No universal stopping selector
is supplied by counting the potential original companions alone.

## Executable selector and exact evidence

The continuation uses both delayed seeds, old/new/alternate all-gap gates,
and actual balanced prefixes through at most 12 comparison steps. A prefix
is admitted only when its actual odd-count difference makes the two affine
slopes equal; it then compiles their actual residual gap. Probes stop when
either arm is already in {1,2}. This prevents ordinary core convergence from
being dressed up as a large new structural certificate. The resulting final
words are checked as WHOLE H cylinders, not merely at their sampled C.

When no new gate applies, the exact parent AR/VL transition is retained,
including its swapped orientation, immutable original roots and accumulated
words. A new gate is terminal; otherwise the old route is preserved. This
proves preservation of parent successes, not just their aggregate count.
The generator authenticates the parent's run.py Git blob
`0ba3954be102188790e05cefa3630e3cb0dbccbc` before loading it.

On the SAME complete C=1..65536 range:

| Selected language | Finite merger certificates | C=2 mod3 successes |
| --- | ---: | ---: |
| #125 valuation bridges | 4366 | 1464 |
| #129 R bridges | 5082 | 1704 |
| This continuation | 6677 | 2223 |

There are 1595 new successes over the immediate parent, with no lost
successes; 519 additions lie in C=2 mod3. There remain 58859 OUTSIDE
outcomes and zero BUDGET outcomes. These are exact selected-language
outcomes, NOT convergence counts or percentages of hypothetical counterexamples.
The separate all-cell construction changes the comparison parameter and
is deliberately NOT used as a fake successful fallback on a failed C.

A controlled ablation using the same new selector but only the old all-gap
compiler gives 6559 successes. Retaining the new long-block/alternate gates
adds 118 beyond that. Do not attribute all 1595 additions solely to the
improved exponent, nor compare this bounded selector against the union of
all other project work without running that comparison.

The full deterministic corpus has 78847 rows:

* 12308 whole all-gap cylinders: all g=1..4096 with three compiler modes,
  and 20 additional long-mode cases including gaps above 2^512;
* 426 whole affine-shadow cylinders across a=1..8, signed intercepts up to
  10000, both seeds, and exact H valuations through k=20;
* 42 CRT-lifted original no-forward-descent certificates, including all
  k=0..20 with both seeds;
* six exact first-meeting classifications and 16 nearby cylinders excluding
  their ordinary isolated center;
* 513 prescribed-cell gates: EVERY residue at every precision P=0..8,
  plus C=2 and C=17 at precision 256;
* all 65536 comparison outcomes, including every failure.

Full-row SHA-256:
`13a016ac35da87771b03d047b3e2e9b95575e40c5c121a7f7b0c75055f94cf45`.

Run from repository root:

    python -S -B experiments/paired-comparison/delayed-shadow-compiler/run.py --full /tmp/ds.jsonl --summary /tmp/ds.json
    python -S -B experiments/paired-comparison/delayed-shadow-compiler/verify.py /tmp/ds.jsonl --summary /tmp/ds.json

The generator passed normally and under -O with -S isolation, producing
byte-identical full corpus and summary. The standalone verifier passed
normally and under -OO with -S isolation. It imports no generator or repository
code: it reconstructs signed word endpoints, actual first meetings, full
positive affine identities, source clocks, and strict all-state minima.
It rejects 36 directly altered semantic witness rows in each run, including
boolean-as-integer and parity corruptions. These are direct row mutations,
not separately resealed full-corpus corruption tests. It checks corpus digest
and complete comparison-source uniqueness. It does NOT independently certify
OUTSIDE classification or turn its finite checks into proofs of the universal
lemmas. Same-author implementation diversity is not independent peer review.

No complete-checkout root validator, remote CI, Lean build, or independent
mathematical review was run. Direct Git transport failed DNS; successful Git
data API publication and local packet execution are distinct from those events.
The sharper exponent and all-parameter conclusions rely on the written proofs,
not extrapolation from this finite corpus. DS-006 is a written finite counting
argument, not a tested global comparison policy.

## What remains for the full problem

The all-intercept compiler now accepts the affine type of EVERY finite paired
prefix, and DS-004 shows every initial dyadic cell has a merger subcell. Neither
forces the ACTUAL fixed parameter into a gate. DS-005 gives explicit ordinary
points that permanently evade uniform H certificates even though they merge.
A complete proof therefore needs more than increasingly rich residue catalogs.

A concrete next route is a root-compatible comparison grammar with a persistent
finite anchor portfolio: cover actual escape parameters, permit correctly
certified isolated/unequal-clock exits or original-companion changes, and prove
that any infinite remaining continuation consumes infinitely many fresh
above-core anchor observations. DS-006 would then supply the contradiction
under least-counterexample minimality. Escape-completeness and that progress
property are not established here. The universal results above remain valid
without either of those missing inferences.
