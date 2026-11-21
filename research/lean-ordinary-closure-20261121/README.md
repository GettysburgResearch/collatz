# Ordinary closure in Lean, and a selected-block predecessor bridge

**Status: Collatz remains OPEN in this packet.** The all-source attack is an actual simultaneous proof search, backed by a Lean kernel checker. Its successful rules are infinite arithmetic-progression rules, but the search has not produced a complete cover. Separately, a written analytic argument derives a uniform Syracuse atom floor and positive lower logarithmic predecessor density from Tao's published mixing theorem. The analytic argument is not a kernel-checked Lean theorem.

## 1. The global proof search

Write `Basin n` for reaching 1 under the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

The target comparisons are

\[
C_3(n):\;\operatorname{Basin}(n)\leftrightarrow\operatorname{Basin}(3n),
\qquad
C_5(n):\;\operatorname{Basin}(n)\leftrightarrow\operatorname{Basin}(5n).
\]

Use one joint natural-number rank, `8n` for `C₃(n)` and `5n` for `C₅(n)`. A search state is a whole affine progression `a t+b`, with **every** `t >= 0` in scope. Two search fronts start at `n` and `pn`. They may use ordinary doubling, halving, odd steps and inverse odd steps, and previously established multiplier comparisons. Every multiplier query at `u=a t+b` must satisfy

\[
w_q a\le w_p M,\qquad 0<w_q b<w_p r,
\]

for the root `n=M t+r`, together with positivity. These inequalities imply strict rank decrease for every parameter. Paths need not have equal clocks, equal odd counts, or matching intermediate states. Their endpoints must be exactly equal as affine forms.

[`lean/Collatz/JointDescent.lean`](lean/Collatz/JointDescent.lean) proves:

- `certificate_sound`: every accepted certificate is a valid whole-progression comparison, **under its explicit lower-rank comparison hypotheses**;
- `comparisons_of_complete`: a complete successful selector proves every comparison by one strong induction;
- `collatz_of_complete`: such a complete selector proves Collatz through the imported reverse-basin theorem.

The last theorem explicitly takes the unproved `Complete weights` hypothesis. It is a closing interface, not a completed proof.

### Kernel-checked search checkpoint

At modulus 1440, there are 720 positive odd source cells for each multiplier. Source 1 is handled directly; its nontrivial lifts use the representative 1441. The fixed-weight checkpoint contains:

| Target | Successful descent rules | Unresolved cells |
|---|---:|---:|
| `C₃` | 605 | 115 |
| `C₅` | 398 | 322 |
| Total | **1003** | **437** |

[`JointCertificates.lean`](lean/Collatz/JointCertificates.lean) checks every stored edge and rank guard with ordinary Lean `decide`. It also kernel-checks the rule and unresolved-list lengths. No Python verdict, native-code oracle, `sorry`, or additional axiom is used to establish these certificate-validity theorems. The successful rows are conditional induction rules; they are **not** a proof that the corresponding source cells converge without their lower hypotheses.

The search and untrusted emitter are in [`search/`](search/). The exact unresolved cells are retained in both JSON and Lean. A residue-dependent weight experiment exposed an additional obligation: even normalization can raise a residue-dependent rank. Such experimental rows are not substituted into this fixed-weight proof.

### Checkpoint 2: a single affine comparison and a uniform even rule

The generalized engine in [`AffineJointDescent.lean`](lean/Collatz/AffineJointDescent.lean) supports an explicit active comparison family. The second frozen search uses **only**

\[
C_\psi(n):\;\operatorname{Basin}(n)\leftrightarrow\operatorname{Basin}(2n-1),
\]

with rank `n`, on **every positive source**, including even inputs. Its [`PurePsiCertificates.lean`](lean/Collatz/PurePsiCertificates.lean) kernel-checks 1,265 whole-progression rules modulo 1440 and retains 175 unresolved even cells. It also proves that the successful and unresolved residue lists cover the complete finite residue set. These remain conditional induction rules. Details and regeneration commands are in [`PURE_PSI_CHECKPOINT.md`](PURE_PSI_CHECKPOINT.md).

The new [`PsiParity.lean`](lean/Collatz/PsiParity.lean) proves the unbounded rule

\[
C_\psi(m)\land C_\psi(4m-1)\Longrightarrow C_\psi(2m)
\qquad(m>0).
\]

Both calls strictly decrease the common rank `R(n)=n` for odd `n` and `R(n)=2n` for even `n`. It proves that full Collatz is equivalent to **two-way** psi comparison on all positive odd sources. It also supplies a global induction theorem with the remaining odd-source rank step stated explicitly as `OddRankStep`. That step is not proved by the partial linear-rank table.

The exploratory search using this common parity rank leaves 150 odd source classes at modulus 1440; that is search output, not an additional kernel-checked table. The report [`GLOBAL_SEARCH_ROUTES.md`](GLOBAL_SEARCH_ROUTES.md) records the other full-proof attempts, exact guards, source cutoffs and large ordinary excursions. It identifies an actual reciprocal family, now also proved in Lean:

\[
C_\psi(6t+4)\leftrightarrow C_\psi(8t+5).
\]

Two individually decreasing rules can select opposite directions of this relation. Their ranks therefore cannot be combined into a proof by taking the union of their covered cells. The formal result concerns those selected arcs, and does not rule out a different global proof.

## 2. The global analytic route

[`LINEAR_BLOCK_ATOM_FLOOR.md`](LINEAR_BLOCK_ATOM_FLOOR.md) gives the full selected-block derivation, its external source attribution, and its precise remaining scope. The only imported analytic estimate is Tao's published Proposition 1.14, with its exact normalized counting-measure formulation. The selected-density and weighted-counting strategy is attributed to El Jaouhari through the identified primary exposition; the linear block schedule and finite-cylinder presentation are developed here.

The key mechanism is a proved bound converting a tail `L¹` error into a pointwise error after transporting it through selected affine prefixes. Fixed-total word injectivity limits residue multiplicities, while linear block lengths give a quadratic accumulated prefix length and summable pointwise errors. This supplies a positive finite residue cylinder. The exact geometric recursion spreads that cylinder to every ternary unit.

[`SelectedWordInjectivity.lean`](lean/Collatz/SelectedWordInjectivity.lean) formalizes the unbounded finite-word injectivity used in that counting argument. The probability and analytic steps remain written mathematics, with a separate review. They are not hidden in a Lean axiom.

A valuation cutoff strengthens the predecessor conclusion: for every positive `a` not divisible by three, the reciprocal mass of its predecessors up to `X` has a positive lower bound proportional to `log X / a`. The proof explicitly handles nonperiodic targets, periodic targets and even targets, and does not assert positive natural density.

[`REPOSITORY_RIGIDITY_COROLLARY.md`](REPOSITORY_RIGIDITY_COROLLARY.md) applies that lower logarithmic density to the pinned PR155 and PR163 analytic interfaces. It discharges the separate predecessor-density input in their finite-energy rigidity theorem. With every domain and invariance hypothesis retained, the resulting statement is:

\[
0<s\le1,\quad
\sum_{\substack{x>0\;x\text{ odd}\\3\nmid x}}
x^{-s}d(f(5x),f(x))<\infty
\quad\Longrightarrow\quad f\text{ is constant}.
\]

Here `f(Tn)=f(n)` on positive ordinary integers and `d` is a metric. **Finiteness of this energy for a hypothetical separating label is still unproved.** The analytic corollary is not advertised as a Lean theorem.

## 3. Another global attempt and its exact limit

[`NegativeFiveEscape.lean`](lean/Collatz/NegativeFiveEscape.lean) supplies a total executable macro for the expanding signed-minus-five pattern. If `n+5=8^r z` with `8` not dividing `z`, it follows exactly `3r` ordinary steps to `9^r z-5`, which is positive, has the same basin membership, and is no longer 3 modulo 8. Its recursion decreases the stripped input, although ordinary values may increase.

The file also verifies an explicit failure of ordinary descent: the macro sends 262139 to 531436, whose next halving is still larger than the source. Thus this macro cannot silently stand in for an all-source descent theorem. Repeated exits still need a global decreasing quantity.

## 4. Source boundaries

The dependency-free foundation is imported from **PR174, `7034109ed60a26bc49824e1ed43c239ceca81194`**, directory `research/psi-closure-20261121/lean`. Its `ReverseBasin146.lean` identifies the original PR146 source `e238c63a5d57f96bb063b7472498d1977df51951` and the core-only shim. The imported foundation files are preserved; the package entrypoint is extended for the new modules.

The current research interfaces were refreshed through PR174. In particular the working PR146 head was `f431078244e868dc699fad011044f0d5e7f76437`, PR167 was `e83cc8b35ad614c616df7c00318cc9645a174c34`, and PR173 was `a09eb47197cd99f218b3fa013c681df65ea0f69a`. No global closure claim is inherited from those branches. A late metadata-only interface refresh also checked PRs175–179; its full head pins and observation scope are in `reports/2026-11-21-lean-ordinary-closure/LATE_INTERFACE_REFRESH.md`.

## 5. Reproduce

The project uses **Lean 4.34.1**, pinned in `lean/lean-toolchain`, with no Mathlib dependency.

```sh
cd research/lean-ordinary-closure-20261121/lean
lake build
lake env lean JointAudit.lean
```

Regenerate the literal certificate source from the retained JSON:

```sh
cd research/lean-ordinary-closure-20261121
python search/emit_lean.py search/joint-descent-1440.json lean/Collatz/JointCertificates.lean
```

Build and axiom receipts belong in `reports/2026-11-21-lean-ordinary-closure`. Repository integrity and the bounded regression bundle are separate from mathematical proof validity.

## Exact remaining global obligations

The certificate route must prove the odd-source step for one common rank, or supply another total successful selector. The uniform even macro is available, but the recorded linear and parity ranks cannot be mixed without a new argument. The analytic route must prove the missing all-source energy estimate; predecessor mass alone does not bound that energy. Neither obligation is discharged in this pass. [`SIGNED_CUTSET_ATTEMPT.md`](SIGNED_CUTSET_ATTEMPT.md) records the final actual-label first-entry attempt: a single failed cut can carry unbounded predecessor occupation, so selecting first defects alone does not supply the missing congestion estimate. This does not refute the specific CI4 compiler.
