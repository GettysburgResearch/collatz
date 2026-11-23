# The ordinary trace-height step: a genuine discounted bound and its lost endpoint

**Status: written calculation and explicit unresolved endpoint; no Collatz
closure.** The excessive profile and notation are those constructed in
`ANCHORED_INVERSE_GREEN.md`. This note does not identify that profile with a
canonical density by assumption.

**Later integration and priority:** PR180 at
`d0349de2108abb7c8fb8393c086610e3372df116` already proves the stronger
fixed-discount bound for all targets, including periodic ones, and supplies
a marked-only Lean closing theorem. The calculations below record the
independent attempt and its failed critical endpoint passage.
[ABEL_CANONICAL_COMPARISON.md](ABEL_CANONICAL_COMPARISON.md) now proves
harmonicity and comparison with PR180's canonical envelope; it does not
prove the remaining upper bound on changing marked targets.

## 1. Every fixed Abel discount gives a sublinear ordinary height bound

For `0<r<1`, recall

\[
H_r(q)=(1-r)\sum_{j\ge0}r^j\rho_j(q).
\]

At every positive odd nonperiodic target, the preceding note proves

\[
S_N(q):=\sum_{j=0}^N\rho_j(q)
\le q(1+8N)+\frac65q^u e^{-cN},
\quad u=\log_2(4/3),\quad c=8u-\log6>0.              \tag{1}
\]

Also `rho_j(q)<=3^j`, directly from its probability definition.
For `1/3<r<1`, split the Abel series at

\[
J=\max(1,\lceil\log_3 q\rceil).
\]

Its initial part is bounded by

\[
(1-r)\sum_{j<J}(3r)^j
\le \frac{1-r}{3r-1}(3r)^J.                         \tag{2}
\]

Summation by parts, retaining the nonnegative tail and then discarding only
the subtractive initial term, gives

\[
\begin{aligned}
(1-r)\sum_{j\ge J}r^j\rho_j(q)
&\le (1-r)^2\sum_{N\ge J}r^N S_N(q)\\
&\le q r^J\big((1-r)(1+8J)+8r\big)
 +\frac65q^u\frac{(1-r)^2(re^{-c})^J}{1-re^{-c}}.
\end{aligned}                                      \tag{3}
\]

Since `J=log_3 q+O(1)`, equations (2)--(3) prove

\[
\boxed{
H_r(q)\le C_r q^{\theta(r)}(1+\log q),\qquad
\theta(r)=1+\log_3 r<1,
}                                                   \tag{4}
\]

uniformly in positive odd nonperiodic `q`. In particular,

\[
\lim_{\substack{q\to\infty\\q\text{ nonperiodic}}}
\frac{H_r(q)}q=0\qquad\text{for every fixed }r<1.     \tag{5}
\]

The residual power in (3) is harmless: `u-c/log 3<0`, so it is smaller than
the main term for `r>1/3`. For `r<1/3`, the elementary estimate
`H_r(q)<=(1-r)/(1-3r)` is already uniform in `q`; the endpoint `r=1/3`
has a logarithmic estimate from the same split. Those cases are not needed
for the critical limit.

This is an actual admissibility-sensitive bound at fixed discount. It uses
the cumulative count at a fixed ordinary target; it is not inferred from
an almost-everywhere density estimate.

## 2. Why this does not yet exclude an escaping orbit

The exact Abel equation is

\[
L_1H_r=\frac{H_r-(1-r)}r.                            \tag{6}
\]

Thus `H_r` is not the excessive profile required for critical trace
propagation. For an actual forward odd edge `U(x)=q`, positivity gives

\[
H_r(q)\ge r\frac3{2^{v_2(3x+1)}}H_r(x).             \tag{7}
\]

Along a path of `k` odd steps, the factor is `r^k`. The critical profile
`h` is obtained only after `r -> 1`, and its bound (4) simultaneously loses
its sublinear exponent: `theta(r) -> 1`.

This loss cannot be removed by exchanging limits. To preserve the mass of
a fixed source transported for `k` steps, a joint limit needs
`(1-r)k` controlled. To make the factor

\[
q^{\theta(r)-1}=
\exp\!\left(\frac{\log r}{\log3}\log q\right)
\]

vanish, it needs `(1-r)log q -> infinity`. But every positive odd step
satisfies `U(x)<2x`, so `log q <= log x_0+k log 2`. These requirements
cannot hold together along one fixed source's path. The additional
discounted loss is therefore not a valid replacement for ordinary
absorption.

The bound in `ANCHORED_INVERSE_GREEN.md` reaches the critical profile and
retains the source; it obtains `h(q)<=8q`, exactly the endpoint left by this
calculation.

## 3. The arithmetic spikes that any improvement must allow

Suppose a positive critical excessive profile satisfies `h>=alpha` on odd
units. For every even `L`, take

\[
q_L=2\cdot3^L-1,\qquad x_L=2^{L+1}-1.
\]

There is an actual inverse path of `L` gap-one steps from `q_L` to `x_L`.
All its states are positive odd units. Repeated excessiveness therefore
forces

\[
h(q_L)\ge(3/2)^Lh(x_L)
\ge\alpha(3/2)^L.                                 \tag{8}
\]

Hence a bounded profile is impossible. A proposed global power envelope
`h(q)<=Cq^theta` must have

\[
\theta\ge\log_3(3/2).
\]

This leaves a nonempty sublinear range. A bound anywhere in that range
would be useful, but is not proved by (4).

For the profile actually constructed from the frozen CFJ input, the exact
source-qualified family can equivalently be written

\[
\boxed{h(2\cdot3^{2k}-1)\ge\alpha(3/2)^{2k}
\qquad(k\ge0).}                                    \tag{8a}
\]

Its terminal inverse source is `2^(2k+1)-1`, a positive odd ternary unit.
Thus (8a) uses the positive floor already justified in the separate note;
it makes no assumption that a generic profinite point has an ordinary
realization.

## 4. A concrete finite-resolution bridge, not supplied by the literature

The author-primary manuscript *A positive semicontinuous density for the
Syracuse stationary law* constructs a greatest lower semicontinuous density
`E` and identifies it with its finite integer trace. Its integer convergence
is Cesaro mean absolute convergence at each fixed integer; it gives no
uniform growing-integer onset. Its density is discontinuous at every
positive unit integer. The companion *Quadratic cylinder energy and
integrability of the Syracuse law* gives uniform finite-level `L^p` bounds
for `1<p<2`. These are reported external analytic/formal developments,
not rebuilt in this pass.

If one uses those stated `L^p` bounds, each depth-`k` cylinder has Haar mass
`3^{-k}`, so Holder's inequality gives the elementary pointwise estimate

\[
\rho_k(q)\le C_p3^{k/p}.                            \tag{9}
\]

A specific sufficient missing bridge is therefore:

> For some `1<b<p<2`, prove that the ordinary trace at every sufficiently
> large positive odd nonperiodic integer `q` satisfies
> \[
> E(q)\le C\max_{0\le k\le b\log_3q}\rho_k(q).
> \tag{10}
> \]

Equations (9)--(10) would give `E(q)<=C' q^(b/p)=o(q)`. Together with the
actual-edge critical propagation and finite correction product, this would
exclude escaping orbits. It would still leave the separate positive-cycle
gate.

No fixed-integer Cesaro theorem, lower semicontinuity statement, Haar
`L^p` estimate, or CFJ lower population bound establishes (10). In
particular, the conductor needed by lower semicontinuity may depend on `q`
without the required height control. This precise missing uniformity is the
first unsupported step in the attempted trace-height completion.

## 5. Two bounded positive unit parents at every unit target

The full excessive inequality supplies more than separate edge
inequalities. This extra additive information yields a uniform lower
trace ratio on every possible positive cycle.

Let `q` be any positive odd integer prime to three. Among `e=1,...,6`,
there are two distinct exponents for which

\[
x_e=(2^e q-1)/3
\]

is a positive odd ternary unit. One explicit choice is:

| `q mod 9` | Two exponents |
|---|---|
| 1 | 2, 4 |
| 2 | 1, 3 |
| 4 | 2, 6 |
| 5 | 3, 5 |
| 7 | 4, 6 |
| 8 | 1, 5 |

Indeed the powers `2^e mod 9` for `1<=e<=6` run through all six units.
Exactly one exponent gives `2^e q=4 mod 9`, and exactly one gives
`2^e q=7 mod 9`. The resulting quotients are integers congruent to one
or two modulo three. They are positive because their positive numerator
is divisible by three, and odd because that numerator is odd. Since `q`
is odd, `3x_e+1=2^e q` also certifies that its valuation is exactly `e`.
Distinct exponents give distinct parents.

Each of these two edges has critical multiplier at least `3/64`. Given
*any* particular positive unit parent `x` of `q`, at least one of the two
chosen parents differs from it. Thus full excessiveness and `h>=alpha`
give

\[
\boxed{
h(q)\ge\frac3{2^e}h(x)+\kappa,
\qquad \kappa=\frac{3\alpha}{64},
\qquad 3x+1=2^e q.
}                                                   \tag{11}
\]

The exponent `e` of the particular parent need not be at most six. Only the
additional parent uses that bound. Equation (11) requires domination of
the *sum* of two parent terms. Separate single-edge inequalities would not
justify adding the positive constant.

## 6. Every positive cycle has a uniform trace-ratio floor

Every positive odd cycle consists of ternary units, because every output
of `U` is prime to three. On any such finite cycle choose a vertex `q`
minimizing

\[
g(y)=h(y)/y,
\]

and let `x` be its preceding cycle vertex. Then `g(x)>=g(q)` and
`3x+1=2^e q` for an integer `e>=1`. Divide (11) by `q` to obtain

\[
g(q)\ge\frac{3x}{3x+1}g(x)+\frac\kappa q
\ge\frac{3x}{3x+1}g(q)+\frac\kappa q.
\]

Consequently

\[
\frac{g(q)}{3x+1}\ge\frac\kappa q,
\qquad
g(q)\ge\kappa\frac{3x+1}{q}
=\kappa2^e\ge2\kappa.
\]

By the choice of `q`, every vertex `y` on the cycle therefore satisfies

\[
\boxed{\frac{h(y)}y\ge\frac{3\alpha}{32}.}           \tag{12}
\]

This includes the trivial odd cycle `{1}`; it is a quantitative restriction
on all cycles, not a proof that no cycle exists. No period-length bound,
absence of additional cycles, or source equidistribution is assumed.

## 7. A finite closing criterion that handles both alternatives

Assume a finite positive profile on all positive odd units satisfies the
full critical excessive inequality and `h>=alpha>0`. Suppose one proves:

1. `h(q)/q -> 0` as positive odd units `q -> infinity`;
2. an explicit integer `M>=2` such that
   `h(q)/q < 3alpha/32` for every positive odd unit `q>=M`;
3. every positive odd ternary unit `q<M` reaches one.

Then every positive integer reaches one.

For the escape alternative, an injective odd forward orbit has summable
reciprocals by the finite-segment packing proved in the Green note. Actual
edge propagation gives

\[
\frac{h(q_k)}{q_k}
\ge\frac{h(q_0)}{q_0}
 \prod_{j<k}\frac{3q_j}{3q_j+1}
\ge\frac{h(q_0)}{q_0}
 \exp\!\left(-\frac13\sum_{j\ge0}\frac1{q_j}\right)>0.
\]

The distinct positive integers `q_k` tend to infinity, contradicting
hypothesis 1. Every orbit therefore eventually enters a cycle. Equation
(12) and hypothesis 2 put every vertex of every such cycle below `M`.
Hypothesis 3 then forces that cycle to be `{1}`. Any initial even factors
can be removed, and the next odd step from an odd multiple of three is a
ternary unit, so this covers all positive ordinary sources.

A tail bound merely below `3alpha/32`, without hypothesis 1 or another
escape argument, would control cycles but would not exclude an escaping
spine with a smaller positive limiting ratio.

For a more explicit sufficient input, suppose

\[
h(q)\le Cq^\theta\qquad(q\ge Q_0),
\quad C>0,\quad 0\le\theta<1.                       \tag{13}
\]

Then hypothesis 1 follows. One may take any integer

\[
M\ge\max\left\{2,Q_0,
 \left(\frac{64C}{3\alpha}\right)^{1/(1-\theta)}\right\},
\]

since `h(q)/q<=3alpha/64<3alpha/32` for `q>=M`. A finite basin
certificate below that supplied `M` completes the criterion.

The current packet proves the profile's existence and the cycle floor,
but does not prove (13), general sublinearity, or the native-height gate
(10). Its CFJ-derived `alpha` is also not numerically evaluated. Therefore
the finite verification threshold is a conditional explicit formula, not
a computed cutoff or a completed proof of Collatz.

### Primary source locations

- Lucas Valbuena, *A positive semicontinuous density for the Syracuse
  stationary law*,
  [author's TeX source](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/paper/positive-stationary-envelope.tex).
  The envelope theorem and integer Cesaro corollary were read; no external
  Lean replay was performed.
- Lucas Valbuena, *Quadratic cylinder energy and integrability of the
  Syracuse law*,
  [author's TeX source](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/paper/quadratic-cylinder-energy.tex).
  Its `L^p` conclusion is used only in the explicitly conditional deduction
  (9)--(10), not in Sections 1--3 or the separate Green estimate.
