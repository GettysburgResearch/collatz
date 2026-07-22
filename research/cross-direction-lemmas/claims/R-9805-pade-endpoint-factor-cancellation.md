# R-9805 -- Endpoint tropical factors cancel in evaluated Pade ratios

Claim ID: `R-9805`
Title: The quadratic two-place cofactor obstruction disappears from the reduced adjacent-order Pade ratio
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: none
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `PR20/L-9408`, `PR20/L-9410`, `L-9891`, `L-9895`
Scope: evaluated canonical scalar couplings of monomial-aligned, equal-allocation adjacent-order Pade pairs
Refuted route: transferring `L-9895`'s quadratic projective cofactor height to the final ratio using only the primes `2` and `3`
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Setup

Use the fixed positive word and notation of `L-9895`.  In particular,

\[
r=|W|,
\qquad S=S(W)>0,
\qquad Z=T^\zeta,
\qquad T={64\over81}.
\tag{1}
\]

For the order-`t` equal-allocation Pade pair of `PR20/L-9410`, put

\[
D=rt
\tag{2}
\]

and write its evaluated numerator and denominator as

\[
A_t=A_t(1),
\qquad B_t=B_t(1).
\tag{3}
\]

The last phase exponent is `gamma_(r-1)`.  Define the fixed positive integer

\[
\boxed{
\kappa=\zeta-\gamma_{r-1}=1+9(S+m)>0.
}
\tag{4}
\]

For the canonical adjacent-order cofactors `d_i` of `L-9891`, put

\[
\mathcal A_{q,n}=\sum_{i=0}^{q-1}d_iA_{n+i},
\qquad
\mathcal B_{q,n}=\sum_{i=0}^{q-1}d_iB_{n+i}.
\tag{5}
\]

## Statement 1 -- exact valuations of the individual numerator

The numerator is a `2`-adic unit:

\[
\boxed{v_2(A_t)=0.}
\tag{6}
\]

At the prime `3`, put

\[
\boxed{
H_A(t)
=\gamma_{r-1}+\zeta(rt-1)
 +9S(r+1){rt(rt-1)\over2}.
}
\tag{7}
\]

Then

\[
\boxed{
v_3(A_t)=-4H_A(t).
}
\tag{8}
\]

If `H_B(t)` is the denominator exponent from `L-9895/(28)`, then

\[
\boxed{
H_A(t)=H_B(t)-\kappa.
}
\tag{9}
\]

Consequently every individual approximant already has the constant
two-place signature

\[
\boxed{
v_2(A_t/B_t)=0,
\qquad
v_3(A_t/B_t)=4\kappa.
}
\tag{10}
\]

### Proof

The polynomial `A_t(Y)` is the part of `B_t(Y)F(Y)` in degrees below `D`.
Its constant monomial from denominator index `k=0`, series index `s=0`, and
phase `j=0` is one.  Every other monomial contains a positive power of `T`:
`gamma_j>0` for `j>0`, `zeta*s>0` for `s>0`, and `zeta*k>0` for `k>0`.
Since `v_2(T)=6`, the constant monomial is uniquely least at `2`, proving
(6).

For the `k`-th denominator term, the Gaussian binomial has degree
`k(D-k)` and leading coefficient one.  Because `v_3(lambda)<0`, its leading
monomial is uniquely least at `3`.  The raw `T` exponent of the resulting
term with phase-series index `s` and phase `j` is

\[
\mathcal H(k,s,j)
=\gamma_j+\zeta(k+s)
 +9S\left\{
 Q(k)+{rs(s-1)\over2}+js
 \right\},
\tag{11}
\]

where

\[
Q(k)=(r+1){k(2D-1-k)\over2},
\qquad k+s<D.
\tag{12}
\]

For fixed `k`, equation (3) of `L-9895` makes (11) strictly increase with
`j`, and

\[
\mathcal H(k,s+1,r-1)-\mathcal H(k,s,r-1)
=\zeta+9S\{rs+r-1\}>0.
\tag{13}
\]

The maximum therefore has `j=r-1` and `s=D-1-k`.  Write `u=D-k>=1`.
The exact slack identity from the height calculation of `PR20/L-9410` is

\[
\begin{aligned}
Q(D)&-Q(D-u)
 -{r(u-1)(u-2)\over2}-(r-1)(u-1)\\
&={(u-1)(u+2)\over2}.
\end{aligned}
\tag{14}
\]

It vanishes uniquely at `u=1`.  Hence the unique globally largest exponent
occurs at

\[
k=D-1,
\qquad s=0,
\qquad j=r-1,
\tag{15}
\]

and equals (7).  Its `3`-adic valuation is `-4H_A(t)`, so it cannot cancel,
proving (8).  Equations (4), (7), and `L-9895/(28)` give (9).  Combine these
with `v_2(B_t)=0` and `v_3(B_t)=-4H_B(t)` to obtain (10). **QED**

## Statement 2 -- exact cancellation in every adjacent coupling

For all `q>=2` and `n>=1`, the coupled numerator and denominator are nonzero
and have equal endpoint valuations at `2`:

\[
\boxed{
v_2(\mathcal A_{q,n})
=v_2(\mathcal B_{q,n})
=v_2(d_{q-1}).
}
\tag{16}
\]

At `3`, both sums are controlled by the opposite endpoint `i=0`:

\[
\boxed{
v_3(\mathcal A_{q,n})
=v_3(d_0)-4H_A(n),
}
\tag{17}
\]

\[
\boxed{
v_3(\mathcal B_{q,n})
=v_3(d_0)-4H_B(n).
}
\tag{18}
\]

In particular, reduction of the evaluated rational approximant leaves the
same fixed signature as at one order:

\[
\boxed{
v_2\left({\mathcal A_{q,n}\over\mathcal B_{q,n}}\right)=0,
\qquad
v_3\left({\mathcal A_{q,n}\over\mathcal B_{q,n}}\right)=4\kappa.
}
\tag{19}
\]

These values are independent of both the width `q` and the starting order
`n`.

### Proof

Every `A_t` and `B_t` is a `2`-adic unit.  The cofactor valuations strictly
decrease with `i` by `L-9895/(14)`.  Thus `i=q-1` is the unique least term in
both sums (5), proving (16).

By (9), the consecutive valuation gaps among `d_iA_(n+i)` are exactly the
same as those among `d_iB_(n+i)`.  `L-9895/(31)` computes that common gap as

\[
4\left\{
\zeta+9S(r+1)
\left[r(n+2i)+{3r-2\over2}\right]
\right\}>0.
\tag{20}
\]

Therefore `i=0` is uniquely least in both `3`-adic sums.  This gives (17),
while (18) is `L-9895/(30)`.  Subtraction and (9) prove (19). **QED**

## Refuted inference

`L-9895` proves

\[
H_{\rm proj}(d_0:\cdots:d_{q-1})
\ge\max\{2^{S_2},3^{S_3}\},
\tag{21}
\]

with quadratic exponents when `q` has linear width.  It is tempting to infer
that the evaluated approximant has comparable reduced height.  Equations
(16)--(19) refute that inference at exactly the two primes which create
(21):

- the reverse-endpoint `2`-adic factor occurs equally in `mathcal A` and
  `mathcal B` and disappears completely from their ratio;
- the identity-endpoint `3`-adic factor also occurs equally, leaving only the
  fixed word-dependent residue `3^(4*kappa)`.

Thus the opposite tropical permutations prove a genuine cofactor-vector
height obstruction but supply no growing `2`- or `3`-adic lower bound for the
height of the reduced evaluated rational number.

## What this advances

- It closes the first proposed transfer route from `L-9895` to reduced
  approximant height instead of leaving an unspecified common-factor caveat.
- It isolates the only remaining sources for a reduced-height lower bound:
  the real absolute value, primes other than `2` and `3`, or a global
  determinant controlling the evaluation map.
- It supplies exact numerator valuations which can be combined with the
  exact normalized error of `L-9891` in a future product-formula argument.

## Dependency audit

- `PR20/L-9408` supplies `zeta`, `gamma_(r-1)`, and the identity (4).
- `PR20/L-9410` supplies the numerator truncation, the Gaussian-binomial
  degree, and the slack identity (14).
- `L-9891` supplies the canonical coupled numerator and cofactor vector.
- `L-9895` supplies both cofactor valuation orders and the denominator
  endpoint calculation.
- The new proof is a unique-monomial calculation in the finite numerator.

## Gap audit

- The refutation concerns only lower bounds obtained from the primes `2` and
  `3`.  The reduced approximants may still have quadratic height from their
  real size or other prime factors.
- Constant valuation of the ratio does not prove small height, useful
  approximation, rationality of the target value, or failure of every
  adjacent-order construction.
- General polynomial multipliers, nonadjacent orders, unequal allocations,
  and Hermite--Pade couplings remain outside the calculation.
- No product-formula lower bound for the linear form is proved.

## Adversarial checks

- The numerator uses only coefficients of degree `<D`; this strict boundary
  is why the maximizing denominator index is `D-1`, not `D`.
- The highest Gaussian-binomial monomial is unique and monic, so the claimed
  `3`-adic term cannot cancel internally.
- In (14), equality occurs only at `u=1`; every other convolution split loses
  a positive exponent before summation.
- Valuations in (19) are valuations of the rational ratio and are therefore
  invariant under clearing denominators and reducing the integer pair.
- The conclusion quarantines one height argument.  It does not refute the
  adjacent-order approximants themselves.

## Remaining uncertainty

What is the actual logarithmic height of
`mathcal A_(q,n)/mathcal B_(q,n)` for `q` proportional to `n`?  The two
distinguished primes erase the cofactor cost exactly, so an answer must see
the archimedean embedding or the remaining prime spectrum.

## Suggested next attack

Write the primitive evaluated pair as a product over all places and bound
the contribution outside `{2,3}` through resultants of adjacent
Gaussian-binomial denominators.  A successful estimate must be compared
directly with the exact error valuation `L-9891/(27c)`.
