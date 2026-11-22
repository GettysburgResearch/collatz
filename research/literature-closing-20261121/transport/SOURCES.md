# Primary sources for the return-transport attempt

These are literature hypotheses used to design the new attempt. They are not
imported Lean axioms and are not claims that a Collatz closure has been proved.

## Tao: the precise first-passage transport domain

Terence Tao, *Almost all orbits of the Collatz map attain almost bounded
values*, Forum of Mathematics, Pi **10** (2022), e12,
[publisher text](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F),
[arXiv:1909.03562](https://arxiv.org/abs/1909.03562).

Proposition 1.11 fixes \(\alpha=1.001\). Its input \(\mathbf N_y\) is
logarithmically uniform on positive odd integers in \([y,y^\alpha]\).
For sufficiently large \(x\), non-passage to \([1,x]\) has probability
\(O(x^{-c})\) for \(y=x^\alpha,x^{\alpha^2}\), and the two passage
location laws differ in total variation by \(O((\log x)^{-c})\).
The constants are absolute. A failed passage is artificially assigned
location one, so the separate non-passage estimate must be retained.
Theorem 3.1 bounds the logarithmic density of sources whose minimum exceeds
\(N_0\) by \(O((\log N_0)^{-c})\). Neither statement is a bound for an
arbitrary fixed atomic source law under indefinitely repeated induced returns.

## Assani: what finite positive atomic recurrence actually requires

Idris Assani, *Collatz map as a non-singular transformation*,
[arXiv:2208.11675v3](https://arxiv.org/pdf/2208.11675),
13 December 2023; published in Studia Mathematica **275** (2024),
[publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/275/3/115387/collatz-map-as-a-non-singular-transformation).

Definition 2.5 requires one finite constant \(M\) with
\(\alpha(T^{-j}A)\le M\alpha(A)\) for every \(j\) and measurable
\(A\). On the positive integers, equivalence to counting measure means
\(\alpha(n)>0\) at every integer. Theorem 4.2 makes existence of a finite
such measure equivalent to boundedness of every trajectory. Theorem 4.1
additionally specifies conservative part \(\{1,2\}\) for equivalence to
the full shortcut Collatz conjecture. The finite invariant measure in
Theorem 3.3 need not have positive mass at every source; it is a different
statement.

The related primary preprint by Assani, Ebbighausen and Hande,
[*Syracuse Maps as Non-singular Power-Bounded Transformations and Their
Inverse Maps*](https://arxiv.org/pdf/2208.11801), contains the general
distinct-atom contradiction in the proof of Theorem 3. Its converse constructs
a measure from the cycle basins. The new argument in RETURN_TRANSPORT.md
retains the same elementary atomic mechanism and adds a quantitative fourth
logarithmic moment budget; it does not invoke the converse construction.

## Meyn--Tweedie: the missing recurrence set is not supplied by forced access

Sean P. Meyn and R. L. Tweedie, *Stability of Markovian processes I:
criteria for discrete-time chains*, Advances in Applied Probability **24**
(1992), 542--574,
[publisher record](https://www.cambridge.org/core/journals/advances-in-applied-probability/article/abs/stability-of-markovian-processes-i-criteria-for-discretetime-chains/8CDC0026BA40C60C5393F21884FF7F68),
[author-hosted paper](https://meyn.ece.ufl.edu/wp-content/uploads/sites/77/archive/spm_files/Papers_pdf/meytwe92a.pdf).

Theorem 4.1(i) characterizes Harris recurrence by existence of a petite set
\(A\) hit almost surely from every state. Part (ii) adds a uniform finite
expected return time on \(A\) for positive Harris recurrence. A petite set
has a common nonzero minorizing measure for a sampled transition kernel.
The forced dyadic band is an accessible set; no such minorization is given.
The deterministic specialization in RETURN_TRANSPORT.md proves directly why
assuming this minorization on the entire band would already force a uniform
return-index bound to one. No irreducibility, minorization, or drift hypothesis
is silently supplied.

## A recent Archimedean variation, used only for its affine identity

Maxwell Siegel and Rory O'Dwyer, *Almost-Boundedness of Collatz-Type Maps on
Number Rings via Archimedean Methods*,
[arXiv:2609.33018v1](https://arxiv.org/abs/2609.33018), 26 September 2026.
The parent task retrieved and extracted the 63-page primary PDF. This is an
unreviewed preprint in this packet. Section 7.2, equations (7.108)--(7.109),
rewrites the orbit equation as Archimedean closeness to the affine offset.
The calculation T13 uses only the elementary exact affine orbit equation,
which is derived independently there. No main theorem, lattice estimate,
distributional approximation, or full-Collatz inference from this preprint
is imported.
