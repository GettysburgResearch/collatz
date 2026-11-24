# Canonical windows, sharp carries, and cycle defect filters

**PROPOSED research checkpoint; Collatz remains open.** This packet continues
[PR188's scalar and cycle routes](../scalar-carry-cocycle-20261124/README.md).
Four GPT-6.2 Astra research lanes developed the actual-source carry proof,
canonical-window packing, cycle filters, and an independent synthesis. The
claims below distinguish compiled finite theorems, written analytic arguments,
and bounded numerical controls.

We use the positive odd map
$$
2^{a_i}q_{i+1}=3q_i+1,\qquad a_i=v_2(3q_i+1).
$$
The actual scalar is $h_i=\sum_{j\ge0}a_{i+j}/3^{j+1}$. Its centered
decomposition $h_i=c_i+f_i$, with $c_i\in\mathbb N$ and
$1/2<f_i\le3/2$, gives canonical digits
$b_i=3f_i-f_{i+1}\in\{1,2,3\}$ and the exact identity
$a_i+c_{i+1}=b_i+3c_i$. All logarithms below are natural unless marked.

## Strongest escape result

Put $B_n=\sum_{i<n}b_i$, $P_n=3^n/2^{B_n}$, and
$R_N=\max_{n\le N}P_n$. If an ordinary positive odd orbit is injective,
the written argument in [CANONICAL_WINDOWS.md](CANONICAL_WINDOWS.md) proves
$$
R_N\ge C(q_0)N^{g}(\log N)^{g/2-\log_3 4}
\quad\text{for every sufficiently large }N,
\qquad g=1.1385654599\ldots .
$$
Here $g=\log3/H_3$, where $H_3$ is the maximum entropy of a
distribution on $\{1,2,3\}$ with mean $\log_2 3$. More precisely, if
the infinite canonical word has factor entropy
$\kappa=\lim_m m^{-1}\log p_b(m)$, then
$$
\liminf_{N\to\infty}\frac{\log R_N}{\log N}
\ge\frac{\log3}{\min(\kappa,H_3)}.
$$
For $\kappa=0$, every fixed polynomial is eventually exceeded. This
holds for every canonical mean, and excludes an explicit irrational phase
with oscillating means that passes the earlier divergence and summability
conditions. At the limiting exponent the same proof forces a specific
independent ternary empirical law. These asymptotic claims have **written
proofs**, using the pinned upstream occupation/product bound.

The finite mechanism **is compiled in Lean for the actual ordinary source**:
if distinct $q_0,\ldots,q_N<3^m$, then
$$
N-m+1\le p_{b,N}(m)+(m+1)\#\{i\le N:c_i>0\}.
$$
A nonzero carry can contaminate at most $m+1$ closed windows. Every other
window is its literal physical gap word; equal words force congruent endpoints
modulo $3^m$, hence equal endpoints below the modulus. The proof derives
that congruence from the actual edge equations.

## Sharp same-source carry penalties

[STRICT_CARRY.md](STRICT_CARRY.md) strengthens the optimal carry exponent.
For an interval, let $A,B$ be its physical and canonical clock sums. Count
$J$ transitions other than $(c,d)=(0,0)$ or $d=3c+2$, and among
these count $D$ with $a>b$. Then the written product inequality is
$$
3^{A-B}\left(\frac{c_{\mathrm{end}}+1}{c_{\mathrm{start}}+1}\right)^2
\ge (4/3)^{J-D}(27/4)^D.
$$
There is no carry, reset, time, or gap bound. The constants are sharp on the
ordinary transitions $3\to5\to1$.

Lean verifies both local penalties, the interval product with $(4/3)^J$,
its specialization to the exact scalar of an ordinary odd source, and the
resulting finite physical prefix inequality with its exact correction
$\prod_{i<n}(1+1/(3q_i))$. It also proves that a tail has no strict
transitions exactly when all future physical gaps are at most three. The
combined two-factor product and its injective asymptotic consequence are
written arguments.

## Cycle results

[CYCLE_FILTERS.md](CYCLE_FILTERS.md) uses $p$ odd steps and $A$ total
shortcut steps. When $\gcd(A,p)=1$, normalize the discrepancies
$pd_i-Ai=r_i+pk_{r_i}$ at their minimum, and put
$F(X)=\sum_{r<p}2^{k_r}X^r$. For an integer cycle, the **entire**
denominator $D=2^A-3^p$ admits a root with
$x^p=2,\ x^A=3,\ F(x)=0\pmod D$.

| Written claim | Scope and qualification |
|---|---|
| CF1 | Every single interval of unit elevations is excluded at every period. |
| CF2 | Every unit-elevation progression of stride 1, 2, 3, or 4 is excluded, with no bound on its number of terms. |
| CF3 | Any nonzero annihilator obeys $D\le M(G)^{p/32}2^{67\deg G}$; in particular degree $\le p/100$ and coefficient sum $\le10$ are impossible. |
| CF4 | Equally spaced blocks of raised residues are excluded when their six distinct boundary exponents lie in $[0,p/4]$; the number of blocks is unbounded. |
| CF5 | Arbitrary elevation support in the first one million residue positions is excluded at every period. |
| CF6 | For each fixed $\epsilon,K>0$, sufficiently large coprime periods cannot admit a nonzero annihilator of degree $\le p^{1-\epsilon}$ and coefficient sum $\le p^K$. |
| CF7 | Without a coprimality restriction, every sufficiently large least-period cycle has a defect beyond $b^{1-\epsilon}$, where $b=p/\gcd(A,p)$. This uses a necessary principal denominator factor. |

The all-period exclusions use published lower bounds from Simons–de Weger,
including their stated historical verification input; that computation was
not replayed here. The effective asymptotic claims use Matveev's
arbitrary-coefficient two-logarithm bound and do **not** include an enumerated
finite remainder. All such dependencies and quantifiers appear beside the
proofs. Widely distributed profiles remain outside these conclusions.

[TRANSLATED_BANDS.md](TRANSLATED_BANDS.md) removes the origin restriction and
handles every clock gcd. For each fixed $0<\epsilon<1$, sufficiently large
least-period cycles cannot have all defects in **any** cyclic interval of
width $b^{1-\epsilon}$. The argument also permits a growing number of intervals
centered at $0,u,2u,\ldots,hu\pmod b$, with arbitrary stride and internal
patterns. A logarithmic-width refinement reaches
$b/(\log b)^C$ for each $C>\kappa_{\rm irr}$, allowing up to
$1+\lfloor(\log b)^\delta\rfloor$ such intervals for an effective $\delta>0$,
where $\kappa_{\rm irr}$ is a finite effective irrationality exponent for
$\log_2 3$.
The proof uses an auxiliary variable to eliminate the interval centers while
controlling both the degree and coefficient size of a nonzero polynomial.
These are effective sufficiently-large-period **written** results; no finite
remainder or universal support cover is asserted.

The new [NormCertificate.lean](NormCertificate.lean) proves full-modulus
divisibility of a monic quotient's norm from a common modular root. The modulus
need not be prime or squarefree. This formalizes the determinant and adjugate
mechanism retaining all prime powers. The analytic norm upper bounds,
resultant estimates, and full cycle family exclusions are written proofs.

## Formal coverage and reproduction

Lean version **4.34.1**, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

| Sources | Formal scope | Printed axiom audits |
|---|---|---:|
| [CarryCocycle.lean](../scalar-carry-cocycle-20261124/CarryCocycle.lean), [ResidueDefect.lean](../scalar-carry-cocycle-20261124/ResidueDefect.lean) | Repaired and compiled the two original PR188 finite kernels | 10 |
| [StrictCarry.lean](StrictCarry.lean), [DebitCarry.lean](DebitCarry.lean) | Sharp local penalties and finite interval product | 4 |
| [ActualCarry.lean](ActualCarry.lean), [ActualPrefix.lean](ActualPrefix.lean) | Actual scalar attachment, equality-tail criterion, physical prefix bound | 11 |
| [CanonicalWindows.lean](CanonicalWindows.lean), [ActualCanonicalWindows.lean](ActualCanonicalWindows.lean) | Endpoint congruence, finite packing, and literal ordinary-source specialization | 3 |
| [CycleDefectFilters.lean](CycleDefectFilters.lean) | Finite profile-order and filter identities and the dyadic margin | 6 |
| [NormCertificate.lean](NormCertificate.lean) | General determinant, algebraic norm, and binomial divisibility certificates | 7 |

The ten modules have 42 public theorem declarations, with 41 explicit axiom
reports (the remaining geometric-series lemma is used by the audited filter
theorems). The reports contain only `propext`, `Classical.choice`, and
`Quot.sound`, or subsets thereof. There are no `sorry` or `admit` proofs or
custom axioms in these sources. Compilation used one worker and warnings as
errors. The actual scalar dependency was freshly compiled from its exact
source, reproducing the previously imported object byte for byte.

[REPLAY.md](REPLAY.md) documents an isolated build of the complete local module
graph using [replay_lean.py](replay_lean.py). This fresh build was executed and
all eleven inputs passed; its complete [receipt](../../reports/astra-closure-20261124/isolated-lean-replay.json)
binds every input to its SHA-256. Original compiler outputs and
source identities are in [the report directory](../../reports/astra-closure-20261124/).
The three control scripts are independent finite sanity checks, not theorem
proofs. They ran identically under normal and optimized Python. Counts include
49,649 canonical windows, 25,155 feasible carry transitions, 25,437 ordinary
prefixes, 8,140 residue profiles, and 9,850 noncoprime positive-denominator
words; these sample counts are not a universal search.

## Frozen upstream inputs

These are the snapshots inspected for this checkpoint; selected proofs were
reconstructed rather than treating every neighboring claim as verified.

| PR | Full head | Role |
|---|---|---|
| 182 | `cbec52dde5bed390a693310dd04e911033ba0cc9` | Actual scalar source and R12 optimal carry / whole-orbit product inputs |
| 185 | `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d` | Earlier injective-segment packing interface |
| 187 | `099058f3f2602a48e109c964899f0a9a2a223338` | Finite-popcount-cap source recurrence route |
| 188 | `beed685ab713923191ae40c9559bf7400298d2d3` | Parent cocycle and full residue-norm construction |
| 189 | `a0be70b1ffa075cbc50755ac76036108c028d120` | Entropy and source-factor-complexity comparisons |
| 190 | `ba58227c5a047ff3859a148a5fdaac4fd1451e4c` | Primitive binary and Mahler route inspected as context |
| 191 | `37b3916633cd32a0c173b20bb18ec3a7ec290a63` | Noncoprime principal-component interface and two-sided packing |

The vendored [ActualScalar.lean](dependencies/ActualScalar.lean) is byte-for-byte
PR182 at the pinned head, path
`research/carry-tower-round10-20261123/ActualScalar.lean`, SHA-256
`5b0f035ad14624376ce722bfdff5d9d216b266a0d7066efc3715fcc19d37f4a9`.
Its source is unchanged from the earlier PR182 pin used in the original note.

## Exact remaining step

For escape, the new results give necessary **lower** expansion and complexity
conditions; no all-source upper bound yet contradicts them. For cycles, no
construction produces a suitably small nonzero annihilator for every possible
profile. Neither statement has been supplied as an axiom or hidden inside a
conditional formal theorem. These are the missing global implications.

[GLOBAL_BRIDGE.md](GLOBAL_BRIDGE.md) explains one precise failure of a possible
closing argument. There are expanding scripts at canonical phase $7/8$ that
attain every sharp carry penalty and have positive debit density. Every finite
prefix has positive ordinary witnesses, while a constructive diagonal script
has no single ordinary source realizing its whole word. This separates the
finite necessary conditions from the needed all-time arithmetic condition.
