# Scoped independent review: positive residual verifier and signed filters

**Verdict: VERIFIED at the exact bytes below.** The positive-decomposition
verifier correctly certifies its four finite residual bounds, and SF1--SF3
are valid with their stated domains and quantifiers. Neither result proves
Collatz, an all-clock diagonal-moment bound, or regularity of the actual
pointwise infinite product.

## 1. Frozen artifacts

The reviewed sources are in `research/global-rigidity-20261120` of the
integration worktree. Hashes refer to their complete file contents.

| Artifact | Bytes | SHA256 |
|---|---:|---|
| `check_ordinary_spectrum_independent.py` | 5045 | `1a7dbc1c157b2dfb3df92fd09175516371551d0fcf1cdfbf079b8a016a3f4e55` |
| `ordinary-spectrum-independent-report.json` | 2337 | `a9ab7014ee9a1484880e200432069e4480a92df92f6c3f41f6807314cc73309f` |
| `SIGNED_CLOCK_FILTERS.md` | 6393 | `051ee11cbb58009819af5542b43bf7e9dab65f59cbbcc8771b1b46151543bf18` |

The spectral verifier authenticates the original producer at SHA256
`395beaf29efeb7f66b88e346d04451e04b089cad63ee8b434c6ac9806feba0d4`.
The source-independent filter theorem uses the ordinary definitions of
`SMOOTHING_BOUNDARY.md`; no packing or harmonic-trace input is needed.

## 2. Positive residual decomposition: reconstructed directly

Let `S` be a finite set of positive odd states, forward closed up to a
root `t0>1` whose next odd image is 1. Let `ell(x)` be the first-hit
depth to the root. For `s=1,2` and `|z|=1`, set

\[
 g(x)=1_S(x)x^{-s}z^{-\ell(x)}.
\]

The norm of `(A_s-zI)g` is the sum of three disjoint nonnegative pieces:

\[
 t_0^{-2s}
 +\sum_{x\in S\setminus\{t_0\}}(1-c(x)^s)^2x^{-2s}
 +\sum_{t\in S}t^{-2s}
  \left[z_s(t)-\sum_{x\in S:Ux=t}d(x)^{2s}\right].       \tag{1}
\]

At the root, the image is outside `S`, giving the first term. At an
inside nonroot, the depth decreases by one and
`A_sg(x)=z*c(x)^s*g(x)`, giving the second term. An outside source has
at most one parent, so its contribution groups without interference
by that parent in `S`. The full column `z_s(t)` is the exact infinite
geometric predecessor sum; subtracting the inside children gives the
third term. Every bracket is nonnegative. Dividing by
`sum_{x in S}x^{-2s}` gives the normalized squared residual. This
proves (1), including its validity simultaneously for the whole unit
circle, without using cancellation of signed scalar sums.

The code implements precisely this decomposition after multiplying all
mass and residual terms by `t0^(2s)`. Its root contribution is then
exactly one. `full_column` independently sums the legal exponent
parity, obtaining the same `0,3/5,12/5` or `0,27/85,432/85` columns.
Every omitted predecessor is accounted for in these full columns.

## 3. Verifier interface and interval directions

The verifier replays each supplied ordinary edge by forming `3n+1`
and computing its exact trailing power of two. It rejects duplicate
vertices, malformed integer rows, invalid odd states, a wrong root,
missing parents and incorrect depths. The root is recomputed from its
explicit parameter. Because nonroot depths strictly decrease, the
checked finite graph gives actual paths to that root and then to 1.

The only original construction routine called is `build_tree`; its
bytes are authenticated before loading. The verifier does not call
the author's verification or residual routines. Producer helper calls
remain part of construction, not independent acceptance evidence.

For each nonnegative term `y`, the integer interval
`floor(2^128 y) <= 2^128 y < floor(2^128 y)+1` is valid, including
zero terms. The accumulated residual lower and upper sums therefore
enclose (1). If `Mlo` is the sum of the 512 scaled mass floors, actual
scaled mass lies between `Mlo` and `Mlo+512`. Accordingly

\[
 \frac{Rlo}{Mlo+512}\le\frac{R}{M}\le\frac{Rhi}{Mlo}
\]

has the correct outward directions. The positive denominator is
explicitly checked. Final acceptance compares exact `Fraction`
values with the squares of the claimed rational norm bounds.

The support digests agree with the original construction. I executed
the complete independent verifier normally and obtained a byte-identical
copy of the frozen report. The four accepted strict norm bounds are
`93/1000`, `2/125`, `41/1000`, and `31/10000` for the two operators at
roots `k=6,8`. The report includes 336 and 348 nonzero external-fiber
terms, respectively; those terms are not silently dropped. The root
author also supplied matching normal/optimized executions. My review
does not relabel those additional executions as separate runs by me.

This is independent acceptance arithmetic for two finite supports. The
infinite essential-spectrum theorem still rests on its written proof.
It does not turn a small residual into an exact eigenvector or a failure
of Collatz convergence.

## 4. SF1: arbitrary finite landing clocks are correctly realized

Fix `ell>=1`. The condition that `H` is even and `3^(ell-1)|(H-1)`
gives `v3(2^(H-1)+1)>=ell`. Hence the displayed `m` is a positive odd
integer; it need not be a ternary unit, and the theorem does not require
it to be one. Substitution in the displayed `x_j` proves exact gap one
for `j<ell-1`. The final pre-landing state is `(2^H-1)/3`, with exact
gap `H` and next odd state 1.

The product's clock convention is correct: the first `ell` inputs are
the large pre-landing states. Thus the limiting product is one through
clock `ell`, and the factors `3/4` begin at clock `ell+1`.

The neighboring decomposition has rational base
`rho_ell=1+(2/3)^ell`, which is positive and odd in the 2-adic sense.
Its denominator is odd, although it may contain powers of three. This
is permitted by the rational odd-map argument. Every fixed finite
trajectory has finite positive valuations because `3x+1` stays positive
and never equals zero.

If `A_q` is the total of a fixed rational valuation prefix, choosing
`H+ell-1>A_q` suffices to preserve every gap in that prefix for the
adjacent ordinary source. The affine difference formula then holds
exactly. At each fixed clock its positive real difference tends to
infinity, so the neighbor's finite product tends to one. The order of
quantifiers is fixed `ell`, fixed `q`, then sufficiently large `H`;
there is no uniform infinite trajectory identification.

## 5. SF2--SF3: signed and complex quantifiers are sound

For an arbitrary complex `l1` coefficient sequence, the bound
`|alpha_q r_q(n)|<=|alpha_q|` justifies dominated summation along each
SF1 family. Thus the adjacent limit is exactly `A-G_ell`. If adjacent
smoothing holds, all `G_ell` equal `A`. Their consecutive difference is

\[
 (1-c_*)\sum_{q\ge\ell+1}\alpha_q c_*^{q-\ell-1}.
\]

The absolutely convergent tail `H_ell` satisfies
`H_ell=alpha_(ell+1)+c_* H_(ell+1)`. All such tails vanish, forcing
every coefficient at clocks at least two to vanish. Conversely a
filter supported at clocks zero and one is `alpha_0+alpha_1 c(n)` and
has vanishing adjacent differences. No normalization or positivity
is needed for this complete classification.

For SF3, pointwise disappearance of coefficients handles any fixed
finite clock range. The uniform total-variation bound controls the
remaining geometrically weighted tail. Therefore `G_1^(v)->0` even
for complex coefficients. Since the total sum is one, the spatial
limsup is at least `|1-G_1^(v)|`, and the stated outer liminf is at
least one. Equality is not asserted and need not hold for signed or
complex filters. The bound on total variation is a real hypothesis;
the argument does not cover unbounded variation or conditional sums.

## 6. Small independent exact controls

`review_signed_clock_controls.py` imports none of the source code. It
constructed 18 admissible ordinary neighbor pairs for landing times
1 through 6, checked 279 literal ordinary edges, and compared 12 odd
steps of each neighbor with the rational prefix and exact affine
difference. It also checked the product at the landing clock and the
subsequent powers of `3/4`.

One signed control is particularly useful: the normalized filter
`(alpha_0,alpha_1,alpha_2,alpha_3)=(4,0,-7,4)` has `G_1=1` but `G_2=0`.
Thus its jump cancels for the original one-step landing family, but
not for the new two-step family. This directly checks why the
arbitrary-landing construction is needed to exclude signed cancellation.

Both normal and optimized control runs passed with identical output.
Their frozen identities are:

- `review_signed_clock_controls.py`: SHA256
  `6928db229879b9d6363e8f8be7109bceb660f2173a348b3c05a5071c9e3ff066`.
- `signed-clock-review-report.json`: SHA256
  `d8a10793ebd788410e16f0015799ece2e6d66a3a2551be4e7b54c065784f96fd`.

The finite controls supplement the reconstructed proof; they do not
establish the theorem's arbitrary-horizon quantifiers by enumeration.

## Final boundary

The signed-filter annex closes the exact source-independent summable
linear-filter possibility that the earlier positive-averaging note
left open. It does not address source-dependent stopping, nonlinear
methods, unbounded-total-variation regularization, or the regularity
of the actual pointwise limit. The positive residual verifier checks
small approximate eigenvectors on convergent supports, not exact
nonperiodic-component vectors. Those distinctions are preserved in
the reviewed files and are essential to this verdict.
