# Full-source psi induction checkpoint

The comparison is

\[
C_\psi(n):\quad \operatorname{Basin}(n)
\;\Longleftrightarrow\;\operatorname{Basin}(2n-1).
\]

The frozen search result contains **1,265 successful residue-family rules** and **175 unresolved families** modulo 1,440. Every auxiliary query in a successful rule has source `u<n` on the entire positive affine cell. The active comparison family is exactly `[psi]`; the exported rules use no triple or five assumptions. Ordinary forward and reverse edges are checked as actual integer affine identities.

Each cell is `n=1440*t+r`, `t>=0`. The cell for residue one uses `r=1441`, because `n=1` is the separately proved base case. Thus both even and odd source integers are included. No even-source normalization is applied to psi.

The unresolved residues are all even: 125 are zero modulo four and 50 are two modulo four. They remain explicit data. They are not emitted as axioms, certificates, or successful fallback branches. This checkpoint does not prove a complete cover or Collatz.

## What Lean verifies

`AffineJointDescent.lean` proves the soundness of ordinary edges, active-kind queries with strict weighted rank, whole affine paths, and certificate pairs. It supports the comparison kinds triple, five, and psi, with a caller-specified active list. Positive affine constant terms protect the `2*n-1` target from natural-subtraction clipping.

Its `comparisons_of_complete` theorem uses strong induction on the natural rank. `collatz_of_complete_triple` and `collatz_of_complete_psi` prove the corresponding global implication from a supplied total cover. No complete-cover hypothesis is inhabited by this checkpoint.

The generated `PurePsiCertificates.lean` proves every successful row valid in chunks of at most 16. It separately proves the exact row count, the relation between row roots and their listed residues, the explicit unresolved count and parity, and the complete finite accounting of successful versus unresolved residues. `checked_row_sound` is the theorem usable at any natural lift of a successful source cell under the smaller-query induction hypothesis.

The engine also contains three arithmetic lemmas for the continuing search:

- At an odd source `n`, the triple comparison is equivalent to the psi comparison at `(3*n+1)/2`.
- The even psi comparison at `2*m` follows from the triple comparison at `m` and the psi comparison at `3*m`. The latter query is larger in the linear rank and is explicitly not certified as a descent.
- A valuation-sensitive candidate rank has the exact three-quarters decrease from `2*m` to `3*m`; the separate triple query has not been shown compatible with it.
- The exact reciprocal family `C_psi(6*t+4) <-> C_psi(8*t+5)` is proved by ordinary exchange on both arms. No one natural rank can decrease on both selected directions. This explains why separately successful linear-rank and valuation-rank tables cannot simply be combined; other paths remain open.

The finite residue accounting uses a structurally recursive, fuel-bounded merge of two sorted residue lists and proves that its exact output is `List.range 1440`. A generic membership theorem for that merge supplies the coverage statement. This avoids both quadratic membership checking and the kernel reduction cost of the library's well-founded merge definition.

## Uniform even macro and the odd-source global criterion

`formal/Collatz/PsiParity.lean` proves the stronger uniform rule

\[
C_\psi(m)\;\land\;C_\psi(4m-1)
\quad\Longrightarrow\quad C_\psi(2m)\qquad(m>0).
\]

The two arms use the ordinary identities `Basin(2m)=Basin(m)` and `Basin(2m-1)=Basin(8m-3)`. The reverse direction of the comparison at `4m-1` is necessary. Both auxiliary sources decrease the valuation rank `n*2^(v_2(n))`: the half has one quarter of the source rank, and the other query is the odd integer `4m-1`, strictly below the source rank.

Ordinary induction on the original input, using the half as the induction query and the odd source as a globally supplied hypothesis, proves the exact theorem

\[
\operatorname{Collatz}\quad\Longleftrightarrow\quad
\forall n>0\text{ odd},\ C_\psi(n).
\]

This is a fully quantified Lean theorem, `collatz_iff_odd_psi`. It does not prove the odd-source hypothesis. In particular, the odd rows checked under linear rank cannot simply be combined with an even rule under a different rank; the reciprocal family above is an explicit obstruction to that inference.

## Reproduce

From `research/lean-ordinary-closure-20261121`:

```sh
python search/emit_pure_psi.py search/pure-psi.json lean/Collatz/PurePsiCertificates.lean --receipt ../../reports/2026-11-21-lean-ordinary-closure/pure_psi_export.json
cd lean
lake build
lake env lean JointAudit.lean
```

The generator imports no search module. It reconstructs all affine destinations and guards, checks the finite residue partition, preserves the missing families, and writes source/output hashes. Lean then checks the generated propositions independently. The exact finite accounting uses a structural merge, with its membership-preservation theorem proved in Lean.

The source JSON SHA-256 is `51d153e2921ab1d2a0085cb227b5037b7180c8bc21c5250c75079736a4aa7873`.

The search source is `search/search_affine_types.py`; the frozen JSON can be reproduced with `--modulus 1440 --weights psi:1 --output result.json` (elapsed-time metadata can differ). The generalized engine and independent exporter were built in a separate agent lane from the search. The analytic atom-floor theorem is a separate result and is not used by these finite induction rules.
