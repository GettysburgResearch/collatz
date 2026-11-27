# Root review of the ordinary-source and full-divisor checkpoint

**Verdict: VERIFIED at the written-proof level under the individually stated inputs.** No complete Collatz proof is claimed. This review covers the new packet only, whose exact scientific file hashes are recorded in [SOURCE_HASHES.json](SOURCE_HASHES.json). The prior packets and external Lean packages were not rebuilt.

## Complete divisor arithmetic

The root independently reconstructed ``1–5 of `arithmetic/README.md` and read Corvaja–Zannier's original arXiv:math/0311030v2, especially Proposition 2, its exceptional subgroups, and its displayed Ridout estimate.

The generator \(z\) is formed in the unit group of the **whole** composite modulus. The two power identities follow from Bézout and \(2^A=3^p\); the mask-to-carry identity holds for every term. Reduction modulo \(X^p-1\) gives \(M=S_p[1+(X-1)H]\), so the quotient is integral and evaluates to one at \(X=1\). Evaluation of \((z-1)S_p(z)=1\) removes exactly the always-unit factor.

For the bounded-degree theorem, the finite set of possible monic factors follows from the uniform root bound. A non-torsion unit has an interior conjugate; Jensen's formula controls its multiplicity independently of the mask's size. Splitting-field valuation normalization correctly returns the rational gcd. At places above two and three, the two proposed units have independent fixed valuations, excluding every exceptional subgroup through the identity in Proposition 2. Torsion factors are treated jointly through a fixed set of rational primes, so unbounded multiplicity does not escape the argument. Ridout also supplies the stated leading size of \(|D|\). The theorem is uniform for each fixed degree bound and fixed \(B\), not uniformly in a growing degree bound.

For (2a), Dirichlet approximation gives a relation of length \(O_B(N)\) and discrepancy at most \(p/N\). The resultant is an integral Bézout combination and is nonzero because its rational power value is not an algebraic unit. The case of zero discrepancy is a nonzero constant resultant. Multiplicativity of Mahler measure and the \(L^2\) norm of the zero-one mask give the uniform bound \(\mathcal M(P)\le\sqrt p\), including repeated factors. Optimizing \(N\) proves the printed effective bound and the aggregate high-degree consequence. It does not bound the degree in the opposite direction.

For (4)–(5a), the root checked the carry orientation, extraction of just one factor \(\gcd(H,\Delta)\), prime-power retention, the Parseval normalization, and the use of only active cyclotomic frequencies when \(g\) is composite. The active homogeneous product divides the full \(D\); no coprimality between its factors is needed. The projection argument for the \(g\) distinct binary rotations gives \(g\le2^{n+1}\). The asymptotic exclusions retain both \(g\to\infty\) and \(\log g=o(b)\).

The fixed-source formulas preserve one escaping ordinary starting integer. The corrected height has a convergent product by the named orbit-packing input. The real limit of the periodized prefixes is negative and their dyadic limit is positive, with growing denominators as stated. The exact local-form product does not meet the Subspace Theorem's shrinking-product premise. No contradiction is inferred.

Independent second review: [transfer/REVIEW_ARITHMETIC.md](../../research/astra-ordinary-boundary-20261124/transfer/REVIEW_ARITHMETIC.md).

## The full finite meeting window

The root reconstructed the first-passage duration argument in `transfer/ALL_EVENTUAL_MEETINGS.md` and the lower-clock proof in `MEETING_CLOCKS.md`, consulting the primary first-landing comparison and Shaik's fixed-target theorem.

The duration test is a bounded deterministic function of the first odd landing value, so the relative law's test-independent estimate applies. A prior shortcut landing reaches that odd value by halvings; the proof includes that clock cost. The near-scale binomial calculation has strictly more contraction than required for the \(y^{.99}\) target. The ordinary-source dyadic decomposition discards only the explicitly bounded highly divisible sources.

Every threshold mark is measured at the original source. The geometric sums pay both the duration and the additive errors, without reusing a fresh-source distribution after conditioning on earlier successes. The patch argument transports a **frozen first-hit deadline**, allowing exactly the extra dyadic clock. Normalizing its error is legitimate on the specified resolved patches.

The remaining roots at fixed floor \(K\) form a finite set. For each pair that actually meets, a finite meeting bound exists; the proof needs no way to compute it. Fixing \(K\) before the large-source limit and sending \(K\) to infinity afterwards correctly removes the error. This upper argument survives arbitrary dependence. The early-time exclusion conditions on the entire independently sampled partner trace, uses uniform orbit sparsity, and therefore retains the required independence hypothesis.

The existence and total mass of the component density vector follow by finite-floor approximation and tightness. For independent sources the collision mass is its squared \(\ell^2\) norm. A second positive-density component makes that norm strictly below one. No estimate of this norm, and no summable rate for the correlated-head error, is supplied.

Independent reviews: [arithmetic/REVIEW_MEETING_FRONT.md](../../research/astra-ordinary-boundary-20261124/arithmetic/REVIEW_MEETING_FRONT.md) and [spectral/REVIEW_TRANSFER.md](../../research/astra-ordinary-boundary-20261124/spectral/REVIEW_TRANSFER.md).

## Rare classes, full ordinary futures, and the limiting chart

The root checked the simultaneous binary and odd-modulus source transfer. Its endpoint interval has scale \(Y=3^pX/2^h\), period \(Q=3^pm\), and exact ratio \(Q/Y=q/X\). The endpoint shift changes only \(O(1)\) selected values. Relative normalization therefore does not incur the inverse mass of the selected class.

For the whole-future statement, the test need not be invariant: equality at the common fusion clock implies equality of every later integer endpoint. The same exceptional set works for every endpoint test, which permits taking the total-variation supremum. A first-hit time needs the additional check that the early paths stay above its fixed target; that hypothesis is stated. The comparison retains an ordinary interval source and an explicit time shift.

On adaptive residue-query trees a nonempty transcript leaf is a whole progression cut by the source interval. Uniform relative bounds mix over leaves without a factor for their number. The advice is scale-dependent and cannot inspect the hidden source outside the permitted queries. The explicit all-odd example retains a subpower modulus and has a parity excess larger than the unconditioned square-root clock window; its positive shift and limiting meeting mass follow with the correct independent-source law.

The binary–ternary chart contraction gives a unique stationary joining and the stated finite-cylinder correlation estimate. The mark survives as an independent invariant coordinate in the ordinary empirical limit. No measurable pointwise label on the unmarked limit, or uniqueness of the ordinary component, is deduced. The transient target construction uses actual positive integers and avoids finite defects at the native prefix horizon; it is not an exceptional Collatz orbit.

Independent second review: [transfer/REVIEW_PHYSICAL_TAILS.md](../../research/astra-ordinary-boundary-20261124/transfer/REVIEW_PHYSICAL_TAILS.md).

## Executed evidence

The root ran only the new packet's driver:

```text
python -X utf8 -B research/astra-ordinary-boundary-20261124/check.py \
  --lean /workspace/scratch/cf806951b2d5/runtime/lean-4.34.1-linux/bin/lean \
  --out /workspace/scratch/cf806951b2d5/ordinary-audit
```

It passed all 11 public Lean declarations under `-j1 -DwarningAsError=true`, with source stability and the standard-axiom whitelist checked. Both Python modes returned identical exact-control output. [Kernel receipt](kernel/CHECKS.json)

Repository integrity and publication readback are separate events recorded in the publication receipts. They do not verify any mathematical implication beyond these stated scopes.
