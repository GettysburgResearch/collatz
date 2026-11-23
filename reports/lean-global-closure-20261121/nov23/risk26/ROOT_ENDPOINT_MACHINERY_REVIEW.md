# Root review: critical repetition demand and complete source products

23 November 2026. **VERIFIED WITH FIX for the repetition supremum;
VERIFIED at written scope for the remaining stated arithmetic.**

Frozen reviewed files:

- `REPETITION_ENTROPY_BOUNDARY.md`, SHA-256
  `1ab94394f4a06a5fb1dc919c8194d4536d7c4a0f9127b605021cecdac7c5100e`.
- `SIEVE_AND_SUBSPACE_SOURCE_PRODUCT.md`, SHA-256
  `06a47e76581557a3e1ecdb7ef92a27f4153a2688c0ff5e46e84ee4bf3ead8fd9`.
- `check_endpoint_machinery.py`, SHA-256
  `3e0998280a4b03bea126994ae0275d4d3338eea04ea1f50df7cd1d8d033bea39`.

The original strict bound on every repetition does not imply a strict
bound on its supremum. I requested R4 be changed to D_i<=q_i+1. That
fix is present in the frozen file. Choosing a strictly larger finite
constant still gives the later strict numerical-budget compatibility.

## 1. All-template moment and exact exponent

At fixed period d and repetition count k, independence under the
specified critical iid law makes the weighted sum a d-fold tensor
power. Summing its geometric single-letter series gives exactly
lambda_k(s)=3^(-s)*(p*2^s)^k/(1-2^(-s)*(r*2^s)^k). Both bases are
strictly below one when s<log_2(ell), and lambda_k decreases in k.

The endpoint bound on lambda_2 is sound without rounded logarithms:
3/2<ell<8/5 gives the quoted upper bound 50/57 at s=log_2(ell).
Log convexity supplies the entire intermediate interval. The double
sum over all period lengths and powers is finite. All positive gaps
and all overlapping descriptions are retained through overcounting;
no omitted-alphabet tail is hidden.

The dyadic union bound and Borel--Cantelli give the upper maximum
exponent. Independent disjoint all-one blocks give the matching lower
exponent. Taking a countable sequence of parameters and interpolating
between dyadic horizons proves the stated almost-sure limit. The
weighted summability argument gives one random polynomial-envelope
constant for every start simultaneously.

These are claims about typical samples of the critical stationary iid
law. The note explicitly does not apply that growing-window theorem
to an arbitrary selected ordinary ray solely because its empirical
fixed-block laws have that limit. That quantifier boundary is essential.

## 2. Difference energy and the literal local product

For each ordered distinct pair of ordinary states, unique factorization
gives the total prime-power weight of its difference. Summing proves
S1 and the exact ternary identity S2. The diagonal correction is
exactly 1/N, or the sum of squared weights in the weighted version.
The right side uses actual diameter. A geometric collision lower
profile alone supplies only a bounded amount of this energy; the
argument does not claim the actual energy has that upper bound.

For x=(2^A,3^d,C), the two nonarchimedean form triples have determinant
-1. The exact source relation gives L_p(x)=2^A(p-q). Multiplication
of all nine absolute values gives C*2^(-A)*|p-q|_2*|p-q|_3, with the
complete carry intact. The vector is primitive and its projective
height is the displayed ordinary maximum. Fixed source and a fixed
negative-power height saving are both correctly identified as separate
requirements for the intended Subspace-Theorem application.

## 3. Exact ordinary CRT construction

The balanced total is computed by floor(log_2(3^d)), without a
floating-point approximation. Its carry bounds are termwise exact.
The two CRT congruences have invertible coefficient D at both moduli.
They make the source positive odd and a ternary unit, force the
prescribed exact positive gaps, and give binary displacement valuation
one and ternary valuation m. Each optional intermediate coincidence
excludes at most one source because distinct clocks have distinct
affine slopes. Thus larger representatives avoid them all.

The product bracket [3^(-m)/6, d*3^(-m)/3] and logarithmic height
d*log3+O(log d) follow. Their quotient tends to zero when m=o(d),
including scales on which the local product exceeds one. These are
changing finite ordinary sources, explicitly not one infinite orbit.

The checker reconstructs actual valuations and complete carries with
integers. It also verifies finite tensor identities and source-difference
energy identities using exact fractions. Its rational test weights
check the algebraic factorization, not the probabilistic infinite
theorem or the irrational critical parameter itself.

## 4. Status

The new results accurately locate two failures of the proposed
machinery application. They neither prove existence of a positive
ordinary critical iid orbit nor exclude such an orbit. The fixed-source
all-prefix follow-up and its Lean proof have their own reviewed bytes;
this report does not extend automatically to them.
