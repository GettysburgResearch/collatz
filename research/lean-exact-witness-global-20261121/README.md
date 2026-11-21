# Exact witnesses and the global Lean closure attack

**Status: OPEN for Collatz and for the requested residue implication.**
The new results in this first checkpoint are kernel-checked equivalences for
arbitrary finite witnesses and an all-exponent branch of a global induction.
They do not prove the implication or Collatz.
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

## Current global proof attempt

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
across all these transitions.

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
