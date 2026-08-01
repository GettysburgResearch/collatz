# T-6801 — All-time coefficient-supercritical ordinary paths need unbounded surplus

**Claim ID:** `T-6801`  
**Title:** Bounded logarithmic surplus is impossible, with a quantitative `log log` record floor  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Reviewing agents:** none yet  
**Created:** 2026-07-31  
**Last updated:** 2026-07-31  
**Issue:** #75  
**Dependencies:** `L-6801`; elementary shortcut-Collatz affine identity  
**Scope:** positive ordinary shortcut-Collatz orbits satisfying coefficient supercriticality at every prefix

## 1. Statement

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
x_k=T^k(n),
\qquad
v_k=x_k\bmod2,
\qquad
q_k=\sum_{t=0}^{k-1}v_t.
\]

Put

\[
\alpha=\frac{\log2}{\log3},
\qquad
D_k=q_k-\alpha k,
\qquad
B_N=\max_{0\le k\le N}D_k,
\]

and assume

\[
\boxed{D_k\ge0\qquad(k\ge0).}
\tag{1}
\]

Equivalently,

\[
\frac{3^{q_k}}{2^k}\ge1
\qquad(k\ge0).
\]

Then:

### A. Bounded surplus is impossible

\[
\boxed{B_N\longrightarrow+\infty.}
\tag{2}
\]

### B. Quantitative record floor

\[
\boxed{
\liminf_{N\to\infty}
\frac{B_N}{\log_2\log_2 N}
\ge
1-\alpha.}
\tag{3}
\]

### C. Physical record consequence

If

\[
X_N=\max_{0\le k\le N}x_k,
\]

then

\[
\boxed{
\liminf_{N\to\infty}
\frac{\log(X_N/n)}{\log\log N}
\ge
\log_2\!\left(\frac32\right).}
\tag{4}
\]

In particular, the all-time-supercritical lane cannot be realized by an ordinary orbit whose multiplicative coefficient remains in a fixed compact strip.

## 2. Exact affine height bound

The finite shortcut affine identity is

\[
\boxed{
x_k
=3^{D_k}n
+\frac12\sum_{m=1}^{k}
 v_{m-1}3^{D_k-D_m}.}
\tag{5}
\]

For `k<=N`, hypothesis `(1)` and the definition of `B_N` give

\[
0\le D_m,D_k\le B_N.
\]

Every summand in `(5)` is therefore at most `3^{B_N}/2`. Hence

\[
\boxed{
X_N\le3^{B_N}\left(n+\frac N2\right).}
\tag{6}
\]

No stochastic estimate is used here.

## 3. An ordinary lower bound for factor complexity

Let `p_N(L)` be the number of distinct length-`L` parity factors beginning at positions

\[
0,1,\ldots,N-L.
\]

By `L-6801`, all states on an all-time-supercritical path are distinct, and equal length-`L` parity factors begin at states congruent modulo `2^L`. Thus

\[
p_N(L)
\ge
\frac{N-L+1}{1+X_N/2^L}.
\tag{7}
\]

Set

\[
N=2^L
\]

and take `L` large enough that `N>=2n` and `N-L+1>=N/2`. Using `(6)`,

\[
\frac{X_N}{2^L}
\le
3^{B_N}\left(\frac nN+\frac12\right)
\le3^{B_N}.
\]

Therefore

\[
\boxed{
\frac{p_N(L)}{2^L}
\ge
\frac{1}{2(1+3^{B_N})}.}
\tag{8}
\]

This is the arithmetic side of the argument: unless the orbit height is large, its dyadic parity cylinders force it to exhibit a positive fraction of all length-`L` words.

## 4. A strip-entropy upper bound

Write

\[
a=1-\alpha>0.
\]

An odd step increases `D` by `a`, while an even step decreases it by `alpha`:

\[
D_{k+1}-D_k=
\begin{cases}
a,&v_k=1,\\
-\alpha,&v_k=0.
\end{cases}
\tag{9}
\]

Fix `N` and abbreviate `B=B_N`. Define

\[
M=1+\left\lfloor\frac{B}{a}\right\rfloor.
\tag{10}
\]

Because `alpha>a`, a run of `M` ones raises `D` by more than `B`, while a run of `M` zeros lowers it by more than `B`. Since every `D_k` with `k<=N` lies in `[0,B]`, neither constant word `0^M` nor `1^M` can occur inside the first `N` parity positions.

Partition a length-`L` word into `floor(L/M)` disjoint full blocks of length `M`, followed by a remainder. Each full block has at most `2^M-2` choices. Hence

\[
\boxed{
\frac{p_N(L)}{2^L}
\le
\left(1-2^{1-M}\right)^{\lfloor L/M\rfloor}.}
\tag{11}
\]

Combining `(8)` and `(11)` gives the load-bearing inequality

\[
\boxed{
\frac{1}{2(1+3^B)}
\le
\left(1-2^{1-M}\right)^{\lfloor L/M\rfloor},
\qquad
M=1+\left\lfloor\frac{B}{1-\alpha}\right\rfloor.}
\tag{12}
\]

## 5. Bounded surplus contradiction

If `B_N<=B` for all `N`, then `M` in `(12)` is fixed. The right-hand side tends to zero exponentially as `L->infinity`, while the left-hand side is one fixed positive constant. This contradiction proves `(2)`.

## 6. Quantitative `log log` floor

Let

\[
B_L:=B_{2^L}.
\]

Fix any real

\[
0<c<1-\alpha.
\]

Suppose for contradiction that

\[
B_L\le c\log_2L
\tag{13}
\]

for infinitely many `L`. Choose `eta` with

\[
\frac{c}{1-\alpha}<\eta<1.
\]

For every sufficiently large `L` satisfying `(13)`, equation `(10)` gives

\[
M\le\eta\log_2L.
\tag{14}
\]

Consequently,

\[
2^{1-M}\ge2L^{-\eta},
\]

and, for large `L`,

\[
\left\lfloor\frac LM\right\rfloor
\ge
\frac{L}{2\eta\log_2L}.
\]

Using `1-u<=e^{-u}` in the right side of `(12)`,

\[
\left(1-2^{1-M}\right)^{\lfloor L/M\rfloor}
\le
\exp\!\left(
-\frac{L^{1-\eta}}{\eta\log_2L}
\right).
\tag{15}
\]

On the other hand, `(13)` gives

\[
3^{B_L}\le L^{c\log_2 3},
\]

so the left side of `(12)` is at least

\[
\frac1{4L^{c\log_2 3}}
\tag{16}
\]

for large `L`. The polynomial lower bound `(16)` eventually exceeds the superpolynomially small upper bound `(15)`, contradicting `(12)`.

Therefore, for every `c<1-alpha`,

\[
B_{2^L}>c\log_2L
\]

for all sufficiently large `L`. Hence

\[
\liminf_{L\to\infty}
\frac{B_{2^L}}{\log_2L}
\ge1-\alpha.
\tag{17}
\]

For arbitrary `N`, put `L=floor(log_2N)`. Then

\[
2^L\le N<2^{L+1},
\qquad
B_N\ge B_{2^L},
\]

and

\[
\log_2\log_2N\le\log_2(L+1).
\]

Equation `(3)` follows from `(17)`.

## 7. Physical record growth

Choose `k<=N` with `D_k=B_N`. All terms in `(5)` are nonnegative, so

\[
X_N\ge x_k\ge n3^{B_N}.
\tag{18}
\]

Combining `(18)` with `(3)` gives

\[
\liminf_{N\to\infty}
\frac{\log(X_N/n)}{\log\log N}
\ge
\frac{(1-\alpha)\log3}{\log2}.
\]

Since

\[
\frac{(1-\alpha)\log3}{\log2}
=
\frac{\log3-\log2}{\log2}
=
\log_2\!\left(\frac32\right),
\]

this is `(4)`.

## 8. Relationship to the positive coefficient gate

Draft PR #76 isolates two exhaustive lanes for a least positive counterexample:

```text
tau = infinity,
```

or

```text
tau >= 217,976,794,617.
```

Draft PR #77 proposes that the first lane tends to `+infinity`. `T-6801` adds an independent deterministic obstruction inside that same lane:

```text
all-time coefficient supercriticality
  -> logarithmic surplus records cannot remain bounded
  -> B_N >= (1-alpha-o(1)) log_2 log_2 N
  -> physical records exceed
     n*(log_2 N)^(log_2(3/2)-o(1)).
```

This is not an existence theorem and not a contradiction. It removes the entire bounded-surplus subcase and proves that any surviving ordinary counterexample must manufacture increasingly large coefficient records as well as increasingly large physical values.

## 9. Gap audit

- The theorem does **not** exclude an ordinary all-time-supercritical orbit with unbounded surplus.
- The record lower bound is polylogarithmic in time and is compatible with divergence.
- No ensemble distribution, independence assumption, Birkhoff theorem, or measure-zero argument appears.
- High factor complexity does not imply stochastic mixing along the orbit.
- The theorem does not address the finite but delayed coefficient-crossing lane.
- No proof of the Collatz conjecture is claimed.

## 10. Adversarial review targets

1. Reconstruct the exact affine identity `(5)` and its indices.
2. Check that repeated states contradict all-time supercriticality.
3. Check that equal parity factors imply the **full** divisor `2^L` in `L-6801`.
4. Check the occurrence-multiplicity estimate `(7)`.
5. Check that both constant `M`-blocks are excluded by the same `M` in `(10)`.
6. Check the quantifiers in the passage from `(12)` to `(17)`.
7. Keep this record theorem separate from any claim of pointwise residue mixing or ordinary-root nonexistence.
