# C-9301 — Historical harmonic exceptional-cylinder conjecture

**Claim ID:** C-9301  
**Title:** Sparse low-energy reciprocal cylinders should have vanishing harmonic mass near the origin  
**Status:** SUPERSEDED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** historical route through `L-9309`, `T-9307`, and `T-9308`  
**Superseded by:** `L-9310`, `T-9311`, `T-9312`  
**Scope:** historical all-depth closure interface  
**Related counterexample candidates:** none

## Historical conjecture

For

\[
q_\ell(h)
\equiv
-17h64^{\ell-K}
\pmod{81^{\ell+1}},
\qquad
0\le q_\ell(h)<81^{\ell+1},
\]

put

\[
y_\ell(h)=\frac{q_\ell(h)}{81^{\ell+1}},
\qquad
\mathcal E_{K,L}(h)
=
\sum_{\ell=0}^{L-1}\|y_\ell(h)\|^2.
\]

The conjecture asked for growing `L_K,H_K` such that

\[
\sum_{\substack{1\le h\le H_K\\
\mathcal E_{K,L_K}(h)\le L_K/64}}
\frac1h
\longrightarrow0.
\tag{1}
\]

Together with `T-9308`, this would have implied the complete weighted EQ criterion at every depth.

The difficulty was correctly identified: `T-9307` gives a power-small **count** of low-energy residue classes, but a sparse set could still concentrate at harmonically expensive representatives such as `h=1`.

## Why it is superseded

`L-9310` discovers a stronger deterministic invariant. For signed reciprocal phases

\[
x_\ell
=
\frac{s_\ell}{81^{\ell+1}},
\]

the adjacent phase relation has an integral carry

\[
a_\ell
=64x_\ell-81x_{\ell+1}\in\mathbb Z.
\]

Small total energy allows only few nonzero carries. The resulting long zero-carry runs are exact multiplicative chains, and a completion-height argument bounds every such run by its distance from the terminal phase plus only `O(log|h|)`.

Chaining the zero runs gives, pointwise for every primitive numerator,

\[
\mathcal E_K(h)
\gg
\log\!\left(
\frac{K}{1+\log|h|}
\right).
\]

`T-9311` therefore proves uniform pointwise Fourier decay on every subexponential numerator window. `T-9312` combines the polynomial low window with `T-9308` and proves

\[
\sum_{1\le h\le2^K}
\frac{|S_K(h)|}{2^Kh}
\longrightarrow0
\]

for every depth.

Thus harmonic location of exceptional cylinders is no longer a hypothesis or an open interface in this packet.

## Historical value

The conjecture remains useful for understanding how the successful proof was found:

1. `L-9309` exposed exact lift cylinders;
2. `T-9307` showed low-energy paths have an entropy deficit;
3. the failure of exact-prefix Euclidean amplification forced attention onto the phase recurrence itself;
4. integral carry quantization supplied the missing deterministic gap.

The old proposed routes—least-representative dispersion, positive room operators, rational-diagonal renewal, and carry-template classification—remain potentially useful for sharper rates or the separate ordinary-integer problem, but they are not needed for weighted EQ.

## Status audit

- `SUPERSEDED` does not mean the historical implication was false.
- The former conjecture is replaced by the stronger theorem chain `L-9310 -> T-9311 -> T-9312`.
- The complete original formulation remains available in Git history.
- All replacing theorem-level claims remain `PROPOSED` pending independent review.
- No Collatz counterexample or M1 conclusion is claimed.