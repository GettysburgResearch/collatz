# Arithmetic rigidity at the binary interpolation center

23 November 2026. **Written research packet; full Collatz remains OPEN.**

The central attempt uses the exact binary value of the weighted parity
series for one positive ordinary source, `B_n(2)=-n`, as an additional
arithmetic interpolation center. It retains the literal orbit, full
affine carry, numerator, and ternary denominator at every step.

[Scalar boundary and second-center construction](SCALAR_BOUNDARY_AND_SECOND_CENTER.md)
contains three precise deductions:

1. If the actual odd-input density has a limit `rho`, the individual
   scalar series is rational or has natural boundary `|z|=3^rho`.
   This applies the checked Bost--Chambert-Loir rationality theorem;
   it does not prove a density limit for arbitrary escaping sources.
2. Dividing the known binary zero by `z-2` preserves `Z[1/3]`
   coefficients, with the exact actual numerator
   `-T^(k+1)(n)`. Its convergence-disc product is
   `min(2,3^rho_minus)*3^(-rho_plus)<=1`. This value-only construction
   gains no strict arithmetic capacity.
3. At critical density `rho=log_3(2)`, an actual rational Taylor germ
   at two with a fixed finite denominator-prime set and the specified
   analytic bounds gives a strictly positive two-center potential
   matrix. Chambert-Loir--Noûs's multipoint theorem then forces
   rationality, contradicting that irrational density.

The third conclusion is a conditional consumer with an explicit
positive margin. The full arithmetic Taylor germ has not been
constructed; even rationality of `B_n'(2)` is unproved for an arbitrary
source. The known constant `-n` and the same value at all shifted
ordinary sources do not provide the missing derivatives.

[Finite-filter test](FINITE_FILTER_TEST.md) separately checks the
Pólya--Carlson denominator hypothesis against finite rational pole
removal. Every nonzero coefficient left by a fixed polynomial filter
retains an exponential denominator. Subexponential common denominator
growth would already force a polynomial remainder and eventual
ordinary periodicity. This is a scoped obstruction to that
regularization, not a claim against the multipoint theorem or all
possible arithmetic constructions.

Exact repository and primary literature pins are in
[`rigidity-sources.json`](../../../reports/2026-11-23-literature-push/rigidity-sources.json).
No new Lean module, candidate verifier, large search, or old proof-corpus
rebuild is claimed. The central analytic and arithmetic deductions
require independent written review.
