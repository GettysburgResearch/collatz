# Why a global selector must make genuine target progress

## Outcome of this attack

The universal coupled selector was not proved. The new unconditional result
rules out a whole proposed replacement for it: a selector that always keeps
the target fixed and pays solely by choosing another complete source at a
lower grade, or a larger source at the same grade.

There are **arbitrarily large actual low-domain source certificates** for
which neither move is possible at the psi target `2S-1`. The result covers
all complete alternative certificates, with arbitrary length, arbitrary
prefix insertion, and arbitrary suffix changes. It is not a finite search
bound or an obstruction to one rewrite catalogue.

`Collatz.SourceRecords` proves this statement in Lean core. It does not
prove a new target-descent estimate, refute `MixedCover`, or claim that
these targets fail to converge. A target-changing merger, ordinary target
descent, or an independent basin proof remains available in principle.

## 1. Exact order and source records

The inherited complete-source grades are

\[
\Gamma(e;W)=([2e+1]\text{ if }e>0\text{, otherwise }[])
             \mathbin{++}\operatorname{map}(2\cdot,W).
\]

For finite lists `new,old`, the existing strict relation `Less new old`
means that at some grade `a` the new multiplicity is smaller, and every
multiplicity strictly above `a` is unchanged. It is the original
well-founded multiset relation from PR177, not a numerical estimate of the
source's size. Permuting a grade list does not change its comparisons.

A **record** is a supplied complete powered certificate `(S,e,W)` such
that:

1. Every complete powered certificate of grade strictly below
   `Γ(e;W)` has source strictly smaller than `S`.
2. Every complete powered certificate whose grade multiset is a permutation
   of `Γ(e;W)` has source at most `S`.

The first condition is strict. It excludes a lower-grade certificate for
the same numerical source as well as a larger source. This distinction is
needed by the unchanged-target argument below.

## 2. Records are cofinal

### Finite ceiling at a fixed grade

For a complete odd certificate,

\[
3^{|W|}q+C(W)=2^{A(W)},\qquad C(W)\ge0.
\]

Since `3^|W| ≥ 1`, this gives `q ≤ 2^A(W)`. Hence every complete
powered source `S=2^e q` satisfies

\[
S\le2^{e+A(W)}\le2^{\sum\Gamma(e;W)}.
\]

The sum is preserved by a grade permutation. Thus all actual source
values in one fixed multiset class form a nonempty bounded subset of the
natural numbers whenever that class is represented. Such a subset has a
maximum. The ceiling is the same elementary observation used by fresh
PR180 to justify its finite source defect; the new module derives it
directly from the existing complete affine certificate.

### Well-founded selection, followed by a bounded maximum

Fix any natural threshold `N`. The powers of two have complete powered
certificates, so some certified source exceeds `N`.

Consider the grade lists for which a complete source above `N` exists.
Well-foundedness supplies a **minimal** such list `G`: no strictly smaller
grade list represents a source above `N`. No theorem that the list
representation is a linear order is needed; minimality is sufficient.

Now take the largest source `S` represented in the permutation class of
`G`, using the finite ceiling. This maximum is at least the already
supplied source above `N`, so `S>N`. Every source at a strictly lower grade
is at most `N`, hence strictly smaller than `S`. Every source at the same
multiset is at most `S` by the maximum choice. Extracting one actual
certificate at that maximum gives a record.

This is `cofinal_records`. The proof does not take a maximum over an
unbounded grade downset or assume that all bounded-alphabet inverse trees
are finite. It maximizes only within one fixed grade class after the
well-founded selection.

## 3. Every nontrivial record is in the actual low domain

Two preexisting source theorems are used exactly as stated.

First, `CollatzGapMultiset.ordinary_step` takes any supplied complete source
certificate with `S≠1` to an actual complete certificate for `T(S)`, with
strictly smaller grade. If a record `S>1` were odd, then

\[
T(S)=\frac{3S+1}{2}>S,
\]

contradicting the record's lower-grade bound. Therefore `S` is even. The
odd core of a powered certificate is odd, so its initial exponent is at
least one.

Second, the existing cofinal replacement theorems show that either an
initial exponent at least four or an odd gap at least five funds a
strictly lower-grade complete source above **any requested bound**. Apply
them with requested bound `S`. Their resulting larger source contradicts
the record property.

Consequently every record `S>1` has

\[
1\le e\le3,\qquad a\le4\quad(a\in W),\qquad S\text{ even}.
\]

This is `record_low_domain`. The high-gap exclusion uses the actual
arbitrary-tail replacement, so a high gap deep inside the word is covered
as well as one at its head.

These are the syntactic premises of the low-domain dispatcher. The result
does not assert that every such record is unclassified by the existing
target-changing rules, or that every record lies in the remaining
head-three affine subfamily.

## 4. The unchanged-target handoff is impossible

Let `(S,e,W)` be a record with `S>2`, and retain its target

\[
t=2S-1.
\]

Suppose a new complete source `C` covers this unchanged target in the
ordinary interval:

\[
0<t\le2C+1.
\]

Thus `C≥S-1`.

### Strictly smaller grade

The record bound gives `C<S`, so the only possible value is `C=S-1`.
Since `S` is even and `S>2`, this child is odd and strictly greater than
one. Its actual next ordinary step is

\[
T(C)=\frac{3(S-1)+1}{2}=\frac{3S}{2}-1>S.
\]

The supplied certificate of `C` gives a strictly lower-grade certificate
for this step. By transitivity it is still strictly below the original
grade. This contradicts the original record bound. Therefore no
lower-grade complete source covers the unchanged target.

The condition `S>2` is necessary: at `S=2`, source one covers target
three, and source one is terminal. The theorem deliberately excludes this
case.

### Equal grade with source enlargement

The record's equal-grade maximum gives `C≤S`. The permitted finite-defect
move requires `S<C`. Those conditions contradict each other.

A replacement with `C=S` at the same grade and the same target is not a
recursive move in the current combined order: it changes neither the
grade, the finite source defect, nor the target. Merely relabeling its
certificate does not supply a strict decrease. The formal definition
`SourceOnlyStep` therefore excludes that no-progress case explicitly.

These two arguments prove `record_no_source_only_psi`.

### Global consequence

For every `N`, `cofinal_source_only_obstruction` supplies a source `S>N`
with `S>2`, a complete certificate, `1≤e≤3`, all gaps at most four, and
the activated odd target

\[
S+1<2S-1\le2S+1,
\]

for which no unchanged-target move of either permitted source type exists.
Thus those two source mechanisms cannot alone be a universal selector.
Even a block passing through larger intermediate grades cannot evade this
particular conclusion if its final unchanged-target handoff is required to
use one of the two excluded endpoints.

## 5. Written corollary for other source orders

The obstruction is more general than this particular histogram. Let
`Cert` be any type of complete source certificates, with numerical source
`s(c)`, such that certified source values are cofinal. Suppose a
well-founded strict order on these certificates has the following
property: for every certificate of an odd source greater than one, an
actual certificate of its next ordinary source exists strictly below it.
Assume the order is transitive, or use its transitive closure for the
following selection; the transitive closure of a well-founded relation is
well-founded.

For any natural threshold `B≥2`, choose a minimal certificate `c` among those with
`S=s(c)>B`. An odd `S` would have an actual next source greater than `S`
with a smaller certificate, contradicting minimality. Hence `S` is even.
If a strictly smaller certificate with source `C` covers the unchanged
target `2S-1` under the interval ceiling `2C+1`, then `C≥S-1`. When `C>B`,
minimality is contradicted immediately. Otherwise the inequalities force
`C=B=S-1`. This is an odd source greater than one, and its next source is
`3S/2-1>S>B`. Its certificate is below the certificate of `C`, hence below
`c` by transitivity, giving the same contradiction.

Thus **every such well-founded certificate order has cofinally many
unchanged-target source-descent obstructions**. This is a written
corollary, not an additional Lean declaration in this packet. It applies
to redesigned source orders only when all the stated properties hold;
in particular, ordinary odd forward steps must strictly decrease that
same order. It does not cover free certificate resets, changed interval
ceilings, genuine target movement, or a new source order that omits this
forward-step property. The formal four-theorem result above additionally
places its records in the actual low domain `1≤e≤3`, all gaps at most
four, and also excludes the existing same-grade source-enlargement move.

## 6. Coupled attack and the first unsupported step

The fresh PR180 reduction was used to avoid repeating the earlier
unbounded-valuation analysis. Its remaining formal head-three family is

\[
q=256j+173,\quad u=96j+65,\quad w=54j+37,
\]

with the supplied prefix `[3,2,2]`, original target `n=2048j+1383`,
and exact target state

\[
T^{10}(n)=243w-122=6(2187j+1478)+1.
\]

The smaller partner already proves convergence of `2187j+1478`. The
missing assertion is the successful return of its larger companion while
retaining the original source budget. I did not prove that assertion.

Two proposed complete repairs were tested and rejected before promoting
them to proof premises. Arbitrary equal-grade permutations need not
enlarge a remaining source. The stronger proposed repair `q→q+4` can
introduce a gap five even when the supplied original word has only gaps at
most four. These observations motivated the record theorem above; no
numerical search is a dependency of that theorem.

On a record, deleting a nonempty source prefix cannot expose an equal or
larger odd source, since retaining the initial even exponent would then
give a forbidden lower-grade source. This supplies strict coefficient
contraction of every such prefix. It does not imply that the complete
word contains a sufficiently long repeated block. Balanced aperiodic
words are not excluded by prefix coefficient inequalities alone.

The attempted continuation was to prove a structural description of
record words forcing a contracting rational shadow for the actual target.
No finite grammar, pumping theorem, or all-parameter carry decrease for
those record words was established. A periodic-block compiler cannot be
invoked until its block occurrence and full clock/debt budget are proved
for this class. This is the first unsupported step of that continuation.

The result directs further proof search to genuine target progress on the
record queries. It is not presented as progress on the positive target
descent estimate itself. The broader arbitrary-target `MixedCover`
obligation also remains open; finishing one psi branch has not been
identified with full interval completeness.

## Dependencies and verification

The new module imports only `Collatz.BoundedGapCofinal` and its existing
Lean-core closure. Its mathematical dependencies are the complete affine
certificate identity, `less_wellFounded`, permutation invariance and
transitivity of `Less`, `ordinary_step`, `large_even_replacement`, and
`high_gap_replacement`. The imported files are the byte-identical PR177
sources pinned at `a0a0d76f91b4e3846c1b1f0706cad56cb6098317`.

Fresh source comparisons were PR177
`8ef9bf0d828fc533721dee1f90c5d78fac80ad39` and PR180
`ab3973099f0d285bbe88972382ad599bb02cd460`. The finite source ceiling is
credited to the latter's `MIXED_COVER.md` / `MixedCoverAttack.lean`
interface; the obstruction proof is new to this packet. Neither refreshed
project was imported or independently replayed for this module.

There are four public theorem declarations, all audited in
`AuditSourceRecords.lean`. The source and audit are compiled with Lean
4.34.1 core, `-j1 -DwarningAsError=true`. The receipt records exit codes,
the exact minimal dependency closure, hashes, and standard-axiom audits.
There is no new axiom, `sorry`, finite verification cutoff, or claim of
full Collatz.
