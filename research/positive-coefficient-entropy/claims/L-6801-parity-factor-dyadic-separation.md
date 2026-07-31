# L-6801 — Equal parity factors force dyadic separation

**Claim ID:** `L-6801`  
**Title:** Repeated shortcut-parity factors begin at states separated by their full dyadic modulus  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Reviewing agents:** none yet  
**Created:** 2026-07-31  
**Last updated:** 2026-07-31  
**Issue:** #75  
**Dependencies:** elementary shortcut-Collatz affine composition  
**Scope:** one positive ordinary shortcut-Collatz orbit; no probabilistic or completion assumption

## 1. Setup

Let

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\[1mm]
(3x+1)/2,&x\equiv1\pmod2,
\end{cases}
\]

and let

\[
x_t=T^t(n),
\qquad
v_t=x_t\bmod2\in\{0,1\}.
\]

For a finite binary word

\[
w=(w_0,\ldots,w_{L-1})
\]

of length `L` and weight

\[
s=\sum_{r=0}^{L-1}w_r,
\]

its exact shortcut affine map has the form

\[
\boxed{
T_w(x)=\frac{3^s x+A_w}{2^L}}
\tag{1}
\]

for one nonnegative integer `A_w` determined by the chronological word.

## 2. Dyadic separation theorem

Suppose the same length-`L` parity factor occurs at two orbit positions `i<j`:

\[
(v_i,\ldots,v_{i+L-1})
=
(v_j,\ldots,v_{j+L-1})
=w.
\]

Then

\[
\boxed{2^L\mid x_i-x_j.}
\tag{2}
\]

In particular, if `x_i != x_j`, then

\[
\boxed{|x_i-x_j|\ge2^L.}
\tag{3}
\]

### Proof

Applying `(1)` from both starting positions gives

\[
2^Lx_{i+L}=3^s x_i+A_w,
\qquad
2^Lx_{j+L}=3^s x_j+A_w.
\]

Subtracting,

\[
2^L(x_{i+L}-x_{j+L})=3^s(x_i-x_j).
\]

Since `gcd(2^L,3^s)=1`, divisibility `(2)` follows. If the two starting states differ, their nonzero difference is a multiple of `2^L`, proving `(3)`. ∎

## 3. Multiplicity consequence

Let

\[
X_N=\max_{0\le t\le N}x_t.
\]

Assume the states

\[
x_0,x_1,\ldots,x_{N-L}
\]

are pairwise distinct. Then any fixed length-`L` parity factor can occur among the starting positions `0,...,N-L` at most

\[
\boxed{1+\frac{X_N}{2^L}}
\tag{4}
\]

times.

Consequently, if `p_N(L)` denotes the number of distinct length-`L` parity factors beginning between times `0` and `N-L`, then

\[
\boxed{
p_N(L)
\ge
\frac{N-L+1}{1+X_N/2^L}.}
\tag{5}
\]

### Proof

All occurrences of one factor begin at states in one residue class modulo `2^L` by `(2)`. Distinct positive integers in one such class and in `[1,X_N]` are spaced by at least `2^L`, so there are at most `1+X_N/2^L` of them. Summing the occurrence multiplicities of the `p_N(L)` distinct factors gives `N-L+1`, yielding `(5)`. ∎

## 4. No-repeat corollary for coefficient-supercritical paths

Put

\[
\alpha=\frac{\log2}{\log3},
\qquad
q_k=\sum_{t=0}^{k-1}v_t,
\qquad
D_k=q_k-\alpha k.
\]

If

\[
D_k\ge0
\qquad(k\ge0),
\tag{6}
\]

then all ordinary orbit states `x_k` are distinct.

### Proof

Suppose `x_i=x_j` for some `i<j`. The intervening parity word, of length `r=j-i` and weight `s=q_j-q_i`, repeats forever. Its positive fixed point identity is

\[
(2^r-3^s)x_i=A_w>0,
\]

so

\[
2^r>3^s
\quad\Longleftrightarrow\quad
s-\alpha r<0.
\]

After `m` repetitions,

\[
D_{i+mr}=D_i+m(s-\alpha r),
\]

which becomes negative for large `m`, contradicting `(6)`. ∎

## 5. Why this lemma matters

The ordinary orbit cannot reuse one parity block cheaply. Repetition of a length-`L` factor requires its starting states to be separated by at least the full parity-cylinder modulus `2^L`.

This is an Archimedean consequence of exact dyadic integrality. It is stronger than the statement that every finite parity word determines one residue class: it compares **two occurrences on one actual ordinary orbit** and converts symbolic repetition into a physical height cost.

`T-6801` combines `(5)` with an upper bound on the number of factors that can remain inside a bounded logarithmic-surplus strip.

## 6. Gap audit

- The lemma does not say that every parity factor repeats.
- Dyadic separation alone does not bound the orbit above.
- The no-repeat corollary uses all-time coefficient supercriticality; general Collatz orbits may repeat only by entering a cycle.
- No claim about an arbitrary binary completion or a free symbolic path is made.
- No proof of Collatz follows from this lemma alone.
