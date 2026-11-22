# Independent review of the rational-shadow compiler

**Reviewer:** `inverse_clock_attack`  
**Date:** 2026-11-22 UTC  
**Verdict:** VERIFIED for the finite physical compiler and its stated
source-language corollaries at the frozen files below. No universal
source coverage or rational periodicity theorem is supplied.

| Frozen file | SHA256 |
|---|---|
| `RATIONAL_SHADOW_DISPATCH.md` | `6124f2dc2796400a8a70b184a23cbde7ff141ce850aaca1d4c94ae847c22fce8` |
| `RationalShadow.lean` | `a8b69dbc0c1c3749568a77c3ea4934f7a6060cb2c468985f1994cffddb4eac69` |
| `RationalSourceBlock.lean` | `3f60b9ce66e8c1139560b3cac50a9e644e196aafcd6c57f972259393fbec8d73` |

These match the final manifest SHA256
`0c227f7c9e30c728116e1dffaf334d199804fa5bb31ec4a1bf087885a031c8b6`.

## Independent mathematical reconstruction

The odd denominator gives an exact parity lift from
\(Dn=2^jv+h\) to \(DT^j(n)=3^{o_j}v+h_j\). The resulting paid
inequality compares the endpoint with the same current target.

The full block numerator obeys the displayed recursion, and iteration
gives \(b^e(Du-C)=a^e(Dr-C)\). Odd/even coprimality gives the complete
source pin. When \(2^{Le}>C\), a negative displacement is impossible,
leaving the exact integer fixed point or a positive integral
displacement. The composed compiler pays the latter uniformly using its
unit-displacement inequality. The fixed point remains an explicit
exception or is discharged by a separate finite target certificate.

The written threshold recipe follows from a supplied contractive
rational prefix and the growth of the source repetition horizon. An
explicit positive rational cycle suffices to produce such a prefix;
the note does not assert universal rational periodicity.

A separate Python integer replay, independent of the author's checker,
confirmed the six-clock gap-4 prefix to numerator 179, its 24-clock
return with 15 odd steps, and its first contractive total prefix
\((j,o_j,h_j)=(192,121,131)\). It reproduced the exact margin

\[
2^{192}-3^{121}
=886070835643387132596249934678851296907928561850481193693.
\]

## Formal evidence and scope

I inspected the final Lean source, strict-build receipt, and axiom logs.
The producer's receipt records exit code zero with warnings treated as
errors for both modules: 15 public audits in `RationalShadow`, 9 in
`RationalSourceBlock`, using only subsets of `propext`, `Classical.choice`,
and `Quot.sound`. I did not run a separate Lean rebuild for this review;
integrated fresh replay is the coordinator's separate verification event.

The actual source trace, complete affine constant, horizon, coefficient
inequality, and fixed-source exception are genuine inputs. The note
correctly retains the original-target comparison if a macro is first
moved to a larger carry, credits the prior gap-3 result, and does not
claim that a finite repetition dictionary covers every source word.
No substantive correction is requested at these hashes. Global source
coverage remains open.
