# L-0111 — Multi-chart schedules still pay 2-adic tax at every chart entry

Claim ID: `L-0111`  
Title: Variable \((M,N)\) / multi-chart transitions do not cancel prefix taxes  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `T-0101`, `T-0102`  
Scope: schedules that change accelerated length/weight between blocks  
Related counterexample candidates: none (obstruction / accounting)

## Statement

Consider a schedule \(\sigma=(w_i)_{i\ge1}\) where the blocks may have
**distinct** lengths \(L_i\) and weights \(a_i\) (a “multi-chart” or
variable-radix schedule). Let \(\Lambda_N=\sum_{i\le N}L_i\).

Then for every \(N\):

1. The followers of the length-\(N\) prefix form a single cylinder of modulus
   \(2^{\Lambda_N}\) (`T-0101`(B) applied to the concatenation).

2. Under generic odd transport, the cumulative tax equals \(\Lambda_N\)
   (`T-0101`(A)).

3. Changing chart — i.e. changing \((2^{L_i},3^{a_i})\) from one block to the
   next — does not refund prior tax. Chart changes may alter the image step’s
   odd modulus \(3^{a_i}\) and the real expansion factor, but the next enabling
   constraint of length \(L_{i+1}\) still costs \(L_{i+1}\) bits when the current
   step is odd.

Therefore multi-chart designs evade `T-0101` only if they introduce a mechanism
outside pure 2-power enabling constraints (e.g. growing prepaid state /
growing digit geometry, or a non-residue certificate format).

## Motivation

Answers the natural generalization of `L-0104`’s two-port drain to arbitrary
variable-length pipelines — the multi-chart groupoid idea without claiming
that groupoid fails, only that it still pays tax.

## Proof

The concatenation of the first \(N\) blocks is one chronological word of length
\(\Lambda_N\), regardless of intermediate chart labels. Apply `T-0101`(A)–(B).
Odd transport between blocks is `L-0106`.

## Gap audit

- Does not prove multi-chart regeneration is impossible — only that tax
  accounting persists.
- Growing prepaid modulus \(A_N\to\infty\) along the certificate (not along the
  integer’s orbit constraints alone) is exactly the “growing geometry” escape
  hatch.

## Adversarial tests

`X-0114` multi-length random schedules: tax equals sum of lengths.

## Suggested next attack

Bridge: growing geometry must increase usable prepaid state faster than tax
accumulates — rephrase collision-fiber `Q-0010` in tax language.
