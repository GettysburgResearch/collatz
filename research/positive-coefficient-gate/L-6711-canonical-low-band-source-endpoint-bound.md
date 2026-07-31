# L-6711 — canonical low-band source–endpoint accumulation bound

**Claim ID:** `L-6711`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-review-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Dependencies:** exact affine remainder identity from independently reconstructed `T-6709`

## Statement

Let `w=v_0...v_{N-1}` be an all-prefix-supercritical shortcut parity word. Put

\[
q_k=\sum_{i<k}v_i,
\qquad
\alpha=\frac{\log2}{\log3},
\qquad
D_k=q_k-\alpha k\ge0,
\qquad
a=1-\alpha.
\]

Let `(r_w,s_w)` be its canonical positive source–endpoint pair:

\[
T_w(r_w)=s_w,
\qquad
1\le r_w\le2^N,
\qquad
1\le s_w\le3^{q_N}.
\]

For `H>0`, define

\[
N_H(N)=\#\{1\le m\le N:v_{m-1}=1,\ D_m<H+a\}.
\]

Then

\[
\boxed{
s_w
\ge
3^{D_N}r_w
+
\frac{N_H(N)}{2}\,3^{D_N-H-a}.
}
\]

In particular, because `D_N>=0`,

\[
\boxed{
s_w-r_w
\ge
\frac{N_H(N)}{2\,3^{H+a}}.
}
\]

If additionally `D_N<H`, the same inequality holds with both endpoints lying at a low-surplus terminal time; hence every new low-band odd endpoint creates a permanent uniform increase in the canonical endpoint relative to the same canonical source.

## Proof

The exact finite affine identity is

\[
s_w
=3^{D_N}r_w
+\frac12\sum_{m=1}^{N}v_{m-1}3^{D_N-D_m}.
\]

For every index counted by `N_H(N)`, one has `D_m<H+a`, and therefore

\[
3^{D_N-D_m}>3^{D_N-H-a}.
\]

Keeping only those positive terms gives the first inequality. Since `D_N>=0`, one has `3^{D_N}r_w>=r_w` and `3^{D_N-H-a}>=3^{-H-a}`, giving the second. ∎

## Fixed-source consequence

Suppose one fixed ordinary source `n` realizes nested all-supercritical words `w_N` for every `N`. Once `2^N>n`, canonicality gives

\[
r_{w_N}=n,
\qquad
s_{w_N}=T^N(n).
\]

For every fixed `H`, if low-band odd endpoints occur infinitely often, then along the nested canonical pairs

\[
s_{w_N}-n
\ge
\frac{N_H(N)}{2\,3^{H+a}}
\longrightarrow\infty.
\]

If low-band visits eventually stop, the multiplicative term eventually stays above `3^H n`. This is the finite canonical-pair version of the low-band proof in `T-6709`.

## Why this does not close SC*

The lemma controls the endpoint `s_w` once a source has been fixed. It does not force the canonical source `r_w` to grow across different words. The endpoint coordinate can absorb every accumulated positive correction while the same small source remains compatible.

Thus the missing implication is not

```text
many low-band contributions -> large endpoint,
```

which is now exact, but rather a two-boundary uncertainty principle forbidding simultaneously

```text
small canonical source,
subexponential canonical endpoint,
and arbitrarily deep all-supercritical divisibility.
```

In valuation form, one still needs a source-dependent upper bound on

\[
v_2(3^{q(w)}r_w+A_w)
\]

for all-supercritical words with bounded `r_w`.

## Gap audit

- Strict `>` in the individual contribution may safely be weakened to `>=` in the displayed boxed bound by replacing the threshold with its infimum.
- The lemma is finite and uses no inverse-limit argument.
- It assumes canonical source–endpoint normalization from the finite parity-cylinder bijection.
- It proves endpoint escape for a fixed ordinary source, not source escape across the finite word family.
