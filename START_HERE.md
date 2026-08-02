# Start here

The Collatz conjecture asks whether repeated application of

\[
C(n)=\begin{cases}
n/2,&n\text{ even},\\
3n+1,&n\text{ odd}
\end{cases}
\]

reaches `1` for every positive integer. This repository often uses the shortcut map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

which removes one forced division by two after an odd step.

**Nothing on `main` resolves the conjecture.** The purpose of the repository is to leave a durable, adversarially checked research trail that humans and later systems can build upon.

## The fastest useful reading path

### New human researcher

1. This page.
2. [`CURRENT_KNOWLEDGE.md`](CURRENT_KNOWLEDGE.md) for the scientific map.
3. [`FRONTIERS.md`](FRONTIERS.md) for the exact open obligations.
4. One proof packet under [`research/integrated/`](research/integrated/README.md).
5. [`CONTRIBUTING.md`](CONTRIBUTING.md) only when you are ready to write or submit work.

### New research or coding agent

1. [`AGENTS.md`](AGENTS.md).
2. [`CURRENT_KNOWLEDGE.md`](CURRENT_KNOWLEDGE.md).
3. The relevant integrated packet and its provenance section.
4. The active source area, issue, or PR for the selected frontier.
5. The archive only when exact historical review or lifecycle evidence is needed.

## The central conceptual firewall

Many attractive constructions prove only finite compatibility:

\[
\forall N\ \exists n_N\text{ realizing the first }N\text{ constraints}.
\]

A Collatz counterexample needs one fixed positive integer:

\[
\exists n\ \forall N\text{, the same }n\text{ realizes every constraint}.
\]

Compatible finite residues determine one 2-adic point, but that point may be negative or nonordinary. The integrated ordinary-extraction packet makes the exact replacement principle explicit:

- canonical least representatives must eventually stabilize for a nonnegative ordinary integer;
- nested positive survivor minima must be uniformly bounded, equivalently eventually constant, for one all-depth positive seed.

Read [`research/integrated/ordinary-extraction/`](research/integrated/ordinary-extraction/README.md) before trusting any finite-prefix, inverse-limit, refund, stack, or automata construction.

## The five current programs

### 1. Ordinary extraction and completion

Question: when does a compatible infinite symbolic or arithmetic construction correspond to one ordinary positive integer?

Known: exact stabilization and bounded-minimum criteria; explicit completion ghosts.

Missing: an architecture-specific theorem proving stabilization or escape.

### 2. Periodic tails and positive cycles

Question: can an eventually periodic parity word be realized by a positive integer outside the trivial cycle?

Known: the answer is controlled by the complete denominator `2^L-3^s` and exact replay.

Missing: a nontrivial positive divisor hit or an all-word exclusion. The combined integrated wording remains pending narrow review.

### 3. Coefficient stopping / SC\*

Question: does every fixed positive source eventually have a coefficient prefix below one?

Known: a source that never crosses has an orbit tending to `+infinity`; the least-source escape formulation is exactly equivalent to universal finite coefficient stopping.

Missing: a fixed-source valuation bound.

### 4. First crossing / FC\*

Question: can a first coefficient crossing nevertheless fail to descend from its canonical source?

Known: cycles and non-descending first crossings can be represented through a common displacement and complete denominator.

Missing: a proof for every word and every denominator factor simultaneously.

### 5. Automata, rigidity, and representation limits

Question: can a finite or tame representation hide the missing all-depth ordinary object?

Known: several broad finite-state, rational-section, semilinear, periodic, and low-complexity templates are excluded in precise settings.

Missing: a genuinely unbounded-state construction or a direct global obstruction.

## Status words used here

- **VERIFIED**: passed an exact-SHA independent review in its stated scope.
- **VERIFIED WITH FIXES**: mathematics survived, but metadata, dependency, wording, source, or artifact fixes remain.
- **SOURCE-QUALIFIED**: valid conditional on an exact external or branch-qualified source theorem.
- **PROPOSED**: complete-looking but not independently accepted.
- **OPEN**: obligation not proved.
- **REFUTED**: false as stated; the refutation remains visible.
- **INTEGRATED REFERENCE**: accepted on `main` as the repository’s reference statement.
- **LOCAL PROOF PACKET**: a readable proof or proof extract physically resides on `main`.

These labels answer different questions. An integrated reference may still have source-resident dependencies. A roadmap record may be accepted while remaining mathematically open.

## What not to infer

- A finite census does not prove an all-length theorem.
- A checker validating a file format does not verify mathematics.
- A periodic 2-adic point need not be a positive integer.
- A full-denominator theorem cannot be replaced by several independently selected proper-factor hits.
- Failure of one method is not evidence that Collatz is false.
- A repaired statement does not retroactively verify the original.

## Deep history

Frozen snapshots, exact review coverage, lifecycle recommendations, machine JSON, and previous handoffs are retained under the [`archive`](archive/README.md) index. They are evidence for integrators and auditors, not the first reading assignment.
