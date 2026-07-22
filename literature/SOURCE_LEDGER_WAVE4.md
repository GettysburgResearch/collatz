# Source ledger — literature audit wave 4

Only sources actually located during wave 4 appear here. The inspection field distinguishes full theorem inspection from abstract/metadata inspection. No abstract-only source is used as a black box.

## S39 — Väänänen and Wallisser, p-adic Tschakaloff values

**Record:** Keijo Väänänen and Rolf Wallisser, *A linear independence measure for certain p-adic numbers*, Journal of Number Theory 39 (1991), no. 2, 225–236. DOI `10.1016/0022-314X(91)90045-D`.

**Inspected:** publisher abstract and bibliographic record; full theorem hypotheses were not obtained.

**Located content:** a linear-independence measure for values of

```text
f_q(z)=sum_(n>=0) q^(n(n-1)/2) z^n
```

with rational `q` satisfying `0<|q|_p<1`.

**Native use:** PR #20 periodic phase vectors are exactly finite vectors of this function at rational points sharing one `q`. Whether the source theorem closes every fixed period is `UNVERIFIED — HIGH PRIORITY` until the complete hypotheses are inspected.

## S40 — Väänänen and Wallisser, theta-value independence

**Record:** Keijo Väänänen and Rolf Wallisser, *Zu einem Satz von Skolem über lineare Unabhängigkeit von Werten gewisser Thetareihen*, Manuscripta Mathematica 65 (1989), no. 2, 199–212.

**Inspected:** EuDML metadata and abstract descriptors.

**Located content:** archimedean and p-adic linear-independence measures for theta-series values.

**Native use:** historical and methodological neighbor of the PR #20 phase-vector problem; not a direct import without the theorem statement.

## S41 — Matala-aho, q-functional equations

**Record:** Tapani Matala-aho, *On Diophantine approximations of the solutions of q-functional equations*, Proceedings of the Royal Society of Edinburgh Section A 132 (2002), no. 3, 639–659. DOI `10.1017/S0308210500001827`.

**Inspected:** publisher abstract and theorem-level scope statement.

**Located content:** determinant-based dimension estimates and linear-independence measures for complex or p-adic values of solutions of linear q-functional equations; initial orbit values `F(t),F(qt),...,F(q^(m-1)t)` are treated under explicit coefficient and nonvanishing conditions.

**Native use:** determinant route for PR #20 periodic phase vectors and for the period-four endpoint problem. Exact native hypotheses must still be normalized.

## S42 — Väänänen and Zudilin, multi-point Tschakaloff values

**Record:** Keijo O. Väänänen and Wadim Zudilin, *Linear independence of values of Tschakaloff functions with different parameters*, Journal of Number Theory 128 (2008), no. 9, 2559–2573. DOI `10.1016/j.jnt.2008.03.009`.

**Inspected:** publisher abstract and bibliographic record.

**Located content:** linear independence for finite families of Tschakaloff values at rational points with different positive integer parameters in the archimedean setting.

**Native use:** exact vector geometry and determinant methodology for PR #20. It is not a p-adic black box for the current rational parameter.

## S43 — Krattenthaler, Rochev, Väänänen, and Zudilin

**Record:** Christian Krattenthaler, P. A. Rochev, Keijo Väänänen, and Wadim Zudilin, *On the non-quadraticity of values of the q-exponential function and related q-series*, Acta Arithmetica 136 (2009), no. 3, 243–269. DOI `10.4064/aa136-3-4`.

**Inspected:** source metadata and abstract-level description.

**Located content:** Hankel-determinant and cyclotomic-factor methods for Tschakaloff/q-exponential-type values.

**Native use:** the most concrete external model for seeking the very small reduced-height saving still needed in PR #20's period-four Padé system.

## S44 — Matala-aho and Seppälä, maximal-minor savings

**Record:** Tapani Matala-aho and Louna Seppälä, *Hermite–Thue equation: Padé approximations and Siegel's lemma*, Journal of Number Theory 191 (2018), 345–383. DOI `10.1016/j.jnt.2018.03.014`; arXiv `1805.00750`.

**Inspected:** full arXiv text, especially the Bombieri–Vaaler discussion and common factors of maximal minors.

**Located content:** the gcd of all maximal minors of a Hermite–Padé coefficient matrix can improve the height bound furnished by Siegel's lemma; explicit Vandermonde-type common factors are proved in the exponential model.

**Native use:** symbolic-minor rather than evaluated-gcd search for the PR #20 period-four deficit.

## S45 — Dubickas, nearest-integer rational powers

**Record:** Artūras Dubickas, *On the distance from a rational power to the nearest integer*, Journal of Number Theory 117 (2006), no. 1, 222–239. DOI `10.1016/j.jnt.2005.07.004`.

**Inspected:** publisher abstract and bibliographic record; full explicit formulas were not obtained.

**Located content:** every sequence `||xi(p/q)^n||` has explicit large and small limit points, with constants expressed through `p,q` and the Thue–Morse sequence.

**Native use:** specialize the large-limit constant to `(p,q)=(81,64)`. If it exceeds `1/81`, PR #16 `T-9315` closes the ordinary section immediately. The numerical specialization is `UNVERIFIED — HIGH PRIORITY`.

## S46 — Dubickas, two-interval avoidance

**Record:** Artūras Dubickas, *On the powers of 3/2 and other rational numbers*, Mathematische Nachrichten 281 (2008), no. 7, 951–958. DOI `10.1002/mana.200510651`.

**Inspected:** publisher abstract and bibliographic record.

**Located content:** noncontainment results for rational-power fractional parts in unions of two intervals, including a `3/2` example whose total interval length exceeds `1/2`.

**Native use:** methodologically much closer than a one-interval width theorem to PR #16's centered two-arc target. Exact specialization to `81/64` remains open.

## S47 — Dvoretzky–Wald–Wolfowitz purification

**Record inspected through:** M. Ali Khan, Kali P. Rath, and Yeneng Sun, *The Dvoretzky–Wald–Wolfowitz theorem and purification in atomless finite-action games*, International Journal of Game Theory 34 (2006), 91–104. DOI `10.1007/s00182-005-0004-3`.

**Inspected:** publisher abstract and theorem summary.

**Located content:** on an atomless space, a randomized choice among finitely many actions can be replaced by a pure measurable choice preserving a finite family of integrals.

**Native use:** may upgrade PR #34 `L-9866` from a static fractional residue allocation to a deterministic measurable static selector if the decoder measure is atomless. It does not supply temporal, integer, or cross-modulus coherence.

## S48 — Anashin, van der Put automata criterion

**Record:** Vladimir Anashin, *Automata finiteness criterion in terms of van der Put series of automata functions*, p-Adic Numbers, Ultrametric Analysis and Applications 4 (2012), no. 2, 151–160. DOI `10.1134/S2070046612020070`; arXiv `1112.5089`.

**Inspected:** full arXiv abstract and theorem scope.

**Located content:** finite-state transducers induce 1-Lipschitz p-adic functions; finiteness of the state set is characterized through the reduced van der Put coefficients.

**Native use:** exact finite-state test for PR #3 padding-address maps, Foundry operators, and PR #34 correction isometries.

## S49 — MacDonald, zero-error symbolic embedding

**Record:** Sophie MacDonald, *Encoding subshifts through sliding block codes*, Ergodic Theory and Dynamical Systems 44 (2024), no. 6, 1690–1709. DOI `10.1017/etds.2023.56`; arXiv `2210.08150`.

**Inspected:** publisher abstract and article structure.

**Located content:** necessary and sufficient conditions for embedding a lower-entropy subshift into a mixing SFT while preserving injectivity through a prescribed surjective sliding-block observation.

**Native use:** PR #3 router after the scale-dependent arithmetic relation is normalized to a stationary mixing SFT. The current system is not yet within the theorem's hypotheses.

## S50 — q-Lucas/cyclotomic congruence framework

**Record:** Boris Adamczewski, Jason P. Bell, Éric Delaygue, and Frédéric Jouhet, *Congruences modulo cyclotomic polynomials and algebraic independence for q-series*, Séminaire Lotharingien de Combinatoire 78B (2017), Article 54; arXiv `1701.06378`.

**Inspected:** full arXiv abstract and metadata.

**Located content:** Lucas-type congruences for q-factorial ratios modulo cyclotomic polynomials and propagation to q-series.

**Native use:** all-dyadic q-Lucas/Cartier renormalization suggested by PR #34 `L-9862` and `L-9864`; no exact native recurrence is imported.

## Inspection cautions

- The complete 1991 Väänänen–Wallisser hypotheses are not available in the inspected record; no all-period closure is claimed.
- Dubickas's explicit `(81,64)` constant has not been evaluated from the full formula.
- DWW purification requires atomlessness and only preserves finitely many static integrals.
- Symbolic embedding requires a stationary symbolic system, entropy separation, and periodic-point compatibility.
- No source in this ledger constructs an ordinary Collatz survivor or counterexample.