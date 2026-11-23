# Independent review: cyclotomic residual value separation

Date: 2026-11-23. Reviewer: `/root/risk25_endpoint`.

## Frozen object and verdict

Reviewed file:
`/workspace/scratch/957bb0caa6f2/risk25/cycles/CYCLOTOMIC_VALUE_SEPARATION_PROPOSED.md`.

SHA-256:
`a65775e58fff641dba07d36e622d38979e1a93268ddea0e5dd8e339ffc35021b`.

**Verdict: VERIFIED as a written lower bound for the complete polynomial
residual, and as a qualified necessary condition for unrestricted
primitive positive integer cycles.** I reconstructed the coefficient
support, the principal-factor survival, the exceptional quadratic
cyclotomic packets, the character product, and the final degree
exponents. I found no missing hypothesis in those arguments. The bound
does not control the final numerical gcd and does not exclude a cycle.

In the notation of the reviewed file, the conclusion is

\[
 |F_0(3)|\ge c_0\left(\frac3{\sqrt{1+\sqrt2}}\right)^d d^{-K_0}.
\]

The larger base is supported for the entire residual polynomial,
including every exceptional half packet. It is not an estimate for
only a selected collection of factors. The hypotheses
`2^A>3^p`, `gcd(a,b)=1`, and `a<=2b` are explicit; positivity of a
rational fixed point alone would not justify silently dropping any of
these hypotheses. Actual positive integer cycles satisfy them.

## Support and principal factor

For a monic integral divisor `P` of `X^p-2^A`, let `k=deg P` and
`r=2^(a/b)`. Its nonzero constant term has modulus `r^k`. The
2-adic valuation of its `b`th power gives `b|a*k`, hence `b|k`.
Real coefficients and the common root modulus give

`X^k P(r^2/X)=P(0) P(X)`.

If the coefficient of `X^i` is nonzero, its reflected coefficient is
also nonzero. Their ratio makes `r^(k-2i)` rational. Therefore
`b|(k-2i)`, and, since `b|k`, `b|2i`. It follows that every such
divisor is a polynomial in `X^(b/gcd(b,2))`. This reconstructs the
support lemma used from the pinned PR185 source; I did not assume an
irreducibility classification for substituted cyclotomic polynomials.

The same constant-term argument proves that `X^b-2^a` is irreducible:
any nonconstant monic rational factor is integral and has positive
degree divisible by `b`. The positive real root `r` is not a root of
the positive-coefficient carry polynomial `Q`. Its entire minimal
polynomial consequently survives in `F_0`. The binomial is squarefree,
so removing this factor removes exactly the normalized root `1` for
odd `b`, and exactly the roots `1,-1` for even `b`.

The degree accounting in (CV2) is correct. For even `b`, `a` is odd,
`R=2^(a/2)` belongs to `Q(sqrt2)`, and `N=2d/b` is even. Rationality
of `H` therefore gives exactly `f^sigma(Y)=f(-Y)`, with no additional
scalar or sign. The same property remains valid after the principal
factor has been removed.

## Cyclotomic orbit classification over the quadratic field

The stated character is the real character modulo eight, with
`chi(1)=chi(7)=1` and `chi(3)=chi(5)=-1`.

If `8` does not divide an order `h`, every unit residue modulo `h`
has a compatible unit residue of character `+1` modulo eight. This
is immediate for odd `h`; when `v_2(h)` equals one or two, either
possible odd class modulo four is represented among `1,7` modulo
eight. Chinese remainder extension proves transitivity of the
automorphisms fixing `sqrt2`, so a full primitive-root packet occurs.

If `8|h`, the same automorphism group has exactly the two stated
character orbits. Both are closed under conjugation because
`chi(-1)=1`. If `16|h`, adding `h/2` to a primitive exponent preserves
both primitivity and its residue modulo eight. Negation thus preserves
each half, while the nontrivial field automorphism exchanges them.
Equation (CV6) forces their simultaneous presence or absence. If
`h=8m` with `m` odd, adding `h/2` instead changes an odd residue by
four modulo eight and exchanges its character. These are precisely the
half packets that the argument must retain individually.

Negation can change the order for some orders not divisible by eight;
this causes no omission, since those packets are already full and are
bounded individually by (CV4).

## Direct reconstruction of (CV7)--(CV10)

Put `zeta=zeta_(8m)`. Before imposing coprimality with the odd integer
`m`, the character-plus residues modulo `8m` are
`1+8k` and `7+8k`, for `0<=k<m`. The product identity

`product_(k=0)^(m-1) (1-zeta^(a+8k)) = 1-zeta_8^a`

for `a=1,7` gives `2-sqrt2`. The analogous classes `3,5` give
`2+sqrt2`. These are products over complete conjugate pairs, so taking
real logarithms is legitimate.

Partition the residues by `d=gcd(j,m)`. Dividing `j` by `d` gives a
primitive exponent modulo `8m/d`, with character
`chi(j/d)=chi(d)*chi(j)`. This is a bijection for every divisor `d`,
including the cases where `m` has repeated prime factors. Subtracting
the two logarithms yields exactly

`sum_(d|m) chi(d)*delta_(m/d) = -2 log(1+sqrt2)`.

The Dirichlet inverse of the completely multiplicative function `chi`
on odd integers is `mu*chi` pointwise. Applying it to the constant
right side gives

`delta_m = -2 log(1+sqrt2) * product_(ell|m)(1-chi(ell))`.

This verifies the signs, the absence of an extra prime-power factor,
and the exponent in (CV8). When `m>1`, the order `8m` is not a prime
power, so the two half logarithms sum to zero. Thus each half is at
least `u^(-2^omega(m))`. For odd `m>1`, every prime-power totient is
at least two, giving `2^omega(m)<=phi(m)`. Its half-packet degree is
`2 phi(m)`. The case `m=1` is correctly handled separately by the
exact values `2-sqrt2,2+sqrt2`, both exceeding `u^(-1)`. Therefore
the universal bound `u^(-k/2)` in (CV10) holds for every permitted
exceptional half of degree `k`.

## Evaluation and final exponents

For each conjugate root pair, (CV3) follows by expanding the product;
the dropped term is exactly `(R-T)^2>=0`. The root `-1` satisfies
the separate one-root bound stated in the file. Consequently a full
nonprincipal cyclotomic packet contributes at least
`(RT)^(k/2) Phi_h(1)>=(RT)^(k/2)`, and an exceptional half contributes
at least `(RT/u)^(k/2)`.

In the even case the remaining normalized degree is
`k=2(d-b)/b`, so multiplying all these bounds gives

`(RT/u)^((d-b)/b)
 = (sqrt(3r)*u^(-1/b))^(d-b)
 >= beta^(d-b)`.

Here `r>3` follows from the explicit positivity assumption and
`u^(-1/b)>=u^(-1/2)` follows from `b>=2`. In the odd case the
remaining factors contribute the stronger `3^(d-b)`. The empty
remaining product when `d=b` is allowed in both cases.

The reduced principal difference satisfies
`2^a-3^b=3^b(exp(L)-1)>=3^b L`. The fixed-base Matveev input gives
`L>c_0 b^(-K_0)`, so multiplication gives (CV1), first with `b` and
then with `d`, since `b|d` and `K_0>0`. I checked this Matveev
specialization against the original source in the separate frozen
core review identified below; the current note introduces no new
logarithm parameters or growing field degree.

For the comparison with the maximum state, I also read the lattice
note through (RL9a). Its use of the minimum valuation index is sound:
an index `j<d` attains the global minimum of `t_j`, hence
`x_k/x_j=(b_k/b_j)*2^(t_j-t_k)<=exp(Lambda)`. The elementary edge
bound gives `x_j+1<=(3/2)^j(m+1)`. Thus the stated lattice estimate
has the fixed base `3/2`, rather than a hidden base depending on `p`.
The pinned injective ordinary-state count bounds `Lambda` absolutely,
and the core theorem bounds `m` polynomially in `d`. Dividing (CV1)
by this maximum-state estimate gives exactly the exponent `K+K_0`
and the ratio `2/sqrt(1+sqrt2)>1` in (CV13).

The divergence assertion means an unbounded residual degree; the
reviewed core power bound on `d` supplies this whenever hypothetical
primitive cycle periods tend to infinity. No uniform bound on a
numerical gcd is obtained from the comparison with `M`.

## Dependency scope and exclusions

The separately reviewed core file is
`INTEGER_RESIDUAL_DEGREE.md`, SHA-256
`d92b1dd9c6da48459dad86a918b1a639f98c43aac8b6610157efd956b7a84b2a`.
My frozen review of it is `REVIEW_INTEGER_RESIDUAL_DEGREE.md`, SHA-256
`12d1916272fd3d565fac2fe9300cb6ed79c59e77cde241547465565694b2b063`.

The lattice file read for (RL9a) is
`RESIDUAL_RECURRENCE_LATTICE.md`, SHA-256
`9f1f08ecd36e84cfd3cdc3021591cd47d9cb4c3cc5e6ce51401cf4686d51aba5`.
Its recurrence interface and the core global-count dependency retain
their stated provenance. This review reconstructs the new cyclotomic
argument and its consumers; it does not assert a full audit of every
historical input in PR185 or PR182.

This is a written mathematical review, not a Lean compilation or a
finite-control receipt. No finite experiment is used to support any
unbounded quantifier. The actual-cycle maximum-state consequence is
distinct from the more general rational-word residual estimate. The
remaining arithmetic obstruction is the same distinguished-fiber
numerical gcd, for which the reviewed note correctly states no closing
bound.

Signed: `/root/risk25_endpoint`, 2026-11-23.
