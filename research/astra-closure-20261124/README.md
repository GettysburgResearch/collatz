# Global arithmetic and physical first-passage attacks

**Status: proposed written theorems, independently reconstructed at recorded hashes, and nineteen new Lean-checked arithmetic declarations. Collatz remains OPEN.** This continuation of PR193 applies Mahler's theorem, the Subspace Theorem and the Evertse–Schlickewei–Schmidt unit-equation theorem to ordinary local minima. It also combines the latest first-passage work with an all-depth inverse-repayment estimate. Four Astra 6.2 workers developed or reviewed these routes. The analytic proofs and recent external inputs have separate evidence levels from the accompanying Lean formalization.

The base is PR193 head `a1379492dbaae85e0d16662b41ccc7176ab3c66e`. The final intake includes the new PR192, PR182 and PR201 checkpoints and PR197's first-passage results. [Repository inputs](LATEST_CONNECTIONS.md) · [Literature](SOURCES.md) · [Verification](../../reports/astra-closure-20261124/VERIFICATION.md).

## 1. Global restrictions on consecutive local minima

Use the shortcut map \(T(n)=n/2\) for even \(n\), \(T(n)=(3n+1)/2\) for odd \(n\). Starting at odd \(x\), take its \(k=v_2(x+1)\) consecutive odd steps, then its \(l\ge1\) consecutive even steps to the next odd \(y=V(x)\). This complete segment is a *mountain*, with exact equation

\[
2^{k+l}y=3^kx+3^k-2^k.
\]

On a cycle its entries are the local minima. [The arithmetic proof](arithmetic/README.md) establishes these written results.

**Finitely many dependent edges in the whole positive integer graph.** If \(x,y>1\) are multiplicatively dependent, write \(x=b^s,y=b^t\) in their common primitive integer base. The target must be \(y=b\). Put \(U=2^k,W=3^k,c=(W-U)/b\). The edge forces

\[
0<c/U<(3/4)^k,\qquad W+c\equiv0\pmod U.
\]

Mahler leaves finitely many \(k\). Each determines at most one \(b\); the unit-equation bound below leaves finitely many sources for that base. Every sufficiently late pair of minima on a hypothetical escaping positive orbit is therefore multiplicatively independent. Every nontrivial ordinary cycle contains an independent pair: rank-one minima would reduce it to Steiner's excluded one-mountain case.

A dependent edge also forces the strict exceptional branch of the ideal Waring inequality. The published computation reported by Habsieger excludes \(k\le471{,}600{,}000\). This is an imported computation, not a local replay or proof that the exceptional set is empty.

**A uniform count with all run lengths unrestricted.** For fixed \(h\ge1\), finite-rank groups \(G_0,G_1\subset\mathbb Q_{>0}^{\times}\), and fixed rational cosets \(a_0G_0,a_1G_1\),

\[
\#\{x>0\text{ odd}:x\in a_0G_0,\ V^h(x)\in a_1G_1\}
\le B_h(r_0+r_1).
\]

The explicit finite bound depends only on \(h\) and the ranks. Odd/even run lengths, prime supports and coset representatives are unrestricted. The proof retains all signed carry terms and checks every possible vanishing subsum. Their joint variable group has rank at most \(r_0+r_1+2h\). First-small-valley splitting covers all ordinary sources.

A positive proportion of \(N\) distinct minima must generate rank at least \(c_\delta\log N-O_\delta(1)\). On escape, gaps between visits to a fixed finite union of finite-rank cosets tend to infinity in *mountain time*. Together with the classical fixed-minima theorem, the bound gives finitely many primitive cycles at each fixed bound on the rank of all their minima.

**Common factors are small at every edge.** Evertse's fixed-prime corollary applied to the primitive equation

\[
3^k(x/g)+(3^k-2^k)/g=2^{k+l}(y/g),\qquad g=\gcd(x,y),
\]

gives, uniformly as \(x\to\infty\),

\[
g\le\sqrt y\,x^{o(1)},\qquad x/g\ge x^{1-\frac12\log_2 3-o(1)}.
\]

This bounds the full numerical gcd without a fixed prime pool, while permitting new target factors. No contrary upper bound on the rank of arbitrary escaping minima has been proved.

[Independent review](transfer/REVIEW_ARITHMETIC.md) · [Six Lean kernels](arithmetic/MountainReturns.lean) · [Latest inverse-minimum comparison](arithmetic/LATEST_ARITHMETIC.md).

## 2. All-depth repayment on actual first roots

Fix \(K>0\) and a finite/countable family \(\mathcal W\) of finite positive odd-gap prefixes. Let \(V_K(\mathcal W)\) consist of odd targets \(q\) admitting a positive odd ancestor \(z\le Kq\) whose path starts with a word in \(\mathcal W\), followed by arbitrarily many further steps. Let \(u(\mathcal W)=\sum_{a\in\mathcal W}2^{-|a|}\), where \(|a|\) is its gap sum.

[The repayment theorem](descent/REPAYMENT.md) proves that the relative odd natural density exists, equals the Haar measure of the union of the legal finite ternary cylinders, and is at most \(CKu(\mathcal W)\). It controls all later visits by complete orbit unions and an exponential fixed-clock image bound, then pays free inverse continuation by a renewal estimate. Additive carry, overlaps and cycles remain included.

The [finite-cutoff strengthening](transfer/REVIEW_DESCENT.md#a-quantitative-combination-for-original-two-arm-sources) is uniform even for families changing with the target cutoff:

\[
|V_K(\mathcal W)\cap[1,M]|\ll_K
M\bigl(u(\mathcal W)+M^{-\eta}\bigr)
\]

for absolute \(\eta>0\). At \(R=81^j,\ d=\log_2R,\ M=d^D\), combining it with the actual head-root marginal bounds the fraction of original children with such an odd landing on either arm by

\[
O_{A,K}\!\left(d^{-A}+\sqrt d(\log d)^{3/2}
[u(\mathcal W)+M^{-\eta}]\right).
\]

For \(u(\mathcal W)\le d^{-2}\) and sufficiently large fixed \(D\), this is summable across head levels. Arbitrary further routing is already included. A closing argument would still have to force discordant roots into this rare event.

The exact inverse inequality \(3^h(z+1)\ge2^h(q+1)\) also identifies the original-floor cost of PR193's preceding critical arms. An all-ones inverse returning below an integer floor \(F\) requires \(2^h\le F\) and \(q+1\le F^{\log_2 3}\). Increasing ternary precision cannot remove that cost. A recent source-qualified router improves the prefix/residue overhead to linear precision cost when the merger horizon can grow; it supplies no original-floor descent.

## 3. Actual joint first-passage laws

For \(x\in[7R,8R)\), parent \(m=\lfloor x/81\rfloor\), and actual first shortcut landing \(P_M\), [HEAD_ROOTS.md](transfer/HEAD_ROOTS.md) proves:

- For every \(\log_2\sqrt3<\alpha<1\), defined unequal roots at \(M=R^\alpha\) number \(\Theta_\alpha(R/\sqrt j)\). One subset works simultaneously at every higher real barrier. This nonsummable literal inequality is compatible with Collatz being true.
- At a sufficiently large polylogarithmic barrier, the landing pair uniquely encodes the differences of the stopped clocks and odd-step counts.
- On any population of at least \(pR\) retained regular children, its joint law \(J\) and its own marginals satisfy

\[
d_{\rm TV}(J,J_1\otimes J_2)
\ge1-O_A\!\left(\frac{d(\log d)^3}{pM}\right).
\]

Mutual information is at least \(\log(pM)-\log d-3\log\log d-O_A(1)\). The unconditioned law is mostly diagonal by early fusion. This support information does not estimate different-component labels.

The independent review repaired a conditioning issue: the version with no \(p\) factor needs PR197's high timely mass. For an arbitrary clock cap the population-dependent version is necessary; the explicit counterexample is preserved.

[Independent review](arithmetic/REVIEW_HEAD_ROOTS.md) · [Five Lean kernels](transfer/PhysicalReturn.lean).

## 4. Returns and the direction of passage

[RETURNS.md](transfer/RETURNS.md), conditional on the named relative-landing and barrier inputs, bounds the probability of a rebound above \(Y^{1.004}\) between the first passages below \(Y\) and \(K\) by

\[
O_A((\log K)^{-A}+Y^{1.001}/R+Y^{-\gamma}).
\]

For power-sized \(Y\) and \(K=\exp((\log R)^\delta)\), this is summable over geometric levels even after a fixed polylogarithmic weight. The all-future bounded-orbit contribution tends to zero by a finite-cap argument. Escaping mass remains.

The [same-source crossing theorem](boundary/CROSSINGS.md) refutes an unmarked reverse transfer: explicit sets at the polylogarithmic ceilings have a summable first-downward-landing probability and a nonsummable **last-upward-crossing** probability. Every source in the lower bound reaches one and returns below the ceiling after that crossing. The proof uses a ceiling-sensitive future mark, CRT and transport into the literal head.

An escaping ray instead makes a permanent departure, with no subsequent return. No estimate here excludes that event. [Independent boundary review](transfer/REVIEW_BOUNDARY.md) · [Three Lean identities](boundary/BarrierExit.lean).

## 5. The unrestricted closing attempts

[GLOBAL_ATTEMPT.md](boundary/GLOBAL_ATTEMPT.md) retains PR192's complete shifted moment and PR201's killed Green reduction. It tests an adelic affine boundary and asynchronous removal of the surviving head imbalance. The latter introduces compulsory binary digits and does not supply the required fresh additive pair law.

[LATEST_ARITHMETIC.md](arithmetic/LATEST_ARITHMETIC.md) preserves specified finite inverse-clock legality/carry tests and an entire finite gcd matrix while making all selected odd values independent. The source changes with the finite tests. This gives no rank upper bound at one fixed source over unbounded horizons.

Universal original-floor descent, vanishing of the full survivor moment, and summability on PR201's remaining mesoscopic profiles are still unproved. None is assumed.

## Reproduction

```sh
python -B research/astra-closure-20261124/check.py \
  --lean /absolute/path/to/lean \
  --out /absolute/path/outside/the/scientific/packet
```

Official Lean 4.34.1 accepted nineteen public declarations in four Std-only modules, with warnings as errors and axiom queries. Only `propext`, `Classical.choice` and `Quot.sound` appeared. Three finite-control programs passed normally and with optimization, with identical paired output. Earlier bundles and external libraries were not rebuilt.

[VERIFICATION.md](../../reports/astra-closure-20261124/VERIFICATION.md) links hashes, receipts, compiler logs, independent reviews and the separate repository-integrity check. Infinite analytic deductions remain written proofs at their stated hypotheses.
