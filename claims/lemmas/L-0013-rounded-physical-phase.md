# L-0013 — Physical parity drives a rounded phase pair

Claim ID: `L-0013`  
Title: Rounded physical-parity form of the exact negative-phase coupling  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0001`, `T-0014`  
Scope: one-step and finite-word phase dynamics  
Related counterexample candidates: none

## Statement

Let

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Write an ordinary integer state as

\[
n=q-v,
\qquad
v\ge1,
\]

and let

\[
e=n\bmod2
\]

be the **physical Collatz parity**. Define two maps on positive phase magnitudes:

\[
\boxed{
S_0(v)=\left\lceil\frac v2\right\rceil,
\qquad
S_1(v)=\left\lfloor\frac{3v}{2}\right\rfloor.
}
\tag{1}
\]

Put \(r=v\bmod2\). Then one shortcut step has the exact form

\[
\boxed{
v'=S_e(v)
}
\tag{2}
\]

and

\[
\boxed{
q'=
\begin{cases}
(q+r)/2,&e=0,\\[1mm]
(3q+1-r)/2,&e=1.
\end{cases}
}
\tag{3}
\]

Both quantities are integers and

\[
\boxed{
T(q-v)=q'-v'.
}
\tag{4}
\]

The two phase branches are complementary:

\[
\boxed{
S_0(v)+S_1(v)=2v
}
\tag{5}
\]

for every \(v\ge1\).

Consequently, for any finite physical parity word

\[
w=e_0e_1\cdots e_{L-1},
\]

the phase endpoint

\[
S_w(v)
=
S_{e_{L-1}}\circ\cdots\circ S_{e_0}(v)
\tag{6}
\]

depends only on \(v\) and the physical parity word, not on the magnitude of the accompanying quotient \(q\).

## Proof

Let \(p=q\bmod2\) and \(r=v\bmod2\). Since \(n=q-v\),

\[
e=p\oplus r.
\]

`T-0014` gives

\[
q'=\frac{3^e q+p}{2},
\qquad
v'=\frac{3^e v+(2p-1)r}{2}.
\]

If \(e=0\), then \(p=r\). Hence

\[
v'=\frac{v+r}{2}
=\left\lceil\frac v2\right\rceil
\]

and

\[
q'=\frac{q+r}{2}.
\]

If \(e=1\), then \(p=1-r\). Hence

\[
v'=\frac{3v-r}{2}
=\left\lfloor\frac{3v}{2}\right\rfloor
\]

and

\[
q'=\frac{3q+1-r}{2}.
\]

This proves (2)--(4).

Finally,

\[
\left\lceil\frac v2\right\rceil
+
\left\lfloor\frac{3v}{2}\right\rfloor
=2v
\]

for both parities of \(v\), proving (5). ∎

## Interpretation

The moving negative reference phase is not governed by a complicated XOR once the **physical** parity is used. It follows a rounded multiplicative pair:

\[
v\stackrel{e=0}{\longmapsto}\lceil v/2\rceil,
\qquad
v\stackrel{e=1}{\longmapsto}\lfloor3v/2\rfloor.
\]

Thus every ordinary Collatz parity word drives a second, exact integer-valued shadow trajectory.

The identity (5) makes \(v\) harmonic under fair physical parity. This is the entry point for `T-0017`.

## Gap audit

- The rounded phase trajectory does not determine an ordinary starting integer by itself.
- An arbitrary infinite physical parity word normally determines only a 2-adic Collatz state.
- Growth of the phase shadow is not yet growth of one ordinary positive trajectory unless an ordinary finite boundary is independently certified.

## Adversarial tests

`X-0009` checks (2)--(5) for

```text
1 <= v <= 500
1 <= q <= 1000
```

and verifies the physical Collatz identity directly.
