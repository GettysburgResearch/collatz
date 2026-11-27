# Original Syracuse collisions on positive odd representatives

**SOURCE-QUALIFIED / OPEN.** Throughout this lane the exponents have
the original independent law \(\Pr(e=j)=2^{-j}\), and transport on
positive integers uses the actual odd Collatz map. The following written
results isolate ordinary escape and prove quantitative laws for genuine
inverse fibres. A full proof of sublinear collision energy remains open.

| Written result | Scope |
|---|---|
| [The fixed-root and moving-root clocks](ROOT_CLOCKS.md) | At every fixed positive odd unit, the exact central-total density converges to the integer trace. Along an escaping source's \(j\)-th forward state, the actual conditional total at depth \(n=j+d\) has law \(A_j+\operatorname{NB}_d+o_{\rm TV}(1)\). Agreement with the unconditioned clock requires \(n/j^2\to\infty\) when \(j,d\to\infty\). |
| [Pointwise corrected-height multiplicities](LOCAL_HEIGHT_LAW.md) | On each escaping component, the number of sites at the exact height \(P_0(4/3)^n\) is asymptotic to \(H_C P_0(4/3)^n/\sqrt{4\pi n}\). The quantitative estimate holds over the whole corrected-height lattice. |
| [Marked fibres and the backward grade law](MARKED_FIBRES.md) | Retaining the native clock identifies each signed output class with an exact corrected height. Its minimum gives a detector independent of the two-sided stationary profile. The trit imbalance is summable and drives a geometric convolution on grades. |
| [Summable physical-source cancellation](PHYSICAL_SOURCE.md) | The actual signed source on every high dyadic octave loses superpolynomially in its logarithmic height in joint endpoint and clock norm. All positive starting sites are included. |
| [The depth difference](DEPTH_DIFFERENCE.md) | The unscaled physical sum norm, supremum norm and signed sum of the consecutive-depth difference each have an actual ordinary limit. The last equals \(\sum_C H_C\). |
| [Source occupation](SOURCE_OCCUPATION.md) and [logarithmic harmonics](LOG_HARMONICS.md) | A fixed summable source bounds first-meeting occupation on translated intervals. Nonzero mantissa harmonics cancel at a quantified range of frequencies. Last-bit tests still require localization. |

The external estimates include Tao's natural-depth mixing, Weaver–Wren's
extra-digit joint mixing, the positive-integer trace and first-hit inputs
quoted at each use, and the previously pinned component profile. The
full quantifiers and the transition from a finite word to a positive
ordinary source are set out in the respective proofs.
[PR 193, pinned original two-copy law](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/global/COLLISION_ENERGY.md)

[Finite Lean kernels](CollisionOccupation.lean) verify first-hit
simplicity, fixed-source domination, propagation under contraction, the
centered-trit identity, simultaneous-clock uniqueness, the ordinary
gap-one parent at a height minimum, and the finite harmonic telescope.
The [exact integer and rational replay](check_marked.py) checks the
marked endpoint formula against direct positive starts and the geometric
forcing recurrence on three actual finite inverse trees.
[Lean receipt](../../../reports/astra-six-hour-20261127/collision/lean_replay.json) · [Arithmetic receipt](../../../reports/astra-six-hour-20261127/collision/marked_replay.json)

The trit mixing estimate cancels the large physical sources. A fixed
source can still move out along its own escaping future. Equation (5)
of the moving-root clock theorem describes precisely which shift survives
in that case. Establishing a conflicting uniform clock estimate at those
moving integer roots, or separately proving \(\liminf S_k\le0\), would
exclude ordinary escape. Alternative positive cycles require a separate
argument.
