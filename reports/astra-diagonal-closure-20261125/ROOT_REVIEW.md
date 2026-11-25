# Independent root review and frozen-source intake

**Verdict:** verified finite kernels and scope-qualified written progress; universal Collatz closure remains OPEN. The pass used three GPT-6.2 Astra agents at the user's requested ultra effort, with separate transport, cycle and shared-source-grid assignments. Root reconstructed the mathematical claims, checked the relevant source domains, and owns the publication replay.

## Frozen inputs

| Source | Full head | Used boundary |
|---|---|---|
| PR192 owned branch | `07d494324c7ea440d45845d725f5cebad8a67124` | Existing actual basin definitions, least-disagreement reduction, previous source/cycle barriers |
| PR195 | `4fd8af31c1ea525252b4d8f7411b5921dd447048` | Round11 full-denominator criterion, bounded-template obstruction and diagonal trace scope |
| PR206 | `45a6a111321f947a8482c9e96e898435b57cee09` | 513-rank common windows, recurrence obligation, physical escape records |
| PR197 | `156652e03fe7a78f9cd4442039779cc622fdf3de` | Actual query program, common coarse source, finite joint-grid transfer |
| PR146 | `f431078244e868dc699fad011044f0d5e7f76437` | Prior fixed-suffix merger scope; not needed for the new explicit 81 cylinders |
| PR205 | `32d722c5d5597846da5dad842c8ea15742abc176` | Bounded least-disagreement cycle, exact normalization and height strip |

Intake corrected one stale shorthand immediately: PR205 uses `n=3q` and `s=(3q-1)/2`. All work in this packet uses that normalization. The fresh PR206 common windows do not prescribe the location of the first bad tower rank. PR195 decides divisibility for a supplied word but does not prove a failed test at every nontrivial candidate. Those missing quantifiers were not supplied by neighboring statements.

## Transport review

Root checked the actual statement of `drop_or_exact_suffix`: the first equality of odd grades is earlier than the supplied hit, has a strictly positive ordinary carry, and retains the original deterministic upper suffix. Its cost bound and `3*3^D < 2*M` guard are explicit. The accumulated-error inequality uses a floor at every intermediate lower value. Neither the existence of a later large surplus nor the first equality itself is a merger.

The canonical failure is an all-parameter ordinary identity, not a claim of badness for those examples. The one-successor criterion concerns a ternary unit and is exactly `n % 18 = 10`. The bounded bad-cycle branch has no such phase, since its even inputs are isolated and are immediately preceded by an odd input. The known longer singleton partner is compatible with this failure of a one-successor mechanism.

The joint-grid agent independently rebuilt both transport modules and reconstructed the arithmetic and finite cases. Its byte-scoped report is [JOINT_REVIEW.md](transport/JOINT_REVIEW.md).

## Cycle review

Root re-read PR205's exact strip and the ordinary least-disagreement definitions. All ancestors of a bad phase are bad, so the floor `9q <= 8z+1` and the stronger bound for multiples of three apply to competitors outside the cycle. The full-lap complementary path gives the displayed native-window distortion. This validates comparisons with competitors of arbitrary positive valuations, rather than only words in the native alphabet `{1,2}`.

For the written all-period assembly, the five-step residue count also works for periods below five by wrapping the cycle. Distinct odd points and oddness give the count modulo 486. The count at `s=729` and the smaller-source finite check supply the stated `9/8` numerical premise without an external logarithmic-form theorem. The attainment from `3q=2s+1` uses the same odd count and one extra shortcut clock after the actual initial merger.

The transport agent independently reconstructed these arguments and the ordinary progression controls: [TRANSPORT_REVIEW.md](cycle/TRANSPORT_REVIEW.md).

### A rejected finite-language closing attempt

Root independently tested the full minimum inverse-clock function on residues modulo `3^k`. The recurrence is

`F_k(y) = min_a (a + F_(k-1)((2^a y-1)/3 mod 3^(k-1)))`,

with `a>=1` and an integral first inverse; a nonterminal multiple of three is forbidden. `F_0=0`. A unit always has a unit predecessor with exponent at most four; the last inverse needs at most two. Thus `F_k<=4k-2`, while any remaining `k-1` steps cost at least `k-1`. These bounds make the C++ minimization finite and exact.

For every native `{1,2}` word through length 15, its shortcut cost equals the full inverse minimum. At length 16 exactly four words save one clock; at length 17 exactly 22 do. There is no saving of two or more in this complete range. Therefore the uniform three-clock exclusion removes **no** native words through depth 17. The experiment gives no global entropy improvement and was not promoted to a closure argument. The one-clock improvements can matter at the minimum, where the stronger test applies.

[C++ source](cycle/inverse_minimum.cpp) · [Independent check](cycle/review_inverse_minimum.py). The independent check enumerates all forward exponent compositions up to the proven cost ceiling for depths 1 through 6 and compares every residue, then reproduces the complete native-word census through 17. It runs in both Python modes during publication replay.

The quantitative motivation was explicit: a uniform cycle-source exponent below `1/3`, combined with a separately justified irrationality measure at most three for the logarithm ratio, would contradict the near-critical cycle approximation at large minima. The recent primary preprint [Chudnovsky, arXiv:2611.30820](https://arxiv.org/abs/2611.30820) supplies a stated homogeneous linear-form exponent two, corresponding to ratio exponent three, not ratio exponent two. Its Lean supplement was not rebuilt here; no new result in this packet depends on it. The attempted language reduction did not reach the needed bound.

## Joint-grid review

Root re-read the complete frozen `GRID_TRANSFER.md`, `LOCAL_RESAMPLING.md`, `SELECTED_TRIT_CELLS.md` and `LOCAL_COLOR_INFORMATION.md`. The distinction between physical source populations and their bounded-parameter enlargement is retained throughout.

The all-lifts cylinders synchronize both ordinary terminal value and weighted odd grade; asynchronous endpoint equality alone would not suffice. Every aligned odd-stride window contains the requisite `2^-14` fraction of rows. The finite gluing argument uses the same row set across the whole chain, so it does not substitute a pairwise marginal for the joint statistic.

The large-gap proof freezes one seed pair across the entire shared string. All clock probabilities use conditional fair parity for one odd-affine arm, never independence of the two arms. The eligible mantissa clocks are deterministic before the remaining bits, with a uniform irrational-rotation count and the first-period height margin. The final many-clock lower bound follows from a bounded first moment. The discarded final logarithmic microblock is accounted for.

The unrestricted-height extension steers actual common native bits, lets the scalar correction contract on a long fair continuation, and keeps one seed pair per opening. Adding a multiple of `2^tau` then realizes each completing grid residue with the same seeds. The resulting representative can have size up to `2^(tau+H-Delta_tau)`, far above the required row. It does not realize the original physical-parent population or true formal replies. The cycle agent independently audited this distinction and the constants: [CYCLE_REVIEW.md](joint/CYCLE_REVIEW.md).

Root's [ordinary cylinder control](joint/review_cylinders.py) independently iterates all 81 witnesses on small and very large positive lifts. Lean supplies the universal lift theorem. The analytic lower bounds remain written proofs.

## Publication boundary

Only this pass's new `research/astra-diagonal-closure-20261125` and `reports/astra-diagonal-closure-20261125` files are added. The fresh replay rebuilds every new module and both project dependencies. Its raw command logs, source hashes, complete-checkout validator receipt and exact publication revision are linked from [VERIFICATION.md](VERIFICATION.md). Existing research history is preserved, and the owned draft PR remains a research proposal.
