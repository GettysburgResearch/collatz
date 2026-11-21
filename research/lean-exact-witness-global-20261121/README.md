# Exact witnesses and the global Lean closure attack

**Status: OPEN for Collatz and for the requested residue implication.**
The results include kernel-checked equivalences for arbitrary finite witnesses,
an all-exponent branch of a global induction, an unbounded reset family, and
three new certificate kernels for directed comparisons and source-witness
descent. The current searches have not supplied a complete recursive cover.
These results do not prove the implication or Collatz.
There is no exponent bound, witness-length bound, `sorry`, or conjectural axiom
in the new Lean module. Lean 4.34.1 is used without Mathlib or other packages.

## The target and its exact formalization

Let `T(n) = n/2` for even `n`, and `T(n) = (3n+1)/2` for odd `n`.
`Basin n` means some finite iterate of this ordinary shortcut map reaches 1.

The user's set consists of positive integers satisfying

\[
3^r x+\sum_{j=0}^{r-1}3^{r-1-j}2^{A_j}=2^{A_r},
\qquad 0=A_0<A_1<\cdots<A_r.
\]

`CollatzWitness.E` formalizes this statement with an arbitrary natural number
`r` and an arbitrary function `A : Nat → Nat`, constrained only through index
`r`. The sum is expressed by the exactly equivalent recurrence

\[
C_A(0)=0,\qquad C_A(r+1)=3C_A(r)+2^{A_r}.
\]

Every increasing tuple of integers in the question has nonnegative entries,
so this use of `Nat` loses no tuples. The arbitrary extension beyond `r` is
never inspected. The empty witness has `r=0` and gives `x=1`.

## Kernel theorems in `lean/Collatz/Witness.lean`

| ID | Theorem | Exact scope |
|---|---|---|
| W1 | `witness_iff_basin` | Inductive positive-gap witnesses are exactly the odd members of the ordinary basin. |
| W2 | `witness_certificate`, `certificate_witness` | The entire exponent-gap identity is equivalent to an ordinary finite witness, in both directions. |
| W3 | `schedule_exists`, `e_iff_certificate` | Every original increasing tuple is represented by positive gaps, and every positive-gap certificate supplies such a tuple. |
| W4 | `e_iff_odd_basin` | For every natural `n`, `E n ↔ n % 2 = 1 ∧ Basin n`. |
| W5 | `original_iff_collatz` | The exact implication on residues 129, 257, and 385 modulo 512 is equivalent to convergence of every positive integer. |

W1–W4 do not use the finite reverse cover. W5 uses the imported
`collatz_iff_deep_reverse_binary` theorem of PR146 in its implication-to-Collatz
direction. It does not assume that reverse propagation is true.

The certificate-to-orbit argument cancels the coprime factor `3^r` against
`2^a`, obtaining the legal first odd step and the remaining certificate.
The converse constructs the full gap list from a finite ordinary hitting
time. `schedule_exists` then reconstructs the original tuple by induction,
including arbitrary gaps. The positivity, parity, empty-list case, and final
power-of-two factor are all handled in Lean.

For W5, `x=128k+1` has one of the three specified residues exactly when
`k % 4 ≠ 0`, and `(x+1)/2=64k+1`. Thus the witness formulation and the existing
reverse-basin criterion have identical quantifiers. In particular the output
witness may have any finite length and any finite exponents.

## Current checkpoint: directed and source-witness induction

The latest pass treats the global closing obligation directly. It develops
three sound induction systems, with separate complete-cover requirements:

- `Collatz/DirectedInduction.lean`: directed multiplication comparisons and
  convergence claims in one induction, with powers of two removed before
  evaluating the rank. Affine proof paths have explicit query directions,
  activation obligations and strict decrease guards.
- `Collatz/WitnessEnergy.lean`: a natural-valued rank for complete supplied
  witnesses. Replacing a removed peak by fewer than `C` strictly smaller
  values decreases the sum of `C^value`, even when the new witness is longer.
- `Collatz/SourceWitness.lean`: exact ordinary-prefix removal and insertion,
  including the early-hit guard; separate global closing theorems for strict
  certificate-length descent and witness-energy descent.

The source-witness kernels accept the entire supplied finite witness. They do
not require a bound on the output witness length or its exponents. Their
global conclusions still require an actual complete family of recursive
rules. That family is not asserted by the search output.

The methods, exact scope of the finite search, source pins, and current
unresolved obligations are recorded in
[`DIRECTED_WITNESS_SEARCH.md`](DIRECTED_WITNESS_SEARCH.md).

## Earlier interval-induction attempt

The new `lean/Collatz/PsiCompletion.lean` works with the entire interval below
a hypothetical least missing positive integer. Let `H(u)=2u+1`.

| ID | Theorem | Exact scope |
|---|---|---|
| P1 | `normalize_adjacent_below` | Every positive `u<n` with missing `H(u)` normalizes to an odd known source `w≤u`, still with missing `H(w)`. This covers all powers of two in `u`. |
| P2 | `adjacent_even_tail` | If `3u+1=4^(d+1)t` with odd `t`, then `Basin(H(u)) ↔ Basin(3^d t)`. |
| P3 | `adjacent_odd_tail` | If `3u+1=2·4^d t`, then `Basin(H(u)) ↔ Basin(H(3^d t))`. |
| P4 | `initial_basin_even_tail` | The entire even-exponent branch closes because `3^d t≤u<n`. |
| P5 | `least_missing_adjacent` | A least missing `n` supplies `0<u<n`, `3n=4u+1`, `Basin(u)`, and missing `H(u)`. |

P1 is needed because the source furnished by P5 may be even. After P1,
P2–P3 partition every possible positive accelerated exponent, without a
valuation cutoff or a finite residue list.

The remaining odd branch has a concrete unresolved transition. At `d=0`,
the next source is the shorter known witness tail `(3u+1)/2`, but it may
leave the initial interval. At `d>0`, the next adjacent source is `3^d t`,
while the known witness is for `t`. Minimality alone does not transfer it
through multiplication by `3^d` once the value is outside that interval.
Neither the source value nor its witness length has been proved to decrease
across all these transitions. The following quantified family tests this
specific proposed completion.

### An unbounded reset from complete two-letter witnesses

`lean/Collatz/ResetFamily.lean` proves the following for **every** natural `j`.
Set

\[
b=12j+10,\qquad
u=\frac{2^{b+3}-11}{9},\qquad
n=2u+1,\qquad
m=2^b-1,\qquad
z=3\frac{3^b-1}{8}.
\]

The kernel theorem `CollatzResetFamily.reset_family` establishes

\[
\operatorname{Certificate}(u,[3,b]),\qquad
u<m<n,\qquad
\operatorname{Basin}(n)\iff\operatorname{Basin}(z),\qquad
2^j n<z.
\]

| ID | Theorem | Exact scope |
|---|---|---|
| R1 | `source_certificate` | The source has the complete two-letter certificate `[3,12j+10]`, for every `j`. |
| R2 | `target_reset_component` | The displayed target and reset are in the same ordinary basin component. |
| R3 | `reset_amplification` | The reset exceeds `2^j` times the target. |
| R4 | `reset_family` | Bundles R1–R3 with the strict intermediate inequalities. |

The component equivalence passes through `2^(b+1)-1` and
`3^(b+1)-1=2(4z+1)`. The growth bound is proved by induction from
`8·2^(13j+10)<3^(12j+10)`. There is no target-orbit search in this proof.

At `j=0`, the exact values are `u=909`, `m=1023`, `n=1819`, and `z=22143`.
Those values illustrate the universal theorem, rather than supply its evidence.

This disproves a uniform linear size bound for **this displayed reset**.
It does not prove that a target diverges, that no other certificate conversion
works, or that no later ordinary descendant is smaller. The equivalence is a
component equivalence; it is not claimed that `z` itself is a forward iterate
of `n`.

The imported exact closing statement is

\[
\forall k\ge0,\quad 4\nmid k,\quad
\operatorname{Basin}(81k+2)\Longrightarrow
\operatorname{Basin}(27k+1).
\]

This is `CollatzClosure.OpenLemma`, not a theorem in this packet. The ongoing
attack uses a least missing positive integer and the fact that every smaller
positive integer is already in the basin. In parallel, the interval route
tries to prove a strict survivor-count decrease at every scale. No universal
closing bound has been established in this checkpoint.

The first unsupported inference remains the displayed universal implication.
The new equivalences preserve its full strength; they do not discharge it.
The parallel interval/moment attempts did not yield a universal survivor bound,
a bound preventing endpoint mass from escaping, or exclusion of nontrivial
positive cycles. None is inserted as an assumption into W1–W5, P1–P5, or R1–R4.

## Source pins and reuse boundary

The following foundation files are copied without theorem-source edits from
[PR174 at `7034109ed60a26bc49824e1ed43c239ceca81194`](https://github.com/GettysburgResearch/collatz/tree/7034109ed60a26bc49824e1ed43c239ceca81194/research/psi-closure-20261121/lean):

- `Collatz/ReverseBasin146.lean`;
- `Collatz/Closure.lean`;
- `Collatz/Shadow.lean`.

`ReverseBasin146.lean` itself documents its source:
[PR146 at `e238c63a5d57f96bb063b7472498d1977df51951`, `research/upper-bit-mergers/ReverseBasin.lean`](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/ReverseBasin.lean).
Its only adaptation is the already-published core-only shim from PR174.
These reused results are attributed rather than presented as new work.

The global interval route was read at
[PR173 `a09eb47197cd99f218b3fa013c681df65ea0f69a`](https://github.com/GettysburgResearch/collatz/tree/a09eb47197cd99f218b3fa013c681df65ea0f69a/research/lean-shell-cover).
It supplies no hidden assumption to W1–W5.

## Reproduce

From this directory, using the pinned toolchain:

```sh
cd lean
lake build
lake env lean Audit.lean
```

`Audit.lean` prints the exact top-level statements, their axiom dependencies,
and the still-open proposition. Standard Lean logical axioms are distinct
from a conjectural axiom or `sorryAx`; the latter are not used.

The repository integrity/regression gate is run separately in a complete
clean checkout. Its process receipts belong in `reports/`, not among these
mathematical claims.
