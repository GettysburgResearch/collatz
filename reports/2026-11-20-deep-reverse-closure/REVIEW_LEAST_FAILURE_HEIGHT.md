# Independent review of the least-failure height argument

**VERDICT: VERIFIED for H1–H5, at the source and artifact pins below.**
These results exclude specified families from containing the globally least
failure of the deep reverse implication. They do not establish the implication
for all inputs, or prove Collatz.

## Frozen material and independent method

The reviewed manuscript is `agent_deep_reverse/LEAST_FAILURE_HEIGHT.md`,
SHA-256 `55e31a4ce1b52b3536c7ddf36e29be8f790deac8ef97a77b3438274fccb93254`.
Its copied certificate is `agent_deep_reverse/deep_reverse_certificate.json`,
SHA-256 `fc15d65eabd0baa1dc5f99af47d430ce3a06b1da6414e4d3c4ae29e269b42571`.
The certificate originates in PR146 at commit
`e238c63a5d57f96bb063b7472498d1977df51951`; the copied data identifies the
original source-script SHA-256 as
`d90e723c8b9fc35fb08dd5547fd346d4c6926abcf188b36a1336603d5e03ae78`.

The independent checker `check_height_review.py` imports neither the source
author's checker nor the new height author's checker. It represents every
intermediate value by a global rational form `a*n+b`, then restricts that form
to each source progression. This differs from the author's progression-local
affine implementation. It checks every ordinary edge, every guarded tripling,
the complete cover, positivity, whole-cell contraction, and the exact maximum
conditional upper-antecedent height. It also recomputes the five integer
inequalities and both finite ordinary trajectories used in H3–H5.

Normal Python and `python -OO` produced byte-identical reports
`height-review-normal.json` and `height-review-optimized.json`. A deliberately
incomplete source cover was rejected. The checker uses explicit exceptions,
not assertions that optimization could erase.

## H1: complete height and legality audit

The independent replay confirms all of the following exact values:

| Quantity | Independently obtained value |
|---|---:|
| Source certificate rows | 71 |
| Common residue period | 62,208 |
| Covered odd ternary-unit residues | 20,736 |
| Expanded ordinary/extra moves | 3,974 |
| Extra tripling occurrences | 284 |
| Longest expanded path | 198 |
| Largest conditional upper-antecedent/source ratio | `2025217/23` |

The maximum occurs on the source cell `432*t+23`, at word position 21
(zero-based), where the extra-tripling input is `1327104*t+71199`. Replacing
that arrow by the two deep-reverse arrows yields larger upper antecedent
`(256/9)*(1327104*t+71199)+1`. At `t=0`, its ratio to the original source is
exactly `2025217/23`, which is less than 88053.

This maximum is a whole-progression calculation. For positive affine
denominator, the derivative of a ratio of affine functions has constant sign.
The supremum therefore occurs at the first allowed source or at the limiting
slope. The independent checker computes both. It does not extrapolate from
ordinary-value sampling.

The replacement of an extra arrow is also valid in its directed sense. If
`v=9h` is positive and odd, then `h` is odd. The two arrows
`64h+1 -> 128h+1 -> 256h+1` have eligible indices `h` and `2h`, and upper
antecedents at most `256h+1`. Ordinary edges identify the first endpoint with
`9h` and the last with `27h`, because
`T^6(64h+1)=27h+1`, `T^8(256h+1)=81h+1`, and each displayed even result has
the required ordinary half-successor. Thus convergence propagates backwards
along the substituted path in exactly the direction needed for H2.

## H2: the same global minimum supports every invocation

Let `X_*` be the least ordinary integer `128k+1` with eligible `k` for which
the upper integer converges and its lower companion does not. Minimality says
that **each eligible implication whose upper antecedent is below `X_*` is
valid**. It does not assert convergence of every integer below `X_*`.

The manuscript uses this statement correctly. Strong induction on positive
ternary units below `X_*/88053` certifies the final, smaller endpoint of the
H1 path. All conditional upper antecedents along that path are strictly below
`X_*`. Backwards convergence propagation then certifies the original source,
even if some other intermediate ordinary values exceed the induction source.
No larger intermediate value is assumed to converge before this backwards
argument. Even ternary units halve, and the source 1 is already certified.

For a general positive `n` with `176106*n<X_*`, strip powers of two to the
odd `q<=n`. If `q` is divisible by 3, `(3q+1)/2` is a positive ternary unit
strictly below `2n<X_*/88053`; otherwise `q` itself is already in the proven
unit interval. This establishes H2 with the strict inequality stated in the
manuscript. There is no change of the minimum from one rank or congruence
class to another.

The independently replayed directed certificates, together with this
replacement and induction, also justify the required logical implication
that absence of all deep-reverse failures implies Collatz. Thus assuming a
Collatz failure permits selection of the minimum used here.

The manuscript's final explanatory section was reread after its later
clarification that a successful remaining construction may depend on the
actual source and its certificate. That clarification changes no H1–H5
formula or proof. A finite bounded-word atlas is correctly distinguished
from the source-dependent task.

## H3: exact parity exclusions

Using the independently reviewed kernel formulas, a least failing upper
antecedent has

`X_*=(2^(c+6)*z-175)/81`, where `z>=1` is an odd ternary unit.

For even `c=2r+4` its lower residual is `3^r*z`; for odd `c=2r+3` it is
`2*3^r*z+1`. Both residuals are outside the basin if the companion is outside
the basin, because the normal form provides actual ordinary connections.

The coarse inequality `4^42>176106*3^42` is exact, and the bounds on the
two residual/source ratios are valid for all `z>=1`, `r>=0`. The sharper
even and odd inequalities are also valid, with positive initial differences
`64338362311137348850935` at `r=34` and
`146945227679902514612563` at `r=38`, respectively. If
`F_r=A*4^r-B*3^r-D`, then `F_(r+1)=3F_r+A*4^r+2D`, so these exact initial
comparisons persist for all larger `r`. H2 therefore excludes every even
`c>=72` and every odd `c>=79`. The separately solved `c=4` case can be
removed. The remaining list is exactly

`{1} union {3,5,...,77} union {6,8,...,70}`.

These exclusions hold for the globally least failure. They are not silently
strengthened to unconditional convergence results for every source with an
excluded valuation.

## H4–H5: rank exclusions and finite exceptions

At upper rank four, `z=1`, and the kernel congruence gives `c=54j+2` for
positive `j`. The height exclusion leaves only `c=56`; its residual `3^26`
reaches 1. Independent literal shortcut iteration confirms 219 clocks,
112 odd inputs, and peak 16286310253592.

At upper rank five, the `c=1` pure-power family has

`243*(X_*-176106*P)=2^(162j+77)-653-243*176106*3^(81j+32)`.

The initial difference at `j=0` is
`71818029920988665229141>0`, and positivity persists because the positive
exponential multiplies by `4^81`, while the subtracted exponential multiplies
by `3^81`. This excludes the entire family from containing the minimum.

For `c=3`, the corresponding difference is

`2^(162j+31)-1037-243*176106*3^(81j+10)`.

Its value at `j=1` is
`12554202350266279230985313864847138776593601623775633598729>0`,
and the same persistence argument applies. At `j=0`, independent shortcut
iteration verifies that the residual `3^10` reaches 1 in 89 clocks with
46 odd inputs and peak 1135052. Therefore this family also cannot contain
the least failure. Together with the already solved `c=4`, H4–H5 have the
precise scopes claimed in the manuscript.

## Remaining gap

The finite valuation list still allows unbounded `z` and unbounded stopping
certificates for the convergent upper source. None of H1–H5 supplies a
complete guarded route from every remaining lower residual to the known
convergent `z` or to the proven initial interval. Reusing the 71 source
paths above their guaranteed antecedent height would invalidate the minimum
argument. No such reuse, and no global closure, is endorsed by this review.
