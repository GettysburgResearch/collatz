# L-8202 — Stage-word residue sparsity

**Claim ID:** `L-8202`  
**Title:** A bounded phase-34 stage word controls only 512 bits of a billion-bit next-cylinder condition  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-refund-01`  
**Created:** 2026-07-22  
**Dependencies:** uniqueness of the word-pair quotient congruence in `LIT-KTHM-0050`  
**Scope:** one 256-transition linear-height stage

## Statement

Fix a current stage word `w`. For each next word

\[
v\in\{0,1,2,3\}^{256},
\]

the next-cylinder condition selects at most one residue `y_0(v)` for `Y` modulo

\[
Q=2^{E(B+4096)}.
\]

Therefore the union of all pairwise transition domains occupies at most

\[
4^{256}=2^{512}
\]

residue classes modulo `Q`.

Allowing the current word to vary as well gives at most `2^1024` labelled word-pair residue classes.

At the first one-stage refund threshold `B=477424`,

\[
E(B+4096)=1361752832.
\]

Thus the domain fraction for a fixed current word is at most

\[
2^{512-1361752832}=2^{-1361752320}.
\]

## Proof

For fixed `w,v`, the condition is

\[
S_B(w)+3^{A(B)}Y\equiv R_{B+4096}(v)\pmod Q.
\]

The coefficient of `Y` is odd and therefore a unit modulo `Q`, so the congruence has exactly one solution. Count the possible words.

## Interpretation

The quotient-refund construction is not a broad expanding cover. It is an expanding map restricted to an extremely sparse, arithmetic family of input residues. A successful selector must **generate** those residues from the current ordinary state. Merely having four tower types at each of 256 positions cannot encode a generic next block.

## Gap audit

- The bound may have collisions and is only an upper bound.
- Sparsity does not imply the absence of a structured ordinary path.
- An unbounded arithmetic generator can target a sparse language; this lemma rules out only arguments based on branch count or generic coverage.
