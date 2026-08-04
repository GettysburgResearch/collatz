# Regular sanctuaries and finite-state safety

## Repo object

A regular sanctuary is a nonempty canonical binary language, excluding the trivial cycle, whose represented positive integers are closed under the shortcut Collatz map. PR #12 supplies a finite subsequential transducer for one shortcut step and an exact certificate checker.

## Standard infrastructure

- subsequential/rational transductions preserve regular languages (`LIT-KTHM-0019`);
- fixed-language closure is decidable by product reachability (`LIT-KTHM-0020`);
- the largest safe accepting subset for a fixed skeleton is a greatest fixed point (`LIT-KTHM-0021`);
- a `q`-state DFA accepting a canonical positive word accepts one of length at most `q` (`LIT-KTHM-0022`).

Caucal–Rispal and Shallit–Wilson confirm that transducer/automata viewpoints around Collatz are established. They do not construct a sanctuary.

## Native burden

The difficult step is synthesis of an invariant transition skeleton under exact finite-word semantics. Carry flushes, leading-zero normalization, undefined terminal outputs, and the exclusion of `{1,2}` are mathematical, not software details.

## Search methods suggested by the literature boundary

- symbolic or antichain reachability for product relations;
- SAT/CEGIS over a frozen unlabeled DFA skeleton;
- automata learning from deep finite-horizon safe sets followed by exact inductiveness checks;
- safety-game fixed points for finite phase covers;
- proof-producing minimization and globally shortest counterexample words.

## Cautions

A finite external verification frontier may prune state sizes but must not enter certificate soundness. Failure in a bounded DFA family is a negative result about that family, not evidence that every orbit converges.