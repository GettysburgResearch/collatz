# Independent reconstruction of adaptive ordinary lattice descent

23 November 2026. **VERIFIED at the stated written and finite-consumer
scope.** The reviewer is the separate integer-repair lane, not the author
of the adaptive lattice packet. This is internal proof reconstruction,
not external referee acceptance.

## Exact sources

- `research/lean-exact-witness-global-20261121/profound-step-20261123/arithmetic/ADAPTIVE_LATTICE_DESCENT.md`
  — SHA256 `c03c84c3288ea50eda3b2fa48d29734276eaf4ace59e286393b8af98fd7f09d4`.
- `research/lean-exact-witness-global-20261121/profound-step-20261123/arithmetic/AdaptiveLattice.lean`
  — SHA256 `fbfada80040f436a0cae32c3c9c7baf57c2280aa6fa8d0acd49e3627b4c33885`.
- The imported `WordTrace`, `WordRepeat`, `word_affine`, and
  `word_repeat_affine` interfaces in the unchanged prior
  `repo-synthesis-20261123/cycles/LatticeDescent.lean` were read directly.
  They retain the ordinary positive endpoints and every literal parity
  condition. Its archived source hash is
  `92b4d94ec3d69259fe9604097548b673693bd577ea20faf76c5c8df342b00339`.

## Reconstructed arithmetic

For a repeated base word, the exact identity is
`Q^k(dv-C)=P^k(dx-C)`. Since `P` and `Q` are coprime, the source
displacement `z=dx-C` belongs to the lattice `Q^k Z`. Composing the
literal defect gives

`S Q^k z' = R P^k z + Q^k E`,
with the complete carry `E=dB-(S-R)C`. No sign of `d=Q-P` was used in
this identity or in the magnitude argument.

When `z != 0`, its lattice gives `|z|>=Q^k`. Therefore

`S Q^k |z'| <= (R P^k + |E|)|z| < S Q^k |z|`.

The positive factor cancels and the nonnegative integer rank decreases
by at least one. The target need not belong to the next repetition
lattice for this single step. Each next source supplies its own lattice
from its own literal repetition.

The finite first-hit argument is correctly stopped at its first zero.
It uses only the first `|z_0|` macroedges under a contrary no-zero
assumption. The actual example `u=10,k=2,t=1,x=1,y=2` has source zero
and target displacement one while paying `29<32`. Thus unconditional
zero absorption would be false, and it is not claimed.

## Changing rational anchors

With positive integer `d_j` and `d_j C_j=(Q_j-P_j)c_j`, the repeated
identity becomes

`Q_j^k(d_j v-c_j)=P_j^k(d_j x-c_j)`.

This still gives the complete source lattice. Substituting the defect
and the next anchor, multiplying by `d_j d_(j+1)`, and collecting all
constant terms yields exactly

`S_j Q_j^k d_j z_(j+1)
 = R_j P_j^k d_(j+1) z_j + Q_j^k F_j`,

where

`F_j=d_(j+1)(R_j c_j+d_j B_j)-S_j d_j c_(j+1)`.

In particular neither the next denominator nor the center change has
been omitted. The hypothesis (AL14) is precisely the inequality needed
to apply the same source-lattice magnitude argument. The ranks at all
boundaries lie in one set of nonnegative integers; no new initial clock
is allocated when the anchor changes.

The example `5 --10--> 4` followed by center zero was checked directly:
the new center raises the resulting magnitude from three to four,
`F=1`, and the demanded strict budget becomes `3+1<4`, correctly false.

## Actual zero hit and all-time consequence

At a first hit, `d_j x_j=c_j`. In the written all-time application,
`d_j>=1`, the next base word is nonempty, and its repetition count is at
least one. The anchor identity then says that this next literal base
word returns `x_j` to itself. Its trace is an actual finite Collatz
cycle. If the chosen fixed point is nonpositive or nonintegral, the hit
contradicts the positive integer boundary; if it is integral, the actual
cycle must be retained. The proof does not assume that an arbitrary
integral center is on the standard cycle.

The general Lean first-hit statements permit some degenerate inputs
because they only assert the algebraic first hit. The additional
nonempty-word, positive-denominator and positive-run conditions are
explicit in the prose periodicity application, which is not claimed as
an extra kernel-checked declaration.

## Individually unbounded defects

For `P<Q`, each fixed defect has normalized cost
`(R/S)(P/Q)^k+|E|/(S Q^k)` tending monotonically to zero. Thus its own
cutoff exists without a uniform defect dictionary. The displayed
`u=10`, `k>=2 max(1,|t|)` example also checks: its normalized upper bound
is `(27/32)^B+2(3/32)^B-2(1/16)^B`, equal to `29/32` at `B=1` and below
`747/1024` for `B>=2` after dropping the negative term.

This applies to any actual infinite word already having the stated
macro decomposition. The source does not assert that every ordinary
orbit has one. The universal selector remains the first unsupported
step, including when the bases and reduced fixed-point denominators
are allowed to vary.

## Evidence boundary

The review reconstructed the identities, inequalities, first-hit clock,
ordinary wrapper and explicit examples, and read the entire new Lean
module. It did not rerun an old census or claim an additional independent
Lean compilation. The author's and coordinating agent's actual compile
receipts are separate evidence. The review uses no external termination
theorem as a substitute for the displayed arithmetic or coverage premise.
