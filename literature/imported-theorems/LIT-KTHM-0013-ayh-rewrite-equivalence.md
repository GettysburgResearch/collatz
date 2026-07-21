# LIT-KTHM-0013 — automated string-rewrite formulation of Collatz

**Source:** [@YolcuAaronsonHeule2023]
**Inspection:** official open article page
**Proof status:** BLACK BOX

## Imported result

Yolcu, Aaronson, and Heule construct a finite mixed binary–ternary string-rewriting system whose termination is equivalent to the standard Collatz conjecture. They analyze termination orders, show limitations of some matrix-interpretation methods, implement a termination prover using natural and arctic matrix interpretations, and obtain automated proofs for nontrivial weakened systems.

## Native mappings

- Direct external foundation for draft PR #6's exact rule import.
- A reusable formal-language target for future translations of collision macro-tiles or carry transducers.

## Non-applications

The article does not prove termination of the full system or the Collatz conjecture. Failure of one termination-order template is not evidence of nontermination. A native rewrite lemma must still be proved in the repository's exact convention.
