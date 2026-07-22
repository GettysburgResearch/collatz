# T-8504 — One complement counter is a complete local counterexample state

**Claim ID:** `T-8504`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Dependencies:** `L-8503`; branch-qualified phase-`-34` physical tower identity  
**Scope:** the linear grid at every multiple of `16` with `t>=3744`

## Deterministic partial map

For a state

\[
(t,i,k),
\qquad
16\mid t,
\quad i\in\{0,1,2,3\},
\quad k\in\mathbb Z_{\ge0},
\]

form the exact source and output words of `L-8503`:

\[
W=b_i(M-r)+Mk,
\]

\[
U=b_i(N-c)+Nk.
\tag{1}
\]

If

\[
U\bmod64\notin\{5,30,20,56\},
\]

the map is undefined. Otherwise let `j` be the unique type with

\[
U\equiv p_j\pmod{64}.
\]

At the next height put

\[
M'=2^{11(t+33)},
\qquad
O'_j=b_j(M'-r').
\]

The next complement quotient exists exactly when

\[
\boxed{M'\mid U-O'_j.}
\tag{2}
\]

When `(2)` holds, define

\[
\boxed{
F(t,i,k)
=
(t+16,j,k'),
\qquad
k'=\frac{U-O'_j}{M'}.
}
\tag{3}

This is one deterministic partial map on finite ordinary integers. It has no externally supplied directive.

## Uniform growth above a finite counter threshold

For every legal transition with

\[
t\ge3744,
\qquad
k\ge256,
\]

one has

\[
\boxed{k'\ge2k.}
\tag{4}
\]

## Explicit counterexample criterion

Assume one finite state

\[
(t_0,i_0,k_0),
\qquad
16\mid t_0,
\quad t_0\ge3744,
\quad k_0\ge256,
\]

has a forward orbit under `(3)` defined for every `n>=0`. Define

\[
W_0=b_{i_0}(M_0-r_0)+M_0k_0
\]

and the positive ordinary integer

\[
\boxed{
n_0=2^{11(t_0+1)}\frac{W_0}{64}-34.}
\tag{5}
\]

Then `n_0` is a shortcut-Collatz counterexample. Its trajectory is the exact concatenation of the finite phase-`-34` tower blocks encoded by `(3)`, remains positive, and is unbounded.

More precisely,

\[
k_n\ge2^n k_0.
\tag{6}
\]

## Proof

`L-8503` proves the local physical identity

\[
M U=NW+b_i
\]

and `W congruent p_i mod64`. If `U congruent p_j mod64`, then

\[
W=p_i+64h,
\qquad
U=p_j+64h'
\]

for nonnegative integers once `k>=0`. Dividing the scaled identity by `64` is exactly the anchor-overlap equation for one physical tower and connector block. Condition `(2)` is precisely the next source-cylinder condition in the complement basis. This proves the deterministic map and physical replay.

For growth, the exact inequality `3^53>2^84` gives, at `t>=3744`,

\[
\frac NM
'>
2^{69/53}.
\tag{7}
\]

Also

\[
2^{175}>3^{106}.
\]

Indeed `3^5<2^8` gives `3^105<2^168`, hence `3^106<2^170<2^175`. Therefore

\[
2^{69/53}>\frac94,
\]

so

\[
\boxed{\frac N{M'}>\frac94.}
\tag{8}
\]

Since `0<r'<M'`, `0<c<N`, and `b_j<=54`, equation `(3)` gives

\[
\begin{aligned}
k'
&=\frac{b_i(N-c)+Nk-b_j(M'-r')}{M'}\\
&>\frac N{M'}k-b_j\\
&>\frac94k-54.
\end{aligned}
\tag{9}
\]

For `k>=256`, the last quantity is greater than `2k`. Since `k'` is integral, `(4)` follows.

The source word in `(5)` satisfies `W_0 congruent p_(i_0) mod64` and is positive, so `(5)` is an explicit positive integer boundary state. Inductively, every legal map step is one exact physical block and `(4)` gives `(6)`. Hence the boundary states and the underlying shortcut trajectory are unbounded and cannot reach the trivial cycle. ∎

## Exact remaining gap

The theorem proves every obligation after infinite definedness. It does not supply a state for which `(2)` holds forever. This is the simplified positive target in `Q-8501`.
