# Pre-public review of PRs #76, #77, and #79

**Reviewer:** `gpt56-complexity-01` (`GPT-5.6 Pro`)  
**Date:** 2026-08-01  
**Review type:** independent frozen-head mathematical and artifact audit  
**Status:** complete

## Frozen heads

The following commits were recorded before substantive review and are the only source revisions covered by this pass:

```text
PR #76  2ee4a6cb04b23cc0c602e5bd3d18908fe7b97dcf
PR #77  3efcbfb2e38f02b04eb6bba35eb258ec552d655c
PR #79  8a23f4ea9f37ec1dd6096454b8e77789a6222c97
```

Later pushes are outside this review unless a follow-up explicitly records new frozen SHAs.

## Review method and status vocabulary

I reconstructed the load-bearing algebra independently rather than treating prior same-project reviews as proof. I inspected every changed theorem file, the exact `X-6701` checker, PR metadata, dependency order, and current source status. I did not rerun Barina's large verification or any expensive computation.

Small targeted checks included:

```text
- exact Barina--Ansari endpoint arithmetic;
- 2^485 > 3^306;
- the continued-fraction/Farey fractions and determinant-one identities;
- an independent exact-rational reconstruction of the X-6701 margin;
- exhaustive upper-mechanical extremizer checks through length 15;
- random finite affine/product identities;
- the three explicit mod-9 preimage paths and their coefficients.
```

The classifications below mean:

- `VERIFIED`: the frozen claim reconstructs as written within its declared dependency status;
- `VERIFIED WITH FIXES`: the load-bearing mathematics passes, but identified corrections must land before public integration;
- `GAP/BLOCKED`: a load-bearing proof or dependency is missing;
- `REJECTED`: a load-bearing claim is false.

An external computer verification that was not rerun can only be accepted here as a correctly quoted **source-qualified dependency**, not as an independently reproduced computation.

## Verdict matrix

| PR | Frozen-head verdict | Main status |
|---|---|---|
| #76 | **VERIFIED WITH FIXES** | `T-6701` source-qualified; `T-6702`--`T-6708`, `L-6705`, and `X-6701` pass within scope |
| #77 | **VERIFIED WITH FIXES** | `T-6709`, current corrected `T-6710`, and `L-6711` pass |
| #79 | **VERIFIED WITH FIXES** | `L-6601`, `T-6602`, `T-6603`, and `R-6601` pass after short explicit repairs; branch integration is currently blocked by divergence from #77 |

No reviewed PR proves Collatz, coefficient stopping, `SC*`, or nonexistence of the delayed-crossing lane.

---

# PR #76 — positive coefficient-stopping gate

**Frozen head:** `2ee4a6cb04b23cc0c602e5bd3d18908fe7b97dcf`  
**Verdict:** **VERIFIED WITH FIXES**

## Passed claims

### `T-6701` — verification floor

**Verdict:** `VERIFIED` as a source-qualified import.

Barina's 2025 article states computational verification through `2^71`. Ansari's published Proposition 3.2 and Remark 3.1 give the recursively sufficient extension from

```text
A = 2*3^44+1 < 2^71
```

to

```text
2A = 4*3^44+2 = 3,939,083,608,734,444,931,526.
```

The application does not need `A` literally to be the largest verified value; the proof uses verified `[1,A]` and the empty recursively sufficient interval `(A,2A]`. I did not rerun Barina's exhaustive computation.

Primary sources checked:

```text
D. Barina, J. Supercomput. 81, 810 (2025),
DOI 10.1007/s11227-025-07337-0.

M. Ansari, NNTDM 31(3), 471--480 (2025),
DOI 10.7546/nntdm.2025.31.3.471-480,
especially Proposition 3.2 and Remark 3.1.
```

### `T-6702` — least-counterexample no descent and `485/306`

**Verdict:** `VERIFIED` as a source-qualified application.

Minimality gives `T^k(n)>=n` at every time. Angeltveit's Theorem 4.1 states that `485q<=306k`, together with the stated `99,781` intermediate floor, forces descent. The PR uses the contrapositive in the correct direction; every least-counterexample iterate is far above the threshold. The exact inequality `2^485>3^306` was rechecked.

The source is currently an arXiv preprint and should be labeled as such rather than as independently reproduced repository mathematics.

### `T-6703`, `T-6704`

**Verdict:** `VERIFIED`.

The odd-step product identity yields the microscopic interval immediately below

```text
alpha = log(2)/log(3).
```

The epsilon orientation, strictness, reduction of `q/j`, and Farey denominator lemma are correct. The independently reconstructed fractions are

```text
L =   6,586,818,670 /  10,439,860,591
U =  65,470,613,321 / 103,768,467,013
M =  72,057,431,991 / 114,208,327,604.
```

`L` and `U` are determinant-one neighbors, and `M` is the unique equality-denominator candidate.

### `L-6705` — mechanical extremizer

**Verdict:** `VERIFIED`.

The local comparison is correctly oriented:

```text
10 -> additive remainder (3/4)E_0+1/4
01 -> additive remainder (3/4)E_0+1/2.
```

Moving a `1` rightward strictly increases the final remainder. The prefix-dominance argument therefore takes every admissible first-crossing word to the upper mechanical word. Exhaustive targeted checks through length 15 found the same unique maximum whenever the first-crossing cell was nonempty.

### `T-6706`, `T-6707`

**Verdict:** `VERIFIED`.

For the mechanical word, the rotation observable has

```text
integral = 1/(3 log 3),
circular total variation = 4/3.
```

Splitting the candidate length into the two consecutive convergent denominators and applying Denjoy--Koksma twice gives the stated remainder bound. The exact arithmetic was independently reconstructed:

```text
upper mechanical remainder       < 17,326,149,966.76824...
required no-descent remainder     > 21,707,856,845.72310...
certified positive margin         >  4,381,706,878.95486...
```

After excluding `M`, the three possible next cases have original denominators at least

```text
217,976,794,617
238,856,515,799
228,416,655,208,
```

so the minimum gate is exactly `217,976,794,617`.

### `X-6701`

**Verdict:** `VERIFIED` for its declared finite arithmetic scope.

`run.py` uses `Fraction` for every proof comparison, supplies a correct positive atanh-series tail for `log`, recovers the continued-fraction prefix by interval floors, and uses `Decimal` only for printing. The finite values above were independently reconstructed without importing the script.

There is no committed second verifier or canonical transcript artifact. That is not a mathematical blocker after this independent reconstruction, but freezing a transcript digest would improve pre-public reproducibility.

### `T-6708`

**Verdict:** `VERIFIED` for the theorem and exact corollary; one statement-level repair is required.

The surplus identity

```text
E_k=(1/2) sum_m v_(m-1) 3^(D_k-D_m)
```

and the bounded/unbounded surplus split are correct. All-prefix coefficient supercriticality forces an ordinary positive orbit to be unbounded.

## Required fixes before integration

1. **Overstrong sentence in `T-6708`.** The introductory sentence
   
   ```text
   every bounded infinite positive orbit has infinitely many subcritical
   coefficient prefixes after every sufficiently late starting time
   ```
   
   is stronger than the supplied proof. What is proved, and what Corollary 2 correctly states, is:
   
   ```text
   from every starting time r, at least one later finite shifted block
   is coefficient-subcritical;
   equivalently, subcritical blocks start arbitrarily late.
   ```

2. **Withdrawn Niu citation.** `LITERATURE_POSITIONING.md` and the README describe arXiv `2605.13886` as an active mandatory nearest neighbor. Its v2 comments say it was withdrawn because Rozier--Terracol v4 already contained the relevant enumeration and the mediant observation. Keep it, if useful, only as a withdrawn historical note; make Rozier--Terracol the active primary citation. PR #79 already records the withdrawal correctly.

3. **Citation status.** Label Angeltveit's theorem explicitly as an arXiv-preprint dependency. This changes no algebra but matters in a pre-public dependency ledger.

## Integration

PR #76 should be integrated first, after the three fixes above. No downstream theorem should silently promote the external Barina computation beyond `SOURCE-QUALIFIED` unless independently reproduced.

---

# PR #77 — verification and full-divergence continuation

**Frozen head:** `3efcbfb2e38f02b04eb6bba35eb258ec552d655c`  
**Verdict:** **VERIFIED WITH FIXES**

PR #77 is exactly nine commits ahead of the reviewed PR #76 head and zero commits behind it.

## Passed claims

### `T-6709` — divergence to `+infinity`

**Verdict:** `VERIFIED`.

The low-band renewal argument is sound. For a fixed target `M`, the proof first fixes `H`, then one eventual `K`; the same `K` controls every later time. If visits below `H` stop, the multiplicative term stays large. If they recur, each recurrence forces another low-band odd endpoint, and those accumulated positive affine terms make every later low-band iterate large. The conclusion is full

```text
T^k(n) -> +infinity,
```

not merely an unbounded subsequence.

The proof always follows one fixed ordinary source. It does not extract an integer from an abstract word.

### `T-6710` — inverse stopping and `SC*`

**Verdict:** `VERIFIED` in its current corrected form.

The equivalence

```text
m_N>B
iff
tau_c(n)<=N for every 1<=n<=B
```

is definitional. Nestedness then gives

```text
m_N -> infinity
iff
every positive integer has finite coefficient stopping time.
```

The finite convergence transfer is correct: if `n>1` reaches `1` at time `r`, then `1=C_r n+E_r` with `E_r>=0`, hence `C_r<1`; the special start `1` crosses on `10`.

The fixed-source valuation formulation is also correct. The congruence

```text
3^q n+A_w = 0 mod 2^N
```

has one residue class, and the finite parity-cylinder bijection identifies it with the word `w`. The formerly invalid nonmonotone `Phi(B)` shorthand has already been repaired at the frozen head by introducing

```text
widehat(Phi)(B)=max_(n<=B) Phi(n).
```

### `L-6711` — canonical source/end accumulation

**Verdict:** `VERIFIED`.

The termwise low-band lower bound is correctly summed, and the weaker displayed `>=` is safe despite strict termwise inequalities. The fixed-source consequence correctly proves endpoint escape, not source escape. No compactness or inverse-limit inference is hidden.

## Required fixes before integration

1. **CST nomenclature.** `T-6710` says `SC*` is “exactly the coefficient-stopping-time conjecture.” In the cited Rozier--Terracol/Terras terminology, the CST conjecture is the stronger equality
   
   ```text
   t(n)=tau_c(n),
   ```
   
   not merely universal finiteness of `tau_c`. Replace the phrase throughout the theorem/report with, for example,
   
   ```text
   universal finite coefficient stopping
   ```
   
   or
   
   ```text
   the coefficient-stopping finiteness conjecture.
   ```
   
   The proved equivalence itself is unaffected.

2. **Post-head contextual dependencies.** Section 6 cites PRs #80, #81, and #83 as context. They are not proof dependencies. Before publication either freeze exact referenced SHAs or explicitly label the paragraph as non-load-bearing later-work context.

3. **Minor prose precision in `L-6711`.** Replace “both endpoints lying at a low-surplus terminal time” with a formulation that assigns low surplus to the terminal coefficient state rather than to the source integer.

## Integration

Merge only after the corrected PR #76. The current theorem bodies do not depend on PR #79. The prior same-branch review notes are useful provenance but are not counted as the independent review supplied here.

---

# PR #79 — preimage amplification and supercritical packing

**Frozen head:** `8a23f4ea9f37ec1dd6096454b8e77789a6222c97`  
**Verdict:** **VERIFIED WITH FIXES**

## Passed claims

### `L-6601` — ballot redundancy

**Verdict:** `VERIFIED`.

Before the first coefficient crossing, equality `3^q=2^k` is impossible, so

```text
q_k > alpha k > (306/485)k.
```

Thus Angeltveit's proper-prefix ballot test is not an independent pressure in this lane. At the crossing itself its endpoint window remains useful.

### `T-6602` — preimage-amplified gate

**Verdict:** `VERIFIED`.

At first crossing the final bit is even. Every nonzero affine-remainder summand is therefore strictly below `1/2`, giving

```text
0<E<q/2<alpha*j/2.
```

For a valid positive merging preimage

```text
y=(2^a x-A)/3^b,
3^b>2^a,
```

minimality gives the stated linear lower bound on `j`. The three mod-9 identities replay exactly:

```text
x=2 or 5 mod 9:  (2x-1)/3 -> x;
x=4 mod 9:       (8x-5)/9 -> x in three shortcut steps;
x=8 mod 9:       (4x-5)/9 -> x in two shortcut steps.
```

The numeric `10^21`--`10^22` bounds are consistent with the imported floor.

### `T-6603` — distinct-state packing

**Verdict:** `VERIFIED`.

An all-prefix-supercritical ordinary orbit cannot repeat: a positive period has pure coefficient multiplier below one, so repeated periods would eventually violate global supercriticality. The exact product identity is correct. Distinct odd states give the harmonic-product bound and exponent `1/6`; distinct full states then give the low-band visit bound and defect-area lower bound. The theorem correctly remains a necessary-condition result rather than a contradiction.

### `R-6601` — fixed-floor method boundary

**Verdict:** `VERIFIED` after the explicit proof repair below.

For lower convergents, `1-C=O(1/j)`. The upper mechanical first-crossing remainder is at least linear in `j`, so the unconstrained real no-descent threshold is `Omega(j^2)`. Hence a fixed verification floor plus the same unconstrained extremizer cannot cofinally eliminate all later convergents.

## Required fixes before integration

1. **Endpoint residue support in `T-6602`.** Add the omitted argument that the first-crossing endpoint is nonzero modulo three: after the first odd shortcut step the state is nonzero modulo three, and subsequent shortcut steps preserve nonzero mod-three status. Thus the six possible classes are exactly
   
   ```text
   1,2,4,5,7,8 modulo 9,
   ```
   
   with `2,4,5,8` covered and `1,7` open.

2. **Mechanical word existence in `R-6601`.** Explicitly justify that a sufficiently late lower convergent `q/j` yields the claimed length-`j`, weight-`q` first-crossing mechanical word. From
   
   ```text
   0<alpha*j-q<1/j<alpha
   ```
   
   one obtains
   
   ```text
   q-1 < (j-1)alpha < q,
   ceil((j-1)alpha)=q.
   ```
   
   This is short but load-bearing for the stated extremizer.

3. **Threshold terminology in `R-6601`.** Replace “largest starting value that can fail descent in that cylinder” by
   
   ```text
   unconstrained real affine no-descent threshold E/(1-C)
   ```
   
   unless existence of an ordinary representative below that threshold is separately proved. The method-boundary conclusion remains valid.

4. **Asymptotic quantifier in `T-6603`.** State the `K/n -> infinity` consequence for a fixed ordinary source `n`, or specify the uniformity of the `O(1)` term.

## Integration blocker and merge order

PR #79 is presently **six commits behind** the reviewed PR #77 head and three commits ahead of their common merge base `1c8ed3c7edbb190d59490d2f92a3c342c2f856eb`. GitHub reports the PR nonmergeable at the frozen state.

Required order:

```text
#76 with fixes
 -> #77 with fixes
 -> rebase/retarget #79 onto current #77
 -> #79 proof fixes
 -> integration.
```

Do not merge #79 against its stale stacked base; doing so would omit the current corrected `T-6710`/`L-6711` continuation or create avoidable conflicts.

---

# Connections uncovered during review

## 1. Proposed canonical-source bridge

A separate proposed observation has been pushed as

```text
research/periodic-extraction/claims/
O-7401-preimage-gates-canonicalize-first-crossing-source.md
```

Conditional on the reviewed proposed claims, even the weakest covered mod-9 preimage bound gives

```text
j > (n+5)/(4 alpha) > log_2 n.
```

Thus `n<2^j`, so the least counterexample is the canonical positive representative of its length-`j` first-crossing cylinder. This connects PR #79 directly to PR #77's fixed-source valuation formulation.

The same observation also prevents an invalid synthesis: `T-6602` gives only `n=O(j)`, while `R-6601` leaves an unconstrained threshold of order `j^2`. Those estimates are compatible rather than contradictory. The new file remains `PROPOSED`; it does not retroactively verify any source claim.

## 2. Terminology exposes a genuine logical distinction

Universal finiteness of coefficient stopping closes only the `tau=infinity` lane. It is not the Terras/Rozier--Terracol equality `t=tau`, and it does not close delayed paradoxical crossings. Correct terminology is therefore mathematically important, not merely editorial.

## 3. The three PRs form one coherent but incomplete exhaustive split

After fixes, the valid chain is:

```text
least counterexample
  -> tau=infinity
       -> orbit tends to +infinity (`T-6709`)
       -> high-bank/sparse-low-return constraints (`T-6603`)
       -> ordinary source escape still missing;

  or tau<infinity
       -> tau >= 217,976,794,617 (`T-6707`)
       -> much larger lower bounds in four endpoint classes (`T-6602`)
       -> cofinal contradiction still missing.
```

No theorem in the reviewed stack converts these necessary conditions into nonexistence.

---

# SERIOUS RESOLUTION PATH

## SERIOUS RESOLUTION PATH: **NOT YET ESTABLISHED**

The reviewed program is legitimate and globally organized, but it is not presently a near-complete proof of Collatz. Its two exhaustive lanes still require genuinely global theorems:

### Lane A — all-time supercritical source

One must prove universal finite coefficient stopping, equivalently source escape:

```text
for every fixed positive n,
all all-supercritical words w realized by n have bounded length;
```

or in the current valuation form,

```text
v_2(3^q n+A_w) < |w|
```

beyond a source-dependent finite threshold. `T-6709` and `T-6603` describe the dynamics after such a source exists; they do not exclude the source.

### Lane B — delayed first crossing

One must supply at least one of:

```text
- cofinal smaller-preimage coverage, including the open endpoint classes 1 and 7 mod 9,
  together with an actual contradiction rather than another lower gate;

- an ordinary-cylinder theorem placing every late canonical source beyond its exact
  no-descent threshold;

- a source-dependent stability theorem showing that an ordinary first-crossing word
  cannot retain the mechanical extremizer's remainder.
```

`R-6601` correctly proves that the fixed floor plus the unconstrained mechanical maximum cannot be iterated cofinally by itself.

These missing statements are precise and worth attacking. They are also still of the same global difficulty class as the unresolved coefficient-stopping/paradoxical-sequence problem. I therefore do **not** recommend advertising the reviewed stack as a serious resolution path yet.

---

# Final integration recommendation

```text
PR #76: VERIFIED WITH FIXES
PR #77: VERIFIED WITH FIXES
PR #79: VERIFIED WITH FIXES and STACK-INTEGRATION BLOCKED
```

After the enumerated repairs and the stack rebase, the claims may be integrated at their existing theorem statuses. Earlier independently passing claims remain verified; the new `O-7401` connection remains separately `PROPOSED` pending review. No PR should be merged by this reviewer, and no public README change is recommended in this pass.
