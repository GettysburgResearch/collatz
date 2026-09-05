# X-ASTRA-003 — unbounded packets and ordinary averaged drift

**Status: exact finite support; all new theorem-level claims PROPOSED.**
Proofs, all-scale induction, and the open end-to-end target are in
[RUN_RENEWAL.md](../../research/astra-critical-mass/RUN_RENEWAL.md).

This experiment is not a proof of Collatz or of the signed discrepancy budget.
It supports a positive ordinary averaged-drift theorem and refutes an invalid
iteration of that theorem on the actual transported distribution.

## Exact mathematical surfaces

A packet contains all consecutive shortcut-odd steps followed by all consecutive
even steps. With n odd, a=v2(n+1), m=(n+1)/2^a, and b=v2(3^a*m-1), its endpoint
is F(n)=(3^a*m-1)/2^b. Packet lengths are unbounded over ordinary sources.

The written proof and exact rational certificate establish:

- mean sqrt((F(n)+1)/(n+1)) < 22/25 over every dyadic odd-source shell
  (2^m,2^(m+1)] with m>=18;
- (9/8)^2 times the corresponding two-packet mean <19/20 for m>=128;
- an ordinary finite-packet moment asymptotic for the precise exponent/range
  in T-ASTRA-016, not a replacement of ordinary sources by random parities;
- an analytic bound for the complete omitted inverse even-run sum.

The finite arithmetic rows alone do not prove all scales. Section 4 of the
proof supplies the 25-scale induction and its explicitly bounded factors.

## Corpus and implementation independence

- 237 exact one/two-packet residue cylinders, total length at most 12.
- 63 complete inverse lists at odd endpoints 3..127, even-run bound 6.
- 40 rigorous intervals for the whole infinite inverse-run seed kernel.
- 50 cofinal-base drift inequalities and five exact induction ratios.
- Every positive n<=262144 reaches 1. Maximum shortcut time: 278 at 230631;
  maximum packet count among odd sources: 65 at the same source.
- 25 all-source mass intervals, at packet indices j=0..24.
- Six resealed corrupt reports rejected, including wrong scope, missing
  cylinders, understated tail, missing cofinal coverage, and a false cycle verdict.
- The generalized shortcut 5x+1 cycle 13,33,83,208,104,52,26,13 is a retained
  nonterminating control, not evidence about the standard 3x+1 map.

The generator uses closed-form powers and valuations. The verifier uses actual
shortcut steps to identify runs, lifts parity bits instead of solving the
final congruence, and checks inverse lists by exhaustive forward enumeration.
For an inverse list with endpoint y and even length b<=6, every possible source
is less than 64*y; the enumeration has no unproved source cutoff.
The two profile implementations use different exact integer-square-root
identities. Both programs have the same author: this is implementation
independence, not independent mathematical review.

## The infinite-source profile is not a finite sample

Set H=2^18 and lambda=9/8. On odd n in the shell indexed by m>=18, use

    h0(n) = 2^(1-m-4*(2^m-H)).

This positive seed is exactly shell-flat and has full support above H. The
height-weighted killed transfer telescopes to the factor
sqrt((F^j(n)+1)/(n+1)). Write M_j=lambda^j times its total mass.
Only the first shell is enumerated. A proved height envelope bounds the whole
omitted source population, whether or not any omitted source converges:

    omitted M_j <= 2^(-216657) < 2^(-120),  0<=j<=24.

Integer square roots at 96-bit directed precision enclose the enumerated part.
The complete rational intervals certify

    M_21 < M_22 < M_23 < M_24.

Thus the fresh-shell factor 99/100 for the discounted mass cannot be iterated
on this actual transported full-support seed. This is a finite-packet
counterexample to that inference, not a refutation of long-run mass decay or
of the weaker signed sublinear discrepancy target.

## Replay

From the repository root:

```bash
python experiments/X-ASTRA-003-run-renewal/run.py \
  --check experiments/X-ASTRA-003-run-renewal/results/canonical.json
python experiments/X-ASTRA-003-run-renewal/verify.py \
  experiments/X-ASTRA-003-run-renewal/results/canonical.json --self-test
```

Both commands passed at the exact committed file contents. Semantic SHA-256:

    1fd9982ca3d98d2dbc647b42aa01b05f178c64fc48a26ed2211c4e329c1f23bf

The compact certificate records 64-bit outward mass intervals and a digest
of the entire reconstructed row set. To materialize every exact row, add
`--full-output /tmp/astra-run-renewal-full.json` to the generator command.
The full replay payload SHA-256 is

    21fbe04f3e3aaffff114bbf6908654af130dda993653a2f6472e18b6dfdfeeb6

The all-time signed discrepancy budget, the original Green bound, SC*, FC*,
and full Collatz closure are not certified. No large external computation,
Lean build, full-repository structural validator, or workflow was run.
