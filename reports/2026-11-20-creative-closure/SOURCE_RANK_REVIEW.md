# Review of the fixed-rank carry obstruction

**VERIFIED within its canonical-input scope.** The reviewed manuscript is
`research/creative-closure-20261120/source_rank.md`, CSR-001, SHA-256
`bc0c2253e8d6c917341c9091a344c5ca5955afb7a30fccaf7ccee0fa9b17b722`.
The root reviewer reconstructed the argument separately, checked its
latest-source direction, and supplied the distinct literal-rule controls
below. This is an internal AI review, not external acceptance or formal
proof-assistant verification. Collatz remains open.

## Marked-token invariant

At an odd canonical binary input, there is no administrative rule to
apply and the terminal dynamic rule is necessarily `bd -> gd`. Mark that
ternary token. No rewrite exchanges two ternary tokens, and a dynamic
rule acts only at the right boundary. All later created ternary tokens
therefore remain to its right. While the marked token survives, no rule
can modify a binary letter to its left except its own crossing of that
letter. Its eventual deletion at the left boundary is necessary for a
complete derivation to `cd`.

This proves the stated scanning order under arbitrary interleaving, not
only a schedule that fully normalizes after every odd event. There is no
assumption that a complete derivation exists. On any such derivation, all
forced exceptional transitions of the marked token count against the same
original allowance.

## The two known-convergent families

For the rank-two family the two accelerated valuations follow immediately
from the displayed equations. Summing its repeated six-bit blocks gives
the binary identity. Scanning one full block or the shortened initial
block in the six actual binary/ternary rewrite rules gives exactly one
exceptional crossing and returns the token to `g`. Thus every complete
derivation requires at least `t`, even though the first-hit odd rank is
always two. This is stronger than merely showing a large count under one
preferred rewrite schedule.

For the PR146 antecedents, put `B=2^54`. The block decomposition follows
algebraically from

\[
3B^j+\frac{13(B^j-1)}{81}-2
=\frac{256B^j-175}{81}.
\]

All blocks lie in the displayed 54-bit range. The three initial
odd/even pairs have exact valuation two and the last odd numerator is a
power of two, so the supplied first-hit odd rank is exactly four. Direct
literal-rule reconstruction verifies nine exceptional crossings in the
last block and in every repeated block, with the indicated carry states.
The remaining leading binary one makes no exceptional crossing. The
conclusion `>=9j` counts only the first token and need not be the minimum
total count.

## The pure-power targets

The valuation identity for powers of nine has an elementary induction:
`9-1` has valuation three, and each successive squaring multiplies the
difference by a factor congruent to two modulo eight. Thus the order of
9 modulo `2^H` is exactly `2^(H-3)`. Its powers lie in `1 mod8`, a set of
that cardinality, and exhaust it. Since 27 is a unit modulo this order,
the progression `9^(27q+13)=3^(27(2q+1)-1)` attains every required low
binary residue for infinitely many positive indices.

Choosing indices with sufficiently many higher bits leaves the whole
prescribed low block strictly below the left boundary. The first token
must cross all those blocks before it can reach any higher digits. This
forces arbitrarily many exceptional crossings on a subsequence of the
required targets. It does **not** certify their ordinary convergence.

Combining this obstruction with the already proved termination of the
fixed-budget controller is legitimate: every maximal admitted schedule
is finite; a budget smaller than the forced count cannot end at `cd`;
its terminal outcome must therefore be UNRESOLVED. This conclusion holds
even though unrestricted rewrite termination on those target sources is
the unresolved problem.

The latest PR146 bounded-rank merger theorem starts with the opposite
certified arm from its deep reverse family. No deadline is reversed here,
and no partner stopping certificate is inferred when a lifted-merger test
fails. The argument excludes a uniform allowance based only on fixed
antecedent rank or the fixed pre-halving parity template. It leaves
source-specific allowances and alternative mixed representations open.

## Actual independent controls

[`source-rank-independent.py`](source-rank-independent.py) imports no
author checker. It derives token transitions from the six literal
rewrite strings, checks both printed 54-bit blocks, and verifies 18
actual ordinary first-hit certificates: twelve rank-two and six rank-four
members. It also constructs three explicit exponent indices satisfying
the pure-power congruences by modular arithmetic. Those controls do not
iterate or assume convergence of the pure-power targets.

Normal generation and optimized comparison actually passed. The retained
[report](source-rank-independent-report.json) has SHA-256
`7fb33df505f96d36f9a29a1e710126a0b24dd9f7cffba138abe8ffacb4d85a57`.
Finite checks validate the fixed block certificate and implementations;
the all-parameter statements use the written invariant and valuation
proofs above. Publication receipts separately identify complete-checkout
executions.

```sh
python -X utf8 -B reports/2026-11-20-creative-closure/source-rank-independent.py --compare reports/2026-11-20-creative-closure/source-rank-independent-report.json
```
