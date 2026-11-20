# Three attempts at the remaining global Collatz implication

**PROPOSED research. Collatz remains unresolved.** This packet follows the
latest directed-merger, ordinary Dirichlet, arithmetic-complexity and spectral
work at the exact source heads in [SOURCE_BOUNDARIES.md](SOURCE_BOUNDARIES.md).
Three agents pursued different closing mechanisms; the root reconstructed
their arguments and two agents cross-reviewed the other routes.
These are AI proof reconstructions, not human referee acceptance or formal
proof-assistant verification.

The shortcut map is \(T(n)=n/2\) on even inputs and \(T(n)=(3n+1)/2\) on odd
inputs. The odd map is \(U(n)=(3n+1)/2^{v_2(3n+1)}\). All source and cycle
statements below concern actual positive ordinary integers.

## What the latest work leaves to prove

PR146 advanced again during this round, to
`e238c63a5d57f96bb063b7472498d1977df51951`. Its refreshed certificate analysis
already includes the same depth-two classification and Mersenne reduction,
with stronger general restrictions on lifted certificates and a rank-three
embedding of all sufficiently large Mersenne exponents. We credit that
overlap explicitly; our depth-two note is retained as an independent
reconstruction with complete-orbit separation. The new reverse-basin
criterion also exposes a pure-power subproblem. None of these reductions
supplies the prime-support or oriented-moment upper bound used by the other
two routes. See [the final source comparison](LATEST_146_COMPARISON.md).

The frozen PR146 proves that full Collatz is equivalent to

\[
16k+1\text{ reaches }1\quad\Longrightarrow\quad
32k+1\text{ reaches }1,\qquad k\ge0.
\]

It also gives thin adjacent-pair criteria and bounded directed return paths
when forward tripling edges are added. Those additional edges are not
ordinary Collatz mergers. PR155 gives subcritical Dirichlet coercivity.
PR156 shows that a general spectral gap is unavailable even on explicitly
convergent ordinary sources. This packet tries to use more of the actual
arithmetic and direction of the remaining implications.

| Attempt | Result obtained | Missing global step |
|---|---|---|
| Directed boundary analysis | A single positive weighting balances inward and outward tripling defects exactly. Either oriented moment gives one-sided functional coercivity. | No arithmetic estimate makes the separating boundary empty. |
| Prime support at height peaks | A prefix using at most \(s\) primes satisfies an explicit height bound with a linear source factor; a cycle has a source-independent bound. | No upper bound prevents an exceptional orbit or cycle from using more primes. |
| Transport a known convergence certificate | Independently reconstruct the now-overlapping depth-two classification and prove separation from the complete known orbit. | A successful transport must use more than the source's odd-event depth; convergence of every residual target is unproved. |

## 1. Exact positive circulation on directed tripling comparisons

Let \(f(Tn)=f(n)\) and put \(g(n)=f(3n)-f(n)\). The source construction
returns from \(3x\) to \(x\) using ordinary edges in either direction and
forward triplings. Fix a deterministic version and let \(S_x\) be the
multiset of tripling sources on that return.

For a positive weight \(\omega\) comparable at fixed multiplicative distance,
define

\[
\pi_\omega(y)=\omega(y)+
\sum_{x\ {\rm odd}>0}\omega(x)\#\{y\text{ in }S_x\}.
\]

The finite affine source list makes this a finite sum at each fixed \(y\),
with \(\pi_\omega\) comparable to \(\omega\). If either oriented moment is
finite, then both are finite and

\[
\sum_{y\ {\rm odd}}\pi_\omega(y)g_+(y)
=\sum_{y\ {\rm odd}}\pi_\omega(y)g_-(y).
\]

The weight is fixed independently of the labeling or component cut.
Nonnegative inequalities first justify the summability; the proof never
subtracts infinite fluxes. Power and logarithmically modified power weights
are included.

Combining this with the pinned ordinary coercivity theorem gives estimates
using either orientation alone. A clipping argument further covers
unbounded real invariant labels: if every component has divergent
\(\beta\)-moment, \(0<\beta<1\), a finite positive or negative defect
\(\beta\)-moment forces the label to be constant. The specialization at
\(\beta=0.84\) retains the explicitly imported Krasikov--Lagarias input.

The directed counting comparisons and their abscissa consequences already
appear in PR146. The additional object here is the common exact circulation
and its functional formulation. Positive balanced circulation alone does
not eliminate a cut.

Read [the construction and proof](DIRECTED_BOUNDARY_CIRCULATION.md).

## 2. A prime-support bound on actual peaks

If a finite odd trajectory prefix uses primes from a single set of cardinality
at most \(s\ge1\), then

\[
\boxed{\max_j n_j\le
\max\{4^s n_0,(s+1)^{64s}\}.}
\]

Every positive odd cycle using at most \(s\) primes satisfies

\[
\boxed{\max n<(s+1)^{64s}.}
\]

The proof charges repeated prime powers to positive affine return numerators.
In a window of \(2s\) transitions ending at a maximum, its total return cost
is below \(6s\). Delete one point of maximum valuation for each prime.
At least \(s+1\) high states remain, and their prime-height tails have no
uncharged first occurrence. Integrating those tails bounds the peak.

The underlying return-tail and maximum-deletion mechanism is credited to
Paper138. The short peak-window synthesis improves the elementary
\(\exp(O(s^2))\) height scale to \(\exp(O(s\log(s+1)))\) in the
prime-support subclass. The parameter is the number of primes, not the
more general multiplicative rank.

There is also a source-specific local statement. At a record with
\(M=\log_2 n_{\rm peak}>\max(8,2\log_2 n_0)\), the last
\(\lceil M/2\rceil\) odd states contain more than

\[
\frac{M}{28+7\log_2 M}
\]

distinct primes. The pool may be selected anew after each such window.
This growth requirement does not contradict a fixed input: a deterministic
trajectory can introduce new primes.

Read [the proof and source comparison](PRIME_SUPPORT_PEAKS.md).

## 3. The exact depth-two obstruction to certificate transport

The classification and Mersenne reduction in this section also appear in
the refreshed PR146. Its general phase and rank results go further. The
independent derivation and literal complete-orbit separation here are useful
for checking that our proposed certificate route respects those limits.

All sources \(n\equiv1\pmod{16}\) whose first odd-event hitting depth is
exactly two are

\[
n_m=\frac{16\cdot64^m-7}{9},\qquad m\ge1.
\]

They satisfy \(U^2(n_m)=1\). Their one-sided partners \(z_m=2n_m-1\)
obey the exact reduction

\[
T^4(z_m)=2^{6m+1}-1.
\]

Moreover the entire known orbit of \(n_m\) lies below
\((8\cdot64^m-2)/3\), whereas the tripled arm remains strictly above this
bound through shortcut clock \(6m+4\). The separation allows any clock
on the known arm. Its first \(6m+2\) odd iterates also stay above 1.

Thus the source's odd-event stopping depth alone cannot bound a successful
target clock. This is an obstruction involving complete certified good
orbits, not a changing finite shadow presented as an infinite orbit.
It leaves height-dependent or recursively constructed certificates open.

Read [the classification and separation proof](DIRECTED_DEPTH_TWO.md).

A further [uniform high-exponent rigidity attempt](UNIFORM_J_ATTEMPT.md)
records the exact legal-input and height inequalities that prevented another
possible strengthening of the thin-family criterion.

## 4. Evidence and replay

The three author programs and two reviewer programs use exact integers and
rational arithmetic. A further root implementation reconstructs the
depth-two witnesses without importing author code. Each retained execution
has its scope recorded in the [review and execution overview](../../reports/2026-11-20-allhands/README.md).
Finite examples check the implementations; the universal statements rely on
the written arguments.

From a complete checkout:

    python -B research/allhands-global-closure-20261120/check_directed_circulation.py
    python -B research/allhands-global-closure-20261120/check_prime_support_peaks.py
    python -B research/allhands-global-closure-20261120/check_directed_depth.py

All three support optimized Python. The source pins and publication receipt
separate previously reported evidence from commands actually run here.
The accepted mathematical baseline and all other research branches are
unchanged.
