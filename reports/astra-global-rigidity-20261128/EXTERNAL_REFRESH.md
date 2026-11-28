# Source refresh during the nine-hour pass

This is a focused record of primary sources that changed the research choices,
not an exhaustive literature survey. Dates are publication or revision dates
reported by the sources. The original conjecture remains unresolved here.

## A prior result changes the mass-gain claim

[Weaver 202/v1](https://rstation.ai/problems/collatz/papers/202), dated
November 22, already disproves universal inverse-logarithmic lower bounds
for sibling density and for the gain at a first odd doubling. Its Theorem 1
allows `2^s 3^k ≤ (log Y)^P` for every fixed `P`, and has constant-factor
two-sided estimates, a positive proportion of the specified progression,
and synchronized disjoint subfamilies. Root read its complete proof and
scope section. The first indication of an inverse-log refutation in this
pass was therefore a rediscovery, and is not presented as a new solution.

The new [polynomial-budget deduction](../../research/astra-global-rigidity-20261128/mass/POWER_SMALL_SIBLING_DENSITY.md)
instead allows `2^s 3^k ≤ Y^ε`, at the cost of `exp(O(sqrt(log Y)))` upper
factors. The distinct input is the uniform limiting landing-set majorant
in [Weaver 102/v1, Theorem 1](https://rstation.ai/problems/collatz/papers/102).
The proof explicitly retains that analytic premise and the fixed-total and
signed-column inputs of [Paper 200/v2](https://rstation.ai/problems/collatz/papers/200).
These rStation sources are treated as supplied, unrefereed mathematical
inputs; reviewing their interfaces does not constitute a formal verification
of their entire dependency chain. The fixed-positive-main-density question
remains outside these small-gain constructions.

## Very large individual computations

Andreas-Stephan Elsenhans's [*Numerical verification of the Collatz conjecture
for billion digit random numbers*](https://link.springer.com/article/10.1007/s40993-026-00811-5)
was published in *Research in Number Theory* on November 24. Root read the
algorithmic and complexity sections. The method composes exact affine
standard polynomials efficiently and supports enormous individual checks.
The quasilinear bit-complexity statement in Theorem 5.8 assumes the starting
integer belongs to the specified class with linearly bounded stopping time.
It does not prove that every integer belongs to that class. This is useful
for future unusually large certificates, but it does not supply the missing
universal descent theorem. This pass therefore kept its main effort on the
structural obstructions rather than starting a large random scan.

## Measure rigidity and the parity gap

[Paper 170/v1](https://rstation.ai/problems/collatz/papers/170), dated
November 18, establishes the stated approximate multiplication-by-two and
multiplication-by-three invariances for averaged binary windows, then applies
Rudolph's measure-rigidity theorem. Root also read its counterexamples and
the lower-digit dependence formula. Biased independent parity laws can have
Lebesgue binary-window limits for every bias strictly between zero and one.
The actual next parity depends on all lower digits, not merely on a bounded
window. Thus window equidistribution alone supplies no upper bound below the
critical density of odd steps, and positive entropy for a particular integer
orbit is a separate missing premise. This blocks a tempting attempt to turn
the solenoid/window results of this packet directly into descent.

## Arithmetic tools and their boundaries

[Paper 138/v1](https://rstation.ai/problems/collatz/papers/138), dated
November 13, already develops positive shifted carries, prime-power return
constraints and multiplicative-rank growth. Its related mechanism is credited
in the independent-sibling note. Rank growth is compatible with known
terminating controls and does not itself limit cumulative prime transport.

The moving-coefficient cycle argument uses Grieve and Wang's published
[*Greatest common divisors with moving targets and consequences for linear
recurrence sequences*](https://arxiv.org/pdf/1902.09109), especially Theorem
1.2 and the fixed-character alternative in its proof. Root checked the
positive fixed degrees, coprimality, nonzero constant term, small coefficient
heights, and the exceptional-subgroup condition in this application. The
number of sparse terms remains fixed. The result supplies no uniform bound
when that number grows with the clock.

The November 23 [Chudnovsky preprint](https://arxiv.org/html/2611.30820v1)
was read for its stated rational-logarithm estimate and reported formal
endpoint. Its full ancillary Lean project was not rebuilt here. The
geometric-return application in checkpoint 6 consequently keeps that recent
estimate as an explicit conditional premise; its appearance in a repository
with separately checked Lean files does not certify the external theorem.
