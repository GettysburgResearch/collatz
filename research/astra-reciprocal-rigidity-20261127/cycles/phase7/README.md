# Global period sparsity and finite-state parity languages

* [The period census](PERIOD_CENSUS.md) proves that the positive gaps of all ordinary cycles have convergent fractional moments, and bounds their distinct reduced slopes, periods of bounded content, unrestricted period vectors and cycle multiplicities with separate hypotheses. The unrestricted elementary argument, the external Subspace Theorem strengthening and the classical and recent irrationality inputs are identified individually. At every cutoff, at most one rational ray prevents the strongest bound from applying to all vectors. No symbolic-height restriction or computational floor is needed.
* [Finite-state counting](FINITE_STATE.md) gives a strict saving from the critical entropy per bit for any primitive right-resolving graph with a positively tilted critical Markov law. The counting theorem requires forward invariance and bounded fixed-time multiplicity. [The two applications](AVOIDANCE_LANGUAGES.md) cover every state on the union of cycles avoiding 1 or 7 modulo 8, and every individual divergent orbit in either language.
* [The joint inverse mask](REVERSE_MASK.md) separates the actual canonical integer source modulo a ternary power and in a real arc at once. The exact dimer predecessor mask gives an alternative strict count for bi-infinite integer points at the original forward time horizon.
* [The iteration limits](BOOTSTRAP.md) quantify the distinction between a sparse ordinary survivor set and a symbolic bridge prior, show that subsequent local inverse masks are inherited, and prove a square-root support-size lower bound on the specific Fourier–Hölder upper certificate. Sharper affine offset bounds enlarge the arithmetic horizon but do not cancel that statistical loss.

All results on this page are written proofs. This packet uses the previously checked phase-6 signed-moment input for the dimer specialization. The general finite-state theorem supplies its own qualitative proof. These counts leave global convergence, individual nontrivial cycles and infinite ordinary dimer survival unresolved.

## Finite controls

Run from this directory with Python 3.9 or later.

~~~sh
python -B check_census.py
python -OB check_census.py
~~~

The checker reconstructs the finite backward masks through depth eleven, raw integral carries and canonical prefix residues for 504 dimer paths, 1,118 Markov cylinder identities and 270 lattice strips. It uses exact rational slopes and weights in these checks. The tests provide independent finite examples of the identities; asymptotic constants and external number-theoretic inputs retain their written-proof scope. [check_census.py](check_census.py)
