# LIT-KTHM-0057 — One zero digit eliminates the six-branch chart

**Status:** `ELEMENTARY EXACT REDUCTION + CONJECTURAL LITERATURE BRIDGE`  
**Source bridge:** Mélodie Andrieu, Shalom Eliahou, and Léo Vivion, *A Normality Conjecture on Rational Base Number Systems*, arXiv `2510.11723`, version 2 dated 7 April 2026  
**Source inspection:** complete accessible preprint, including Conjectures 1.3/1.6, Theorem 1.7, Question 3.15, Proposition 3.16, and Remark 3.17  
**Native interface:** PR #64 `D-7401/Q-7401`  
**Counterexample status:** no Collatz counterexample is claimed

## Exact arithmetic reduction

Put

\[
P=3^{12}=531441,
\qquad
Q=2^{19}=524288,
\qquad
c=P-Q=7153=23\cdot311.
\]

For

\[
F(x)=\left\lceil {Px\over Q}\right\rceil
\]

one has

\[
\boxed{F(x)=x+\left\lceil {cx\over Q}\right\rceil.}
\tag{1}
\]

The canonical rational-base digit is

\[
\delta(x)=QF(x)-Px.
\]

Using `(1)`,

\[
\boxed{
\delta(x)=Q\left\lceil {cx\over Q}\right\rceil-cx.}
\tag{2}
\]

Because `gcd(c,Q)=1`,

\[
\boxed{
\delta(x)=0
\iff
Q\mid x.}
\tag{3}
\]

The six allowed physical digits are

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\},
\]

so `0` does not belong to `A`.

Therefore:

\[
\boxed{
\forall x>0\ \exists n\ge0:\ Q\mid F^n(x)
\Longrightarrow
\text{the six-branch architecture has no positive all-time root}.}
\tag{4}
\]

Equivalently, it is enough to prove that every nonzero minimal word in the single rational base `P/Q` contains the one letter `0` at least once.

This is a much smaller negative target than normality, equidistribution, or occurrence of every digit.

## Literature bridge

Andrieu–Eliahou–Vivion conjecture that every nonzero minimal word in rational base `p/q` is normal over the alphabet

\[
\{0,1,\ldots,q-1\}.
\]

They prove that this normality conjecture is equivalent to equidistribution of every positive ceiling-map orbit modulo every power of `q`.

They also recall the Dubickas–Mossinghoff approximate-multiplication question and prove that their normality conjecture would imply universal termination for every proper allowed residue set. Their Remark 3.17 identifies that termination question with occurrence of every letter in every minimal word.

For the six-branch chart, full normality is unnecessary. The single-letter statement

\[
\boxed{
0\text{ occurs in every positive }P/Q\text{ minimal word}}
\tag{5}
\]

already implies `(4)`.

## Positive-side consequence

A positive all-time six-branch root would have a minimal word supported on only six of the `Q=524288` possible digits. It would therefore disprove the Andrieu–Eliahou–Vivion normality conjecture for the base

\[
3^{12}/2^{19}.
\]

Subject to the native physical conjugacy, it would simultaneously provide a Collatz counterexample.

Thus the chart sits at a sharp intersection of two open problems:

```text
six-digit survivor
  -> Collatz counterexample;
  -> counterexample to rational-base minimal-word normality.
```

## Why this gains ground

The global least-root question can now be attacked through one concrete hitting statement:

\[
\boxed{
F^n(x)\equiv0\pmod {2^{19}}
\text{ for some }n.}
\]

No occurrence frequencies or arbitrary forbidden digits are needed.

The additive normalization `(1)` also removes the large rational multiplier from the statement:

\[
F(x)=x+\left\lceil {7153x\over524288}\right\rceil.
\]

A proof may therefore target the first hitting time of one explicit lattice under an increasing integer map.

## Applicability audit

- The normality and equidistribution statements are conjectural and are not used as theorems.
- Equations `(1)`–`(4)` are elementary exact identities.
- The implication from a six-branch survivor to a Collatz counterexample remains branch-qualified to the physical chart theorem.
- Hitting digit zero is sufficient for chart exit; it is not necessary, because any digit outside `A` also exits.

## Gap audit

- No theorem currently proves `(5)` even for this one base.
- The recent normality paper presents the broader all-letter problem as difficult.
- Finite richness or discrepancy data cannot prove eventual occurrence for every seed.
- Proving that almost every root hits zero does not decide every ordinary root.

## Suggested next attack

Attack the exact one-letter theorem rather than full normality:

```text
For every x>0,
F(x)=x+ceil(7153x/524288)
hits a multiple of 524288.
```

Potential proof objects should preserve the actual ordinary root. Suitable directions include a descent on the first hitting obstruction, a source-specific residue-renewal identity, or a contradiction from an orbit avoiding one lattice forever. A finite-state or periodic controller is already excluded by the native and imported rigidity theorems.