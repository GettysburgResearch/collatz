# Carry blocks across marked returns

This attempt starts from PR173 head
`fa0c9e2a2851e6324391e39c17afcb5913185aec` and targets descent across the
large increasing returns constructed in `RisingReturns.lean`.

## Exact positive result

For a positive integer `n`, write `n+1 = 2^r q`, where `q` is odd, and set

\[
H(n)=3^r q.
\]

Every one of the next `r` shortcut steps is part of the same rising odd run.
For `0 <= j <= r`, the exact identities are

\[
T^j(n)=2^{r-j}3^j q-1,
\qquad H(T^j(n))=H(n),
\qquad T^r(n)=H(n)-1.
\]

Thus every marked return occurring inside this run has the same natural-number
carry height, even when its ordinary size is much greater than the initial
marked point. This removes those rising returns from the accounting without
claiming they descend.

The source is `CarryBlocks.lean`. `CarrySection.lean` connects the invariant
directly to PR173's actual `next` and `returnTime` definitions. It uses the
original shortcut orbit, not an altered map.

## The exact boundary that still needs repayment

At the even endpoint `H-1`, remove all its `a` factors of two. Let the next
odd point have `s` trailing one bits and odd cofactor `v`. Then

\[
H-1=2^a(2^s v-1),\qquad
H+2^a-1=2^{a+s}v,\qquad H_{\rm next}=3^s v.
\]

In particular, the signed change is

\[
H_{\rm next}-H=(3^s-2^{a+s})v+2^a-1.
\]

The additive term `2^a-1` must remain in the accounting. This map does have
expanding resets: `H=63, a=1, s=5, v=1` gives `H_next=243`. These values are
on the ordinary orbit beginning at 27: the first full rising run ends at 62,
one halving reaches 31, and the next full rising run ends at 242.

**First unproved step:** prove that changing successive reset pairs `(a,s)`
cannot sustain carry height at or above its initial nonterminal value forever.
The band recurrence supplies no bound yet on the new trailing-one depth `s`
relative to the halving depth `a` at these reset points. The invariant alone
therefore does not establish full Collatz.

## Why the offset induction did not close

For `x=2^d+u`, the lower trajectory controls at most `d` shortcut parity bits:

\[
T^j(x)=3^{p_j(u)}2^{d-j}+T^j(u),\qquad 0\le j\le d.
\]

The band bounds `u/x` by order `1/d`; it does not bound the first contraction
clock of `u` by `d`. Long trailing-one tails can exhaust the precision before
they contract. The carry height groups exactly those growing prefixes, but
their later resets still require the repayment assertion above.

## Replay status

The current `lean/CarryBlocks.lean` and `lean/CarrySection.lean` both compile
under Lean 4.34.1 with warnings treated as errors. Their printed axiom lists
contain only `propext`, `Classical.choice`, and `Quot.sound`. The complete
packet replay and source hashes are recorded in
`../../reports/2026-11-21-forward-band-closure/lean-check.json`.

An earlier resource-related import stall was resolved before this result was
accepted. No `sorry` or conjectural axiom is used.
