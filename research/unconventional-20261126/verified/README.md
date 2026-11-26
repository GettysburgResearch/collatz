# Rebuilding the two previously uncompiled closing interfaces

These files preserve the statements of two candidates at PR200 head
`8e6add443b13acbcfd553676898c120183f07377`. The original files remain untouched:

* `research/regularity-rigidity-20261124/minimum-closure/MinimumClosure.lean`;
* `research/regularity-rigidity-20261124/global-trace-20261125/FinalProposal.lean`.

The copies here use narrow imports supported by the available pinned Mathlib
cache. Importing all of Mathlib failed because that cache lacks some unrelated
dependencies. There were also proof errors, not just missing dependencies.
`MinimumClosure.lean` needed a valid forward-iteration proof for `Good`, an
updated power inequality invocation, and an explicit ring calculation for the
relative carry identity. `TraceProposal.lean` needed the correct implication
for cancelling a positive right factor from an inequality. Every local
theorem has a transitive axiom audit in the new replay.

The six minimum-closure statements and the five trace-proposal statements have
not been strengthened. In particular `collatz_of_minimum_and_descent` still
requires the universal smaller merging witness, and `final_proposal` still
requires exclusion of escapes and of nontrivial ordinary cycles. Compiling
these consumers proves that the listed hypotheses imply the conclusion; it
does not supply those hypotheses.

The replay receipt identifies the exact source hashes, Lean/Mathlib versions,
strict command flags and accepted transitive axioms. The seven earlier
regularity-rigidity modules were also independently rebuilt before this pass:
their 46 audited theorem reports exactly matched the previous receipt. Those
baseline results are separate from the new modules and from the written
operator and Diophantine proofs.
