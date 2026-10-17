# T-9419 — Withdrawn all-positive-stack irrationality claim

Claim ID: `T-9419`  
Title: The attempted uniform irrationality theorem depended on the invalid completion-identification step in `T-9418`  
Status: `WITHDRAWN — INVALID PROOF; STATEMENT OPEN`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Withdrawn: 2026-07-22  
Dependencies audited: `L-9407`, `L-9408`, withdrawn `T-9418`  
Scope: arbitrary positive stack increment directives  
Related counterexample candidates: none

## Withdrawn statement

The previous version claimed that every infinite positive height-increment
directive selected an irrational stack context.

That conclusion is **not proved**.

## Failure propagation

For a positive directive, the sparse support gaps do tend to infinity. The
previous proof then invoked withdrawn `T-9418` to conclude irrationality.

`T-9418` was invalid because it combined:

```text
- denominator descent for a rational Q_2 tail value;
- a geometric bound for a separate real tail limit.
```

The same conflation appeared again in the direct proof of this file. Thus both
presentations fail at the same point.

## What remains valid

The following statements are unchanged:

1. `L-9407` gives the exact sparse `2`-adic partial-theta normal form.
2. `L-9408` gives the exact finite-prefix and periodic transfer identities.
3. `L-9416` gives descending reduced denominators **if** a `2`-adic one-tail is
   rational.
4. `T-9412`--`T-9417` exclude the periodic families stated there, using valid
   Padé or source-dependent arguments.
5. `L-9415` reduces every fixed periodic word to a homogeneous order-two
   `q`-difference equation.

None of these supplies a uniform theorem for arbitrary positive directives.

## Current status of the stack frontier

The balanced nonperiodic `17/18` directive and general positive adaptive
increments remain open. A valid proof must control the ordinary height of the
same rational `2`-adic tails, or use a source theorem/Padé family directly at
the `2`-adic value.

## Dependency audit

No result prior to the withdrawn `T-9418` is demoted by this correction.
`T-9420` and `T-9421` are also withdrawn because they reused the same false
archimedean state bound.

## Suggested next attack

Return to the two valid routes:

```text
1. fixed-period order-two q-difference irrationality;
2. period-uniform standard-word Padé/height estimates.
```

The denominator descent may be retained only as an auxiliary arithmetic
coordinate, not as a standalone irrationality proof.
