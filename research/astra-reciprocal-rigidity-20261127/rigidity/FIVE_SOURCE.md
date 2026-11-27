# One monomial of forcing inside the known component

**Proposed weighted consequence.** Every number used below is an ordinary positive integer, and the support visits the known orbit `5,8,4,2,1`. This supplies a concrete control for a mixed-section regularity argument.

Let `P` be the set of positive integers whose shortcut trajectory reaches 5. Set `a(0)=0`, set `a(5)=1/64`, and set `a(n)=0` off `P`. For `n` in `P` multiply `a(5)` by the products of the usual squared slopes along its first-hit path to 5. No such path repeats a vertex before 5. Since 8 never revisits 5, the odd relation fails exactly once. Writing `A(z)=sum a(n)z^n` and `S_{q,r}A(z)=sum a(qn+r) z^n`, one has

\[
  4 S_{2,0} A=A,\qquad
  S_{2,1} A-\tfrac94 S_{3,2} A=\tfrac1{64}z^2 .
\]

Indeed, at the exceptional source `2n+1=5` the target is `3n+2=8` with zero mass. At every other source, visiting 5 is equivalent to its successor visiting 5, and first-hit propagation supplies the indicated weight. The coefficient at zero satisfies the even identity.

On `P`, write `D(n)=prod(1+1/(3x))` over the odd inputs of the first-hit path. The endpoint law gives `n²a(n)=25/(64 D(n)²)`. The finite reciprocal packing bound in [the ordinary spectrum note](ORDINARY_SPECTRUM.md) gives a uniform positive lower and finite upper bound. Bell and Lagarias, Theorem 1.2(1), show that the unweighted characteristic series of this particular predecessor set has the unit circle as a natural boundary. Consequently this binary support cannot be eventually periodic, since an eventually periodic support has a rational generating function. [Original theorem](https://arxiv.org/pdf/1408.6884)

All the hypotheses of the right-limit proofs in [the ordinary spectrum note](ORDINARY_SPECTRUM.md) are thus satisfied independently of universal convergence. The squared-slope series `A` has an uncountable closed singularity set containing a nonempty perfect subset, and for all but countably many positive real `s` the series `sum_{n in P} a(n)^(s/2) z^n` has its entire unit circle as a natural boundary. The first assertion rules out any general conclusion of countably many singularities for solutions of the mixed section equations with polynomial right-hand sides, even if the forcing is one monomial on the known component. The second assertion concerns a parameter family. Using arbitrarily long ordinary intervals entering 85 gives the stronger conclusion that the full natural boundary occurs at every positive exponent, including 2. [Proof using ordinary basin blocks](BASIN_BLOCK_BOUNDARY.md)

The antecedent use of the actual visit-5 label and its exceptional edge is PR201 `d21bac748e705a64b6b57a7996a8ad6282f0bcbf`, `research/six-hour-20261127/escape/DYADIC_SIBLING_FLUX.md`; that note uses the color to test asymptotic cancellation and the disjoint 85-basin. Bell and Lagarias treat the characteristic series. The squared-slope weighting, explicit polynomial source, and weighted singular-spectrum deductions above are the extensions here. A polynomially forced ordinary solution leaves open uniqueness for the exact homogeneous equation.
