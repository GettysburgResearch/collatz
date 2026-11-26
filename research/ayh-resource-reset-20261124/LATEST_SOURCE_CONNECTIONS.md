# Publication-time comparison with PRs 192–196

The initial inventory froze the frontier through PR 191. A final remote read found five further packets. Their PR descriptions were read; the source statements below received additional focused reconstruction by the root and the three existing agents. This is not a full audit of those branches, and their author's Lean counts are not added to this packet's counts.

## PR 196 supplies a smaller marked partner

At `10fcd50c45c219d8f794034f8d46d127d86e562c`, `research/astra-orbit-cycle-20261124/mergers/TWO_ANCHOR_MERGERS.md` and `HalfSource.lean` state the half-size merger for **every** positive exact valuation `H >= 1`; the separate extra-clock obstruction assumes `H >= 2`. Retaining that distinction exposes the useful case here.

For a source in our marked section with excess at least eight, `n > 1` forces `n = 5 mod 8`. Consequently `H = v₂(n+1) = 1`, and the half-size theorem's successful congruence holds. The even partner `(n-1)/2` immediately halves to the odd partner `(n-1)/4`, which stays in the mark and reduces the exact excess by eight. This yields the new closed eight-excess equivalence in `CriticalSection.lean`. The proof is direct arithmetic and imports no code or theorem from PR 196. Its source is credited for the connection.

The written [critical-section proof](positive-section/CRITICAL_SECTION.md) further establishes uniqueness per next odd value and cofinal representatives of the same original target. Convergence inside the boundary remains open. It contains infinitely many starting integers, including unbounded sources at each of its eight excess values.

[Frozen PR 196 merger source](https://github.com/GettysburgResearch/collatz/blob/10fcd50c45c219d8f794034f8d46d127d86e562c/research/astra-orbit-cycle-20261124/mergers/TWO_ANCHOR_MERGERS.md).

## PR 193's guarded partners do not complete the induction

At `c6cb5e66516a86c33a757154983bbddc822510de`, `research/astra-universal-descent-20261124/shadow.md` and `ShadowCore.lean:guarded_certificate` supply

\[
n=3^h u,\quad 3^{h+4}\mid1+2\,4^h u,\quad
m=\frac{2^{h+5}(1+2\,4^h u)}{3^{h+4}}-1<n,
\]

for positive odd `u`, with a physical merger at `T(n)`. At height zero the required class is `n = 121 mod 162`. The binary valuation condition in our section does not imply that odd-modulus guard. Chinese remaindering with `n = 1 mod 81`, inside sufficiently long marked intervals, gives arbitrarily large unguarded section members.

Even on the overlap, the displayed partner is `-1 mod 32`, so its exact valuation `v₂(3m+1)` is one. Every such partner at least 32 lies outside the marked-power section. There is also a quantitative obstruction to using this partner to beat the original target in our inverse rows. Since `3^h <= n` and `(9/8)^9 < 3`,

\[
m+1\ge\frac{64}{81}(8/9)^h n
\ge\frac{64}{81}n^{8/9}.
\]

For sufficiently large `n` this partner exceeds the already supplied endpoint `v <= 4 n^(4/5)`. In our construction `v >= q`, so it also exceeds the original target `q`. This is a written comparison of these two specified constructions. It does not exclude other partners or later endpoints.

[Frozen PR 193 source](https://github.com/GettysburgResearch/collatz/blob/c6cb5e66516a86c33a757154983bbddc822510de/research/astra-universal-descent-20261124/shadow.md).

## PR 195's direct source family is disjoint

At `a24ef018147a1e16bf314d14085e2d0d6c620d32`, `research/astra-global-closure-20261124/structural/CycleShadows.lean` and its README give `n = 2^(33k)u-17`, `m = 2^(21k)u-1`, with positive `k = 148 mod 256`, a supplied divisibility guard, and a long physical merger.

Both displayed integers are `3 mod 4`, with exact valuation one in their respective `3x+1`. Every marked-power source at least 32 has valuation at least two, hence is `1 mod 4`. The direct families are disjoint. A later orbit state may satisfy the guard; neither source proves this for every required marked input, or that the resulting partner lies below the original marked source rather than merely below that later state. The arbitrary finite-radius construction in PR 195 is not a universal coverage theorem.

[Frozen PR 195 source](https://github.com/GettysburgResearch/collatz/blob/a24ef018147a1e16bf314d14085e2d0d6c620d32/research/astra-global-closure-20261124/structural/README.md).

PR 192 at `be783656f0e889fe0d5318a2f7a9140099cb94b5` and PR 194 at `b1bf1f151a2da8936f80d229f132d0b7539ba42c` were read at metadata/claim-summary level in this late check. No theorem from those two packets is a dependency of this checkpoint.
