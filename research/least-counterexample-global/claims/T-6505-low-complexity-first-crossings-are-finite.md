# T-6505 — Bounded-surplus linear-complexity first crossings are finite

**Claim ID:** `T-6505`  
**Title:** No acyclic ordinary first-crossing family can remain in a bounded surplus strip with uniformly linear factor complexity at unbounded lengths  
**Status:** **PROPOSED / SOURCE-QUALIFIED**  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #78  
**Dependencies:** `L-6502`; branch-qualified PR #81 `L-6801/L-6802`; Baker's lower bound for nonzero linear forms in `log 2, log 3`  
**Scope:** acyclic positive ordinary first-coefficient-crossing segments

## 1. Source-qualified logarithmic lower bound

Because `2` and `3` are multiplicatively independent algebraic numbers, Baker's theorem on linear forms in logarithms gives effectively computable constants

\[
c_0>0,
\qquad
\mu>0,
\]

such that every nonzero form

\[
\Lambda=j\log2-q\log3,
\qquad
j\ge1,
\quad0\le q\le j,
\]

satisfies

\[
\boxed{|\Lambda|\ge c_0j^{-\mu}.}
\tag{1}
\]

No particular numerical value of `c_0` or `mu` is needed for the finiteness theorem below. Independent source reconstruction is required before status promotion.

## 2. The family to be excluded

Fix constants

\[
B\ge0,
\qquad
C\ge1.
\]

Consider a positive ordinary shortcut-Collatz segment

\[
x_t=T^t(n)
\qquad(0\le t\le j)
\]

whose first `j` parity bits form a first coefficient-crossing word. Thus

\[
D_t=q_t-{\log2\over\log3}t\ge0
\quad(0\le t<j),
\qquad
D_j<0.
\tag{2}
\]

Assume additionally:

1. the proper-prefix surplus is uniformly bounded,
   \[
   \boxed{D_t\le B\quad(0\le t<j);}
   \tag{3}
   \]
2. the physical states `x_0,...,x_(j-1)` are pairwise distinct;
3. for
   \[
   L=\left\lfloor{j-C-2\over3}\right\rfloor,
   \tag{4}
   \]
   whenever `L>=1`, the number of distinct length-`L` parity factors beginning before the crossing satisfies
   \[
   \boxed{p_{j-1}(L)\le L+C.}
   \tag{5}
   \]
4. the endpoint does not descend:
   \[
   x_j\ge n.
   \tag{6}
   \]

Then `j` is bounded above by an effectively computable constant depending only on `B,C,c_0,mu`.

Equivalently:

\[
\boxed{
\text{there are no arbitrarily long acyclic ordinary no-descent first crossings satisfying `(3)--(5)`.}}
\tag{7}
\]

## 3. Exponential ordinary-height lower bound

Apply branch-qualified PR #81 `L-6802` with horizon `N=j-1`.

The choice `(4)` makes

\[
j-L>L+C
\]

for every sufficiently large `j`, so one length-`L` factor occurs at least twice. Dyadic factor separation and the bounded strip `(2)--(3)` give

\[
\boxed{
n
\ge
3^{-B}(2^L+1)-{j-1\over2}.}
\tag{8}
\]

Since `L=j/3+O_C(1)`, the right side grows exponentially in `j`.

This lower bound is on the **same ordinary initial integer** that realizes the crossing word.

## 4. Polynomial no-descent upper bound

Write

\[
q=q_j,
\qquad
\lambda=j\log2-q\log3>0,
\qquad
C_j=e^{-\lambda}.
\]

The final crossing step is even. The exact affine remainder therefore satisfies

\[
0<E_j<{q\over2}<{j\over2}.
\tag{9}
\]

No descent `(6)` gives

\[
n(1-C_j)\le E_j.
\tag{10}
\]

Because this is the first crossing,

\[
0<\lambda<\log2.
\]

On that interval,

\[
1-e^{-\lambda}\ge{\lambda\over2}.
\tag{11}
\]

Combining `(9)--(11)` with the Baker lower bound `(1)`,

\[
\boxed{
n
<{j\over\lambda}
\le c_0^{-1}j^{\mu+1}.}
\tag{12}
\]

Thus every no-descent start in this class is bounded polynomially in the crossing length.

## 5. Exponential versus polynomial contradiction

The lower bound `(8)` grows as

\[
3^{-B}2^{j/3+O_C(1)},
\]

whereas `(12)` grows at most as `c_0^(-1)j^(mu+1)`. Therefore the two inequalities are incompatible for all sufficiently large `j`.

This proves `(7)`.

## 6. Mechanical and Sturmian corollary

For the upper mechanical first-crossing word used as the remainder extremizer in PR #76:

\[
D_t=\lceil\alpha t\rceil-\alpha t
\in(0,1)
\qquad(0<t<j),
\]

so one may take `B=1`.

Its factors lie in one Sturmian language, whose factor complexity is exactly

\[
p(L)=L+1.
\]

Thus `C=1` is valid. Consequently:

\[
\boxed{
\text{the upper-mechanical extremizer cannot be an acyclic ordinary no-descent first-crossing prefix at arbitrarily large lengths}.}
\tag{13}
\]

This directly complements PR #79 `R-6601`. The symbolic mechanical threshold may grow quadratically and defeat a fixed verification floor, but the same word cannot be realized by one ordinary least-counterexample segment cofinally: dyadic repetition forces an exponential starting height, while Baker and no descent permit only polynomial height.

## 7. Strategic consequence

The cofinal delayed-crossing route cannot be saturated by a bounded-surplus low-complexity extremizer. A surviving late first-crossing word must do at least one of:

```text
carry unbounded proper-prefix coefficient surplus;
have factor complexity exceeding every fixed L+C corridor at the linear scales used above;
contain a repeated physical state, hence a positive cycle;
or fail ordinary no descent.
```

This removes an infinite Lane-B certificate class, not a bounded set of Farey cells.

## 8. Gap audit

- The theorem does not cover high-complexity first-crossing words.
- It does not cover families whose proper-prefix surplus bound `B` grows with `j` fast enough to erase the exponential lower bound.
- A repeated state is handed to the positive-cycle lane; no whole-denominator cycle exclusion is proved here.
- The constants from Baker's theorem are not instantiated numerically.
- PR #81 `L-6802` is a branch-qualified dependency and requires independent reconstruction.
- The result does not close Lane B in full and does not prove Collatz.
