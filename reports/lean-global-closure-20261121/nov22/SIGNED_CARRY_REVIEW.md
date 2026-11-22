# Independent semantic review: signed carry and complete-word compiler

Review date: 2026-11-22. Reviewer: global_analytic22.

**Verdict: VERIFIED at the finite-arithmetic and explicitly guarded
complete-source transport level. The full stopping/interval-cover
assertion remains OPEN.** This review reconstructs the mathematics and
checks the theorem statements against their intended use. It is not a
new compiler execution or a global convergence proof.

## Frozen files reviewed

| File | SHA-256 |
|---|---|
| SignedCarry.lean | a1d335151f39635e0be98a1b34ddf7bf7bdd31f4186ac23f8a5d777f3db809ad |
| SIGNED_CARRY_CALCULUS.md | 6118298a6f97757f68457ece7bae717141a4371f3e722f92be43b2f70b3d64bd |
| SignedCarry.receipt.json | 4a46552c5025909617a9ef614e6ed196a9d8c8566b7fab16bb478ff071ab75cd |
| SignedCarry.log | 9ed41648b55bad6a36e78705f3894abb60def60eb295c4b1775e440f5eaee9ab |

The inspected files were in the agent22_certificate scratch directory.
The imported foundation was inspected in the PR175 checkout at
2bc2ad37b490a5aea63658eaf657bc048da4532e:

| Foundation | SHA-256 |
|---|---|
| CollatzGlobalClosure/EndpointSteering.lean | b4f87c7b9eb38cd015f31a9f7ae60b0eaef6aeba77d496c5d586090e2da65416 |
| vendor/pr177/Collatz/GapMultiset.lean | 45a76cf399891cf91afafa8cda81eabef68fd33a9fe0665c45be047cdd39afbf |
| vendor/pr177/Collatz/Witness.lean | 5bdf16ad454994bfe07d8371f7939d0b1bc2673363a00269f088cb5349d6f0cc |

The latter vendor packet retains its existing source pin to PR177
00a611094043afeb256d6532b477c0709e8ed270. This review does not upgrade
unread newer PR177 results.

## 1. Ordinary map versus the signed arithmetic scaffold

The ordinary target map is the existing nonabsorbed natural shortcut
map. The signed extension uses the same even/odd formulas. The separate
scaffold is \(S(z)=z/2\) or \((3z-1)/2\); the sign relation is
\(T(-z)=-S(z)\), not an identification of the two maps.

For \(2v-z\), parity agrees with \(z\). Direct substitution in each
parity case gives
\[
T(2v-z)+S(z)=3^{z\bmod2}v.
\]
Both divided numerators are even in their respective cases, so negative
integer division causes no rounding ambiguity. After the first step,
the remaining target is
\[
2^{k-1}\,3^{z\bmod2}v-S(z).
\]
Induction therefore gives the stated endpoint and odd-count identities.
The Nat-to-Int bridge uses the identical natural shortcut definition;
it does not interpret a negative source as an ordinary input.

The public finite_signed_lift theorem is correctly obtained by using
the zero-translation identity to relate the scaffold at \(-\mathrm{seed}\)
to the supplied signed orbit. It requires an actual natural source
satisfying the displayed affine equality. It asserts an exact finite
endpoint and total odd count, with no signed convergence assumption.
The proof's stepwise parity relation also explains why the prescribed
finite ray has the intended ordinary parity history.

## 2. One-gap transport and exact budget

With \(p>0\) and \(3r+1=2^a u\), the identity
\[
3^p r-c
=2^a3^{p-1}u-(3^{p-1}+c)
\]
is exact over integers. Substitution into the complement theorem yields
\[
p'=p-1+o_a^-(3^{p-1}+c),\qquad
c'=S^a(3^{p-1}+c).
\]
The same source gap clock \(a\) and the actual target odd count are used.
There is no independent parity-word choice or natural truncated
subtraction of the signed debt.

For the initial carry \(9r+2\), \((p,c)=(2,-2)\) makes the scaffold
start at one. Since \(S(1)=1\), the first transition is exactly
\((2,-2)\mapsto(a+1,1)\). Later debts stay nonnegative.
The theorem allows an algebraic gap zero, but genuine supplied complete
certificates have positive gaps, as required by the imported certificate
definition. This generality does not weaken a downstream physical guard.

## 3. Literal certificate preservation and positive targets

The complete certificate is the existing positive-gap full identity,
not merely a statement of basin membership. The composition proof
uses certificate_cons_iff to peel its actual first gap and returns
the literal requested suffix. At each induction stage the target is the
actual natural iterate orbit a n. No fresh certificate or new
unbounded history is selected.

Enabled requires strictly positive power before every consumed gap.
Although advance is syntactically defined at power zero, its arithmetic
transport is not applied there. The budget
\[
p_f+|\mathrm{front}|=p+o_{\sum\mathrm{front}}(n)
\]
follows by adding the exact one-gap budgets, with each consumed source
gap spending one exponent.

The initial compiler's target \(9r+2\) is positive. The positivity lemma
shows that its actual natural iterates stay positive, so the later
integer debt equation cannot introduce an artificial nonpositive target.

## 4. Common grade and the exact conditional query

The grade is precisely the existing multiset
grades 0 word, with twice each supplied odd gap. A nonempty removed
prefix has a strict decrease at its highest present grade. The unchanged
tail cancels under the existing Less relation. The proof does not switch
to source value, target value, exponent alone, or a different numerical
energy.

The interval rule explicitly assumes the lower-grade complete-source
induction hypothesis and the target upper bound \(3^{p_f}u-c_f\le2u+1\).
Its child target is positive by actual transport. If power is zero and
the debt is nonnegative, the stronger upper bound by \(u\) is correct.

The note correctly preserves a further scope condition: the initial
carry \(9r+2\) is outside the interval \(t\le2r+1\). A surrounding
dispatcher must pay for its relation to the genuine parent query.
The compiler does not generate that missing parent rank budget.

## 5. Exhaustion remains an unresolved alternative

The maximal-enabled-prefix theorem constructs a split of a finite
selected word. Its conclusion is power zero OR exhaustion of that
selected word. If a separately supplied tail remains, exhaustion does
not mean that the complete certificate has reached one. If the entire
complete certificate is consumed, the remaining target is \(3^{p_f}-c_f\)
at source one, with no general smallness conclusion.

The note's example is arithmetically correct:
17 has complete gaps [2,3,4], the carry transitions are
\[
(2,-2)\to(3,1)\to(4,10)\to(6,61),
\]
and the actual target 155 reaches \(3^6-61=668\) after nine
shortcut steps. This was reconstructed directly, not inferred from
a terminal-state search.

The two stationary terminal carry families represent actual targets one
and two. Gap-two padding preserves them with positive power. They
correctly refute exponent-only termination as a required compiler rule;
they do not refute convergence, since those two targets are already
convergent. General padding reproduces the actual target dynamics, so
declaring it successful would reinstall the unresolved theorem.

## 6. Evidence boundary and publication handoff

The supplied receipt records a development compilation of these exact
source bytes, with 31 public theorem audits and only the standard axioms
propext, Classical.choice, and Quot.sound. This reviewer read the receipt
and log; that is not an independent replay. The integrating root is
responsible for the fresh complete-packet build and published-checkout
validation.

No semantic correction is required for the reviewed files. The narrow
verified output is an exact arbitrary-word carry calculus, preserved
complete suffix, actual target odd budget, and guarded query with a
strict common-grade decrease. Neither a universal successful stopping
policy nor full Collatz convergence has been proved.
