# Independent review of the repaired Farkas certificates

**Outcome: VERIFIED within the two stated point scopes.** This record
preserves the independent merger reviewer's derivation and checks, reported
to the assembling agent on 2026-11-20. It is an argument and arithmetic
review, not a proof-assistant certificate or a Collatz resolution.

Reviewed checker:
`research/gemini-dirichlet-global-20261120/check_farkas_and_ruelle.py`,
SHA-256 `5f26580b11b45b6ed3a1bcecce2b2c66bbaabe6f6c8a1901d6bbad7fb51f5829`.

Reviewed supplied decimal-vector file:
`farkas_certificates_r4_r6.json`,
SHA-256 `ab41ca28f00904efa2732ffbdc06f19b592ae4e874b586554c550c2f975bde5c`.

The companion audit is pinned at SHA-256
`c907cfc33d842457b0173b73814f7b91644954c13398d37ef7c38ed7bc2509c7`.

## Residual coordinates reconstructed independently

Let `M=3^r`, `P=M/3`, and interpret `2^{-1}` in subscripts as the inverse
of two modulo `P`. Directly from the supplied matrix rows, the residual
at coordinate `j` is

\[
C_j+A_j2^{-s}+B_j3^{-s}+F_j(2/3)^s,
\]

where

\[
\begin{aligned}
C_j={}&w_{\rm norm}-u_j
 +\mathbf1_{j\equiv2\ (3)}w_{(j-2)/3}
 +\mathbf1_{j\equiv0\ (3)}w_{P+j/3},\\
A_j={}&u_{2j\bmod M},\\
B_j={}&w_{(2j-1)2^{-1}\bmod P}-w_{P+(j\bmod P)},\\
F_j={}&-w_{(j-1)2^{-1}\bmod P}.
\end{aligned}
\]

The reviewer compared these closed formulas, derived separately from the
checker's accumulation loops, against every coordinate returned by
`coeffs()`: all 81 plus 729 coordinates matched exactly. The identity
`(2/3)^s * 2^(-s) = 3^(-s)` is collected algebraically. No equality of two
independent floating approximations is assumed.

## Contradiction sign and exact normalization

For a feasible `v>=0` with `Av<=0`, `Bv=b`, and `u>=0`,

\[
(u^{\mathsf T}A+w^{\mathsf T}B)v\le w^{\mathsf T}b=-1.
\]

The verified strictly positive residual coordinates and `sum(v)=1` make
the left side strictly positive. This is the required contradiction.
The repaired audit correctly uses an inequality; the original source's
explanatory comment incorrectly discarded `u^TAv` as if it vanished.

## Outward intervals

The review checked the logarithm tail

\[
R_N\le\frac9{4(2N+1)3^{2N+1}},
\]

the positive exponential tail

\[
R_L\le\frac{2^{L+2}}{(L+1)!},\qquad0\le x\le2,
\]

binary normalization, positive-power products, reciprocal enclosure,
coefficient-sign endpoint selection, and the final scaling denominator
`10^10 * 10^50`. The decimal multipliers are parsed as exact rationals.

The reproduced minimum residual enclosures are:

| Point | Certified minimum residual interval |
|---|---|
| `r=4, s=21/25` | `[0.999999999412877118, 0.999999999412877119]` |
| `r=6, s=913/1000` | `[0.999999999270272552, 0.999999999270272553]` |

## Scope and negative controls

The checker explicitly accepts only these two `(r,s)` points. It provides
neither an interval covering all smaller exponents nor an `r=8` certificate.
The exact uniform feasible primal at `s=1`, and the negative residual of
each supplied dual there, are consistent with this boundary.

For the v2 comparison, the source matrices have source rows and
inverse-target columns. This matches the constant-target-column-sum
proof in the audit. Its spectral formula concerns the stated hidden-lift
averaged matrices; it supplies no theorem for mass transported from one
fixed ordinary source.

No defect was found in this requested scope. No new threshold scan was
performed. The root agent separately checked the interval remainders,
coefficient signs, and stated finite/infinite distinction during assembly.
