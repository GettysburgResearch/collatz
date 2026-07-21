# Generalized Collatz undecidability and automated rewriting

## Generalized-map undecidability

Conway's “unpredictable iterations” introduced generalized piecewise-affine integer maps capable of universal computation. Kurtz and Simon give a modern undecidability theorem for a generalized Collatz problem and document the Conway provenance. [@Conway1972; @KurtzSimon2007]

This is not an undecidability theorem for the single standard `3x+1` map. It shows that broad syntactic classes containing Collatz-like maps can encode undecidable behavior.

## Exact binary–ternary computation inside the standard map

Stérin and Woods define a quasi-cellular automaton that exactly simulates standard Collatz evolution and prove that its binary/ternary geometry embeds a base-3-to-base-2 conversion algorithm. Their finite-state-transducer viewpoint is a direct predecessor for mixed-radix carry analysis, but it does not provide nontermination or finite-boundary closure. [@SterinWoods2020]

## Exact standard-map rewriting

Yolcu, Aaronson, and Heule construct a mixed binary–ternary string-rewrite system and prove that its termination is equivalent to the standard Collatz conjecture. They also obtain automated termination certificates for proper subsystems while the full system remains unresolved. [@YolcuAaronsonHeule2023]

This is the exact external baseline for `TERM/...` and a useful comparison for the collision-rewrite branches:

- AYH studies global termination of one exact rewrite presentation.
- PR #3 and issue #4 seek nontermination/regeneration certificates in induced expanding subsystems.
- A finite rewrite pattern is not enough unless it corresponds to one ordinary integer and closes forever.

## Citation correction

The verified citation has authors **Emre Yolcu, Scott Aaronson, and Marijn J. H. Heule**. “Aaronson–Yolcu” alone is incomplete attribution.
