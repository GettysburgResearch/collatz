# T-0046 — Two-sided cap–root overlap forced by every ordinary survivor

Claim ID: `T-0046`  
Title: An ordinary six-branch survivor is simultaneously a stabilized past root and a canonical future root at a linearly growing overlap horizon  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-08-01  
Dependencies: `L-0041`; elementary affine growth bounds  
Scope: the strict stationary six-branch chart  
Related counterexample candidates: none

## 1. Setup

Retain

\[
P=3^{12},
\qquad
Q=2^{19},
\qquad
\lambda={P\over Q}>1,
\qquad
d=P-Q=7153,
\]

and the root/cap notation `(R_w,S_w)` of `L-0041`.

Put

\[
a_- =229376,
\qquad
a_+=413343,
\]

\[
b_-={a_-\over d},
\qquad
b_+={a_+\over d}.
\]

Every legal orbit satisfies

\[
\boxed{
\lambda^n(x_0+b_-)-b_-
\le x_n\le
\lambda^n(x_0+b_+)-b_+.}
\tag{1}
\]

Indeed the lower and upper comparison sequences use the fixed digits `a_-` and `a_+`, whose fixed points are `-b_-` and `-b_+`.

## 2. Exact past stabilization

Assume that one positive ordinary root `x_0` is legal forever, with type word

\[
i_0i_1i_2\cdots .
\]

Let

\[
u_n=i_0\cdots i_{n-1}.
\]

Once

\[
Q^n>x_0,
\]

the least representative of the length-`n` source cylinder is exactly `x_0`.  Hence

\[
\boxed{R_{u_n}=x_0}
\tag{2}
\]

and exact replay gives

\[
\boxed{S_{u_n}=x_n.}
\tag{3}
\]

This is the ordinary most-significant stabilization condition in its chart-specific form.

## 3. Exact future canonical root

For `ell>=1`, let

\[
v_{n,\ell}=i_ni_{n+1}\cdots i_{n+\ell-1}
\]

be the length-`ell` future word starting at time `n`.

The state `x_n` belongs to its source cylinder.  Therefore

\[
x_n=R_{v_{n,\ell}}+Q^\ell h
\]

for one `h>=0`.  Whenever

\[
Q^\ell>x_n,
\]
none of the positive lifts fits below `Q^ell`; consequently

\[
\boxed{R_{v_{n,\ell}}=x_n.}
\tag{4}
\]

Combining `(3)` and `(4)` gives the exact two-sided overlap

\[
\boxed{
S_{u_n}=R_{v_{n,\ell}}.}
\tag{5}
\]

Thus every late ordinary boundary is simultaneously:

```text
canonical cap of its entire past,
canonical root of a sufficiently long piece of its future.
```

No completion or limiting interpretation occurs in `(5)`; both sides are finite ordinary integers.

## 4. Sharp overlap scale

Define the minimal future-root length

\[
\boxed{
\ell_n=1+\lfloor\log_Q x_n\rfloor.}
\tag{6}
\]

Then `Q^(ell_n)>x_n`, so `(5)` holds with `ell=ell_n` for every sufficiently late `n`.

The bounds `(1)` imply

\[
\boxed{
{\ell_n\over n}
\longrightarrow
\alpha:=\log_Q\lambda.}
\tag{7}
\]

Numerically,

\[
\boxed{
\alpha
=
\log_{2^{19}}\left({3^{12}\over2^{19}}\right)
=0.001028947823888\ldots .}
\tag{8}
\]

Hence the future word needed to recover the complete current ordinary state has length only about one step per `971.866...` past steps.

## 5. Finite exclusion criterion

For integers `n,ell>=1`, define the finite bridge set

\[
\mathcal B_{n,\ell}
=
\{(u,v): |u|=n,\ |v|=\ell,\ S_u=R_v,\ Q^{\ell-1}\le S_u<Q^\ell\}.
\tag{9}
\]

If the chart had an ordinary survivor, then for every sufficiently large `n`,

\[
\boxed{
(u_n,v_{n,\ell_n})\in\mathcal B_{n,\ell_n}.}
\tag{10}
\]

Therefore either of the following excludes the complete stationary six-branch architecture:

1. `B_(n,ell)` is empty on a cofinal family with `ell/n -> alpha` covering the integer interval in `(1)`;
2. every cofinal chain of exact overlaps fails compatibility with the next root/cap extension.

This is a direct ordinary-extraction target.  It is not another completion formalism: a positive chain supplies the written states `x_n`, while a negative theorem eliminates every ordinary root in the chart.

## 6. Why the overlap is not automatic

Every finite past word has a cap and every finite future word has a root, but equality `(5)` is highly nongeneric.  It requires the same integer to satisfy simultaneously:

- a `P`-adic-style output condition determined by the complete past;
- a `Q`-adic source condition determined by the future;
- the ordinary height window `Q^(ell-1)<=x_n<Q^ell`.

Finite compatibility on either side separately does not imply the equality.

Conversely, isolated finite equalities do not prove a survivor.  They must form one compatible cofinal chain whose initial roots stabilize as in `T-0043`.

## Proof of the growth bounds

From

\[
Qx_{n+1}=Px_n+a_n,
\qquad a_-\le a_n\le a_+,
\]
we obtain

\[
x_{n+1}+b_-\ge\lambda(x_n+b_-),
\]

\[
x_{n+1}+b_+\le\lambda(x_n+b_+).
\]

Iteration proves `(1)`.  Taking logarithms in `(1)` gives

\[
\log_Qx_n=n\log_Q\lambda+O(1),
\]

which proves `(7)`.  Sections 2--3 prove the remaining claims. ∎

## Gap audit

- The theorem supplies a necessary finite equality, not its exclusion.
- The bridge length is small relative to the past but still unbounded.
- Counting, zero density, or failure of a bounded search does not prove `B_(n,ell)` empty.
- No ordinary survivor or Collatz counterexample is claimed.
