# L-8507 — The eight-block core decoder has a type-independent four-cylinder top boundary

**Claim ID:** `L-8507`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-23  
**Dependencies:** `L-8506`, `T-8507`  
**Scope:** every intrinsic core state at a multiple of `16`

## Statement

Fix a finite intrinsic state

\[
(t,\gamma,i),
\qquad
\gamma\in\{1,2,3\},
\quad i\in\{0,1,2,3\},
\]

and put

\[
G=7(t+1)+\gamma-\beta_i,
\qquad
D=11(t+17)-i,
\qquad
A=3^G,
\]

with

```text
beta=(2,3,2,1).
```

Choose one of the eight current blocks of `L-8506`, indexed by a current target type `j` and an allowed ternary lift `nu`:

\[
C=\widehat R_{j,\nu}+3\,2^{D+6}m,
\]

\[
C'=\widehat S_{j,\nu}
   +3\,2^{6-j}A\,m.
\tag{1}
\]

The next finite state is

\[
(t+16,\beta_i,j).
\]

Let

\[
D'=11(t+33)-j
\]

be its high binary exponent. For every prospective following target type

\[
k\in\{0,1,2,3\},
\]

there is exactly one allowed next ternary lift `mu=mu(k)` whose next source block satisfies

\[
\widehat R'_{k,\mu}\equiv\widehat S_{j,\nu}\pmod3.
\tag{2}
\]

Define

\[
g_j=3\,2^{6-j}
\tag{3}
\]

and the complete top-boundary modulus

\[
\boxed{
H_t=2^{D'+j}=2^{11(t+33)}.
}
\tag{4}
\]

The cancellation in `(4)` is exact: `H_t` is independent of `gamma`, `i`, the current target `j`, the following target `k`, and both ternary lifts.

For each `k`, put

\[
\Delta_k=
\frac{\widehat R'_{k,\mu(k)}-\widehat S_{j,\nu}}{g_j},
\tag{5}
\]

\[
\boxed{
\rho_k=[A^{-1}\Delta_k]_{H_t},
}
\tag{6}
\]

and

\[
\boxed{
\sigma_k=
\frac{
\widehat S_{j,\nu}+g_jA\rho_k-\widehat R'_{k,\mu(k)}
}{g_jH_t}.
}
\tag{7}
\]

Then:

1. `Delta_k` and `sigma_k` are integers;
2. `sigma_k>=0`;
3. the four residues `rho_k mod H_t` are distinct;
4. the current output belongs to the complete next block `(k,mu(k))` exactly when
   \[
   \boxed{m\equiv\rho_k\pmod{H_t};}
   \tag{8}
   \]
5. writing
   \[
   m=\rho_k+H_t\ell,
   \qquad \ell\in\mathbf Z_{\ge0},
   \tag{9}
   \]
   gives the exact next top quotient
   \[
   \boxed{
   m'=\sigma_k+A\ell.
   }
   \tag{10}
   \]

Consequently every current ordinary block has exactly four complete continuation cylinders in its one unbounded top quotient. Each continuation has the mixed-radix form

\[
\boxed{
\rho_k+2^{11(t+33)}\ell
\longmapsto
\sigma_k+3^G\ell.
}
\tag{11}
\]

No future tower type is preloaded: for an actual ordinary `m`, at most one of the four distinct residues in `(8)` can occur.

## Proof

### Unique ternary lift

For a fixed following type `k`, `L-8506` gives exactly two next source blocks, occupying the two nonzero residue classes modulo three. The current output core `\widehat S_(j,nu)` is coprime to three. Hence exactly one next lift has the same ternary residue, proving `(2)`.

### Shared binary signature

The current output has physical boundary word

\[
2^j3^{\beta_i}\widehat S_{j,\nu}
\equiv p_j\pmod {64}.
\]

Every next source block at the state `(t+16,beta_i,j)` has the same physical source marker,

\[
2^j3^{\beta_i}\widehat R'_{k,\mu}
\equiv p_j\pmod {64}.
\]

Since `3^(beta_i)` is odd, subtraction shows

\[
2^{6-j}\mid
\widehat R'_{k,\mu}-\widehat S_{j,\nu}.
\]

Together with `(2)`, this proves divisibility by `g_j` and hence integrality of `(5)`.

### Exact cancellation of the next modulus

The complete next source modulus is

\[
3\,2^{D'+6}.
\]

The coefficient of `m` in `(1)` is

\[
g_jA=3\,2^{6-j}A.
\]

After dividing the common factor `g_j`, the remaining modulus is

\[
\frac{3\,2^{D'+6}}{3\,2^{6-j}}
=2^{D'+j}
=2^{11(t+33)},
\]

which proves `(4)`.

Because `A` is odd, it is a unit modulo `H_t`. Thus the next-block congruence

\[
\widehat S_{j,\nu}+g_jAm
\equiv
\widehat R'_{k,\mu(k)}
\pmod {g_jH_t}
\]

has the unique solution `(6)` modulo `H_t`. This proves `(8)` and the integrality of `(7)`.

### Nonnegative carry

The next canonical source block satisfies

\[
0\le \widehat R'_{k,\mu}<g_jH_t,
\]

while `widehat S_(j,nu)>0`, `rho_k>=0`, and `g_jA>0`. Therefore the numerator in `(7)` is strictly greater than `-g_jH_t`. It is divisible by `g_jH_t`; its quotient is consequently nonnegative.

### High-tail transport

Substitute `(9)` into `(1)`:

\[
\begin{aligned}
C'
&=\widehat S_{j,\nu}+g_jA(\rho_k+H_t\ell)\\
&=\widehat R'_{k,\mu(k)}
  +g_jH_t\sigma_k
  +g_jH_tA\ell.
\end{aligned}
\]

Since `g_jH_t=3*2^(D'+6)` is the complete next source modulus, the next top quotient is exactly `(10)`.

Finally, if two different target types had the same `rho`, the same ordinary output would lie in two distinct complete next source blocks. Their physical residues modulo `64` are `p_k` and `p_(k')`, which are distinct. This is impossible. The four residues are therefore distinct. ∎

## Constructive meaning

The local eight-block compiler is not followed by another eight-way oracle. Ternary compatibility is forced, and the binary type correction cancels from the changing modulus. The complete unresolved top boundary is one ordinary quotient with four exact residue choices modulo the single power

\[
2^{11(t+33)}.
\]

This is the same structural object isolated independently in PR #51's negative-three-cycle run-core chart: one changing dyadic cylinder, one odd multiplicative refund, and one canonical top-boundary carry.

## Gap audit

- Four exact continuation cylinders do not prove that one finite quotient hits one of them at every future scale.
- The map `(11)` is an ordinary finite transition, but an infinite branch still requires one all-time top-boundary invariant.
- Distinctness of the four residues is not coverage of all residues.
- No finite-state or measure argument is used to replace ordinary realization.
