# Independent review of the residual-unit cycle bridge

Date: 2026-11-23. Reviewer: `nov23_escape`.

**Verdict: VERIFIED at the stated written-proof and finite-formal scopes.**
I reconstructed the principal-binomial proof, the complete unit
classification, the repetition interface, and the semantic connection of
the twelve public Lean declarations to those arguments. I found no
implicit assumption of Collatz convergence and no missing parity phase.

## Frozen files and read scope

Both files were read in full. These hashes delimit this review:

| File | SHA-256 |
|---|---|
| `/workspace/scratch/c6766c1207a3/collatz_work/nov23_root/ResidualWord.lean` | `420d1eb7976dca248cc4e85846586e253751379907739bc6a2bd816aca3f79e6` |
| `/workspace/scratch/c6766c1207a3/collatz_work/nov23_cycle/RESIDUAL_UNIT_EXCLUSION.md` | `3d6619371246f4918e0c5a57eee2ef1c2f08b76c0794fddcaba869baab498eaf` |

The source continuation is PR185 at
`39ba48e6a8af781193e28c679ea8ab64663c3aa6`. This review did not run Lean,
replay earlier modules, or rebuild any cache; compilation remains the
root agent's separate evidence. It does not review the optional
all-factor theorem or the separately cited control-family construction.

## Written principal-binomial proof

For coprime positive `a,b`, every monic integer factor of
`X^b-2^a` has all roots of modulus `2^(a/b)`. If its positive degree is
`h`, its nonzero constant coefficient has absolute value `2^(ah/b)`.
Integrality and prime factorization force `b|ah`, hence `b|h`. A proper
nonconstant factor is therefore impossible. Gauss's lemma supplies the
monic integer factor needed when starting with a rational factorization.
This also handles `b=1`.

The parity numerator is strictly positive at the positive root. Hence
the principal irreducible polynomial cannot divide that numerator or
its common factor with `F`. It survives in `F_0`, and monic division
preserves the integer coefficient domain. Its value at three supplies
the stated positive integer divisor of `D_pol`.

If `D_pol=1`, the difference `2^a-3^b=1` forces `a=2,b=1` by the
displayed elementary modulo-eight argument. Thus `A=2p`. Every root
of the monic residual polynomial has modulus four; each distance from
three is at least one. Product one forces all roots to equal four.
The original binomial is squarefree and the residual is nonconstant,
so the residual is exactly `X-4`. Neither multiplicity nor the
degree-one case is omitted.

The repetition equivalence is also valid: the geometric quotient has
separated coefficient blocks, giving the repeated exponent profile;
conversely, its residual degree-`b` factor is irreducible and cannot
divide the shorter numerator. The extra degree bound for primitive
words follows because every monic factor degree is divisible by `b`.

## Formal-to-written linkage

`principal_factor_survives` expressly assumes irreducibility and a
positive real root. It proves the polynomial divisibility implication
using numerator positivity. It does **not** formally establish the
general reduced-binomial irreducibility or the complex-root unit
classification. The file header and written note correctly distinguish
those scopes; the irreducibility premise is not a hidden axiom.

`quotient_of_linear_residual` uses exactly the factorization obtained
after the written root-modulus argument. The subsequent degree and
coefficient lemmas correctly force
`d_i=d_0+2i`. The bound on the last position gives `d_0<=1`, including
`p=1`. `ordinary_realizer_of_linear_residual` assumes the necessary
ordinary fixed-point equation and proves `n=1` or `n=2`; it does not
assume any universal ordinary-cycle assertion.

For clarity, the actual shortcut map is
`T(n)=n/2` for even `n`, and `T(n)=(3n+1)/2` for odd `n`.
For an actual length-`A` parity word with ordered odd positions `d_i`,
its affine iterate is

\[
 2^A T^A(n)=3^p n+\sum_{i<p}2^{d_i}3^{p-1-i}.
\]

Thus an actual cycle satisfies exactly the equation used by the Lean
realizer theorem after `A=2p`. In phase `d_0=0`, the word is `(10)^p`
and `n=1`; in phase `d_0=1`, it is `(01)^p` and `n=2`.
Both are legal actual words because `T(1)=2` and `T(2)=1`. The two
phases are retained, not accidentally collapsed into one ordinary
starting value. This explicit shortcut-map paragraph could be added
to the main note for readability; it is not a mathematical repair.

The remaining nonunit evaluation condition is still
`D_pol | Q_0(3)`. Polynomial coprimality and positivity at a real root
do not exclude integer cancellation at `X=3`; the reviewed note states
this limitation correctly. The new result closes the polynomial
residual-unit exception, not the complete positive-cycle problem.
