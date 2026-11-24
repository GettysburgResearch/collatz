# One pressure maximum with both forward and inverse coefficient bounds

**Status: written deduction from the pinned elementary escaping-orbit product
bound; no escape exclusion or complete source dispatcher.** The new selection
uses one fixed ordinary unit root for both directions. The finite coefficient
and residue algebra is separated from the infinite product construction.

## 1. Start after the unrestricted source optimization

The source inputs are:

- PR177, `6de3e304bb49a93a6c5ef0e5563137e75c7defb4`,
  `research/lean-exact-witness-global-20261121/HIGH_VARIANCE_WITNESS.md`,
  FB1--FB9, Git blob `f3143fc4c63c3eff749ceb2d18ce7326a184a5c1`.
- PR180, `04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`,
  `research/high-variance-20261123/GLOBAL_SOURCE_SYNTHESIS.md`,
  Git blob `400cdfc4bba491488247a744996e8555e131abf7`.
- PR177 at the same pin,
  `research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md`,
  HE2, HE15, HE18--HE24e, Git blob
  `314fce3965adf36775fac9b5f2097c0181e830de`.

For a target `t=2B+1`, the new finite optimizer already considers **every**
complete capturing witness. Its sources are exactly

`F_B={2m: m belongs to R_B, B<=2m}`,

where `R_B` is the whole finite inverse closure of one below `B`. Trimming
at the last actual exit pays with the literal supplied grade. Every
multiwindow edit, changed length, or larger exponent producing a complete
cheaper source would trim to one of these finite competitors with no larger grade.

I therefore did not try to improve that genuine optimum using source
geometry alone. Such an optimum also exists for convergent difficult
targets. Instead I tried to combine the actual least-bad information with
the ordinary atomic pressure, to obtain a contradictory constraint on the
component containing that target.

## 2. A single ordinary root extremizes every pressure parameter

Use the accelerated odd map

`U(n)=(3n+1)/2^a(n)`, `a(n)=v2(3n+1)`.

Let `E` be a hypothetical escaping component of positive odd integers
prime to three, with component relation given by eventual forward meeting.
All ordinary inverse unit branches remain in `E`. Let `m_0=min E`.

Retain the exact functions of HE18:

\[
\Lambda(n)=\prod_{j\ge0}\frac{3U^j(n)}{3U^j(n)+1},\qquad
r(n)=\frac{\Lambda(n)}n.
\tag{1}
\]

The product is positive by the elementary orbit-count argument in the
pinned source. It gives `0<r(n)<=1/n` and, on every actual edge,

\[
2^{a(n)}r(n)=3r(Un).
\tag{2}
\]

**Selection theorem.** There is an ordinary `m in E` such that

\[
r(m)=\max_{n\in E}r(n).
\tag{3}
\]

It is simultaneously a maximum atom of every canonical component pressure
measure `mu_(E,s)=sum_(n in E) r(n)^s delta_n`, `s>1`.

**Proof.** Choose any `p in E`. Since `r(p)>0`, choose an integer
`N>1/r(p)`. For `n>N`, `r(n)<=1/n<r(p)`. The nonempty finite set
`E intersect [1,N]` therefore contains a global maximizer. Raising
positive numbers to any positive power preserves the ordering, so the
same root works for every `s`. If a single specified root is desired,
choose the least ordinary integer among the maximizers. No maximizer
is selected separately for the forward and inverse statements below.

### The root lies near the ordinary component minimum

The pinned elementary count gives, for the odd states `S` of any one
escaping forward orbit,

`#(S intersect [1,X])<=4X^(39/40)`.

Every such state belonging to `E` is at least `m_0`. Tonelli therefore
improves the uniform reciprocal bound to

\[
\sum_{n\in S}\frac1n
 =\int_{m_0}^{\infty}\frac{\#(S\cap[1,x])}{x^2}\,dx
 \le160m_0^{-1/40}.
\]

Hence, uniformly for `n in E`,

\[
\Lambda(n)\ge\delta_{m_0}
 :=\exp\!\left(-\frac{160}{3}m_0^{-1/40}\right).
\]

Comparing the chosen maximum with `r(m_0)` yields

\[
\boxed{m_0\le m\le
m_0\exp\!\left(\frac{160}{3}m_0^{-1/40}\right).}
\tag{4}
\]

In particular `m/m_0 -> 1` as the component minimum tends to infinity.
This does not identify `m` with the ordinary least element, or give an
algorithm deciding component membership in the finite interval (4).

## 3. Both coefficient inequalities hold at that same root

For a supplied nonempty actual odd-gap prefix of length `h` and total
ordinary clock `A`, iterating (2) gives

\[
2^A r(n)=3^h r(q),\qquad U^h(n)=q.
\tag{5}
\]

Apply (5) first with `n=m`. Since `r(q)<=r(m)` and `r(m)>0`,

\[
\boxed{2^A<3^h\quad
\text{for every nonempty actual forward prefix from }m.}
\tag{6}
\]

The weak inequality follows by cancellation. Equality is impossible:
`A>=h>=1`, so `2^A` is even while `3^h` is odd. The complete physical
identity `2^A q=3^h m+C`, with `C>0`, then shows `q>m` at every positive
odd clock. Thus this selected root is also a strict forward record minimum.

Apply (5) instead to **any** positive odd unit ancestor `n` reaching `m`.
The maximum still gives `r(n)<=r(m)`, and therefore

\[
\boxed{3^h<2^A\quad
\text{for every nonempty actual inverse prefix ending at }m.}
\tag{7}
\]

Every intermediate inverse prefix satisfies the same inequality because
its ordinary source remains in `E`. There is no prescribed inverse depth,
word alphabet, or search cutoff in (7).

For any distribution on actual inverse words of a fixed length `h`, (7)
gives a mean total gap at least `floor(h log_2(3))+1`. It does **not** give
a uniform positive excess per odd step over `log_2(3)`: the rounding excess
divided by `h` tends to zero along suitable lengths. Likewise the two
inequalities refer to different directed paths and do not identify their
probability laws.

### Local ordinary consequences

At the selected root the forward gap is exactly one, since (6) at `h=1`
gives `2^a<3`. Thus `m=3 mod4`.

An incoming unit gap one is impossible by (7). Such an edge exists precisely
at unit roots `m=2` or `8 mod9`; its source is `(2m-1)/3`. The residue
`m=5 mod9` must **not** be excluded: there this source is divisible by three
and lies outside the unit domain. Combining the correct restrictions gives

\[
\boxed{m\bmod36\in\{7,19,23,31\}.}
\tag{8}
\]

This is a consequence of one globally selected pressure maximum, rather
than a claim that the four classes are an exhaustive convergent cover.

## 4. The attempted finite-graph pressure argument

Assume now that the original target `t` is the least positive integer not
reaching one. For every `n<t`, its complete ordinary orbit is finite.
Consequently

\[
K=\bigcup_{1\le n<t}\{T^j(n):j\ge0\}
\]

is a finite, forward-invariant subset of the basin of one containing
`[1,t)`. This uses the **actual** least-bad hypothesis, not a fixed clock
cutoff. Its maximum can be far above `t`; leastness gives no common height
bound in terms of `t` here.

If the bad component escapes, its unit component `E` is disjoint from
`K`. Its ordinary minimum is at least `t`, and the selection (3)--(8)
applies. I tried to combine this minimum restriction with the pressure
identity at a finite known graph boundary.

The exact operator is

\[
(P_s f)(q)=\sum_{\substack{e\ge1\\I_e(q)\text{ positive odd unit}}}
       (3/2^e)^s f(I_e(q)),\qquad I_e(q)=(2^eq-1)/3.
\]

It preserves ordinary components: every legal parent of `q in E` is still
in `E`. Thus a test supported on `K`, or on any finite inverse enlargement
of `K`, has both `f=0` and `P_s f=0` on `E`. Integrating it against the
actual eigenmeasure `mu_(E,s)` gives exactly `0=0`. Weighting the known
finite boundary does not change this separation.

The least-component floor does constrain long incoming gap-one runs. If
`q in E` and `v3(q+1)>=j+1`, then the actual unit ancestors

`I_1^i(q)=(2/3)^i(q+1)-1`, `0<=i<=j`,

all remain in `E`. Therefore

\[
\boxed{(2/3)^j(q+1)-1\ge m_0.}
\tag{9}
\]

This is a height-dependent limit on those prefixes, not their deletion
from the pressure operator. Their original masses remain in its row.
The maximum root adds the stronger coefficient restriction (7), but it
still supplies no uniform gap excess at increasing depth.

Finally, the Green integration shortcut retains the obstruction already
proved in HE24e. For one unchanged source `p in E` and `q_k=U^k(p)`,

`mu_(E,s)({q_k}) Z_s(q_k)>=r(p)^s>0`.

The infinitely many distinct future states make the integral of `Z_s`
diverge. The lower cutoff `m_0` does not remove these terms. In particular,
ordinary finiteness of the known graph cannot justify integrating the
Green equation as a finite identity against this atomic measure.

## 5. What is and is not gained

The positive deduction is the simultaneous selection of one ordinary unit
root with (4), all forward inequalities (6), and all inverse inequalities
(7). It is derived directly from the pinned actual product and retains
its ordinary source throughout. No new external analytic assumption is
used. The selected root is independent of the pressure parameter.

I did not prove that the simultaneous forward/inverse restrictions are
inconsistent. The pressure operator is component-local; information that
all smaller integers belong to another component does not cross between
them through a boundary identity. A specifically arithmetic comparison
between components, or a construction using the actual target to violate
(6) or (7), is still missing. Nontrivial cycles require a separate argument:
the escaping product and its positive atomic pressure measure are not
asserted on a periodic component.

## 6. Formalization boundary

`TwoSidedPressure.lean` proves twelve statements over a generic
Archimedean ordered field. In particular, `attained_maximum` proves
existence of the ordinary global maximizer from positivity and the
explicit bound `n*r(n)<=1`; it does not take maximum attainment as an
assumption. `GapPath` retains every positive odd unit, every positive
actual valuation, and each exact physical identity. `path_balance`
telescopes the explicitly supplied edge-weight identity along that path.

`common_root_two_sided` returns one root and quantifies both inequalities
over all nonempty actual finite paths at that root. It does not select
the root separately for each word. Supporting statements prove strictness
of the power comparisons, forward ordinary growth with the full affine
correction, and the unit-sensitive residue conclusion (8).

The construction and positivity of the infinite product (1), its edge
identity, and the sharpened floor bound (4) remain the source-pinned
written argument. The module's generic weight hypotheses are explicit
parameters, not new global Collatz axioms. Development compilation under
Lean 4.34.1, one thread and warnings as errors passed; fresh replay and
complete declaration-dependency auditing are recorded separately in the
parent checkpoint.
