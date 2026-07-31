# T-6607 — only a modulus wrap can make a nonmechanical first crossing harder to descend

**Claim ID:** `T-6607`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** `L-6601`; elementary integer algebra  
**Scope:** canonical representatives of all first-coefficient-crossing words at one fixed `(j,q)`  

## 1. Setup

Fix a first-crossing length and weight `(j,q)`, and put

\[
D=2^j-3^q>0.
\tag{1}
\]

Let `w` be the upper mechanical extremizer, and let `v` be any other first-crossing word of the same length and weight.

Write

\[
A_w-A_v=\Delta>0.
\tag{2}
\]

Let

\[
r_w=r(w),\qquad r_v=r(v)
\]

be their least nonnegative parity-cylinder representatives modulo `2^j`, and let

\[
y_w=T_w^j(r_w),
\qquad
y_v=T_v^j(r_v).
\]

Define the integer descent defects

\[
\delta_w=r_w-y_w,
\qquad
\delta_v=r_v-y_v.
\tag{3}
\]

Thus the desired canonical first-crossing inequality is exactly

\[
\delta_v>0.
\]

## 2. Displacement residue

Because

\[
3^q\equiv-D\pmod{2^j},
\]

`L-6601` gives

\[
r_v-r_w
\equiv
-D^{-1}\Delta
\pmod{2^j}.
\]

Let

\[
\boxed{
s=[-D^{-1}\Delta]_{2^j}}
\qquad(1\le s<2^j).
\tag{4}
\]

Then

\[
r_v=[r_w+s]_{2^j}.
\]

Put

\[
\varepsilon=
\begin{cases}
0,&r_w+s<2^j,\\
1,&r_w+s\ge2^j.
\end{cases}
\tag{5}
\]

Thus

\[
\boxed{r_v=r_w+s-\varepsilon2^j.}
\tag{6}
\]

Since `Ds+Delta` is divisible by `2^j`, define

\[
\boxed{
m={Ds+\Delta\over2^j}\in\mathbf Z_{>0}.}
\tag{7}
\]

## 3. Exact descent-defect transport

For any word `u` of this fixed length and weight,

\[
\delta_u
={Dr_u-A_u\over2^j}.
\tag{8}
\]

Using `(2)`, `(6)`, and `(7)`,

\[
\begin{aligned}
\delta_v-\delta_w
&={D(r_v-r_w)+\Delta\over2^j}\\
&={D(s-\varepsilon2^j)+\Delta\over2^j}\\
&=m-\varepsilon D.
\end{aligned}
\]

Therefore

\[
\boxed{
\delta_v
=
\delta_w+m-\varepsilon D.}
\tag{9}
\]

This is the complete canonical effect of leaving the mechanical extremizer.

## 4. No-wrap words are easier to descend

If `epsilon=0`, then

\[
\boxed{\delta_v=\delta_w+m>\delta_w.}
\tag{10}
\]

Thus, once the mechanical canonical representative descends, **every non-wrap word of the same `(j,q)` descends with a strictly larger integer margin**.

The mechanical extremizer is therefore the hardest word only inside the no-wrap sector; any harder nonmechanical candidate must exploit the modulus boundary.

## 5. Complete wrap criterion

If `epsilon=1`, then

\[
\boxed{
\delta_v
=
\delta_w-(D-m).}
\tag{11}
\]

Assume the mechanical representative descends, so `delta_w>=1`. A wrapped word fails to descend exactly when

\[
\delta_v\le0,
\]

or equivalently

\[
\boxed{
m\le D-\delta_w.}
\tag{12}
\]

Therefore all canonical words of the fixed `(j,q)` descend as soon as the following two finite conditions hold:

\[
\boxed{
\delta_w>0
\quad\text{and}\quad
m>D-\delta_w
\text{ for every wrapped displacement}.}
\tag{13}
\]

No-wrap displacements require no further checking.

## 6. Immediate complete cases

Because `m>=1`, if

\[
\boxed{\delta_w\ge D,}
\tag{14}
\]

then every word at this `(j,q)` descends automatically:

- no-wrap words by `(10)`;
- wrap words because
  \[
  \delta_v\ge\delta_w-(D-1)\ge1.
  \]

More generally, only the narrow integer interval

\[
1\le m\le D-\delta_w
\tag{15}
\]

can contain a dangerous wrapped displacement.

## 7. Full-denominator interpretation

Equation `(7)` is the exact two-place divisibility relation

\[
\boxed{Ds+\Delta=m2^j.}
\tag{16}
\]

Thus a canonical target failure is no longer an unstructured comparison of a residue and a real threshold. It requires simultaneously:

```text
a positive displacement numerator Delta=A_w-A_v;
a solution s to D*s == -Delta mod 2^j;
a wrap r_w+s>=2^j;
a small quotient m=(D*s+Delta)/2^j;
and m<=D-delta_w.
```

This is a mixed dyadic/full-denominator certificate analogous to the cycle-side remainder gate, but attached to first-crossing descent.

## 8. Composition with `T-6604`--`T-6606`

The delayed-crossing program now has two complementary consumers.

### Recurrence consumer

`T-6604`--`T-6606` exclude candidates whose mechanical margin forces a long repeated factor incompatible with the logarithmic gap.

### Wrap consumer

`L-6601/T-6607` show that candidates outside the no-wrap sector must solve the exact small-quotient relation `(12)--(16)`.

A complete proof of Box 2 may therefore proceed by showing:

```text
all low-swap/recurrent words fail the return-gap gate;
all remaining displacement numerators have either no wrap
or quotient m>D-delta_w.
```

## 9. Gap audit

- The theorem does not prove `delta_w>0` for every mechanical length.
- The wrapped small-quotient interval can be nonempty.
- No distribution or lower bound for `m` over all displacement numerators is proved.
- Positive cycles remain part of the fixed-word landscape and are not silently discarded.
- The result is nevertheless an exact reduction of every nonmechanical canonical target failure to one finite wrap quotient.
