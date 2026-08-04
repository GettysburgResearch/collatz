# T-8501 — The linear connector class is a deterministic expanding one-counter safety problem

**Claim ID:** `T-8501`  
**Status:** `PROPOSED`  
**Dependencies:** `D-8501`, `L-8501`, `L-8502`, branch-qualified physical tower replay  
**Scope:** every local connector state at height `t>=3744`, `16|t`

## Deterministic next-type decoder

Fix a current edge `i -> j` at height `t` and an ordinary residual `z>=1`. Use

\[
N=3^{7(t+1)},
\quad
(\eta,\theta)=(\eta_{t;i,j},\theta_{t;i,j}).
\]

At the next connector height `t+16`, put

\[
M'=2^{11(t+33)}
\]

and use the inverse data of `L-8502` to form `omega'_j` and the four six-bit cells

\[
\delta'_{jk}=[p_kr'-p_jc']_{64},
\qquad k\in\{0,1,2,3\}.
\]

Define

\[
L(z)=Nz+\theta+\omega'_j.
\tag{1}
\]

For `z>=1`, a next physical connector exists if and only if both conditions hold:

\[
\boxed{
\frac{M'}{64}\mid L(z),
}
\tag{2}
\]

and

\[
\boxed{
\left[\frac{64L(z)}{M'}\right]_{64}
\in
\{\delta'_{j0},\delta'_{j1},\delta'_{j2},\delta'_{j3}\}.
}
\tag{3}
\]

When it exists, the next type `k` is unique, and

\[
\boxed{
z'
=
\frac{Nz+\theta-\eta_{t+16;j,k}}{M'}.
}
\tag{4}
\]

Thus the next type is not a future directive symbol. It is decoded causally from the current ordinary counter.

## Uniform growth

For every multiple of `16` with `t>=3744`,

\[
\boxed{N>2M'.}
\tag{5}
\]

Hence every legal transition with `z>=1` satisfies

\[
\boxed{z'\ge2z.}
\tag{6}
\]

## Counterexample criterion

Suppose one explicit finite state

\[
(t_0,i_0,i_1,z_0),
\qquad
16\mid t_0,
\quad t_0\ge3744,
\quad z_0\ge1,
\]

has the property that the deterministic decoder (2)–(4) is defined forever. Then the physical integer

\[
\boxed{
n_0
=
A_{i_0}(t_0)
+2^{11(t_0+1)}
\left(
\eta_{t_0;i_0,i_1}
+2^{11(t_0+17)}z_0
\right)
-34
}
\tag{7}
\]

is a positive ordinary shortcut-Collatz counterexample. Every finite block replays exactly, every boundary state stays positive, and the residuals satisfy

\[
z_n\ge2^n z_0,
\]

so the orbit is unbounded.

## Proof

At the next connector, `L-8502` gives

\[
\eta_{t+16;j,k}
=-\omega'_j+\frac{M'}{64}\delta'_{jk}+\epsilon'_{jk}M'.
\]

The continuation equation

\[
M'z'=Nz+\theta-\eta_{t+16;j,k}
\]

therefore first requires divisibility of `L(z)` by `M'/64`, proving (2). After division by that block, its residue modulo `64` must be `delta'_(jk)`, proving (3). The four values are distinct because the `p_k` are distinct modulo `64` and `r'` is odd. Hence `k` is unique, and (4) follows.

For growth, `3^53>2^84` gives

\[
\log_2\frac N{M'}
>
\frac{84\cdot7(t+1)-53\cdot11(t+33)}{53}
=
\frac{5t-18651}{53}.
\]

At `t=3744` the last numerator is `69>53`, and it increases with `t`, proving (5). Since

\[
0\le\theta<N,
\qquad
0\le\eta_{t+16;j,k}<M',
\]

we have

\[
z'>\frac N{M'}z-1>2z-1.
\]

The left side is integral, so `z'>=2z`, proving (6). Equation (7) is the exact branch-qualified tower initialization. Induction through (4) gives the infinite positive physical replay and unboundedness. ∎

## Exact remaining gap

No state satisfying the forever-defined hypothesis is supplied here. `Q-8501` is exactly that integer-first existence problem.
