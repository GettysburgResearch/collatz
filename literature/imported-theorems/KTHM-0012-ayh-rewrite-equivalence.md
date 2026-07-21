# KTHM-0012 — Yolcu–Aaronson–Heule rewrite equivalence

**Source:** Yolcu, Aaronson, and Heule, abstract and main reduction in the open-access article. [@YolcuAaronsonHeule2023]  
**Proof status:** black-box import  
**Maps to:** `TERM/...`; methodological comparison for `PR3/Q-0007`

## Statement

Yolcu, Aaronson, and Heule construct a finite mixed binary–ternary string-rewrite system that simulates iterated application of the standard Collatz function on encodings of positive integers. They prove:

\[
\text{the rewrite system terminates on all encoded positive integers}
\quad\Longleftrightarrow\quad
\text{the Collatz conjecture is true}.
\]

They also automate termination proofs for nontrivial weakened subsystems, while the full system remains unresolved.

## Scope limitations

- Termination of proper subsystems is not termination of the full system.
- Failure of one interpretation or prover is not evidence of nontermination.
- The theorem does not supply a counterexample or a finite nontermination certificate.
- Repository ports must preserve the exact eleven rules and encoding conventions before depending on the equivalence.
