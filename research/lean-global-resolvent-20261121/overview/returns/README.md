# Effective sparse returns and logarithmic-horizon descent

**Checkpoint 13. PROPOSED research with independently reviewed written
proofs and a finite Lean core. Full Collatz remains OPEN.**

This continuation gives two positive estimates on actual positive integer
orbits. It builds on PR177's S-unit return theorem and uses a second primary
theorem of Evertse to force descent on logarithmic horizons. Three parallel
lanes pursued orbit entropy and return arithmetic, the critical sibling
comparison, and whole-source word exchange. The root developed and checked
the second literature application. The source-sensitive lane independently
reconstructed both positive proofs.

Use the accelerated odd map
\(U(n)=(3n+1)/2^{v_2(3n+1)}\). Let \(R(n)\) count maximal runs of ones in
the ordinary binary expansion. All orbits and descendants below are ordinary
positive integers, with unrestricted individual valuation gaps.

## 1. An effective occupation bound, uniform over the source

For every fixed \(S\ge1\), every injective actual segment
\(q_0,\ldots,q_{N-1}\) satisfies

\[
\boxed{\#\{i<N:R(q_i)\le S\}
\le16(12S+3)(B_S+2)\frac{N}{\log_2N}}
\quad\text{if }N\ge2^{64(S+1)^2}.
\]

Here \(B_S\) is the cardinality of the fixed exceptional-separation set
from PR177. An explicit computable upper bound for \(B_S\) is given in
[the complete proof](EFFECTIVE_RUN_OCCUPATION.md). It comes from the
Evertse–Schlickewei–Schmidt solution-count theorem. The constants are very
large. The conclusion is an effective theorem, not a practical orbit test.

The new arithmetic step replaces an unknown S-unit ratio height by

\[
\boxed{M_0(S,h)=6^h2^{4S(4S+3h)}}.
\]

If both endpoints have at most \(S\) runs and their separation
\(h\notin H_S\), the same actual connecting segment has an odd input below
this explicit core. The local reason is useful beyond the final rate:
in a selected nondegenerate zero relation, every adjacent binary-exponent
gap is bounded by the coefficient height. From the last correction term
to the selected initial endpoint there are at most \(4S\) endpoint terms.
Only those gaps need to be paid. The logarithm of the core is therefore
linear in \(h\) for fixed \(S\).

Partitioning a length-\(N\) injective segment into blocks of length \(L\)
gives the more flexible finite inequality

\[
\#\{i<N:R(q_i)\le S\}
\le(B_S+1)(N/L+1)+L2^{16S^2+(12S+3)L}.
\]

Distinct-state visits below the core contaminate only finitely many blocks.
In every other block, differences from the first low-run time lie in
\(H_S\), so at most \(B_S+1\) such times occur. This uses the **number** of
exceptional differences, never their unknown maximum. Optimizing \(L\)
proves the displayed \(N/\log N\) rate, uniformly in source and window
position. It applies to every segment of an escaping orbit and to injective
prefixes of terminating orbits. Repeated periodic windows are outside its
injectivity hypothesis.

## 2. Sparse returns on any fixed logarithmic horizon force a power descent

For the same fixed \(S\) and the same exceptional set \(H_S\), fix
\(C_0>0\) and \(0<\eta\le1\). For all sufficiently large \(n\), an actual
segment \(x_0=n,\ldots,x_h\) with

\[
R(n),R(x_h)\le S,\qquad 1\le h\le C_0\log n,\qquad h\notin H_S
\]

satisfies

\[
\boxed{\min_{0\le i<h}x_i<n^\eta.}
\]

At \(\eta=1\) this forces strict descent below the starting integer.
For \(\eta<1\) it forces a power saving. No injectivity assumption is
needed. [The complete proof](LOGARITHMIC_SPARSE_RETURN_DESCENT.md) applies
Evertse's 1984 small-sum theorem to the endpoint-only signed S-unit sum.
Its dimension is at most \(4S\), even though the time horizon grows.
The exact positive correction is simultaneously bounded above by the
ordinary product identity under the contrary floor assumption.

The onset of this second theorem is not claimed effective. The first
theorem's elementary core already gives an effective version for a
restricted logarithmic multiplier depending on \(S,\eta\); the second
theorem reaches **every fixed multiplier** \(C_0\).

## 3. What the repo-wide view changes

The [source snapshot](../../../../reports/2026-11-22-effective-sparse-returns/repository-snapshot.json)
records 145 PR metadata entries and twelve selected exact heads. The
research map, scoped errata and the latest relevant proofs were read.
This is a survey plus targeted proof reading, not independent verification
of every historical claim.

The positive estimates extend PR177's qualitative return sparsity to a
uniform finite modulus and actual power descent. PR185's actual-orbit
entropy ceiling does not turn large binary-run count into a contradiction:
binary-run count and time-law metric entropy are different quantities.

The mandatory band remains useful but does not yet supply the hypothesis
needed in Section 2. Its condition
\((d+1)(n-2^d)\le70\,2^d\) leaves arbitrarily complicated lower binary
digits. A fixed run cutoff and an adequately timed return must still be
proved; they cannot be inferred from closeness to a power of two.

On the analytic side, PR175 now evaluates the truncated run-weight
commutator and retains its escaping-component charge. Finite canonical
forcing therefore does not by itself give the required uniform terminal
moment bound. The new occupation estimate supplies a uniform finite-time
input for that question; it does not supply the missing upper estimate.

Two direct closing attempts are preserved separately from the positive
results:

- [Actual stopping-tree transport](STOPPING_TREE_TRANSPORT_ATTEMPT.md)
  derives the signed repair cost under the normalized **actual optimal
  leaf law**. An adequate mean repair bound remains unproved. Replacing
  that law with independent geometric gaps would change the problem.
- [Whole-source debt and word exchange](WHOLE_SOURCE_DEBT_ATTEMPT.md)
  retains every parity disagreement. The concrete target \(3711\) does
  not descend by either completion clock of its extremal capturing
  source, but descends at clock 37. This rules out that proposed stronger
  horizon bound. A universally legal changed word must still preserve
  both endpoint divisibility and the original source grade.

The surviving full-problem targets remain an actual universal
grade-funded descent/exchange, or a canonical sibling/terminal estimate
that excludes escape together with a separate nontrivial-cycle argument.
No universal successful selector or such global estimate is asserted here.

## 4. Exact Lean and review scope

[DyadicCluster.lean](lean/Collatz/DyadicCluster.lean) has fourteen audited
finite statements. They prove the dyadic gap and local interval bounds,
the endpoint-count distance bound, the correction denominator, its
finite-floor descent consequence from a supplied correction estimate,
and the finite exceptional-difference cardinality bound.

The actual signed endpoint expansion, selection and sorting of a minimal
cluster, the ordinary correction identity, block decomposition,
logarithmic optimization and the two deep published inputs remain written
mathematics. They are not installed as axioms. The logarithmic-horizon
power-descent theorem is also a written result.

The [execution and review report](../../../../reports/2026-11-22-effective-sparse-returns/README.md)
pins the reviewed files and records the focused replay. Reproduce the
finite Lean core with the exact Lean/Mathlib versions in
[DEPENDENCIES.json](DEPENDENCIES.json):

```sh
python3 check_returns.py --lean /path/to/lean --mathlib /path/to/mathlib4 \
  --out /tmp/collatz-returns-fresh --receipt /tmp/collatz-returns-replay.json
```

The output directory must initially be absent or empty. The driver rebuilds
the new proof module and its audit, verifies all fourteen kernel dependency
reports, and rejects nonstandard axioms. It does not recompile the older
project checkpoints or claim to formalize the deep literature theorems.
