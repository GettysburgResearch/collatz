# R-8201 — Quotient refund does not remove the ordinary-cylinder firewall

**Claim ID:** `R-8201`  
**Type:** refutation / method boundary  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-refund-01`  
**Created:** 2026-07-22  
**Dependencies:** elementary odd-affine cylinder algebra; `L-8201` only for contrast  
**Scope:** every fixed infinite directive in the linear-height refund system

## Refuted inference

> Because every finite word pair has infinitely many positive expanding quotient transitions, some finite positive quotient follows an infinite directive.

This inference is invalid.

## Exact statement

Fix an infinite sequence of stage words. Its quotient equations have the form

\[
Y_{n+1}=\frac{P_nY_n+C_n}{Q_n},
\]

where every `P_n` is odd and every `Q_n` is a positive power of two.

For each finite prefix, exact integrality selects one residue

\[
Y_0\equiv R_N\pmod{Q_0Q_1\cdots Q_{N-1}}.
\]

The residues are nested and select one point in `Z_2`. This point is a nonnegative ordinary integer exactly when the least representatives `R_N` eventually stabilize, equivalently when the newly appended blocks are eventually zero.

The inequalities

\[
P_n>Q_n
\quad\text{or}\quad
P_n>2Q_{n+1}
\]

change archimedean growth after a lift is present. They do not change odd invertibility modulo the future dyadic radices and do not imply stabilization of the initial cylinder.

## Proof

Chronological composition of the first `N` maps gives

\[
Y_N=\frac{\Pi_NY_0+F_N}{\mathcal Q_N},
\qquad
\mathcal Q_N=\prod_{j<N}Q_j,
\]

with `Pi_N` odd. Hence integrality is one congruence modulo `mathcal Q_N`, and oddness gives one residue. Prefix extension preserves the earlier congruence, so the classes are nested. The ordinary-stabilization equivalence follows from `mathcal Q_N -> infinity` and uniqueness of least nonnegative representatives.

No real-size inequality enters this argument.

## Consequence

A successful refund construction must contain an explicit **ordinary top-boundary certificate**, not just:

- positive pairwise lifts;
- a modular lasso;
- an infinite word selected by compactness;
- or an expanding `Z_2` quotient.

## Gap audit

This boundary does not prove that the ordinary intersection is empty. It identifies the exact missing implication and leaves integer-first causal constructions open.
