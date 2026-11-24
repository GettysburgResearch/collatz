# Direct closure attempts through inverse trees, measures and ordinary transfer

**Collatz remains OPEN.** This continuation constructs a finite potential on
every ordinary input with a uniform debit away from a specified sparse reset
section, finds an optimal bounded correction for an ordinary transfer
operator, and resolves the previously open whole inverse-tree envelope
candidate by an actual increase. It does not prove descent at every reset,
decay of the ordinary atomic moment, or exclusion of every bad component.

The starting checkpoint is PR182 at
`f5e65dbad5eaf2a5f85cde8916e91fe6e5102e67`. Three GPT-6.2 Astra lanes worked
on a global rank, fixed-source arithmetic and actual band mergers. They
continued through failed first proposals and cross-reviewed the resulting
arguments. Current related source heads, prior overlap and external inputs
are pinned in [SOURCES.json](SOURCES.json).

Throughout, the shortcut map is

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

A valley starts at a positive odd input, takes all consecutive odd shortcut
steps and then all consecutive even steps, and ends at the next odd source.
For type \((a,b)\), its affine law is
\(2^{a+b}z=3^a y+3^a-2^a\).

## 1. A rank on every ordinary input, with the reset step exposed

For any proper nonnegative integer function \(F\) on the positive odd
integers, and any \(\epsilon,\eta>0\), we construct a finite atomless
measure of mass at most \(\eta\) whose valuation potential satisfies

\[
F(n)\le H_\mu(n):=\int v_2(n-r)\,d\mu(r)\le F(n)+\epsilon
\quad\text{for every positive odd }n.
\]

Both a singular continuous measure and an absolutely continuous measure
with an integrable density are possible. The construction uses localized
dyadic spikes with controlled leakage onto all earlier ordinary inputs.
It proves that diffuse representability itself is available. A global
uniform debit still requires a rank chosen independently of termination.
[Interpolation theorem and exact finite optimization](DIFFUSE_RANK.md).

We then choose such an \(F\) without assuming convergence. A finite actual
orbit search selects successively narrower ternary heads. Its image is one
decidable set of natural density zero: an output \(x\) can only come from
an input \(n\le x^2\), so membership is a finite search. Mark each odd
valley containing a selected output before its endpoint. The marked odd
set \(M\) also has density zero, and every ordinary orbit reaches it.

Let \(u\) be the first marked valley reached from \(y\), and \(\tau\)
the actual shortcut time to \(u\). The total computable function

\[
F(y)=\tau+u
\]

is proper, finite on **all** positive odd integers, and satisfies
\(F(y)=a+b+F(z)\) whenever \(y\notin M\). Applying interpolation with
\(\epsilon<1\) gives a single all-ordinary finite potential with debit
at least \(2-\epsilon\) on every unmarked valley. This includes a
hypothetical source outside the basin of 1. The remaining failure is an
actual reset: both 7 and 13 are marked and the valley \(7\to13\)
increases the constructed potential. A strict later return below each
marked source would close the proof; density zero does not establish that
return. [Total construction, bounds and reset example](SPARSE_RESET_MEASURE.md).

## 2. An optimal quarter shift for the ordinary moment

The exact identity

\[
T(n)+\tfrac14=\frac{3^{n\bmod2}}2\left(n+\tfrac12\right)
\]

balances the positive real correction on both parities. Define, for
\(1<s<2\), the inverse operator on \(\mathbf Z_3\)

\[
L_sg(x)=2^{-s}g(2x)+(3/2)^s
\mathbf1_{x\equiv2\pmod3}g((2x-1)/3).
\]

Its Haar mean contracts by
\(\lambda_s=2^{-s}(1+3^{s-1})<1\). The ordinary quantity needed instead is

\[
I_k(s)=\sum_{n\ge1}n^{-s}(L_s^k1)(n).
\]

With the centered weight \((n+1/4)^{-s}\), each atom moves along its own
actual shortcut and pays the factor
\(((n+1/4)/(n+1/2))^s\) at every step. The centered and uncentered moments
have the same liminf and limsup rates of their k-th roots.

Since all positive starts below 20 reach 1, a sufficient full closing
estimate, including every possible nontrivial cycle, is

\[
\liminf_{k\to\infty} I_k(3/2)^{1/k}
 <(81/82)^{3/2}=0.9817632\ldots.
\]

The Haar rate is \(\lambda_{3/2}=0.9659258\ldots\). No argument here
transfers this mean contraction to the ordinary atomic sum. The required
estimate remains open. The quarter correction is optimal for the uniform
additive defect among bounded real coordinate changes, even on the
predecessor basin of any one prescribed positive target prime to three.
[Balanced identity, minimax proof and exact missing estimate](QUARTER_SHIFT.md).

The ordinary trace reduces, up to an exponentially small tail, to one
least positive endpoint for each parity word. Its average displacement
from a complete binary grid is exponentially small, but the required
negative moment is singular at the grid's smallest points. A proposed
biased coupling fails: it leaves a positive fraction of count differences
unclosed at every horizon. Symmetrizing the coupling incurs an endpoint
factor that exactly restores the bias. These statements do not disprove
the desired first-moment bound. [Endpoint calculation](ORDINARY_MOMENT.md)
and [weighted coupling test](TILTED_COUPLING.md).

PR192 at `045be43632f274dd64faf15714e42cc8de27a2e9` already supplies an
overlapping odd-clock moment reduction, an exact shifted killed criterion
for all nonconvergers, and a fixed-ancestor obstruction to its Green
potential. Those reductions are credited there. Restoring the complete
real shift in the shortcut calculation likewise preserves the entire
weight of each fixed surviving source; it does not prove that such a
source exists or that its weight disappears.

## 3. The whole inverse-tree envelope really increases

Let \(R\) be the complete rational inverse-valley tree of \(-5\), and
write its reduced centers as \(-h/q\), with \(q\) a power of three.
The candidate from the previous checkpoint was

\[
E(n)=\sup_{-h/q\in R}\frac{2^{v_2(qn+h)}}h.
\]

We now prove \(E(31)\le18<128/7\le E(121)\), and \(31\to121\)
is one actual valley. The bound on 31 covers **every** center of the
infinite tree, using its first 30 physical decisions and a finite residual
box. Lean proves the strict inequality between the real suprema for the
operational negative-orbit definition of the tree. Exact rational Python
enumeration also determines

\[
E(31)=\frac{4294967296}{291622243},\qquad
E(121)=\frac{67108864}{2804503}.
\]

The repaired envelope
\(K_c(n)=\sup 2^{v_2(qn+h)}/(h+cqn)\), \(c>1\), is nonincreasing
under every actual valley. It has a strict comparison at each matched
center, but its supremum is identically one on the known basin of 1 and
is not attained there. Thus pointwise strict comparisons do not give a
well-founded strict rank.

The same tree supplies a different fixed-source criterion. With the
explicitly pinned orbit-count and high-floor product inputs, an odd
ordinary \(n\) escapes exactly when centers approach \(n\) dyadically
and \(-n\) in the reals. Two inverse branches give quantitative
approximations at both places. The resulting joint error fails to supply
the power gain needed for the cited Subspace Theorem contradiction.
[Full comparison, repairs and two-place construction](RESTRICTED_RANK.md).

## 4. Actual boundaries and the time needed for head mergers

For any binary coloring constant on ordinary Collatz components, an
adjacent color boundary has a unique persistent dyadic child. A whole
family of exact ordinary mergers forbids the binary suffixes
\(10(11)^s0\). All persistent real addresses therefore lie in a set of
Hausdorff dimension at most \(1/2\). Exact tripling and inverse-third
identities transfer oriented boundaries on specified levels. At other
levels new opposite boundaries can appear; signed cancellation does not
control the unsigned failures required for closure.
[Ordinary identities and the unresolved propagation](BOUNDARY_RAYS.md).

On PR197's head \([7X,8X)\), \(X=81^j\), the family
\(x=81m+64\) supplies at least a constant times \(X^{1-c}\) pairs
with no meeting at any independent clocks at most
\((1+b)\log_2 X\), whenever \(0<b<c<0.16\), for all sufficiently
large levels. The proof uses exact ordinary prefixes, one finite binary
exposure and a fixed two-logarithm lower bound. This prevents a short
physical search from establishing the \(o(X^{0.84})\) failure estimate.
Every such pair could still meet later. [Finite-clock theorem](CLOCK_WINDOW.md).

## Verification and scope

Five final Lean sources were copied into separate empty build directories
and compiled with pinned Lean 4.34.1 and Mathlib, with warnings treated as
errors. All 24 requested transitive axiom inventories passed and contain
only `propext`, `Classical.choice` and `Quot.sound` (or a subset). The four
exact finite controls passed in both normal and optimized Python.

| Lean source | What its statements check |
|---|---|
| `EnvelopeCertificate.lean` | General matched-prefix identity, infinite-tree tail control, finite box, root witnesses and the strict real supremum comparison |
| `NonlinearTransport.lean` | Strict general per-center nonlinear transport inequality with its affine hypothesis |
| `QuarterShift.lean` | Balanced shortcut identity and full finite product, odd and even runs, and convergence of all positive inputs below 20 |
| `FourTritDelay.lean` | Arbitrary odd runs and the exact two-arm four-trit family |
| `OrientedBoundary.lean` | Unique-child dichotomy, two oriented transfer identities and the unbounded forbidden-gap family |

**The diffuse-measure theorem, sparse-reset construction, analytic moment
estimates, minimax theorem, real-address geometry and asymptotic counting
arguments are written proofs, not Lean formalizations.** The two-place
escape equivalence additionally retains its source-qualified inputs. The
published verification floor below \(2^{71}\) is an external computation,
not one rerun in this checkpoint.

Replay with an already built pinned Mathlib checkout:

```sh
python -X utf8 -B research/high-variance-closure-20261124/checks/replay.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --mathlib /path/to/mathlib \
  --receipt /tmp/high-variance-closure-replay.json
```

The actual output, source hashes and independent reconstruction record are
in `reports/2026-11-24-high-variance-closure/`. The complete-checkout
validator checks repository integrity separately. No declaration or
receipt asserts that Collatz has been settled.
