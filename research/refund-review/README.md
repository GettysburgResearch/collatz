# Linear-refund review and constructive frontier

**Agent:** `gpt56-refund-01` (`GPT-5.6 Pro`)  
**Issue:** #43  
**Branch:** `agent/gpt56-refund-01/43-linear-refund-invariant`  
**Date:** 2026-07-22

This packet combines three independent tasks:

1. adversarial reconstruction of PR #45's compressed critical-cycle packet;
2. adversarial reconstruction of PR #42 `T-8601`, with an explicit boundary on the unreplayed large finite computation `T-8602`;
3. an integer-first analysis of the linear-height phase-34 quotient-refund architecture.

No positive-integer Collatz counterexample or `K-####` object is claimed.

## Main new result

For linear stage bases

```text
B_n=B_0+4096n,
A(B)=1792B+3657472,
E(B)=2816B+5792512,
```

a coherent ordinary path has canonical quotient coordinates

```text
Y_n=y_n+2^E(B_n+4096) k_n.
```

Once `B_n>=955024` and `k_n>=1`, the exact two-stage refund inequality forces

```text
k_(n+1)>=2 k_n.
```

Thus any already-coherent positive lift path is automatically unbounded. The remaining positive obligation is existence and ordinary top-boundary closure.

## Main method boundary

The refund multiplier is archimedean. For any fixed directive, the future constraints still select one nested dyadic cylinder for the initial quotient. Pairwise positive transitions do not turn the selected inverse-limit point into an ordinary integer.

## Review order

1. `reports/gpt56-refund-01/2026-07-22-41-critical-cycle-adversarial-review.md`
2. `reports/gpt56-refund-01/2026-07-22-9-congruence-sanctuary-review.md`
3. `research/refund-review/claims/L-8201-two-stage-refund-growth.md`
4. `research/refund-review/claims/R-8201-refund-cylinder-firewall.md`
5. `research/refund-review/claims/L-8202-stage-word-residue-sparsity.md`
6. `research/refund-review/claims/Q-8201-causal-top-boundary-compiler.md`
7. `experiments/X-8201-wave-review/README.md`
