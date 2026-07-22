# T-8805 — Complete two-phase connector coboundary

Claim ID: T-8805  
Title: Every connector on phases `-2,-1` has a telescoping odd-step excess  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: L-8803, T-8802  
Scope: all finite signed phase segments contained in the `T_5` cycle `-2 <-> -1`  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

Under the signed shortcut map `T_5`,

```text
T_5(-2)=-1,
T_5(-1)=-2.
```

Define

```text
chi(-2)=0,
chi(-1)=1.
```

Let a connector start at `d_0 in {-2,-1}`, have length `L`, endpoint
`d_L=T_5^L(d_0)`, and odd-step count `s`. Then

```text
2s-L = chi(d_0)-chi(d_L),                              (1)
```

or equivalently

```text
s = [L+chi(d_0)-chi(d_L)]/2.                           (2)
```

Together with L-8803, every such connector is exactly

```text
T_5^L(2^L*q+d_0)=5^s*q+d_L.                            (3)
```

Consequences:

1. The endpoint is forced by the parity of `L`; there is exactly one phase word
   for each start phase and length.
2. A one-way switch can have an apparent half-step excess or deficit, but the
   quantity is a boundary coboundary.
3. Every closed phase circuit has

   ```text
   d_L=d_0,
   s=L/2.
   ```

4. Segmenting, rebracketing, or scheduling connectors whose only state is
   `{-2,-1}` cannot improve the closed-loop odd-step density beyond `1/2`.

The closed-loop quotient multiplier remains the genuine positive-drift baseline

```text
5^(L/2)/2^L = (sqrt(5)/2)^L,
```

but phase switching contributes no additional asymptotic gain.

## Definitions

- A connector here is a signed orbit segment contained entirely in the two
  phases `-2,-1`.
- **Phase-only gain** means an alleged long-run improvement coming solely from
  choosing connector boundaries or switch directions, without introducing
  quotient/carry state, additional phases, collisions, or unbounded memory.

## Motivation

The first packet left open whether a finite connector family between the two
phases could replenish precision. This theorem closes the coarsest version of
that question completely. The two-state phase graph has no combinatorial
freedom: it is one alternating orbit, and its odd-step imbalance telescopes.

## Proof or construction

The displayed transition identities are immediate:

```text
-2 / 2 = -1,
(5*(-1)+1)/2 = -2.
```

Therefore `chi(d_(k+1))=1-chi(d_k)`, while the parity bit at step `k` is exactly
`chi(d_k)`. Hence

```text
2*chi(d_k)
 = 1 + chi(d_k)-chi(d_(k+1)).
```

Summing from `k=0` to `L-1` gives

```text
2s
 = L + chi(d_0)-chi(d_L),
```

which is (1) and (2). Equation (3) is L-8803.

If the connector closes, the endpoint terms cancel and `2s=L`. Concatenating
connectors merely adds equations (1), so all internal endpoint terms cancel;
only the initial and final phases remain. Thus no phase-only scheduling can
create a persistent excess. **QED**

## Dependency audit

- L-8803 supplies the lifted connector identity.
- T-8802 supplies the same two physical phases in the original chart, although
  the signed alternation is also checked directly here.
- No finite experiment is used in the proof.

## Gap audit

- This theorem does not exclude finite-state connectors whose states refine the
  quotient, carry, or residue cylinder beyond the phase label.
- It does not exclude connectors that leave the signed cycle `{-2,-1}` and
  return through other phases.
- It does not remove the baseline positive multiplier `5/4` per two steps.
  It removes only an alleged extra gain from phase-switch scheduling.
- Precision replenishment may be encoded in a different invariant than odd-step
  density; such a mechanism must state and prove that invariant explicitly.

## Adversarial tests

X-8802 checks every start phase and connector length through `20`, replays the
physical lifted identities for quotient samples through `1000`, and checks all
closed even-length circuits in scope.

## Remaining uncertainty

Whether a refined finite-state connector with quotient/carry memory can create
an ordinary positive infinite branch remains open.

## Suggested next attack

Work in the exact base-`5/4` representation tree of T-8806. There the missing
state is explicit: it is the growing integer node, not the two-valued phase.
Search for a finite quotient or residue abstraction that proves eventual escape
from digits `{0,1}`, or find a self-replicating low-digit subtree.
