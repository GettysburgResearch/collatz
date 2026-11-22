# Actual-orbit phase, inverse windows, and whole-word closure attacks

**22 November 2026. Full Collatz remains open.** This checkpoint adds a
written power-law phase estimate for every supplied distinct ordinary
odd-orbit segment, its finite Lean core, and three attempts to turn the
latest repository results into a closing contradiction. No universal
descent, escape exclusion, or complete nontrivial-cycle exclusion is
claimed.

The work began at PR178 head
9d4ae09cd50ccd54036141edc3938d2cabe786fd. The
[source snapshot](SOURCE_SNAPSHOT.json) records all **145 available PRs:
122 open and 23 closed**, the main head, and the active input versions.
The main research map and catalog were read, and the current frontier
was examined in detail. Four peer branches advanced again during the
work and their new results were incorporated below. This is a broad
metadata survey with targeted proof work, not a claim to have re-proved
every contribution.

## Main outcomes

| Attack | Result established here | Closing step still missing |
|---|---|---|
| Actual leading phases and binary runs | Uniform discrepancy \(D_N\ll((1+\log N)/N)^{1/8.616}\), hence \(O(N^{-1/9})\); a growing run threshold proportional to \(\log N\); polynomial run moments. The finite exact-edge Fourier bound is checked in Lean. | A contradictory upper bound on the same actual weighted energy, or an arithmetic bridge to the actual ternary entropy law. |
| Canonical inverse windows of the same orbit | Relative entropy and total variation tend to zero uniformly over **all inverse window lengths**, retaining the original endpoints. Normalized real fibres converge to one common limit. | Identify the conditional kernel at the compact actual time limit; ordinary pointwise harmonicity does not supply that passage. |
| Actual high-spike sector | Combine the previously known finite-spine concentration with the new moving-fibre theorem to obtain uniform trace convergence across an entire fixed-height spike sector. | Preserve enough mass at the required sibling; the clock-dependent precision remains. |
| Entire source word with both merger clocks free | Exact arithmetic membership condition for a smaller-source merger, a necessary endpoint-residue coverage bound, and a complete finite control covering every smaller-source inverse clock. | Prove existence of a legal better word for every original joint counterquery. |

## 1. A power estimate on each actual segment

Let \(q_0,\ldots,q_N\) be positive integers satisfying the exact accelerated
edges
\[
2^{g_i}q_{i+1}=3q_i+1.
\]
Assume only that \(q_0,\ldots,q_{N-1}\) are distinct. Ordinary consecutive
odd states satisfy these hypotheses. Set
\[
\alpha=\log_2 3,\qquad
\theta_i=\{\log_2 q_i\},\qquad
\epsilon_i=\log_2(1+1/(3q_i)).
\]
The exact recurrence is
\[
\theta_{i+1}=\theta_i+\alpha+\epsilon_i\pmod1.
\]
Distinctness pays for the whole error budget:
\[
\sum_{i<N}\epsilon_i
\le\frac{H_N}{3\log2}
\le\frac{1+\log N}{3\log2}.
\]
There is no probabilistic parity model and no averaging over starting
integers.

For a continued-fraction denominator \(q\le N\) of \(\alpha\), the
rational-grid block argument gives
\[
D_N\le\frac4q+\frac{2qH_N}{3N\log2}+\frac qN.
\]
An elementary integer-power separation already yields an explicit
\(O(1/\log N)\) bound.

Rhin's published linear-form estimate, reproduced precisely in
Lagarias--Soundararajan's Lemma 5.3, equation (5.11), strengthens the
denominator growth to \(q'\le Cq^{7.616}\). Optimizing the same block
bound gives
\[
\boxed{
D_N\le C_R\left(\frac{1+\log N}{N}\right)^{1/8.616}
=O(N^{-1/9}).
}
\]
The constant is independent of the source and the starting position of
the window. A numerical value of the literature constant has not been
computed. The original Rhin chapter was not independently reconstructed;
the full-paper reproduction of the exact input was inspected by two
researchers. The separate stochastic theorem of Lagarias--Soundararajan
is not used.

Let \(R(n)\) count maximal one-runs in the binary expansion. For fixed
\(S\ge1\),
\[
\boxed{
\frac1N\#\{i<N:R(q_i)\le S\}
\ll_S N^{-1/9}(\log N)^{2S-1}.
}
\]
More strongly, for every \(0<c<1/4\), put
\[
S_N=\left\lfloor c\left\lfloor\frac{\log_2N}{9}\right\rfloor\right\rfloor.
\]
Then
\[
\boxed{
\frac1N\#\{i<N:R(q_i)\le S_N\}
\ll_c N^{-(1-H_2(2c))/9}.
}
\]
Thus, for every \(\rho>1\) and
\(0<\kappa<(\log_2\rho)/36\),
\[
\boxed{\frac1N\sum_{i<N}\rho^{R(q_i)}
\ge C_{\rho,\kappa}N^\kappa}
\]
eventually, uniformly over the supplied distinct windows.

[Full proof, exact finite constants, and comparisons](phase/EFFECTIVE_PHASE_AND_RUNS.md)

The newly advanced PR176 obtains an explicit \(O_S(N/\log N)\) count
using its ESS finite core, and a separate sparse-return descent on
arbitrary fixed logarithmic horizons. Our power estimate improves the
asymptotic occupation rate through a different literature input; it does
not supply the sparse endpoint return required for that descent theorem.
PR177's fixed-separation finite-core result also retains geometric
information absent from a phase distribution bound.

The qualified actual terminal-energy lower bound now grows at least
like \(N^\kappa\). The direct opposing-bound attempt still fails:
PR175's exact commutator and PR177's new finite-depth/time profile
retain the escape coefficient. Choosing a smaller finite Green depth
leaves the omitted tail with the surviving energy.

## 2. The exact ordinary-edge core is formalized

The new Lean theorem proves, for every integer frequency \(h\),
\[
\left|e^{2\pi i h\log_2 3}-1\right|
\left|\sum_{i<N}e^{2\pi i h\log_2q_i}\right|
\le 2+\frac{2\pi|h|}{3\log2}H_N.
\]
A second composed theorem replaces \(H_N\) by \(1+\log N\).
Both start from literal natural-number edge equalities, positivity, and
distinctness. The logarithmic recurrence and its complex phase
conversion are proved internally.

The module includes reciprocal rearrangement, the summed correction
budget, integer-frequency periodicity, and finite Fourier telescoping.
Its 12 public declarations are separately audited. The compiler checks
the finite core; continued fractions, Rhin's theorem, discrepancy,
binary-prefix counting, and the canonical-energy application remain
written mathematics.

[Lean source and reproducible build instructions](phase/lean/README.md) ·
[Execution scope and receipts](../../reports/2026-11-22-whole-repo-synthesis/README.md)

## 3. Remove the inverse-horizon restriction without changing the orbit

Under the pinned ordinary canonical inputs, let \(K_F\) be the actual
inverse kernel, \(a_i=K_F(q_i,q_{i-1})\), and
\(D_k=\prod_{i=1}^k a_i\). Exact telescoping gives \(D_k\downarrow D_\infty>0\).

Choose \(j\) uniformly from \(0,\ldots,L-1\). Compare the marked actual
reversed word from \(q_{j+m}\) to \(q_j\) with the actual canonical
inverse chain from the same marked starting vertex. Their laws satisfy
\[
\boxed{
\operatorname{KL}(P_{L,m}\Vert Q_{L,m})
\le b_L:=\frac1L\sum_{j<L}\log(D_j/D_\infty)\longrightarrow0,
}
\]
and \(\operatorname{TV}(P_{L,m},Q_{L,m})\le b_L\), **uniformly over every
\(m\)**, even when \(m\) is much larger than \(L\).

This couples the canonical endpoint ensemble to the same ordinary time
law whose entropy PR185 bounds. It transfers bounded observables and
normalized finite-resolution entropy. It does not control unbounded
moments without an additional tail bound.

A precise sufficient escape-closing criterion follows. If the actual
compact stationary law has a finite positive canonical density \(E\)
and the same transition formula
\[
k(x,e)=3\,2^{-e}E(I_ex)/E(x),
\]
then finite mean gap \(a\) implies
\[
H(e\mid x)=a\log2-\log3.
\]
With two positive branches this forces \(a>\log_2 3\), contradicting the
actual-orbit mean-gap bound. The proof handles the log-density
coboundary without assuming its integrability.

**The kernel identification is still unproved.** The new moving trace
recovers the ordinary spike at precision containing its original clock.
Weak convergence alone does not pass those values to a finite positive
density representative at the compact time limit.

The normalized real fibre does converge along the same ordinary orbit
to a common probability law, uniformly over later shifts. Testing this
limit against the already instantiated Kesten--Goldie tail gives only a
weaker orbit bound than the elementary edge bound. It does not remove
the growing ternary precision.

[Exact transfer, entropy criterion, fibre limit, and failed closing applications](entropy/CANONICAL_TIME_ENTROPY_ATTEMPT.md)

## 4. Put all high spikes under the moving trace theorem

For a fixed \(\eta>0\), the sector \(\{n:\nu(n)\ge\eta\}\) is covered by
finitely many actual forward spines. That finite-spine statement is
**credited prior PR185 work**, reconstructed here using finite-antichain
mass and contact. Combining it with PR175's new sourcewise moving-trace
theorem yields uniformity over the entire fixed-\(\eta\) sector.

The retained anchor clock still appears in the precision. The newest
PR175 payoff concentration theorem sharpens this issue: a witness with
\(V^{[r]}(q_k)\ge\eta q_k\) must have \(r\ge k-K_\eta\).
Its particular common-precision routing coefficient therefore remains
exponentially small in the original clock. This is consistent with our
all-horizon coupling: that coupling removes the future window length,
not the endpoint's remaining ancestral clock.

[Whole-sector deduction and direct sibling attempt](sibling/HIGH_SPIKE_SECTOR.md)

## 5. Change the entire source word and allow both clocks to vary

For target endpoint \(N=T^k(t)\), source length \(m\), and odd count \(h\),
the full-word correction set is
\[
\mathcal C_{m,h}=
\left\{\sum_{i=0}^{h-1}3^{h-1-i}2^{d_i}:
0\le d_0<\cdots<d_{h-1}<m\right\}.
\]
A smaller positive source exists at these clocks exactly when an
admissible \(C'\) supplies the required divisibility and interval:
\[
C'\equiv2^mN\pmod{3^h},\qquad
0<2^mN-C'<3^ht.
\]
The affine identity then forces each literal intermediate parity. This
retains the complete proposed word, the original target, and both
independent clocks.

The current source bounds make an alternative word with one extra odd
event especially powerful, but do not construct it. An unconditional
endpoint-residue coverage calculation also shows why a generic
all-residue high-odd word selector is too strong; no independence of
the actual endpoint is assumed.

One exact control makes the source-clock issue concrete. For \(t=1263\),
the maximal permitted source in the tested all-word grade is 820.
Every smaller start belongs to a checked 2,008-state forward-closed
set. This proves that **no smaller source at any inverse clock**
merges with target clocks 0 through 24. The first merger is at target
clock 25 and the first descent at 26. The target converges; this is a
control against a premature clock bound, not a Collatz counterexample.

The fresh logarithmic sparse-return theorem also gives a restriction on
a least bad target: for each fixed \(S,C\), at most \(|H_S|+1\) of its
first \(\lfloor C\log t\rfloor+1\) odd states can have at most \(S\) runs,
once \(t\) is sufficiently large. An elementary check shows that the
exceptional set already contains \(\{1,\ldots,2S\}\). Using the forward
run-growth estimate to choose a larger cutoff therefore makes the
tested separation exceptional; it does not supply the needed return.
The phase and sparse-return results give compatible scarcity bounds.

[Complete-word attempt and exact control](arithmetic/WHOLE_WORD_MERGER_ATTEMPT.md)

## Evidence and remaining objective

The written phase proof received independent reconstruction and final
transcription review. The entropy and sibling deductions received
scoped cross-review; their original analytic inputs remain qualified.
The arithmetic control is executable and is not being promoted as a
universal theorem.

The main positive advance is the uniform polynomial estimate on actual
distinct windows, with a substantial finite Lean core. The central
closing targets remain a successful original-target merger, a
source-preserving sibling lower bound, or identification of the actual
compact canonical kernel. Complete nontrivial-cycle exclusion is also
still required.

The [previous deep-machinery checkpoint](../deep-machinery-20261122/README.md)
and its evidence remain intact. The previous PR description is archived
in the [verification packet](../../reports/2026-11-22-whole-repo-synthesis/pr-description-before.json).
