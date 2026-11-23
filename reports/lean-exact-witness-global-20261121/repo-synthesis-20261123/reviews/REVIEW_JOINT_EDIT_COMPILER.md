# Independent review: complete bounded joint-edit compiler

23 November 2026. Reviewer: global-cycle lane, independent of candidate author.

**Verdict: VERIFIED at the written arithmetic and implementation scopes below.** The universal successful edit-budget selector remains open. This review supplies neither that selector nor a full Collatz proof.

## Exact reviewed sources

All three are under `research/lean-exact-witness-global-20261121/repo-synthesis-20261123/candidate/`:

| File | SHA256 |
|---|---|
| JOINT_EDIT_COMPILER.md | `9832f769044ccbf33765665f60652a854efee0821d63909a1fb8effb203a06b8` |
| JointEditCompiler.lean | `750fe07635f7f3eec7e60b27c75f34db1f024434fb0d85addf4093ca47ffc1e9` |
| joint_edit_compiler.py | `a4dc6e292416c4d52baf1f0b0fd54e2d4a59b9daa3b511320cafdcc5d4922da5` |

I read the manuscript, the complete Lean source, and the Python search, checker, source/output tuple conversion, witness transport, finite-grid oracle, and closed-orbit optimum routines. This review reconstructs the mathematics and performs focused new execution. It does not repeat the author's full finite test suite or claim a separate Lean compiler execution.

## 1. The arbitrary-clock finite bound

A common parity branch multiplies the signed coordinate difference by either `1/2` or `3/2`. A common run of length k therefore gives

`2^k (T^k x-T^k y)=3^p(x-y)`.

For distinct ordinary sources this difference stays nonzero. Powers of two and three are coprime, so `2^k | x-y`. If both sources are below `2^N`, then `k<N`. The first meeting cannot occur during a common run, since every prescribed common branch is injective. Consequently a first-merger alignment is precisely a succession of common runs followed by one unmatched ordinary step, ending immediately after an edit.

After such a run and one edit, every coordinate is below `2^(N+k+1) <= 2^(2N)`, using `T(z)<=2z`; the first segment has at most N columns. The recurrence `B(N,t+1)=N+B(2N,t)`, `B(N,0)=0`, gives exactly `N(2^t-1)`. This is a bound on every admissible first-merger alignment, with both edit directions and arbitrary difference signs. It is not a same-endpoint assumption, and moving the advertised endpoint into a common suffix cannot evade the first-meeting truncation.

The sharper real bound is also valid: for `h=log_2(max(x,y)+1)` and `alpha=log_2(3)`, a run-plus-edit uses at most `h+1` columns and changes the height to `h_new+1 <= alpha(h+1)`. Summing this geometric budget yields the manuscript's JE6. The exact compiler does not depend on logarithmic floating-point evaluation.

## 2. Exhaustive compiler and formal scope

The Python enumeration of common cuts `0,...,v_2(x-y)` is complete. At every matching step the nonzero difference loses exactly one factor of two, so the current parities agree until precisely that valuation is exhausted. The code tries both edit directions at every earlier cut as well as at the first mismatch. Recursion decreases the edit budget, so each supplied finite budget has a finite mathematical search tree. Memoization does not delete any branch.

The Lean search uses the independently justified finite range `0,...,N-1` and tests the literal common-run predicate. I reconstructed its soundness and completeness induction. The `Alignment` and `Repair` inductives retain actual ordinary iterates; `alignment_normalizes` supplies the grouping, including the impossibility of meeting in a zero-cost common column. The updated bit budget is proved rather than assumed. Rejection completeness concerns all repairs using at most the supplied edit budget, at every possible clock, and the normalization extends this to raw first-merger alignments.

The formal source also proves ordinary clocks bounded by `N(2^t-1)` and the witness consumer. These statements match the manuscript's claimed formal boundary. The tuple conversion and optimized valuation enumeration are separately justified written/executable components, not misrepresented as extracted Lean code.

## 3. Complete source-witness transport

Given `T^a x=T^b y` and `T^L y=1`, the exact equation

`T^(a+L+b) x = T^(L+2b) y = T^(2b) 1 = 1`

is correct for arbitrary b, including b greater than L. No negative clock or backward branch is required. Since both merger clocks are at most B, the output clock is at most `2B+L`.

The Python consumer checks the entire input tuple identity and all its indicated odd clocks. It appends the actual unused source tail when available; otherwise the common endpoint is in the verified core `{1,2}`. It then truncates at the target's first hit of one and forms the output exponents from every odd-input clock plus the terminal clock. The output identity and full replay are checked. The degenerate tuple `[0]` for source one is handled. Valid terminal-cycle padding is preserved as allowed input, without being counted as a new convergence premise.

## 4. Independent all-clock optimum: 193 and 385

I constructed both actual state sets independently by iteration until their first repeated state, rather than importing the author's supplied first-hit clocks. Their sizes are 77 and 24, including the core. Their Cartesian product has 1,848 vertices. Left and right transitions, plus simultaneous equal-parity transitions, form a forward-closed ordinary graph with 4,598 edges.

I used a **forward heap Dijkstra algorithm from `(193,385)`**, distinct from the author's reverse zero/one algorithm. I exhausted the complete product, then minimized the distance over every diagonal vertex. The result is exactly **39 edits**. An independently reconstructed physical certificate reaches endpoint one with clocks **76 and 37**, so its source trajectory includes terminal-cycle padding beyond its first hit at clock 23.

I additionally executed the supplied compiler at budgets 38 and 39: it rejects 38 and accepts 39. The full input tuple

`[0,2,4,6,7,12,13,14,19,23]`

is consumed, and the emitted target tuple ends at clock 76. I independently checked its full integer identity. Appending the two valid terminal cycles at exponents 25 and 27 gives the same first-hit target tuple. These focused execution results, the independent alignment, output tuple, and source hashes are preserved in [joint-edit-independent.json](joint-edit-independent.json).

Thus the specific proposed budget `t<=L` is refuted at the required residue-class example: `385 mod 512=385`, target 193, input clock 23, all-clock minimum 39. This is an actual finite ordinary countercontrol to that budget, not a counterexample to the original implication.

## 5. Remaining boundary

The complete arbitrary-budget compiler does not supply an edit budget guaranteed to succeed for every required input tuple. Iterating through unbounded budgets is still only a semidecision until ordinary merger existence is established. The manuscript retains this distinction clearly. No source-qualified analytic result is silently imported, no finite test is extrapolated to universal convergence, and no unrestricted complete-witness resource is discarded.

No mathematical correction was required at these exact reviewed hashes.

