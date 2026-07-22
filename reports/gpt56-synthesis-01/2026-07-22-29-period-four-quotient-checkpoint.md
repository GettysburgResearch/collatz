# Period-four quotient checkpoint

Agent: `gpt56-synthesis-01`  
Issue: `#29`  
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`  
Date: 2026-07-22

## Starting hypothesis

The positive period-four Padé quotient might be controlled by splitting its
cyclotomic obstruction into odd-prime, dyadic, and genuinely composite local
problems.

## Approaches attempted

Parallel lanes attacked tropical block minimizers, carry gaps, root-of-unity
q-Lucas descent, normalized Hasse jets, and a characteristic-two Cartier
product. Separate agents tried direct product lifts, composite residual
classification, divided-difference induction, and finite automata witnesses.

## New results

- `L-9868` gives the exact two-level block decomposition, finite residual
  states, and strict prime-power carry gap.
- `L-9869` gives the two-jet odd-prime cancellation bound; subject to external
  review, it excludes every odd prime-power order above the cutoff.
- `L-9870`--`L-9872` give the carry-optimal composite state and exact value and
  first-jet descents.
- `L-9873` records an integral finite-channel interpolation at arbitrary jet
  order as a candidate theorem. Its interpolation algebra is complete; its
  universal period-product degree lemma is the explicit review boundary.
- `L-9874` closes the two dyadic boundary families.
- `L-9875` proves the characteristic-two product, scalar-kernel valuation,
  transfer recurrences, and binary-cluster arithmetic.
- `X-9876` vendors portable exact checkers and records the finite `p=3`
  squarefree census without promoting it to a theorem.

The direct upper product lift is false modulo `Phi_m^2`; the smallest exact
counterexample is `(m,A,r)=(5,1,2)`. The correct replacement is finite-channel
interpolation.

## Candidate counterexamples

None.

## Failed approaches

- value-only composite peeling fails, e.g. `(u,L)=(4,12)` has two simple
  residual zeros below the required multiplicity;
- a one-channel local product does not lift past the value jet;
- three minimum-word automata images do not eliminate every gate;
- exploratory dyadic halving identities were not frozen or promoted.

## Potential errors

The long rational ledger in `L-9869` needs external symbolic reconstruction.
The arbitrary-order degree lemma in `L-9873` needs a fuller formal proof.
Every theorem-level claim therefore remains `PROPOSED`.

## Files changed

Eight claim files, nine proof appendices, `X-9876`, this report, and the three
packet indexes.

## Claims affected

`L-9868`--`L-9875`; experiment `X-9876`.

## Recommended next actions

1. Prove the uniform dyadic transfer valuation, then its mod-four lift.
2. Externally reconstruct `L-9873`'s degree lemma.
3. Prove the observed `p=3` residual classification from `L-9872`.
4. Build the central-carry finite Hasse-jet automaton for general composite order.

## Organizational improvement ideas

Keep universal proofs, finite audit scripts, and empirical censuses in
separate files, with claim wrappers stating exactly which layer is proved.

