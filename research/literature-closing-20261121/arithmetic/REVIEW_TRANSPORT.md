# Independent arithmetic review of the return-transport derivation

**Verdict: VERIFIED as written for T3–T13 and the stated sharpness example.**
This is a mathematical reconstruction of the displayed arguments, not a
global Collatz proof or a claim that the missing domination premise holds.

Reviewed file: `../transport/RETURN_TRANSPORT.md`.

Reviewed content SHA-256 after the one wording correction below:

```text
8cf29ebc9f40d74265de8504290c785a490fec9b48ef87b6a7f657b7aecc9b05
```

The file was an uncommitted proposed source in the common research packet at
the time of review. The base checkout was PR 183 at
`8659cf62ac685540cadeef320e596c852fbb0959`. A later content hash is outside
this exact review boundary unless its changes are separately checked.

## Reconstructed calculations

- **T3:** the complete odd inverse fan has exponents in one parity class.
  For an odd target congruent to two modulo three, the minimum target is five,
  and `(2y−1)/3≥3y/5` is valid exactly from that bound. Summing the fourth
  inverse powers gives the displayed factor below eight. The target one is
  included in the other class. The passage from `U` to `R` is valid because
  all intervening even states are unmarked.
- **T4–T6:** splitting original sources into even and odd gives precisely
  `rho=(16/15)(mu_D+sigma)`. Applying the killed operator preserves the
  residual and gives the factor eight, not an unproved density ratio. The
  disjoint interval integration over odd sources above `2^70` gives
  `1/[6(2^70−1)^3]`; multiplication by `16/15` gives `8/45` in T6.
- **T7–T10:** the retained original atom has the same positive weight at
  every surviving endpoint. Distinctness permits each reference atom to be
  charged once. Each dyadic time block contains at least half a block of
  endpoints with logarithmic cost at least its block index. Using the
  nondecreasing envelope at `2^(k+1)` gives T8 with the stated indexing and
  constant. The `j log^5 j` upper envelope makes the resulting series dominate
  the harmonic series. The finite marked count used in T10 is present in the
  pinned `ForwardSection.lean` as `marked_count_bound`.
- **Manufactured reference:** comparison of `c_j/c_(j+k)`, with
  `c_j=1/[(j+1)log^2(j+2)]`, proves T11. The original atom is still retained
  because `alpha≥c_0 rho`. Finiteness of total mass supplies no fourth
  logarithmic moment, and the packet correctly leaves T12 unbounded.
- **Exponential absorption of the residual:** the shifted geometric series
  gives `Q beta≤8 beta`, and its added mass is at most `||epsilon||/7`.
  This does not give the critical growth envelope.
- **Sharpness example:** for the shift and
  `lambda(n)=1/[n log^p(n+1)]`, the fourth logarithmic moment is finite when
  `p>5`. The displayed density ratio has the required `j log^p j` envelope.
  This is correctly labeled an abstract example, not an ordinary Collatz
  trajectory.
- **T13:** the source weight identity is exact with the positive denominator
  `m−B_w=A_w n`. A coefficient saving alone cancels against this denominator.

## Correction and scope

The phrase that replacing an envelope by its running maximum did so
“without weakening an upper bound” was imprecise. The replacement preserves
the validity of the domination inequality while it can increase its
numerical right side. The author corrected that wording before the hash
above was recorded. The stated monotone target envelope still bounds the
running maximum, so no mathematical conclusion changes.

This review does not establish an actual bound on the transport constants,
uniform control of the additive residual relative to the reference law,
finiteness of T12, or exclusion of a persistent nontrivial cycle. It also does
not verify any external theorem merely because the transport note discusses
it; the review above concerns the displayed elementary derivations.
