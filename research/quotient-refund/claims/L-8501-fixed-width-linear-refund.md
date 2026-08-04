# L-8501 — Every fixed linear stage width eventually refunds the next complete radix

**Claim ID:** `L-8501`  
**Status:** `PROPOSED`  
**Dependencies:** branch-qualified `PR3/L-0031`; elementary integer inequalities  
**Scope:** every fixed width `L>=1` on the height grid `B+16j`

## Statement

Fix an integer `L>=1`, a multiple of `16` denoted `B`, and one physically overlapping word of `L` tower types on

\[
t_j=B+16j,
\qquad 0\le j\le L.
\]

Composing the scaled-tail recurrence gives

\[
2^{E_L(B)}W_{\rm out}
=
3^{A_L(B)}W_{\rm in}+\tau_B(w),
\tag{1}
\]

where `tau_B(w)>0` is the exact finite `{2,3}`-unit toll sum and

\[
\boxed{
A_L(B)=7L(B+1)+56L(L-1),
}
\tag{2}
\]

\[
\boxed{
E_L(B)=11L(B+1)+88L(L+1).
}
\tag{3}
\]

The next complete width-`L` stage begins at `B+16L` and has binary exponent

\[
E_L(B+16L).
\]

If

\[
\boxed{
5B>9288L+9363,
}
\tag{4}
\]

then

\[
\boxed{
3^{A_L(B)}>2^{E_L(B+16L)}.
}
\tag{5}
\]

More quantitatively,

\[
\boxed{
\log_2\frac{3^{A_L(B)}}{2^{E_L(B+16L)}}
>
\frac{L(5B-9288L-9363)}{53}.
}
\tag{6}
\]

The least qualifying multiples of `16` include

```text
L=1:    B=3744,
L=256:  B=477424.
```

Thus the 256-transition width is not required for quotient refund. A single stabilized connector already has more odd multiplier than the following complete connector radix once `t>=3744`.

## Exact quotient transition

Fix a current stage word `w` and a physically overlapping next word `v`. Write their canonical boundary forms as

\[
W_{\rm in}=R_B(w)+2^{E_L(B)}Y,
\]

\[
W_{\rm out}=S_B(w)+3^{A_L(B)}Y,
\]

and put

\[
Q=2^{E_L(B+16L)}.
\]

There is exactly one residue

\[
y_0(w,v)\pmod Q
\]

such that the output enters the next cylinder. Every lift

\[
Y=y_0+kQ
\]

has next quotient

\[
\boxed{
Y_{\rm next}=c(w,v)+3^{A_L(B)}k
}
\tag{7}
\]

for one integer `c(w,v)`. Under (4), all sufficiently large lifts are positive and expanding.

## Proof

Summing the `L` source odd exponents gives

\[
7\sum_{j=0}^{L-1}(B+16j+1)
=7L(B+1)+56L(L-1),
\]

which is (2). Summing the `L` target binary exponents gives

\[
11\sum_{j=1}^{L}(B+16j+1)
=11L(B+1)+88L(L+1),
\]

which is (3).

Use the exact inequality

\[
3^{53}>2^{84}.
\]

It is enough to prove

\[
84A_L(B)>53E_L(B+16L).
\]

Direct substitution gives the exact identity

\[
\boxed{
84A_L(B)-53E_L(B+16L)
=L(5B-9288L-9363).
}
\tag{8}
\]

Equations (4), (8), and `3^53>2^84` prove (5)–(6).

For (7), the next-cylinder congruence is

\[
S_B(w)+3^{A_L(B)}Y
\equiv R_{B+16L}(v)\pmod Q.
\]

The odd coefficient is invertible modulo `Q`, so there is one residue `y_0`. Substituting `Y=y_0+kQ` and dividing the exact difference by `Q` proves (7). ∎

## Boundary

This lemma proves expanding finite ordinary transitions. It does not choose one finite quotient whose entire future lies in the required residue classes. The full target is the integer-first invariant in `Q-8501`.
