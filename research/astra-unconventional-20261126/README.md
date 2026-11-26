# Ordinary phase returns, exact inverse fibers, and tests of global proof strategies

**Collatz remains OPEN.** This pass proves thirteen infinite-family exclusions at a least canonical reverse disagreement, reduces the bounded three-odd upper-hit alternative to one explicit Mersenne family, and proves a full qualitative theorem on ordinary inverse paths with both grades prescribed. It also develops exact source-minimum laws, integral moment lattices, a pointed spectrum for a hypothetical escaping component, and complete essential- and rooted point-spectrum results for specified transfer operators. None supplies the remaining universal merger or excludes every positive nontrivial cycle.

The positive shortcut is
\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]
`Good n`, also written \(C(n)\), means that this actual positive ordinary orbit hits one. A shortcut clock counts each application of \(T\); an odd grade counts odd inputs. These two counts must not be interchanged. A rational numerator model and a modified-carry model are explicitly labeled when used.

## 1. Thirteen infinite progressions now have a formal return

At a least canonical reverse disagreement \(z\), the existing quantitative return supplies
\[
 \mathcal F(z):\quad \forall n>0,\quad 2^{40}n<z\Longrightarrow C(n).
\]
The new theorem proves \(\mathcal F(z_t)\Rightarrow C(z_t)\) at **every** parameter of each of thirteen explicit progressions. These progressions therefore contain no least canonical reverse disagreement. The floor is a real hypothesis of the formal theorem; it is not an assertion of convergence for an arbitrary supplied source without that hypothesis.

For example, for every integer \(t\ge0\), put
\[
 z_t=\frac{2^{147+1782t}-15-2^{25}}{81}.
\]
Its actual lower path satisfies
\[
 T^{147+1782t}(z_t)=3^{80+1134t}-17.
\]
The ordinary integer
\[
 w_t=2^{118+1701t}-5
\]
merges with that lower path, and hence \(C(w_t)\iff C(z_t)\). For \(t\ge1\), \(2^{40}w_t<z_t\). The remaining base \(z_0\) hits one in 675 shortcut steps. The gain is 81 binary height bits per parameter increment, so the argument covers all parameters without a growing computation.

The mechanism combines two different negative periodic phases while realizing both arms on positive ordinary inputs:
\[
 C(3^{2k+2}-17)\iff C(2^{3k+1}-5),\qquad k\ge1.
\]
The signed \(-17\) cycle uses eleven clocks and seven odd inputs; the signed \(-5\) cycle uses three clocks and two odd inputs. A three-clock ordinary merger joins their positive lifts. All thirteen base words, the exceptional finite bases, the all-parameter scale comparisons, and the first upper hits are kernel-checked.

[Full table and proof](renormalization/PHASE_RETURN.md) · [Phase transfer](renormalization/PhaseReturn.lean) · [All thirteen formal families](renormalization/PhaseFamilies.lean)

The remaining third-odd exponents and phases, and arbitrary upper odd counts, are still open. In particular this does not settle the previously isolated \(e=6\) family.

## 2. Ordinary inverse routing with both exact grades

For every fixed positive odd endpoint \(y\) with \(3\nmid y\), and every positive modulus \(M\), the new Lean theorem proves
\[
 \exists K\;\forall k\ge K\;\exists H\;\forall E\ge H\;\forall a<M\;
 \exists n>0:
 \begin{cases}
 n\text{ odd},\\
 n\equiv2a+1\pmod M,\\
 T^E(n)=y,\\
 \#\{i<E:T^i(n)\text{ odd}\}=k.
 \end{cases}
\]
Thus every compatible residue occurs at the **same supplied** odd depth and clock. There is no remaining interval-width or reachability premise in `GradedBasin.joint_source_and_grades`.

The written proof gives a sharper logarithmic odd-depth threshold, explicit clock compression, and a complete residue-fiber description for rational numerator lattices. It distinguishes an ordinary cycle candidate from a reduced rational cycle at the whole determinant \(D=2^h-3^p\): an ordinary predecessor basin reaches zero modulo \(D\); a reduced denominator \(d>1\) dividing \(D\) obstructs that residue. The ordinary witness may be far above every available descent threshold. Congruence reachability alone does not contradict a cycle minimum.

[Routing statements, proofs and exact formal boundary](cycle/README.md) · [Full qualitative Lean theorem](cycle/GradedBasin.lean)

## 3. Stronger constraints on a bounded ordinary counterexample

If \(q\) is a least tripling disagreement, every bad positive integer \(n\) has a bad multiple of three at height at most \(2n+1\). Hence \(2n+1\ge3q\). The sharp floor is attributed to the existing literature in the lane proof, not claimed as a new discovery here.

On the bounded branch, \(s=(3q-1)/2\) is consequently the globally least bad integer, including other components. At every odd phase \(x\) of the candidate cycle, the new ordinary consequences include
\[
 C(x-1),\qquad C(x+1),\qquad C(2x-1).
\]
Every maximal odd-run entry also supplies an oriented good/bad tripling pair. The formal modules prove these implications using the actual shortcut map and explicit ordinary hypotheses.

The same global floor restricts competing inverse clocks. One-lap and many-lap versions have different requirements: the many-lap conclusion uses the separately pinned, replayed \(p\ll s^{0.49}\) height-strip certificate. A weaker displayed one-lap estimate is not silently reused for that conclusion.

[Proofs, attribution, hypotheses and rational controls](cycle/GOOD_NEIGHBORS.md) · [Global floor](cycle/GlobalFloor.lean) · [Neighbor consequences](cycle/GoodNeighbors.lean)

### A much stronger canonical floor and a single remaining three-odd family

Let \(z\) be the least canonical reverse disagreement on this bounded branch. The descending run into the global minimum \(s\) has length
\[
 r=v_3(s-1)\in\{2,3,4,5\}.
\]
Its opening phase \(x\) is itself canonical and has a good triple. Consequently
\[
 s\le z\le x=1+(4/3)^r(s-1),\qquad
 s\ge1+\frac{243}{1024}(z-1).
\]
The last inequality replaces the earlier \(z/2^{40}\) floor **on this branch**. If \(4^r\mid z-1\), the actual \(2r\)-clock descent and the global minimum force \(z=x\). In particular every such least canonical source lies on the cycle when \(r=2\). The new Lean theorem extracts the descending run from six native backward edges under the displayed bounded-branch hypotheses and proves this floor and equality condition.

Now suppose the first upper hit of \(3z\) uses exactly three odd departures. The prior restriction gives \(6\le e\le48\) in
\[
 81z+15+2^{e+2}=2^H.
\]
Short ordinary prefixes below the stronger floor eliminate almost every \(e\). A nonnative visitor eliminates \(e=7\). At \(e=8\) and \(e=10\), the fifth lower iterate is a **smaller canonical** bad source whose triple reaches below the floor, contradicting canonical leastness. The actual all-parameter merger identities and strict scale comparisons are kernel-checked.

| Descending run into \(s\) | Remaining middle even gap \(e\) |
| --- | --- |
| \(r=2\) | None |
| \(r=3,4,5\) | Only \(e=6\) |

At \(r=2\), the remaining \(e=6\) source is on the cycle; its long all-odd ramp violates the bounded ceiling. At \(r=3,4,5\), a surviving source must reach the **first bad Mersenne** \(M_j=2^j-1\), with \(j=11\bmod162\), while \(3M_j\) is good. That smaller reverse disagreement has residue \(31\bmod48\), so it does not yet contradict leastness in the canonical class \(17\bmod48\).

[Bounded canonical floor and exact assumptions](cycle/CANONICAL_FLOOR.md) · [Formal floor and capture](cycle/CanonicalFloor.lean) · [Three-odd reduction](renormalization/BOUNDED_RANK_THREE.md) · [Formal prefixes and smaller canonical returns](renormalization/RankThreeFloor.lean)

The remaining row also has a precise obstruction to finite fixed-word searches. At the single ternary limiting parameter \(N_*=590\), an all-word denominator argument reduces every eligible low-slope endpoint from \(N-1\) or \(2N-1\) to 932 ordinary starting integers. Exhausting their complete finite orbits leaves eight affine forms, with the original parent as the sole canonical one. Consequently no finite ternary-cylinder cover by this specified word grammar closes the row through the three stated floor/canonical tests. An unbounded selector depending on the actual ordinary exponent is still possible. This followup is a written theorem with an exact finite replay, not a Lean theorem.

[All-word reduction and finite-cover obstruction](renormalization/FINITE_COVER_BARRIER.md)

## 4. Exact optimization reveals what a reset must accomplish

For an all-odd ascent from \(x=2^ra-1\) to \(y=3^ra-1\), let \(L(r)\) be the least signed clock with \(r\) odd inputs ending at \(-2\), and define
\[
 K(r)=\min\{k:3^k>2^{k+L(r)+1-r}\}.
\]
Every smaller ordinary visitor entering \(y\) on its other incoming edge uses at least \(r+K(r)\) odd inputs, even at an unrestricted clock. Every \(r\) has infinitely many positive cofactors attaining this bound, with first native intersection at the apex in the stated construction. The exact equality condition at a supplied cofactor is a finite ternary congruence condition. Also \(K(r)-r\to\infty\). For \(r=11\), the lower bound is 34 visitor odds. Varying attaining cofactors does not solve an arbitrary prescribed cofactor.

[Exact optimum and attainment](renormalization/FIRST_MEETING.md) · [Fixed postpeak windows and Yu's logarithmic estimate](renormalization/POSTPEAK.md)

For one **fixed** reference orbit, optimize all equal-clock visitors at each compensated odd grade \(N\). The minimum has three exact asymptotic forms:

| Reference | Minimum or uniform source law |
| --- | --- |
| A supplied hit at one with charge \(I=2(j+p_0)-H_0\) | \(m(N)=2^{2N-I}\) whenever \(2N\ge I\) |
| An eventual cycle of clock period \(L\) and odd count \(q\) | \(m(N+q)=2^L m(N)\) for every sufficiently large \(N\) |
| A nonperiodic positive reference | Every eligible source satisfies \(u/3^N\to A_y>0\), uniformly over all sources at that grade |

Requiring the good visitor to be a canonical triple changes the optimizer but still gives the exact eventual recurrence
\[
 27m(g+27)+5=2^{54}(27m(g)+5).
\]
The elementary insertion and witnesses for all 54 charges are formalized; the eventual optimizer classification uses the written simple-path product argument.

These laws prove that an escaping bad lower arm and its supplied good triple cannot admit arbitrarily large balanced compensated-grade resets. Such resets would compare growth \(3^g\) on the lower side with \(4^g\) on the upper side. **No all-source construction of those resets has been found.** Two tempting rank-two replacement rules are disproved by ordinary convergent controls, including the supplied source 3233.

[Fixed-reference and canonical minimum laws](renormalization/GRADED_MINIMA.md) · [Both all-height rank-two controls](renormalization/RankTwoControl.lean)

A late cross-branch comparison yields another exact limitation. Uniformly over every positive ordinary target \(X\), the total number of sources reaching it within \(H\) clocks is at most \(C(25/16)^H\), with an explicit absolute constant. Each internal odd inverse has only two permitted exponent classes modulo six; a convergent weighted word count proves the bound. Since \((25/16)^{19}<3^8\), the existing 19-clock/8-odd chain saving reaches an exponentially vanishing fraction of all classes at its required ternary precision. For its one prescribed rational class, a separate exact count shows that more than 99.4% of endpoints below \(B\) miss every paid depth up to the stated logarithmic cutoff. This does not exclude that particular class at arbitrarily large depths for one supplied endpoint.

[Fixed-target clock-budget obstruction and source pin](renormalization/PORTAL_BUDGET.md)

## 5. Testing high-rank arithmetic and spectral mechanisms

The literature-inspired determinant strategy was tested on exact ordinary fibers, rather than on an unspecified analogue of an arithmetic-geometric object. At sufficiently large fixed grades into one fixed endpoint, the binomial moment vectors through degree \(d\) span the full lattice \(\mathbb Z^{d+1}\). At any prescribed finite number \(J\) of internal cuts with sufficiently large separate grades, the mixed moment lattice is exactly \(\mathbb Z^{(d+1)^J}\). Full carries are polynomial functions of the same coordinates and are included. Signed integer combinations cannot be converted into a positive smaller witness without a new argument.

On a reduced rational cycle of denominator \(d\), the degree-\(m\) native eigenline lattice has Smith factors \(1,d,\ldots,d^m\). In the ordinary case \(d=1\), the frame is already unimodular. Larger symmetric powers alone supply no new independent divisibility.

[One-cut lattice and height costs](adelic/MOMENT_LATTICE.md) · [Arbitrarily many internal cuts](adelic/MULTIPLE_CUTS.md) · [Cycle transport and exact Smith factors](cycle/HOLONOMY.md)

Separately, for the mass-transfer operator \(P\delta_n=\delta_{T(n)}\) on complex weighted \(\ell^1\) with a sequentially regularly varying weight of index \(\alpha\), both its spectrum and Fredholm essential spectrum are the disk of radius
\[
 R_\alpha=\max(2^{-\alpha},(3/2)^\alpha)\ge1.
\]
The same disk occurs after killing any fixed finite floor. Equivalent norms, compact perturbations and adjoining finitely many auxiliary coordinates preserve this essential disk. The proof constructs physical parity-cylinder approximate eigenvectors and an infinite family of collision eigenvectors. This rules out a strict essential contraction in this specified class of spaces; it does not exclude other function spaces or prove anything about all-time convergence of one integer.

[Complete spectral proof and formal kernels](spectral/README.md)

The disk persists inside the true inverse basin of **any one fixed** odd ternary-unit target, with that target's outgoing edge killed. This includes the convergent basin of one, where every individual basis vector eventually vanishes. For this rooted operator, a nonzero complex number \(\lambda\) is an eigenvalue exactly when one actual infinite inverse ray satisfies \(\sum_j |\lambda|^j w(x_j)<\infty\). For positive weight index \(\alpha\), its point-spectrum radius is
\[
 \left(3^{\rho(y)}/2\right)^\alpha,\qquad
 \rho(y)=\sup_{\text{true inverse rays}}\liminf_j\frac{\text{odd departures through }j}{j},
 \qquad \frac14\le\rho(y)\le\log_3 2.
\]
No eigenvalue has modulus at least one in this positive-index case. The distinction between the full essential disk and this inverse-ray invariant is exact; neither is an automatic forward-descent criterion.

[Single-basin theorem and complete eigenvector criterion](spectral/POINT_SPECTRUM.md)

## 6. What a single escaping component would have to look like

Assume one actual positive ordinary escaping origin. The exact component coordinate \(\eta\), combining its ordinary height with both integer grades, has a compact countable spectrum with Cantor–Bendixson height \(\omega+1\). Its successive derived sets are precisely its odd-level truncations. At each fixed shortcut delay, the ordinary fiber stabilizes to a finite set. The two parity subsequences of its normalized fibers have explicit Hausdorff limits.

There are at least \(2^{\lfloor\Delta/17\rfloor}\) actual unit ancestors in a delay-\(\Delta\) fiber. Outside any fixed neighborhood of the highest-rank point, only polynomially many remain. The normalized counting measures therefore concentrate at that point. This is compatible with an escaping component; it is not a contradiction. The stronger near-full exponential count and box-dimension statement depend on a separately identified analytic input.

The entire high-level component also has a uniform ordinary floor and an attained highest-shortcut-grade profile with increments between one and four. Under criticality its mean tends to \(\log_2 3\). A mixed profinite control shows why dropping this critical-mean condition loses essential information, even when all finite inverse comparisons are retained.

[Pointed spectrum and exact finite-fiber consequences](adelic/POINTED_SPECTRUM.md) · [Ordinary minimum profile and the local-limit limitation](adelic/MINIMUM_PROFILE.md)

A separate sparse-correction construction preserves one starting integer, long native finite words, native valuations, and arbitrarily strong sublogarithmic congruence tests, while changing the unit carry at rare times. It admits no rational native shadow. This is a countercontrol to proposed implications from those weakened data, **not an ordinary Collatz orbit**.

[Construction and exact scope](adelic/SPARSE_SHADOW.md)

## 7. Evidence and the final open obligation

The fresh project build compiled **37 Lean modules**, including **26 new modules** and eleven retained dependencies/consumers, into an empty project output cache. It checked **225 selected declaration axiom inventories**, including **129 in the new modules**. They contain only the standard logical axioms. Warnings were errors and automatic implicit variables were disabled. The compiler and cached Mathlib/package dependencies are pinned; those dependencies were not rebuilt in this pass.

All six exact finite-control programs ran both normally and with Python optimization enabled: twelve successful executions, with byte-identical output in each pair. These comprise the four lane controls, the final bounded-rank reduction, and the separately reviewed finite-cover followup. The pinned height-strip checker was separately replayed in both modes. These executions are finite evidence, not substitutes for the written unbounded proofs or the remaining universal premise.

[Lean receipt](../../reports/astra-unconventional-20261126/lean/receipt.json) · [Four-lane replay receipt](../../reports/astra-unconventional-20261126/control-replay.json) · [Bounded-rank replay receipt](../../reports/astra-unconventional-20261126/bounded-rank-replay.json) · [Pinned strip replay](../../reports/astra-unconventional-20261126/pinned-strip-replay.json) · [Source pins](SOURCES.json)

[Written review at the published science commit](../../reports/astra-unconventional-20261126/REVIEW.json) · [Clean-checkout publication receipts](../../reports/astra-unconventional-20261126/PUBLICATION.json) · [Finite-cover followup replay](../../reports/astra-unconventional-20261126/finite-cover-replay.json)

Rebuild with the pinned Lean executable, Mathlib checkout, and external package cache:

```bash
python -B research/astra-unconventional-20261126/check_lean.py \
  --lean /path/to/lean \
  --mathlib /path/to/mathlib \
  --package-cache /path/to/packages \
  --report-dir /outside/checkout/lean-replay
python -B research/astra-unconventional-20261126/check_controls.py \
  --report-dir /outside/checkout/control-replay
python -B research/astra-unconventional-20261126/renormalization/check_bounded_rank.py
python -O -B research/astra-unconventional-20261126/renormalization/check_bounded_rank.py
python -B research/astra-unconventional-20261126/renormalization/check_finite_cover.py
python -O -B research/astra-unconventional-20261126/renormalization/check_finite_cover.py
```

The central fixed-source merger remains unproved. The retained final Lean consumer takes `FrontierMerger` as an explicit argument. The separate critical-record consumer takes `RecordLock` and `CycleExclusion` as explicit arguments. Their standard axiom inventories do not discharge those arguments.

[Final proposal, exact remaining statements and decision](FINAL_PROPOSAL.md)
