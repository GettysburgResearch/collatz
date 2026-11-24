# Coordinating review of the freshness deductions

**Scope:** source-level reconstruction of the new deductions, plus the
separate exact compiler and arithmetic replays. This is in-session review,
not external referee acceptance or a formalization of the whole chain.

The three authors froze these mathematical notes before integration:

| Note | SHA-256 |
|---|---|
| LATEST_BAND.md | `b77f9b8ff871fb24fc18d1292ce9d59c1ce274cd308ff0b479f80b8e5032db30` |
| LATEST_PHASE.md | `15451b011eb7b022d7ef1b5532c2577ef8d9966615053fc2e5e4f4a7784cf7a0` |
| LATEST_CYCLE.md | `84afa56fc80558f4165c68d8ee8be5ddfcedd1f64ede6df8b12a526840151c6e` |
| GuardedPredecessor.lean | `4230db8a85e98f3d4eaa6230734d1f9a3e3c027001dc5887099fc10069dc48ab` |
| mixed_top_control.py | `81ef291acc641f79c76ee1a6c63624c19ed1dc0b5bc4b05aa7d9503dd4462a6e` |

## Marked fibers: VERIFIED written implication

The band is capped at the top of its actual binary octave. Every even
member therefore has positive odd part strictly below the entire band;
binary ancestor preservation gives a marked witness. An accepted odd
member has a positive half partner, again below the entire octave, whose
odd part is marked. It is not necessary for that accepted member itself
to be smaller than the marked source under induction. Both sources have
the same convergence status by actual common endpoints and determinism.

After such fibers are discarded, every nonminimal member reduces to the
smaller marked minimum in its own fiber. Thus strong induction over marks
is sound. The unconditional forced-section visit supplies the all-source
implication; it never assumes the first visited mark is smaller than the
original ordinary source. The return script is bounded and the common
clock is explicitly `(d+2)^3`, so membership is decidable without deciding
the full inductive acceptance language or knowing the unspecified
analytic clock constant.

The PR193 image count is used at a common *odd* clock. Later clocks can
only coarsen the image set. With band length comparable to `2^d/d`, its
critical count becomes `O(2^(theta*d)/d^(theta+1/2))`. Summing the
contribution weighted by `2^(-theta*d)` proves the endpoint summability
because `theta>1/2`. This does not forbid even one nonconvergent retained
minimum. The translated counting theorem remains a written input.

The five-step guard is a literal reverse odd run followed by a halving.
The general identity and size saving are covered by the new compiled
source. The strengthened least-nonconverger inequality still requires a
guarded visit at a sufficiently low height to give a contradiction. The
CRT construction retains the linear-horizon half-partner obstruction
while admitting this different predecessor; these statements are
compatible. The predecessor need not itself lie in the marked section.

## Mixed top factor: VERIFIED written implication

For the new seed, the five odd positions per eight-bit cell give exactly
the coefficient rows `1, 2(1+I), 8, 16(1+J), 64`. Each coset grid has zero
sum at every primitive projected root. Their simultaneous least period
is `g`; a repeat count must divide both clocks, forcing a whole-cell
translation. This proves seed primitivity and full top-factor absorption.

The chosen upper approximants remain above `log_2(3)` after reduction.
Their denominator stays divisible by five and their numerator coprime
to five. The columns `(a0,b0)` and `(c,d)` have determinant minus one,
so combining them with coordinates `(t,5)` preserves coprimality. The
error is `(t+5d/b0)*delta0+5/b0`, positive, tending to zero and greater
than `5/b=1/n`. This lower bound is essential for the quantitative
denominator estimate and avoids invoking the external two-log theorem
for this particular constructed family.

The lift's mismatch set under an n-shift lies in one nonempty terminal
column. Any period preserves that set and hence is a multiple of n;
seed primitivity then gives full period. The complete carry grouping
includes the last prefix contribution. The substitution maps every root
of the new monic top factor to a seed top root, giving polynomial
divisibility over the integers and full divisibility after evaluation.

Positive odd cyclic carries over the odd, 3-free full denominator realize
the literal rational gap cycle. The complete product controls every odd
phase from below, and every intervening even phase is at least its next
odd phase. The arbitrary-defect denominator bound sees `5g` distinct
boundaries, `n-1` common odd bits, `3g` defect zeros and `5g` defect ones.
Together with the error lower bound it gives `d >= c_g 2^n/n` for a
positive constant depending only on g. These are nonintegral rational
cycles, not positive integer counterexamples. The exact fixture is
separate finite evidence, not a proof of the unbounded construction.

## Cyclic entropy: VERIFIED written implication under the pinned partition estimate

For uniform cyclic starts, every carry position has the same mean,
including the terminal one. Thus no end-of-window clipping term is
discarded. The cycle telescope gives `2 mean(c)=A/k-mean(b)`. With the
chosen partition parameters, `-log x=2 log lambda`, so canonical-clock
terms cancel exactly. The half-bit clock estimate controls the remaining
correction uniformly for `1<=m<=k`. The endpoint law stays uniform on
the cycle. The complete affine identity makes its residue a function
of the physical gap word, justifying the entropy and collision direction.

When the modulus exceeds the cycle maximum, all k endpoint residues are
distinct; this yields the height lower bound. The case where that modulus
requires more than k odd steps is handled by the already exponential
height, not by applying a window estimate beyond its range. Fixed
canonical phase means at most L cyclic canonical words per length. The
occupation-based reciprocal tail estimate sums actual invariant-set
shells; it is not an assertion about a branching predecessor basin.

No reviewed source supplies an opposing height bound, an upper bound on
the same actual collision statistic, or a theorem eliminating every
remaining band fiber. Those are still mathematical obligations.
