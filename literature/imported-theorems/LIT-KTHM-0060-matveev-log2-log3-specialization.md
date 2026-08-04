# LIT-KTHM-0060 — Source-audited Matveev specialization for the pulse repetition forms

**Status:** `KNOWN — EXACT SOURCE SPECIALIZATION + EXACT CERTIFICATE`  
**Primary source:** E. M. Matveev, *An Explicit Lower Bound for a Homogeneous Rational Linear Form in the Logarithms of Algebraic Numbers. II*, Izvestiya: Mathematics 64 (2000), 1217–1269, Corollary 2.3  
**Source inspection:** complete English PDF, especially pp. 1219–1220 and the height conventions in Section 5  
**Native interfaces:** PR #53 `T-8202/T-8255`, PR #70 `T-8260`, `LIT-KTHM-0061/0064/0065`  
**Counterexample status:** no positive cycle is claimed

## Source theorem in the required case

Matveev considers a nonzero form

\[
\Lambda=b_1\log\alpha_1+\cdots+b_n\log\alpha_n
\]

in fixed logarithms of algebraic numbers. Corollary 2.3 gives

\[
\log|\Lambda|
>
-C_1(n)D^2\Omega\log(eD)\log(eB),
\tag{1}
\]

where `D` is the field degree, `Omega=A_1...A_n`, the `A_i` dominate the logarithmic heights and logarithm moduli, and `B` is Matveev's weighted coefficient parameter from equation `(1.3)`. Corollary 2.3 also permits the coarser replacement

\[
B^*=\max_i|b_i|.
\]

For a real rational field, `n=2`, `D=1`, and `kappa=1`, the first source branch is

\[
C_1(2)
\le e\,30^5\,2^{7/2}.
\]

The exact rational certificate proves

\[
e\,30^5\,2^{7/2}<748000000<2^{32}.
\tag{2}
\]

Taking

\[
\alpha_1=2,
\qquad
\alpha_2=3,
\qquad
A_1=\log2,
\qquad
A_2=\log3
\]

therefore yields the safe general bound

\[
\boxed{
\log|m\log2-n\log3|
>
-748000000\log2\log3\,
\bigl(1+\log\max\{|m|,|n|\}\bigr).}
\tag{3}
\]

The form is nonzero because `2` and `3` are multiplicatively independent.

## Native coefficient normalization

For the pulse claims,

\[
\Lambda=(Ar+t)\log2-kr\log3>0.
\tag{4}
\]

Order the two source logarithms as

\[
\alpha_1=2,
\qquad
\alpha_2=3,
\]

so `A_2=log 3` is the denominator in Matveev's weighted parameter `(1.3)`. Then

\[
B
=
\max\left\{
1,
(Ar+t)\frac{\log2}{\log3},
kr
\right\}.
\tag{5}
\]

Once `Lambda<log3`,

\[
(Ar+t)\frac{\log2}{\log3}
=
kr+\frac{\Lambda}{\log3}
<kr+1,
\]

and therefore

\[
\boxed{B<kr+1.}
\tag{6}
\]

This is a bound on Matveev's **weighted** parameter `B`, not on the coarser

\[
B^*=\max\{Ar+t,kr\}.
\]

An earlier version of this note incorrectly labeled `(6)` as a `B^*` bound. The numerical pulse certificates used `kr+1` and are justified by the weighted parameter `(5)`; their inequalities and cutoffs are unchanged by this notation correction.

Equations `(1)`, `(2)`, and `(4)--(6)` justify the exact logarithmic lower bound required by PR #53, PR #70, and the fixed-support extensions. The previous use of `2^32 log2 log3` was safe but unnecessarily coarse.

## Strengthened certified cutoffs

Combining the source bound with the native upper bounds gives the following clean source-audited cutoffs:

| claim/family | previous cutoff | strengthened cutoff |
|---|---:|---:|
| `T-8255`, `P3=(1,2)` | `100,000,000,000` | `14,600,000,000` |
| `T-8255`, `P11=(1,1,1,2,1,1,4)` | `25,000,000,000` | `3,800,000,000` |
| `T-8260`, `P3` | `200,000,000,000` | `23,800,000,000` |
| `T-8260`, `P11` | `50,000,000,000` | `5,800,000,000` |

The exact margins and derivative certificates are frozen by `LIT-X-0060`. Positive derivative after each cutoff proves persistence for every larger repetition.

## Status consequence for native claims

The phrase

```text
SOURCE-DEPENDENT on an unreconstructed Matveev normalization
```

is no longer necessary for the logarithmic-form step itself. It may be replaced by

```text
SOURCE-AUDITED at the Matveev step.
```

This does not automatically promote `T-8255` or `T-8260`: their pulse identities, largest-gap normalization, continued-fraction coverage, resultant caps, and finite replay retain their native review statuses.

## Applicability audit

- Corollary 2.3, not an unspecified two-logarithm folklore bound, is the exact source used.
- `A_1=log2` and `A_2=log3` satisfy the height hypotheses because the absolute logarithmic heights of the rational integers are those logarithms.
- The coefficient signs are allowed.
- The sharper native estimate uses the weighted parameter `B` from Matveev `(1.3)`; the universal display `(3)` uses the permitted coarser `B^*`.
- The theorem is Archimedean; it does not bound any `p`-adic valuation.

## Gap audit

- The cutoffs remain large and do not replace the continued-fraction reduction.
- Matveev does not prove the pulse corrections nonzero or physically legal.
- It gives no positive cycle.
- It does not handle a support size whose geometric rate is nonpositive.

## Exact artifact

```bash
python3 literature/experiments/LIT-X-0060-matveev-specialization/run.py \
  --check-results \
  literature/experiments/LIT-X-0060-matveev-specialization/results/canonical.json
```
