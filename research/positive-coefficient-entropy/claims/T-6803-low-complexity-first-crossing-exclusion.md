# T-6803 — Low-complexity first-crossing families are eventually nonparadoxical

**Claim ID:** `T-6803`  
**Status:** **PROPOSED / SOURCE-QUALIFIED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6802`, `L-6803`; a standard effective lower bound for the nonzero linear form `j log 2-q log 3`  
**Scope:** coefficient-first-crossing words with controlled proper-prefix surplus and repeated-factor complexity

## 1. Setup

Let

\[
w=(v_0,\ldots,v_{j-1})
\]

be coefficient-first-crossing:

\[
3^{q_m}\ge2^m
\quad(1\le m<j),
\qquad
3^q<2^j,
\tag{1}
\]

where `q_m` is the number of ones in the first `m` bits and `q=q_j`.

Write

\[
T_w(x)=\frac{3^q x+A_w}{2^j},
\]

and let `(r_w,s_w)` be the canonical start–end pair from `L-6803`.

Put

\[
\alpha=\frac{\log2}{\log3},
\qquad
D_m=q_m-\alpha m,
\]

and define the proper-prefix surplus height

\[
B_w=\max_{0\le m<j}D_m.
\tag{2}
\]

By `(1)`,

\[
0\le D_m\le B_w
\qquad(0\le m<j).
\tag{3}
\]

Let `p_w(L)` be the number of distinct length-`L` factors beginning in the proper prefix

\[
v_0\cdots v_{j-2}.
\]

Thus there are `j-L` starting positions, and put

\[
M_w(L)=
\left\lceil
\frac{j-L}{p_w(L)}
\right\rceil.
\tag{4}
\]

## 2. Exact finite exclusion gate

Assume the canonical orbit segment

\[
r_w,T(r_w),\ldots,T^{j-1}(r_w)
\]

has no repeated state. Then `L-6802`, applied at horizon `j-1`, gives

\[
\boxed{
r_w
\ge
H_w(L):=
3^{-B_w}
\bigl((M_w(L)-1)2^L+1\bigr)
-\frac{j-1}{2}.}
\tag{5}
\]

Define

\[
\lambda_w=j\log2-q\log3>0.
\tag{6}
\]

The exact affine numerator expansion gives

\[
\frac{A_w}{3^q}
=
\sum_{m=1}^{j}
 v_{m-1}\frac{2^{m-1}}{3^{q_m}}.
\tag{7}
\]

Every nonzero summand is at most `1/2` by the proper-prefix barrier; for the final bit, first crossing forces `v_{j-1}=0`. Hence

\[
\frac{A_w}{3^q}\le\frac q2,
\]

and because `3^q/2^j=e^{-\lambda_w}<1`,

\[
\frac{A_w}{2^j}
\le
\frac q2e^{-\lambda_w}
<\frac j2.
\tag{8}
\]

Therefore

\[
\boxed{
\frac{A_w}{2^j-3^q}
<
\frac{j}{2(1-e^{-\lambda_w})}.}
\tag{9}
\]

Combining `(5)`, `(9)`, and `L-6803` proves the exact finite implication

\[
\boxed{
H_w(L)>
\frac{j}{2(1-e^{-\lambda_w})}
\quad\Longrightarrow\quad
s_w<r_w.}
\tag{10}
\]

Thus `(10)` certifies that the canonical member descends at the first coefficient crossing.

If a state repeats instead, the canonical orbit has entered a positive periodic orbit. The theorem does not silently discard that alternative: it is a finite positive-cycle obstruction requiring the separate full-denominator cycle program.

## 3. Effective polynomial ceiling for the no-descent threshold

A standard theorem on linear forms in logarithms gives effectively computable constants

\[
c_0>0,
\qquad
C_0>0,
\]

depending only on `2` and `3`, such that for integers `j>=2` and `0<=q<=j`,

\[
0<|j\log2-q\log3|
\quad\Longrightarrow\quad
|j\log2-q\log3|
\ge c_0j^{-C_0}.
\tag{11}
\]

This is the only external source input. Any audited Baker–Wüstholz, Matveev, or sharper two-logarithm specialization suffices.

For `0<\lambda<=1`,

\[
1-e^{-\lambda}\ge\lambda/2.
\]

For `\lambda>1`, the denominator is bounded below by `1-e^{-1}`. Hence `(9)` and `(11)` give an effective polynomial bound

\[
\boxed{
\frac{A_w}{2^j-3^q}
\le C_1j^{C_0+1}}
\tag{12}
\]

for one effective constant `C_1`.

The possible no-descent height grows only polynomially with the word length.

## 4. Asymptotic low-complexity theorem

Consider a sequence of coefficient-first-crossing words `w_j` with lengths tending to infinity. Suppose there are integers `L_j` such that

\[
L_j\to\infty,
\qquad
\frac{L_j}{\log j}\to\infty,
\tag{13}
\]

\[
M_{w_j}(L_j)\ge2,
\tag{14}
\]

and

\[
B_{w_j}=o(L_j).
\tag{15}
\]

Then `(5)` gives

\[
H_{w_j}(L_j)
\ge
\exp\bigl((\log2-o(1))L_j\bigr)-O(j),
\tag{16}
\]

which dominates every fixed polynomial in `j` by `(13)`. Combining `(12)` and `(16)` yields:

\[
\boxed{
\text{for all sufficiently large }j,
\quad
s_{w_j}<r_{w_j},}
\tag{17}
\]

unless the canonical orbit has already entered a positive cycle.

Therefore no aperiodic low-complexity family satisfying `(13)`–`(15)` can supply infinitely many CST counterexamples.

## 5. Mechanical and Sturmian specialization

For the upper mechanical first-crossing word of slope

\[
\alpha=\frac{\log2}{\log3},
\]

the proper-prefix counts are

\[
q_m=\lceil\alpha m\rceil,
\]

so

\[
0<D_m<1
\qquad(m<j),
\]

and hence

\[
B_w<1.
\tag{18}
\]

Its factors lie in one Sturmian language, so

\[
p_w(L)\le L+1.
\tag{19}
\]

Choose

\[
L=\left\lfloor\frac{j-2}{3}\right\rfloor.
\]

For all sufficiently large `j`, equations `(4)` and `(19)` give `M_w(L)>=2`; equations `(13)`–`(15)` hold. Consequently:

\[
\boxed{
\text{every sufficiently long upper-mechanical first-crossing word}
\text{ has }s_w<r_w,
}
\tag{20}
\]

unless its canonical realization enters a positive cycle.

The same conclusion applies to any family contained in a fixed linear-complexity language with bounded proper-prefix surplus.

## 6. Why this advances the PR #76 lane

PR #76 uses the upper mechanical word as the maximum-remainder extremizer and excludes the first forced Farey candidate by a directed Denjoy–Koksma bound.

`T-6803` adds a complementary all-length conclusion:

```text
exactly mechanical / bounded-surplus low-complexity families
    -> canonical source grows exponentially;

coefficient denominator gap
    -> no-descent threshold grows only polynomially;

therefore
    -> only finitely many such first-crossing words can be paradoxical.
```

The remaining finite-crossing problem is a stability theorem: show that any word retaining enough remainder to avoid descent must remain in a complexity class to which this theorem applies.

## 7. Gap audit

- The theorem does not cover arbitrary high-complexity first-crossing words.
- The constants in `(11)` must be imported from and checked against one exact primary linear-forms theorem before a numerical cutoff is claimed.
- The repeated-state alternative is a positive-cycle obstruction, not automatically impossible.
- `p_w(L)` must be a certified factor-complexity bound for the actual finite word or its containing language.
- No proof of CST or Collatz is claimed.

## 8. Review targets

1. verify the numerator bound `(7)`–`(9)`, especially the final even bit;
2. reconstruct the `L-6802` horizon and factor-position count;
3. audit the exact linear-forms input `(11)`;
4. check the asymptotic comparison `(13)`–`(16)`;
5. preserve the positive-cycle alternative;
6. verify the mechanical/Sturmian complexity specialization.