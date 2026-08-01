# L-6808 — Bank area and individual-shift geometry around the mechanical extremizer

**Claim ID:** `L-6808`  
**Status:** **PROPOSED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** elementary binary-word geometry; `L-6601/T-6605` notation  
**Scope:** arbitrary coefficient-first-crossing words relative to their upper-mechanical extremizer

## 1. Prefix-excess path

Fix a first-crossing length \(j\) and weight \(q\).  Let \(w\) be the
upper-mechanical word and \(v\) any admissible word of the same length and
weight.

For \(0\le m\le j-1\), define

\[
e_m=S_m(v)-S_m(w).
\tag{1}
\]

Prefix admissibility gives

\[
e_m\in\mathbf Z_{\ge0},
\qquad
e_0=e_{j-1}=0.
\tag{2}
\]

Both words are binary, hence

\[
|e_{m+1}-e_m|\le1.
\tag{3}
\]

Let

\[
H=\max_{m<j}e_m.
\tag{4}
\]

## 2. Swap area identity

Write the odd positions as

\[
d_1(v)<\cdots<d_q(v),
\qquad
d_1(w)<\cdots<d_q(w),
\]

and put

\[
h_i=d_i(w)-d_i(v)\ge0.
\]

The exact adjacent-swap distance of `T-6605` is

\[
I(v)=\sum_{i=1}^q h_i.
\tag{5}
\]

For each \(i\), the displaced one contributes one unit to \(e_m\) precisely
for

\[
d_i(v)<m\le d_i(w).
\]

Summing the indicators in either order gives the exact area identity

\[
\boxed{
I(v)=\sum_{m=1}^{j-2}e_m.
}
\tag{6}
\]

## 3. Height costs square area

A nonnegative integer path that begins and ends at zero, has step size at most
one, and reaches height \(H\), has area at least

\[
1+2+\cdots+H+(H-1)+\cdots+1=H^2.
\]

Therefore

\[
\boxed{I(v)\ge H^2.}
\tag{7}
\]

Let

\[
B(v)=\max_{m<j}\bigl(S_m(v)-\alpha m\bigr),
\qquad
\alpha=\frac{\log2}{\log3}.
\]

Since

\[
S_m(w)-\alpha m
=
\lceil\alpha m\rceil-\alpha m
\in(0,1)
\]

at every nonzero proper prefix,

\[
\boxed{
B(v)<H+1\le\sqrt{I(v)}+1.
}
\tag{8}
\]

This strengthens the earlier linear estimate \(B<I+1\).

## 4. Displaced-support bound

Let

\[
R(v)=\#\{i:h_i>0\}.
\tag{9}
\]

At any cut, each excess one comes from a different displaced odd position.
Hence

\[
\boxed{H\le R(v).}
\tag{10}
\]

Now assume the canonical representative of \(v\) does not descend.  Put

\[
C=\frac{3^q}{2^j},
\qquad
E(u)=\frac{A_u}{2^j}.
\]

The exact displacement numerator of `L-6601` gives

\[
E(w)-E(v)
=
C\sum_{i:h_i>0}
\frac{2^{d_i(v)}}{3^i}(2^{h_i}-1).
\tag{11}
\]

At the source position of the \(i\)-th odd bit,

\[
0\le (i-1)-\alpha d_i(v)\le B(v),
\]

so

\[
\frac{2^{d_i(v)}}{3^i}
\ge
3^{-B(v)-1}.
\tag{12}
\]

The no-descent assumption implies \(E(v)>0\), while every first-crossing
mechanical remainder satisfies \(E(w)<j/2\).  Also \(C\ge1/2\).
Equations `(11)--(12)` therefore give, for every displaced odd position,

\[
\boxed{
2^{h_i}-1<j\,3^{B(v)+1}.
}
\tag{13}
\]

Consequently,

\[
\boxed{
h_i
<
1+\log_2j+(B(v)+1)\log_2 3.
}
\tag{14}
\]

Summing over the support,

\[
\boxed{
I(v)
<
R(v)\left[
1+\log_2j+(B(v)+1)\log_2 3
\right].
}
\tag{15}
\]

Using `(8)` and `(10)` gives the support-only ceiling

\[
\boxed{
I(v)
<
R(v)\left[
1+\log_2j+(R(v)+2)\log_2 3
\right].
}
\tag{16}
\]

## 5. Meaning

A target failure cannot hide arbitrary integrated displacement in one
uncontrolled odd position:

- a large prefix bank costs quadratic swap area;
- the bank height requires at least as many displaced odd positions;
- no descent caps every individual shift logarithmically in \(j\) and
  exponentially only in the bank.

These elementary facts combine with the return/gap uncertainty theorem to
force growing displacement and growing support.

## 6. Gap audit

- `(13)--(16)` assume canonical no descent.
- The estimates are deliberately coarse; they retain only positivity of
  \(E(v)\).
- Large-bank, growing-support words remain possible.
- No distribution statement modulo the complete denominator is proved.
- No CST or Collatz conclusion follows from this lemma alone.
