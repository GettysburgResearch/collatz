# Independent review: finite collisions and growing resolution

Date: 23 November 2026. Reviewer: `rational_selector6`.
Parent checkpoint: `afe6f4d1a661b377c9daa4623bdd732ba478386b`.

## Frozen objects and verdict

| Path | Git blob | SHA-256 |
| --- | --- | --- |
| `research/profound-round6-20261123/COLLISION_CLOSURE.md` | `c03dda2fa13ba592515b4ca6bc93bbc6e4f81c65` | `056f6c0362c347e30c4277eabfceee18c8139988ffc0a7442d9ea080c331a8f9` |
| `research/profound-round6-20261123/CollisionClosure.lean` | `34b6773e3d9e00c9e35161be1107fdf647f032b0` | `7c6dd6ed0d61478afcc65bbc07dda2778677da46e0a112277a0570b4b64d44f0` |

**VERIFIED at the displayed contents:** the finite collision packing theorem,
the total-variation discrepancy inequality, the growing-scale lower bound,
the optimized conditional rate restriction, and the preservation of that
restriction under the stated finite-flow comparison. No correction to the
frozen science files is required.

This verdict concerns these claims and their explicit hypotheses. Imported
stationary lower bounds and the construction of the harmonic flow remain
**SOURCE-QUALIFIED**. It does not certify the literature packet wholesale,
a convergence rate for an actual orbit, an ordinary height upper, or Collatz.

## 1. Finite arithmetic and actual-source attachment

I read both complete files and reconstructed the pair injection. For a
finite set of ordinary naturals, equality of the first source and of the
second source's complete quotient, together with the collision residue,
recovers both original sources. Thus the injection keeps every ordered pair.
The uniform normalization is exactly the pair count divided by \(N^2\).
For \(Q>H_N\), only the ordinary diagonal remains.

The Lean declarations implement these same objects. In particular their
cardinality bound uses a set of the actual naturals, not residue
representatives or a list with silently deleted repetitions. The arithmetic
statement allowing \(Q=0\) causes no application gap: its proof uses the
valid natural division identity, and the analytical application always has
\(Q=3^m>0\).

The manuscript assumes distinct positive ordinary states explicitly. A
nonperiodic deterministic orbit supplies distinct states; a periodic orbit
does not satisfy this growing-prefix assumption. Hence this lane is an
escape constraint, not an exclusion of other positive cycles. For the
stationary application, the empirical laws must come from the same actual
prefixes and the same fixed source.

## 2. The growing-scale calculation

For finite probability vectors with total variation \(\varepsilon\),
the positive and negative masses of their difference both equal
\(\varepsilon\). Therefore
\(\|p-q\|_2^2\le2\varepsilon^2\), with the factor \(\sqrt2\) in the note
correct for its half-\(\ell^1\) normalization. Combining the reverse
triangle inequality with the finite packing upper gives equation (6),
including its positive part.

Hold the source, limiting law \(\mu\), and subsequence \(N_i\) fixed.
For each fixed \(\kappa>0\),

\[
N_i^\kappa/3<Q_i=3^{\lfloor\kappa\log_3N_i\rfloor}
\le N_i^\kappa.
\]

Thus the ratio of the packing upper to \(cQ_i^{-d}\) is bounded by a
constant times

\[
N_i^{\,\beta-1-\kappa(1-d)+o(1)}
+
N_i^{\,\kappa d-1}.
\]

Both exponents are strictly negative under equation (8). Its strictness
absorbs the height error \(o(1)\), and \(\kappa>0\) ensures that the
eventual stationary collision lower bound applies at \(m_i\to\infty\).
The finite discrepancy inequality then gives precisely

\[
\varepsilon_{N_i,m_i}
\ge(\sqrt{c/2}-o(1))Q_i^{-d/2}.
\]

No fixed-modulus limit is interchanged with this growing resolution.

For the optimized rate assertion (10), suppose first \(\gamma>0\).
Fix any

\[
0<\kappa<\frac{\min\{1,2\gamma\}}{d}.
\]

The claimed bound
\(\varepsilon_{N_i,m_i}\le N_i^{-\gamma+o(1)}\) is then
\(o(Q_i^{-d/2})\). The preceding obstruction forces
\(\beta\ge1+\kappa(1-d)\).
Taking the supremum of these already established inequalities gives
equation (10), including the endpoint \(\gamma=1/2\).
The errors and threshold indices may depend on the fixed \(\kappa\);
uniform convergence in \(\kappa\) is not needed.
If \(\gamma\le0\), the stated weaker inequality follows already from
\(H_N\ge N\) for distinct positive integers and therefore \(\beta\ge1\).

The geometric example is a conditional application of the displayed
collision lower, not a substitution of an iid process for the finite
ordinary source. The process-specific exponent in the general stationary
application is likewise not asserted to be uniform over all laws.

## 3. The finite-flow comparison does not estimate convergence to the limit

I additionally inspected these exact source files:

- PR178, head `c91b80a3156e640ad471cf30c47721145ae21eb1`,
  [FAST_EQUIVALENT_FLOW.md](https://github.com/GettysburgResearch/collatz/blob/c91b80a3156e640ad471cf30c47721145ae21eb1/research/central-step-20261123/stationary/FAST_EQUIVALENT_FLOW.md),
  blob `39ccf195e42ee17121ff856c45541e70e05d393f`, especially
  its component hypotheses and Section 4.
- PR180, head `7cfd911d35382d9d3bc988060ba88ade78a4267e`,
  [COLLISION_CORE.md](https://github.com/GettysburgResearch/collatz/blob/7cfd911d35382d9d3bc988060ba88ade78a4267e/research/whole-source-20261123/COLLISION_CORE.md),
  blob `d94a3c4153c7d02802f50bd3a1136c71f6936dca`, particularly
  the ordinary empirical source, stationary extraction, and limit order.

The first source's comparison is with exactly the unchanged ordinary
empirical law. Its \(O(1/N)\) constant is fixed after choosing the source and
flow, and is uniform in finite quotient and selected inverse clocks.
Flow existence and its supplied component hypotheses are retained.
Projection and the triangle inequality consequently justify equation (13).
Because \(\kappa d<1\), one has
\(N_i^{-1}=o(Q_i^{-d/2})\); hence the discrepancy obstruction survives.

Neither this comparison nor the stationary extraction supplies a modulus
of convergence to the fixed limiting law at \(m_i\asymp\log N_i\).
The note correctly preserves that unsupported step and does not infer
componentwise conditional mean bounds from the global stationary mean.

## Evidence boundary

This was an independent mathematical reconstruction and complete Lean
source inspection. I did not modify either frozen science file and did
not rerun its Lean build or the repository regression bundle. Fresh
compilation and axiom-audit receipts belong to the parent checkpoint's
execution report. The written total-variation and asymptotic arguments
are not represented as Lean-checked theorems.
