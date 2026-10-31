# Independent reconstruction of the collective-overlap clipping barrier

**Disposition: VERIFIED within the stated mathematical scope, pending
ordinary external/project review.** This is an internal independent
reconstruction of root's current `CRITICAL_ENERGY.md`, CE-001--003. It does
not assert an external Lean replay, a new discovery of Valbuena's non-L2
theorem, or an upper bound on actual positive predecessor density.

## 1. Finite recursion and normalization

The law uses the full-group mean-one normalization
`rho_q(x)=3^q Pr(Y_q=x mod3^q)`. Splitting the first geometric exponent at
one is exact even at finite q:

* With probability one half, `Y_q=(1+3Y_{q-1}')/2`.
* With probability one half, removing one from the first exponent gives
  a fresh copy of the full q-term law, followed by division by two.

Writing D for x=2 modulo three and
`Bh(x)=1_D(x)h((2x-1)/3)`, this proves

\[
\rho_q(x)=\tfrac12\rho_q(2x)+\tfrac32B\rho_{q-1}(x).
\]

The affine map on D changes Haar mass by one third. Thus
`integral Bh=(1/3)integral h` and `||Bh||_2²=(1/3)||h||_2²`.
As a direct low-level control, rho_1 has values (0,1,2) at residues (0,1,2),
which satisfy this recursion with rho_0=1. Projectivity makes the lifted
cylinder densities a nonnegative mean-one martingale.

## 2. The L2 contradiction

Assume their L2 norms are bounded. L2 martingale convergence gives a
nonnegative density rho with integral one and a limiting equation
`rho=a+b`, where `a=(1/2)rho(2x)` and `b=(3/2)B rho`.

Because a<=rho, its positive support is contained in the positive support
of rho up to a null set. Multiplication by two preserves Haar measure, so
these support sets have equal measure and must coincide up to a null set.
Since `integral b=1/2`, b is positive on a positive-measure subset of that
same support. Consequently `integral ab>0`; Cauchy--Schwarz makes it finite.

The exact square norms are `(1/4)||rho||_2²` and `(3/4)||rho||_2²`.
Squaring rho=a+b therefore forces `integral ab=0`, a contradiction.

This uses no ergodicity of doubling, no preexisting absolute continuity,
and no uniform atom floor. The density is introduced only inside the
contradiction. The argument therefore establishes the unconditional
unboundedness of finite-level quadratic energies in the stated model.

## 3. The finite energy coefficient

Put `E_q=||rho_q||_2²`, `a_q=(1/2)rho_q(2x)`, and
`b_q=(3/2)B rho_{q-1}`. Expansion gives

\[
E_q=\tfrac14E_q+\tfrac34E_{q-1}+2\int a_qb_q.
\]

Hence

\[
E_q-E_{q-1}=\tfrac83\int a_qb_q
=2\int_D\rho_q(2x)\rho_{q-1}((2x-1)/3).
\]

Both coefficients in CE-001 are correct. Positivity explains monotonicity;
the qualitative contradiction supplies no rate of increase on its own.

If the separately source-qualified unit atom floor `rho_q>=alpha>0` is
additionally assumed, the last identity would give
`E_q-E_{q-1}>=2alpha/3`, since 2x is a unit on D and the remaining integral
is one third. This optional consequence is conditional on that additional
input and is not needed for CE-001--003.

## 4. Uniform clipping envelopes

For `mathcal E_q(U)=integral(rho_q-U)_+`, Tonelli yields exactly

\[
\int_0^\infty\mathcal E_q(U)\,dU=E_q/2.
\]

The integral through U=1 is at most one. An integrable upper envelope on
U>=1, uniform in q, would therefore bound all E_q. This contradicts the
preceding theorem. A polynomial envelope with exponent delta>1 is
integrable, giving the explicit impossible bound
`E_q<=2+2C/(delta-1)`. Omitting finitely many q does not repair that bound.

This does not prove the endpoint `C/U`, disprove it, or yield a pointwise
lower bound of order 1/U. Those distinctions are retained in the draft.

## 5. Census consequence

The stated mechanism has
`Z<=A U W+B t mathcal E_q(U)`, a root-independent lower bound `Z>=z_0>0`,
and source count at least `(X/t)W`. If its only error input is a uniform
bound `C U^(-delta)`, choosing the error below a fixed fraction of z_0
requires the sufficient clipping height on scale `t^(1/delta)`. The
guarantee then has target-loss exponent `1+1/delta`. Since delta<=1,
that method cannot obtain an exponent below two in this way.

The qualifiers are essential and present: this is a limitation of the
specified polynomial-envelope extraction. It is not a lower bound on
necessary error at every selected height, not a restriction on root-dependent
or nonpolynomial mechanisms, and not an upper bound on true basin density.
The earlier single-negative-spike exponent remains a valid weaker bound.

No defect was found in these statements. The cited source's analytic
extensions and reported formal artifacts are outside this review.
