# The global Riesz remainder and an arithmetic barrier attack

Date: 23 November 2026.

**Status: written exact deductions and a closing attempt; escape exclusion
remains OPEN.** The first part identifies the entire ordinary atomic cone
inside one explicit excessive measure. Its defect has an explicit Hurwitz
zeta mass, and its Green integral is finite without an orbit-termination
assumption. The uncomputed remainder is exactly the total escape mass.

The second part attacks the remainder through actual arithmetic barriers.
A correction based on trailing binary ones controls every gap-one block,
but fails at the legal edge `41 -> 31`. Dense rational cycles of both signs
and an exact product-cylinder routing argument then give a complete
classification of continuous binary/ternary leading profiles for
`n^beta (log n)^delta`, with `beta>0`. A nonzero profile survives only
for `beta=1`, `delta=0`, and a constant profile. The classification permits
a uniform lower-order error and changes at finitely many ordinary states.
The rational cycles used in its proof are not positive integer
counterexamples. No new exclusion of an ordinary escaping component is
claimed, and arbitrary slowly varying multipliers are qualified separately.

## 1. Domain and exact inputs

Let

\[
 O=\{n\ge1:n\text{ is odd},\ 3\nmid n\},\qquad
 U(n)=\frac{3n+1}{2^{a(n)}},\quad a(n)=v_2(3n+1),
 \quad \lambda(n)=\frac{3n}{3n+1}.
 \tag{AE1}
\]

Use the operator on `X=Z_3^times` from
[the preceding pressure note](HIGH_VARIANCE_ESCAPE.md):

\[
 P_s f(q)=\sum_{\substack{e\ge1\\I_eq\in X}}
       (3/2^e)^s f(I_eq),\qquad I_eq=(2^eq-1)/3.
 \tag{AE2}
\]

At an ordinary root, every retained branch is an actual positive odd unit
parent. Conversely, for a fixed `n in O`, only `e=a(n)` has its forward
target in `O`. This uniqueness is used in every atom computation below.

The exact inherited input is PR177 at
`6de3e304bb49a93a6c5ef0e5563137e75c7defb4`,
`HIGH_VARIANCE_ESCAPE.md`, HE2 and HE18--HE24a: an escaping orbit has
`Lambda_infinity(n)=product_j lambda(U^j n)>0`, and its component measure
has atoms `(Lambda_infinity(n)/n)^s`. The elementary orbit-cylinder proof
of product positivity in that source is the only infinite arithmetic
input needed for the identification in Section 2.

Two newly advanced peer files were read for overlap and boundary checks:

- PR175, `8870528daa6a13cc941d602e578e35c8bfa4bf4f`,
  `research/lean-global-closure-20261121/risk23/FOURIER_IDEMPOTENT_CLOSURE_ATTEMPT.md`:
  symmetric Fourier-measure regularity, exact pullback failures, and the
  still-unproved norm bound for the actual basin. None is assumed here.
- PR180, `04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`,
  `research/high-variance-20261123/ANALYTIC_GLUING.md`:
  the actual real boundary and coherent affine deformation, including the
  failure to obtain a second integral parameter. Its qualified canonical
  population and routing inputs are not used below.

All infinite results in this file are written mathematics. The term
"Riesz decomposition" describes the explicit telescoping construction
below; no general representation theorem is imported.

## 2. A single explicit measure contains every escape component

For `s>1` put

\[
 H_s=\sum_{n\in O}n^{-s}\delta_n,
 \qquad
 D_s=\sum_{n\in O}n^{-s}(1-\lambda(n)^s)\delta_n.
 \tag{AE3}
\]

Both are finite positive measures. If a measure `nu` is written as a row,
`nu P_s` means the measure satisfying
`(nu P_s)(f)=nu(P_s f)` for nonnegative measurable `f`.

### AE-P1. Exact excessive measure and total-variation remainder

For every `n in O`,

\[
 (H_sP_s)(\{n\})
   =(3/2^{a(n)})^s(Un)^{-s}
   =\left(\frac3{3n+1}\right)^s
   =n^{-s}\lambda(n)^s.
 \tag{AE4}
\]

Thus `H_sP_s=H_s-D_s<=H_s`. Inductively, with
`Lambda_N(n)=product_(j<N) lambda(U^j n)`,

\[
 (H_sP_s^N)(\{n\})=n^{-s}\Lambda_N(n)^s.
 \tag{AE5}
\]

The measures decrease pointwise in `N`, and their atom masses are
dominated by the summable sequence `n^{-s}`. Therefore they converge in
total variation to

\[
 R_s=\sum_{n\in O}n^{-s}\Lambda_\infty(n)^s\delta_n.
 \tag{AE6}
\]

If an orbit enters a positive cycle, its product tends to zero: one
complete turn multiplies it by a fixed product of numbers strictly
between zero and one. If it does not enter a cycle, it is injective and
escapes, and the inherited elementary product bound is strictly positive.
Consequently

\[
 \boxed{R_s=\sum_{E\text{ escaping}}\mu_{E,s}.}
 \tag{AE7}
\]

This is a countable sum with finite total mass, bounded by `H_s(X)`.
The equality uses the actual ordinary components, not closures in the
ternary topology. The preceding classification gives `R_sP_s=R_s`.
It can also be obtained directly by the edge formula in (AE6).

Finite telescoping now proves the global decomposition

\[
 H_s=\sum_{j=0}^{N-1}D_sP_s^j+H_sP_s^N,
 \qquad
 \boxed{H_s=\sum_{j\ge0}D_sP_s^j+R_s.}
 \tag{AE8}
\]

The sum on the right is increasing and converges in total variation.
This identifies the exact invariant part of the explicit excessive
measure. In particular, it supplies a concrete pure-potential target:
escape is absent exactly when that invariant part is zero.

### AE-P2. The defect Green integral is finite and its missing mass is exact

Let `Z_s=sum_(j>=0) P_s^j 1`, allowing the value infinity. Tonelli and
(AE8) give, for every `s>1`,

\[
 \boxed{\int_X Z_s\,dD_s=H_s(X)-R_s(X)\le H_s(X)<\infty.}
 \tag{AE9}
\]

No pointwise estimate for `Z_s` is needed to justify this integral.
Indeed, the coarse bound `Z_s(n)<=zeta(s)n^s` would only leave a
harmonic `sum 1/n` when multiplied by the defect masses and would not
prove finiteness. The finite telescoping identity supplies the needed
domination before the infinite sum is taken.

This is compatible with the previous identity
`integral Z_s dmu_E,s=infinity`: the source defect and the invariant
remainder are different measures. On an original escaping source `n`,
the contribution of the defect at future time `N` is exactly

\[
 (D_sP_s^N)(\{n\})
  =\frac{\Lambda_N(n)^s}{n^s}
       \bigl(1-\lambda(U^Nn)^s\bigr).
 \tag{AE10}
\]

Its sum is `n^{-s}(1-Lambda_infinity(n)^s)`; the remaining atom is
strictly positive. Thus the extra decay of the defect does not consume
the entire source mass.

The explicit total masses are

\[
 \begin{aligned}
 H_s(X)&=(1-2^{-s})(1-3^{-s})\zeta(s),\\
 (H_sP_s)(X)&=6^{-s}
       \bigl[\zeta(s,2/9)+\zeta(s,8/9)\bigr],\\
 D_s(X)&=H_s(X)-(H_sP_s)(X).
 \end{aligned}
 \tag{AE11}
\]

Here `zeta(s,a)=sum_(j>=0)(j+a)^{-s}`. To verify the second line,
partition `O` as `6j+1` and `6j+5` in (AE4); the respective denominators
are `18j+4` and `18j+16`. The first line removes the multiples of two
and three from the positive zeta series.

At the second Haar-critical parameter this becomes

\[
 \boxed{R_2(X)=\frac{\pi^2}{9}-\int_X Z_2\,dD_2.}
 \tag{AE12}
\]

The Haar identity `mP_2=m` does not evaluate the integral against the
atomic `D_2`. The attempt to obtain that missing evaluation from the
extra decay is already exhausted by (AE9)--(AE10). Equation (AE12)
does not assert that the two terms on its right cancel.

## 3. Shifting the real height: the exact failed exhaustion

For `t>=0` define

\[
 H_{s,t}=\sum_{n\in O}(n+t)^{-s}\delta_n.
 \tag{AE13}
\]

Its mass tends to zero as `t` tends to infinity, by domination by `H_s`.
If `q_N=U^Nn` and `w_N=3^N/2^{A_N}`, its iterates have atoms

\[
 (H_{s,t}P_s^N)(\{n\})
 =\left(\frac{w_N}{q_N+t}\right)^s
 =\frac{\Lambda_N(n)^s}{n^s}
        \left(\frac{q_N}{q_N+t}\right)^s.
 \tag{AE14}
\]

For every fixed `t`, these converge in total variation to the same
`R_s`: on an escaping source `q_N` tends to infinity, and on a source
entering a cycle the product tends to zero. The domination in (AE5)
applies for all `t>=0`. Thus any positive remainder would give the exact
noncommutation

\[
 \lim_{t\to\infty}\lim_{N\to\infty}(H_{s,t}P_s^N)(X)=R_s(X),
 \qquad
 \lim_{N\to\infty}\lim_{t\to\infty}(H_{s,t}P_s^N)(X)=0.
 \tag{AE15}
\]

One might try to dominate that common remainder by each `H_{s,t}` and
then send `t` to infinity. The needed excessivity has an exact threshold:

\[
 H_{s,t}P_s\le H_{s,t}
 \quad\Longleftrightarrow\quad
 1+(2^{a(n)}-3)t\ge0\quad\text{for every }n\in O.
 \tag{AE16}
\]

This follows by comparing the two atom denominators. Since gap-one
states exist in `O`, the condition holds precisely for `0<=t<=1`.
For every `t>1`, every such state has the wrong sign. For example
`7 -> 11` is an actual unit edge with gap one. Therefore the simple
shift-to-zero exhaustion is invalid at a finite ordinary edge; the
failure is not merely an unspecified exchange of limits.

## 4. A valuation correction and its actual failure

For a nonnegative function `v` on `O`, put

\[
 H_{s,v}=\sum_{n\in O}(n+v(n))^{-s}\delta_n.
\]

Its precise excessivity condition is

\[
 \boxed{3v(n)\le1+2^{a(n)}v(Un)\qquad(n\in O).}
 \tag{AE17}
\]

If `v(q_N)=o(q_N)` on an escaping ray, the limit of its transported
atom is again `(Lambda_infinity(n)/n)^s`. Hence a nonnegative family
`v_t` satisfying (AE17), pointwise diverging with `t`, and sublinear
along every hypothetical escaping ray would force `R_s=0`.
Constructing that family is the substantive requirement.

The first arithmetic candidate uses the entire trailing block of ones.
Let `odd(k)=k/2^{v_2(k)}` and

\[
 \beta=\frac{\log(3/2)}{\log3}\in(0,1),\qquad
 \psi(n)=\operatorname{odd}(n+1)^\beta,
 \qquad v_t(n)=1+t\psi(n).
 \tag{AE18}
\]

On every gap-one edge, `Un+1=3(n+1)/2`, and
`odd(Un+1)=3 odd(n+1)`. Thus
`psi(Un)=(3/2)psi(n)`, so (AE17) is an equality for every `t`.
This controls a gap-one run of arbitrary length with its actual binary
valuation retained.

It does not control the transition into such a run. At the legal edge
`41 -> 31`, the gap is two and the two odd parts are `21` and `1`.
For `t=4`, condition (AE17) would require

\[
 3+12\,21^\beta\le21.
\]

But `21^beta>3^beta=3/2`, giving the strict opposite inequality.
Thus this arithmetic correction cannot be increased to an unbounded
barrier family. The next result shows that merely repairing finitely
many binary or ternary residue classes cannot fix this type of power
ansatz globally.

## 5. Rational cycles of each sign are dense in both completions together

Let `Y=Z_2^times x Z_3^times`, with its product topology. Rational numbers
whose numerator and denominator are coprime to six embed diagonally in
`Y`. The word "cycle" in this section permits rational states.

For a positive gap word `W=(a_0,...,a_(h-1))`, let `A=sum a_i` and let
`C` be its positive affine correction, so its formal forward map is

\[
 F_W(x)=\frac{3^hx+C}{2^A}.
 \tag{AE19}
\]

Choose `L>=0` and `e>=1` and append `L` gaps equal to one and one final
gap `e`. The resulting word has length `r=h+L+1`, total `A+L+e`, and
correction

\[
 C_{W,L,e}=3^{L+1}(C+2^A)-2^{A+L+1}.
 \tag{AE20}
\]

It is positive because it is the actual positive gap-word correction.
For sufficiently large `L`,

\[
 D=3^{h+L+1}-2^{A+L+e}>0,
 \qquad x=-C_{W,L,e}/D<0
 \tag{AE21}
\]

is the rational fixed point of that word. Its multiplier is
`w=3^r/2^(A+L+e)>1`.

Every rotated word has the same positive `D` and a positive, odd
correction not divisible by three. Hence every cyclic state is
negative, belongs to both unit spaces, and has exactly the stipulated
2-adic valuation: `3x_i+1=2^{a_i}x_(i+1)` with `x_(i+1)` a 2-adic
unit. Reduction of the fraction does not change these properties.

### AE-P3. Joint density, separately for each sign

Fix any binary unit cylinder modulo `2^M` and ternary unit cylinder
modulo `3^K`. Choose a positive ordinary unit `q` in the binary cylinder,
and take a finite actual gap prefix `W` of `q` with `A>=M`.
Its endpoint `q_h` is odd and
`3^h q+C=2^A q_h`.

The explicit formula gives

\[
 C_{W,L,e}+Dq
 =3^{L+1}2^A(q_h+1)
     -2^{A+L}(2+2^eq),
\]

which is divisible by `2^(A+1)`. Since `D` is odd, the negative rational
cycle point satisfies `x=q mod 2^(A+1)` and lies in the desired binary
cylinder.

For `L+1>=K`, (AE20)--(AE21) also give

\[
 \boxed{x\equiv-2^{1-e}\pmod{3^K}.}
 \tag{AE22}
\]

Because two generates the units modulo `3^K`, an `e>=1` can be chosen
to put this residue in any prescribed ternary unit cylinder. Increasing
`L` afterwards preserves both congruences and makes `D>0`.
Thus these negative rational cycle points are dense in `Y`.

There is a second choice of parameters giving positive rational cycles
in the same two prescribed cylinders. First fix `L` with `L+1>=K`.
Choose `e` in the required residue class modulo `2*3^(K-1)`, and increase
it within that class until `2^(A+L+e)>3^(h+L+1)`. The correction in
(AE20) is unchanged, while `D` in (AE21) is now negative. Thus
`x=-C_(W,L,e)/D>0`, its multiplier is strictly below one, and both
congruences proved above still hold. Every rotated correction is
positive and coprime to six, so all cyclic states are positive, odd and
ternary-unit rationals. Positive rational cycle points are therefore
also dense in `Y`. Their fractions are not asserted to be integers.

The elementary primitive-root fact used here follows from
`4^(3^j)=1+3^(j+1) mod 3^(j+2)` by induction, together with
`2=-1 mod 3`. No distribution theorem about ordinary Collatz orbits is
being assumed.

## 6. Complete classification of continuous power-logarithm profiles

### AE-P4. Classification for the actual affine barrier

Fix `beta>0` and a real `delta`. Let `F:Y->[0,infinity)` be continuous.
Suppose a function on `O` has the uniform asymptotic form

\[
 v(n)=h(n)F(n,n)+o(h(n)),\qquad
 h(n)=n^\beta(\log n)^\delta
 \quad(n\to\infty,\ n\in O),
 \tag{AE23}
\]

and satisfies (AE17) for every sufficiently large ordinary `n`.
Then either `F` is identically zero, or

\[
 \boxed{\beta=1,\quad\delta=0,\quad F\text{ is a positive constant}.}
 \tag{AE24}
\]

This remaining possibility is realized: `v(n)=c n`, for any constant
`c>=0`, obeys (AE17), since its right side minus its left side is `1+c`.
Such a positive linear barrier is not sublinear along an escaping ray.
The conclusion classifies the nonzero leading profile, not every possible
lower-order perturbation of a linear barrier.

#### 6.1. Rational cycles eliminate every power exponent other than one

Fix a rational cycle from Section 5 starting at `x`, with word length
`r`, total valuation `A`, and affine map

\[
 F_W(z)=wz+b,\qquad w=3^r/2^A,\quad b>0,
 \qquad wx+b=x.
\]

For arbitrarily large precision `k`, CRT gives arbitrarily large positive
ordinary integers `n_k` agreeing with `x` modulo `2^(A+k)` and `3^k`.
They realize the complete finite word with exact valuations. All their
intermediate values tend to infinity in the real sense, so eventual
validity of (AE17) suffices. Their endpoints are `m_k=wn_k+b`.
Both points converge to `x` in `Y`, while `m_k/n_k -> w` in the real
absolute value. The exact iterated barrier is

\[
 \boxed{v(m_k)\ge wv(n_k)-b.}
 \tag{AE25}
\]

The correction is the same `b` because the barrier has the opposite
sign on its additive constant. Since `h(n_k)` tends to infinity and
`h(m_k)/h(n_k) -> w^beta`, division and continuity give

\[
 w^\beta F(x,x)\ge wF(x,x).
 \tag{AE26}
\]

For `beta<1`, use the dense negative cycles, whose multipliers exceed
one. For `beta>1`, use the dense positive rational cycles, whose
multipliers are below one. In either case (AE26) forces zero on a
dense set, so `F=0`.

The affine argument deliberately assumes `beta>0`, so that `h(n)`
tends to infinity and its bounded additive correction disappears.
For example the constant barrier `v=1` satisfies (AE17); the additive
term cannot be discarded at exponent zero.

#### 6.2. At exponent one the profile is constant

For `z=(z_2,z_3) in Y` with `z_2 != -1/3`, define

\[
 a(z)=v_2(3z_2+1),\qquad
 S(z)=\left(\frac{3z_2+1}{2^{a(z)}},
            \frac{3z_3+1}{2^{a(z)}}\right).
 \tag{AE27}
\]

The valuation is finite and positive, and the image is again in `Y`.
The map is continuous on each finite-valuation branch. Approximate `z`
by large positive ordinary integers with the same valuation, using CRT.
For `beta=1`, dividing the one-edge barrier by `h(n)` gives

\[
 \boxed{F(z)\le F(Sz).}
 \tag{AE28}
\]

Here the fixed-scale limit is `h(Un)/h(n) -> 3/2^{a(z)}` for every
real `delta`; the same multiplier occurs on both sides and cancels.

The following routing observation turns (AE28) into constancy. Given
any two nonempty product cylinders in `Y`, there is a finite orbit of
`S` starting in the first and ending in the second, with all displayed
valuations finite. To construct it, take an actual positive gap prefix
`W` whose initial binary cylinder lies in the source binary cylinder.
Its total valuation can be made at least that cylinder's precision.
Append `L` ones and a final gap `e`. If the target ternary precision is
`3^K`, take `L>=K` and choose `e` so
`-2^(1-e)` lies in the target ternary cylinder.

The maps `Phi_a(y)=(3y+1)/2^a` preserve ternary units. After `W`, the
`L` one-steps send any ternary unit `y` to
`-1+(3/2)^L(y+1)`, which equals `-1 mod 3^K`. The final gap therefore
places every initial ternary unit in the desired target cylinder.
In particular the initial ternary coordinate may be chosen freely
inside the prescribed source cylinder.

For the binary coordinate choose any odd 2-adic target in the desired
target cylinder and pull it backwards through the full word using
`I_a(y)=(2^a y-1)/3`. Each pullback is odd and has exactly the assigned
forward valuation. The initial prefix `W` places the resulting initial
coordinate in the desired source binary cylinder: two odd tails after
`W` change its initial coordinate by a multiple of `2^(A+1)`.
This proves the finite routing claim without asserting that those two
independently chosen coordinates are one ordinary integer.

There is also an ordinary realization of every such finite cylinder
bridge. Each of its finitely many valuation branches is open, and the
branch maps are continuous. A sufficiently small product neighborhood
of the constructed starting point therefore retains the complete word
and its terminal cylinder. CRT places arbitrarily large positive odd
ternary units diagonally in that neighborhood. They follow the actual
finite ordinary trajectory into the target cylinder. This does not
assert that one ordinary integer realizes an infinitely prescribed route.

Now choose cylinders on which `F` is arbitrarily close to its values at
any two given points. Iterating (AE28) along the constructed finite
orbit gives `F(first)<=F(second)` in the limit. Reverse the roles of
the cylinders to get the opposite inequality. Thus `F` is constant
on all of `Y`, including the excluded binary-pole fibre by continuity.

#### 6.3. Two exact ordinary families eliminate nonzero logarithmic powers

Suppose `F=c>0`. Then (AE23) says
`v(n)~c n(log n)^delta` uniformly on ordinary inputs. Put
`alpha=log 3/log 2`.

If `delta<0`, take arbitrarily large even `k` and the actual gap-one
segment

\[
 n_k=2^{k+1}-1,
 \qquad U^k n_k=2\,3^k-1=:q_k,
 \qquad w_k=(3/2)^k.
 \tag{AE29}
\]

The intermediate values are `2^(k+1-j)3^j-1`. For `j<k` their next
gap is exactly one. Even `k` makes the initial state a ternary unit;
every subsequent state is also a unit. The iterated barrier gives
`v(q_k)>=w_k v(n_k)-(w_k-1)`. But

\[
 \frac{v(q_k)}{w_k v(n_k)}\longrightarrow\alpha^\delta<1,
 \qquad
 \frac{w_k-1}{w_kv(n_k)}\longrightarrow0,
 \tag{AE30}
\]

a contradiction. The segment stops at the odd state `2*3^k-1`;
it does not append a spurious further gap-one step.

If `delta>0`, use the actual all-gap-two segment

\[
 n_k=1+2^{2k+2},
 \qquad U^k n_k=1+4\,3^k=:q_k,
 \qquad w_k=(3/4)^k.
 \tag{AE31}
\]

Its intermediate values are `1+2^(2(k-j)+2)3^j`. For `j<k` the
next gap is exactly two, and all states are ternary units. Now the
barrier gives `v(q_k)>=w_kv(n_k)-(1-w_k)`, whereas

\[
 \frac{v(q_k)}{w_kv(n_k)}\longrightarrow(\alpha/2)^\delta<1,
 \qquad
 \frac{1-w_k}{w_kv(n_k)}\longrightarrow0.
 \tag{AE32}
\]

The second limit holds because `w_kv(n_k)` grows exponentially like
`3^k k^delta`. This is again a contradiction. Hence `delta=0`.
These long actual integer blocks remove the need for any Hölder
assumption on `F` and retain the entire uniform lower-order error in
(AE23). This completes the classification.

### Scope for more general regularly varying scales

The fixed-word and cylinder-routing arguments apply more generally to
any positive scale `h` tending to infinity with

\[
 \frac{h(wn+b)}{h(n)}\longrightarrow w^\beta
 \quad\text{for each fixed }w>0\text{ and fixed }b.
 \tag{AE33}
\]

Under this explicit scaling hypothesis and a uniform `o(h)` error,
they force `F=0` when `beta!=1`, and force `F` to be constant when
`beta=1`. The power-logarithm theorem above then fully treats the
specified family of scales.

This does not classify every possible slowly varying multiplier at
index one. For instance the two long blocks have
`log log(q_k)/log log(n_k) -> 1`, so their displayed constant-ratio
contradiction does not extend automatically to arbitrary iterated
logarithms or other slowly varying factors. No assertion that every
regularly varying barrier must be asymptotic to `c n` is made here.

The failed candidate (AE18) is within the excluded power class: `psi`
has leading profile `F(x_2,x_3)=|x_2+1|_2^beta`, which is continuous
and vanishes at the single fixed point `-1`. Other negative rational
cycles force zeros on a dense set. The classification excludes nonzero
continuous profiles; it does not exclude discontinuous ordinary
arithmetic barriers or barriers outside the specified asymptotic forms.

## 7. A lifted thermodynamic closing test

The product map in (AE27) suggests a different transfer operator from
the ternary-only operator (AE2). Retain the binary coordinate and put

\[
 (Q_s f)(q_2,q_3)=
 \sum_{\substack{e\ge1\\I_e q_3\in\mathbb Z_3^\times}}
 (3/2^e)^s f(I_eq_2,I_eq_3).
 \tag{AE34}
\]

The binary images of different branches are disjoint valuation strata.
For product Haar probability `m_Y`, the inverse branch has Jacobian
`3/2^e`: it contracts binary measure by `2^{-e}` and expands ternary
measure by three. Changing variables branch by branch gives

\[
 \int Q_s f\,dm_Y
 =\int (3/2^{a(z)})^{s-1}f(z)\,dm_Y(z).
 \tag{AE35}
\]

The binary pole is a null fibre. In particular `m_Y Q_1=m_Y`.
For other `s`, the multiplier in (AE35) is a function of the binary
valuation; it is not the scalar Haar multiplier of the old ternary-only
operator on arbitrary product functions.

Each hypothetical component measure lifts diagonally to `Y`, with the
same atoms `r_E(n)^s` at `(n,n)`, and obeys `mu_E,s Q_s=mu_E,s`.
It has full joint support. For example, choose a word `W` coding a
desired initial binary cylinder, with length `h`, total `A`, and
correction `C`, and fix an ordinary root `q in E`. A parent obtained
by the word `W` followed by a last gap `e` is

\[
 n=\frac{2^{A+e}q-2^A-3C}{3^{h+1}}.
\]

To place it in a ternary unit class `b mod 3^K`, choose `e` solving
`2^(A+e)q=2^A+3C+3^(h+1)b mod 3^(h+K+1)`.
The right side is a ternary unit, so the primitive-root property gives
arbitrarily large such exponents. Then `n` and every intermediate state
are positive ordinary integers, the given word is exact, and the fixed
binary prefix puts `n` in the required binary cylinder. The resulting
positive atom belongs to `E`.

A positive right eigenfunction would be a powerful closing object.
If `Q_s h=h` on the ordinary component, `h` is nonnegative and positive
at some atom, and `integral h dmu_E,s` is finite, then `h mu_E,s` is a
nonzero finite `S`-invariant measure. Indeed
`Q_s[(f composed with S)h]=f h`. Such a measure is impossible on an
escaping component: invariance makes every future atom of a positive
atom have at least its mass, while those future vertices are distinct.
Thus the pointwise equation and this particular integrability would
exclude escape.

### The primary theorems do not supply that ordinary eigenfunction

There is already a concrete obstruction to a compact continuous
Perron-Frobenius argument. At a negative rational periodic point from
Section 5, one return branch in `Q_s^r` has weight `w^s>1`. If a
nonnegative finite function obeys `Q_s h=h` pointwise, then
`h(x)>=w^s h(x)`, so `h(x)=0`. By joint density, every nonnegative
continuous finite right eigenfunction at eigenvalue one is identically
zero. This holds for every `s>0`.

Sarig's primary survey, *Thermodynamic formalism for countable Markov
shifts*, Theorem 4.9, identifies the relevant extra hypotheses: a
topologically mixing countable Markov presentation, summable variations,
finite Gurevich pressure, and positive recurrence with a conservative
conformal measure give the integrable positive right eigenfunction.
Those hypotheses have not been established for a presentation retaining
the ordinary component and its conformal measure. The theorem does not
turn an arbitrary finite conformal measure into a recurrent one.
The exact inspected statement is on PDF page 16:
<https://www.weizmann.ac.il/math/sarigo/sites/math.sarigo/files/uploads/tdf-survey.pdf>.

There is a real measurable stationary-density input, but its exceptional
set matters. Tao's *Almost all orbits of the Collatz map attain almost
bounded values*, Remark 1.13 and Proposition 1.14, define the consistent
ternary Syracuse laws and bound the L1 difference of a fine law from
the uniform lift of a coarser law. Consequently their uniform cylinder
densities are L1-Cauchy and define a Haar-absolutely-continuous ternary
stationary law. Its stationary identity gives a right eigenfunction for
`Q_1` almost everywhere with respect to product Haar, independent of the
binary coordinate. This consequence does not give pointwise values or
the eigenfunction equation on the countable ordinary diagonal, and does
not give integrability against the ordinary atomic measure.
This density is specific to `s=1` and supplies no right eigenfunction for
the `s>1` operators carrying the finite ordinary component measures
constructed here.
Modifying values on that diagonal does not affect the Haar-almost-everywhere
statement. The primary statements were read in arXiv version 7,
pages 11--12: <https://arxiv.org/pdf/1909.03562v7>.

The lifted operator is therefore a valid different closing test, but
neither the continuous RPF route nor the inspected measurable density
result provides its required ordinary positive integrable eigenfunction.
No recurrence or pointwise regularity has been inserted as an assumption
in the earlier results of this note.

## 8. What remains after these attacks

The global residual is explicit and finite:

\[
 R_s(X)=\sum_{E\text{ escaping}}\sum_{n\in E}
           (\Lambda_\infty(n)/n)^s.
\]

The exact defect Green integral (AE9) computes its complement but has
not been independently evaluated as the full explicit mass `H_s(X)`.
The real-shift attempt stops at the actual gap-one sign in (AE16).
The valuation-based correction survives every gap-one run and then
fails at an actual gap-two transition. The dense rational-cycle proof
shows that a broad class of continuous profinite repairs cannot supply
the required sublinear affine barrier either.

These results do not imply that every arithmetic barrier is impossible.
In particular, no continuity has been proved for
the unknown ordinary selector that a successful proof might use. A
successful continuation must either evaluate the global potential
without discarding its residual, or construct a genuinely different
ordinary barrier outside the excluded regularity classes and prove its
needed positivity and sublinearity. No such closing inference is
claimed in this checkpoint.
