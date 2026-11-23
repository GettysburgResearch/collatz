# A sublinear inverse-density attack on the whole ordinary graph

**Status: OPEN global construction; proved arithmetic and Lean implication.**
The construction of a suitable density envelope is not completed. This note
records an attempted global potential, two explicit failures of natural
candidates, and the precise positive result obtained from the attempt. No
unproved envelope or convergence theorem is installed as a Lean axiom.

The shortcut map is the repository's `T`. On positive odd integers, write

\[
U(n)=\frac{3n+1}{2^{e(n)}},\qquad e(n)=v_2(3n+1).
\]

After at most one such odd step, every state is coprime to three. The
discussion below concerns these positive odd ternary units. It builds on
PR180 at `9010a8790535002b6d9ff92304f0ba289e2e98fe`, especially its ordinary
atom floor, and on the actual-map definitions imported from PR173 at
`fa0c9e2a2851e6324391e39c17afcb5913185aec`. The newer selected marked
contractions in PR182 and reserved mergers in PR184 were inspected at
`8372e302041a55057742a9e6ee9b4fa600c88fdb` and
`366dab89ee9548084ab9b5e4e90ff82abf287a20`; they are motivation, not extra
axioms or dependencies of this module.

## 1. The upper-envelope target

Let `D_s(q)` be the normalized Syracuse offset density from the pinned
[selected-density argument](../lean-ordinary-closure-20261121/LINEAR_BLOCK_ATOM_FLOOR.md).
For an ordinary positive unit `q`, its exact inverse recursion is

\[
D_{s+1}(q)=
 \sum_{\substack{e\ge1\\2^e q\equiv1\pmod3}}
 \frac3{2^e}D_s\!\left(\frac{2^e q-1}{3}\right).
\tag{A1}
\]

Every summand has a positive ordinary integer argument. This positivity is
essential: the proposed upper estimate is about ordinary arguments, not an
arbitrary point of the three-adic completion.

The earlier source-qualified atom floor gives an absolute `c0>0` and a depth
after which `D_s(q)>=c0` for every positive ternary unit. The concurrent
[renewal attack](GLOBAL_RENEWAL_ATTACK.md) now constructs an actual finite
positive excessive function `F` on ordinary arguments: its Cesaro atom
averages are bounded pointwise, Abel averaging preserves the inverse
recursion, and a diagonal limit followed by Fatou gives

\[
F(q)\ge c_0,\qquad (PF)(q)\le F(q)<\infty.
\tag{A2}
\]

Here `P` is the positive inverse operator in `(A1)`. This is a
source-qualified analytic construction, not a Lean formalization. It does
not require a pointwise limit of the original `D_s` to exist. An `L1`
three-adic limit by itself would not have supplied ordinary-point
finiteness; the explicit ordinary Cesaro estimate is doing that work.

Taking a finite pair of summands in `(A2)` yields

\[
F(q)\ge\frac3{2^e}F(n)+\frac3{2^f}F(b)
\tag{A2-pair}
\]

whenever `n` and `b` are distinct positive odd unit parents of `q` with the
indicated exponents. The new **open** target is to construct such an
excessive envelope with the additional property

\[
\boxed{\frac{F(q)}q\longrightarrow0
\quad(q\to\infty\text{ through positive odd units}).}
\tag{UE}
\]

The finite envelope just constructed is not claimed to satisfy `(UE)`.
Alternatively, a finite sublinear `liminf_s D_s(q)` would satisfy the same
two-parent inequalities by superadditivity of liminf, but that stronger
pointwise-density assertion is unnecessary for the formal mechanism.

The Lean module keeps `(A2-pair)` as the explicit proposition `PairTransfer`.
The source-qualified excessive-function construction and `(UE)` have not
been formalized or assumed there.

## 2. An off-parent term treats cycles and divergence together

Every positive odd unit target has two distinct positive odd unit parents with
exponents at most six. The following table gives the two exponents; the
parents are `(2^e q-1)/3`.

| `q mod 9` | First exponent | Second exponent |
|---:|---:|---:|
| 1 | 2 | 4 |
| 2 | 1 | 3 |
| 4 | 2 | 6 |
| 5 | 3 | 5 |
| 7 | 4 | 6 |
| 8 | 1 | 5 |

For any supplied actual odd edge `n -> q`, at least one of these two parents
is different from `n`. Its contribution in `(A2-pair)` is at least `3*c0/64`.
Consequently, with

\[
c=\frac{3c_0}{64},\qquad H(n)=\frac{F(n)}n,
\]

we obtain

\[
F(q)\ge\frac3{2^{e(n)}}F(n)+c.
\tag{A3}
\]

Since `2^e q=3n+1`, this implies the exact normalized inequality

\[
H(q)-H(n)\ge
\frac{c-H(n)/2^{e(n)}}q.
\tag{A4}
\]

Thus `H(q)>H(n)` whenever `H(n)<2c`. The extra parent is indispensable to
this strict increase. Keeping only the actual parent would give a small
loss rather than a strict improvement.

By `(UE)`, there is one finite `N` such that `H(n)<2c` for every odd unit
`n>=N`. Every positive ordinary orbit must physically visit an odd unit
below `N`. Here is a proof that treats cycles and divergence at once.

Assume an odd unit `n0` has no such visit. Positivity gives `H(n0)>0`.
The sublinear envelope makes the superlevel set

\[
\{n:\ n\text{ is an odd unit},\ H(n)\ge H(n_0)\}
\]

finite. Restrict it to states whose forward orbits avoid the floor, and
choose a state of maximal `H`. Its actual odd successor still avoids the
floor and has strictly greater `H` by `(A4)`. It belongs to the same finite
set, a contradiction.

This is stronger than a claim of eventual periodicity. It supplies a
**single finite absorbing floor for every ordinary positive source**.
Verifying convergence of the odd units below that explicit floor would
complete Collatz. The floor is not currently known: `(UE)` remains open.

### Lean declarations

`lean/InverseDensityPotential.lean` contains:

- `two_short_unit_parents` and `short_off_parent`: unconditional ordinary
  arithmetic, including distinctness and the exponent bound six;
- `additive_transfer_of_pair_floor`: the positive two-parent transfer plus
  an explicitly supplied uniform floor implies `(A3)` with `3*c0/64`;
- `normalized_strict_increase`: the exact real algebra behind `(A4)`;
- `all_odd_units_of_floor`: a finite-superlevel maximum argument for any
  predicate inherited backwards along actual odd edges;
- `finite_absorbing_floor`: positivity, sublinearity and additive transfer
  imply an actual hit below one finite floor for every positive source;
- `universal_of_inverse_envelope_and_base`: an explicit certified base below
  the selected floor supplies the final convergence theorem.

These are implications with displayed hypotheses. They do not establish
`(UE)`, do not instantiate an analytic excessive function, and do not assert
Collatz.

### A stronger connection to the new band: only marked upper decay is needed

The full ordinary estimate `(UE)` is stronger than the argument requires.
It suffices to prove

\[
\boxed{\frac{F(n)}n\longrightarrow0
\quad(n\to\infty,\ n\text{ marked},\ 3\nmid n).}
\tag{MUE}
\]

Here marked means exactly the odd section imported from PR173, with
`(floor(log2 n)+1)(n-2^floor(log2 n))<=70*2^floor(log2 n)`.

The key is a threshold barrier already implicit in `(A3)`. If `H(n)>=2c`,
then

\[
F(q)\ge\frac3{2^e}(2cn)+c
 =2cq+c\left(1-\frac2{2^e}\right)\ge2cq.
\]

Thus `H(q)>=2c`. Contrapositively, a final odd endpoint with `H<2c`
forces every earlier odd state on that finite segment to have `H<2c`.
Equation `(A4)` then makes `H` strictly increase across every odd step
of the segment.

Choose `N` so that all marked unit states above `N` satisfy `H<2c`. Suppose
one marked unit never reaches a marked unit below `N`. By `(MUE)`, the set
of such bad marked units with `H` at least its value is finite. Choose a
maximizer. PR173 supplies a **positive odd-index** marked return. Its
endpoint remains bad, hence is at least `N` and has `H<2c`. The threshold
barrier and strict segment increase give a larger value at this next marked
point, contradicting maximality.

Consequently every positive ordinary source hits one finite part of the
actual marked band. A verified base in that finite marked part completes
Collatz. This argument uses no upper estimate at the intermediate unmarked
states.

`lean/MarkedDensityPotential.lean` formalizes the barrier, the segment
increase and the marked-only finite-floor argument. Its positive marked
odd return is proved from the imported public `descent_or_section` theorem
by ordinary strong induction; the proof does not identify different clocks
without a transport theorem. The final declarations are
`finite_marked_absorbing_floor` and
`universal_of_marked_inverse_envelope_and_base`. The proposition
`MarkedSublinear` remains an explicit open input.

## 3. A genuine harmonic envelope, with decay on every fixed ray

The finite excessive function from the companion proof can be improved
without any new upper-envelope assumption. The following is a written
analytic consequence of that construction and the same atom floor; it has
been checked independently in the parallel renewal attack. It is not a
Lean declaration.

Work first on the positive odd integers, as in the companion construction.
Define

\[
G_k=P^kF.
\]

Positivity of `P` and `PF<=F` show that `G_k` decreases pointwise to a finite
nonnegative function `G`. This limit is **uniformly positive** on the units.
Indeed, direct summation of the first-letter law gives

\[
D_1(q)=
\begin{cases}1&q\equiv1\pmod3,\\2&q\equiv2\pmod3,\\0&3\mid q.\end{cases}
\]

Thus `F >= (c0/2)D1`, and

\[
G_k(q)\ge\frac{c_0}{2}D_{k+1}(q)\ge\frac{c_0^2}{2}
\]

for all unit `q` once `k+1` is past the uniform atom-floor depth. For each
fixed `q`, the parent summands of `PG_k(q)` are dominated by those of
`PF(q)`, whose sum is finite. Dominated convergence therefore gives

\[
\boxed{PG=G,\qquad
 \frac{c_0^2}{2}\le G(q)\le F(q)<\infty\quad(3\nmid q).}
\tag{H1}
\]

This proves existence of a finite positive **harmonic**, rather than merely
excessive, ordinary envelope. It does not claim that the original Abel
limit `F` itself was harmonic. The uniform floor ensures that taking the
decreasing harmonic part does not collapse the function to zero.

Extend `G` to positive even arguments by its parent sum `PG(q)`. This is
finite: if `q=2^v a` with `a` odd, a change of exponent gives

\[
G(2^v a)=2^v
 \sum_{\substack{f\ge v+1\\2^f a\equiv1\pmod3}}
 \frac3{2^f}G\!\left(\frac{2^f a-1}{3}\right)
 \le2^vG(a).
\tag{H2}
\]

All parents in these sums are odd, so the extension changes no previously
defined summand and is harmonic on all positive arguments. At multiples of
three it is zero.

For every **fixed** positive unit `q`, the same exponent change gives

\[
\frac{G(2^E q)}{2^E q}=
\frac1q
 \sum_{\substack{f\ge E+1\\2^f q\equiv1\pmod3}}
 \frac3{2^f}G\!\left(\frac{2^f q-1}{3}\right)
 \longrightarrow0.
\tag{H3}
\]

The right side is a tail of the convergent nonnegative series `PG(q)=G(q)`.
This is genuine sublinear decay along **every fixed dyadic ray**. Similarly,
the individual summands tend to zero, giving

\[
\frac{G((2^e q-1)/3)}{(2^e q-1)/3}\longrightarrow0
\tag{H4}
\]

along the legal inverse exponents. The convergence in `(H3)` is uniform
over any fixed finite set of cores `q`, by taking the maximum of their
finitely many cutoffs.

There is an elementary quantitative separation from the marked-band target.
If a marked source `n=2^d+r` satisfies `3n+1=2^e q`, then

\[
\boxed{d+1\le211q.}\tag{H5}
\]

To see this, put `Delta=3r+1=2^e q-3*2^d>0`. It is a positive integer
multiple of `2^min(e,d)`. If `e>=d`, this gives `q*Delta>=2^d` since
`q>=1`. If `e<d`, then `Delta>=2^e` and `2^e q>3*2^d`, giving the same
inequality. The exact band width and `d+1<=2^d` now give

\[
(d+1)2^d\le q(d+1)(3r+1)
 \le q\bigl(210\,2^d+d+1\bigr)\le211q\,2^d.
\]

Thus a fixed ordinary target has only finitely many marked immediate inverse
parents; all of them are below `2^(211q)`. In particular the fixed-target
ray `(H4)` eventually leaves this marked band. This written elementary
bound is not presently a separate Lean declaration.

Neither raywise assertion establishes `(UE)` or the weaker sufficient
`(MUE)`: in an arbitrary large odd marked source the core itself changes.
The exact positive powers of two are even, while the marked sources above
them are odd. Closeness in real relative size supplies no continuity
estimate for this arithmetic function. Proving that missing band estimate
would complete the connection to the marked finite-floor theorem.

## 4. First explicit candidate: a ternary carry singularity

Long inverse exponent-one chains suggest

\[
F_0(q)=\left(\frac32\right)^{v_3(q+1)}.
\]

It has the required sublinear scale:
`F0(q)<=sqrt(q+1)`, because `(3/2)^2<=3`.
On a valuation-one edge, `q+1=3(n+1)/2`, so
`F0(q)=(3/2)F0(n)`. It exactly repays arbitrary runs of such edges.

It fails after a valuation-two handoff. For every integer `k>=1`, put

\[
n_k=2\,3^{2k}-1,\qquad q_k=\frac{3^{2k+1}-1}{2}.
\]

Both are positive odd units, `3*n_k+1=4*q_k`, and

\[
F_0(n_k)=\left(\frac32\right)^{2k},\qquad F_0(q_k)=1.
\]

Already at `k=1`, the required single-parent inequality would read
`1>=27/16`. The explicit ordinary edge is `17 -> 13`.
This is an unbounded failure family, not a numerical truncation artifact.

## 5. A convergent infinite repair, and its exact failure

The first candidate's singularity moves under other inverse exponents.
A natural repair includes every dyadic translate:

\[
F_1(q)=\sum_{j\ge0}2^{-j}
 \left(\frac32\right)^{v_3(2^j q+1)}.
\tag{A5}
\]

The `j=e-1` term pays for the original carry singularity at every inverse
exponent `e`. Unlike a finite residue fit, this candidate retains arbitrarily
deep ternary valuations and infinitely many translated singularities.

The series is genuinely convergent and sublinear. For every `j`,

\[
\left(\frac32\right)^{v_3(2^j q+1)}
 \le\sqrt{2^j q+1}\le2^{j/2}\sqrt{q+1}.
\]

Grouping `j=2k,2k+1` therefore gives

\[
F_1(q)\le4\sqrt{q+1},\qquad
\sum_{j\ge2K}\cdots\le4\,2^{-K}\sqrt{q+1}.
\tag{A6}
\]

Nevertheless, it fails the genuine ordinary valuation-one edge `7 -> 11`.
The first twelve terms give the exact fractions

\[
F_1(7)\ge\frac{154611}{65536},\qquad
F_1(11)\le\frac{2925}{1024}+\frac14.
\]

The latter tail follows from `(A6)` with `K=6` and `sqrt(12)<4`. Hence

\[
\frac32F_1(7)-F_1(11)
\ge\frac{56665}{131072}>0.
\tag{A7}
\]

This rules out `(A5)` as an inverse-transfer potential even before asking
for the additive term. `verify_inverse_density_majorants.py` replays the
finite rational arithmetic and records the analytic tail bound used in the
certificate. It does not approximate the infinite series and call the
result exact.

The failed handoff can be seen directly. A general translated expression
at a parent transforms as

\[
2^j n+1=\frac{2^{e+j}q+3-2^j}{3}.
\]

For `j>=2`, the new numerator constant is negative. The family
`2^j q+1` in `(A5)` is therefore not closed under the full inverse transfer.
The failure is of the entire stated candidate, not just of a missing finite
precision in its implementation.

## 6. Why finite periodic corrections do not repair the candidate

There is also a complete obstruction to a simpler family of supersolutions.
Fix any positive modulus `M`, positive coefficients `a_r`, and `0<=theta<1`.
The function

\[
G(n)=a_{n\bmod M}\,n^\theta
\]

cannot satisfy the single-parent inequality along every positive odd unit
edge. Set `n=12Mt-1`, `q=18Mt-1`, with `t` a positive integer. Both states
are odd units in the same residue class modulo `M`, and `3n+1=2q`.
But

\[
\frac{G(q)}{G(n)}\longrightarrow\left(\frac32\right)^\theta<\frac32.
\]

Thus the transfer inequality fails for all sufficiently large `t`. This
does **not** rule out such a function merely bounding a density from above;
an upper bound need not itself satisfy the transfer equation. It does rule
out using this finite-residue power family directly as the global potential
in Section 2.

## 7. Unconditional contraction of histories ending at one fixed target

There is a useful ordinary-arithmetic fact about the possible upper
envelope. It does not use mixing, a density floor, or Collatz convergence.

For a positive odd source `a`, let

\[
\omega_d(a)=\frac{3^d}{2^{e(a)+e(Ua)+\cdots+e(U^{d-1}a)}}.
\]

For one **fixed** positive odd target `q`, put

\[
\Omega_d(q)=\sup\{\omega_d(a): a>0\text{ odd},\ U^d(a)=q\},
\]

with value zero when the set is empty. Then

\[
\boxed{\Omega_d(q)\longrightarrow0\quad(d\to\infty).}
\tag{UDC}
\]

**Proof.** The exact positive-step product gives

\[
U^d(a)=\omega_d(a)\,a
 \prod_{i<d}\left(1+\frac1{3U^i(a)}\right).
\tag{6.1}
\]

Thus any history ending at `q` has `omega_d(a)<=q/a`. Fix `epsilon>0`.
Only the finitely many sources `a<=q/epsilon` can have multiplier at least
`epsilon`.

If `q` is not periodic, each such fixed source can hit `q` at most once:
two hits would give a positive return of `q` to itself. The finitely many
existing hit depths therefore have a finite maximum. Beyond it, every
history has multiplier smaller than `epsilon`.

If `q` has a positive odd period `p`, put `lambda=omega_p(q)`. Formula
`(6.1)` around that positive cycle shows `0<lambda<1`, including for a
hypothetical nontrivial cycle. For each of the finitely many small sources
that actually hits `q`, choose its first hit depth `h`. Write a later hit
depth as `d=h+kp+r`, with `0<=r<p`. Periodicity and the final equality
imply `U^r(q)=q`; the multiplier of that remaining return is at most one.
The multiplicative cocycle therefore gives

\[
\omega_d(a)
 =\omega_h(a)\lambda^k\omega_r(q)
 \le q\lambda^k.
\]

The chosen first-hit depths have a finite maximum. As `d` tends to infinity,
`k` tends to infinity uniformly over this finite source set. Since
`lambda^k` tends to zero, these histories also eventually have multiplier
smaller than `epsilon`. The sources above `q/epsilon` were already covered
by `(6.1)`. This proves `(UDC)`.

When `q` is a ternary unit, there is a positive ordinary inverse history at
every depth. Consequently `(UDC)` can also be stated as an all-history
clock surplus:

\[
\inf_{U^d(a)=q}\left(
 e(a)+\cdots+e(U^{d-1}a)-d\log_2 3\right)
 \longrightarrow+\infty.
\]

This is a written unconditional theorem, not currently a Lean declaration.
Its quantifiers concern all finite histories ending at the same fixed
target. It is not the open forward coefficient-stopping claim for a fixed
source. No effective rate has been obtained: the proof uses the maximum
of existing first-hit times from a finite set of sources. In particular,
`Omega_d(q)->0` alone does not justify choosing a mixing block whose length
is a prescribed positive power of `d`.

The clock-sensitive operator does have one elementary improvement relevant
to a possible use of `(UDC)`. For a **single output clock**, prefixes with
different totals use different input clocks. Under the same real-offset
and multiplier bounds as the mixed operator in `JOINT_CLOCK_MIXING.md`,
the fixed-total counting argument gives

\[
\sup_{u,r}\left|\sum_w\mathcal T_w H(u,r)\right|
 \le (B+3^k\Omega)\,\|H\|_{1,1}.
\tag{6.2}
\]

The factor counting distinct prefix totals disappears from this weaker
output norm. It does **not** disappear from `sup_r sum_u`, which is the
norm used for total density. Summing `(6.2)` over an unbounded set of clocks
would reintroduce an uncontrolled loss. This is why the qualitative
backwards contraction has not yet supplied `(UE)`.

## 8. Remaining construction

The required new estimate is now the **marked-band** sublinear envelope
`(MUE)`; the stronger all-ordinary `(UE)` would also suffice. A finite
positive harmonic envelope exists, and `(H3)`--`(H4)` prove its decay on
each fixed ray, but no estimate uniform over changing odd marked sources
has been obtained. The atom floor supplies the additive term, and the Lean
argument supplies the complete marked finite-floor mechanism. The two
explicit candidates above fail
because their singularities are not stable under every actual arithmetic
handoff. No universal upper envelope follows from these failures, from
finite numerical density values, or from three-adic `L1` mixing alone.
