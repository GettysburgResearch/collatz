# An explicit deadline for repetition or exit from a bounded core family

**Status: SOURCE-QUALIFIED corollary, pending independent review.** This
settles a bounded-resource class of actual ordinary trajectories. Exiting
that class is not numerical descent and is not a Collatz certificate.

The only inputs are SC1–SC2 and the elementary clock in
[`SHIFTED_CORE_TRANSITIONS.md`](SHIFTED_CORE_TRANSITIONS.md), frozen at
14,609 bytes, SHA-256
`f53846e08e1522058797c6cab57111cf9c7ed4385f39b0e055ab05264f7acb71`.
Their external dependency is Evertse's quantitative S-unit theorem,
Theorem 3 on printed page 7 of the
[primary author PDF](https://pub.math.leidenuniv.nl/~evertsejh/95-decforms.pdf).
The optional PR145 compressed-word theorem is not used in this corollary.

## SC4. A finite horizon with all endpoints included

Fix a finite prime pool `P` containing 2 and 3, and put `s=|P|`. Let

\[
 B_s=(9\cdot2^{35})^{27(s+1)}.
\]

Fix an integer `K>=1` and a positive odd ordinary source `n_0`. Set

\[
 \ell=\left\lceil\log_2(n_0+1)\right\rceil,
 \qquad
 H_{\mathrm{int}}=
 \ell\left(2^{B_sK^2+1}-1\right).                   \tag{1}
\]

Follow the actual accelerated orbit `n_j=U^j(n_0)`. By time
`H_int`, at least one of the following holds:

1. two ordinary states `n_i=n_j` occur with
   `0<=i<j<=H_int`;
2. the list `R_P(n_j+1)`, `0<=j<=H_int`, contains at least `K+1`
   different cores.

In particular, for any fixed set `Q` of at most `K` cores, the orbit
must either repeat a state or leave `Q` within at most `H_int` odd
transitions. If its initial core is already outside `Q`, the exit is
at time zero. The statement includes the endpoint at time `H_int`.

**Proof.** Suppose neither alternative occurs. The `H_int+1` states
are then pairwise distinct, and their core set has size at most `K`.
Let `D` be the number of exponents at least two among those first
`H_int` transitions. SC2 gives `D<=B_sK^2`. The exact conservative
clock, equation (18) of the source note, gives

\[
 H_{\mathrm{int}}<\ell(2^{D+1}-1)
 \le\ell(2^{B_sK^2+1}-1)=H_{\mathrm{int}},
\]

a contradiction. The fixed-family assertion follows because `K+1`
different cores cannot all lie in a set of size at most `K`. Every
iterate is from the same fixed ordinary source. \(\square\)

## A sharper symbolic deadline

Let `h_0=log_2(n_0+1)`, `gamma=log_2(3/2)`, and
`alpha=log_2 3=1+gamma`. The sharper elementary clock in the source
proof also permits

\[
 H_{\mathrm{sharp}}=
 \left\lceil
 \frac{h_0}{\gamma}
       \left(\alpha^{B_sK^2+1}-1\right)
 \right\rceil.                                    \tag{2}
\]

Indeed every simple prefix with at most `K` cores has length strictly
less than the real expression inside this ceiling. If that expression
happens to be an integer, equality of the tested length with it is
still excluded; the strict inequality handles the endpoint.

The integer expression (1) supplies the explicit effective budget
without any decision about rounding a real logarithmic expression.
It is no smaller than (2), since `h_0<=ell` and

\[
 \frac{\alpha^r-1}{\alpha-1}
   =\sum_{i=0}^{r-1}\alpha^i
   \le\sum_{i=0}^{r-1}2^i=2^r-1
 \qquad(r\ge1).
\]

## What this finite decision does and does not certify

The test can literally iterate until either a repeated ordinary value
appears or a prescribed core family is exited. The theorem supplies
a finite bound for this alternative, with no restriction on individual
division exponents. The number is enormous; no claim of practical
feasibility is made, and no computation of all these steps is part of
the evidence.

For `K=1` and `Q={1}`, a simple path whose shifted values are all
supported by one pool of `s` primes lasts at most a constant depending
only on `s` times `log_2(n_0+1)`. This is uniform in which primes
constitute the pool. If such support confinement continues forever,
an actual state must repeat by the stated deadline, proving eventual
periodicity.

A repeated state certifies eventual periodicity, which could still be
a hypothetical nontrivial positive cycle. An exit merely says that a
new arithmetic core is needed. It need not make the ordinary value
smaller, lead to 1, or prevent further exits. No successful all-source
descent selector or unrestricted Collatz theorem follows.
