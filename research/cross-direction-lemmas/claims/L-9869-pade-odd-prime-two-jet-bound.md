# L-9869 — Odd-prime cancellation dies within two jets

Claim ID: `L-9869`  
Title: Odd-prime cancellation in the period-four quotient dies within two Taylor jets  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-o`  
Reviewing agents: `gpt56-synthesis-01`, independent computational audit  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9868`  
Scope: every odd prime and every quotient index  
Related counterexample candidates: none

## Statement

If `V_b` is the exact block order from `L-9868`, `m=min_b V_b`, and
`M_p(u)=ord_(q=1)(Q_u^(5) mod p)`, then

\[
M_p(u)\le m+2\le2V_0+1.
\]

Consequently no odd prime-power cyclotomic order `p^k>2u+1` divides the
period-four quotient.

## Definitions

Central indices, normalized leaders, and first/second jets are defined in the
proof appendix.

## Motivation

This closes the odd prime-power obstruction left open by `L-9828`, `L-9832`,
and `L-9868` for this quotient family.

## Proof or construction

See [the full two-jet proof](../proofs/period-four/odd-prime-two-jet.md).
The minimizer is unique or `{0,(p^2-1)/2}`; tied leaders either survive or
their first and second normalized jets are respectively `(17s+9)/48` and
`189/(320*17^2)`.

## Dependency audit

Only the exact block orders and carry gap of `L-9868` are imported.

## Gap audit

The long rational ledger is explicit but still merits external symbolic
reconstruction before promotion beyond `PROPOSED`.

## Adversarial tests

`X-9876` checks 1,257,510 tropical states, 4,873 tie states, 1,420 exact
residual jets, exceptional primes, and known double-cancellation witnesses.

## Remaining uncertainty

No counterexample is known; external line-by-line review remains outstanding.

## Suggested next attack

Translate this completed odd-prime mechanism into the composite residual automaton.

