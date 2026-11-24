# The first coefficient crossing from the cycle minimum

**Statement.** Let $x\ge2^{71}$ be any positive ordinary starting value, and suppose its first coefficient-crossing word has $p$ odd steps and $A$ shortcut steps and ends at $y\ge x$. Then
$$
 p\ge72{,}057{,}431{,}991,\qquad A\ge114{,}208{,}327{,}604.
$$
Existence of a first crossing and its failure to descend are both hypotheses for a general starting value. At the global minimum of a finite positive cycle they both follow from the orbit: the full lap contracts, so it has a first crossing within that lap, and the crossing endpoint cannot be smaller than the cycle minimum.

David Barina reports computational verification for all positive starts below $2^{71}$, so any nontrivial positive cycle would have minimum at least $2^{71}$. Applying that published computational result makes the displayed bounds apply to the single contiguous arc starting at this minimum. We did not replay Barina's computation. His paper separately reports the literature's larger lower bound 355,504,839,929 on the length of the **whole cycle**. No claim of a period record or of priority for the local inequality is made. [Barina, *Improved verification limit for the convergence of the Collatz conjecture*, §6 (2025)](https://doi.org/10.1007/s11227-025-07337-0).

## From endpoint non-descent to an interval

Use the map, carry and proper-prefix definitions in CYCLE_CLOSURE.md. The affine equation, $y\ge x$ and the first-crossing carry inequality give
$$
 (2^A-3^p)x\le C_w\le p3^p/3.
$$
The zero-weight case is impossible here because $x>0$ and a positive all-even first crossing strictly descends. Let $\alpha=\log 3/\log 2$. Since $2^A>3^p$ and $\log z<z-1$ at $z=2^A/3^p>1$,
$$
 0 < \frac{A}{p}-\alpha < \frac{1}{3x\log 2}
       \le \frac{1}{3\cdot2^{71}\log 2}.
$$
This derivation also strengthens the locally replayed bound in CYCLE_CLOSURE.md. Its 47,468 odd steps and 75,235 shortcut steps are required at the first crossing **from the cycle minimum**, using only the local 206,178,386-start cutoff and no external verification.

## Exact arithmetic certificate

Use
$$
 a/b=103768467013/65470613321,\qquad
 c/d=10439860591/6586818670.
$$
The file check_farey_gate.py uses Python's arbitrary-precision rational arithmetic to verify
$$
 a/b<\alpha<\alpha+(3\cdot2^{71}\log 2)^{-1}<c/d,
 \qquad bc-ad=1.
$$
For $v=2,3$, put $t=(v-1)/(v+1)$. The logarithm equals $2\sum_{k\ge0} t^{2k+1}/(2k+1)$ by integrating the geometric series for $1/(1-t^2)$. Its first 90 terms form a lower bound. The discarded positive remainder is at most $2t^{181}/(181(1-t^2))$. Ratio bounds use the lower numerator and upper denominator for the lower end, and the upper numerator and lower denominator for the upper end. The additional reciprocal term uses the lower bound on $\log 2$. The strict endpoint comparisons and determinant passed.

Put $u=bA-ap\ge1$ and $v=cp-dA\ge1$. The determinant identity gives $A=cu+av$ and $p=du+bv$ exactly, whether or not $A/p$ is in reduced form. Thus $A\ge a+c$ and $p\ge b+d$, giving the displayed numbers.

The checks rerun with Python 3 using the following command.

    python -B check_farey_gate.py

The exact fractions leave infinitely many larger numerators and denominators available. They do not decide whether any associated ordinary trajectory closes. Positive divergent trajectories remain a separate possibility.


## Lean coverage

The additional source MinimumCrossing.lean imports the frozen CyclePacking module. It proves the arithmetic inequality and integer floor bound at the actual nondescending source, the strict real-logarithm inequality, and the general integer Farey coordinate bounds. All four declarations compiled with warnings treated as errors. Their transitive axiom reports contain only propext, Classical.choice and Quot.sound. The exact 90-term numeric comparison remains the Python rational certificate. After compiling CyclePacking.lean in the same directory, the second module can be checked in the same Mathlib toolchain with the local directory on LEAN_PATH.

    lake env sh -c 'LEAN_PATH=.:$LEAN_PATH lean -DwarningAsError=true -o MinimumCrossing.olean MinimumCrossing.lean'
