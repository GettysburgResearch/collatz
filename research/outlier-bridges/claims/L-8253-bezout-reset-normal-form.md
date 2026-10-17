# L-8253 — Bézout-centered 36-bit reset normal form

**Claim ID:** `L-8253`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-outlier-01`  
**Reviewing agents:** none yet  
**Created:** 2026-07-23  
**Last updated:** 2026-07-23  
**Issue:** #52  
**Dependencies:** `L-8251`, `L-8252`  
**Scope:** the centered nine-B high-block machine  
**Related counterexample candidates:** none

## Statement

Retain the exact constants

\[
D_9=16^9-9^9,
\qquad
\omega=37\,933\,813\,917,
\tag{1}
\]

\[
a=215\,072\,362,
\qquad
b=38\,148\,886\,279
\tag{2}
\]

from `L-8251` and `L-8252`. They satisfy the exact Bézout identity

\[
\boxed{2^{36}a-9^9b=1.}
\tag{3}
\]

For an ordinary centered state `X`, define

\[
\boxed{Y=9^9X+a.}
\tag{4}
\]

Then `Y` is a positive integer whenever `X>=0`, and

\[
Y\equiv a\pmod {9^9}.
\tag{5}
\]

The centered branch labeled `s>=0` from `L-8252` is defined if and only if

\[
\boxed{
\nu_2(Y)=3s,}
\tag{6}
\]

and, writing

\[
Y=2^{3s}u,
\qquad u\text{ odd},
\tag{7}
\]

one has the fixed-depth gate

\[
\boxed{
9^{s+9}u+1\equiv0\pmod {2^{36}}.}
\tag{8}
\]

When `(6)--(8)` hold, the next state is

\[
\boxed{
Y'=\frac{9^{s+9}u+1}{2^{36}},}
\tag{9}
\]

and automatically

\[
Y'\equiv a\pmod {9^9}.
\tag{10}
\]

Thus

\[
X'=\frac{Y'-a}{9^9}
\tag{11}
\]

is an integer, and `(9)--(11)` reproduce exactly the branch of `L-8252`.

Equivalently, put

\[
V=9^su.
\tag{12}
\]

Then the gate and output are the two-base digit exchange

\[
\boxed{
V=b+2^{36}X',}
\tag{13}
\]

while the input is

\[
\boxed{
Y=a+9^9X=2^{3s}u.}
\tag{14}
\]

In one equation,

\[
\boxed{
9^s(a+9^9X)=8^s(b+2^{36}X').}
\tag{15}
\]

The branch label is no longer an external directive. It is recovered intrinsically from the ordinary input by

\[
\boxed{
s={\nu_2(9^9X+a)\over3}.}
\tag{16}
\]

A branch exists exactly when the valuation is divisible by three and the normalized odd unit passes the fixed 36-bit gate `(8)`.

For every `s>=44`, a defined branch on `Y>0` satisfies

\[
\boxed{Y'>Y.}
\tag{17}
\]

Finally, define the rational `2`-adic center

\[
\Theta=-a\,9^{-9}\in\mathbf Z_2.
\tag{18}
\]

Every label-`s` branch lies in the annulus

\[
\boxed{
\nu_2(X-\Theta)=3s.}
\tag{19}
\]

Its exact residue is

\[
\boxed{
\xi_s
\equiv
-a9^{-9}
+2^{3s}b9^{-(s+9)}
\pmod {2^{3s+36}}.}
\tag{20}
\]

Consequently every high branch `s>=44` shares the common 132-bit prefix

\[
\boxed{
X\equiv
598\,051\,932\,619\,127\,473\,212\,326\,704\,339\,812\,739\,814
\pmod {2^{132}}.}
\tag{21}
\]

This prefix is maximal for any alphabet containing label `44` and one larger label: for every `t>44`,

\[
\boxed{
\nu_2(\xi_{44}-\xi_t)=132.}
\tag{22}
\]

## Motivation

`L-8251` compressed the physical nine-run resource window, and `L-8252` removed every fixed odd congruence. The remaining formulas still appeared to require a branch table with a different modulus for every `s`.

Identity `(3)` removes that table. The machine is now:

```text
Y=a+9^9 X;
q=v2(Y);
require q=3s with s>=44;
u=Y/2^q;
require 9^(s+9)u=-1 mod2^36;
Y'=(9^(s+9)u+1)/2^36.
```

The only changing-depth condition is the intrinsic valuation of one written integer. The normalized-unit test always has depth exactly 36.

This is the closest current analogue of a finite-state digit exchange: a block of `3s` zero binary digits is exchanged for `2s` ternary factors, then one fixed 36-bit carry gate returns to the same ordinary `9^9` section.

## Proof

### 1. Derivation of the reset equation

The centered branch of `L-8252` is

\[
2^{3s+36}X'
=
9^{s+9}X+9^sa-8^sb.
\tag{23}
\]

Define `Y'=9^9X'+a`. Multiply `(23)` by `9^9` and add `2^(3s+36)a`:

\[
\begin{aligned}
2^{3s+36}Y'
&=9^{s+9}(9^9X+a)
  +8^s(2^{36}a-9^9b)\\
&=9^{s+9}Y+8^s,
\end{aligned}
\tag{24}
\]

using `(3)`.

If `Y=2^(3s)u` with `u` odd, cancel `2^(3s)` from `(24)` to obtain

\[
2^{36}Y'=9^{s+9}u+1,
\tag{25}
\]

which is `(8)--(9)`.

Conversely, suppose `(6)--(8)` hold and define `Y'` by `(9)`. Modulo `9^9`, equation `(9)` gives

\[
2^{36}Y'\equiv1\pmod {9^9}.
\]

Identity `(3)` gives the same congruence for `a`, and `2^36` is invertible modulo `9^9`. Therefore `(10)` holds, so `(11)` is integral. Reversing the algebra yields `(23)`.

### 2. Intrinsic label and exact gate

The raw synchronized map in `L-8251` has exact next high run `s` precisely when

\[
\nu_2(1+9^9W)=3s.
\]

Since

\[
1+9^9W
=D_9(9^9X+a)
=D_9Y
\tag{26}
\]

and `D9` is odd, this is exactly `(6)`. Hence the valuation determines the unique branch label, and `(8)` is the only remaining integrality condition.

### 3. Two-base digit exchange

Multiply `(7)` by `9^s` and use `(9)`:

\[
9^su
=\frac{2^{36}Y'-1}{9^9}.
\]

Substitute `Y'=a+9^9X'` and use `(3)`:

\[
9^su
=\frac{2^{36}a-1}{9^9}+2^{36}X'
=b+2^{36}X'.
\]

This proves `(13)`. Combining `(7)`, `(12)`, and `(14)` gives `(15)`.

### 4. Pointwise growth

From `(24)`,

\[
2^{3s+36}(Y'-Y)
=
(9^{s+9}-2^{3s+36})Y+2^{3s}.
\tag{27}
\]

For `s>=44`, `9^(s+9)>2^(3s+36)` by `L-8252`; the right side is strictly positive. This proves `(17)`.

### 5. The common high prefix

Equation `(4)` gives

\[
Y=9^9(X-\Theta).
\]

Since `9^9` is a `2`-adic unit, `(6)` is equivalent to `(19)`.

The fixed gate `(8)` says

\[
u\equiv-9^{-(s+9)}\equiv b9^{-s}\pmod {2^{36}},
\]

where the second congruence follows from `(3)`. Substituting

\[
9^9X+a=2^{3s}u
\]

and multiplying by `9^(-9)` gives `(20)`.

The second term of `(20)` has exact valuation `3s`. Hence all labels `s>=44` agree with `Theta` through bit `131`, giving `(21)`. If `t>s`, the label-`s` correction has valuation exactly `3s`, while the label-`t` correction has larger valuation. Their difference therefore has valuation `3s`. Taking `s=44` proves `(22)`.

## Exact ordinary counterexample interface

An unconditional counterexample is now equivalent to one explicit nonnegative integer `X0` for which the deterministic map

\[
\mathcal G(X)=
\frac{
9^{q/3+9}(9^9X+a)/2^q+1
}{2^{36}}
\quad\text{in the `Y` coordinate},
\tag{28}
\]

with

\[
q=\nu_2(9^9X+a),
\tag{29}
\]

is defined forever, has `q>=132`, and has `q divisible by 3` at every step. More explicitly, iterate `(9)` in `Y`, then recover `X` from `(11)`.

The physical initial Collatz integer is decoded by `L-8251` once its initial high run is read from `(16)`.

No external branch schedule, real approximation, or limiting object is part of the certificate.

## Dependency audit

1. `L-8252` supplies `(23)` and the exact growth threshold.
2. `L-8251` supplies the physical interpretation and `(26)`.
3. Every step after those interfaces is elementary integer and `2`-adic algebra.
4. No external theorem is used.

## Gap audit

This result does **not** prove that the deterministic map is defined forever for any ordinary `X`.

In particular:

- the common 132-bit prefix is finite compatibility, not an ordinary survivor;
- the rational center `Theta` is a `2`-adic address, not a positive integer;
- a fixed 36-bit gate does not remove the unbounded valuation requirement;
- pointwise growth follows only after exact branch definedness;
- no candidate `K-####` is proposed.

## Adversarial tests

`X-8252` independently checks:

- identity `(3)`;
- raw/centered/reset agreement;
- intrinsic label recovery;
- the fixed 36-bit gate;
- automatic return to `Y=a mod9^9`;
- digit exchange `(13)--(15)`;
- pointwise high growth;
- prefix `(21)` and exact maximality `(22)` on the declared range.

## Suggested next attack

Use the fixed gate rather than the old branch table. The live state is now

```text
ordinary Y congruent a mod9^9;
q=v2(Y) in 3*Z, q>=132;
odd unit u=Y/2^q;
fixed test 9^(q/3+9)u=-1 mod2^36.
```

This is suitable for a finite transducer on the normalized unit together with one unbounded zero-block counter. The next claim `L-8254` makes the finite-prefix compiler explicit.
