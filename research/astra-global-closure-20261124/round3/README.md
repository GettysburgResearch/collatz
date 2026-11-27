# Original-source divisor counts, persistent descent, and cycle transport

**Collatz remains open.** This continuation strengthens three direct approaches using the literal unit carry. It began at PR195 head `07aa5124f7ca482b6665d61355fac0af5f6e55b2`, re-examined the current repository frontier, and compared the proposed arguments with recent primary literature. Three GPT-6.2 Astra agents and the parent developed and cross-reviewed the packet. Seven new Lean modules and their complete two-module project dependency closure passed a fresh build; the analytic conclusions have the narrower formal boundaries stated below.

## 1. Almost every short prefix has distinct prime witnesses

Use the accelerated odd map
\[
 U(x)=\frac{3x+1}{2^{v_2(3x+1)}}.
\]
For a positive odd source \(x\), put \(q_i=U^i(x)\), \(0\le i<t\). A position \(j\) is **covered** when every prime satisfies
\[
 v_p(q_j)\le\sum_{i\ne j}v_p(q_i).
\]
Let \(E_t(X)\) count sources \(x\le X\) having at least one such position. The unconditional written theorem is
\[
 \boxed{E_{t(X)}(X)\le X^{o(1)}\quad\text{if}\quad
             2\le t(X)=o(\log\log X).}
\]
Outside this exceptional set, every position has its own strictly dominating prime valuation. The witnessing primes are distinct, and all \(t\) actual states are multiplicatively independent. For example, the window length may tend to infinity like \(\sqrt{\log\log X}\). This is a count of original starting integers; it makes no assertion about a random law along a single exceptional orbit.

The decisive finite observation is divisibility. Fix the complete division word and a covered position. Its actual state divides an explicit fixed product of affine carries, and each divisor determines at most one original source. The total division budget is at most \(\lfloor\log_2X\rfloor+2(t-1)\). Summing divisor counts over every word and row, then using an elementary uniform divisor estimate, gives the bound. The argument credits the existing valuation criterion and affine gcd identity; it does not rebrand earlier whole-prefix rank theorems.

A separate pointwise conclusion retains the starting floor. If a covered position occurs in the first \(t\ge3\) states and \(m\) is their minimum, then
\[
 m^{t-1}\le(4^{t-1}x)^{t-2}.
\]
Thus \(x>4^{(t-1)(t-2)}\) forces an actual iterate below \(x\). For three states the test is exact: a covered position exists if and only if \(U^2(x)\mid x\); for \(x>1\) it then gives \(U^2(x)<x\).

Under precisely the external density and phase hypotheses used by PR199 Theorem A, deleting this subpower set preserves the full exponent \(1-1/k\) in **each fixed target's** critical ancestor section. This includes the target one and any hypothetical nonconvergent target. An upper bound on nonconvergent sources in that class is still needed. [Complete proof, finite bound, terminating-prefix construction and literature comparison](analytic/README.md).

## 2. A smaller ordinary source through a larger infinite language

Use the shortcut map \(T(n)=n/2\) for even \(n\), \((3n+1)/2\) for odd \(n\). Write \(L=(2,1)\), \(P=(1,4)\) for two consecutive odd valuations. Their boundary equations are
\[
 8q'=9q+7\quad(L),\qquad32q'=9q+5\quad(P).
\]
The fully kernel-checked `TwoLight.two_light_descent` theorem applies to any one actual infinite input in which paid runs have length one or two, with at least two light blocks between paid runs. At **every original odd phase** it produces a smaller positive odd integer that never reaches one.

The comparison is \(F(q)=(183q+1)/128\). It has exact ordinary returns on the three tiles
\[
 L,\qquad LLP,\qquad LLPP.
\]
Two upcoming light blocks clear its denominator. Three upcoming lights give \(q=1024v-7\), so the single initial partner is
\[
 m=F(q)/2=732v-5,
 \qquad m<q,\qquad m<(3q+1)/4=768v-5.
\]
The same comparison orbit persists through arbitrary future choices in the language. At phases with fewer initial lights, a subsequent paid endpoint supplies the smaller source directly. This retains the original floor throughout the proof.

`ResetTiles.tile_descent` also checks arbitrary infinite concatenations of certified affine returns. Its concrete catalog adds
\[
 LLPLPP,\qquad LLPPPLPLPP,\qquad LLPPPPLLLLP.
\]
These can be mixed indefinitely with the original three tiles, so repeated short gaps, triples and quadruples of paid blocks are allowed. The formal generic theorem includes an entrance divisibility condition. The independently reviewed written phase argument removes that extra condition for this concrete six-tile catalog: at a boundary one has a direct \(LLP\) descent or three lights; in an interior phase there are at most four lights before a paid endpoint.

A separate finite theorem covers every continuation after a long enough sequence of \(PLL\) loops. On an actual prefix \(L^r(PLL)^sP\), \(r\ge3\), the endpoint after the final paid block is below both original odd floors whenever
\[
 5\,9^r729^s\le13\,8^r2048^s.
\]
It is a point of the original trajectory, so every later continuation remains available. These languages and the cone do not cover all possible ordinary inputs. [Proofs, exact scope and the failed unrestricted extension](descent/README.md).

## 3. Integer cycles must be far from balanced words

Let a primitive positive rational shortcut cycle have least binary period \(A\), \(p\) odd inputs and full reduced denominator \(d\). Suppose its parity word can be obtained from a same-weight mechanical word by \(K\) adjacent circular swaps. The written theorem gives
\[
 \log_2 d\ge\frac{A}{4K+2}-O(\sqrt K+\log A).
\]
The proof first establishes an exact finite inequality with \(\eta=(2^A-3^p)/2^A\); only its asymptotic form uses the cited two-logarithm estimate. For an integer cycle this forces
\[
 \boxed{K=\Omega(A^{2/3}).}
\]
If the swaps have disjoint supports, it forces \(K=\Omega(A/\log A)\). Their locations and directions are unrestricted. The noncoprime clock case is included.

The additional ingredient is a quadratic cost for moving ones around the circle. If \(R\) is the range of the net edge flux, then \(R^2\le2K\). This controls the word's cyclic discrepancy, which feeds PR188's full-denominator shift bound. `CyclicFlux.lean` checks the quadratic inequality without a finite search bound. `RotationProduct.lean` checks a separate signed product identity on actual paired closed walks; its valuation budgets are kept distinct from the already-counted matching-run lengths.

Large-transport words remain possible candidates. The conclusion is a restriction on individual hypothetical integer cycles, not their universal exclusion. [Exact theorem, proof and antecedents](cycles/README.md).

A [separate modified-carry construction](cycles/CONGRUENCE_MODEL.md) tests the boundary of congruence arguments. A map can agree with the literal carry one outside a density-zero set and eventually modulo every fixed modulus while having infinitely many integer cycles. On those same words the genuine unit-carry rational cycles retain their full unbounded denominators. The construction changes the map and supplies no Collatz counterexample.

## Verification and reproduction

The combined build used Lean 4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. It rebuilt all seven new modules plus `CycleShadows` and `ResidualDescent` in an initially empty temporary olean directory. Existing Mathlib/package oleans were reused. All 17 selected new transitive axiom inventories contain only standard Lean principles or no axioms.

| Module | Selected roots | Kernel-checked scope |
|---|---:|---|
| `analytic/FixedWord.lean` | 7 | Actual affine/carry identities, covered-row divisor and floor-product bounds |
| `controller/DivisorCount.lean` | 2 | Original-source injection into divisors and finite source-selected union bound |
| `descent/TwoLight.lean` | 1 | All-phase smaller odd nonconverger for the two-light singleton/pair language |
| `descent/ResetTiles.lean` | 2 | General persistent certified-tile theorem and six exact tile certificates |
| `descent/LoopCone.lean` | 1 | Original-floor endpoint inequality through the complete loop cone |
| `cycles/RotationProduct.lean` | 3 | Local mixed factors, path product and closed signed product |
| `cycles/CyclicFlux.lean` | 1 | Unbounded quadratic cyclic flux cost |

The asymptotic divisor estimate, assembly over all division words, critical-section corollary, six-tile all-phase completion, and final cycle asymptotics remain written mathematics. Kernel checking of the finite modules does not certify those entire analytic arguments.

Exact bounded controls separately checked 8,000 odd sources at each of five prefix lengths and 360 prescribed word/target lifts; 1,131 primitive contracting necklaces, 12,282 rotations and 13,413 swap comparisons through period 13; and independent literal checks of the basic comparison chart. These controls support the formulas and their scope, not a universal numerical verification.

Run the fresh-import build in a compatible provisioned environment with:

```sh
python -B research/astra-global-closure-20261124/round3/check_lean.py \
  --lean /path/to/lean \
  --mathlib /path/to/mathlib \
  --report-dir /path/to/receipt-directory
```

[Combined kernel receipt](../../../reports/astra-global-closure-20261124/round3/kernel/receipt.json) · [Root mathematical review](../../../reports/astra-global-closure-20261124/round3/ROOT_REVIEW.md) · [Frozen repository and literature inputs](SOURCES.json) · [60-PR frontier snapshot](../../../reports/astra-global-closure-20261124/round3/frontier-snapshot.json).

## The closing step still required

The three routes now expose different remaining obligations. The merger route needs a smaller ordinary source from the original floor outside the certified languages and finite cone. The divisor route needs an upper bound on nonconvergent critical sources, or a reason a named orbit must meet a covered window early enough. The cycle route needs a pointwise exclusion for words of high transport complexity. Recent first-passage and macroscopic-mixing results were checked against these obligations; their marginal or paired laws do not supply the missing implication automatically.

One attempted positive-offset extension was rejected during cross-review because its proposed long-light condition cannot be realized by a fixed ordinary source in the stated language. Its exact countercalculation is retained with the descent notes. The accepted results above do not use that inference, an iid substitution, or an unproved transfer from density to a single trajectory.
