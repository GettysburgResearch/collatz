# L-8001 — Exact two-pulse reduction around a repeated negative cycle

**Claim ID:** `L-8001`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pulse-01`  
**Issue:** #46  
**Scope:** two valuation increases at distinct positions of a repeated known negative accelerated cycle

## 1. Setup

Let

\[
w=(a_0,\ldots,a_{k-1}),\qquad A=\sum_i a_i,
\]

be a rotated accelerated valuation word with negative odd fixed state `z_0`.
Write its cyclic negative states as

\[
2^{a_i}z_{i+1}=3z_i+1,
\qquad z_{i+k}=z_i<0.
\]

Repeat the word `r>=1` times.  Put

\[
N=kr,\qquad U=2^{Ar},\qquad Q=3^N.
\]

Choose two distinct pulse positions.  By cyclic rotation put the first at
position `0`, and orient the pair so that the second is at a gap

\[
1\le g\le \lfloor N/2\rfloor.
\]

Increase the two valuations by `d_1,d_2>=1`, and set

\[
X=2^{d_1},\qquad M=2^{d_2}.
\]

Let

\[
S=\sum_{i=1}^{g}a_i
\]

in the rotated repeated word, and define

\[
\alpha=(-z_1)3^g,
\qquad
\beta=(-z_{g+1})2^S,
\qquad
\gamma=\alpha-\beta.
\tag{1}
\]

The unpulsed `g`-step relation from `z_1` to `z_(g+1)` gives

\[
\gamma=2^S z_{g+1}-3^g z_1>0.
\tag{2}
\]

Moreover `alpha` and `gamma` are odd, while `beta` is even.

## 2. Reduced two-pulse numerator

The pulsed word has denominator

\[
\boxed{D=UXM-Q.}
\tag{3}
\]

Its full affine numerator `C'` satisfies

\[
\boxed{
C'=z_0D+2^{a_0}3^{N-g-1}R,
\qquad
R=X(\beta M+\gamma)-\alpha.}
\tag{4}
\]

### Proof

In the unpulsed numerator, the first term is unchanged by both pulses.  Terms
strictly after the first pulse acquire `X`, and terms strictly after the
second acquire the additional factor `M`.  Split the numerator at the two
pulse positions and use the fixed negative-cycle identities for the initial
state, the `g`-step gap, and the remaining suffix.  Collecting the baseline
multiple `z_0D` leaves exactly the term in (4).  A direct expansion gives the
same identity:

\[
C'-z_0D
 =2^{a_0}3^{N-g-1}
   \{X[(-z_{g+1})2^S M+(2^Sz_{g+1}-3^gz_1)]-(-z_1)3^g\}.
\]

Substitution of (1)--(2) proves (4). **QED**

Since `D` is odd and coprime to `3`, the exterior factor in (4) is invertible
modulo `D`.  Therefore

\[
\boxed{D\mid C'\iff D\mid R.}
\tag{5}
\]

Any hit reconstructs the rational fixed point

\[
\boxed{
n=z_0+2^{a_0}3^{N-g-1}{R\over D}.}
\tag{6}
\]

Positive integrality is still followed by a complete exact valuation replay.

## 3. Two determinant eliminants

Define

\[
\boxed{
K(M)=Q(\beta M+\gamma)-UM\alpha,}
\tag{7}
\]

and

\[
\boxed{
J(X)=U(X\gamma-\alpha)+\beta Q.}
\tag{8}
\]

Then

\[
UMR-(\beta M+\gamma)D=K(M),
\tag{9}
\]

and

\[
UXR-\beta XD=XJ(X).
\tag{10}
\]

Because `gcd(D,2)=1`, both identities are reversible modulo `D`:

\[
\boxed{D\mid R\iff D\mid K(M)\iff D\mid J(X).}
\tag{11}
\]

Neither eliminant can vanish.

First, `beta*M+gamma` is odd, so the first term in (7) is odd while the second
is even.  Hence

\[
\boxed{K(M)\text{ is odd and nonzero}.}
\tag{12}
\]

Second, `v_2(beta*Q)=S`, while the other summand in (8) is divisible by
`U=2^(Ar)`.  Since `g<N`,

\[
S<Ar.
\]

The two summands in (8) therefore have distinct `2`-adic orders, proving

\[
\boxed{J(X)\ne0.}
\tag{13}
\]

Thus the two-variable search has no hidden zero-determinant resonance.

## 4. Finite caps for every fixed repetition and gap

Write

\[
K(M)=cM+d,
\qquad
c=Q\beta-U\alpha,
\qquad
d=Q\gamma>0.
\tag{14}
\]

If a divisibility hit exists, then `D<=|K(M)|`.  Since `M>=2`,

\[
UXM-Q\le |c|M+d
\]

gives

\[
\boxed{
X\le
\left\lfloor{2|c|+d+Q\over2U}\right\rfloor.}
\tag{15}
\]

For each surviving power `X`, the nonzero second eliminant gives

\[
UXM-Q\le |J(X)|,
\]

hence

\[
\boxed{
M\le
\left\lfloor{|J(X)|+Q\over UX}\right\rfloor.}
\tag{16}
\]

Equations (15)--(16) exhaust **all** positive pulse sizes for the fixed
`(r,rotation,g)`.  They are not a threshold-slack approximation.

## 5. Cyclic completeness

Given any raw two-pulse placement, rotate one pulse to index `0`.  Of the two
oriented cyclic gaps between the pulses, choose the shorter; it is at most
`N/2`.  Scanning every primitive rotation, every such `g`, and all ordered
pulse sizes therefore covers every two-pulse word up to cyclic rotation.

## 6. Frozen exact consequence

`X-8001` applies the complete caps to:

- every two-pulse perturbation of `(1,2)^r` for `1<=r<=50`;
- every two-pulse perturbation of `(1,1,1,2,1,1,4)^r` for `1<=r<=20`;
- and the minimal total pulse crossing `D>0` plus the next three totals through
  `r=5000` in both families.

It tests `16,445,391` all-size reduced candidates and `168` long-scan reduced
candidates.  The only hit is

\[
(1,2)^2\longmapsto(2,2)^2,
\qquad n=1,
\]

the trivial cycle.

## 7. Boundary

- The algebraic reduction and caps are valid for every `r`.
- The negative scan ranges are finite and exactly declared.
- Three or more pulses are outside the lemma; `X-8002` begins that offense.
- No positive nontrivial cycle or divergent seed is claimed.
