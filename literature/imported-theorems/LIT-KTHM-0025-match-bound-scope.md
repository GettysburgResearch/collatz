# LIT-KTHM-0025 — What unbounded standard match height does and does not prove

**Verdict:** `KNOWN — COROLLARY / SCOPE NOTE`.  
**Maps to:** `TERM/L-9001` in PR #6.  
**Source context:** Geser, Hofbauer, and Waldmann, *Match-bounded string rewriting systems*, develop match-boundedness as a termination criterion. The repository must still verify that its annotation update is the same convention as any tool-specific claim.

## Statement

Fix one precise match-lift annotation convention. If, for every integer \(B\), a legal lifted derivation from the language of interest reaches a symbol of height greater than \(B\), then the system is not globally match-bounded on that language under this convention. Therefore no termination proof whose certificate is a finite global bound for that exact lift can succeed.

## Proof

Global match-boundedness is the existence of one finite \(B\) bounding every annotation in every relevant lifted derivation. The assumed family contradicts each proposed \(B\). ∎

## Non-consequences

Unbounded standard match height does **not** imply:

- a nonterminating rewrite sequence;
- failure of relative match bounds;
- failure after semantic labeling or dependency-pair transformation;
- failure for a different annotation update;
- failure of natural, tropical, arctic, polynomial, or matrix interpretations;
- failure under a restricted strategy.

`TERM/L-9001` is therefore valuable exactly as a method-specific obstruction. Any broader conclusion would require another theorem.