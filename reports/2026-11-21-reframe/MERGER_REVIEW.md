# Independent review of marked transport and population packing

Reviewer: the discrete-closure research lane, independent of the merger-lane
author. Review date: 2026-11-21.

## Artifacts and scope

The review covers:

- `research/reframe-20261121/lean/MarkedDyadicTransport.lean`;
- `research/reframe-20261121/lean/MergerPopulationPacking.lean`;
- `research/reframe-20261121/UNIVERSAL_MERGERS.md`.

The source hashes below were pinned after the author reported successful
strict compilation of both modules and froze the proof changes:

| Artifact | SHA-256 |
| --- | --- |
| `MarkedDyadicTransport.lean` | `3d4f84900ddb2f5d6f2ad72448bddb0606853214749987b5ad32ccb886d7a521` |
| `MergerPopulationPacking.lean` | `57ac88e6ace8379db791bf68086d52078d099930df780affdeb5626ab6c052cc` |
| `UNIVERSAL_MERGERS.md` | `f14f5b3fce434d90b5531cb73ceec5b5564b5dbc9f89526e19f6f0580380c645` |

The final proof edits were read and the hashes independently recomputed.
No parallel Lean process was started for this semantic review; the final
combined compiler and axiom-audit receipt is supplied separately. The author
reports `-j1 -DwarningAsError=true` passes and standard Lean axioms only for
all ten public transport theorems and six public packing theorems.

**Semantic verdict:** no mathematical gap found in the rounded-up prefix
argument, ordinary dyadic transport, guarded merger application, or
equal-first-hit population packing. The written fan-to-antichain and octave
consequences have the stated constants and retain their necessary hypotheses.
This is not a finding that the universal merger selector exists.

The imported map and predicates were checked against the credited PR173
vendor sources: the shortcut map counts every halving; `Basin n` is an
actual finite hit of one; `Marked n` is oddness together with

\[
(d+1)(n-2^d)\le70\,2^d,
\qquad d=\lfloor\log_2 n\rfloor.
\]

The review uses PR173's proved global marked-visit interface as credited. It
does not re-audit that entire imported packet or claim a new proof of the
finite fan credited to PR176.

## 1. Ordinary dyadic extraction

For a marked `n`, odd `x`, and an actual decomposition

\[
n=2^j x+c,\qquad j\le d,\qquad 0\le c\le n-2^d,
\]

the offset guard supplies the essential lower bound
`2^d<=2^j*x`. Together with `2^j*x<=n<2^(d+1)`, it determines
`floor(log2 x)=q=d−j`. Oddness implies positivity, so this logarithm
calculation does not include zero.

The subtraction identity

\[
n-2^d=2^j(x-2^q)+c
\]

is justified before it is used: both `x>=2^q` and `n>=2^d` have already
been established. Thus the Lean natural-number subtraction is not silently
being treated as integer subtraction outside its valid range.

Multiplying the desired new mark inequality by `2^j` gives a quantity
bounded by `(d+1)(n−2^d)`. Cancellation is legal because `2^j>0`.
For `j>0`, positivity and `2^j>=2` give `x<n` independently of any orbit
assertion.

The floor-prefix corollary retains the same offset guard: since `2^d` is
divisible by `2^j`, the remainder `n mod 2^j` equals
`(n−2^d) mod 2^j` and is therefore at most `n−2^d`. No fractional
approximation to the section is used.

## 2. Rounded-up prefixes

The new theorem assumes `0<j<=d` and that
`x=floor(n/2^j)+1` is odd. Since marked `n` is odd and `j>0`, this is
exactly `ceil(n/2^j)`. Let `q=d−j` and `t=x−2^q`.

The proof has two essential features, both present in the source.

First, quotient bounds give

\[
2^q<x\le2^{q+1}.
\]

The right endpoint is even, while `x` is odd. Hence the upper inequality is
strict, `floor(log2 x)=q`, and `t>0`. The potentially problematic rounded
endpoint at the next power of two is therefore excluded by an explicit
hypothesis, not overlooked.

Second, quotient multiplication gives

\[
2^j(t-1)\le n-2^d.
\]

The parent mark and cancellation yield
`(d+1)(t−1)<=70*2^q`. Positive depth gives the additional room
`q+2<=d+1`, so

\[
(q+2)(t-1)\le70\,2^q.
\]

To recover the unit lost by rounding, split into two cases:

- If `t<=q+2`, use
  `(q+1)t <= (q+1)(q+2) <= 3*2^q <= 70*2^q`.
- If `t>q+2`, use
  `(q+1)t <= (q+2)(t−1) <= 70*2^q`.

The auxiliary bound `(q+1)(q+2)<=3*2^q` is valid at `q=0,1`, and its
inductive step for `q>=1` uses `q+3<=2(q+1)`. There is no asymptotic
qualification or omitted low-depth exception.

The resulting theorem proves exactly markedness of the rounded prefix.
For `n>1`, the rounded prefix at positive depth is also at most
`(n+1)/2<n`. The separate upper-half corollary handles `n=1` explicitly.
An actual ordinary merger remains necessary before this section-membership
result transfers convergence.

The written canonical candidate `U(n)=2*floor(n/4)+1` follows correctly:
for odd `n=3 mod 4` it is the lower half, and for odd `n=1 mod 4` it is
the upper half. It is marked whenever `n` is marked, and it is strictly
smaller when `n>1`. This gives an explicit decreasing tree of candidates;
the text correctly leaves the actual merger along every edge unproved.

## 3. Merger semantics and the global equivalence

`Merge n x` means that some finite forward iterate of `n` equals some
finite forward iterate of `x`; the two clocks may differ. The basin
equivalence follows from the imported actual-hit basin transfer on each
arm. The proof does not assert that `x` itself occurs on the forward orbit
of `n`.

In the guarded rising phase, the explicit clocks are correct. For
`n=2^k*u−1`, `m=2^(k−1)*u−1`, and `3^(k−1)*u=4z+3`, the two rising
prefixes land at `12z+8` and `4z+2`. Both reach `3z+2` after two further
shortcut steps. Thus

\[
T^{k+2}(n)=T^{k+1}(m).
\]

The phase guard is preserved in the theorem. Because `k>=2`, the original
source is `3 mod 4`, and its lower half is the odd partner `m`. The new
floor-prefix theorem therefore supplies markedness for the whole guarded
phase, with strict ordinary size decrease.

The equivalence
`Universal ↔ DyadicMarkedCover` is also correctly scoped. Universal
convergence supplies the cover by choosing `x=1`, `j=d`, and the actual
hit-to-one certificate. Conversely, the supplied cover gives an actual
smaller marked partner, so strong induction proves convergence of all
marked inputs and the credited global visit theorem finishes the transfer.
The Lean source defines the cover as a proposition and does not supply a
proof of its existence or introduce it as an axiom.

For `n=2^d+1`, the original nonnegative-offset cover forces `c=1`, then
`x=2^(d−j)`, and oddness forces `x=1`. The manuscript correctly limits
this rigidity to that cover. Rounded-up candidates
`2^(d−j)+1` at `j<d` escape the rigidity and are marked; their universal
merger property remains unproved. This distinction is important and is
maintained in the text.

## 4. Equal-first-hit antichains

The packing module's `FirstHit k n` includes both the hit at clock `k`
and absence of a hit at every earlier clock. Mere membership in the basin
would not imply the antichain result.

If `a` and `b>2` have the same first-hit clock and `a` reaches `b` after
`j` steps, then:

- `j=0` gives `a=b`;
- `j>=k` would place `b` on the terminal orbit `{1,2}`, contradicting `b>2`;
- `0<j<k` would make `b` hit one after `k−j<k` steps, contradicting its
  first-hit condition.

The source explicitly proves invariance of the small terminal set before
using it. Thus it handles later returns through `1→2→1`, rather than
treating one as an absorbing state.

For a common predecessor of two targets, ordering its two hit clocks makes
one target a forward successor of the other. The antichain argument then
forces equality. This proves disjointness of complete ordinary predecessor
sets without requiring equal inverse clocks. The assumptions `a,b>2` are
retained where they are needed.

## 5. Marked-octave capacity and formal packing

Within `[2^d,2^(d+1))`, the mark inequality confines all marked sources to
an interval with at most

\[
\left\lfloor\frac{70\,2^d}{d+1}\right\rfloor+1
\]

integer points. Counting all integers there is a valid upper bound even
though marked points are required to be odd. The inequality `d+1<=2^d`
absorbs the endpoint and yields

\[
(d+1)\#\{\text{marked points in octave }d\}\le71\,2^d.
\]

For finite targets on one first-hit level, supplied populations in one
octave are disjoint by the preceding theorem. Their cardinalities therefore
sum to at most that capacity. The rational density theorem correctly
deduces

\[
\gamma |P|\le71(d+1)
\]

from the individual lower bounds
`gamma*2^d <= (d+1)^2 * |A_p|`. The Lean statement permits arbitrary rational
`gamma`; the manuscript imposes `gamma>0` when interpreting the result as a
height obstruction. No positive-density conclusion is extracted from a
negative parameter.

These are capacities for supplied inverse populations. They are not upper
bounds on forward survivors above a fixed floor and do not equate inverse
tree growth with loss of ordinary source mass.

## 6. Written consequences of the finite fan

Conditional on PR176's credited finite fan of `2^Q` marked sources, the
normalization to ternary-unit targets has fibers of size at most two. An
unchanged source contributes at most one preimage, and the shortcut odd
branch is injective. Normalized targets stay above `2^Q`, below
`2^(10Q+1)`, and reach one before clock `11Q`. They may be even, as the
manuscript explicitly notes.

Pigeonholing by the actual *first* hit clock therefore gives a target set
on one level with

\[
|P|\ge2^Q/(22Q).
\]

For a common successful population octave, substituting this lower bound
into the formal packing inequality gives

\[
d+1\ge\frac{\gamma\,2^Q}{1562Q},
\]

where `1562=71*22`. This is a conditional necessity for such simultaneous
populations. It does not assert that a common octave exists.

The stronger manuscript corollary also allows a separate successful
octave `d_p<=D` for each target. Partitioning the targets by this assigned
octave and summing the capacities gives

\[
\gamma|P|\le\frac{71(D+1)(D+2)}2,
\qquad
(D+1)(D+2)\ge\frac{\gamma\,2^Q}{781Q}.
\]

The factor `781=1562/2` and the scope of this strengthening are correct.
It excludes a uniform small upper bound for all the assigned witness
octaves, even when they need not coincide. It retains the same positive
target-independent density constant. The argument does not contradict
arbitrarily large target-dependent witness octaves.

The finite-fan extraction and these substitutions remain written
deductions, separate from the six public declarations in the packing
module. No extra formal import of PR176 or PR180 is claimed.

## Remaining global obligation

The reviewed results enlarge the class of section-preserving candidate
partners and quantify the cost of simultaneous inverse populations. They
do not construct an actual successful merger for every marked source.
The universal selector or another globally sufficient closure principle
remains open, as stated in the manuscript and in the formal cover interface.
