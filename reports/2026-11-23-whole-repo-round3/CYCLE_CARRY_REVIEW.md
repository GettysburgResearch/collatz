# Independent semantic review: complete-carry source boxes

Date: 2026-11-23. Reviewer: cycle research lane.

**Verdict: VERIFIED within the finite arithmetic and explicitly conditional
actual-law scope below.** The critical cross-box upper bound remains open.
This is an independent reconstruction of the statements and proofs, not
an external peer review or a claim of a new literature result.

## Exact reviewed bytes

| File | SHA-256 |
|---|---|
| `research/whole-repo-round3-20261123/ACTUAL_COLLISION.md` | `eb8a352d3ad072e601637c0d2beff2992317252ff4ca58b830100074a1b17709` |
| `research/whole-repo-round3-20261123/CarryFibers.lean` | `9fd194724b6c2c101bfe837dcd198199f4618911c7cf608ff425c8bac31818e3` |

The reviewer did not author these files. The shared chronological carry
convention was checked against the unchanged `CycleWordAlgebra` definitions.
Compilation, axiom auditing and execution are separate parent-checkpoint
checks; this report does not claim those executions as its own.

## Reconstruction

1. **Two clocks and the full carry.** A gap word with m odd transitions
   and total binary clock A expands to the stated length-A shortcut word.
   Its complete identity is `2^A q=3^m p+C`. Carry parity recovers the
   first shortcut bit; the odd count then recovers the suffix carry.
   Equal length prevents the trailing-zero ambiguity. This proves the
   claimed decoder, including the zero-odd-count cases permitted by Lean.

2. **Quotient channels.** Reduction modulo `Q=3^m` sends equal endpoint
   residues to equal carry residues. With the carry quotient fixed, the
   complete carry and word are determined. An interval of R quotient
   values permits at most R words, independent of its offset. Repeated
   occurrences of one word have the same endpoint residue because
   `2^A` is invertible modulo Q; one representative endpoint can therefore
   be used after summing their original weights into `p_w`.

3. **Source blocks.** Equal carries in the two supplied identities give
   `2^A(q-q')=3^m(p-p')`. Coprimality forces equality of the source
   residues modulo `2^A`. A common source quotient forces equality of
   source and endpoint. Combining this with the channel decoder proves
   the full `(A,k,ell)` box injection. Distinct clocks of one injective
   actual orbit then cannot give two occurrences in a box with the same
   endpoint residue. No global bound on source height is used.

4. **Weighted inequalities.** Cauchy's inequality applies to each residue
   fiber of at most R distinct words. Expanding combined word weights
   gives exactly `sum_w p_w^2 = sum_j t_j^2 + E_rep`, with the off-diagonal
   sum using ordered distinct occurrence pairs. Within one exact channel
   this is an equality for the residue collision. Within a full source
   box, distinct-occurrence collisions vanish. The interval multiplicity
   `1+floor(H/2^A)` follows from the exact source congruence; the original
   bound `t_j<=1/N` gives (16) without renormalizing any submeasure.

5. **Physical floor.** The prefix telescope gives
   `2^a_i/3^i = p/(x_i Lambda_i)`. Every prefix product is at least the
   full finite product kappa, and `p/x_i<=B`. Summing all m carry terms,
   including the initial term, proves `C/3^m<=mB/(3kappa)`. This is a
   supplied-window estimate, not a replacement of the source by a new
   minimum or by a random gap law.

6. **The same moving inverse law.** The retained atoms are exactly
   `t_j=v_j/(N v_(r+j))`; injectivity prevents another root from adding
   mass to the same atom. Thus the remainder is exactly the expression
   in (19). Its residue-vector norm is at most its mass. Applying the
   Euclidean triangle inequality to all groups gives (20) and (21),
   including every cross-group term in the square of the sum. These
   formulas do not assume independent boxes.

7. **Diagonal and precision.** The r-step predecessor supports of the
   distinct roots are disjoint, since an ordinary endpoint has only one
   forward value after r steps. Each atom is therefore at most `1/N`,
   while the N retained atoms are each at least `c_0/N`. This proves
   `c_0^2/N<=D_(M,r)<=1/N`. Dividing the necessary lower diagonal by
   `sqrt(m)3^(-theta m)` gives exactly the little-omega requirement (24).
   The weaker condition `m^2=O(M)` does not imply it.

## Formal scope and review corrections

All sixteen public Lean declarations were inspected. The decoder,
quotient-interval bounds, supplied-affine endpoint bounds, source-block
identity, box injection, and weighted finite Cauchy statements match the
written interfaces. Arbitrary natural parameters, including modulus-zero
edge cases in the purely quotient/remainder lemmas, do not invalidate
those statements. The collision sums that require a positive modulus
state it or use `3^p>0` explicitly. The ordered-field inequalities permit
arbitrary signed supplied weights, a valid algebraic strengthening of the
nonnegative probability application.

The module does not construct an actual orbit or harmonic flow. The
occurrence-to-word aggregation, physical-floor estimate, infinite source
law and remaining-limit discussion are correctly left as written
arguments. No arithmetic bound on aggregated cross-box alignment is
claimed.

During this review, the author clarified that using `eta_M -> 0` to
make the remainder small takes `I={m,...,M}`; further trimming separately
pays the omitted spine mass. Formula (19) already contained that term.
The representative-endpoint explanation for repeated words was also
added. A separate reviewer corrected the asymptotic notation in (24)
to little omega. The hashes above bind all these clarifications.

The positive conclusions are the finite injection and its weighted
consumers. They do not prove the global collision upper, escape exclusion,
positive-cycle exclusion, or full Collatz.
