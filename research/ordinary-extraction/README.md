# Ordinary-integer extraction from nested legal cylinders

**Agent:** `gpt56-global-01`  
**Issue:** `#55`  
**Status:** isolated `76xx` theorem packet; all theorem-level claims are `PROPOSED` pending independent review  
**Counterexample status:** none

## Executive conclusion

The repeated logical gap in the constructive branches is the quantifier swap

\[
\forall n\ \exists x_n\in\mathbf Z_{>0}
\text{ legal through depth }n
\quad\not\Longrightarrow\quad
\exists x\in\mathbf Z_{>0}\ \forall n,
x\text{ legal through depth }n.
\]

Nested-cylinder compactness can replace the left side by one compatible inverse-limit point

\[
\exists \alpha\in\mathbf Z_2\ \forall n,
\]

but it does not prove that `alpha` is an ordinary positive integer.

The exact missing inference is ordinary boundedness.  For one fixed prefix-closed machine, let

\[
S_n=\{x\in\mathbf Z_{>0}:x\text{ is legal through depth }n\},
\qquad
m_n=\min S_n.
\]

Then

\[
\boxed{
\bigcap_n S_n\ne\varnothing
\iff
(m_n)\text{ is bounded}
\iff
(m_n)\text{ eventually stabilizes}.}
\]

This is `T-7601`.  It is the only compactness principle needed for ordinary extraction, and it is not supplied by arbitrarily long prefixes, a compatible `2`-adic path, positive entropy, refund capacity, fresh-prime turnover, or a theorem that every hypothetical survivor grows.

## Why the usual amplifier package is insufficient

`T-7602` gives a Collatz-native exact counterexample to the invalid inference.  The periodic parity schedule

```text
(1110)^\infty
```

has all of the following:

- every finite prefix is realized by infinitely many positive integers;
- the infinite parity path is exact and computable;
- its four-step formal multiplier is `27/16>1`;
- any positive ordinary realization would be unbounded;
- its unique `2`-adic realization exists.

Nevertheless its unique realization is

\[
-19/11\in\mathbf Z_2\setminus\mathbf Z.
\]

Thus finite compatibility plus an exact supercritical infinite path plus conditional growth can still be a pure completion ghost.

## Why the Diagonal Foundry is not yet a reduction

`R-7601` audits the strictly causal parity-digit closure proposal directly.

For a strictly causal operator

\[
E_k:\{0,1\}^k\to\{0,1\},
\]

the closure equation

\[
\operatorname{par}(\alpha_E)
=E(\operatorname{dig}(\alpha_E))
\]

has one uniquely computable point `alpha_E in Z_2`.  However:

```text
E -> alpha_E is surjective onto all of Z_2;
computable E -> alpha_E is surjective onto all computable 2-adic points.
```

More strongly, for every tail property `P` invariant under finite changes and containing `1^infinity`,

```text
some uniformly P-output foundry has a positive ordinary point
    iff
some positive ordinary integer already has parity word in P.
```

For the supercritical one-density property this says that the foundry target is exactly the pre-existing restricted divergent-integer target.  Strict causality gives uniqueness and computability, but no eventual-zero binary tail and no ordinary extraction.  Unrestricted foundry enumeration is therefore a reparametrization of computable `2`-adic points, not a weaker route to a counterexample.

A restricted operator family could still matter only after proving architecture-specific eventual-zero or bounded-least-root information.

## Exact restricted target

The cleanest live positive target is the PR `#45` / PR `#50` six-branch chart.  Put

```text
P=3^12,
Q=2^19,
A={229376,258048,290304,326592,367416,413343},
x_(k+1)=ceil(P*x_k/Q),
a_k=Q*x_(k+1)-P*x_k.
```

Let

```text
S_n={x_0>0 : a_0,...,a_(n-1) all lie in A},
m_n=min S_n.
```

`T-7603` proves the exhaustive architecture-level decision:

```text
(m_n) bounded/eventually constant
    -> one explicit restricted minimal-word root
    -> branch-qualified physical Collatz K-candidate;

some S_n empty or m_n -> infinity
    -> no positive ordinary survivor in this entire six-branch chart.
```

This is a narrower decision problem than Collatz.  Its negative side eliminates only one fixed subsystem.  Its positive side is a restricted sufficient condition for Collatz to be false; it is not logically weaker than the statement “Collatz is false.”

## Claim index

| ID | Title | Status |
|---|---|---|
| `D-7601` | Nested legal-cylinder trees and ordinary seed sets | `PROPOSED` |
| `L-7601` | Signed stabilization criterion for one compatible branch | `PROPOSED` |
| `T-7601` | Bounded-minimum ordinary compactness theorem | `PROPOSED` |
| `T-7602` | Supercritical compatible parity schedules can be nonordinary ghosts | `PROPOSED` |
| `T-7603` | Six-branch restricted-minimum decision reduction | `PROPOSED`, physical implication branch-qualified |
| `R-7601` | Strictly causal foundry is surjective and preserves the original tail-witness problem | `PROPOSED / ARCHITECTURE REFUTATION` |
| `Q-7601` | Decide boundedness versus escape of the six-branch least roots | `IDEA / GLOBAL BLOCKER` |
| `T-7701` | Every eventually periodic supercritical parity schedule is nonpositive | `PROPOSED`, independent review extension |
| `T-7702` | A finite portfolio extracts an ordinary seed only through one constituent | `PROPOSED`, independent review extension |

## Repository-wide verdict

The architecture audit in [`ARCHITECTURE_AUDIT.md`](ARCHITECTURE_AUDIT.md) classifies the current programs.

The important distinction is:

- PR `#33` / PR `#44` genuinely cross the extraction boundary **negatively** for one frozen corrected stage class by proving that every compatible completion is nonordinary.
- PRs `#45`, `#49`, `#51`, and `#19` have exact ordinary state machines and strong consequences **conditional on infinite legality**, but none proves a bounded least-root sequence or supplies one finite forever-defined root.
- fixed-modulus PDR, prescribed directives, unrestricted causal foundries, and raw or transported stack capacity do not supply the missing quantifier swap.
- the cycle lanes have a different global blocker: complete divisibility by the entire denominator and exact replay.  This packet does not pretend that ordinary-extraction compactness resolves that finite arithmetic obligation.

## Progress gate

For a nested ordinary-survivor architecture, a new result changes the full-objective status only if it proves at least one of:

1. a uniform upper bound `m_n<=B` for all depths;
2. eventual stabilization of the canonical pulled-back residue;
3. one explicit seed together with an all-time legality induction;
4. divergence `m_n->infinity` or eventual nonboundary residue blocks for the entire fixed architecture.

Longer finite prefixes, larger multipliers, more refund, additional stack capacity, denser surviving residue trees, stronger growth after legality, or another uniquely generated nonordinary `2`-adic point are useful local mathematics but do not cross the ordinary-extraction boundary.

## Independent review extension

The reconstruction by `gpt56-global-review-01` is recorded in

[`INDEPENDENT_REVIEW_2026-07-25.md`](INDEPENDENT_REVIEW_2026-07-25.md).

It verifies the abstract proofs of `L-7601`, `T-7601`, and `T-7602`; reconstructs the six-branch digit normalization in `T-7603`; scope-checks the Diagonal Foundry refutation `R-7601`; and independently checks the stronger abstract compactness countermodel on PR #56.

Two further exhaustive closures are added:

1. `T-7701` proves that **every** eventually periodic supercritical shortcut-parity schedule has a negative rational realization. Autonomous finite-state high-drift schedule generators are therefore closed as a positive certificate class.
2. `T-7702` proves that a finite union of fixed nested architectures has an ordinary survivor only when one constituent already does. A genuine cross-machine program must provide exact physical switching transitions and is a new architecture.

The review recommends consolidating the overlapping PR #56 and PR #57 theorem packets, retaining PR #57 as the Collatz-native canonical presentation and importing PR #56's universal affine countermodel without duplicate least-root ledgers.