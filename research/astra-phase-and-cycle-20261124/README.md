# Actual scalar digits, convergent cylinders, and cycle cancellation

24 November 2026. **Collatz remains OPEN.** This contribution uses three GPT-6.2 Astra workers, with separate mathematical reconstruction and actual local Lean execution. It builds on the current scalar, repetition, cycle and entropy packets rather than treating their open premises as established.

The most useful new results are exact arithmetic statements about the actual scalar and an improvement to the residual cycle denominator. The strongest limitations are constructive: every finite canonical word already occurs inside the convergent basin, and all the component norm tests can simultaneously lose their saving on a primitive positive rational cycle.

## Results and their verification boundaries

| Result | What it establishes | Boundary |
|---|---|---|
| [PS1–PS3: actual phase separation](PHASE_SEPARATION.md) | A run of L lowest canonical digits from odd q requires `2^(L+1) <= q+1`; a run of highest digits requires `4*8^L <= (5q-1)*3^L`. These give explicit two-sided separation of the actual centered scalar from every ternary grid, with different exponents on its two sides. | The run kernels and actual-map bridges have separate Lean receipts. Real approximation and sharpness deductions are written proofs. They do not classify arbitrary scalar phases. |
| [PS4–PS5: complete finite canonical language](PHASE_SEPARATION.md) | Every finite canonical word has an ordinary witness. More strongly, every word of length m has an explicit positive witness whose first visit to one is exactly m+2 accelerated odd steps later. Its actual scalar is known exactly. | Different words and lengths may use different sources. This proves no fixed source realizes an arbitrary infinite word. The unbounded construction is a written proof. |
| [PS6: exact scalar fibers](PHASE_SEPARATION.md) | On the two-step first-hitting layer, scalar `(6d+2)/9` has exactly d sources. Their residues modulo every power of three have counts differing by at most one. | A statement about many convergent sources, not a stationary measure on one escaping trajectory. |
| [Residual degree and denominator](CYCLE_FACTORS.md) | Primitivity forces `log p <= 3 sqrt(n) log(2n)`, where n is the residual polynomial degree. With the pinned PR185 value estimate, the denominator after polynomial cancellation grows faster than every fixed power of p. Prime-power clock gcds have stronger exponential bounds. | Written proof. The value estimate retains PR185's explicit linear-forms and finite-certificate dependencies. Numerical cancellation after evaluation remains unresolved. |
| [Simultaneously saturated norms](CYCLE_FACTORS.md) | Exact primitive rational examples have full polynomial survival and nonzero component norms, yet every component divides its norm. One example has every cyclic state above one. | Refutes a universal saving from that norm test alone; it is not an integer Collatz counterexample. |
| [Literal smaller shadow](OrdinaryShadow.lean) | An infinite actual L/P path in the PR191 residue class yields a strictly smaller positive source that never reaches one, with an unbounded actual shortcut clock. | Extends the formal scope of the pinned PR191 one-step algebra. Coverage of all nonconvergent sources is still open. |

[Formalization and replay scope](FORMALIZATION.md) records exactly which files and declarations were checked. [The independent phase review](REVIEW_CYCLE_AND_PHASE.md) reconstructs PS1–PS6 and separately reports its finite controls. The two mathematical workers did not review their own contributions as independent reviewers.

## 1. Actual phases retain a source-dependent arithmetic restriction

For the actual accelerated odd map

\[
U(q)=\frac{3q+1}{2^{a(q)}},\qquad a(q)=v_2(3q+1),
\]

use PR182's actual discounted gap series

\[
h(q)=\sum_{i\ge0}\frac{a(U^i(q))}{3^{i+1}}.
\]

The existing theorem gives `1/2 < h(q) <= 1 + log_2(q)/3` and the exact recurrence. Write

\[
h_i=c_i+\tfrac12+y_i,\quad c_i\in\mathbb N,\quad0<y_i\le1,
\qquad b_i=1+3y_i-y_{i+1}\in\{1,2,3\}.
\]

The physical gaps satisfy `a_i+c_(i+1)=b_i+3c_i`. The key normalized height is `X_i=q_i/2^c_i >= 1`. Its exact recurrence bounds extreme canonical runs without assuming any rationality, periodicity, or convergence of the source.

Let alpha=log_2(3), gamma=log(3)/log(8/3), and delta=1+log(3/2)/log(8/3). The written consequence is

\[
y(q)>(q+1)^{-\alpha},\qquad
1-y(q)\ge\frac13\left(\frac{5q-1}{4}\right)^{-\gamma}.
\]

At every precision `3^n`, the corresponding fixed-source approximation exponents are alpha (approximately 1.585) from below and delta (approximately 1.4134) from above. This excludes explicit Liouville-type phase proposals. Ordinary inputs `2^k-1` show that the local lower-side exponent cannot be decreased. No optimality claim is made for the other exponents.

## 2. All finite phase patterns occur even before certified convergence

For a word w of length m in `{1,2,3}`, let D_w be the ternary integer with digits `w_i-1`. The PS5 witness has

\[
y(q_w)=\frac{D_w+7/18}{3^m},\qquad
h(q_w)=\frac52+\frac{D_w+7/18}{3^m},
\]

and reaches one for the first time at odd clock `m+2`. Thus each canonical cylinder contains an explicit convergent ordinary source. The construction simultaneously controls the real discounted scalar and a terminal congruence modulo `3^m`; it is stronger in this particular respect than merely realizing a physical parity prefix.

The arithmetic ingredient is a family of two-step predecessors on one exact scalar level. A parameter map preserves 3-adic distance, so its first `3^m` values give every required terminal residue. PS6 classifies the whole reduced-denominator-nine two-step scalar layer and proves the exact residue discrepancy.

Consequently an all-source forbidden finite canonical word cannot be a closing argument. A useful restriction must retain the fixed source, its height, or another unbounded state. The explicit finite witnesses do not assert an infinite escaping ordinary orbit.

## 3. More polynomial survival still leaves the integer evaluation

For a parity word of length A and weight p, define

\[
F(X)=X^p-2^A,\quad Q(X)=\sum_i2^{d_i}X^{p-1-i},\quad
G=\gcd(F,Q),\quad F_0=F/G.
\]

The new count uses the complete root-of-unity orders forced by ordinary word primitivity. Each maximal prime-power factor of `gcd(A,p)` consumes cyclotomic degree. This replaces PR185's exponential bound on p in terms of n by a subexponential one. Combining it with PR185's specified positive-cone estimate yields `|F_0(3)| > p^K` for every fixed K once p is sufficiently large.

An actual cycle instead needs the entire remaining integer denominator to divide `(Q/G)(3)`. The accompanying examples show that both large surviving polynomial factors and all nonzero component norms may fail to prevent this numerical cancellation. In one exact example PR191's norm lower bound is one although the actual rational denominator is 82,955, with all cyclic values greater than one. The missing input must distinguish the evaluation at 3 inside each algebraic component or impose a different global arithmetic constraint.

## 4. Current repository intake

[SOURCE_SNAPSHOT.json](SOURCE_SNAPSHOT.json) pins the fetched heads and trees of PR146–191, including PR182's concurrent round-12 update at `cbec52dde5bed390a693310dd04e911033ba0cc9`. This inventory is not a claim of line-by-line review of every source file in those PRs.

The deep reading in this pass covered the following interfaces:

| Sources | Retained conclusion | Still required for a full proof |
|---|---|---|
| PR146; PR173–184 band and merger work | Exact directed comparison reductions, forced marked visits, and supplied smaller-partner certificates | A universally available partner smaller than the original source or an adequate marked representative |
| PR182, including rounds 10–12 | Actual scalar construction, triadic equivalence, fixed-source repetition, phase-conditioned carry arithmetic and contracting-phase classification | Universal scalar membership or another contradiction for low/irrational phases |
| PR185 | Residual polynomial survival, complete numerical cancellation boundary, actual-source collision lower bounds | A numerical denominator saving or a matching bound for the same source law |
| PR187 | Finite-window repeat/mismatch obstruction for prescribed carry scripts | Universal recurrence or script coverage |
| PR188–189 | Carry amortization, residue norms and stationary/carry entropy restrictions | A source-preserving opposite estimate, not an independent random model |
| PR190 | Proposed binary uniform/primitive substitution exclusion through Mahler methods | A structure theorem putting arbitrary actual exceptional schedules in the treated class; full analytic Lean verification is separate |
| PR191 | Two-sided packing, all-clock component norms and a smaller actual shadow in one residue class | Useful coverage or simultaneous arithmetic separation for unrestricted cycles and escapes |

The source-qualified population/flow inputs of PR180 and their consumers remain source-qualified. No claimed GRH consequence is inserted into the Collatz proof chain. The Alpoge RH/Dirichlet-GRH announcement and public verification records were checked separately; they do not supply an identified implication resolving these Collatz obligations.

## Reproduction and handoff

Run `python -B phase_controls.py` and `python -B cycle_controls.py` from this directory; the optimized Python executions must return the same bytes. These are exact finite controls, not exhaustive Collatz verification.

For Lean use the pinned environment and the sequential replay in [FORMALIZATION.md](FORMALIZATION.md). The vendored actual-scalar source is byte-exact, with its PR, commit, Git blob and SHA-256 in [VENDOR.json](VENDOR.json). Execution logs and receipt identities are kept under the companion reports directory.

The next mathematical task is still a universal fixed-source obstruction: for example, a theorem preventing the remaining low-complexity or arbitrary canonical phases from satisfying the actual carry/congruence system, or an arithmetic argument at the distinguished cycle evaluation that survives the explicit saturated-norm controls. Nothing in this packet proves that the current alternatives cover every orbit.
