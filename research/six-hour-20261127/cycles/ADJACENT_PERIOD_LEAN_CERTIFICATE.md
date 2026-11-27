# Kernel-checked finite adjacent-gap census

The Lean module reconstructs the successive fractions from 1,944 simple continued-fraction coefficients. The input pairs each coefficient with a proposed integer window length. There are no stored convergent numerators, period denominators, candidate counts or census bounds in the input list. The two explicitly supplied rational endpoints have numerators and denominators obtained from independent positive series for $\log 2$ and $\log 3$. Each endpoint's full Euclidean quotient stream is checked against the same list. Their strict order and separation below $2^{-7300}$ are also kernel-checked.

For a reconstructed row $(A,P,b)$, the predicate WithinScreen requires $10^6<P\le10^{1000}$, $A>P\lambda_+$ and $2^{71}(A-P\lambda_+)<P$. Here $\lambda_+$ denotes the explicit upper rational endpoint. Exactly 959 rows satisfy it. The kernel proves, for every reconstructed row with this predicate, that $b\ge2$, $A<2P$ and
$$
 (b+1)9^w+\big(Y+(b+1)3^b\big)7^w<P9^w,\qquad
 w=\left\lfloor\frac{(2P-A)(b-1)}P\right\rfloor,\quad
 Y=\left\lceil\frac1{A-P\lambda_+}\right\rceil.
$$
The positive denominators and nondescending natural subtractions are guaranteed by the screen and the stated conclusions. The six arithmetic declarations use conversion or decidable propositions; the universal seventh uses the bounded-list decision procedure. The independent fresh build and separate fresh import printed an empty axiom list for every declaration, including the universal statement.

The written proof continues to supply the analytic enclosure of $\lambda=\log_2 3$, the completeness inference from its continued-fraction interval and Legendre's criterion, explicit avoidance of the rank seams, the physical recurrence and the adjacent-gap census inequality that each hypothetical period must satisfy. The finite theorem concerns the stated ordinary positive canonical-height-one cycles with least odd phase at least $2^{71}$.

The complete source is AdjacentPeriodCensus.lean. The generator recomputes the endpoint integers, common quotient list and candidate windows directly from the independent rational arithmetic checker. Running generate_adjacent_period_lean.py checks the embedded data; its optional writing mode replaces only the two generated data blocks. The independent pinned build uses verify_adjacent_period_lean.py and the existing pinned toolchain helper. Its normal JSON receipt records source and fresh object hashes, all seven axiom lists and the separate import. The source requires no compiled object from the research repository.
