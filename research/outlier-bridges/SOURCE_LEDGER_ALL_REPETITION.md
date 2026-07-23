# Outlier source ledger addendum — all-repetition single-pulse reduction

**Agent:** `gpt56-outlier-01`  
**Issue:** #52  
**Inspection date:** 2026-07-23

## OUT-SRC-0008 — Matveev's explicit real linear-form bound

- **Primary source:** E. M. Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, Izvestiya: Mathematics 64:6 (2000), 1217–1269.
- **DOI:** `10.1070/IM2000V064N06ABEH000314`.
- **Exact statement located:** the zbMATH review reproduced by the MaRDI portal states that, for a number field of degree `D`, nonzero algebraic numbers `alpha_j`, integer coefficients `b_j`, and nonzero
  ```text
  Lambda=sum_j b_j log(alpha_j),
  ```
  with
  ```text
  A_j=max{D h(alpha_j), |log(alpha_j)|, 0.16},
  B=max{1, max_j |b_j| A_j/A_n},
  C(n)=2^(6n+20),
  ```
  one has
  ```text
  log|Lambda|
   >= -C(n) D^2 A_1...A_n (1+log D)(1+log B).
  ```
- **Native substitution:** `n=2`, `D=1`, `alpha_1=2`, `alpha_2=3`, `A_1=log(2)`, `A_2=log(3)`, `b_1=Ar+delta`, `b_2=-kr`.
- **Exact dependency:** yes. This theorem supplies the finite repetition cutoff in `T-8202`.
- **Inspection boundary:** the exact formula was inspected in a scholarly review tied to the primary DOI, not reconstructed line-by-line from the primary PDF. `T-8202` therefore remains `SOURCE-DEPENDENT PROPOSED` until an independent reviewer checks the primary paper, logarithm conventions, and substitution.
- **No native conclusion in source:** Matveev's paper does not mention Collatz, negative cycles, pulses, or the divisibility reduction.

## OUT-SRC-0009 — Continued-fraction reduction

- **Object:** Legendre's criterion and the standard lower error bound for convergents.
- **Native use:** an approximation satisfying
  ```text
  |delta/r-alpha|<1/(2r^2)
  ```
  reduces, after cancellation, to an ordinary continued-fraction convergent `p/q`; the next denominator `q_+` gives
  ```text
  |q alpha-p|>1/(q+q_+).
  ```
- **Exact dependency:** elementary. The lower bound is derived from the complete-quotient formula inside `T-8202`; the Legendre criterion is stated explicitly and can be reconstructed independently without any numerical source.
- **Verification:** both programs certify every continued-fraction digit from rational intervals rather than importing a numerical continued-fraction package.
