# Six odd-valuation mismatches at an arbitrary rotation

The [full denominator theorem](ROTATION_DENOMINATORS.md) strengthens the rational estimate below to $q>2^{p/4096}$ through six mismatches using the actual common block clocks.

The [five-mismatch theorem](FIVE_ROTATIONS.md) also holds with **six** in place of five, without a restriction on the rotation order, the division exponents or the physical spread. In a primitive positive rational cycle with large odd period $p$, a proper odd-valuation rotation differing in at most six places forces
\[
     \max\{\log_2q,\Lambda\}>p/4096,\qquad q>p/65536,
     \quad \Lambda=h-p\log_2 3.
\]
In particular only finitely many primitive ordinary integer cycles can have such a rotation. The onset remains ineffective, by Evertse's theorem. General cycles can have more than six mismatches for every proper rotation.

It remains to handle exactly six actual mismatches. Use the two chronological cut lists, variables and all the rows (3)–(5) of the five-mismatch proof with $s=6$. Suppose the two contrary bounds there both hold with $\eta=1/4096$, so $h=O(p)$. Include two normalized variables at each cut,
\[
       B_i=\min(U_i,V_i),\qquad E_i=\min(u_i+v_i,U_i,V_i).
\]
Both lie in the unit cube. Include the exact five linear rows $U_i-B_i$, $V_i-B_i$, $U_i-E_i$, $V_i-E_i$, and $u_i+v_i-E_i$, all nonnegative. The verifier only requires these upper bounds, so the actual variables remain feasible for this relaxation.

For any block of $k=2,\ldots,6$ consecutive mismatches ending at $b$, unroll indices cyclically and let $I=\{b-k+1,\ldots,b\}$. Apply the [general native-chain inequality (2)](MISMATCH_CHAINS.md) with the smaller positive post-mismatch numerator at every cut. Its terminal maximum plus its terminal smaller height equals $p(U_b+V_b)$. The last payload may be either compact or split, so its remaining cost is exactly $pE_b$. Each interior compact payload costs at most $p(u_i+v_i+B_i)$. Substituting $a_{b+1}\le A_{b+1}/p$ from equation (3) of the five-mismatch paper proves the genuine necessary row
\[
 U_b+V_b+E_b+\sum_{i\in I\setminus\{b\}}(u_i+v_i+B_i)
          -a_{b+1}-\gamma\sum_{i\in I}l_i \ge -o(1).
\]
A six-cut chain returns to its starting cut. The original identity and the distinct dyadic valuations of its compact right-hand terms still hold, even if a starting and a terminal quotient have the same value. The proof for a split last payload uses its ternary unit and the same argument as for shorter chains. There are finitely many chain lengths and the normalized error tends to zero uniformly. No giant or distinguished mismatch is required.

For each of the seven wrap counts $w=0,\ldots,6$, [seven exact positive-weight certificates](six_rotation_duals.json) give a weighted row sum whose supremum on the full $43$-dimensional cube, divided by the sum of weights, is below $-1/512$ at both rational slope endpoints. For fixed variables the weighted form is affine in the slope, so the bound covers $\gamma=\log_2 3$. Every genuine row is at least $-2\eta-o(1)$ and $2\eta=1/2048$. This proves the first assertion; the distinct-numerator correction integral from the five-mismatch proof proves the second. [Exact rational verifier](check_six_rotations.py) · [Archived numerical fractions](../../../reports/astra-infinite-descent-20261127/cycles/SIX_ROTATIONS.json)

The finite computation checks nonnegative affine combinations. The native Diophantine chain bound and its ineffective error are written arguments with the external Evertse input. [Evertse, Theorem 2, p. 228](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

The [real cube and weighted-row theorem](CubeDual.lean), [twenty-five two-endpoint matrices](RotationDuals.lean), and [interpolation certificate](RotationInterpolation.lean) compile in Lean 4.34.1; each numerical check uses kernel reduction. The Lean theorem `certified_interior` produces a row below the stated margin at every real interpolation and every real cube point. The [exporter](export_rotation_duals.py) reproduces the named sparse matrices from the rational row definitions, including all six-cut chain rows chosen by the duals. The [native cut replay](check_rotation_cuts.py) verifies 22,850 paired clocks and 45,700 chronological prefix rows in 2,033 primitive positive rational cycles, including 4,592 exact translated seams. [Physical control counts](../../../reports/astra-infinite-descent-20261127/cycles/NATIVE_ROTATION_CUTS.json)
