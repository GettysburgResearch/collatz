# Independent review: moving ordinary joint fibres

Date: 2026-11-22. Reviewer lane: potential / arithmetic Harnack.

## Frozen object and verdict

Reviewed the complete written draft:

`machinery22/entropy/MOVING_CESARO_FIBRES.md`

SHA-256:

`dd959aa34c35773d20642582d0aeb7c25d2d1eee65bc969b9a35a22304cd4be5`

**PASS as a mathematical deduction from the explicitly stated, frozen inputs.** I reconstructed the scalar and joint moving-root proofs, including the stopped inequality, the terminal ternary digit, all fixed endpoint clock shifts, the original-label extension, and the persistent original-source submeasure. I found no correction needed in this version.

This review is source-qualified in exactly the draft's sense. It does not independently establish the new external ordinary trace theorem or replay its analytic/formal dependencies; it checks its precise statement and proves that the displayed conclusions follow from it and the repository inputs. It is not a Lean verification or a proof that escape is absent.

## 1. External input and its normalization

I independently inspected the primary TeX at the exact pinned commit:

- Lucas Valbuena, *A positive semicontinuous density for the Syracuse stationary law* (2026-10-08).
- Repository `x1xhlol/collatz-two-coordinate-obstruction`, commit `a7275d5a73814d3d9a400c6fe6577de9542b03a3`.
- [Primary frozen source](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/positive-stationary-envelope.tex).

The source's Corollary `cor:integer`, equation `eq:cesaro-absolute`, states absolute Cesàro convergence at every positive ordinary integer. Its normalization is additive Haar probability on all of Z₃. The draft's renaming of `rho_j` as D_j and the arithmetic function `g` as h is consistent. In particular, its h is not the differently named normalized quantity G(n)/n from other notes.

The source does not merely give signed Cesàro convergence. Its claimed lower semicontinuous representative gives liminf D_j(a)≥h(a), and the displayed identity using min(D_j,h) converts the signed statement into the absolute one. The review imports that stronger ordinary-integer result; it does not replace it with an almost-everywhere trace statement or claim that signed convergence alone suffices.

I also read the frozen repository comparison in PR176 `31c4a880ea4acf6eec4783e68bfc75e2cf8e7fe6`, `ABEL_CANONICAL_COMPARISON.md`, and the contact-law argument in PR180 `a9f471543d7fed0a76f348e6d97a9d6d44fa369e`, `STOPPED_MIXING.md`. Their finiteness, positivity, and common-reference conclusions remain imported hypotheses in this receipt.

## 2. Harmonicity and full-path comparison

The domination D_j≤2V and PV≤V permits dominated convergence of the Cesàro means inside the parent sum. The shifted endpoint term is bounded by a fixed-root constant divided by the averaging length. This proves Ph=h without an uncontrolled exchange of an infinite sum and an unbounded sequence.

The ratio r=h/G lies in [α,2]. The finite-prefix likelihood ratio r(X_j)/r(a) is a bounded martingale under the G-law, hence uniformly integrable. Its limiting density gives the full h-path law and preserves the same bounds. Thus both comparisons in (7), and their application to the almost surely finite contact event, are valid. A finite-cylinder comparison alone would have needed this extension; the draft supplies it.

## 3. Centered clocks and the scalar moving theorem (14)

For a contact endpoint x, the exact remaining depth at deterministic time k+r is r−d_p(x). The proof retains the condition d_p(x)≤r. Its complement is exactly the event that contact has not yet occurred, because the eventual contact time is finite and τ−k=d_p(X_τ).

For a fixed endpoint, Q_R in (11) treats both signs of d_p(x) correctly. If d is negative, the sequence starts at the fixed shifted index −d. If d is nonnegative, at most d initial slots are omitted and paid for by the explicit bounded term. In either case Q_R≤B and tends to zero. The common ordinary reference is finite and dominates every moving contact law with the same constant M_p. Dominated convergence therefore controls the supremum over k.

Equation (15) follows from conditioning at τ only on τ≤k+r. Equivalently this is conditioning at the bounded stop τ∧(k+r), so no missing integrability hypothesis is needed. The conclusion (14) has absolute error inside the average, as claimed, because the imported fixed-root hypothesis has that stronger form.

## 4. Selection and exact terminal-digit formula

For a fixed root, the proof of (16) first conditions on a finite path prefix and uses ordinary fixed-integer Cesàro convergence at its random endpoint. The errors are uniformly bounded. Approximation of a bounded full-path function by its finite-prefix conditional expectations is consequently legitimate in L¹. A finite sup-norm net then gives the mean of the supremum for a compact family. This is enough for c_j in (24); the proof does not interchange a supremum with a limit without justification.

For (21), a prefix w of length t has independent-digit probability 2^(−S_t), while the density factor at depth t+1 is 3^(t+1). Their product is 3A_w. The remaining congruence is precisely Z′≡x_w mod3. This verifies the prefactor 3/h(a), the one remaining ternary digit, and the correct seed D₁ in the replacement expression.

A nonunit terminal endpoint has zero contribution because Z′ is a unit. An earlier nonunit cannot support a further congruent inverse digit. Every retained congruent prefix from a positive ordinary root has positive odd intermediate states. Thus the summation over actual unit prefixes matches the event decomposition.

The fractional moment bound (18) is the geometric sum obtained from subadditivity with ratio 3^β/(2^(1+β)−1)<1. The estimate in (22) uses A_w/a≤1/x_w and h(x_w)≥α separately on every prefix. Its error bound is therefore available before any later split at contact, not merely after summing over all prefixes.

## 5. Joint stopped inequality (26) and conclusion (23)

The three terms in (25) suffice:

1. The terminal-digit replacement error is bounded by C_β times the conditional remaining-depth expectation of X_s^(−β).
2. Affine composition gives (27) on each contact prefix. Its factor A_τ/q_k≤1/x is pointwise, so the normalized remaining real-offset error is bounded by b_s(x) even when the root moves.
3. The final path functional becomes φ(v)=f(u+(1−u)v), with u=B_τ/q_k in [0,1]. This function remains in the same bounded Lipschitz unit ball. Its selection error is bounded by c_s(x) uniformly over the entire contact prefix and the test function.

On the event of no contact yet, the three respective bounds are C_β, C_g, and B_g. Conditioning on the complete contact prefix and then integrating over its endpoint proves precisely (26), with s=r−d_p(x). Taking the supremum over tests is valid because all three bounds are independent of the test.

Actual inverse paths have distinct positive integer states, so X_j tends to infinity on each path. Hence a_j tends to zero. Monotone convergence of the real affine offsets gives the same conclusion for b_j. Compact-family selection gives Cesàro convergence for c_j. The same fixed-shift finite-reference argument from Section 3 therefore proves the mean of per-depth BL distances in (23), including its uniformity over moving roots.

## 6. Original labels and surviving original-source mass

The label/endpoint reference (29) is finite: its label factor is bounded by a constant times n^(−4)n^(5/2)=n^(−3/2). Its fixed shift is attached to the original pair (n,x). This makes (30) a dominated-convergence statement with the original weights intact. Collisions add their original labels; killing only removes nonnegative terms.

For (32), the actual inverse prefix from q_k to the same original p has probability a_k h(p)/h(q_k). Its real affine offset is b_k=q_k−a_kp. Continuing from p therefore maps t to 1−λ_k+λ_k t. Multiplication by h(q_k)/q_k leaves exactly λ_k h(p)/p. This proves the claimed nonnegative submeasure, including its normalization and retention of the original source.

Under the imported product bound, λ_k tends to a limit at least δ. Testing (32) against a nonnegative bounded continuous function proves (33). The full-path comparison pushed through the same real-limit map proves (34). Neither operation removes the surviving mass. The final statement that the new moving comparison does not imply vanishing escape amplitude is therefore mathematically essential and correct.

## Scope of this receipt

The frozen theorem establishes the stated source-qualified moving scalar and joint-fibre comparisons. No uniform rate, ordinary-fibre absolute continuity, sibling leakage lower bound, or Collatz convergence follows from this review. I performed no old Lean build and no numerical enumeration; the review is of the written deductions and exact source statements identified above.
