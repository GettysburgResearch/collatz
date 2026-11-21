# A harmonic threshold for atomic transport

**Status:** proved elementary operator/finite-path statements; proposed Collatz
application. No universal Collatz weight is constructed. This note was developed
on 21 November 2026 while pursuing the forced dyadic section, and is inspired by
the full-support finite-measure approach of Assani. The proofs below are
self-contained and do not import that paper's counting-measure assertions.

## 1. Exact finite-horizon statement

Let `X` be a set, `F : X -> X`, and write `x_k=F^k(x_0)`. Let
`w : X -> R_{≥0}` have finite total mass at most `W`: equivalently, for every
finite subset `E` of `X`, `sum_(x in E) w(x) <= W`. Assume `w(x_0)>0`.
For positive real numbers `M_0,...,M_(N-1)`, suppose

\[
 w(x_0)\le M_k w(x_k)\qquad(0\le k<N).                 \tag{1}
\]

If the first `N` points are pairwise distinct, then

\[
 w(x_0)\sum_{k=0}^{N-1}\frac1{M_k}\le W.              \tag{2}
\]

**Proof.** Divide (1) by `M_k>0`, sum, and use injectivity to identify the
sum of endpoint weights with the mass of the finite orbit set. There is no
distributional, almost-everywhere, independence, or limiting assumption.

### Integer/rational encoding

If all masses and `M_k` are rational, (2) is an exact rational inequality.
For natural-number multipliers `M_k>=1`, put `D=product_(k<N) M_k`. Clearing
denominators gives

\[
 w(x_0)\sum_{k<N}(D/M_k)\le D W.                      \tag{3}
\]

Here every `D/M_k` is an exact natural quotient; the masses may also be
scaled by a common denominator. This version has no analytic dependencies.

An especially simple consequence avoids a product denominator. If
`M_k <= C(k+1)` for `k<2^J-1` and those points are distinct, split the
indices into `2^j <= k+1 < 2^(j+1)`, `0<=j<J`. Each complete block has
`2^j` terms, each endpoint weight is at least
`w(x_0)/(C*2^(j+1))`, and hence

\[
                    J w(x_0)\le 2CW.                \tag{4}
\]

This is a quantitative finite repetition certificate whenever a concrete
weight and a verified linear transport bound are supplied.

## 2. Operator orientation and the global consequence

Now let `X` be countable and let `w(x)>0` for every `x`. The pushforward on
nonnegative atomic masses and the composition operator are respectively

\[
 (P\eta)(y)=\sum_{F(x)=y}\eta(x),\qquad Uf(x)=f(F(x)).
\]

All sums below contain nonnegative terms. Reordering gives

\[
 \|U^k f\|_{L^1(w)}
   =\sum_y |f(y)|(P^k w)(y),\qquad
 \|U^k\|=\sup_y\frac{(P^k w)(y)}{w(y)}.              \tag{5}
\]

Thus `||U^k|| <= M_k` implies (1), because the preimage fiber over `x_k`
contains the original atom `x_0`. If

\[
                 \sum_{k\ge0}\frac1{M_k}=\infty,      \tag{6}
\]

every orbit repeats and is eventually periodic. Otherwise all its points
would be distinct, contradicting (2) for sufficiently large `N`.

Uniform power boundedness is therefore stronger than necessary. The bounds
`M_k=C(k+1)`, and even
`M_k=C(k+1)(1+log(k+1))`, suffice. The latter reciprocal series diverges by
the integral test. For a fixed source only the atom inequalities (1) are
needed; a global operator-norm bound is a convenient sufficient condition.

This conclusion is eventual periodicity. On the ordinary Collatz map, it
does not by itself distinguish the known cycle from another possible cycle.

## 3. A constructive universal bound just above the threshold

The following construction works for **every** map of a countable set, even
one with all orbits wandering. It is useful for locating exactly the extra
estimate that would be needed, rather than accidentally calling a generic
resolvent a recurrence proof.

Choose any probability mass `mu` with `mu(x)>0` everywhere, and positive
summable coefficients `c_j` with `sum c_j=1`. Define

\[
                   w=\sum_{j\ge0}c_j P^j\mu.          \tag{7}
\]

Then `w` has total mass one and `w(x)>=c_0 mu(x)>0`. Moreover

\[
 P^k w=\sum_{j\ge k}c_{j-k}P^j\mu
 \le\left(\sup_{i\ge0}\frac{c_i}{c_{i+k}}\right)w.    \tag{8}
\]

For `c_j=1/((j+1)(j+2))`, the coefficients telescope to one and

\[
             \|U^k\|\le\frac{(k+1)(k+2)}2.          \tag{9}
\]

For an arbitrarily chosen `p>1`, take the normalized coefficients

\[
 c_j=\frac{Z_p^{-1}}{(j+1)(1+\log(j+1))^p},\qquad
 Z_p=\sum_{j\ge0}\frac1{(j+1)(1+\log(j+1))^p}<\infty.
\]

Set `g(x)=x(1+log x)^p` for `x>=1`. Since

\[
 (\log g)''(x)
 =-\frac{1+p/(1+\log x)+p/(1+\log x)^2}{x^2}<0,
\]

the function `g(x+k)/g(x)` decreases in `x`. Consequently

\[
 \frac{c_i}{c_{i+k}}
 \le (k+1)(1+\log(k+1))^p,
 \qquad
 \|U^k\|\le(k+1)(1+\log(k+1))^p.                   \tag{10}
\]

This is an explicit full-support finite weight with transport growth
arbitrarily close to the divergent-reciprocal threshold. It proves no
recurrence because the reciprocal series in (10) converges.

### Sharpness on a countable shift

For `F(n)=n+1` on the nonnegative integers and `w(n)=c_n` above,

\[
 (P^k w)(n)=\begin{cases}c_{n-k}&n\ge k,\\0&n<k.\end{cases}
\]

The supremum in (5) is attained at `n=k`, so equality holds in (10).
All orbits are nonperiodic. Thus the generic construction cannot be improved
to exponent `p=1` without information that genuinely excludes a wandering
orbit. This is an exact example, not evidence for a divergent Collatz orbit.

## 4. Applying the framework to the unavoidable dyadic section

For the shortcut Collatz map
`T(n)=n/2` if even and `(3n+1)/2` if odd, use PR173 at
`fa0c9e2a2851e6324391e39c17afcb5913185aec` and its positive marked set

\[
 S=\{n\text{ odd}>0:(d+1)(n-2^d)\le70\,2^d,
                       \ d=\lfloor\log_2 n\rfloor\}.
\]

Its first strictly positive return map `R:S->S` is total. The forward-visit
theorem ensures that every positive ordinary orbit enters this section.
The finite-path theorem applies directly to `R`, with original source atoms
preserved. It never replaces a transported distribution by a fresh shell.

The section's elementary octave count is `O(2^d/(d+1))`. Consequently

\[
 \mu(n)\ \propto\ \frac1{n(1+\log_2 n)^\varepsilon},
 \quad n\in S,\quad\varepsilon>0,                    \tag{11}
\]

is a finite full-support seed: octave `d` contributes
`O((d+1)^(-1-epsilon))`. With this concrete seed, (7) is an unconditional
finite full-support weight for the **actual** marked return map, and (10)
holds. This is a constructive positive statement, including all merger
fibers, but remains above the critical time-growth threshold.

### First unsupported step in the closing attempt

To rule out a nonperiodic marked orbit by this route, one must prove an
additional return-specific estimate, for example

\[
        P_R^k w\le C(k+1)(1+\log(k+1))w.             \tag{12}
\]

The coefficient comparison in (8) supplies an exponent `p>1`, not `p=1`.
An improvement would have to exploit genuine overlap among transported
histories or other arithmetic structure. Section sparsity only makes the
seed in (11) summable; it does not remove a logarithm from the time
coefficients. The current forward-band population theorem gives lower
mass on target-dependent high source octaves, with no uniform onset in the
target. It does not establish (12).

The cofinal expanding return families in PR175 also prevent a direct
pointwise comparison of regular size weights at successive returns. The
resolvent (7) handles those returns without a false one-step contraction,
but a harmonic-threshold estimate for it is still open.

The adjacent source pins used for these comparisons are PR175 at
`06215e69346c4d32bf970af9c846a6894586c1e7` and PR180 at
`9010a8790535002b6d9ff92304f0ba289e2e98fe`, specifically the latter's
`research/lean-forward-band-20261121/MARKED_PREDECESSOR_POPULATIONS.md`.

## 5. Incorporating cycle exclusion, if needed

There is a precise way to use the same finite theorem for full absorption,
rather than merely eventual periodicity. On `S x N`, define

\[
 \widehat R(n,h)=
 \begin{cases}(1,0)&n=1,\\(R(n),h+1)&n\ne1.\end{cases}
\]

Every orbit avoiding `1` is injective, including a possible nontrivial
Collatz cycle, because its second coordinate strictly increases. A finite
full-support weight for this **clock-lifted** map satisfying (6) would prove
that every marked source reaches one, and hence full Collatz via PR173.
The universal construction (7) applies to this lift too, but still only
gives the summable-reciprocal rate (10). No critical weight for this lift is
claimed.

## 6. Literature and a narrowly scoped correction

Assani's main full-support finite-measure perspective motivates (5).
Relevant primary sources are:

- I. Assani, *Collatz map as a non-singular transformation*, Studia Math.
  275 (2024), 249--261, DOI 10.4064/sm230913-14-12;
  [arXiv:2208.11675v3](https://arxiv.org/html/2208.11675v3).
- I. Assani, E. Ebbighausen, A. Hande, *Syracuse Maps as Non-singular
  Power-Bounded Transformations and Their Inverse Maps*,
  [arXiv:2208.11801v2](https://arxiv.org/pdf/2208.11801).

The elementary implication from finite full-support power boundedness to
eventual periodicity follows from (2), independently of their other claims.
No novelty priority is asserted for that elementary implication or the
standard resolvent construction.

**Specific correction to the text of arXiv:2208.11675v3, Theorems 3.2 and
3.3:** with counting measure, take `A={1}` and
`Y={2,4,...,2^m}`. Every point in `Y` has limiting visit frequency `1/2`
to `A`, so the integrated Cesaro limit is `m/2`, whereas `mu(A)=1`.
There is no bound by one fixed `M mu(A)` for all such finite `Y`.
Likewise `f=1_A` is in `ell^1`, but its limit is `1/2` on all powers of
two and is not in `ell^1`. The singleton-to-finite-set step in that text
loses the cardinality factor. This correction concerns those displayed
counting-measure claims; it does not invalidate the elementary
full-support power-bounded criterion used here.

## 7. Exact clock-lift fibers and a quantitative survivor extraction

This gives a concrete finite-horizon test of the proposed logarithmic gain.
It does not resample at a return. All endpoint masses retain their original
source weights and all incoming fibers are counted.

Let `A=S\{1}`. On nonnegative atomic masses on `A`, define the killed
pushforward

\[
 (K\eta)(y)=\sum_{\substack{x\in A\\R(x)=y}}\eta(x),
 \qquad y\in A.
\]

A source is killed on its first arrival at one. Choose `a(x)>0` on `A`
with total `S_0<infinity`, and put

\[
 b_j=K^j a,\qquad S_j=\sum_{x\in A}b_j(x).
\]

Thus `S_j` is the mass of actual original sources that survive `j` complete
marked returns. It decreases in `j`. In the clock lift, seed the nonterminal
states by `mu(n,h)=a(n)2^(-h-1)`. Positive summable seed masses may be added
at `(1,h)` to make the entire lift full support; these never return to `A`
and do not affect any formula below.

For the resolvent `w=sum_(j>=0)c_j P_hat^j mu`, the exact formula at a
nonterminal endpoint is

\[
 w(n,h)=\sum_{j=0}^{h}c_j2^{-(h-j+1)}b_j(n).          \tag{13}
\]

Indeed a history ending at clock `h` after `j` steps must have started at
clock `h-j`; it cannot have visited one. In particular

\[
 (\widehat P^k w)(n,k)=\frac{c_0}2 b_k(n).            \tag{14}
\]

For `b_k(n)>0`, a bound `||U_hat^k||<=L_k` therefore requires exactly the
following pointwise inequality on this clock slice:

\[
 \sum_{j=0}^{k}c_j2^{j-k}b_j(n)
       \ \ge\ \frac{c_0}{L_k}b_k(n).                \tag{15}
\]

The last summand alone supplies `c_k b_k(n)`. Thus saving a logarithm over
the generic rate `c_0/c_k` requires additional **actual incoming mass at
earlier killed depths**, with its geometric clock cost included.

### A finite quantitative lower bound

Suppose the coefficients have a ratio majorant `G_r`:

\[
 c_i/c_{i+r}\le G_r\quad(i,r\ge0),\qquad
 A_G:=\sum_{r\ge0}2^{-r}G_r<\infty.
\]

Both coefficient choices above satisfy this. For the quadratic coefficients,
`G_r=(r+1)(r+2)/2` and `A_G=8`, by
`sum_(r>=0) binom(r+2,2) z^r=(1-z)^(-3)` at `z=1/2`.
For the logarithmic coefficients, take
`G_r=(r+1)(1+log(r+1))^p`, whose geometric weighted sum is finite.

Writing `j=k-r` and using `S_j<=S_0` gives

\[
 \sum_{j=0}^{k}c_j2^{j-k}S_j
 \le c_k S_0\sum_{r=0}^{k}2^{-r}G_r
 \le A_G c_k S_0.                                   \tag{16}
\]

Summing (13)--(14) over the nonterminal clock slice and using the defining
operator bound yields the exact finite consequence

\[
 \boxed{\quad
 \|\widehat U^k\|\ \ge\
       \frac{c_0}{c_k}\frac{S_k}{A_G S_0}.
 \quad}                                             \tag{17}
\]

The same argument works pointwise for a specified original source `x` that
survives `k` returns. At `n=R^k(x)`, `b_k(n)>=a(x)`, while each incoming
mass is at most `S_0`. Thus

\[
 \|\widehat U^k\|\ge
       \frac{c_0}{c_k}\frac{a(x)}{A_G S_0}.           \tag{18}
\]

These inequalities remain true at finite horizons without assuming that
any source survives forever.

There is a useful distinction from the generic theorem in Section 2.
For this **specific clock-lift resolvent**, any bound

\[
                    \|\widehat U^k\|=o(c_0/c_k)       \tag{18a}
\]

already forces every source to reach one, by (18). For the entirely rational
quadratic coefficients this only asks for `o(k^2)` growth: even a bound
`O(k^2/log log(k+3))` would suffice. It does not need the reciprocal of
the proposed norm bound to have a divergent sum. The reason is the extra
clock-fiber formula (13), not a strengthening of the general arbitrary-weight
recurrence theorem. This is a sufficient criterion; unbounded norms caused
by changing finite surviving sources need not imply a fixed counterexample.

The weight in (18a) must remain the same quadratic resolvent of the product
seed `a(n)2^(-h-1)`. The universal logarithmic construction in Section 3 uses
a different weight. Its smaller operator bound cannot be substituted into
(18) for the quadratic weight. Taking a second resolvent also changes the
clock-seed fibers and requires a new calculation; no uniform comparison
between these weights has been proved.

### A terminating countermodel to necessity of the proposed norm gain

The subquadratic bound is not automatically available even when every orbit
terminates. Consider `F(n)=max(n-1,0)` on the nonnegative integers, absorbing
at zero, with spatial seed `a(n)=1/((n+1)(n+2))` and the same geometric clock
seed. Every source reaches zero. At a nonterminal endpoint `y`, however,
the unique depth-`j` ancestor is `y+j`, so

\[
                 b_j(y)=\frac1{(y+j+1)(y+j+2)}.
\]

For `y>=max(k,1)` and `0<=j<=k`,

\[
              0<b_j(y)\le4b_k(y).
\]

Using the same finite convolution calculation with `S=4b_k(y)` gives

\[
 \frac{(\widehat P^k w)(y,k)}{w(y,k)}
 \ge\frac{G_k}{32},\qquad G_k=(k+1)(k+2)/2.
\]

Together with the universal upper bound this proves quadratic norm growth
for this fully terminating map. The witnesses move to higher endpoints as
`k` increases; no fixed source survives forever. Thus the proposed fixed
weight estimate is a genuinely additional structural demand, not a
rephrasing of termination or something that follows from it. This
countermodel does not refute the estimate for the actual Collatz section.
The latter lacks the simple uniformly small marked inverse branch used by
the shift example, and its norm growth is unresolved here.

### What the proposed improvement would buy

For `p>1`, `c_0/c_k=G_k`. If the arithmetic of marked returns established

\[
 \|\widehat U^k\|\le C(k+1)(1+\log(k+1)),
\]

then (17) would give the explicit original-source tail bound

\[
 S_k\le \frac{C A_G S_0}{(1+\log(k+1))^{p-1}}.       \tag{19}
\]

Since every source has positive initial mass, (19) would force every
ordinary marked source to reach one. Formula (18) gives the corresponding
finite bound: a source `x` cannot survive any `k` for which

\[
 (1+\log(k+1))^{p-1}>C A_G S_0/a(x).                 \tag{20}
\]

Conversely, any hypothetical nonconverging ordinary source has positive
mass `a(x)` and would force the norm of this particular resolvent to stay
at least a fixed positive multiple of its generic `k log^p k` upper rate,
by (18), for **every** `k`. The obstruction includes nontrivial cycles,
because the clock lift makes their paths injective.

### Two focused closing attempts and their present boundary

1. **Use section sparsity as a time-weight improvement.** It rigorously
   supplies the summable seed (11). Formula (15), however, shows that its
   static octave saving does not appear in the comparison of the depth
   coefficients. A proof needs extra incoming mass relative to `b_k(n)`,
   not a second count of available marked states. No such estimate follows
   from the currently proved section count.
2. **Use the large equal-clock predecessor fans as that extra mass.** The
   current fan theorem provides high-height ordinary predecessors with a
   common ordinary clock, at target-dependent witness octaves. It supplies
   neither a uniform return-count depth nor a bound relating their
   original `a`-mass to an arbitrary transported `b_k(n)`. In (15), earlier
   depths also incur `2^{j-k}`. Dropping that factor, or replacing the
   fan's ordinary clock by a marked-return count, would be invalid.
   Consequently the needed pointwise gain in (15) remains unproved.

The exact route is now constructive up to one explicitly displayed
transport estimate. The general finite theorem, resolvent, section seed,
fiber formulas, and survivor extraction are proved. The critical
return-specific estimate and therefore full Collatz remain open.

## 8. Formalization boundary

`FiniteResolvent.lean` kernel-checks the quadratic coefficient ratio, the
exact finite geometric sum and its constant-eight bound, the finite
convolution bound, the source-atom extraction and its denominator-cleared
form, and the finite terminating-shift fiber obstruction. It compiled with
Lean 4.34.1 and pinned Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`,
with warnings treated as errors.

`ExplicitSeed.lean` additionally supplies a fully explicit alternative
spatial seed, `a(n)=1/((n+1)(n+2))`, with every atom positive and every
finite source sum at most one. Its exact identity is

\[
               \sum_{n<N}a(n)=1-\frac1{N+1}.
\]

It also kernel-checks the unconditional finite transport baseline
`c_0 b_k <= G_k D_k(b)` for every nonnegative incoming history. Thus the
remaining target need not contain an unconstructed seed: this explicit
one can be used, with `S=1`. Whether its actual Collatz fibers admit the
required arbitrarily small relative quadratic budget remains open. A fixed
constant-factor gain alone would not suffice, because the positive source
atoms tend to zero.

`ActualSurvivorMass.lean` now constructs the actual incoming fibers as
suprema of finite sums of the original marked source atoms. It proves that
one fixed surviving atom remains in its true return fiber, without any
replacement distribution. `ExplicitClosure.lean` instantiates the seed
above, proves the unconditional quadratic baseline on those fibers, and
proves full Collatz under the displayed arbitrarily-small-factor uniform
fiber estimate. The estimate itself remains an explicit hypothesis.

The full countable resolvent, the logarithmic coefficient construction,
and the operator interpretation are written proofs in this note. They are
not hidden Lean axioms. In particular the finite module does not assert
that the Collatz transport improvement holds, nor does it infer a global
ordinary theorem from a finite computation.
