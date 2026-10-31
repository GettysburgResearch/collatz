# A dyadic regularity route through softened stopping times

**Status: PROPOSED local theorems with complete arguments below; external density inputs are SOURCE-QUALIFIED. The decisive regularity hypothesis is OPEN. This is not a proof of Collatz.**

Research date: 2026-10-30. Baseline inspected: `GettysburgResearch/collatz` main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. This note is a new analytic bridge, not a claim that positive-density convergence alone closes the conjecture. It does not repeat the earlier density-one-to-all reduction as a new result.

## 1. Maps, clocks, and the target

Use the shortcut map

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n.\end{cases}
\]

Let \(\tau(n)\) be the first shortcut hitting time of 1, with \(\tau(n)=\infty\) if no such time exists. For \(n>1\), finite hitting times satisfy \(\tau(Tn)=\tau(n)-1\), and infinite hitting times remain infinite. The ordinary map \(C\) instead uses \(3n+1\) at odd inputs. Ordinary convergence and shortcut convergence agree; an ordinary step count bounds the shortcut count from above.

The key observable is

\[
F(1)=1,\qquad F(n)=\exp\!\left(-\frac{\tau(n)}{\log n}\right)\quad(n\ge2),
\tag{1}
\]

where \(e^{-\infty}=0\). Unlike the convergence indicator, this observable admits a uniform finite-computation approximation without assuming Collatz. Its invariance defect also tends to zero pointwise, uniformly over every possible finite or infinite hitting time.

The proposed proof target is **dyadic logarithmic regularity of (1)**. This means approximating it, in a precise average norm, by functions of a fixed finite number of low binary digits. This is a sufficient condition, not a condition proved here and not an asserted equivalent reformulation of Collatz.

## 2. Two ordinary-integer seminorms

For a bounded real sequence \(u\), define

\[
\|u\|_{\rm C}=\limsup_{X\to\infty}\frac1X\sum_{1\le n\le X}|u(n)|,
\qquad
\|u\|_{\log}=\limsup_{X\to\infty}\frac1{\log X}
\sum_{1\le n\le X}\frac{|u(n)|}{n}.
\tag{2}
\]

Write \(\mathcal D_{\rm C}\) and \(\mathcal D_{\log}\) for the closures, in these seminorms, of bounded sequences periodic modulo a power of 2. The approximating period is fixed before the cutoff \(X\) tends to infinity. Allowing the period to grow with the tested cutoff changes the condition and does not suffice.

These are seminorms: a nonzero sequence can have zero seminorm. No assertion identifies ordinary integers with typical 2-adic points. The connection below is made through a completed function space, and only for sequences proved to belong to that space.

### DREG-001. Ordinary pullback is bounded

For either norm in (2),

\[
\|u\circ T\|\le2\|u\|.
\tag{3}
\]

**Proof for the Cesaro norm.** The even sources contribute
\(\sum_{m\le X/2}|u(m)|\). The odd sources map injectively to the integers \(m\equiv2\pmod3\) below \((3X+1)/2\). Dropping that residue restriction bounds their sum by the full sum up to \((3X+1)/2\). Divide by \(X\), then take upper limits: the two factors are \(1/2\) and \(3/2\).

**Proof for the logarithmic norm.** Even sources contribute \(\frac12\sum_{m\le X/2}|u(m)|/m\). For odd sources, \(n=(2m-1)/3\), so their weight is

\[
\frac1n=\frac3{2m-1}=\frac3{2m}+O(m^{-2}).
\]

The sum of the error is bounded because \(u\) is bounded. Drop the residue restriction, divide by \(\log X\), and use \(\log(cX)/\log X\to1\). The same factors \(1/2\) and \(3/2\) result. This proves (3).

### DREG-002. Dyadic completion and Liouville theorem

Let \(f\) be bounded. If, for either norm in (2),

\[
f\in\mathcal D,\qquad \|f\circ T-f\|=0,
\tag{4}
\]

then there is a constant \(c\) such that \(\|f-c\|=0\).

**Proof.** A function \(g\) periodic modulo \(2^r\) defines a locally constant function on \(\mathbb Z_2\). For both norms,

\[
\|g\|=2^{-r}\sum_{a\bmod2^r}|g(a)|=\|g\|_{L^1(\mathbb Z_2,\mu)}.
\tag{5}
\]

Here \(\mu\) is Haar probability measure. For the logarithmic version, the elementary harmonic sum in each residue class gives \(\sum_{n\le X,n\equiv a(2^r)}1/n=2^{-r}\log X+O_r(1)\). Thus a sequence of dyadic functions approaching \(f\) is Cauchy in Haar \(L^1\), with limit \(\widehat f\). Equation (5) makes this an isometric identification of the dyadic completion with \(L^1(\mathbb Z_2)\).

The shortcut map extends continuously to \(\mathbb Z_2\) and preserves \(\mu\): each residue modulo \(2^r\) has exactly two inverse residues modulo \(2^{r+1}\), one even and one odd. Therefore Haar pullback is an \(L^1\) isometry. If \(g\) has period \(2^r\), then \(g\circ T\) has period \(2^{r+1}\). Applying (3) to the ordinary approximation errors and using (4) gives

\[
\|g\circ T-g\|\le3\|g-f\|+\|f\circ T-f\|\longrightarrow0.
\]

Consequently \(\widehat f\circ T=\widehat f\) in Haar \(L^1\).

For completeness, the ergodicity used at this point has a finite arithmetic origin. The first \(r\) parities of an orbit are in bijection with the residues modulo \(2^r\). To see the induction step, the two lifts of one residue modulo \(2^r\) differ by \(2^r\); after the prescribed \(r\) parity steps their images differ by the odd integer \(3^s\), where \(s\) is the number of odd steps. Hence the next parity distinguishes the lifts. The full parity map sends Haar measure to independent fair bits and conjugates \(T\) to the one-sided shift. A shift-invariant measurable function is constant, by the tail zero-one law (or by independence of disjoint finite bit blocks followed by approximation). Thus \(\widehat f=c\) almost everywhere. Equation (5) and the approximation of \(f\) now give \(\|f-c\|=0\). This proves DREG-002.

The classical conjugacy is due to Bernstein and Lagarias; the preceding argument supplies the particular norm-transfer facts needed here. The theorem does **not** say that an arbitrary bounded ordinary-integer invariant sequence extends measurably in this manner. That extension is exactly the membership hypothesis in (4).

## 3. A uniformly computable, asymptotically invariant observable

### DREG-003. Softened stopping has a uniform invariance bound

For \(n\ge4\), the observable (1) satisfies

\[
|F(Tn)-F(n)|\le
\frac{1+\log2/e}{\log n-\log2}
\le\frac{2(1+\log2/e)}{\log n}.
\tag{6}
\]

In particular, its invariance defect has zero norm for both seminorms in (2).

**Proof.** If \(\tau(n)=\infty\), both values are zero. Otherwise put \(t=\tau(n)\), \(L=\log n\), and \(L'=\log Tn\). Since \(n/2\le Tn\le2n\), \(|L-L'|\le\log2\). Split the difference between \(e^{-t/L}\) and \(e^{-(t-1)/L'}\) into a change in the clock and a change in \(L\). For fixed \(L'>0\), the absolute derivative with respect to the nonnegative time is at most \(1/L'\). For fixed \(t\ge0\),

\[
\left|\frac{d}{dL}e^{-t/L}\right|
=\frac1L\left(\frac tL\right)e^{-t/L}\le\frac1{eL}.
\]

Both denominator arguments remain at least \(L-\log2\). The mean value theorem gives the first inequality in (6), and \(L\ge2\log2\) gives the second. A bounded sequence tending to zero has zero norm in either (2).

### DREG-004. Total finite-computation approximation

For a fixed positive integer \(M\), put \(b(n)=1+\lfloor\log_2 n\rfloor\) and simulate only \(M b(n)\) shortcut steps. If 1 has been reached, output \(e^{-\tau(n)/\log n}\); otherwise output 0. Call this \(F_M(n)\), with \(F_M(1)=1\). Then

\[
\sup_{n\ge1}|F(n)-F_M(n)|\le e^{-M}.
\tag{7}
\]

Indeed, an unobserved finite hitting time is larger than \(Mb(n)\ge M\log n\); an infinite one already has value 0. The clock is an exact integer and uses no rounding decision about a transcendental number. The output's logarithm and exponential can be evaluated with certified real arithmetic to any specified error. This is uniform approximation of a real observable. It is **not** an algorithm deciding whether its exact value is zero.

### DREG-005. Exact-rational companion

There is a version needing only integer simulation and rational outputs. Put

\[
b(n)=1+\lfloor\log_2 n\rfloor,\qquad
R(n)=\frac{b(n)}{b(n)+\tau(n)},
\tag{8}
\]

with value 0 when \(\tau=\infty\). Thus \(R(1)=1\). Although \(R(n)\) is a rational number at each individual input, the argument supplies its uniform computability **as a real number**, not an algorithm returning its exact rational representation or deciding whether it is zero. For \(n\ge4\),

\[
|R(Tn)-R(n)|\le\frac1{b(n)-1}.
\tag{9}
\]

For integer \(M\ge1\), simulate exactly \(M b(n)\) steps and output \(b(n)/(b(n)+\tau(n))\) if 1 has been reached, otherwise 0. The resulting exact-rational \(R_M\) satisfies

\[
\sup_n |R(n)-R_M(n)|\le\frac1{M+1}.
\tag{10}
\]

**Proof of (9).** Let \(b=b(n)\), \(b'=b(Tn)\), and \(t=\tau(n)\). The infinite case is immediate. Otherwise \(t\ge1\) and \(|b-b'|\le1\), so

\[
\left|\frac{b'}{b'+t-1}-\frac b{b+t}\right|
=\frac{|(b'-b)t+b|}{(b+t)(b'+t-1)}
\le\frac1{b+t-2}\le\frac1{b-1}.
\]

The denominator is positive for the stated inputs. If \(t>Mb\), then \(b/(b+t)<1/(M+1)\), proving (10). This companion makes finite reproducible diagnostics straightforward without turning them into proofs of asymptotic regularity.

## 4. What regularity would now prove

The following two external inputs must be kept distinct.

* **Fast positive density:** Mazur's supplied v2.1 paper states that some fixed positive lower natural density of inputs reaches 1 within \((523/50)\log n\) ordinary steps. This also bounds their shortcut times.
* **Bad-basin amplification:** Mazur's separate predecessor paper states that, for every fixed positive ordinary target \(a\) with \(3\nmid a\), its ordinary predecessor set has positive lower natural density, without assuming \(a\) converges. This gives positive lower density of nonconvergence if any counterexample exists.

### DREG-006. Soft-regularity criterion for the full conjecture

Assume the two source-qualified external inputs above. If **either** \(F\) or \(R\) belongs to \(\mathcal D_{\log}\), then every positive integer reaches 1. Membership in \(\mathcal D_{\rm C}\) also suffices.

**Proof.** DREG-003 or DREG-005 gives zero invariance defect. DREG-002 gives a constant \(c\) with zero approximation error to the observable. On the positive-density fast-convergence set,

\[
F(n)\ge e^{-523/50},\qquad
R(n)\ge\frac1{1+(523/50)\log2}.
\tag{11}
\]

The second inequality uses \(b(n)\ge\log n/\log2\). Therefore the corresponding positive lower bound also holds for \(c\). Otherwise the mean absolute error would be bounded below by a positive constant on a positive-density set.

The logarithmic version uses the elementary implication

\[
\underline d(A)>0\quad\Longrightarrow\quad
\liminf_{X\to\infty}\frac1{\log X}\sum_{n\le X,\ n\in A}\frac1n>0,
\tag{12}
\]

which follows by summation by parts. Thus the preceding argument applies to both norms.

If a counterexample exists, take its odd part and then an ordinary odd step; this supplies a positive target \(a\) with \(3\nmid a\) that is still nonconvergent. Every ordinary predecessor of \(a\) is nonconvergent and hence has observable value 0. The second external input and (12) then force \(c=0\), contradicting (11). This includes both a nontrivial cycle and a trajectory with infinitely many distinct values.

**Exact boundary.** Regularity of \(F\) or \(R\) is not established. It is stronger than merely constructing the observables, proving their small invariance defect, or evaluating them on large finite intervals. It also implies concentration, in the chosen norm, of the softened normalized hitting time around a constant. We do not claim that Collatz alone implies this concentration or the regularity condition.

### DREG-007. Basin-indicator version and pointwise Liouville

Let \(G\) be the convergence basin and let \(f=1_G\). Under the predecessor-density input,

\[
\text{Collatz}\quad\Longleftrightarrow\quad
1_G\in\mathcal D_{\log}
\quad\Longleftrightarrow\quad
1_G\in\mathcal D_{\rm C}.
\tag{13}
\]

For the nontrivial direction, exact invariance and DREG-002 first force density concentration around 0 or 1; positive density of \(G\) excludes 0, and a bad basin excludes 1 if a counterexample exists. The converse is immediate if \(G\) is every positive integer. This equivalence applies to the indicator, **not** to the softer observables of DREG-006.

More generally, any bounded exactly \(T\)-invariant sequence lying in either dyadic completion is pointwise constant. DREG-002 makes it equal to a constant in seminorm. If its value at one integer differed, its whole ordinary predecessor basin would carry that difference; move to a unit target if necessary and use the predecessor-density theorem. Exact \(T\)-invariance implies ordinary \(C\)-invariance because \(C(n)=2T(n)\) at odd \(n\) and \(f(2m)=f(m)\).

## 5. A precise fiber-variance diagnostic

For a bounded \(f\), fix \(r\), and suppose the conditional first and second moments in every residue class modulo \(2^r\) have limits in the chosen sampling convention (ordinary uniform or logarithmic weights). Denote them by \(m_r(a)\) and \(s_r(a)\). The limiting within-class variance is

\[
V_r=2^{-r}\sum_{a\bmod2^r}\bigl(s_r(a)-m_r(a)^2\bigr).
\tag{14}
\]

If these limits exist for all \(r\), then

\[
f\in\mathcal D\quad\Longleftrightarrow\quad V_r\longrightarrow0.
\tag{15}
\]

To prove this, choose the periodic approximation \(g_r(n)=m_r(n\bmod2^r)\). Its limiting mean squared error is exactly \(V_r\), and it is the best such squared-error approximation at that period. These minimum errors are nonincreasing when the period is refined. For uniformly bounded functions, convergence in mean square and mean absolute value are equivalent: Cauchy--Schwarz gives one implication, and \(|x-y|^2\le K|x-y|\) gives the other after clipping approximants to the bounded range of \(f\). Conversely, dyadic approximation implies the existence of the conditional first and second moments: at each **fixed** resolution \(r\), the conditional error is at most \(2^r\) times the global approximation error, and clipping also controls the difference of squares. The approximation error then tends to zero with \(r\) still fixed. Thus (15), with that existence condition included, is an exact characterization.

For an indicator, \(s_r=m_r\), and the variance becomes

\[
I_r=2^{-r}\sum_a m_r(a)(1-m_r(a)).
\]

It lies between one half and one times the best limiting binary-classification error. Thus a hypothetical mixture of convergent and nonconvergent basins must either prevent some required conditional limits or retain nonvanishing impurity at arbitrarily fine fixed dyadic resolutions.

**Finite diagnostic caveat.** Replacing these limiting moments by data on \([1,X]\) is a discovery experiment only. Small empirical variance at growing periods, or changing the residue labels with \(X\), does not establish (15). The limits in \(X\) come first, and the period is then increased. For the soft observables, the uniform approximation (7) or (10) permits bounded-time evaluation to a prescribed numerical error, but does not supply uniform convergence of their empirical residue moments.

## 6. Why the most immediate shortcuts fail

1. **Haar ergodicity alone.** It acts on a completed probability space, while all positive ordinary integers form a Haar-null subset. DREG-002 requires the ordinary-norm approximation that connects the two spaces.
2. **Pointwise small invariance defect.** This is already proved for (1) and (8), yet it does not imply their dyadic regularity. Near-invariant dyadic functions and slowly varying height functions supply independent negative controls, developed in the companion root note.
3. **Fixed hitting-time cutoffs.** For every fixed integer \(K\), the set \(\{n:\tau(n)\le K\}\) is finite: backwards from 1, every shortcut predecessor is at most twice its target, so every such source is at most \(2^K\). These cutoff indicators all have zero norm in (2), although their pointwise limit \(1_G\) has positive density by the external theorem. Pointwise convergence is therefore insufficient for the required norm convergence.
4. **The new explicit target density is still too weak for least-source descent.** Lau's source-qualified theorem gives density \(D^{-1}t^{-25/11}\), with \(D=2^{2^{2^{163}}}\). At cutoff \(N=t\), its lower count is \(\lfloor D^{-1}t^{-14/11}\rfloor=0\). It supplies no predecessor below the target and therefore no automatic contradiction with a least counterexample.

## 7. Concrete continuation

The next lemma should exploit the *hitting-time structure* of \(F_M\) or \(R_M\), not generic approximate invariance. One sufficient target is to prove existence of their conditional dyadic first/second moments, with a variance bound tending to zero as the fixed resolution increases, uniformly enough in the truncation parameter to pass using (7) or (10). A weaker sufficient target is to prove dyadic approximation directly only for the limiting observable.

The bounded experiments accompanying this note measure finite versions of (14), record the approximation error budget, and check the exact rational defect identity. They cannot certify regularity from a finite range. They are intended to identify which residue effects survive a change of scale and which disappear when the sampling interval is enlarged.

The replay `python -X utf8 -B experiments/beeping-density-swarm-20261030/check_density_bridge.py --maximum 100000 --output /tmp/density-bridge.json` completed successfully. It checked 24,180 scalar instances of the rational identity, 99,997 finite-orbit instances, and the parity bijection/Haar residue balance through 12 bits. All 100,000 tested inputs reached 1 inside the reference clock \(32b(n)\); the longest observed shortcut time was 221, at 77,031. These are finite observations only. At \(X=100000\), the empirical ordinary within-class variance of \(R_{32}\) decreased from approximately 0.005497 at zero bits to 0.004737 at eight bits. The logarithmic version at eight bits was approximately 0.006858. In particular, these modest fixed resolutions do not remove the observed variance; no extrapolation to (15) is claimed.

## 8. Sources and verification boundary

* Lech Mazur, *Explicit Positive-Density Collatz Convergence in Logarithmic Time*, manuscript v2.1, 2026-09-06, supplied PDF: <https://www.proofatlas.ai/papers/positive-density-log-time-collatz/Mazur_Explicit_Positive_Density_Collatz_Convergence_in_Logarithmic_Time_v2.pdf>. Read the full 13-page exposition. The theorem counts ordinary steps and strictly sub-cutoff positive starts.
* Current source/evidence: <https://www.proofatlas.ai/sources/positive-density-log-time-collatz/> and <https://www.proofatlas.ai/proofs/artifact.collatz.positive_density_log_time.lean-package.v003.html>. The reported pinned source is `830b9d3f38f2a8da8cd921bf6a9310dd69336fd0`; the evidence reports a successful build and no `sorryAx`/unexpected axioms, with accepted-result publication pending. These are source-reported checks, not a build replay by this pass.
* Lech Mazur, *Positive Lower Density of Collatz Predecessors*, v1.0, 2026-09-06: <https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf>; current theorem page <https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/>. Inspected the proof's target-uniformity and no-return requirements. The reported assembled source is `c290ac229b379d2b51026d3e86140496870d6f39`. Density constants are target-dependent. This pass did not replay its Lean closure.
* Kenny Lau, *Explicit positive lower density for the Collatz Conjecture*, Hexagon `2610.00249v2`, current version dated 2026-10-21 in the version history: <https://hexagonmath.org/2610.00249v2>, PDF <https://hexagonmath.org/pdf/2610.00249v2>. Inspected the introduction, target-dependent theorem, seed construction, count assembly, and verification appendix. The 71-page development and Lean dependency closure were not fully replayed. The identifier is a **Hexagon** identifier, not an arXiv identifier.
* Daniel J. Bernstein and Jeffrey C. Lagarias, *The 3x+1 Conjugacy Map*: <https://websites.umich.edu/~lagarias/doc/bernstein.pdf>. Classical source for the 2-adic parity conjugacy and measure preservation.

No third-party PDF is redistributed. Source descriptions above are limited scope/provenance notes; the mathematical arguments in Sections 2--7 are the local research contribution. The external density theorems remain separate assumptions wherever used, even though their public packages report formal checks.
