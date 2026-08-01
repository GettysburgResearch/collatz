# T-6806 — The upper-mechanical first-crossing family is completely closed, modulo the positive-cycle alternative

**Claim ID:** `T-6806`  
**Status:** **PROPOSED / SOURCE-QUALIFIED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6801`, `L-6802`, `L-6803`; the Rhin lower bound quoted in `L-6604`; exact certificate `X-6801`  
**Scope:** upper-mechanical coefficient-first-crossing words at every length  
**Counterexample status:** none

## 1. Statement

Put

\[
\alpha=\frac{\log 2}{\log 3}.
\]

For every integer \(j\ge2\), let

\[
q=\left\lceil\alpha(j-1)\right\rceil.
\]

When

\[
3^q<2^j,
\tag{1}
\]

define the upper-mechanical first-crossing word \(w_j\) by

\[
S_m(w_j)=\lceil\alpha m\rceil
\qquad(0\le m<j),
\tag{2}
\]

and append a final zero at time \(j-1\).  Thus \(w_j\) has length \(j\),
weight \(q\), every proper coefficient is at least one, and its complete
coefficient is below one.

Let

\[
(r_j,s_j)
\]

be its canonical start--end pair from `L-6803`.

Then:

\[
\boxed{
j=2
\quad\Longrightarrow\quad
w_j=10,\quad r_j=s_j=1,
}
\tag{3}
\]

and, for every valid \(j>2\),

\[
\boxed{
s_j<r_j
\quad\text{or the canonical segment contains a nontrivial positive cycle.}
}
\tag{4}
\]

Consequently, subject to exclusion of nontrivial positive cycles,

\[
\boxed{
\text{every nontrivial upper-mechanical first crossing descends at its canonical source.}
}
\tag{5}
\]

The exact finite portion \(j<373\) has no cycle alternative: `X-6801`
directly reconstructs \(r_j,s_j\) and proves \(s_j<r_j\) for every valid
\(j>2\).

## 2. Proper-prefix bank and factor complexity

For \(m<j\), put

\[
D_m=S_m-\alpha m.
\]

Irrationality of \(\alpha\) and `(2)` give

\[
0<D_m<1.
\tag{6}
\]

Thus the proper-prefix bank satisfies

\[
B_j:=\max_{m<j}D_m<1.
\tag{7}
\]

The word in `(2)` is a factor of the characteristic Sturmian language of
slope \(\alpha\), apart from the forced final zero.  Every collection of
proper length-\(L\) factors therefore has cardinality at most

\[
p_j(L)\le L+1.
\tag{8}
\]

Choose

\[
L_j=\left\lfloor\frac{j-1}{3}\right\rfloor.
\tag{9}
\]

For \(j\ge4\),

\[
j-L_j>L_j+1.
\tag{10}
\]

Hence two proper starts have the same length-\(L_j\) parity factor.

If the corresponding physical states coincide, the canonical segment
contains a positive cycle.  In the acyclic case they are distinct, and
`L-6801/L-6802` give

\[
r_j
>
\frac{2^{L_j}+1}{3}-\frac{j-1}{2}.
\tag{11}
\]

The strict factor \(1/3\) follows from \(3^{-B_j}>1/3\).

## 3. No-descent ceiling

Put

\[
\lambda_j=j\log2-q\log3>0.
\tag{12}
\]

If the canonical endpoint does not descend, `L-6603` gives

\[
r_j<\frac{q}{3\lambda_j}<\frac{j}{\lambda_j}.
\tag{13}
\]

The exact source input quoted by Rozier--Terracol and recorded in PR #82
`L-6604` is the specialization of Rhin's theorem

\[
\boxed{\lambda_j\ge j^{-13.3}.}
\tag{14}
\]

The primary-source normalization remains an explicit review obligation.
Combining `(13)` and `(14)`,

\[
\boxed{r_j<j^{14.3}.}
\tag{15}
\]

## 4. Exact analytic cutoff

Define the integer

\[
H_j
=
2(2^{L_j}+1)-3(j-1),
\tag{16}
\]

so that the right side of `(11)` is \(H_j/6\).

`X-6801` proves with integer arithmetic that, for

\[
j=373,374,375,
\]

one has

\[
\boxed{H_j^{10}>6^{10}j^{143}}
\tag{17}
\]

and

\[
\boxed{(j+3)^{143}<2^{10}j^{143}.}
\tag{18}
\]

For every \(j\ge5\),

\[
L_{j+3}=L_j+1
\]

and

\[
H_{j+3}-2H_j=3j-14>0.
\tag{19}
\]

Therefore, separately in each residue class modulo three, `(17)--(19)`
inductively imply

\[
\boxed{\frac{H_j}{6}>j^{143/10}}
\qquad(j\ge373).
\tag{20}
\]

Equations `(11)`, `(15)`, and `(20)` are incompatible.  Thus every valid
acyclic mechanical word of length at least \(373\) descends.

## 5. Exact finite range

`X-6801` independently reconstructs all valid lengths

\[
2\le j<373.
\]

There are exactly \(234\) such rows.  The only nonpositive descent defect is

```text
j=2, q=1, word=10, root=1, endpoint=1.
```

Every valid \(j>2\) has

\[
r_j-s_j>0.
\]

The generator uses modular inversion; the independent verifier uses
one-bit canonical-pair lifting and imports no generator module.

Frozen semantic digest:

```text
5d88f47548ca6716b7c10cf839dc7d65eb6efdff748b35cca9d709aa36771d2e
```

## 6. Global consequence for Box 2

PR #82 `T-6607` proves that, once the mechanical representative descends,
every **no-wrap** nonmechanical word of the same \((j,q)\) descends with a
strictly larger integer defect.

Combining that theorem with `T-6806` gives the source-qualified reduction

\[
\boxed{
\begin{array}{c}
\text{every nontrivial canonical Box-2 failure}\\
\text{either contains a positive cycle}\\
\text{or is a nonmechanical modulus wrap.}
\end{array}}
\tag{21}
\]

Thus the maximum-remainder extremizer and the complete no-wrap sector are
closed at every length.  The surviving acyclic problem is exactly the short
full-denominator wrap window of PR #82 `L-6602/T-6609`.

## 7. Why this is genuine but not Collatz

The theorem closes an infinite, cofinal family at all lengths and discharges
the mechanical premise in the wrap-only classification.  It is not a finite
Farey-cell exclusion.

It does not prove:

- absence of nontrivial positive cycles;
- avoidance of every wrapped displacement numerator;
- the full coefficient-stopping-time conjecture;
- Box 1;
- the Collatz conjecture.

## 8. Review targets

1. audit the quoted Rhin exponent and normalization against the primary source;
2. reconstruct the Sturmian factor-complexity bound with the forced final zero excluded from the factor starts;
3. verify `(11)` from `L-6802`, including the acyclic alternative;
4. replay `X-6801` independently;
5. check the three-class induction `(17)--(20)`;
6. preserve the positive-cycle alternative in `(4)`.
