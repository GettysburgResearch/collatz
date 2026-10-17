# Carry-chain endpoint audit for `L-9310`

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Purpose:** isolate the combinatorial indexing behind `L-9310(20)`  
**Status:** proof audit; no new claim ID

## 1. Carry word and zero runs

The phase chain has indices

\[
0,1,\ldots,K-1.
\]

The carry word has indices

\[
0,1,\ldots,K-2.
\]

Suppose exactly `W` carries are nonzero, at positions

\[
p_1<p_2<\cdots<p_W.
\]

Define the `W+1` zero-run lengths from left to right:

\[
r_0=p_1,
\]

\[
r_i=p_{i+1}-p_i-1
\qquad(1\le i<W),
\]

and

\[
r_W=K-2-p_W.
\]

If `W=0`, there is one zero run of length

\[
r_0=K-1.
\]

In all cases,

\[
\sum_{i=0}^{W}r_i+W=K-1.
\tag{1}
\]

## 2. Terminal phase lengths

For each zero run, let `t_i` be the number appearing in the zero-run theorem:

\[
t_i=K-\ell_i-r_i,
\]

where `ell_i` is the first carry index of the run.

For the final run,

\[
\ell_W=p_W+1,
\qquad
r_W=K-2-p_W,
\]

so

\[
\boxed{t_W=1.}
\tag{2}
\]

For `0<=i<W`, the run `r_i` is followed by one nonzero carry and then the run `r_(i+1)`. Therefore

\[
\boxed{
t_i=t_{i+1}+r_{i+1}+1.
}
\tag{3}
\]

This is the endpoint convention used in `L-9310(18)`.

## 3. Insert the zero-run bound

Write

\[
\kappa=\kappa_{M,N},
\qquad
C=C_h,
\qquad
A=1+\kappa,
\qquad
D=C+1.
\]

Every run satisfies

\[
r_i\le\kappa t_i+C.
\tag{4}
\]

For `0<=i<W`, equations `(3)` and `(4)` applied to `r_(i+1)` give

\[
\begin{aligned}
t_i
&=t_{i+1}+r_{i+1}+1\\
&\le
(1+\kappa)t_{i+1}+C+1\\
&=At_{i+1}+D.
\end{aligned}
\tag{5}
\]

Starting from `t_W=1`, iteration gives

\[
\begin{aligned}
t_0
&\le
A^W+D(1+A+\cdots+A^{W-1})\\
&=
A^W+D\frac{A^W-1}{A-1}\\
&=
A^W+D\frac{A^W-1}{\kappa}.
\end{aligned}
\tag{6}
\]

## 4. Initial run and total depth

The initial zero run starts at carry index `0`. Its terminal parameter is `t_0`, and

\[
K=r_0+t_0.
\tag{7}
\]

Using `(4)`,

\[
K
\le
At_0+C
\le
At_0+D.
\tag{8}
\]

Substitute `(6)`:

\[
\begin{aligned}
K
&\le
A^{W+1}
+D\left[
A\frac{A^W-1}{\kappa}+1
\right]\\
&=
A^{W+1}
+D\frac{A^{W+1}-1}{\kappa}.
\end{aligned}
\tag{9}
\]

The final equality uses

\[
A-\kappa=1.
\]

Put

\[
B=1+\frac{D}{\kappa}
=1+\frac{C+1}{\kappa}.
\]

Then `(9)` gives

\[
\boxed{
K
\le
B A^{W+1}.
}
\tag{10}
\]

This is `L-9310(20)`.

## 5. Edge case `W=0`

If every carry vanishes, then the one zero run has length

\[
r_0=K-1
\]

and terminal parameter `t_0=1`.

Equation `(4)` gives directly

\[
K-1
\le
\kappa+C,
\]

or

\[
K\le A+C.
\tag{11}
\]

The general bound `(10)` becomes

\[
K\le BA.
\]

Since

\[
BA
=
A+
(C+1)A/\kappa
\ge
A+C,
\]

it includes `(11)`.

## 6. Inversion

Because `A>1` and `B>0`, equation `(10)` implies

\[
W
\ge
\frac{\log(K/B)}{\log A}-1.
\]

Since `W>=0`, the uniform form is

\[
\boxed{
W
\ge
\left(
\frac{\log(K/B)}{\log A}-1
\right)_+.
}
\tag{12}
\]

Combining `(12)` with the integer carry-energy inequality yields `L-9310(22)`.

## 7. Audit conclusion

The right-to-left recurrence, final value `t_W=1`, initial-run conversion `K=r_0+t_0`, and `W=0` edge case are mutually consistent. No asymptotic approximation is used in the chaining step.