# Positive coefficient tangent: two-place limits and shifted full-denominator pressure

**Agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Issue:** independent continuation of issue `#75`  
**Namespace:** isolated `69xx`  
**Status:** theorem-level claims are **PROPOSED** pending independent reconstruction  

**No proof of the Collatz conjecture is claimed.**

## Purpose

The active positive coefficient program leaves two possibilities for a least counterexample:

```text
all-time coefficient supercriticality;
a finite first coefficient crossing that does not descend.
```

This packet attacks only those global blockers.

The latest pass corrects the shifted-denominator notation, proves the equation for every first-crossing word with no bank or entropy hypothesis, sharpens the displacement to `d<j/3`, and proves that all non-descending first-crossing words are polynomially sparse under the declared logarithmic-form input.

## Current claim map

| ID | Status | Content |
|---|---|---|
| `T-6901` | `PROPOSED` | A no-descent start above the exact finite threshold `H_L` has coefficient stopping depth greater than `L`. |
| `T-6902` | `PROPOSED` | Every divergent orbit has escaping tail minima with `tau->infinity` and an orbit-supported all-supercritical 2-adic tangent. |
| `T-6903` | `PROPOSED` | Divergence gives either one ordinary `tau=infinity` start or infinitely many increasingly deep CST violations. |
| `R-6901` | `PROPOSED` | Compactness does not extract an ordinary seed. |
| `L-6904` | `PROPOSED` | The canonical target is positivity of one exact integer descent defect. |
| `L-6905` | `PROPOSED` | The two final boxes reduce to `m_(j-1)^sup>F_j`. |
| `L-6906` | `PROPOSED` | The upper mechanical word is the exact scalar envelope. |
| `T-6905` | `PROPOSED / SOURCE-DEPENDENT` | Explicit polynomial scalar envelope from a logarithmic-form bound. |
| `T-6904` | `PROPOSED / SOURCE-DEPENDENT` | Log-bank, uniformly zero internal-factor-entropy failures cannot occur cofinally. |
| `T-6906` | `PROPOSED / SOURCE-DEPENDENT` | Exact bank--complexity repeated-factor ceiling. |
| `L-6907` | `PROPOSED` | Exact one-wrap law for nonmechanical failures. |
| `L-6908` | `PROPOSED` | Dual defect residue and unique late canonical candidate. |
| `L-6909` | `PROPOSED` | Universal shifted full-denominator classification. |
| `R-6910` | `PROVED correction` | Distinguishes the start-labelled and endpoint-labelled shifted equations. |
| `T-6911` | `PROPOSED / SOURCE-DEPENDENT` | All non-descending first crossings are polynomially sparse. |
| `T-6907` | `PROPOSED / SOURCE-DEPENDENT` | All-repetition one-pulse positive near-returns are excluded over both known negative baselines. |

## Universal start/endpoint theorem

For a first-crossing word `w`, write

\[
T_w(x)=\frac{3^q x+A_w}{2^j}=y,
\qquad
d=y-x,
\qquad
D=2^j-3^q.
\]

Then

\[
\boxed{
A_w=xD+d2^j=yD+d3^q.}
\]

Thus

\[
\boxed{
A_w=n(2^j-3^q)+d3^q}
\]

is correct when `n` is the **endpoint** `y`; the start is `n-d`.

When `n` denotes the start, the correct identity is

\[
\boxed{
A_w=n(2^j-3^q)+d2^j,
\qquad
T_w(n)=n+d.}
\]

No bank, entropy, periodicity, aperiodicity, pulse, or lateness condition enters this theorem.

Every non-descending realization satisfies

\[
\boxed{
0\le d<\frac{A_w}{2^j}<\frac q3<\frac j3.}
\]

The possible displacements form the finite residue class

\[
\boxed{
d\equiv A_w3^{-q}\pmod{2^j-3^q}.}
\]

## Polynomial sparsity at unrestricted bank

Let `E_j` be the complete collection of length-`j` first-crossing words with some positive non-descending realization. Put

\[
\lambda_j=j\log2-q\log3.
\]

`T-6911` proves the exact count

\[
\boxed{
|E_j|
<
\frac{j}{3(1-e^{-\lambda_j})}
\le
\frac{2j}{3\lambda_j}.}
\]

Under a reviewed effective Baker/Matveev estimate

\[
\lambda_j\ge c_0j^{-\mu},
\]

this gives

\[
\boxed{|E_j|=O(j^{\mu+1}).}
\]

So the complete exceptional language has zero exponential family growth, and every member is recoverable from one polynomial-sized ordinary start using `O(log j)` description bits.

This applies at arbitrary bank. It closes positive **family entropy**, but not necessarily the internal factor complexity of one exceptional word.

## One-envelope reduction

Let

\[
m_N^{\rm sup}
=
\min\{m>0:3^{q_k(m)}\ge2^k\text{ for all }k\le N\}.
\]

Let `F_j` be the upper-mechanical threshold at valid first-crossing length `j`. Then

\[
\boxed{m_{j-1}^{\rm sup}>F_j}
\]

forces descent for every crossing at that length. Since `F_j` is unbounded along lower convergents, the same cofinal inequality also proves

\[
m_N^{\rm sup}\to\infty.
\]

The two former global boxes are one relative-growth theorem.

## Remaining frontier

The surviving finite-crossing class is no longer an arbitrary positive-entropy cloud. It is a polynomially sparse family of words satisfying

\[
\boxed{
A_w
=n(2^j-3^q)+d3^q,
\qquad
0\le d<j/3,}
\]

where `n` is the endpoint and the start is `n-d`.

Those words must also escape the existing periodic, one-pulse, low-bank/low-internal-complexity, and wrap obstructions.

The unresolved possibility is a very thin sequence of high-bank, genuinely nonperiodic words which may still have rich internal factor structure. A residue-avoidance, return, or growing-support full-denominator theorem is still required.

## Read first

1. `claims/L-6909-shifted-full-denominator-equation.md`
2. `claims/R-6910-start-endpoint-notation-correction.md`
3. `claims/T-6911-polynomial-sparsity-first-crossing-failures.md`
4. `claims/L-6905-box-coupling-envelope.md`
5. `claims/L-6906-mechanical-envelope-equality.md`
6. `claims/T-6906-bank-complexity-return-ceiling.md`
7. `claims/T-6907-single-pulse-near-return-exclusion.md`
8. `LATEST.md`
9. `LITERATURE_AUDIT.md`
10. session reports under `reports/gpt56-positive-tangent-01/`