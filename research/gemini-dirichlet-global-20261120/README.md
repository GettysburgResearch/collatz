# Ordinary Dirichlet control and the three Gemini follow-ups

**PROPOSED research packet. Collatz is not resolved.** The main result is a
weighted inequality for actual ordinary invariant functions throughout
`0 < s < 1`. It replaces the uploaded v3 package's proposed numerical cutoff
with an ordinary argument across the whole open strip. It does not assert
infeasibility of every abstract residue relaxation. The proof reconstructs
its finite variation input from the pinned PR146 source, and separates that
input from the new analytic deductions.

The three supplied archives are [preserved verbatim](../../archive/gemini-followups-20261120/README.md).
The original initial-thread audit remains in
[PR152](https://github.com/GettysburgResearch/collatz/pull/152).
This packet audits all three additional packages, repairs the useful
certificates, and records the first unsupported step in each proposed
completion route. It does not promote the uploaded `PROVEN` or `VERIFIED`
labels into the accepted project baseline.

## 1. Main result: control from ordinary tripling defects

Use the positive shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

For an invariant labeling `f(T(n))=f(n)`, define

\[
N_s(f)=\sum_{n\ge1}\frac{|f(n)|}{n^s},\qquad
\delta_3f(n)=f(3n)-f(n),\qquad
\delta_5f(n)=f(5n+1)-f(n).
\]

The [full proof](ORDINARY_DIRICHLET_COERCIVITY.md) establishes the following.

| Claim | Exact conclusion | Essential scope |
|---|---|---|
| OD1 | `N_s(h) <= K_s N_s(delta_3 h)` as extended nonnegative sums | `h >= 0` invariant; its dyadic arithmetic means tend to zero; every `0<s<1` |
| OD2 | The same weighted inequality | Real or complex invariant `f` with `N_s(f)<infinity` |
| OD3 | A unique constant `c` has `N_s(f-c) <= K_s N_s(delta_3 f)` | Bounded invariant real or complex `f` with finite defect moment; `c` is 0 or 1 for a Boolean labeling |
| OD4 | Component, tripling-boundary, and five-ray-boundary abscissae agree; their positive subcritical critical moments converge or diverge together | A fixed invariant set with convergence abscissa below one |

Here `C,C'` are finite absolute constants in PR146's homogeneous ordinary
variation lemma, and

\[
K_s=\frac{C(2C')^s}{2(1-2^{s-1})}.
\]

The [independent source reconstruction](../../reports/2026-11-20-gemini-dirichlet/TRIPLING_VARIATION_REVIEW.md)
gives, for example, the conservative choices `C=1054` and
`C'=6000*3^30`. Optimization of these constants is not needed for the theorem.
The [separate analytic review](../../reports/2026-11-20-gemini-dirichlet/ORDINARY_DIRICHLET_REVIEW.md)
checks the weighted summations, complex coarea, full-sequence limiting
argument, and the precise odd-to-full norm conversion.

For clarity, if `K` is such an invariant set, write

\[
\partial_3K=\{n:1_K(3n)\ne1_K(n)\},\qquad
\partial_5K=\{n:1_K(5n+1)\ne1_K(n)\},\qquad
D_A(s)=\sum_{n\in A}n^{-s}.
\]

Then at every `0<s<1`, allowing infinite sums,

\[
K_s^{-1}D_K(s)\le D_{\partial_3K}(s)\le(1+3^s)D_K(s),
\]

\[
\frac{1-2^{-s}}{K_s4^s}D_K(s)
\le D_{\partial_5K}(s)\le(1+6^s)D_K(s).
\]

Thus the boundary/component Dirichlet ratios have positive lower limits
at a positive subcritical abscissa **even when the critical series is
finite**. There is no need to assume the critical divergence used by the
uploaded v3 normalization argument.

### Why this argument is global

The finite ordinary variation lemma bounds adjacent differences in a dyadic
interval by odd tripling defects at a fixed larger scale. Pairing even and
odd terms gives an exact identity for the difference between consecutive
dyadic means. Telescoping to the zero mean and applying Tonelli yields the
weighted inequality. For bounded labelings modulo constants, the same
variation controls logarithmic profiles; their limit is invariant under
the irrational rotation `log_2(3)` and is therefore constant.

The five-ray transfer is the exact ordinary identity
`T^2(20x+1)=15x+1`. It gives
`|delta_3 f(x)| <= |delta_5 f(3x)| + |delta_5 f(4x)|`.
For odd `x`, the two parameter sets are disjoint, giving the factor `4^s`
without an additional collision factor. This uses fixed ordinary
trajectories and all scales, rather than averaging unrevealed digits.

### What remains missing for a full solution

No argument here puts a hypothetical exceptional component below abscissa
one, or gives the upper bound on its actual separating boundary that would
contradict a predecessor lower bound. The theorem supplies a comparison
between those quantities, not an upper bound for either one. Taking the
complement preserves the same defect; it does not create the missing
summability. The displayed constant diverges as `s` approaches one.
The [endpoint analysis](ENDPOINT_BOUNDARY.md) records exactly what survives
under a finite harmonic-defect assumption and where the logarithmic loss
appears.

For attribution, pinned PR146 already proves the power-0.84 infinitely-often
boundary lower bounds and the corresponding critical-moment divergence,
using its published predecessor input. This is not a claim of the first
polynomial boundary amplification. The contribution here is the general
weighted norm estimate, its modulo-constants extension, and the fixed-set
equal-abscissa and critical-moment conclusions across the open strip.

## 2. What survives from the three supplied packages

| Uploaded route | Verified or repaired content | Unsupported completion step |
|---|---|---|
| v3 Farkas/Dirichlet | The **serialized** decimal vectors rigorously certify the two points `(r,s)=(4,21/25)` and `(6,913/1000)` after outward integer interval evaluation | No supplied r8 certificate or all-exponent cover; the reported `0.950131` threshold was hard-coded |
| v2 Dirichlet/Ruelle and exponent crossing | The scalar shift identity is valid; the proposed averaged matrices have exact spectral radius `3^(s-1) sum_{g<=G} 2^(-gs)`, independent of residue precision | Fresh-lift averaging does not close a fixed integer population; an inverse predecessor lower bound is not a survivor upper bound |
| v2 mixed Mahler equation | Exact equivalence with ordinary component invariance; complete finite-alphabet rational-solution classification | No rationality, analytic continuation, or separate finite-order base-2 and base-3 Mahler equations have been established |
| v2 adelic positivity and separate Route 3 | Correct denominator-height sign; exact rational counterexamples to the product test; correct all-word positivity statement | Full divisibility/cancellation, a justified fixed-dimensional S-unit application, and an effective universal cycle bound remain absent |
| Separate Route 2 compiler | Exact 162-state Bellman equality proves minimax slope `5/2` for the specified precision-five game; a terminal policy repairs its uniform compiler interface | This is weaker than the existing PR148 compiler and supplies no inverse-to-forward closing implication |
| Separate Route 4 spectral penalty | Finite denominator-sector reweighting is an isometric conjugacy; the correct Haar transfer has essential radius one on `C(Z_2)` | The proposed norm cannot change the fixed operator's spectrum; a stronger space still needs a proof controlling every ordinary source |
| Separate Routes 1 and 5 | Exact finite affine counts, finite controls, and rational-cycle replay | Finite cylinder counts do not cover all clocks; the fixed-list harness does not test arbitrary proposed invariants |

Detailed arguments are in:

- [Farkas, Dirichlet, and averaged-matrix audit](FARKAS_DIRICHLET_AUDIT.md).
- [Mixed Mahler equation and global integrality audit](MAHLER_AND_INTEGRALITY_AUDIT.md).
- [Separate-thread routes and exact compiler repair](ROUTES_BUNDLE_AUDIT.md).
- [Denominator sectors and the spectral penalty](DENOMINATOR_SECTORS.md).

The two repaired point certificates have minimum residuals rigorously in

\[
[0.999999999412877118,\;0.999999999412877119]
\quad\text{and}\quad
[0.999999999270272552,\;0.999999999270272553],
\]

respectively. These bounds are computed from the file's exact decimal
rationals, with explicit series remainders and outward integer rounding;
no LP solver decides their validity. Each conclusion is still a point
certificate. The ordinary theorem above is a separate proof, not an
interpolation between those points.

For the spectral proposal, the obstruction is also stronger than a finite
counterexample: the rational shortcut map preserves the reduced denominator
when it is prime to six. Consequently, any finite positive factor depending
only on that denominator yields an onto isometry commuting with the same
atomic forward operator. Its full and essential spectra are unchanged.
This statement is limited to the explicitly defined spaces and operators.

## 3. Reproduction and evidence

From the repository root, the new scoped checks require only Python's
standard library:

```sh
python -X utf8 -B research/gemini-dirichlet-global-20261120/run_checks.py --receipt ../gemini-dirichlet-exact.json
```

The driver authenticates the thirty uploaded files and the three cached
dependency proofs. It runs all four new checkers in normal and optimized
Python, compares their complete payloads, verifies that the exported
[Bellman potential](bellman-p5-certificate.json) matches the exact
reconstruction, and checks that a broken serialized Farkas normalization
is rejected in both modes. No rejection check is disabled by `-O`.

The ten original numerical scripts can be replayed separately in temporary
copies; that command requires NumPy and SciPy:

```sh
python -X utf8 -B research/gemini-dirichlet-global-20261120/replay_sources.py --receipt ../gemini-original-replay.json
```

The original sources are not overwritten. Successful original execution
does not endorse their mathematical labels. In particular, the regenerated
v2 receipt differs in two floating-point roundoff values; the reproduced
v3 receipt and decimal-vector file are byte-identical to the uploads.

The finite replays check explicit coefficients, complete finite game states,
affine parity cylinders, outward interval inequalities, and counterexamples.
The infinite coarea, Tonelli, Fourier, and limiting arguments are written
proofs and have a separate review boundary. No Lean build, external theorem
reproof, or Collatz verification beyond those scopes is claimed.

Exact pins, source hashes, execution receipts, and review records live in
the [evidence report](../../reports/2026-11-20-gemini-dirichlet/README.md).
Repository validation is recorded for the actual published scientific
commit in a subsequent documentation commit; it is not mathematical
certification of the new results.
