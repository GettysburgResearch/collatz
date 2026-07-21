# O-0007 — A four-branch chart centered on the negative 11-cycle

Claim ID: `O-0007`  
Title: The `2048 -> 2187` return chart at the negative cycle phase `-136`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0001`, `L-0003`, `T-0002`, `T-0008`, `T-0010`, `X-0007`  
Scope: one exact finite collision chart and its negative-cycle interpretation  
Related counterexample candidates: none

## Statement

Put

\[
L=11,
\qquad
a=7,
\qquad
M=2^{11}=2048,
\qquad
N=3^7=2187,
\qquad
c=N-M=139.
\]

Let

\[
r=1912,
\qquad
s=2051,
\qquad
D=\{0,2,4,5\}.
\]

Then, for every integer \(q\ge0\) and every \(d\in D\),

\[
\boxed{
T^{11}(2048q+1912+d)=2187q+2051.
}
\tag{1}
\]

Equivalently, the four ordinary negative integers

\[
-136,
\quad-134,
\quad-132,
\quad-131
\]

coalesce after eleven shortcut steps:

\[
\boxed{
T^{11}(-136+d)=-136
\qquad(d\in D).
}
\tag{2}
\]

The branch \(d=0\) is one full circuit of the negative 11-cycle

\[
-61\to-91\to-136\to-68\to-34\to-17
\to-25\to-37\to-55\to-82\to-41\to-61.
\tag{3}
\]

Starting at the phase \(-136\), its chronological parity word is

```text
00011110111
```

and contains seven odd steps.

## Signed rational-base return map

The natural negative target and template data are

\[
v=136,
\qquad
u_d=136-d.
\]

Hence the signed displacement alphabet from `T-0008` is exactly

\[
\boxed{A=D=\{0,2,4,5\}.}
\tag{4}
\]

At positive boundaries

\[
n(q)=2187q-136,
\]

one block is available precisely when

\[
2187q=2048q'+d
\qquad(d\in D),
\tag{5}
\]

and then

\[
T^{11}(n(q))=2187q'-136.
\tag{6}
\]

The exact address system is therefore

\[
\boxed{
q'=rac{2187q-d}{2048},
\qquad d\in\{0,2,4,5\}.
}
\tag{7}
\]

Digit zero is the cycle-spine return. The digits \(2,4,5\) are side returns to the same phase.

## Relation with the earlier induced coordinate

Here

\[
h=s-r=139=c.
\]

Thus the lifting class of `T-0002` is

\[
A_{\mathrm{old}}\equiv0\pmod{139}.
\]

Writing \(A_{\mathrm{old}}=139q\) converts the old induced map directly into (7). This chart is therefore the cleanest recorded instance in which the quotient coordinate is visible without a nontrivial affine gauge.

## Exact parity words

| \(d\) | positive residue \(r+d\) | negative template \(-136+d\) | parity word |
|---:|---:|---:|:---|
| 0 | 1912 | -136 | `00011110111` |
| 2 | 1914 | -134 | `01001110111` |
| 4 | 1916 | -132 | `00111110011` |
| 5 | 1917 | -131 | `10011110011` |

Every word has seven ones and reaches the stated common target.

## Aspect ratio

The offset diameter is five, so the normalized aspect ratio of `T-0010` is

\[
\boxed{
\Delta=rac5{139}\approx0.0359712230216.
}
\tag{8}

This is the second-largest aspect ratio found by `X-0007` among all nontrivial supercritical fibers through depth 22, behind only the depth-six value \(1/17\).

Any hypothetical infinite orbit of this chart would force

\[
\left\{C\left(\frac{2187}{2048}\right)^t\right\}
\]

into the circle arc

\[
[-5/139,0]\pmod1.
\]

## Motivation

This chart combines four properties not simultaneously visible in the earlier examples:

1. a near-critical expansion ratio
   \[
   2187/2048\approx1.06787109375;
   \]
2. an explicit negative-cycle spine;
3. three finite side returns to the same cycle phase;
4. a small signed alphabet containing zero and requiring no gauge translation.

It is a natural first testbed for the graph-directed criterion `T-0013`. Additional return templates to phases of the same 11-cycle may route the cylinders not handled by \(\{0,2,4,5\}\).

## Proof

`L-0003` gives the exact affine table at depth 11. The four residues

\[
1912,1914,1916,1917
\]

share

\[
(a_{11},s_{11})=(7,2051).
\]

`L-0001` gives (1) for every \(q\ge0\). Substituting \(q=-1\) gives (2). Direct iteration gives the displayed parity words and the cycle (3). The signed return system follows from `T-0008`, and the aspect ratio follows from `T-0010`. ∎

## Gap audit

- The four digits cover only four residue classes modulo 2048.
- The digit-zero cycle branch alone has only the nonpositive 2-adic fixed shadow as an infinite stationary path.
- A renewal or multi-phase graph is still needed to handle missing cylinders and produce one ordinary positive invariant quotient.
- A favorable aspect ratio is necessary construction room, not a counterexample.

## Adversarial tests

`X-0007` reconstructs the depth-11 affine table, verifies all four branches by direct positive and negative iteration, checks the 11-cycle, and independently computes \(5/139\).

## Suggested next attack

Build return charts at every phase of the negative 11-cycle. Enumerate side returns with good cycle-mean weights, then use `T-0013` to search for a deterministic graph-directed cylinder system with one explicit positive survivor.
