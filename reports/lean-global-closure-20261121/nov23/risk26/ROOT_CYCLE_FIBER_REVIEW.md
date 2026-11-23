# Root review: full numerical fiber and positive-gap attacks

23 November 2026. **VERIFIED at the narrow written scope below.**

Reviewed files:

- `FULL_FIBER_INTEGER_NUMERATOR_ATTACK.md`, SHA-256
  `4098ccd0481ce93fcef5c6e4fb4fcc37408495eb45102589b501db06d5047a9d`.
- `POSITIVE_GAP_FULL_FIBER.md`, SHA-256
  `6a6cbaba0e0c55b035dfb152934e7c21baedd34001c4d08bfca36cccc57a8736`.
- Exact-control code `check_positive_numerator_models.py`, SHA-256
  `48c968f3a978c5047137a0b79f49b1796047659d82641e41b0b92c95e96d59b6`.

No conclusion excluding all positive cycles is established. The
countermodel has arbitrarily large degrees along its specified clock
sequence, not a claim covering every independently prescribed degree.

## 1. Evaluation fiber and primitive quotient

Evaluation at three has kernel (X-3), and adjoining the monic
polynomial f reduces its integer image precisely modulo f(3). This
proves SN1--SN4 with the complete numerical gcd, including all prime
powers. The cokernel is finite cyclic, so its Smith invariants are
ones followed by |f(3)|.

The leading two coefficients of (X-3)J=q+mf give the explicit Bezout
identity j1-m(f1+3)=1. This proves IN1 without a positivity hypothesis.
The degree-one endpoint follows from m dividing one. Thus primitive J
does not add another integrality constraint once complete cancellation
and the two monic polynomials are already assumed. The resultant
identity RE1 follows by multiplying the same identity at all roots
of the monic F0; its sign is (-1)^d.

## 2. Infinite positive polynomial countermodel

I independently reconstructed PC1--PC14. The residue choice m=7 mod192
and the ceiling step give 4<=m*eta<4+192*eta<=5. The recurrence for y
gives positive carries of exactly the displayed powers of two, the
leading coefficient one, and the terminal positivity bound. Coprimality
of A,d makes X^d-2^A irreducible by the constant-term modulus of any
monic integer factor. Evaluating at three gives the entire denominator
as the numerical gcd, not only a selected factor.

The coefficient-ratio annulus was checked in both directions. Its
upper endpoint needs the separate first and second indices, where the
specified congruence for m makes the relevant y odd; the remaining
indices use y>=(3/2)^j*m. The lower endpoint follows from the explicit
upper recurrence bound and the stated M. The binomial root lies in
the same annulus by the concavity and mean-value inequalities given
in the proof. The two-adic root condition follows by rescaling J(2Y)
and dividing by the odd leading coefficient; the three-adic statement
uses unit leading and constant coefficients.

The exact bound D/M>=eta^2*2^d/4 is correct. The polynomial upper bound
on m and exponential lower bound along arbitrarily large reduced
clocks retain the risk25 fixed two-logarithm lower bound as an explicit
dependency. They are not inferred from finite numerical controls.

The construction does fail positive-gap Collatz legality. Its first
six nonconstant carry exponents are 0,1,2,4,5,5; the repeated exponent
is a zero gap. The terminal coefficient is not shown to be a power of
two. The note retains both failures. Consequently the model refutes
only an implication using the listed polynomial geometry and local
integrality properties, not an argument that uses the complete actual
positive-gap coefficient law.

## 3. Restored positive-gap law

The residual rotation relation PG2 follows from the full numerator
rotation identity after division by the common polynomial gcd. The
numerical denominator is prime to six, so every rotation multiplies
the old residue by a unit. PG4 correctly truncates prime valuations
at each exponent in the full denominator; no independence of rotated
congruences is introduced.

The minimal recurrence of u and v has the same squarefree residual
polynomial. Vandermonde factorization of their Hankel matrices gives
PG5 with the stated sign. Positive gaps supply the common factor
2^(d(d-1)). The minimum rotation bounds each normalized u entry by
exp(Lambda); Hadamard then gives precisely the quadratic-in-degree
allowance PG7. The ratio identity does not bound its remaining odd
integer determinant factor by m or M.

Direct expansion verifies PG8. Appending complete laps at each phase
changes the total two-block clock to (2k+1) times the original clock,
while preserving the two integer endpoints. Hence PG10 follows from
the same identity. Removing only factors two and three leaves the
complete denominator times the nonsmooth part of the displacement.
This does not create the strict inequality required by PR177.

## 4. Literature and evidence boundary

I opened the primary Corvaja--Zannier and Grieve--Wang texts myself:

- <https://arxiv.org/pdf/math/0311030>, Theorem 1.
- <https://arxiv.org/pdf/1902.09109>, Theorem 1.2.

Their fixed-function or fixed-degree/dimension hypotheses, and the
moving-target coefficient-height condition, are correctly retained in
the attempted encodings. The manuscript does not promote either
theorem to a uniform result for variable-degree Collatz carry arrays.

The accompanying code uses explicit runtime failures, exact integers
and rational arithmetic. Its root-annulus controls are coefficient
certificates, not numerical root approximations. Root execution
receipts are recorded separately. Those executions check the stated
finite models; the all-parameter proof and the analytic root lemma
remain written mathematics.
