# Proof program: from unconditional density-one EQ to the all-depth and M1 frontiers

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Status:** research program; every unproved step is labeled

## 1. Exact theorem boundary

The active self-contained chain is

```text
L-9309  exact lift-prefix / residue-class bijection
   |
   v
T-9307  exponential entropy deficit for low-energy prefixes
   |
   v
T-9308  uniform harmonic high-frequency tail at every depth
   |
   +------------------------------+
   |                              |
   v                              v
all-depth low/high reduction   T-9303 valuation-stratified
                               low-frequency depth periods
                                  |
                                  v
                            T-9309 unconditional
                            density-one full EQ
```

The split/room chain is

```text
D-9303 fixed Z_3 mirror
   |
   v
L-9305 moving-character identity
   |
   + L-9301 fixed Z_2 survivor
   v
T-9304 exact CRT product
   |
   +-----------------------------+
   |                             |
   v                             v
L-9306 full-group moments    L-9307/L-9308 stitched phase chain
                                 |
                                 v
                          T-9305/T-9306 split collapse
```

The direct counterexample-format chain is separate:

```text
D-9301 survivor attractor
   |
   v
D-9302 adelic natural extension and integer section
   |
   v
Q-9301 nontrivial ordinary-integer intersection
```

## 2. What is already closed

### 2.1 The exponential frequency range

`T-9308` proves, uniformly in every depth,

\[
\sum_{M\le h\le2^K}
\frac{F_K(h)}h
\le
C M^{-\delta}
+
\pi2^{-5K}
\]

for one explicit `delta>0` and every growing cutoff `M`.

Therefore all-depth EQ no longer requires a frequency-block theorem or a pointwise attack on exponentially many frequencies. Only the smallest growing window remains.

### 2.2 Density-one full EQ

`T-9309` combines the uniform tail with the exact depth-period estimate `T-9303`. It proves

\[
E_K\to0
\]

along a natural-density-one set of depths with no external mathematical hypothesis.

The exceptional depth set can be infinite. Density one is not all-depth convergence.

### 2.3 Naive exact-prefix amplification

`L-9309` proves that a length-`L` exact lift prefix is one residue class modulo `81^L`. `R-9301` therefore refutes the claim that one exact prefix persists on a consecutive Euclidean neighborhood.

Any surviving amplification theorem must use:

- approximate-cylinder unions;
- transference from arithmetic progressions;
- harmonic location of many sparse classes;
- or a nonlinear positive operator.

### 2.4 Independent local spectral gain

`L-9307` and `L-9308` prove that the dyadic and triadic factors are adjacent pieces of one phase chain. `T-9305` and `T-9306` show that every split is equivalent to the original coefficient in sub-`64^K` ranges, even against arbitrary bounded harmonic tests.

A multi-place proof may still be easier, but its target is not weaker.

## 3. Exact state variable

For fixed depth `K`, define

\[
q_\ell(h)
\equiv
-17h64^{\ell-K}
\pmod{81^{\ell+1}},
\qquad
0\le q_\ell<81^{\ell+1},
\]

and

\[
y_\ell(h)=
\frac{q_\ell(h)}{81^{\ell+1}}.
\]

The lift digit

\[
d_\ell(h)
=
\left\lfloor
\frac{q_{\ell+1}(h)}{81^{\ell+1}}
\right\rfloor
\in\{0,\ldots,80\}
\]

gives the exact recurrence

\[
\boxed{
y_{\ell+1}
=
\frac{\{64y_\ell\}+d_\ell}{81}.}
\tag{1}
\]

For every `L`, the map

\[
h\pmod{81^L}
\longleftrightarrow
(q_0,d_0,\ldots,d_{L-2})
\]

is a bijection.

This finite exact state—not an informal random model—is the common object underneath:

- the issue-#4 Markov decomposition;
- the triadic Cantor classes;
- the room tower;
- the depth-period arithmetic;
- and the proposed all-depth inverse theorem.

## 4. Offense A: harmonic location of exceptional cylinders

`T-9307` gives, in every interval of length `H`, at most

\[
O(H^{1-\eta})
\]

frequencies whose first `floor(log_81 H)` phases have energy at most the fixed threshold.

Counting is not enough near the origin. The all-depth target requires a harmonic-location theorem of the form

\[
\sum_{h\in\mathcal B_K(H)}
\frac1h
\le
H^{-c}
\quad\text{or at least }o(1),
\tag{2}
\]

where `B_K(H)` is the exceptional low-energy set in `[1,H]`.

### Proposed stratification

For each exceptional prefix record:

1. `v_3(h)` and any exact initial zero phases;
2. the first level with distance at least a chosen threshold;
3. the lift-digit word up to that level;
4. the terminal residue `q_(L-1)`;
5. the least positive representative of its class modulo `81^L`.

Seek a theorem saying that many low-energy classes cannot all have anomalously small least representatives.

### Exact terminal relation

A length-`L` prefix reconstructs

\[
h
\equiv
-17^{-1}64^{K-L+1}q_{L-1}
\pmod{81^L}.
\tag{3}
\]

Thus harmonic location is a problem about the real sizes of the representatives of a low-energy subset of terminal reciprocal residues after multiplication by one unit.

This is a finite, explicit target. It is also where individual-orbit arithmetic re-enters.

## 5. Offense B: carry-template inverse theorem

The flagship all-depth inverse theorem should be stated as follows.

> **Carry-template inverse theorem, tentative.** Every polynomial-height frequency whose phase energy stays `O(log K)` admits a bounded-complexity lift-digit description. Every such description either:
> 1. reduces by an exact power of `64`;
> 2. loses levels through an exact power of `81`;
> 3. is arithmetically impossible;
> 4. or belongs to an approximate-cylinder family whose harmonic mass violates the entropy/location bounds.

The exact dyadic representatives also satisfy

\[
17h
=
81^{\ell+1}s_\ell
+
64^{K-\ell}m_\ell.
\tag{4}
\]

Eliminating `h` between separated levels produces four-term `{2,3}`-unit relations. A specialized effective height gap—not a bare citation to the general S-unit theorem—could force the divisibility or finite-template alternatives.

## 6. Offense C: exceptional-depth coherence

`T-9309` produces a zero-density exceptional depth set by Markov's inequality. To upgrade to all-depth EQ, exploit overlap between scales.

If one depth is bad for several adjacent `m`, then it must contain coherent low-frequency mass in nested windows

\[
81^{\alpha m}.
\]

At the same time:

- `T-9307` says low-energy prefixes are sparse;
- `T-9308` removes frequencies outside those windows;
- `T-9303` says such behavior is rare across complete depth periods;
- the room first marginal contracts over the period-9 twist.

The proposed theorem is:

> A depth exceptional at `r` adjacent scales determines a carry word of complexity `O(r)` whose arithmetic height is exponentially smaller than its required modulus.

Classify or rule out those words.

## 7. Offense D: positive room-tower operator

Issue #4's room walk does not close at any fixed modulus: the marginal at level `m` is driven by joint information at level `m+1`.

Absolute Fourier majorants are vulnerable to exact copies. A positivity-native route should:

1. write the exact inverse-limit kernel on `Z_3` using `D-9303`;
2. retain the deterministic period-9 twist;
3. choose a positive observable—interval mass, relative entropy, or room imbalance;
4. prove one-period contraction;
5. bound the information flux imported from the next tower level by less than that contraction.

This may prove the harmonic-location theorem without controlling individual Fourier coefficients.

## 8. Offense E: rational-diagonal renewal

The CRT local pair is the image of one rational `h/Q` in the dual S-arithmetic solenoid. Under multiplication by `81/64`, its local coordinates move hyperbolically.

A viable theorem must be quantitative and low-height:

> Every nonzero rational character of numerator at most `K^A` accumulates logarithmic Bernoulli-mask energy over the relevant finite bilateral orbit.

Generic Haar mixing or unique ergodicity is insufficient. The measure is singular and the orbit is a prescribed rational diagonal.

The product formula

\[
|\beta|_\infty|\beta|_2|\beta|_3=1
\]

suggests a conservation law: prolonged resonance at one place must create height or complexity elsewhere. Making that effective is the dynamical offense.

## 9. Direct offense on M1

The open intersection is

\[
\Phi(\Omega)\cap\mathcal I.
\]

### Constructive route

A candidate requires:

1. an exact infinite digit rule;
2. proof that its `2`-adic sum is one ordinary positive integer;
3. proof of the chart congruence;
4. independent reconstruction of the induced-to-Collatz lift.

Compatible finite prefixes may converge only to a `2`-adic ghost.

### Rigidity route

Assume a nontrivial integer intersection and construct an invariant or empirical object from its orbit. Only after proving entropy or a second invariance can measure rigidity engage.

Neither density-one nor all-depth finite equidistribution automatically settles this existence question.

## 10. Computation boundary

`X-9301` remains the only computation. It uses exact modular arithmetic through `K=80`, `h<=K^2` only to falsify lemma shapes.

The next permissible computation is to emit exact lift-digit and least-representative data for existing argmins. It must serve a stated harmonic-location or carry-template lemma. Increasing the brute-force depth alone is not progress.

## 11. Falsification criteria

Revise or abandon a route if:

1. an explicit polynomial-height family has bounded energy along infinitely many depths;
2. low-energy residue classes can be proved to concentrate at the origin with nonvanishing harmonic mass;
3. the lift-prefix bijection or local character crosswalk is inconsistent with the live subsystem;
4. the room tower imports information at least as fast as every available marginal contraction;
5. exceptional-depth carry words have unbounded irreducible complexity;
6. a nontrivial integer-section point is constructed, in which case priority shifts to adversarial candidate verification.

## 12. Best next theorem

The highest-leverage theorem is now a **harmonic exceptional-cylinder bound**:

\[
\boxed{
\sum_{\substack{1\le h\le H\\
\mathcal E_{K,L}(h)\le L/64}}
\frac1h
=o(1)
}
\]

for a growing `L` tied to `H`, uniformly in `K` in the all-depth regime.

Combined with `T-9308`, this would close full all-depth EQ. A proof may proceed through terminal-residue location, carry-template classification, the positive room tower, or rational-diagonal renewal. The packet now exposes all four representations of the same finite obstruction.