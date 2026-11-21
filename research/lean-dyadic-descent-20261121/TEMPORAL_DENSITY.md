# A uniform logarithmic bound for temporal band visits

**Full Collatz remains OPEN.** This continuation concerns the number of marked
states along one actual finite ordinary odd-orbit segment. It gives a uniform
quantitative refinement of the qualitative temporal-density theorem in PR178.
It does not identify temporal occupation with density of starting values or
with mass transported through the section.

Let `T` be the ordinary shortcut map and let

\[
x_0=n,\qquad x_{j+1}=\frac{3x_j+1}{2^{v_2(3x_j+1)}}
\]

for a positive odd starting value. Put `alpha=log_2 3`. The marked set is the
same one as PR173: an odd `x`, with `d=floor(log_2 x)`, is marked when
`(d+1)(x-2^d)<=70*2^d`. Write `V_n(N)` for the number of marked states among
`x_0,...,x_(N-1)`.

## 1. Distinctness supplies a finite error budget

Suppose only that these **N observed states are pairwise distinct**. The
endpoint `x_N` may repeat an earlier state, and no infinite escape-rate
assumption is needed. Any set of N distinct positive integers satisfies

\[
\sum_{j<N}\frac1{x_j}\le H_N,
\qquad H_N=\sum_{i=1}^N\frac1i\le1+\log N.
\]

The proof inserts the largest member of a finite set. If its cardinality is
N, that largest positive integer is at least N, so its reciprocal is at most
`1/N`. This gives the exact harmonic bound by induction; it does not assume
that orbit values are increasing.

The actual phase increment is

\[
\log_2x_{j+1}=\log_2x_j+\alpha-v_2(3x_j+1)
  +\log_2\left(1+\frac1{3x_j}\right).
\]

Telescoping the corresponding complex rotation and retaining every error
therefore gives, for each positive integer frequency k,

\[
\left|1-e^{2\pi i k\alpha}\right|
\left|\sum_{j<N}e^{2\pi i k\log_2x_j}\right|
\le 2+4\pi k H_N.
\]

Thus the normalized Fourier sum is `O_k(log(N)/N)`, uniformly over the
starting value and every segment satisfying the finite distinctness condition.
The implicit frequency constant is explicit in the displayed inequality.
This sharpens a limit statement into an actual finite estimate. It does not
establish uniform low-bit frequencies.

## 2. A finite marked-count estimate

The elementary integer-power separation already present in PR173 implies the
conservative nonresonance bound

\[
1\le(4^k+1)\left|1-e^{2\pi i k\alpha}\right|.
\]

The PR178 nonnegative trigonometric kernel can consequently be used at a
specified finite horizon. Define

\[
F(K,N)=(4^K+1)(2+4\pi K H_N).
\]

For any natural K and B such that `1120*pi*K<=B+1`, the new finite theorem is

\[
\boxed{\quad
K^2V_n(N)\le K^2 2^B+4KN+4K^2F(K,N).
\quad}
\]

Distinctness bounds the number of observed values smaller than `2^B` by
`2^B`. Every remaining marked value has a sufficiently small phase for the
kernel lower bound. The Fourier estimate controls the sum of that kernel.
This splits actual observed states by size; it does not replace them with
uniformly sampled integers.

`AnalyticCoupling.lean` proves these harmonic, Fourier, and finite-count
statements. Its PR178 dependencies are preserved byte for byte under
`vendor-pr178/`; their provenance is recorded in `SOURCES.json`.

## 3. An explicit bound for every horizon

`TemporalDensity.lean` chooses the free parameters in the preceding finite
inequality. The resulting bound is

\[
\boxed{\qquad
(\lfloor\log_2N\rfloor+1)V_n(N)\le196608\,N.
\qquad}
\]

The N=0 case is trivial. For N>0, let

\[
L=\lfloor\log_2N\rfloor,\quad
K=\left\lfloor\frac{L}{16384}\right\rfloor,\quad B=8192K.
\]

If K=0, use `V_n(N)<=N`. Otherwise,

\[
L+1\le16384(K+1)\le32768K,
\qquad 2^{16384K}\le N.
\]

The elementary inequalities `K<=2^K` and `pi<4` give

\[
K2^B\le N,\qquad
F(K,N)\le2^{21}4^K K^2,\qquad 4K F(K,N)\le N.
\]

For the last bound, `4K*2^21*4^K*K^2<=2^(23+5K)<=2^(16384K)`.
Substitution in the finite kernel estimate gives `K V_n(N)<=6N`; multiplying
by the digit bound proves the stated constant `32768*6=196608`.

The constant is deliberately large. The uniform statement is an asymptotic
research result; it is not advertised as a useful small-horizon numerical
cutoff. The parameterized finite inequality and the fixed-frequency bound
retain more information for a concrete application.

## 4. What the bound does and does not close

For every fixed nonrepeating infinite odd orbit, the estimate proves
`V_n(N)=O(N/log N)` and hence zero temporal density. PR173 still forces
infinitely many marked visits. These facts are compatible: infinitely many
visits can have a vanishing frequency.

The finite theorem also applies to one distinct period of a hypothetical
cycle, ending at its first repeated state. It must not be reapplied to many
repeated periods under a false injectivity premise.

This route does not yet give the survivor-specific upper bound sought by the
population arguments. A fixed positive starting atom can retain all its
weight while its deterministic orbit visits the section sparsely. No mass is
destroyed merely because the time between visits grows. The source-mass
transport in PR176 and the marked predecessor populations in PR180 remain
different quantities. Establishing a quantitative relation that excludes
every surviving ordinary source is still the missing global step.

## Evidence boundary

The exact Lean statements, pinned compiler and Mathlib versions, source
hashes, fresh compilation output, and axiom audit are recorded by
`replay_continuation.py` and the continuation report. The theorem is about the
ordinary map and actual finite states. No conjectural survivor decay,
equidistribution of parity residues, or custom convergence axiom is used.
