# Atomic finite-certificate and collision problems

## 2. Direct finite certificates

### ACL-P001 — Positive accelerated-cycle certificate

**Statement.** Find integers \(k\ge1\), \(a_0,\dots,a_{k-1}\ge1\), put
\(A_j=\sum_{i<j}a_i\) and \(A=A_k\), and prove that

\[
n_0=
\frac{\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}}
     {2^A-3^k}
\]

is a positive odd integer such that, recursively,

\[
n_{j+1}=\frac{3n_j+1}{2^{a_j}}
\]

is a positive odd integer, \(\nu_2(3n_j+1)=a_j\) exactly, and \(n_k=n_0\). Require that the cycle is not the trivial \(1\leftrightarrow2\) cycle.

**Full-conjecture implication.** The displayed finite certificate is a nontrivial positive Collatz cycle, hence a disproof.

**Existing inputs.** `L-9905`, the exact affine monoid from issue #9, and the proposed exponent-shape filters `L-9910`/`L-9912`.

**Completion certificate.** A tiny verifier taking only \((a_0,\dots,a_{k-1})\) and reconstructing every integer.

---

### ACL-P002 — The \(m=8,\ K=13\) cycle packet

**Statement.** Exhaust the 792 ordered compositions of \(13\) into eight positive parts under the exact cycle equation and valuation replay. Either output an `ACL-P001` certificate or a proof-producing modular/divisibility certificate excluding every composition.

**Full-conjecture implication.** A positive hit disproves Collatz. A complete negative packet settles the smallest currently stated open odd-term case under proposed `L-9912`.

**Atomicity.** This is a finite, fixed input set with no asymptotic assumption.

**Warning.** The local-minimum parameter in external cycle bounds is not the accelerated odd-step count; record both.

---

### ACL-P003 — Regular sanctuary certificate

**Statement.** Exhibit a deterministic finite automaton \(A\) recognizing canonical least-significant-digit-first binary words \(L_A\) such that:

1. \(L_A\neq\varnothing\);
2. the words for \(1\) and \(2\) are not accepted;
3. every accepted word decodes to a positive integer;
4. for every accepted canonical word \(w\), the canonical word for \(T(\operatorname{val}(w))\) is accepted.

**Full-conjecture implication.** Any \(n\in L_A\) stays forever in a positive invariant set avoiding the trivial cycle, so Collatz is false.

**Existing inputs.** PR #12's exact transducers, product-graph inclusion checker, and certificate format.

**Completion certificate.** DFA transition table plus independently checked product-graph witnesses.

---

## 3. Corrected collision architecture atoms

PR #33 now proposes `T-9705`: no signed ordinary completion exists for the entire frozen corrected 256-transition class. The statement below therefore treats that class as **proposed closed**. A new positive program must escape the theorem's hypotheses rather than choose another word inside the same class.

### ACL-P010 — Evertse-escape collision architecture

**Statement.** Define an exact family of physically replayable supercritical Collatz stages \(\mathcal A_m\) and prove that an infinite ordinary path through them would **not** produce the fixed-dimension nondegenerate admissible projective zero sums used by PR #33 `T-9705`. Identify and prove failure of at least one closing hypothesis:

1. eventual cap/co-cap quotient dichotomy;
2. fixed coordinate count;
3. fixed finite internal prime set \(S\);
4. uniform proper-subsum nonvanishing;
5. outside-\(S\) height exponent \(d<1\);
6. pairwise projective distinctness;
7. connector-free physical-coordinate reduction.

Then construct one positive ordinary infinite path through \(\mathcal A_m\).

**Full-conjecture implication.** The constructed physical path is a Collatz counterexample.

**Acceptance rule.** Merely asserting that Evertse does not apply is insufficient; the stage family, exact replay, escaping hypothesis, and ordinary path must all be proved.

---

### ACL-P011 — Growing-rank corrected-stage escape

**Statement.** Construct corrected stages whose exact physical equation has \(N_m\to\infty\) essential internal coordinates, while retaining:

1. exact finite compiler and overlap;
2. net supercritical growth;
3. an ordinary initialization;
4. an all-scale recurrence selecting one path.

Prove that no bounded-rank regrouping recovers the PR #33 fixed-258-coordinate admissible equation.

**Implication.** Provides one concrete realization of `ACL-P010`.

**Risk.** Raw stage width is not enough if the equation compresses to bounded essential rank.

---

### ACL-P012 — Quantitative outside-prime-mass escape

**Statement.** Construct a physical stage family and positive path for which, for every fixed finite \(S\), the outside-\(S\) content of the primitive endpoint coordinates has logarithmic exponent at least the finiteness threshold needed to defeat the \(d<1\) hypothesis, while the path remains in an expanding low-digit chart.

**Implication.** Removes the height gate in the PR #33 Evertse closure; combine with an ordinary path construction.

**Not sufficient.** Qualitatively infinitely many fresh primes. PR #33 already allows fresh endpoint primes and still closes the class because their total outside-\(S\) height is too small.

---

### ACL-P013 — Controlled degenerate-subsums escape

**Statement.** Build a physically meaningful stage architecture in which every primitive stage equation has a specified proper vanishing subsum that:

1. persists at every scale;
2. is not a removable common factor or a decomposition into subcritical independent stages;
3. transfers growth or quotient information between the remaining coordinates;
4. permits one ordinary positive infinite path.

**Implication.** Escapes the nondegenerate \(S\)-unit finiteness input and supplies a counterexample if the path is constructed.

**Why hard.** In the frozen architecture, the one-positive/rest-negative sign pattern rules out proper vanishing subsums automatically.

---

### ACL-P014 — Signed-quotient refund channel

**Statement.** Construct an exact corrected stage family for which a signed ordinary trajectory can retain an unbounded or recurrent quotient \(Y_m\notin\{0,-1\}\) despite paying the next stage radix, and prove that the quotient channel supplies enough information to maintain overlap and positive growth forever.

**Implication.** Escapes the cap/co-cap reduction at the first step of `T-9705`; with a positive initialization, yields a counterexample.

**Required feature.** The refund must be physical and exact, not a formal real or \(2\)-adic high tail.

---

### ACL-P015 — Positive marked initialization for an escape architecture

**Statement.** Given an architecture satisfying one of `ACL-P011`–`ACL-P014`, exhibit one finite positive integer \(n_0\) whose physical shortcut-Collatz orbit enters the first marked state, replays every stage, stays positive, and never reaches \(1\).

**Full-conjecture implication.** Completes the escape construction.

**Why separate.** A stage recurrence or projective equation is not automatically an ordinary marked orbit.

---

### ACL-N016 — Maximal fixed-width almost-\(S\)-unit exclusion

**Statement.** Generalize the PR #33 closing argument to a theorem with explicit hypotheses on a family of corrected affine stages. The theorem should allow arbitrary bounded stage width, finitely many internal prime alphabets, signed cap/co-cap tails, and endpoint outside-\(S\) height exponent \(d<1\), and conclude that no signed ordinary infinite completion exists.

**Implication.** Identifies the exact boundary any future collision architecture must cross and prevents relabeling the same excluded mechanism.

**Deliverable.** A source-qualified statement with all constants, primitive normalization, nondegeneracy, and distinctness conditions visible.

---

### ACL-N017 — H/collision almost-\(S\)-unit transfer theorem

**Statement.** Determine whether the partial H renewal equations can be converted, in every remaining subcritical case, into infinitely many distinct nondegenerate admissible projective zero sums satisfying an Evertse-type \(d<1\) height gate.

**Implication.** A positive theorem would close the H route by the same template that PR #33 proposes for the frozen collision class. A precise obstruction would identify the arithmetic feature H retains that the collision class lacks.

---

### ACL-N018 — Room/seam theorem relevance audit

**Statement.** Prove one of the following:

1. the all-room/all-seam constraints are logical inputs to a corrected-stage class not covered by `T-9705`; or
2. every room/seam survivor in the frozen class is already excluded solely by `T-9705`, making further seam search irrelevant to counterexample construction.

**Implication.** Prevents effort from continuing on a branch that has no remaining edge to the full conjecture.

**Scope.** This is dependency analysis, not proof verification of `T-9705`.
