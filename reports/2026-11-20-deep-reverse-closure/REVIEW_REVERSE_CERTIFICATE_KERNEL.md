# Independent review: reverse-certificate normal form

**Verdict: VERIFIED WITH A WORDING FIX for K1--K3 and the stated open
boundary, at the exact bytes below.** This is an independent agent
reconstruction, not human referee acceptance or proof-assistant
verification. No claim of full Collatz convergence is approved.

Reviewed file:
`agent_deep_reverse/REVERSE_CERTIFICATE_KERNEL.md`.
SHA-256:
`4bf600fce574029b03e2af1b79acb9809b5efb944c5a92296ae82149d6a2da85`.

The ordinary map and all clocks were independently reconstructed from
`T(n)=n/2` for even `n`, `T(n)=(3n+1)/2` for odd `n`. The reviewer
did not import or run the author's checker. The separate program
`check_reverse_kernel_review.py` uses only literal shortcut steps and
standard-library arithmetic.

## Claim-level reconstruction

| Claim | Verdict and scope |
|---|---|
| K1 | Verified. Three odd-even pairs give `54k+1` and `27k+1`. Solving `162k+4=2^c z` yields precisely the two displayed affine reconstructions. The `c=1` congruence is `z=83 mod162`; `c>=3` has `2^(c-2)z=1 mod81`. These conditions are sufficient as well as necessary and produce positive eligible `k`. The first four upper-arm odd inputs all exceed 1, so first-hit rank is exactly `4+r(z)`. |
| K2 A | Verified. In the odd-index case, `T^6Y=(z+1)/3` is even, and its next halving gives `(z+1)/6`. |
| K2 B | Verified. Starting from `T^7Y=2^(c-2)z+1`, actual odd-even pairs reduce the binary exponent by two and multiply the odd coefficient by three. For even `c=2r+4`, the result at clock `c+6` is exactly `T(3^r z)`. This is an ordinary merger, so convergence is equivalent in both directions. |
| K2 C | Verified. For odd `c=2r+3`, the same identity gives `2*3^r z+1` at clock `c+4`. |
| K2 equivalence | Verified relative to the imported criterion (D). Every eligible `(k,c,z)` is covered and reconstructed, and every admissible kernel source gives such a `k`. The claim that (D) is equivalent to full Collatz remains source-qualified to PR146, `e238c63a5d57f96bb063b7472498d1977df51951`, `DEEP_REVERSE_BASIN.md`; this review does not reexecute that source's full affine certificate or Lean development. |
| K3 complete parameterization | Verified. Exact one-odd-input first-hit rank requires `z=(2^a-1)/3`, `a>=4` even. Substitution produces the displayed source and congruence modulo 243. Order 162 of 2 modulo 243 follows from the stated 3-adic valuation identity; the rearranged target is a unit congruent to 1 modulo 3, hence exactly one even exponent class exists. Exponent 2 is correctly removed where present. |
| K3 four rows | Verified. Residues `a=70,22,68,118 mod162` correspond respectively to `c=1,3,4,5`. Literal paths give the stated powers-of-three, power-of-two, and Mersenne endpoints. The lower arm at `c=4` has exactly five odd inputs before 1, including its two consecutive final odd inputs at clocks six and seven. |
| Claimed closing limit | Correctly OPEN. Lowering the certified tail rank does not preserve the target operation. The `z=1` instance of B already asks for all powers `3^(27j-1)`. Neither numerical decrease in A nor availability of a certificate for `z` supplies the missing certificate for the new target. |

One draft phrase required repair. The pair identity applies to every
integer binary exponent `b>=2`, not only to even `b`; the odd-valuation
case uses odd exponents. The author corrected this before the frozen
hash and executions above. The formula and clocks themselves were
unchanged.

## Execution evidence

The independent checker completed normally and with Python `-OO`,
producing byte-identical reports:

- 6,144 eligible indices from `1<=k<=8192`, split into 4,096 A,
  683 B, and 1,365 C cases.
- 188 complete rank-five upper certificates over 63 fourth gaps,
  using up to three representatives of each permitted last-gap class.
- 16 complete checkpoints for the four displayed infinite families.
- Five negative controls: four ineligible indices and a corrupted
  supplied odd-gap word.

The finite evidence checks the displayed identities at ordinary positive
inputs and supplies an independent implementation check. The all-size
quantifiers rest on the algebra and parity reconstruction above; no
finite execution establishes one of the still-open A/B/C closures.

The two reports are `reverse-kernel-review-normal.json` and
`reverse-kernel-review-optimized.json`. Their proof-hash field identifies
the exact reviewed body; this verdict does not extend to subsequent
unreviewed edits or to the rest of PR146.
