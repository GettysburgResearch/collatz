# KTHM-0001 — Parity-cylinder affine iterate formula

**Source:** Everett, Theorem 1 and equations in the parity-vector construction; Terras, Section 1 / initial coding theorems. [@Everett1976; @Terras1976]  
**Proof status:** complete reconstruction in repository notation  
**Maps to:** `PR3/L-0001`, `CLAUDE/D-0001`, `CLAUDE/L-0001`, `CLAUDE/L-0002`

## Statement

Let

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

Fix a binary word `ε=(ε_0,…,ε_{L-1})` and suppose the first `L` parities of `n` are `ε_j`. Put

\[
a=\sum_{j=0}^{L-1}\varepsilon_j.
\]

Then

\[
T^L(n)=\frac{3^a n+B(\varepsilon)}{2^L},
\]

where

\[
B(\varepsilon)=
\sum_{j=0}^{L-1}
\varepsilon_j 2^j 3^{\varepsilon_{j+1}+\cdots+\varepsilon_{L-1}}
\in\mathbb Z_{\ge0}.
\]

## Proof

For `L=0`, take `B=0`. Assume the formula holds for a word of length `L`, weight `a`, and constant `B`.

If the next parity is `0`, then

\[
T^{L+1}(n)=\frac12T^L(n)=\frac{3^a n+B}{2^{L+1}}.
\]

If the next parity is `1`, then

\[
T^{L+1}(n)=\frac{3T^L(n)+1}{2}
=\frac{3^{a+1}n+3B+2^L}{2^{L+1}}.
\]

Thus appending a zero leaves `B` unchanged, while appending a one replaces it by `3B+2^L`. Iterating this recurrence gives the displayed sum: a contribution `2^j` created by an odd step at time `j` is multiplied by `3` once for every later odd step. Every summand is nonnegative. ∎

## Dependency audit

Only the definition of the shortcut map is used.

## Scope limitations

The formula is valid on the parity cylinder realizing `ε`. It does not assert that an arbitrary integer follows a chosen word; KTHM-0002 supplies the exact residue criterion.
