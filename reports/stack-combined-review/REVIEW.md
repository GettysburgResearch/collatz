# Independent review of the combined-moment period-eighteen theorem

**VERIFIED at the frozen scope.** Local author checkpoint
`291bec0490479078e84d06814af0c984de6ec712`,
`research/stack-combined-moments/PROOF.md`, blob
`a018c49014c07a62cf9f457f1b29f6845249edf9`. The claim covers every
positive periodic stack increment word of period at most eighteen, every
initial m>=0 and finite positive steering prefixes. Reference normalization
is PR 20, `82ca2f932438a9fe0897704ba62959ca23ec830f`, L-9407
and L-9408 under `research/padic-repetition/claims/`.

I independently derived the combined convolution and sampled identities
before reading the finished manuscript, then compared each bound to its
frozen text. The central checks are as follows.

1. Periodic increments give E_(s+j)-E_s-E_j=9(S/r)sj when s is a multiple
   of r. The same identity applies separately to both completions. Under
   rationality of the two-adic target, equality with the real limit would
   produce a nonzero integer divisible by 64^E_s and of absolute value at
   most const times 64^E_s/81^(E_s-E_(s-1)). The gaps diverge.
2. For D=M=6n/5 and mu=M+n/2, the cleared n-row coefficient system has
   aggregate row spread a D n²/4+O(n²). The integer box has D+1 variables
   and n constraints, giving height cost 3a n²/2+o(n²) in base 81.
   Subtracting two box points leaves a nonzero polynomial and exact
   cancellation of degrees M,...,M+n-1.
3. The first *possible* surviving term has a lower two-valuation controlled
   by j=M+n, k=D. Larger j only raise the bound, also after the uniform
   O(j+n) error. For the truncated rows j<M, k<=j and the upper exponent
   cap is (sigma+d)²/2+d/2 with d=6/5. The finite prefix carries the
   same cap at k=D. No actual nonzero tail coefficient is needed.
4. For all sampled s, clearing the posited identity uses an odd integer.
   The exact endpoint lower bounds 1469/310 and 227/930 follow using
   rho>88/93. Concavity forces the identity throughout the window, even
   when V vanishes there. Only this rational identity passes between
   embeddings.
5. Positive real sample points are separated by fixed ratio T^(9S).
   Distinct sample intervals exclude at most deg(V) root moduli. At a
   remaining point y, multiplying |y-z|>=c(y+|z|) over all roots bounds
   every |coefficient| y^k, including the constant-polynomial case.
   The strict sample surplus at r=18 is 22/18-6/5=1/45 per n. The lower
   endpoint real margin 73/950 follows using 1-rho>1/19. These margins
   absorb fixed-word constants and all subquadratic terms.
6. Splitting at a steering prefix gives a rational affine function of the
   updated tail with nonzero multiplier; the native context transform also
   has nonzero rational multiplier. This proves the stated ordinary-context
   exclusion, without a conclusion for unrestricted Collatz trajectories.

The three rational margins were recomputed by exact integer fractions.
This review concerns this specific source head and its period range.
