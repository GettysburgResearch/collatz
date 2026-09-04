# Astra three-route research pass — 2026-09-05

**Agent:** `astra-three-route-01` (GPT-6 Pro).

**Request:** pursue all three end-to-end routes and publish one research PR. **Outcome:** proofs of partial results in all three routes, one shared exact arithmetic section, two independent implementations, and an explicit residual problem. **No complete Collatz proof was obtained.** All new theorem-level claims remain PROPOSED pending independent review.

Base main: `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`. The fresh PR query found #90 at `aeb69ce631370be36fd1f80b472ab448e7df2a73`, in addition to #87 and #88 from the earlier assessment. The new packet credits that work and starts directly from main without changing it.

## 1. Research development and strongest results

The initial mass attack retained PR #90's summable-weight idea but changed the arithmetic section and affine form. Exact elimination of the intermediate `2 mod 3` states produced a complete inverse fan at `H={n>=4:n==1 mod 3}`. That fan made the rank

```text
P(n) = (2n+1)^2 / 3^v3(2n+1)
```

natural. The resulting charged inequality is `KV<=QV/2`, where the endpoint charge is explicit in two ternary valuations. It gives deterministic, quantitatively bounded entry into resonance or 1 and a geometric all-source weighted bound for excursions avoiding resonance. The full resonance-return operator has a proved tail bound for adaptive finite truncations.

The same inequality supplies an ordinary no-descent source budget: `product Q>=2^r/u(n)`. Under a prefixwise subcritical budget, the available shortcut duration is explicitly `O(log^2 n)`. This is a source bound, unlike an ambient entropy count, but the universal budget remains unproved. Two plausible polynomial startup budgets were tested and refuted by exact small paths; both are retained.

The termination attack then used the **same** rank. A single finite rank drop lifts to an infinite arithmetic progression because the transformed affine correction is strictly positive and the source/end valuations are fixed. More substantially, `10010(10)^(2h)` repays a first rank increase exceeding `3^(h+1)/16` and ends below `3P(n)/4`, for every `h>=2` and every legal ordinary source at that height. CRT proves these classes are nonempty at every height. The two-parameter strengthening `1^a0(10)^(2(h+a)+3)` includes initial numerical growth for every `a>=2`. Universal coverage by such blocks remains open.

## 2. Failed strengthenings preserved

- `P(R(n))<P(n)` is false: `13 -> 10` raises rank from 27 to 147.
- The same example prevents the unmodified `V=1/P` from being a nonexpanding resonance-return supersolution.
- `product Q <= P(n)*(3/2)^r` fails at `n=31,r=4`.
- `product Q <= P(n)^4*(3/2)^r` fails as a global trajectory budget at `n=121,r=11`; its no-descent-only restriction is not refuted by that path, whose first return descends.
- A finite collection of progression tiles is not a complete source cover.
- Exponential weighted loss before entering resonance is not fixed-floor convergence or a power saving for eternal exceptional sources.

These failures guide the next attack toward amortized resonant excursions; they are not interpreted as evidence against Collatz.

## 3. Checks actually run

From the locally materialized packet root:

```bash
python experiments/X-ATR-001-three-routes/run.py \
  --write experiments/X-ATR-001-three-routes/results/canonical.json
python experiments/X-ATR-001-three-routes/run.py \
  --check experiments/X-ATR-001-three-routes/results/canonical.json
python experiments/X-ATR-001-three-routes/verify.py \
  experiments/X-ATR-001-three-routes/results/canonical.json
python -m py_compile experiments/X-ATR-001-three-routes/run.py \
  experiments/X-ATR-001-three-routes/verify.py
```

Both implementations use only the standard library. The verifier does not import the generator. It uses literal shortcut forward stepping, a separate reverse-tree traversal, and independently reconstructed certificate equations. Both programs were authored in this session: this is **implementation independence, not independent mathematical review**.

| Check | Exact finite scope / result |
|---|---|
| Inverse fan / kernel | 16,384 endpoints through 49,153; 32,766 inverse edges |
| Deep valuations | 809 separate inputs, including height through 32 and second-carry probes through 24 |
| Forward first returns | 4,096 hard sources through 12,289 |
| Nonresonant endpoints | 8,395 in the inverse-fan range; all pass the charged contraction |
| Source pressure | 3,025 completed no-descent prefixes |
| Endpoint jets | 28,666 frozen pairs, 11,187 explicitly unfrozen pairs |
| Progression tiles | 32 exact finite certificate rows, each with a proved infinite-family interpretation |
| Parametric repayment | 31 one-parameter and 120 two-parameter CRT cases; all-parameter proofs are separate |
| Excursion operator | 24 exact lower/upper intervals, six resonant targets and four truncation depths |
| Finite rank-drop pilot | All 4,096 sources found a drop or 1 within cap 128; maximum 76 shortcut steps at 4,009 |

The finite pilot is hypothesis-generation/regression data, not global coverage. Every reported bound retains the exact source range and clock. The resonance density interval is instead backed by an analytic tail for **all omitted valuation heights**; the numerical cutoff alone is not its proof.

The first excursion fixture accidentally included a nonresonant target and was rejected by the explicit precondition; it was replaced by resonant target 37 before the final report. A mistyped command-line flag was also corrected. These were development errors, not failed mathematical conclusions; final generation and replay pass.

Four semantic tamper tests recomputed the checksum after the mutation, so rejection did not rely merely on a stale digest:

```text
tile modulus changed to 1:       REJECTED
scope inflated to global proof: REJECTED
one operator interval deleted: REJECTED
one progression tile deleted: REJECTED
```

Frozen semantic SHA-256:

```text
7f0043a57062d879843936c1df324346c0381787fa9fb8b82cda7edc596e2f66
```

No full external Lean build, large predecessor payload replay, broad cycle search, full-repository structural validator, or workflow was run. Validation here is of the new local packet, not an authenticated full repository checkout.

## 4. Publication and review boundary

This PR adds only the isolated research packet, its two checkers and frozen report, and this pass report. Main, other contributors' branches, canonical result statuses, repository settings, permissions, and workflow configuration are unchanged. The final PR metadata and Git tree record provide the exact published head; no mutable branch name is used as a mathematical source pin for predecessor work.

Review [the packet README](../../research/astra-three-routes/README.md), then Route 1's inverse fan and tail, Route 2's source-budget hypotheses, and Route 3's all-height repayment proof. The highest-risk issue is not a finite arithmetic mismatch but an accidental promotion of resonance absorption or partial block coverage into full termination.

## 5. One next-pass handoff

Work on the **first-return process on resonance**, using the exact tail-controlled operator to locate difficult return families and the unbounded repayment theorem to remove them with one common rank. The desired next result is an amortized rank or mass inequality with a complete coverage argument; increasing the finite source range without such an argument will not close any of the three routes.
