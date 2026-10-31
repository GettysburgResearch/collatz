# Collective overlap strengthens the global clipping obstruction

**Status: PROPOSED local reconstruction and consequence. Collatz remains open.**
The non-L2 stationary-law argument is credited to Lucas Valbuena,
*Quadratic cylinder energy and integrability of the Syracuse law*, Section 5,
at commit `a7275d5a73814d3d9a400c6fe6577de9542b03a3`, file
[`paper/quadratic-cylinder-energy.tex`](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/quadratic-cylinder-energy.tex),
Git blob `2aeeda46df2e78b5fa541626d8a94f216a82702f`.
It is not a discovery claimed by this pass. We reconstruct its short argument
directly for the finite reference laws, then apply it to the specific census
mechanism from PR142. No external Lean execution is claimed.

## 1. Law and finite recursion

Let Haar probability on the additive 3-adic integers be lambda. For independent
positive exponents with probability `P(A=a)=2^(-a)`, define

\[
Y=\sum_{j\ge1}3^{j-1}2^{-(A_1+\cdots+A_j)}\in\mathbb Z_3.
\]

The series converges 3-adically. Its first q terms determine its residue
modulo `3^q`. Write mu for its law, and let rho_q be the function constant on
each depth-q residue cylinder whose value there is `3^q` times the cylinder
probability. Put rho_0=1. These are the same mean-one reference densities
used in PR142 and in the accompanying inverse-transport note.

Set `D={x:x=2 mod3}` and define the branch lift

\[
(Bh)(x)=\mathbf1_D(x)h((2x-1)/3).
\]

Doubling preserves lambda, and

\[
\int Bh\,d\lambda=\frac13\int h\,d\lambda,
\qquad \|Bh\|_2^2=\frac13\|h\|_2^2.
\tag{1}
\]

The memoryless geometric law, separated at `A_1=1`, gives

\[
\rho_q(x)=\frac12\rho_q(2x)+\frac32(B\rho_{q-1})(x),\quad q\ge1.
\tag{2}
\]

For `A_1=1`, the branch is `(1+3Y')/2`, with Haar density multiplier three.
For `A_1>=2`, removing one from that exponent leaves the original geometric
law and then halves the output. This proves (2) without a mixing theorem.

The cylinder functions form a nonnegative martingale under refinement of
ternary cylinders: the average over the three children equals the parent
density. Their integrals are one.

## 2. CE-001: the second moments are unbounded

\[
\boxed{\sup_q\int\rho_q^2\,d\lambda=\infty.}
\tag{3}
\]

**Proof.** If these moments were uniformly bounded, the L2 martingale
convergence theorem would give a nonnegative rho in L2 with integral one and
`rho_q -> rho` in L2. Both operators in (2) are bounded on L2, by (1).
Passing to the limit yields

\[
\rho=a+b,\qquad a(x)=\tfrac12\rho(2x),\qquad b(x)=\tfrac32 B\rho(x).
\tag{4}
\]

All terms are nonnegative. Since `a<=rho`, its positive support is contained
in that of rho up to a null set. Doubling preserves Haar measure, so these
two supports have equal measure and therefore agree up to a null set.
Where b is positive, (4) makes rho positive; consequently a is positive there
as well. But `integral b=1/2`, so that set has positive measure. The product
ab is integrable by Cauchy--Schwarz and has strictly positive integral.

On the other hand,

\[
\|a\|_2^2=\tfrac14\|\rho\|_2^2,\qquad
\|b\|_2^2=\tfrac34\|\rho\|_2^2.
\]

Squaring (4) would give
`||rho||_2^2=||rho||_2^2+2 integral ab`, a contradiction. QED.

This proof needs neither a previously proved absolutely continuous law nor
a uniform positive density floor. Absolute continuity is obtained only
inside the contradiction from the supposed bounded L2 martingale. It also
does not need ergodicity of multiplication by two. The cited source proves
additional subcritical integrability statements using further analytic inputs;
none of those inputs is needed for (3).

There is also an exact finite-level identity. Put

\[
E_q=\int\rho_q^2\,d\lambda,
\quad a_q=\tfrac12\rho_q(2x),\quad b_q=\tfrac32 B\rho_{q-1}.
\]

Then (2) gives

\[
\boxed{E_q-E_{q-1}=\frac83\int a_q b_q\,d\lambda
=2\int_D\rho_q(2x)\rho_{q-1}((2x-1)/3)\,d\lambda.}
\tag{5}
\]

This identifies the collective overlap responsible for increasing energy.
Equation (3) gives no quantitative lower rate by itself. A claimed linear
rate would require a separate uniform lower bound on the overlaps, or a
justified limiting argument with additional hypotheses.

## 3. CE-002: no uniform integrable clipping envelope

For U>=0 define the global clipping error

\[
\mathcal E_q(U)=\int(\rho_q-U)_+\,d\lambda.
\]

There is no nonnegative function B on `[1,infinity)` with finite integral
such that `mathcal E_q(U)<=B(U)` for every q and U>=1. In particular,

\[
\boxed{\mathcal E_q(U)\le C U^{-\delta}\ \hbox{uniformly in q and U>=1}
\quad\Longrightarrow\quad \delta\le1.}
\tag{6}
\]

**Proof.** Tonelli gives the exact layer-cake identity

\[
\frac12 E_q=\int_0^\infty\mathcal E_q(U)\,dU.
\tag{7}
\]

The part through one is at most one because `integral rho_q=1`. An integrable
uniform envelope on the remainder would bound all E_q, contradicting (3).
For a polynomial envelope with delta>1, the resulting upper bound would be
`E_q<=2+2C/(delta-1)`. QED.

An eventual-in-q uniform envelope is also excluded: the finitely many omitted
levels have finite energy and cannot affect the contradiction. The endpoint
bound `C/U` is not disproved by this argument, and is not proved here.
Likewise, (6) is not a pointwise lower estimate `mathcal E_q(U)>=c/U`.

## 4. CE-003: the specified polynomial clipping census cannot beat exponent two

PR142 studied a certificate of the form

\[
Z\le A U W+B t\mathcal E_q(U),\qquad
\#\{\text{retained sources near scale }X\}\ge (X/t)W,
\tag{8}
\]

with root-independent positive constants A,B and a retained marked lower bound
`Z>=z_0>0`. The height U is fixed for the root before the depth limit.
Using only a uniform polynomial tail `mathcal E_q(U)<=C U^(-delta)`, making
the error term a fixed fraction of z_0 costs `U` on scale `t^(1/delta)`.
The resulting guaranteed density therefore has exponent `1+1/delta` in t.
By (6),

\[
\boxed{1+1/\delta\ge2.}
\tag{9}
\]

This strengthens the single-negative-spike obstruction `log_2(3)` from
PR142. That earlier bound remains valid; it simply did not detect the full
stationary overlap. The improvement here is an application of the credited
non-L2 theorem to this explicitly delimited counting mechanism.

The conclusion does not bound actual predecessor density. Indeed the newly
located external papers claim a reciprocal density bound by using different
inputs and removing the global clipping loss. Neither those claims nor
source-conditioned, root-dependent, or nonpolynomial error mechanisms are
excluded by (9). No assertion of achievability at exponent two is made.

## 5. Finite evidence and source boundary

The accompanying verifier constructs the exact infinite-geometric residue
laws using finite modular periods, then independently reconstructs each law
from its cyclic doubling recursion. It verifies projectivity, normalization,
the complete finite recursion (2), and both rational expressions in (5).
No exponent tail is truncated. Saved exact fractions and counts describe only
the bounded computation; the unbounded conclusion (3) follows from its proof.

The external manuscript's non-L2 argument was read and reconstructed. The
reported Lean build and its large dependency closure were not executed here.
The source's stronger density and canonical-trace results are separately
catalogued with that evidence ceiling in the pass report.
