# Positive-entropy avoidance and large determinant divisors

The finite shell bounds cover whole collections of positive ordinary cycles. At the published verification floor, the sum of logarithmic defects of all hypothetical nontrivial dimer cycles is below \(2^{-44}\). The three other open mod-8 avoidance classes have analogous all-period sums below \(2^{-17}\), \(2^{-26}\) and \(2^{-12}\) for avoidance of 1, 5 and 7, respectively. A positive individual defect may be arbitrarily small. [Dimer reciprocal mass](DIMER_MASS.md) · [All four explicit budgets](AVOIDANCE_BUDGETS.md)

At any location, an interval of length \(X\) contains \(O(X^{0.3208518\ldots}/\sqrt{\log X})\) odd points whose full forward trajectory avoids both 5 and 7 modulo 8. For a two-sided ordinary trajectory avoiding 5, the exponent is \(0.6177244\ldots\). This includes every avoid-5 cycle. The one-sided and two-sided hypotheses are different. A source-qualified consequence shows that along hypothetical dimer cycles of growing period, a proportion tending to one of the odd states exceeds the minimum by a growing power of the period. [Initial intervals and height consequences](AVOIDER_COUNTS.md) · [Uniform-location proof](INTERVAL_COUNTS.md)

An independent canonical-cut argument bounds the count of rooted parity words whose numerator is divisible by any specified large divisor of the complete determinant. At critical density the exponent on the varying reduced-denominator allowance is \(0.94995\ldots\) for binary words and \(0.3208518\ldots\) for dimer compositions. The bounds include polynomial factors in word length. [Large-divisor list bounds](DIVISOR_TAIL.md)

## Verification

The written arguments carry the global counting, Diophantine and convergence-verification inputs. Lean 4.34.1 checks the list of dimer histories at each odd count, the complete-block and factor-mass formulas, the algebraic tail difference, and the numerical floor and defect comparison. Six printed axiom inventories use only standard Lean axioms. The kernel replay uses mathlib commit \(\mathtt{d13f23b723b8a846827a245b89c10fc7d3f11612}\). [DimerMass.lean](DimerMass.lean)

Run the finite controls from this directory using standard Python 3.

~~~sh
python -B check_dimer.py
python -OB check_dimer.py
python -B check_entropy_tail.py
python -OB check_entropy_tail.py
~~~

The first program enumerates 8,358 factors through 16 odd bits, 187,742 valid fixed-physical-time inversions, 2,046 inverse ternary histories and translated intervals centered as high as \(10^{30}\). It checks the four strict cutoff budgets using exact integers and fractions. The second checks 18,722 canonical binary words and 2,211 dimer arrangements, including every full-determinant divisor in 79 strata. [Dimer and avoidance controls](check_dimer.py) · [Canonical-cut controls](check_entropy_tail.py)
