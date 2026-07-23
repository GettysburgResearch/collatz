# T-8512 — A permanent refund tail generates an unbounded ordinary stack at linear depth

**Claim ID:** `T-8512`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-23  
**Dependencies:** `T-8510`, `T-8511`  
**Scope:** the permanently noncanonical tail of every hypothetical infinite ordinary refund orbit

## Ordinary mixed-radix stack

Let a permanent noncanonical tail begin at connector index `n`, with height

\[
t=t_n\ge5632
\]

and positive top quotient `m_n`.

At a later index `n+r`, put

\[
t_r=t+16r.
\]

The future complete top-boundary radices are

\[
\boxed{
H_{r+h}=2^{11(t_r+16h+33)},
\qquad h\ge0.
}
\tag{1}

For every `s>=0`, the ordinary integer `m_(n+r)` has one unique finite mixed-radix expansion

\[
\boxed{
\begin{aligned}
m_{n+r}
={}&a_0+H_r\bigl(a_1+H_{r+1}(\cdots\\
&\qquad +H_{r+s-1}u_s)\cdots\bigr),
\end{aligned}
}
\tag{2}

with

\[
0\le a_h<H_{r+h},
\qquad
u_s\in\mathbf Z_{\ge0}.
\]

Define the **ordinary quotient-stack depth** to be the largest `s` for which `u_s>=1`.

Equivalently, put

\[
P_s(t_r)=\prod_{h=0}^{s-1}H_{r+h}.
\]

Then

\[
\boxed{
u_s\ge1\iff m_{n+r}\ge P_s(t_r).}
\tag{3}

The equivalence is ordinary Euclidean mixed-radix division; it does not use a completion.

## Theorem

For every `r>=288`, the quotient-stack depth at connector `n+r` is at least

\[
\boxed{
\left\lfloor\frac r{288}\right\rfloor.
}
\tag{4}

Consequently every hypothetical infinite ordinary refund path dynamically creates an unbounded stack:

\[
\boxed{
\operatorname{depth}(m_{n+r})\longrightarrow\infty.
}
\tag{5}

The stack is not initialized in advance. It consists of ordinary finite quotient blocks present in the current finite integer and grows forward under the physical Collatz orbit.

## Proof

### Lower bound for the top quotient

`T-8510` gives, for every step on the permanent tail,

\[
m_{s+1}>2^{175+q(t_s)}m_s,
\]

where

\[
q(v)=\left\lfloor\frac{63v-353166}{665}\right\rfloor.
\]

Using the lower sum in `T-8510/(8)` and `m_n>=1`, after `r` steps one obtains

\[
\boxed{
\log_2m_{n+r}
>
175r
+
\frac{
r(63t-353831)+504r(r-1)
}{665}.
}
\tag{6}

### Exact size of an `s`-level stack

From `(1)`,

\[
\begin{aligned}
\log_2P_s(t_r)
&=\sum_{h=0}^{s-1}11(t_r+16h+33)\\
&=\boxed{
11s(t+16r+33)+88s(s-1).
}
\tag{7}
\end{aligned}

Let

\[
s=\left\lfloor\frac r{288}\right\rfloor.
\]

Then `s<=r/288`, and `(7)` gives

\[
\log_2P_s(t_r)
\le
\frac{11r}{288}(t+16r+33)
+
\frac{88r^2}{288^2}.
\tag{8}

Subtract the right side of `(8)` from the lower bound `(6)`. Exact simplification gives

\[
\boxed{
\begin{aligned}
\log_2m_{n+r}-\log_2P_s(t_r)
>{}&r\left(
\frac{1547}{27360}t
+rac{143531}{984960}r\\
&\qquad
-rac{4584925}{12768}
\right).
\end{aligned}
}
\tag{9}

The bracket is increasing in both `t` and `r`. At the smallest allowed values

\[
t=5632,
\qquad
r=288,
\]

it equals

\[
\boxed{
\frac{84263}{63840}>0.
}
\tag{10}

Thus `m_(n+r)>P_s(t_r)`. Equation `(3)` gives `u_s>=1`, proving `(4)`. Letting `r` grow proves `(5)`. ∎

## Relation to the exact path cylinders

Along an actual infinite path, the digits `a_h` in `(2)` are not arbitrary bookkeeping. The successive future legality conditions select one residue at each changing radix. Therefore the ordinary mixed-radix stack is exactly the finite top-boundary data consumed by later connectors.

The theorem proves that a hypothetical witness does not rely on a preloaded infinite directive or completed stack. Its current positive integer contains finitely many stack levels, and the physical forward dynamics creates new nonzero levels at a linear rate.

## Strategic consequence

The constructive architecture has reached the machine class originally sought by issue #43:

```text
finite control:
  height signatures and four physical types;

one ordinary unbounded root:
  the intrinsic core/top quotient;

causally generated stack:
  mixed-radix future-cylinder quotients;

stack growth:
  depth >= floor(r/288) after r permanent-refund connectors;

physical growth:
  core >2^170 per connector and top quotient accelerating.
```

The remaining positive theorem is now sharply one of **entry and exact routing**: find one written integer that enters the permanent-refund regime and whose generated stack digits always match the four legal cells.

## Gap audit

- Unbounded stack depth is conditional on an infinite ordinary orbit existing.
- The theorem does not choose the required mixed-radix digits.
- Large stack capacity is not the same as legal stack content.
- The numerical constant `288` is rigorous and convenient; it is the first integer accepted by this direct uniform envelope, but no global optimality is claimed.
- No `K-85xx` candidate is produced.
