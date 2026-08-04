# L-8407 — Intrinsic phase-core and top-boundary normal form

Claim ID: `L-8407`  
Title: The six-branch pulse chart has one intrinsic prime-to-six core and one exact nineteen-bit ordinary top quotient  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-23  
Dependencies: `L-8405`; elementary valuation arithmetic  
Scope: every positive ordinary path in the `(L,b)=(6,1)` negative-three-cycle pulse chart  
Related counterexample candidates: none

## 1. Frozen six-branch chart

Use the exact chart of `L-8405`

```text
M=2^19,
N=9^6=3^12,
M h_(n+1)=N h_n+C_(i_n),
i_n in {0,...,5}.
```

The branch data are

| `i` | word | domain `d_i` | output `e_i` | `C_i=M e_i-N d_i` |
|---:|:---|---:|---:|---:|
| 0 | `AAAAAB` | 360448 | 365367 | 688128 |
| 1 | `AAAABA` | 471040 | 477468 | 774144 |
| 2 | `AAABAA` | 267776 | 271431 | 870912 |
| 3 | `AABAAA` | 366784 | 371790 | 979776 |
| 4 | `ABAAAA` | 19416 | 19683 | 1102248 |
| 5 | `BAAAAA` | 349523 | 354294 | 1240029 |

They satisfy

\[
\boxed{
\nu_2(d_i)=15-3i,
\qquad
\nu_3(e_i)=2i+1,
}
\tag{1}
\]

and

\[
\boxed{
C_i=21\,2^{15-3i}3^{2i}.}
\tag{2}
\]

Put

\[
 s_i={d_i\over 2^{15-3i}}
 =(11,115,523,5731,2427,349523)_i.
\tag{3}
\]

## 2. Intrinsic binary and ternary phase signatures

Assume that the boundary `h_n` was produced by type `r=i_(n-1)` and is about to use type `i=i_n`. Then

\[
 h_n\equiv d_i\pmod {2^{19}},
\qquad
 h_n\equiv e_r\pmod {3^{12}}.
\tag{4}
\]

Since the valuations in `(1)` are strictly below the ambient powers,

\[
\boxed{
\nu_2(h_n)=15-3i,
\qquad
\nu_3(h_n)=2r+1.}
\tag{5}
\]

Thus both phase labels are recovered from the ordinary integer itself:

\[
\boxed{
 i={15-\nu_2(h_n)\over3},
\qquad
 r={\nu_3(h_n)-1\over2}.}
\tag{6}
\]

Write uniquely

\[
\boxed{
h_n=2^{15-3i}3^{2r+1}u_n,
\qquad \gcd(u_n,6)=1.}
\tag{7}
\]

No externally trusted phase metadata remains.

## 3. Constant-toll core recurrence

Let the next type be `j=i_(n+1)`. Substituting `(2)` and `(7)` into the chart equation gives

\[
\boxed{
2^{19+3(i-j)}u_{n+1}
 =3^{12+2(r-i)}u_n+7.}
\tag{8}
\]

The displayed exponents lie in the finite ranges

```text
2 <= 12+2(r-i) <= 22,
4 <= 19+3(i-j) <= 34.
```

The relation with the maximal-run chart of PR #51 is exact. If

\[
R_n=5+i_n-i_{n+1}\in\{0,\ldots,10\},
\tag{9}
\]

then `(8)` is

\[
\boxed{
2^{4+3R_n}u_{n+1}=9^{R_{n-1}+1}u_n+7.}
\tag{10}
\]

Hence the fixed-weight macro chart is precisely the bounded-coboundary section

\[
R_n-5=i_n-i_{n+1}
\tag{11}
\]

of the negative-three-cycle run-core system.

## 4. The invariant seven split

Equation `(8)` proves

\[
\boxed{7\mid u_n\iff7\mid u_{n+1}.}
\tag{12}
\]

There are therefore two invariant ordinary sections.

### Section `g=1`

If `7` does not divide `u_n`, put

```text
g=1,
c_n=u_n,
delta=7.
```

### Section `g=7`

If `7` divides `u_n`, put

```text
g=7,
c_n=u_n/7,
delta=1.
```

In both cases

\[
\boxed{
2^{E_n}c_{n+1}=3^{A_n}c_n+\delta,}
\tag{13}
\]

where

\[
 A_n=12+2(i_{n-1}-i_n),
\qquad
 E_n=19+3(i_n-i_{n+1}).
\tag{14}
\]

Moreover

\[
\boxed{\gcd(c_n,c_{n+1})=1.}
\tag{15}
\]

For `delta=1` this is immediate. For `delta=7`, a common divisor must divide seven, while this section has `7` not dividing `c_n`.

## 5. Exact intrinsic source cells

For a phase pair `(r,i)` and section `g`, put

\[
 B_i=2^{4+3i},
\qquad
 s_g={21\over g}\in\{21,3\}.
\tag{16}
\]

The full physical source condition `h congruent d_i modulo M` is equivalent to

\[
\boxed{
 c\equiv
 s_i\bigl(3^{2r+1}g\bigr)^{-1}\pmod {B_i}.}
\tag{17}
\]

Together with the prime-to-`3` condition, and with the prime-to-`7` condition in the `g=1` section, this gives exactly

```text
phi(21)=12 cells modulo 21*B_i in section g=1;
phi(3)=2 cells modulo 3*B_i in section g=7.
```

Denote one such least residue by `a_(r,i,g,mu)` and its modulus by

\[
 H_{i,g}=s_g B_i.
\tag{18}
\]

Every ordinary core in that cell is uniquely

\[
\boxed{c=a_{r,i,g,\mu}+H_{i,g}q,
\qquad q\in\mathbf Z_{\ge0}.}
\tag{19}
\]

The integer `q` is the exact most-significant remainder after all finite binary, ternary, and seven-signature data have been removed.

## 6. The nineteen-bit top-boundary transition

Fix a current cell `(r,i,g,mu)` and a proposed next type `j`. The finite-place residue of `(13)` selects exactly one compatible next cell `(i,j,g,mu')`; call its least residue `a'`.

Put

\[
 A=12+2(r-i),
\qquad
 E=19+3(i-j).
\tag{20}
\]

Because

\[
 2^E H_{j,g}=2^{19}H_{i,g}=M H_{i,g},
\tag{21}
\]

the constant

\[
\boxed{
\kappa={3^A a+\delta-2^E a'\over H_{i,g}}
\in\mathbf Z}
\tag{22}
\]

is integral, and the complete ordinary transition becomes

\[
\boxed{M q'=3^Aq+\kappa.}
\tag{23}
\]

Thus exactly one nineteen-bit quotient block is consumed at every macro step. Define

\[
\rho=[-\kappa 3^{-A}]_M,
\qquad
\sigma={3^A\rho+\kappa\over M}.
\tag{24}
\]

Then

\[
\boxed{
q=\rho+M\ell
\quad\Longleftrightarrow\quad
q'=\sigma+3^A\ell,
\qquad \ell\in\mathbf Z.}
\tag{25}
\]

This is the exact top-boundary refund law. The next phase is an output of the current ordinary core; no future directive, inverse-limit digit, or hidden logarithm is supplied.

## 7. Deterministic intrinsic decoder

Given one finite ordinary state `(r,i,g,c)` satisfying an intrinsic cell, compute

\[
 X=3^{12+2(r-i)}c+\delta.
\tag{26}
\]

Let `v=nu_2(X)`. A next macro exists precisely when

\[
\boxed{
 j=i+{19-v\over3}\in\{0,\ldots,5\}}
\tag{27}
\]

and

\[
 c'=X/2^v
\tag{28}
\]

lies in one of the exact next cells for `(i,j,g)`. When it exists, the next state is uniquely

```text
(i,j,g,c').
```

The corresponding physical ordinary integer is

\[
\boxed{
n=2^{16-3i}3^{2r+1}g c-5.}
\tag{29}
\]

If the decoder is defined forever, `(29)` initializes an exact positive Collatz orbit. Every six-block macro has multiplier `N/M>1`, so the physical boundaries are strictly increasing and unbounded.

## Strategic meaning

The ordinary top boundary is no longer an informal carry-flush obligation. It is the single finite integer `q` in `(19)`, updated by the exact changing-affine law `(25)` after one nineteen-bit cylinder test.

The result does not prove that any finite `q` survives forever. It proves that a successful counterexample needs no additional infinite object once such a state is found.

## Gap audit

- The phase signatures alone are insufficient; the full cells `(17)` are essential.
- A compatible `2`-adic path need not have a finite ordinary `q`.
- Pairwise quotient refunds do not imply all-time definedness.
- No counterexample is claimed.