# Checkpoint 1: independent reconstruction and exact scope

**Collatz remains unresolved.** The coordinator reconstructed the two new written arguments at agent commits `c853dee7b9a6d5cb3fa2466ecc51367c9be00520` (arithmetic) and `114ce547ebb2bc8c62a22b77ecf1325810bdfba4` (dynamics). The proofs remain proposed research deductions with explicit external inputs. This review is an independent argument check within the same project, not external peer review.

## 1. Complete native branch spectrum

For every prescribed grade sequence p_k/k tending to a, the branch exponent is min(h_2(a),a log_2 3). The matching upper bound was already in Fourier Wren's paper 64, section 10.5. The new lower proof uses Leen's entropy-dimension theorem, truncates the random native total to its concentration window, chooses one total carrying exponentially many distinct residues, and appends a common word to reach the originally prescribed clock and grade. For interior a and a fixed positive slack epsilon, both the added grade and the added even count are eventually nonnegative. Complete ternary residue separation survives the suffix. Letting epsilon decrease proves the lower exponent; the endpoints use the elementary capacity upper bound and nonemptiness.

The coordinator checked the reversed-gap orientation, canonical endpoint interval, padding inequality, endpoint cases, uniformity by subsequence compactness, and the maximum at the entropy intersection. For an aligned positive block, different grades have disjoint endpoint intervals, so the same total exponent is a true unmarked endpoint count. The spatial zero-entropy consequence is inherited from the old upper bound; it is not presented as a new result. Residual-function separation and directed witnesses use the separately identified papers 212 and 225. The same spectrum for the minus-sign map prevents a sign-blind complexity contradiction from resolving positive Collatz dynamics.

Primary sources inspected here: Wren paper 64 v2 section 10.5; papers 212 and 225 version 1; and Leen's original version-specific TeX, SHA-256 `3855fc67c0c30c0e8e78af3de93fd85279d4376f2cb7c1e5d63d24433ce70afc`, definition of the tilted law and Theorem C. The theorem supplies the entropy formula for every parameter in (0,1). Its analytic proof was not independently reconstructed or formalized in this pass.

## 2. Strong approximate component colours still have real defects

The coordinator checked the nested-frequency construction, the exactly half-mean interpolation, the original-source sampling estimate, freezing after removal of powers of two, and the simultaneous path argument. The interpolation gate occupies the same relative part of every fine cell, preserving half-density throughout a frequency transition. The frequencies approximate every fixed rational dilation while remaining subpolynomial in the ordinary source scale. The true affine correction accumulates negligibly while all odd parts remain above the specified height floor. A single bad set of original phases controls all permitted dates; the proof does not add a per-date statistical error or assume an endpoint distribution.

Inselmann's primary Theorem 1.1 profile was checked. Pure halving stretches would contradict that uniform profile, so odd parts as well as raw heights remain large through every strictly precritical fraction. The eventual-defect conclusion separately uses the imported natural-density minimum-tightness input. The new colouring is exactly doubling-invariant and only approximately odd-edge invariant. It has actual late colour changes on a positive proportion of starts; no nontrivial exactly invariant positive component is constructed. McNamara's moving-character method and the earlier visit-to-five observable are explicitly credited.

## 3. Verification actually performed

The coordinator's runner rebuilt both modules into a new temporary object directory with Lean 4.34.1, `warningAsError=true` and `autoImplicit=false`. A separate import audit covered five public roots, including the one-step phase inequality, and reported only `propext`, `Classical.choice` and `Quot.sound`. Pinned cached third-party objects were reused. This is not a cold Mathlib rebuild or independent kernel implementation. The [Lean receipt](CHECKPOINT_01_LEAN.json) records source hashes and actual output.

The finite branch checker ran again under ordinary and optimized Python. Both outputs were byte-identical and matched the committed fixture. The [finite receipt](CHECKPOINT_01_FINITE.json) records the source and output hashes. These finite checks do not verify the asymptotic entropy input. Repository validation is recorded separately from mathematics.

The first runner invocation stopped before compilation because the supplied Mathlib source directory had no build artifacts. The corrected invocation explicitly uses the existing matching compiled cache. No unsuccessful build was counted as a verification.

## 4. Next work

The arithmetic lane has resumed a whole-cycle attack. The dynamics lane has moved from the counterexample to exact small-height information and component transport. The outside lane is developing an ordinary arithmetic obstruction using all smooth factors and many convergent centers. The coordinator continues the critical inverse-control investigation. The pass remains active through its requested endpoint, 18:08:39 UTC.

