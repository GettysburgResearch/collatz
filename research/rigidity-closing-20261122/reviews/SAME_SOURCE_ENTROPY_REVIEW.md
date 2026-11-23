# Independent review: same-source inverse entropy

Reviewed file:
`collatz_work/rigidity_attack/SAME_SOURCE_INVERSE_ENTROPY.md`

Reviewed SHA256:
`cacbb6d3f2ab8e8bc54c15d215806ce79eeabdc9d291593565b93cc9a166f7e2`

Reviewer: the independent canonical-path/Harnack lane, 2026-11-22.

**Verdict: the finite coupling and entropy deductions are valid under the
stated positive bounded ordinary harmonic-flow input and the imported finite
actual-source entropy bound.** This review does not certify the construction
of that flow, the cited external analytic inputs, or a proof of Collatz.

## Exact endpoint law and capacity limit

The non-eventually-periodic actual ray is injective. An inverse endpoint
`q_k` reached in `r` steps from `q_(r+j)` must satisfy
`q_(r+k) = q_(r+j)`, so `k=j`. The deterministic forward map also makes
the path to that endpoint unique. Its telescoping weight is
`v_j / v_(r+j)`. Therefore (7a) gives exactly the mass on the entire
forward ray. On the support of `π_M`, the inverse endpoint law is
pointwise dominated by `π_M`; its remaining mass lies off the forward
ray. This proves the exact endpoint TV identity, not merely a projection
bound.

For fixed `M`, monotonicity of `v` makes every summand of `ε_(M,r)`
increase with `r`, and convergence `v_j → C > 0` gives its limit. Thus
`sup_r ε_(M,r) = η_M`, while Cesàro convergence gives `η_M → 0`.
All labels and the original orbit remain unchanged. The inverse depth
can be arbitrarily large relative to `M`.

## Finite-alphabet continuity, equations (8)–(9)

The proposed coupling agrees on successful complete retracing. Adjoining
the binary failure indicator gives conditional entropy at most
`h_b(ε) + ε log(3^m)` in both directions, even when a failed path has the
same ternary endpoint. Subtracting the two entropy chain rules proves
(8); keeping the root label proves (9). Ordinary endpoint TV is exact,
but the ternary projection may reduce TV, as the final text now states.

The replacement of the actual error `ε_(M,r)` by its uniform bound `η_M`
is made only after `η_M ≤ 1/2`. Binary entropy is increasing on this
interval, so that replacement is valid. No global monotonicity of binary
entropy has been assumed.

## Boundary terms and the growing-precision limit, equations (10)–(12)

For `1 ≤ m ≤ M`, precisely `m` of the `M+1` sampled times precede time
`m`. Their probability is `t=m/(M+1)`, and their entropy modulo `3^m`
is at most `m log 3`. The remaining `M-m+1` endpoints have the finite
actual-source bound with average-gap budget `A_M/(M-m+1)`. Adjoining
the split indicator yields exactly (10), including both mixture weights.

For any positive integer sequence `m_M=o(M)`, eventually `1≤m_M≤M`,
`t→0`, and
`limsup A_M/(M-m_M+1) ≤ log_2 3`. The function `Φ` is continuous and
increasing on `[1,∞)`, with the continuous value `Φ(1)=0`. All entropy
error terms divided by `m_M log 3` vanish: positivity `m_M≥1` bounds
the binary-entropy terms, and `t,η_M→0` handle the remaining terms.
These bounds are independent of `r`, which justifies the displayed
`sup_r` in (12). Fixed positive precision is included.

## Closing criterion and scope

For the same endpoint laws, Shannon entropy is at least the negative
logarithm of the collision sum. Thus (13), if proved with the stated
precision and clock choices, contradicts (12). Equation (13) is
explicitly unproved. No invariance under separate dilations, Feller
property, almost-everywhere boundary conclusion, or fixed-root mixing
rate is inserted into the finite proof.

The two requested textual refinements—distinguishing ordinary from
ternary endpoint TV, and naming monotonicity of `Φ`—are present in the
bound final source. No mathematical correction to (8)–(12) was required.
