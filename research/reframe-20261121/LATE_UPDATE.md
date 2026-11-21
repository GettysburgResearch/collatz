# Publication refresh: the new word erasure and source-preserving routes

**Full Collatz closure remains OPEN.** After freezing this packet's science
commit, a second GitHub read found PR185 and later heads of PR175, PR180,
and PR183. The team read their current bodies and the principal new notes.
The older exact source pins in the main packet are retained. PR173's imported
head remains `fa0c9e2a2851e6324391e39c17afcb5913185aec`; no formal dependency
or checked Lean source in this packet changes in this update.

This is a targeted reading and connection note. It does not independently
certify the full newer analytic derivations or inherit their earlier compiler
receipts for newly added code.

## 1. PR185 adds a physical merger in part of the complementary phase

Source: PR185 at `3a2341f4b909cb83f6c2a0eabe946d3d96fc6148`, especially
[LITERATURE_LIFTING.md](https://github.com/GettysburgResearch/collatz/blob/3a2341f4b909cb83f6c2a0eabe946d3d96fc6148/research/literature-orbit-closure-20261121/LITERATURE_LIFTING.md)
and its neighboring README. It is stacked on PR184's already inspected head.

Its exact eight-step identity is

\[
T^8(256v+184)=T^8(768v+554)=27v+20\qquad(v\ge0).
\tag{L1}
\]

The identity can be reconstructed directly. The first arm's parity word is
`00011100`, with three odd steps; the second's is `01000001`, with two odd
steps. Every displayed source coefficient is a multiple of `256`, so each
word remains valid for every natural `v`. Substitution gives the displayed
common endpoint, without a convergence assumption.

For `n=2^k*u-1`, `k>=2`, `u>0`, and

\[
3^{k-1}u=256v+185,
\]

the rising prefixes from `n` and `x=(n-1)/2` land respectively at the two
arms of `(L1)`. Hence

\[
T^{k+8}(n)=T^{k+7}(x).
\tag{L2}
\]

Our checked `marked_half_of_three_mod_four` makes `x` marked whenever
`n` is marked, and `x<n`. Thus `(L2)` supplies another genuine smaller
marked component partner. The condition `185 mod256` lies in the `1 mod4`
phase complementary to the earlier guarded rising exchange.

This is a written composition of the new source identity with this packet's
checked transport. It is not an extra theorem in the 25-statement Lean audit.
The source's progression cover remains explicitly incomplete: it reports
446 covered and 130 unresolved progressions in its 576-class refinement.
The arbitrary-multiplier pullback still requires the exact ternary divisibility
`3^p | m-1`, and power-of-two pullback can enlarge the source. These facts do
not provide an all-source terminating selector.

## 2. PR175 localizes the remaining moment to exhausted sources

Source: PR175 at `2055b8a311ab87d07bffc730154a7f8546fe382c`. The relevant
new-head surfaces are its README,
[WIDE_CLOSURE_ATTEMPT.md](https://github.com/GettysburgResearch/collatz/blob/2055b8a311ab87d07bffc730154a7f8546fe382c/research/lean-global-closure-20261121/WIDE_CLOSURE_ATTEMPT.md),
and [FULL_SOURCE_TRACE_ATTEMPT.md](https://github.com/GettysburgResearch/collatz/blob/2055b8a311ab87d07bffc730154a7f8546fe382c/research/lean-global-closure-20261121/FULL_SOURCE_TRACE_ATTEMPT.md).
Its PR body still identifies an older head and older 17-unit receipt as final;
that body does not certify the entire newer checkpoint.

The new analysis states an exponentially small difference between the
full fourth-derivative moment and its exhausted-source core,
`0<=D_q-B_q<=1/2*(3/5)^q`, and the source-localized estimate

\[
\sum_{\substack{x>0\text{ odd}\\x\ge2^{L_q(x)}}}
\frac{J_q(x)^4}{U^q(x)^2}
\le\frac32(3/5)^q.
\]

The localization uses the exact threshold
`U^q(x)>=3^q iff x>=2^(L_q(x))`. Its finite rational kernel and scaling
are reported as core-Lean checked; the population substitutions, infinite
sums, and accelerated-clock crosswalk are identified as written deductions.
The required quadratic bound on the exhausted core remains open, and every
fixed ordinary source eventually enters that core. This is relevant to the
fixed-source spectral target; it does not remove the need to control it.

The constructive additions include complete inverse continuation with ternary
carries, a maximal reserve at each source clock, an arbitrary-phase compiler
for supplied certificates, and the terminal power-of-two recursion. The
nonterminal successful selector remains incomplete. The new head does not
change the PR173 vendor source used here.

## 3. PR180 proposes a stronger ordinary predecessor-density input

Source: PR180 at `cf91e46fa9fbadba3df7942202a5197c134d0ce0`,
[JOINT_CLOCK_MIXING.md](https://github.com/GettysburgResearch/collatz/blob/cf91e46fa9fbadba3df7942202a5197c134d0ce0/research/lean-forward-band-20261121/JOINT_CLOCK_MIXING.md)
and [GLOBAL_RENEWAL_ATTACK.md](https://github.com/GettysburgResearch/collatz/blob/cf91e46fa9fbadba3df7942202a5197c134d0ce0/research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md).

The checkpoint presents a new written, non-Lean analytic derivation of
absolute constants `c,C>0` such that every positive ternary-unit target `a`
has at least `cX/a` odd ordinary predecessors below `X` whenever `X>=Ca`.
It also states a unit-source variant after changing constants. This stronger
source claim has its own recorded review; the present refresh does not add
an independent acceptance verdict on that analytic proof.

Its asserted conclusion is compatible with the marked-octave packing proved
here. The proposed sources are ordinary predecessors without a prescribed
shrinking marked octave, and their lower coefficient depends on `a` through
`1/a`. The target-independent coefficient `gamma` in our marked packing
hypothesis is different. For disjoint predecessor families the new note
retains a reciprocal restriction `c*sum_a(1/a)<=1` and leaves the actual
survivor-decay and repeated-renewal step open.

## 4. PR183 normalizes an endpoint but retains physical erasure as a premise

Source: PR183 at `cc046e189366e7e876fc283b80459e64faa9c486`, the
[new README](https://github.com/GettysburgResearch/collatz/blob/cc046e189366e7e876fc283b80459e64faa9c486/research/literature-closing-20261121/README.md)
and [CONSTRUCTIVE_NORMAL_FORM.md](https://github.com/GettysburgResearch/collatz/blob/cc046e189366e7e876fc283b80459e64faa9c486/research/literature-closing-20261121/mergers/CONSTRUCTIVE_NORMAL_FORM.md).

The mixed-base normalizer reaches an actual endpoint
`n'=3^k*(6q+1)+r`. Its erased-symbol candidate `m=3^k*(2q)+r` is smaller
than that endpoint and decreases its matrix rank. The existence of an
actual finite common endpoint for every required erasure remains the
explicit `BlockedErasureCover`. Its equivalence with `Universal` does not
establish that cover.

The candidate need not be marked, and the normal-form endpoint may exceed
the original source. Thus the normalizer alone does not meet this packet's
marked-induction hypothesis. The added renewal inequality also retains
repeated-transport and cycle obligations. At this exact head, the four new
Lean scripts are explicitly awaiting compiler replay; the earlier
43-theorem receipt does not cover them.

## Effect on the current checkpoint

The new physical identity `(L1)` supplies a concrete extra case of the
marked-merger strategy. The other updates sharpen the source-level
interfaces and the statement of the missing normal-form/renewal step.
None of the inspected updates supplies the universal successful cover,
the exhausted-core moment bound, or the ordinary sampling transfer left
open in this packet. Its full-theorem status and frozen formal dependencies
therefore remain unchanged.
