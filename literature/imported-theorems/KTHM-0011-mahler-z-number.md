# KTHM-0011 — Mahler Z-numbers: definition and countability theorem

**Source:** Mahler's 1968 paper; statement cross-checked against the EMS reprint abstract. [@Mahler1968]  
**Proof status:** black-box import  
**Maps to:** analogy audit for `CLAUDE/Q-0002`

## Definition

A positive real number `ξ` is a **Z-number** if

\[
0\le \{\xi(3/2)^n\}<\frac12
\]

for every integer `n≥0`, where `{x}` is the real fractional part.

## Mahler's theorem and open problem

Mahler proves that the set of Z-numbers is at most countable, with a quantitative upper bound on their counting function. He does not prove that a Z-number exists. The existence question remains the classical open `3/2` problem.

## Mapping to the repository

`CLAUDE/Q-0002` has the same broad “multiplicative orbit confined to a digit set” shape, but it is a `2`-adic carry problem for `81/64`. It is therefore an analogue, not a reformulation to which Mahler's theorem directly applies.
