# One changed odd edge splits the critical collision mass

**PROPOSED, SOURCE-QUALIFIED calibration theorem.** This note changes the map. It proves no counterexample for the genuine Collatz map and no lower bound of one-eighth for that map. Its purpose is to test which inputs can actually determine that endpoint.

Let \(T(2n)=n\), \(T(2n+1)=3n+2\), on positive ordinary integers. Define
\[
 U(5)=10,\qquad U(n)=T(n)\quad(n\ne5).                                \tag{1}
\]
Thus only one odd edge changes; even halving remains exact everywhere. Let
\(B=\{n:T^t n=1\text{ for some }t\}\) and
\(A=\{n:T^t n=5\text{ for some }t\}\).
Their natural densities are denoted \(b\) and \(h\), respectively.

The following statements hold, with the analytic inputs specified below.

1. The new cycle is \(5\leftrightarrow10\), with basin **exactly** \(A\). The old cycle \(1\leftrightarrow2\) has basin \(B\setminus A\). All other components are unchanged. Both displayed basins have positive density.
2. For every positive source and every date,
   \[
       |\log U^t n-\log T^t n|\le\log10.                              \tag{2}
   \]
   If the source is changed at all, its two trajectories agree through exactly four steps before the genuine \(T\)-minimum time. The first-minimum times for the two maps differ by either four or five; otherwise they agree.
3. The complete normalized Brownian descent and its independence from the actual minimum survive, including the fixed arithmetic-progression versions. The same is true of the Gaussian first-minimum clock. This follows from an everywhere bounded change to the path and clock, together with the original terminal-label theorem, not from a claim that the actual minimum labels remain identical.
4. At
   \[
    H_X=\lfloor\mu\log X+\sigma u\sqrt{\log X}\rfloor,
    \quad \mu=2/\log(4/3),\quad
    \sigma^2=2(\log3)^2/\log^3(4/3),
   \]
   the two-independent-source collision limits satisfy
   \[
      L_U(u)=L_T(u)-\Phi(u)^2 h(b-h).                                 \tag{3}
   \]
   In particular
   \[
      L_U(0)=L_T(0)-\frac{h(b-h)}4<\frac18.                            \tag{4}
   \]
5. For every prescribed finite branch table \([1,R]\), one may instead change a single odd edge strictly above \(R\), with the same conclusions after replacing the fixed constants in (2) and in the clock comparison by constants depending on that edge.

Thus even **pointwise bounded all-time log-height error**, a bounded first-minimum clock error, and preservation of any prescribed finite branch table do not determine the one-eighth endpoint. The exact odd equation at every integer remains necessary for an argument using these data.

## 1. The actual orbit classification

Before a path first reaches 5 the two maps are identical. If it never reaches 5 under one map, it never does under the other: an alleged first visit is preceded only by equal edges. Upon its first visit under \(U\), it stays on the two-cycle \(5,10\). The converse is also exact, since a visit to 10 is followed by 5 under both maps. This proves the new basin is \(A\).

The genuine tail of 5 is
\[
                     5\longmapsto8\longmapsto4\longmapsto2\longmapsto1.
\]
Hence \(A\subset B\). Sources outside \(A\) retain their entire genuine trajectory, proving the remaining component statements. If \(a(n)\) is the first genuine date at 5, then the first date at 1 is exactly
\[
                         \tau_T(n)=a(n)+4.                            \tag{5}
\]
There cannot have been an earlier visit to 1, since its genuine cycle never visits 5. Up to date \(a(n)\), the paths agree. At the next date their values are 8 and 10, so this is their first actual discrepancy.

After date \(a(n)\), both paths remain in \([1,10]\). Before that they agree. This proves (2) for **all** dates, including arbitrarily late dates after either minimum. More exactly, for all \(t\ge\tau_T(n)\),
\[
                              U^t n=5T^t n.                            \tag{6}
\]
Both sides are at 5 at date \(\tau_T(n)\), and thereafter alternate between 5 and 10. In particular the parity tapes agree again forever from the genuine first-1 date onward.

On a source in \(A\), the only possible \(U\)-minimum below 5 is 3: the genuine futures of 1, 2 and 4 do not reach 5. If 3 occurs, it is immediately followed by the first 5, and the \(U\)-minimum clock is \(a(n)-1\). Otherwise its minimum is 5 at date \(a(n)\). Thus
\[
                  \tau_T(n)-\tau_U(n)\in\{4,5\}\quad(n\in A).         \tag{7}
\]
The sources visiting 3 form precisely \(\{3\cdot2^j:j\ge0\}\), since an odd shortcut departure is never divisible by three. This set has natural density zero. Consequently the new minimum law splits the old atom at 1 into mass \(b-h\) at 1 and mass \(h\) at 5; its possible atom at 3 has mass zero. All other minimum masses are unchanged.

## 2. The two positive masses are unconditional on Collatz

The density \(h\) exists by the genuine fixed-target natural-density theorem and is positive by Mazur's positive-predecessor theorem, applied to the ordinary target 10 to obtain shortcut predecessors of 5. Similarly \(85\) is prime to three and its genuine tail is
\[
                    85\longmapsto128\longmapsto64\longmapsto\cdots\longmapsto1.
\]
It avoids 5. Its whole predecessor set is disjoint from \(A\): an orbit visiting 5 can only follow the displayed genuine 5-tail afterwards, and cannot subsequently visit 85. Thus
\[
                          b-h\ge h_T(85)>0.                           \tag{8}
\]
The full-map target used for this second positivity assertion is 170. No hypothesis that all other integers converge has been inserted.

The imported results and map conversion are [Mazur, Theorem 1.1 and equation (1.3)](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf) and [Leen, fixed-target and terminal-label theorems](https://doi.org/10.5281/zenodo.23269488). The original Leen TeX inspected here has SHA-256 `211bc4fe107b3821e510486be28cf53f69751f71394582822faf385d09561e37`. The proof uses their written analytic statements; their validation status is not enlarged by this construction.

The positive-density split using visits to 5 and the complementary predecessors of 85 is already used in [Lean Assurance Lab, Paper 212, November 23](https://rstation.ai/problems/collatz/papers/212/v1), and its directed refinement [Paper 225, November 25](https://rstation.ai/problems/collatz/papers/225/v1). That terminal-label device is prior work. The claims evaluated here are the explicit changed maps, their all-time and passage-clock comparisons, and the resulting exact collision-coefficient losses.

## 3. Why the full stopped-path laws persist

Use the finite terminal label
\[
 \zeta(n)=\begin{cases}m_U(n),&n\in A,\\0,&n\notin A.\end{cases}
\]
Its values lie in \(\{0,3,5\}\). If \(n>5\) lies in \(A\), its future reaches 5, so deleting its initial value does not change its minimum. Outside \(A\) the label is zero and membership is unchanged by \(T\), except at the edited source itself. Consequently \(\zeta(Tn)=\zeta(n)\) for every \(n>5\). Also \(\zeta(2m)=\zeta(m)\) for every positive \(m\), by exact even halving and preservation of the first-hit set. For the ordinary full map \(C\), an odd departure satisfies \(C(n)=2T(n)\), so \(\zeta(C(n))=\zeta(n)\) for every \(n>5\). This verifies the **full-map** terminal-label hypothesis in Leen's theorem.

Leen supplies joint Brownian independence from \((m_T,\zeta)\). The new actual minimum is exactly the function
\[
 m_U(n)=\begin{cases}\zeta(n),&\zeta(n)>0,\\m_T(n),&\zeta(n)=0.\end{cases}
\]
Thus it too is independent of the limiting Brownian descent, jointly with its distribution and with every fixed source residue. The actual minimum \(m_U\) itself need not be invariant above 5 on a hypothetical escaping component; the finite label just constructed is the required input. No such invariance is assumed.

For the **entire passage-clock process** in Leen's main theorem, use a direct first-passage comparison. The paths agree through \(\tau_U\), and \(0\le\tau_T-\tau_U\le5\). For any height threshold, if a first passage occurs before \(\tau_U\), it is common to both paths. Otherwise the \(U\)-clock is capped at \(\tau_U\) and the capped \(T\)-clock lies between \(\tau_U\) and \(\tau_T\). Hence the two capped first-passage clocks differ by at most five, **uniformly over all thresholds**. In particular, for thresholds \(n^{1-s}\), \(0\le s\le1\), their centered normalized processes differ in supremum norm by at most \(5/(\sigma\sqrt{\log n})\). This proves transfer of the complete Brownian first-passage limit. Bounded log-height error alone would not justify an inverse passage-clock comparison.

For the physical height paths, (2) separately bounds their difference at every common native date. Reparametrizing by the respective first-minimum clocks changes indices by at most five, by (7). Each one-step log-height change has magnitude at most \(\log2\), under either map. Thus their centered, interpolated, time-rescaled height paths differ by an absolute constant before normalization by \(\sqrt{\log n}\). The claimed joint limits follow from the original terminal-data theorem and these deterministic comparisons.

This statement concerns the full Brownian weak limit and Gaussian clock, with genuine \(U\)-minimum semantics. It does not assert that every exact integer orbit statistic, minimum value, finite-clock merger, or ordinary branch equation is unchanged.

## 4. The exact change in the limiting collision statistic

The genuine formula at the frozen prior packet is
\[
 L_T(u)=\Phi(u)^2\left(\frac{b^2}{2}
                 +\sum_{C\ne\{1,2\}}\frac{d_C^2}{P_C}\right).         \tag{9}
\]
The source-qualified proof is [PR #214, synchronous phase dispersion](../../astra-critical-rigidity-20261128/ordinary/SYNCHRONOUS_PHASE_DISPERSION.md), pinned at `504d29d399efa941a62006d1ea4635385ce6bb5f`. Its inputs also apply to \(U\), with the following direct checks.

- Exact even halving is unchanged. The odd triple-phase identity fails at at most finitely many source values, so its empirical total-variation error still tends to zero.
- Density-one neighboring fusion is inherited. Fix a native clock \(t\). For all starts \(n>2^t5+1\), neither arm can reach the edited source before that date, since every step under either map is at least a halving. Every genuine successful fusion cylinder is therefore a \(U\)-fusion there. First let the sampling cutoff grow and then let \(t\) grow.
- There are finitely many cycles below every fixed period cutoff: apart from the new two-cycle, they are genuine \(T\)-cycles. The full component densities are exactly the split and unchanged masses identified above.
- The proper minimum law and its independent Gaussian clock hold by the preceding section. Fixed cycle-entry clocks differ from the corresponding minimum clocks by a tight amount, by the same finite-minimum truncation used in the genuine proof.

Consequently the same short-period / long-period phase decomposition gives
\[
 L_U(u)=\Phi(u)^2\left(\frac{(b-h)^2+h^2}{2}
                 +\sum_{C\ne\{1,2\}}\frac{d_C^2}{P_C}\right).         \tag{10}
\]
Subtracting (10) from (9) proves (3). At the median \(\Phi(0)^2=1/4\), and (8) gives the strict loss in (4).

This is a limiting identity, not a finite-date monotonicity claim. The changed cycle can make some within-\(A\) pairs merge a few dates earlier. Those pairs lie in a bounded-width entry-time window at the comparison date, whose normalized population tends to zero by the continuous clock law.

## 5. Protecting any finite branch table with one edit

Let \(k\ge2\) be an integer not divisible by three, and set
\[
                  q=q_k=\frac{4^k-1}{3}=1+4+\cdots+4^{k-1}.
\]
Then \(q\) is positive and odd, \(q\equiv k\pmod3\), and its genuine first-1 clock is exactly \(2k\): its first step is \(2^{2k-1}\), followed by halvings. Define
\[
                  U_q(q)=2q,\qquad U_q(n)=T(n)\ (n\ne q).
\]
The same first-hit argument makes its new two-cycle basin exactly \(\operatorname{Pred}_T(q)\). For all positive sources and all dates,
\[
                 |\log U_q^t n-\log T^t n|\le\log(2q).               \tag{11}
\]
On a changed source, the first discrepancy is one date after the first genuine visit to \(q\), equivalently at \(\tau_T-2k+1\). At every date at or after \(\tau_T\),
\[
                              U_q^t n=qT^t n.                         \tag{12}
\]
The exponent \(2k\) is even, which supplies the stated cycle phase in (12).

The earlier first minimum needs a separate bound. Let \(M_q\) be the maximum first-hit time to \(q\) among those finitely many integers \(1\le v\le q\) which actually reach \(q\). The set is nonempty, as it contains \(q\), and each included time is finite by its definition. If a changed source has \(U_q\)-minimum \(v\), that minimum occurs by its first visit to \(q\), so
\[
                      2k\le\tau_T-\tau_{U_q}\le2k+M_q.               \tag{13}
\]
No uniform or explicit bound for \(M_q\) is assumed. For each fixed \(q\) it is a fixed finite constant, which is exactly what the limit comparison needs.
The paths agree through \(\tau_{U_q}\), so the same capped-passage argument gives a uniform threshold-clock difference at most \(2k+M_q\).

For the terminal-law transfer define \(\zeta_q=m_{U_q}\) on \(\operatorname{Pred}_T(q)\), and zero elsewhere. It takes values in \(\{0,1,\ldots,q\}\), is invariant under \(T\) above \(q\), and satisfies \(\zeta_q(2m)=\zeta_q(m)\). Hence it is invariant under the ordinary full map above \(q\). The pair \((m_T,\zeta_q)\) reconstructs \(m_{U_q}\) exactly, as in Section 3. This establishes the needed joint independence for the general edit as well.

Choose \(q_\ell>q_k\) with \(3\nmid\ell\). Its genuine tail contains only itself and powers of two, so it avoids the odd \(q_k>1\). Its predecessor density is positive and supplies the nonzero complementary mass just as 85 did above. With \(h_q=d(\operatorname{Pred}_T(q))\), the same collision calculation gives
\[
                    L_{U_q}(0)=L_T(0)-h_q(b-h_q)/4<1/8.               \tag{14}
\]
Finally, choose \(k\) large enough that \(q_k>R\). Then \(U_q\) agrees with \(T\) on the entire prescribed table \([1,R]\) and at every integer outside the single edited source.

## 6. A one-unit edit also lowers the critical collision mass

There is an even smaller local perturbation, although this paragraph does not place it above an arbitrary prescribed table. Define
\[
 V(5)=9=T(5)+1,\qquad V(n)=T(n)\quad(n\ne5).
\]
Its new cycle is the following least-period-ten cycle:
\[
 5\to9\to14\to7\to11\to17\to26\to13\to20\to10\to5.
\]
The ten listed states are distinct, every arrow is the actual shortcut arrow except the edited first arrow, and each listed state genuinely reaches 5 under \(T\). The first-hit argument therefore gives new-cycle basin exactly \(A\), old two-cycle basin \(B\setminus A\), and unchanged remaining components. The cycle minimum is 5. The first-minimum comparison (7) remains exact, and for all sources and all dates
\[
                  |\log V^t n-\log T^t n|\le\log26.
\]
The finite terminal-label construction and path comparison apply unchanged, so the full Brownian descent, its independence from the actual new minimum, and the Gaussian clock all persist. The phase argument of Section 4 applies with the new period ten, yielding
\[
 \begin{split}
 L_V(u)&=\Phi(u)^2\left(\frac{(b-h)^2}{2}+\frac{h^2}{10}
                 +\sum_{C\ne\{1,2\}}\frac{d_C^2}{P_C}\right)\\
       &=L_T(u)-\Phi(u)^2h\left(b-\frac35h\right),\\
 L_V(0)&=L_T(0)-\frac{h(b-3h/5)}4<\frac18.
 \end{split}
\]
Here strictness already follows from \(h>0\) and \(b\ge h\). This is a **single-unit error at one odd input**, with pointwise bounded all-time log-height and first-minimum errors. Unlike the two-cycle edits, this ten-cycle edit does not have eventual equality of the two parity tapes. No arbitrary-table or infinite-family claim for unit-sized edits is made.

## 7. Finite formal kernel and its boundary

[SingleEdgeSplit.lean](SingleEdgeSplit.lean) states the actual shortcut formula locally and defines both edited maps. Its fifteen public roots cover unchanged branches, exact even halving, generic prefix preservation before the edited vertex, equality of the genuine and modified first-hit sets, the two-cycle and its exact phase scaling, the genuine five-tail, eventual factor-five rescaling, preservation of a prescribed finite branch table, and the unit edit's least period ten. They were freshly compiled and then imported into a separate complete root/axiom audit using Lean 4.34.1 and pinned Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. The only reported axioms are `Classical.choice`, `Quot.sound`, and `propext`.

The [receipt](../../../reports/astra-collision-factor-bridge-20261128/collision/single-edge-lean.json) and [runner](check_single_edge.py) record the exact source and toolchain hashes. Cached pinned dependencies were reused; this is not a cold dependency build or an independent LeanChecker replay. The infinite-density, complete passage-clock, minimum-law and limiting-collision claims remain written and source-qualified. Their independent review is [recorded separately](../../../reports/astra-collision-factor-bridge-20261128/arithmetic/one-edge-split-independent-review.json).

## Remaining positive task

The one-eighth lower bound must use an exact ordinary arithmetic property that excludes this single-edge split. Complete Brownian descent, bounded path and clock perturbations, density-one local fusion, and any fixed finite verification table do not supply that exclusion. The [dyadic boundary route](DYADIC_BOUNDARY_ZERO_ONE.md) still asks for a summable bound on the **actual, unmodified** component boundary. No such odd-edge estimate is derived from this calibration.
