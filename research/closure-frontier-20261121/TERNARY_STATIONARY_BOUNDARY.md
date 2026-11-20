# Ternary mixing, weighted coercivity, and the exact square-integrability boundary

**Status: PROPOSED.** TM1--TM5 below are elementary statements about a
specified random affine process and its finite projections. TM6--TM7 are
source-qualified consequences of Tao's published fine-scale mixing theorem.
These statements do not establish an approximation to an ordinary Collatz
component, and do not prove Collatz. The random choices below must not be
substituted for the successive parities of one fixed ordinary integer.

The reason for investigating this process was to extend the
[finite-conductor approach](FINITE_CONDUCTOR_RIGIDITY.md) to conductors
divisible by three. It gives a positive weighted inequality, but also
disproves the uniform square-integrability estimate that would make a
straightforward conversion to unweighted approximation errors possible.
The stationary Syracuse measure itself is established prior literature;
no priority claim is made for it, its finite projections, or the
general principle of contraction of random affine maps.

## 1. The chain and its relation to the Syracuse measure

Put `q=3^s`, `s>=1`. On `Z/qZ`, independently choose each of

\[
 F_0(x)=x/2,\qquad F_1(x)=(3x+1)/2
 \tag{1}
\]

with probability one half. Division by two is inversion modulo `q`.
Call this transition kernel `K_s` and its stationary probability `pi_s`.
The same maps are defined on `Z_3`. They are not a deterministic
Collatz map on the ternary quotient: the parity of an ordinary integer
is additional information. For a uniformly sampled positive integer in
each residue class, the one-step parity average is precisely (1).

Writing `D=F_0`, `B=F_1`, stationarity is
`nu=(D_*nu+B_*nu)/2`. Iteration of the first summand gives

\[
 \nu=\sum_{a\ge1}2^{-a}(D^{a-1}B)_*\nu,
 \qquad D^{a-1}B(x)=\frac{3x+1}{2^a}.
 \tag{2}
\]

The remainder after `j` substitutions has mass `2^{-j}`, so (2) is
justified in total variation. Conversely, (2) implies the original
stationary equation by separating its first term. Thus this is the
stationary Syracuse measure discussed by Tao after his equation (1.25).

## 2. TM1: explicit finite mixing and support

**Theorem TM1.** There is a unique stationary probability `pi_s`. It is
positive at every ternary unit and zero at every multiple of three. At
`N=4s` steps,

\[
 \sup_x\|K_s^N(x,\cdot)-\pi_s\|_{\rm TV}
 \le \theta_s:=\frac13\left(\frac{16}{27}\right)^s
 \le\frac{16}{81}.
 \tag{TM1}
\]

Here total variation is `sup_A |mu(A)-nu(A)|`.

**Proof.** Drive two initial states with the same coin sequence. A word
of length `N` containing `j` copies of `F_1` has affine slope
`3^j/2^N`. Thus the endpoints agree modulo `3^s` whenever `j>=s`.
This is simultaneous agreement for all initial states, not merely
agreement in distribution. A stationary law exists for a finite chain;
coupling any two laws proves uniqueness, and coupling an arbitrary
initial state to a stationary one bounds total variation by
`Pr(Bin(N,1/2)<s)`. For `N=4s`,

\[
 \Pr(J<s)\le 3^{s-1}{\mathbb E}3^{-J}
 =3^{s-1}(2/3)^{4s}=\theta_s.
\]

The units form a closed class. Each use of `F_1` sends every state to
`2 mod3`; a chain started in the multiples of three stays there for
`N` steps only if all `N` coins are zero. Its stationary mass is
therefore zero. Finally multiplication by two is a single cycle on the
units modulo `3^s`: its order is `2*3^(s-1)`, by induction using
`v_3(4^(3^j)-1)=j+1`. The edges of `F_0` alone make the closed unit
class irreducible, proving positivity there.

Projection of `pi_s` modulo `3^(s-1)` is stationary for `K_(s-1)`.
Uniqueness therefore makes the probabilities consistent. They define
one probability measure `nu` on `Z_3`.

## 3. TM2: a weighted finite-conductor inequality

For a real label `p` on `Z/3^sZ`, define

\[
 \varepsilon_s(p)=\frac12\sum_a\pi_s(a)
 \left(|p(a)-p(F_0a)|+|p(a)-p(F_1a)|\right),
\]
\[
 \mathcal O_s(p)=\sum_{a,b}\pi_s(a)\pi_s(b)|p(a)-p(b)|.
\]

**Theorem TM2.** For every such real label,

\[
 \boxed{\mathcal O_s(p)\le\frac{648s}{49}\varepsilon_s(p).}
 \tag{TM2}
\]

The measure is `pi_s`, not uniform counting measure. Values on multiples
of three have zero weight. No claim for arbitrary metric-valued labels
is inferred from the real-valued coarea proof.

**Proof.** For a set `A` with `pi_s(A)<=1/2`, let
`Q_t(A,A^c)=sum_(a in A) pi_s(a) K_s^t(a,A^c)`. TM1 gives

\[
 Q_N(A,A^c)\ge(1/2-16/81)\pi_s(A)=\frac{49}{162}\pi_s(A).
\]

A stationary path from `A` to `A^c` in `N` steps crosses that cut at
least once. Summing the expected number of outward crossings yields
`Q_N(A,A^c)<=N Q_1(A,A^c)`. Hence

\[
 Q_1(A,A^c)\ge\frac{49}{648s}\pi_s(A).
 \tag{3}
\]

Stationarity implies equality of inward and outward flows. Taking the
smaller of a set and its complement in (3) consequently gives
`pi_s(A)pi_s(A^c) <= (648s/49) Q_1(A,A^c)` for every `A`.
For `A_t={a:p(a)>t}`, integrate this inequality over `t`. The left
side, doubled, is `O_s(p)`; the outward-flow integral, doubled, is
`epsilon_s(p)`. This proves TM2, including constant labels.

## 4. TM3: exact conversion from a supplied ordinary approximation

Let `f` be any real-valued label on positive integers with `f(Tn)=f(n)`
for the actual shortcut map. Extend `p` periodically and put

\[
 \delta_s(f,p)=\limsup_{X\to\infty}\frac{3^s}{X}
       \sum_{n\le X}\pi_s(n\bmod3^s)|f(n)-p(n)|.
 \tag{4}
\]

**Theorem TM3.** Whenever the right side is finite,

\[
 \varepsilon_s(p)\le5\delta_s(f,p),\qquad
 \mathcal O_s(p)\le\frac{3240s}{49}\delta_s(f,p).
 \tag{TM3}
\]

**Proof.** Set `e(n)=|f(n)-p(n)|`. Invariance gives
`|p(Tn)-p(n)|<=e(n)+e(Tn)`. Weighted averaging of the left side over
ordinary integers gives exactly `epsilon_s(p)`, since `q` is odd and
both parities occur equally in each residue. For even sources `n=2m`,
stationarity gives `pi_s(2m)<=2pi_s(m)`. Thus their contribution to
the upper mean of `e(Tn)` is at most `delta_s`.

For odd sources, `m=Tn=(3n+1)/2` determines `n` injectively and
`m<=3X/2+O(1)`. The summand `pi_s(n)` is one of the incoming
`F_1` weights in the stationary identity, so it is at most
`2pi_s(m)`. Positivity, without replacing a subsequence by an average,
bounds this contribution by `3delta_s`. The ordinary source-error
contribution is at most `delta_s`, proving the first inequality.
TM2 proves the second. For a positive fixed finite conductor, the
harmless `O(1)` cutoff change is absorbed by using `floor(3X/2)+1`
in the upper-limit definition.

There is an anchor value `c=p(a)` whose `pi_s`-average distance from
`p` is at most `O_s(p)`, by averaging over `a`. Thus the upper
weighted mean of `|f-c|` is at most
`(1+3240s/49)delta_s(f,p)`. No estimate for the actual
`delta_s(f,p)` is supplied by TM1. In particular mixing a random
quotient chain does not bound the error for a fixed ordinary component.

## 5. TM4: exact stationary recursion and finite energy identities

Set `pi_0(0)=1`. Stationarity and consistency give, for `x mod3^s`,

\[
 \pi_s(x)=\frac12\pi_s(2x)+
 \frac12 1_{x\equiv2\ (3)}\pi_{s-1}((2x-1)/3).
 \tag{5}
\]

The argument in the last term is modulo `3^(s-1)`. Iterating the
doubling permutation on the unit cycle gives an exact rational
algorithm. With `h=2*3^(s-1)` and
`mu_s(x)=1_(x=2 mod3)pi_(s-1)((2x-1)/3)`,

\[
 \pi_s(x)=\frac{\sum_{j=0}^{h-1}2^{h-j-1}\mu_s(2^jx)}{2^h-1}
 \quad(3\nmid x).
 \tag{6}
\]

Computing (6) at `x=1` and using
`pi_s(2x)=2pi_s(x)-mu_s(x)` traverses the whole unit cycle.
All operations use rational integers. They do not approximate an
infinite geometric tail numerically.

Let `m` be normalized Haar measure on `Z_3` and define the step density
`g_s(x)=3^s pi_s(x mod3^s)`, including `g_0=1`. Then

\[
 g_s(x)=\tfrac12g_s(2x)+
 \tfrac32 1_{x\equiv2\ (3)}g_{s-1}((2x-1)/3).
 \tag{7}
\]

Write `R_s=integral g_s^2 dm`. Squaring (7), using Haar preservation
of multiplication by two and the factor `1/3` for the indicated
ternary coset, gives the exact identity

\[
 \boxed{R_s-R_{s-1}=2I_s,\quad
 I_s=\int_{x\equiv2\ (3)}g_s(2x)g_{s-1}((2x-1)/3)\,dm(x)>0.}
 \tag{TM4}
\]

Strict positivity follows from TM1; for `s>=2`, the classes `2,8 mod9`
already have both factors positive. For `s=1`, `g_0=1`.
This identity supplies an independent check of the stationary algorithm.

Two useful elementary atom bounds are

\[
 \pi_s(-1)\ge2^{-s},\qquad \max_x\pi_s(x)\le(2/3)^s.
 \tag{8}
\]

For the first, `s` successive `F_1` maps send every input to `-1 mod3^s`.
For the second, expand (5) along the unit doubling cycle as an infinite
geometric sum: the nonzero `mu_s(2^jx)` occur in only one parity of
`j`, whose total weights are either `1/3` or `2/3`. Induct from
`pi_0(0)=1`. In particular the density at `-1` grows at least as
`(3/2)^s`. It is already impossible to use a conductor-independent
pointwise density bound.

## 6. TM5: no square-integrable stationary density

**Theorem TM5.** The stationary probability `nu` has no density in
`L^2(Z_3,m)`. Consequently

\[
 \boxed{R_s=3^s\sum_x\pi_s(x)^2\longrightarrow\infty.}
 \tag{TM5}
\]

This does not assert that `nu` is singular. Indeed TM6 below gives an
`L^1` density from a published theorem. Nor does TM5 rule out `L^p`
densities for `1<p<2` or estimates in weak `L^2`.

**Proof.** Suppose `g>=0` is an `L^2` stationary density. The density
version of (1) is

\[
 g(x)=\tfrac12g(2x)+\tfrac32 1_{x\equiv2\ (3)}g((2x-1)/3).
 \tag{9}
\]

All stationary mass is on the units. Let `S={x:g(x)>0}` there. The
inequality `g(x)>=g(2x)/2` shows `2^{-1}S` is contained in `S`
modulo null sets. Haar preservation makes this an equality modulo
null sets. Multiplication by two is ergodic on the units: its action
on every finite unit quotient is one cycle; conditional expectations
of any invariant indicator on those quotients are constant, and
convergence of these conditional expectations proves the assertion.
Since `g` has positive integral, `S` therefore contains almost every
unit.

Now square (9) and integrate. The two diagonal terms are respectively
`||g||_2^2/4` and `3||g||_2^2/4`. Thus the remaining cross term must
vanish:

\[
 \frac32\int_{x\equiv2\ (3)}g(2x)g((2x-1)/3)\,dm(x)=0.
 \tag{10}
\]

The integral is finite by Cauchy--Schwarz. It is strictly positive:
on `x=2 or8 mod9`, both arguments are units, and both factors are
positive almost everywhere. This contradicts (10).

For the last assertion, consistency makes `g_s` a nonnegative density
martingale. In elementary Hilbert-space terms, for `t>=s`,
`integral(g_t-g_s)^2 dm=R_t-R_s`. If the increasing sequence `R_s`
were bounded, the `g_s` would converge in `L^2` to a nonnegative
density `g` of integral one. Its integrals on every ternary cylinder
would equal those of `nu`; hence it would be the forbidden `L^2`
density. This proves divergence, without using TM6.

## 7. TM6: what the published fine-scale theorem does supply

Tao's Proposition 1.14, together with his consistency identity (1.23),
states for the same stationary projections that

\[
 \|g_n-g_m\|_1\ll_A m^{-A}\qquad(1\le m\le n)
 \tag{11}
\]

for every fixed `A>0`. Taking the `L^1` limit proves that `nu` has a
density `g` and `||g-g_m||_1 <<_A m^-A`. Combined with TM5,

\[
 \boxed{g\in L^1(Z_3,m)\setminus L^2(Z_3,m).}
 \tag{TM6}
\]

Equation (11) is imported from the published result, not established
by the elementary coupling in TM1. Its global arithmetic Fourier
argument is not replayed by this packet. The passage from (11) to
an `L^1` density is the Cauchy criterion in `L^1`; the conditional
densities identify the limiting measure on every cylinder. Rapid
`L^1` approximation and divergent `L^2` norm are compatible because
small sets can carry increasingly high densities.

Primary source: Terence Tao, *Almost all orbits of the Collatz map attain
almost bounded values*, Forum of Mathematics, Pi **10** (2022), e12,
[DOI 10.1017/fmp.2022.8](https://doi.org/10.1017/fmp.2022.8),
equations (1.23), (1.25), and Proposition 1.14. The published
article was inspected directly for these normalization and scope facts.

## 8. TM7: uniform conversion of bounded ordinary errors

The failure of a uniform `L^2` bound does not prevent every conversion
from ordinary counting weights. The published `L^1` estimate supplies
the following positive comparison for bounded errors.

Let `e: N_(>0) -> [0,1]` be any function, and define

\[
 \delta_H(e)=\limsup_{X\to\infty}\frac1X\sum_{n\le X}e(n),
 \qquad
 \delta_s(e)=\limsup_{X\to\infty}\frac1X
                 \sum_{n\le X}g_s(n)e(n).
 \tag{12}
\]

The same supplied ordinary error `e` appears on both sides; no orbit
resampling, change of source, or error equidistribution is assumed.

**Theorem TM7.** For every `A>0` there is a constant `C_A`, independent
of `e`, `s`, and `m`, such that for all `s,m>=1`,

\[
 \boxed{\delta_s(e)\le2^m\delta_H(e)+C_A m^{-A}.}
 \tag{TM7a}
\]

For sufficiently small `0<delta_H(e)<1`, this implies the uniform bound

\[
 \boxed{\sup_{s\ge1}\delta_s(e)
       \ll_A\bigl(\log(1/\delta_H(e))\bigr)^{-A}.}
 \tag{TM7b}
\]

If `delta_H(e)=0`, then `delta_s(e)=0` for every fixed `s`, directly
from the finite bound `g_s<=2^s`; hence the supremum is zero as well.

**Proof.** If `s>=m`, view `g_m` as a periodic function modulo `3^s`
by lifting its residue classes. Positivity and `0<=e<=1` give

\[
 \frac1X\sum_{n\le X}g_s(n)e(n)
 \le \|g_m\|_\infty\frac1X\sum_{n\le X}e(n)
       +\frac1X\sum_{n\le X}|g_s(n)-g_m(n)|.
 \tag{13}
\]

The last summand is periodic. Its limiting ordinary average equals
`||g_s-g_m||_(L^1(m))`, because each ternary residue occurs with the
same ordinary counting frequency. The error `e` itself need not have
any residue-frequency property. By (8), `||g_m||_infinity<=2^m`.
The imported estimate (11) now proves TM7a. If `s<m`, use
`g_s<=2^s<=2^m` and no fine-scale remainder. To obtain TM7b, choose
`m=floor(log_2(1/delta_H(e))/2)` once this is positive. The first
term is at most `sqrt(delta_H(e))`; the second gives the claimed
inverse-logarithmic bound. This completes the proof.

There is also an exact finite-scale comparison. If `s>=m` and `X` is
a positive integer multiple of `3^s`, the last average in (13) already
equals its Haar integral, so

\[
 \frac1X\sum_{n\le X}g_s(n)e(n)
 \le2^m\frac1X\sum_{n\le X}e(n)+\|g_s-g_m\|_1.
 \tag{14}
\]

For `s<m`, the inequality without the last term holds at every cutoff.
These statements retain the same actual finite source set and error.

### Consequence for approximations with growing conductor

Suppose `f` is an actual invariant Boolean label and `p_s` a Boolean
periodic approximation modulo `3^s`. Set `e_s(n)=|f(n)-p_s(n)|`.
If there are fixed `c,beta>0` such that

\[
 \delta_H(e_s)\le\exp(-c s^\beta)
 \quad\hbox{for all sufficiently large }s,
 \tag{15}
\]

then TM7b with any fixed `A>1/beta` gives
`s*delta_s(e_s)->0`. TM3 consequently yields

\[
 \mathcal O_s(p_s)\longrightarrow0,
 \qquad
 \inf_{c_s\in\{0,1\}}
   \limsup_{X\to\infty}\frac1X
       \sum_{n\le X}g_s(n)|f(n)-c_s|\longrightarrow0.
 \tag{16}
\]

Each use of TM7 is for the same error on its two sides; the sequence
`e_s` in this consequence is allowed to change with the stated
approximating conductor. The constants remain uniform in that choice.

This supplies a positive alternative to the rejected uniform-`L^2`
shortcut. It does **not** construct approximations satisfying (15),
and it does not supply positive weighted ordinary mass in both label
classes. Those missing ordinary statements remain necessary for a
pointwise convergence conclusion. Uniform integrability of the
stationary densities alone is not a proof about a fixed integer.

## 9. Exact remaining ordinary obligation and controls

TM2--TM3 would become useful for the full problem if one constructed
periodic approximations to an actual separating ordinary label with
the required small weighted error, and retained enough ordinary mass
in both label classes for a pointwise contradiction. Neither property
is an output of the random quotient process.

A tempting shortcut was to bound this weighted error from an
unweighted error using a uniform `L^2` density and Cauchy--Schwarz.
TM5 disproves that particular uniform bound. It does not disprove
source-specific estimates, a weaker integrability exponent, weak
`L^2` control, or the dyadic route in the companion note.

The maps with `3x-1` in place of `3x+1` are conjugate on `Z_3` by
`x -> -x`. They have the same mixing and norm conclusions, whereas
their positive ordinary dynamics include the distinct cycles `1`
and `5,7,10`. This is a direct check that the modular statements alone
do not decide ordinary convergence.

The exact checker verifies stationarity, projective consistency, the
square-norm identity, support, atom bounds, and bounded instances of
the coupling and cut inequalities. It cannot establish TM5 by finite
sampling; that conclusion rests on the proof above. The observed
near-linear growth of `R_s` over the checked levels is diagnostic
only; no universal rate for its divergence is asserted.
