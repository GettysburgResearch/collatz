# Independent cycle-lane review: finite ordinary phase concentration

Date: 2026-11-23. Reviewer: cycle research lane.

**Verdict: VERIFIED in the stated finite ordinary-orbit scope.** The
construction, source-height payment, local product laws and phase-collision
bound are consistent. They do not supply an infinite escaping source or an
upper bound for its canonical harmonic law. No mathematical correction is
requested for the pinned note or module.

## Reviewed bytes and independence

| File | SHA-256 |
|---|---|
| `research/literature-round4-20261123/ACTUAL_LAW_RIGIDITY.md` | `a57e7aef865315ef3471a25e0fee18de4d6db75cf40455a0d658912666783e08` |
| `research/literature-round4-20261123/ActualLawRigidity.lean` | `9248f4e4041d3241038fef6a64ed502b2ab203228345c3aec3e9c4e735d432b8` |
| `research/literature-round4-20261123/exact_replay.py` | `ccf0cae72418f7d8250e6cc9125a2190f100522668460e09f3e3826d97aa6791` |

The checker review covers its complete-carry helpers, periodic construction,
actual valuation replay, source bounds, phase and local-law checks, source
boxes, and missing-final-odd-bit control. It does not independently certify
the separate triadic or cycle sections of that checker. In particular the
reviewer authored the separate cycle lane and makes no independent-review
claim for that work.

The reviewer reconstructed the written argument and inspected all twelve
public Lean statements. Compilation and axiom auditing of this module are
separate parent executions. The reviewer additionally ran an independent
explicit-sum/Fraction reconstruction on three small ordinary trajectories,
described below; it did not reuse the checker's carry recurrence or its
de Bruijn generator.

## 1. Signed shadow and exact source payment

For the chronological periodic script, expanding its carry at the first
gap gives `3 b_j = Delta + 2^g_j b_(j+1)`, where
`Delta=3^d-2^A>0`. Consequently the accounting orbit is
`z_j=-b_j/Delta`; the minus sign is required and is correct.

Combining this equation with an actual edge
`3 q_j+1=2^g_j q_(j+1)` cancels the two copies of Delta and gives the
displayed telescope with the unchanged source `p=q_0`. Coprimality of
powers of two and three gives both divisibilities in (6). Positivity of
`Delta p+b_0` then pays the complete binary clock in (8). Since every
prescribed gap is positive, `a_T>=T`, so one fixed positive source cannot
follow the script indefinitely. No global cycle exclusion is needed for
this conclusion.

The phase residue is `-b_j/Delta mod 3^m`, with the same sign as the
negative rational shadow. It applies whenever `j>=m`; the sample starts
at `J=max(m,L)`, so all its endpoints have paid that precision.

## 2. CRT realization and ordinary-source cost

The modulus in (9) must be `2^(A_T+1)`. Its congruence makes the final
affine quotient odd, whereas the modulus `2^A_T` alone does not. For an
intermediate cut, split the complete carry and first cancel the odd
power of three to obtain divisibility by the prefix binary clock. After
division, the remaining nonempty carry is odd and its remaining binary
clock is positive. Reduction modulo two therefore makes the intermediate
quotient odd as well. Positivity follows from the positive source and
nonnegative prefix carries. The prescribed gaps are consequently exact
valuations.

The extra condition `p=1 mod 3` is a compatible CRT condition. Later
states are units modulo three directly from their odd recurrence. The
period of admissible sources is exactly `3*2^(A_T+1)`.

For distinct clocks i,j, the affine slopes cannot agree: that would
equate a nontrivial power of three with a power of two. Each equality of
two ordinary states excludes at most one source. There are
`T(T+1)/2` such pairs, so that many plus one admissible lifts above H
contain a good source. The first lift lies below H plus one CRT period;
the last permitted lift lies strictly below the upper bound in (11).

For a fixed script, (8) gives `log2 p>=A_T-O_v(1)` once T is large.
Equation (11) gives the stated maximum of the floor cost and
`A_T+O(log(T+1))`, up to a constant. It would be incorrect to add those
two upper bit costs; the note correctly uses their maximum.

## 3. Local product statistics and actual carry bounds

The labelled Eulerian construction supplies every length-L labelled
block exactly once. Projection of a length-ell block, for ell<=L, has
`B^(L-ell)` extensions, and mapping labels to gaps multiplies this by
the product of the corresponding label counts. This proves (13)
without a probabilistic approximation. A collapsed gap script may have
a smaller primitive period than d; using d is still valid.

Rotating at the largest proper prefix ratio gives every normalized
prefix ratio at most one. Across the cyclic boundary the additional
factor is the full ratio rho<1. For any later clock i>=f, the ratio
`R_i/R_f` is at most `1/min_(r<d) R_r`; the intervening full-period
factor is at most one. The actual correction product decreases, so the
same constant bounds `q_f/q_i`. This proves the bound for actual states,
with the affine correction retained.

The normalized complete carry is exactly one third of the sum of
those prefix ratios, giving (16). The correction-product estimate uses
the ordinary lower bound `q_i>=p` at every state. Constants may depend
on the fixed script and therefore on P and L; no uniformity in growing
L is asserted.

The choice `T=J+N+L-1` retains every forward length-L block after a
sampled state. The choice J>=L retains every backward such block, and
J>=m retains every backward m-window used in the source-box comparison.
Sampling N consecutive phases with d dividing N gives exact frequencies
regardless of the initial phase.

## 4. Collision, ordinary diagonals and cross-box terms

Every sampled phase has total weight 1/d and determines one ternary
residue. Different phases may determine the same residue, so their
coincidence can only increase collision. Counting the ordered
same-phase pairs proves (17). All sampled ordinary states are distinct,
so the ordinary diagonal is exactly 1/N.

Within one phase, the backward m-word and its two clock/carry labels
are identical. Subtracting the two complete affine equations forces
their distinct original window sources into one residue class modulo
`2^A`. Their source quotients are therefore distinct. Each phase has
N/d different source boxes, each with weight 1/N. Its sum of box
diagonal energies is `1/(dN)`, but its actual residue collision is
`1/d^2`. The ratio N/d is exact. The square of the sum of square roots
retains that mass; replacing it by the sum of energies would lose it.

For iid gaps in {1,2}, the last gap is recovered from the terminal
residue modulo three. Multiplying by its power of two, subtracting one
and dividing by three recovers the preceding endpoint modulo
`3^(m-1)`. Induction proves injectivity of the complete ternary code
on these words and the claimed iid collision `2^(-m)`. This does not
turn the actual script's finite block statistics into independence at
longer windows.

The final checker correctly allows an incidental product marginal at
depth L+1 after labels have been collapsed. Its nonproduct control uses
a longer depth h at which the number of positive-probability iid blocks
exceeds d. A periodic script has at most d observed blocks, so some
positive iid block is absent. This support argument guarantees the
tested discrepancy for the stated nondegenerate input laws.

## 5. Independent finite reconstruction

The following were reconstructed using the explicit finite sum for each
prefix carry and `Fraction` for every affine quotient. The scripts were
supplied explicitly, and their local product frequencies were checked.

| Script | L | m | N | T | A_T | Ordinary source p | Collision | Ordinary diagonal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| (1,1,2,2) | 2 | 1 | 8 | 11 | 16 | 346951 | 1/2 | 1/8 |
| (1,1,2,2) | 2 | 5 | 12 | 18 | 26 | 189483847 | 1/4 | 1/12 |
| (1,1,1,1,2,1,1,2,2) | 2 | 5 | 18 | 24 | 31 | 7705976479 | 1/9 | 1/18 |

Each reconstruction checked every actual valuation, every clock of the
signed-shadow telescope, both source bounds, forward and backward block
counts, every present sampled carry cap and downward-ratio bound, phase
residues, and source-box injection. The first control exercises phase
merging: the lower bound 1/d is strict there.

Continuing each *same* chosen integer gives its first script mismatch
at odd-step indices 11,19,25 respectively. The corresponding exact
binary valuations of `Delta p+b_0` are 17,30,33. Thus these controls
also retain the fixed-source obstruction rather than treating a new CRT
lift as a continuation of the same orbit.

## 6. Literature and the new PR180 boundary

The reviewer directly inspected Hochman's Theorem 2.7 in the linked
primary PDF and Eberhard–Varjú's recursion and Theorem 1.1 in their
linked arXiv version. The note correctly identifies the convolution
and iid-law hypotheses and the latter theorem's almost-all-moduli
qualification. The reviewer did not audit either full analytic proof.
The linked Moreno PDF was access-blocked during this review; the
self-contained Eulerian full-alphabet proof above was reconstructed
instead, so no direct re-verification of its cited Lemma 4 is claimed.

The new PR180 file was fetched directly at commit
`a436db7b85f37abafea25f42d6f34afed02a29c0`, path
`research/whole-source-20261123/COLLISION_CORE.md`, Git blob
`d94a3c4153c7d02802f50bd3a1136c71f6936dca`. Its Sections 2–7
retain the actual fixed source, time-limit extraction, strict
process-dependent collision-exponent gap, and the separate finite-block
deficit consumer. Its same-limit upper bound remains an open closing
step. This review checks that stated boundary and its comparison with
the finite examples; it is not a full independent certification of all
PR180 arguments.

The present theorem quantifies: for each fixed P,L and each requested
finite m,N,H, there exists an ordinary source. It does not quantify:
there exists one source working for every horizon. The source-payment
identity proves why that interchange is unavailable. The sampled
weights are uniform ordinary-state weights, not the harmonic weights
of a hypothetical escaping component. The note preserves these
distinctions, so its finite examples do not contradict the new
stationary-limit theorem.

## 7. Formal acceptance boundary

All twelve public statements have the advertised finite meanings.
The actual edges, shadow equations, unit condition, phase coding and
weights are explicit hypotheses where needed. The collision inequality
is valid even for signed field weights, so the nonnegative empirical
application is included. The source-height statement uses positivity
explicitly. No infinite source or canonical measure appears as an axiom.

The CRT selection, de Bruijn existence, finite avoidance counting and
asymptotic bit-cost interpretation remain written arguments, exactly
as the note says. This verdict binds the bytes above and does not
extend to changed files, a uniform collision upper bound, or a Collatz
convergence theorem.
