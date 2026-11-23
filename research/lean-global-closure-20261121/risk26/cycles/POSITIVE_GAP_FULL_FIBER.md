# Direct positive-gap attack at the complete numerical fiber

23 November 2026. **Status: exact reductions and an unsuccessful
unrestricted closing attempt. Full positive integer cycle exclusion is
OPEN.** This follows the primitive-numerator calculation in
`FULL_FIBER_INTEGER_NUMERATOR_ATTACK.md`; it does not replace the target
by a fixed alphabet, fixed number of blocks, or a complementary cycle.

## 1. Restore the exact law omitted by the polynomial model

The positive polynomial model in the companion note has full integer
cancellation and the known root and height properties, but its first
carry exponents include `5,5`. For an actual odd cycle the stronger law
is

\[
u_j=2^{s_j},\qquad v_j=2^{s_j}x_j,\qquad x_j\text{ odd},
\quad v_{j+1}=3v_j+u_j,
\]

\[
\boxed{u_j=2^{v_2(v_j)},\qquad
s_{j+1}-s_j=v_2(3x_j+1)\ge1.}                      \tag{PG1}
\]

The terminal law is `v_p=2^A v_0` and `s_p=A`. Positivity of polynomial
coefficients, their divisibility by `2^j`, and an archimedean root
annulus do not imply PG1. A proof using PG1 must retain the odd part of
each coefficient, rather than replace it by a real root-radius bound.

The last coefficient is essential even for local legality. Given the
complete positive-gap carry law and an integral quotient `m`, synthetic
division defines integer `v_j` with `v_(j+1)=3v_j+2^(s_j)` and
`v_p=2^A m`. Starting from `s_p=A`, backward induction shows
`v_2(v_j)=s_j`: the next coefficient is divisible by `2^(s_j+1)`,
whereas the subtracted carry term has valuation exactly `s_j`.
Division by three does not change that valuation. Thus the full
terminal law and strict gaps recover all ordinary odd states. Treating
the terminal coefficient as an arbitrary positive integer, as in the
countermodel, removes precisely this backward induction.

We tested three ways of carrying this law into the full cancellation
problem: local evaluation ideals, a determinant of the actual recurrence,
and the new cross-carry lattice mechanism.

## 2. Exact prime-power rotation constraints

Keep the original full `F=X^p-2^A`, its full monic polynomial gcd `G`,
and the residual pair `F0,Q0`. Let `Q_i` denote the residual numerator
after the `i`th odd rotation. The complete polynomial identity is

\[
2^{a_i}Q_{i+1}(X)=XQ_i(X)-F_0(X).                    \tag{PG2}
\]

Put `D=|F0(3)|`. Since `D` divides `|2^A-3^p|`, it is coprime to
six. Reducing PG2 modulo the **whole** `D` gives

\[
Q_{i+1}(3)\equiv3\,2^{-a_i}Q_i(3)\pmod D.           \tag{PG3}
\]

Every multiplier is a unit. Therefore all rotated full-divisibility
conditions are equivalent, not independent. More precisely, for each
prime power `ell^e` dividing `D`,

\[
\boxed{\min\{e,v_\ell(Q_{i+1}(3))\}
=\min\{e,v_\ell(Q_i(3))\}.}                         \tag{PG4}
\]

If the right valuation is less than `e`, the `F0(3)` term in PG2 has
strictly larger valuation and cannot cancel its leading unit. If it is
at least `e`, both terms are divisible by `ell^e`. This proves PG4
without assuming squarefreeness or discarding exceptional prime powers.

After a full turn, the multiplier is `3^p 2^(-A)`, congruent to one
modulo `D`. Hence the cyclic consistency of PG3 itself imposes no new
condition on the initial residue. The system of homogeneous rotated
values is one cyclic module, parameterized by `Q0(3) mod D`.

**First failed inference in this route.** The strict positivity of the
gaps changes the units in PG3 but does not make the rotated congruences
independent. An estimate that multiplies their local rarity or charges
each rotation a new factor of `D` is unsupported. This is a prime-power
version of the same full-fiber boundary already retained in PR182.

## 3. Why the two special primes do not decide the original integer grid

For any positive-gap word with `2^A>3^p`, its rational fixed point is
`Q(3)/(2^A-3^p)`. The denominator is coprime to six. At every rotation
the numerator is odd, since its leading term is odd and all subsequent
terms have a factor two. Modulo three only its constant term survives,
and that term is a power of two. Consequently every rational cycle
state is an odd two-adic unit and a three-adic unit. Its prescribed
gaps are exact: the affine equations hold and all successor states
are odd units, so the valuations of `3x_i+1` are the specified `a_i`.

Thus the strict-gap law is compatible with every legal rational word at
the places two and three. The remaining reduced denominator is supported
at other primes dividing the original complete numerical denominator.
An integrality proof may combine the places two and three with a new
global estimate, but checking those two places alone does not remove
the reduced odd denominator.

This observation does not replace an ordinary source by a rational one.
It identifies why the proposed local proof cannot yet distinguish them.
The denominator-five risk25 control already demonstrates that a small
remaining odd denominator can coexist with a large full-fiber gcd.
That control was not rerun in this pass.

## 4. The actual Hankel determinant retains an uncontrolled integer factor

Let `u_j=2^(s_j)` and `v_j=2^(s_j)x_j` be extended periodically with
`u_(j+p)=2^A u_j`, `v_(j+p)=2^A v_j`. Their exact minimal polynomial
is `F0`; its `d` roots `lambda_1,...,lambda_d` are distinct. Write

\[
v_j=\sum_{k=1}^d b_k\lambda_k^j,
\qquad u_j=v_{j+1}-3v_j
=\sum_{k=1}^d (\lambda_k-3)b_k\lambda_k^j.
\]

Minimality makes every `b_k` nonzero. For any starting index `t`, let
`H_v(t)=(v_(t+i+j))_(0<=i,j<d)` and similarly define `H_u(t)`.
Vandermonde factorization makes both determinants nonzero and gives

\[
\boxed{\det H_u(t)=(-1)^d F_0(3)\det H_v(t).}         \tag{PG5}
\]

For nonnegative `t`, both matrices have integer entries on an actual
integer cycle. The determinant ratio is therefore exactly the original
residual denominator, with no evaluation at unrelated conjugates.

The positive-gap law gives the genuine dyadic factor

\[
2^{d(d-1)}\mid\det H_u(0),\qquad
2^{d(d-1)}\mid\det H_v(0),                           \tag{PG6}
\]

because `s_(i+j)>=i+j`: extract `2^i` from row `i` and `2^j` from
column `j`. This common factor does not constrain the odd ratio in
PG5. Extra two-adic valuations can arise from cancellation in either
determinant. The odd part of a Hankel determinant of powers of two
need not be one: the legal prefix `(a0,a1)=(1,3)` has

\[
\det\begin{pmatrix}1&2\\2&16\end{pmatrix}=12.
\]

This small prefix is only a determinant control, not a closing word or
a cycle.

There is also an archimedean normalization at the minimum. With
`r=2^(A/p)` and `t_j=s_j-Aj/p`, the actual identities imply
`2^(t_j)<=exp(Lambda)` for `0<=j<p`; periodicity extends this bound.
Hadamard's inequality therefore gives

\[
|\det H_u(0)|
\le r^{d(d-1)}d^{d/2}e^{d\Lambda}.
\]

After removing only the guaranteed factor in PG6, the allowed size is

\[
\boxed{(r/2)^{d(d-1)}d^{d/2}e^{d\Lambda},}            \tag{PG7}
\]

which has logarithm of order `d^2`, even when `r` tends to three.
The desired denominator scale has logarithm of order `d`. The
known root and normalization estimates therefore do not force the
integer factor `det H_v/2^(d(d-1))` in PG5 to be too small.

**First failed inference in this route.** Replacing the determinant's
odd part by a unit, by `m`, or by `M` is not justified by the exact
positive-gap valuation law. The available determinant upper bound is
too large even before one tries to remove all of its additional common
dyadic factors. No full-fiber cancellation bound follows.

## 5. Applying the new contracting-block mechanism to actual cycle cuts

The PR177 unequal-block theorem is genuinely integer-specific. It can
force all boundary values into one smooth residue class, and a minimum
corner must then pay a complete two-block denominator. We tested whether
an arbitrary hypothetical cycle can be amplified until its blocks satisfy
the theorem's strict inequality.

Take any two complementary actual segments joining distinct cycle states
`x` and `y`. Write their complete data as

\[
Q_1y=P_1x+C_1,\qquad Q_2x=P_2y+C_2,
\]

where each `Q_i` is a power of two and each `P_i` a power of three.
No contracting assumption is needed for the following exact identity:

\[
\begin{aligned}
(Q_2-P_2)C_1-(Q_1-P_1)C_2
&=(Q_1Q_2-P_1P_2)(y-x).
\end{aligned}                                       \tag{PG8}
\]

The first factor on the right is the original complete denominator
`2^A-3^p`. If `y>x` are integer states, remove the entire 6-smooth
part from the positive cross-carry. Since the full denominator is
coprime to six, the remaining part is exactly

\[
\boxed{(2^A-3^p)(y-x)_*,}                            \tag{PG9}
\]

where `n_*` denotes the part of `n` coprime to six. It is at least
the full denominator. This is exactly the non-strict lower threshold
in PR177's necessary inequality, not a contradiction.

Prepending `k` complete laps at the correct phase to each segment makes
both affine blocks contracting for sufficiently large `k`. But their
complete two-block clocks are then `(2k+1)A,(2k+1)p`. The same calculation
gives

\[
\boxed{E_k=(2^{(2k+1)A}-3^{(2k+1)p})(y-x).}           \tag{PG10}
\]

The cross-carry's non-smooth part grows with the **same complete
denominator** that the minimum corner must pay. Thus arbitrarily long
ordinary repetitions do not create the strict cross-carry upper bound.
There is no substitution of an unrelated block denominator in PG10.

For a fixed dictionary chosen independently, PR177's strict inequality
can still be useful. What failed here is the attempt to manufacture
that inequality from an arbitrary original cycle by repeating its laps.
The calculation covers arbitrary periods and arbitrary actual cuts.

## 6. Exact status after the positive-gap attempt

PG1 restores the coefficient law omitted by the polynomial countermodel.
It provides the correct two-adic behavior of the actual recurrence, but
PG3--PG4 leave only the original residue condition at each denominator
prime. PG5 puts the same full denominator into an exact integer
determinant ratio; PG7 is too weak to bound its odd part. PG8--PG10
show that the strongest new common-lattice mechanism does not amplify
arbitrary cycle cuts into a strict contradiction.

The first unresolved step is therefore not a formal link or an absent
conditional wrapper. It is an arithmetic inequality for the same
full-fiber odd gcd or determinant factor, using the complete exact
positive-gap law. Neither a fixed-S-unit theorem with growing dimension
nor the automatically primitive integer polynomial supplies it.

No unrestricted cycle exclusion is asserted. No old finite controls,
historical cycle census, or new bounded-family exclusion is offered as
a replacement for that missing step.
