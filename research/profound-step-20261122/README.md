# Independent cycle blocks, ordinary spectral residues, and arbitrary carry

**Full Collatz remains OPEN.** This continuation of PR183 pursues the global
step through three complementary mechanisms suggested by primary literature:
ordinary repetition plus logarithmic forms; harmonic transport plus Wold's
decomposition; and an exact arbitrary-debt carry system feeding the existing
source-certificate induction. It starts from PR183 at
`907a540943090968bc683b1b9246208e9053c1f8`; current related sources are frozen
in [SOURCES.json](SOURCES.json).

The proof packet contains five new Lean modules with **52 public theorem
declarations**. The [execution report](../../reports/profound-step-20261122/README.md)
records their actual compilation and transitive axiom audit. That count is
an inventory of formal declarations, not a count of new historical results.
The larger infinite-sum and transcendence arguments are written proofs;
their exact hypotheses and independent reconstruction boundaries are kept
beside them.

## 1. Every fixed power-block cycle language has an effective classification

Fix any finite list of nonempty binary parity words `V1,...,Vr`. Allow all
their repetition counts to vary **independently**:

\[
W(\mathbf k)=V_1^{k_1}\cdots V_r^{k_r},\qquad k_i\ge0.
\]

The [arithmetic theorem](arithmetic/FREE_EXPONENT_CYCLES.md) gives a terminating
exact procedure that finds every primitive positive cycle represented by
this language and describes all accepted exponent tuples by a finite
semilinear description. It retains repeated traversals of a fixed cycle;
it does not falsely bound the supplied length of `(10)^k`.

The new finite ordinary core is stronger than a fixed-parameter calculation.
Suppose a prefix of **one actual source** `n` has length `N` and is a product
of `r` power blocks whose atoms have length at most `B`. Then either the
source already reaches a genuine cycle of period at most `B`, or

\[
\boxed{2^N\le(2^{2B}n)^{2^r-1},\qquad
N\le(2^r-1)(2B+\lfloor\log_2n\rfloor+1).}
\]

[`BlockCompression.lean`](arithmetic/BlockCompression.lean) proves this
dichotomy, including the exact fixed-block alternative and its application
to primitive cycles. It allows arbitrary independently chosen block lengths
and repetition counts within the displayed bound.

For a primitive cycle with minimum `m`, the complete-cycle identity and
Matveev's explicit theorem give a polynomial upper bound for `m` in its
period `N`. The repeated-block budget gives an exponential lower bound.
Comparing them gives a literal computable cutoff. The written proof includes
the missing boundary-minimum comparison, the primitive-root truncation, the
full cycle denominator, and the final finite automaton for exponent tuples.
The conservative constant is `K=2^33`; the cutoff is enormous and is used
to prove effectivity, not reported as an executed enumeration.

This uses the chaining-and-transcendence architecture of the classical
cycle literature, with credit to Simons--de Weger and their predecessors.
No historical priority claim is made. The global missing input would be a
strong enough repeated-word description for every unresolved orbit; the
forced band does not yet supply it.

## 2. The full original source has an exact all-clock boundary residue

The transport route uses the actual accelerated odd map `U`. It imports
PR185's **source-qualified** ordinary harmonic reference

\[
L\nu=\nu,\qquad \gamma/q\le\nu(q)\le A,
\]

on the positive odd ternary units not themselves periodic. `L` carries
unchanged masses and kills them on entering any periodic orbit. All analytic
population and envelope hypotheses of that reference remain explicit.

The source is the original full-support law `sum n^-4 delta_n`, projected
to its first odd ternary unit by an actual finite orbit map `pi(n)<=2n`.
Every source collision is retained. For its nonperiodic part `a`, put

\[
B_ra=\sum_{k\ge0}r^kL^ka,\qquad
\mathcal E_\nu(b)=\sum_q b(q)^2/\nu(q).
\]

The [all-clock theorem](transport/ASYNCHRONOUS_RESIDUE.md) proves

\[
\boxed{\lim_{r\uparrow1}(1-r^2)\mathcal E_\nu(B_ra)
=\lim_{J\to\infty}\frac1J
\mathcal E_\nu\!\left(\sum_{k<J}L^ka\right)
=\sum_{C\ \mathrm{escaping}}\frac{a(C)^2}{C_C}.}
\]

Here `C_C=lim_j nu(U^j x)` is the finite positive capacity of an ordinary
escaping component. Sources meeting after different clocks contribute their
full cross term. The proof treats all original source pairs, with the
summable domination `sum a(q)/sqrt(nu(q))<=7 sqrt(2/gamma)/5`. Both
renormalized energies are bounded by `98/(25 gamma)` at every clock or
discount. This bound does not make their positive limiting residue vanish.

The [operator theorem](operator/WOLD_CHANNELS.md) identifies the underlying
structure. The pullback is an isometry, and its unitary part is exactly

\[
\boxed{\bigoplus_{C\ \mathrm{escaping}}\ell^2(\mathbb Z,C_C).}
\]

Each integer coordinate is a genuine clock-lag class of mass `C_C`. Thus
there is one bilateral shift per escaping ordinary component. The note
gives its orthogonal projection and the complete boundary-frequency formula,
including a uniform full-source limit. [`ClockLags.lean`](operator/ClockLags.lean)
checks the finite meeting algebra; [`AsynchronousKernel.lean`](transport/AsynchronousKernel.lean)
checks the independent-clock geometric and overlap kernels and summability.

Nontrivial cycles are retained in a separate second-order pole. With the
map killed only at one, a hybrid reference equal to `nu` off cycles and one
on nontrivial cycles gives a boundary residue that is zero for full
convergence, finite and positive for escapes without nontrivial cycles,
and infinite if a nontrivial positive cycle exists. This exact trichotomy
states a cycle-sensitive zero-residue target. **Its vanishing is not proved.**

## 3. One total carry calculation for every positive debt exponent

The [carry theorem](mergers/ARBITRARY_DEBT.md) replaces a special-state
transition table by a general exact complement calculation. If an actual
source gap satisfies `3r+1=2^a u` and the positive target is represented by

\[
n+d=3^p r,\qquad p>0,
\]

define the auxiliary positive `3x-1` shortcut map

\[
S(b)=\begin{cases}b/2,&b\text{ even},\\(3b-1)/2,&b\text{ odd}.
\end{cases}
\]

Let `o_a(b)` count its odd inputs during the first `a` clocks. Then

\[
\boxed{T^a(n)+S^a(3^{p-1}+d)
=3^{p-1+o_a(3^{p-1}+d)}u.}
\]

This is a finite identity on actual nonnegative ordinary values; no
convergence of the auxiliary map is assumed. [`AffineCarry.lean`](mergers/AffineCarry.lean)
checks it for every gap and debt. [`CarryCapture.lean`](mergers/CarryCapture.lean)
composes it through every finite source prefix and plugs a funded interval
capture into the exact preexisting common-grade induction.

If the largest removed source gap is `m`, an initial even padding `e<m`
strictly lowers that same grade order while retaining the literal supplied
tail. The capture guard is the concrete inequality `3^q<=2^(e+1)` at the
computed endpoint. It is a guard to prove, not a premise silently inferred
from the transducer's totality.

The unbounded language `1 {2,3}* 2` now has a valid paid capture rule; it
need not consume the additional final gap one used by the previous rule.
A second exact family excludes a uniform intermediate debt bound, even for
initial segments of complete source certificates. For every `k>=1`, ordinary source and target
prefixes have a coefficient `3^(4k+2)` after `15k` clocks. Their source
word is `(100)^(5k)` and target word `(11100)^(3k)`. They are varying finite
ordinary witnesses, not an infinite ordinary counterexample. Their targets
also have direct ordinary descent after five clocks. Thus the family tests
the fixed-debt abstraction while leaving compatible direct-descent rules
available; it is not an obstruction to every combined strategy.

The [carry/compression comparison](arithmetic/CARRY_COMPRESSION_BRIDGE.md)
checks whether the two approaches close each other's gap. In this family
the growing source height pays exactly for the long repetition. For one
fixed source, its available binary precision limits such a run; controlling
debt across switches of repeated atoms remains unsupported.

## Verification and reproduction

The [report](../../reports/profound-step-20261122/README.md) records five new
module compilations, two byte-exact imported dependency bodies with module
export wrappers, and the combined 52-declaration axiom audit. Prior band and
literature modules are reused by checked source/artifact hashes rather than
recompiled. No existing workflow, access setting, or accepted claim status
is changed.

With the earlier builds available at the paths used in their successful
receipts:

```bash
python research/profound-step-20261122/check_lean.py \
  --lean /absolute/path/to/lean-4.34.1-linux/bin/lean \
  --mathlib /absolute/path/to/mathlib \
  --dependencies-output /absolute/path/to/prior-build \
  --literature-output /absolute/path/to/literature-build \
  --dependencies-receipt /absolute/path/to/dependency-replay.json \
  --literature-receipt /absolute/path/to/literature-replay.json \
  --output /absolute/path/to/profound-build \
  --receipt /absolute/path/to/profound-replay.json
```

The pinned toolchain is Lean4.34.1 with Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The earlier packet's
[build instructions](../literature-closing-20261121/README.md#primary-sources-replay-and-remaining-work)
produce the required prior artifacts from their preserved source files.

The complete theorem still needs a global arithmetic input: a sufficiently
strong fixed-source repetition principle, complete capture in the common
certificate induction, or the actual cycle-sensitive zero-residue estimate.
The present proofs establish the displayed structural results and preserve
these remaining assertions as open.
