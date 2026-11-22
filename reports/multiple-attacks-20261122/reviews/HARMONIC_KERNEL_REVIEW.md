# Independent review of the harmonic-kernel factorization

**Reviewer:** `inverse_clock_attack`  
**Date:** 2026-11-22 UTC  
**Verdict:** VERIFIED at the written operator-argument level, conditional
on the explicitly imported actual-path occupation and strict-Green
theorems. No Lean formalization of this analytic argument is asserted.

The frozen source is `HARMONIC_KERNEL_FACTORIZATION.md`, SHA256
`013fb3c5a3a1c6fd2f18ad9d81c57e55ed04192b5ffa4c9861823a3379763b9d`.
The verdict does not extend automatically to later edits or to upstream
analytic inputs.

I independently reconstructed the following points:

- The immigration multiplier maps \(X_s\) into unweighted \(\ell^1\),
  hence into the maximal domain of \(L\). Thus
  \((I-zD)a\in\mathcal D(L)\) exactly when \(a\in\mathcal D(L)\),
  even when \(I-zD\) has a zero coordinate.
- The positive physical kernel gives \(LK=K-B\ge0\). Applying it to
  absolute values controls every parent sum for complex inputs and
  proves \(K(X_s)\subset\mathcal D(L)\).
- The identity \(R(z)=I-zKR(z)\) makes the domain automorphism
  algebraic; closedness or closability is not needed. The right
  factorization gives the stated exact range equality and stationary
  kernel isomorphism, without claiming full spectral conjugacy.
- The coefficient of \(S_TB\) has immigration at the original source
  and critical factors only at interior states, so
  \(R(1)=I-S_TB\) has the correct order. For any nonnegative ordinary
  harmonic \(\nu\in X_s\), monotone \(T^k\nu\) stays between
  \(\delta\nu\) and \(\nu\), and its telescoping limit is
  \(R(1)\nu\).
- Positivity in both directions therefore gives the claimed order
  isomorphism of harmonic cones. The escape indicator is constant on
  retained edges and commutes with the correction, preserving its
  positive escaping sector.

No substantive correction is requested. The theorem preserves the
stationary obstruction exactly: an entire inverse for the correction is
not an inverse for the unsmoothed stationary equation. Periodic states
remain excluded from this domain.
