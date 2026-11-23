# Independent selector and symbolic-family review

**Verdict: VERIFIED for the stated selector theorem and written G3–G4
classification.** The lead researcher independently reconstructed the
argument, read all eleven public Lean declarations, and checked their
interpretation against the written note. The G4 certified subfamily was
suggested by the lead and then independently derived and written by the
merger researcher; that provenance is separate from the independent
review of the original selector implementation.

| Reviewed file | SHA256 |
|---|---|
| `research/global-synthesis-20261122/GLOBAL_MERGERS.md` | `5349c6c4fa33c356340b1da3746b86abf68c0ea643d4d965b02d272610fa7633` |
| `lean/QuantitativeInverseSelector.lean` in that packet | `132f0cd8318e20271456a4f776a90621407bc0a69dce805382b5860a08a13048` |
| `inverse_alphabet_selector.py` in that packet | `605f3b6d896836cfe1ec8601fab9006ba94ee0b0b4120b145d33d844ac69db24` |

## Selector semantics

The ordinary map and clock are the frozen `CollatzShell` definitions.
The six residue rows provide positive odd unit predecessors greater than
one and exact gaps in one through four. Every intermediate shortcut value
before a gap endpoint is different from one. Therefore the least hitting
time of one strictly increases along the inverse chain **when its root has
the supplied complete certificate**. Supplied certificate padding is not
mistaken for a least hitting time.

Distinctness of the selected vertices gives a first crossing within the
number of odd unit states at most `N`. At that first crossing the previous
vertex is at most `N`; the exact gap equation gives `3p+1<=16N`, hence
`3p<16N`. Prefix construction and concatenation retain the supplied tail
literally. The depth and ordinary shortcut-clock bounds count precisely
these newly inserted letters.

The strongest theorem assumes `GapPath q tail 1`, `q%3!=0`, and `q<=N`.
It returns a certified predecessor; it does not prove convergence of an
arbitrary wanted target in an interval below that predecessor. One
development doc comment was clarified to make this explicit. No proof
statement changed. The final-byte compiler run is recorded separately.

## Symbolic alphabet-three graphs

For `q0=1+3^h u` with the stated conditions, an integral exponent in
`1..3` is forced to be two until the displayed valuation block is
exhausted. The terminal residue is zero modulo three and has no odd
predecessor. This proves that the chain is the **entire** graph and that
its last value is its exact maximum, without assuming convergence.

For `k=1+2*3^h`, the source `(4^k-1)/3` has the actual one-gap tail `2k`
to one. The displayed recurrence for
`4^(3^h)=1+3^(h+1)v_h` preserves `v_h=1 mod3` and gives
`u=4v_h(4^(3^h)+1)=2 mod3`. Thus the finite-chain family contains growing
fully certified roots with every prescribed depth. This rules out the
universal cofinal **odd alphabet-three prefix** strategy, not every
certificate rewrite or the selected residual alphabet-four strategy.

The executable closed-graph controls distinguish a finite closed tree from
an unfinished search. They explicitly replay every legal predecessor edge
and check acyclic depth consistency. Normal and optimized runs, exact data,
and source hashes belong to the separate execution receipt. Finite examples
are not used to prove the arbitrary-root claim.

The inherited inverse table, high-grade rank payment, and upstream open
selector interfaces remain credited to their frozen PR sources. This
review does not independently replay the entire upstream projects or
establish their global missing hypotheses. G3–G4 are written arithmetic,
outside the eleven formal selector statements.
