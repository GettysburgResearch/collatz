# Which ordinary points lie inside affine merger certificates?

**PROPOSED; unconditional on the stated convergent domain.** This is an exact
local membership theorem, not a proof of Collatz. It refines the distinction
between a compatible affine family and the individual ordinary parameters at
which its fixed-word certificates apply.

Use the positive shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

The source is PR #146 at
`561d48a4d3a793a59b1cdf0406062ae1a6d47515`,
[`research/upper-bit-mergers/AFFINE_RAYS.md`](https://github.com/GettysburgResearch/collatz/blob/561d48a4d3a793a59b1cdf0406062ae1a6d47515/research/upper-bit-mergers/AFFINE_RAYS.md).
That note proves that slopes with the same factor after removing 2 and 3 admit
certificates in a refinement of every binary class. It does **not** assert that
every ordinary parameter belongs to a successful refinement. The stopping
defect used here is inherited from PR #149 at
`92c0129e794dde3ec55ceec470a12d51ba3f7e2f`,
[`research/persistent-defect-classes/README.md`, Section 1](https://github.com/GettysburgResearch/collatz/blob/92c0129e794dde3ec55ceec470a12d51ba3f7e2f/research/persistent-defect-classes/README.md).
That note explicitly credits the overlapping opposite-sign grade in PR #148
at `6ff18e4f63be8f3bece76215fcfe44d83b001d7f`. Its definition and elementary
cocycle are reconstructed below, without a novelty claim for the invariant.
No global boundedness or existence assertion from either PR is needed.

## Definitions

For a positive integer known to reach 1, let `d(n)` be its first-hit clock and
`p(n)` the number of odd inputs before that first hit. Set

\[
\kappa(n)=d(n)-2p(n),\qquad
w(a)=v_2(a)+2v_3(a),\qquad
a_*=a/(2^{v_2(a)}3^{v_3(a)}).
\]

At 1 the first-hit clock and odd count are both zero. The complete cycle
`1 -> 2 -> 1` has two steps and one odd input, so padding a path by complete
cycles leaves `clock - 2 odd_count` unchanged. Consequently, if an orbit
prefix from `n` reaches `z` at clock `i` with `q` odd inputs, and `n` reaches 1,
then

\[
\kappa(n)=i-2q+\kappa(z). \tag{G1}
\]

For fixed positive integer slopes `a_i`, integer offsets `b_i`, and an ordinary
parameter `t0` with all `a_i t0+b_i > 0`, a **local affine merger certificate
through t0** consists of a binary class containing `t0` and one fixed legal
parity word for each arm. On every parameter in that class with all starts
positive, those fixed words end at the same value. Clocks may differ between
arms. The common endpoint may depend on the parameter.

## LC-1: exact membership theorem

Suppose every arm `x_i=a_i t0+b_i` reaches 1. A local affine merger certificate
through `t0` exists if and only if both conditions hold:

1. All `a_i,*` are equal.
2. All integers `kappa(x_i)-w(a_i)` are equal.

The list is finite and nonempty. No claim is made that the arms reach 1 at
arbitrary ordinary parameters.

### Necessity

A shortcut word of length `l_i`, with `q_i` odd inputs, has endpoint slope
`a_i 3^{q_i}/2^{l_i}` as a function of the parameter. Equality on a binary
class gives equality at infinitely many positive parameters, hence equality
of these slopes. Unique factorization gives, for every pair `i,j`,

\[
l_i-l_j=v_2(a_i)-v_2(a_j),\qquad
q_i-q_j=v_3(a_j)-v_3(a_i),
\]

and equality of the residual factors `a_i,*`. At `t0` the endpoint `z` is in
the basin of 1. Subtracting (G1) for the two arms gives

\[
\kappa(x_i)-\kappa(x_j)
 =l_i-l_j-2(q_i-q_j)=w(a_i)-w(a_j).
\]

This proves necessity, including certificates that meet before either arm
first visits 1.

### Sufficiency and explicit certificate

Write `u_i=v2(a_i)`, `v_i=v3(a_i)`, and let the common adjusted defect be `C`.
Choose any integer

\[
h\ge\max(0,\max_i(d(x_i)-u_i)),\qquad h\equiv C\pmod2.
\tag{G2}
\]

Set `l_i=h+u_i`. The difference `l_i-d(x_i)` is nonnegative and even, since
`d(x_i)-u_i` has the parity of `C`. Follow the first-hit path from `x_i` and
pad by `(l_i-d(x_i))/2` complete cycles. Every resulting word ends at 1. Its
odd count is

\[
q_i=p(x_i)+(h+u_i-d(x_i))/2,
\qquad q_i+v_i=(h-C)/2=:Q.
\]

Every exponent here is integral and `Q>=0`, since `q_i+v_i>=0`.
On `t=t0+2^h k`, the initial value in arm `i` changes by a multiple of
`2^{h+u_i}=2^{l_i}`. Thus all `l_i` parity decisions stay unchanged. The
endpoint changes by

\[
\frac{a_i3^{q_i}}{2^{l_i}}\,2^h k
  = a_*3^Q k.
\]

Therefore every arm ends at exactly

\[
                    1+a_*3^Q k. \tag{G3}
\]

This proves sufficiency on every positive lift. Positivity of intermediate
states follows from ordinary positive shortcut iteration, not from a
2-adic realization argument. The smallest nonnegative `h` satisfying (G2)
is at most `max(0,max_i(d(x_i)-u_i))+1`.

## LC-2: the multiplication-by-three criterion has an ordinary residual set

For a positive `n` such that `n` and `3n` both reach 1, the pair belongs to a
local affine merger certificate in the family `(t,3t)` precisely when

\[
                    \kappa(3n)-\kappa(n)=2. \tag{G4}
\]

For example `n=15` has first-hit data `(d,p)=(12,5)`, while `45` has
`(d,p)=(12,4)`. Thus `kappa(15)=2`, `kappa(45)=4`; choosing `h=12` gives

\[
T^{12}(15+4096k)=T^{12}(45+12288k)=1+243k
\]

for every nonnegative integer `k`. This is an infinite ordinary merger
family, and (G4) decides why the parameter 15 belongs to it.

In contrast, for every integer `r>=0`,

\[
\kappa(2^r)=r,\qquad\kappa(3\cdot2^r)=r+1.
\]

The second identity uses the exact path `3 -> 5 -> 8 -> 4 -> 2 -> 1`, whose
clock is 5 and odd count is 2. These pairs all meet at 1, but **none** belongs
to any binary-class fixed-word merger certificate in the family `(t,3t)`.
For each fixed word pair that certifies such an ordinary meeting, the
endpoint slopes differ, so equality singles out at most one parameter.

This is not merely a mismatch between the two phases of the cycle. A second
explicit family is `n=5*2^r`: the first-hit data of 5 and 15 are `(4,1)` and
`(12,5)`, respectively, so

\[
\kappa(5\cdot2^r)=\kappa(15\cdot2^r)=r+2.
\]

These two arms eventually have the same value **and the same odd count at
the same clock**, yet their triple-ray slope condition requires one extra
odd input on the first arm. Hence these parameters also lie outside every
local certificate in the family `(t,3t)`.

Consequently even the union of *all* cylinder certificates for `(t,3t)`
misses infinitely many explicitly convergent ordinary parameters. Adding
finitely many individual parameters cannot repair that cover. This does not
rule out a proof that also uses doubling, induction, or another systematic
ordinary rule: doubling already handles the displayed power-of-two family.

The source's theorem that every binary class has a successful subclass is
fully compatible with this obstruction. A fixed positive integer cannot
choose its higher digits after it has been specified.

## LC-3: arbitrary compatible affine lists and isolated meetings

If the adjusted defects are not all equal at a convergent parameter, then
every fixed-word description of its simultaneous meeting is nonidentical
as a function of the parameter. At least one pair of arms has unequal
endpoint slopes, and that pair's equality holds at at most one parameter.
This is a finite-word statement. It does not rule out ordinary meetings
with words that change with the parameter.

For the family `(t,3^r t)`, with both values known to reach 1, the exact local
condition is `kappa(3^r n)-kappa(n)=2r`. For equal-slope translates it is
equality of their stopping defects. These statements follow directly from
LC-1 and do not assume convergence of any unverified shifted-power family.

## What this does and does not advance

The new result classifies local membership at an individual convergent
ordinary point and supplies a certificate constructor. The source's
slope-only theorem classifies existence somewhere inside each binary
class. Those are different quantifiers. The inherited stopping defect
makes their exact boundary decidable once the finite first-hit paths are
supplied.

The multiplication-by-three equivalence in PR #146 still leaves the
universal ordinary merger statement open. To close it using cylinder
certificates, an additional ordinary argument must cover their residual
set. Merely producing more successful refinements, or proving they are
dense, does not do so. No bound on that residual set strong enough for
pointwise closure is proved here.

The accompanying standard-library checker independently follows integer
orbits, reconstructs affine numerators from the resulting words, builds
certificates from (G2), and checks positive lifts. Its finite census and
controls support implementation correctness; LC-1's all-parameter content
comes from the written proof above.
