# Coordinating reconstruction of the ordinary entrance law

23 November 2026. **VERIFIED in the displayed written scope.** The
coordinating reviewer coauthored the preceding basin-minimum and
complete-capacity inputs. This review reconstructs the new probability,
phase and change-of-law arguments; it is not external referee acceptance
or independent discovery of those shared inputs.

Source:
`research/lean-exact-witness-global-20261121/profound-step-20261123/pressure/ORDINARY_ENTRANCE_LAW.md`

SHA256:
`e38a7749ca5b7290daf33838586751d46232ca27f414e83fefe847b6ce72f93b`.

## Reconstructed mathematical steps

1. **EL1--EL4.** The nonnegative complete inverse potential is finite
   on the retained escaping component because its path sum equals the
   finite ordinary predecessor mass divided by the positive root weight.
   The identity `Z=1+PZ` gives a stochastic row only after the killing
   probability `1/Z(q)` is included. Multiplying along the unique inverse
   path and then killing cancels every interior potential factor. The
   terminal atom is `r(n)^s/A_s(q)`, with the **starting-root** normalizer.
   These atoms sum to one, proving almost-sure finite killing without
   assuming a finite expected lifetime.
2. **EL5--EL8.** The increasing predecessor sets exhaust exactly the
   original coalescing component. Conditioning its fixed probability
   `mu_s` on these sets gives the stated exact total-variation distance
   and the correctly oriented relative entropy. Injectivity of the ray
   makes `k-m` independent of the chosen merger. The graph map retaining
   both endpoint and phase is injective, so its joint total-variation
   distance is unchanged. The proposed coupling has marginal `nu_j`
   even on the branch where a replacement sample is needed, and
   eventually needs no replacement almost surely. A finite phase is
   tight without any moment assumption. Thus the increasing lifetime
   is compatible with a tight terminal integer.
3. **EL9--EL11.** Split the power-distance sum over the old basin and
   the new mass. The exact expression is
   `[1-(1-d)^(1/s)]^s+d`. Since its first term is at most `d`, the
   complete-capacity root bound gives finite total length in `ell^s`.
   The derivation retains all new atoms and side basins. At `s=2` this
   is finite Hellinger length; it does not give a chronological rate.
4. **EL12--EL15.** The code is the exact full component partition.
   Its order-`1/s` power sum follows from the ray reciprocal budget and
   the complete side-basin root sum. Concavity/Jensen gives finite
   Shannon entropy as stated. The ungrouped terminal source need not
   have finite critical Renyi entropy; the manuscript preserves that
   distinction. The sparse-time example has finite power sums but
   divergent expected logarithmic time, so it correctly rejects the
   proposed conversion from code entropy to a chronological bound.
5. **ST1--ST4.** The balanced tree bijection is over actual unit
   ancestors of the fixed sibling. Its exact weight multiplier yields
   the displayed Radon--Nikodym derivative and normalizer. Holder gives
   the fractional overlap. The negative part of the original signed
   cost is integrable because its positive exponential moment is finite;
   this justifies the displayed extended KL identity. On each finite
   trial support, subtracting `-log R` gives an ordinary nonnegative
   relative entropy. Finite restrictions of the tilted law have gaps
   tending to zero, proving the infimum identity without an unproved
   tightness or full-cost integrability premise.
6. **ST5--ST7.** Conditioning on a fixed finite ordinary source set
   gives the displayed sufficient cost bound, whose existence is
   explicitly open. A uniform cost shift changes the partition function
   while preserving its normalized tilt. The stronger anchored example
   retains zero cost on the root atom: `R=t+t^2-t^3`, its total-variation
   distance is at most `t`, and its density tail integral is at most
   `1/M` for `M>1`. This is an abstract probability control, clearly
   separated from any claim of an actual escaping Collatz realization.

## Primary source normalization checked directly

The reviewer opened Vigon's primary PDF and inspected its actual page
885 (PDF page index 10), including Proposition 3.3 and its proof:
<https://www.numdam.org/item/10.1214/10-AIHP391.pdf>.

The displayed terminal distribution there has `Ug(y)` in its final
denominator. The correct potential-transform calculation has `Ug(x)`,
where `x` is the starting state. Indeed the transformed Green kernel is
`U(x,y) Ug(y)/Ug(x)` and the killing probability at `y` is `g(y)/Ug(y)`.
Their product is `U(x,y)g(y)/Ug(x)`.

For the two-state matrix with its only nonzero entry `P(a,b)=1` and
`g(a)=g(b)=1`, the potential is `Ug=(2,1)`. Starting at `a`, the two
terminal probabilities are `1/2,1/2`. The printed `y` denominator would
give `1/2,1`, whose sum is not one. This is a local printed normalization
correction, not a rejection of the general potential-transform mechanism
or a review of the whole paper. The new manuscript proves its own
correct formula and does not import the printed error.

## Formal and execution boundary

The nine Lean declarations certify finite phase, path and normalization
ingredients. The countable construction, limits, root variation and
entropy arguments above remain written proofs. Root execution records
are kept in `ROOT_REPLAY.json`; this review does not manufacture a
separate execution. The surviving open step is an absolute arithmetic
cost or side-basin mass estimate, not an unrecorded Markov mixing claim.
