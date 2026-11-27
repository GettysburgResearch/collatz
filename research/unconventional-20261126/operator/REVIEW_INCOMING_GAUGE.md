# Independent review of the incoming-slope integral test

**Verdict.** VERIFIED for all eventually nondecreasing doubling $\psi$ in the statement, assuming OP-U2 as proved in the pinned operator file. This includes infinite measure at $\psi(q)=\sqrt q$. The original strict power threshold does not use the endpoint argument.

| Reviewed file at PR201 base `94ce06ccbd312ccd0ce4450b567cc514a2f0b54a` | SHA-256 |
|---|---|
| `../renewal/INCOMING_GAUGE_TEST.md` | `8469f7f6fb26fcad6a83b59735c440106b94553d1a021f856f3d3357ac479678` |
| `UNRESTRICTED_GAUGE.md` | `74e455ba41cda2453b4d21a6cc1ef14b3aa04278f6a705f97d2fcf639e5c30c6` |
| `TERNARY_BARRIER.md` | `0d480c5b713f9df6c095168c74979b4381a688d30cf8b6d1a8691137216d3b18` |

The convergence half requires only a first-passage cover and the centered one-sided survival estimate. A geometric shell of lengths from $4^l$ to $4^{l+1}$ contributes at most a fixed multiple of $(1+L)\psi(4^l)2^{-l}$ by doubling. The first-passage overshoot contributes the factor $e^{-hL}$, and the radii tend uniformly to zero.

For divergence, the restricted events $G_N$ for $N=4^l$ are disjoint. OP-U2 supplies a uniformly positive multiple of $N^{-1/2}$ for each, even with both the fixed overshoot range and the occupation restriction. Thus the total normalization can exceed any earlier likelihood bound by summing a finite range in the divergent tail. For a partial prefix of length $r$, events with $N\le2r$ are jointly bounded by probability one, with maximum weight $\psi(2r)$. Each larger $N$ requires survival through time $N-1$ and contributes at most $C(1+|s|)\psi(N)/\sqrt N$ at current local level $s$. Because the normalizer dominates $c\sum\psi(N)/\sqrt N$, the latter losses are uniform. These two arguments control prefixes even immediately after a long previous block.

The stage choices are deterministic and finite, so their previous maximal cumulative likelihood bounds are finite. The reset at stage $j-1$ bounds the actual completed ratio by $e^{-(j-1)^2}\psi(m_{j-1})$; the next reset controls its ratio to $Z_j$ by $e^{-j^2}$. A word has unique first-ladder parsing, so the two bounds combine into (U7) without repeated branching factors. At odd depth $q$ and fixed total clock the carry decoding is injective. The accumulated weighted occupation is at most $Kj e^{O(j)}$, and negative total log slope reduces the word mass by $e^{hS}$ against the multiplicity factor $e^{-S}$. Since $h>1$, summing over every possible binary clock is uniform after multiplication by the polynomial loss from $\psi(k)/\psi(q)$ and the local-distance factor. The remaining $e^{-(j-1)^2+O(j)}$ is summable. For large $q$ all possible prefixes must have reached arbitrarily high stage indices, since each fixed finite union of stages has a finite maximum length. The resulting cell mass divided by its gauge therefore tends to zero uniformly. The direct mass distribution argument gives infinite Hausdorff measure without increasing the gauge afterward.

The endpoint normalization by reweighting first-ladder lengths was identified independently in the operator and renewal lanes. The renewal proof treats general doubling weights and gives the full integral criterion. The wording-only clarification to the original draft makes explicit that the exceptional set has no positive ordinary integer.
