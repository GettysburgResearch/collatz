# Independent reconstruction of the collision criterion and sparse sampling

**VERIFIED WITH SOURCE QUALIFICATIONS at the pins below.** This review reconstructs the new deductions from their stated analytic inputs. It does not certify the external Collatz papers, prove the missing collision lower bound, or extend a verdict to later source revisions.

The review was carried out independently of the coordinating proof author. The substantive conclusions are that the earlier \(1/8\) criterion has no missing finite-period or moving-deadline step in the inspected argument, and that the new one-sided semiprime transfer correctly pays for failure relative to the sparse population. The latter payment is the decisive improvement over an unweighted union bound.

## Frozen objects and source scope

| Object | Exact boundary inspected |
|---|---|
| Earlier ordinary collision theorem | [PR 214, head `504d29d399efa941a62006d1ea4635385ce6bb5f`, `ordinary/SYNCHRONOUS_PHASE_DISPERSION.md`](https://github.com/GettysburgResearch/collatz/blob/504d29d399efa941a62006d1ea4635385ce6bb5f/research/astra-critical-rigidity-20261128/ordinary/SYNCHRONOUS_PHASE_DISPERSION.md); SHA-256 `bd9da43d81cc04abe9ced69692eeeb67ddbb72611606ae14006ced3c2642d70b` |
| Semiprime sufficient family | [PR 217, head `a2d3f9c44c798c1956d29f88d12ccb2904cb0eb4`, `SEMIPRIME_SUFFICIENCY.md`](https://github.com/GettysburgResearch/collatz/blob/a2d3f9c44c798c1956d29f88d12ccb2904cb0eb4/research/astra-collision-factor-bridge-20261128/SEMIPRIME_SUFFICIENCY.md); SHA-256 `c2e7f74f7fb4e49836e898b746e41dc66a3a7e103af553cffbf553e675fd6e63` |
| Leen pair source | Original TeX at [Zenodo 23268751](https://doi.org/10.5281/zenodo.23268751), SHA-256 `d2f961635d339a4b215c82b1f2f8b9ca53143043f4c58b9aa67290f46056996e`; the exact-cylinder, balanced-shortcut dictionary and uniform-absorption theorem statements and their displayed derivations were read |
| Leen minimum/clock source | Original TeX at [Zenodo 23269488](https://doi.org/10.5281/zenodo.23269488), SHA-256 `211bc4fe107b3821e510486be28cf53f69751f71394582822faf385d09561e37`; the minimum-law, terminal-data, arithmetic-progression and dependency statements were read |
| Semiprime supply | Matomäki–Teräväinen, [*Almost primes in almost all short intervals II*, arXiv:2207.05038v2](https://arxiv.org/pdf/2207.05038v2), Theorem 1.1, read in the original PDF |
| Existing critical-moment comparison | [PR 215, head `4f33ecc2de6f0ccf605a68c28da5abea0348e47b`, `TILTED_ORDINARY_REPRESENTATIVE.md`](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/escape/phase8/TILTED_ORDINARY_REPRESENTATIVE.md), read as a separate prior route, not imported into the semiprime proof |

The positive-predecessor premise remains the named external Mazur theorem. Its role and map conversion were checked; a fresh rebuild of its development is not claimed. The fixed-target and minimum laws are also external written inputs. Leen's source expressly distinguishes its written arguments, reported formal cross-checks, and results not claimed.

## 1. The genuine phase quotient

For the shortcut map \(T\), define \(x\sim y\) when the two values coincide at some common date. This is transitive: extend two witnessing dates to their maximum. The quotient shift \(S[x]=[Tx]\) is injective because a merger after one more step was already a merger, and surjective because \(T(2x)=x\). Thus its orbits are the ordinary asynchronous components, with no completion or stochastic replacement.

A finite shift orbit of least length \(P\) gives an actual return \(T^{t+P}x=T^t x\). Conversely a true least-period \(P\) cycle has exactly \(P\) distinct phases. The argument therefore does not turn a finite quotient into an ordinary periodic orbit without a witness. There are only finitely many cycles of bounded period: each finite parity word has affine slope \(3^g/2^t\ne1\) and at most one fixed point.

The two empirical dilation equations have the correct orientation. Doubling sends a source phase to \(S^{-1}\) of that phase. For odd \(n\), the exact equality \(T(n)=T(3n+1)\) preserves the phase. Restriction to the odd residue and to the image residue \(4\pmod6\) is legitimate because a fixed residue comparison costs only the density of adjacent label disagreements. The complete-cylinder coalescence input supplies that density bound for actual ordinary lifts.

The comparison of \(2^pX\) and \(3^qX\) is taken with \(p,q\) fixed before \(X\to\infty\). It yields the stated shift discrepancy. To equidistribute a period \(P\), approximation can be chosen with \(p\equiv1\pmod P\): the irrational rotation along that residue class is dense. This does not require a uniform Diophantine approximation rate.

## 2. The long-period and aperiodic tail

The tail argument handles all components together. Choose at most one phase from each component of period exceeding \(Mp\), or from an infinite component. Its first \(M\) translates by \(S^p\) are disjoint. An empirical measure whose \(S^p\)-discrepancy is at most \(\varepsilon\) therefore assigns the selected set mass at most

\[
             \frac1M+\frac{M-1}{2}\varepsilon.
\]

Choosing the approximation error smaller than \(M^{-2}\) and then letting \(M\to\infty\) makes the sum of the largest phase masses in the tail vanish. The selected set may depend on \(X\), since total variation controls every measurable set. Finite sample support ensures the maxima can be selected.

This is enough to pass from a finite list of cycles to the complete collision formula. It is not necessary to assume that the number of cycles is finite, or that the total mass of the aperiodic components is zero. Independent collision probabilities on those components vanish because their phase mass disperses.

## 3. The moving median date

For a fixed cyclic component, entry into the cycle differs from first attainment of the global minimum by a tight amount after restricting to finitely many possible minima. Each retained minimum is a fixed ordinary integer with a fixed finite future to that cycle. The imported joint minimum/clock law consequently gives entry mass \(d_C\Phi(u)\).

The maximal atom of the entry-time measure tends to zero. This follows from weak convergence, after normalization, to a finite multiple of the continuous Gaussian law: cover a compact interval by finitely many sufficiently short intervals and control the two tails. It is a uniform bound over all integer entry dates, which is what the transient-collision argument needs.

The phase argument still works after restricting to entry by the moving deadline. Fix a coalescence time \(t\). All sufficiently large starts stay above the fixed cycle for those first \(t\) dates, so fusion preserves both their entry time and their phase. A fixed multiplicative change in source size changes the median deadline by \(O(1)\), hence by \(o(\sqrt{\log X})\); the continuous entry law makes that threshold change negligible. The dilation comparison is therefore valid for the active submeasure, rather than only for the unrestricted basin.

Two independent sources which coincide off a fixed cycle at the common deadline have exactly the same later entry date. The maximal-atom bound makes this contribution vanish. On-cycle equality is equality of one of the uniformly distributed phases. Together with the tail truncation, this gives

\[
 \lim_{X\to\infty}\Pr(T^{H_X}n_1=T^{H_X}n_2)
       =\Phi(u)^2\sum_C\frac{d_C^2}{P_C}.
\]

At \(u=0\), the right side is at most \(1/8\), because every positive cycle has period at least two. A nonzero lower bound is not enough; the proposed route requires the maximal value. To turn maximal concentration into an all-integer theorem, the positive-predecessor premise is indispensable: a single counterexample must carry a positive-density exceptional population. The inspected proof uses that premise explicitly.

## 4. The arithmetic weighting in the new semiprime proof

Matomäki–Teräväinen's original statement has exactly the needed quantifiers: integer starting points outside \(O(X/(\log X)^\delta)\) exceptions, intervals of length \((\log x)^{2.1}\), at least \(c_0(\log x)^{1.1}\) products, and a smaller prime in \(((\log x)^{1.09},(\log x)^{1.1}]\). Those products lie in the packet's fixed family

\[
 \mathcal S=\{pq:\ p<q\text{ prime},\quad\log(pq)<p\le\log^2(pq)\}
\]

for all sufficiently large starting points. The source provides a lower bound, not a full asymptotic law for every interval.

With \(Q=2^{\lfloor(\log_2X)/4\rfloor}\), every smaller factor is invertible modulo \(Q\). Brun–Titchmarsh gives at most \(C X/(pQ\log X)\) choices of the larger prime in any specified odd product residue. Summing \(1/p\) over the permitted logarithmic prime band costs a constant. Thus every odd residue has at most \(CX/(Q\log X)\) candidates. The estimate is uniform in the residue, including residues selected because fusion fails.

For each displacement \(j\le H\), the original pair theorem gives only

\[
 O\!\left(Q\sqrt{\frac{1+\log(1+H)}t}\right)
\]

failing binary residues. Multiplying by the per-residue sparse count, rather than by an unrestricted integer count, gives the requisite error

\[
 O\!\left(\frac X{\log X}
              \sqrt{\frac{\log\log X}{\log X}}\right)
\]

per displacement. No independence of primality and the fusion event has entered. Summing incidences over the \(H\) displacements and dividing by the maximum multiplicity \(H\) retains an error smaller than the semiprime scale \(X/\log X\).

## 5. Exceptional windows, deadlines and the all-integer implication

The exceptional short intervals cost \(L\) times their number in the lower incidence bound, where \(L\asymp H/\log X\). They do not cost their maximal possible number of semiprimes. The upper incidence count costs \(H\) times the number of marked target semiprimes, plus the genuine failing incidences. These are exactly the two sides of the finite inequality formalized in [SparseSampling.lean](SparseSampling.lean).

For targets \(v\le X^{1/2}\), every actual state before the chosen merger time is at least \(X/2^t\ge X^{3/4}\), because each shortcut step decreases a positive integer by at most a factor two. Neither source has already visited the target. Their later visit indicators, including a common finite deadline, therefore agree. The formal kernel proves this last implication for any iterated map once actual merger and absence of earlier visits are supplied.

A set of positive lower natural density need not have positive mass in each individual dyadic octave. The packet avoids that false step: choose a fixed number of adjacent octaves whose union must contain a positive fraction of the set, then sum the uniform lower bounds. The total error is still \(o(X/\log X)\).

If one source does not converge, the named positive-predecessor input supplies a fixed positive-density exceptional set. The semiprime transfer places a positive fraction of \(\mathcal S\) in that set at every sufficiently large cutoff. Therefore even upper relative density one of convergence within this specific family forces convergence of every positive integer. Density one among all semiprimes is a different premise and is not substituted.

## 6. Formal scope and remaining obligation

The five public roots in [SparseSampling.lean](SparseSampling.lean) prove the exact finite incidence budget, insertion of aggregate error bounds, persistence of equality after actual merger, and equality of target-visit indicators when the earlier prefixes avoid the target. The [fresh receipt](../../../reports/astra-collision-factor-bridge-20261128/arithmetic/sparse-sampling-lean.json) records compilation and a separate import/type/axiom audit. The only recursive axioms reported are `Classical.choice`, `Quot.sound` and `propext`; pinned compiled dependencies were reused.

None of these finite declarations asserts the external short-interval, pair-fusion or positive-density theorems. The analytic transfer remains written. The remaining full-proof obligation is explicit: prove convergence on the specific easily factored semiprime family, or prove its relative convergence density is one. Factoring such an input is already polynomial in its bit length; the missing conclusion is an actual dynamical certificate.
