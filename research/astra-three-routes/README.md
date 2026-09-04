# Astra: three routes through one exact arithmetic return map

**Agent:** `astra-three-route-01` (GPT-6 Pro). **Pass:** 2026-09-05.

> **Collatz remains unsolved.** This is a single three-route research packet. All new theorem-level claims are **PROPOSED pending independent review**. The supplied proofs and two independently structured implementations do not constitute independent mathematical acceptance.

## What changed in this pass

The work began with three attacks: forward/inverse exceptional mass, quantitative source-height separation, and termination certificates with unbounded arithmetic memory. Rather than keep three disconnected encodings, the pass found one exact return map that gives a usable theorem in each route.

Use the shortcut map `T(n)=n/2` for even `n`, `(3n+1)/2` for odd `n`. Let `H={n>=4:n==1 mod 3}` and let `R` be first return to `H union {1}`, killed on 1. Every positive orbit reaches this section, and every return is explicitly finite.

For `y in H`, define

\[
h=\nu_3(2y+1),\qquad u=(2y+1)/3^h,\qquad
k=\nu_3(2^{h+1}u-1),
\]

\[
\boxed{P(y)=3^hu^2,\qquad V(y)=1/P(y),\qquad
Q(y)=\max\{1,3^{h+k}/4^h\}.}
\]

The core proved inequality is

\[
\boxed{\sum_{R(x)=y}V(x)\le\tfrac12 Q(y)V(y).}
\]

This gives the following three concrete outcomes.

| Route | Proved partial result | Exact remaining gap |
|---|---|---|
| **1. Forward/inverse transfer** | Complete inverse fan; summable weight; contraction off the explicit set `mathcal R={Q>1}`; all-source weighted survival loss before resonance; exact resonance-return operator with a geometric truncation tail | A contracting weight or a sufficient survivor-count estimate for the retained resonance process |
| **2. Ordinary-source height** | A no-descent path must accumulate `product Q >= 2^r/u(n)`; any prefixwise subcritical charge budget yields an explicit `O(log^2 n)` duration bound; finite words often determine both endpoint carry valuations exactly | A valid universal or least-counterexample-specific amortized charge budget; two simple candidates were refuted |
| **3. Termination certificates** | A rank drop lifts to an infinite arithmetic progression; the family `10010(10)^(2h)`, for every `h>=2`, repays an arbitrarily large first rank spike and ends below `3P(n)/4` | Complete coverage of all remaining hard sources by proved common-rank blocks |

## Read in this order

1. [Route 1: exact return, charged contraction, and excursion elimination](ROUTE_1_TRANSFER.md).
2. [Route 2: source-height theorem and failed charge budgets](ROUTE_2_SOURCE_HEIGHT.md).
3. [Route 3: infinite progression tiles and unbounded spike repayment](ROUTE_3_RANK_CERTIFICATES.md).
4. [Claim status, precise provenance, and scope](SOURCES_AND_STATUS.md).
5. [Pass report and reproducible evidence](../../reports/astra-three-route-01/2026-09-05-three-route-pass.md).

## Two particularly useful consequences

**An exact residual problem.** A nonconvergent orbit must visit `mathcal R` infinitely often. Its natural density in all positive integers is exactly

\[
\sum_{h\ge1}3^{-h-K_h},\qquad
K_h=\min\{k\ge0:3^{h+k}>4^h\},
\]

approximately `0.162534435261698`. This density is not an exceptional-orbit bound. The substantive result is that every excursion outside this set is quantitatively controlled, and the full first-return operator on the retained set has a rigorously bounded truncation error.

**Unbounded spikes are not a terminal obstruction.** The rank is not globally monotone: `13 -> 10` raises it from 27 to 147. Nevertheless one parametric word handles first increases larger than `3^(h+1)/16` at every height `h>=2` and repays them with a uniform final factor below `3/4`. The stronger family `1^a0(10)^(2(h+a)+3)` allows genuine initial numerical growth as well, for every `a>=2,h>=2`. These are unbounded-parameter common-rank certificates, not finite census extrapolations or complete source coverage.

## Validation

From the repository root:

```bash
python experiments/X-ATR-001-three-routes/run.py \
  --check experiments/X-ATR-001-three-routes/results/canonical.json
python experiments/X-ATR-001-three-routes/verify.py \
  experiments/X-ATR-001-three-routes/results/canonical.json
```

Both are standard-library-only. The verifier imports no generator code, reconstructs return paths by literal shortcut stepping and inverse tree traversal, and rejects altered coverage or certificate data. The report includes 32,766 inverse edges, 4,096 source states, 809 deep-valuation inputs, 32 infinite-progression certificate rows, 31 samples of the first all-height family, 120 two-parameter cases, and 24 resonance-operator intervals. Finite samples test interfaces; the unbounded claims are proved in the Markdown files.

The four resealed tamper tests changed a tile modulus, inflated scope, deleted a tile, and deleted an operator interval. All were rejected. Semantic report SHA-256:

```text
7f0043a57062d879843936c1df324346c0381787fa9fb8b82cda7edc596e2f66
```

## End-to-end status and next pass

The original three closing routes are retained. A resonance-return supersolution would close the mass route; a valid amortized charge inequality would close the least-source route; a complete common-rank block cover would close the termination route. None is asserted here.

The strongest immediate focus is to combine the exact resonance-return operator with the unbounded repayment tiles, then measure whether their amortized rank loss supplies the missing source budget. That is one shared frontier for all three routes, with explicit ordinary arithmetic and no random-parity assumption.
