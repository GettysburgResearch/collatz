# Exact rational controls for the missing compactness

**Status: proved elementary operator examples and finite exact replay.
These are comparison operators, not alternative Collatz maps or
counterexamples to Collatz.**

The operator note proves that the canonical backwards Collatz operator
\(P\) is weakly stable and that

\[
P^n(P^*)^n-I\text{ is compact},\qquad
\|P^n\|_{\mathrm{ess}}=\|P^n\|=1
\]

for every finite \(n\). Each nonzero vector loses norm strictly in one
step. These facts are compatible both with a zero and with a nonzero
strong asymptotic limit
\(A=\operatorname{s-lim}(P^*)^nP^n\). The following exact rational
examples demonstrate this distinction without floating matrices.

## 1. Two explicit weighted shifts

On \(\ell^2(\mathbb N_0)\), with orthonormal basis \(e_j\), set

\[
T_\pm e_j=w_j^\pm e_{j+1},
\qquad
w_j^-=\frac{j+1}{j+2},
\qquad
w_j^+=\frac{(j+1)(j+3)}{(j+2)^2}.
\tag{1}
\]

All coefficients are rational. Both weight sequences lie strictly
between zero and one and tend to one. For every finite \(n\),

\[
\begin{aligned}
\prod_{i=0}^{n-1}w_{j+i}^-
 &=\frac{j+1}{j+n+1},\\
\prod_{i=0}^{n-1}w_{j+i}^+
 &=\frac{(j+1)(j+n+2)}{(j+2)(j+n+1)}.
\end{aligned}
\tag{2}
\]

These identities follow by cancellation of consecutive numerator and
denominator factors. Empty products, for \(n=0\), equal one.

For either operator, a nonzero vector satisfies

\[
\|T_\pm f\|^2=\sum_j(w_j^\pm)^2|f_j|^2<\|f\|^2.
\tag{3}
\]

Moreover \(T_\pm^n f\) is supported on indices at least \(n\). Thus

\[
|\langle T_\pm^n f,g\rangle|
\le\|f\|\left(\sum_{j\ge n}|g_j|^2\right)^{1/2}\longrightarrow0.
\tag{4}
\]

Both operators are weakly stable.

For fixed \(n\), the diagonal of \(T_\pm^n(T_\pm^*)^n\) is zero at the
first \(n\) indices and is the square of a product of \(n\) consecutive
weights thereafter. That product tends to one as the index grows.
Consequently

\[
T_\pm^n(T_\pm^*)^n-I\text{ is compact}.
\tag{5}
\]

The vectors \(e_j\), as \(j\to\infty\), give
\(\|T_\pm^n e_j\|\to1\). Since compact operators send an orthonormal
sequence to zero in norm, both finite-time essential norms and ordinary
norms equal one.

## 2. Their asymptotic limits differ

The positive operator \((T_\pm^*)^nT_\pm^n\) is diagonal, with entries
given by the squares of (2). The entries are bounded by one, so
coordinatewise convergence implies strong convergence by summation
dominated convergence.

For the first example,

\[
\frac{j+1}{j+n+1}\longrightarrow0,
\qquad A_-=0.
\tag{6}
\]

For the second,

\[
\frac{(j+1)(j+n+2)}{(j+2)(j+n+1)}
\longrightarrow\frac{j+1}{j+2},
\]

and hence

\[
A_+e_j=\left(\frac{j+1}{j+2}\right)^2e_j.
\tag{7}
\]

The eigenvalues in (7) approach one, so \(A_+\) is noncompact and has
essential norm one. It has no eigenvalue equal to one. Therefore weak
stability, strict one-step norm loss, essential norm one at every
finite time, and the compact defects in (5) do not determine whether
the strong asymptotic limit vanishes.

## 3. Exact agreement on any prescribed finite prefix

Fix any finite rational list \(0<p_0,\ldots,p_{L-1}<1\). Use these as
the first \(L\) weights in both examples; after that use respectively
\(w_{j-L}^-\) and \(w_{j-L}^+\).

Every path using only the prescribed weights agrees exactly. In
particular all basis transitions and all products whose last used
weight index is below \(L\) agree. Given any finite collection of
matrix coefficients and finite iteration times, \(L\) can be chosen
large enough to cover all the weights those observations use.

Both extensions retain (3)–(5), weak stability, and finite-time
essential norm one. The first remains strongly stable. For the
second, the infinite product starting at \(j<L\) is

\[
\frac12\prod_{i=j}^{L-1}p_i>0,
\tag{8}
\]

and starting at \(j\ge L\) it is
\((j-L+1)/(j-L+2)\). Its asymptotic limit remains noncompact.

Thus finitely many exact coefficient observations, combined with
the common abstract properties above, do not resolve the missing
compactness. This does not rule out a finite arithmetic proof using
additional properties of the Collatz map.

## 4. Exact physical-tail witnesses for Collatz

This part checks an inequality for the actual integer inverse map.
It does not simulate the unknown harmonic trace. Write

\[
I_a(y)=\frac{2^ay-1}{3},\qquad a\ge1.
\]

Every legal inverse step satisfies

\[
I_a(y)\ge\frac23(y+1)-1.
\]

For any inverse word of length \(n\) from \(t\), every intermediate
state is at least

\[
L_n(t)=(2/3)^n(t+1)-1.
\]

If \(L_n(t)>0\), its reciprocal product therefore obeys

\[
\prod_{j=1}^n\frac{3x_j}{3x_j+1}
\ge\left(\frac{3L_n(t)}{3L_n(t)+1}\right)^n
\ge1-\frac{n}{3L_n(t)+1}.
\tag{9}
\]

The canonical backwards kernel is a probability distribution on
such words. Averaging (9) proves the same bound for the exact
diagonal coefficient \(d_n(t)\) of \(P^n(P^*)^n\).

For any finite cutoff \(M\), finite time \(n\), and rational
\(\epsilon>0\), choose a target \(t\) so that

\[
L_n(t)>
\max\left\{M,\frac{n}{3\epsilon}\right\}.
\]

One can choose \(t\) to be an arbitrarily large positive odd
integer not divisible by three. Then every inverse path stays
above \(M\), and \(d_n(t)>1-\epsilon\). These witnesses establish
the two exact tail-norm identities in the operator note.

The checker constructs such targets using rational powers and
integer ceilings. It then explores every legal unit inverse word
with exponents at most six through the specified finite depth.
Each unit target has exactly two such children: the three
exponents with the correct parity have distinct residues modulo
nine, and exactly one yields a child divisible by three.

This finite tree replay checks implementation and boundary cases.
The proof of (9) applies to every exponent, with no cap or finite
depth restriction.

## 5. Reproduction and scope

Run from this directory:

    python verify_operator_controls.py --output operator_controls_report.json

The program uses only integer arithmetic and the standard-library
Fraction type. It verifies:

- 4,160 telescoping product identities, including empty products;
- exact agreement on a shared finite prefix and identities across
  its boundary;
- explicit rational norm witnesses above multiple cutoffs and at
  multiple finite times;
- complete capped inverse trees for twelve arithmetic witnesses;
- rejection of a wrong telescoping endpoint, a changed shared
  prefix weight, and a reversed inverse-floor factor.

The program uses explicit checks, so Python optimization does not
disable verification. It does not numerically approximate \(H\),
compute \(A\) from finite matrices, certify all-time Collatz
behavior, or prove an infinite-limit claim by testing examples.
The infinite conclusions above are analytic consequences of the
exact formulas.

The operator mechanism belongs to established weighted-shift
theory; see the Gehér primary references in
ASYMPTOTIC_OPERATOR.md. These simple controls supply an exact
demonstration of the logical boundary of the proposed Collatz
operator approach.
