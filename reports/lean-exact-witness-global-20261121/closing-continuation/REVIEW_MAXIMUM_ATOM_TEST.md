# Independent review of the maximum-atom test

Date: 23 November 2026. Reviewer: `cycle_exclusion`.

## Frozen source and verdict

Source: owned PR177 continuation, based on
`6de3e304bb49a93a6c5ef0e5563137e75c7defb4`, file
`research/lean-exact-witness-global-20261121/MAXIMUM_ATOM_TEST.md`.

Reviewed SHA256:
`c6c800ae9e98065e1c4915cf39a1c8fbcd96d04bf88be295e822bbfeb0bc729f`.

**VERIFIED WITH THE OPERATOR-DOMAIN QUALIFICATION NOW PRESENT:** MA1--MA5
and the four-row table, as written deductions conditional on the stated
positive-product component measure. This review independently derives
the new formulas and maximum-root restrictions; it does not audit the
external PR182 proof modules or repeat the historical product-positivity
proof. No ordinary escape exclusion follows, and none is claimed.

## Reconstruction

Because `0<r(n)<=1/n`, a maximum `M=r(m)` is attained: after fixing one
positive value, only finitely many ordinary indices can exceed it.
The edge relation is

\[
 r(q_k)=(3/2^{a(q_k)})r(q_{k+1}).
\]

It gives `w_k=3^k/2^(A_k)=M/r(q_k)>=1`. Equality is impossible for
`k>0`, by unique factorization of powers of 2 and 3. Thus MA1 is strict.
All `q_k` are distinct on the hypothetical escaping component.

On the ordinary domain, direct singleton transport gives

\[
 P_s\mathbf1_{\{q_k\}}
 =(3/2^{a(q_k)})^s\mathbf1_{\{q_{k+1}\}}.
\]

This proves MA2 exactly. Integrating its finite support against the
component measure gives boundary mass

\[
 w_{N+1}^s\mu_{E,s}(\{q_{N+1}\})=M^s,
\]

which proves MA3 without a limiting interchange. In fact
`integral F_N dmu_(E,s)=(N+1)M^s`. The increasing infinite-ray test
is pointwise finite but has infinite component integral, so its formal
strict deficit at `m` cannot be integrated as a finite identity to
remove the boundary.

The physical product telescopes to
`Lambda_k(m)=m w_k/q_k`. Hence

\[
 D_s(\{q_k\})w_k^s
 =m^{-s}(\Lambda_k(m)^s-\Lambda_{k+1}(m)^s).
\]

Summing first to a finite depth, then taking the monotone limit, gives
`m^-s-M^s`. The residual atom is directly
`m^-s Lambda_infinity(m)^s=M^s`. This proves both parts of MA4.

The root restrictions can also be recovered directly from maximality.
The first forward ratio must exceed one, forcing `a(m)=1`, hence
`m=3 mod 4`. A legal gap-one parent would have value of `r` equal to
`3M/2`, which is impossible. For ternary units such a parent exists
precisely when `m=2 or 8 mod 9`. Excluding these two classes gives
`m mod 36 in {7,19,23,31}`.

For each remaining class, legality is exactly
`2^e m=4 or 7 mod 9`. Enumerating the six powers of 2 modulo 9 gives
the legal exponent pairs `(4,6)`, `(2,4)`, `(3,5)`, `(2,6)`.
Summing `3*2^-e` over the resulting geometric progressions gives,
respectively, `5/21`, `20/21`, `10/21`, `17/21`. Every legal exponent
is at least two, so each branch weight is below one and the displayed
bound for all `s>=1` follows. Meanwhile `a(m)=1` gives MA5 directly
from edge balance. The row bound and nonvanishing boundary are
therefore compatible exactly as stated.

## Scope qualification applied before freeze

The singleton transport identity is valid on ordinary roots `O`.
For the full ternary-only operator on `Z_3^times`, a singleton at `n`
also contributes at dyadic rational roots `(3n+1)/2^e` with
`e!=a(n)`. I raised this distinction before the source froze; the
reviewed version explicitly restricts MA2 to `O` and explains the
extra branches. Both component and defect measures are supported on
`O`, so the restriction preserves every integration used here.

The exact saturation proves that this particular finite maximum-atom
test does not eliminate the escape remainder. It is not a proof that
all possible tests or all uses of the common-root restrictions fail.
