# T-0008 — Collision charts are negative-template rational-base return systems

Claim ID: `T-0008`  
Title: Negative-shadow duality and signed rational-base conjugacy for every finite collision chart  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0001`, `L-0001`, `T-0002`  
Scope: arbitrary finite shortcut-Collatz collision fibers  
Related counterexample candidates: none

## Statement

Extend the shortcut Collatz map to every integer by

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\[1mm]
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

Fix integers \(L\ge1\) and \(a\ge0\), and put

\[
M=2^L,
\qquad
N=3^a.
\]

Suppose a finite collision chart consists of distinct residues

\[
R=\{r_i:i\in I\}\subseteq\{0,1,\ldots,M-1\}
\]

and one integer \(s\) such that

\[
\boxed{
T^L(MQ+r_i)=NQ+s
}
\tag{1}
\]

for every \(Q\ge0\) and every \(i\in I\). Define

\[
u_i=M-r_i,
\qquad
v=N-s.
\tag{2}
\]

Then:

### 1. Exact negative-shadow duality

We have \(u_i>0\), \(v>0\), and

\[
\boxed{
T^L(-u_i)=-v
}
\tag{3}
\]

for every \(i\in I\). More strongly, for every integer \(q\),

\[
\boxed{
T^L(Mq-u_i)=Nq-v.
}
\tag{4}
\]

Thus every finite positive collision chart is exactly a family of positive affine shadows of several negative integers coalescing to one negative target.

### 2. Signed rational-base return map

Put

\[
A=\{v-u_i:i\in I\}.
\tag{5}
\]

At a chart boundary write the positive state as

\[
n(q)=Nq-v.
\tag{6}
\]

If integers \(q,q'\) satisfy

\[
\boxed{
Nq-Mq'=v-u_i\in A,
}
\tag{7}
\]

then

\[
\boxed{
T^L(n(q))=n(q').
}
\tag{8}
\]

Equivalently, the return dynamics on the quotient coordinate is

\[
q'=
\frac{Nq-a}{M},
\qquad a\in A,
\tag{9}
\]

where the applicable signed digit \(a\) is uniquely determined whenever it exists. This is a rational-base \(N/M\) expansion with a finite signed digit alphabet.

### 3. Exact address polynomial

For a finite return itinerary \(a_0,\ldots,a_{k-1}\in A\),

\[
Nq_t=Mq_{t+1}+a_t
\qquad(0\le t<k)
\tag{10}
\]

if and only if

\[
\boxed{
N^kq_0-M^kq_k
=
\sum_{t=0}^{k-1}
 a_tN^{k-1-t}M^t.
}
\tag{11}
\]

### 4. Counterexample criterion

Assume \(N>M\). If there is an infinite integer chain

\[
Nq_t=Mq_{t+1}+a_t,
\qquad a_t\in A,
\tag{12}
\]

such that

\[
q_0>
\max\left\{
\frac vN,
\frac{\max A}{N-M}
\right\},
\tag{13}
\]

then \(n(q_0)=Nq_0-v\) is a positive-integer Collatz counterexample. Indeed the block-boundary states are positive and strictly increasing.

## Definitions

The integers \(-u_i\) are the **negative templates**, \(-v\) is their **return target**, and \(A=\{v-u_i\}\) is the **natural displacement alphabet** of the chart.

Unlike the nonnegative offset alphabet \(D\) used in `T-0002`, the natural displacement alphabet is intrinsic to the negative return picture and may contain negative digits.

## Proof

### Extension of the affine identity to all integer quotients

For a fixed branch \(i\), every integer congruent to \(r_i\) modulo \(M=2^L\) has the same first \(L\) parities. Therefore `L-0001` gives one affine expression on the entire residue class, not only on its nonnegative members. Since (1) holds for all \(Q\ge0\), that affine identity is

\[
T^L(MQ+r_i)=NQ+s
\]

for every integer \(Q\).

Substitute \(Q=q-1\). Using \(u_i=M-r_i\) and \(v=N-s\),

\[
Mq-u_i=M(q-1)+r_i
\]

and

\[
N(q-1)+s=Nq-v.
\]

This proves (4), and setting \(q=0\) proves (3).

The input \(-u_i\) is negative. The shortcut map preserves strict negativity: an even negative integer maps to a negative integer, while for an odd negative integer \(n\le-1\),

\[
\frac{3n+1}{2}\le-1.
\]

Hence the output \(s-N=-v\) is strictly negative, so \(v>0\). Also \(u_i=M-r_i>0\).

### Return equation

Suppose (7) holds with \(a=v-u_i\). Then

\[
Nq-v=Mq'-u_i.
\]

The left side is the current boundary state \(n(q)\), while the right side has the form required by (4). Therefore

\[
T^L(n(q))
=T^L(Mq'-u_i)
=Nq'-v
=n(q'),
\]

which proves (8) and (9).

Because \(A\) lies in an interval of length strictly less than \(M\), two different digits cannot be congruent modulo \(M\). Thus at most one \(a\in A\) makes \(Nq-a\) divisible by \(M\).

### Address polynomial

Multiply the equation at time \(t\) by

\[
N^{k-1-t}M^t
\]

and sum. The intermediate terms telescope, leaving exactly (11). The converse follows by reversing the same finite elimination together with the divisibility equations (10).

### Growth criterion

From (12),

\[
q_{t+1}-q_t
=
\frac{(N-M)q_t-a_t}{M}.
\]

If \(q_t>\max A/(N-M)\), then this difference is positive for every allowed digit. The hypothesis at \(t=0\) therefore propagates and \(q_t\) is strictly increasing. Also \(q_0>v/N\) makes \(n(q_0)=Nq_0-v>0\), and all later boundary states are larger. Applying (8) indefinitely concatenates deterministic finite Collatz blocks and produces an unbounded positive trajectory. ∎

## Relationship with the earlier induced coordinate

For a chart written as

\[
r_i=r_0+d_i,
\qquad
h=s-r_0,
\qquad
c=N-M,
\]

`T-0002` uses digits \(d_i-h=r_i-s\). The natural negative-shadow digits are

\[
v-u_i
=(N-s)-(M-r_i)
=r_i-s+c.
\]

The two alphabets differ by the common translation \(c\), corresponding to translating the quotient coordinate by one. The rational-base return equation is therefore the same induced dynamics in its gauge-free negative-template coordinate.

## Motivation

This theorem exposes a structure that was hidden by the nonnegative offset notation:

> collision fibers are return codes in the ordinary integer Collatz graph, centered at a negative template.

The full counterexample problem can now be attacked using signed rational-base numeration, renewal codes, negative preimage trees, and graph-directed return systems. The separate lifting congruence of `T-0002` is absorbed into the integral quotient equation (7).

## Dependency audit

- `L-0001` supplies the affine identity on a complete residue class modulo \(2^L\).
- `T-0002` is not logically required for the proof, but establishes equivalence with the prior induced-map formulation.
- No infinite existence statement is assumed.

## Gap audit

- A large or structured displacement alphabet does not prove that an infinite rational-base return chain exists.
- The negative templates are exact finite devices; this theorem does not assert that a negative orbit itself gives a positive counterexample.
- Positivity and growth require the explicit threshold in (13).

## Adversarial tests

`X-0006` checks (3), (4), (7), and (8) for all branches of the recorded charts, including all 339 branches of `O-0005`, and checks finite address-polynomial identities.

## Remaining uncertainty

The author believes the finite conjugacy is complete. Its usefulness depends on constructing a finite or finitely generated infinite return code satisfying the criterion.

## Suggested next attack

Study negative return templates to one target \(-v\) as a prefix-code language. Seek an infinite regular renewal code or a finite multi-target graph whose signed rational-base return maps preserve a positive invariant set and expand every admissible branch.
