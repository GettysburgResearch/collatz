# X-8703 — Exact centered height renewal

**Experiment ID:** `X-8703`  
**Agent:** `gpt56-sol-02`  
**Issue:** #40  
**Classification:** `EMPIRICAL` exact finite computation  
**Associated claim:** `L-8702` (`PROPOSED`, elementary proof pending review)  
**Random seed:** none

## Question

For the partial exact recurrence

\[
64B_{n+1}=81B_n+e_n-e_{n+1},\qquad e_n\in\{0,1\},
\]

construct a compact affine atlas from one height band

\[
H/64\le B_0<H
\]

to the first crossing \(H\le B_t<64H\). Enumerate every binary word through
the universal bound \(t\le18\), but do not store a million large affine
records.

The recurrence is partial. This atlas covers exactly the initialized states
whose forced tail remains legal until a crossing; it does **not** cover states
that fail first, and it does not establish an infinite survivor.

## Exact formulas

For a word \(e_0\ldots e_t\), define

\[
D_j=\sum_{i=0}^{j-1}81^{j-1-i}64^i(e_i-e_{i+1}).
\]

The unique integrality residue and affine orbit are

\[
r=[-81^{-t}D_t]\bmod64^t,\qquad
B_0=r+64^tQ,
\]

\[
c_j=\frac{81^jr+D_j}{64^j},\qquad
B_j=c_j+81^j64^{t-j}Q.
\]

All \(c_j\) are integral. The first-crossing conditions reduce to

\[
Q\in\mathbb Z\cap[L,U),
\]

where

\[
L=\max\left\{
\frac{H-64r}{64^{t+1}},
\frac{H-c_t}{81^t}
\right\},
\]

\[
U=\min\left(
\left\{\frac{H-c_j}{81^j64^{t-j}}:0\le j<t\right\}
\cup
\left\{\frac{64H-c_t}{81^t}\right\}
\right).
\]

Thus the stored integer interval is exactly
`[ceil(L), ceil(U))`. Strict upper bounds require `ceil(U)`, not
`floor(U)`; this matters when an endpoint is integral or negative.

`L-8702` proves these identities and the 18-step bound independently of the
finite run. The bound combines \(D_{18}\ge-81^{17}\) for \(H\ge11\) with
the exact minimum positive branch increment \(4\) for \(1\le H<11\).

## Canonical finite scope

The formulas accept any positive integer `H`. A frozen finite artifact needs a
specific height, so the canonical run chooses

```text
H = 64^18 = 324518553658426726783156020576256
t = 1,...,18
words at depth t = every e_0...e_t in lexicographic binary order
total words = 2^20 - 4 = 1,048,572
```

This choice aligns the largest congruence modulus \(64^{18}\) with the top of
the height band. It is a reproducibility convention, not a claim that this
height is dynamically distinguished.

## Storage and independent verification

`build.py` streams each chart. It retains:

- exact per-depth counts and interval-width summaries;
- SHA-256 digests of all charts and of nonempty charts;
- first, last, and first-widest nonempty charts at every represented depth;
- exact probes at `Q_start-1`, `Q_start`, `Q_stop-1`, and `Q_stop`.

The digest projection and canonical JSON encoding are recorded in
`canonical.json`. No full chart list is materialized.

`verify.py` does not import `build.py`. It independently uses the closed
modular residue sum, direct recurrence replay from both \(r\) and
\(r+64^t\), exact rational comparisons, fresh aggregate counts, fresh
digests, and fresh representative selection.

## Canonical result

```text
all words:                    1,048,572
nonempty affine charts:         344,613
represented (B_0,e_0) states:
  4,364,569,155,216,182,243,127,889,516,389

all-chart digest:
  f92e9b079019becf4ad9996e7f473c4ce8f86be71909a9ff690cb110799f1144
retained-chart digest:
  94e3e331fb0b9efa0899551354c8781a9039bd57999340b7b19adb8b728b0ed4
semantic digest:
  d751531e8e59f7a232a49baeadb6e1cf098cfc34e0ef281bd2ad883dfe8f5e08
artifact digest:
  f4188cf4dda110a04d59fbed7526cfb4c518bafab64f45a3dcd341104137b712
```

Every word has a nonempty integer interval through depth 16. At depth 17,
`81,243` of `262,144` words remain, each representing one state. At depth 18,
`1,230` of `524,288` words remain, again with singleton intervals. Thus the
finite run contains exact depth-18 witnesses and confirms that the proved
upper bound is attained at this height.

The first stored depth-18 boundary certificate is

```text
word = 0000000000000110101
Q = 0
B_0 = 5670112270801773814566451412992
B_17 = 311012197201478980395098656046641 < H
B_18 = 393624812083121834562546736559030 >= H
```

This is a finite crossing certificate, not an infinite forced tail.

## Replay

From the repository root:

```bash
python3 -B experiments/X-8703-centered-height-renewal/build.py \
  --height-power 18 --max-steps 18 \
  --output /tmp/X-8703-canonical.json \
  --check-results \
  experiments/X-8703-centered-height-renewal/results/canonical.json

python3 -B experiments/X-8703-centered-height-renewal/verify.py \
  experiments/X-8703-centered-height-renewal/results/canonical.json

python3 -m unittest \
  experiments/X-8703-centered-height-renewal/test_renewal.py -v
```

Recorded environment and timings:

```text
CPython 3.12.3
Linux 6.12.94+ x86_64, glibc 2.39
full build:  30.247 s wall
full verify: 51.515 s wall
tests:        0.043 s wall, 9 passed
```

## Test coverage

The tests cover:

1. the defining \(D_j\) sum and direct recurrence replay;
2. every affine \(c_j\) and slope on all words through test depth five;
3. exact ceiling behavior for positive, integral, and negative endpoints;
4. both included interval endpoints and both excluded neighboring integers;
5. first-crossing inequalities and itinerary replay;
6. both exact pieces of the universal 18-step proof;
7. a brute-force deterministic partition at `H=64^2`, horizon four;
8. independent-verifier acceptance;
9. deterministic digest regeneration and tamper rejection, including tampering
   followed by recomputation of both outer digests.

## Classification and limitations

- **Proved elementary identities (claim status `PROPOSED`):** the iterated
  recurrence, residue class, integrality of every \(c_j\), affine interval,
  deterministic partition of crossing survivors, and universal 18-step bound
  are proved in `L-8702`. Repository promotion still requires review.
- **Finite computation (`EMPIRICAL`):** all canonical counts, digests, active
  endpoint frequencies, and depth-18 examples concern only `H=64^18`.
- **Not established:** the experiment does not show renewal compatibility
  across infinitely many height bands, an all-time legal ordinary seed, or a
  physical Collatz counterexample.
- Existentially choosing a fresh `Q` in each band would not preserve one
  ordinary trajectory and would repeat the completion-versus-ordinary error
  identified by `R-8701`.
