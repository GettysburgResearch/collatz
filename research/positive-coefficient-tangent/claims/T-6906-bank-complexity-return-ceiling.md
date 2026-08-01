# T-6906 — a first-crossing failure has an explicit bank--complexity return ceiling

**Claim ID:** `T-6906`  
**Status:** **PROPOSED / SOURCE-DEPENDENT**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** `L-6904`; an effective Baker lower bound for nonzero linear forms in `log 2` and `log 3`  
**Scope:** acyclic positive ordinary no-descent first coefficient crossings

## Setup

Let `w` be a first-crossing word of length `j`, realized by a positive ordinary start `n`, and assume

\[
T^j(n)\ge n.
\tag{1}
\]

For proper prefixes put

\[
D_t=q_t-\alpha t,
\qquad
B=\max_{0\le t<j}D_t,
\qquad
\alpha=\frac{\log2}{\log3}.
\]

Assume the physical states

\[
n,T(n),\ldots,T^{j-1}(n)
\]

are pairwise distinct.

Let `p_w(L)` be the number of distinct length-`L` factors occurring in `w`.

Use an effective logarithmic-form lower bound

\[
\lambda=j\log2-q_j\log3
\ge c_0j^{-\mu}
\tag{2}
\]

with fixed effective constants `c_0,mu>0`.

## Exact return ceiling

If one length-`L` parity factor occurs at two distinct positions before the crossing, then

\[
\boxed{
2^L+1
\le
3^B\left(c_0^{-1}j^{\mu+1}+\frac j2\right).}
\tag{3}
\]

Equivalently, every repeated factor has length at most

\[
\boxed{
R(j,B)=
B\log_2 3
+
\log_2\left(c_0^{-1}j^{\mu+1}+\frac j2\right).}
\tag{4}
\]

Therefore, for every integer `L` with

\[
R(j,B)<L<j,
\]

all `j-L+1` occurrences are distinct and

\[
\boxed{p_w(L)=j-L+1.}
\tag{5}
\]

## Proof

Suppose equal length-`L` factors begin at times `a<b`. Exact affine subtraction for the common word gives

\[
2^L\mid T^a(n)-T^b(n).
\]

Acyclicity makes the difference nonzero, hence

\[
|T^a(n)-T^b(n)|\ge2^L.
\tag{6}
\]

For every proper prefix, the exact affine formula is

\[
T^t(n)
=3^{D_t}n
+
\frac12\sum_{m=1}^t v_{m-1}3^{D_t-D_m}.
\]

Since `0<=D_m` and `D_t<=B`,

\[
T^t(n)
\le
3^B\left(n+\frac j2\right).
\tag{7}
\]

The two positive states in `(6)` are both bounded by `(7)`, so

\[
2^L+1
\le
3^B\left(n+\frac j2\right).
\tag{8}
\]

At the first crossing, the final bit is even and every odd affine contribution is below `1/2`. Thus the endpoint remainder is less than `j/2`. Combining no descent `(1)` with `0<lambda<log2` gives

\[
n<\frac j\lambda.
\]

Using `(2)`,

\[
\boxed{n<c_0^{-1}j^{\mu+1}.}
\tag{9}
\]

Substitution of `(9)` into `(8)` proves `(3)--(4)`.

If `L>R(j,B)`, repetition would contradict `(3)`. Hence every starting position has a distinct length-`L` factor, proving `(5)`. ∎

## General exclusion criterion

Any proposed unbounded failure family is impossible if, for all sufficiently large members, there is an integer `L` satisfying

\[
\boxed{
R(j,B)<L<j
\quad\text{and}\quad
p_w(L)<j-L+1.}
\tag{10}
\]

This is an exact bank--complexity interface. It asks only whether the language forces a repeated factor beyond the maximum length allowed by ordinary height and Baker.

## Polynomial-complexity corollary

Fix `d>=1` and `C>0`. Suppose an unbounded family satisfies

\[
p_w(L)\le C(1+L)^d
\qquad(1\le L<j),
\tag{11}
\]

uniformly, and

\[
\boxed{B=o(j^{1/d}).}
\tag{12}
\]

Then the family is impossible.

Indeed, `(4)` gives

\[
R(j,B)=o(j^{1/d}).
\]

Take `L=ceil(R(j,B)+1)`. Then `L=o(j)`, while `(11)` gives

\[
p_w(L)=o(j)<j-L+1,
\]

contradicting `(10)`.

### Linear-complexity specialization

For every uniformly linear-complexity family

\[
p_w(L)\le C(1+L),
\]

one obtains the strong conclusion

\[
\boxed{B\not=o(j).}
\tag{13}
\]

Thus a cofinal acyclic ordinary no-descent family inside a Sturmian, automatic, fixed-substitution, or other verified linear-complexity language must carry a **linear** proper-prefix coefficient bank.

This strictly strengthens PR #80 `T-6505`, which assumed a fixed bounded bank and the special corridor `p(L)<=L+C`.

## Relationship to `T-6904`

- `T-6904` handles arbitrary uniformly subexponential complexity when `B=O(log j)`.
- `T-6906` handles much larger banks when the language has a quantitative polynomial complexity bound.

Together they remove a broad low-complexity region of Box 2:

```text
zero entropy with logarithmic bank;
polynomial complexity degree d with bank o(j^(1/d));
linear complexity with every sublinear bank.
```

## Gap audit

- Positive-entropy languages remain open.
- A linear-complexity failure with a genuinely linear bank remains open.
- Repeated physical states are transferred to the positive-cycle lane rather than excluded.
- The constants `c_0,mu` require primary-source review.
- The theorem does not control the canonical residue for high-complexity, high-bank words.
