# Eighth checkpoint: ternary pasts, source entropy and a named cycle threshold

**Collatz remains open.** This checkpoint adds an unconditional structural theorem for binary predecessor histories, a written entropy consequence with specified analytic inputs, and a verified finite certificate for the least-disagreement cycle branch.

## An arithmetic restriction on every ordinary binary cycle

Let `B` be the union of the odd phases of all positive ordinary cycles whose odd-step division exponents are one or two. The new Lean proof shows that `B` contains no nonconstant three-term arithmetic progression. It proves the stronger finite statement: if three integer endpoints in arithmetic progression each admit `n` binary odd predecessors, their common spacing is divisible by `3^n`. The predecessor witnesses can be signed integers and need not belong to one component.

The associated written argument identifies a ternary residue tree with at most two children at every prefix. For every finite `A` in this set,

\[
E(A)\le |A|^{\log_2 6},\qquad
|A+A|\ge |A|^{4-\log_2 6}.
\]

The proof uses the exact first-trit energy split and Kane–Tao's scalar inequality. It applies to arbitrary subsets and has no height-dependent logarithmic loss. Its sharpness statement concerns the larger class of abstract two-child ternary trees. An explicit recurrence also bounds the number of such phases in any arithmetic progression, at any nonzero spacing.

For ordinary binary cycles of any fixed physical max/min ratio, four actual source segments and an entropy-bin argument give a lower bound on the native word entropy. With the separately quoted input `mu(log_2 3) <= 3`, this exceeds `3/5` bits per odd edge. A cycle language avoiding `222` has entropy below `43/72` at the required composition. Hence every sufficiently large such cycle must have a positive density of three consecutive exponent-two descents, and a positive density of their run starts lie at `257 mod 384`. The entropy and analytic source-transfer argument is written mathematics, not a new fully formalized cycle exclusion.

[Full statements and proofs](arithmetic/TERNARY_PAST_ENTROPY.md) · [Lean progression theorem](arithmetic/TernaryPast.lean) · [Exact finite controls](arithmetic/TERNARY_PAST_CONTROLS.json)

## A concrete improvement above ratio four

On the bounded least-tripling-disagreement branch, let `s` be the least bad integer and `p` the fundamental odd period. Put

\[
C=4\cdot2^{1/700}>4.0039.
\]

If the fraction of odd phases above `Cs` tends to zero along unbounded periods, the written source count gives

\[
\limsup\frac{\log p}{\log s}\le\frac{99999}{300000}<\frac13.
\]

The count uses fixed-place Subspace-Theorem separation. With the quoted irrationality exponent at most three, it forces a positive fraction of phases above this explicit `Cs`. The onset and proportion are ineffective. The whole branch still has ceiling `(16s+7)/3`; its exclusion is open.

The finite certificate includes genuine third-grade choices and their nonzero signed carries. At each return to the phase interval of length `1/700`, Fourier–Hölder bounds the count at the actual incoming residue by zero-residue self-energies. The three return lengths are 665, 971 and 1636. Literal endpoint quadruples and the 1209-state rival automaton give a strict contraction below `97/100` after dividing by `3^r`. Three independently enumerated short schedules test the nonzero-carry case. The C++ transfer uses upward integer rounding and retains overflow checks.

[Carry proof and source conditions](arithmetic/ANCHOR_CARRIES.md) · [Exact replay](arithmetic/check_anchor_carries.py) · [Retained control](arithmetic/ANCHOR_CARRY_CONTROLS.json)

## Verification and comparison

The root reconstructed both arguments, checked Kane–Tao's primary statement, and replayed the new Lean module and both complete controls. There are **three new printed Lean audits**, all using only standard axioms, and **two deterministic controls**, each reproduced in normal and optimized Python. Existing rival-transfer dependencies are hashed in the receipt.

PR #200 at `df2f17a117bea06bb34040a5a97e7dc9711d9871` separately supplies a certified fifth absolute moment and its third-grade extension. The root read its actual one-variable source reduction and the extension. This checkpoint does not confuse that paper's global real-discrepancy hypothesis with a physical max/min ratio, and does not claim to have rebuilt its fifth-moment grid. The two new packets identify their respective scope and antecedents.

[Root review](../../reports/six-hour-20261127/ROOT_EIGHTH_REVIEW.md) · [Replay driver](../../reports/six-hour-20261127/replay_eighth.py) · [Receipt](../../reports/six-hour-20261127/EIGHTH_REPLAY.json) · [Manifest](../../reports/six-hour-20261127/EIGHTH_CHECKPOINT_MANIFEST.json)
