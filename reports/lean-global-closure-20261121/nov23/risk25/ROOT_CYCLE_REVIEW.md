# Root review of the integer residual-degree attack

Date: 2026-11-23. Reviewer: coordinating agent, independently reconstructing
the proofs from the proposed statements. This review concerns the two
risk25 cycle notes at the bytes recorded in the final manifest. It does
not extend to later edits or to neighboring results in the cited PRs.

## Verdict

**VERIFIED WITH FIXES, as written deductions with the stated external
inputs.** The resulting theorem is a necessary condition for hypothetical
primitive positive integer cycles. It is not nondivisibility of the
complete denominator and does not exclude any escaping component.

The main new conclusion is a positive power lower bound on the residual
polynomial degree in the odd period. The older all-word lower bound and
the new bound have different hypotheses: actual integer states supply
the spacing estimate in the new proof.

## Reconstruction of the decisive chain

1. For one actual rotation put v_j=2^{s_j}x_j. Its edge identity is
   v_{j+1}=3v_j+2^{s_j}. Coefficient comparison gives
   (X-3)H=Q+x_0F, including the constant term. The polynomial rotation
   is 2^{a_0}Q_next=XQ-F. The minus sign matters, though either sign
   would leave the abstract gcd conclusion unchanged.

2. Since F(3) is nonzero, the entire monic common factor G divides H.
   The quotient J has degree d-1 and leading coefficient x_0. Its
   roots are among H's roots, whose moduli lie between 3+1/M and
   3+1/m by the positive-coefficient argument supplied in the note.
   That argument scales the minimum adjacent coefficient ratio and
   excludes roots in the open unit disk by an exact triangle bound.

3. The last actual edge gives
   H(0)/x_0=2^A/(3+1/x_{p-1}). All roots of G have modulus
   r=2^{A/p}. Removing all p-d roots gives
   |J(0)|/x_0=r^d/(3+1/x_{p-1}). The product of the d-1 remaining
   root moduli therefore proves the two-sided inequality IR8.
   Rotation allows the predecessor to be the minimum, so
   log(1+1/(3m)) <= d Lambda/p. This step remains valid for positive
   rational cycles; integrality has not yet entered.

4. Distinct positive integer states give
   Lambda <= (1+log p)/3. Also
   log(1+1/(3m)) >= 1/(3m+1) >= 1/(4m).
   Hence p <= (4/3)d m(1+log p). No density assertion or average
   random gap law is involved.

5. Write A=ga,p=gb with gcd(a,b)=1. The monic constant term of F_0
   has absolute value 2^{ad/b}, so b divides d. At the reduced
   clock the positive linear form is L=a log2-b log3, not Lambda.
   The actual cycle product gives a<=2b and tau=L/b<=1/(3m).
   Matveev then yields m<C_m b^K<=C_m d^K. Combining these two
   independent estimates proves IR17.

6. I separately reconstructed PR182's global count at its frozen head.
   With a common number of odd steps, high total binary clocks inject
   into a smaller part of the same forward-invariant set, regardless
   of intervening heights. The remaining words are counted by their
   exact residue modulo 2^{A+1}; the negative-binomial tail identity
   and Stirling bounds give the critical exponent. A finite primitive
   cycle is a valid domain because U permutes its distinct states.
   Integrating that count above the actual minimum gives IR19.
   Substitution yields p<=C_* d^{1+K theta}, hence IR21.

The quotient at X=3 is retained throughout. A large value of |F_0(3)|
is not the reduced rational denominator after its numerical gcd with
Q_0(3). The proof does not identify a prime at which full cancellation
must fail.

## Primary logarithm source

I opened Matveev's original English paper, Corollary 2.3 on printed
page 1219, including its page image. With field Q, two positive arguments
2 and 3, and height parameters log2 and log3, the displayed constant
permits C_1(2)<=2^32 and the corollary permits B*. Since B*<=2b, the
specialization IR15 follows. This checks the application and the
published statement; it is not a reconstruction of Matveev's proof.

I also read Simons--de Weger's Lemma 12 and its reference to Rhin.
The original Rhin proposition was not available in the sources opened,
so no improved numerical exponent has been substituted into this
checkpoint.

## Recurrence lattice

The characteristic polynomial r^{-d}F_0(rY) has coefficients in Q(r)
that are algebraic integers, since all its roots are roots of unity.
Its constant term is an algebraic unit. Thus every d consecutive
normalized coefficients generate the same fractional ideal. At each
prime above two, oddness of the actual integer states gives the exact
valuation s_j-Aj/p. Taking ideal valuations proves that its global
minimum occurs in every d-position window. The resulting clearing
and maximum-state estimates RL7--RL10 follow directly.

For rational controls with an odd denominator, the same formula measures
only the two-adic deficit. Multiplication by a power of two does not
clear the separate odd denominator. I requested that this distinction
be explicit in the control family; it cannot be treated as a global
algebraic-integrality assertion.

## Fixes and retained limits

The root lemma needs degree at least one; constant-polynomial cases are
handled separately. The literal rotation sign is minus. The rational
control uses a two-adic deficit rather than a full integrality clearing
factor. A future exponential lower bound for the minimum in terms of d
would still need the finitely many remaining periods excluded.

The finite exact controls are useful checks on normalization and
factorization, not evidence replacing the unbounded argument. No full
Lean formalization of the root-location, logarithm, or infinite-count
steps is claimed.

## Final-byte additions

The main note was independently reviewed at SHA256
`d92b1dd9c6da48459dad86a918b1a639f98c43aac8b6610157efd956b7a84b2a`;
the lattice note at
`9f1f08ecd36e84cfd3cdc3021591cd47d9cb4c3cc5e6ce51401cf4686d51aba5`.

I separately checked the stronger lattice estimate RL9a. Let j<d be a
global minimum of the normalized binary clock, and write
b_j=m exp(E_j-j tau). For any k, the differences E_k-E_j and
(k-j)tau have the same sign and absolute values at most Lambda. Thus
the normalized amplitude ratio is at most exp(Lambda). Clock minimality
then gives x_k<=exp(Lambda)x_j. The actual edge inequality
x_(i+1)+1<=(3/2)(x_i+1) gives

`M <= exp(Lambda)((3/2)^(d-1)(m+1)-1)`.

The explicit denominator-five rational control preserves its odd
denominator. Its large numerical gcd disproves the proposed rational
height bound, without disproving an integer-specific theorem that has
not yet been found. The checker now omits a tautological damaged-carry
comparison; it retains six substantive exact controls and all 76
rotations. Its actual normal and optimized execution receipts are
separate from this written-proof review.
