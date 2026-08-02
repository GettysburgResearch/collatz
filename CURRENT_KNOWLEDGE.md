# Current knowledge and research map

**Repository status:** Collatz remains unsolved.

This page is the scientific synthesis for `main`. It answers four questions:

1. What narrow results have survived exact-SHA review?
2. Which proof bodies are readable locally?
3. How do the main research programs connect?
4. What exact lemma is still missing at each boundary?

For machine-readable provenance, use `claims/registry/`. For frozen review-wave evidence, use the [`archive`](archive/README.md). Neither is required to understand this page.

## Status and residency key

- **Integrated reference**: accepted on `main` as the repository’s reference statement.
- **Local proof packet**: a readable proof or proof extract resides under `research/integrated/`.
- **Source-pinned dependency**: a dependency is exact-SHA reviewed but its proof body is not yet imported locally.
- **Pending narrow review**: component results were reviewed, but the exact integrated synthesis still needs independent checking.
- **Open**: the mathematical obligation is not proved.
- **Proposed connection**: a useful synthesis or attack route that has not been independently established as a theorem.

## At a glance

| Integrated ID | Result | Mathematical status | Local residency | Main boundary |
|---|---|---|---|---|
| `IC-EXTRACT-001` | Ordinary extraction by signed residue stabilization and bounded nested minima | verified | local proof packet | Does not decide any concrete least-root sequence. |
| `IC-GHOST-001` | Explicit supercritical `(1110)^∞` completion ghost | verified | local proof packet | Shows a quantifier failure; does not exclude seed-first constructions. |
| `IC-PERIODIC-001` | Periodic tails and complete-denominator divisibility | reviewed components; integrated synthesis pending narrow review | local proof packet | Exact all-zero, finite-preperiod, and fixed-block scope must be independently checked as one statement. |
| `IC-SC-001` | Supercritical divergence and SC\* source-escape equivalence | verified | local proof packet | SC\* itself remains open. |
| `IC-AUT-001` | Fixed-depth cofinite-tail automata obstruction | verified | local proof packet | Does not exclude every regular or infinite-state sanctuary. |
| `IC-RIG-001` | Finite affine/rational six-branch rigidity and no semilinear sanctuary | verified | local proof packet | Does not decide the six-branch least roots or exclude unbounded nonlinear state. |
| `IC-REF-001` | Refutation of the unrestricted factor-complexity screen | refuted as stated | local proof packet | Only the unrestricted statement is false. |
| `IC-REP-001` | Separate nonconstant factor-complexity repair | verified | local proof packet with source-pinned PR #16 dependencies | Applies only to the induced `64→81` centered-cylinder model. |

## Program A — ordinary extraction and completion

### Established theorem interface

Let

\[
1=K_0\mid K_1\mid K_2\mid\cdots,
\qquad K_n\to\infty,
\]

and let `r_n` be compatible canonical least residues. The induced inverse-limit point is:

- a nonnegative ordinary integer exactly when `r_n` is eventually constant, equivalently the appended blocks are eventually zero;
- a negative ordinary integer exactly when `K_n-r_n` is eventually constant, equivalently the appended blocks are eventually maximal.

For nested nonempty positive survivor sets

\[
S_0\supseteq S_1\supseteq\cdots,
\qquad m_n=\min S_n,
\]

one positive all-depth seed exists exactly when `(m_n)` is bounded, equivalently eventually constant.

**Local proof:** [`research/integrated/ordinary-extraction/`](research/integrated/ordinary-extraction/README.md)

### Why it matters

This is the project’s main finite-versus-infinite firewall. It replaces the invalid inference

\[
\forall n\ \exists x_n
\quad\not\Rightarrow\quad
\exists x\ \forall n
\]

with a precise ordinary compactness condition.

### Exact missing lemma

For each concrete aperiodic architecture, prove one of:

\[
\sup_n m_n<\infty
\]

or

\[
m_n\to\infty.
\]

The first supplies one fixed ordinary seed; the second eliminates the whole architecture. Conditional growth, branch abundance, inverse-limit uniqueness, stack capacity, and finite SCCs do not decide this dichotomy.

### Canonical countermodel

The periodic parity word `(1110)^∞` has one exact 2-adic realization `-19/11`, while every finite prefix has infinitely many positive integer representatives and the block multiplier is `27/16>1`.

**Local proof:** [`research/integrated/completion-ghost/`](research/integrated/completion-ghost/README.md)

This proves that finite physical compatibility, computability, positive symbolic drift, and an exact infinite 2-adic path still do not produce a positive ordinary trajectory.

## Program B — periodic tails, cycles, and the full denominator

For a nonempty parity word `w` of length `L`, weight `s`, and affine constant

\[
C_w=\sum_{j=0}^{L-1}\varepsilon_j2^j3^{s-s_{j+1}},
\]

the block map is

\[
T^L(x)=\frac{3^s x+C_w}{2^L}.
\]

The periodic tail `w^∞` has the unique 2-adic realizer

\[
x_w=\frac{C_w}{2^L-3^s}.
\]

Consequences:

- when `3^s>2^L`, a nonzero periodic realizer is negative, so the schedule cannot be a positive ordinary divergent orbit;
- when `3^s<2^L`, positive ordinary realization requires the **complete** divisibility
  \[
  2^L-3^s\mid C_w;
  \]
- if the divisibility holds, exact parity replay gives a positive cycle whose period divides `L`;
- the all-zero word is the separate endpoint `x_w=0`;
- a positive ordinary eventually periodic itinerary must enter a positive cycle after its finite prefix.

**Local packet:** [`research/integrated/periodic-tails/`](research/integrated/periodic-tails/README.md)

### Current integration boundary

The component source theorems were independently reconstructed, but the exact integrated statement combining the all-zero endpoint, finite preperiod, complete denominator, and fixed-block controller interpretation remains **PENDING NARROW REVIEW**. It must not be cited as a newly reviewed synthesis before that review.

### Exact missing lemma

The periodic class reduces positive-cycle existence to a finite certificate:

```text
complete denominator divisibility
+ nontrivial positive primitive cycle
+ exact physical replay.
```

The general cycle program still lacks either:

- one nontrivial exact divisor hit; or
- an all-word proof that no such hit exists.

Proper-factor congruences and independently selected local residues are insufficient.

## Program C — coefficient stopping and SC\*

For a positive source `n`, let

\[
C_k(n)=\frac{3^{q_k(n)}}{2^k}
\]

and define the coefficient stopping time

\[
\tau_c(n)=\min\{k\ge1:C_k(n)<1\}.
\]

Let `S_N` be the sources whose first `N` coefficient prefixes are all at least one, and let `m_N=\min S_N`.

### Established results

1. If one positive ordinary orbit satisfies `C_k(n)≥1` for every `k`, then
   \[
   T^k(n)\to+\infty.
   \]
2. The inverse relation is exact:
   \[
   m_N>B
   \iff
   \tau_c(n)\le N\text{ for every }1\le n\le B.
   \]
3. Therefore
   \[
   m_N\to\infty
   \iff
   \tau_c(n)<\infty\text{ for every positive integer }n.
   \]

**Local proof:** [`research/integrated/coefficient-stopping/`](research/integrated/coefficient-stopping/README.md)

### What is open

`SC*` is the universal assertion on the right-hand side. The equivalence is proved; the assertion is not.

### Smallest missing lemma

For every fixed positive integer `n`, prove a finite bound `Φ(n)` such that no all-supercritical word `w` realized from `n` has length exceeding `Φ(n)`. Equivalently, beyond a source-dependent threshold, prove

\[
v_2(3^{q(w)}n+A_w)<|w|.
\]

A moving family of finite sources or a compatible 2-adic path does not satisfy this fixed-source obligation.

## Program D — first crossing and FC\*

A coefficient-first-crossing word has

\[
3^q<2^j,
\qquad D=2^j-3^q>0.
\]

For its canonical source `r`, endpoint `s=r+d`, and affine numerator `A_w`, the reviewed architecture uses

\[
A_w=Dr+2^j d=Ds+3^q d.
\]

A non-descending canonical realization has `d≥0`. Nontrivial positive cycles can be rotated to a minimum state and placed in this same first-crossing lane.

### What is established

Reviewed work supplies:

- the exact source/end/displacement representation;
- reduction of nontrivial positive cycles to a first-crossing witness;
- complete-factor synchronization and resultant-root formulations for reviewed subclasses;
- several support, mechanical-word, and finite-range exclusions.

These results remain source-pinned; they are summarized in [`FRONTIERS.md`](FRONTIERS.md#fc-complete-first-crossing-exclusion).

### What is open

`FC*` asks for an exclusion of **every** complete nontrivial first-crossing realization with `d≥0`, including:

- `d=0` nontrivial cycles;
- `d>0` acyclic near-returns;
- every complete prime-power factor of `D`;
- one common ordinary displacement and compatible source/end quotients;
- exact physical replay.

The smallest missing theorem is a global cross-factor incompatibility or least-residue lower bound that works for growing support.

## Program E — automata, rigidity, and representation limits

### Fixed-depth safety automata

For each fixed depth `d`, the set of positive integers avoiding `{1,2}` through depth `d` is cofinite. Its minimal LSD-first canonical DFA has one terminal two-state cyclic SCC caused by eventual canonicality; the remaining boundary is acyclic. The safe set is not forward invariant, and no cofinite forward-invariant set can exclude `{1,2}`.

**Local proof:** [`research/integrated/finite-safety-automata/`](research/integrated/finite-safety-automata/README.md)

This rules out interpreting the obvious recurrent component of a finite safety approximation as an all-depth sanctuary.

### Six-branch finite tame rigidity

For the reviewed chart

\[
P=3^{12},\qquad Q=2^{19},
\]

with six specified digits, the following complete-tree certificate classes collapse:

- finite affine self-sections;
- finite rational-function self-sections with eventual integrality;
- semilinear or ultimately periodic value-space sanctuaries.

The only finite affine/rational self-section is the original expanding forward map.

**Local proof:** [`research/integrated/six-branch-rigidity/`](research/integrated/six-branch-rigidity/README.md)

The least-root sequence remains undecided, and unbounded nonlinear state is not excluded.

### Factor-complexity boundary

The unrestricted claim that every low-complexity itinerary has nonstabilizing nearest-integer blocks is false: `0^∞` and `1^∞` are exact counterexamples. A separate theorem repairs the statement for **nonconstant** words in the reviewed `64→81` centered-cylinder model and gives the slope threshold

\[
\frac{1}{\log_{64}(81/64)}=17.654847\ldots.
\]

**Local packet:** [`research/integrated/factor-complexity/`](research/integrated/factor-complexity/README.md)

The repair depends on reviewed PR #16 recurrence-cone and centered-cylinder results whose proof bodies remain source-pinned.

## Exact logical dependency map

```text
ordinary residue stabilization
        +
nested least-root compactness
        └──> ordinary-extraction firewall
                  ├──> completion ghosts expose invalid finite-prefix inference
                  ├──> SC* becomes fixed-source least-root escape
                  └──> aperiodic architectures must prove stabilization or escape

periodic affine block identity
        +
parity-cylinder injectivity
        └──> complete-denominator periodic classification
                  └──> positive cycles are finite full-denominator certificates

fixed-source coefficient identity
        ├──> all-supercritical ordinary orbit diverges
        └──> SC* equivalence

first-crossing source/end identity
        +
cycle rotation to a minimum
        └──> FC* obligation

SC* + FC*
        -- PROPOSED, not yet independently accepted as one crosswalk -->
        Collatz
```

## Proposed connections worth testing

The following are scientifically useful but remain **PROPOSED**.

### P1 — ordinary-boundary state should be explicit in automata/PDR

The cofinite-tail theorem and completion-ghost theorem suggest that any sound automata abstraction aimed at ordinary extraction must carry a canonical most-significant boundary, height counter, finite-support proof, or equivalent concretization witness. Residue-only recurrence is structurally too weak.

### P2 — rigidity turns extraction into an unbounded-state problem

Combining the six-branch finite rational rigidity with the ordinary-extraction theorem suggests a sharper search rule: either discover a genuinely unbounded nonlinear state variable tied to the same initial root, or prove direct least-root escape. More finite tame recodings should not be treated as progress toward extraction.

### P3 — periodic classification is the cycle endpoint of FC\*

The periodic complete-denominator theorem and first-crossing displacement architecture appear to meet at `d=0`: a successful FC\* theorem should include the periodic cycle case without a separate cycle premise. The exact repository-level crosswalk is still pending review.

### P4 — factor complexity can constrain ordinary boundary stabilization

The nonconstant complexity repair suggests coupling language recurrence bounds to canonical appended-block dynamics. A useful next theorem would derive a low-complexity presentation from an equality or near-extremal language and then invoke the repair to force nonstabilization.

## What main still does not contain

- a proof of SC\*;
- a proof of FC\*;
- an independently accepted SC\*/FC\* bridge theorem;
- a nontrivial positive cycle or divergent positive seed;
- a decision of the six-branch least-root sequence;
- local proof packets for every reviewed theorem in the repository;
- independent replay of every large computational artifact.

These absences are part of the current scientific state, not documentation defects.
