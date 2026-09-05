# Supporting interface: confluent carry sorting and an exact unbounded macro

**Status:** elementary support rederived here; **PROPOSED pending review**.
No global Collatz termination certificate is supplied.

## 1. Mixed-radix semantics

Let a,b represent (base,digit)=(2,0),(2,1); let e,f,g represent
(3,0),(3,1),(3,2). Read a word left to right as successive affine maps
x -> base*x+digit. If it has B binary and E ternary symbols, it represents

\[
x\longmapsto 2^B3^E x+c,\qquad 0\le c<2^B3^E.
\]

The six carry rules are

```
ae -> ea     af -> eb     ag -> fa
be -> fb     bf -> ga     bg -> gb
```

They preserve the affine map because each is the equality
3i+j=2j'+i'. These rules are the administrative carry core appearing in the
Yolcu--Aaronson--Heule mixed-radix program. The full boundary-system equivalence
is external context; none of the proof below needs it.

## 2. Termination and uniqueness of the normal form

Count pairs in which a binary symbol is to the left of a ternary symbol.
Every rule replaces one adjacent binary-ternary pair by a ternary-binary pair.
It removes exactly one inversion, without changing the types or the count of
any other pair. Thus every rewrite sequence terminates after exactly the
initial inversion count, which is at most B*E.

A normal form has every ternary symbol before every binary symbol. With B,E
fixed, this form is unique for the represented offset c: its binary suffix is
the B-bit representation of c modulo 2^B, including leading zeros, and its
ternary prefix is the E-digit representation of floor(c/2^B), again padded with
zeros. This proves uniqueness directly, without relying on a termination
prover or assuming confluence of the full Collatz boundary system.

Unbounded standard match height, as observed in PR #6, does not contradict this
simple inversion measure. A match-height annotation and a termination measure
are different objects. This packet does not claim to repair all the remaining
boundary rules by the same measure.

The generator normalizes by leftmost swaps. The independent verifier uses
rightmost swaps and an arithmetic mixed-radix decoder. They agree on all 19,531
words of length at most 6, performing 64,746 swaps in total.

## 3. An exact adaptive macro on every positive odd integer

Write

\[
n=2^a u-1,\qquad a=v_2(n+1)\ge1,\quad u\text{ odd}.
\]

For 0<=i<=a the first a shortcut steps satisfy

\[
T^i(n)=3^i2^{a-i}u-1.
\]

For i<a these states are odd, and the state at i=a is even. Set

\[
b=v_2(3^a u-1)\ge1.
\]

Exactly b even steps then reach the next odd state

\[
\boxed{\mathcal M(n)=(3^a u-1)/2^b.}
\]

This macro takes exactly a+b shortcut steps. It keeps unbounded a,b,u exactly;
it is neither a bounded residue table nor an autonomous finite-state itinerary.
For n=1 it returns 1, so any strict rank condition must exclude that terminal
case. The checker verifies the formula on every positive odd n<=32767 (16,384
sources), using a separate direct branch replay.

## 4. The still-open semantic interface

A rank in a well-founded order that strictly decreases under M at every odd
n>1 would prove Collatz: an infinite nonterminal orbit would give an infinite
strictly descending rank sequence. There is no possible infinite even-only
tail from a positive integer, so the odd macro covers every failure mode.

A finite proof can legitimately reason about unbounded a,b,u. However, the
finite affine-valuation logarithmic template in [ROUTE3_RANKS.md](ROUTE3_RANKS.md)
is impossible for any fixed shortcut block. That theorem does not automatically
exclude every rank for this adaptive macro, whose block length a+b is unbounded.
The separate T-A3-302 argument does exclude that same finite scalar template
for this particular adaptive macro. It is not an automatic consequence of the
fixed-block theorem and does not cover every adaptive macro or nonlinear rank.

No macro-wide rank, well-foundedness certificate, or all-time termination
invariant has been found in this pass.
