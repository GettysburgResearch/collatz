# Independent reconstruction of the sparse semiprime transfer

**Verdict: VERIFIED at the written, source-qualified scope below.** This is a reconstruction of the stated implication, not an independent proof of the external analytic inputs and not a proof of Collatz on the resulting family.

- Reviewed file: `research/astra-collision-factor-bridge-20261128/SEMIPRIME_SUFFICIENCY.md`.
- Reviewed file SHA-256: `c2e7f74f7fb4e49836e898b746e41dc66a3a7e103af553cffbf553e675fd6e63`.
- Review performed: November 28, 2026, approximately 09:20 UTC.
- Directly reopened original: [Matomäki–Teräväinen, arXiv:2207.05038v2, Theorem 1.1](https://arxiv.org/pdf/2207.05038v2).
- Original Leen TeX inspected at labels `pair:cylinders`, `pair:dictionary`, `pair:uniform-tail`: [DOI 23268751](https://doi.org/10.5281/zenodo.23268751), downloaded source SHA-256 `d2f961635d339a4b215c82b1f2f8b9ca53143043f4c58b9aa67290f46056996e`.

The short-interval theorem has the required integer exception count, lower population of order \((\log x)^{1.1}\), and smaller-factor window \((\log x)^{1.09}<p\le(\log x)^{1.1}\). At the octave scale these primes lie in the manuscript's fixed family, and enlarging to its common window \(H\) preserves the lower bound with an absolute constant.

The crucial weighted step is valid. For each odd residue modulo \(Q=2^t\), multiplication by each permitted prime factor is invertible. Brun–Titchmarsh applies to the other prime with \(Q\le X^{1/4}\) and smaller factor polylogarithmic in \(X\); its logarithmic denominator remains a fixed positive fraction of \(\log X\). The reciprocal prime sum over the smaller-factor window is bounded. Thus each bad residue contains \(O(X/(Q\log X))\) semiprime targets. This is an actual upper sieve bound, not an assumption that the fusion failure and primality are independent.

The pair-fusion input gives \(O(Q\sqrt{\log(1+H)/t})\) failed residues. Multiplying by the preceding bound produces a failure budget small relative to \(X/\log X\), even after summing the \(H\) incidences. Dividing by the maximum target multiplicity \(H\) is legitimate. Trimming the at most \(H\) targets beyond the octave costs \(o(X/\log X)\). All errors are independent of the selected component union.

The fixed-target and common-deadline variants retain genuine physical semantics. Through the fusion time, both actual paths stay above \(X/2^t\ge X^{3/4}\), so they have not visited a target \(v\le X^{1/2}\). Once they meet, their remaining futures and deadline-visit indicators agree. The deadline is required to be at least the fusion time.

Finally, the fixed finite union of top dyadic octaves correctly transfers a positive lower natural density to a positive semiprime count. It does not assume positive mass on every individual octave. The upper sieve bound for the entire selected family then gives positive lower relative density there. Applying Mazur's correctly normalized positive-predecessor implication to a fixed eligible target closes the stated reduction.

No inverse-probability loss, unproved independence assumption, moving-target density onset, or density-one-convergence premise was found in this reconstruction. The unproved remaining task is convergence on the selected family itself, or a sufficiently strong relative convergence statement within it.
