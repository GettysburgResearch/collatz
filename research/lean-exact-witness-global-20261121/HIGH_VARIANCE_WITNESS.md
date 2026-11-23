# All-certificate source optimization on a finite ordinary boundary

## Result and purpose

The direct closing attempt in this continuation replaces local witness edits
by **the global optimum over every complete source witness**. For a fixed
original odd target `t = 2B+1`, that optimum is computable from a finite
ordinary Collatz graph below `B`. No artificial cap on input exponents,
witness length, or edit radius is needed.

The five public theorems in
[`lean/Collatz/FiniteSourceBoundary.lean`](lean/Collatz/FiniteSourceBoundary.lean)
prove the unrestricted last-exit reduction and exact minimum/maximum-source
interfaces. The graph algorithm and canonical-certificate interpretation
below are written proofs; they are not counted as Lean declarations.

This finite optimization does **not** prove that the original target enters
the certified graph. I attempted that final step using the graph boundary
and the joint minimum. Section 8 gives the precise remaining issue. Full
Collatz and `FloorIntervalStep` remain open.

The normalization throughout is the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

The complete supplied-source grade is unchanged:

\[
\Gamma(e;W)
=\bigl(\{2e+1\}\text{ if }e>0\bigr)
 \uplus\{2a:a\in W\}.
\]

Grades are ordered by the multiplicity at the largest changed entry. A
complete source is `S=2^e q`, where the actual positive-gap word `W` takes
the positive odd integer `q` to `1`. It captures `t=2B+1` exactly when
`S>=B`. Assume `B>2` so the terminal cycle is strictly below the floor.

## 1. Last-exit trimming uses the supplied witness

**Theorem FB1.** From any complete source certificate capturing `2B+1`,
one can retain a complete certificate for a state `S*` of its actual
ordinary orbit with

\[
\boxed{B\le S_*<2B,\qquad S_*\equiv0\pmod2,
       \qquad T^k(S_*)<B\quad(k\ge1).} \tag{FB1}
\]

The retained grade is the original grade if no clock was consumed, and
strictly smaller otherwise.

**Proof.** The supplied certificate reaches `1` at a finite clock. After
that clock every state is `1` or `2`. Hence there is a last ordinary time
at which the supplied trajectory is at least `B`; call its state `S*`.
Every subsequent state is below `B`.

An odd positive state grows under one shortcut step, so `S*` is even.
Writing `m=T(S*)` gives `S*=2m`, with `m<B`, and therefore `S*<2B`.

The existing `SourceOrbitProgress.advance_certificate` consumes the
literal supplied certificate along this same trajectory. Its endpoint is
at least `B>2`, so no terminal-cycle exception applies. A positive number
of consumed clocks strictly decreases the original complete grade. At
clock zero the supplied certificate is retained unchanged. This proves
the grade assertion as well as actual integral realization. No new
certificate is chosen for an inferred target. \(\square\)

Lean separates the ordinary statement `last_exit` from its supplied
certificate consumer `trim_certificate`. The proof handles all future
clocks, including clocks after the supplied finite hitting witness ends.
It is not a last exit only up to an arbitrary search horizon.

## 2. The exact minimum and maximum-source tie are finite-source problems

Let `Boundary_B(S)` mean exactly (FB1). No assumption that the target is
bad is part of this definition.

**Theorem FB2.** For every original source grade `G`,

\[
\begin{split}
&\text{there is a complete capturing certificate of grade }<G\\
&\quad\Longleftrightarrow\quad
\text{there is such a certificate at a source satisfying Boundary}_B.
\end{split} \tag{FB2}
\]

**Proof.** The reverse implication is immediate. For the forward
implication, apply FB1 to the smaller-grade certificate. Its retained
grade is equal to or smaller than that smaller grade. Transitivity
preserves the comparison with the original `G`. \(\square\)

This is `boundary_minimum_iff`. Consequently any globally minimum-grade
capturing source already satisfies (FB1), without a bad-target premise,
least-target induction, or bounded-gap assumption
(`minimum_on_boundary`).

At the globally minimum grade, **every** capturing source lies on the
same boundary. Otherwise FB1 would produce a strictly smaller capturing
grade. Thus the maximum numerical source at that grade can also be
chosen by searching only this boundary (`boundary_maximum_iff`).

This retains the joint selection used in
[`JOINT_MINIMAL_COUNTEREXAMPLE.md`](JOINT_MINIMAL_COUNTEREXAMPLE.md): first
the original grade minimum, then the numerical maximum at exactly that
grade. The finite restriction does not reset either selection.

## 3. A finite graph computes the entire boundary

Define

\[
R_B=\{1\le n<B:\ T^k(n)<B\text{ for all }k\ge0,
                    \ T^j(n)=1\text{ for some }j\}.
\]

It is computed exactly by starting from `1` and repeatedly adjoining all
positive ordinary predecessors that are below `B`. Those predecessors are

\[
2m,\qquad (2m-1)/3\quad\text{when }m\equiv2\pmod3.
\]

There are at most `B-1` vertices. The process terminates after each is
adjoined at most once. Distance labels recording first hitting clocks give
a readily checked certificate:

1. `1` has label zero.
2. Every other retained vertex has positive label, its literal successor
   is retained, and that successor has label one smaller.
3. Every legal predecessor below `B` of every retained vertex is retained.

The first two conditions prove soundness by finite descent of labels.
The third proves completeness by backward induction along any finite
actual hitting path that stays below `B`. Thus a verified closed graph is
the whole `R_B`, not a sample of its inverse tree.

The complete ordinary boundary is then

\[
\boxed{F_B=\{2m:m\in R_B,\ B\le2m\}.} \tag{FB3}
\]

FB1 proves that every unrestricted capturing witness is dominated by a
complete witness at one of these finitely many sources. Conversely, each
source in (FB3) has a complete actual certificate and satisfies (FB1).

The boundary is nonempty: the least power of two at least `B` lies below
`2B`, and its later ordinary orbit stays below `B` and reaches `1`.

## 4. Why one certificate per boundary source is enough

Every boundary source has a unique first-hitting ordinary trajectory to
`1`. Factor out its initial power of two; at each subsequent odd input,
the next gap is the exact valuation `v_2(3q+1)`. This gives a unique
complete **first-hit** positive-gap certificate.

Any supplied positive-gap certificate at that same source has the same
initial even exponent, since its represented odd source is odd. Its gaps
before the first occurrence of `1` are forced by the same exact valuations.
After reaching `1`, the only possible next positive-gap certificate edge
is `1 --[2]--> 1`. Thus every other complete certificate consists of the
first-hit word followed by some number of terminal gaps `2`.

Removing nonempty terminal padding strictly lowers the grade by deleting
entries `4`, while leaving the source and capture unchanged. Therefore
the global minimum is attained among the unique first-hit certificates
of the finite set `F_B`; a noncanonical padded certificate cannot attain
that minimum. The maximum-source tie is computed among precisely the
first-hit certificates with the minimum grade.

The resulting algorithm searches **all** input exponents and witness
lengths through a proved reduction. It does not assume a finite cutoff
and compare only the certificates that happen to fit it.

There are also intrinsic output bounds. If `K=|R_B|`, every first-hit
boundary trajectory has at most `K` ordinary clocks. Let
`h=ceil(log_2 B)`. Its initial even exponent is at most `h`; every odd
gap is at most `h`, because the peak `2^(a-1)u` immediately after that odd
input is below `B`. Hence every retained grade entry is at most `2h+1`.
These bounds follow from the physical boundary, not from an assumption
on the original arbitrary witness.

The supplied implementation materializes all boundary certificates, using
at most quadratically many ordinary-state operations in the numerical
floor `B`, plus integer arithmetic for their exact identities. This is
not polynomial complexity in the bit length of the target. It is a
complete finite optimization procedure, not a practical all-target
decision procedure.

## 5. Executable control on the existing difficult targets

[`finite_source_boundary.py`](finite_source_boundary.py) builds and checks
the entire graph, enumerates its boundary, checks every first-hit
certificate identity, compares the original grade multisets, and applies
the maximum-source tie. It does not simulate the target in order to
select its source.

Python's lexicographic comparison of the descending grade lists is exactly
the original multiset order: after their common prefix, the first differing
entry identifies the largest value whose multiplicities differ; a proper
prefix is the smaller grade.

| Original target | Floor `B` | Retained vertices | Complete boundary sources | Globally selected source | First-hit certificate |
|---|---:|---:|---:|---:|---|
| 2047 | 1023 | 439 | 140 | 1092 | `2^2 * 273`, gaps `[2,3,3,3,1,2,3,4]` |
| 3711 | 1855 | 751 | 243 | 2184 | `2^3 * 273`, gaps `[2,3,3,3,1,2,3,4]` |

Both minimum-grade source sets are singletons. The computation recovers
the earlier exact extremal sources without using their special
one-gap-four inverse-cluster classification and without imposing gap
four as an enumeration bound. All larger exponents and longer witnesses
are covered by FB1--FB3 and the padding argument.

These are controls of the new global optimizer. The sources and the
failure of their completion clocks to bound target descent were already
established by the pinned peer work below. They are not presented as new
target convergence results.

The script also rejects three damaged finite-graph certificates: a
missing legal predecessor, a false first-hit clock, and a vertex outside
the floor. Ordinary and optimized Python produce identical output; the
checks do not disappear under `python -O`.

Reproduction:

```sh
python -X utf8 -B finite_source_boundary.py --controls
python -O -X utf8 -B finite_source_boundary.py --controls
```

## 6. How this differs from the local carry restriction

The earlier `ContextSurgery` program proves the soundness of accepted
backward affine carries with nonnegative dyadic exponent and offset. It
does not establish their completeness. Recent attempts also show that
unbounded words over a smaller gap alphabet need not provide source
growth, and that positive source debt can consume the original interval
slack.

The present optimization imposes none of those carry restrictions. A
certificate found by any simultaneous multiwindow edit, signed affine
carry, altered odd length, changed initial even exponent, or much larger
exponent is still a complete capturing certificate. If it has a strictly
smaller original grade, FB1 reduces it to one of the finitely many
boundary competitors. Conversely every boundary competitor is physically
legal and can be checked without reconstructing a proposed edit.

This is why the finite boundary is useful for a central attack: it makes
the exhaustive source side concrete. It does not make a proposed edit
successful automatically, and it does not constrain what forms an output
certificate for the target itself may take.

## 7. Exact graph updates and the record process

The finite reduction supports a further global attack: follow the changes
of the optimum as the floor increases, rather than repair each witness
independently. The following written statements are exact at every floor;
they are not extrapolations of the two finite controls.

### Only a certified even vertex can attach a new component

Raise the floor from `B` to `B+1`. Any vertex in `R_(B+1)` not already
in `R_B` must have a first-hitting path that visits the one newly allowed
state `B`. Therefore the retained graph changes precisely when

\[
\boxed{B\text{ is even and }B/2\in R_B.} \tag{FB4}
\]

If `B` is odd and `B>=3`, its next ordinary state exceeds `B`; hence it
cannot be retained below `B+1`. If `B` is even, membership of `B/2` in
`R_B` is sufficient. It is also necessary: a first-hitting path from
`B/2` that revisited `B` would repeat the edge `B -> B/2` and could
never reach `1`. Thus its successful path must stay strictly below `B`.

When (FB4) holds, let `A_B` be the entire set of states in `[1,B]`
whose forward path reaches `B` without leaving `[1,B]`. This is the
finite inverse closure of `B` in that interval. Its states are disjoint
from `R_B`, and

\[
R_{B+1}=R_B\sqcup A_B,
\qquad
F_{B+1}=(F_B\setminus\{B\})
 \cup\{2n:n\in A_B,\ B+1\le2n\}. \tag{FB5}
\]

Every new boundary source in (FB5) passes through the actual state `B`.
Its canonical complete grade is strictly larger than the grade at `B`,
by the supplied ordinary-step grade theorem. If (FB4) fails, both
retained graph and boundary are unchanged. In particular, for every
odd `B>=3`,

\[
\boxed{R_{B+1}=R_B,\qquad F_{B+1}=F_B.} \tag{FB6}
\]

The equality of boundaries also uses that `2n` is even: changing its
threshold from odd `B` to `B+1` removes no boundary source. This is the
parity relevant to a least bad target `2B+1=3 mod 4`.

### Constant plateaus and the next record

Let `G(B)` be the globally minimum capturing grade and `S(B)` the largest
source at that grade. Finite boundary optimization makes both well-defined
and computable. For every integer `C` with `B<=C<=S(B)`,

\[
\boxed{G(C)=G(B),\qquad S(C)=S(B).} \tag{FB7}
\]

Indeed the set of captures shrinks when the floor increases, so its
minimum grade cannot decrease. The same selected source still captures
every such `C`, giving the reverse inequality. The source maximizing
that grade stays eligible, and no new larger same-grade source can
appear when the admissible set shrinks.

At the next floor `C=S(B)+1`, the grade increases strictly: a capture
there at the old grade would contradict the old maximum-source tie.
Writing `S'=S(S(B)+1)`, its own boundary geometry gives

\[
\boxed{S(B)<S'\le2S(B),\qquad G(S(B)+1)>G(B).} \tag{FB8}
\]

The upper bound follows from `S'<2(S(B)+1)` and the evenness of `S'`.
Thus all floors are partitioned into exact optimum plateaus, whose
right endpoints form an increasing cofinal sequence of certified even
record sources, with successive ratios at most two. No proposed
ordinary target-time bound is used here.

This identifies the target intervals a record argument would have to
close. If consecutive record sources are `s<s'`, the new floor plateau
is `s+1,...,s'`; its target band is

\[
2s+3,\ 2s+5,\ \ldots,\ 2s'+1. \tag{FB9}
\]

The original lower-grade interval hypothesis already covers all positive
targets up to `2s+1`. The same complete next-record certificate supplies
the entire band (FB9). The remaining claim would have to control the
actual targets in that band using this previously certified interval.
The plateau and jump laws do not assert that control.

## 8. Attempted graph-boundary closure and the remaining step

I tried to turn inverse closure of `R_B` and the global grade optimum into
entry of the original target `2B+1`. The exact finite graph contains all
ordinary paths to `1` staying below `B`, and all of its incoming boundary
sources. It carries complete arithmetic and complete grade comparisons.

That closure statement has a specific direction: it adds **predecessors
below the floor of an already retained vertex**. For the target itself,

\[
T(2B+1)=3B+2>B.
\]

No edge of the computed graph provides a path from `3B+2` back into
`R_B` or its boundary. Enlarging the finite graph without a proved bound
on this missing return would simply be a target-orbit search.

At a true joint minimum, all lower-grade complete captures have already
been excluded by the finite optimization. Therefore a universal theorem
asserting that some further source-only edit must beat that optimum is
too strong: the optimum exists for ordinary targets such as 2047 and
3711 as well. A successful argument must use the **actual target** and
its least-bad hypothesis to produce either a return below that same
target, or an explicit contradiction to one of the optimized finite
graph's invariants. Source optimization alone cannot be its concluding
step.

The update (FB5) pays for the entire newly attached source component, but
it does not add the target's forward excursion. At a record jump it
supplies the precise band (FB9), not a path from each band member into
the previously certified interval. I did not prove such a return or
contradiction. In particular, the
finite source clock bound in Section 4 is not transferred to the target
clock; the pinned controls already refute that transfer. The exact global
optimizer is the completed result of this attack, with the target-entry
step still open.

## Dependencies and scope

- **This PR, baseline `0444986571f09f302cb3687b4bba3552600e4119`:**
  `lean/Collatz/SourceOrbitProgress.lean`, `advance_certificate`, for
  literal supplied-witness consumption; `JointMinimalCounterexample.lean`
  for the original `SourceMinimal` and `SourceMaximal` definitions and
  joint counterquery; `ContextSurgery.lean` for the earlier carry scope.
- **PR180, `5e29f56f6d44669a8aa9134e5617b78d65c074c2`,**
  `research/retained-source-attacks-20261122/LEGAL_DESCENT.md`,
  L1--L9: residue-record deletion and the unbounded positive-carry slack
  obstruction. Those statements motivated allowing every complete
  certificate rather than one restricted carry architecture.
- **PR175, `8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`,**
  `research/lean-global-closure-20261121/closing/NONLOCAL_SURPLUS_REPAIR_ATTEMPT.md`:
  original-clock copied-tail restrictions and the 2047 control.
- **PR176, `fdcb137214f4be8ac30dbb025d6eeb6568e22e2a`,**
  `research/lean-global-resolvent-20261121/overview/returns/WHOLE_SOURCE_DEBT_ATTEMPT.md`:
  whole-source count/debt alignment and the 3711 extremal-source control.

No external analytic existence theorem, random-parity premise, or
unproved Collatz hypothesis is an input to FB1--FB3. The final target
entry remains separate. The graph proof and algorithmic interpretation
are written mathematics, while the five named finite reduction theorems
are core-Lean proofs with the original definitions.
