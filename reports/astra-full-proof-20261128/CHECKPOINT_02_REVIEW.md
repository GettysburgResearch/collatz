# Independent coordinator review: second research checkpoint

28 November 2026. The three-hour attempt remains active. No full proof is
claimed. This review concerns the exact committed files named below; later
edits need their own review.

## Scope and reconstruction

The coordinator reconstructed the signed record-flux formula in
`mass/RECORD_FLUX.md`: a first hit of 1 at odd date h with cumulative exponent
A_h, after an accepted prefix, dies at exactly `8h - 4A_h + 1`. Reverse debt
records are precisely the same forward acceptance condition. The omitted
pre-hit deaths have distinct departing states, and the correction product,
principal-source census, and summable births give the stated exponentially
small error. This does not evaluate the remaining normalization. A constant
permanent mass remains compatible with the proved error estimate.

The new rooted-rotation argument retains actual integral inverse paths at 1.
For two putative cuts AB and BA, integrality forces the intermediate sources
above `2 * 3^length` of the opposite block, contradicting the low total gap
sum. The periodic rational completion's denominator bound is also a direct
consequence of `D = 2^s - 3^h m`; it does not assert that the terminating path
is itself a cycle.

The concentration and pair-floor notes use actual positive controls. A first
permanently safe entry is reached through a strict negative-debt cone; the
first such entry is obtained at the earliest global minimum of the actual
forward debt. The geometric cone estimate is elementary. Its quantitative
height tail additionally uses Weaver's written first-landing theorem, which
was not formally rebuilt here. The roots 5 and 85 both feed 1, are mutually
incomparable as targets, and have positive-density predecessor sets under the
qualified outside input. Their fixed-gap joint predecessor density is zero
by finite-clock coalescence. Thus two separate positive-density roots do not
supply the desired paired lower bound.

The exact pole identity in `parity/POSITIVE_SAMPLING.md` was independently
reconstructed, including the forcing term on the two non-odd-inverse trits.
The pole series is an exact positive resolvent. On the ordinary diagonal,
large valuation selects precisely the true positive inverse graph. The
unweighted pointwise Green sum is finite even on a hypothetical escaping
component, by uniqueness of arrival to a nonperiodic target. For a periodic
target the geometric lap multiplier is strictly below one. The global tilted
sum is a stronger proposed condition, not a consequence of Haar contraction
or of pointwise finiteness.

For `descent/UPPER_CERTIFICATE_SHADOW.md`, the coordinator checked the exact
denominator release, the positive-source identities through the available
binary precision, and the two exhaustive positive-shadow cases. The cutoff
is row-dependent and may use the positive shadow's own stopping certificate.
For a negative release `-A` at remaining precision m, padding the upper cycle
gives `m' = m + 1 - v2(A)` and the displayed positive A'. Writing
`B = 2^m - A` yields exactly
`B' = (3 * (B / 2^v2(B)) + 1) / 2`.
Consequently padding advances the original lower trajectory; it does not
create a new merger theorem. The eventual negative-chart argument for a bad
source retains its physical floor and covers cycles as well as escape.

The norm consumers in `descent/BOUNDARY_NORM.md` retain all coefficients of
the analytic function when applying Paley or McGehee–Pigno–Smith. No bounded
Fourier projection onto an arbitrarily selected support is assumed. The
dyadic summability consumer additionally needs the named existence-of-density
and positive-predecessor inputs. Its analytic upper estimate is still open.

## Checks actually performed by the coordinator

`replay_core.py` freshly rebuilt `ParityTail`, `ClosureConsumer`, and
`ExternalClaimChecks` into an empty temporary module directory, with warnings
treated as errors. Lean 4.34.1 and Mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612` were used. All nine printed theorem
roots use only the standard axioms, or fewer. Source and object hashes and
literal axiom outputs are in [CORE_LEAN.json](CORE_LEAN.json). The closure
consumer has explicit density and upper-tail arguments; the upper-tail
argument remains unproved. This replay did not rebuild the external projects.

The coordinator independently reran these exact checkers successfully:

- `descent/check_upper_shadow.py`: 417 canonical sources, the stated padded
  releases, and the three full-height parameter examples printed by the
  checker. This checks the identities on the stated examples; the all-row
  theorem is a written proof.
- `parity/check_sampling.py`: 24,528 exact pole/target cases checking transport,
  the integer diagonal and positive weights. Pointwise and global infinite
  claims remain subject to the proofs and scope above.

Agent-provided local Lean and finite replay receipts remain attributed to
their own files. No statement in this review silently promotes a written
analytic result to a formal theorem.

## Concurrent work boundary

PR 217 at `a2d3f9c44c798c1956d29f88d12ccb2904cb0eb4` and PR 219 at
`d49aee2567464a6408be22f2475108ee86af35bc` were inspected during the pass.
They are separate concurrent efforts. Their semiprime sufficiency, affine
branch spectrum, and approximate-color results are not claimed as work of
this packet. The latter two are consistent with the need for actual positive
integer and late-trajectory information isolated here.

## Remaining full-proof steps

The signed positive-interval parity estimate, the ordinary record-mass
normalization, and an actual merger/descent from the negative upper-certificate
chart remain open. Each would require a new estimate or construction beyond
the checks in this checkpoint.
