# Status of the `SC* + FC*` bridge

## Current verdict

```text
SC* + FC* => Collatz
```

is a strong **proposed repository-level bridge**, not yet an accepted canonical theorem.

There is meaningful reviewed evidence:

- PR #80 `D-6501` at `5ca112a783fc269acdadadc6e2e86e2cdadb4298` gives the least-counterexample two-lane framework. The independent review explicitly found the Lane A/Lane B split and minimum-cycle rotation correct.
- PR #77 `T-6709/T-6710` at `3efcbfb2e38f02b04eb6bba35eb258ec552d655c` supplies the reviewed all-supercritical divergence theorem and the definition/equivalence behind SC*.
- PR #81 `L-6814/L-6817` at `816c364ab2019a6dda235f710f8d30de2da33ab9` supplies reviewed cycle absorption and primitive/injective reductions for the first-crossing lane.

What is missing is one clean, independently reviewed theorem proving that the **current repository definitions** of `RD-SC-001` and `RD-FC-001` match those reviewed lane components without a normalization, canonical-source, endpoint or trivial-cycle gap.

The registry therefore adds `RD-BRIDGE-001` as `PROPOSED / ROADMAP`, not as an accepted proof.

## Proposed exact framework

Use the shortcut Collatz map

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

Assume Collatz is false and let \(n_*\) be the least positive integer whose orbit never reaches \(1\).

For its first \(k\) shortcut steps let

\[
q_k=\#\{0\le i<k:T^i(n_*)\text{ is odd}\},
\qquad
C_k=\frac{3^{q_k}}{2^k}.
\]

For every parity prefix \(w\) of length \(k\), write the exact affine identity

\[
T^k(r)=\frac{3^{q(w)}r+A_w}{2^k}.
\]

### Least-counterexample no descent

Every iterate of \(n_*\) is at least \(n_*\). Otherwise a smaller iterate would converge by minimality, forcing \(n_*\) to converge.

### Lane A — no coefficient crossing

\[
C_k\ge1\qquad\text{for every }k\ge1.
\]

This is exactly the fixed-source all-supercritical situation. `RD-SC-001` asserts that every positive source has a finite coefficient crossing. Therefore SC* excludes Lane A.

The reviewed PR #77 theorem also says that an ordinary positive orbit in Lane A tends to \(+\infty\); this classifies the lane but is not itself the exclusion.

### Lane B — finite first crossing

There is a first \(j\ge1\) such that

\[
C_k\ge1\quad(1\le k<j),
\qquad
C_j<1.
\]

Let \(w\) be this first-crossing word. For its canonical positive source/end pair write

\[
s_w=r_w+d,
\qquad
D=2^j-3^{q(w)}>0.
\]

The source/endpoint identity is

\[
A_w=D r_w+2^j d
    =D s_w+3^{q(w)}d.
\]

The actual least counterexample is one positive lift of the same canonical word. Because higher lifts change endpoint-minus-source by \(-D\) per lift, no-descent of the actual lift forces the canonical displacement \(d\ge0\).

`RD-FC-001` is intended to exclude every complete nontrivial canonical first-crossing realization with \(d\ge0\), using the complete denominator, one common displacement, compatible source/end quotients and exact replay. Therefore FC* excludes Lane B.

### Positive cycles

For a nontrivial positive cycle, rotate to its minimum state. Over the full primitive period,

\[
2^p n=3^q n+A,\qquad A>0,
\]

so \(3^q<2^p\). A first coefficient crossing exists within the period. The endpoint at that crossing is another cycle state and is at least the rotated minimum, so the associated canonical displacement is nonnegative. Thus the cycle enters Lane B.

The trivial \(1\leftrightarrow2\) shortcut cycle must be excluded explicitly from FC*'s forbidden family or treated as the allowed word `10`.

### Other nonconvergent behavior

A positive deterministic integer orbit that does not tend to infinity visits a bounded set infinitely often; a repeated value then makes it eventually periodic. Hence every nonconvergent positive orbit is either divergent to infinity or eventually enters a nontrivial positive cycle. The Lane A/Lane B coefficient partition itself is immediate from whether a first crossing exists, so bounded aperiodic behavior does not form a third coefficient lane.

## Proposed bridge theorem

> **BRIDGE-L1 (proposed).**  
> Under the shortcut-map normalization above, suppose:
>
> 1. `SC*`: every positive integer has finite coefficient stopping time; and
> 2. `FC*`: apart from the trivial cycle word, every complete canonical first-crossing realization has negative displacement \(d<0\).
>
> Then every positive integer reaches \(1\).

### Proposed proof

Assume a least positive counterexample \(n_*\). If it has no coefficient crossing, SC* is contradicted. Otherwise take its first crossing. Least-counterexample no-descent and canonical-lift monotonicity produce a nontrivial complete first-crossing realization with \(d\ge0\), contradicting FC*. A nontrivial positive cycle is included by the minimum-rotation argument. Therefore no least positive counterexample exists.

## Narrow missing review obligation

An independent reviewer should verify:

1. the precise definition of canonical positive source when the residue is zero;
2. the source/end lift formula and sign of the displacement change;
3. that `RD-FC-001` includes every first-crossing word, not only internally injective, mechanical, bounded-support or already factorized subclasses;
4. that the primitive/injective reduction does not omit repeated-state witnesses;
5. the treatment of the trivial `10` cycle;
6. consistency of `q`, `j`, source `r`, endpoint `s`, displacement `d`, and denominator orientation across PRs #77/#80/#81/#83;
7. whether SC* should be stated as universal finite coefficient stopping or directly as \(m_N^{sup}\to\infty\);
8. that no source-qualified theorem is being silently promoted in the bridge proof.

If this narrow review passes, `RD-BRIDGE-001` can become an accepted conditional bridge theorem even though SC* and FC* remain open.

## Language rule

Until that review passes, use:

```text
SC* + FC* is the principal proposed roadmap bridge.
```

Do not use:

```text
the repository has established a logically exhaustive proof reduction.
```

The bridge is valuable because its components are close to a clean theorem, not because the open obligations are solved.
