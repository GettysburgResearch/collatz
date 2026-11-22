# Independent review: logarithmic sparse-return descent

**Verdict: the written theorem and proof pass mathematical review.** No
correction is required to the reviewed version. This review does not certify
Lean formalization or a proof of universal Collatz descent.

## Exact reviewed artifact

- File: `LOGARITHMIC_SPARSE_RETURN_DESCENT.md`, checkpoint 13 root draft.
- SHA-256: `16a1e35acb93001811674c67856cbaf3dd8ab5a86efcc0ccd8e9daa69976170e`.
- Reviewed all sections, including the stated quantifiers and evidence boundary.
- Reviewer: the separate source-sensitive renewal agent.

## Primary-source check

I independently downloaded Evertse's original article, *On sums of S-units and
linear recurrences*, Compositio Mathematica **53** (1984), 225–244, and visually
read Theorem 2, equations (13)–(14), on printed page 228, and the norm definition
(2) on printed page 226.

Source: <https://www.numdam.org/item/CM_1984__53_2_225_0.pdf>.

Theorem 2 applies to integral vectors with every nonempty subsum nonzero.
Its inequality is

\[
\left(\prod_j\prod_{v\in\mathcal S}|z_j|_v\right)
\prod_{v\in\mathcal T}\left|\sum_jz_j\right|_v
\ge c\left(\prod_{v\in\mathcal T}\max_j|z_j|_v\right)
\|z\|^{-\epsilon}.
\]

For the choices in the draft, each coordinate product is one and
\(\|z\|=\max_j|z_j|\). Hence the claimed lower bound with exponent
\(1-\epsilon\) follows exactly. Neither primitive coordinates nor pairwise
coprimality are hypotheses of this theorem. Signs are permitted. Minimizing
the constants over the finitely many arities through \(4S\) gives the asserted
uniformity.

## Application audit

1. The run-boundary expansion has distinct binary exponents within each
   endpoint group. Its largest selected power dominates all smaller selected
   powers, so no nonempty subset within one group vanishes.
2. Any vanishing subset of the combined endpoint terms contains an
   inclusion-minimal vanishing subset. This subset is nondegenerate, uses
   both groups, and has at most \(4S\) terms. A cross-group ratio has ternary
   valuation \(\pm h\). Thus it would put \(h\) in the fixed set \(H_S\),
   contradicting the hypothesis. No correction terms or growing dimension
   enter the deep theorem.
3. The full endpoint sum is the positive exact correction \(C_w\), so the
   whole-set condition is satisfied too. The largest initial endpoint term
   exceeds \(T=3^h n\). Since \(0<\epsilon<1\), Evertse gives
   \(C_w/T\ge cT^{-\epsilon}\). No upper bound on endpoint term sizes or on
   individual valuation gaps is needed.
4. The actual recurrence gives exactly
   \(C_w/T=\prod_{i<h}(1+1/(3x_i))-1\). Under the contrary assumption
   \(x_i\ge n^\eta\), its upper bound is eventually
   \(2C_0\log n/(3n^\eta)\).
5. With \(D=1+C_0\log3\), the horizon assumption implies \(T\le n^D\).
   Choosing \(\epsilon=\eta/(2D)\) yields the conflicting lower bound
   \(c n^{-\eta/2}\). The resulting threshold depends only on
   \(S,C_0,\eta\), and existence follows from power growth over logarithmic
   growth.

The descent is correctly stated for an input \(i<h\), not merely for the
terminal endpoint. The proof does not need orbit injectivity. The
exceptional set depends only on \(S\), not on the horizon or the power
exponent. The fixed-cutoff family consequence \(h/\log n\to\infty\) follows
by passing to a bounded-ratio subsequence if that limit fails.

## Scope

This is a valid new application of the cited theorem: a nonexceptional return
between endpoints of uniformly bounded run count on a logarithmic horizon
forces descent below a fixed power of the original source. Its threshold is
not claimed effective. The argument does not supply the requisite sparse
returns, a run cutoff growing with the source, exclusion of all cycles, or
universal convergence. Those limitations are stated accurately in the draft.

The primary PDF and page renders used for this independent check are temporary
review materials, not proposed repository artifacts.

## Final comparison update

I also reviewed the final draft at SHA-256
`086358d37609522226c5f585a07ecb2fff3e9e82e80c8289adfcf9bb7bd2725b`.
Its proof is unchanged; Section 5 now compares it with the sharpened
effective core. The revised comparison is correct:

\[
\log M_0(S,h)=16S^2\log2+(12S\log2+\log6)h.
\]

Writing \(a_S=12S\log2+\log6\), a fixed multiplier
\(C_0<\eta/a_S\) gives \(M_0(S,h)\le n^\eta\) whenever
\(h\le C_0\log n\) and

\[
\log n\ge\frac{16S^2\log2}{\eta-a_SC_0}.
\]

The effective core therefore already implies power descent on these
restricted logarithmic horizons. Evertse's theorem extends that conclusion
to every fixed positive multiplier, at an unspecified threshold. The final
draft states this distinction accurately. **Final verdict remains PASS.**
