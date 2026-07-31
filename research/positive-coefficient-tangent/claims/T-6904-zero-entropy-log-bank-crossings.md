# T-6904 — logarithmic-bank zero-entropy first crossings are finite

**Claim ID:** `T-6904`  
**Status:** **PROPOSED / SOURCE-DEPENDENT**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** `L-6904`; an effective Baker lower bound for nonzero linear forms in `log 2` and `log 3`  
**Scope:** unbounded families of acyclic ordinary no-descent first coefficient crossings

## Source input

Because `2` and `3` are multiplicatively independent algebraic numbers, an effective Baker theorem supplies constants

\[
c_0>0,
\qquad
\mu>0,
\]

such that every nonzero form

\[
\lambda=j\log2-q\log3,
\qquad 0\le q\le j,
\]

satisfies

\[
\boxed{\lambda\ge c_0j^{-\mu}}
\tag{1}
\]

whenever `lambda>0`.

The precise source normalization must be independently reconstructed before status promotion.

## Family hypotheses

Let `w_r` be first-crossing words with lengths

\[
j_r\longrightarrow\infty,
\]

and let `n_r` be positive ordinary starts realizing `w_r` such that

\[
T^{j_r}(n_r)\ge n_r.
\tag{2}
\]

For proper prefixes put

\[
D_{r,t}=q_{r,t}-\alpha t,
\qquad
B_r=\max_{0\le t<j_r}D_{r,t},
\qquad
\alpha=\frac{\log2}{\log3}.
\]

Assume:

1. **logarithmic bank:** for fixed constants `b,C`,
   \[
   \boxed{B_r\le b\log_2j_r+C;}
   \tag{3}
   \]
2. **acyclicity:** the physical states before the crossing are pairwise distinct;
3. **uniform zero factor entropy:** if `p_r(L)` denotes the number of distinct length-`L` factors in `w_r`, then
   \[
   \boxed{
   \lim_{L\to\infty}
   \sup_{r:j_r\ge2L}
   \frac{\log_2p_r(L)}{L}=0.}
   \tag{4}
   \]

Then no such unbounded family exists.

Equivalently, every unbounded acyclic no-descent first-crossing family with logarithmic bank has positive factor entropy at logarithmic scales.

## Proof

Choose a constant

\[
K>b\log_2 3+\mu+1.
\tag{5}
\]

For each large `r`, put

\[
L_r=\lceil K\log_2j_r\rceil.
\tag{6}
\]

By `(4)`, choose `epsilon>0` with `epsilon K<1`. For all sufficiently large `r`,

\[
p_r(L_r)\le2^{\epsilon L_r}=j_r^{\epsilon K+o(1)}<j_r-L_r+1.
\]

Hence two occurrences of the same length-`L_r` factor begin before the crossing.

Let those occurrences begin at physical states `x_a` and `x_b`. Exact affine subtraction gives

\[
2^{L_r}\mid x_a-x_b.
\]

Acyclicity makes the difference nonzero, so

\[
|x_a-x_b|\ge2^{L_r}.
\tag{7}
\]

For every proper prefix, the exact affine formula is

\[
x_t
=3^{D_{r,t}}n_r
+\frac12\sum_{m=1}^t v_{m-1}3^{D_{r,t}-D_{r,m}}.
\]

Because `0<=D_(r,m)` and `D_(r,t)<=B_r`,

\[
x_t\le3^{B_r}\left(n_r+\frac{j_r}{2}\right).
\]

Combining this with `(7)` gives

\[
\boxed{
2^{L_r}+1
\le
3^{B_r}\left(n_r+\frac{j_r}{2}\right).}
\tag{8}
\]

At the first crossing write

\[
\lambda_r=j_r\log2-q_r\log3>0.
\]

The final step is even, every odd additive contribution is below `1/2`, and `(2)` therefore implies

\[
n_r(1-e^{-\lambda_r})<\frac{j_r}{2}.
\]

First crossing gives `0<lambda_r<log2`, so `1-e^(-lambda_r)>=lambda_r/2`. Using `(1)`,

\[
\boxed{n_r<c_0^{-1}j_r^{\mu+1}.}
\tag{9}
\]

Substitute `(3)` and `(9)` into `(8)`. Taking base-two logarithms gives

\[
L_r
\le
\bigl(b\log_2 3+\mu+1\bigr)\log_2j_r+O(1),
\]

contradicting `(5)--(6)`. ∎

## Quantitative entropy floor

The proof gives a sharper contraposition. Under `(2)--(3)` and acyclicity, every factor length

\[
L>
\bigl(b\log_2 3+\mu+1+o(1)\bigr)\log_2j
\]

has no repeated occurrence. Hence

\[
p_w(L)=j-L+1.
\]

For every fixed

\[
K>b\log_2 3+\mu+1,
\]

one obtains at `L=ceil(K log_2 j)` the finite-word entropy floor

\[
\boxed{
\liminf
\frac{\log_2p_w(L)}{L}
\ge\frac1K.}
\tag{10}
\]

## Families eliminated

The theorem excludes, under the logarithmic-bank hypothesis, every cofinal canonical target-failure family contained in a fixed zero-topological-entropy language. This includes any particular Sturmian, automatic, primitive-substitutive, or other uniformly subexponential factor language once its stated complexity bound is verified.

It strictly broadens the linear-complexity corridor in PR #80 `T-6505`: the factor complexity may be any uniformly subexponential function, and the proper-prefix bank may grow logarithmically rather than remain bounded.

## Relationship to Box 2

If `n_r=r^+(w_r)` is the canonical root and Box 2 fails, `L-6904` supplies the no-descent condition `(2)`. Therefore every unbounded acyclic canonical failure family must escape at least one hypothesis above:

```text
proper-prefix bank grows faster than logarithmically;
factor language has positive entropy at logarithmic scales;
or the physical segment contains a repeated state, hence a positive cycle.
```

This is an exhaustive negative theorem for one broad infinite class, genuinely weaker than Collatz.

## Gap audit

- High-bank and positive-entropy first-crossing families remain open.
- A repeated state is transferred to the full-denominator positive-cycle lane; it is not excluded here.
- The Baker constants are not instantiated.
- Uniform zero entropy across a changing family is stronger than saying each individual finite word has low empirical complexity.
- The theorem does not prove universal canonical descent.
