# Building on the forced dyadic-band visit

**Full Collatz convergence remains OPEN.** This pass builds directly on
the updated PR173 result that every positive ordinary orbit visits an odd
integer just above a power of two. It pursues the missing descent on that
section through actual finite certificates and through pointwise phase
dynamics. New theorem statements are checked in Lean; the open closing
inferences remain visible.

The frozen source is PR173 at
`fa0c9e2a2851e6324391e39c17afcb5913185aec`. Its four exact Lean modules
are retained under `lean/vendor/`; [SOURCES.md](SOURCES.md) gives their
Git blob identities, attribution, map convention, and dependency pins.
The older PR178 common-rank work is not treated as a proof of global coverage.

## The exact source result being used

Write `T(n)=n/2` for even inputs and `(3n+1)/2` for odd inputs. An odd
integer `n`, of binary depth `d=floor(log2 n)`, is marked when

\[
(d+1)(n-2^d)\le70\,2^d.
\]

PR173 proves that every positive orbit reaches such a point at a clock
strictly below `4*floor(sqrt n)+floor(log2 n)`. If `R` is the first
strictly positive marked return, then full Collatz is equivalent to

\[
\forall n>1\text{ marked},\quad \exists k\ge1:\quad R^k(n)<n.
\tag{OPEN}
\]

The source also proves `R(n)/n` can be arbitrarily large. This pass uses
both results; it does not presume contraction at each individual return.

## 1. Genuine first-return descent on an unbounded symbolic family

The new [`BandBridge.lean`](lean/BandBridge.lean) proves a quantitative
bridge into the exact global criterion. If `T^t(n)=m>0` and

\[
2^{4\lfloor\sqrt m\rfloor+\lfloor\log_2m\rfloor}m<n,
\]

then some positive complete marked-return iterate is below `n`. A simple
sufficient guard is `2^d<=n` and `6m<d`. No convergence or ordinary-floor
assumption for `m` is required. If every positive prefix clock before `t`
is even, the **first** marked return itself is smaller.

An unconditional family discharges that stronger obligation. For all
natural `r`, define

\[
\begin{aligned}
d_r&=256\,4^r,& L_r&=128\,4^r-(r+1),\\
N_r&=2^{d_r}+\frac{4^{L_r}-1}{3},& m_r&=12\,4^r+1.
\end{aligned}
\]

Lean proves markedness, unboundedness, the exact ordinary endpoint
`T^(2L_r)(N_r)=m_r`, an entirely even intervening prefix, `6m_r<d_r`, and

\[
\boxed{R(N_r)<N_r\quad\text{for every }r\ge0.}
\]

This is a proved portion of the actual return-map closure requirement.
It supplies no assertion that every marked input belongs to this family
or reaches another endpoint satisfying the guard.

## 2. Actual stopping certificates transfer to a whole binary cylinder

[`BandCertificates.lean`](lean/BandCertificates.lean) proves

\[
T^t(a)<a\quad\Longrightarrow\quad
T^t(a+2^t q)<a+2^t q
\qquad(q\in\mathbb N).
\]

In particular a stopping prefix for the small offset `a`, within the
available binary depth `d`, gives ordinary descent of `2^d+a`. This is
an exact all-parameter certificate rule, with the affine multiplier guard
derived from the actual smaller-offset path. It is not a statistical
assertion about typical offsets.

**The induction interface matters.** An ordinary smaller endpoint need
not be a smaller marked endpoint. A least marked failure supplies basin
facts only for smaller marked points; a least ordinary failure need not
be marked. The source's visit theorem does not supply a free ordinary
induction floor at its potentially larger output.

## 3. A complete ordinary family beyond the offset window

[`BandDescent.lean`](lean/BandDescent.lean) constructs, for every `k>=0`,

\[
b=2^{k+1},\quad d=b+k+1,\quad
a_k=2^b-1,\quad n_k=2^d+a_k.
\]

Every `n_k` is marked. Both the offset and the full input stay at least
their initial value through every clock `t<=d`. Thus the band condition
does not provide the stopping prefix required by section 2.

The proof continues past the failed window. With the positive odd integer

\[
v_k=\frac{3^{2^{k+1}}-1}{2^{k+3}},
\]

Lean proves exact paths and basin equivalences

\[
\operatorname{Basin}(a_k)\iff\operatorname{Basin}(v_k),\qquad
\operatorname{Basin}(n_k)\iff\operatorname{Basin}((2^{k+1}+1)v_k).
\]

The recurrence of `v_k`, smaller-index certificates, and shared binary
prefixes were pursued as possible ways to close that multiplier problem.
None supplies the needed product certificate. The [offset attack](BAND_DESCENT.md)
records the exact attempt and its first unsupported implication.

## 4. Pointwise Fourier control and zero temporal density of marked visits

For the actual odd orbit `x_j`, put `alpha=log2 3`. The new
[`ReturnFourier.lean`](lean/ReturnFourier.lean) proves

\[
\left|1-e^{2\pi i k\alpha}\right|
\left|\sum_{j<N}e^{2\pi i k\log_2x_j}\right|
\le2+4\pi k\sum_{j<N}\frac1{x_j}.
\]

Distinct positive states satisfy the free-cutoff bound
`sum(1/x_j)<=K+N/(K+1)`. Lean derives the full epsilon-form vanishing of
every nonzero normalized Fourier sum on **each injective odd orbit**.
There is no random-start or independent-parity premise. The usual
Fourier criterion gives uniform binary mantissas as a paper consequence.

The module retains the integer information erased by passing to a phase:

\[
\log_2x_N-\log_2x_0
=N\alpha-\sum_{j<N}\nu_2(3x_j+1)+E_N,
\qquad 0\le E_N\le\sum_{j<N}\frac1{x_j}.
\]

The missing drift argument must control the halving sum in this identity.
Phase uniformity alone does not do so. [RETURN_DYNAMICS.md](RETURN_DYNAMICS.md)
separates the compiled statements from the remaining descent implication.

The stronger orbitwise conclusion is also checked in Lean. For the same
fixed odd source with injective odd orbit, let `M(n,N)` count marked
states among its first `N` odd-step indices. The theorem in
[`MarkFrequency.lean`](lean/MarkFrequency.lean) proves

\[
\forall\varepsilon>0\ \exists N_0\ \forall N\ge N_0,
\qquad M(n,N)<\varepsilon N.
\]

This is **temporal density zero on one actual orbit**, a different
statement from the source's natural-density bound on the marked set.
The proof uses the nonnegative finite kernel
`|sum(r<K,exp(2*pi*i*r*u))|^2`, its checked Fourier expansion, and the
actual marked-phase estimate from [`MarkPhase.lean`](lean/MarkPhase.lean).
It assumes no Weyl criterion or equidistribution hypothesis. The forced
visits can therefore be infinite while their time proportion tends to
zero. This does not settle the integer halving drift or exclude cycles.

## 5. The biased limiting law has arbitrary finite ordinary realizations

The limiting phase/2-adic dynamics permits uniform phase paired with
the fixed 2-adic state `-1`. Its valuation is constantly one, so its
formal logarithmic drift is positive. This is not an ordinary positive
counterexample.

[`BandSimulation.lean`](lean/BandSimulation.lean) proves the precise
ordinary finite realization: for any horizon `L`, precision `K>=1`, and
height floor `M`, there is a marked positive `n>M` whose states through
`L` clocks are odd, at least `n`, and congruent to `-1 mod2^K`.
The explicit construction even lies in the narrower constant-two band.

The start depends on `L,K,M`. This distinction prevents replacing a
fixed ordinary orbit by a sequence of compatible-looking finite witnesses.
The [joining attempt](JOINING_ATTEMPT.md) develops the real/2-adic route
and identifies the required fixed-source exclusion.

## Build, audit, and publication

Use Lean 4.34.1 and Mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The [build guide](LEAN_ROUTE.md)
explains the exact imports and the small compatible extraction of PR178's
orbit lemmas. With that runtime on `PATH`:

```sh
MATHLIB_DIR=/absolute/path/to/mathlib4 bash lean/build.sh \
  BandCertificates BandDescent BandSimulation ReturnFourier \
  MarkPhase MarkFrequency BandBridge BandAudit
```

`BandAudit.lean` prints logical dependencies of every public theorem in
the new modules and the reused arithmetic extraction. Standard Lean
axioms are distinguished from a conjectural premise; no such premise or
`sorry` supplies the open global criterion.

Checkpoints are published to [PR178](https://github.com/GettysburgResearch/collatz/pull/178).
The PR body records the exact checked commit and actual clean-checkout
execution receipt. A compiled conditional theorem establishes exactly its
displayed statement; it does not prove an omitted universal selector.
