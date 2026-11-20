# Independent reconstruction of directed circulation and DC3

Reviewer: arithmetic-route agent, separate from the circulation author.
Scope: exact files below, read and checked on 2026-11-20. This is an AI proof
reconstruction, not external referee acceptance or formal verification.

## Frozen artifact identities

| Artifact | SHA-256 |
|---|---|
| `DIRECTED_BOUNDARY_CIRCULATION.md` | `23e0fb30ca213fbac8aa1a6a948b323bebd2c192e6422eceed5a0d643fb220a6` |
| `check_directed_circulation.py` | `8e2b7ca383655a4bf60cb22584ca38812402d0d1b7b3d3f1ba6293e5ef037e33` |
| Author normal and optimized JSON | `d39d61b4b20137f524aef9495a409d95eb1d55f7f6e86b868a5f261661eaa639` |

Source pins inspected:

* PR146, `6863d298187af8b2619efbf78cc4b0aa8e627393`,
  `research/upper-bit-mergers/DIRECTED_TRIPLING.md` and
  `THREE_RAY_DENSITY.md`.
* PR155, `92f499b9d340d1ff8cc643c3eef3477d61b477c1`,
  `research/gemini-dirichlet-global-20261120/ORDINARY_DIRICHLET_COERCIVITY.md`,
  especially OD2--OD4. Its analytic theorem is retained as a named pinned
  input; this review reconstructs the new deduction from it, not a new
  exhaustive review of PR155.

## Verdicts

| Claim | Narrow verdict |
|---|---|
| Canonical ordinary return, bounded length and finite affine multiplicity | VERIFIED against the pinned construction, with independent source-list reconstruction |
| DC1 finite positive weight and two oriented inequalities | VERIFIED |
| DC1 exact signed flux when either orientation is summable | VERIFIED; absolute summability is established before rearrangement |
| DC2 one-sided weighted coercivity and modulo-constant conclusion | VERIFIED conditional on pinned PR155 OD2/OD3 |
| DC3 for bounded real invariant labels | VERIFIED under its explicitly stated component-divergence input |
| DC3 extension to arbitrary finite real invariant labels | VERIFIED by monotone clipping |
| DC3 at exponent 0.84 | SOURCE-QUALIFIED through the stated Krasikov--Lagarias predecessor theorem; not independently reproved here |
| Full Collatz closure | OPEN; none of the claims supplies finite oriented moment for a hypothetical separating label |

## 1. The return and its multiplicities

In the high case `x=3^5 v`, the upward tripling sources have powers
`3^i v` with `6<=i<a`; the final upward sources have `b<=i<5`.
These ranges are disjoint. Each intervening exponent descent uses exactly
one source `8*3^(i-3)*v-1`, with a different exponent at each descent.
Thus the seventeen listed affine labels cover every occurrence and each
label is used at most once within one return.

Both neighbor crossings use at most eight ordinary edges. There are at
most seven eleven-edge descents, and each outer tripling leg has at most
three edges. The bound 99 is therefore valid. Ordinary edges may be
traversed backward here; this is precisely why the construction is an
augmented directed return rather than a proof of ordinary meeting.

In the low case `x=3^j u`, `0<=j<=4`, the initial and final power-source
ranges are again disjoint. The embedded high return uses
`v=(2^a u-1)/729`, a positive ordinary integer by the chosen congruence.
Label that embedded source also by `j,a`, retaining multiplicity even if
two numerical affine functions agree. This gives exactly the stated
upper label count

\[
17+5(A+1)+5A\cdot17=2799922.
\]

The modular choices exist because 2 has order 486 modulo 729 and
`3^486` has order 64 on each fixed odd class modulo 8 inside the units
modulo 512. The four neighbor cylinders meet those four classes. The
chosen exponent is at most 31110. The total edge bound `3a+116<L`
holds. Every elementary edge changes height by a factor at most three,
so the stated `H=3^(L+1)` controls all sources relative to `x`.

All affine labels have strictly positive slope, hence at most one
ordinary preimage for a prescribed target. Restricting their legal
domains does not destroy that injectivity. This is the required global
multiplicity fact; finite numeric evidence alone would not establish it.

## 2. DC1 and the sign bookkeeping

For an invariant real label, the ordinary edges have zero change. A
complete directed cycle therefore gives

\[
g(x)+\sum_{y\in S_x}g(y)=0.
\]

This implies `g_-(x)<=sum g_+(y)` and the reversed-sign inequality.
Multiplication by the positive weight and Tonelli are legitimate before
any summability is known. Bounded multiplicity and comparability of the
weight yield the two estimates with constant `M K_omega`.

If either oriented moment is finite, the other one is consequently
finite. Comparability also makes the entire double sum of absolute
defects finite. Only at this stage is the signed sum rearranged.
The coefficient of `g(y)` is exactly the finite positive `pi_omega(y)`.
Thus the common-weight flux identity does not subtract two infinite
fluxes or assume cancellation from a formal residue model.

The power/logarithm weight example satisfies the comparability condition:
if `x/y` lies between `H^-1` and `H`, the ratio of `log(ex)` and `log(ey)`
lies between `(1+log H)^-1` and `1+log H`. Negative exponents are correctly
handled by absolute values in the stated constant.

## 3. DC2 and DC3

The tripling defect inherits exact doubling invariance from `f`, so its
full weighted norm is the sum of its odd positive and negative moments
divided by `1-2^-s`. Combining DC1 with pinned OD2 proves the first
functional inequalities. For bounded labels, OD3 gives one unique
constant and the same estimates for `f-c`. No abscissa-divergence
assumption is introduced.

For DC3, fix the input

\[
\sum_{n\in C}n^{-\beta}=\infty
\]

for every ordinary component, with `0<beta<1`. If a bounded real
invariant `f` has one finite oriented beta moment, DC2 supplies `c` with
`sum |f(n)-c| n^-beta<infinity`. If `f(n_0)!=c`, invariance makes this
same nonzero absolute value occur on the whole component of `n_0`.
Its divergent component series gives a contradiction. Therefore `f=c`
everywhere, not merely almost everywhere in a limiting profile.

For finite real labels without a boundedness assumption, let
`F=min(b,max(a,f))` with finite `a<=b`. This function is invariant.
The clipping map is monotone and 1-Lipschitz; therefore pointwise

\[
(F(3x)-F(x))_+\le(f(3x)-f(x))_+,
\qquad
(F(x)-F(3x))_+\le(f(x)-f(3x))_+.
\]

The assumed finite orientation remains finite after clipping, so the
bounded conclusion makes every such `F` constant. If two original
values differed, choosing `a,b` equal to those values would preserve
their difference, contradiction. The constants supplied for different
clippings need not be identified or passed through a limit.

The cited predecessor count at exponent beta implies divergence at the
critical exponent by partial summation: a bound `A_C(X)>=c_C X^beta`
for all sufficiently large `X` makes the integral
`beta integral A_C(t)t^(-beta-1)dt` diverge. The PR146 source explicitly
asserts the published Krasikov--Lagarias bound for every fixed target
prime to three, and explains why each component has such a target.
The beta=0.84 specialization thus has exactly the advertised dependency.
Neither the external large inverse-tree theorem nor a formal build was
replayed in this review. No claim at beta=1 is obtained from this argument.

## 4. Execution evidence

The reviewer program `review_circulation.py` reuses the author's path
producer and fixture list. Its acceptance checks are separate:

* independently reconstructed elementary ordinary edges and directed
  tripling orientation;
* an independent affine-source list, including labels and multiplicity;
* a separately implemented union-find quotient and exact rational flows;
* both scalar oriented clipping inequalities.

Normal and `-OO` runs of the standard 218-source fixture set passed and
produced byte-identical reports. They checked 24,039 literal edges,
4,447 return-tripling sources, three quotient flows on 2,196 vertices,
and 44,217 exact rational clipping cases.

A separate expanded normal-mode run also included the sources
`1,3,9,27,81`. It completed successfully with 223 sources, 388,919 literal
edges, 125,977 return-tripling edges, and three balanced flows on 26,498
quotient vertices. Its longer routes are preserved in the expanded
report; that larger fixture was not rerun under optimization. The final
reviewer script exposes it through `--extra-sources`.

The finite checks do not certify the analytic Tonelli/coercivity or
predecessor-divergence arguments. Those were reconstructed above with
their dependencies retained. There was no finding requiring a change
to the reviewed mathematical artifact.
