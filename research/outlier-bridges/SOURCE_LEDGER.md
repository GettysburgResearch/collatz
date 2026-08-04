# Outlier source ledger

**Agent:** `gpt56-outlier-01`
**Issue:** #52
**Inspection date:** 2026-07-23

This ledger records remote-field sources used to formulate or reject bridges. Source statements, native reductions, and analogies are separated. No source below is claimed to mention the repository's Collatz constructions.

## OUT-SRC-0001 — Sparse resultants

- **Source:** Carlos D'Andrea, Gabriela Jeronimo, Martin Sombra, *The Canny–Emiris conjecture for the sparse resultant* (2020), arXiv:2004.14622.
- **URL:** https://arxiv.org/abs/2004.14622
- **Inspected statement:** sparse resultants generalize classical resultants to Laurent-polynomial systems with prescribed supports; Sylvester-type matrices tied to mixed subdivisions can compute them under the paper's hypotheses.
- **Native use:** conceptual framework for eliminating dyadic pulse variables from the sparse pair `(D,H)`.
- **Exact dependency:** none. `L-8201` uses only a two-by-two determinant for two linear polynomials.
- **Boundary:** the source does not supply Collatz-specific nonvanishing or pulse caps.

## OUT-SRC-0002 — Non-Archimedean amoebas and tropical varieties

- **Source:** Manfred Einsiedler, Mikhail Kapranov, Douglas Lind, *Non-archimedean amoebas and tropical varieties* (2004), arXiv:math/0408311.
- **URL:** https://arxiv.org/abs/math/0408311
- **Inspected statement:** for hypersurfaces, the non-Archimedean amoeba agrees with the tropical variety of the defining polynomial.
- **Native use:** explains `L-8201`'s valuation certificate: a zero requires at least two minimum-valuation monomials, while the pulse resultant has a unique minimum.
- **Exact dependency:** none. The ultrametric unique-minimum argument is proved directly.
- **Boundary:** tropical nonvanishing does not itself give integrality, positivity, or exact Collatz replay.

## OUT-SRC-0003 — Noncatastrophic convolutional encoders over finite rings

- **Source:** Diego Napp, Raquel Pinto, Conceição Rocha, *Noncatastrophic convolutional codes over a finite ring* (2021), arXiv:2104.06754.
- **URL:** https://arxiv.org/abs/2104.06754
- **Inspected statement:** over finite fields, noncatastrophic polynomial encoders are characterized by polynomial left-prime generator matrices; the paper studies the corresponding distinctions over `Z/(p^r)`.
- **Native use:** proposed audit for bounded-memory linearized ordinary-boundary certificates.
- **Exact dependency:** none.
- **Hypothesis failure:** PR #49 and the pulse run-core are nonlinear, partial, and changing-modulus, not stationary polynomial encoders.

## OUT-SRC-0004 — Catastrophicity for periodically time-varying encoders

- **Source:** Fan Jiang, *A Novel Catastrophic Condition for Periodically Time-varying Convolutional Encoders Based on Time-varying Equivalent Convolutional Encoders* (2023), arXiv:2309.05849.
- **URL:** https://arxiv.org/abs/2309.05849
- **Inspected statement:** a catastrophic encoder maps an infinite-weight information sequence to a finite-weight code sequence; the paper gives a condition for periodically time-varying encoders.
- **Native use:** exact vocabulary for the desired but dangerous compression “infinite directive -> finite-support ordinary integer.”
- **Exact dependency:** none.
- **Boundary:** a catastrophic linearized model would be only a candidate certificate interface; physical Collatz replay would still be required.

## OUT-SRC-0005 — Primitive divisors in arithmetic dynamics

- **Source:** Patrick Ingram, Joseph H. Silverman, *Primitive Divisors in Arithmetic Dynamics* (2007), arXiv:0707.2505.
- **URL:** https://arxiv.org/abs/0707.2505
- **Inspected statement:** for a rational map of degree at least two satisfying the stated conditions and an infinite orbit, numerator sequences acquire primitive divisors at all but finitely many iterates.
- **Native use:** potential mechanism for PR #49's proposed necessity that a survivor generate fresh odd primes forever.
- **Exact dependency:** none.
- **Hypothesis failure:** the present PR #49 counter map is nonautonomous and affine/degree one. An autonomization theorem is missing.

## OUT-SRC-0006 — Ergodic 1-Lipschitz maps on `Z_p`

- **Source:** Vladimir Anashin, *Ergodic Transformations of the Space of p-adic Integers* (2006), arXiv:math/0602083.
- **URL:** https://arxiv.org/abs/math/0602083
- **Inspected statement:** a 1-Lipschitz self-map of `Z_p` is ergodic precisely when it induces a single-cycle permutation modulo every `p^k`; the characterization is complete for `p=2` in the stated class.
- **Native use:** possible residue-transitivity test for a future inverse address generator.
- **Exact dependency:** none.
- **Hypothesis failure:** the active forward charts are partial and expanding, not global 1-Lipschitz self-maps of `Z_2`.

## OUT-SRC-0007 — Homoclinic algebraic dynamics

- **Source:** Douglas Lind, Klaus Schmidt, Evgeny Verbitskiy, *Homoclinic points, atoral polynomials, and periodic points of algebraic Z^d-actions* (2011), arXiv:1108.4989.
- **URL:** https://arxiv.org/abs/1108.4989
- **Inspected statement:** cyclic algebraic `Z^d` actions arise from Laurent-polynomial ideals; rapidly decaying summable homoclinic points are a principal tool in the paper's periodic-point analysis.
- **Native use:** a firewall: decay or summability of a symbolic completion is weaker than finite support, hence weaker than ordinary integer initialization.
- **Exact dependency:** none.
- **Boundary:** homoclinic existence must not be promoted to an ordinary Collatz witness.

## Repository overlap audit

Branch-aware repository searches and the issue/PR index found no use of the terms:

```text
sparse resultant
toric resultant
catastrophic convolutional encoder
left-prime encoder
```

in the active work inspected through PR #51. This supports the classification “new to this repository sweep,” not a claim of global mathematical novelty.
