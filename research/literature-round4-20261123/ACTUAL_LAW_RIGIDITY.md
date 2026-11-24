# Exact local randomness and persistent collisions on ordinary finite orbits

Date: 2026-11-23.

**Status: written finite arithmetic theorem; twelve Lean finite statements
development-compiled with warnings treated as errors.**
This is a constructive obstruction to an entropy-to-collision transfer that
forgets the original source. The examples are genuine positive ordinary
Collatz segments, with exact removed powers of two and uniform weights on
distinct actual states. They are not claimed to be escaping orbits or to carry
the canonical harmonic weights of a hypothetical escaping component.

The main result combines three controls that can otherwise look incompatible:

* every prescribed finite gap-block law is exactly a chosen Bernoulli product;
* every deep ternary endpoint law has collision at least the reciprocal of one
  fixed script period, even with arbitrarily many distinct sampled states;
* all prefix multipliers expand from the same starting state, every window has
  a linear normalized-carry bound, and the necessary source size is explicit.

The source changes with the requested horizon. An exact divisibility estimate
proves that this change is necessary. No same-source collision upper estimate
or Collatz closure is obtained.

## 1. What the literature does and does not supply

Hochman's entropy inverse theorem, Theorem 2.7 of
[On self-similar sets with overlaps and inverse theorems for entropy](https://annals.math.princeton.edu/wp-content/uploads/annals-v180-n2-p07-p.pdf),
concerns the convolution of two probability measures. Its small entropy-growth
conclusion constrains their components at many scales. Applying it to an
arithmetic decomposition requires a convolution law, or a proved quantitative
comparison with that law. Marginal block entropies alone do not establish the
independence implicit in convolution.

Eberhard and Varjú's
[Mixing time of the Chung--Diaconis--Graham random process](https://arxiv.org/html/2003.08117v2)
starts with the recursion `X_(n+1)=a X_n+b_n`, where the innovations are iid.
Its Theorem 1.1 gives an entropy-governed mixing result for almost all admissible
moduli. Neither iid innovations nor a conclusion for the specific sparse
sequence of moduli `3^m` can be inferred merely from that theorem for an actual
Collatz time law. These are two separate hypothesis checks.

The combinatorial ingredient used here is an Eulerian de Bruijn cycle. A
primary account is Moreno,
[De Bruijn sequences and De Bruijn graphs for a general language](https://repositorio.uchile.cl/bitstream/handle/2250/124628/Moreno_E.pdf),
Lemma 4. We give the elementary full-alphabet construction below. The new
deduction in this note is its exact realization by ordinary trajectories,
together with the phase-collision, source-height, and carry-box accounting.

## 2. Conventions and finite carry identities

Use the odd map

\[
 U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

A chronological gap word `w=(g_0,...,g_(h-1))` has positive integer entries,
prefix clock `a_i=sum_(s<i) g_s`, total `A=a_h`, and complete carry

\[
 C(w)=\sum_{i=0}^{h-1}3^{h-1-i}2^{a_i}.
 \tag{1}
\]

An actual realization `q_0,...,q_h` satisfies

\[
 3q_i+1=2^{g_i}q_{i+1},\qquad
 2^{a_i}q_i=3^i q_0+C(g_0,...,g_{i-1}).
 \tag{2}
\]

There is no omitted affine correction in (1)--(2). Concatenation gives

\[
 C(uv)=3^{|v|}C(u)+2^{\sum u}C(v).
 \tag{3}
\]

For a nonempty periodic gap template `v` of length `d`, write

\[
 A_v=\sum v,\qquad \Delta=3^d-2^{A_v}.
\]

We will require `2^(A_v)<3^d`, so `Delta` is a positive odd integer prime to
three. Let `b_j=C(rot_j(v))`, with the rotation starting at phase `j mod d`.
The exact rotation identity is

\[
 \boxed{3b_j=\Delta+2^{g_j}b_{j+1}.}
 \tag{4}
\]

Indeed, writing `v=(g)::u`, its two carries are
`C(v)=3^|u|+2^g C(u)` and `C(ug)=3 C(u)+2^(sum u)`; substitution proves (4).
Thus `z_j=-b_j/Delta` is a periodic negative rational orbit for this script.
This signed rational orbit is an accounting object. All trajectories we
construct below are positive integers.

## 3. Phase locking and its necessary ordinary-source cost

Suppose one actual positive trajectory follows the periodic script for `T`
odd steps. Combining (2) and (4) gives

\[
 2^{g_j}(\Delta q_{j+1}+b_{j+1})
       =3(\Delta q_j+b_j),
\]

and hence, with `p=q_0`,

\[
 \boxed{2^{a_j}(\Delta q_j+b_j)
       =3^j(\Delta p+b_0)\qquad(0\le j\le T).}
 \tag{5}
\]

The powers of two and three are coprime. Therefore both divisibilities hold:

\[
 \boxed{3^j\mid\Delta q_j+b_j,\qquad
        2^{a_j}\mid\Delta p+b_0.}
 \tag{6}
\]

As `Delta` is invertible modulo every `3^m`, the first proves the exact phase
lock

\[
 q_j\equiv-b_j\Delta^{-1}\pmod{3^m}\qquad(j\ge m).
 \tag{7}
\]

In particular equal phases give equal endpoint residues. Positivity in the
second divisibility proves the source-height lower bound

\[
 \boxed{2^{a_T}\le\Delta p+b_0,
 \qquad p\ge\frac{2^{a_T}-b_0}{\Delta}.}
 \tag{8}
\]

Consequently a fixed positive integer `p` cannot follow this periodic template
for arbitrarily many steps: `a_T>=T` while the right side of the first
inequality is fixed. This argument does not assume the absence of other
positive cycles. It shows exactly which height is spent by the finite
construction.

## 4. A positive ordinary realization with a quantitative source bound

Every finite positive gap word `w` of length `T` and total clock `A_T` has one
odd source class modulo `2^(A_T+1)` realizing it exactly. Explicitly choose

\[
 p\equiv (2^{A_T}-C(w))(3^T)^{-1}\pmod{2^{A_T+1}}.
 \tag{9}
\]

Then the final affine quotient in (2) is odd. Each intermediate quotient is
also an integer: split (3) at that position and cancel the odd power of three
from the resulting divisibility by `2^(a_i)`. The same split shows it is odd:
the nonempty remaining carry is odd and its remaining total clock is positive.
All quotients are positive because `p>0` and the prefix carries are nonnegative.
The edge equation and oddness of its output make each prescribed `g_i` the
**exact** valuation `v_2(3q_i+1)`, not just a lower bound.

Impose also `p=1 mod 3`. The Chinese remainder theorem gives one class modulo

\[
 Q_T=3\,2^{A_T+1}.
 \tag{10}
\]

The initial source and every later odd state are now prime to three. To ensure
all `T+1` states are distinct, retain the source rather than assuming that an
arbitrary prescribed finite word avoids a cycle. For distinct indices `i,j`,
the rational affine functions

\[
 q_i(p)=\frac{3^i p+C(w_{<i})}{2^{a_i}}
\]

have different slopes, since equality would require a positive power of three
to equal a power of two. Their equality excludes at most one value of `p`.
There are `B_T=T(T+1)/2` index pairs. Among `B_T+1` consecutive admissible
lifts above any integer floor `H>=1`, at least one avoids every equality.
This is an explicit finite search using exact integer recurrences, with bound

\[
 \boxed{H\le p<H+(B_T+1)3\,2^{A_T+1}.}
 \tag{11}
\]

For a fixed periodic template, (8) and (11) give a matching leading source
bit cost `A_T`, up to constants depending on the period and an `O(log T)`
upper overhead (and the chosen floor `H`). The upper statement is equivalently
`log_2 p <= max(log_2 H,A_T+O(log(T+1)))+O(1)`; it is not a sum of two
independently necessary bit costs.

## 5. Exact finite Bernoulli statistics

Let `P` be a finitely supported rational probability on positive gaps,

\[
 P(g)=c_g/B,\quad c_g\in\mathbb N,\quad\sum_g c_g=B,
 \qquad \beta=\sum_g gP(g)<\log_2 3.
 \tag{12}
\]

Assume `B>=2` and a nondegenerate distribution. Fix a testing depth `L>=1`.
Take a labelled alphabet of size `B` and a cyclic de Bruijn word of order `L`.
Its period is `d=B^L`, and each labelled length-`L` word appears once.
Existence follows by taking an Euler circuit in the directed graph whose
vertices are length-`L-1` words and whose edges are length-`L` words. All
vertices have indegree and outdegree `B`, and the graph is strongly connected.
The case `L=1` is just the list of labels.

Map exactly `c_g` labels to the gap `g`. The resulting cyclic gap word `v`
satisfies, for every `1<=ell<=L`,

\[
 \frac{\#\{j\bmod d:(g_j,...,g_{j+\ell-1})=u\}}d
       =\prod_{i=0}^{\ell-1}P(u_i).
 \tag{13}
\]

The count is `B^(L-ell) product_i c_(u_i)`. In particular
`A_v/d=beta`, so `Delta>0`. Cyclic rotation preserves (13).

Rotate `v` at a largest prefix ratio `2^(a_i)/3^i`, for `0<=i<d`.
For the rotated word put

\[
 R_j=2^{a_j}/3^j,\quad\rho=R_d<1.
\]

Every `R_j<=1`: within the original end this follows from maximality, and
across the end the extra factor is `rho<1`. Repetition gives
`R_(kd+r)=rho^k R_r<=1`. Thus every positive realization satisfies `q_j>=p`.
Define the finite, explicit period constant

\[
 K_v=\left(\min_{0\le r<d}R_r\right)^{-1}\ge1.
 \tag{14}
\]

For all `i>=f`, `R_i/R_f<=K_v`. This depends on the template, not the eventual
precision, number of repetitions, or large source.

## 6. The actual finite-orbit theorem

**Theorem.** Fix `P,L,v,d,K_v` as above. For every precision `m>=1`, every
positive multiple `N` of `d`, and every floor `H>=1`, put

\[
 J=\max(m,L),\qquad T=J+N+L-1.
\]

There is a positive odd source `p=1 mod 3`, satisfying (11), whose first `T`
odd steps follow the periodic script and whose `T+1` states are distinct.
For the unchanged uniform empirical law

\[
 \pi=\frac1N\sum_{j=J}^{J+N-1}\delta_{q_j},
 \tag{15}
\]

the following assertions hold simultaneously.

1. Every forward and backward consecutive gap block of length `ell<=L` has
   exactly the product law `P^(tensor ell)`. There are enough actual steps
   on each side of every sampled state. Sampling `N` consecutive phases,
   with `d|N`, gives (13) without a boundary error.
2. Every state in the full constructed segment is at least `p`. Each actual
   window satisfies `max_(0<=i<=m) q_f/q_(f+i)<=K_v` when it is present.
3. Every present `m`-window has its complete normalized carry bounded by

   \[
   \boxed{\frac{C(w)}{3^m}
    =\frac13\sum_{i=0}^{m-1}\frac{R_{f+i}}{R_f}
    \le\frac{mK_v}{3}.}
   \tag{16}
   \]

4. Its finite multiplicative correction obeys
   `kappa >= exp(-m/(3p))`. The floor `H` can make it arbitrarily close to
   one at any requested finite horizon.
5. The ternary endpoint collision satisfies

   \[
   \boxed{\operatorname{Col}_{3^m}(\pi)\ge\frac1d.}
   \tag{17}
   \]

   Its ordinary diagonal is exactly `1/N`; thus its unequal ordinary
   congruent-pair mass is at least `1/d-1/N`.

**Proof of the remaining assertions.** The path and statistics were proved
above. The actual correction identity is
`q_j=p/(R_j Lambda_j)`, with
`Lambda_j=product_(i<j) 3q_i/(3q_i+1)`. Since `Lambda` decreases,
`q_f/q_(f+i) <= R_(f+i)/R_f <= K_v`. The bound on `kappa` follows from
`log(1+1/(3q_i))<=1/(3p)`. Formula (1) gives (16) directly; it does not need
a probabilistic approximation to `kappa`.

By (7), at most `d` endpoint residues occur. Each phase has mass exactly
`1/d`. Its residue class may coincide with another phase, which only
increases collisions. Equivalently the ordered same-phase pairs alone
contribute `d(N/d)^2/N^2=1/d`. This retains diagonal pairs and proves (17).

There is no restriction requiring a short empirical window. For fixed
`P,L,v`, choose `N=d R_m` as large as desired. In particular one can enforce

\[
 N\sqrt m/3^{\theta m}\longrightarrow\infty,
 \qquad \theta=0.949955527188\ldots,
 \tag{18}
\]

while the collision lower bound stays `1/d`. Thus the construction respects
the necessary diagonal budget from the previous round; the obstruction is
not the ordinary `1/N` diagonal.

## 7. Where the earlier source-box bound is saturated

Use the boxes of
[ACTUAL_COLLISION.md](../whole-repo-round3-20261123/ACTUAL_COLLISION.md):
for an `m`-window record its total `A`, its carry quotient
`k=floor(C/3^m)`, and its actual source quotient `ell=floor(q_(j-m)/2^A)`.
Equal phase gives the same complete word, hence the same `A,k`. Its `N/d`
occurrences have distinct sources, and equal words force those sources to
be congruent modulo `2^A`. Consequently their `ell` values are distinct.

Within one phase, every source box therefore carries a single atom of mass
`1/N`. Summing its box diagonals gives `1/(dN)`, whereas its actual residue
collision is exactly `1/d^2`. The cross-box factor is `N/d`, with no change
to the weights, source, endpoint, clock, or residue. The square of the sum
of box square roots is exactly `1/d^2` on this phase. Replacing it by the
sum of box energies would fail by that factor. Repeated-word mass is
explicit here; it has not been erased by counting distinct scripts.

All normalized carries obey (16). Thus keeping a linear carry band and all
fixed local word statistics does not control aggregation across the unbounded
ordinary source quotients. This is the arithmetic location of the lost
independence in this construction.

For a particularly transparent comparison, choose the fair law on gaps
`{1,2}`. Its mean is `3/2<log_2 3`. For a truly iid `m`-word, the ternary
endpoint code is injective on `{1,2}^m`: the last gap is recovered from the
endpoint modulo three, and stripping that affine step recovers the earlier
code modulo `3^(m-1)`. Its ternary collision is therefore exactly `2^(-m)`.
Our actual segment has exactly those iid block laws through depth `L`, but
collision at least `2^(-L)` at every precision `m`, with a source-dependent
horizon. The difference is present even at the reference law's own collision
exponent, without invoking the larger critical exponent.

More generally, rational finite gap laws of mean strictly below `log_2 3`
can approach the critical geometric law in total variation, first moment,
and Shannon entropy: truncate its exponentially small tail onto gap one,
then approximate the resulting probabilities rationally while preserving
the strict mean inequality. For every fixed testing depth their product
laws also approach the geometric products. This does not identify the fair
`{1,2}` law with a geometric law, or identify Shannon entropy with Rényi-2
entropy.

## 8. The fixed-source boundary and the fresh stationary result

The new PR180 checkpoint
[`a436db7b85f37abafea25f42d6f34afed02a29c0`](https://github.com/GettysburgResearch/collatz/blob/a436db7b85f37abafea25f42d6f34afed02a29c0/research/whole-source-20261123/COLLISION_CORE.md)
proves a strict, process-dependent upper Rényi-2 dimension below `theta` for
each actual stationary time-limit law of an escaping source. The argument
propagates a finite Shannon deficit, or handles the exact geometric iid
equality case with its smaller collision exponent. Its finite-deficit branch
also retains an explicit moving-window comparison. We use none of those
infinite conclusions as premises of the finite construction.

There is no conflict. Our finite trajectories change their initial integer
as the requested horizon grows; inequality (8) makes that change compulsory.
They provide neither one escaping source nor its canonical harmonic flow.
The full local Bernoulli property is asserted only to the prescribed depth
`L`; at larger depths the periodic dependence is explicit. Sending `L` to
infinity through different constructions is another change of source, not
the time limit of a fixed ordinary orbit.

The construction rules out a proposed upper estimate if its entire input is
these finite local statistics, a mean-gap cap, positive ordinary realization,
a source floor, and a period-dependent linear carry band, with no retained
upper source-height cost or fixed-source hypothesis. It does not rule out a
proof using additional arithmetic correlations of one unchanged escaping
source, or a theorem for its specified harmonic law. Those are precisely the
correlations that an application of convolution or iid affine-walk results
would still have to establish. The same-limit upper estimate required by
PR180 remains unproved.

## 9. Lean scope

`ActualLawRigidity.lean` is the finite arithmetic companion. Its twelve
public statements are:

| Statements | Formal content |
|---|---|
| `gapCarry_append`, `rotated_gap_carry`, `period_shadow_step` | Complete gap carries and the exact rotated shadow equation |
| `actual_shadow_step`, `shadow_telescope` | One ordinary edge and the full original-source telescope |
| `shadow_ternary_divisibility`, `shadow_binary_divisibility`, `source_height_payment` | Both coprime cancellations and the necessary source-height payment |
| `same_shadow_phase_residue`, `phase_residue_card`, `phase_collision_lower` | Equal-phase residue equality, finite support count, and the weighted collision lower bound |
| `affine_coincidence_unique` | At most one original-source coincidence for each pair of different affine slopes |

The actual edge equations, shadow equations, denominator coprimality, and
finite phase code are explicit parameters where used. The de Bruijn/Eulerian
construction, CRT realization and avoidance of pairwise affine coincidences,
probability identifications, and all asymptotic comparisons above remain
written mathematics. The pairwise affine uniqueness statement is formal;
the finite counting that selects a good CRT lift is written. Development
compilation used Lean 4.34.1 and the shared pinned Mathlib; the parent packet
records its independent fresh replay and axiom audit separately.
No infinite ordinary orbit or canonical measure is introduced as an axiom.
