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

## A sharply stated counting question

Polson and Sokolov's *On the Collatz Conjecture*, edition 1, records the
near-maximal correction-word question R9 and the untruncated cocycle
question R8 in its [exact November 10 source](https://github.com/VadimSokolov/collatz/blob/5840497a23fc0d64127b850aea68862d7c93f2b7/book/chapters/ch10h_ratchets.tex),
tag `v1.4.0`. Root retrieved that complete file and independently checked
the word definition, forced last exponent, pressure normalization and
question statements; a second agent did the same. The near-one rate in
checkpoint 8 is a new deduction relative to that exact source. The depth
model and proposed epsilon-log-inverse-epsilon scale belong to the book.
A targeted search found no additional result resolving that question;
this is not an exhaustive priority certification. The proof uses no
unverified density or number-theory premise from other chapters.

## First coefficient-crossing restrictions

De Jesús's [November 25 revision](https://hexagonmath.org/2611.00459v4)
gives restrictions on the first coefficient crossing in a putative
non-descending orbit. Root read the primary PDF's relevant proofs and
scope, including the finite odd-run regime, restart reductions, the
repeated-110 family and a square-prefix restriction. These can exclude
structured first crossings; they do not bound every crossing's complexity.
The claimed verification status of that unrefereed source was not treated
as an independent Lean rebuild, and none of its numerical thresholds is
used as a premise of the near-maximal entropy proof.

## Full word limits and concurrent arithmetic comparison

The same exact Polson–Sokolov source now supplies the questions answered by
checkpoint9: the full M4 count formula and both parts of R8, retaining the
R9 expansion. Kingman's scalar subadditive theorem is used with explicit
boundedness hypotheses; root read the original paper's primary statement
and Steele's author-hosted proof. The new critical transition argument is
proved directly and does not invoke a random-environment wetting theorem.

Root opened [Weaver160/v1](https://rstation.ai/problems/collatz/papers/160)
and [Weaver163/v1](https://rstation.ai/problems/collatz/papers/163), including
the latter's higher-order cancellation fixture and stated unrestricted-cost
question. Those are the precise antecedents of the new product arguments.
The pair theorem and bounded-division all-order theorem are credited.
Root also read [Paper137 Lemma4](https://rstation.ai/problems/collatz/papers/137)
for the earlier maximal-coefficient gcd criterion.

A GitHub refresh froze PR212 at 0172f15109b8749c14fed272e733c97a5a0f7d24,
PR214 at be010b2874b88267e710666d3c5f963a0c994356, and PR215 at
121054cf6569859585ede5c2d6e024eb2d97bbc5. Main remained
ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a. Their current front-door metadata
was read; this is not a review of all their new proofs. In addition, root
read PR215's complete moving-sparse-sum, moving-template and moving-residue
notes at d444e332d111115daa650c58a917dd46dacd4c1e. That prior publication
changes the attribution of the overlapping checkpoint7 method, as now
explained in `MOVING_FULL_MODULUS.md` and the checkpoint9 review.

## Checkpoint 10: native counts and full measures

The fixed-even-budget argument uses the rational S-adic Subspace Theorem
in the form of Theorem 5 of Varju's
[*On the multiplicative group generated by two primes in Z/QZ*](https://arxiv.org/pdf/2104.04367v2).
Root read that primary statement, including its integer-vector formulation
and finite exceptional-subspace conclusion. The original 1977 DOI could
not be retrieved. This is an external classical theorem, not one of the
finite Lean lemmas in the packet.

Root re-read the actual finite-source comparison and certified-stage rank
bounds in [Weaver102](https://rstation.ai/problems/collatz/papers/102),
the unit floor and finite ternary densities in
[Paper200](https://rstation.ai/problems/collatz/papers/200), and the prior
finite forward-orbit containment in
[Paper202](https://rstation.ai/problems/collatz/papers/202).
The new full-measure deductions retain these as explicit premises.
Paper200's earlier unbounded excess and Paper202's earlier containment are
credited directly; neither is claimed as new here. Root also read the
pinned PR193 canonical inverse-path construction and PR213's strict
no-return floor where the new acquisition and stopped-law arguments use
them. The exact book source above asks for an upper bound in R6; failure
of a matching two-sided fair-coin rate is not a disproof of that question.

A further November 28 search opened the abstract of
[*Collatz orbits of almost all primes attain almost bounded values*](https://aixiv.online/abs/2611.01542).
The catalog's word "proves" refers to a partial result, not universal
Collatz convergence. Its reported Lean package has not been rebuilt here,
and none of checkpoint10 depends on that claim. The same refresh opened
[Paper227](https://rstation.ai/problems/collatz/papers/227), whose sparse
sufficient-set construction is already credited in `PRIME_MIDPOINTS.md`,
and [Paper231](https://rstation.ai/problems/collatz/papers/231), which states
a large finite completeness interval for paradoxical sequences with
explicit record-table and census inputs. That finite computational claim
has not been replayed in this pass and does not cover all lengths.
