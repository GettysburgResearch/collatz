# Iteration 08B: exact prefix-return capital barrier

All theorem-level claims remain `PROPOSED` pending independent review. This
file sharpens the structured-counterexample restrictions in `ITERATION_08.md`.

Retain a hypothetical nonperiodic exact positive orbit

\[
p_{n+1}={3^{2r_n+1}\over2^{3r_n+2}}p_n+1,
\]

its capital

\[
K_n=\sum_{i<n}(r_i-\kappa),
\qquad
\kappa={\log(4/3)\over\log(9/8)},
\]

and the bounded toll coordinate from `T-9502`, so

\[
p_n\le Q_\infty(9/8)^{K_n}.
\tag{1}
\]

Assume the itinerary lies in a finite alphabet `A`, and put

\[
e_*=\min_{r\in A}(3r+2),
\qquad
H_N=\max_{0\le i\le N}K_i.
\tag{2}
\]

---

## L-9523: exact prefix-return versus capital inequality

**Claim ID:** `L-9523`  
**Title:** Every early symbolic return consumes a proportional capital wall  
**Status:** `PROPOSED`  
**Dependencies:** `T-9502`, exact affine block differences  
**Scope:** nonperiodic finite-alphabet exact survivors

### Statement

Suppose a length-`ell` itinerary factor occurs at two distinct starting
positions `i<j`. Then

\[
\boxed{
H_j\ge
{e_*\ell\log2-\log(2Q_\infty)\over\log(9/8)}.
}
\tag{3}
\]

In particular, let `tau(ell)` be the first positive return time of the prefix
factor

\[
r_0r_1\cdots r_{\ell-1}.
\]

Whenever it exists,

\[
\boxed{
H_{\tau(\ell)}\ge
{e_*\ell\log2-\log(2Q_\infty)\over\log(9/8)}.
}
\tag{4}
\]

Assume for all sufficiently large `ell` that

\[
\tau(\ell)\le C\ell
\tag{5}
\]

and

\[
H_N\le\gamma N+O(1).
\tag{6}
\]

Then necessarily

\[
\boxed{
\gamma\ge{e_*\log2\over C\log(9/8)}.
}
\tag{7}
\]

If `r_max=max A`, then always `H_N<=(r_max-kappa)N+O(1)`. Hence no such
survivor exists whenever

\[
\boxed{
C(r_{\max}-\kappa)
<{e_*\log2\over\log(9/8)}.
}
\tag{8}

For the binary alphabet `{2,3}`, one has `e_*=8`, and (8) excludes every
prefix-linearly recurrent candidate with integer return constant

\[
\boxed{C\le84.}
\tag{9}

### Proof

Let `w` be the common length-`ell` factor. Its exact affine map is

\[
F_w(p)={V_wp+A_w\over2^{E_w}},
\]

with `V_w` odd. Applying it at `p_i` and `p_j` and subtracting gives

\[
2^{E_w}\mid p_j-p_i.
\tag{10}
\]

The states are distinct because the orbit is nonperiodic, so the difference is
nonzero. Since every letter contributes at least `e_*` to `E_w`,

\[
2^{e_*\ell}
\le |p_j-p_i|.
\tag{11}
\]

Equation (1) and the definition of `H_j` give

\[
|p_j-p_i|
\le p_j+p_i
\le2Q_\infty(9/8)^{H_j}.
\tag{12}
\]

Taking logarithms proves (3)--(4). Substituting (5)--(6), dividing by `ell`,
and passing to the limit proves (7). The trivial capital upper bound proves
(8).

For `A={2,3}`,

\[
{e_*\log2\over(r_{\max}-\kappa)\log(9/8)}
=84.4438535291\ldots,
\]

so every integer `C<=84` satisfies (8). QED.

---

## R-9506: short-return substitution candidates are closed

**Claim ID:** `R-9506`  
**Title:** Bounded-return finite-alphabet templates need an explicit capital rate above the completion-height threshold  
**Status:** `PROPOSED`  
**Dependencies:** `L-9523`

A primitive substitution, morphic word, automatic sequence, or Sturmian word
is not excluded merely by its name. But once its prefix-return bound

\[
\tau(\ell)\le C\ell
\]

and its capital upper rate `gamma` are certified, `L-9523` is a direct exact
veto whenever

\[
C\gamma<{e_*\log2\over\log(9/8)}.
\]

In particular, every `{2,3}` template with prefix-return constant at most 84
is impossible, independently of its letter frequencies. This extends
`R-9505`: even a zero-entropy substitution with **linear** positive capital can
be excluded when its symbolic returns occur too early.

The theorem does not cover directives with very long return times or positive
entropy. Such delayed novelty is now a necessary design resource for a
structured counterexample.

---

## Q-9510: delayed-novelty counterexample interface

A viable finite-alphabet structured counterexample must now satisfy all of:

1. eventual zero carry for one positive ordinary initialization;
2. nonperiodicity and real escape;
3. the factor-entropy lower bound of `L-9522` whenever capital is logarithmic;
4. the prefix-return lower bound (4) at every repeated prefix;
5. if capital is at most linear, return times large enough to evade (7)--(8);
6. infinitely many fresh bridge primes as required by `T-9513`.

Thus a low-memory morphism or short-return substitution is no longer a viable
candidate architecture. A positive construction must generate delayed
symbolic novelty and fresh arithmetic information at compatible rates, while
still producing one eventually stable ordinary cylinder.