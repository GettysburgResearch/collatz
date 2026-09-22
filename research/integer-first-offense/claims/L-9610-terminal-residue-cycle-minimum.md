# L-9610 — The terminal residue forces cycle-minimum level 8 or 9 modulo 9

**Claim ID:** `L-9610`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-26  
**Dependencies:** `L-9609`; the centered fixed-weight pulse formula of `T-9608`  
**Scope:** contracting fixed-weight macro alphabets in the negative-three pulse chart

## 1. Setup

Use the centered negative-three letters

\[
A:\quad 8y'=9y+3,
\qquad
B:\quad 16y'=9y.
\tag{1}
\]

Fix a macro shape with

\[
a=\#A\ge1,
\qquad
b=\#B\ge1,
\qquad
L=a+b\ge2.
\]

Every chronological word `w` of that shape has the common affine summary

\[
QF_w(y)=Py+E_w,
\qquad
Q=8^a16^b=2^N,
\qquad
P=9^L,
\tag{2}
\]

where

\[
N=3a+4b
\tag{3}
\]

and

\[
\boxed{
E_w=3\sum_{q:w_q=A}
9^{L-1-q}2^{3A_q+4B_q}.}
\tag{4}
\]

Here `A_q,B_q` count the corresponding letters before position `q`.
Assume the packet is contracting:

\[
D=Q-P>0.
\tag{5}
\]

## 2. Cycle-minimum normal form

Suppose an arbitrary finite word in the complete fixed-weight macro alphabet
has a positive integral cycle. Rotate the macro word so that its first boundary
state `m` is minimal, and write the next boundary as

\[
m+k,
\qquad k\ge0.
\]

By `L-9609`, the first selected macro constant satisfies

\[
E_w=Dm+Qk.
\tag{6}
\]

Every `E_w` is divisible by three. Since

\[
D\equiv Q\not\equiv0\pmod3,
\]

equation `(6)` gives

\[
m+k\equiv0\pmod3.
\]

Write

\[
m+k=3r,
\qquad r\ge1.
\tag{7}
\]

Then

\[
\boxed{E_w=3rD+Pk.}
\tag{8}
\]

## 3. Exact terminal residue

Modulo `27`, every term in `(4)` vanishes except possibly an `A` in the
last position.

- If `w` ends in `B`, then

  \[
  E_w\equiv0\pmod{27}.
  \tag{9}
  \]

- If `w` ends in `A`, then the final prefix exponent is `N-3`, so

  \[
  E_w\equiv3\,2^{N-3}\pmod{27}.
  \tag{10}
  \]

On the target side, `L>=2` gives `27|P`, and hence `D≡Q=2^N mod27`.
Equation `(8)` becomes

\[
E_w\equiv3r2^N\pmod{27}.
\tag{11}
\]

If `(9)` holds, the unit `2^N modulo 9` gives

\[
r\equiv0\pmod9.
\tag{12}
\]

If `(10)` holds, divide by `3\,2^{N-3}` modulo `9`:

\[
8r\equiv1\pmod9.
\]

Since `8≡-1 mod9`,

\[
r\equiv8\pmod9.
\tag{13}
\]

Therefore every positive integral macro cycle satisfies the exact alternative

\[
\boxed{r\equiv0\text{ or }8\pmod9.}
\tag{14}
\]

The residue also identifies the terminal macro letter:

```text
r == 0 mod 9  -> the first selected macro ends in B;
r == 8 mod 9  -> the first selected macro ends in A.
```

## 4. Immediate all-repetition gate

Let

\[
E_{\max}=\max_w E_w.
\]

Equation `(8)` gives

\[
E_w\ge3rD.
\]

The smallest positive integer in the residue classes `(14)` is `r=8`.
Consequently

\[
\boxed{E_{\max}<24D}
\tag{15}
\]

excludes every positive integral cycle at every macro repetition length and
every chronological switching pattern.

For the fixed-weight pulse alphabet, `T-9608` gives

\[
E_{\max}=3\,16^b(9^a-8^a).
\tag{16}
\]

Thus `(15)` is equivalent to

\[
\boxed{
9^a(16^b+8\,9^b)<9\,8^a16^b.}
\tag{17}
\]

## 5. Strength

The result is not a period search. It reduces an arbitrary cycle grammar to
one sparse arithmetic ladder:

\[
r\in\{8,9,17,18,26,27,\ldots\}.
\]

The obstruction uses both ends of one physical macro:

- the cycle minimum controls the complete denominator through `(8)`;
- the last physical letter controls the exact residue modulo `27`.

This is the first two-sided residue rule in the fixed-weight pulse program.

## 6. Gap audit

- The lemma excludes cycles, not aperiodic infinite paths.
- The packet must be contracting; supercritical packets are treated separately by sign.
- The common fixed-weight summary `(P,Q)` is load-bearing.
- When `E_max>=24D`, the lemma leaves a sparse finite set of `r`-levels; it does not by itself eliminate them.
- The terminal residue is an exact physical-word fact, not a statement about an abstract relabeling of the macro alphabet.

## 7. Suggested continuation

For a surviving level `r`:

1. use the exact height bound in `(8)` to cap `k`;
2. use the word-independent phase modulo `7` to restrict `k` further;
3. use the first two or three physical letters modulo a power of two to close the remaining finite pairs.
