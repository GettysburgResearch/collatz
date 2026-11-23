# Minimum cycle roots, numerical carry gaps, and the cycle-lemma limit

Date: 2026-11-23. Baseline: `a7fd3ac9e5bff7412858df23d776bb847e9c1371`.

**Status: finite arithmetic proved in Lean; written reductions proposed for
scoped independent review. No unrestricted integer-cycle exclusion is proved.**
The five public statements in `CycleRigidity.lean` retain the complete
chronological carry and the full numerical denominator. The development
compile used Lean 4.34.1 with warnings as errors. A separate parent replay
and axiom audit are not claimed as this author's execution.

This attempt connects minimum-root selection with the cycle lemma and
first-passage methods. Its positive output is an exact cut certificate:
at the least state of a primitive integral cycle, every distinct rotated
carry has a positive gap of at least the full denominator. Its closing
attempt fails at a precise counting step. Selecting the unique minimum
rotation leaves the proportion of integral words exactly unchanged.
Counting that selection as a further independent rare event would pay the
same necklace factor twice.

## 1. Literature read and scope

The primary sources that guided this attempt were read directly:

| Source | Passage inspected and use here |
|---|---|
| [Halbeisen and Hungerbühler, *Optimal bounds for the length of rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf) | Sections 2–3, including the complete carry and minimum-rotation comparison; p.238, equations (13)–(15), Lemma 9, and the final integer-cycle reformulation. This is the classical rotation/gcd backbone. In particular, the gcd of all rotated carries is already identified there. No novelty is claimed for that identity or the rational-cycle formula. |
| [Dershowitz and Zaks, *Patterns in Trees*, MIT preliminary manuscript (1984)](https://groups.csail.mit.edu/tds/papers/Zaks/TM-271.pdf) | Section 3, pp.5–6, states the Dvoretzky–Motzkin cycle lemma for integer step types. It motivates choosing a canonical cyclic root. Its exact number of dominating rotations is not imported for the incommensurable logarithmic increments used below. |
| [Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F) | Propositions 1.9, 1.11 and 1.14 and their stated input laws. They distinguish first-passage estimates for specified logarithmic input distributions from a measure conditioned on an exact integer cycle. No probability estimate from that paper is applied to the latter measure here. |
| [De Jesús, *Realizer Bounds and Repetition Constraints at the First Coefficient Crossing in the 3x+1 Problem*, 14 November 2026, v2](https://hexagonmath.org/pdf/2611.00459) | Sections 1–2 and 7: the first-crossing realizer threshold and its explicit attribution to Terras/Lagarias, and the remaining least-realizer inequality. This prevents rebranding that existing open inequality as a new cycle argument. Its quantitative computational or logarithmic-form results are not imported. |
| [Lyapunov Weaver and Fourier Wren, *Effective equidistribution and path laws for long Collatz excursions*, Paper 87, 2 November 2026, v1](https://rstation.ai/problems/collatz/papers/87) | Sections 1–3, especially (5b) and Corollary 2, and the stated proof boundaries. The comparison in Section 7 below uses the theorem's displayed conductor window, not an independent audit of its long proof. This is a working manuscript. |

The local carry convention is pinned by
[`CycleWordAlgebra.lean`](../high-variance-20261123/CycleWordAlgebra.lean),
SHA-256 `fc42bf2a602592c7f7ebbe42ca3c21bb96b58f7ce2dc93aed2cafdbac47f984e`.
The finite proof also imports the earlier complete-denominator coprimality
lemma from [`CycleCancellation.lean`](../closure-round2-20261123/CycleCancellation.lean)
and the fixed-clock carry decoder from
[`CarryFibers.lean`](../whole-repo-round3-20261123/CarryFibers.lean).
The earlier zero-fibre and polynomial minimum-census targets remain those
pinned in [`COMPLETE_CYCLE.md`](../whole-repo-round3-20261123/COMPLETE_CYCLE.md).

## 2. Full-word convention and the least root

Let w be a chronological binary shortcut word of length A and weight p,
with

\[
1\le p<A,\qquad D=2^A-3^p>0.
\tag{1}
\]

The carry C(w) satisfies

\[
T_w(x)=\frac{3^p x+C(w)}{2^A},\qquad
C(uv)=3^{\#1(v)}C(u)+2^{|u|}C(v).
\tag{2}
\]

Write w_i for the rotation starting at position i, and C_i=C(w_i).
All rotations have the **same full D**, and their rational cycle states
are x_i=C_i/D. The usual odd-denominator parity convention gives actual
rational Collatz steps: the head-carry parity is its first bit, and

\[
2C_{i+1}=3^{w_i(0)}C_i+w_i(0)D.
\tag{3}
\]

In particular, D divides C_0 if and only if these are ordinary integer
cycle states. This is an equivalence for the full denominator, including
every prime power; testing one proper divisor of D would not suffice.

A word is *primitive* here if no proper cyclic rotation equals it.
At fixed length and weight, the carry decodes the whole word, as proved
in `CarryFibers.word_eq_of_length_ones_carry`. Thus all A rotated carries
of a primitive word are distinct. There is exactly one rotation whose
carry is smallest. Call this the **least root**. It is the least physical
state of the rational cycle because D>0. The least state is odd: an even
positive state would immediately halve to a smaller cycle state.

This choice uses the complete carries. It is not defined by a coefficient
walk, a lexicographic order, or a selected local block.

## 3. Exact cut determinant and integral gap

Cut w=uv and put

\[
a=|u|,\quad b=|v|,\quad r=\#1(u),\quad s=\#1(v),
\qquad d_u=2^a-3^r,\quad d_v=2^b-3^s.
\]

The block denominators d_u,d_v may have either sign. They are not used in
place of the full D=2^{a+b}-3^{r+s}. Direct expansion of (2) gives

\[
\boxed{C(vu)-C(uv)=d_v C(u)-d_u C(v).}
\tag{4}
\]

The same expansion gives the complete transport identity

\[
\boxed{2^a C(vu)=3^r C(uv)+D C(u).}
\tag{5}
\]

Since D is odd, (5) proves that D dividing C(uv) also divides C(vu).
No prime of D is discarded. The positivity and positive-weight
hypotheses in (1) derive the needed coprimality with two; it is not an
independent arithmetic assumption.

Suppose now that uv is the least root of a primitive word and that
0<a<A. Distinct-word carry decoding makes the left side of (4) strictly
positive. If the cycle is integral, it is a positive multiple of D, so

\[
\boxed{d_v C(u)-d_u C(v)\ge D.}
\tag{6}
\]

At a cut whose source and endpoint are both odd, their distinct ordinary
integer values differ by at least two, giving the stronger written
consequence that the left side is at least 2D. The Lean consumer proves
the D bound; it does not encode this odd-endpoint refinement.

Consequently, finding any proper cut at the least root with

\[
0<d_v C(u)-d_u C(v)<D
\tag{7}
\]

is an exact full-denominator exclusion certificate for that word.
This applies to arbitrary complete words. It is not a template
assumption, a norm test, or a numerical tolerance test.

## 4. The coefficient barrier that every least root satisfies

For every nonempty suffix v of a positive least-root word,

\[
\boxed{2^{|v|}>3^{\#1(v)}.}
\tag{8}
\]

One proof stays in ordinary cycle coordinates. If x_0 is the least
positive rational state and x_a is the state at the cut, then

\[
2^b x_0=3^s x_a+C(v),\qquad x_a\ge x_0>0.
\]

If v has an odd bit, its carry is positive and the strict inequality in
(8) follows. If it has no odd bit, b>0 and (8) is immediate. The Lean
proof derives the same result directly from the complete carry formulas,
without supplying rational states as extra hypotheses.

Equivalently, put

\[
\delta_i=i\log2-\#1(w_{[0,i)})\log3,
\qquad \delta_A=\log(2^A/3^p)>0.
\]

Then every proper prefix from the least root obeys

\[
\delta_i<\delta_A.
\tag{9}
\]

Thus the coefficient-defect path ends strictly above all of its proper
prefixes. Reversing the increments gives a strictly positive-prefix
walk. This is the actual connection to cyclic ballot and renewal ideas.
It is a necessary property of **rational** least roots already; no
integrality has entered (8) or (9).

If the first positive coefficient deficit occurs at a proper prefix u,
then both d_u and d_v are positive. For an integer cycle minimum n,
the complete prefix identity also gives

\[
n\le C(u)/d_u.
\tag{10}
\]

Trying to exclude every eligible integer realizer of such a
first-crossing word by the opposite strict inequality is the existing
coefficient stopping-time problem. The first-crossing d_u in (10) is
explicitly a block denominator; it does not replace D in (4)–(7).

## 5. Two exact controls

### 5.1 A ballot root need not be the least physical root

For

\[
w=1110010,\quad A=7,\quad p=4,\quad D=47,
\]

the chronological rotated carries are

\[
(89,157,259,412,206,103,178).
\tag{11}
\]

The least rational state is 89/47. The first coefficient crossing is at
the proper prefix u=11100. For v=10,

\[
C(u)=19,\quad d_u=5,\quad C(v)=1,\quad d_v=1,
\qquad C(vu)-C(uv)=19-5=14<47.
\]

This verifies the full-D rejection (7). The word is primitive, because
its length is prime and it is not constant. It is a positive rational
cycle, **not** an ordinary integer cycle.

Both 1110010 and its cut-5 rotation 1011100 satisfy (8) for every
nonempty suffix, even though the latter has the larger state 103/47.
Thus the coefficient barrier does not select the least physical state.

There is also a small exact counting check at these clocks. All 35
length-7 weight-4 words are primitive. There are five least roots and
seven words satisfying (8). Every least root satisfies (8), so under
the uniform word law

\[
\mathbb P((8))=1/5,\qquad
\mathbb P((8)\mid\text{least root})=1.
\tag{12}
\]

The seven-word set contains the five roots with carries
65,73,85,89,101 and the two additional words 1011100 and 1011010,
with carries 103 and 119. Multiplying the two unconditional rarity
factors would already be incorrect before imposing integrality.

### 5.2 Large root gaps do not establish integrality

For the primitive balanced word w=11011010,

\[
A=8,\quad p=5,\quad D=13,
\qquad (C_i)=(319,485,734,367,557,842,421,638).
\tag{13}
\]

Its least positive root gap is 367−319=48>D. Every proper cut therefore
passes the coarse necessary inequality (6). Nevertheless
gcd(319,13)=1, so the cycle is nonintegral and its reduced denominator
is the full 13. The strict grid condition “every gap is a multiple of
D” has not been replaced by a lower bound on the sizes of those gaps.

These controls are finite exact integer calculations. The Lean file
includes the first control's carry values, denominator, and nondivisibility;
the complete rotation lists and counts above are written finite controls
for independent replay.

## 6. Exact obstruction to multiplying ballot rarity into the zero fibre

Fix A,p satisfying (1), and let W be the set of primitive words at those
clocks. Define

\[
Z=\{w\in W:D\mid C(w)\},\qquad
R=\{w\in W:w\text{ is its least root}\}.
\]

Each rotation orbit in W has exactly A elements. The set Z is
rotation-invariant by (5), and each orbit contains exactly one element
of R. Hence, without any independence hypothesis,

\[
\boxed{|W|=A|R|,\qquad |Z|=A|Z\cap R|.}
\tag{14}
\]

Whenever W is nonempty, this gives

\[
\boxed{\frac{|Z\cap R|}{|R|}=\frac{|Z|}{|W|}.}
\tag{15}
\]

If Z is nonempty, the conditional chance of being the least root given
integrality is exactly 1/A. If Z is empty, that conditional probability
is undefined; the cardinal equalities (14) still hold. No existence of
a hypothetical nontrivial integer cycle is assumed in this counting
argument.

In particular, choosing one root per primitive necklace has not improved
the *proportion* of integral candidates. The familiar factor A in the
full zero-fibre target has simply been quotiented out. A further
Bernoulli exponential tilt depending only on the two clocks assigns
the same weight to every word in W and leaves (14)–(15) unchanged.
More generally, rotation-invariant word weights give the same identities
for weighted masses. A non-invariant tilt would require a new comparison
of the actual weights; none is available here.

Let B be the suffix-barrier event (8). We have R subset B. Thus its
conditional probability on R is one. An unconditioned ballot bound for
B cannot be multiplied by a further 1/A root factor or by an assumed
independent zero-residue probability. **That multiplication is the first
unsupported inference in this proposed closing route.**

There is an additional exact dependence among the arithmetic gap tests.
If the rotated carries are indexed cyclically, set

\[
G=\gcd\{C_i-C_0:0\le i<A\},
\]

with signed differences interpreted through their nonnegative gcd.
Then

\[
\boxed{G=\gcd(D,C_0).}
\tag{16}
\]

To see the reverse divisibility, G divides every difference from C_0.
There is an even step because p<A, and its relation C_i=2C_{i+1}
implies G divides C_0 and then every C_i. An odd step in (3) gives
G dividing D. Conversely, h=gcd(D,C_0) is odd; (3) propagates h
dividing every C_i, and hence every difference. This proves (16),
including repeated words. It is an elementary gap version of the
classical rotated-carry gcd identity in Halbeisen–Hungerbühler,
Lemma 9; it is not an external novelty claim.

Thus imposing **all** exact full-D root-gap congruences recovers the
original numerical cancellation condition. They are useful certificates
and coordinates, but not independent arithmetic savings.

## 7. Why the available source-equidistribution window does not finish it

The first-passage literature offers a more serious possible alternative:
control the ordinary source representatives of surviving words directly.
However, the stated window in Paper 87 does not supply the estimate
required by the present attempt. This comparison is a diagnosis of this
application, not a theorem excluding every future use of that paper.

Even granting a polynomial candidate bound n<=k^B for a fixed B, a
length-k parity cylinder places that ordinary source in a normalized
interval of width k^B/2^k. Resolving such intervals by the usual Fourier
discrepancy route requires frequencies of order 2^k/k^B. At that scale
the paper's conductor gap is only

\[
\Gamma_k=k-\log_2|b|=O(\log k),
\]

so Gamma_k/(1+log k) need not tend to infinity. Its displayed moving-window
decay therefore does not yield vanishing discrepancy at this scale,
let alone an error smaller than one candidate. No asserted uniformity
under conditioning on D dividing C is present either. Replacing the
least ordinary source by a fresh uniform residue at a smaller modulus
would lose the exact question.

The earlier polynomial minimum census is already stronger than a raw
exponential ballot count of all words. This note supplies no improved
unrestricted numerical bound for that census and no bound |Z|<A.

## 8. Formal scope and remaining step

`CycleRigidity.lean` proves five public statements:

| Statement | Exact scope |
|---|---|
| `cut_determinant` | Signed identity (4) for arbitrary complete blocks. |
| `rotation_transport` | Natural-number identity (5), with this word's positive full denominator. |
| `full_denominator_rotation_dvd` | Full-D divisibility survives the supplied cut; coprimality is derived. |
| `least_rotation_full_denominator_gap` | The D lower bound in (6), assuming the complete carry is no larger than this rotation and that the rotated words differ. Distinct carries are derived from the earlier decoder. |
| `least_rotation_suffix_contracts` | Necessary coefficient barrier (8), for arbitrary positive rational least-root words. |

The module does not construct the finite necklace quotient, formalize
the logarithmic path, prove (16), import a probabilistic theorem, or
assert universal nonintegrality. Those portions are written arguments.

For the attempted cycle-lemma attack to close the problem, one still
needs a new estimate or arithmetic obstruction on the **same primitive
least-root set**, proving that its full-D zero subset is empty outside
the trivial cycle. Neither minimum-root rarity, the suffix barrier,
the joint root-gap reformulation, nor the cited source-law window proves
that statement. The numerical condition remains intact throughout.
