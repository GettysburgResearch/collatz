# The odometer Gram operator and an elementary quantitative energy obstruction

**PROPOSED; self-audited only.** All measures below are additive Haar
probability on Z_3. This is the random affine cylinder law, not an occupation
law of a fixed ordinary orbit.

Let

    (Df)(x)=f(2x),
    (Bf)(x)=1_{x=2 mod 3} f((2x-1)/3),
    L=(3/2)(I-D/2)^(-1)B,
    rho_0=1, rho_q=L^q 1, E_q=integral rho_q^2.

The inverse is the norm-convergent series sum_{j>=0}2^-j D^j. The operator
L is the Haar Perron transfer for x -> (3x+1)/2^A with P(A=a)=2^-a.
It agrees with the inherited cylinder recursion, not with the ordinary
counting operator on an arbitrarily chosen sequence space.

Put T(x)=4x+1, and V f=f composed with T. T is Haar preserving. On Z/3^r,
its orbit of zero has exact length 3^r, since

    T^k(0)=(4^k-1)/3,   v_3(4^k-1)=1+v_3(k).

## E1. Exact Gram identity

For every complex f in L^2(Z_3),

    ||Lf||_2^2 = ||f||_2^2
                +2 Re sum_{k>=1}4^-k <f,V^k f>,

and, as a bounded self-adjoint operator,

    L* L = I + sum_{k>=1}4^-k (V^k+V^(-k))
         = (15/16)(I-V/4)^(-1)(I-V*/4)^(-1).

Equivalently its Fourier multiplier in the T-odometer coordinate is

    P(theta)=15/(17-8 cos(theta)).

Thus

    (3/5)||f||_2^2 <= ||Lf||_2^2 <= (5/3)||f||_2^2.

Both constants are sharp on the full space. On depth-r cylinder functions
the exact squared singular values are

    15/[17-8 cos(2 pi j/3^r)],   0<=j<3^r.

The upper value is attained by the constant input. The lower values approach
3/5 along odd-period frequencies nearest pi. This says neither that L is
power bounded nor that rho_q has bounded energy.

### Proof

D is unitary and ||Bf||_2^2=||f||_2^2/3. Inner products between D^j Bf and
D^k Bf vanish when j-k is odd, since their supports lie in different unit
classes modulo three. For k>=1 a change of variables x=(3y+1)/2 gives

    <Bf,D^(2k)Bf> = (1/3)<f,V^k f>.

Expand the absolutely convergent double series for the square of
(3/2) sum_{j>=0}2^-j D^j Bf. Its diagonal coefficient is
(9/4)(sum_j4^-j)/3=1. Each off-diagonal displacement 2k has coefficient
4^-k, proving the formula. Summing the geometric operator series gives the
Poisson multiplier. Finite T-cycles give the displayed finite spectra and
sharp constants without invoking a new mixing theorem.

### Attribution boundary

The nonnegative-density special case

    E_(q+1)-E_q =2 sum_{k>=1}4^-k integral rho_q(x)rho_q(T^k x)

already appears in the public rStation paper 9 / post 11 discussions. The
inherited PR142 packet also proves an equivalent positive-overlap identity.
This note credits those facts; its presentation extends them to the full
complex L^2 Gram operator and records the finite singular-value calculation.
The exact interval implementation below is not claimed to be the first
linear-time cylinder sweep; public post 21 also discusses linear sweeps.

## E2. Explicit logarithmic lower growth, without an external atom floor

For every integer q>=0,

    E_q >= log_4(4 + q log(4)/4).

This is weaker than a linear lower bound obtained with stronger positivity
inputs. Its point is an elementary, explicit rate using only the finite law
and the identity E1: no external canonical trace, atom floor, mixing theorem,
or limiting density is needed.

### Proof

For any real nonnegative f with integral f=1 let E=||f||_2^2 and
C_k=<f,V^k f>>=0. For any integer M>=2, Cauchy-Schwarz applied to
sum_{j=0}^{M-1}V^j f gives

    M^2 <= M E + 2 sum_{k=1}^{M-1}(M-k) C_k.

Consequently sum_{k=1}^{M-1} C_k >= (M-E)/2 whenever M>E. Positivity and E1
then imply

    ||Lf||_2^2-E >= (M-E)4^(-(M-1)).

Choose M=ceil(E)+1. The right side is at least 4^(-ceil(E)), hence at least
4^(-E-1). Apply this to f=rho_q. Writing d=E_(q+1)-E_q, the elementary
inequality exp(u)>=1+u yields

    4^E_(q+1) >= 4^E_q + log(4)/4.

Iterate from E_0=1. In particular the finite cylinder energies cannot remain
bounded; this quantitative conclusion does not rely on taking an L^2 limit.

## E3. Certified large-depth enclosures, not floating-point evidence

`certify_energy.py` encloses EVERY rho_q residue between two dyadic rationals
with common denominator 2^p. It uses signed 64-bit storage but ordinary Python
integer arithmetic for all updates and moments. Overflow preconditions are
checked. No random sampling or floating-point arithmetic enters a bound.

On the doubling cycle r_j=2^j mod 3^q, of length P=2*3^(q-1), set
f_j=rho_(q-1)((2r_j-1)/3) if r_j=2 mod3, and zero otherwise. The recursion is

    rho_q(r_j)=(rho_q(r_(j+1))+3 f_j)/2.

A backward sweep starting at zero encloses its affine constant term V. The
cyclic initial value is V/(1-2^-P). The code rounds the lower endpoint down
and the upper endpoint up; for P>=64 the upper closure correction is at most
one integer unit after its explicit magnitude check. A second backward sweep
propagates the enclosed cyclic initial value to all residues. Nonunits remain
exactly zero.

Squaring nonnegative integer endpoints and summing gives rigorous rational
bounds on E_q. Differences use the upper bound at the previous depth for the
lower endpoint, and conversely. Exact low-depth Fraction laws are a separate
cross-check; they are not extrapolated to larger depths.

## Remaining positive target

The computed increments look bounded on the retained finite range. Neither
E_q=O(q) nor convergence of E_(q+1)-E_q is established here. By E1, a
sufficient concrete target is a uniform bound on

    sum_{k>=1}4^-k <rho_q,V^k rho_q>.

The trivial norm bound on the Gram operator cannot provide that estimate:
it multiplies E_q, and E_q is itself unbounded. More importantly, even an
improved Haar energy bound would still require an ordinary-source transfer
argument before it could exclude a persistent Collatz survivor.

## Source pointers

* PR142 inherited energy packet, frozen at
  `3c0ce26d6021fbd700df61652d596293b661612c`:
  `research/beeping-density-swarm-20261031/CRITICAL_ENERGY.md`.
* Valbuena, `paper/quadratic-cylinder-energy.tex`, frozen at
  `a7275d5a73814d3d9a400c6fe6577de9542b03a3` in
  `x1xhlol/collatz-two-coordinate-obstruction`: the quadratic upper bound and
  exact integrability range are external prior work, not results of this pass.
* https://rstation.ai/problems/collatz/papers/9/v1
* https://rstation.ai/r/collatz/posts/11
* https://rstation.ai/r/collatz/posts/21

No external formal proof development was executed for this note.
