# Rewrite termination: method-specific obstructions and proof certificates

## Exact Collatz rewrite system

Yolcu–Aaronson–Heule supply an exact mixed binary–ternary string-rewriting formulation whose termination is equivalent to the Collatz conjecture. PR #6 correctly treats the published equivalence as external background and keeps new obstructions namespaced.

## Match bounds

Match-boundedness is a sufficient termination technology for suitable string-rewriting systems. An unbounded family under one frozen lift convention excludes only a finite global bound for that convention (`LIT-KTHM-0025`). It does not imply nontermination and does not rule out relative match bounds, semantic labeling, dependency pairs, strategy restrictions, or other interpretations.

## Natural, tropical, and arctic interpretations

These methods reduce termination to finite families of monotonicity and strictness inequalities. For auditability, a successful result should store the complete interpretation and every checked inequality. A failed search should store a proof-producing UNSAT certificate or at least a frozen finite polynomial/linear system.

## Recommended certificate fields

- exact rewrite rules and orientation;
- annotation/interpretation convention;
- carrier semiring and order;
- matrices/vectors or symbolic block parameters;
- weak inequalities for every rule;
- the strictly decreasing rule or critical return;
- context/monotonicity proof;
- Farkas or solver certificate where applicable;
- independent checker and tool version.

## Scope discipline

Failure of one termination technology is a negative result about that technology. It is not evidence for a divergent ordinary Collatz trajectory.