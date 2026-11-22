# A complete bounded-gap certificate language cannot be both sound and cofinally context-free

## Result and its role

Let a letter denote one **fixed positive valuation gap** in the accelerated odd Collatz map

\[
U(q)=\frac{3q+1}{2^{v_2(3q+1)}}.
\]

Suppose \(L\) is a context-free language over a finite collection of such letters, and every word in \(L\) is a genuine complete positive odd orbit certificate ending at \(1\). Then the set of odd sources represented by \(L\) is finite.

More explicitly, if every letter is at most \(M\) and \(N\) is a context-free pumping threshold, every source represented by \(L\) is at most

\[
q\le 2^{MN}.
\]

If an initial even exponent is separately bounded by \(e\le E\), the powered source satisfies

\[
S=2^e q\le 2^{E+MN}.
\]

This excludes a sound context-free grammar of complete bounded-gap certificates as a way to cover the cofinal source records from checkpoint 11. Those records are in the low-gap domain, with gaps at most four and initial even exponent at most three. A proposed grammar with pumping threshold \(N\) would cover only sources \(S\le 2^{3+4N}\), whereas the record theorem supplies arbitrarily large records.

The exact existing interfaces are `CollatzSourceRecords.cofinal_records` and `CollatzSourceRecords.record_low_domain` in `research/lean-global-resolvent-20261121/overview/central/lean/Collatz/SourceRecords.lean`. The application combines those theorems with the new powered-source bound; that final combination is explained here rather than added as another import to the new module.

**This result does not prove target descent or Collatz.** It identifies a whole proposed architecture that cannot supply a cofinal collection of source certificates. Arithmetic guards or source-dependent target-return rules may remain useful. The universal target-progress obligation in the joint-minimal-counterexample construction remains open.

## Certificate conventions

For a gap word \(W=[a_1,\ldots,a_r]\), write \(A(W)=\sum_i a_i\) and define its correction recursively by

\[
C([])=0,\qquad C(a::V)=3^{|V|}+2^aC(V).
\]

The repository's `CollatzWitness.Certificate q W` asserts positive gaps and

\[
3^{|W|}q+C(W)=2^{A(W)}.
\]

The existing certificate machinery proves that this identity supplies an actual positive odd orbit to one. A prefix certificate from \(n\) to \(y\) has the corresponding identity

\[
3^{|W|}n+C(W)=2^{A(W)}y.
\]

The existing `split_certificate` theorem cuts any complete certificate at an arbitrary word boundary and produces the integer endpoint and the complete tail certificate. Thus the argument below never assumes that arbitrary affine words have integer intermediate values: every split comes from a complete certificate already hypothesized to be sound.

## The all-parameter rigidity argument

### 1. Equal words force strong endpoint congruences

Suppose the same prefix word \(W\) carries actual integer sources \(n,m\) to endpoints \(y,z\). Subtracting their two identities gives

\[
2^{A(W)}(y-z)=3^{|W|}(n-m).
\]

Since powers of two and three are coprime,

\[
3^{|W|}\mid y-z.
\]

There is no assumption about the sign of \(y-z\), the size of the source, a contracting coefficient, or a fixed-point denominator. Lean states the divisibility for the absolute value of the integer difference.

### 2. Arbitrary inverse repetition fixes the boundary

Fix words \(V,T\), with \(V\ne []\), and suppose that for every \(k\ge0\), the word \(V^kT\) is a complete certificate for some positive odd source. Let \(x\) be the unique source of \(VT\), and let \(y\) be the unique source of \(T\).

For any \(k\), split the complete certificate for \(V^{k+1}T\) after its first \(V^k\). The remaining tail is \(VT\), so uniqueness of the source determined by that tail makes the split endpoint \(x\). Independently, the certificate for \(V^kT\) has the same prefix \(V^k\) and endpoint \(y\).

The preceding congruence therefore gives

\[
3^{k|V|}\mid x-y\quad\text{for every }k.
\]

An integer divisible by arbitrarily large powers of three is zero, so \(x=y\). The actual prefix \(V\) is therefore a loop at the source of the fixed tail. All powers \(V^k\) can be erased immediately before \(T\), even inside a longer actual complete certificate, without changing its source.

If \(V=[]\), erasure is immediate. This covers the possibility that either individual pumped block below is empty.

The proof does not need a classification of positive cycles. Since the loop in this particular argument also has a known completion to one, one can additionally conclude that its boundary is one and its gaps are all two. That observation explains harmless terminal padding; it is not an extra hypothesis of the Lean proof and is not used in the quantitative bound.

### 3. Two-sided CFL pumping preserves the numerical source

Suppose every word in the all-parameter family

\[
u\,v^k\,w\,x^k\,y\qquad(k\ge0)
\]

is a complete certificate, possibly for a different source for each \(k\).

First split off the fixed right-hand tail. The suffixes \(x^ky\) are all complete certificates, so the preceding rigidity argument erases \(x^k\) from every family member while preserving the original source. This leaves complete certificates

\[
u\,v^k\,w\,y.
\]

Now the suffixes \(v^kwy\) are all complete certificates. Apply the same argument a second time to erase \(v^k\). Every original family member has the same numerical source as \(uwy\).

The order matters: the right pumped block has a fixed terminal suffix before the first application. After its removal, the left block also has a fixed terminal suffix. No independence of the two pumping parameters is assumed.

### 4. A shortest representative cannot be pumpable

Fix any numerical source represented by \(L\), and choose a shortest word of \(L\) representing it. If its length is at least the context-free pumping threshold \(N\), the standard pumping lemma gives a factorization \(uvwxy\) with \(|v|+|x|>0\) and every \(uv^kwx^ky\in L\).

Soundness supplies a complete certificate for every parameter. Step 3 says that pumping down to \(k=0\) preserves the source. The resulting word is still in \(L\) and is strictly shorter, a contradiction.

Thus every source has a representative of length less than \(N\). Over a fixed finite alphabet there are only finitely many such words. Quantitatively, its total gap is at most \(MN\), and its certificate identity implies \(q\le 2^{A(W)}\le 2^{MN}\).

Lean uses strong induction on word length in place of choosing a shortest word. It proves exactly the source-preserving shortening statement needed in this argument.

## Scope: the alphabet and the absence of semantic filters matter

The theorem applies to a finite alphabet whose letters are fixed positive valuation gaps. It permits arbitrary context-free nesting and both standard pumped pieces. It therefore goes beyond a fixed dictionary of independently repeated blocks. Regular languages are included as a special case.

It does **not** apply to unrestricted shortcut-parity words. For example, for \(k\ge1\), the regular parity language

\[
1\,0^{2k-1}
\]

describes the shortcut orbits from

\[
q_k=\frac{2^{2k}-1}{3}
\]

to one. Each source has a single odd-step valuation gap \(2k\), so these cofinal odd sources use unbounded gap values. Pumping zeros here changes one valuation letter, rather than repeating a fixed word over a bounded valuation alphabet. There is no contradiction with the theorem.

Likewise, an unbounded initial even exponent already gives the regular cofinal family of sources \(2^e\). That exponent must be bounded before one can infer bounded powered sources from bounded odd sources. The low-domain record application has the needed bound \(e\le3\).

Finally, a grammar that generates candidate words and then applies an unbounded arithmetic integrality filter is not a sound context-free language in the theorem's sense. Nor does the theorem exclude finite context-sensitive rewrite systems, source-dependent guarded programs, or a rule with an unbounded arithmetic state. It does not put a bound on every possible proof language.

## Formalization boundary and exact dependencies

`lean/Collatz/CertificateLanguage.lean` kernel-checks seven public theorems:

1. `endpoint_congruence`;
2. `unbounded_repetition_fixed`;
3. `pumping_erasure`;
4. `short_representative`;
5. `source_bound`;
6. `powered_source_bound`;
7. `not_cofinal_sources`.

The language theorems take the explicit predicate `PumpsAt L N`, which states the usual five-piece all-parameter pumping conclusion, together with soundness and the numerical letter bound. It omits the standard additional upper bound on the length of the middle three pieces, because the proof does not need that bound.

The bridge from “context-free” to `PumpsAt` is the classical context-free pumping lemma. It is a written application, **not a newly kernel-checked theorem about Mathlib's `Language.IsContextFree`**. The pinned Mathlib context-free grammar module does not supply a pumping theorem. No external pumping-lemma package was imported into this replay.

The module imports only `Collatz.LowGapLoops` and uses the existing Lean-core certificate closure. There are no new mathematical axioms, no admitted proofs, and no native-decision proof step. `lean/AuditCertificateLanguage.lean` audits the seven public theorem dependencies. The parent checkpoint's focused replay should compile the exact source closure and the new module; the local development replay reused the already compiled checkpoint 11 closure.

## Relation to the attempted central attack

The initial aim was a word-changing return for the universal target-progress clause, using the fresh joint minimum from PR 177 and the direct closure work in PR 180. The fresh extremal-clock counterexample in PR 185 rules out substituting the whole interval source-clock deadline for that clause. The present argument does not restore that deadline or prove the still open residual target return.

The arithmetic proposals were evaluated at their missing hypotheses. The correction \(C(W)\) has a number of summands growing with \(|W|\); a bounded gap alphabet does not by itself put it into a fixed-dimensional S-unit equation or a fixed collection of linear forms. No valid Subspace Theorem estimate with the required all-place saving was obtained. The actual use of a bounded alphabet here is narrower and rigorous: after source-preserving pumping, it bounds the number and size of short representatives.

Earlier checkpoint 9 and PR 183 already use affine-displacement divisibility to control fixed block descriptions. The endpoint congruence above is a dual elementary use of that mechanism, with terminal rather than initial data fixed. The contribution here is the sound context-free-language consequence, including coupled two-sided pumping; no claim of literature priority is made.

## Primary references

- Alfred V. Aho, [Pumping Lemma for Context-Free Languages, Columbia lecture notes](https://www.cs.columbia.edu/~aho/cs3261/Lectures/L10-PL_for_CFLs.html). This is the exact five-piece all-parameter pumping statement used for the written CFL corollary, with its parse-tree proof.
- Y. Bar-Hillel, M. Perles, and E. Shamir, [On formal properties of simple phrase structure grammars](https://cris.huji.ac.il/en/publications/on-formal-properties-of-simple-phrase-structure-grammars/), 1961, institutional publication record. This is bibliographic context for the classical pumping theorem; the full original article was not replayed here.
- [Linglib's formal context-free pumping theorem documentation](https://linglib.io/docs/Linglib/Core/Computability/ContextFreeGrammar/Pumping.html) provides a separate formal implementation of a CFL pumping bridge. It was inspected as an available formalization lead, but it is not a dependency of this checkpoint and has not been locally replayed here.
