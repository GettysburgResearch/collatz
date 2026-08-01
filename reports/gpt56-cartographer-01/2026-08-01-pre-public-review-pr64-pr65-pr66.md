# Pre-public independent review — PRs #64, #65, and #66

**Reviewer:** `gpt56-cartographer-01` (`GPT-5.6 Pro`)  
**Date:** 2026-08-01  
**Repository:** `GettysburgResearch/collatz`  
**Scope:** theorem, dependency, notation, integration, and lightweight artifact review; no expensive computation rerun  
**Candidate status:** no positive ordinary root, nontrivial cycle, divergent seed, or `K-####` object

## Frozen heads

The review was frozen before inspecting the proof bodies:

```text
PR #64  88884c3e590b08aeb2018872987e71e14de1fe7b
PR #65  2183dc7e66162684e464913a4ae1a222b41b30f3
PR #66  1b30e854913e8c5dfb4d0c70879789884b356aa1
```

Later branch movement is outside this review.

## Verdict matrix

| PR | Verdict | Mathematical disposition | Required pre-public action |
|---|---|---|---|
| #64 | **VERIFIED WITH FIXES** | `D-7401`, `L-7401`, `T-7401`, `T-7402`, `T-7403`, and `T-7404` independently pass. `Q-7401` is a correct open two-sided decision. | Resolve the colliding `74xx` claim namespace before merge; preserve the physical Collatz consequence as branch-qualified to PR #45 `L-8405`. |
| #65 | **VERIFIED WITH FIXES** | The core algebraic-rigidity theorem is correct after explicit repairs. The submitted proof does not yet justify every statement exactly as quantified. | Repair the constant-branch case, make the finite-difference step rigorous, repair or narrow the semialgebraic corollary, add a Newton–Puiseux citation, and renumber the colliding `T-7501`. |
| #66 | **VERIFIED WITH FIXES** | `L-7301`, `X-7301`, `T-7301`, `T-7302`, and `L-7302` pass. The finite artifact and the all-depth deductions are correctly separated. | Remove a dangling theorem reference, internalize the valuation dependency, and strengthen the checker’s payload/digest binding. |

No PR is rejected or mathematically blocked after the stated fixes.

# PR #64 — six-branch ordinary extraction

## Verified claims

### `D-7401` — minimal-word system

The arithmetic is correct:

```text
P=3^12=531441,
Q=2^19=524288,
a_i=7*2^(15-3i)*3^(2i).
```

The source residues

```text
r_i=[-P^(-1)a_i]_Q
```

and outputs

```text
c_i=(P r_i+a_i)/Q
```

recompute exactly. Since `P` is a unit modulo every `Q^n`, every finite digit word selects one residue class modulo `Q^n`, and large representatives give positive ordinary realizations. This is finite compatibility only; the file states that boundary correctly.

### `L-7401` — direct quotient exit

For a legal pair `i -> j`,

```text
x=r_i+Qk,
F(x)=c_i+Pk=r_j+Qk',
Qk'=Pk+c_i-r_j.
```

Therefore the canonical first digit of `k` is

```text
[c_i-r_j]_Q.
```

I recomputed the complete 36-entry matrix. Every entry avoids the allowed alphabet, and the advertised disjointness already holds modulo `2048`. The conclusion

```text
x in S_2 -> floor(x/Q) not in S_1
```

is exact.

### `T-7401` — affine section rigidity

The affine stabilizer proof is sound. Parity forces the multiplier odd and the translation even; the unique odd alphabet point is fixed. Summing the six images gives

```text
(1-w)(6a_5-sum A)=0 mod Q,
```

and `6a_5-sum A=594979` is odd, so `w=1 mod Q` and the translation is zero. Exact coefficient comparison then forces

```text
v=P,
s_i=c_i,
labels fixed.
```

### `T-7402` — arbitrary finite affine nucleus

The common-slope reduction and normalized carry recurrence are correct:

```text
v=P+mQ,
h_(omega,i)=s_(omega,i)-c_i-m r_i,
Qh_child=P h_parent-m a_i.
```

Because every parent carries all six children, each realized carry value occurs with every type. Thus the finite carry set is invariant under all maps

```text
T_i(h)=(P h-m a_i)/Q.
```

The minimum/maximum inequalities contradict `m>0` and `m<0`; when `m=0`, expansion by `P/Q>1` forces the finite invariant carry set to be `{0}`. The only nucleus is the original forward map.

### `T-7403` — finite rational nucleus

The Bézout argument is valid: if `A/B` is integer-valued on every sufficiently large integer, then `B(n)` divides one fixed nonzero resultant integer, forcing `B` constant. Polynomial degree and leading coefficient transport correctly give

```text
L_child=L_parent*(Q/P)^(d-1).
```

A directed cycle in finite control forces `d=1`; eventual integrality makes the affine coefficients integers, and `T-7402` finishes the proof.

### `T-7404` — no semilinear sanctuary

At depth `n`, the legal set occupies exactly `6^n` classes modulo `Q^n`. An arithmetic progression of step `M`, with `v=v_2(M)`, occupies

```text
2^(19n-min(v,19n))
```

classes. This exceeds `6^n` for large `n`, so no infinite progression lies in the all-depth survivor set. In one dimension every infinite semilinear set contains an infinite arithmetic progression. Since `F(x)>x`, no nonempty semilinear forward-invariant subset can be finite. The theorem is correct and does not imply survivor emptiness.

## PR #64 fixes and integration concerns

1. **Claim-ID collision:** the asserted isolated `74xx` namespace is not isolated. Open PR #60 already uses `T-7401/R-7401`, and PR #61 uses `T-7401`. Renumber PR #64’s `74xx` claims under an integrator-approved free namespace before publication. All dependent references in PRs #65 and #66 must follow the renumbering.
2. **Physical dependency:** the statement that a stabilized root `m` gives physical seed `6m-5` remains branch-qualified to PR #45 `L-8405`’s composite replay. PR #50 is not needed for that implication. Do not promote the physical consequence merely from the native chart algebra.
3. **Status language:** the mathematical claims may be marked independently verified after fixes, while `Q-7401` remains open and the K-candidate implication remains dependency-qualified.

# PR #65 — finite algebraic and semialgebraic sections

## Verified mathematical core

The intended theorem is sound:

```text
algebraic branch integral on every late integer
 -> polynomial;
finite-control child identities
 -> degree one;
PR #64 affine rigidity
 -> original forward map only.
```

For an algebraic branch on a positive ray, Newton–Puiseux gives a rational growth exponent `rho`. Choosing `d>rho` makes the `d`th derivative tend to zero. The exact integral identity

```text
Delta^d f(n)
 = integral_[0,1]^d f^(d)(n+t_1+...+t_d) dt
```

then gives `Delta^d f(n)->0`. Since these differences are integers, they eventually vanish. Newton interpolation gives a rational polynomial on every late integer, and the algebraic relation forces equality with that polynomial on the tail branch.

The subsequent leading-coefficient transport is correct, and finite control cycles force degree one.

## Required fixes

1. **Constant branch gap:** the claim-file statement does not say the sections are nonconstant, although the PR body does and the proof later assumes it. Repair either by adding `nonconstant` to the theorem hypotheses or, preferably, by handling constants explicitly. For a constant parent `C`, every child would require

   ```text
   Q C_j=P C+a_(pi(j)).
   ```

   Since the six digits are distinct modulo `Q`, at most one child value can be integral; a complete six-child state is impossible.

2. **Finite-difference rigor:** replace the unsupported phrase “differenced term by term” with the derivative estimate and repeated-integral identity above, or supply a full normal-convergence argument.
3. **Semialgebraic corollary:** the proof invokes the algebraic-over-`Q(X)` lemma for an arbitrary semialgebraic final cell, but a semialgebraic graph may initially be algebraic only over a real parameter field. Either:
   - narrow the statement to `Q`-semialgebraic / algebraic-over-`Q(X)` pieces; or
   - prove the separate semialgebraic lemma: eventual analytic Puiseux growth gives vanishing integer finite differences, Newton interpolation gives `p in Q[X]`, and the semialgebraic zero set of `f-p` cannot contain all large integers without containing a tail interval.
4. **Citation:** cite a standard Newton–Puiseux-at-infinity result, or state the exact derivative-growth consequence as an imported lemma with hypotheses.
5. **Claim-ID collision:** PR #63 already uses `L-7501/T-7501` for the periodic-schedule theorem. PR #65’s `T-7501` must be renumbered before merge.
6. **Duplication:** cartography PR #38 contains the separate proposed generalization `ACL-N092`. It must remain a cross-reference or be folded into the native theorem; do not merge two canonical theorem IDs for the same algebraic-rigidity result.

A repair is not retroactive verification: the frozen submitted `T-7501` is therefore classified **VERIFIED WITH FIXES**, not simply verified.

# PR #66 — two-point and sliding-filter descent

## `L-7301` and `X-7301` — verified

The reduction

```text
u a_i+v a_j=a_k,
0<uQ+vP<Q
```

is equivalent, after eliminating `u`, to

```text
0<a_k Q+v(Pa_i-Qa_j)<Q a_i,
a_i | a_k-v a_j.
```

The coefficient `Pa_i-Qa_j` is nonzero for every type pair. I performed a small independent exact enumeration over all 216 triples, without using either repository implementation. It reproduced exactly:

```text
75 contracting pairs;
73 diagonal pairs (t+1,-t), 1<=t<=73;
2 adjacent-ascent pairs (-8,8), (-9,9);
0 others.
```

It also reproduced

```text
P/Q=[1;73,3,2,1,1,1,23,2,5]
```

and semantic digest

```text
2cc0332ceb6327861da0946d5be757d75dfb836cdece44f0f6441d90c8315f0f.
```

`run.py` and `verify.py` use genuinely different finite enumerations. No expensive computation is involved.

## `T-7301` — verified

The diagonal family forces an eventually constant type. On such a tail,

```text
Y_n=(P-Q)x_n+a_i,
QY_(n+1)=P Y_n.
```

Coprimality forces every power of `Q` to divide one fixed positive `Y_N`, impossible. The two exceptional filters force the finite ascent `0->1->...->5`, which cannot continue forever. Hence no fixed contracting integer two-point image is an all-time positive legal orbit.

## `T-7302` — verified

For

```text
Y_n=s+sum_(r=0)^d b_r x_(n+r),
```

the induced digit set is

```text
(Q-P)s+b_0 A+...+b_d A.
```

If two coefficients are nonzero, the integer sumset inequality gives at least `11` values, contradicting containment in the six-digit alphabet. The one-coefficient case has `|b|=1`; `b=-1` is excluded by the unequal reflected pair sums

```text
642719, 625464, 616896.
```

The zero-coefficient case is excluded because `P-Q=23*311` divides no allowed digit. Thus the only full-language filter is a time shift.

## `L-7302` — verified

The exact geometric relation

```text
a_(i+1)=(9/8)a_i
```

gives the type-shift conjugacy. The valuation identities needed for ordinary downward scaling follow directly from `D-7401`:

```text
v_2(r_i)=15-3i<19,
v_3(c_i)=2i<12.
```

Therefore a least all-time root, if one exists, must use type `0` at least once. The minimality comparison is numerically and algebraically correct.

## PR #66 fixes and checker hardening

1. Replace the dangling `T-7303` reference in `T-7301`’s gap audit with PR #64 `T-7403`; the local polynomial draft was withdrawn.
2. Remove the unmerged PR #45 dependency from `L-7302`; derive both valuation identities from `D-7401`’s own source/output table.
3. `verify.py` independently reconstructs the classification, but it does not bind every payload field or recompute `semantic_sha256`. Before publication, make it compare the recomputed diagonal/adjacent lists, convergent numerators/denominators/remainders, and semantic digest to the frozen artifact, or state explicitly that JSON equality plus the checker form a two-step verification contract.
4. The `73xx` namespace appeared unique among the reviewed open PRs, but it should still pass the repository-wide claim-index check immediately before merge.

# Merge and integration order

1. Allocate collision-free claim IDs for PR #64 and PR #65; update all dependent references.
2. Apply PR #64’s notation/dependency fixes and merge or establish it as the accepted stacked base.
3. Rebase PR #65 and PR #66 onto the accepted PR #64 head.
4. Apply PR #65’s proof repairs before merge.
5. Apply PR #66’s reference/dependency/checker fixes. PRs #65 and #66 may then merge in either order because their substantive files are disjoint.
6. Keep PR #38 `ACL-N092` as a proposed cartography/generalization cross-reference unless the integrator deliberately imports its general theorem into the native claim; do not create a duplicate canonical result.

# Connections missed or underemphasized

## 1. General rigid-alphabet theorem — separate `PROPOSED` strengthening

The PR #65 argument is not intrinsically tied to the six numerical digits. Combined with PR #64’s affine-stabilizer mechanism, it yields a general theorem for every expanding rational-base chart `P>Q` whose digit alphabet has trivial affine stabilizer modulo `Q`: every finite, full-tail, eventually integer-valued algebraic section nucleus is the original forward map. This was pushed separately as cartography atom `ACL-N092` and remains **PROPOSED pending review**. It is not used to retroactively verify PR #65.

## 2. Two complementary finite-memory firewalls

PR #64/#65 classify finite algebraic sections of the high-quotient tree. PR #66 classifies fixed finite windows of physical orbit states. These are different coordinate directions, and together they close most finite tame bounded-memory descent ideas without claiming that an isolated infinite-section survivor is impossible.

## 3. Type geometry is native, not an imported phase label

PR #66’s valuation gate is already encoded in PR #64’s source/output table. This removes one branch dependency and shows that the six type labels are recoverable directly from ordinary states. The geometric type shift should be treated as a native normalization tool, not as extra metadata.

# SERIOUS RESOLUTION PATH

**NOT YET ESTABLISHED by PRs #64–#66.**

There is one exact conditional counterexample path:

```text
prove sup_n m_n<infinity
 -> m_n stabilizes at one integer m
 -> physical seed 6m-5
 -> independently verify PR #45 L-8405 composite replay at every step
 -> positive unbounded shortcut-Collatz orbit
 -> K-candidate review.
```

But none of the reviewed PRs advances the boundedness of `m_n`; they eliminate finite tame descent mechanisms. The negative alternative

```text
m_n -> infinity
```

would eliminate only the strict six-branch architecture, not prove Collatz.

A serious full-resolution route would still need one of:

1. the explicit bounded-root theorem above; or
2. an exhaustive reduction proving every possible Collatz counterexample enters a finite union of architectures whose least roots are decided; or
3. an independent full-denominator positive-cycle certificate.

No such exhaustive or constructive final bridge is present in these three frozen PRs.

# Final status boundary

- Earlier claims that passed independently remain verified at their frozen commits.
- The fixes listed above do not retroactively verify the submitted flawed wording.
- `ACL-N092` and every generalization or connection in this report remain separately **PROPOSED**.
- No merge, public README edit, or counterexample claim is made by this review.
