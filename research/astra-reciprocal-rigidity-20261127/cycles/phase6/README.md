# Strict entropy savings for two positive-entropy avoidance classes

There is a uniform bound for the number of ordinary odd points in every interval of length \(X\),
\[
  O\!\left(X^{h_D-10^{-12}}\right)\quad\hbox{for forward dimer survivors},
 \qquad O\!\left(X^{h_5-10^{-12}}\right)\quad\hbox{for bi-infinite avoid-5 states}.
\]
Here \(h_D=0.3208518\ldots\) and \(h_5=0.6177244\ldots\) are the critical symbolic entropy exponents. The forward set avoids 5 and 7 modulo 8, and includes any nonperiodic as well as cyclic forward survivor. The avoid-5 estimate requires an ordinary backward history of all lengths in addition to the forward history. The Subspace Theorem makes the thresholds ineffective. Isolated ordinary cycles and trajectories remain possible. [Forward survivor proof](STRICT_DIMER_SAVING.md) · [Bi-infinite survivor proof](STRICT_REVERSE_SAVING.md)

The numerator estimate uses independent copies of a finite-state word source. At sites with enough fresh binary decisions, the next low bit of a signed sum is nearly fair. The dimer source has deterministic transitions, so the proof also counts the chance of too few active copies. At a small positive fraction of physical precision this gives concentration for the actual canonical source or endpoint residue after the standard fixed-place separation argument. [Markov numerator moments](MARKOV_MOMENTS.md) · [Canonical source circle](CANONICAL_ARCS.md)

The fixed exponent \(10^{-12}\) follows using fourth moments, rational finite-state potentials and conservative explicit parameter margins. Weaver 28 v3 and 73 supplied the separation and moment-to-ordinary-count method for the unrestricted geometric law; the finite-state inputs and the two restricted ordinary-point counts are the applications here. [Explicit gain and provenance](EXPLICIT_GAIN.md) · [Weaver 73](https://rstation.ai/problems/collatz/papers/73)

Lean 4.34.1 checks both fourth-moment potential tables and both potential ranges with no axioms. The probability argument, Subspace Theorem input and asymptotic induction remain written mathematics. [MarkovCertificate.lean](MarkovCertificate.lean)

From this directory the following standard-library replay checks all 40 parity rows, the rational logarithmic and entropy enclosures, the common numerical gain and 1,024 exact reconstructions of both canonical circles from separated chunks.

~~~sh
python -B check_markov.py
python -OB check_markov.py
~~~

[Exact arithmetic replay](check_markov.py)
