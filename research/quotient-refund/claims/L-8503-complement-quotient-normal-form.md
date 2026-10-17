# L-8503 — Complement quotients parametrize every local refunded connector

**Claim ID:** `L-8503`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Dependencies:** `D-8501`, `L-8502`  
**Scope:** every stabilized phase-`-34` connector at a height divisible by `16`

## Exact complement coordinate

At source height `t`, put

\[
N=3^{7(t+1)},
\qquad
M=2^{11(t+17)},
\]

and let

\[
Nr=1+Mc,
\qquad
0<r<M,
\quad 0\le c<N
\]

be the inverse residue and carry of `L-8502`.

For a source type `i` and an integer `k`, define

\[
\boxed{
W_{t,i}(k)=b_i(M-r)+Mk,
}
\tag{1}
\]

\[
\boxed{
W^+_{t,i}(k)=b_i(N-c)+Nk.
}
\tag{2}
\]

Then

\[
\boxed{
M W^+_{t,i}(k)=N W_{t,i}(k)+b_i.
}
\tag{3}
\]

Moreover,

\[
\boxed{
W_{t,i}(k)\equiv p_i\pmod{64}.
}
\tag{4}
\]

Thus every `k>=0` gives a positive ordinary source tail of type `i` and its exact ordinary output.

Conversely, every integer `W` satisfying

\[
W\equiv p_i\pmod{64},
\qquad
M\mid NW+b_i
\]

has one unique representation `(1)` with `k in Z`. Every sufficiently large positive such `W` has `k>=0`.

## Six-bit target decoder

For source type `i` and target type `j`, put

\[
\boxed{
\kappa_{t;i,j}
=
[N^{-1}(p_j-b_i(N-c))]_{64}.
}
\tag{5}
\]

The four values `kappa_(t;i,j)` are distinct. Equation `(2)` has target type `j` exactly when

\[
\boxed{
k\equiv\kappa_{t;i,j}\pmod{64}.
}
\tag{6}

Hence one six-bit block of the ordinary quotient selects at most one next tower type.

## Exact next-scale cylinder

At height `t+16`, write

\[
N'=3^{7(t+17)},
\qquad
M'=2^{11(t+33)},
\]

and let `r',c'` be its inverse data. Define the next source origin

\[
O'_{j}=b_j(M'-r').
\tag{7}
\]

For every ordered type pair `(i,j)`, there is one residue

\[
\boxed{
\rho_{t;i,j}
=
[(O'_j-b_i(N-c))N^{-1}]_{M'}
}
\tag{8}
\]

such that

\[
W^+_{t,i}(k)=O'_j+M'k'
\]

for an integer `k'` if and only if

\[
\boxed{
k\equiv\rho_{t;i,j}\pmod{M'}.
}
\tag{9}

The full residue reduces to the six-bit type cell:

\[
\rho_{t;i,j}\equiv\kappa_{t;i,j}\pmod{64}.
\tag{10}
\]

Writing

\[
\sigma_{t;i,j}
=
\frac{b_i(N-c)+N\rho_{t;i,j}-O'_j}{M'},
\tag{11}
\]

every lift

\[
k=\rho_{t;i,j}+M'\ell
\]

has the exact next quotient

\[
\boxed{
k'=\sigma_{t;i,j}+N\ell.
}
\tag{12}

## Proof

Use `Nr=1+Mc`:

\[
\begin{aligned}
N W_{t,i}(k)+b_i
&=Nb_i(M-r)+NMk+b_i\\
&=M\bigl(b_i(N-c)+Nk\bigr),
\end{aligned}
\]

which proves `(3)`. Since `M` is divisible by `64`,

\[
W_{t,i}(k)\equiv-b_i r\pmod{64}.
\]

The stabilized tower table satisfies `Np_i+b_i congruent 0 mod64`; multiplying by `r` gives `-b_i r congruent p_i mod64`, proving `(4)`.

The divisibility condition has the unique solution

\[
W\equiv-b_i r\pmod M.
\]

Equation `(1)` is exactly that residue class with an integer coordinate shifted by `b_i`, proving the converse.

Reducing `(2)` modulo `64` proves `(5)`--`(6)` because `N` is a unit and the four `p_j` are distinct. Solving

\[
b_i(N-c)+Nk\equiv O'_j\pmod{M'}
\]

proves `(8)`--`(9)`. Reduction modulo `64` proves `(10)`, and substitution of a general lift proves `(11)`--`(12)`. ∎

## Constructive meaning

The exact root state can be reduced from

```text
(height, source type, target type, residual)
```

to

```text
(height, source type, complement quotient k).
```

The target type is an output digit of `k`, not externally supplied control data. Infinite definedness remains a genuine ordinary one-counter safety problem.
