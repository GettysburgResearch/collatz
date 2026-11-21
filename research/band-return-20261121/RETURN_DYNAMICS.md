# Return dynamics: a deterministic Fourier estimate and the missing drift

## Scope and source

This investigation starts from GettysburgResearch/collatz PR173, frozen at
`fa0c9e2a2851e6324391e39c17afcb5913185aec`. The read scope was the README and
`ForwardSection.lean`, `SectionDynamics.lean`, and `RisingReturns.lean`, with
special attention to the actual odd-orbit phase equation. The imported files
were not edited. The purpose is to establish descent through several marked
returns, including returns which individually increase.

The new results in this lane are a deterministic finite Fourier estimate
for each actual orbit prefix, the pointwise vanishing Fourier limit, and a
directly formalized zero temporal density theorem for marked visits. They
apply to each positive odd orbit that is not eventually periodic, rather
than almost every starting value. They do not establish the halving drift
needed for Collatz. The obstruction to that final inference is explicit
below.

## 1. The exact additive quantity which has to turn negative

Let

\[
 x_{j+1}=\frac{3x_j+1}{2^{a_j}},\qquad
 a_j=v_2(3x_j+1),\qquad x_0>0\text{ odd},
\]

and put \(y_j=\log_2x_j\), \(\alpha=\log_2 3\). Then

\[
 y_{j+1}=y_j+\alpha-a_j+\varepsilon_j,
 \qquad
 \varepsilon_j=\log_2\!\left(1+\frac1{3x_j}\right),
 \qquad 0<\varepsilon_j\le\frac1{x_j}.
\]

For any complete block of odd steps,

\[
 y_N-y_0=N\alpha-A_N+E_N,
 \quad A_N=\sum_{j<N}a_j,
 \quad E_N=\sum_{j<N}\varepsilon_j.
 \tag{1}
\]

If the block begins and ends at marked points, its fractional endpoint
phases are small. That restricts \(N\alpha\) modulo one. The integer
\(A_N\), which counts the actual halvings, still determines the sign of
the full change. A downward block requires

\[
 A_N>N\alpha+E_N.
 \tag{2}
\]

Several marked returns concatenate exactly in (1); their phase errors do
not acquire a favorable sign on concatenation. Thus replacing one return by
many returns is useful only if it supplies new information about \(A_N\).

## 2. A finite pointwise estimate for every orbit prefix

For a positive integer frequency \(k\), write

\[
 z_j=\exp(2\pi i k y_j),\qquad
 \lambda_k=\exp(2\pi i k\alpha).
\]

The integer \(a_j\) disappears from the character, leaving the exact
identity

\[
 z_{j+1}=\lambda_k z_j\exp(2\pi i k\varepsilon_j).
\]

Consequently

\[
 (1-\lambda_k)\sum_{j<N}z_j
 =z_0-z_N+\sum_{j<N}(z_{j+1}-\lambda_kz_j).
 \tag{3}
\]

Using \(|z_j|=1\) and the elementary exponential bound gives the following
conservative constant, chosen to match the Lean implementation:

\[
 \boxed{
 |1-\lambda_k|\left|\sum_{j<N}z_j\right|
 \le 2+4\pi k\sum_{j<N}\frac1{x_j}.}
 \tag{4}
\]

There is no randomness assumption, no unspecified measure, and no
conditioning on an unproved stopping time in (4). Repeated states are
allowed in this finite theorem.

### Distinct states give a uniform error budget

If the first \(N\) states are distinct, then for every integer cutoff
\(K\ge0\),

\[
 \sum_{j<N}\frac1{x_j}\le K+\frac{N}{K+1}.
 \tag{5}
\]

Indeed, at most \(K\) distinct positive states are at most \(K\), each
contributing at most one. Every remaining state contributes at most
\(1/(K+1)\). The estimate does not depend on the initial height.

Combining (4) and (5) gives a fully finite estimate:

\[
 |1-\lambda_k|\frac1N\left|\sum_{j<N}z_j\right|
 \le \frac{2+4\pi kK}{N}+\frac{4\pi k}{K+1}.
 \tag{6}
\]

The free cutoff is sufficient to obtain a limit: choose \(K\) first,
then let \(N\) increase. Since \(\log_2 3\) is irrational,
\(\lambda_k\ne1\) for every positive \(k\). Thus on every injective
infinite positive odd orbit,

\[
 \frac1N\sum_{j<N}\exp(2\pi i k\log_2x_j)\longrightarrow0
 \qquad(k\ge1).
 \tag{7}
\]

The same holds for negative frequencies by conjugation. The Fourier
criterion therefore gives uniform distribution of \(\log_2x_j\) modulo
one. For each fixed \(1\le a<b\le2\), the limiting frequency of binary
significands in \([a,b)\) is \(\log_2(b/a)\).

An orbit of a deterministic map which is not eventually periodic is
injective: one repeated state forces eventual periodicity. Thus the
conclusion covers every such positive odd orbit, including any
hypothetical divergent one.
It makes no assertion excluding a nontrivial cycle.

### A consequence for the actual marked-return clocks

There is also a **kernel-checked** orbitwise conclusion about the shrinking
section itself.
An injective sequence of positive integers tends to infinity, since each
bounded set contains only finitely many states. Therefore the section's
allowed phase width tends to zero along an injective orbit. For any fixed
\(\eta>0\), every sufficiently late marked odd state has phase in
\([0,\eta]\). Uniform distribution bounds the upper temporal density of
those indices by \(\eta\). Letting \(\eta\) decrease gives

\[
 \frac{\#\{j<N:x_j\text{ is marked}\}}{N}\longrightarrow0.
\]

The imported visit theorem still guarantees infinitely many such indices.
Thus, if \(q_r\) is the odd-step index of the \(r\)-th marked visit on an
injective orbit, \(q_r/r\to\infty\). This is an orbitwise zero-frequency
result, distinct from the natural density of marked integers in the ambient
number line. The count limit itself is formalized below. The inverse-count
conclusion about \(q_r\) is an elementary paper deduction; neither statement
claims that zero-frequency visits force descent.

### Direct finite kernel proof of temporal zero density

The pinned Mathlib has no ready-made Weyl equidistribution criterion. The
formal proof therefore bypasses a general equidistribution library and
constructs a finite nonnegative kernel:

\[
 G_K(u)=\left|\sum_{r=0}^{K-1}e^{2\pi i r u}\right|^2\ge0.
\]

Its checked successor identity is

\[
 G_{K+1}(u)=G_K(u)+1+
 2\sum_{r<K}\operatorname{Re}(e^{2\pi i(K-r)u}).
\]

Fix \(K\) and \(\delta>0\). The pointwise Fourier theorem provides a
common horizon after which every frequency \(1\le k<K\) has Fourier
sum of norm at most \(\delta N\). Induction in the displayed finite
identity then proves

\[
 \sum_{j<N}G_K(y_j)\le KN+K^2\delta N.
 \tag{9}
\]

For an injective integer sequence, every sufficiently late marked state
has phase \(u=y_j-\lfloor y_j\rfloor\) in
\([0,1/(8\pi K)]\). The already checked bound
\(|e^{2\pi i r u}-1|\le4\pi r|u|\) puts each of the \(K\)
summands within \(1/2\) of one. The triangle inequality consequently gives
\(G_K(y_j)\ge K^2/4\) at every sufficiently late marked visit. Let
\(J\) be the start of that tail and \(C_N\) its total visit count through
odd clock \(N-1\). A finite counting inequality gives

\[
 K^2C_N\le K^2J+4\sum_{j<N}G_K(y_j),
 \qquad
 \frac{C_N}{N}\le\frac JN+\frac4K+4\delta.
 \tag{10}
\]

Choose \(K\) large, \(\delta\) small, and then \(N\) large. Every
step, including the actual-state phase tail and the final epsilon limit,
is checked in `MarkPhase.lean` and `MarkFrequency.lean`. In particular,
`marked_visits_density_zero` quantifies over one fixed odd starting integer
and assumes only injectivity of its actual odd orbit. It imports no
equidistribution or valuation-independence hypothesis.

The formal count uses **odd-step indices**. Zero temporal density at full
shortcut clocks follows mathematically as well: marked states are odd,
and there are no more odd steps than full shortcut steps. This latter
change-of-clock corollary is not separately formalized in this module.

### Sharper paper estimate

Sorting the distinct positive odd states gives the additional elementary
bound, for \(N\ge1\),

\[
 \sum_{j<N}\frac1{x_j}
 \le\sum_{r=0}^{N-1}\frac1{2r+1}
 \le1+\tfrac12\log(2N-1).
\]

The first inequality uses that the \(r\)-th smallest distinct positive odd
integer is at least \(2r+1\); the second follows by comparison with the
integral of \(1/(2t+1)\). This improves the finite Fourier estimate to
\(O_k(\log N)\). This sharper harmonic estimate is a paper derivation,
separate from the simpler cutoff estimate in Lean.

## 3. Why this does not yet determine the return drift

For an injective orbit, (5) also implies \(E_N/N\to0\). Equation (1)
therefore gives

\[
 \frac{y_N-y_0}{N}=\alpha-\frac{A_N}{N}+o(1).
 \tag{8}
\]

Uniform phase distribution controls the fractional part of \(y_N\).
Equation (8) requires the integer halving cocycle. No implication from the
former to the latter was found. In particular, uniform distribution of
leading digits is not independence from the trailing binary digits which
determine \(a_j\).

This gap survives a natural real/2-adic joining formulation. In the regime
where ordinary states tend to infinity, the leading-phase perturbation
tends to zero. The limiting skew map is

\[
 (\theta,z)\longmapsto
 (\theta+\alpha\pmod1,\ S(z)),
 \qquad S(z)=\frac{3z+1}{2^{v_2(3z+1)}}
\]

on the circle and odd 2-adic integers, away from \(z=-1/3\). The point
\(z=-1\) is fixed by \(S\), and its valuation is exactly one. Therefore

\[
 \text{Haar measure on the circle}\ \times\ \delta_{-1}
\]

is an invariant joining with uniform phase marginal and mean valuation
one. Its formal logarithmic drift is \(\alpha-1>0\).

This joining is **not** a positive ordinary Collatz orbit. It demonstrates
that invariance and the newly proved phase marginal alone cannot establish
the required mean valuation. A successful joining argument must exclude
this and other biased 2-adic invariant laws specifically for empirical
measures of positive ordinary orbits; silently replacing them by the Haar
2-adic law would assume the missing arithmetic conclusion.

The analogous full-shortcut phase identity in base three also gives a
uniform marginal along an injective orbit. Two such marginal statements
still do not supply the correlation with trailing digits.

## 4. Two tempting extensions checked and not used

**A fixed number of rising returns.** The existing rising-prefix family
does not immediately give arbitrary many consecutive expanding returns.
A positive ordinary all-odd prefix has length at most its binary size,
while the marked window has width proportional to the reciprocal of that
size. Repeating a Dirichlet denominator accumulates approximation error.
The initial positive buffer used in `RisingReturns.lean` is finite; it
cannot be reused indefinitely. No unproved assertion about the continued
fraction coefficients of \(\log_2 3\) is used here.

**Making the offset absolutely small by steering.** A long phase-steering
search allows a comparably long interval of height growth. The existing
proof controls the relative dyadic offset by an inverse logarithm of the
visited value; it does not make the integer offset bounded. Replacing the
relative bound by a bounded or uniformly short-stopping offset would
require additional orbit-growth information.

## 5. Status of the full proof attempt

The phase route has produced new actual-pointwise control and a precise
joining obstruction. It has not proved (2) on every marked orbit, excluded
all nontrivial cycles, or discharged `collatz_iff_return_descent`.

`ReturnFourier.lean` **compiled successfully** with Lean 4.34.1 and
`-j1 -DwarningAsError=true`. The new import beyond `ForwardSection` is
`Mathlib.Analysis.SpecialFunctions.Complex.Log` at the packet's pinned
Mathlib revision. The checked theorems are:

- `actual_log_cocycle`: the exact real-height equation, retaining the
  integer halving sum and the actual reciprocal error budget;
- `odd_prefix_fourier`: (4) for each finite prefix;
- `injective_prefix_fourier`: the finite cutoff estimate;
- `fourier_averages_vanish`: (7) in its full epsilon definition for every
  injective positive `oddOrbit`;
- `ordinary_odd_fourier_limit`: the odd-source wrapper, for which the
  imported `odd_orbit_hit` identifies every state with an actual ordinary
  shortcut iterate of the same source.

All five printed axiom reports contain only `propext`, `Classical.choice`,
and `Quot.sound`.

The extension `MarkFrequency.lean` also compiled with the same strict
settings. Its audited main theorem, `marked_visits_density_zero`, has only
those same three axioms. Its explicit dependencies are
`ReturnFourier → MarkPhase → MarkFrequency`; `MarkPhase.lean` supplies the
actual marked-phase estimate and escape of an injective natural-valued
sequence from each fixed finite interval. The finite kernel sum, kernel
lower bound, visit-count bound, and epsilon argument are all checked.

The general interval-frequency interpretation via the Fourier criterion,
the sharper harmonic estimate, the inverse-count return-clock consequence,
and the final change to full shortcut clocks remain the mathematical
deductions identified above. No empirical experiment or assumed low-bit
independence enters either formal module.
