# Direct closure attempt: what failed and what was proved

**Checkpoint 11, 22 November 2026. Full Collatz remains OPEN. No positive
global closing estimate was obtained in this pass.** The work targeted the
universal coupled selector and the elimination of one fixed ordinary
escaping source. Its two new results rule out proposed ways of completing
those arguments; they do not establish either missing conclusion.

The source convention is the shortcut map `T(n)=n/2` for even `n` and
`T(n)=(3n+1)/2` for odd `n`. For positive odd states, `U` divides `3n+1`
by its full power of two. A complete source certificate is an actual
finite ordinary path to one. Every source considered in the record theorem
is therefore already certified to converge; its associated target is a
separate integer.

## 1. A universal source-only selector is impossible

[SOURCE_RECORDS.md](SOURCE_RECORDS.md) proves that there are arbitrarily
large complete source certificates `(S,e,W)` with

\[
S>2,\qquad 1\le e\le3,\qquad a\le4\quad(a\in W),
\]

for which the active target `t=2S-1` cannot be handed off unchanged using
either a strictly lower-grade complete source or a larger complete source
of the same multiset grade. Here the inherited grade is

\[
\Gamma(e;W)=([2e+1]\text{ if }e>0\text{, otherwise }[])
                \mathbin{++}\operatorname{map}(2\cdot,W).
\]

**The quantifier covers all complete alternative certificates**, of any
length, with any prefix or suffix changes. It does not range only over a
finite rewrite dictionary.

The proof chooses a minimal grade admitting a source above a prescribed
threshold, then maximizes the source within that grade class. The latter
maximum exists because a complete source satisfies
`S <= 2^(sum Gamma)`. Such a record is even, since an odd record's actual
next step would be a larger source of smaller grade. The preexisting
cofinal replacement theorems exclude every initial exponent at least four
and every gap at least five, even deep in the supplied word.

If a lower-grade source `C` covered `2S-1` under the ceiling `2C+1`, it
would have to be `S-1`. Its actual odd step would then produce the larger
source `3S/2-1>S` at still smaller grade, a contradiction. Same-grade
enlargement is excluded by the maximum choice.

The companion written corollary extends the obstruction to any transitive
well-founded certificate order with the stated odd-forward-step property
and the same interval ceiling. That extension is not an extra Lean claim.

**Consequence for the proof attempt:** source changes of these types cannot
replace genuine target progress universally. The theorem does not refute
`MixedCover`, show that any target fails to converge, or say that these
records evade every existing target-changing rule. It also does not place
all records in one unresolved head-three family.

The four public record theorems and their complete actual grade scope are
in [SourceRecords.lean](lean/Collatz/SourceRecords.lean), with
[explicit axiom audits](lean/AuditSourceRecords.lean).

## 2. Literal prefix copying cannot provide uniform source-weight amplification

[FIXED_SOURCE_SIBLING_LIFTS.md](FIXED_SOURCE_SIBLING_LIFTS.md) considers an
arbitrary actual odd word of length `s` and total binary clock `A`, taking
`p` to `q`:

\[
2^Aq=3^sp+C,\qquad C\ge0.
\]

The ordinary siblings `q[j]=4^j q+(4^j-1)/3` have the same next odd image.
Pulling a sibling back through the **identical supplied word** gives

\[
p[j]=4^jp+\frac{(4^j-1)(3C+2^A)}{3^{s+1}}.
\]

Exactly,

\[
p[j]\in\mathbb Z\iff 3^s\mid j.
\]

Every integral lift really has positive odd intermediate states and the
same exact valuations. For a nonzero legal index,

\[
p[j]\ge4^{3^s}p,\qquad
\sum_{\substack{j\ge1\\3^s\mid j}}p[j]^{-2}
\le\frac{p^{-2}}{16^{3^s}-1}.
\]

Thus the permitted copies become too expensive in original source weight
to supply a positive depth-independent amplification by this construction.
The exact source-unit guard is retained: integral copies need not be
ternary units. The sum remains valid after restricting to unit sources.

The all-depth divisibility, affine identities and height bounds are
formalized in [SiblingPrefixLift.lean](lean/SiblingPrefixLift.lean).
Actual trajectory legality, the unit congruence and the infinite geometric
sum have written proofs. This is **not** an upper bound on the accumulated
canonical potential `G` or component mass `nu`, and it does not rule out
different-word constructions.

## 3. Where the direct positive attempts stopped

[DIRECT_FLOW_ATTEMPTS.md](DIRECT_FLOW_ATTEMPTS.md) records the attempted
contradictions and their first unsupported steps:

- An explicit sibling at every escaping spine point gives a genuine
  possible harmonic amplification. A uniform comparison between the
  canonical potentials of those siblings was not proved. The copying
  calculation above blocks one attempted proof of that comparison; it
  does not prove the comparison false. Its stated harmonic domain kills
  periodic states, so a cycle argument remains separate.
- The available parity-count saving is too weak to exclude the atom of
  one fixed original source. Repeated use at longer clocks would require
  a distribution statement that the present inputs do not supply.
- The fresh contact-time contraction and resolvent factorization retain
  the last escaping excursion. No legitimate clock change or inversion
  in those results removes that source.

The coupled arithmetic attack used the fresh PR180 family

\[
q=256j+173,\quad w=54j+37,\quad n=2048j+1383,
\qquad T^{10}(n)=243w-122=6(2187j+1478)+1.
\]

Convergence of the smaller partner `2187j+1478` is supplied there. This
pass did not prove the required return for the larger companion. Nor did
it derive a word structure for all source records that would force such
a return. Completing this branch would still require connection to the
full arbitrary-target coverage obligation.

These are failures of specific proof attempts. The new mathematical
contribution is the two obstructions above, not a reduction in the
remaining positive global estimate.

## Sources, review and replay

[SOURCES_AND_REVIEW.md](SOURCES_AND_REVIEW.md) freezes the read-only source
heads, exact claims used, independent review and evidence boundaries.
[DEPENDENCIES.json](DEPENDENCIES.json) pins the complete formal import
closure: thirteen existing Lean-core modules, the new record module and
its audit, and the standalone Mathlib sibling module. Earlier proof
packets are not rerun beyond these exact imports.

With the pinned Lean and Mathlib installations, reproduce the build with:

```sh
python -X utf8 -B research/lean-global-resolvent-20261121/overview/central/check_central.py \
  --lean /path/to/lean-4.34.1-linux/bin/lean \
  --mathlib /path/to/mathlib4 \
  --out /tmp/collatz-central-fresh \
  --receipt /tmp/collatz-central-receipt.json
```

The output directory must be absent or empty. The driver checks source
hashes before and after compilation, uses warnings as errors and audits
every new public theorem. The execution record and its exact scope are in
[the checkpoint report](../../../../reports/2026-11-22-central-attempt/README.md).
