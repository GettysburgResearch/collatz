# Quick independent audit of T-6710 and L-6711

**Reviewing model:** `GPT-5.6 Thinking`  
**Issue:** #75  
**PR:** #77  
**Review date:** 2026-08-01  
**Frozen pre-correction blobs:**

```text
T-6710: f7f49b8e7dfb695ae073b7a4cc070a28b7b0d74c
L-6711: 200b57ed4d9fc3ac729b0c403a483b3e2c7178a0
T-6709 second review: f671fc4a79882b2dbf30497b822914d502d7c69e
```

## Verdict matrix

| Item | Verdict |
|---|---|
| `T-6709` second reconstruction | **PASSED** |
| `T-6710` exact inverse theorem | **PASSED** |
| `T-6710` SC* equivalence | **PASSED** |
| `T-6710` finite-verification transfer | **PASSED** |
| `T-6710` fixed-source valuation form | **PASSED after adding the omitted parity-cylinder justification** |
| `T-6710` final quantitative `Phi` shorthand | **CORRECTED** |
| `L-6711` canonical source–endpoint bound | **PASSED** |

No claim of SC*, coefficient stopping, or Collatz is established by these files.

## 1. T-6709

The low-band proof was reconstructed again. The indexing

\[
E_k=\frac12\sum_{m=1}^k v_{m-1}3^{D_k-D_m}
\]

is correct. The first future odd source after a visit `D_r<H` ends below `H+1-alpha`, and the quantifier order is valid:

```text
choose target M;
choose fixed H with 3^H n>M;
then choose one eventual K.
```

The same `K` controls every later time. The proof uses one fixed ordinary source and proves full divergence, not merely a subsequence result.

## 2. T-6710 inverse identity

For

\[
S_N=\{n\ge1:\tau_c(n)>N\},
\qquad m_N=\min S_N,
\]

one has directly

\[
m_N>B
\iff
\tau_c(n)\le N\quad(1\le n\le B).
\]

This is definitional and correct. Nestedness of `S_N` proves

\[
m_N\to\infty
\iff
\tau_c(n)<\infty\quad\forall n\ge1.
\]

The converse uses the discreteness of `m_N`: a bounded nondecreasing integer sequence stabilizes, and its stabilized value belongs to all sufficiently deep `S_N`, hence by nestedness to every `S_N`.

## 3. Finite convergence transfer

If `n>1` reaches `1` at time `r`, then

\[
1=C_rn+E_r,
\qquad E_r\ge0,
\]

so `C_r<=1/n<1`. Thus `tau_c(n)<=r`. The special start `n=1` has coefficient crossing at the word `10`. Therefore a certified maximal hitting time through `B` gives the stated finite source-escape bound. This argument is correct.

## 4. Fixed-source valuation form

The pre-correction file wrote the valuation condition together with the phrase “and the induced parity prefix is `w`,” then omitted that phrase in the equivalent fixed-source statement. The intended equivalence is nevertheless valid:

\[
3^{q(w)}n+A_w\equiv0\pmod{2^{|w|}}
\]

has one residue class because `3^{q(w)}` is odd. Its canonical member is the parity-cylinder source `r_w`; therefore the finite parity-cylinder bijection implies that every solution follows `w`.

The branch file was updated to state this justification explicitly.

## 5. Corrected quantitative envelope

The only genuine mathematical error found was the final shorthand

\[
m_N>\max\{B:\Phi(B)\le N\}.
\]

For an arbitrary source-dependent bound `Phi(n)`, knowing only `Phi(B)<=N` does not control smaller sources. The correct monotone envelope is

\[
\widehat\Phi(B)=\max_{1\le n\le B}\Phi(n).
\]

Then

\[
N\ge\widehat\Phi(B)
\Longrightarrow
m_N>B,
\]

and

\[
m_N>\max\{B:\widehat\Phi(B)\le N\}.
\]

This defect was non-load-bearing: it affected only the final quantitative corollary, not the exact SC* equivalence or the isolated missing inequality.

## 6. L-6711

For every counted low-band odd endpoint, `D_m<H+a`, hence

\[
\frac12 3^{D_N-D_m}
>
\frac12 3^{D_N-H-a}.
\]

Keeping these positive terms yields

\[
s_w
\ge
3^{D_N}r_w+
\frac{N_H(N)}2 3^{D_N-H-a}.
\]

Since all-prefix supercriticality gives `D_N>=0`, subtracting `r_w` yields

\[
s_w-r_w
\ge
\frac{N_H(N)}{2\,3^{H+a}}.
\]

The use of `>=` is safe although the termwise estimates are strict. Once one fixed source `n<2^N` realizes the nested word, canonicality indeed gives `r_{w_N}=n`; the canonical endpoint is `T^N(n)`. The lemma correctly proves endpoint accumulation, not source escape.

## Final verdict

The previous work was substantially reliable. After correcting the `Phi` envelope and making the parity-cylinder implication explicit:

```text
T-6709: passes.
T-6710: passes.
L-6711: passes.
SC*: remains open.
```
