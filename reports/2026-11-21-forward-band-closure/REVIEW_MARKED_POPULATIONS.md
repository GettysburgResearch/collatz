# Independent review: marked predecessor populations

**Reviewer:** the independent band-return agent.
**Scope:** `agent-band-mass/MARKED_PREDECESSOR_POPULATIONS.md`, with
`LINEAR_BLOCK_ATOM_FLOOR.md` checked at the selected-density and weighted-count
interfaces invoked by the new argument. No Lean compilation was performed.

## Verdict

**No mathematical gap found in the main population theorem or its survivor
corollary, as analytic consequences of the fine-scale estimate (FM) quoted in
the parent note.** The new argument does not require conditional mixing at a
fixed total. It does not prove the missing survivor upper bound or Collatz.

This review checks the derivation from the stated analytic interface; it is
not a fresh verification of the published source of (FM), and it is not a
claim of kernel formalization.

## Checks that matter to the conclusion

1. **Every sufficiently large depth is covered.** The choice
   `d_(N+1) <= h < d_(N+2)` gives exactly
   `b_N <= k=h-d_N < b_N+b_(N+1)`. The weighted transport bound therefore
   turns (FM) into a uniform error `O(N^2/N^4)`. The additional factor
   `3^k rho^(d_N)` is bounded because `k` is linear and `d_N` quadratic.
   This fills the gaps between the parent note's triangular depths.

2. **Terminal truncation is unconditioned and its pointwise loss is bounded.**
   The difference `D_k-D_k^good` is nonnegative, and its normalized `L1`
   norm is exactly the rejected probability. The same positive prefix
   operator and weighted-count estimate bound its output uniformly by a
   quadratic factor times an exponentially small tail. No residue-conditioned
   or total-conditioned estimate is inserted here.

3. **The real offset remains uniformly bounded.** For every terminal word,
   `beta_v <= (3/2)^k-1 < 2^k`; hence
   `beta_(w*v) <= B_*+rho^(d_N)2^k <= B_*+1` eventually, uniformly over the
   allowed intermediate depths. Prepending the spreading exponent preserves
   a fixed bound, for example `B=2B_*+3`. The exponent range expands by only
   the fixed constant `E`.

4. **Spreading preserves all three required controls simultaneously.** The
   bounded exponent `1 <= e <= E=2*3^q` sends each unit residue into the
   positive cylinder. Its normalized mass multiplier is `3*2^(-e)`, so the
   lower floor is uniform in both residue and depth. The resulting family
   is still finite and simultaneously has controlled total and real offset.

5. **The phase buffer handles every word and every positive unit target.**
   The rational grid gives `2/q <= u_s <= 5/q`. The chosen actual parent
   has `Cs <= a_s <= 65Cs` after a target-dependent onset, and its
   word-dependent logarithmic correction is at most `1/(6s) <= 1/(6q)`.
   Thus no correction crosses an integer. This also works for an even
   supplied target: `3a_s+1=2^(e_s)a` places `a` at ordinary shortcut clock
   `e_s`, even though the full odd-only valuation would then be larger.

6. **Fixing the total really fixes both octave and clock.** With `A` fixed,
   the integer part in equation (5.4) is fixed and all correction terms stay
   inside its positive phase buffer. All retained sources therefore share
   one octave and ordinary clock `A+e_s`. Distinct words give distinct
   sources at this one depth, including periodic targets. The comparison
   height `H=a_s 2^A/3^s` has the same integer part by the same calculation
   with `beta=0`.

7. **The counting constant is target-independent.** Pigeonholing at most
   `2s` totals gives the stated mass `c/(2s)`. From `a_s <= 65Cs` and
   `s <= 5(d+1)`, the calculation gives exactly
   `gamma=c/(3250C)`. Both `c` and `C` are absolute; the dependence on the
   supplied target is confined to the onset and the selected octave
   subsequence. The argument does not claim uniform onset.

8. **The survivor quantifiers are in the correct order.** Each nonconvergent
   unit target supplies arbitrarily large witness octaves whose retained
   predecessor sets survive at every time. A nonconvergent positive
   component always has a positive unit target. A condition that passes
   every sufficiently large octave therefore intersects those witnesses;
   an arbitrary unbounded passing subsequence would not suffice. The
   comparison `gamma(d+1) >= 1` gives the contradiction to the strict cubic
   survivor inequality exactly as stated.

## Remaining obligation

The first unproved step toward universal convergence remains an unconditional
upper estimate for these actual section survivors, such as (7.2). Neither
the section's density-zero upper bound nor this near-linear predecessor
lower bound supplies that estimate. The manuscript states this limitation
correctly.

## Optional unit-source refinement

I also reviewed `agent-band-mass/UNIT_SOURCE_APPENDIX.md`.
**No gap found in this refinement, under the same analytic interface.**

- The extra final-letter rejection is bounded by `2^(-K_h)` before any
  conditioning. The already available prefix-operator factor is `O(h)`,
  so `K_h=ceil(4 log2(h+2))` makes the added pointwise loss tend to zero.
  Prepending the cylinder-spreading exponent leaves the final letter intact.
- Applying the refined floor to the **actual target modulo `3^(s+1)`** is
  essential and is done explicitly. The legal final inverse step implies
  that the source after its length-`s` prefix is a ternary unit. Admissibility
  merely modulo `3^s` would not justify that conclusion.
- Partitioning full words by their distinct prefixes is legitimate. For
  a fixed actual prefix source, legal final exponents have one parity, and
  their normalized multipliers sum to exactly 1 or 2. Thus the prefix mass
  is at least `c_last/2`; no multiplicity is lost without accounting for it.
- Deleting the last letter loses at most `K_(s+1)=O(log s)` in the lower
  total bound and decreases the real offset. This preserves the eventual
  height bounds and the at-most-`2s` total count. The rotation uses the
  retained prefix depth `s`, so there is no extra phase shift from the
  auxiliary additional inverse step.
- Replacing the main floor `c` by `c_last/2` yields the stated absolute
  constant `gamma_unit=c_last/(6500C)`. The final sources are distinct,
  odd, units, in the same octave, and at one ordinary clock.

The appendix deliberately states the selection's dependence on the next
ternary digit of the actual target. That qualification is necessary and
prevents an otherwise invalid residue-only formulation.
