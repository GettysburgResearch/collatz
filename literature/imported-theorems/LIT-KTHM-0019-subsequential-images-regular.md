# LIT-KTHM-0019 — Subsequential transducers preserve regularity

**Verdict:** `KNOWN — EXACT`; constructive proof supplied.  
**Maps to:** `REG/L-9101` and `REG/L-9105` in PR #12.  
**Literature context:** standard rational-transduction theory; Caucal–Rispal provide a modern Collatz-adjacent synchronized-transducer treatment.

## Theorem

Let \(F\) be a deterministic subsequential transducer: each input transition emits a finite output word, and each accepting terminal state has a finite final output. If \(L\) is regular, then \(F(L)\) is regular. An automaton for the image is effectively constructible.

## Proof

Take a DFA for \(L\) and form its product with the finite control of \(F\). Each product transition carries the finite output word emitted by the transducer. Replace an edge labelled by a word \(y_1\cdots y_m\) by a path of \(m\) fresh edges labelled \(y_1,\ldots,y_m\); an empty output becomes an epsilon edge. Append the terminal-output paths at accepting endpoints. The resulting finite epsilon-NFA accepts exactly the transducer outputs of words in \(L\). Epsilon elimination or the subset construction gives a finite automaton. ∎

## Boundary

The theorem proves regularity of an image. It does not prove that a proposed language is nonempty, canonical, avoids the trivial cycle, or is forward invariant. Undefined terminal outputs and noncanonical flushed outputs must be treated explicitly, as PR #12 does.