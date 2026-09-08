# Claim-level review at frozen source heads

VERIFIED below is this reviewer's verdict on the exact written argument and its displayed hypotheses. It is not a formal-proof certificate, canonical promotion, whole-file approval, or assertion that the complete published numerical payload was rerun. Conditional theorems retain their premises. The proposed universal completions are classified separately in README.md.

Every row carries the full `(PR, commit, path, claim ID)` identity through its group header. The code-integrity finding F01 is independent of these mathematical verdicts.

## PR #105 — `research/astra-tail-transport/PROOF.md`
Commit: `912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe`. [Exact source](https://github.com/GettysburgResearch/collatz/blob/912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe/research/astra-tail-transport/PROOF.md).

| Claim | Verdict and statement | Independent check | Required boundary |
|---|---|---|---|
| ATT-001 | **VERIFIED** — Sharp ordinary-source tail: 1/(9N^2) <= sum_{n>N} R(n)^(-2) <= 43/N^2. | Reconstructed all-component positive majorization and shifted small-component tails; powers of three supply the lower atom. | N>=2; source-height tail, not endpoint rank tail or natural density. |
| ATT-002 | **VERIFIED** — At each fixed k>=1, critical rank tail is Theta_k(Y^-1); positive moment threshold is 1 and weak-critical norm grows at scale (9/4)^k. | Checked nonzero affine remainder, ternary separation on power sources, both adjacent-clock spike families, and the explicit constant inequalities. Independently tested 28 fixed-clock power cases. | The lower tail has its stated large-Y threshold. Finite-clock tightness and growing weak norms do not decide uniform-in-time tightness. |
| ATT-003 | **VERIFIED** — Every non-core maximal module satisfies A(n)+5 <= (n+5)^(9/4). | Checked modes 0, 1, 2, higher modes, maximal repetition divisibility and the strict logarithm bracket 3^17<2^27. | A is maximal repeated 1^a0, not one shortcut step or the older whole-run map; this is a height ceiling, not descent. |
| ATT-004 | **VERIFIED** — One quarter-unsafe return has rank tail <=200 C Y^(-4/9) for input f<=C/R^2; moments 0<s<4/9 are finite. | Combined the module ceiling, nonincreasing safe continuation and ordinary source tail; checked the layer-cake bound including the 1/3 moment constant 602. | One return and its original dominated input only. The output does not regenerate that envelope for another return. |
| ATT-005 | **VERIFIED** — The explicit even-j family gives infinite weak first-rank output and refutes a fixed quadratic R(A(n))/R(n)^2 ceiling. | Reconstructed exact valuations, maximal mode, both unsafe endpoint guards and the (9/4)^a/1152 lower ratio; independently replayed j=2,4,6,8. | Same canonical old-R unsafe input; neither infinite unweighted mass nor a divergent individual orbit is asserted. |
| ATT-006 | **VERIFIED** — Uniform tail defect equals divergent-basin mass; limiting finite-ball Cesaro occupation equals nontrivial-cycle-basin mass. | Checked finite-atom truncation for the supremum/limit order, properness, deterministic orbit classification and dominated convergence for occupation. | Both defects must vanish. This is an equivalence/diagnostic, not a proof of either vanishing. Optional SC* crosswalk retains its separate source. |

## PR #105 — `research/astra-tail-transport/repeated-spikes/PROOF.md`
Commit: `912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe`. [Exact source](https://github.com/GettysburgResearch/collatz/blob/912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe/research/astra-tail-transport/repeated-spikes/PROOF.md).

| Claim | Verdict and statement | Independent check | Required boundary |
|---|---|---|---|
| ATT-101 | **VERIFIED** — Initial source truncation yields a once-only error for all later bounded observations and finite source-dependent clocks. | Checked source-tagged pushforward before merging; positivity bounds every omitted event by the original tail. | Does not pay once for an arbitrary unbounded moment or for the total repeated visits in the unknown complement. |
| ATT-102 | **VERIFIED** — Finite first exits and surviving mass decompose exactly into killed, exited and internally cyclic sources. | Reconstructed the finite sum of powers through first exit and classification of deterministic components; no inverse of I-K is invoked on a cycle. | An exit from the finite ball is not absorption. The initial tail and internal cycle mass remain in the bound. |
| ATT-103 | **VERIFIED** — A forward-closed clearance forest has nilpotent internal dynamics and controlled total inflow/late occupation. | Checked strictly decreasing distance labels, absence of forest-to-unknown feedback, and summed residence <=L times newly supplied mass. | Forward closure and actual absorption labels are essential hypotheses, not outputs of an assumed universally terminating search. |
| ATT-104 | **VERIFIED** — Three complete forests give positive all-future canonical-input bounds; at Y=2^32 the residual is 12/2^48 for j>=52. | Independently rebuilt all three complete rank balls and literal physical forests. Largest case: 163168 sources, 78828 unsafe roots, 111763 forest nodes, 32935 outside nodes, maxima 52 returns / 261 shortcut steps / 21206132666 height. | Verified numerical statement plus its analytic tail proof, not every field of the published JSON envelope. Residual is positive; no cofinal clearance guarantee or density claim. |
| ATT-105 | **VERIFIED** — The induced unsafe operator has l1 norm one at every finite iterate J. | Checked finite ordinary CRT shadows, both unsafe phases and preservation of unit-atom mass. Rebuilt nine shadows through J=128. | Sources vary with J. This refutes a global block contraction, not eventual absorption of each fixed atom. |

## PR #105 — `research/astra-tail-transport/expanding-word-rank/PROOF.md`
Commit: `912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe`. [Exact source](https://github.com/GettysburgResearch/collatz/blob/912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe/research/astra-tail-transport/expanding-word-rank/PROOF.md).

| Claim | Verdict and statement | Independent check | Required boundary |
|---|---|---|---|
| ATT-201 | **VERIFIED** — The expanding-word minimum rho is proper/computable, with n-1<=rho<=R<=n^2. | Checked unreduced forms, fixed 5/4 coefficient gap, positive offsets, inclusion of old components and the strict n*2^L<4M cutoff. | Finite in the input value, not a polynomial-bit-complexity claim. A minimizing formal word need not be physically legal. |
| ATT-202 | **VERIFIED** — N_rho(X)<250X^(39/40); sum 1/rho<=10000 and sum 1/rho^2<2. | Reconstructed the entropy word count, offset-sensitive component counting, short/long length split and convergent positive sums; exact constant margins reproduced. | This is the stated upper spectrum, not sharpness or an invariant transported weight. |
| ATT-203 | **VERIFIED** — A legal minimizing component yields strict decrease of the same rho. | Checked the affine defect transport, base words, every tied minimizer, and the separately absorbed core. | The total algorithm can return UNRESOLVED; legal activation and complete source coverage are not supplied. |
| ATT-204 | **VERIFIED** — Guarded arbitrarily long 111010 phases have exact all-word minima and rho contraction at every shortcut step. | Checked the nonzero-comparison length regimes and zero-comparison primitive-period argument, all six phases and old unsafe guards. Exhaustively minimized rho at 21 large ordinary phase positions. | Full e/K congruence and size guards remain required. The claim is not for arbitrary existing sources or an infinite positive periodic trajectory. |
| ATT-205 | **VERIFIED** — An even phase exit has an illegal unique minimizer and an unbounded actual successor-rank ratio. | Reconstructed h=5 mod16, h>=21, both word-length lower-bound regimes and the 2^h/4352 ratio. | The huge successor rank was not exhaustively enumerated in this review. The written all-word bound supplies the theorem; no canonical-input moment assertion is inferred. |
| ATT-206 | **VERIFIED** — Every fixed forward horizon can be defeated by an ordinary source with all next K ranks >16 rho(n). | Checked small odd CRT units, ternary valuations of all base forms, nonzero affine remainder and complete short/long word split. | Forward-only delay and inverse-only failure are not a lower bound for every two-sided merging diagram; sources depend on K. |

## PR #106 — `research/astra-linear-frontier/LINEAR_PRECISION.md`
Commit: `7b7471ea0e7b359a2ac46fb1e6aff269331509c3`. [Exact source](https://github.com/GettysburgResearch/collatz/blob/7b7471ea0e7b359a2ac46fb1e6aff269331509c3/research/astra-linear-frontier/LINEAR_PRECISION.md).

| Claim | Verdict and statement | Independent check | Required boundary |
|---|---|---|---|
| ALF-001 | **VERIFIED** — Negative paths ending at -2 have correction product >=(q+1)^(-1/5). | Checked distinct negative odd magnitudes, their ordering, the positive fifth-power polynomial and telescoping product. | Finite actual negative comparison paths only; not positive divergence or ordinary extraction. |
| ALF-002 | **VERIFIED** — The complete negative precision budget satisfies floor(r/3)+2<=B_r<=4r+2, with the stated refined linear asymptotic. | Reconstructed the m=q+v3(2v+1) exponential inequality, elementary induction constants and greedy odd-exit lower family. Independently rebuilt cones through radius 10. | Improves the earlier coarse bound without refuting it; no optimal linear constant is claimed. |
| ALF-003 | **VERIFIED** — Remaining-depth gap pruning preserves the exact inverse minimum with at most 4D-2 retained exits. | Combined the linear budget with the old shield; retained the parent and terminal child, checked depth bookkeeping, value/clock bounds and 2*4^D*D! node ceiling. Independently compared 1196 full/pruned minima. | Output-sensitive finite search, not polynomial in D or a successful all-source selector. Section-return clocks are not raw shortcut clocks. |

## PR #106 — `research/astra-linear-frontier/SECTION_DEPTH_AND_REPAYMENT.md`
Commit: `7b7471ea0e7b359a2ac46fb1e6aff269331509c3`. [Exact source](https://github.com/GettysburgResearch/collatz/blob/7b7471ea0e7b359a2ac46fb1e6aff269331509c3/research/astra-linear-frontier/SECTION_DEPTH_AND_REPAYMENT.md).

| Claim | Verdict and statement | Independent check | Required boundary |
|---|---|---|---|
| ALF-004 | **VERIFIED** — For every D, infinitely many guarded ordinary sources defeat every lower-P merger in the full D-by-D section-return box. | Reconstructed low/high rational comparison nodes, shifted-remainder obstruction, high-node gap pruning, positive comparison tree, strict valuation freezing and the h/K budgets. | All positive section witnesses in the specified box, not all ordinary raw-clock witnesses. Keep h>=256(D+1), K=36D+20 and both physical/CRT guards. |
| ALF-005 | **VERIFIED** — Longer explicit words repay the same P; a least-lift family has minimum section merging cost Theta(log n). | Checked CRT source, exact terminal even valuation, P-quarter drop and both source-size inequalities. Independently checked 12 family cases and full unpruned boxes for the two stated small cases. | Family-local cost with completed section returns; not a universal stopping-time bound or a raw two-sided clock lower bound. |
| ALF-006 | **VERIFIED** — The P-hard family immediately drops the existing n+5 component, while both min(P,C) and max(P,C) increase. | Reconstructed C transport 9/64, simultaneous P/C comparisons and all shared family guards. | The component identity is credited prior work; the simultaneous comparison is new. No exclusion of every scalar combination or switching rule. |
| ALF-007 | **VERIFIED** — A separate family has certified compressed (110)^D 0^L paths to 1. | Checked principal-unit exponent lifting, exact source depth and cofactor, integrality and physical word replay via affine cylinders. Independently rebuilt four modular exponent certificates. | Enormous ordinary sources and complete paths were not materialized or literally simulated. The other family's logarithmic source-size conclusion does not transfer here. |

## PR #106 — `research/astra-linear-frontier/prefix-rank/PROOF.md`
Commit: `7b7471ea0e7b359a2ac46fb1e6aff269331509c3`. [Exact source](https://github.com/GettysburgResearch/collatz/blob/7b7471ea0e7b359a2ac46fb1e6aff269331509c3/research/astra-linear-frontier/prefix-rank/PROOF.md).

| Claim | Verdict and statement | Independent check | Required boundary |
|---|---|---|---|
| APR-001 | **VERIFIED** — Actual nonzero prefix displacement rank Gamma is proper and has an evaluator using <=floor(log_2 n) shortcut steps. | Checked raw affine numerator bounds in both multiplier signs, zero-displacement omission, baseline candidate and rigorous early stopping. Two evaluators agreed on all n=2..8192. | Use raw T inside the rank even after visiting 1; only Gamma(1)=0 is exceptional. No convergence oracle or chosen-word assumption. |
| APR-002 | **VERIFIED** — An even minimizing displacement, or even minimizing baseline source, gives strict same-Gamma one-step decrease. | Reconstructed same-parity rotation and exact 1/4 or 3/4 factors; checked 4675 sufficient guards independently. | The residual can have only odd minimizing nonzero displacements, with any minimizing baseline at an odd source. That residual is not excluded. |
| APR-003 | **VERIFIED** — Complete Gamma sublevels have O(sqrt(M) log M) upper counts; reciprocal-power summability holds exactly for s>1/2. | Checked word/displacement integrality, both signs, complete source bound n<=M, count constants, dyadic tail and lower n^2 comparison. Independently matched nine complete balls through 65536, last count 587. | No sharp asymptotic constant or transported-envelope conclusion. The logarithmic upper/lower counting gap is not erased. |
| APR-004 | **VERIFIED** — Strict-Gamma safe excursions admit explicit all-source tails and finite undiscounted occupation. | Checked finite rank-ball residence, killed-at-unsafe-entry projection, envelope summation and occupation constant 21200/27. | Requires the stated entry envelope each time; exit can be unsafe rather than 1. Not a repeatedly invariant input class. |
| APR-005 | **VERIFIED** — A complete physical lower-Gamma merging cover implies Collatz; a suitable strict summable supersolution is an alternative. | Reconstructed least exceptional rank argument, finite physical meeting, core exception and positive-sum contradiction for the specified killed operator. | Both sufficient conditions remain uninstantiated. Finite candidate enumeration is not a complete temporal cover. |

## PR #106 — `research/astra-linear-frontier/prefix-rank/PERIODIC_SWITCHING.md`
Commit: `7b7471ea0e7b359a2ac46fb1e6aff269331509c3`. [Exact source](https://github.com/GettysburgResearch/collatz/blob/7b7471ea0e7b359a2ac46fb1e6aff269331509c3/research/astra-linear-frontier/prefix-rank/PERIODIC_SWITCHING.md).

| Claim | Verdict and statement | Independent check | Required boundary |
|---|---|---|---|
| APR-006 | **VERIFIED** — Every primitive expanding period has ordinary finite-horizon families with unique period-length minima at every phase. | Checked nonmultiple-prefix valuation separation, repeated-period strict domination and EVERY unprescribed prefix via growth/4^k cutoff; reconstructed source existence and phase transfer. Independently evaluated all prefixes at all 1440 phases of 64 family cases. | Sources depend on word/horizon; no positive all-time periodic realization, universal aperiodic coverage or endless renewal of the guard. |
| APR-007 | **VERIFIED** — Gamma decreases across arbitrarily many old quarter-unsafe 111010 switches without a terminal repayment guard. | Checked credited old rank formulas and maximal modes, the same-source <4/27 initial comparison and new unique-prefix theorem. Independently checked 32 old unsafe edges. | A family theorem, not a universal comparison with R or automatic continuation beyond the prescribed phase. |
| APR-008 | **VERIFIED** — Unique minimizing actual-prefix lengths are unbounded. | Checked primitive run pattern (1110)^j110, expansion and application of the quantified previous theorem. | Rules out a fixed prefix-length dictionary for this evaluator, not finite computation at each input. |

## PR #106 — `research/astra-linear-frontier/prefix-rank/SPIKES.md`
Commit: `7b7471ea0e7b359a2ac46fb1e6aff269331509c3`. [Exact source](https://github.com/GettysburgResearch/collatz/blob/7b7471ea0e7b359a2ac46fb1e6aff269331509c3/research/astra-linear-frontier/prefix-rank/SPIKES.md).

| Claim | Verdict and statement | Independent check | Required boundary |
|---|---|---|---|
| APR-009 | **VERIFIED** — All powers 3^H have unavoidable first-step Gamma spikes; pure power supersolutions and finite-p-moment class invariance fail for raw transport. | Checked Gamma(3^H)=3^H with unique baseline; two prefix-length regimes give kappa>11/10; every lower-rank merger must leave the inverse even ray. Reconstructed the positive full-support input with divergent output moment; tested 40 powers. | The moment statement is an existence counterexample for each p>0, not automatically the canonical Gamma^-2 input or an induced unsafe-return operator. |

