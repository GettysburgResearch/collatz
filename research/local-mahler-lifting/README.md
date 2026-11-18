# Morphic parity and rational-base values

**Proposed research results.** Every binary morphic word with exponential emitted growth in some presentation has a rational 2-adic inverse-parity source if it is eventually periodic, and a transcendental source otherwise. This includes primitive substitution and automatic words. It applies to individual 2-adic sources, including arbitrary signed rationals. [Inverse-parity theorem and Galois descent](TRANSCENDENTAL_PARITY.md)

For coprime $2\le Q<P$, the sum of a nonperiodic exponential morphic digit word at $Q/P$ is transcendental at infinity and all primes of $Q$ when distinct digits occupy distinct residues modulo $Q$. For any finite list of rational digit observables of the same word, their joint algebraic relations agree over $\mathbb Q$ at those places. A positive rational-base representation-tree ray can have neither automatic nor any other exponential morphic digits. [Rational-argument theorem](RATIONAL_ARGUMENTS.md) · [Minimal word of base 3/2](AUTOMATIC_CHARTS.md)

### Proof dependencies

1. The [univariate specialization](PROOF.md) adapts the published Adamczewski–Faverjon relation-ideal argument to a finite place. Its auxiliary coefficient field is fixed before degree choices. A Gauss norm on one closed disk supplies the local estimate. The [multivariate proof](PRIMITIVE_DIRECTIVES.md) clears matrix denominators on a polydisk.
2. The [primitive case](ALL_PRIMITIVE.md) handles torus equations among the sampled arguments using S-unit equations and Skolem–Mahler–Lech. Its regularity lemma follows from the algebraic S-integral series criterion of Bell, Chen, Nguyen and Zannier. The [exponential case](EXPONENTIAL_MORPHIC.md) separates letters of different growth rates, allowing unlimited slow-variable auxiliary degrees while sampling only after the degrees are fixed.
3. The [output normalization](MORPHIC_NORMALIZATION.md) permits erasure and arbitrary output morphisms. The [signed rational step](SIGNED_PARITY.md) obtains a finite nonzero real affine limit using the reciprocal estimate on a nonperiodic orbit. [Algebraic descent](TRANSCENDENTAL_PARITY.md) then excludes all algebraic irrational inverse-parity values for the indicated words.

The [Jordan-chain examples](JORDAN_EXAMPLES.md) separate the new class from all substitution classes in rStation paper 16 by the growth of their sparse zero counts. A [frequency-free example](NO_FREQUENCY_EXAMPLE.md) has distinct upper and lower densities, both exceeding the ordinary growth threshold, and irrational lower density rules out every automatic presentation.

The unrestricted parity problem remains open. A morphic presentation of a hypothetical nonperiodic signed rational orbit would have to exhibit polynomial emitted growth of degree at least two and rational supercritical odd frequency. [Polynomial growth boundary](MORPHIC_NORMALIZATION.md) · [Decorated quadratic templates and two-run exclusion](../two-prime-growing-blocks/QUADRATIC_MORPHIC.md)

### Review and finite checks

Independent internal readings checked the univariate specialization and the signed rational step. A separate reading checked the layered cone, fast-letter prefix estimate, auxiliary dimension comparison and real convergence in the exponential extension, conditional on the earlier specialization and torus reduction. These are written proof candidates. The [exact layer replay](check_growth_layers.py) exercises three growth levels, a frozen letter and a Laurent monomial change of coordinates on 242 sampled prime vectors and 15 complete word levels. The [two-prime checker](../two-prime-growing-blocks/check_reverse.py) separately exercises the Gaussian determinant used for the quadratic boundary.
