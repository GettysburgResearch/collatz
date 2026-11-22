# Sources and inspection scope: independent power blocks

Inspected on 22 November 2026. Technical inputs below are primary sources.
No new Collatz proof announcement is used as a theorem.

## Mat00 — Matveev's explicit logarithmic-form bound

E. M. Matveev, **An explicit lower bound for a homogeneous rational linear
form in the logarithms of algebraic numbers. II**, *Izvestiya: Mathematics*
64:6 (2000), 1217–1269.

- DOI: <https://doi.org/10.1070/IM2000v064n06ABEH000314>
- Publisher/Math-Net record:
  <https://www.mathnet.ru/php/archive.phtml?jrnid=im&option_lang=eng&paperid=314&wshow=paper>
- Full English primary PDF:
  <https://www.mathnet.ru/links/11696330cc866d273c92c771a63da235/im314_eng.pdf>
- Inspected: §2, pp. 1219–1220, definitions (2.1), (2.2), (2.4), and
  **Corollary 2.3**, especially constant (2.6) and its permission to replace
  the coefficient parameter by `B*`.
- Used specialization: real field `Q`, two logarithms of 2 and 3, coefficients
  `N` and `-s`, `0<s<=N`, `A1=log 2`, `A2=log 3`, `B*=N`.
- The bound `C1(2)<=2^32`, together with `(log 2)(log 3)<2`, gives the
  deliberately loose constant `K=2^33`. Nonvanishing is supplied by the
  positive complete-cycle logarithmic identity.
- Formal status here: a published theorem used in a written proof, not a
  new Lean declaration or custom axiom. No attempt is made to reconstruct
  Matveev's full transcendence proof in this checkpoint.

## SdW05 — the classical cycle-chaining architecture

John Simons and Benne de Weger, **Theoretical and computational bounds for
`m`-cycles of the `3n+1`-problem**, *Acta Arithmetica* 117 (2005), 51–70.

- DOI: <https://doi.org/10.4064/aa117-1-3>
- Author-hosted published PDF:
  <https://math.deweger.net/papers/%5B35%5DSidW-3n%2B1-ActaArith%5B2005%5D.pdf>
- Journal record:
  <https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/117/1>
- Inspected: definition of `m` in §1.2; the attribution of fixed-`m` finiteness
  to Brox in §1.4 and Theorem 3(a); §§3.2–3.4, especially the chain inequality
  in Lemma 6; and §5's logarithmic-form comparison.
- Used as inspiration and precedence: exact integrality bounds a rising run;
  chaining controls subsequent minima; a logarithmic-form estimate bounds a
  complete cycle. This packet replaces a monotone run by an arbitrary
  repeated finite parity atom and allows its exponent to vary independently.
- Not claimed new: Steiner's single-rise/single-fall cycle exclusion, Brox's
  fixed-`m` finiteness, or the use of transcendence bounds in cycle problems.
  The primary source itself credits those earlier results. This packet does
  not claim to have independently read Steiner's original 1978 proceedings
  article or to improve the paper's numerical `m`-cycle exclusions.
- The later author version 1.44, dated 31 August 2010, was located but is not
  the source of the theorem constants used here. No current computational
  cycle lower bound is imported.

## Repository inputs frozen for this pass

| Source | Full head | Exact material used |
|---|---|---|
| PR 183 | `907a540943090968bc683b1b9246208e9053c1f8` | `research/literature-closing-20261121/arithmetic/BandArithmetic.lean`, especially `repeated_parity_requires_displacement`; the existing compiled dependency is reused |
| PR 185 | `276be8154f4e867acc0230466b34d9cb224aacf5` | `research/whole-repo-closure-20261122/EFFECTIVE_FIXED_BLOCK_CYCLES.md`; comparison with its one-parameter fixed linear block schemas |
| PR 182 | `45354128f890fb479f6c23b547368bcddd9cebe6` | `research/lean-dyadic-descent-20261121/LITERATURE_SYNTHESIS.md`; source-indexed Fourier/label regularity is distinguished from temporal word compression |
| PR 186 | `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493` | `literature/deep-machinery-20261122/README.md` and arithmetic task cards; used as a research map, not an imported proof |

The global-period and free-exponent derivations are reconstructed in
`FREE_EXPONENT_CYCLES.md`; no proof status from another PR is extended to
these new written claims. The selected source heads and statements have
independent evidence boundaries.
