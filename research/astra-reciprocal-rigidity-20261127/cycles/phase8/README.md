# Lower bounds for every rational cycle at almost every period

The final [joint denominator census](FAREY_CENSUS.md) improves the exponent
to `1/(2 H₂(log₃ 2)) = 0.5263404293…` and includes the factor
`(1+log n)^(11/38)`. It counts all reduced denominators together using
native parity separation and the entire high excursion. Its uniform
all-prefix ballot estimate is proved in [ENDPOINT_CENSUS.md](ENDPOINT_CENSUS.md).
Both files are written proofs with independent root and rigidity reviews.
The exceptional period set can still contain an ordinary integer cycle.

## Earlier ascent census

For a density-one set of physical least periods \(n\), **every** nonzero signed rational shortcut cycle of that period has full reduced denominator exceeding \(n^{20/39}\). More generally the conclusion holds for each fixed exponent below \(1/(1+H_2(\log_3 2))=0.5128322087\ldots\). All word shapes and both signs are covered. Positive rational cycles of every period \(n\ge2\) exist. The exceptional set of periods can still contain an individual ordinary nontrivial cycle. [Ascent and charge census](ASCENT_CENSUS.md)

The proof splits true cycles according to their real minimum. On every high-minimum cycle a rational future-minimum construction assigns its gap to phases whose forward words have high odd counts at **every** horizon. Each low-minimum cycle of large least period and limited denominator supplies a bounded-height witness just before an ascent lasting at least a logarithmic number of steps. The resulting large-gap count includes multiplicities. The small-gap argument counts possible period values by irrational equidistribution. These steps use neither a quantitative irrationality estimate nor any finite convergence-verification floor.

* [The denominator-uniform census](DENOMINATOR_CENSUS.md) bounds fractional moments of full cycle gaps at each prescribed denominator, and counts distinct slopes or period vectors when the allowed denominator grows. It also gives a linear denominator lower bound whenever the mean odd count stays a fixed distance from its critical value.
* [The independent shrinking-floor proof](SHRINKING_FLOOR.md) treats fair affine parity words at real heights tending to zero. Its survival bound is uniform in the floor, and it supplies a near-square-root period bound by a separate argument. Its density-one denominator exponents are weaker than the main ascent result.

The Lean 4.34.1 module proves that the actual finite cyclic charge is nonnegative and that its positive values force every forward partial sum to be positive. It also checks periodic-potential summation and the complete rational majorant-to-Gronwall comparison. The five printed dependencies use only the standard Lean axioms. The entropy, crossing, asymptotic census and density-one conclusion remain written mathematics. [RationalCycleCharges.lean](RationalCycleCharges.lean)

## Verification

Run both commands from this directory.

~~~sh
python -B check_denominators.py
python -OB check_denominators.py
~~~

The exact checker traces all 411 ordered-necklace representatives of nonzero primitive signed rational cycles through length eleven, including 314 positive and 97 negative cycles. It verifies 203 active rational phase charges, 3,940 prefix inequalities across two laps and 324 last-ascent witnesses, and checks the finite scalar margins from the shrinking-floor proof. The density-one theorems are written arguments, not consequences of this enumeration. [check_denominators.py](check_denominators.py)
