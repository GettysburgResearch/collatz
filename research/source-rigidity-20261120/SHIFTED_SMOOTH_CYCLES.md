# Complete cycle exclusion in the shifted two-prime class

**PROPOSED, elementary cycle theorem.** The only positive odd Collatz cycle
whose every shifted value `n+1` is `{2,3}`-smooth is `{1}`. The exact
within-class basin of 1 has seven elements. An additional, explicitly
source-qualified corollary proves convergence for an orbit eventually
confined to this shifted class.

No result here proves that an arbitrary ordinary orbit enters or stays in
the class. In particular, starting with a smooth shifted value does not
justify assuming that the next one is smooth.

## 1. Actual map, class, and compressed index

Use the positive odd map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

Let

\[
\mathcal S=\{2^s3^t-1:s\ge1,\ t\ge0\}.
\tag{1}
\]

Its elements are positive odd ordinary integers. For a state in this
class, its unique exponents define the index `k=s+t`.

If `s>=2`, then `v_2(3n+1)=1` and

\[
U(n)+1=2^{s-1}3^{t+1}.
\tag{2}
\]

Thus precisely `s-1` consecutive valuation-one steps lead to the
boundary state

\[
N_k=2\cdot3^{k-1}-1.
\tag{3}
\]

The index stays `k` throughout that run. At the boundary, put

\[
b=b(k)=v_2(3^k-1)\ge1.
\]

The next actual odd value and its shift are

\[
U(N_k)=\frac{3^k-1}{2^b},\qquad
U(N_k)+1=\frac{3^k+2^b-1}{2^b}.
\tag{4}
\]

The boundary division exponent for `3N_k+1` is `b+1`; it must not be
confused with `b`.

If the successor remains in `S`, write its shift as `2^{s'}3^{t'}`,
with `s'>=1,t'>=0`, and let `k'=s'+t'`. Its exact necessary equality is

\[
3^k+2^b-1=2^{b+s'}3^{t'}.
\tag{5}
\]

Following its next valuation-one run gives the next boundary index `k'`.

## SS1. Every class-preserving boundary transition above 15 increases the index

**Claim.** If `k>=16` and the successor in (4) belongs to `S`, then
`k'>k`.

**Proof.** First,

\[
b(k)=\begin{cases}1,&k\text{ odd},\\
2+v_2(k),&k\text{ even}.
\end{cases}
\tag{6}
\]

For odd `k` this follows modulo four. For even `k=2^v u`, with `u` odd,
factoring out the odd geometric sum reduces the valuation to that of
`3^{2^v}-1`. At `v=1` it is three. Every subsequent squaring introduces
the factor `3^{2^v}+1`, whose valuation is one, proving (6).

Let `v=floor(log_2 k)>=4`. Then `b<=v+2<k`. Also

\[
v_3(2^b-1)<b<k,
\]

since `0<2^b-1<3^b`. Taking the 3-adic valuation of (5) consequently
gives

\[
t'=v_3(2^b-1)\le b-1.
\tag{7}
\]

If `k'<=k`, then (5) and (7) imply

\[
3^k<2^{b+s'}3^{t'}
=2^{b+k'}(3/2)^{t'}
\le2^{b+k}(3/2)^{b-1}
=2^{k+1}3^{b-1}.
\tag{8}
\]

The opposite strict inequality holds for all `k>=16`. The base

\[
(3/2)^{16}>2\cdot3^5
\]

is exactly the integer certificate `3^{11}=177147>131072=2^{17}`.
If `(3/2)^{2^v}>2*3^{v+1}`, squaring proves
`(3/2)^{2^{v+1}}>2*3^{v+2}` because `2*3^v>1`. Hence, throughout
the dyadic block `2^v<=k<2^{v+1}`,

\[
(3/2)^k\ge(3/2)^{2^v}>2\cdot3^{v+1}
\ge2\cdot3^{b-1}.
\tag{9}
\]

This contradicts (8). QED.

This is a monotonicity theorem for class-preserving transitions, not a
claim that all boundary transitions preserve the class. Large admissible
indices need not be enumerated or bounded to use it in a finite cycle.

## SS2. The complete small table and the cycle theorem

For `1<=k<=15`, factor the exact successor shift in (4) as
`2^{s'}3^{t'}q'`, where `(q',6)=1`. The full table is:

| `k` | `b` | `s'` | `t'` | `q'` | Next boundary index when `q'=1` |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 1 | 1 |
| 2 | 3 | 1 | 0 | 1 | 1 |
| 3 | 1 | 1 | 0 | 7 | — |
| 4 | 4 | 1 | 1 | 1 | 2 |
| 5 | 1 | 1 | 0 | 61 | — |
| 6 | 3 | 2 | 0 | 23 | — |
| 7 | 1 | 1 | 0 | 547 | — |
| 8 | 5 | 1 | 0 | 103 | — |
| 9 | 1 | 1 | 0 | 4921 | — |
| 10 | 3 | 1 | 0 | 3691 | — |
| 11 | 1 | 1 | 0 | 44287 | — |
| 12 | 4 | 6 | 1 | 173 | — |
| 13 | 1 | 1 | 0 | 398581 | — |
| 14 | 3 | 4 | 0 | 37367 | — |
| 15 | 1 | 1 | 0 | 3587227 | — |

**Theorem.** Every positive odd cycle contained in `S` is `{1}`.

**Proof.** Compress each finite valuation-one run as in (2)–(4). Such
runs always finish, so a finite cycle produces a finite cyclic list of
boundary indices. If its largest index is at least 16, SS1 makes the
next index strictly larger, a contradiction. All its indices are
therefore at most 15. The table permits only

\[
4\longmapsto2\longmapsto1\longmapsto1.
\]

The only cycle in this list is `1`. Its ordinary odd boundary state is
`N_1=1`, and `U(1)=1`. QED.

For the shortcut map, this is the usual positive cycle `1,2`.
No estimate from a finite census of arbitrary source heights is used:
SS1 handles every larger index, and the table covers the finite
complement of its explicit range.

## SS3. The exact basin of 1 while remaining in the class

**Theorem.** The positive odd starts whose entire path up to its first
visit to 1 remains in `S` are precisely

\[
\boxed{\{1,3,5,15,23,35,53\}.}
\tag{10}
\]

**Proof.** A finite class-preserving path to 1 cannot have a boundary
index at least 16, because subsequent admissible boundary indices
strictly increase and can never reach 1. The table forces each boundary
index to be `1`, `2`, or `4`. The initial index equals its first boundary
index. All initial exponent pairs therefore have `s+t` in `{1,2,4}`.
Enumerating these seven pairs gives exactly (10). Conversely (2) and
the small table give their complete paths, with the longest being

\[
15\to23\to35\to53\to5\to1.
\]

Thus every listed path remains in the class and terminates. QED.

This elementary statement classifies finite within-class convergence;
it does not alone exclude an infinite class-preserving path with
strictly increasing large indices.

## SS4. Eventual confinement now implies arrival at 1

**SOURCE-QUALIFIED corollary.** Add SC3 from
`SHIFTED_CORE_TRANSITIONS.md`, frozen at SHA-256
`f53846e08e1522058797c6cab57111cf9c7ed4385f39b0e055ab05264f7acb71`.
That theorem, using Evertse's S-unit finiteness theorem, proves that
an actual ordinary orbit eventually confined to a finite shifted prime
pool is eventually periodic. In the particular pool `{2,3}`, SS2
identifies that eventual cycle as `{1}`. Therefore:

\[
\boxed{\text{If every sufficiently late }n_j+1\text{ is }\{2,3\}
\text{-smooth, then the orbit reaches }1.}
\tag{11}
\]

In particular, an orbit confined to `S` from time zero starts at one of
the seven values in (10). This last all-time assertion uses SC3 in
addition to the elementary finite-path classification.

There is also an explicit, enormous hit-or-exit deadline. Using SC4
from `BOUNDED_CORE_HORIZON.md`, frozen at SHA-256
`48b87b072ebd2a8e31f6767efd300d42df3599c10efdd9c82543eae2d266dec8`,
with `P={2,3}`, `K=1`, and core set `Q={1}`, put

\[
B_2=(9\cdot2^{35})^{81},\qquad
\ell=\lceil\log_2(n_0+1)\rceil,\qquad
H=\ell\bigl(2^{B_2+1}-1\bigr).
\tag{12}
\]

Within at most `H` actual odd transitions, the orbit either visits 1
or has a shifted value with a prime factor outside `{2,3}`. If the
source is already outside `S`, the exit is at time zero. Otherwise,
if no exit occurs by that horizon, SC4 forces a repeated state. The
resulting cycle lies inside `S`, hence is `{1}` by SS2; 1 has therefore
already been visited within the same horizon. No additional cycle
length needs to be added to (12).

The only external theorem in this corollary is the dependency of
SC1–SC4: Evertse, *The number of solutions of decomposable form
equations*, Theorem 3, printed page 7, at the
[primary author PDF](https://pub.math.leidenuniv.nl/~evertsejh/95-decforms.pdf).
The argument does not use the optional compressed-word strengthening
from PR145 and does not evaluate the astronomical integer `H`.

## Scope and verification

The elementary cycle theorem and seven-state finite basin are independent
of S-unit finiteness. The eventual-confinement and uniform deadline
corollaries explicitly retain that external dependency. An exit from the
class can increase the ordinary value and does not certify convergence.
Nothing here proves that every initial state `2^s3^t-1` reaches 1 after
it exits, nor that an arbitrary Collatz orbit is eventually confined to
this class.

`check_shifted_smooth_cycles.py` reconstructs the complete 15-row table,
the seven terminating paths, the exact run formulas, and the integer
inequality used for the unbounded dyadic induction. It also checks
selected larger valuation instances and a negative control showing
that SS1 fails when the requirement `q'=1` is dropped. Those checks
do not prove the external S-unit theorem or replace the written
universal induction.
