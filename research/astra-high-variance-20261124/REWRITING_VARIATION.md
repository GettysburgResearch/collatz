# A finite variation budget for changing affine shadows

**Written theorem.** Two infinite injective ordinary shortcut trajectories are sampled at increasing macro boundaries. Assume that corresponding finite macros contain the same number of odd inputs. If they also contain the same total number of shortcuts, the sequence of logarithms of the ratios of their shifted heights Y+7 and q+7 has finite total variation, with an absolute bound independent of the two sources, the segmentation, and the initial ratio. With unequal raw clocks there is an exact integer clock correction to this statement. Neither arm needs to coalesce with the other.

This addresses positive expanding shadows such as those in DESCENT_MACRO.md, where a multiplier greater than one is affordable because its comparison starts below the original floor. It controls changes of the multiplier; the single constant multiplier used there has zero cost in this observable. The new assertion concerns whole infinite injective trajectories. An indefinitely repeated hypothetical nonstandard positive cycle falls outside its hypotheses.

## Ordinary source budget

For one shortcut input x of parity b=0 or 1, set T(x)=(3^b x+b)/2. With natural logarithms, exactly

    ln(T(x)+7) − ln(x+7) = b ln 3 − ln 2 + e_b(x),
    e_b(x) = ln(1+(b+14−7·3^b)/(3^b(x+7))).

At an even input this correction is ln(1+7/(x+7)); at an odd input it is ln(1−2/(x+7)). In both cases its absolute value is ≤7/x by the elementary logarithm inequalities. The signs differ, so keep absolute values.

The positive odd states of an injective shortcut trajectory form an admissible set for the common-odd-clock packing theorem of PR193. Its count below X is O(X^θ/√log(2X)) with θ=H₂(log 2/log 3)<1 and an absolute constant. Consequently their reciprocal sum is bounded absolutely. To include even states, group every run of even inputs with its next odd q. The even reciprocals are at most (1/2+1/4+…) /q. This also includes a possible initial even run. An infinite positive orbit cannot end in an infinite even run. Hence the total shortcut reciprocal sum is at most twice the sum over its odd states. This proves a uniform absolute bound on the sum of |e_b(x)| on the entire trajectory. Only the packing input is external to this calculation. [PR193, escape.md §§1a–1b](https://github.com/GettysburgResearch/collatz/blob/c6cb5e66516a86c33a757154983bbddc822510de/research/astra-universal-descent-20261124/escape.md).

## Two paths with arbitrary macro lengths

Let q_j,Y_j be the respective positive boundary states. Denote the numbers of shortcuts in the j-th macro by a_j and d_j; its number of odd inputs is the same on both paths. Put

    v_j = ln((Y_j+7)/(q_j+7)),
    h_j = Σ_{i<j}(d_i−a_i).

Subtracting the two telescopes proves

    Σ_j |(v_{j+1}−v_j)+(d_j−a_j)ln 2| ≤ C.                   (1)

The bound is absolute because each arm's macros use disjoint successive shortcut intervals. Thus v_j+h_j ln 2 has finite total variation and converges to a finite real number. Equivalently 2^{h_j}(Y_j+7)/(q_j+7) tends to a positive finite limit. Projecting v_j onto the circle of circumference ln 2 gives finite total circular variation even when h_j is unbounded. The proof permits arbitrary positive finite macro lengths, arbitrarily large initial sources, and unbounded gaps between odd inputs.

In particular, if a_j=d_j and Y_j=λ_j(q_j+7)−7, then Σ|ln λ_{j+1}−ln λ_j|≤C. Any palette with positive minimum separation η in logarithms has at most C/η changes along the entire execution. A finite palette therefore eventually uses just one multiplier. More generally, a finite palette with unequal clocks eventually lies in one dyadic equivalence class (ratios integral powers of 2). Indeed between distinct classes the circular distance is bounded below away from zero. Within a fixed finite palette, eventually each remaining ratio switch is *exactly* compensated by the local dyadic clock mismatch: there are only finitely many values of Δv within the palette, and a nonzero residual Δv+k ln 2 has a positive minimum absolute value among these values and integers k. Equation (1) permits only finitely many nonzero residuals. Even bounded but repeatedly changing cumulative clock offsets can thus support dyadically equivalent switches. Unbounded cumulative mismatch is not necessary for that possibility.

If the source is injective and the shadow is produced by a fixed finite palette of strictly positive slopes in this affine relation, then Y_j→∞ because q_j→∞. This forces the ordinary target trajectory to be injective too. Thus separate injectivity of the target need not be assumed in that particular application. If one path cycles, direct use of the infinite reciprocal estimate is unjustified.

## A short incompatible switch forces a small actual state

Allow the odd counts to differ as well. Fix a finite palette of positive rational multipliers and one actual pair of finite ordinary paths, with boundary relations Y+7=λ(q+7) at the start and Y'+7=μ(q'+7) at the end. Let A,B be their respective shortcut lengths, p,u their odd counts, L=A+B≥1, and H the smallest positive input along either segment (endpoints may also be included). Unless the multiplier change exactly compensates the two clocks, there are effective palette-dependent constants C and κ such that

    H ≤ C (1+L)^{κ+1}.                                           (2)

Indeed, the nonzero real linear form Λ=ln(μ/λ)−(u−p)ln 3+(B−A)ln 2 equals the difference of the two accumulated ordinary corrections. Thus |Λ|≤7L/H. On the other hand Matveev's Corollary 2.3 applied to the fixed rational bases μ/λ, 3 and 2 gives |Λ|≥c(1+L)^{−κ}: the two clock coefficients have absolute values at most L, the first coefficient is one and the finitely many heights are fixed. When μ=λ omit its zero logarithm; cases with vanishing clock coefficients can likewise use fewer logarithms or a fixed nonzero constant. Take the worst constants over the finite palette. This proves (2) on a single tile without any infinite-orbit assumption. If its two arms are known to be nonconverging and C(1+L)^{κ+1} is smaller than the proposed original floor, an actual state on one of them falls below that floor. Its odd part is a positive odd nonconverger no larger than that state. In particular polylogarithmic L in a growing original floor is eventually sufficient, if such an incompatible switch can actually be constructed.

The companion ARITHMETIC_MACRO.md gives the global source-dependent switch bound obtained independently by both lanes: on disjoint intervals of two injective trajectories, the same nonzero linear forms charge the summable variation budget. Thus the sum of (1+L)^{−κ} over incompatible switches is bounded, and Jensen's inequality bounds their number by O(T^{κ/(κ+1)}) through combined clock T. Congruent switches with exact compensation have zero charge. The finite-source implication (2) is independent of this global argument. No bound is known forcing every hypothetical least source to admit even one such nonconverging switch at the required clock. [Matveev, Corollary 2.3, p. 1219](https://www.mathnet.ru/links/11696330cc866d273c92c771a63da235/im314_eng.pdf).

## Why cylinder universality does not move a surviving path into a new sector

For the exact L/P alphabet, TCP-5 already gives the positive comparison (60q+5)/83 for arbitrary clustering when 83 divides q+7; that theorem is not new here. The section theorem of REWRITING_FRONT.md measures arbitrary eventual-intersection components in every finite leading-phase/gap cylinder. It does not ensure a specified infinite physical itinerary within such a component.

There is a specific arithmetic obstruction to combining those statements by prepending a finite segment. For an infinite concatenation of L=(2,1) and P=(1,4), its alignment into blocks is forced even on the ultimate tail: a pair crossing a block boundary belongs to {(1,2),(1,1),(4,2),(4,1)}, disjoint from {L,P}. If two ordinary odd trajectories meet eventually and both have infinite L/P tails, their block boundaries must therefore align after the meeting. On every boundary edge with P-indicator b, the shifted numerator q+7 satisfies 2^{3+2b}(q'+7)=9(q+7)+166b. Its vanishing modulo 83 is invariant in both directions. Consequently the guarded and unguarded infinite L/P tails cannot occur in the same eventual-intersection component, although any finite prefix of prescribed gap and phase type can occur in that component. The same observation applies to all shift-invariant eventual-language obstructions after a merger. [PR191, TCP-5](https://github.com/GettysburgResearch/collatz/blob/37b3916633cd32a0c173b20bb18ec3a7ec290a63/research/two-sided-cycle-packing-20261124/README.md).

A concrete remaining option for unguarded infinite paths is a comparison with infinitely many nonconstant intercepts or convergent, continuously varying slopes. To close by that method one needs actual integral target iterates at every step and a comparison beginning below the originally specified floor. Equation (1) supplies the necessary source budget, not those target iterates. The forced rotation at the leading end does not decide the full trailing gap schedule. No coverage of every positive source or every unguarded L/P path follows.
