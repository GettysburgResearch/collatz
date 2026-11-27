# Two arrival clocks in short intervals

[SHORT_WINDOW_CLOCKS.md](SHORT_WINDOW_CLOCKS.md) gives a written total-variation estimate for every ordinary first-landing row and both clock residues in a shrinking interval. For high moving barriers it proves a matching complete obstruction above the continued-fraction scale. It also gives a growing-block corollary at fixed ordinary targets of positive predecessor density. Neither conclusion specifies the final fate of an arbitrary start.

[ClockResidues.lean](ClockResidues.lean) verifies the unimodular coordinate change and the exact cardinality of every row window over a finite commutative ring, given its Bézout identity. Its three axiom inventories use only the standard Lean axioms. The analytic passage theorem is written.

[short_window_controls.py](short_window_controls.py) checks actual shortcut and ordinary first hits, exact accumulated correction bounds, modular fiber counts, and vertical-class rotation grids using rational arithmetic. [SHORT_WINDOW_CONTROLS.json](SHORT_WINDOW_CONTROLS.json) records its output. Run both Python modes and compare their exact outputs with that file. The finite controls test arithmetic instances. They do not establish an asymptotic law or sample every ordinary trajectory.
