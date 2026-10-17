# LIT-KTHM-0022 — Short accepted canonical word bound

**Verdict:** `FOLKLORE / STANDARD`; complete proof supplied.  
**Maps to:** `REG/L-9104` and the conditional state floor in PR #12.

Let a complete DFA have \(q\) states and read binary words least-significant digit first. Call a nonempty word canonical positive when its last symbol is `1`.

## Theorem

If the DFA accepts any canonical positive word, it accepts one of length at most \(q\).

## Proof

Choose an accepted canonical word \(v1\), separating its final `1`. Let \(p\) be the state reached after reading \(v\). In the directed transition graph, a shortest word \(u\) from the initial state to \(p\) has length at most \(q-1\): a longer shortest path would repeat a state and could be shortened. Then \(u1\) reaches the same accepting endpoint as \(v1\), remains canonical, and has length at most \(q\). ∎

## Computational-frontier corollary

If every positive integer represented by at most \(B\) binary digits has been rigorously verified to enter the trivial cycle, then a regular sanctuary under these exact semantics needs more than \(B\) raw DFA states. This is search pruning, not part of the certificate's soundness.

## Boundary

The numerical corollary must quote the external verification range with exact strict/weak inequalities. It does not imply that a sanctuary exists at the next state size.