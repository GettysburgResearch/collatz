# Source ledger — literature audit wave 7

Only sources actually located during this pass appear here. Inspection level and native use are explicit.

## S63 — Akiyama, Frougny, and Sakarovitch: rational-base division

**Record:** Shigeki Akiyama, Christiane Frougny, and Jacques Sakarovitch, *Powers of rationals modulo 1 and rational base number systems*, Israel Journal of Mathematics 168 (2008), 53–91. DOI `10.1007/s11856-008-1056-4`.

**Inspected:** full abstract and accessible source text/metadata.

**Located content:** least-significant-first rational-base division; every nonnegative integer has a unique finite expansion; the integer-representation language is not regular; addition is realizable by a finite right transducer.

**Native use:** `LIT-KTHM-0048`. A centered or collision chart is only a restricted/translated rational-base language after a definition-level mapping.

## S64 — Frougny and Klouda: p-adic rational-base representations

**Record:** Christiane Frougny and Karel Klouda, *Rational base number systems for p-adic numbers*, RAIRO — Theoretical Informatics and Applications 46 (2012), no. 1, 87–106. DOI `10.1051/ita/2011114`.

**Inspected:** complete open-access PDF, including the introduction, Algorithms 3.1/GMD, Lemma 3.3, and the theorem roadmap for finite and eventually periodic representations.

**Located content:** exact p-adic rational-base algorithms; finite-representation characterization; eventual-periodicity criterion under the paper's convention; finite transducers between four rational-base systems.

**Native use:** completion-safe placement of appended residue blocks. No real and p-adic limits are identified.

## S65 — Akiyama, Marsault, and Sakarovitch: all rational-base subtrees differ

**Record:** Shigeki Akiyama, Victor Marsault, and Jacques Sakarovitch, *On subtrees of the representation tree in rational base numeration systems*, Discrete Mathematics & Theoretical Computer Science 20 (2018), no. 1, article 10. DOI `10.23638/DMTCS-20-1-10`; arXiv `1706.08266`.

**Inspected:** complete open-access HTML theorem text and introduction.

**Located content:** every rooted integer subtree is distinct; bottom words are distinct and non-ultimately-periodic; the successor map is realized by an infinite sequential transducer; the span closure has an interval/Cantor dichotomy.

**Native use:** `LIT-KTHM-0049`. A finite modular lasso need not preserve the exact rooted future; positive architectures need a proved quotient/nucleus lift.

## S66 — Hercher: the local-minimum cycle frontier

**Record:** Christian Hercher, *There are no Collatz m-Cycles with m <= 91*, Journal of Integer Sequences 26 (2023), Article 23.3.5; arXiv `2201.00406`.

**Inspected:** official journal abstract, full-source links, and parameter statement.

**Located content:** a nontrivial positive Collatz cycle must have at least 92 local minima. The paper's parameter is local-minimum count, not accelerated odd length.

**Native use:** scope boundary for `LIT-KTHM-0051` and issues #9/#41. Every candidate must report the exact local-minimum convention.

## S67 — Dubickas and Mossinghoff: restricted rational-base searches

**Record:** Arturas Dubickas and Michael J. Mossinghoff, *Lower bounds for Z-numbers*, Mathematics of Computation 78 (2009), 1837–1851. DOI `10.1090/S0025-5718-09-02211-X`.

**Inspected:** article abstract, bibliographic record, and the search problem definition.

**Located content:** proof-producing algorithms for lower bounds in restricted rational-multiplication problems and connections with integer iteration.

**Native use:** methodological neighbor for PR #35 and issue #40. Finite lower bounds do not imply asymptotic emptiness.

## S68 — recent rational-base normality conjecture

**Record:** Mélodie Andrieu, Shalom Eliahou, and Léo Vivion, *A Normality Conjecture on Rational Base Number Systems*, arXiv `2510.11723` (2025).

**Inspected:** full abstract and stated implications.

**Located content:** conjectural normality of minimal and maximal rational-base words, supported by numerical experiments, with consequences for Z-number-type and Collatz-inspired problems.

**Native use:** heuristic discriminator only. It is not imported as a theorem and cannot close PR #35, issue #40, or a collision chart.

## Inspection cautions

- Rational-base object-class similarity is not a definition-level conjugacy.
- Finite or eventually periodic p-adic representation theorems do not identify a separate real limit.
- Hercher's `m` is local-minimum count, not valuation-word length.
- The 2025 normality statement is conjectural.
- No source in this ledger constructs a standard `3x+1` counterexample.