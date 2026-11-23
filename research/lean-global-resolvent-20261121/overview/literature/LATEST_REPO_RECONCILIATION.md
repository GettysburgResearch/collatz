# Reconciliation with the late PR177 and PR180 updates

**Status: source reconciliation and a new conditional analytic bridge;
full Collatz OPEN.** The final refresh found substantial developments on
two branches after the heads used when this continuation began.

| PR | Latest head read | Material change |
|---|---|---|
| 177 | `a0a0d76f91b4e3846c1b1f0706cad56cb6098317` | Cofinal certified predecessors using gaps at most four; all high-gap interval states are covered under the common induction |
| 180 | `d0349de2108abb7c8fb8393c086610e3372df116` | Canonical least excessive envelope, harmonicization, fixed-basin sublinearity, and a Lean closing criterion requiring sublinearity only on the marked section |
| 184 | `366dab89ee9548084ab9b5e4e90ff82abf287a20` | Unchanged at this refresh |

The earlier CFJ source remains pinned at `cf91e46...`; its later development
is credited here. The claims below concern the named files and heads, not a
blanket verification of either PR.

## 1. The new deficit family is covered by PR177's high-gap rule

Our complete source word is `deficitWord D ++ [h]`, with

\[
B=22D+132,\quad t=21D+132,\quad d=244\,2^D-5,
\qquad h\ge B+3\ge135.
\]

The last inequality is a proved consequence of actual source legality.
PR177's `BOUNDED_GAP_ATTACK.md` and `BoundedGapCofinal.lean` cover any
complete source word containing a gap at least five. Apply
`high_gap_replacement` with the supplied prefix `deficitWord D`, the gap
`h`, empty retained tail, and requested bound `2m+1`. It returns a certified
source `p>2m+1` with an inserted prefix over `{1,2,3,4}` and a strictly
smaller complete grade. The wanted target stays `2m+1`, inside the new
source interval.

Consequently the family is a **covered comparison case under the common
induction hypothesis**. It is not a remaining obstruction to the latest
combined interval dispatcher. This does not assert unconditional convergence
of all these targets while that dispatcher's `LowIntervalStep` remains open.

The family still establishes an unconditional structural fact: raw clock
deficits are unbounded, even for prefixes over `{1,2,3,4}`. A proof based on
a uniform deficit bound is false; the newer high-grade replacement avoids
needing such a bound.

The actual arithmetic residual now has an initial even run in `{1,2,3}`,
every supplied odd gap at most four, and an odd target in `(S+1,2S+1]`.
The source word has no nonempty prefix with `2^(sum prefix)<=3^(length prefix)`
after the proved compensated-prefix deletions. The exact further valuation
and residue exclusions are in PR177's `LOW_INTERVAL_REFINEMENT.md` and
`BOUNDED_GAP_ATTACK.md` at the head above. Its word length is still unbounded.

## 2. PR180 already supplies a stronger closing interface

`MINIMAL_ENVELOPE_ATOM_REMOVAL.md` constructs the least excessive majorant

\[
V_0=g,\quad V_{k+1}=\max(g,PV_k),\quad
V=\lim V_k,\qquad g=1_{3\nmid q}.
\]

It proves absence of inverse-ray atoms by minimality, then defines
`G=lim_k P^k V` with `PG=G` and a positive uniform unit floor. Its heavy-tree
argument proves `V(n)/n -> 0` through the **entire predecessor basin of each
fixed ordinary target**. These are written analytic results, with their
source-qualified dependencies; this checkpoint does not claim to have
formally rebuilt them.

The same PR's `InverseDensityPotential.lean` already proves the short
two-parent arithmetic and additive transfer. `MarkedDensityPotential.lean`
proves `universal_of_marked_inverse_envelope_and_base`, requiring sublinearity
only on the forced constant-70 marked section, together with its explicit
finite base. Our `CriticalTrace.lean` supplies an independently compiled
general propagation/minimum interface; it is not a new stronger reduction
than this marked-only theorem. PR180's `ABEL_MARKED_UPPER_ATTACK.md` also
subsumes our fixed-discount bound by covering periodic targets as well.

## 3. Combining the constructions removes an additional analytic gap

The new canonical envelope controls the **whole actual Abel family**. With
`D_k=P^k 1`, the pointwise inequality `D_1<=2g<=2V` gives

\[
D_k\le2P^{k-1}V\le2V\quad(k\ge1),
\qquad
H_r=(1-r)\sum_{k\ge0}r^kD_k\le1+2V. \tag{1}
\]

At every fixed ordinary target, the parent sum of this majorant is finite:
`P(1+2V)=D_1+2PV<infinity`. Thus the actual Abel parent tails are uniformly
integrable. Every common pointwise Abel subsequential limit is **harmonic**,
and is bounded above by `2G`, so it inherits the absence of inverse-ray atoms
and fixed-basin sublinearity.

This resolves the parent-tail issue left open in our standalone excessive
profile construction. The short complete argument, its lower comparison with
`V`, and its exact dependency boundary are in
[ABEL_CANONICAL_COMPARISON.md](ABEL_CANONICAL_COMPARISON.md).
It uses the canonical majorant; the earlier linear height bound alone would
not justify the exchange of the Abel limit and the parent sum.

Fatou's lemma and leastness also compare `liminf_k D_k` and `limsup_k D_k`
between `alpha V` and `2G`. A depth-j spike persists at fraction `alpha/2`
at every depth `n>=j-1+k_0`. Consequently `sup_k D_k` is comparable with `V`,
and the whole finite-depth and Abel families inherit uniform sublinearity
inside each fixed ordinary predecessor basin. These statements still have
a root-dependent height cutoff.

The newly proved actual inverse Green estimate remains useful as a
pointwise row estimate with explicit floor decay. It neither sums all rows
nor makes the fixed-basin cutoff uniform when the target moves forward.

## 4. The remaining targets after this reconciliation

The analytic target is an upper bound for `G(q)/q`, uniform through all
**marked** ordinary units as `q` grows. The canonical envelope, all of its
fixed-root basins, and the Abel approximants are now connected; the missing
step is uniform control as that ordinary target changes. An explicit cutoff
and its finite basin certificate must also be supplied.

The arithmetic target is a successful `LowIntervalStep` for the complete
unbounded word language over `{1,2,3,4}` and the remaining low initial runs.
Our arbitrary-deficit family no longer belongs on that residual list.

The exact source-weighted primitive moment from the earlier checkpoint
remains a separate complete criterion that includes both escape and cycles.
None of the new statements proves that this moment tends to zero.
