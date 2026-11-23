# The universal source-to-target attack

## Result and scope

This pass attacked the missing universal target return. It did not add another
finite family of successful source prefixes. No universal target-return proof
was obtained.

One proposed bridge is now refuted exactly, including its infinite tail:
**a complete rational source shadow with bounded gaps and strictly contracting
coefficients at every accelerated source prefix can have an affine target
shadow whose every positive-time coefficient expands.** The example uses the residual target shape `8q+19`,
the source gap alphabet `{1,2}`, and actual rational Collatz dynamics. The
finite entry and the symbolic repetitions are checked in
[`lean/RationalShadowTest.lean`](lean/RationalShadowTest.lean).

This is not a positive integer counterexample. In particular, the example
does not supply a positive integer source carrying a complete bounded-four
certificate with a nonconvergent positive target. It excludes a coefficient-only
rational-shadow completion of the source argument.

A second calculation gives the exact arithmetic cost of copying an inverse
word to a sibling `B^j(n)`, where `B(n)=64n+21`. Preserving an inverse word of
depth `r` first becomes integral at `j=3^(r-1)`. Thus that direct transport
has a doubly exponential height cost in the depth; altered gap words are
needed for the proposed inexpensive sibling comparison.

## Pinned inputs

| Input | Exact head | Used here |
|---|---|---|
| Published PR180 base | `ab3973099f0d285bbe88972382ad599bb02cd460` | Complete source grades, finite source ceiling, and the equal-grade larger-source tie in `research/lean-joint-20261122/MIXED_COVER.md`. |
| PR177 | `8ef9bf0d828fc533721dee1f90c5d78fac80ad39` | `ROOTED_SOURCE_FLOOR.md`, `STRICT_PREFIX_CONTRACTION.md`, `NEGATIVE_SHADOW_RETURN.md`, and `BOUNDED_FOUR_NORMAL_FORM.md`, under `research/lean-exact-witness-global-20261121/`. |
| PR185 | `53f01ca5b443ef57ef2160b4996dbb2cc87f7395` | Arbitrary rational-shadow compiler in `research/multiple-attacks-20261122/RATIONAL_SHADOW_DISPATCH.md`. |

The new Lean module imports Mathlib only. Its checked arithmetic does not
depend on the analytic hypotheses in the companion capacity notes.

## 1. What the attempted proof needed

Write `T(n)=n/2` for even `n` and `T(n)=(3n+1)/2` for odd `n`.
For an accelerated odd word of length `r`, let `A` be its total number of
ordinary steps and put

\[
Q=\frac{2^A}{3^r}.
\]

PR177 supplies cofinally many complete bounded-four sources for which every
nonempty source prefix has `Q>1`. It also selects a complete source covering
any sufficiently large target while putting all subsequent source states
below that target's original floor. Those statements are unconditional;
the assertion that the **target** must return below that floor is not.

The attempted bridge was to turn a hypothetical long non-descending target
prefix into its negative periodic rational shadow. The complete source
certificate and its coefficient contraction would then have to force a
contracting target prefix, or force an impossible source expansion.

The first unsupported step is sign preservation for the induced source
shadow. Negative integer orbits stay negative. Negative rational orbits
need not, even when every one of their source-prefix coefficients contracts.
The counterexample below retains an actual negative target orbit as well;
the problem is not an arbitrary choice of unrelated source and target
parity sequences.

## 2. An exact coupled rational counterexample

For a fixed positive odd denominator `d`, use the numerator map

\[
R_d(h)=
\begin{cases}
h/2,&h\equiv0\pmod2,\\
(3h+d)/2,&h\equiv1\pmod2.
\end{cases}
\]

Then `R_d(h)/d` is the usual Collatz map on the odd-denominator rational
`h/d`, with parity determined by its numerator. Reduction of the fraction
does not change parity, since every cancelled denominator factor is odd.

Take

\[
d=2187,\qquad x=-\frac{6005}{2187},\qquad
y=8x+19=-\frac{6487}{2187}.
\]

For positive integers `q>=3`, the corresponding target form `t=8q+19`
satisfies `8q+1<t<=16q+1` and `t≡3 (mod 4)`. Thus this affine form belongs
to the actual residual interval shape. The rational values `x,y` themselves
are negative, so they are not interval-query witnesses.

### Complete source shadow

The accelerated source orbit is

| Odd-step index | Rational state | Numerator over 2187 | Next gap |
|---:|---:|---:|---:|
| 0 | `-6005/2187` | `-6005` | 2 |
| 1 | `-1319/729` | `-3957` | 2 |
| 2 | `-269/243` | `-2421` | 2 |
| 3 | `-47/81` | `-1269` | 2 |
| 4 | `-5/27` | `-405` | 2 |
| 5 | `1/9` | `243` | 2 |
| 6 | `1/3` | `729` | 1 |
| 7 | `1` | `2187` | 2 forever |

Each row is an exact identity `3h+2187=2^a h'`, with both endpoint
numerators odd. Consequently the gap is exactly `a`, not just a divisible
power of two. All gaps are at most two.

For the first six nonempty odd prefixes,

\[
Q_j=(4/3)^j>1\qquad(1\le j\le6).
\]

The seventh prefix has

\[
Q_7=\frac{2^{13}}{3^7}=\frac{8192}{2187}>1.
\]

Every later odd prefix adds a gap of two, so

\[
Q_{7+k}=\frac{8192}{2187}(4/3)^k>1\qquad(k\ge0).
\]

The source shadow therefore has a complete literal word to one, a bounded
gap alphabet, and strict coefficient contraction at **every** nonempty
odd prefix. Nevertheless it crosses from negative to positive between
`-5/27` and `1/9`.

Bounded-four here means a bound on each gap. It does not mean `Q_j<=4`;
for example `Q_5=1024/243` and `Q_6=4096/729` exceed four. No upper bound
on cumulative `Q_j` is part of PR177's strict-prefix contraction theorem.

### Permanently expanding target shadow

The target's ordinary orbit is

| Clock `j` | Rational state | Numerator over 2187 | Odd steps in first `j` clocks |
|---:|---:|---:|---:|
| 0 | `-6487/2187` | `-6487` | 0 |
| 1 | `-2879/729` | `-8637` | 1 |
| 2 | `-1318/243` | `-11862` | 2 |
| 3 | `-659/243` | `-5931` | 2 |
| 4 | `-289/81` | `-7803` | 3 |
| 5 | `-131/27` | `-10611` | 4 |
| 6 | `-61/9` | `-14823` | 5 |
| 7 | `-29/3` | `-21141` | 6 |
| 8 | `-14` | `-30618` | 7 |
| 9 | `-7` | `-15309` | 7 |
| 10 | `-10` | `-21870` | 8 |
| 11 | `-5` | `-10935` | 8 |
| 12 | `-7` | `-15309` | 9 |

All states are negative. From clock nine onward the cycle is
`-7 -> -10 -> -5 -> -7`, with two odd steps and three ordinary clocks.
It multiplies the target coefficient `3^o/2^j` by `9/8` each time.

For clocks one through eight, the coefficients are

\[
\frac32,\frac94,\frac98,\frac{27}{16},\frac{81}{32},
\frac{243}{64},\frac{729}{128},\frac{2187}{256},
\]

all strictly above one. For `j=9+3k+s`, with `s` in `{0,1,2}`,

\[
\frac{3^{o_j}}{2^j}
=\begin{cases}
\dfrac{2187}{512}(9/8)^k,&s=0,\\[2mm]
\dfrac{6561}{1024}(9/8)^k,&s=1,\\[2mm]
\dfrac{6561}{2048}(9/8)^k,&s=2.
\end{cases}
\]

These are all strictly above one. Thus the target has **no coefficient-
contracting prefix at any positive clock**, while the source has a complete
bounded-gap word and strict coefficient contraction at every odd prefix.

### What this excludes

This refutes the implication obtained by replacing the positive integer
source in the universal interval problem with a complete rational shadow
and retaining only bounded gaps, source coefficient contraction, and the
affine source-target relation. A proof using that relaxation must add a
further arithmetic restriction and prove it for the actual integer query.

It does not refute PR185's compiler, which requires an actual contracting
target-shadow prefix as input. It does not refute a positive-source
periodic-block compiler under additional hypotheses. It does not show
that a positive integer lift of the source has a complete bounded-four
certificate. Those are precisely extra hypotheses that must not be
silently replaced by the rational calculation.

## 3. Why copied inverse words do not give an inexpensive sibling bridge

Let a positive integer inverse word of `r>=1` accelerated odd steps have
total gap `A`, correction `C`, endpoint `q`, and source `z`:

\[
3^r z+C=2^Aq.
\]

The sibling map and its iterates are

\[
B(q)=64q+21,\qquad
B^j(q)=64^j q+\frac{64^j-1}{3}.
\]

If the **same** gap word is to end at `B^j(q)`, its only possible source is

\[
z_j=64^jz+
\frac{(64^j-1)(3C+2^A)}{3^{r+1}}.
\tag{U1}
\]

This follows by subtracting `64^j` times the original affine identity
from the proposed new one. The factor `3C+2^A` is a ternary unit. For
`j>0`,

\[
v_3(64^j-1)=2+v_3(j).
\]

For completeness, write `j=3^s u` with `3∤u`. Starting from
`64=1+9*7`, repeated cubing increases the exact ternary valuation by one
at each step; the remaining `u`th power leaves it unchanged. This proves
the displayed valuation without a distributional assumption.

Therefore (U1) is integral exactly when

\[
\boxed{3^{r-1}\mid j.}
\tag{U2}
\]

When this holds, the intermediate inverse states are integral, positive,
and odd as well. Their original unit residues are preserved except
possibly at the oldest source. If the intended inverse operator kills
multiples of three, that oldest source's unit status must still be checked.
The sufficient stronger condition `3^r | j` preserves it too. Thus (U2)
is an exact **integer-word** criterion, not an unconditional retained-unit
criterion.

The first positive admissible integer lift is `j=3^(r-1)`. Its height
factor is already

\[
64^{3^{r-1}},
\]

and its geometric sibling weight is at most the reciprocal of that
factor. This excludes a cheap deep-witness transfer that leaves every
gap unchanged. It does not exclude an adaptive transformation of the
gap word.

## 4. The ordinary-size and adaptive-carry attack

The relevant canonical sector is a finite spike
`V_r(n)>=eta*n`, not an arbitrary ternary cylinder. Since the inverse
operator's row sum is at most two, `V_r<=2^r`; a high linear spike must
therefore have `eta*n<=2^r`, and hence

\[
\frac{n}{3^r}\le\eta^{-1}(2/3)^r.
\]

So the ordinary integer is far smaller than the modulus at deep spikes.
An isolated cylinder near `3^r` does not test this sector. The sought
bridge should exploit the long zero high digits of the ordinary integer
together with its full finite inverse witness.

I tried changing the inverse gaps as ternary carries appear, rather than
using (U1). Legal inverse gaps at a unit endpoint occur in one parity
class, and adding two cycles the parent through the three ternary
residues. This lets one repair a local residue obstruction with bounded
changes to a single gap. The missing estimate is global: the repairs
must retain a substantial fraction of the weighted inverse population
while controlling the accumulated change in total gap. Local
repairability alone supplies neither assertion.

In particular, long strings of the smallest inverse gaps can force the
coupled height ratio to drift. A first-record or killed-tree condition
limits which such strings are possible, but I did not derive a uniform
weighted correction bound from that restriction. The first unsupported
step would be to claim that the local repairs give a source/target
density ratio of order `1/log(n)` or better. No such bound is proved here.

The exact remaining target is an inexpensive **altered-word** transfer
for the high linear canonical sector, or another actual target-return
argument that bypasses it. The large-depth integer size condition has
not been discarded; it remains the promising additional input absent
from the generic cylinder obstruction.

## 5. Source extremality is a constraint, not the missing return proof

As a supporting observation, one can minimize the well-founded whole
source grade among all complete certificates above a target's coverage
floor, then maximize the source at that fixed grade using the finite
source ceiling. Such a certificate has no lower-grade replacement that
still covers the same target, and no equal-grade source enlargement.
These irreducible sources occur at unbounded heights. Thus source
rearrangements that always decrease this particular mixed source rank
cannot alone form a total same-target dispatcher with a finite terminal
base.

This observation was not promoted to a new closing theorem. The work
above tested target-dependent bridges on precisely the remaining side
of that distinction. The universal actual target return, and universal
Collatz convergence, remain unproved.

## Verification boundary

`RationalShadowTest.lean` checks the exact source gap identities and
parities, the complete source clock to one, all source-prefix coefficient
inequalities, the finite target entry, and every target coefficient through
symbolic repetition of the negative cycle. It uses neither `sorry` nor
an assumed Collatz theorem.

The module compiled with Lean 4.34.1, `-j1 -DwarningAsError=true`, against
the pinned Mathlib runtime. Its axiom output contains only `propext`,
`Classical.choice`, and `Quot.sound`; the finite target-state certificate
uses no axioms.

The copied-word calculation, its general valuation criterion, the
ordinary-size discussion, and the source-extremality observation are
written mathematics. The root module separately checks the depth-at-least-
two obstruction for the first sibling. No unproved weighted-carry estimate
is included as a theorem.
