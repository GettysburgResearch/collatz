# Polynomial rational exclusion on ordinary Collatz windows

Let \(x_i\) be successive odd sites, \(2^{e_i}x_{i+1}=3x_i+1\), and \(S_i=\sum_{j<i}e_j\). Write \(M_i=3^i/2^{S_i}\). A strict record \(k\) satisfies \(M_k>M_i\) at every earlier index \(i\). The record and excursion bounds concern one ordinary orbit at a time.

## A quantitative gain at an actual record

There is an absolute explicit integer \(C\) with the following property. Fix positive integers \(d,H,n\), a signed integer \(A\), and an odd starting integer coprime to three. Suppose \(k\ge n\) is a strict record and \(d x_k\equiv A\pmod{3^n}\). Then
\[
 C H^{718}\bigl(\lfloor |A|/d\rfloor+1+d^{19}\bigr)\le n
 \quad\Longrightarrow\quad
 M_k>H M_{k-j}\quad\text{for some }1\le j\le n .
\]
The theorem applies to every such record, including on orbits that later repeat. For a fixed rational \(A/d\) approached through increasingly many ternary digits at records with at least that much history, the largest recent gain grows at least as a constant times \(n^{1/718}\). This follows by taking the integer part of the corresponding root in the displayed inequality. The constant \(C\) is \(31(1+(76\cdot10^{10})^{20}(4\cdot10^2\cdot3^{200})^{19})\). [ReturnOrbitGrowth.lean](mathlib/ReturnOrbitGrowth.lean)

The same file proves an excursion without a rational approximation hypothesis. For every fixed positive odd unit \(a\) and \(K\ge1\), there exists \(j\le T_2(1,K,a)\) with \(M_j>K\) or \(M_j<1/K\). Here \(a\) itself supplies the integral dyadic shadow. [ReturnOrbitGrowth.lean](mathlib/ReturnOrbitGrowth.lean)

There is also a simultaneous statement on one fixed nonrepeating ray. Assume bounded coefficient drawdown \(M_i\le B M_j\) for all \(i\le j\) and unbounded gaps between strict records. For every depth \(n\) and starting index \(R\), an actual record \(k\ge\max(n,R)\) satisfies \(d x_k\not\equiv A\pmod{3^n}\) for **every** \(d>0,A\in\mathbb Z\) with \(T_3(d,2B,A)\le n\). Both the rational and its denominator can vary with \(n\). The proof selects the first record after a sufficiently long record-free interval. Its last \(n\) suffix coefficients are between 1 and \(2B\), giving all the exclusions at the same endpoint. [ReturnOrbitRecords.lean](mathlib/ReturnOrbitRecords.lean) · [HourEscapeDrawdown.lean](HourEscapeDrawdown.lean)

## Exact horizons and both primes

Define
\[
\begin{aligned}
 U(d,K,A)&=\lfloor |A|/d\rfloor+1+
 (76K^{10})^{20}(4\cdot3^{200}K^2d)^{19},\\
 T_2(d,K,A)&=30K^4U(d,K,A),\\
 T_3(d,K,A)&=(30K^4+1)U(d,10K^3,A).
\end{aligned}
\]
If \(w_j=3^j/2^{\sum_{i<j}e_i}\in[1/K,K]\) on every prefix of a signed integral history starting at \(A\), the forward equations \(2^{e_i}y_{i+1}=3y_i+d\) with odd sites cannot hold through \(T_2\). The backward equations \(3y_{i+1}+d=2^{e_i}y_i\) cannot hold through \(T_3\) for any positive denominator. Every gap \(e_i\) may be any positive integer. In particular the latter bound applies to even denominators and either sign of \(A\). [ReturnOrbitBinary.lean](mathlib/ReturnOrbitBinary.lean) · [ReturnOrbitTernary.lean](mathlib/ReturnOrbitTernary.lean)

For an ordinary forward window in \([m,Km]\), put \(N_2=(3K+2)(T_2(d,2K,A)+1)\). If the window has \(N_2\) edges and \(m\ge K N_2>0\), then its starting site \(x\) satisfies \(d x\not\equiv A\pmod{2^{N_2}}\) for every odd \(d\). A ternary endpoint in a window of \(N_3=T_3(d,2K,A)\) edges with \(m\ge K N_3>0\) satisfies \(d x\not\equiv A\pmod{3^{N_3}}\). Each phase of a cycle in a sufficiently high band obeys both exclusions for its respective rational. On an injective ordinary orbit the dyadic exit theorem also applies at any positive floor \(m\), with an exit by \((K^2+1)N_2\) steps. If \(m<K N_2\), a longer window would contain more distinct sites than the band. [ReturnOrbitWindows.lean](mathlib/ReturnOrbitWindows.lean) · [ReturnOrbitTernaryWindows.lean](mathlib/ReturnOrbitTernaryWindows.lean)

## Finite proof

Take \(b=200r\). The weight bounds imply that any \(b\)-gap window has total at most \(317r+P\), where \(P=1+\lfloor\log_2 K^2\rfloor\). Let \(W\) count positive words of this length and total at most \(317r+P\). Cumulative gap sums give \(W=\binom{317r+P}{200r}\). The binomial term with weights 12 and 7, combined with the exact integer comparison
\[
 (19^{317})^{20}\le(3^{200})^{19}(12^{200}7^{117})^{20},
\]
gives \(W^{20}\le19^{20P}(3^b)^{19}\). Also \(19^P\le19K^{10}\). Choosing the first such \(b\) with \(3^b>Dn\) puts the signed diameter inside one ternary modulus; for \(n>(4\cdot19^P)^{20}(3^{200}D)^{19}\), the census plus the required window length fits inside \(n\). [ReturnOrbitCensus.lean](mathlib/ReturnOrbitCensus.lean) · [ReturnOrbitPacking.lean](mathlib/ReturnOrbitPacking.lean)

In the forward signed history the increments of \(y_i/w_i\) are \(d/(3w_i)\). In the backward signed history the decrements of \(w_i y_i\) are \(d w_{i+1}/3\). These identities give a linear height bound and separate a later block from an explicit reference state. In the chronological forward direction, a previous repeat would trap the later state in the repeated block. For an even inverse denominator, each halving of \(d\) removes one preliminary edge and reduces to an integral shadow for \(d/2\); the first \(d\) steps suffice. Equal short words force identical terminal residues modulo \(3^b\). The signed diameter then forces identical states, contradicting distinctness when the number of samples exceeds \(W\). [ReturnOrbitPacking.lean](mathlib/ReturnOrbitPacking.lean) · [ReturnOrbitBinary.lean](mathlib/ReturnOrbitBinary.lean) · [ReturnOrbitTernary.lean](mathlib/ReturnOrbitTernary.lean)

## Existing estimates and the outstanding step

Weaver gives a logarithmic improvement at the entropy exponent for ordinary orbit-event counts, and states an ineffective strict power saving. The present word exponent 19/20 is above the ordinary entropy exponent of approximately 0.94996. It gives a finite estimate uniform over rational signed histories. The moving denominators, modulus precisions and pointwise gain conclusion are the comparisons at issue here. PR 210 uses a one-sided clock bound on a distinct inverse signed path and obtains a sublinear exponent in the size of the starting numerator for fixed \(d\). Its displayed integer denominator factor is \((3d)^d2^{400d}\). The two-sided strip here supplies polynomial dependence on both width and denominator and allows repeats in the starting hypotheses. [Weaver, Paper 28](https://rstation.ai/problems/collatz/papers/28) · [PR 210, Sections 3–4](https://github.com/GettysburgResearch/collatz/blob/592328fecf8ea2cf41736294856d95f890a1ba98/research/critical-record-rational-rigidity-20261125/README.md)

The proofs require a rational approximation at the stated precision to force a record gain. Such precision is not supplied at the required records by the current rational-diagonal or phase-mass estimates. Arbitrarily long ordinary balanced windows can be realized on orbits that reach a prescribed next target, including 1, when one varies the starting integer. An escaping source can still have large coefficient gains or record coordinates avoiding these rational neighborhoods. High bounded-width cycle phases can still accumulate at irrational coordinates satisfying the two computed restrictions. [PR 201, rational diagonal](https://github.com/GettysburgResearch/collatz/blob/21bed7ac2b1b1bb4baf0f6cabd53f8b9dd11b58a/research/unconventional-20261126/renewal/RATIONAL_DIAGONAL.md) · [PR 193, phase pair mass](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/arithmetic/PHASE_PAIR_MASS.md) · [Ordinary finite-window realization](HourCycleRealization.lean)

PR 201 supplies two concrete witnesses that illustrate the missing estimate. For a record after \(k\) odd steps and \(s\) physical clocks, the rational obtained by starting the same word at \(-1\) has reduced denominator exactly \(2^{s-v_2(x_0+1)}\) once \(s>v_2(x_0+1)\). Since \(s\ge k\), its nineteenth power already exceeds the available \(k\)-digit guarantee at late records. Periodizing the word gives a different rational with denominator \((3^k-2^s)/\gcd(3^k-2^s,x_k-x_0)\). Fix an earlier positive strict record \(h<k\). The quotient \(d_{\mathrm{per}}\) itself satisfies \(2^k\le 3^h(x_0+1)d_{\mathrm{per}}\). Indeed \(3^k\le3^h(3^k-2^s)\) by the previous record, while the gcd is at most \(x_k-x_0\) and \(2^k(x_k+1)\le3^k(x_0+1)\). Both constructions therefore have exponentially large denominators on a fixed source as its record indices grow. [Denominator growth](mathlib/ReturnOrbitWitness.lean) · [PR 201, exact witness identities](https://github.com/GettysburgResearch/collatz/blob/21bed7ac2b1b1bb4baf0f6cabd53f8b9dd11b58a/research/unconventional-20261126/CLOSING_AUDIT.md)

PR 201 added a checkpoint during this pass. Its positive weighted escape mass obeys a one-sided forward clock restriction. The ternary decoder predicts a finite predecessor word on a selected portion with a table allowed to depend on the depth. The rational exclusion here requires a two-sided bound on a window and an explicit numerator and denominator at its endpoint. The cost of the two complete-prefix rational witnesses therefore persists. [New permanent sieve](https://github.com/GettysburgResearch/collatz/blob/3376695869fcf7d2e34f676a876d2b78a391d799/research/six-hour-20261127/escape/PERMANENT_SIEVE.md) · [New ternary decoder](https://github.com/GettysburgResearch/collatz/blob/3376695869fcf7d2e34f676a876d2b78a391d799/research/six-hour-20261127/escape/TERNARY_DECODER.md)
