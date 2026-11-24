# Independent review of complete denominator rigidity

23 November 2026. Reviewer: `density_free_germ8`.

**Verdict: PASS for the written statements R9-P1--R9-P6 in their
stated domains.** The complete-denominator and finite-realization
arguments reconstruct. The finite-field estimate is correctly limited
to a prime modulus. No all-time ordinary carry control, universal
rationality theorem, or proof of Collatz follows from these results.

## Exact review binding

Parent: `6352608dd6c04735e1f8bd86fef4ebc97b1aeacb`.
Paths below are under `research/scalar-rigidity-round9-20261123/`.

| File | Git blob | SHA256 |
| --- | --- | --- |
| `PHASE_RIGIDITY.md` | `0fe27307dd075284bc03ac93ce9c40925b45f2bc` | `4c87b64c237f3fbc9d02c308fa9a94050046adf664cbe9f88282505d1b3d79a4` |
| `phase_controls.py` | `c42a1ed4036f5748b6d9a35043424acb56233ca9` | `612c8e0231416caa3a7989b1a41bdb673597d5c6530b5398d61049fd96d57ad1` |

The actual scalar bounds and phase contraction are the exact parent
dependencies identified in the note, including the strict bound
`h(q)>1/2` and the verified ordinary floor `Q=31`. The review does not
replace these with a statement about independent random gaps.

## Reconstruction of R9-P1--R9-P4

**Complete fibers.** The complete order ratio in (4), together with
equal prime support, makes every projected residue occur in all M
distinct unit lifts. For `0<f<1`, the lifts `(b+f)/M` have average
`1/2+(f-1/2)/M`. Counting those at or below one half gives the stated
odd and even formulas, including the exact-half convention. Since
`m(f)>1/2` and `f>0`, the strict lower mean is valid. The exclusion
for `M>=4` uses the parent phase theorem at the whole denominator.

**Support caps.** For an odd prime p, the p-adic valuation of the
order contributed by the other prime powers is exactly `ell_p`:
lifting at q adds only q-powers, and the binary factor adds only
two-powers. Once `k>w_p+ell_p`, lowering k by one therefore lowers
the complete order by p, and preserves the prime support. This is
precisely the complete-fiber hypothesis. The binary reduction by
two similarly lowers the complete order by four when
`a>=max(5,ell_2+4)`.

For the remaining `a=4,ell_2=0` case, the binary order four is
coprime to the odd-component order. Fixing the latter residue yields
four CRT lifts with lower b-values r,s differing by 2 or 6 modulo 8.
Their mean is at least `3/4+((r+s)/2+f)/16>=13/16>4/5`.
This also covers the trivial odd component. Thus the boundary case
uses exactly the stronger verified-floor hypothesis it needs.
The support bounds `96800` for `{5,11}` and `1456` for `{7,13}`
recompute correctly.

**Doubling identity.** On unit fractions other than one half,
`m(f)-1={2f}-f`. For an odd denominator, multiplication by two
permutes the cosets; for an even denominator greater than two, it
projects uniformly to the orbit modulo half the denominator. These
give (10) and (11) with their stated domains. A power of three
equal to two forces mean one in every coset. The note correctly
does not infer transport of an actual source into a different coset.

**Low families and sharpness.** The displayed minimum lifts give
the exact canonical words, periods, reduced denominators, and means
for both families. For `d=2(3^N-1)`, the order is `2N`, and the
two-fiber formula gives `3/4+1/(4N)`. The strict clock bound reduces
at `N=6` to `2^19<3^12`; every earlier prefix has smaller or equal
average charge, and complete repeats preserve the strict inequality.
For even N, an odd prime divisor of `3^(N/2)+1` exists and its
tripling order has binary valuation exactly `v_2(N)`. Every other
odd factor has order dividing N. Consequently the binary support
cap is attained. These are arithmetic phase examples, without an
asserted positive ordinary infinite realization.

## R9-P5: actual finite sources and the departure gate

The denominator `3^L-2^A` is positive and odd for the words used.
Every cyclic rational state has an odd carry numerator and the
same odd denominator, so the prescribed valuations of the negative
rational cycle are exact. Choosing the positive odd residue modulo
`2^(A_K+1)` preserves them through K: at the i-th state the
difference has valuation at least `A_K+1-A_i>=g_i+1`.
All constructed ordinary states are positive by their literal odd
step equations.

Since every gap is at most three, the source has at most `3K+1`
bits. The ordinary bound `q_(i+1)<=2q_i` gives at most `4K+1`
bits at the endpoint. The parent's actual tail bound and the exact
discounted-tail identity then give (14). Compatible least positive
residue representatives are nondecreasing as the modulus grows.
If bounded, they would eventually be a fixed positive integer equal
to the negative rational 2-adic limit, which is impossible. Thus
the stated sources tend to infinity, while their scalar values tend
to the fixed phase. This does not identify a fixed positive source
with that infinite canonical word.

For the first family, an exact equality `h(q)=u_N` starts with zero
integer carry. At its first valuation departure, a larger gap
violates the strict scalar lower bound; a canonical one cannot be
replaced by a smaller positive gap. The departure must therefore
replace a terminal two by a one. After j full periods the original
state difference has valuation `j(N+1)+(N-1)+1`, proving (15).
At N=2, the successor identity `n+7=3(q+5)/2` gives the stated
equivalent valuation gate for the 7/8 phase. Later carries remain
unrestricted by this necessary gate.

## R9-P6: primary-source and normalization check

I directly inspected Section 1 of Kurlberg's [author PDF](https://people.kth.se/~kurlberg/eprints/short_expsum.pdf),
*Bounds on exponential sums over small multiplicative subgroups*
(2007), [arXiv:0705.4573](https://arxiv.org/abs/0705.4573).
The complete subgroup estimate there follows from multiplicative
character orthogonality, the nontrivial Gauss-sum magnitude, and the
principal-character sum. A coset is covered by rescaling the
nontrivial additive character. No stronger small-subgroup theorem
or composite-modulus estimate is needed here.

For the note's sampled function, the cyclic first difference equals
`1/p` at every residue except one, where it equals `1/p-1`.
Its mean is zero. The unnormalized nonzero Fourier coefficients
therefore have magnitude `1/(2|sin(pi k/p)|)`. Inversion contributes
`1/p`; pairing k with p-k and using `sin(pi k/p)>=2k/p`
leaves exactly `sqrt(p)/(2t)` times the stated harmonic sum.
Squaring the sufficient strict bound of 1/5 gives (17).
The deduction is sound for the complete residual prime p, without
an assertion that the same formula applies to a composite modulus.

## Finite controls and remaining scope

I inspected the full control source, including its exact order and
valuation routines, terminal odd cylinder replay, finite source
enclosures, first-departure checks, support boundaries, and rational
prime threshold. The checks use explicit exceptions and exact
integers or fractions; they remain active under optimization. In
particular, the controls do not compute an actual infinite scalar
by silently substituting its rational periodic candidate.

The author reports normal and optimized runs passing 14,768 checks,
including 62 actual positive cylinders and 1,152 departure gates.
This review inspected those calculations and their mathematical
scope; execution receipts and the publication replay belong to
the owner/root, not to a new broad run by this reviewer.

The universal proofs are written mathematics. The code's finite
domains do not make them Lean theorems. The first unresolved step
remains control of later integer carries on one fixed actual
positive ordinary source, or an additional arithmetic construction
that excludes the surviving phases and irrational scalar values.
