# Large least-root gaps do not force numerical cycle exclusion

Date: 23 November 2026. Local parent:
`cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`.

**Status: exact written obstruction theorem; unrestricted positive integer
cycle exclusion remains OPEN.** This pass attacked the missing step in
the least-root cut test: can one force a positive rotated carry gap
smaller than the full denominator after imposing a large minimum and
first-crossing structure? The answer is no under those geometric and
coefficient hypotheses, even with arbitrarily large fully reduced
numerical denominator. A two-parameter family below proves this at all
thresholds, rather than at one small word.

The family consists of classical rational circuit words. This note does
not claim a new circuit exclusion theorem or historical priority for
their affine formulas. Its role is to test the proposed unrestricted
bridge, retain the exact numerical gcd, and show precisely where the
ordinary source condition does work. No new Lean wrapper is added for
reused carry identities. The theorem and its density argument have
written-proof scope.

## 1. Current sources and attempted closing steps

The source refresh found the following relevant current heads:

| Source | Exact head and file | Inspected claim and boundary |
|---|---|---|
| PR178 | `c91b80a3156e640ad471cf30c47721145ae21eb1`, `research/central-step-20261123/cycles/COMPLEMENTARY_DENOMINATOR_CAPACITY.md`, blob `97c3b1342bad9fbc7b9a1cd3a45aff031e1c124d` | A primitive nontrivial positive integer cycle of length K has complementary reduced denominator greater than K/2, with a stronger continuous envelope. The missing opposite bound on that denominator remains explicit. |
| PR180 | `7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`, `research/profound-step-20261123/ARITHMETIC_CLOSURE.md`, blob `c1fed85a4090ade76f73e23efed6548dc2fcff8d` | The complementary denominator is greater than `3(2p-A)`, retaining the complete complementary numerical gcd. Original integrality has not supplied the required complementary cancellation. |
| PR185 | `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d` | Metadata and current description refreshed: residual polynomial denominator growth still precedes additional numerical gcd cancellation. Earlier exact file reviews remain separately pinned. |
| PR186 | `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493` | Metadata refreshed; earlier deep-machinery scope remains pinned in the preceding local packet. No exception-free S-unit conclusion is imported. |

The preceding [complete cycle note](../whole-repo-round3-20261123/COMPLETE_CYCLE.md)
retains the conditioned-law obstacle, and
[round-four cycle rigidity](../literature-round4-20261123/CYCLE_RIGIDITY.md)
proves the full-denominator cut criterion. For a primitive least-root
word w, with full carry C and positive D, integral closure implies

\[
 C(\operatorname{rot}_i w)-C(w)\in D\mathbb Z_{>0}
 \quad(0<i<A).
 \tag{1}
\]

The intended new bridge would find a cut with gap in `(0,D)`, perhaps
after using a sufficiently large minimum, a near-critical slope, or
first coefficient crossing. Section 3 refutes every fixed-threshold
version using only those hypotheses.

Two other attempts were considered but do not supply a closing theorem:

- The new complementary-denominator lower bounds require an upper bound
  forced by the positive original cycle. No such gcd comparison was
  obtained. The two complete word denominators differ, and rotations
  preserve each denominator separately.
- Christoffel extremality maximizes the rational cycle minimum among
  all words at fixed clocks. Excluding that maximizing word does not
  exclude the smaller minima of other words. No argument was found that
  makes an arbitrary integral candidate attain, or lie in a controlled
  neighborhood of, that extremum.

The latter distinction follows directly from the primary statements:
Halbeisen–Hungerbühler, Lemma 5 and Corollary 1, give the balanced
extremizer; Fernández–Ibáñez, Theorem 7.3 and Section 9, state the
unique extremality and the remaining suboptimal patterns. Knight's
published abstract and Sections 4–5 identify the high-cycle restriction.
These are distinct from an all-word integrality theorem.

Primary sources inspected:

- [Halbeisen and Hungerbühler, *Optimal bounds for the length of rational Collatz cycles*](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf), Sections 2–3, Lemmas 1–2 and 5.
- [Fernández and Ibáñez, *Christoffel Words as Extremal Structures in Collatz Dynamics*, arXiv:2607.24844v1](https://arxiv.org/html/2607.24844v1), Sections 5–9, especially Theorem 7.3. This is a 2026 preprint; its full proof is not newly audited here.
- [Knight, *Collatz high cycles do not exist*, Discrete Mathematics 349 (2026), 114812](https://www.sciencedirect.com/science/article/pii/S0012365X25004200), DOI `10.1016/j.disc.2025.114812`. The publisher's abstract and available section previews were read. The HAL full-text endpoint presented an access challenge; no successful HAL full-text read or new audit of the paper is claimed.

## 2. An exact circuit calculation with the full gcd

Let `p>=2`, `h>=1`, `A=p+h`, and consider the chronological shortcut
word

\[
 w=1^p0^h,\qquad D=2^{p+h}-3^p>0,\qquad C=3^p-2^p.
 \tag{2}
\]

Its rational fixed point at the start of the odd run is

\[
 m=\frac C D,
 \qquad m+1=\frac{2^p(2^h-1)}D.
 \tag{3}
\]

The identity for C follows by summing the complete ordered carry. The
states during the odd run and the subsequent even run are exactly

\[
 x_i=(3/2)^i(m+1)-1\quad(0\le i\le p),
 \qquad x_{p+j}=2^{h-j}m\quad(0\le j\le h).
 \tag{4}
\]

These are legal rational Collatz states, not just real affine branches.
The denominator D is odd. For `i<p`, substitution of (3) writes x_i
with numerator

\[
 3^i2^{p-i}(2^h-1)-D,
\]

which is odd. At `i=p`, its numerator is `2^h C`, with exact binary
valuation h since C is odd. The following h halvings therefore have
exactly the indicated parity, returning to the odd initial state.
Cancelling a common odd gcd does not change any of these parities.

The word is primitive: a cyclic repetition of a shorter mixed word
would have more than the two symbol changes of `1^p0^h`. A shorter
state period would give a shorter parity period, so all A states are
distinct.

Assume now `m>1`. The odd-run states strictly increase; all proper
even-run states are at least `2m`. Since `(3m+1)/2<2m`, the unique
least state is m, and the least gap to any other state is exactly

\[
 \boxed{\min_{0<i<A}(x_i-m)=\frac{m+1}{2}.}
 \tag{5}
\]

Equivalently, the least proper rotated carry gap is

\[
 \boxed{\min_{0<i<A}\{C(\operatorname{rot}_i w)-C\}
       =\frac{C+D}{2}=2^{p-1}(2^h-1).}
 \tag{6}
\]

Every term here is a complete carry; no block denominator replaces D.

The fully reduced numerical denominator is

\[
 q=\frac{D}{g},\qquad
 g=\gcd(D,C)=\gcd(D,2^h-1).
 \tag{7}
\]

Indeed `D+C=2^p(2^h-1)`, and D is coprime to two. This is an equality
for the full integer gcd, with every prime power retained. In particular,

\[
 q\ge\frac{D}{2^h-1}>\frac D{2^h}.
 \tag{8}
\]

Write `R=2^A/3^p`. Then

\[
 m=\frac{1-(2/3)^p}{R-1},\qquad
 \boxed{q>2^p\frac{R-1}{R}.}
 \tag{9}
\]

## 3. All-threshold obstruction theorem

**Theorem.** For every pair of positive integers B,Q, there exists a
primitive positive rational Collatz cycle, with chronological least-root
word `1^p0^(A-p)`, such that:

1. Every state is greater than B.
2. Every proper least-root state gap is greater than B; equivalently,
   every proper least-root carry gap is greater than `B*D`.
3. Its fully reduced numerical denominator is greater than Q.
4. Every nonempty proper prefix has multiplicative coefficient greater
   than one, while the complete word has coefficient less than one.
5. Its slope `A/p` can be arbitrarily close to `log_2(3)` from above.

Thus large floors, near-critical clocks, primitivity and first coefficient
crossing do not force a root gap below D. The examples are proved
nonintegral by (3), not merely labelled rational without a gcd check.

**Proof.** Set `epsilon=1/(16B)`. The irrationality of `log_2(3)` and
density of irrational rotations give arbitrarily large p such that,
with `A=ceil(p log_2(3))`,

\[
 1+\varepsilon<R=2^A/3^p<1+2\varepsilon.
 \tag{10}
\]

This requires the fractional part of `p log_2(3)` to lie in the
nonempty interval

\[
 \left(1-\log_2(1+2\varepsilon),\,
       1-\log_2(1+\varepsilon)\right).
\]

Choose such p large enough that `(2/3)^p<1/2` and
`2^p epsilon/(1+2epsilon)>Q`. Equations (5) and (9) give

\[
 m>\frac1{4\varepsilon}=4B,
 \qquad\frac{m+1}{2}>2B,
 \qquad q>\frac{2^p\varepsilon}{1+2\varepsilon}>Q.
 \tag{11}
\]

In particular q>1, so the cycle is nonintegral. Its legal rational
realization and primitivity were proved in Section 2.

During a nonempty odd prefix, the coefficient is `(3/2)^i>1`.
After p odd steps and `j<h` even steps, it is `2^(h-j)/R>1`, because
`R<1+2epsilon<2`. The complete coefficient is `1/R<1`. This proves
the first-crossing statement. Finally

\[
 0<\frac A p-\log_2(3)=\frac{\log_2 R}{p}
   <\frac{\log_2(1+2\varepsilon)}p\longrightarrow0
 \tag{12}
\]

along the arbitrarily large choices of p. This proves all five claims.
No unbounded-partial-quotient conjecture for `log_2(3)` is used: epsilon
is fixed before p is sent to infinity. \(\square\)

For completeness, irrational-rotation density here is elementary. By
pigeonhole there are nonzero integer multiples with distance to an
integer as small as desired. Positive multiples of such a multiple
trace either an increasing or decreasing mesh of arbitrarily small
spacing around the circle. Every nonempty interval is met. Every tail
of the orbit is a translate of the same dense orbit, so it is met at
arbitrarily large indices. The irrationality follows from unique prime
factorization: `log_2(3)=a/b` would give `2^a=3^b`.

## 4. Where the ordinary integer condition actually enters

The examples retain positivity, a large minimum and all proper-prefix
coefficient inequalities. They fail the full integer grid condition.
The precise reason is visible without guessing a small root gap.

Any positive ordinary integer realizing the first p odd inputs must
satisfy

\[
 n\equiv-1\pmod{2^p},\qquad n\ge2^p-1.
 \tag{13}
\]

This follows by iterating `2(x_{i+1}+1)=3(x_i+1)` through those p odd
inputs and cancelling powers of three. If `D>2^h-1`, (3) instead gives

\[
 m+1=\frac{2^p(2^h-1)}D<2^p.
 \tag{14}
\]

Thus every ordinary realizer starts strictly above the rational fixed
point. Its complete affine return is

\[
 T_w(n)=m+\frac1R(n-m)<n.
 \tag{15}
\]

The large-p choices in Section 3 can also be required to satisfy
`D/2^h>Q>=1`, so (14) applies to the whole chosen family. Every finite
ordinary realizer therefore makes a genuine descent over this word,
even though the associated rational least-root cycle has arbitrarily
large positive gaps. Finite ordinary realizers exist in the usual
complete parity cylinder; no single ordinary source realizes the
periodic word forever.

For arbitrary parameters, an integral circuit fixed point would have
to obey the sharper exact identity

\[
 \frac{2^h-1}{D}\in\mathbb Z_{>0},
 \qquad m=2^p\frac{2^h-1}{D}-1.
 \tag{16}
\]

Section 3 selects parameters where this is impossible. This elementary
subfamily exclusion is not a replacement for the classical complete
circuit theorem, and neither extends here to arbitrary words.

The attempted generalization is the old first-crossing target in a
concrete form: compare the least ordinary source of the complete word
with its rational fixed point. For a general word, the long odd-run
congruence (13) is unavailable, and the complete source residue remains
coupled to the ordered carry. No all-word lower bound that beats that
fixed point was obtained.

## 5. Exact controls and scope

All numerical displays below were reconstructed with Python integers,
`Fraction`, and the full numerical gcd. Decimal values are orientation
only; the floor, gap and denominator comparisons use integer cross
multiplication.

| B | Q | p | A | Fully reduced denominator bit length | Least state, approximately | Least root gap, approximately |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 100 | 41 | 65 | 59 | 86.73890135 | 43.86945068 |
| 100 | 1,000,000 | 306 | 485 | 476 | 977.74477254 | 489.37238627 |
| 1,000 | 1,000,000,000 | 14,271 | 22,619 | 22,606 | 9477.92057679 | 4739.46028840 |
| 10,000 | 1,000,000,000,000 | 47,468 | 75,235 | 75,219 | 91493.70028957 | 45747.35014478 |

For the first row the exact values are

\[
 D=420491770248316829,\quad
 C=36472994178147530851,\quad \gcd(D,C)=1,
\]

\[
 m=\frac{36472994178147530851}{420491770248316829},\qquad
 \min_i(x_i-m)=
 \frac{18446742974197923840}{420491770248316829}.
\]

All four displayed gcds are one, but that empirical observation is
not used in the all-threshold theorem; the theorem retains the exact
possibly nontrivial gcd through (7)–(9). The long rows do not claim a
fresh replay of every rotated full carry or a search for integer cycles.
Their role is to check the displayed closed-form controls. A separate
bounded replay was executed for `2<=p<=24`, `1<=h<=24`, retaining
the 22 cases with `D>0` and `m>1`. It checked all 482 literal rational
edges and all 482 rotated complete carries, primitivity, the exact
minimum gap, the full gcd identity, and every proper-prefix coefficient.
Whenever `D>2^h-1`, it also constructed the least positive ordinary
source residue modulo `2^A`, replayed the literal integer branches, and
checked the strict descent. All checks passed with exact arithmetic.
This author execution is not a parent replay or a universal proof by
census; the parent publication record states its separately executed
checks.

**Outcome.** The hoped-for unrestricted small-gap bridge fails even
after arbitrary floor and denominator thresholds and exact first-crossing
conditions are imposed. The missing successful implication must use the
ordinary source grid substantively, or a different global arithmetic
constraint. No full positive-cycle exclusion, universal denominator
selector, or improved count of unrestricted integer cycles was proved.
