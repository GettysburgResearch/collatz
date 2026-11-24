# Independent review of the reverse basin consumer and strict-return estimate

**Verdict: VERIFIED at the two files identified below.** Signed by the PR197 unit-return research agent, 2026-11-24 UTC. I authored the upstream 11-residue localization and separately checked the downstream consumer and entropy argument written by the integration team. The receipt distinguishes those roles.

| Reviewed input | SHA-256 |
|---|---|
| Residue17Closure.lean | 59305b3ef5f0a8706ab7dd3bc3ab48317f630e86c4119ce812fd5634bb5e5d37 |
| STRICT_RETURN_REFINEMENT.md | 59a214f834d3dc50b420f6103ed02a1ed2800828591bab27b55731f08ccd4668 |
| vendor/ReverseBasin.lean | 633af7b92dc57e2296036d4d3e2a71d74b16207ed7e23a325c11c301be5cdf65 |
| DirectedEleven.lean | 7527fb54500831c6cebac3376a3195984d4f414c3df97241a7aa48f91225b677 |
| DirectedElevenLocal.lean | c4ad0e555251d1d14351758ca68a111936fa1dbb67c8e18c3e972d180c78102f |

## Ordinary formal equivalence

I compared vendor/ReverseBasin.lean byte for byte with research/upper-bit-mergers/ReverseBasin.lean at commit f431078244e868dc699fad011044f0d5e7f76437. Both give Git blob a5b56da6e23c2efd0c71d670ac3e275fd7f94567. The source defines the ordinary shortcut on natural numbers. Its predicate Hits at clock zero means equality to 1. Its successor-clock case applies the ordinary shortcut once. Basin is existence of a natural clock with Hits. The left side of the consumer quantifies over every strictly positive natural number, so it is the ordinary Collatz convergence statement.

For the forward implication, universal convergence puts every \(z\equiv17\bmod48\) in the basin because \(z>0\). For the reverse implication, the consumer assumes only \(\forall z\equiv17\bmod48,\ B(3z)\Rightarrow B(z)\). The imported binary criterion then asks for \(B(32k+1)\Rightarrow B(16k+1)\) at every \(k\ge0\). A failure gives the ordered labels false, true at \(16k+1,3(16k+1)\): the ordinary path connecting \(3(16k+1)\) and \(32k+1\) passes through \(27k+2\). The complete pointwise localization gives the identical order at \(z,3z\) for one positive \(z\equiv17\bmod48\). Its actual basin membership contradicts the restricted implication at that same \(z\). The proof uses neither a counting estimate nor a hypothesis about any other residue. The restricted basin implication remains open.

I freshly compiled the copied vendor and consumer in a separate scratch directory against my previously compiled, hash-matching DirectedEleven, DirectedElevenLocal, UnitResidueExchange and NonunitExit objects. Both compilation commands used Lean 4.34.1 (5045d0056413266e57c625dcd7c365b10e377c52), the pinned Mathlib environment, \(-j1\), autoImplicit=false and warningAsError=true. Exit code was 0. The kernel reported exactly propext, Classical.choice and Quot.sound for both Residue17Closure.localize_seventeen and Residue17Closure.collatz_iff_reverse_seventeen.

## Fixed contraction at the entropy threshold

For a positive \(n\) of color different from \(f(1)\), the pinned reverse-basin descent supplies a path to 1 in contracting batches. Each batch uses at most 61 expanded moves and starts no higher than its predecessor. Consequently its changing forward tripling has source \(v\le K n\), uniformly over all batches. Its ordered colors are different-from-\(f(1)\), then \(f(1)\). The two ordinary nonunit successors and the new finite substitution preserve that order. The \(11\leftrightarrow17\) exchange also preserves it and has bounded height ratio. One constant \(K_0\) is valid for both target classes simultaneously.

For \(k=\lfloor\log_2X\rfloor\), fix \(0<q<1\) and \(C_q\) as in the proposed theorem. A parity path with \(p\) odd steps has slope \(3^p/2^k\). Its positive additive term is at most \((3/2)^k-1\), by induction with maximal additive update \(E\mapsto(3E+1)/2\). Both original rays start below \(6X\). If both \(p\)'s are at most \(k\log_32-C_q\), the larger endpoint is at most \(6X3^{-C_q}+o(X)\). Once \(X\) is sufficiently large, either endpoint is below \(qX/K_0\). They have different labels when the initial pair is a defect.

Each length-\(k\) parity word occurs on a single source residue modulo \(2^k\). The substitution \(x\mapsto3x\) also permutes that grid. Every original octave has bounded occupancy per residue; using both ray tails costs at most their sum. The first excluded odd count is \(ks+O_q(1)\) for \(s=\log_32>1/2\). Stirling bounds its coefficient by \(O_q(2^{kh_2(s)}/\sqrt{k})\); bounded index shifts only change the constant, since \(s\) is strictly interior. Subsequent coefficients form an upper geometric tail, their ratios tending at its left endpoint to \((1-s)/s<1\). This yields \(O_q(X^{h_2(s)}/\sqrt{\log X})\) original exceptions. I checked \(s=0.6309297535714574\), \(h_2(s)=0.9499555271883305>0.84\). This proof bounds a source census only. A chosen smaller witness may lie in the next exceptional set, and distinct sources may have identical witnesses.

The high-stakes boundary is explicit in both reviewed files: the kernel equivalence has an unproved reverse implication as its right side, and the written strict-return theorem has an exceptional population and no transport multiplicity bound.
