# PR 206 at the live refresh

Reviewed the [pull request](https://github.com/GettysburgResearch/collatz/pull/206) and six source blobs at `45a6a111321f947a8482c9e96e898435b57cee09`. The earlier comparison used `b2b56b94175174a680a296478f16c619a8828972`. This review checks source statements, proof structure, and byte identities. The upstream check is a separate build from the PR 197 execution receipts.

## Where the 513 ranks occur

For every fixed odd positive integer $w$ and every chosen starting rank $s$, `recurring_common_endpoint` gives a single offset $d\le 2^{1379}$ and a single endpoint $y<3^{s+d}w$ such that

$$
T^{1381}(3^{s+d+r}w)=y\qquad(0\le r\le512).
$$

Here $T$ is the shortcut map. Two affine residue classes modulo $2^{1381}$ carry 513 mergers each. Multiplication by a suitable power of three takes $3^s w$ into one of those classes. Thus the base remains the given $w$ throughout. The location of the block on its tower depends on $w,s$. The height comparison is with the first vertex of that block. The theorem gives no bound $y<w$ and does not determine whether $y$ reaches 1. [Merger proof](https://github.com/GettysburgResearch/collatz/blob/45a6a111321f947a8482c9e96e898435b57cee09/research/clock-itineraries/TowerFrontierMergers.lean)

## Which implication remains open

Write $B_r$ for the truth of “$3^r w$ reaches 1,” and $D_r$ for disagreement between $B_r$ and $B_{r+1}$. The theorem `universal_iff_recurring_changes` gives

$$
\mathrm{Universal}\iff
  \forall\,w\text{ odd},\quad D_0\Longrightarrow
  \forall s\;\exists i<512,\ D_{s+i}.
$$

Under the recurrence premise the common-endpoint block yields a contradiction, because all 512 of its edges have equal basin labels. The least-source reduction in PR 197 supplies precisely an initial $D_0$ at its odd witness. The missing inference is that a disagreement at that witness reappears inside the shifted merging block. As a check on the quantifiers, the abstract sequence $B_0=\mathrm{false}, B_r=\mathrm{true}$ for all $r\ge1$ has a rank-zero change and constant blocks of every length after every starting rank. This is an example of a label sequence only. It makes no claim about a realized Collatz tower. [Recurrence criterion](https://github.com/GettysburgResearch/collatz/blob/45a6a111321f947a8482c9e96e898435b57cee09/research/clock-itineraries/TowerRecurrence.lean)

The same module makes the arbitrary-length common-block premise explicit in `universal_iff_syndetic_changes`. The companion note gives a written extension for each prescribed finite length from PR 146. Even if that extension is granted, constant blocks of arbitrary length still coexist with the abstract single-change sequence. In the other direction, `prescribed_rank_obstruction` allows any fixed edge $r$, deadline $H$, and threshold $L$, then produces a base $w>L$ at which the two trajectories are disjoint through all pairs of clocks up to $H$. The base in this obstruction may vary with $r,H,L$. [Tower frontier](https://github.com/GettysburgResearch/collatz/blob/45a6a111321f947a8482c9e96e898435b57cee09/research/clock-itineraries/TowerFrontier.md) · [Prescribed-edge obstruction](https://github.com/GettysburgResearch/collatz/blob/45a6a111321f947a8482c9e96e898435b57cee09/research/clock-itineraries/TowerFrontierPrescribed.lean)

The separate `universal_iff_bounded_clocks_and_cycle_tests` also retains two obligations. Each eligible odd source requires its own finite bound on $3^k/2^{\mathrm{elapsed}(k,a)}$ for every $k$, and there must be arbitrarily large $b$ with `witnessTest b = false`. [November proposal](https://github.com/GettysburgResearch/collatz/blob/45a6a111321f947a8482c9e96e898435b57cee09/research/clock-itineraries/NovemberProposal.lean) · [Upstream scope](https://github.com/GettysburgResearch/collatz/blob/45a6a111321f947a8482c9e96e898435b57cee09/research/clock-itineraries/November25.md)

## Exact source identities

Every path below is relative to `research/clock-itineraries/` at the reviewed head. Both digests were recomputed from each retrieved source's UTF-8 bytes. The Git object identifiers matched all six provider results.

| File | Git blob SHA-1 | SHA-256 |
| --- | --- | --- |
| TowerFrontierMergers.lean | `2aee18b60726053842e3b18d2e279f271e5144da` | `6cea45face03093df3cd7f2f72a3c79c1f899be17cda35724953bf4ba18d2bb4` |
| TowerRecurrence.lean | `a6b6737fdc671ba298da3b7c74523cecc1b4a6e7` | `e246069b78fb1d004b855fc15b19a2b61cb2d3474b626eddf1104310ff82b1fc` |
| TowerFrontierPrescribed.lean | `dad1195b442f8a81f93defd061d8ac4f6fbc791f` | `f1cd37679ccb9a87a7750af2a5726caad7017574711db03333bf37ebe840671a` |
| TowerFrontier.md | `5e4a7ba2be67054c20f7d477b7908001d262006a` | `09ce69a8c5d312abd92c6738702f634666eb66475b751f31b6103f5d1ba61e67` |
| NovemberProposal.lean | `5f3bea94f335cca19c3d8bcbd9b6f908bd0d53bc` | `cb32ff1c2038d10c5c961c074dec56047042cdd30b06e76afd113d69fe1fa90b` |
| November25.md | `51ee88c236aa43d7fef6db0d69ad8690f4d41fa0` | `0b03a1dddd1882c8f892ab581026212eedf404ccb1f90c87268914ba09fdcba9` |
