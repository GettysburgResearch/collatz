# Proof program: from averaged cusp decay to an all-depth theorem

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Status:** research program; every unproved step is labeled

## 1. Exact boundary after the current packet

The one-place route is

```text
D-9301  fixed Z_2 survivor measure
   |
   v
L-9301  moving-character identity
   |
   +--------------------------+
   |                          |
   v                          v
L-9303 phase energy       D-9302 adelic natural extension
   |                          |
   v                          v
C-9301 / energy target    Q-9301 integer-section intersection
   |
   v
T-9301 polynomial-window reduction
   ^
   |
L-9302 weighted shell tail  <--- frequency block mean (branch-qualified)
```

The density-one route is

```text
L-9304 exact phase reciprocity
   |
   v
T-9303 valuation-stratified depth periods
   |
   + frequency block mean
   v
T-9302 full weighted EQ on density-one depths
```

The room/Cantor route is now

```text
D-9303 fixed Z_3 mirror measure
   |
   v
L-9305 triadic moving-character identity
   |
   + L-9301
   v
T-9304 exact CRT product factorization
   |
   +-----------------------------+
   |                             |
   v                             v
L-9306 full-group moments    L-9307/L-9308 one stitched phase chain
                                 |
                                 v
                          T-9305/T-9306 split collapse
```

The split-collapse theorems prove that in every range

\[
H=o(64^K),
\]

the original survivor coefficients, the triadic mirror coefficients, and every CRT split are equivalent—both in magnitude and against arbitrary bounded harmonic tests—up to `O(H/64^K)`.

Therefore the all-depth EQ problem is concentrated in one sentence:

> Exclude a polynomial-height rational character whose common reciprocal phase chain has only `O(log K)` energy at infinitely many depths.

The direct M1 problem remains different:

> Determine whether the symbolic stable leaf `Phi(Omega)` meets the ordinary-integer section `I` outside the two trivial endpoints.

EQ can hold while one exceptional M1 point survives. These objectives must not be conflated.

## 2. What split collapse rules out

`L-9307` and `L-9308` show that the two local CRT character classes are the images of one rational

\[
r=\frac h{64^n81^j}
\]

and that their Bernoulli factors stitch the chain

\[
q_\ell(h)
\equiv
-17h64^{\ell-K}
\pmod{81^{\ell+1}},
\qquad
0\le\ell<K.
\tag{1}
\]

`T-9305` and `T-9306` imply the following methodological restrictions.

1. **No weaker absolute target.** Proving decay of the two-place absolute product in the EQ range already proves the original EQ criterion.
2. **No different bounded signed target.** Every bounded harmonic test of the complex two-place coefficients is asymptotically the corresponding one-place test.
3. **No independent local-energy heuristic.** The local factors are adjacent pieces of one chain, not independent samples.
4. **Full-group moments are insufficient.** The complete dual group factors, but the rational diagonal may still be exceptional.
5. **Position transfer is not the missing Fourier step.** Ordered-position rigidity remains important geometrically, but the absolute and complex coefficient comparisons are now direct.

A two-place proof can still be valuable. Its value must come from a better representation of the **same chain**, not from a weaker conclusion.

## 3. Offense A: bilateral low-energy inverse theorem

### Target statement

Prove a finite theorem of the following form.

> **Bilateral low-energy inverse theorem, tentative.** There are constants `A,C,c>0` such that if
+> \[
+> 1\le h\le K^A
+> \]
+> and the phase energy of `(1)` is at most `C log K`, then one of the following holds:
+> 1. `h` has an exact `64`-power reduction;
+> 2. `h` has an exact `81`-valuation loss;
+> 3. the carry sequence belongs to one of finitely many bounded-complexity templates;
+> 4. a full block of at least `K^c` nearby frequencies inherits comparable low energy.

The first two outcomes reduce the problem to smaller parameters. The fourth contradicts the frequency-block mean for suitable constants. The third becomes a finite classification problem.

### Exact carry recurrence

Let

\[
y_\ell(h)=\frac{q_\ell(h)}{81^{\ell+1}}.
\]

Reduction of `(1)` from level `ell+1` to level `ell` gives

\[
q_{\ell+1}
\equiv64q_\ell
\pmod{81^{\ell+1}}.
\]

Writing the new lift digit as `j_ell in {0,...,80}` yields

\[
\boxed{
y_{\ell+1}
=
\frac{\{64y_\ell\}+j_\ell}{81}.
}
\tag{2}
\]

This is the deterministic chain underneath the Markov decompositions in issue #4. A low-energy exception is a path of `(2)` that spends too much time near the annihilator of the Bernoulli mask.

### Robustness-or-loss dichotomy

For every level record:

- the distance of `y_ell` from an integer;
- the distance from the boundary of a chosen degeneracy window;
- the lift digit `j_ell`;
- the carry discarded by `{64 y_ell}`.

Seek a dichotomy:

1. at least `c log K` levels lie in boundary annuli, and their moderate cosine loss proves polynomial decay;
2. many degenerate levels have robust margins, and the corresponding carry constraints persist under a structured frequency perturbation.

The perturbation set may be an arithmetic progression rather than a consecutive interval. A successful proof must include a transference from that progression to the arbitrary-block frequency theorem or combine several scales until a full block appears.

## 4. Offense B: specialized `{2,3}` height gap

The dyadic signed representatives satisfy exact equations

\[
17h
=
81^{\ell+1}s_\ell
+
64^{K-\ell}m_\ell.
\tag{3}
\]

A low-energy path has many `s_ell` small relative to `64^(K-ell)`. Choose logarithmically many separated levels and eliminate `h` between their equations. This produces exact four-term `{2,3}`-unit relations.

The desired specialized lemma is:

> If `(3)` is simultaneously very small at `L` separated levels, then `h` is divisible by a power of `64` or `81` exponential in `L`, unless the carries lie in one of finitely many explicitly classifiable templates.

For

\[
h\le K^A,
\]

an exponential divisibility conclusion with `L` proportional to `log K` closes the energy target.

Invoking the phrase “S-unit theorem” is not enough. The proof needs effective uniformity in the moving exponents and must exploit

\[
\gcd(64,81)=1,
\qquad
17\nmid64\cdot81.
\]

## 5. Offense C: positive room-tower transfer

Issue #4 now identifies the base-`81` room digits as wrap counts of successive `H`-steps. The first marginal contracts empirically, but reconstruction at modulus `81` requires joint information at modulus `81^2`, and in general every level is driven by the next. This is an inverse-limit skew product.

Absolute Fourier products may be a poor proof language below the fair window because exact copies defeat majorants. The alternative program is:

1. write the exact tower kernel on `Z_3` using `D-9303`;
2. preserve the deterministic period-9 twist from multiplication by `64`;
3. define a positive observable measuring interval mass, relative entropy, or room imbalance;
4. prove contraction after one full twist period while controlling the information imported from the next tower level;
5. iterate without closing at a false finite modulus.

A useful theorem would bound the information flux from level `m+1` to level `m` by less than the proven nine-step marginal contraction.

## 6. Offense D: hyperbolic renewal on the rational diagonal

`D-9302` places the system in

\[
(\mathbb R\times\mathbb Q_2\times\mathbb Q_3)
/
\Delta\mathbb Z[1/6]
\]

under multiplication by `81/64`.

The CRT character pair is the local image of one rational `h/Q`, not an arbitrary point of the product dual. A dynamical theorem should therefore be stated directly on this rational diagonal:

> Every nonzero rational character of numerator at most `K^A` accumulates at least `c log K` total mask energy along the relevant finite bilateral orbit.

Generic mixing is insufficient. The measure is singular, the orbit has low rational height, and the constants must be uniform in the cusp parameters.

The product formula

\[
|\beta|_\infty|\beta|_2|\beta|_3=1
\]

suggests a conservation principle: prolonged resonance at one expanding place must generate complexity at another place or in the real height. Turning that principle into a quantitative return bound is the conceptual dynamical target.

## 7. Exceptional-depth coherence

`T-9302` proves full weighted EQ on a density-one set of depths. The remaining exceptional set may still be infinite.

A depth bad at several adjacent scales must simultaneously defeat:

- the valuation-stratified period averages;
- the frequency-block tail estimate;
- the exact room-tower contraction at its first marginal.

The proposed inverse theorem is:

> Multi-scale exceptional depths force a coherent bounded-height carry word across several adjacent `81`-adic annuli.

Once such a word is exposed, either classify it arithmetically or amplify it to excessive frequency-block mass.

## 8. Direct offense on M1

The exact open intersection is

\[
\Phi(\Omega)\cap\mathcal I.
\]

### Constructive program

Seek a finitely generated but nonautomatic itinerary whose solenoid point lies in the integer section. A candidate must include:

1. an exact infinite digit rule;
2. proof that its `2`-adic sum is one ordinary positive integer;
3. proof of the required chart congruence;
4. independent reconstruction of the induced-to-Collatz translation.

Compatible prefixes alone may converge to a `2`-adic ghost.

### Rigidity program

Assume a nontrivial integer intersection and construct an invariant or empirical object from its orbit. Determine whether the shared itinerary forces positive entropy, a second multiplicatively independent invariance, or concentration on a forbidden rational subsolenoid.

No such consequence is presently proved. Measure rigidity cannot engage until the invariant object and its hypotheses are explicit.

## 9. Computation boundary

Computation remains limited to lemma discovery and falsification.

`X-9301` scans

\[
K\le80,
\qquad
1\le h\le K^2
\]

with exact modular arithmetic. The next permissible extension is to emit complete carry and lift-digit paths for selected worst cases. Merely increasing the depth bound is not a research result.

## 10. Falsification criteria

Revise or abandon the corresponding route if any of the following occurs:

1. an explicit polynomial-height family has bounded phase energy along infinitely many depths;
2. one exceptional frequency remains isolated and defeats every amplification mechanism while respecting the block mean;
3. the issue-#4 frequency-block theorem fails the arbitrary-consecutive-block quantifier;
4. the character or word-order crosswalk is inconsistent with the live subsystem;
5. the room tower imports information at a rate at least as large as every available marginal contraction;
6. a direct nontrivial integer-section point is constructed, in which case priority shifts immediately to adversarial verification.

## 11. Best next theorem

The highest-leverage next result is now:

> **Carry-template inverse theorem.** Every polynomial-height low-energy chain `(q_ell)` admits a bounded-complexity lift-digit description. Every such description either reduces by an exact power of `64` or `81`, is arithmetically impossible, or persists on enough nearby frequencies to contradict the arbitrary-block mean.

This theorem would close `C-9301` in energy form and therefore close all-depth EQ through `T-9301`. The split-collapse results guarantee that it may be proved in whichever of the dyadic, triadic, room, or solenoid representations makes the carry structure most transparent.