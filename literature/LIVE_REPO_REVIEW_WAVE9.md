# Live repository review — wave 9

**Date:** 2026-07-29  
**Agent:** `gpt56-pro-03`  
**Scope:** global-blocker and latest six-branch, centered, and pulse work  
**Status:** literature/strategy audit; no native status promotions

No positive-integer Collatz counterexample, nontrivial positive cycle, or unconditional resolution is claimed.

## Latest work inspected

The pass focused on:

- PR #57 and PR #56 ordinary-extraction and foundry no-reduction theorems;
- PR #64 finite rational-section and semilinear-sanctuary rigidity;
- PR #65 finite algebraic-section closure;
- PR #66 complete two-point and sliding-linear-filter rigidity;
- PR #67 centered `64 -> 81` height-renewal work;
- PR #68 bounded transported run-core search;
- PR #70 three-pulse all-repetition theorem;
- the retained PR #13, PR #16, PR #19, PR #20, PR #45, PR #50, and PR #53 interfaces.

# 1. The six-branch chart is exactly a published approximate-multiplication problem

The native map is

\[
F(x)=\left\lceil {3^{12}x\over2^{19}}\right\rceil
\]

with canonical digit restricted to

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\}.
\]

The exact source-residue set is

\[
\mathcal S=
\{294912,331776,438784,297024,6472,466033\}.
\]

Thus the chart is precisely the Dubickas–Mossinghoff partial map

```text
x -> ceil(p*x/q) if x mod q belongs to S;
STOP otherwise,
```

with `(p,q,S)=(3^12,2^19,mathcal S)`.

This changes the external assessment. The six-branch problem is not merely a repository encoding. It is one explicit, unusually sparse instance of the long-standing approximate-multiplication termination question.

Dubickas–Mossinghoff prove singleton allowed sets terminate universally, but do not solve six-element sets. They also show that, because

\[
3^{12}<6\cdot2^{19},
\]

existence of a `Z_(3^12/2^19)`-number would force a nonterminating six-branch root. Subject to the native physical conjugacy, that would give a Collatz counterexample.

The likely direction remains negative: rational-base normality conjectures predict universal digit escape, not a survivor.

# 2. A strictly smaller target than least-root divergence has emerged

Write

\[
c=3^{12}-2^{19}=7153=23\cdot311.
\]

Then

\[
\boxed{
F(x)=x+\left\lceil {7153x\over524288}\right\rceil.}
\]

Its canonical digit is

\[
\delta(x)=524288\left\lceil {7153x\over524288}\right\rceil-7153x.
\]

Since `7153` is odd,

\[
\boxed{\delta(x)=0\iff 2^{19}\mid x.}
\]

Zero is not one of the six allowed digits. Therefore the entire chart is eliminated by the one-letter theorem

\[
\boxed{
\forall x>0\ \exists n:\ 2^{19}\mid F^n(x).}
\]

This is materially weaker than:

- full normality of every minimal word;
- equidistribution modulo every power of `2^19`;
- occurrence of every possible digit;
- or an explicit lower recurrence forcing `m_n -> infinity`.

It is now the cleanest negative target for PR #64/Q-7401.

The 2026 Andrieu–Eliahou–Vivion conjecture predicts every nonzero minimal word is normal and proves that normality is equivalent to full residue equidistribution. Their formulation of the Dubickas–Mossinghoff question is equivalent to occurrence of all letters. For this chart, just one occurrence of letter zero suffices.

A positive six-digit survivor would simultaneously disprove that normality conjecture for the base `3^12/2^19`.

# 3. Latest finite-section rigidity has a precise external envelope

PR #64 and PR #65 now rule out finite affine, rational, algebraic, and semilinear extraction schemes. PR #66 classifies all fixed two-point contractions and all fixed finite-window affine filters preserving the full six-digit alphabet.

Dubickas's 2009 theorem supplies the closest external umbrella:

```text
bounded fixed finite linear observable of the ceiling orbit
  iff
its coefficient polynomial is divisible by qX-p.
```

Consequently every bounded fixed linear observable factors through a finite convolution of the canonical digit word.

The same source proves the canonical digit word is not ultimately periodic and gives the exact complexity floor

\[
\liminf {p_d(L)\over L}
\ge
{\log(2^{19})\over\log(3^{12}/2^{19})}
=971.866577472\ldots .
\]

This does not subsume the native alphabet-preservation classification. It does show that the recent rigidity theorems are aligned with the canonical source theory: no fixed finite linear observable can reveal a simpler bounded arithmetic coordinate outside the digit word itself.

# 4. What the normality literature does and does not give

The recent rational-base preprint supplies a sharp conjectural picture:

```text
minimal words normal
 <=> ceiling orbits equidistributed modulo q^k for all k
 => every proper approximate-multiplication map terminates.
```

It also explicitly describes the general termination question as difficult.

For the repository this has two implications.

1. The six-branch target is externally meaningful and likely very hard; it is not obviously one elementary lemma short of resolution.
2. Full normality is unnecessary. The most disciplined research target is zero-digit occurrence in one base.

A useful positive or negative agent should therefore work on the hitting problem

```text
x -> x+ceil(7153*x/524288)
hits 0 mod 524288,
```

while preserving the actual integer root.

# 5. Centered `81/64`: the highest-value missing PDFs

PR #67 advances the native centered-height recurrence, but the most relevant external papers remain only abstract-level audited:

1. Dubickas 2006 — exact nearest-integer large/small limit-point constants in terms of `p,q` and Thue–Morse;
2. Dubickas 2008 — two-interval exclusions for rational powers;
3. Dubickas 2009 — impossibility of confinement to a small interval.

The next source pass should not rely on remembered formulas. It must extract:

```text
the exact (81,64) constant;
strict versus non-strict endpoints;
equality cases;
the extremal sign/Thue-Morse language;
translation to native appended blocks q_K.
```

The user has offered to acquire inaccessible PDFs. These three papers are the highest-priority request.

# 6. Pulse/cycle work: move from crude cutoffs to an effective logarithmic pipeline

PR #70 and PR #53 now expose fixed-support pulse equations in which pulse coordinates are capped and repetition is the remaining unbounded parameter.

The correct external ladder is:

```text
native exact resultant or divisibility identity
 -> Archimedean linear form in log 2 and log 3
 -> explicit Matveev cutoff
 -> p-adic two-log bound where the residual has high valuation
 -> de Weger lattice reduction
 -> certified continued fractions / exact replay.
```

Relevant sources are:

- Matveev 2000 for the initial explicit real bound;
- Bugeaud 2002 for simultaneous non-Archimedean estimates;
- Chim 2025 for sharper explicit two-term p-adic bounds;
- de Weger 1987 for practical real and p-adic LLL reduction.

The exact Matveev normalization used in PR #70 has not yet been source-checked by this agent. The full English PDF should be supplied before status promotion.

Zero resultants and proper vanishing subsums should be isolated as constructive resonant families, not discarded as exceptional solver rows.

# 7. The Väänänen–Wallisser source remains correctly scoped

The supplied 1991 paper proves a quantitative p-adic linear-independence measure for a fixed finite vector of Tschakaloff values in distinct multiplicative orbits, under an explicit dimension-dependent numerical condition.

It remains valuable for:

- periodic stack tails;
- finite-dimensional prescribed controllers;
- exact Padé determinant nonvanishing.

It does not provide:

- ordinary least-root boundedness;
- zero-digit occurrence in a rational-base minimal word;
- or a period-uniform infinite-dimensional extraction theorem.

# 8. Recommended next work

## Priority 1 — zero-digit hitting theorem

Attack only

\[
\forall x>0\ \exists n:\quad
F^n(x)\equiv0\pmod {2^{19}},
\qquad
F(x)=x+\left\lceil {7153x\over524288}\right\rceil.
\]

A proof eliminates the complete six-branch architecture. A counterexample is already an all-time orbit avoiding one digit but must still be checked against the other five-digit restrictions before becoming a Collatz candidate.

## Priority 2 — source-acquire the centered trilogy

Obtain and inspect the three Dubickas PDFs listed above. This could turn PR #67's native recurrence into an exact source-threshold/equality-language theorem.

## Priority 3 — source-audit PR #70

Acquire Matveev 2000 and check every constant. If valid, add a de Weger/LLL reduction layer rather than accepting a huge theoretical cutoff as the final finite range.

## Priority 4 — subalphabet hierarchy

Because singleton allowed sets terminate, classify the physical subalphabets of sizes two through five. This will not solve the full six-letter chart but can reveal whether one specific interaction is load-bearing.

## Priority 5 — no more finite linear recodings

PR #64–#66 plus Dubickas 2009 have largely exhausted fixed finite linear/rational extraction. New positive work must retain an actual unbounded root state; new negative work should attack digit occurrence or least-root escape directly.

# Bottom line

The latest literature does not solve the remaining global blocker. It does sharpen it substantially:

\[
\boxed{
\text{Prove one digit—zero—appears in every positive minimal word of one explicit base.}}
\]

That theorem is strictly weaker than the leading rational-base normality conjecture, eliminates the entire six-branch Collatz architecture, and is now the cleanest literature-connected negative target in the repository.