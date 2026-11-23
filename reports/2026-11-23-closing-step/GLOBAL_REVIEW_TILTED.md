# Independent review of the tilted carry-moment obstruction

Date: 2026-11-23. Reviewer: `global_construction`.

**Verdict: VERIFIED as a written counterexample to the stated abstract
moment upgrade. No source changes requested.**

Reviewed file:
`research/closing-step-20261123/TILTED_MOMENT_OBSTRUCTION.md`.

Frozen SHA256:
`e6219d59418a7796854ff86513bd686025ea2d639cb24c1fa9aea872194a8f96`.

I independently reconstructed the following steps.

1. The distribution `P(R=r)=4/[r(r+1)(r+2)]` has tail
   `P(R>=r)=2/[r(r+1)]` and mean `2`. The suspension of the two-sided iid
   process under the integrable roof `2R` has the stated probability
   measure with normalizing factor `1/4`. Telescoping the within-fiber
   sum proves invariance. A set invariant under the one-step suspension
   transformation is constant along each entire fiber and induces an
   invariant set for the iid base shift, proving ergodicity. The even
   roof permits a periodic factor but does not invalidate this ergodicity
   argument.
2. The gap mean is exactly `3/2`. An all-`2` word of length `m` has
   `(R-m+1)_+` possible starting positions in a roof, giving stationary
   probability `1/(2m)`; an intervening `1` block prevents additional
   cross-roof occurrences. The all-`1` word has the same mass. Both the
   lower bound `Z_m >= 1/(2m^2)` and the use of `Z_m <= 1` in the tilted
   mass estimate retain the actual normalizing constant.
3. With the exact chronological convention in the collision note, the
   all-`2` carry is
   `sum_{i<m} 3^(m-1-i)*4^i = 4^m-3^m`. Consequently
   `K_m+1=floor((4/3)^m) >= (4/3)^m/2`. Combining this with the actual
   squared-word mass gives the stated exponential lower bound for every
   fixed positive moment exponent. The same calculation works for each
   fixed `q>1` word tilt.
4. The original mean drift is strictly negative because
   `(3/2)*log 2 < log 3`. Birkhoff's theorem therefore makes the walk
   tend to minus infinity almost surely. Its all-time maximum is finite
   almost surely, so its normalized running maximum tends to zero.
   Bounded gaps give the displayed deterministic domination. The
   logarithmic carry bound then proves the sublinear expected
   original-law logarithmic carry, with no missing integrability step.

The model is a bounded stationary ergodic process, not an asserted
ordinary Collatz orbit. The conclusion rules out deriving the required
tilted moment bound solely from the specified probabilistic properties.
It does not rule out an additional arithmetic constraint for the actual
ordinary source. Those quantifiers are stated accurately in the source.
