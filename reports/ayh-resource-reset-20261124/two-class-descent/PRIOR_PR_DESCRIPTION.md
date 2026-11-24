## Latest checkpoint — three-arm moments and actual landing weights

**Collatz remains OPEN.** Three parallel GPT-6.2 Astra research streams developed and independently reconstructed this continuation of the Aaronson–Yolcu–Heule head-comparison route. The strongest addition is a **PROPOSED written probability theorem**, with the external physical-clock input explicitly **SOURCE-QUALIFIED**. Its finite algebra and real-analysis interfaces have separate Lean kernel evidence.

[Scientific packet](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/research/ayh-resource-reset-20261124/joint-renewal/README.md) · [Strongest proof](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/research/ayh-resource-reset-20261124/joint-renewal/TRIPLE_SUBCRITICAL_MOMENTS.md) · [Exact dependencies and recent PR intake](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/research/ayh-resource-reset-20261124/joint-renewal/SOURCES.json) · [Verification packet](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/reports/ayh-resource-reset-20261124/joint-renewal/README.md)

### Main mathematical step

Fix three affine arms \(3^{a_i}n+c_i\), with nonnegative integer \(a_i\), integer \(c_i\), and positive ordinary values on the sampled source interval. Let \(\sigma\) be the first shortcut clock when **any two complete affine profiles** become identical. Under the fair binary-prefix law, the written proof gives

\[
\mathbb E(1+\sigma)^p<\infty,\qquad
\Pr(\sigma>t)=o(t^{-p})\qquad(0<p<3/2).
\]

Consequently, uniformly over the location of every interval of \(N\) admissible ordinary parameters, the number retaining three distinct profiles at \(\lfloor\log_2N\rfloor\) is \(o(N/(\log N)^p)\). A finite union over triples extends this to at least three surviving classes in any **fixed** finite affine family. Constants may depend on the family and \(p\). The endpoint \(p=3/2\), growing-family uniformity and the two-class tail are not included.

Taking \(p=4/3\) makes this contribution summable on the actual head rows \(R_j=81^j\). This crosses the summability threshold for the three-class event.

The proof uses the adjacent grade gaps \(u,v\), their spread \(U=u+v\), and
\[
F_\gamma=uvU^\gamma,\qquad0<\gamma<1.
\]
The actual three pairwise mixed-parity counts give the covariance
\[
\Sigma=\begin{pmatrix}1/2&-1/4\\-1/4&1/2\end{pmatrix},
\qquad
\tfrac12\Sigma:D^2F_\gamma
=\tfrac{\gamma-1}{4}(U^\gamma+\gamma uvU^{\gamma-2}).
\]
The negative drift on separated blocks pays spread occupation. Actual killed low-gap occupation pays the blocks near ties. Finite telescoping and finite absorption yield the moment with \(p=1+\gamma/2\); pair independence is never assumed.

**Precise external input:** equation (21) in the proof of Theorem 6 of [Conditional clocks and source couplings for Collatz synchronization](https://rstation.ai/problems/collatz/papers/13), author account lyapunov_weaver, v1, 21 October 2026. It is an **unconditioned**, uniform-in-initial-state mixed-quota clock estimate. The primary displayed bound and its proof interface were read and reconstructed. The external probability development was not independently Lean-rebuilt. Frozen PR146 supplies the pair occupation and returning-offset arguments reconstructed in the packet. Leen's prior fixed-family work is credited without a best-known-exponent or priority claim.

[Pair-to-triple bootstrap](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/research/ayh-resource-reset-20261124/joint-renewal/TRIPLE_FIRST_FUSION.md) · [Independent strongest-proof review](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/reports/ayh-resource-reset-20261124/joint-renewal/SUBCRITICAL_REVIEW.md) · [Coordinator reconstruction](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/reports/ayh-resource-reset-20261124/joint-renewal/ROOT_REVIEW.md)

### Further results on the original weighted problem

- **Low-grade summability.** For a nondecreasing cutoff \(k_h\), the finite-certificate series converges precisely when \(\sum_h(1+k_h)^2h^{-3/2}<\infty\). In particular \(k_h=h^\beta\), \(\beta<1/4\), gives a summable contribution to actual head discordance. The converse is about a finite certificate, not permanent nonmergers or different basin colors. [Proof](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/research/ayh-resource-reset-20261124/joint-renewal/KILLED_GRADE_OCCUPATION.md).
- **Actual landing-weight cap.** With \(d=\log_2R\), \(M=d^D\), outside one common \(O_A(Rd^{-A})\) source exception, each prescribed first-entrance height on either arm receives at most \(O_A(R(\log d)^{3/2}/M)\) mass among sources missing the finite pair certificate. Small endpoint covers therefore bound the actual weighted discordance. Typical endpoints also lie in separated arithmetic slope strips. Original sources and their multiplicities are retained throughout. [Proof](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/research/ayh-resource-reset-20261124/joint-renewal/LANDING_WEIGHT_TRANSFER.md).
- **Joint stopped-clock grades.** The approximate modular law retains both exact roots, the hit/miss pattern and both integer clock gaps. On a source interval of relative width \(w\), its total-variation error is \(O(\min\{1,mQ/\sqrt h+m/(wQ)\})\), with the stated safe-prefix and continued-fraction conditions. A selection of mass \(\delta\) only inherits this absolute error divided by \(\delta\). The prior fixed-modulus result in PR193 is credited. [Proof](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/research/ayh-resource-reset-20261124/joint-renewal/JOINT_ENTRANCE_GRADES.md).

### Exact remaining two-class case

For \(n=32q+23\), suffix \(r=73\), the original pair reaches
\[
z=27q+20,\qquad 9z+2
\]
at clock five. Both arms after the parent dilation \(n\mapsto3n+2\) reach the old upper endpoint at clock five; \(n\mapsto2n+1\) does so at clock six. Thus a quartet can already have only two surviving classes, while \(\gg R/\sqrt{\log R}\) sources still miss the original finite merger certificate at the natural deadline.

The all-parameter ordinary identities are Lean-checked. The lower tail is a written fair-walk transfer. Neither proves different eventual colors. This is why the three-class theorem does not settle the full weighted basin-discordance sum. [Exact cylinder and scope](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/research/ayh-resource-reset-20261124/joint-renewal/QUARTET_COLLAPSE.md).

The closing obligation remains
\[
\sum_j81^{-j}\sum_{v,w}W_j(v,w)\mathbf1_{f(v)\ne f(w)}<\infty.
\]
Here \(W_j\) counts the **actual original head children** with ordered first-entrance pair \((v,w)\), and \(f\) is the basin-of-one indicator. The previous source-qualified density/rigidity argument supplies the implication to Collatz; this checkpoint does not prove this remaining sum.

### Lean and executed checks

Eight new modules, **26 public theorem declarations**:

| Module | Theorems | Checked interface |
| --- | ---: | --- |
| KilledGradeGreen | 3 | Killed finite-walk Green occupation and level rewards |
| EndpointFibers | 3 | Odd-count uniqueness and endpoint-only entrance cardinality |
| EntranceGrades | 4 | Safe prefixes, exact entrance/missing transfer and finite averaging |
| AffineGradeRigidity | 4 | Two-point slope equality and valuation constraints |
| QuartetCollapse | 4 | Exact all-parameter trajectories and residual profile |
| TripleGradeProduct | 3 | Ordered drift, tie injection and mixed-parity identity |
| MiddleIsolationWindow | 2 | Physical-window isolation and overlap bounds |
| SubcriticalCurvature | 3 | Actual second directional derivatives, covariance contraction and negativity |

The final fresh build passed in **47.877 seconds**, using Lean 4.34.1, Mathlib commit **d13f23b723b8a846827a245b89c10fc7d3f11612**, one worker, autoImplicit=false and warnings as errors. It rebuilt all eight new modules and their four-module local dependency closure into a fresh temporary directory, while reusing the pinned third-party Mathlib cache. The 26 transitive axiom sets contain only propext, Classical.choice and Quot.sound; one theorem is axiom-free.

The coordinator also executed the frozen finite checker: **172,935 digit trials**, **13,181 paired certificates**, four target-set pairs, all four hit/miss patterns under both dilations, and exact rational finite averaging. Exit zero, empty stderr. These checks do not formalize the asymptotic probability theorem.

[Build log](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/reports/ayh-resource-reset-20261124/joint-renewal/lean-build.log) · [Named axiom audit](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/reports/ayh-resource-reset-20261124/joint-renewal/axiom-audit.json) · [Finite replay](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/reports/ayh-resource-reset-20261124/joint-renewal/finite-checks.json) · [Scientific source hashes](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/reports/ayh-resource-reset-20261124/joint-renewal/source-hashes.json)

### Exact published-head validation

- Parent: **578e43911f49d41ef610b368a89b5a1ec269e134**
- Published head: **9ab91d964b38fc870d1034bac628d62f59488467**
- Tree: **50162b090c78750728cb44965ba61ab3fa1d084b**
- The remote tree equals the locally built and reviewed tree.
- The remote commit was fetched into a clean complete checkout: **440 tracked files**.
- The mandatory default validator passed all **five commands** at this exact head; the checkout identity was unchanged afterward.
- Receipt SHA-256: **4e002f13432fc14c7e3cc9f01f8a842fb612997e67abf4bd2b6c4250420ad7ef**
- Repository integrity is separate from mathematical verification. Optional historical regressions were not rerun.

<details>
<summary>Full exact-head validation receipt</summary>

```json
{
  "schema": "collatz-checkout-validation/v1",
  "started_utc": "2026-11-24T08:30:15.518885+00:00",
  "python": "3.12.14 (main, Aug 25 2026, 14:00:49) [Clang 22.1.3 ]",
  "platform": "linux",
  "scope": "structure, frozen identities and selected bounded regressions; not a proof of Collatz",
  "regressions": false,
  "commands": [
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_integration_state.py"
      ],
      "exit_code": 0,
      "stdout": "OK: durable front door and lifecycle practice; 8 integrated records (6 verified local proofs, 1 accepted refutation, 1 source-qualified periodic synthesis), 3 roadmap records, 13 reviewed research families, 314 curated local links, frozen 45/42 PR snapshot preserved.\n",
      "stderr": "",
      "seconds": 0.113
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_review_integration.py"
      ],
      "exit_code": 0,
      "stdout": "OK: 4 qualified assemblies, 9 namespaces, 14 exact blob pins, 8 exact subtree pins, 374 local links, 2 optimized guards; no mathematical verification\n",
      "stderr": "",
      "seconds": 0.271
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_review_integration.py",
        "--self-test"
      ],
      "exit_code": 0,
      "stdout": "SELF-TEST PASS: 8 invalid fixtures rejected; no repository scan or mathematical verification performed\n",
      "stderr": "",
      "seconds": 0.032
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/test_integrity_portability.py"
      ],
      "exit_code": 0,
      "stdout": "PASS: 11 real-Git mode/content/coverage controls; Windows metadata selection simulated on non-Windows; no complete repository scan\n",
      "stderr": "",
      "seconds": 0.058
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "reports/prepublic-2026-09-05/integration-d/check_followup.py",
        "--self-test"
      ],
      "exit_code": 0,
      "stdout": "PASS scoped D follow-up: 7 active files / 7 exact archived originals / 8 dispositions\n{\"overlap_band_cases\": 64, \"quotient_cases\": 81, \"scope\": \"finite edge cases only; not universal Collatz proof checking\", \"signed_residues\": 1584, \"strict_strip_counterexamples\": 2}\nInvalid scoped fixtures rejected: 8\n",
      "stderr": "",
      "seconds": 0.035
    }
  ],
  "success": true,
  "checkout": {
    "commit": "9ab91d964b38fc870d1034bac628d62f59488467",
    "tree": "50162b090c78750728cb44965ba61ab3fa1d084b",
    "tracked_files": 440
  },
  "checkout_after": {
    "commit": "9ab91d964b38fc870d1034bac628d62f59488467",
    "tree": "50162b090c78750728cb44965ba61ab3fa1d084b",
    "tracked_files": 440
  },
  "finished_utc": "2026-11-24T08:30:16.056324+00:00"
}
```

</details>


<details>
<summary>Earlier checkpoints — preserved descriptions and validation receipts</summary>

## Fourth checkpoint: first-passage source bounds and Lean parity marks

**Collatz remains OPEN.** This continuation develops the ordinary global step behind the Aaronson–Yolcu–Heule head reduction. Four GPT-6.2 Astra attack streams and the parent pursued and reviewed the new arguments. The checkpoint adds **six Lean modules with 21 audited public theorems**, written probability and rotation arguments, exact source pins, and a finite physical replay.

**Published head:** `578e43911f49d41ef610b368a89b5a1ec269e134`
**Tree:** `7e7dc25e077d14365c8ecb58713948c93ebbb1f6`
**Previous checkpoint:** `9ed095c3b3386d66c1dba103117e8dda0268b7aa`

[Scientific overview](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/README.md) · [Evidence and independent reviews](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/reports/ayh-resource-reset-20261124/literature-step/README.md) · [Sources and latest PR scope](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/SOURCES.json)

### 1. A checked positive-density theorem on actual discordant pairs

For the shortcut map, let p_n(t) count odd inputs. If n never reaches one, u reaches one at an actual clock q, and n≤2^L, Lean proves at every clock:

`8(p_n(t)−p_u(t)) ≥ t−C`, where `C=5L+4q+4`.

The new forward Pliss count then proves that at least `(N−2C)/15` clocks s<N satisfy

`16(p_(T^s n)(b)−p_(T^s u)(b)) ≥ b` for **every** future block length b.

The full finite count and infinite-future quantifier are kernel-checked. The allowance depends on the pair; no uniform bound on q is supplied. A separate checked theorem supplies arbitrarily late actual height-minimum windows. The two families of clocks are distinct. The sharp real-log speed above 0.1306 has written scope.

[Parity and mark arguments](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/BALLISTIC_COLOR.md) · [Physical inequalities](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/BallisticColor.lean) · [Forward counting theorem](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/ForwardPliss.lean) · [Actual Collatz instantiation](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/DiscordantPliss.lean)

### 2. Actual first passages and all short sliding windows

The new stopped-fiber theorem proves an exact original-source cardinality bound:

`#S ≤ 1 + floor(t U / (3Y))`.

Here all members of S are at most U and share a first entrance below Y, its time t, its endpoint and its odd count, with t≤3Y. No landing-distribution assumption enters.

The written application uses descending thresholds and simultaneous native-grid tests. For every fixed A>1, suitable constants D,K give M=(log₂R)^D and b=ceil(K log₂log₂R), with at most O(R/(log R)^A) exceptional ordinary head sources. Outside the exception each arm enters below M within O(log R) clocks, and every b-step window starting through its first entrance plus b has odd count within b/40 of b/2. This excludes either signed Pliss mark through the smaller of the two actual entrance times plus b. It also treats a partner already on the terminal cycle while the other remains in its controlled range.

Standalone polylogarithmic descent and original-source first-passage counting are credited to Shaik's 2026 primary manuscript. This packet gives a coarse self-contained proof for the sliding-window and paired-mark application. The full probability theorem is written, not among the Lean declarations.

[First-passage proof and prior art](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/FIRST_PASSAGE_MARKS.md) · [Three checked first-passage declarations](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/FirstPassageMarks.lean) · [Independent review](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/reports/ayh-resource-reset-20261124/literature-step/FIRST_PASSAGE_REVIEW.md)

### 3. A precise remaining weighted estimate

For R_j=81^j let W_j(v,w) count original head children whose two actual first entrances land at the ordered pair (v,w) in [M/2,M)² within the specified time bound. Their opposite-color count equals the sum of W_j over opposite-color pairs, up to O(R_j/(log R_j)^A). The error is summable after dividing by R_j.

**Summability of the normalized weighted opposite-color count would prove universal convergence under the separately source-qualified positive lower basin-density input. This summability estimate is not proved.** Small landing integers, few possible pairs, or a time-frequency statement do not bound the actual original-source weights. The new arguments retain those weights rather than assigning a fresh law to the landings.

### 4. Other positive consequences

- **Long common-clock transfer:** profile-dependent binary tests of power-small grid mass pull back to power-small sets of actual head sources after a descent beyond their initial binary-digit window. The proof controls both real endpoints, the profile offset and actual source multiplicity. Arbitrary source restrictions preserve the absolute bound. Finite-state occupation and ballistic block tests are two consumers; neither controls every failed edge.
- **Spatial discrepancy:** for any invariant binary color, every interval of the rescaled logarithmic annulus has discrepancy O(q/sqrt(j)+1/q), for a convergent denominator q of log₈₁2. This gives a shrinking-interval independent-pair closing criterion, even on two separately prescribed residue streams modulo growing powers of 2 and 3. The needed collision probability tending to one remains open.
- **Critical common scales:** for every β>0, arbitrarily high common octaves have actual critical partners m<n^β for all but an exponentially small fraction in each exact fiber. The surplus may change. This does not replace the preceding all-scale same-surplus theorem.

[Long-descent transfer](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/POST_DESCENT_TRANSFER.md) · [Spatial and residue-stream criterion](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/MACROSCOPIC_PAIR_CLOSURE.md) · [Critical partners](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/CRITICAL_SMALL_SCALE.md)

The spatial and summable-error global deductions use Mazur's primary positive lower natural density statement for fixed positive targets, with its exact ordinary-map scope. The source reports a 388-file check at c290ac229b379d2b51026d3e86140496870d6f39; that external build was not reproduced here and is not imported as a project axiom. With only the published Krasikov–Lagarias input, the preceding power criterion at exponent 0.84 remains available. The fixed-grid merger estimate inherited from PR 146 has its separate written scope.

### Verification actually performed

- Final fresh Lean 4.34.1 build: six new modules plus their complete three-module local dependency closure; Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612; one worker, autoImplicit=false, warnings as errors. All **21** public declarations report only subsets of propext, Classical.choice and Quot.sound. Pinned third-party compiled dependencies were reused.
- The direct finite replay enumerated **538,083** actual head children over levels 1–3 and checked **6,643** higher-lift affine profiles. It records finite missed deadlines; it proves no asymptotic count or all-time merger.
- Independent written reviews cover spatial normalization and residue streams, physical transfer and critical reparametrization, all-future mark counts, and adaptive first-passage window coverage. The parent reconstructed the final weighted criterion.
- All **15** research-file hashes are recorded; local Markdown links and exact public-axiom coverage passed. The 26 changed paths contain 1,836 insertions and one navigation-line replacement.

[Build log](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/reports/ayh-resource-reset-20261124/literature-step/lean-build.log) · [Public axiom audit](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/reports/ayh-resource-reset-20261124/literature-step/axiom-audit.json) · [Finite receipt](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/reports/ayh-resource-reset-20261124/literature-step/finite-checks.json) · [Source hashes](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/reports/ayh-resource-reset-20261124/literature-step/source-hashes.json) · [Parent reconstruction](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/reports/ayh-resource-reset-20261124/literature-step/PARENT_REVIEW.md)

### Exact published-head repository validation

The connector-created tree matched the checked local tree exactly. GitHub metadata and Git fetch both returned the published commit above. The mandatory validator then passed all five default commands on the **clean complete checkout of 412 tracked files**, with the same head and tree afterward. The optional historical regression bundle was not run. This is repository integrity, separately from mathematical proof checking.

`python -X utf8 -B tools/validate.py` — exit 0.

Receipt SHA-256: `b46bca0244597b44e046f58ecfef541a646443af81d627637bf58d637937ccd9`.

<details>
<summary>Complete integrity receipt for this exact published head</summary>

```json
{
  "schema": "collatz-checkout-validation/v1",
  "started_utc": "2026-11-24T07:40:59.088217+00:00",
  "python": "3.12.14 (main, Aug 25 2026, 14:00:49) [Clang 22.1.3 ]",
  "platform": "linux",
  "scope": "structure, frozen identities and selected bounded regressions; not a proof of Collatz",
  "regressions": false,
  "commands": [
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_integration_state.py"
      ],
      "exit_code": 0,
      "stdout": "OK: durable front door and lifecycle practice; 8 integrated records (6 verified local proofs, 1 accepted refutation, 1 source-qualified periodic synthesis), 3 roadmap records, 13 reviewed research families, 314 curated local links, frozen 45/42 PR snapshot preserved.\n",
      "stderr": "",
      "seconds": 0.088
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_review_integration.py"
      ],
      "exit_code": 0,
      "stdout": "OK: 4 qualified assemblies, 9 namespaces, 14 exact blob pins, 8 exact subtree pins, 374 local links, 2 optimized guards; no mathematical verification\n",
      "stderr": "",
      "seconds": 0.401
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_review_integration.py",
        "--self-test"
      ],
      "exit_code": 0,
      "stdout": "SELF-TEST PASS: 8 invalid fixtures rejected; no repository scan or mathematical verification performed\n",
      "stderr": "",
      "seconds": 0.038
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/test_integrity_portability.py"
      ],
      "exit_code": 0,
      "stdout": "PASS: 11 real-Git mode/content/coverage controls; Windows metadata selection simulated on non-Windows; no complete repository scan\n",
      "stderr": "",
      "seconds": 0.073
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "reports/prepublic-2026-09-05/integration-d/check_followup.py",
        "--self-test"
      ],
      "exit_code": 0,
      "stdout": "PASS scoped D follow-up: 7 active files / 7 exact archived originals / 8 dispositions\n{\"overlap_band_cases\": 64, \"quotient_cases\": 81, \"scope\": \"finite edge cases only; not universal Collatz proof checking\", \"signed_residues\": 1584, \"strict_strip_counterexamples\": 2}\nInvalid scoped fixtures rejected: 8\n",
      "stderr": "",
      "seconds": 0.034
    }
  ],
  "success": true,
  "checkout": {
    "commit": "578e43911f49d41ef610b368a89b5a1ec269e134",
    "tree": "7e7dc25e077d14365c8ecb58713948c93ebbb1f6",
    "tracked_files": 412
  },
  "checkout_after": {
    "commit": "578e43911f49d41ef610b368a89b5a1ec269e134",
    "tree": "7e7dc25e077d14365c8ecb58713948c93ebbb1f6",
    "tracked_files": 412
  },
  "finished_utc": "2026-11-24T07:40:59.749213+00:00"
}
```

</details>

<details>
<summary>Earlier checkpoints and their original verification records</summary>

## Third checkpoint: ordinary AYH mergers and a sharper closing criterion

**Collatz remains OPEN.** This continuation attacks the positive ordinary-source steps suggested by the Aaronson–Yolcu–Heule rewriting system. Four GPT-6.2 Astra workstreams developed the constructions and independent reviews. The checkpoint adds seven Lean modules, 20 audited public declarations, exact controls and written analytic results with separate scopes.

**Published head:** `9ed095c3b3386d66c1dba103117e8dda0268b7aa`
**Tree:** `676bf46be00fe4d0fb2f0576d8aa82650277df5e`
**Previous checkpoint:** `2fb1f11c959e35eba875338833d84969222dc089`

### 1. Ten physical clocks and four terminal trits

For the shortcut map T, every positive n reaches a state below 600 or x in [7·3^k,8·3^k), k≥4, within ten ordinary steps. All positive states below 600 are kernel-certified to reach one. For n≥600 and the selected head, the positive partner m=floor(x/81) satisfies **7m<5n**, measured against the original source even when the orbit grows.

Lean proves universal convergence iff every such head meets its four-trit truncation at finite, possibly different clocks. A separate kernel certificate proves that every parent in one explicit arithmetic progression modulo 2^172 has **all 81 children** 81m,…,81m+80 at its own same 172-clock endpoint.

[Fixed head and proof scope](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation/FIXED_HEAD.md) · [Lean equivalence](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation/TernaryHeadDescent.lean) · [Whole-fiber certificate](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation/WholeTernaryFiber.lean)

The written growing schedule follows the original orbit to a density-zero section with increasingly many prescribed ternary digits. With D=floor(log₂ n), H=floor(sqrt(D)/log(D+2)), its partner is below (n+1)2^-H. PR 146's identified written finite-grid estimate gives actual mergers outside O(2^D/log(D+2)) exceptions per octave. The deterministic hitting result is separate from that inherited counting input.

[Growing-head construction and conditioning](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation/GROWING_HEAD.md)

### 2. Strong smaller partners within the exact critical strip

In every sufficiently high nonempty fiber with fixed binary exponent d and exact valuation e, at least a 1−δ fraction have an ordinary common future with a critical m≤n^(1−η(δ)) and **exactly the same surplus** 5e−d−1. The Lean theorem checks arithmetic and physical transport from a supplied endpoint merger; the frequency theorem uses the stated written PR 146 estimate. Its output has a long prescribed odd prefix, so a fresh uniform law cannot be restarted automatically.

[Critical compression](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation/CRITICAL_COMPRESSION.md) · [Formal transport](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation/CriticalCompression.lean)

### 3. Actual ancestors of one fixed target

A twelve-cell inverse policy covers every positive ternary unit, including even targets. Lean checks arbitrary-input legality, internal prefix cost and actual single-link clocks. Written concatenation gives a cost of at most 3s+4 at every inverse-odd index.

Combined with a sharper one-sided rotation mesh and the published Krasikov–Lagarias predecessor exponent, the upper counting exponent of the exact critical ancestors of each fixed eligible target is at least **0.654197799645**. Convergence outside any deleted subset of strictly smaller upper exponent therefore suffices. The separately source-qualified exponent 0.901 raises the threshold to **0.701705020810**. The growing-head image retains at least X^(0.84−o(1)) actual ancestors below X at all sufficiently large X, despite having natural density zero.

[Counting theorem, external input and quantifiers](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation/BASIN_COUNTING.md) · [Inverse cover](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation/INVERSE_WORD_COVER.md)

### 4. A stronger closing criterion for actual failed edges

Let D_j count x in the **single** head band [7·81^j,8·81^j) whose orbit never meets that of floor(x/81). The new written theorem proves:

**If Collatz fails, limsup D_j / 81^(0.84j) > 0.**

Thus D_j=o(81^(0.84j)) would settle the conjecture. A suitable upper bound for failures of a finite certificate suffices too. This implication uses exact doubling symmetry, summable changes of a rescaled binary convergence indicator, positive-density subcells and irrational-rotation rigidity on a proper arc. It overcomes the generic single-bad-root objection for this comparison family under the stronger power hypothesis. It does not follow from ancestor counts alone.

The available certificate estimates of order X/sqrt(log X) do not meet the required power bound. **That upper bound remains open.** The full analytic implication is written and independently reviewed. Three supporting Lean declarations check the floor identity, actual halving on the subcells, and generic local ergodic return rigidity.

[Closing criterion](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation/HEAD_EDGE_RIGIDITY.md) · [Formal ingredients](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation/HeadEdgeTransport.lean) · [Independent review](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/reports/ayh-resource-reset-20261124/continuation/EDGE_RIGIDITY_REVIEW.md)

### Verification actually performed

- Final fresh Lean build: seven new modules plus six supporting modules; Lean 4.34.1, Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612; one worker, autoImplicit=false, warnings as errors. All **20 new public declarations** have only standard axioms propext, Classical.choice and Quot.sound.
- Four exact Python controls ran normally and with optimization; all eight runs passed with identical paired output. The compression replay verified 442 smaller critical mergers on 4,096 samples at explicit finite budgets. Other outcomes remain recorded.
- Inverse controls checked all 162 unit classes modulo 243, 16,238 physical inverse links, and an independent twelve-cylinder prefix-cost checker. Three first-return constructions replayed all intermediate clocks, up to source binary exponent 1328.
- Independent written reviews cover the new conditioning, critical lift, fixed-target counting and edge-rigidity argument. The inherited PR 146 probability proof and the published linear-program computation were not re-formalized or replayed.
- Latest-source metadata was frozen through PR 198, with the updated 192 and 196 heads recorded. This is a focused mathematical continuation, not a blanket re-audit of every file in those PRs.

[Research overview](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/research/ayh-resource-reset-20261124/continuation/README.md) · [Evidence and reviews](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/reports/ayh-resource-reset-20261124/continuation/README.md) · [Lean log](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/reports/ayh-resource-reset-20261124/continuation/lean-build.log) · [Source hashes](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/reports/ayh-resource-reset-20261124/continuation/source-hashes.json) · [Finite receipts](https://github.com/GettysburgResearch/collatz/blob/9ed095c3b3386d66c1dba103117e8dda0268b7aa/reports/ayh-resource-reset-20261124/continuation/finite-checks.json)

### Published-head integrity

The pushed tree was compared with the checked local tree and matched exactly. GitHub and Git fetch both returned `9ed095c3b3386d66c1dba103117e8dda0268b7aa`. The required complete-checkout validation then ran at that exact commit in a clean checkout of **387 tracked files**, with unchanged head/tree afterward.

`python -X utf8 -B tools/validate.py` passed all five default commands (exit 0). The optional historical regression bundle was not run. This gate checks repository structure and frozen identities, not mathematical truth.

Finished: `2026-11-24T06:46:08.673877+00:00`.
Receipt SHA-256: `63cf337ebbbe78d2f80eb78079321d75795a9053213c59d0082502d74e435291`.

<details>
<summary>Complete published-head integrity receipt</summary>

```json
{
  "schema": "collatz-checkout-validation/v1",
  "started_utc": "2026-11-24T06:46:07.988766+00:00",
  "python": "3.12.14 (main, Aug 25 2026, 14:00:49) [Clang 22.1.3 ]",
  "platform": "linux",
  "scope": "structure, frozen identities and selected bounded regressions; not a proof of Collatz",
  "regressions": false,
  "commands": [
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_integration_state.py"
      ],
      "exit_code": 0,
      "stdout": "OK: durable front door and lifecycle practice; 8 integrated records (6 verified local proofs, 1 accepted refutation, 1 source-qualified periodic synthesis), 3 roadmap records, 13 reviewed research families, 314 curated local links, frozen 45/42 PR snapshot preserved.\n",
      "stderr": "",
      "seconds": 0.185
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_review_integration.py"
      ],
      "exit_code": 0,
      "stdout": "OK: 4 qualified assemblies, 9 namespaces, 14 exact blob pins, 8 exact subtree pins, 374 local links, 2 optimized guards; no mathematical verification\n",
      "stderr": "",
      "seconds": 0.326
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_review_integration.py",
        "--self-test"
      ],
      "exit_code": 0,
      "stdout": "SELF-TEST PASS: 8 invalid fixtures rejected; no repository scan or mathematical verification performed\n",
      "stderr": "",
      "seconds": 0.036
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/test_integrity_portability.py"
      ],
      "exit_code": 0,
      "stdout": "PASS: 11 real-Git mode/content/coverage controls; Windows metadata selection simulated on non-Windows; no complete repository scan\n",
      "stderr": "",
      "seconds": 0.061
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "reports/prepublic-2026-09-05/integration-d/check_followup.py",
        "--self-test"
      ],
      "exit_code": 0,
      "stdout": "PASS scoped D follow-up: 7 active files / 7 exact archived originals / 8 dispositions\n{\"overlap_band_cases\": 64, \"quotient_cases\": 81, \"scope\": \"finite edge cases only; not universal Collatz proof checking\", \"signed_residues\": 1584, \"strict_strip_counterexamples\": 2}\nInvalid scoped fixtures rejected: 8\n",
      "stderr": "",
      "seconds": 0.034
    }
  ],
  "success": true,
  "checkout": {
    "commit": "9ed095c3b3386d66c1dba103117e8dda0268b7aa",
    "tree": "676bf46be00fe4d0fb2f0576d8aa82650277df5e",
    "tracked_files": 387
  },
  "checkout_after": {
    "commit": "9ed095c3b3386d66c1dba103117e8dda0268b7aa",
    "tree": "676bf46be00fe4d0fb2f0576d8aa82650277df5e",
    "tracked_files": 387
  },
  "finished_utc": "2026-11-24T06:46:08.673877+00:00"
}
```

</details>

<details>
<summary>Earlier checkpoints and their original verification records</summary>

## Why this change

Collatz remains **OPEN**. The full Aaronson–Yolcu–Heule eleven-rule system still needs a terminating argument, and the ordinary-source constructions still need a return below the original induction target. This packet attacks both obligations with new Lean results and explicit failed closing mechanisms.

**Published head:** `2fb1f11c959e35eba875338833d84969222dc089`
**Tree:** `dec94cf76589d28f4d00107bfb7bcbb94651538a`

## 1. A nonlinear AYH interpretation obstruction

On positive integer triples, use coordinatewise weak order and strictness in coordinate zero. Every letter preserves both comparisons. Only binary zero must have nonzero natural-coefficient polynomial coordinates; degree is unrestricted and the other six letter maps may be arbitrary order-compatible functions.

Weak orientation of all eleven rules then rules out strict orientation of any one rule. The proof combines `A²(x) ≤ A⁴(x)` with a literal 32-step all-rule derivation along 41 → 62 → 31 → 47 → 71 → 107 → 161.

Supporting checked results include arbitrary strictly increasing scalar-map rigidity in both word orientations, an extensive-algebra obstruction, and natural-matrix carry defects vanishing on returning digit paths.

## 2. Cofinal ordinary predecessors and a smaller exact section

For every fixed positive target q not divisible by three and every bound, the first checkpoint constructs a larger marked ordinary predecessor n whose initial odd/halving prefix ends at u with `u⁵ ≤ 4⁵ n⁴`, and whose same endpoint u reaches q. Universal convergence is equivalent to convergence on this marked power-descent section.

The second scientific checkpoint sharpens the equivalence. For odd n put `d=floor(log₂ n)`, and mark n by `(d+1)(n−2^d) ≤ 70·2^d`. Require `e=v₂(3n+1)` to be exact. Lean now proves:

**Universal convergence ⇔ convergence of every marked odd n with `d+1 ≤ 5e ≤ d+8`.**

Above these eight possible excess values, the explicit odd quarter partner `m=(n−1)/4` remains marked, is smaller, and satisfies `T(m)=T³(n)`. Its exact excess falls by eight. Strong induction reaches the boundary or the known base one. An odd cofactor in `3n+1=2^e u` enforces exactness; an arbitrary smaller exponent would not prove the refinement.

This connection came from the H=1 case of PR196's half-size merger. The new Lean proof is direct arithmetic and imports no PR196 code. Independent written arguments additionally establish at most one boundary representative per next odd value, and arbitrarily large boundary predecessors hitting the same supplied q. The latter claims are not counted as Lean theorems.

The boundary still contains infinitely many integers. Their next odd values are comparable to n^(4/5) and need not belong to the section. The original inverse construction keeps its supplied endpoint above q. Neither a return to a smaller boundary member nor universal convergence within the boundary is proved.

## 3. Written extensions and latest-source comparison

The packet separately contains independently reviewed written arguments for dimension three with zero auxiliary coordinates, positive coordinates through dimension five, and a constructive positive-monomial/natural-affine equivalence in every dimension. Exact trace controls and a boundary-reset matrix counterexample accompany them.

Bell's theorem is a source-qualified input to the two-base rank argument. Nashida's later natural/arctic barrier primary source was inspected but not rebuilt; neither is a dependency of the main new Lean theorems.

The initial PR inventory ran through 191. Publication readback found PRs 192–196; their metadata were read, and the smaller-partner sources in 193, 195 and 196 received focused reconstruction. PR193's specified partners leave the section and do not beat our original target for sufficiently large row inputs. PR195's direct source family is disjoint from the large marked-power section. PR196 supplies the successful quarter-reduction connection above. This is not a full audit of every branch.

## Verification actually performed

- Fresh final compilation of all **11 modules**, warnings as errors, Lean **4.34.1** and Mathlib **d13f23b723b8a846827a245b89c10fc7d3f11612**.
- **31 new public theorem axiom reports**: only subsets of `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx` or project-specific axioms in those reports.
- Four exact finite checkers passed normally and under `python -O`, with matching paired stdout.
- Ordinary-section replay: **24 rows, 8,216 entries, 728 marked predecessors**, each checked against its original supplied target.
- Critical-section census through 250,000: **6,090 reducible sources and 11,718 boundary members**, with every reduction chain checked and 11,718 distinct exact odd endpoints.
- Four independent internal reviews, with exact file hashes and separate checked/written scopes.
- All **26 research-file hashes** match the delivered manifest. The uploaded tree equals the locally checked tree.
- The exact final remote head above was fetched into a clean complete checkout: **354 tracked files**, clean before and after, all five default repository-integrity checks **passed**. Optional old regressions were not rerun. Repository integrity is separate from mathematical verification.

## Reading order

1. [Scientific overview](https://github.com/GettysburgResearch/collatz/blob/2fb1f11c959e35eba875338833d84969222dc089/research/ayh-resource-reset-20261124/README.md)
2. [AYH arguments and failed strengthenings](https://github.com/GettysburgResearch/collatz/blob/2fb1f11c959e35eba875338833d84969222dc089/research/ayh-resource-reset-20261124/GLOBAL_METHODS.md)
3. [New critical-section proof](https://github.com/GettysburgResearch/collatz/blob/2fb1f11c959e35eba875338833d84969222dc089/research/ayh-resource-reset-20261124/positive-section/CRITICAL_SECTION.md) · [Lean](https://github.com/GettysburgResearch/collatz/blob/2fb1f11c959e35eba875338833d84969222dc089/research/ayh-resource-reset-20261124/positive-section/CriticalSection.lean)
4. [Focused latest-source comparison](https://github.com/GettysburgResearch/collatz/blob/2fb1f11c959e35eba875338833d84969222dc089/research/ayh-resource-reset-20261124/LATEST_SOURCE_CONNECTIONS.md)
5. [Build, independent review and execution receipts](https://github.com/GettysburgResearch/collatz/blob/2fb1f11c959e35eba875338833d84969222dc089/reports/ayh-resource-reset-20261124/README.md)

Earlier source checkpoints remain in branch history: `8d9be8ad35b440626fa8efb1ee93b9376a2441fd` (initial science), `840c4b16099c392010b66a3e51b7ad55ef789dad` (its integrity receipt), and the current second scientific checkpoint. This contribution stays in research and reports; it does not upgrade the canonical acceptance registry.

<details>
<summary>Complete integrity receipt for the exact final published head</summary>

```json
{
  "schema": "collatz-checkout-validation/v1",
  "started_utc": "2026-11-24T04:40:28.601787+00:00",
  "python": "3.12.14 (main, Aug 25 2026, 14:00:49) [Clang 22.1.3 ]",
  "platform": "linux",
  "scope": "structure, frozen identities and selected bounded regressions; not a proof of Collatz",
  "regressions": false,
  "commands": [
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_integration_state.py"
      ],
      "exit_code": 0,
      "stdout": "OK: durable front door and lifecycle practice; 8 integrated records (6 verified local proofs, 1 accepted refutation, 1 source-qualified periodic synthesis), 3 roadmap records, 13 reviewed research families, 314 curated local links, frozen 45/42 PR snapshot preserved.\n",
      "stderr": "",
      "seconds": 0.084
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_review_integration.py"
      ],
      "exit_code": 0,
      "stdout": "OK: 4 qualified assemblies, 9 namespaces, 14 exact blob pins, 8 exact subtree pins, 374 local links, 2 optimized guards; no mathematical verification\n",
      "stderr": "",
      "seconds": 0.272
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_review_integration.py",
        "--self-test"
      ],
      "exit_code": 0,
      "stdout": "SELF-TEST PASS: 8 invalid fixtures rejected; no repository scan or mathematical verification performed\n",
      "stderr": "",
      "seconds": 0.05
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/test_integrity_portability.py"
      ],
      "exit_code": 0,
      "stdout": "PASS: 11 real-Git mode/content/coverage controls; Windows metadata selection simulated on non-Windows; no complete repository scan\n",
      "stderr": "",
      "seconds": 0.073
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "reports/prepublic-2026-09-05/integration-d/check_followup.py",
        "--self-test"
      ],
      "exit_code": 0,
      "stdout": "PASS scoped D follow-up: 7 active files / 7 exact archived originals / 8 dispositions\n{\"overlap_band_cases\": 64, \"quotient_cases\": 81, \"scope\": \"finite edge cases only; not universal Collatz proof checking\", \"signed_residues\": 1584, \"strict_strip_counterexamples\": 2}\nInvalid scoped fixtures rejected: 8\n",
      "stderr": "",
      "seconds": 0.032
    }
  ],
  "success": true,
  "checkout": {
    "commit": "2fb1f11c959e35eba875338833d84969222dc089",
    "tree": "dec94cf76589d28f4d00107bfb7bcbb94651538a",
    "tracked_files": 354
  },
  "checkout_after": {
    "commit": "2fb1f11c959e35eba875338833d84969222dc089",
    "tree": "dec94cf76589d28f4d00107bfb7bcbb94651538a",
    "tracked_files": 354
  },
  "finished_utc": "2026-11-24T04:40:29.141007+00:00"
}
```

</details>

</details>


</details>

</details>
