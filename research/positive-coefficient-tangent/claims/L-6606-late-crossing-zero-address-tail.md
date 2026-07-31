# L-6606 — Late canonical first-crossing failures have a zero address tail

**Claim ID:** `L-6606`  
**Status:** **PROPOSED**; the logarithmic-support corollary is source-qualified  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** elementary parity-cylinder lifting; `T-6605` only for the source-qualified polynomial bound on the fixed-point threshold  
**Scope:** one finite first coefficient-crossing word  

## 1. Compatible canonical prefix roots

Let

\[
w=(v_0,\ldots,v_{j-1})
\]

be a first coefficient-crossing word. For each `0<=k<=j`, let

\[
r_k\in[0,2^k)
\]

be the canonical residue realizing the first `k` parity bits of `w`, with `r_0=0`.

Compatibility gives one binary address digit

\[
\varepsilon_k\in\{0,1\}
\]

such that

\[
\boxed{
r_{k+1}=r_k+\varepsilon_k2^k.}
\tag{1}
\]

Thus `(r_k)` is nondecreasing, and the final canonical positive representative is

\[
r^+(w)=r_j.
\]

Let

\[
T_w(x)={3^q x+A_w\over2^j},
\qquad
x_*(w)={A_w\over2^j-3^q}.
\tag{2}
\]

## 2. Exact support-collapse theorem

Assume the canonical representative does not descend at the first crossing:

\[
T_w(r_j)\ge r_j.
\tag{3}
\]

The canonical crossing identity of `T-6605` gives

\[
\boxed{r_j\le x_*(w).}
\tag{4}
\]

If `epsilon_k=1`, equations `(1)` and monotonicity imply

\[
2^k\le r_{k+1}\le r_j\le x_*(w).
\tag{5}
\]

Therefore

\[
\boxed{
2^k>x_*(w)
\quad\Longrightarrow\quad
\varepsilon_k=0.}
\tag{6}
\]

Put

\[
K(w)=1+\left\lfloor\log_2 x_*(w)\right\rfloor
\tag{7}
\]

when `x_*(w)>=1`. Then

\[
\boxed{
\varepsilon_k=0
\quad(K(w)\le k<j),}
\tag{8}
\]

and hence

\[
\boxed{
r_{K(w)}=r_{K(w)+1}=\cdots=r_j.}
\tag{9}
\]

If `x_*(w)<1`, equation `(4)` is already impossible for a positive canonical root.

Thus any failure of Box 2 has an eventually zero pulled-back binary address, with the support cutoff given by the exact real fixed-point threshold of the same word.

## 3. Physical meaning of a zero address digit

Let

\[
z_k=T^k(r_k)
\]

be the endpoint of the canonical `k`-bit root, and let `q_k` be the number of odd bits in the prefix.

The two lifts `r_k` and `r_k+2^k` reach, after `k` steps,

\[
z_k
\quad\text{and}\quad
z_k+3^{q_k},
\]

respectively. Since `3^(q_k)` is odd, their next parities are opposite. Therefore

\[
\boxed{
\varepsilon_k
\equiv
v_k-z_k
\pmod2.}
\tag{10}
\]

On the zero tail `(8)`, the fixed ordinary integer `r_(K(w))` itself generates every remaining parity bit:

\[
v_k=T^k(r_{K(w)})\bmod2
\qquad(K(w)\le k<j).
\tag{11}
\]

This is not compactness or a free `2`-adic path. It is one finite ordinary initialization whose binary support was already complete by depth `K(w)`.

## 4. Final-sibling reduction

Write

\[
u=(v_0,\ldots,v_{j-2}),
\qquad
M=2^{j-1},
\]

and let `a=r_(j-1)` and `z=T^(j-1)(a)`. A first coefficient crossing necessarily ends in `v_(j-1)=0`.

The two length-`j` child roots are exactly

\[
a
\quad\text{and}\quad
a+M.
\]

The child whose next bit equals `z mod2` uses the lower root `a`; the other child uses the upper root `a+M`. Hence the first-crossing child satisfies

\[
\boxed{
r_j=
\begin{cases}
a,&z\equiv0\pmod2,\\
a+2^{j-1},&z\equiv1\pmod2.
\end{cases}}
\tag{12}
\]

Consequently, whenever

\[
x_*(w)<2^{j-1},
\tag{13}
\]

the upper-child case in `(12)` descends automatically. A non-descending candidate must then satisfy

\[
\boxed{
z\equiv0\pmod2,
\qquad
r_j=r_{j-1}.}
\tag{14}
\]

So every sufficiently late hard crossing takes the zero top lift at the final step.

## 5. Source-qualified logarithmic ordinary support

Let

\[
\lambda=j\log2-q\log3>0.
\]

As recorded in `T-6605`, a standard lower bound for the nonzero two-logarithm form gives effective constants `c_0,mu>0` such that

\[
\lambda\ge c_0j^{-\mu},
\]

while the first-crossing affine remainder gives

\[
x_*(w)<c_0^{-1}j^{\mu+1}.
\tag{15}
\]

Combining `(7)` and `(15)`, every canonical Box-2 failure satisfies

\[
\boxed{
K(w)
\le
(\mu+1)\log_2j
+\log_2(c_0^{-1})+1.}
\tag{16}
\]

Thus the full `j`-step parity word is rooted in an ordinary integer whose pulled-back address has only `O(log j)` potentially nonzero bits; the remaining `j-O(log j)` address bits are exactly zero.

In particular, `(13)` holds for every sufficiently large `j`, so all sufficiently late hard crossings are lower-child, zero-top-lift crossings.

The precise logarithmic-form source must be frozen and independently reconstructed before `(15)--(16)` are promoted. Equations `(1)--(14)` are elementary.

## 6. Relationship to the two global boxes

The result gives a direct interface between the project’s two remaining positive targets.

```text
Box 1:
  rule out an eventually zero address for an infinite
  all-supercritical path;

Box 2:
  rule out an address that becomes zero after O(log j)
  bits and then physically generates a late first crossing
  without descent.
```

A finite-crossing counterexample cannot hide in a diffuse inverse-limit completion. It is already one ordinary finite-support root extremely early relative to the crossing length.

## 7. Gap audit

- A polynomial-size ordinary root can still have a very long orbit segment; logarithmic address support is not itself a contradiction.
- The lemma does not exclude lower-child zero-tail crossings.
- The source-qualified constants in `(16)` may be enormous.
- No finite verification range is silently extrapolated.
- Box 2, eventual CST, and Collatz remain open.
