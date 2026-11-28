# A formal exclusion on the original cycle spectral grid

[CycleGridObstruction.lean](CycleGridObstruction.lean) proves the finite arithmetic obstruction used by the [ordinary spectral-grid theorem](../cycles/ODD_SPECTRAL_GRID.md). It uses the actual native site weights. The infinite operator classification, its compactness and its analytic source inputs remain the separate written proof.

Let a nonempty finite indexed family consist of positive odd integers $x_i$, and put
\[
 t_x=\frac1{3x+1},\qquad
 \lambda=\prod_i\frac{3x_i}{3x_i+1},\qquad
 Q(z)=\prod_i(z-t_{x_i})-\lambda z^p.
\]
The indexing permits repeated entries; an actual primitive cycle is a specialization. For every positive odd integer $y$, the formal endpoint is
\[
                              Q(t_y)\ne0.
\]
In the cyclic Green matrix, the characteristic polynomial is $Q(z)/(1-\lambda)$. Thus this finite exclusion applies even when $y$ lies outside the particular cycle being examined.

The proof clears the original denominators explicitly:
\[
 \left(\prod_i(3x_i+1)\right)Q(z)
   =\prod_i((3x_i+1)z-1)-3^p\left(\prod_i x_i\right)z^p.
\]
At $z=t_y$, the right side equals
\[
                 (3t_y)^p\left[\prod_i(x_i-y)-\prod_i x_i\right].
\]
The first integer product is even and the second is odd. Their difference cannot vanish, and the rational prefactor is nonzero. Both the denominator identity and the final nonvanishing theorem are checked.

The module has five public theorem endpoints: odd-product separation, the exact substitution identity, exclusion for the cleared polynomial, the native denominator-clearing identity, and exclusion for the native-weight characteristic. Its private product lemma is also included in the aggregate declaration audit. Strict compilation uses the same pinned Lean and Mathlib as the rest of the packet, with warnings treated as errors and no implicit variables. The only transitive axioms are `propext`, `Classical.choice` and `Quot.sound`.

This establishes the parity step needed to prevent a cyclic block from replacing a missing physical grid value. It does not by itself identify the spectrum of the full infinite operator or exclude an additional positive cycle.
