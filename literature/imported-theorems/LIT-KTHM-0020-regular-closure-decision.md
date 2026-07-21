# LIT-KTHM-0020 — Exact closure decision for a fixed regular language

**Verdict:** `KNOWN — COROLLARY`; complete proof supplied.  
**Maps to:** `REG/L-9102` in PR #12.

## Theorem

Given a DFA \(D\), a subsequential transducer \(F\), and a regular semantic domain \(C\), it is decidable whether

\[
F(L(D)\cap C)\subseteq L(D)\cap C.
\]

If inclusion fails, a finite counterexample input word can be reconstructed.

## Proof

By `LIT-KTHM-0019`, the image \(I=F(L(D)\cap C)\) is regular and effectively constructible. The target \(L(D)\cap C\) is regular; so is its complement. Inclusion holds exactly when

\[
I\cap\overline{L(D)\cap C}=\varnothing.
\]

Emptiness of a finite automaton is finite graph reachability. If an accepting state is reachable, predecessor pointers reconstruct an output witness; retaining input labels in the product transducer reconstructs a corresponding input. ∎

## Boundary

This is decidability for one fixed certificate. It says nothing about the unrestricted existence of some DFA of arbitrary size. Canonical endpoint semantics and terminal-output failures are part of the domain definition and may not be silently dropped.