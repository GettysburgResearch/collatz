# Iteration 04: exclusion of the critical near-Pillai regime

All native theorem-level claims remain `PROPOSED` pending independent review.
The principal result below imports one standard external theorem of Kunrui Yu on
explicit `p`-adic logarithmic forms. No claim here excludes the remaining
subcritical zero-carry regime.

---

## External input: a two-factor specialization of Yu's theorem

We use the following qualitative consequence of Kunrui Yu,
*P-adic logarithmic forms and group varieties III*, Forum Math. 19 (2007),
187--280, DOI `10.1515/FORUM.2007.009`.

For fixed prime `p=2` and two nonzero rational numbers `alpha_1,alpha_2`, Yu's
explicit estimate bounds

\[
 v_2(\alpha_1^{b_1}\alpha_2^{b_2}-1)
\]

by a constant times the product of logarithmic-height terms and `log B`, where
`B>=max(3,|b_1|,|b_2|)`. In the specialization

\[
 \alpha_1=3,
 \qquad
 \alpha_2=-u,
 \qquad
 b_1=n,
 \qquad
 b_2=1,
\]

with positive odd `u`, this gives an absolute constant `C>0` such that

\[
 \boxed{
 v_2(3^n u+1)
 \le C(1+\log u)\log(2n+2).
 }
 \tag{1}
\]

The case `u=1` also follows directly from LTE when `n` is odd. The displayed
soft form is all that is used below; no numerical value of `C` is needed.

### Applicability audit

For the H core recurrence, `n=2r+1` is positive and odd, `u` is a positive odd
integer with `3` not dividing `u`, and

\[
 -3^n u\ne1.
\]

If `u>1`, the rational numbers `3` and `-u` are multiplicatively independent:
a multiplicative relation would force every prime divisor of `u` to be `3`,
contrary to `3` not dividing `u`. Thus the usual nondegenerate two-logarithm
hypotheses hold. If a chosen formulation of Yu's theorem does not require
multiplicative independence, this check is redundant.

---

## T-9509: Critical real escape is impossible

**Claim ID:** `T-9509`  
**Title:** No nonperiodic exact H survivor lies in the critical near-Pillai regime  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-h-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Dependencies:** `T-9505`, `T-9508`; Yu's 2007 `p`-adic logarithmic-form theorem  
**Scope:** hypothetical nonperiodic infinite exact positive H orbit

### Statement

Let a hypothetical nonperiodic exact orbit have capital `K_i`, letters `r_i`,
odd cores `u_i`, and

\[
 c_*=\frac{\log9}{\log8},
 \qquad
 Z_i=K_i/c_*^i.
\]

Then

\[
 \boxed{\lim_{i\to\infty}Z_i=0.}
 \tag{2}
\]

Equivalently, the positive-limit alternative in `T-9508` cannot occur. Every
hypothetical nonperiodic survivor must satisfy

\[
 \boxed{
 K_i=o(c_*^i),
 \qquad
 r_i=o(c_*^i).
 }
 \tag{3}
\]

### Proof

Assume instead that

\[
 Z_i\to Z_\infty>0.
\]

By `T-9508`,

\[
 r_i\sim (c_*-1)Z_\infty c_*^i,
 \qquad
 \frac{r_{i+1}}{r_i}\to c_*,
 \tag{4}
\]

and

\[
 \sum_i\frac{\log u_i}{r_i}<\infty.
 \tag{5}
\]

The exact core equation is

\[
 2^{3r_{i+1}+2}u_{i+1}-3^{2r_i+1}u_i=1.
\]

Hence

\[
 v_2(3^{2r_i+1}u_i+1)=3r_{i+1}+2.
 \tag{6}
\]

Apply (1) with `n=2r_i+1`. For all sufficiently large `i`, (4) gives
`r_(i+1)>=c_0r_i` for some fixed `c_0>0`. Therefore

\[
 c_0r_i
 \le C_1(1+\log u_i)\log(2r_i+2).
\]

Since `r_i` tends to infinity, after increasing the starting index this implies

\[
 \boxed{
 \frac{\log u_i}{r_i}
 \ge\frac{c_1}{\log r_i}
 }
 \tag{7}
\]

for some fixed `c_1>0`.

But (4) also gives

\[
 \log r_i=i\log c_*+O(1).
\]

Thus the right side of (7) is bounded below by a positive constant times `1/i`.
Consequently

\[
 \sum_i\frac{\log u_i}{r_i}
\]

diverges, contradicting (5). This proves (2)--(3).

### Significance

The infinite obstruction is no longer split between a critical and a
subcritical alternative. The critical branch is eliminated by an existing
Diophantine theorem. Any positive ordinary-integer ghost must now satisfy the
strictly subcritical conditions (3), in addition to every earlier survivor,
carry, harmonic-kernel, repetition-height, and prime-support restriction.

### Gap audit

- The proof depends on the quoted soft specialization (1). An independent
  reviewer should reconstruct the specialization directly from Yu's exact
  theorem and verify normalization of `v_2`, height, and `B`.
- No effective value of the constant is required.
- This theorem does not exclude `Z_infinity=0`; it narrows `Q-9505` to the sole
  remaining infinite regime.

---

## Corollary: discounted capital has no positive exponential residue

Combining `T-9505` and `T-9509`, every hypothetical nonperiodic survivor obeys

\[
 \frac{K_i}{c_*^i}\to0
\]

while

\[
 \sum_i c_*^{-(i+1)}\log u_i<\infty.
\]

The capital recurrence can therefore be written as the exact future-tail
identity

\[
 \boxed{
 K_i=
 \sum_{k=0}^{\infty}c_*^{-(k+1)}
 \left(\frac{\log u_{i+k}}{3\log2}-\eta_{i+k}\right),
 }
 \tag{8}
\]

where `eta_i` is the convergent sequence from `T-9505`. Equation (8) is a useful
starting point for the transformed-height problem: in the only remaining regime,
current capital is an exponentially weighted **future** odd-core demand rather
than a surviving homogeneous mode.
