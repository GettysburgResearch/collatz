# Independent reconstruction: infinite-dictionary lattice descent

Reviewer: `global_candidate_attack`, 23 November 2026. The reviewer did
not develop the cycle lane. **Verdict: VERIFIED in the stated conditional
ordinary-language scope.** This is an internal independent reconstruction,
not external referee acceptance or a full Collatz proof.

## Exact reviewed sources

All paths below are in
`research/lean-exact-witness-global-20261121/repo-synthesis-20261123/cycles/`.

| File | SHA256 |
|---|---|
| `INFINITE_DICTIONARY_DESCENT.md` | `40f359ad13850a995ed798bd5c6ae8b3bf2257c9f62991d7a004c8441afa597d` |
| `LatticeDescent.lean` | `92b4d94ec3d69259fe9604097548b673693bd577ea20faf76c5c8df342b00339` |
| `check_lattice_descent.py` | `be61f95feb6b167d119868a961a3c07c24f9e3939e4486a19b0286c55ff3a5d7` |

The complete note, complete Lean module, and complete checker were read.
The author execution receipt was inspected separately. The conclusions
below apply to these exact source bytes only.

## Mathematical reconstruction

For the fixed contracting word, write `d=Q-P`, `z=dx-C`. Subtracting
the fixed-point relation from its literal affine edge gives `Qz'=Pz`.
After `k` actual copies, `Q^k z_v=P^k z_x`. Coprimality of the complete
binary denominator and ternary multiplier implies `Q^k|z_x` even when
the displacement is negative. This uses every intermediate integer;
it would not follow for a rational periodic realizer.

The defect calculation was reconstructed independently:

`S Q^k z_y = R P^k z_x + Q^k E`,

where `E=dB-(S-R)C`. This sign and the occurrence of the full defect
carry are correct. The next boundary also begins at least `K` actual
copies, so both displacements are divisible by the same `D=Q^K`.
After writing `z_x=Dh` and `z_y=Dh'`, the normalized equation is

`b h' = a h + e`, with

`a=R P^k D`, `b=S Q^k D`, and `e=Q^k E`.

For every independent `k>=K`, the monotonicity
`P^k Q^K <= P^K Q^k` multiplies the one-cutoff certificate into
`a+|e|<b`. For a nonzero integer `h`, its magnitude is at least one,
so `b|h'| <= (a+|e|)|h| < b|h|`. Thus `|h'|<=|h|-1`.
For `h=0`, integrality and `|e|<b` force `h'=0`. Induction gives the
explicit bound `|h_j|<=max(|h_0|-j,0)` and eventual zero. Substituting
zero on both sides forces each later defect's `E` to vanish.

No finite bound on the number of macroblocks, defect labels, defect
lengths, or repetition exponents enters this argument. The required
condition is the same displayed cutoff for every defect actually used.
The cutoff is not deduced from arbitrary word complexity.

The finite-prefix qualification is essential and correctly retained:
the last target needs its own lattice divisibility, supplied by a next
run or a separate finite certificate. The author control starting at 1,
taking two `10` copies and the defect `1`, reaches 2 and correctly
exhibits failure of that missing final lattice.

## Written corollaries and examples

The uniform normalized-bound specialization follows by dividing the
cutoff by `S Q^K`. For a finite defect family, `P/Q<1` and `Q>1`
make both error terms tend to zero, giving an effective integer search
for K. Infinite families need the stated uniform multiplier and error
bounds. Their existence is not assumed for arbitrary itineraries.

For `u=100` and defect `1`, the complete data give `d=5`, `E=6`,
and `3*3+6<2*8`. Its center is 1/5, so an all-time positive ordinary
path in the stated language would force an impossible integer boundary.
Finite compatible prefixes are not ruled out. The rational control
`11/7` really has period `1001`; its normalized displacement is 6/7.
It satisfies the affine contraction equation but cannot supply the
integer descent. This correctly tests the central ordinary hypothesis.

For `u=10` and every defect of length at most B, the upper real bound
`F_t(1)<=2(3/2)^B-1` is valid for both branches and the empty word.
For B>=1, it gives `|E|/S<=2(3/2)^B-2`. At K=2B the asserted bound
is `(27/32)^B+2(3/32)^B-2(1/16)^B`. Its B=1 value is 29/32;
for B>=2, discarding the negative term gives at most 747/1024.
Thus the explicit whole-language conclusion and divisor `16^B` are
correct. These real estimates are written deductions, not additional
formal declarations.

A periodic sequence of macroblocks can be repeated to an all-time path.
Eventual zero plus periodicity forces zero at every boundary, proving
the stated cycle consequence. If its center is a positive integer,
the actual trace of the fixed word supplies a genuine cycle. The note
correctly does not identify an arbitrary such cycle with the standard
one; the special `u=10` example does identify its center with 1.

## Lean scope and actual reviewer execution

The final `ordinary_word_language_hit` wrapper consumes literal positive
shortcut traces, with each input parity and every intermediate endpoint.
It obtains its affine data through `word_affine`, its complete coprimality
through `word_coprime`, and its repeated block through
`word_repeat_affine`. Thus its normalization is tied to actual ordinary
words, not an unconstrained affine premise or an omitted realization
assumption. The displayed all-defect cutoff remains an explicit hypothesis.

The reviewer freshly executed:

```sh
/workspace/scratch/c6766c1207a3/collatz_work/nov23_runtime/lean-4.34.1-linux/bin/lean \
  -j 1 -DwarningAsError=true \
  research/lean-exact-witness-global-20261121/repo-synthesis-20261123/cycles/LatticeDescent.lean
```

It exited zero. All 20 printed declarations have axiom sets contained
in `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or
custom research axiom appeared. The exact returned output is retained
in `INFINITE_DICTIONARY_REVIEW_EXECUTION.json`.

The reviewer did not rerun the author Python controls or a historical
census: the complete checker was inspected, and the central identities,
strict boundary, final-lattice qualification, and rational countercontrol
were reconstructed directly. The author's normal/optimized receipt
remains distinct evidence.

## Remaining boundary

The theorem eliminates escape and nonconstant cycle boundaries inside
the certified infinite language. A proof that every unresolved ordinary
orbit has such a full tail is absent. The reviewer found no defect in
the scoped theorem and no implication that removes this coverage premise.
