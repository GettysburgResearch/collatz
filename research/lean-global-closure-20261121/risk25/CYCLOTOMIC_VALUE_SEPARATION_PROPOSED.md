# A stronger residual value base from complete cyclotomic packets

Date: 2026-11-23. **Status: PROPOSED written continuation, pending separate
independent review.** This is not part of the already reviewed core
packet until that review occurs. The following argument aims to replace
the inherited exponential base `3/2` by a fixed larger base, at the cost
of a polynomial in the reduced denominator `b`.

Let `F=X^p-2^A`, `Q=sum_(j=0)^(p-1) 2^(s_j)X^(p-1-j)`, and
`F_0=F/gcd(F,Q)`, with monic gcd, come from a positive-gap word whose
rational fixed point is positive: explicitly assume **`2^A>3^p`**.
Write `A=ga,p=gb,gcd(a,b)=1`, assume also `a<=2b`, and put
`d=deg F_0`. These conditions hold for every actual positive integer
cycle. Put

\[
 u=1+\sqrt2,\qquad \beta=\frac3{\sqrt u}>\frac32.
\]

With the explicit Matveev constants `c_0,K_0` in
`INTEGER_RESIDUAL_DEGREE.md`, the proposed conclusion is

\[
 \boxed{|F_0(3)|\ge c_0\beta^d b^{-K_0}
                  \ge c_0\beta^d d^{-K_0}.}
\tag{CV1}
\]

For odd `b`, the stronger bound has `3^d` in place of `beta^d`.
The claim concerns the complete polynomial residual and all of its
factors. It does not bound the final numerical gcd.

## 1. Reduction to roots of unity over a field of degree at most two

The coefficient-support lemma of PR185 at
`2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`,
`research/central-closure-20261123/PRIMITIVE_DENOMINATOR_GROWTH.md`,
Section 1, states that every monic integer divisor `P` of `X^p-2^A`
is a polynomial in `X^(b/e)`, where `e=gcd(b,2)`.
Here is its short argument, retained for the precise scope.

All roots of `P` have modulus `r=2^(a/b)`, and its degree `k` is a
multiple of `b` because `|P(0)|=2^(ak/b)` is an integer. If
`P(X)=sum c_i X^i`, conjugation of its roots gives
`X^k P(r^2/X)=c_0P(X)`. For nonzero `c_i`, coefficient comparison
then makes `2^(a(k-2i)/b)` rational, forcing `b|2i`.

Apply this to `F_0`, and write

\[
 F_0(X)=H(X^t),\qquad t=b/e,\quad N=d/t,\quad
 R=2^{a/e},\quad T=3^{b/e},\quad
 f(Y)=R^{-N}H(RY).
\tag{CV2}
\]

The roots of `f` are roots of unity. The coefficients of `f` lie in
`Q` if `b` is odd. If `b` is even, then `a` is odd, `N=2d/b` is
even, and its coefficients lie in `K=Q(sqrt2)`.

The principal binomial `X^b-2^a` is irreducible over `Q`: any nonconstant
monic integer factor has all its roots of modulus `2^(a/b)`; its
integer constant term therefore forces its degree to be divisible by
`b`, as above, hence to be the full degree. The positive root `r` of
`F` is not a root of `Q`, since every coefficient of `Q` is positive.
Thus it survives in `F_0`, and its minimal polynomial `X^b-2^a`
divides `F_0`.

When `b` is odd this principal binomial is the root `1` of `f`; when
`b` is even it consists of the two roots `1,-1`. Remove this principal
binomial and denote the remaining degree by `d-b`. No root `1` remains
in the normalized polynomial. In the even case no root `-1` remains
either. All root multiplicities here are one, because `F` is squarefree.

## 2. Full cyclotomic packets and their positive real value

For any conjugate pair of unit roots `zeta,bar(zeta)` and positive
`R,T`,

\[
 (T-R\zeta)(T-R\bar\zeta)
 =(R-T)^2+RT(2-\zeta-\bar\zeta)
 \ge RT(1-\zeta)(1-\bar\zeta).
\tag{CV3}
\]

For the single root `-1`, the same normalized estimate is
`R+T>=2 sqrt(RT)`. Thus any full nonprincipal cyclotomic packet
`Phi_h` satisfies

\[
 R^{\varphi(h)}\Phi_h(T/R)
 \ge (RT)^{\varphi(h)/2}\Phi_h(1)
 \ge (RT)^{\varphi(h)/2},\qquad h>1.
\tag{CV4}
\]

The standard elementary evaluation used here is `Phi_h(1)>=1` for
`h>1` (equal to a prime for a prime power and to one otherwise).
All values are positive, since nonreal roots are paired.

When `b` is odd, `f` is a monic rational polynomial with roots of
unity, hence a product of full cyclotomic polynomials. Since `R>T`,
each nonprincipal packet contributes at least `T^(degree in Y)`.
Returning to `X` gives

\[
 \boxed{|F_0(3)|\ge(2^a-3^b)3^{d-b}\quad(b\text{ odd}).}
\tag{CV5}
\]

## 3. Which half packets can survive when b is even?

Assume `b` even. Let `chi(j)=(2/j)` for odd `j`, the real quadratic
character modulo eight. The cyclotomic automorphism indexed by an odd
integer `j` sends `sqrt2=zeta_8+zeta_8^(-1)` to `chi(j)sqrt2`.

For an order `h` not divisible by eight, the automorphisms fixing
`sqrt2` act transitively on primitive `h`th roots. One can check this
without an implicit conductor assumption: prescribe any unit residue
modulo `h` and choose a compatible residue of character `+1` modulo
eight. If `v_2(h)<=2`, the Chinese remainder compatibility always allows
such a choice. Thus the whole cyclotomic packet must occur.

For `8|h`, there are exactly two orbits, distinguished by `chi(j)=+1`
and `chi(j)=-1` among primitive exponents. Let their monic polynomials
be `f_(h,+)` and `f_(h,-)`. Each orbit is closed under complex
conjugation, since `chi(-1)=1`, so both evaluate positively at one.

The nontrivial automorphism `sigma` of `K` sends `R` to `-R`.
Rationality of `H`, together with even `N`, gives

\[
 f^\sigma(Y)=f(-Y).
\tag{CV6}
\]

If `16|h`, replacing a primitive root by its negative replaces exponent
`j` by `j+h/2`, preserving `chi(j)`. Thus negation preserves each half,
whereas `sigma` exchanges the halves. Equation (CV6) forces both halves
to be present or both absent. They then form a full packet.

Only when `h=8m` with `m` odd does negation exchange the two halves.
Such a half packet may occur by itself. The next section bounds its
value directly. This retains every partially split rational factor;
it does not assume that all homogeneous cyclotomic substitutions are
irreducible.

## 4. Exact values at one of the exceptional halves

For odd `m>=1`, define

\[
 A_m=\log f_{8m,+}(1),\qquad B_m=\log f_{8m,-}(1),
 \qquad \delta_m=A_m-B_m.
\]

First drop the coprimality condition with `m`, retaining all exponents
of character `+1`. These exponents consist of the two progressions
`1+8k` and `7+8k`, for `0<=k<m`. Their product at one is

\[
 (1-\zeta_8)(1-\zeta_8^{-1})=2-\sqrt2.
\]

The analogous character-minus product is `2+sqrt2`. Partition either
product according to `d=gcd(j,m)`. Since `chi(j)=chi(d)chi(j/d)`,
taking the difference of logarithms gives

\[
 \sum_{d\mid m}\chi(d)\delta_{m/d}
 =\log\frac{2-\sqrt2}{2+\sqrt2}=-2\log u.
\tag{CV7}
\]

Möbius inversion, using complete multiplicativity of `chi` on odd
integers, yields

\[
 \boxed{\delta_m=-2\log u\prod_{\ell\mid m}(1-\chi(\ell)).}
\tag{CV8}
\]

For `m>1`, `Phi_(8m)(1)=1`, so `A_m+B_m=0`. Every factor in the
product in (CV8) is zero or two. Hence

\[
 f_{8m,\pm}(1)\ge u^{-2^{\omega(m)}}\ge u^{-\varphi(m)}.
\tag{CV9}
\]

The second inequality follows from `2^omega(m)<=phi(m)` for odd
`m>1`: each prime-power totient is at least two. The degree of either
half is `phi(8m)/2=2 phi(m)`. When `m=1`, the exact values
`2±sqrt2` are both at least `u^(-1)`, which gives the same bound by
half the degree. Consequently every exceptional half of degree `k`
satisfies

\[
 \boxed{f_{8m,\pm}(1)\ge u^{-k/2}.}
\tag{CV10}
\]

Pairing its conjugate roots in (CV3) now gives a homogeneous value at
least `(RT/u)^(k/2)`.

## 5. Assemble all components and the principal factor

After removing the principal binomial in the even case, the normalized
remaining degree is `2(d-b)/b`. A full packet satisfies the stronger
bound (CV4), and every allowed exceptional half satisfies (CV10).
Multiplying gives

\[
 |(F_0/(X^b-2^a))(3)|
 \ge\left(\sqrt{3r}\,u^{-1/b}\right)^{d-b}
 \ge\beta^{d-b},
\tag{CV11}
\]

because `r>3` and `b>=2`. For odd `b`, (CV5) gives the stronger
base three. The empty remaining factor is allowed.

The reduced linear form `L=a log2-b log3` is positive. By the
explicit fixed-base Matveev specialization already checked in the core
note, `L>c_0 b^(-K_0)` when `a<=2b`. Therefore

\[
 2^a-3^b=3^b(e^L-1)\ge3^b L
 >c_0 3^b b^{-K_0}.
\tag{CV12}
\]

Equations (CV5), (CV11), and (CV12), with `3>=beta` and `b<=d`,
prove the proposed (CV1). No continued-fraction finite gap certificate
is used in this asymptotic value bound.

## 6. Comparison with the maximum state, and the remaining failure

For actual primitive integer cycles, the core proof gives `m<=C_m d^K`.
The ordinary-state count gives an absolute upper bound on `Lambda`.
The lattice estimate (RL9a) then yields

\[
 M\le C_1 d^K(3/2)^{d-1}.
\]

Thus (CV1) would imply

\[
 \boxed{
 \frac{D_{\rm pol}}M
 \ge c_1\frac{(\beta/(3/2))^d}{d^{K+K_0}},
 \qquad \beta/(3/2)=\frac2{\sqrt{1+\sqrt2}}>1.
 }
\tag{CV13}
\]

This makes the residual denominator exponentially larger than **every
actual cycle state**, not only the minimum, along hypothetical
unbounded cycles. It still does not prove nondivisibility: no theorem
that the distinguished-fiber gcd is at most `M` has been established.
The denominator-five rational control in the lattice note explicitly
violates such a height bound under its rational-word hypotheses.

The first unsupported closing step remains an integral-specific bound
on the same-fiber gcd, or a different contradiction for the primitive
integer polynomial `J`. The proposed stronger value estimate must also
receive its separate independent review before being treated as part
of the core written theorem packet.
