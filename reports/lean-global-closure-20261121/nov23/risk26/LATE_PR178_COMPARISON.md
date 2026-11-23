# Late source comparison: PR178 at 398b3a04

23 November 2026. **SOURCE-QUALIFIED delta inspection, not a new independent
proof audit.** No code was replayed and no previously frozen science was
modified for this comparison.

## Exact versions and inspection boundary

- Previously frozen PR178 head:
  `a9b23dcee61a4b65a63aa4e7ca653d875a405037`.
- New fetched PR178 head:
  `398b3a04da071e96362005792417bd5cf8cc6497`.
- Fetch of the exact new SHA from `origin` completed successfully.
- The intervening history contains one commit, titled
  `Prove full numerical gcd bounds for unbounded Collatz word families`.
- The exact tree delta contains **59 added files, 7412 insertions, no
  modifications or deletions**. In particular the old fixed-clock,
  fixed-source repetition, and collision interfaces were not edited.

The added research index and the following source files were directly
read at the new full SHA. The canonical-fibre note and all three analytic
notes were read in full. The full numerical-separation theorem, its
parameter domain, construction, and conclusion were inspected; this
refresh does not claim a fresh audit of its complete polynomial-gcd
proof, the new Lean modules, execution receipts, or cited primary papers.

All paths in the table are relative to
`research/literature-push-20261123/` at the new SHA.

| New source | Claim read and exact remaining premise | Effect on our frozen results |
|---|---|---|
| `arithmetic/FULL_NUMERICAL_SEPARATION.md`, §1, (8)–(11), and §§2, 7 | Complete numerical gcd bound and integer-cycle exclusion for the explicitly constructed disjoint-pattern family, with pairwise coprime pattern periods and distinct residue supports. The pattern count and periods are unbounded. No reduction of arbitrary words to the family is supplied. | A substantive family theorem, but it neither bounds arbitrary actual prefix gcds nor changes our exact identity `gcd(C_N,D_N)=gcd(q_N−p,D_N)`. It excludes no general escaping source. |
| `boundary/CANONICAL_FIBRE_DEPTH.md`, (17)–(24) | An exact original-prefix mass lower bound, then the necessary Cesaro depth cost `3^M/M >= c q_j^2` on one fixed escaping spine, retaining the specified canonical trace law and a separate positive correction-product lower bound. | A sharper obstruction to a particular model-to-ordinary comparison. It supplies no sufficient depth, frequency-dependent comparison error, or same-law ternary collision upper. The correction-product premise can be supplied by the current global count, as detailed below. |
| `rigidity/SCALAR_BOUNDARY_AND_SECOND_CENTER.md`, Theorems 1–3 | Under an actual limiting parity density, the individual source series is rational or has its convergence circle as a natural boundary. At critical density a full arithmetic Taylor germ at the binary center implies rationality. Value-only deflation has convergence-disc product at most one. | A conditional scalar boundary theorem sharper in scope than an operator-norm boundary. The arithmetic germ is not constructed by our fixed-source normalization, gcd identity, or local-product bounds. |
| `rigidity/GENERAL_DENSITY_JET.md`, §§1–5 | With a limiting actual parity density, the explicit Jet hypothesis J is equivalent to eventual ordinary periodicity. Its rational coefficients, common finite denominator-prime set, and all required positive convergence radii remain hypotheses. | It strengthens the consumer for J beyond critical density; it does not establish J or a density limit. Even eventual periodicity would leave general positive-cycle exclusion separate. |
| `rigidity/FINITE_FILTER_TEST.md`, (2)–(7) | For fixed rational filters of the actual source series, the tested subexponential common-denominator condition forces eventual periodicity. Nonzero filtered coefficients retain an exponential ternary denominator. | Confirms that finite rational pole removal does not freely provide the arithmetic denominator premise. It neither changes nor bypasses our canonical consecutive-prefix product obstruction. |

## The new boundary estimate and the one premise our count supplies

The new boundary note distinguishes its model and ordinary laws. For the
specified independent fair affine model,

\[
 R\overset d=AR'+B,\qquad
 (A,B)=(1/2,0)\text{ or }(3/2,1/2),
\]

its primary-renewal application states

\[
 x\,\mathbb P(R>x)\longrightarrow[\log(27/16)]^{-1}.
\]

The finite model measures are the **unnormalized**, trace-weighted
ternary restrictions

\[
 \eta_m^q(dR)=3^m\nu(dR,Y\in q+3^m\mathbb Z_3),
 \qquad \overline\eta_M^q=M^{-1}\sum_{m=1}^M\eta_m^q.
\]

For the stated canonical harmonic trace `h` and its actual inverse law
`mu_q`, the reversed original prefix from `q_j` back to the same `q_0`
forces mass at a fixed positive fraction of `q_j`. For its specified
bounded scaled test `f(R/q_j)`, equations (17) and (22) give

\[
 \frac{h(q_j)}{q_j}\mu_{q_j}[f(R/q_j)]
 -\frac1{q_j}\overline\eta_M^{q_j}[f(R/q_j)]
 \ge c_0-C_0\frac{3^M}{M q_j^2},
\]

provided

\[
 \Lambda_*:=\inf_j\prod_{i<j}\frac{3q_i}{3q_i+1}>0.
\]

This last premise **is available from the fixed-source normalization
already reconstructed in this round**:

\[
 E_j=q_0\prod_{i<j}\left(1+\frac1{3q_i}\right)
 \uparrow E_\infty<\infty,
 \qquad \Lambda_j=q_0/E_j\ge q_0/E_\infty>0.
\]

The dependency is PR182
`a7fd3ac9e5bff7412858df23d776bb847e9c1371`,
`research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`, §§1–6,
as applied in `../root/UNCONDITIONAL_CYCLE_BOUNDARY.md`, (UB8)–(UB9).
Thus the correction-product qualification can be discharged when
combining these sources. The canonical trace construction and its
selection/fibre interface retain their separate source qualifications.
The displayed ordinary real inverse law is also not silently identified
with our stationary ternary endpoint law.

Consequently `3^M/M >= c q_j^2` remains a **necessary payment**, not an
approximation theorem. For arbitrary positive weights the corresponding
necessary payment is `sum_m w_m3^m >= c q_j^2`; the factor `1/M` is
specific to Cesaro averaging. No bound on actual repeated-word energy
`J`, omitted mass `tau`, or same-source ternary collision probability is
proved by this step.

The new note explicitly explains that the shallow model Fourier regime
`M=o(log|t|)` cannot provide this moving-root comparison when
`log|t|=O(log q_j)`. It also keeps physical-root and common-boundary
frequencies separate. These are useful restrictions on that proposal;
they do not invalidate a different, adequately deep source comparison.

## Relationship with the fixed-source prefix shadows

The frozen prefix note retains the same integer through all horizons,
proves exact displacement-controlled gcd cancellation, and obtains
critical height exponent `log3` and binary approximation exponent one.
Its canonical local products are exactly `q_N` and a positive tail
bounded below by `1/3`. None of the new PR178 results changes those
identities or supplies a strict Subspace saving for those forms.

The arithmetic Jet hypothesis concerns the **entire actual binary
Taylor expansion** `B_n(2+t)`, not just `B_n(2)=-n`. Its first derivative
is already unproved rational for a general positive source. The finite
correction `E_infinity`, ordinary integrality, and convergence in two
completions do not provide J. If our critical clock is known only at
selected horizons, the new theorem's full limiting-density hypothesis
must not be silently imported either.

## Verdict

**No genuinely closing theorem or changed frozen input was found in
this delta.** The added complete-gcd cycle-family theorem, scalar boundary
alternative, and conditional two-center consumer are substantive within
their stated domains. The directly relevant new source comparison is a
stronger necessary depth bound, with its positive correction-product
premise now supplied by the global orbit count. The central same-source
collision upper, unrestricted ordinary escape exclusion, and general
positive-cycle exclusion remain OPEN.

This is a source-pinned late comparison. It does not extend the frozen
proof reviews to this entire new head or certify its reported builds.
