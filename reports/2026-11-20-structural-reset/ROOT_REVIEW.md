# Root reconstruction of the physical-pair and component arguments

Date: 20 November 2026. Scope is the exact files and claims listed below.
This is a written mathematical reconstruction, not a formal build. The root
coauthored part of the prime-height argument and therefore does not count
as that argument's independent reviewer.

## CP-001--005: VERIFIED at the pinned file

Path: `research/structural-reset-20261120/capacity/PAIR_COUPLING.md`.

SHA-256:
`428020612e96c3fffed495f605214ca88db8050b164954304f8bcf815fe353b9`.

The three maps have positive odd integral outputs in their exact residue
classes. For the difficult class n divisible by three, write J(n)=4n+1.
Direct shortcut replay gives T^3(J(n))=T(n) and
T^2((16n+3)/3)=J(n). Thus the displayed class-zero move is a legal
ordinary component diagram, although n itself has no odd inverse.

On a common ternary class, the difference is multiplied by 2/3, 4/3,
or 16/3. Its ternary valuation decreases exactly once and its nonzero
part away from two and three is preserved. For H=max(x,y), every branch
satisfies 1+H' <= (16/3)(1+H). This verifies the asserted proper-cost
decrease when kappa>log(16/3). Collapsing all diagonal states into a single
absorbing point is necessary for the printed properness formulation and
is explicitly part of the state space.

The carry difference follows by subtracting the two affine formulas.
At (18u+3,18u+5), the images are (96u+17,12u+3); their difference is
14(6u+1), prime to three. The full renewal therefore has no stripping
credit, and its height cost strictly increases for every u>=0. This
refutes precisely that reset, rather than all possible physical kernels.

The proposed sufficient drift criterion is also valid as a conditional
statement. Telescoping bounds E[V] and the total expected positive drift
budget. Properness makes the off-diagonal distribution tight. On each
finite sublevel the budget has a positive minimum, so the probability of
remaining in that sublevel tends to zero. Letting the sublevel grow gives
coalescence probability one. A kernel with these properties is not
constructed or inferred from the stripping calculation.

For the physical-clock bound, a shortest simple path in a functional graph
can be oriented forward then backward to a common endpoint: a backward
then forward switch would require two distinct outgoing edges at the
switch vertex. At the inputs (2^K-1,2^K), any proposed endpoint with total
clock less than K is odd on the first arm and even on the second. Thus
the distance is at least K if finite. Integer-valued separation then
gives the stated lower bound on expected total physical clock for any
uniform ordinary-distance contraction. No convergence of the Mersenne
arm is assumed.

Finally, two fixed sources in one ordinary component have equal forward
tails after finite clocks. The odd accelerated section has logarithmic
height at most x0+j. On an escape W_N/N tends to infinity, so a fixed
number of shifted boundary terms is negligible relative to W_N, uniformly
over chosen prime sets. The inherited dispersion property therefore
persists across fixed sources in a component. Changing the ancestor with
the horizon does not provide persistent prime retention.

## CR-001--002: independent algebra reconstruction

Published path: `research/structural-reset-20261120/component/PROOF.md`.

Published SHA-256:
`0a7d555cfa52a1b8d0de147ff2ebdf6e33e5a51d6a2a39500986ef6c206a7985`.

The original inspected proof had SHA-256
`274f47167d64bc49d5a34e222d1e5ef883652d0f037f510d88ecc2d5468fb245`.
The only subsequent change in this file explicitly restricts the auxiliary
two-fixed-word slope observation to each fixed a. That qualification does
not alter CR-001, CR-002, or any selector case.

Repeated application of T^2(4z+1)=3z+1 at t=4^a x gives exactly
f(x)=f(5*3^(a-1)*x), on the stated odd ternary-unit domain. Iteration in
the factor five justifies every multiplicative law for F(n)=f(5n).
F=f is used only on ternary units or multiples of five, with the two
domains established separately. The multiplier-nine identity comes from
two actual odd steps on 5n when n=3 modulo four; it is not an extension
of the multiplier-three identity to an unsupported domain.

All least-label cases were recomputed. Removing 2,3,5 and the classes
1 modulo four and 7 modulo eight leaves n=3 modulo eight. The three
modulo-five descents leave n=2 modulo five. The inverse multiplier-fifteen
case removes n=2 modulo three. The last class is n=67 modulo 120.
There u=(3n+1)/2 is an odd ternary unit and v=(9n+5)/8 is 1 modulo 15.
The three displayed final targets are integral, positive, and strictly
smaller. Each conditional law is applied on its exact domain.

Every positive source reaches a ternary unit after removing powers of
two and, if needed, one ordinary odd step. Thus constancy of F transfers
back to f. Taking actual merger-component labels proves the stated
equivalence. The proof never asserts that the hypothesis E has been
established. The logarithmic abstract reduction count is correctly kept
separate from all physical Collatz clocks.

**Verdict: VERIFIED at the printed scope.** A separate nonauthor review
also reconstructs the final file and the reduced-law corollary. No full
Collatz conclusion is drawn without the still-open hypothesis.

## Software scope

The root read both new checkers. The component checker represents an
unbounded input cell by its affine coefficients and checks domains at
the coefficient level; it does not merely test 480 numerical starts.
Its assertion-dependent entry point explicitly rejects optimized Python.
The prime-height checker uses explicit exceptions and exact integer
inequalities, including incomplete blocks and large actual divisions.
Its adaptive prime choices range over a declared finite candidate pool;
the proof, not that finite pool, establishes uniformity over all primes.
Actual command receipts are recorded separately in VALIDATION.md.
