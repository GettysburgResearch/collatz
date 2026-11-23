# Expanding psi family: focused semantic review

**Verdict: VERIFIED for the stated finite paths, conditional certificate
transport, and strict common-rank descent.** This review concerns the new
`CollatzGlobal/PsiExpansion.lean` only. It does not repeat the earlier
orbit-lift or well-foundedness reviews.

Reviewed source SHA-256:
`12a891feaec71395f061b0d68fa3b11beff609a55b636ea78382319ce784a9fa`.

The frozen file passed an independent Lean 4.34.1 execution of
`lake env lean -DwarningAsError=true CollatzGlobal/PsiExpansion.lean`
with exit status zero. This is a focused development-file check; the final
clean-commit build and axiom audit are separate publication checks.

## Actual unbounded family

For every natural parameter `h`, the file proves

\[
m_h=106495+2^{52}h,
\qquad r_h=131455+3^{33}h,
\]

\[
T^{52}(m_h)=r_h,
\qquad T^{52}(3m_h-1)=3r_h-1.
\]

Both seed arms have exactly 33 odd steps. The upper initial value is
`319484 + 2^52*(3*h)`, so the upper high-bit lift uses parameter `3*h`.
Its endpoint is `394364 + 3^33*(3*h)`, exactly `3*r_h-1`.
There is no bounded enumeration of `h` in this argument.

The family increases in ordinary value: the constant difference is positive
and `3^33 > 2^52`. The input is a ternary unit when `h%3 != 2`;
the output is always congruent to one modulo three. These congruence facts
do not establish convergence of the upper source.

## Rank and goal direction

The proof separately checks both strict inequalities

\[
131455\,200^{52}<106495\,201^{52},
\qquad
3^{33}\,200^{52}<2^{52}\,201^{52}.
\]

Their affine combination gives `r_h*200^52 < m_h*201^52` for every `h`.
For a supplied clock `d >= 52`, this is exactly

\[
P(3r_h-1,d-52)<P(3m_h-1,d),
\qquad P(n,d)=(n+1)(201/200)^d.
\]

The factor three cancels because the scored value is the **known upper
source**, not the unknown lower target. The theorem
`psi_expanding_family_rank` uses these upper-source states explicitly.

The semantic implication has the correct recursive direction. An actual
upper-source witness at clock `d`, together with `52 <= d`, gives an
upper-child witness at clock `d-52`. A proof of `Basin r_h` then pulls back
along the lower finite path to prove `Basin m_h`. The target theorem states
the valid full basin equivalence. No change of goal kind is assumed.

## Concrete seed and limits

At `h=0`, the source certificate is actually proved:

\[
T^{196}(319484)=1,
\qquad T^{144}(394364)=1,
\]

and the file proves `ScoreLT (394364,144) (319484,196)`. A separate exact
recurrence replay reproduced both 52-step endpoints and odd counts, the
196-step hit, and the 144-step residual hit. The Lean concrete proofs use
short blocks of literal arithmetic joined by ordinary orbit/count
concatenation; each block is checked with `decide +kernel`.

For `h>0`, the file proves finite affine paths and the numerical descent
guard, but does **not** assert upper-source convergence. The source
transport theorem explicitly requires its actual hit witness and the
clock bound. The ternary-unit theorem supplies only its arithmetic side
condition. No universal rule cover, `ResidualPsiClosure`, or full Collatz
conclusion follows from this family alone.
