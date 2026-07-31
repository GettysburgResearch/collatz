# L-6602 — dangerous wraps occupy only a short mechanical-remainder window

**Claim ID:** `L-6602`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** `T-6607`  
**Scope:** wrapped canonical displacements from one first-crossing mechanical extremizer  

## 1. Setup

Use the notation of `T-6607`:

\[
D=2^j-3^q>0,
\qquad
\Delta=A_w-A_v>0,
\]

and suppose the displacement wraps:

\[
r_v=r_w+s-2^j.
\]

Put

\[
u=2^j-s=r_w-r_v,
\tag{1}
\]

and

\[
h=D-m,
\tag{2}
\]

where

\[
m={Ds+\Delta\over2^j}.
\]

Let

\[
\delta_w=r_w-y_w,
\qquad
\delta_v=r_v-y_v,
\qquad
E_w={A_w\over2^j}.
\]

## 2. Exact wrap coordinates

Substituting `s=2^j-u` into the defining equation for `m` gives

\[
\boxed{
\Delta=Du-h2^j.}
\tag{3}
\]

The physical and affine data transport as

\[
\boxed{
\begin{aligned}
r_v&=r_w-u,\\
A_v&=A_w-Du+h2^j,\\
\delta_v&=\delta_w-h,\\
y_v&=y_w-u+h.
\end{aligned}}
\tag{4}
\]

Thus `u` is the ordinary root drop caused by the wrap, while `h` is exactly the lost descent margin.

## 3. The short dangerous window

Assume the mechanical representative descends:

\[
\delta_w>0.
\tag{5}
\]

A wrapped word fails to descend exactly when

\[
\delta_v\le0,
\]

which by `(4)` means

\[
h\ge\delta_w.
\tag{6}
\]

On the other hand, `Delta>0` in `(3)` gives

\[
h<{Du\over2^j}.
\]

Because `r_v>=1`, one has `u<r_w`, and therefore

\[
h
<{Dr_w\over2^j}
=\delta_w+{A_w\over2^j}
=\delta_w+E_w.
\tag{7}
\]

Combining `(6)--(7)` yields the exact short interval

\[
\boxed{
\delta_w
\le h
<\delta_w+E_w.}
\tag{8}
\]

Equivalently, the quotient `m=D-h` lies in

\[
\boxed{
D-\delta_w-E_w
<m
\le D-\delta_w.}
\tag{9}
\]

## 4. Cycle and acyclic levels

The equality level

\[
h=\delta_w
\]

is exactly

\[
\delta_v=0,
\]

so the canonical representative closes a positive cycle.

Every acyclic target failure has

\[
\delta_v<0,
\]

and hence

\[
\boxed{
\delta_w+1
\le h
<\delta_w+E_w.}
\tag{10}
\]

The number of possible acyclic integer levels is therefore at most

\[
\boxed{
\max\{0,\lceil E_w\rceil-1\}.}
\tag{11}
\]

For a first-crossing mechanical word, every odd remainder contribution is below `1/2`, so

\[
E_w<{q\over2}<{j\over2}.
\tag{12}
\]

Thus the exponentially large displacement family can create a canonical failure only through fewer than `j/2` possible defect-loss levels.

## 5. Immediate acyclic closure when `E_w<=1`

If

\[
\boxed{E_w\le1,}
\tag{13}
\]

then interval `(10)` contains no integer. Consequently:

\[
\boxed{
\delta_w>0\text{ and }E_w\le1
\Longrightarrow
\text{every acyclic word at this }(j,q)\text{ descends}.}
\tag{14}
\]

The only remaining non-descending possibility is the equality level `h=delta_w`, namely a positive cycle.

More generally:

```text
1<E_w<=2  -> at most one acyclic defect level;
2<E_w<=3  -> at most two;
...
```

## 6. Reduced finite search object

For each integer `h` in `(10)`, a dangerous displacement must solve

\[
\boxed{
0<Du-h2^j<A_w,
\qquad
1\le u<r_w,}
\tag{15}
\]

with

\[
\Delta=Du-h2^j
\]

belonging to the exact mechanical displacement set

\[
\left\{
\sum_{i=1}^{q}
3^{q-i}2^{d_i(v)}(2^{h_i}-1)
\right\}.
\]

This is a finite full-denominator membership problem indexed by fewer than `ceil(E_w)` values of `h`, not by every first-crossing word.

## 7. Strategic meaning

The delayed-crossing target now separates into:

```text
mechanical representative:
  prove delta_w>0;

non-wrap displacement:
  automatic descent by T-6607;

wrapped displacement:
  test only the short h-window (10),
  with recurrence/swap obstructions from T-6604--T-6606.
```

A complete theorem must show that none of the acyclic levels in `(10)` is represented by an admissible displacement numerator.

## 8. Gap audit

- The short list of `h` values may still contain admissible displacements.
- Equation `(15)` does not by itself recognize the displacement language.
- The cycle equality level remains and must be handled by the positive-cycle lane.
- The result reduces, but does not eliminate, all wrapped canonical failures.
