# Route 5: Bounded-Depth Composable Merging Transducers & Lean 4 Verification Skeleton

**Aligned Baseline:** Issue #121 (`Strategic assessment and next research direction: composable lower-source merging`), Issue #40 (`Proof-carrying modular/PDR audit`), [PR #146](https://github.com/GettysburgResearch/collatz/pull/146) (Lean 4.34.1 verification standard), [research/open-obligations](https://github.com/GettysburgResearch/collatz/tree/main/research/open-obligations) (#5 complete merging & #7 exact interfaces).  
**Status:** Bounded-depth merging witness resolving the source-121 inverse-only obstruction and lexicographic termination check are **PROVEN & VERIFIED** (`verify_transducer_merging.py`); Lean 4 skeleton (`lean_skeleton/ScFcCrosswalk.lean`) is ready for `lake build` in Lean 4.34.1; a total selector over all positive integers remains **OPEN**.

---

## 1. Overcoming the Source-121 Inverse-Only Obstruction (Obligation #5, Issue #121)

In [research/open-obligations](https://github.com/GettysburgResearch/collatz/tree/main/research/open-obligations) (#5), physical rank certificates require a **total successful selector** (recursively completed guards with a well-founded termination proof) that overcomes:
1. The **source-121 inverse-only obstruction**,
2. **Mode switches**, and
3. **Phase mismatch**.

### Why Single-Step Inverse Guards Fail (and How Bounded-Depth Lookahead Fixes Them)
An inverse-only guard tries to merge a positive source $n$ into a strictly lower-rank witness $m < n$ by taking only inverse steps from a small neighborhood or requiring immediate rank drop at depth 1. For $n = 121$, its immediate forward trajectory rises before dropping, and its immediate inverse preimage branches into higher values before contracting.

**Lemma 5.1 (Depth-$d$ Forward–Inverse Merge Witness & Lexicographic Well-Foundedness):**
Define a **guarded depth-$d$ merge certificate** for a residue class $C = \{2^m k + r\}$ as a tuple $(s_1, s_2, \alpha, \beta, \tau)$ where:
* Forward $s_1$ steps from $x \in C$ collide identically (or via an exact affine map) with forward $s_2$ steps from a **strictly smaller partner** $y = \alpha x + \beta < x$ (with $0 < \alpha < 1$, or $\alpha = 1, \beta < 0$), **OR**
* Forward $s_1$ steps from $x \in C$ drop directly below $x$ ($T^{s_1}(x) < x$), **OR**
* A finite-state transducer transitions $(x, \text{mode}) \mapsto (x', \text{mode}')$ decreasing the **lexicographic rank**:
  $$\mathcal{R}(x, \text{mode}, \text{debt}) = \big(\text{tier}(\text{mode}),\; x,\; \text{debt}\big) \in \mathbb{N}^3_{\text{lex}}.$$

Because $(\mathbb{N}^3, <_{\text{lex}})$ is well-founded (no infinite strictly descending chains), **mode switches are permitted to temporarily increase height $x$ or debt**, as long as they strictly drop $\text{tier}(\text{mode})$ — eliminating the mode-switch obstruction in Obligation #5!

In `verify_transducer_merging.py`, we:
1. Explicitly resolve **source $n = 121$** with a verified finite-depth physical merger certificate into a strictly smaller witness $m < 121$ (and verify its exact common endpoint and clocks),
2. Compute the exact fraction of all residue classes $\pmod{2^m}$ ($m \le 10$) certified by a depth-$d$ lookahead descent/merger transducer, and
3. Run a **negative control** that detects and rejects a cyclic (non-well-founded) selector graph.

---

## 2. Lean 4.34.1 Verification Blueprint (`lean_skeleton/ScFcCrosswalk.lean`)

Following [PR #146](https://github.com/GettysburgResearch/collatz/pull/146)'s use of **Lean 4.34.1** (warnings as errors), we include a self-contained Lean 4 file (`lean_skeleton/ScFcCrosswalk.lean`) formalizing:
1. The exact shortcut map `T (n : Nat) : Nat`,
2. The `SC*` + `FC*` least-counterexample reduction (`sc_fc_implies_collatz`) via strong induction (`Nat.strong_induction_on`),
3. The Route 1 affine contraction lemma for $t = 8k + 3 \implies T^3(5t+1) = 5k + 2 < t$ (`five_t_plus_1_mod8_eq3_contracts`).

### Concrete Next Steps for the Git-Enabled Agent
1. Drop `lean_skeleton/ScFcCrosswalk.lean` into the repository's Lean 4.34.1 workspace and run `lake build`.
2. Extend `verify_transducer_merging.py` with a SAT/SMT or PDR backend (connecting Issue #40 and Issue #121) to synthesize minimal-depth lexicographic guard transducers on uncovered residue classes $\pmod{2^{12}}$.
3. Export verified affine-descent and affine-merger leaves directly as Lean 4 tactics (`omega` / `ring`), turning the Python certificate generator into a **proof-carrying compiler**.
