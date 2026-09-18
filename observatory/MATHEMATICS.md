# Mathematical contracts for the investigation preview

**Evidence level: exact bounded computations and software fixtures. No new global Collatz theorem is asserted.** Repository definitions are inherited with their scope; a successful computation does not upgrade a historical claim's review status.

## Provenance

Research baseline: `main @ ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
Application source baseline: PR #119 at `f0bf47d9c4253c3a16617f4b70388a7a4ba4e1de`.

Definitions follow the pinned [conventions](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/integrated/CONVENTIONS.md), with [errata](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/integrated/ERRATA.md) retained. The explicit moving-rank/module formula is from [MOVING_GHOST_RANK.md](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/astra-three-routes/pass4/MOVING_GHOST_RANK.md). Original source-stage status and later resident scoped review are distinct; this application does not adjudicate a proof by displaying it.

## Carries and cross-clock meetings

For odd n, let input bits be `u_j`, shifted bits `u_(j-1)` with `u_-1=0`, and inject `c_0=1`. Then

```
s_j = u_j + u_(j-1) + c_j
v_j = s_j mod 2
c_(j+1) = floor(s_j/2)
```

The `v_j` are the bits of `3n+1`. A carry motif counts **outgoing propagated carries**, not the injected +1 as a separate run position. For even n, the actual raw operation is halving and no addition carries are assigned. A carry-difference row is defined only when both selected branches are odd additions. Bit columns retain absolute powers of two even when the view is cropped.

Each displayed trace supplies exact raw-clock anchors. Dense raw support independently replays only the actually computed displayed support, including hidden intermediates, then applies separate storage/step bounds. Common-state detection compares integer strings produced from exact integers, never approximate coordinates. Both displayed-support and raw-support intersections are available. Null displayed arrival means the exact raw value is not an anchor in that acceleration.

Meeting order is increasing maximum of the two raw arrivals, then their sum, then A's arrival. It is a documented ordering of finite witnesses, not simultaneity or a global minimal-merger theorem. No state is extrapolated beyond the stopped or computed support. A displayed anchor outside the dense raw prefix is inspectable exactly without asserting that all intervening raw states have been retained.

## Motif trials

The finite population is the exact progression `seed + j*stride`, for `0 <= j < count`, with a specified bit flip or offset partner. Every member is retained. Predicates are carry-run threshold, valuation threshold on an odd branch, or a fixed shortcut prefix (including the trivial-cycle continuation for that **feature**, explicitly separate from stopped target traces).

Targets are:

- the two **stopped raw prefixes** share a state with both raw arrivals no greater than the configured horizon; or
- A has a displayed raw state below its source by that horizon.

For these bounded predicates a fully computed horizon is complete even when ordinary orbit convergence is not known. A bit/storage/time limit is different: absent a positive witness, the relevant target is unknown. A known positive witness can establish the finite target even when later computation is truncated. An unknown feature remains unfinished. The result labels support, counterexample, control_pass, control_fail, unfinished and invalid_partner separately.

No p-values, independent-sample claims, held-out predictive accuracy or causal interpretation are produced. Prefix features can include later information; meeting alignment is retrospective. Shared trajectory suffixes invalidate naive independent train/test splits. These experiments are structured falsification of bounded implications, not evidence that a pattern proves Collatz.

## Affine drift and the two ranks

For shortcut source n0 and k transitions with q odd branches,

```
2^k T^k(n0) = 3^q n0 + B
D = 2^k - 3^q
d = T^k(n0) - n0
B = D*n0 + 2^k*d
```

Every plotted prefix is checked against the first identity exactly. Coefficient crossing means `3^q < 2^k`; physical descent means `T^k(n0) < n0`. They are recorded separately. `B=0` is processed algebraically; no logarithm of zero is used.

The section/global rank is

```
h(n) = v3(2n+1)
P(n) = (2n+1)^2 / 3^h(n)
```

The moving-envelope rank uses

```
z_a(n) = 3^a(n+1) - 2^a(2n+1)
R_a(n) = z_a(n)^2 / 3^v3(z_a(n)), with R_a=0 for z_a=0
R*(n) = min(R_0,R_1,R_2), also including R_h when h>=3
```

The finite evaluation formula is inherited from the source. Tests compare it to a larger finite direct dictionary for small inputs, not to every index for all n. Neither rank is asserted globally decreasing, and comparisons of P and R* do not transfer a theorem between them.

## Maximal repeated-word modules

For n>1, let `a=0` for even n and `a=v2(n+1)` for odd n; put

```
Q=3^a, P=2^(a+1), d=Q-P, c=Q-2^a, z=d*n+c
k=floor(v2(abs(z))/(a+1))
z_next=Q^k * (z/P^k)
A(n)=(z_next-c)/d
```

The emitted shortcut block is `(1^a0)^k`, with shortcut cost `k(a+1)` and raw cost `k(2a+1)`. n=1 is separately absorbed. Integrality and positivity are checked; small fixtures independently replay every branch and maximality.

The two tests `4 R*(A(n)) <= R*(n)` and `R*(A(n)) <= R*(n)` remain distinct. Examples include `7 -> 13`, rank `12 -> 36`, and `577363 -> 649534`, rank `50808384 -> 7144929`. These are finite witnesses, not unsafe-return control or an exhaustive lower-rank certificate selector. Module caps constrain **endpoints**, not omitted raw peaks.

## Transport

Initial source mass is uniform on a finite progression. The implementation advances the actual members; a merged endpoint retains its source multiplicity. At each completed frame:

```
alive + killed + unresolved = initial source count
```

Residue arrays and rank mass use those weights. They are not statistics of the set of distinct endpoints or a fresh resampled shell. A selected floor kills values at represented shortcut times. Module transport permits **floor=1 only**: an arbitrary floor could be crossed inside a hidden module. General fixed-floor module crossing is not inferred from endpoints.

Module safe and nonincreasing membership uses each actual endpoint's next module, with unresolved membership recorded when its endpoint exceeds the configured bound. These weights are not assigned to shortcut transport under another clock. On interruption only complete frames are authoritative; there is no partial-row mass loss masquerading as transport.

## Blocks, roots and cycles

For a shortcut word w, store `(L,q,B)` for `(3^q n+B)/2^L`. For w then v:

```
B_wv = 3^qv B_w + 2^Lw B_v
```

Binary exponentiation composes repeated blocks; total expanded length remains bounded. Periodic candidate `B/(2^L-3^q)` uses the complete denominator. The implementation replays **every** branch of the bounded expanded word over exact rationals, even when only 64 replay states are displayed. A rational parity is defined only at an odd denominator. Selected modular probes never replace the full denominator or branch replay.

The source cylinder is a residue modulo `2^L`; canonical zero and the least **positive** representative differ. A growing list of finite roots is not one all-time ordinary source. `1110` gives periodic rational candidate `-19/11`; its positive finite-prefix witnesses are not that rational completion. The UI root plot covers at most 512 prefixes and explicitly labels that scope; it is not the entire 4,096-step composed word's root history.

Odd-valuation candidates independently retain the system identity (`3n+1`, `3n-1`, or `5n+1`) and full denominator. Replay checks positivity, oddness, exact valuations and return. Positive controls include `5 -> 7 -> 5` in `3n-1` and `13 -> 33 -> 83 -> 13` in `5n+1`. A control cycle is never labeled a positive Collatz counterexample.

## Evidence boundary

`verify.py` is a small separate raw/accelerated replay checker for `collatz-meeting/v1`; it imports no main arithmetic provider. It authenticates the finite equality and clocks, not global truth or novelty. Unit tests, browser interactions, fingerprints and exact arithmetic each establish different facts. No visual pattern, digest, test count or imported repository claim changes the project's unresolved mathematical status.
