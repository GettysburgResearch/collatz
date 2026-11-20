# A complete energy comparison from one multiplicative-five slice

**Status: PROPOSED, elementary comparison theorem with an exact universal affine certificate.** The comparison closes the particular global propagation question left OPEN in PR160, `critical/SINGLE_SLICE_ENERGY.md`, SE-002. It does not prove that the required energy is finite, does not prove physical multiplier-five closure, and does not resolve Collatz.

## 1. Map, domain, and statement

Let

\[
 T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

Let \(f:\mathbb N_{>0}\to(Y,d)\) be any map into a metric space with
\(f(Tn)=f(n)\) for every positive integer. No boundedness is assumed.
Set

\[
 e_5(x)=d(f(5x),f(x)),\qquad
 E_5(s)=\sum_{\substack{x>0\\x\text{ odd},\;3\nmid x}}x^{-s}e_5(x),
\]
\[
 D_3(s)=\sum_{n>0}n^{-s}d(f(3n),f(n)),\qquad s>0.
\]

All series are nonnegative extended sums. In particular no summability is assumed before proving the inequalities.

**Theorem FE1.** For every \(s>0\),

\[
 \boxed{D_3(s)\le
 \frac{248(7153/21)^s}{(1-2^{-s})^2}\,E_5(s).}
 \tag{1}
\]

At the harmonic endpoint a sharper sum of individual query ratios gives

\[
 \boxed{D_3(1)<10000E_5(1)}
 \tag{2}
\]

whenever \(0<E_5(1)<\infty\); the non-strict version with constant 10000 holds in all extended cases, including zero and infinity.

The five domain is exactly **odd positive ternary units, compared with their products by five**. In the old notation \(t=4x\), this is the single five-ray slice \(v_2(t)=2,\;3\nmid t\): ordinary paths identify \(f(20x+1)=f(5x)\) and \(f(4x)=f(x)\). Thus

\[
 \sum_{\substack{v_2(t)=2\\3\nmid t}}
 t^{-s}d(f(5t+1),f(t))=4^{-s}E_5(s).
 \tag{3}
\]

No query at an odd multiple of three is admitted.

## 2. The finite affine certificate

The accompanying `five_cover_candidates.json` contains 67 pairs of words, with 109 positive odd residue cells in total. The common modulus is

\[
 P=2{,}073{,}600=2^{10}3^4 5^2.
\]

Its cells cover all 1,036,800 odd residues modulo \(P\), with overlap allowed. Each word pair starts at \(n\) and \(3n\), respectively, and ends at **identical affine expressions** on every integer in its cell. The longest pair has 24 moves. Across the 67 pairs there are 1,172 moves and 248 five queries.

A cell means \(n=mu+r\), \(u\ge0\), with \(0<r<m\) odd. The moves are:

| Symbol | Move | Guard | Label change |
|---|---|---|---|
| D | \(v\mapsto2v\) | positive integer | zero |
| E | \(v\mapsto v/2\) | even positive integer | zero |
| O | \(v\mapsto(3v+1)/2\) | odd positive integer | zero |
| I | \(v\mapsto(2v-1)/3\) | resulting value is positive odd integer | zero |
| M | \(v\mapsto5v\) | \(3\nmid v\) | \(e_5(v)\) |
| V | \(v\mapsto v/5\) | \(5\mid v,\;3\nmid v\) | \(e_5(v/5)\) |

The five-query parameter can be even. This is handled exactly in Section 3, not replaced by an assumption of bounded odd-part multiplicity.

For a simple example, all positive \(n\equiv7,11\pmod{12}\) are covered by the two words

\[
 n\xrightarrow{M,O}\frac{15n+1}{2},\qquad
 3n\xrightarrow{O,E,M,I}\frac{15n+1}{2}.
\]

The second arm goes successively through \((9n+1)/2\), \((9n+1)/4\), \(5(9n+1)/4\), and \((15n+1)/2\). Every parity and integrality guard holds on those whole cells; both five parameters are ternary units.

The verifier does not infer universality from sampled orbits. For each residue cell it starts with the coefficient pairs \((m,r)\) and \((3m,3r)\), and checks each operation on the integer affine expression \(au+b\). In particular:

- positivity is \(a>0,b>0\), valid for every \(u\ge0\);
- E and O check the exact parities of both coefficients;
- I checks divisibility by three and that the resulting coefficients give odd values for every lift;
- M requires \(3\mid a\) and \(3\nmid b\);
- V checks divisibility of both coefficients by five and the same ternary-unit condition after division;
- the endpoint coefficient pairs agree exactly.

Finally, it expands the residue cells to the stated common modulus and checks the complete odd cover. This is a finite exhaustive check of an infinite family of affine identities, not a finite-start extrapolation. The search that found the words is not a proof dependency.

These paths are in an augmented comparison graph. M and V are not declared ordinary Collatz edges. Their nonzero label changes are retained in full.

## 3. Positive all-source congestion bound

On one row let \(Q_j(n)=\alpha_jn+\beta_j\) be its query parameters, before M or after V as appropriate. They have positive slopes and are positive ternary units on every eligible source. The triangle inequality along the two paths gives

\[
 d(f(3n),f(n))\le\sum_j e_5(Q_j(n)).
 \tag{4}
\]

For a query with expression \(au+b\) in the cell \(n=mu+r\),

\[
 \sup_{u\ge0}\frac{au+b}{mu+r}
 =\max\{a/m,b/r\}.
 \tag{5}
\]

If a row has several residues, take the maximum of (5) over those residues. Call the resulting bound \(H_j\). The map \(Q_j\) is injective on the union of those residue cells: it is the same positive-slope affine function of \(n\) there. Hence, by positive summation,

\[
 \sum_{n\text{ in row}}n^{-s}e_5(Q_j(n))
 \le H_j^s\sum_{\substack{y>0\\3\nmid y}}y^{-s}e_5(y).
 \tag{6}
\]

Exact doubling invariance gives \(e_5(2^v x)=e_5(x)\). Partition the last sum by its odd part:

\[
 \sum_{3\nmid y}y^{-s}e_5(y)
 =\frac{E_5(s)}{1-2^{-s}}.
 \tag{7}
\]

Thus the infinite possible multiplicity after stripping powers of two is accounted for by its full convergent geometric series. No finite-source truncation or independence hypothesis is used.

Every odd source belongs to at least one row. Sum (4) on all rows; overlap only enlarges the nonnegative right side. Equations (6)--(7) prove

\[
 \sum_{n\text{ odd}}n^{-s}d(f(3n),f(n))
 \le\frac{K_s}{1-2^{-s}}E_5(s),\qquad K_s=\sum_jH_j^s.
 \tag{8}
\]

There are 248 row-query occurrences, and the exact coefficient checks give

\[
 H_j\le7153/21.
\]

Doubling the tripling defect as in (7) gives (1). At \(s=1\), the exact sum is

\[
 K_1=
 \frac{2890739393835460424046931534118546302327}
 {1265433188657605285832552427069681000}<2500.
 \tag{9}
\]

Consequently \(D_3(1)\le4K_1 E_5(1)\), proving (2). The verifier reconstructs every \(H_j\), the rational sum, and the strict rational comparison in (9).

## 4. Consequences with source boundaries retained

These are consequences of FE1, not new proofs of the named predecessor or coercivity inputs.

### Subcritical coercivity

For bounded real invariant \(f\) and \(0<s<1\), if \(E_5(s)<\infty\), PR155 OD3 applied after FE1 gives a unique constant \(c\) with

\[
 \sum_{n>0}|f(n)-c|n^{-s}<\infty.
\]

For a Boolean label, \(c\in\{0,1\}\). If every ordinary component has divergent \(s\)-moment, this forces constancy. In particular the source-qualified Krasikov--Lagarias predecessor input at \(s=0.84\) yields this implication. For arbitrary real labels, clip between two distinct values; for arbitrary metric labels, apply the bounded 1-Lipschitz function \(y\mapsto\min(d(y,f(a)),d(f(a),f(b)))\). Either construction has defect bounded by the original metric defect and reduces constancy to the bounded real case.

### Harmonic finite-energy rigidity

Under the named fixed-target positive-lower-density input PD in PR160, the implication

\[
 \boxed{E_5(1)<\infty\quad\Longrightarrow\quad f\text{ is constant}}
 \tag{10}
\]

holds for arbitrary metric invariant labels. Indeed FE1 makes the full harmonic tripling energy finite. PR155's endpoint theorem gives a constant logarithmic-profile limit after any separating bounded Lipschitz test. PD makes each of the two separated components have positive lower density, contradicting that constant limit. This is exactly the missing global transport in PR160 SE-002, now provided by (1). PD remains source-qualified; no external Lean build is claimed here.

### Abscissae below one

Let \(K\) be an invariant set with \(\sigma_K<1\), and let
\(B_5^{\rm unit}=\{x>0:x\text{ odd},\;3\nmid x,\;1_K(5x)\ne1_K(x)\}\).
Then its Dirichlet abscissa equals \(\sigma_K\), and at any positive common abscissa below one its critical moment converges exactly when the component moment does. One direction is the elementary estimate

\[
 \sum_{x\in B_5^{\rm unit}}x^{-s}\le(1+5^s)\sum_{n\in K}n^{-s}.
\]

The other follows from FE1 and PR155 OD4 for the tripling boundary, or from OD3 with the constant forced to zero because the complement has divergent \(s\)-moment for \(s<1\). This extends the earlier full-five-ray comparison to the single legal multiplicative-five domain.

## 5. What remains to prove

No bound \(E_5(1)<\infty\) has been established for the indicator of a hypothetical proper component. Neither the finite certificate nor (1) produces that upper bound. The reverse energy inequality is not supplied: the known square-root logarithmic upper count for ordinary tripling failures does not transfer through (1) to five failures.

There is also no one-sided version being asserted. The paths retain both M and V moves. In contrast to PR159's directed tripling circulation, a uniformly bounded affine return from \(5x\) to \(x\) using only forward-five moves and ordinary edges is impossible by prime factorization of slopes: its net slope would be a product of powers of 2 and 3 times a nonnegative power of 5, and could not equal \(1/5\). This does not prohibit nonuniform directed paths or a different analytic proof of an oriented estimate.

The actual positive-return sublog occupation upper bound in PR157 remains OPEN. FE1 addresses a different precisely stated analytic propagation gap and does not assert a bound on that Green functional.

## 6. Exact source pins

- PR160, `6d877e718f5ef9d57fe1830912c444359718747a`, `research/closure-attacks-20261120/critical/SINGLE_SLICE_ENERGY.md`, SE-001/002: two local quinary classes and the previously open finite-energy propagation problem.
- PR160 at the same head, `critical/CRITICAL_SINGULARITY.md`, PD/UP/EP and CS-003: source-qualified harmonic metric-label rigidity and the explicit PD dependency.
- PR155, `92f499b9d340d1ff8cc643c3eef3477d61b477c1`, `research/gemini-dirichlet-global-20261120/ORDINARY_DIRICHLET_COERCIVITY.md`, OD2--OD4, and `ENDPOINT_BOUNDARY.md`: imported coercivity and profile limit.
- PR159, `0e7d2841b1591073c6399f91f3b6944ebcdbdbd5`, `research/allhands-global-closure-20261120/DIRECTED_BOUNDARY_CIRCULATION.md`, DC3: the separately source-qualified predecessor moment input and its metric/real-label reduction.
- PR157, `64361ecca770092d6c8242dc6211e38818af2e50`, `research/global-closure-20261120/merger.md`, GCM-002: the stronger one-sided *zero-defect basin* criterion, which is not newly claimed here. Its `transport.md`, GCT-001/002, remains the distinct positive-source occupation target.

## 7. Executed verification

`check_five_energy.py` has no search-program imports. It checks all affine cells, complete coverage, query domains, and positive weight constants. It also performs 9,620 bounded literal move checks as a separate diagnostic and rejects eight damaged certificates. It runs under normal and `-OO` Python, with identical report bytes. `five_energy_report.json` records the actual execution and scope. The universal claim rests on the affine proof and full residue cover, not on the diagnostic sampled lifts. Independent review by a second author is still required before integration.
