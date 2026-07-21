# KTHM-0014 — Stérin–Woods base-conversion embedding

**Source:** Stérin and Woods, Theorem 16 and the surrounding simulation lemmas. [@SterinWoods2020]  
**Proof status:** black-box import  
**Maps to:** mixed-radix/carry context for `PR3/...`, `CLAUDE/...`, and `TERM/...`

## Statement

Stérin and Woods define a two-dimensional quasi-cellular automaton whose horizontal rows exactly simulate shortcut-Collatz evolution in base `2`, while vertical columns simultaneously express the evolution in base `3`. Their main theorem states that this automaton embeds an algorithm converting every natural number from base `3` to base `2`, using `Θ(log x)` Collatz iterations on input `x`.

The same framework gives finite-state-transducer descriptions of the local `3x+1` and `x/2` operations and reformulates the cyclic Collatz problem on rational `2`-adic inputs as a reachability problem.

## Repository relevance

This is the closest located predecessor for treating ordinary Collatz evolution as an exact interaction between binary and ternary digit systems. It provides a genuine algorithmic/carry interface for the collision-radix and rewrite branches.

## Scope limitations

- The theorem is a base-conversion embedding, not a collision-fiber conjugacy or finite-boundary regeneration theorem.
- A quasi-cellular automaton simulation does not yield an infinite ordinary-integer orbit.
- Its reachability formulation of cycles is not a proof that a nontrivial cycle exists.
- Any local transducer or carry identity imported into this repository still needs an explicit notation/rule crosswalk.
