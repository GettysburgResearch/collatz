# Two completions and growing-resolution renewal: direct closing attempts

**23 November 2026. Status: written calculations and a scoped failed
application, not an exclusion of an escaping positive integer orbit.**

This route tries to bring a global Diophantine theorem to the actual
integer source, then tries a joint real/ternary renewal estimate at the
precision carried by that source. The calculations below retain the
integer throughout. They identify why these particular applications do
not close. No new analytic theorem is assumed or installed as a Lean
axiom.

## 1. One orbit, a positive real limit, and a negative 2-adic limit

Let `q_0=p` be a positive odd integer, and let

\[
2^{g_j}q_{j+1}=3q_j+1,\qquad
A_0=0,\qquad A_j=\sum_{i<j}g_i.
\tag{1}
\]

Here the gaps are the exact positive 2-adic valuations, not independent
random variables. Define the integer correction and its rational value
by

\[
C_j=\sum_{i<j}3^{j-1-i}2^{A_i},\qquad
R_j=C_j/3^j=\sum_{i<j}\frac{2^{A_i}}{3^{i+1}}.
\tag{2}
\]

The affine identity is

\[
2^{A_j}q_j=3^jp+C_j.
\tag{3}
\]

For the real convergence calculation, retain explicitly the premise

\[
\sum_{j\ge0}\frac1{q_j}<\infty.
\tag{4}
\]

The preceding repository's ordinary path-product input supplies this
premise on the retained nonperiodic component; it is not reproved here.
The elementary deduction from it is

\[
p+R_j=\frac{2^{A_j}q_j}{3^j}
=p\prod_{i<j}\left(1+\frac1{3q_i}\right)
\longrightarrow p+L<\infty,
\tag{5}
\]

where `L>0`. Thus the series in (2) converges to `L` in the real
completion. In the 2-adic completion, (3), oddness of `q_j`, and
`A_j>=j` instead give

\[
R_j\longrightarrow-p\quad\text{in }\mathbb Q_2,
\qquad |C_j+p3^j|_2=2^{-A_j}.
\tag{6}
\]

The two limits are in different fields. In particular this argument
does not identify `L` with the rational number `-p`, or establish that
`L` is algebraic.

## 2. The exact product in the proposed Subspace Theorem application

For `j>=1`, `C_j` is odd, and `C_j` is a unit modulo three: its last
summand is `2^(A_(j-1))`, while all the preceding summands are divisible
by three. Therefore

\[
\mathbf x_j=(C_j,3^j)
\]

is a primitive integer vector, with height comparable to `3^j` by (5).

Even if one additionally supposes that `L` is algebraic, the direct
two-dimensional application has the following independent pairs of
linear forms at the three places:

| Place | First form | Second form |
|---|---|---|
| real | `X-LY` | `Y` |
| 2-adic | `X+pY` | `Y` |
| 3-adic | `X` | `Y` |

Normalize `|ell|_ell=ell^(-1)`. The unnormalized product of the six
values is exactly

\[
\begin{aligned}
P_j
&=\prod_{v\in\{\infty,2,3\}}
  \prod_{a=1}^2|L_{a,v}(\mathbf x_j)|_v\\
&=|C_j-L3^j|\,2^{-A_j}\\
&=\sum_{k\ge0}\frac{2^{A_{j+k}-A_j}}{3^{k+1}}
\ge\frac13.
\end{aligned}
\tag{7}
\]

The real factor `3^j` from the form `Y` cancels its 3-adic factor;
the 2-adic smallness is exactly consumed by the real tail. All terms
in the last series are positive. Its first term is already `1/3`.

The relevant two-dimensional S-adic Subspace Theorem requires a
bound of the form `P_j <= C H(x_j)^(-epsilon)` for some fixed
`epsilon>0`, before it concludes that the vectors lie in finitely
many proper rational subspaces. Equation (7) does not meet that
hypothesis for arbitrarily large `j`, even under the extra algebraicity
supposition. Taking `-p` at the real place instead would give the
larger product `q_j`, not an improvement.

Subtracting any fixed number `s` of further tail terms does not create
the missing power saving either. With the same normalization, the
remaining positive real tail is at least

\[
\frac{2^{A_{j+s}-A_j}}{3^{s+1}}
\ge\frac{2^s}{3^{s+1}}>0.
\tag{8}
\]

A growing block and additional structure could lead to a different
Diophantine argument. Neither such structure nor the required
algebraicity is supplied by this calculation. The failure is scoped
to this direct approximation scheme; it is not a claim that every
Subspace Theorem route is impossible.

## 3. The other joint law: real and ternary affine limits

For the renewal test, the random reference law must be named separately.
Let independent positive integers `E_i` have probability `2^(-e)`, and
put

\[
\omega_k=3^k2^{-(E_1+\cdots+E_k)},\qquad
B_k=\sum_{i=1}^k3^{i-1}2^{-(E_1+\cdots+E_i)}.
\tag{9}
\]

This series has limits `R` in the reals and `Z` in the ternary
integers. These are not the series (2) or its two limits. The affine
maps here are `x -> (3x+1)/2^e` under the specified random law.

Brofferio's Poisson-boundary theorem applies to this rational affine
random walk: its drifts at the real, 2-adic and 3-adic places are
respectively

\[
\log3-2\log2<0,\qquad 2\log2>0,\qquad-\log3<0.
\tag{10}
\]

Thus its contracting boundary coordinates are real and ternary. Under
the classical tail tilt `P_*(E=e)=3/4^e`, the mean gap is `4/3` and
the real drift becomes positive, so only the ternary completion
contracts. This boundary identification concerns the random path
measure. It does not by itself bound a conditional density at every
specified positive integer.

The moving-fibre input from PR175, and the deductions already recorded
in this branch's [actual-window note](../../whole-repo-synthesis-20261122/entropy/CANONICAL_TIME_ENTROPY_ATTEMPT.md),
give the following consequence for a hypothetical retained escaping
ordinary orbit. For sufficiently large `j`, at a precision
`m_j=j+O_p(1)`, an event in a fixed proportional real band has mass
at least

\[
\mathbb P\{\eta q_j<R<(1-\delta)q_j,
              \ Z\equiv q_j\pmod{3^{m_j}}\}
\ge c_pq_j3^{-m_j},
\tag{11}
\]

for some fixed positive constants, with the constants and retained
inputs as specified in that note. This is a source-qualified premise
of the test, not a new unconditional trace theorem.

## 4. Testing every finite shell moment at the required precision

The source-qualified Theorem 16 of rStation paper 9/v2 gives, with
respect to full Haar probability on `Z_3`, the shell density

\[
s_B(z)\,dm_3(z)=\mathbb P\{B<R\le2B,\ Z\in dz\},
\qquad
\|s_B\|_r\le C_r B^{1-2/r}
                    [\log(eB)]^{1-1/r}
\tag{12}
\]

for every fixed finite `r>=1` and `B>=1`. The written theorem was
inspected; its analytic proof and other dependencies were not rebuilt
or formally certified here.

Cover the proportional band in (11) by a fixed number of dyadic
shells. At least one shell, with `B` comparable to `q_j`, retains a
fixed fraction of that lower mass. Hölder's inequality on its
depth-`m_j` cylinder then gives

\[
c_pq_j3^{-m_j}
\le C_{r,p}q_j^{1-2/r}[\log(eq_j)]^{1-1/r}
                         3^{-m_j(1-1/r)}.
\]

After rearranging,

\[
\boxed{q_j^2\le C_{r,p}3^{m_j}
                   [\log(eq_j)]^{r-1}.}
\tag{13}
\]

At `r=1` this is the earlier scalar-tail comparison. Larger finite
moments do not improve its exponential scale. In particular (13)
is compatible with the elementary orbit bound

\[
q_j+1\le(3/2)^j(p+1).
\tag{14}
\]

Taking `r` to grow is not justified by a theorem whose constants
depend on each fixed `r`. Even a successful passage to a uniform
all-cylinder `o(B)` shell bound would encounter the exact control
in the next section.

## 5. An explicit obstruction to the proposed uniform shell bound

Let `a_k=(3/2)^k` and `b_k=a_k-1`, for `k>=1`. On the event that
the first `k` gaps in (9) are all one,

\[
B_k=b_k,\qquad \omega_k=a_k,\qquad
R=b_k+a_kR',\qquad Z\equiv-1\pmod{3^k},
\tag{15}
\]

where `R'` is an independent copy of `R`. There is a fixed
`c_0= P(0<R'<=1/3)>0`: first restrict a further independent finite
real limit to a bounded set of positive probability, then choose
one sufficiently large first gap.

Since `a_k>=3/2`, the event `0<R'<=1/3` implies
`b_k<R<=2b_k`. Consequently the exact cylinder bound is

\[
\boxed{3^k\mathbb P\{b_k<R\le2b_k,
                      \ Z\equiv-1\pmod{3^k}\}
       \ge c_0(3/2)^k.}
\tag{16}
\]

For `k>=2`, we have `b_k>=1`, in the stated range of the shell-density
estimate (12). Its essential supremum is at least this cylinder
average. Thus, for `k>=2`,

\[
\|s_{b_k}\|_\infty\ge c_0(b_k+1).
\tag{17}
\]

An `o(B)` bound uniform over all ternary cylinders is therefore false.
This control is an elementary use of the negative fixed point of
`x -> (3x+1)/2`; it is not an integer Collatz counterexample, and
no novelty for that fixed point is claimed.

The least positive ordinary representative of this cylinder is
`3^k-1`, whereas its real shell has scale `(3/2)^k`. Their ratio
tends to infinity. Therefore (16) does **not** disprove a sharper
bound restricted to the positive ordinary diagonal in (11). It
shows why that arithmetic restriction cannot be dropped when
trying to obtain such a bound from renewal alone.

For an actual compatible prefix and an ordinary positive odd root `q`,
the same arithmetic restriction reads

\[
v=\frac{q-B_k}{\omega_k}\in\mathbb Z_{>0}.
\tag{18}
\]

When `B_k<q`, the affine equality forces the whole parity word,
so `v` is an actual positive integer predecessor of `q`. The
remaining diagonal estimate must control these particular
predecessors; the random boundary theorem does not erase them.
No such uniform diagonal estimate was proved in this attempt.

## Sources and status

- J.-H. Evertse, [The Subspace Theorem and p-adic generalizations,
  Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf),
  author lecture notes, May 2011, for the precise product/height
  hypothesis of the Schlickewei theorem tested in Section 2.
- Sara Brofferio, [The Poisson boundary of random rational
  affinities](https://www.numdam.org/article/AIF_2006__56_2_499_0.pdf),
  Annales de l'Institut Fourier 56 (2006), 499–515, main theorem
  for the random boundary identification used in Section 3.
- [Ternary Syracuse laws: real localization, clock stability, and
  critical regularity, paper 9/v2](https://rstation.ai/problems/collatz/papers/9/v2),
  Theorem 16 and Appendix B. This is a source-qualified 2026
  research manuscript, not presented here as an independently
  certified theorem.
- PR175 at `08fe1388ad63c758680b3695249aca319515c47d`,
  [MOVING_CESARO_FIBRES.md](https://github.com/GettysburgResearch/collatz/blob/08fe1388ad63c758680b3695249aca319515c47d/research/lean-global-closure-20261121/machinery/MOVING_CESARO_FIBRES.md),
  for the named ordinary trace and moving-fibre input.
- PR178 at `7e4569476e152f6b8537bdc1711df595ec1ffd89`,
  [CANONICAL_TIME_ENTROPY_ATTEMPT.md](https://github.com/GettysburgResearch/collatz/blob/7e4569476e152f6b8537bdc1711df595ec1ffd89/research/whole-repo-synthesis-20261122/entropy/CANONICAL_TIME_ENTROPY_ATTEMPT.md),
  for the retained path product and the actual ordinary
  normalized-fibre lower mass used in (4) and (11).

Equations (7), (8), (13), and (16) are written calculations of this
attempt. No Lean theorem count is attached to them. Their conclusion
is that the two proposed applications do not yet eliminate escape;
the unrestricted positive integer theorem remains open here.
