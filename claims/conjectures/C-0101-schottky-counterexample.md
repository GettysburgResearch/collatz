# C-0101 — Aperiodic integer Schottky certificate exists

Claim ID: `C-0101`  
Title: Existence of an aperiodic integer Schottky automaton certifying a divergent Collatz orbit  
Status: `IDEA`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0102`, `L-0101`, `L-0102`, `L-0103`, `L-0104`  
Scope: speculative existence claim for a certificate format  
Related counterexample candidates: none yet

## Statement

There exists a finite directed edge-labeled graph \(\mathcal{A}\) (a Schottky
automaton) such that:

1. every edge label is a finite chronological Collatz parity word;
2. every edge carries an exact affine update on a finite CRT state
   (moduli allowed to be general positive integers, not only powers of two);
3. the accepted infinite language contains at least one aperiodic word
   (`L-0103` compliance);
4. a single ordinary positive integer seed realizes one accepted infinite run;
5. a height function \(h\) tends to infinity along that run.

Such an object would be a Collatz counterexample certificate in the sense of
`D-0102`.

## Motivation

After `L-0101`–`L-0104`, the surviving geometric hope is not compact IFS
ping-pong on \(\mathbb{R}_{>0}\) or \(t=1/x\), nor periodic two-port block
cycles, but an aperiodic automaton with precision accounting.

## Proof or construction

None. Speculative.

## Dependency audit

- Format: `D-0102`.
- Negative constraints: `L-0101`–`L-0104`.

## Gap audit

- May be false. The precision-drain phenomenon of `L-0104` may be universal
  (`C-0102`), in which case `C-0101` fails unless a precision-regeneration
  edge type exists.
- Even if \(\mathcal{A}\) exists abstractly, exhibiting the seed may be as hard
  as Collatz.

## Adversarial tests

Attempts so far: `X-0102`–`X-0107` (all negative for infinite certificates).

## Remaining uncertainty

Very high — this is an organizing conjecture for the packet, not evidence.

## Suggested next attack

Decide `C-0102` first. If precision drain is universal for pure odd-multiplier
port transitions, redesign edges to include explicit precision-regeneration
gadgets (possibly importing collision-fiber geometry-growing ideas without
merging that packet’s ledgers).
