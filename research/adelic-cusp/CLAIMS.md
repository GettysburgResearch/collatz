# Claim ledger: adelic cusp Fourier packet

This is an isolated `93xx` namespace for issue #15. It is not a replacement for any canonical root ledger and does not renumber claims on unmerged branches.

| ID | Type | Status | Short title | Dependencies |
|---|---|---|---|---|
| `D-9301` | Definition/construction | `PROPOSED` | Stationary survivor measure on `Z_2` | elementary 2-adic convergence |
| `D-9302` | Definition/construction | `PROPOSED` | Adelic natural extension and integer section | `D-9301`; elementary quotient algebra |
| `D-9303` | Definition/construction | `PROPOSED` | Stationary triadic mirror measure | elementary 3-adic convergence and separation |
| `L-9301` | Lemma | `PROPOSED` | Moving-character survivor Fourier identity | `D-9301`; issue-#4 notation crosswalk |
| `L-9302` | Lemma | `PROPOSED` | Conditional weighted shell tail from frequency-block means | elementary interval decomposition |
| `L-9303` | Lemma | `PROPOSED` | Phase energy controls the survivor Fourier product | `L-9301`; elementary cosine inequality |
| `L-9304` | Lemma | `PROPOSED` | Exact 2–3 phase reciprocity and valuation shift | elementary modular arithmetic; LTE reproved locally |
| `L-9305` | Lemma | `PROPOSED` | Moving-character triadic Fourier identity | `D-9303` |
| `L-9306` | Lemma | `PROPOSED` | Full-group absolute moments factor exactly | `T-9304`; CRT; Parseval for `p=2` |
| `L-9307` | Lemma | `PROPOSED` | Global rational diagonal and bilateral phase stitching | `L-9301`, `L-9305`, `T-9304`; circle reciprocity |
| `L-9308` | Lemma | `PROPOSED` | Complex bilateral phase stitching | `L-9307`; local character conventions |
| `L-9309` | Lemma | `PROPOSED` | Lift-digit prefixes are residue classes modulo `81^L` | `L-9307`; elementary modular lifting |
| `L-9310` | Lemma | `PROPOSED` | Completion-height rigidity for integral phase carries | elementary modular lifting and height separation |
| `L-9311` | Lemma | `PROPOSED` | Repeated itinerary factors are orbit-difference zero-carry chains | `D-9302`; integer divisibility |
| `L-9312` | Lemma | `PROPOSED` | Centered `81/64` orbits force a three-state four-phase `3/2` schedule | `T-9315`; residue arithmetic modulo `64` |
| `L-9313` | Lemma | `PROPOSED` | Every itinerary has one bounded error path; ordinary realization is cylinder stabilization | elementary affine recurrence; `T-9315` crosswalk |
| `L-9314` | Lemma | `PROPOSED` | Exact appended base-`M` digit of the nearest-integer cylinder | `L-9313`; finite affine iteration |
| `T-9301` | Conditional theorem | `SUPERSEDED` | Conditional polynomial-window reduction | superseded by self-contained `T-9308` |
| `T-9302` | Conditional theorem | `SUPERSEDED` | Conditional density-one full EQ | superseded by unconditional `T-9309` |
| `T-9303` | Theorem | `PROPOSED` | Valuation-stratified fixed-frequency depth-period decay | `L-9304`; exact cosine-grid second moment |
| `T-9304` | Theorem | `PROPOSED` | Stationary two-place CRT Fourier factorization | `L-9301`, `L-9305`; CRT |
| `T-9305` | Theorem | `PROPOSED` | Split collapse and weighted discrepancy equivalence | `L-9307`; cosine Lipschitz and product telescoping |
| `T-9306` | Theorem | `PROPOSED` | Complex coefficient and bounded test-sequence equivalence | `L-9308`; complex-mask Lipschitz and telescoping |
| `T-9307` | Theorem | `PROPOSED` | Low-energy lift prefixes have an explicit entropy deficit | `L-9309`; exponential moments; `L-9303` for Fourier corollary |
| `T-9308` | Theorem | `PROPOSED` | Uniform harmonic high-frequency tail at every depth | `T-9307`, `T-9305`; geometric shell summation |
| `T-9309` | Theorem | `PROPOSED` | Unconditional full weighted EQ on density-one depths | `T-9303`, `T-9308`; valuation strata and Markov |
| `T-9310` | Theorem | `PROPOSED` | Weighted EQ converges in uniform density | `T-9303`, `T-9308`; translated-period Markov bounds |
| `T-9311` | Theorem | `PROPOSED` | Uniform pointwise cusp decay on every subexponential numerator window | `L-9310`, `L-9303`, `T-9305`, `L-9301` |
| `T-9312` | Theorem | `PROPOSED` | Complete weighted EQ at every depth | `T-9311`, `T-9308`; harmonic splitting |
| `T-9313` | Theorem | `PROPOSED` | Fixed-room equivalence and exact `C_j`/`R_j` minimum duality | `D-9302`, `D-9303`, `L-9301` |
| `T-9314` | Theorem | `PROPOSED` | Exact depth-46 minimum survivor; ordinary rooms exceed `2^227` | `T-9313`, `X-9303` |
| `T-9315` | Theorem | `PROPOSED` | Ordinary binary-chart orbits are exactly critical centered rational-power orbits | elementary nearest-integer arithmetic; `D-9302` crosswalk |
| `T-9316` | Theorem | `PROPOSED` | Efficient recurrence cone; Thue--Morse cylinder blocks do not stabilize | `L-9311`, `L-9313`, `T-9315` |
| `T-9317` | Conditional theorem | `PROPOSED / CONDITIONAL` | Exact threshold/equality bridge for Dubickas-type bounds | `T-9315`, `T-9316` |
| `R-9301` | Refutation | `PROPOSED` | Exact carry prefixes do not amplify to consecutive intervals | `L-9309` |
| `R-9302` | Refutation | `PROPOSED` | Matching repetition/carry criticalities do not contradict | `L-9310`, `L-9311` |
| `R-9303` | Refutation | `PROPOSED` | Pure real scheduled-cylinder emptiness cannot close the ordinary section | `L-9312`, `L-9313` |
| `C-9301` | Historical conjecture | `SUPERSEDED` | Harmonic control of low-energy cylinders | superseded by `L-9310`, `T-9311`, `T-9312` |
| `Q-9301` | Open question | `IDEA` | Integer-section intersection | `D-9302`; issue-#4 M1 translation |
| `Q-9302` | Open question | `IDEA` | Fixed-room and active-cylinder nonstabilization | `D-9302`, `D-9303`, `L-9310`--`L-9314`, `T-9312`--`T-9317` |
| `Q-9303` | Open question | `IDEA` | Centered nearest-integer cylinder nonstabilization and source specialization | `T-9315`--`T-9317`, `L-9312`--`L-9314`, `R-9303` |
| `O-9301` | Observation | `EMPIRICAL` | Bounded polynomial-window scattering census | `X-9301` |
| `O-9302` | Observation | `EMPIRICAL` | Bounded carry counts and zero-run census | `X-9302` |
| `O-9303` | Observation | `INTERNAL EXACT COMPUTATION` | Exact dual minima and survivor replays through depth 46 | `X-9303` |
| `O-9304` | Observation | `EMPIRICAL` | Exact finite-prefix centered reconstructions and phase schedules | `X-9304` |
| `O-9305` | Observation | `EMPIRICAL` | Exact finite Thue--Morse block and square replay | `X-9305` |
| `X-9301` | Experiment | `EMPIRICAL` | Exact cusp-scattering probe through depth 80 | standard-library exact modular arithmetic |
| `X-9302` | Experiment | `EMPIRICAL` | Exact completion-height carry audit through depth 80 | standard-library exact modular arithmetic and fractions |
| `X-9303` | Experiment | `INTERNAL EXACT COMPUTATION` | Meet-in-the-middle exact survivor-minimum certificate | exact modular subset sums and direct replay |
| `X-9304` | Experiment | `EMPIRICAL` | Exact centered-power reconstruction and four-phase replay | standard-library integers and fractions |
| `X-9305` | Experiment | `EMPIRICAL` | Exact Thue--Morse appended-block audit through index 1024 | standard-library exact integers |

## Status boundary

- Every complete-looking native argument remains `PROPOSED` pending independent reconstruction.
- `T-9312` is the strongest finite-set theorem: complete weighted EQ tends to zero at every depth.
- `T-9313` gives exact fixed-room coherence and the finite minimum identity
  \[
  \min(R_j\setminus\{0,1\})
  =
  \left\lceil
  \min(C_j\setminus\{0,1\})(64/81)^j
  \right\rceil.
  \]
- `T-9314` and `X-9303` compute the exact first nontrivial depth-46 survivor and exclude every nontrivial infinite ordinary room through `2^227`.
- `T-9315` gives the exact centered-power equivalence
  \[
  \Phi(\{0,1\}^{\mathbb N})\cap\mathbb Z_{\ge2}\ne\varnothing
  \iff
  \exists\xi>0:\ \|\xi(81/64)^n\|\le1/81\ \forall n.
  \]
- `L-9313` proves that the bounded real error language is a full shift. Ordinary realization is the arithmetic question whether the nested nearest-integer cylinders stabilize.
- `L-9314` gives the exact appended block; eventual zero is exactly ordinary stabilization.
- `T-9316` adds the first infinite symbolic family for which nonstabilization is proved: every finite shift or complement of the Thue--Morse word has infinitely many nonzero appended blocks.
- `T-9317` freezes the source bridge: a Dubickas-type lower constant greater than `1/81` closes immediately, while equality at `1/81` also closes if the equality language has efficient recurrence, including shifted/complemented Thue--Morse.
- `X-9305` is bounded evidence only. It checks 1024 Thue--Morse block extensions but is not a premise of `T-9316`.
- `Q-9301` remains open. Neither an exact reformulation, a finite exact minimum, nor exclusion of one extremal family is an all-itinerary theorem.
- No positive integer survivor, divergent orbit, cycle, universal Collatz-counterexample bound, or Collatz resolution is claimed.

## Main implication graph

```text
L-9309 lift-chain arithmetic
   -> L-9310 completion-height carry rigidity
   -> T-9311 subexponential-window decay

L-9309 -> T-9307 prefix entropy -> T-9308 harmonic tail

T-9311 + T-9308 -> T-9312 all-depth weighted EQ
```

The ordinary-section chain is now:

```text
D-9302 integral tails + bounded real companion
   + D-9303 triadic past classes
   + L-9301 finite survivor coding
   |
   +-------------------------------+
   |                               |
   v                               v
T-9313 fixed-room              T-9315 centered
and minimum duality            rational-power equivalence
   |                               |
   + X-9303 exact minimum           v
   |                          L-9313 full real shift
   v                          + nearest-integer cylinders
T-9314 depth-46 bound               |
                                   v
                              L-9314 appended blocks
                                   |
                 +-----------------+------------------+
                 |                                    |
                 v                                    v
        T-9316 recurrence cone              Q-9303 all-itinerary
        + Thue--Morse exclusion             nonstabilization
                 |
                 v
        T-9317 source threshold/equality bridge
                 |
                 v
        Q-9301 ordinary-section nonintersection
```

Method closures:

```text
L-9311 orbit-difference zero carries
   + L-9310 reciprocal-character zero carries
   -> R-9302 identical criticality does not double-count

L-9312 scheduled real geometry
   + L-9313 full symbolic support
   -> R-9303 pure real-cylinder emptiness is insufficient
```

## Generalization and literature crosswalk

`L-9310`, `L-9313`, `L-9314`, and `T-9315` are stated for every coprime expanding pair `M<N`.

For `64 -> 81`, the wave-5 literature audit correctly identifies the appended blocks, not the real intervals, as decisive. It requests exact specialization of Dubickas 2006/2008 at radius `1/81`, including the extremal Thue--Morse sign word.

`T-9316` supplies the native extremal-word half: every shifted/complemented Thue--Morse sign itinerary fails ordinary stabilization. `T-9317` shows why this matters—a critical equality theorem can be as decisive as a strict lower bound once its equality language is classified.

No source formula is inferred from an abstract. The exact constant, quantifiers, endpoints, and equality classification remain an acquisition task.

## Branch crosswalk

- issue-#4 `C_j` recursion = the reductions of `D-9303`;
- issue-#4 finite Cantor product = `L-9305`;
- exact CRT transform of `R_n x C_j` = `T-9304`;
- integral carries and prefix entropy assemble into all-depth EQ = `T-9312`;
- one ordinary itinerary has one fixed room across every past/future split = `T-9313`;
- finite Cantor minima transform exactly into finite survivor minima = `T-9313(18)`;
- the depth-46 dual computation yields `T-9314`;
- ordinary-section points are exactly positive critical centered `81/64` orbits = `T-9315`;
- every itinerary has a real error lift but selects one `2`-adic nearest-integer cylinder = `L-9313`;
- the appended cylinder block is explicit = `L-9314`;
- efficient repeated factors obstruct stabilization = `T-9316`;
- the Dubickas threshold/equality trichotomy is `T-9317`;
- `Q-9302` and `Q-9303` target monotone minimum divergence and all-itinerary nearest-integer cylinder nonstabilization.
