# PROPOSED repair for PR #19 `T-9509` via Chim's two-logarithm theorem

**Status:** `PROPOSED / SOURCE-SPECIALIZATION PENDING INDEPENDENT REVIEW`  
**Review packet:** pre-public review of PRs #3, #14, #16, and #19  
**Target frozen source:** PR #19 at `3c3556aa05f50f30f1c7a984cdffa8b6acfbed45`  
**Target claim:** `research/h-frontier/claims/ITERATION_04.md`, `T-9509`  
**Source:** K. C. Chim, *Lower bounds for linear forms in two p-adic logarithms*, Journal of Number Theory 266 (2025), 295–349, Theorem 2.1, DOI `10.1016/j.jnt.2024.07.012`

This file is a new proposed repair. It does **not** retroactively verify the original Yu specialization in `T-9509`.

## Proposed source lemma

There is an absolute constant `C>0` such that, for every odd integer `n>=1` and every positive odd integer `u` satisfying `3` not dividing `u`,

\[
\boxed{
 v_2(3^n u+1)
 \le C(1+\log u)\log(2n+2).
}
\tag{1}
\]

Only existence of an absolute constant is needed by `T-9509`; no numerical optimization is required.

## Specialization of Chim, Theorem 2.1

Assume first that `u>1`. Apply Chim's theorem at the prime `p=2` to

\[
\alpha_1=-3,
\qquad
\alpha_2=u^{-1},
\qquad
b_1=n,
\qquad
b_2=1.
\tag{2}
\]

Because `n` is odd,

\[
\Lambda
=\alpha_1^{b_1}-\alpha_2^{b_2}
=(-3)^n-u^{-1}
=-\frac{3^n u+1}{u}.
\tag{3}
\]

The integer `u` is odd, so `v_2(u)=0`; hence

\[
\boxed{v_2(\Lambda)=v_2(3^n u+1).}
\tag{4}
\]

### Hypotheses

1. **2-adic units.** Both `-3` and `u^{-1}` have 2-adic valuation zero.
2. **Principal-unit exponent.** Both are congruent to `1` modulo `2`, so the source parameter `g` may be taken to be `1`.
3. **Field data.** The two numbers are rational, so the degree and local field parameters reduce to `D=e=f=1`. For `p=2`, Chim's parameter is `kappa=2`.
4. **Multiplicative independence.** If
   \[
   (-3)^a u^{-b}=1
   \]
   with integers `a,b`, unique factorization and `gcd(u,3)=1`, together with `u>1`, force `a=b=0`.

Thus the multiplicative-independence and unit hypotheses in Chim's Theorem 2.1 hold.

Choose source height parameters

\[
\log A_1=\log3,
\qquad
\log A_2=\max\{\log u,\log2\}.
\tag{5}
\]

Chim's coefficient parameter satisfies

\[
 b
 =\frac{n}{\log A_2}+\frac1{\log A_1}
 \le \frac n{\log2}+\frac1{\log3}.
\tag{6}
\]

Consequently the source quantity `H` in Theorem 2.1 obeys

\[
H\le C_0\log(2n+2)
\tag{7}
\]

for one absolute constant `C_0`; all other entries in the maximum defining `H` are absolute constants when `p=2` and `D=1`.

Theorem 2.1 therefore gives

\[
 v_2(\Lambda)
 \le C_1 H\log A_1\log A_2
 \le C_2(1+\log u)\log(2n+2),
\tag{8}
\]

which is `(1)` for `u>1`.

If `u=1`, then `3` does not divide `u`, and the required estimate follows directly from LTE for odd `n` (indeed `v_2(3^n+1)` is uniformly bounded in this parity).

## Native consequence for `T-9509`

The H core identity is

\[
2^{3r_{i+1}+2}u_{i+1}-3^{2r_i+1}u_i=1,
\]

so `(1)` with `n=2r_i+1` gives

\[
3r_{i+1}+2
\le C(1+\log u_i)\log(4r_i+4).
\tag{9}
\]

In the positive-limit alternative of `T-9508`, one has `r_(i+1) comparable to r_i`, while

\[
\sum_i\frac{\log u_i}{r_i}<\infty.
\]

Equation `(9)` forces, for all sufficiently large `i`,

\[
\frac{\log u_i}{r_i}
\gg\frac1{\log r_i}
\asymp\frac1i,
\]

which contradicts convergence. Thus this proposed source replacement would recover the conclusion of `T-9509`.

## Status boundary

- The derivation above is a **new proposed repair**, not an audit verdict on the original Yu citation.
- The original `T-9509` remains source-blocked until either its exact Yu specialization or this Chim specialization is independently reconstructed.
- Chim's theorem is a single-prime two-logarithm result. No simultaneous-prime or many-term conclusion is inferred.
- The choice `(-3,u^{-1})` is essential for using Chim's difference-of-powers normalization. The original pair `(3,-u)` belongs to a different multiplicative-form normalization and must not be copied into this source without translation.
