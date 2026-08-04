# Termination-frontier literature map

**Namespace:** `TERM/...` for draft PR #6.

## Verified external root

Yolcu, Aaronson, and Heule's article is real and directly relevant. It introduces a mixed binary–ternary string-rewriting formulation whose termination is equivalent to the standard Collatz conjecture, studies termination orders, and obtains automated proofs for nontrivial weakened systems. This is **KNOWN — EXACT** background for the packet's imported eleven-rule system.

## Generalized undecidability boundary

Conway's generalized iteration work and Kurtz–Simon prove undecidability / `Π^0_2`-completeness for generalized Collatz families. This is **KNOWN — EXACT** for the generalized problem and **NOT APPLICABLE** as a proof that ordinary `3x+1` is undecidable.

## Native packet claims

- `TERM/L-9001` and `TERM/R-9001` are repository arguments, not claims imported from Yolcu–Aaronson–Heule.
- `TERM/Q-9001` and `TERM/Q-9002` are open interfaces for stronger termination orders.
- The packet's provenance boundary is literature-correct: unavailable previous artifacts must not be cited as admitted proofs.

## Strategic connection to the collision program

The AYH system and the collision-fiber system are two different exact encodings:

- AYH asks for global termination of a finite rewrite relation equivalent to standard Collatz;
- collision fibers construct partial expanding radix maps and seek one infinite admissible finite boundary.

A useful future bridge would map native collision macro-tiles into certified derivation fragments of the AYH system. Such a bridge could reuse termination tooling without claiming that a termination order exists. No such theorem was located or proved in this wave.
