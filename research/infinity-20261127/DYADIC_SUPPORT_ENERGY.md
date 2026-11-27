# A support gap lowers the dyadic energy needed for compactness

**Conditional criterion; the required summability is open.** This note
distinguishes the energy of a component boundary from the energy needed to
make a general positive function converge. It uses exact ordinary
invariance, not merely approximate invariance of a constructed coloring.

Let `T` denote the shortcut Collatz map. A component indicator is a map
`b : N_{>0} -> {0,1}` with `b(T n)=b(n)`. In particular `b(2n)=b(n)`.
Define its even-wall density on an octave by

\[
 e_k(b)=2^{-k}\sum_{2^k\le n<2^{k+1}}
       |b(2n+1)-b(2n)|,\qquad k\ge0.
\]

**Written proposition.** Suppose a component indicator has both labels on
sets of positive lower natural density. Then

\[
                         \sum_{k\ge0}e_k(b)=\infty.                 \tag{1}
\]

The proof uses the pinned ordinary affine-coalescence estimate from
[PR146](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md):
for a genuinely invariant bounded label, the average of
`|b(3n)-b(n)|` on each large octave tends to zero. The exact path estimate
must be retained as an input; arbitrary approximate colorings do not
satisfy the conclusion of (1) without the other assumptions.

## Proof of the compactness implication

On `1 <= t < 2` set `g_k(t)=b(floor(2^k t))`. The left half of each cell
of `g_k` agrees with `g_{k+1}`, by exact doubling invariance. Only its right
half can change. Consequently

\[
 \|g_{k+1}-g_k\|_{L^1([1,2))}=\tfrac12 e_k(b).                       \tag{2}
\]

If the series in (1) were finite, these Boolean functions would converge
in `L^1` and almost everywhere to a Boolean function `G`. For example,
the sum of the measures on which consecutive values differ is finite,
so almost every point changes value only finitely often. The exact
identity `g_k(2t)=g_{k+1}(t)` extends the limit consistently to every compact
subinterval of `(0,infinity)` and gives `G(2t)=G(t)` almost everywhere.

Here is the small rounding issue needed to obtain tripling invariance.
Write `d(n)=b(n+1)-b(n)`. Exact doubling gives

\[
 d(n)=d(2n)+d(2n+1),\qquad
 |d(2n+1)|\le |d(n)|+|d(2n)|.                                      \tag{3}
\]

Put `W(N)=sum_{1<=n<N}|d(n)|`. Summing (3), with an absolute endpoint
error, gives

\[
 W(2N)\le W(N)+2\sum_{1\le n<N}|d(2n)|+O(1).                       \tag{4}
\]

Since `e_k(b)->0`, dyadic summation shows
`N^{-1} sum_{1<=n<N}|d(2n)| -> 0`. Divide (4) by `2N` and iterate to
obtain `W(N)=o(N)`. This uses only convergence of the even-wall densities
to zero, which follows from the assumed summability.

For `n=floor(2^k t)`, the integer `floor(3*2^k t)` differs from `3n` by
0, 1, or 2. Integrating the two possible intervening differences is
bounded by `O(2^{-k} W(6*2^k))=o(1)`. The affine-coalescence input gives
another `o(1)` bound when replacing `b(3n)` with `b(n)`. Therefore
`g_k(3t)-g_k(t)` tends to zero in `L^1([1,2))`, and the already established
local limits give `G(3t)=G(t)` almost everywhere.

Now put `H(s)=G(2^s)`. This is a bounded measurable function on the circle
`R/Z`, invariant under rotation by `log_2(3)`, an irrational number.
For completeness, if `c_j` is its `j`th Fourier coefficient, the rotation
identity gives `(1-exp(2*pi*i*j*log_2(3)))*c_j=0`. Thus every nonconstant
coefficient is zero, and `H` is constant almost everywhere. As `H` is
Boolean, that constant is 0 or 1.

Each label's positive lower natural density forces it to occupy a
uniformly positive fraction of every sufficiently large octave. One
explicit argument is useful here. If a doubling-invariant set has at
least `dX` members through `X`, discard the at most `dX/2` integers below
`dX/2`, and double each remaining member into `[X,2X)`. Every image has
at most `2+ceil(log_2(2/d))` such preimages. This gives a fixed positive
octave fraction. Equation (2) therefore cannot converge in `L^1` to
either constant. This contradiction proves (1).

## Passing from a separated support to square energy

Let a bounded real function `a(n)` vanish off a doubling-invariant set
`C`, and suppose

\[
                   a(n)\ge\delta>0\quad(n\in C).
\]

Its Boolean support `b=1_C` satisfies the pointwise estimate

\[
 |b(m)-b(n)|\le\delta^{-2}|a(m)-a(n)|^2.                            \tag{5}
\]

Consequently summability of the **square energy itself**,

\[
 \sum_{k\ge0}2^{-k}\sum_{2^k\le n<2^{k+1}}
               |a(2n+1)-a(2n)|^2<\infty,                           \tag{6}
\]

would imply the compactness used above. There is no square root in (6).
This relies on the gap between zero and the nonzero values of `a`;
square energy alone does not make an arbitrary bounded real sequence of
profiles converge.

Apply this observation to the actual escaping-component coefficient in
[PR193, ordinary Hardy section](https://github.com/GettysburgResearch/collatz/blob/792f8ac0fa8a80a6fc9acc91d7cafebc8695aa41/research/astra-diagonal-20261127/global/ORDINARY_HARDY.md).
There `a(n)=F(n)^2` on one escaping component and is zero off it, where
the ordinary simple-orbit reciprocal estimate gives a component-dependent
constant `c>0` with `c<=F(n)<1`. Thus `delta=c^2`, and (5) has factor
`c^{-4}`. The support is exactly invariant under the ordinary map.

The separately cited fixed-target predecessor-density theorem gives
positive lower density to this component and to the basin of 1. A target
divisible by three can first be advanced to a positive target prime to
three. The theorem is the
[ProofAtlas fixed-target release](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/),
not a uniform density assertion over moving targets. Under these named
inputs, every escaping component must make the series (6) diverge.

For a full Collatz criterion, one can instead take `a=b` to be the
indicator of all numbers that do not reach 1. Summability of its series
(6) would exclude both escape and nontrivial cycles. This statement does
not provide a way to estimate that unknown indicator.

## Why the existing bounds do not close the argument

The new PR193
[compression control](https://github.com/GettysburgResearch/collatz/blob/792f8ac0fa8a80a6fc9acc91d7cafebc8695aa41/research/astra-diagonal-20261127/global/COMPRESSION_CONTROL.md)
is positive everywhere. It shows that square-energy summability cannot
force strong compactness of a general real profile. Its support is
constant, so it does not contradict (5) or the Boolean compactness
argument. This is a narrower use of energy than convergence of the full
voltage.

On the other hand, the available ordinary synchronization bounds provide
only nonsummable errors of order `k^{-1/2}` at dyadic scale `k`. The
retained-wall dimension bound in PR197 controls walls followed from a
fixed birth; it does not count all walls newly born at later scales.
The explicit approximate colorings in PR200 already show why averaged
shift and tripling estimates by themselves do not yield summability.

**Open estimate:** prove (6) for an actual escaping-component coefficient,
or prove the Boolean version for the full bad set, using its zero ordinary
edge defects. No such bound is established in this checkpoint. This note
is a written reduction, not a new Lean proof of a universal Collatz claim.
