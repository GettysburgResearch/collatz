# A fixed upper rank cannot set the lower descent deadline

Use the ordinary shortcut map T. A least reverse defect z is the least positive integer in class 17 modulo 48 for which 3z reaches 1 and z fails to reach 1. The established bounded-return theorem places some reverse defect at most 2^40 times any positive nonbasin input. The results below leave open whether a least defect exists.

## Fixed-rank obstruction

For every R≥3, every deadline H and every lower size cutoff L, there is a single ordinary z≥L in the requisite residue whose triple first reaches 1 with exactly R odd inputs. For some q≥H the lower arm takes q consecutive odd steps after clock seven, and z≤128 T^i(z) holds throughout 0≤i≤7+q. This disproves any proposed deadline depending only on R for an actual forward drop below z/2^40. The examples require no assumption that z lies outside the basin. They allow an alternative same-component comparison and a deadline depending on the particular certificate or source.

At R≥4 apply PR197's ordinary word realization with the empty post-ascent word. Its auxiliary count is bounded below by one and above by one irrespective of q. The free count R−4 completes an actual first hit at the required rank. At R=3 use the existing t=1 Mersenne construction. The triple reaches an explicit power of two greater than two in nine clocks with three odds, which excludes an earlier visit to the trivial cycle. On the lower arm every step loses at most a factor of two and the ensuing odd steps increase the current value. These assertions are proved in *FixedRankDeadlines.lean*, theorem `no_rank_deadline`.

## Pointwise clock criterion

Odd inputs at height at least B satisfy 2BT(x)≤(3B+1)x. Even inputs give 2T(x)=x. For q actual odd inputs in h clocks this bounds B^q 2^h T^h(x) above by (3B+1)^q x. An exact small certificate proves that every integer from 1 through 2719 reaches 1. The estimate therefore applies throughout any positive nonbasin orbit for each B≤2720.

At every positive nonbasin x, with no size restriction, these two equivalences hold at the stated endpoint.

- 2^40 T^1024(x)<x if and only if the lower count is at most 620.
- If x=3^r w with w positive, then T^1024(x)<w if and only if the count plus r is at most 646.

The forward implications use the uncorrected lower bound 2^h T^h(x)≥3^q x. The reverse implications use B=226 and B=2720, respectively. In either case the pure integer inequalities are kernel checked. For a least reverse defect z one also obtains the all-clock restriction B^q 2^h≤(3B+1)^q 2^40. Its 1024-step lower count must be at least 621. Among a complete progression of 2^1020 consecutive candidates 48k+17, the first four bits are 1010. The remaining bits run through every 1020-bit word once, by odd-slope lifting after the four forced bits. The fraction passing this necessary count test is exactly 2^(-1020) times the sum of binomial(1020,i) for 619≤i≤1020, approximately 4.55126×10^(-12). It gives no guarantee about the least candidate. *OddClockFloor.lean* and *DefectClockFloor.lean* prove the pointwise and least-defect implications. The residue-population formula has a written derivation and exact integer replay.

## A single sparse binary family visits every ternary residue

Write 27m_t+17=44·2^(18t). Within every block of 3^d consecutive indices t the m_t attain each residue modulo 3^d once. Cubing the identity (2^18)^(3^d)=1+27·3^d(3v+1) proves it at depth d+1. Consequently increasing t by n·3^d changes m_t by 3^d times a coefficient equal to 2n modulo three. All three lifts occur in the next block. The kernel proves the displacement, full blocks and the implication that an eventually total fixed-depth ternary test on this one family must cover the whole original m row in *ShadowTernaryDigits.lean*.

The earlier 214-row bank therefore covers exactly 1000 of 59049 classes of t. In particular t=2034+2187u gives m_t=181 modulo 2187. The original parent z of each such index is excluded as a least reverse defect by an existing positive-cycle comparison: a smaller eligible w reaches the bad Mersenne candidate in 21 clocks, while 3w falls below z/2^40 by clock 224. This conclusion is at the same parent whose two other checkpoints have unbounded initial delays. *ShadowTernaryRescue.lean* and *DefectClockFloor.lean* prove its attachment, using the pre-existing positive-cycle query and unconditional return theorem. This adds a formal application of the original bank.

A numerical decrease t=3u+i to u would compare exponents related by 44²(27m_(3u+i)+17)=2^(18i)(27m_u+17)^3. The identity does not entail a basin implication. An ordinary merger between the two parent sizes needs at least the base-two logarithm of their ratio in total clocks over the two arms. Along the prescribed shadow family, reversing the known −5 and −17 laps returns to the original queries 12·2^j−5 and 27·2^(j−1)−17. Neither supplies a 2^40 drop. At the checkpoints themselves the ternary valuations are zero. The ternary powers in 3^q−5 and 32·3^s−17 are additive terms, so deleting smooth tower powers at these sites does not apply.

## Frozen source comparison

| Source | Pinned path and claim | Scope |
|---|---|---|
| PR197, 156652e03fe7a78f9cd4442039779cc622fdf3de | research/ayh-resource-reset-20261124/source-progress/OrdinaryWordRealization.lean, realization and powerFinish; closing-proposal/MersenneBarrier.lean, mersenne_family; closing-proposal/OppositeArm.lean, family_query; closing-proposal/QuantitativeReturn.lean, bounded_return (paths under the same research directory). | Ordinary source realization, existing positive-cycle row, and bounded return. |
| PR192, 570476be82f706122cdd23ebd7a00f3d4ff90cd8 | research/astra-ultra-closure-20261125/core/ExponentTransport.lean and bridge/PairedReturn.lean. | Count-saving comparisons require specified common paths, residue or positive-reference hypotheses. An exponent-one transport can exit to exponent two. |
| PR195, 5b2bdcb6e4e60da15c29eadff8bd08b3991c5b57 | research/astra-global-closure-20261124/round10/closure/TowerClock.lean, short_cone_iff. | Classifies meetings through H clocks of a 3^r w with r≥2H. Does not produce a heavier word in every prefix fiber. The cycle shift restrictions apply to cycles. |
| PR208, 72635b2a3af2f5b6cbf4eeff7ce1c89b6e6a5f7f | research/openai-machinery-20261125/tensor/TowerFrontier.lean, unbounded_guarded_tower_exclusions. | A genuine smaller-base meeting for arbitrary positive tower exponent on unbounded constructed bases, with prescribed guards. |
| PR209, 2d0230aa52d85732dbc85b5df20e30108dc1396f | research/astra-ultra-closure-20261125/machinery/TowerCertificate.lean, EC1024, TD116 and TU116 in the accompanying README. | EC1024 is pointwise for w≥2^1024. The simultaneous coverage selects bases on which all tower exponents 0 through 115 work. A tower exponent is distinct from the first-hit odd count R in PR197. |

A complete proof would require progress at the supplied remaining least positive reverse defect. The exact-rank theorem excludes one possible uniform stopping mechanism. The count and row exclusions leave that pointwise assertion open.
