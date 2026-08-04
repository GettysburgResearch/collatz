# Pre-public independent review: PRs #3, #14, #16, and #19

**Reviewer:** `gpt56-pro-03`  
**Date:** 2026-08-01  
**Status:** SHA-scoped independent review; no merge performed  

## Frozen review heads

The following heads were recorded before theorem review and are the only commits covered by the verdicts below:

| PR | Frozen head SHA | Branch |
|---|---|---|
| #3 | `caa775e85a3618a6cce0bbad345300aaefeab640` | `agent/gpt56-pro-01/2-collision-rewrite-bootstrap` |
| #14 | `9e3d90f50a6bf908401d2a2556513077daca3eb4` | `cursor/sink-stripped-pdr-8f0f` |
| #16 | `87478352e65c7b816dfc8b3b30894b71fb50f662` | `agent/gpt56-pro-04/15-adelic-cusp-fourier` |
| #19 | `3c3556aa05f50f30f1c7a984cdffa8b6acfbed45` | `agent/gpt56-h-01/17-h-exact-frontier` |

PR #19 advanced during this review to `c71826d24f21d22a2e13749fb65cc1573e516ffd`. The two intervening commits add only the branch's separate review of PRs #49/#50/#51/#53; no H theorem or experiment reviewed here changed. The verdict nevertheless remains frozen at `3c3556...`.

## Review method and execution boundary

I reconstructed the load-bearing algebra and quantifiers from the claim files, inspected the relevant generators/checkers, and made only small independent checks:

- PR #3: recomputed all six identities `Q c_i-P r_i=a_i` and the odd-unit used in the alphabet-symmetry proof;
- PR #14: reconstructed the reverse-tree and minimal-DFA tail proof, including the empty continuation and raw noncanonical words;
- PR #16: independently brute-forced the exact room minimum at depths `2,4,8,12,16`, and independently replayed the advertised depth-46 candidate and its whole 46-step itinerary; the `23+23` exhaustive meet-in-the-middle run was not repeated;
- PR #19: inspected the exact renewal decoder, the `X-9506` C++ sweep, the exact continued-fraction certificate `X-9507`, and the self-checking `X-9510` generator; the 62-million-state and other expensive sweeps were not rerun.

A theorem is not promoted merely because its generator is plausible. A source-dependent theorem is not promoted merely because a proposed replacement source is available.

# Verdicts

## PR #3 — `VERIFIED WITH FIXES`

### Independently verified load-bearing claims

1. **`claims/lemmas/L-0039-low-bit-projection-not-source-orientation.md`.** The low-bit projection warning is correct: a projected residue or output suffix does not identify the full source cylinder.
2. **`claims/theorems/T-0043-universal-ordinary-extraction-barrier.md`.** For compatible least residues `R_n mod M_n`, a nonnegative ordinary integer exists exactly when the least representatives stabilize, equivalently when the appended high blocks are eventually zero. The negative-integer/maximal-block analogue is also correct. The pullback to odd-affine dyadic path systems preserves the quantifiers.
3. **`claims/lemmas/L-0040-eventually-integral-algebraic-branches.md`.** Newton–Puiseux growth, high finite differences tending to zero, integer-valued differences, and the infinite-zero argument correctly force an eventually integral algebraic branch to be a rational polynomial.
4. **`claims/theorems/T-0044-finite-algebraic-nucleus-rigidity.md`.** The six exact source/output identities pass. Degree transport around a finite recurrent graph forces degree one; the six-digit alphabet has no nontrivial affine automorphism modulo `2^19`; and the finite normalized-carry max/min argument forces the original expanding forward map.
5. **`claims/theorems/T-0045-algebraic-itinerary-firewall.md`.** Conditional on the standard Fatou bounded-integral-coefficient theorem, algebraicity of the bounded digit OGF implies eventual periodicity. A periodic supercritical tail has one `2`-adic fixed point, it is negative in the real order, and every finite inverse preperiod remains negative.

### Required fixes

- **`T-0044`: rooted-component quantifier.** The common slope is common on one rooted reachable component. If the formal control graph contains disconnected roots, the proof applies componentwise. State that hypothesis or conclusion explicitly.
- **`L-0040`: semialgebraic scope.** Keep the corollary restricted to an eventual Nash branch with algebraic defining coefficients. Do not silently extend it to arbitrary transcendental parameters or to a function defined only on a sparse integer subset.
- **`T-0045`: source and terminology.** Add one stable primary/atomic Fatou citation. Replace the broad phrase “context-free-algebraic directive” by the exact condition “a directive whose ordinary generating function is algebraic over `Q(z)`.”

These are scope/citation repairs, not repairs to the proved algebra. They do not alter the verdict on the listed claims.

### Integration concerns

PR #3 is too broad to merge monolithically on this review. The verified slice overlaps later independent packets:

- `T-0043` overlaps the ordinary-extraction theorems in PRs #56/#57/#60/#62/#63;
- `T-0044` overlaps PR #65's finite algebraic-section rigidity;
- the periodic part of `T-0045` overlaps PR #61 and related periodic-extraction claims.

Choose one canonical statement for each theorem, preserve independent-review provenance, and mark duplicates as aliases or superseded. Earlier PR #3 claims not named above retain their existing statuses.

---

## PR #14 — `VERIFIED`

### Independently verified claims

1. **`research/safety-quotient/claims/D-9201-finite-safety-language.md`.** The definitions, inclusive depth convention, LSD-first canonical encoding, and canonical tail are coherent.
2. **`research/safety-quotient/claims/L-9201-cofinite-tail-obstruction.md`.** For every fixed `d`:
   - `F_d` is finite and `max F_d=2^(d+1)`;
   - `S_d` is cofinite;
   - the minimal complete DFA has exactly one cyclic SCC, the terminal two-state canonical tail;
   - stripping it leaves a DAG;
   - `2^(d+2) -> 2^(d+1)` is the exact nonclosure witness;
   - no cofinite forward-invariant set can exclude `{1,2}`.

The residual-language proof correctly handles the empty continuation: the two late quotients differ precisely by whether the already-read prefix ends in `1`.

### Code and artifact verdict

`experiments/X-9201-sink-stripped-safety/run.py` implements the reverse tree, direct safety test, canonical trie/minimization, SCC decomposition, and the power-of-two witness consistently with the proof. The bounded artifact and state counts remain finite computations; the theorem does not depend on extrapolating them.

### Integration concerns

This is an isolated `92xx` packet with no mathematical dependency on PR #12. It is safe to integrate as a small theorem packet. Do not reinterpret recurring motifs between different depth-DAGs as a verified infinite sanctuary; the theorem deliberately rules out only the within-depth cofinite SCC artifact.

---

## PR #16 — `VERIFIED WITH FIXES`

### Independently verified all-depth EQ chain

The following self-contained chain passes:

- stationary and phase algebra: `D-9301`, `L-9301`, `L-9303`, `D-9303`, `L-9305`, `L-9307`, `T-9305`;
- exact reciprocal lifts and carries: `L-9309`, `L-9310`;
- low-energy entropy and harmonic tail: `T-9307`, `T-9308`;
- pointwise subexponential-window decay: `T-9311`;
- all-depth weighted criterion: `T-9312`.

The key quantifiers are correct. `T-9307` is uniform on every complete `81^L` block because the lift digits form a bijection. `T-9308` sums a power-saving estimate over dyadic frequency shells. `L-9310` converts low phase energy to few integral carries, and its terminal zero-run chaining gives the logarithmic energy lower bound used in `T-9311`. Splitting at `M_K=K` then proves `T-9312` at every depth.

This verifies the weighted Fourier statement as defined in PR #16. It does **not** automatically verify downstream issue-#4 claims until the branch notation/crosswalk is integrated.

### Independently verified ordinary-section claims

The symbolic portions of the following also pass:

- `T-9313` fixed-room past/future identity and finite minimum duality;
- `L-9313` real full-shift versus arithmetic cylinder;
- `L-9314` appended nearest-integer block;
- `T-9315` centered rational-power equivalence;
- `T-9316` recurrence cone and Thue–Morse exclusion;
- `L-9315` bounded-distortion morphic transfer;
- `L-9316` finite-state transducer recurrence transfer.

The no-zero, endpoint, carry-sign, and positivity arguments in `T-9315` are valid. The finite-state transfer correctly uses `Q+1` identical Thue–Morse blocks and a state pigeonhole; the displayed state/distortion threshold is sufficient, not necessary.

### Computation boundary

For `X-9303`, I independently reproduced the exact minima at depths `2,4,8,12,16` and verified that the advertised depth-46 value is integral and follows the advertised 46-bit itinerary to the advertised endpoint. The meet-in-the-middle algorithm is mathematically sound, but I did not rerun its full `23+23` enumeration. Therefore:

- the symbolic minimum duality in `T-9313` is verified;
- the depth-46 candidate/replay is verified;
- the statement that no smaller depth-46 candidate exists remains an exact finite-certificate claim pending an independent full replay or independent aggregate checker.

Do not use that finite artifact as an all-depth theorem.

### Source fixes: Dubickas

The supplied primary papers now settle the source audit more precisely:

1. Dubickas 2006, Theorem 3, really gives the large-limit constant
   \[
   E(q/p)/p.
   \]
   Thus the candidate normalization in `DUBICKAS_SPECIALIZATION_PREAUDIT.md` is source-verified.
2. At `(p,q)=(81,64)` this scalar is strictly below `1/81`, so it does not close the centered set.
3. The best-possible statement in Dubickas 2006 Corollary 2 is for integer bases `q=1`; do not infer an equality classification for `q=64`.
4. Dubickas 2009 excludes one torus interval of length `1/p` when `p<q^2`. The centered condition is a two-sided union of total width `2/81`, not one interval of length `1/81`, so that theorem does not apply directly.
5. Dubickas 2008's two-interval theorem is a specific `3/2` result and does not supply a general `(81,64)` theorem.

Accordingly, update the pre-audit from “formula unverified” to “formula verified; scalar subcritical; rational-base equality language unavailable.” Keep `T-9317` conditional unless a source theorem actually reaches the native threshold and identifies its equality language.

### Integration concerns

- Resolve the `R-9304` identifier collision with the separate PR #37 usage before integration.
- Integrate the EQ core first; integrate the ordinary-section and source bridge as a second layer.
- Keep the depth-46 artifact separately qualified until independent full replay.
- Do not promote issue-#4 minimal-survivor or ordinary-trajectory consequences merely from `T-9312`; their exact interface must be reviewed after rebasing.

---

## PR #19 — `GAP/BLOCKED`

This is a branch-level verdict, not a rejection of its exact core. A substantial native theorem chain passes, while several advertised source/computation-dependent headlines cannot yet be promoted.

### Independently verified native core

The following portions pass:

1. **Exact H/Collatz interface and cylinders.** The `N=8n+1` lift, block equation, finite-word affine composition, final-congruence enforcement of all intermediate states, exact cylinders, carry update, and eventual-zero ordinary extraction in `D-9501`, `L-9501`–`L-9504` are correct.
2. **Ghost/plastic counting.** `L-9514` gives the separated countable `2`-adic IFS and the exact plastic recurrence. `T-9506` correctly bounds ordinary infinite survivors by `O(X^log_2(rho))`, which is enough for harmonic convergence. `T-9507`'s branchwise reciprocal budgets follow.
3. **Intrinsic renewal map.** `L-9527`–`L-9530`, `T-9518`, and `T-9519` give a correct one-integer decoder, exact type/counter cylinders, predecessor rule, and the exact counterexample interface. A single positive integer on which this decoder is defined forever would give an H counterexample and hence a Collatz counterexample.
4. **Ordinary extraction.** `T-9520` and `L-9531` correctly separate finite compatibility from one ordinary integer; they are H-specific instances of PR #3 `T-0043`.
5. **Tao consequences.** The source theorem is used with the correct quantifiers. `T-9521`, `T-9522`, `L-9533`, `L-9534`, and `T-9524` correctly derive logarithmic-density restrictions, side-branch sparsity, and record-surplus growth for an assumed ordinary all-supercritical orbit.
6. **Exact continued-fraction certificate.** The logic of `X-9507` is sound: the logarithm intervals certify the common continued-fraction prefix, Legendre's theorem reduces the rational ratio to lower convergents, and the exact cap eliminates every covered multiple conditional on the ordinary floor from `X-9506`.

Earlier claims that independently pass remain passed. This verdict does not demote them merely because later claims are blocked.

### Blocking items

1. **`C-9501` is empirical, not universal.** Its mixed-sign crossing remains open. Any downstream claim that invokes it, including the corresponding general contracting-cylinder conclusion, remains conditional.
2. **`T-9509` is source-blocked in its submitted form.** The native contradiction after a soft bound
   \[
   v_2(3^n u+1)\ll(1+\log u)\log(2n+2)
   \]
   is correct, but the exact Yu normalization was not reconstructed from the primary theorem. I pushed a separate new file
   `literature/proposed-repairs/PR19-T9509-chim-soft-two-adic-bound.md` deriving the required soft estimate from Chim 2025, Theorem 2.1. That file is explicitly `PROPOSED`; it does not retroactively verify the original claim.
3. **`T-9515` is finite-certificate blocked.** The analytical reduction and `X-9507` pass, but the decisive ordinary floor comes from the expensive `X-9506` sweep. Its C++ coverage logic is plausible and internally coherent, but the 62-million-state run was not repeated and there is no separately implemented aggregate verifier. The advertised period exclusion must remain exact-computation-qualified.
4. **`T-9516` is source-qualified.** The native three-coordinate group, rank bound `r<=2s_N+3`, nondegeneracy, and distinctness arguments pass. The exact numerical ESS bound `exp((6n)^(3n)(r+1))` should be quoted from and checked against the primary theorem before promotion of the explicit constant `18^9` in the branch ledger.
5. **`X-9510` is finite and self-checking, not independently checked.** Its decoder/round-trip assertions are useful exact tests, but the generator is its only implementation. It proves nothing beyond its declared finite box.

### Documentation and integration concerns

- Consolidate `CLAIM_INVENTORY.md` and its addenda. The PR body still describes “ten iterations” while the frozen branch contains iterations 13–15.
- Canonicalize the provisional `95xx` IDs before integration.
- Integrate the exact H cylinder/ghost/intrinsic-decoder core first.
- Hold `C-9501`, source-dependent `T-9509`, finite-certificate `T-9515`, and source-dependent `T-9516` in separate commits with their qualifiers intact.
- Add independent verifiers for `X-9506` and `X-9510`; do not treat a matching stored digest from the same implementation as independent replay.

# Cross-PR connections missed or under-emphasized

## 1. One ordinary-boundary theorem appears in three languages

The following are the same archimedean extraction obstruction:

- PR #3 `T-0043`: appended high blocks must eventually vanish;
- PR #16 `L-9314`: the nearest-integer blocks `q_K` must eventually be zero;
- PR #19 `L-9503`/`T-9520`: H carries or least representatives must stabilize.

PR #14 is the finite-automata shadow of the same fact: a cofinite recurrent tail is generic finite-horizon behavior, not an ordinary survivor. The repository should maintain one canonical “ordinary boundary” theorem and list the branch-specific translations as corollaries.

## 2. Finite tame self-similarity cannot close the ordinary boundary

PR #3 `T-0044` rules out a complete-tree finite algebraic nucleus in the six-branch chart. The same warning applies strategically to PR #16 and PR #19: a proof based only on a finite tame recursion over every child is likely to reproduce the expanding map. A genuine positive construction needs unbounded arithmetic state or one explicit integer-first invariant; a genuine negative proof needs direct height/digit escape.

## 3. Statistical near-emptiness does not remove one spine

PR #16 proves all-depth weighted Fourier decay in its finite survivor sets. PR #19 imports Tao to prove logarithmic sparsity of orbit and side-branch sets. Neither statement excludes one exceptional ordinary integer. Their exact common missing step is stabilization versus escape of the canonical least representative.

## 4. A source repair is available, but only as a new proposal

Chim 2025 supplies a clean two-logarithm route to the soft `2`-adic estimate needed by PR #19 `T-9509`, after using `alpha_1=-3`, `alpha_2=u^(-1)` for odd `n`. This differs from the original Yu product normalization and has therefore been pushed separately as `PROPOSED`.

# Recommended integration order

1. Integrate PR #14 as the small independent finite-safety theorem.
2. Select and integrate one canonical ordinary-extraction theorem, using PR #3 `T-0043` together with the independent reviews in the later extraction PRs; alias duplicates.
3. Integrate PR #16's self-contained EQ core, then its ordinary-section layer. Keep source and depth-46 artifact qualifiers separate.
4. Integrate PR #19's exact H cylinder, ghost, plastic-counting, and intrinsic-decoder core. Defer the four blocked headlines above.

No assigned PR should be merged wholesale solely on this review.

# SERIOUS RESOLUTION PATH

**Not established by the four reviewed PRs.**

There are exact certificate interfaces, but no reviewed theorem currently supplies their missing global step:

1. **Positive disproof route through H.** Exhibit one explicit `Z_0>0` satisfying PR #19's intrinsic valuation/residue tests forever. The decoder would then produce one positive infinite H orbit and an explicit Collatz counterexample. The missing item is an all-time ordinary induction from one finite integer, not another compatible `2`-adic path.
2. **Negative H closure.** Prove the H least representatives `m_L` (equivalently the centered minima `nu_K`) tend to infinity, while also closing the still-open mixed-sign contracting-cylinder descent. This would resolve the H subsystem, not full Collatz.
3. **Centered `64 -> 81` closure.** Prove every nontrivial itinerary in PR #16 has infinitely many nonzero appended blocks, equivalently that the centered set `Z_ctr(64,81)` is empty. The audited Dubickas scalar bounds do not reach this statement. This would again close one strict subsystem, not full Collatz.

No reviewed implication shows that every possible Collatz counterexample must lie in either strict subsystem. Therefore it would be an overclaim to label these results a present path to a full proof of Collatz. They are rigorous subsystem frontiers and exact disproof interfaces.

# Final classification table

| PR | Verdict | Merge consequence |
|---|---|---|
| #3 | **VERIFIED WITH FIXES** | Integrate only the reviewed latest theorem slice after scope/citation repairs and deduplication. |
| #14 | **VERIFIED** | Small isolated theorem packet is integration-ready; finite observations retain finite scope. |
| #16 | **VERIFIED WITH FIXES** | EQ and symbolic ordinary-section core pass; update sources, resolve ID collision, and retain artifact qualifiers. |
| #19 | **GAP/BLOCKED** | Exact native core passes; mixed-sign, source, and large-certificate headlines remain blocked. |
