# T-6604 — long returns force a large coefficient bank at first crossing

**Claim ID:** `T-6604`  
**Status:** **PROPOSED / SOURCE-DEPENDENT**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** elementary shortcut-Collatz affine algebra; a standard effective Baker lower bound for the nonzero form `j log 2-q log 3`  
**Scope:** finite positive ordinary first-coefficient-crossing segments whose endpoint does not descend  

## 1. Statement

Let

\[
x_t=T^t(n),\qquad 0\le t\le j,
\]

be a positive ordinary shortcut-Collatz segment. Write

\[
q_t=\#\{0\le r<t:x_r\text{ is odd}\},
\qquad
\alpha={\log2\over\log3},
\qquad
D_t=q_t-\alpha t.
\]

Assume that `j` is the first coefficient crossing:

\[
D_t\ge0\quad(0\le t<j),
\qquad
D_j<0,
\tag{1}
\]

and that the endpoint does not descend:

\[
x_j\ge n.
\tag{2}
\]

Put

\[
B=\max_{0\le t<j}D_t.
\tag{3}
\]

Suppose the same parity factor of length `L>=1` occurs beginning at two distinct times

\[
0\le a<b\le j-L,
\tag{4}
\]

and suppose the two physical starting states are distinct:

\[
x_a\ne x_b.
\tag{5}
\]

There are effective absolute constants

\[
c_0>0,\qquad \mu>0,
\]

coming only from the two logarithms `log 2` and `log 3`, such that

\[
\boxed{
2^L+1
\le
3^B\left(c_0^{-1}j^{\mu+1}+{j\over2}\right).}
\tag{6}
\]

In particular,

\[
\boxed{
L
\le
B\log_2 3
 +(\mu+1)\log_2j
 +\log_2(c_0^{-1}+1/2).}
\tag{7}
\]

Thus a repeated long factor is impossible unless its dyadic length is paid for by coefficient-bank height or by the polynomial Baker allowance.

## 2. Dyadic separation of the repeated factor

Let the common length-`L` factor have weight `s` and affine numerator `A`. Starting from either occurrence,

\[
2^Lx_{a+L}=3^sx_a+A,
\qquad
2^Lx_{b+L}=3^sx_b+A.
\]

Subtracting gives

\[
2^L(x_{a+L}-x_{b+L})=3^s(x_a-x_b).
\]

Since `gcd(2^L,3^s)=1`,

\[
2^L\mid x_a-x_b.
\]

By `(5)`,

\[
|x_a-x_b|\ge2^L.
\tag{8}
\]

## 3. Upper height inside the coefficient corridor

For every `t<j`, the exact affine identity can be written

\[
x_t
=3^{D_t}n
 +{1\over2}\sum_{m=1}^{t}
 v_{m-1}3^{D_t-D_m},
\tag{9}
\]

where `v_r=x_r mod 2`.

By `(1)` and `(3)`, every exponent occurring in `(9)` is at most `B`. Therefore

\[
x_t\le3^B\left(n+{t\over2}\right)
\le3^B\left(n+{j\over2}\right)
\qquad(t<j).
\tag{10}
\]

The two positive integers in `(8)` both lie below the right side of `(10)`. Their difference is at least `2^L`, so their maximum is at least `2^L+1`. Hence

\[
2^L+1
\le3^B\left(n+{j\over2}\right).
\tag{11}
\]

This lower bound is placed on the same ordinary start `n` that appears in the no-descent inequality.

## 4. First crossing gives a polynomial upper bound for the start

Put

\[
q=q_j,
\qquad
\lambda=j\log2-q\log3>0.
\]

The final crossing step must be even. Therefore its exact affine formula is

\[
x_j=e^{-\lambda}n+E_j,
\]

with

\[
0<E_j<{q\over2}<{j\over2}.
\tag{12}
\]

Indeed, each odd-source contribution is

\[
{1\over2}3^{D_j-D_m}<{1\over2}
\]

because `D_j<0<=D_m` at every preceding odd endpoint.

From `(2)` and `(12)`,

\[
n(1-e^{-\lambda})<{j\over2}.
\tag{13}
\]

First crossing also gives `0<lambda<=log 2`, and on this interval

\[
1-e^{-\lambda}\ge{\lambda\over2}.
\]

Thus

\[
n<{j\over\lambda}.
\tag{14}
\]

A standard effective Baker theorem for two logarithms supplies constants `c_0,mu` such that every nonzero

\[
j\log2-q\log3
\]

with `0<=q<=j` satisfies

\[
\lambda\ge c_0j^{-\mu}.
\tag{15}
\]

Equations `(14)--(15)` yield

\[
\boxed{n<c_0^{-1}j^{\mu+1}.}
\tag{16}
\]

Combining `(11)` and `(16)` proves `(6)`, and `(7)` follows because `mu>=0` may be assumed.

## 5. Asymptotic return barrier

Consider any family of such acyclic no-descent first crossings with lengths `j_r->infinity`, maximum proper-prefix banks `B_r`, and repeated-factor lengths `L_r`.

If

\[
L_r\log2
 -B_r\log3
 -(\mu+1)\log j_r
\longrightarrow+\infty,
\tag{17}
\]

then `(6)` is eventually impossible. Hence no such family exists.

A particularly useful consequence is:

\[
\boxed{
B_r=o(j_r)
\quad\Longrightarrow\quad
L_r=o(j_r)
}
\tag{18}
\]

for the longest repeated parity factor of every surviving family.

Thus a late first crossing with sublinear coefficient bank must become asymptotically recurrence-poor: it cannot contain two copies of any factor occupying a fixed positive fraction of its total length.

## 6. Canonical first-crossing consequence

For a first-crossing word `w` of length `j`, let `r^+(w)` be its least positive parity-cylinder representative and put

\[
y^+(w)=T^j(r^+(w)).
\]

The exact target

\[
r^+(w)>{A_w\over2^j-3^q}
\]

is equivalent to

\[
r^+(w)>y^+(w).
\]

If this target fails, the canonical representative itself satisfies the no-descent hypothesis `(2)`. Therefore every non-cycle counterexample to the target must obey the return barrier `(6)--(7)`.

Consequently, any unbounded family of target failures must choose at least one of the following escape mechanisms:

```text
coefficient bank B comparable to the repeated-factor scale;
longest repeated factor o(j);
a repeated physical state, hence a positive cycle;
or failure of the Baker/source dependency.
```

This is a direct narrowing of the delayed-crossing blocker, not a finite prefix census.

## 7. Families eliminated

The theorem excludes every unbounded no-descent first-crossing family for which

- the proper-prefix bank is sublinear in `j`; and
- a repeated factor has length at least `delta*j` for some fixed `delta>0`.

This includes, once their return constants are supplied, bounded-bank families generated by primitive substitutions, linearly recurrent systems, Sturmian/mechanical systems, and bounded-distortion finite-state codings with linear-size repeated supertiles.

The conclusion is family-local: no blanket claim about every substitution or transducer is made without checking the stated return hypothesis.

## 8. Gap audit

- The theorem does not exclude high-bank, recurrence-poor first-crossing words.
- The Baker constants are not instantiated numerically; source reconstruction is required before promotion.
- If `x_a=x_b`, the segment contains a positive cycle and must be handled by the full-denominator cycle lane.
- The theorem does not prove the universal canonical descent inequality.
- It nevertheless closes a complete asymptotic class with growing lengths, rather than one bounded Farey cell.
