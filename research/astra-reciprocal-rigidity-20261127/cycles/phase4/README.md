# Arithmetic statistics of full cycle denominators

The binary theorem proves a total-variation approximation by the complete divisor law \(e\mapsto\varphi(e)/|2^n-3^u|\) on each exact-weight stratum whose odd frequency stays away from zero and one. It includes primitive necklaces and gives a stretched-exponential uniform additive error. A large cancellation of any fixed positive fraction of the length has exponentially small probability. The ordinary cycle condition corresponds to the individual divisor \(e=1\), whose model probability can be exponentially smaller than the error. [Binary theorem and scope](DENOMINATOR_LAW.md)

The block theorem gives a coset correction for every fixed finite dictionary and arbitrary macroscopic exact multiplicities. It includes the critical positive-entropy \(\{2,12\}\) exponent family, explains the deterministic case of commuting blocks and gives an infinite family with 7 forced into every gcd. [Block dictionaries](BLOCK_ALPHABETS.md)

The probability estimates and the sieve are written mathematics. Lean 4.34.1 checks the integer frequency-escape lemma used for the binary theorem. The printed axiom inventories for all three public declarations contain only \(\mathtt{propext}\) and \(\mathtt{Quot.sound}\). The module imports mathlib at commit \(\mathtt{d13f23b723b8a846827a245b89c10fc7d3f11612}\). [PairFrequency.lean](PairFrequency.lean)

## Replaying the finite controls

From this directory run both programs under Python 3. They have no third-party dependencies. Running them again with optimization checks that the validation routines stay active.

~~~sh
python -B check_law.py
python -OB check_law.py
python -B check_blocks.py
python -OB check_blocks.py
~~~

The binary program checks 26,400 nonzero starting frequencies, 1,336 small-representative transitions, 594 conditional orientation laws and 45,228 burst-recovery cases. It computes exact divisor histograms, checks the finite inclusion–exclusion remainder, and obtains exact marginal counts through the slice with \(n=200,\ u=126,\ g=77\). [Binary controls](check_law.py)

The block program checks 900 ordered commutator and commuting-word tests, entire strata covering a forced prime, deterministic commuting words and nonunique binary representations. Exact dynamic programming on three larger macro slices checks both the uncorrected law and support on a strict coset. The finite samples illustrate the proved bounds. [Block controls](check_blocks.py)
