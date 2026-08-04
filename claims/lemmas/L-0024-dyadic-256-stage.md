# L-0024 — Exact 256-step residual-stack stage

Claim ID: `L-0024`  
Title: Finite-control dyadic staging for the corrected two-connector budget  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Dependencies: `L-0019`, `T-0023`  
Scope: each phase-34 self-return tower type of the negative eleven-cycle  
Related counterexample candidates: none

## Statement

Fix one phase-34 self-return tower type with recovery depth \(r\). For

\[
m\ge r+8
\]

and

\[
0\le j\le256,
\]

define

\[
\boxed{
t_{m,j}=2^m+j2^{m-8}.}
\tag{1}

Put

\[
\boxed{H_m=m-r-7.}
\tag{2}

Then:

### 1. Exact 256-step stage

\[
\boxed{t_{m,256}=t_{m+1,0}.}
\tag{3}

For every \(0\le j<256\), the corrected update of `T-0023` is exactly

\[
\boxed{t_{m,j}\longmapsto t_{m,j+1}.}
\tag{4}

Thus one scale stage contains 256 equal counter jumps, followed by one scale doubling.

### 2. Exact eight-bit odometer law

Let

\[
\omega_{m,j}=\omega_{t_{m,j}}.
\]

For every \(1\le j\le256\),

\[
\boxed{
\nu_2(\omega_{m,j}-\omega_{m,0})
=H_m+\nu_2(j).
}
\tag{5}

The first \(H_m\) low bits are stable throughout the stage. The next eight bits carry exactly as the binary odometer

\[
0,1,2,\ldots,256.
\]

At overflow,

\[
\boxed{
\nu_2(\omega_{m+1,0}-\omega_{m,0})
=m-r+1.
}
\tag{6}

### 3. Actual connector seeds

Let \(\eta_{m,j}\) be the connector seed from tower instance \(t_{m,j}\) to \(t_{m,j+1}\). Then, at every displayed precision,

\[
\eta_{m,j}
\equiv
-\omega_{m,j}.
\]

Consequently the exact odometer valuation law (5) transfers to the connector seeds.

### 4. Positive residual-stack slope

There is a finite type-dependent threshold \(m_0\) such that every pair of consecutive connectors beginning in a stage \(m\ge m_0\) satisfies

\[
\boxed{
3^{G_{t_{m,j}}}
>
2^{K_{t_{m,j+2}}}
}
\tag{7}

when \(j+2\le256\), with the evident interpretation across the stage boundary.

Thus the residual-stack recurrence of `T-0023` has slope greater than one on every sufficiently late stage transition.

### 5. Finite-control architecture

The counter controller is

```text
(m,j) -> (m,j+1)       for 0 <= j < 255
(m,255) -> (m+1,0)
```

with 256 finite states for \(j\) and one unbounded scale register \(m\).

At each scale overflow:

- the dyadic height doubles;
- the stable frontier gains one bit;
- the quadratic bulk advances by `L-0023`;
- the residual stack retains positive asymptotic slope.

## Proof

For \(0\le j<256\),

\[
2^m\le t_{m,j}<2^{m+1},
\]

so

\[
\lfloor\log_2t_{m,j}\rfloor=m.
\]

Equation (8) of `T-0023` therefore gives

\[
\Delta(t_{m,j})=2^{m-8},
\]

which proves (4). Equation (3) follows from

\[
2^m+256\,2^{m-8}=2^{m+1}.
\]

The recovery core has period at most 16, and \(2^{m-8}\) is divisible by that period for sufficiently large \(m\). Hence the finite \(\mu\)-term is constant across the stage.

The odd-count difference from \(j=0\) is

\[
7j2^{m-8}.
\]

As in `L-0021`, 2-adic LTE gives

\[
\begin{aligned}
\nu_2(3^{7j2^{m-8}}-1)
&=2+\nu_2(7j2^{m-8})\\
&=m-6+\nu_2(j).
\end{aligned}
\]

Dividing the normalized prefix difference by \(2^{r+1}\) gives

\[
m-r-7+\nu_2(j)
=H_m+\nu_2(j),
\]

proving (5). Setting \(j=256=2^8\) gives (6).

The connector-seed statement follows from the long-prefix identity of `L-0022`; the target anchors are divisible by powers of two far beyond the displayed valuations.

Positive residual slope is exactly `T-0023`. For two connectors entirely within one stage, the future height is

\[
t_{m,j+2}=t_{m,j}+2\,2^{m-8}.
\]

Across the boundary the second jump doubles, but `T-0023`'s uniform bound already covers that case. ∎

## Comparison with the 128-step precursor

`L-0020` and `L-0021` remain correct statements about the one-connector height map. Their 128-step stage preserves a larger prefix at a faster rate, but `T-0023` proves that its residual \(z\)-stack contracts after the next cylinder is parsed.

The 256-step stage is the first dyadic lane in this packet satisfying all three local resource conditions:

1. exact Hensel prefix preservation;
2. positive residual-stack slope;
3. finite control plus one unbounded scale register.

## Gap audit

- Positive residual slope applies only on valid integral residual transitions.
- The 256-state controller does not generate the required inverse-prefix or residual congruence by itself.
- One explicit finite initialization is still absent.

## Adversarial tests

`X-0012` verifies the stage recursion, exact eight-bit odometer valuations, stage-boundary rational frontier, and two-connector residual slopes for all four tower types.

## Suggested next attack

Treat one 256-transition stage as the atomic string-rewrite macro. Its input should carry:

```text
periodic frontier state | 8-bit odometer | quadratic bulk | residual z | marked integer
```

The target is a net rewrite returning the same syntactic tracks at scale \(m+1\), with one more certified frontier bit and a larger ordinary residual.