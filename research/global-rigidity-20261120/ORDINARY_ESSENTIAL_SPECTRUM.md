# Ordinary essential spectrum on certified convergent basins

**PROPOSED; exact written argument and finite rational certificates.**
This is not a Collatz proof, a diagonal-moment bound, or an exclusion of
nontrivial positive cycles. The main result is an unconditional obstruction:
the entire unit circle belongs to the essential approximate point spectrum
of the particular ordinary operators used in PR143 and PR144, already on
states whose convergence to 1 is certified by their construction.

The root/pressure collaboration supplied the disjoint convergent-basin
construction and independently reconstructed its arithmetic. The compact
comparison, whole-circle extension, finite-support construction, and exact
certificate interface are developed here. No literature-priority claim is
made for weighted-composition or approximate-spectrum arguments.

## 1. Maps, spaces, and frozen inputs

Let `O` be all positive odd integers, including multiples of 3. Put

\[
 a(n)=v_2(3n+1),\quad U(n)=\frac{3n+1}{2^{a(n)}},\quad
 d(n)=\frac3{2^{a(n)}},\quad c(n)=\frac{3n}{3n+1}.
\]

For `s=1,2`, on the ordinary Hilbert space `l2(O)` define

\[
 (A_s f)(n)=d(n)^s f(U(n)),\qquad
 (B_s f)(n)=\left(\frac{U(n)}n\right)^s f(U(n)).       \tag{1}
\]

Thus `A_1` is PR143's `A`, and `A_2` is PR144's `R4`. No state is killed
in (1). In particular `U(1)=1` and `A_s f(1)=(3/4)^s f(1)`.
The inverse column sums are

\[
 z_s(t):=\sum_{Un=t}d(n)^{2s}
 =\begin{cases}
 0,&t\equiv0\pmod3,\\
 3/5,&s=1,\ t\equiv1\pmod3,\\
 12/5,&s=1,\ t\equiv2\pmod3,\\
 27/85,&s=2,\ t\equiv1\pmod3,\\
 432/85,&s=2,\ t\equiv2\pmod3.
 \end{cases}                                           \tag{2}
\]

Indeed the positive odd predecessors are `(2^a t-1)/3`, with positive
even `a` for `t=1 mod3`, positive odd `a` for `t=2 mod3`, and none for
`3|t`. Summing geometric series proves (2). Consequently both `A_s` are
bounded. Since `3/4 <= c(n)<1` and `B_s=M_{c^{-s}}A_s`, both `B_s` are
bounded as well.

Source pins:

- PR143, `41a408e5e617fb4e65142485f6f3ff3e6ef6c408`,
  `research/pressure-decay-20261031/PROOF.md`, PF-002, and
  `ENERGY.md`, PF-006--008.
- PR144, `df756794e1d8de5cabff148ef433df505e3b68b4`,
  `research/pressure-diagonal-20261031/PROOF.md`, D1--D6, and
  `DISSIPATION.md`, L1--L4.
- PR149, `92c0129e794dde3ec55ceec470a12d51ba3f7e2f`,
  `research/asymptotic-inverse-operator/ASYMPTOTIC_OPERATOR.md`,
  inspected for the comparison in section 8.

The main essential-spectrum theorem below does **not** use a packing
theorem, a harmonic trace, a conjectural escape, or an external density
theorem. A separate corollary in section 7 identifies its packing input.

## 2. OE1: an explicit compact comparison, at the trace-class boundary

Set `K_s=B_s-A_s`. Different columns of `K_s` have disjoint supports:
column `t` is supported on the fiber `U^{-1}{t}`. Thus its nonzero
singular values are precisely the column norms, rearranged in decreasing
order. For `s=1` these are

\[
 k_1(t)^2=\sum_{\substack{a\ge1\\2^a t\equiv1\ (3)}}
 \frac9{4^a(2^a t-1)^2}.                                \tag{3}
\]

For `s=2`, the corresponding formula is

\[
 k_2(t)^2=\sum_{\substack{a\ge1\\2^a t\equiv1\ (3)}}
 \left\{\frac9{4^a}
 \left[\left(1-\frac1{2^a t}\right)^{-2}-1\right]\right\}^{2}.
                                                               \tag{4}
\]

Both are zero when `3|t`. Write `a0=2` for `t=1 mod3` and `a0=1` for
`t=2 mod3`. Direct geometric summation gives

\[
 \frac{\alpha(t)}t\le k_1(t)
 \le\frac{\alpha(t)}{t(1-2^{-a0}/t)},\qquad
 \alpha(t)=\begin{cases}3/\sqrt{255}&t=1\ (3),\\
                       12/\sqrt{255}&t=2\ (3),\end{cases}       \tag{5}
\]

and

\[
 \frac{\beta(t)}t\le k_2(t)
 \le\frac{\beta(t)}{t(1-2^{-a0}/t)^2},\qquad
 \beta(t)=\begin{cases}18/\sqrt{4095}&t=1\ (3),\\
                       144/\sqrt{4095}&t=2\ (3).
             \end{cases}                                      \tag{6}
\]

For (5), factor each term in (3) as
`9/(16^a t^2) * (1-1/(2^a t))^-2`. For (6), use

\[
 1\le\frac{(1-z)^{-2}-1}{2z}
       =\frac{2-z}{2(1-z)^2}\le(1-z)^{-2}\quad(0<z<1).
\]

The inequalities also yield the convenient global bounds

\[
 k_1(t)<1/t,\qquad k_2(t)<3/t.                           \tag{7}
\]

For `t=1 mod3`, use `t>=1` and `a0=2`. For `t=2 mod3`, the least
positive **odd** target is 5, so `1-1/(2t)>=9/10`. The needed squared
constant comparisons are elementary; for example
`1600 < 9*255` and `1600^2 < 27^2*4095` cover the latter residue class.

Since the column norms tend to zero, truncating to finitely many target
columns approximates `K_s` in operator norm. Thus `K_s` is compact.
More precisely, the two nonzero target classes have natural density
`1/6` among positive integers, and (5)--(6) give

\[
 s_j(K_1)\sim\frac{5}{2\sqrt{255}}\frac1j,\qquad
 s_j(K_2)\sim\frac{27}{\sqrt{4095}}\frac1j.               \tag{8}
\]

To justify the rearrangement, if `k(t)~a_r/t` on each of finitely many
residue classes of density `delta_r`, then
`#{t:k(t)>lambda}~(sum delta_r a_r)/lambda` as `lambda down to0`.
Inverting this counting asymptotic gives (8). In particular `K_s` is
in every Schatten class `S_p`, `p>1`, and is not trace class. This
precise trace-class boundary is not needed for the theorem below;
compactness suffices.

## 3. OE2: disjoint basins with arbitrarily small root leakage

For each integer `k>=2`, define

\[
 h_k=3^{k-1},\quad m_k=\frac{2^{h_k}+1}{3^k},\quad
 n_k=2^k m_k-1,\quad
 t_k=2\,3^{k-1}m_k-1=\frac{2^{h_k+1}-1}{3}.             \tag{9}
\]

These are positive odd integers. The divisibility follows from
`v3(2^{3^{k-1}}+1)=k`. An elementary proof starts with `v3(2+1)=1`
and observes that, when `v3(x+1)=j>=1`,
`v3(x^3+1)=v3(x+1)+1`, because `x^2-x+1` has 3-adic valuation one.

For `0<=j<=k-1`, the ordinary states

\[
 x_{k,j}=2^{k-j}3^j m_k-1                               \tag{10}
\]

satisfy `x_{k,0}=n_k`, `x_{k,k-1}=t_k`. For `j<k-1`,

\[
 3x_{k,j}+1
  =2\left(2^{k-j-1}3^{j+1}m_k-1\right),
\]

and the factor in parentheses is odd. Thus every one of these `k-1`
odd steps has **exact** valuation one. Finally
`3t_k+1=2^{h_k+1}`, so `U(t_k)=1`. Every displayed source is therefore
proved convergent. Since `k>=2`,

\[
 0<\frac{n_k}{t_k}<\left(\frac23\right)^{k-1}.           \tag{11}
\]

The inequality follows by comparing `(am-1)/(bm-1)` with `a/b` when
`b>a>0`. The roots `t_k` are distinct and larger than 1.

Let

\[
 C_k=\{x\in O:U^j(x)=t_k\text{ for some }j\ge0\}.
\]

All members of `C_k` converge to 1. Distinct `C_k` are disjoint:
after reaching one of their roots an orbit goes directly to 1 and
never visits another root. Each member has a unique first-hit odd
depth `ell_k(x)` to `t_k`; except at the root,
`ell_k(Ux)=ell_k(x)-1`.

Put

\[
 S_{k,s}=\sum_{x\in C_k}x^{-2s},\qquad
 f_{k,s,z}(x)=\frac{z^{-\ell_k(x)}1_{C_k}(x)}
                    {x^s\sqrt{S_{k,s}}},\quad |z|=1.           \tag{12}
\]

The sums are finite and positive because `s=1,2` and `n_k in C_k`.
For fixed `s,z`, these vectors are orthonormal. Away from the root,
`B_s f=z f`. Outside `C_k`, no source can have its parent in `C_k`.
At the root `B_s f(t_k)=0`, since `1` is outside `C_k`. Hence

\[
 \|(B_s-zI)f_{k,s,z}\|
 =\frac1{t_k^s\sqrt{S_{k,s}}}
 \le\left(\frac{n_k}{t_k}\right)^s
 <\left(\frac23\right)^{s(k-1)}.                         \tag{13}
\]

No full Collatz hypothesis, ordinary-basin decision oracle, or infinite
trajectory assumption entered this construction.

## 4. OE3: the whole unit circle is essential approximate spectrum

**Theorem.** For each `s=1,2` and every complex `z` with `|z|=1`, there
is an orthonormal sequence in the basin of 1 satisfying

\[
 \|(A_s-zI)f_{k,s,z}\|\longrightarrow0.                  \tag{14}
\]

Consequently `A_s-zI` is not Fredholm, even after restricting the
operator to its reducing subspace `l2({x: x reaches1})`.

**Proof.** A compact operator sends an orthonormal sequence to zero
in norm. Apply this to `K_s` and use (13):

\[
 \|(A_s-zI)f_{k,s,z}\|
 \le\|(B_s-zI)f_{k,s,z}\|+\|K_s f_{k,s,z}\|\to0.
\]

The basin of 1 is reducing because membership is unchanged across
every forward edge. A Fredholm operator is bounded below on the
orthogonal complement of its finite-dimensional kernel, whereas
an orthonormal sequence is weakly zero. Thus (14) contradicts
Fredholmness. This proves the asserted essential approximate spectrum.

The compact term's norm does not depend on `z`, because the columns
are disjoint and the absolute values of (12) do not depend on `z`.
The same root sequence therefore works for the entire circle.

### Exact eigenvectors are a different matter

On the basin of 1, `ker(A_s-zI)={0}` for every `|z|=1`. At 1 the
equation is `z f(1)=(3/4)^s f(1)`, so `f(1)=0`; propagating backwards
along any finite path to 1 gives `f(x)=0` everywhere in the basin.
Thus the approximate eigenvectors in (14) coexist with a trivial
exact eigenspace on their entire supporting basin.

In particular a spectral gap, bounded inverse, or Fredholm estimate
at 1 for these operators is unavailable **even if Collatz is true**.
This does not disprove PR144's specific-vector moment target
`D_q=||A_2^q(1/x)||_2^2=O(q^2)`. Nor does approximate unit-circle
spectrum alone decide strong convergence of powers or convergence
on a specified order interval. Those are different assertions.

## 5. OE4: finite supports and an exact all-predecessor certificate

The infinite basin vectors are not needed as numerical certificates.
Take a finite set `S subset C_k` containing `t_k` and closed under
`U` until that root. Define the unnormalised vector

\[
 g_{S,s,z}(x)=1_S(x)\,x^{-s}z^{-\ell_k(x)}.
\]

Every state in `S` has a finite, explicitly stored path to `t_k` and
then to 1. For **every** `|z|=1`,

\[
 \boxed{
 \frac{\|(A_s-zI)g_{S,s,z}\|_2^2}{\|g_{S,s,z}\|_2^2}
 =\frac{
 \displaystyle\sum_{t\in S}(1+z_s(t))t^{-2s}
 -2\displaystyle\sum_{x\in S\setminus\{t_k\}}
           c(x)^s x^{-2s}}
 {\displaystyle\sum_{t\in S}t^{-2s}}.}                    \tag{15}
\]

The phase cancellation is exact: along each inside edge
`g(Ux)=z*(x/Ux)^s g(x)`. The identity
`||A_s g||^2=sum_t z_s(t)|g(t)|^2` uses **all infinitely many**
ordinary predecessors through the exact geometric column sums (2).
The cross term is finite because `g` has finite support. Thus (15)
does not omit off-support predecessors. All quantities on its right
are rational, even though the certificate covers every unit complex
phase. For `z=1`, the unnormalised vector itself is rational.

An increasing exhaustion of `C_k` by finite inverse trees gives
`g_S -> 1_{C_k}z^{-ell}/x^s` in `l2`. Boundedness of `A_s` shows that
the normalised residuals converge to those of (12). Choosing distinct
roots and sufficiently large finite trees therefore also gives a
finitely supported orthonormal sequence satisfying (14).

### A terminating construction does not need to decide unknown orbits

Here is a finite-candidate search for any rational `eta>0` and either
`s`. Let `C_1=1,C_2=3`, the constants in (7). Choose `k0` so that
`(2/3)^{s(k0-1)}<eta/4`, and an integer `M>4 C_s/eta`.
Among any `ceil(M/2)+1` distinct basins with `k>=k0`, at least one
contains no positive odd integer at most `M`: the basins are disjoint
and there are only `ceil(M/2)` such integers. On that basin the norm
of `K_s` is at most `C_s/M<eta/4`, by its disjoint-column formula.
Consequently its infinite vector has residual less than `eta/2`.

Dovetail finite inverse-tree exhaustions for this finite collection of
roots and test (15) until a residual smaller than `eta` is certified.
At least one search terminates by the preceding `l2` approximation.
Every vertex admitted to every search has its explicit path to 1.
The procedure never asks whether an arbitrary uninspected integer
converges. No useful uniform complexity bound is asserted.

For an effective exhaustion, maintain the least unused predecessor
of each discovered unit target in a priority queue, ordered by its
ordinary value. When one is inserted, add its next same-parent
sibling (increase `a` by 2) and its own least predecessor if present.
Every prescribed vertex is eventually inserted: after its parent is
present, only finitely many positive integers precede it in the queue.
Uniqueness of `U` prevents duplicated vertices from different parents.

## 6. Finite certificates actually executed

`check_ordinary_spectrum.py` deterministically constructs 512-state
inverse trees for `k=6` and `k=8`. A separate verification pass
reconstructs every `U` edge by literal integer arithmetic, checks
depths and the root's immediate hit of 1, and evaluates (15) using
128-bit outward dyadic enclosures. Summands are evaluated with
integer division; decimal display is not part of acceptance.

The following strict rational upper bounds passed for the residual
norm, simultaneously for all `|z|=1`:

| Root parameter | States | `A_1` residual | `A_2=R4` residual |
|---|---:|---:|---:|
| `k=6` | 512 | `<93/1000` | `<16/1000` |
| `k=8` | 512 | `<41/1000` | `<31/10000` |

The report contains each support digest, exact integer enclosure,
maximum depth and root bit length. The large support integers are
regenerated, not stored as an enormous decimal dump. Domain and
direct semantic corruptions are rejected. These are finite exact
checks of the certificate interface, not the proof of arbitrary
accuracy or independent mathematical peer review.

## 7. OE5: the literal correction is a bounded coboundary on escape

This section uses the self-contained local packing lemma from PR150,
`ef4022fa5ae43dd943ecca0b7c84d69af624c5c9`,
`research/pointwise-closure-20261120/LOCAL_DISTORTION.md`, LD1--LD2:
every finite simple shortcut path has reciprocal sum smaller than
600. Its stated proof and review status are retained. Expanding a
simple odd path to shortcut steps preserves simplicity; otherwise a
repeated shortcut state would force repeated later odd states.

Set

\[
 r_q(n)=\prod_{j<q}c(U^j n),\qquad r(n)=\lim_q r_q(n).
\]

On every eventually periodic source, `r(n)=0`, since a positive
cycle supplies a repeated product smaller than one. On every
nonperiodic source its orbit is simple, and the packing lemma gives

\[
 e^{-200}\le r(n)\le1,\qquad r(n)=c(n)r(Un).              \tag{16}
\]

Let `N` be the union of actual nonperiodic components. Its coordinate
subspace is reducing. On `l2(N)`, multiplication by `r^s` is bounded
and boundedly invertible, and

\[
 \boxed{A_s=M_{r^s} B_s M_{r^{-s}}.}                     \tag{17}
\]

Thus the correction from `3n` to `3n+1` is a bounded diagonal
coboundary on a hypothetical escaping sector. This is a conditional
description of that sector, not a proof that it is empty.

In particular, for `u(n)=1/n`, `t_q=U^q(n)` and
`J_q=3^q/2^{sum_{j<q}a(U^j n)}`, the diagonal moment restricted to `N`
obeys the exact comparison

\[
 e^{-800}\sum_{n\in N}\frac{t_q(n)^2}{n^4}
 \le \sum_{n\in N}\frac{J_q(n)^4}{t_q(n)^2}
 \le\sum_{n\in N}\frac{t_q(n)^2}{n^4}.                   \tag{18}
\]

Indeed `J_q/t_q=r_q/n`, and `e^{-200}<=r_q<=1` on `N`.
These sums are finite for every finite `q` by the bounded operators.
The missing global moment estimate is therefore genuine control of
ordinary orbit heights with fixed original-source weights. The
compactness of `K_s`, or the positivity of the literal loss, does not
supply it. A separate regularity attempt and its exact failure are
recorded in `SMOOTHING_BOUNDARY.md`.

## 8. What is new here, and what remains open

PR143 PF-002 already classifies **exact** fixed vectors of `A_1` by
actual nonperiodic components, and supplies unit-circle eigenvectors
if such a component exists. That classification is not reproved as
a new result here. The present theorem constructs **approximate**
unit-circle vectors unconditionally, supported entirely on certified
convergent states, and proves a Fredholm obstruction even on that basin.

PR149 studies a different inverse Markov contraction on `l2(S,H/x)`.
Its finite-power essential norm is one even if Collatz is true, and
its strong asymptotic limit has nonzero blocks precisely when escape
exists. The present operators are the ordinary derivative-weighted
composition operators on unweighted `l2(O)`, requiring no harmonic
trace. The convergent-basin essential approximate spectrum, compact
comparison (3)--(8), and finite rational residual interface (15)
are the additional statements; PR149's norm-one truncation theorem
is not being repackaged as a discovery.

General functional-analytic approaches are established. Relevant primary
background includes M. Neklyudov, *Functional analysis approach to the
Collatz conjecture*, [arXiv:2106.11859v9](https://arxiv.org/abs/2106.11859v9),
and V. Béhani, *Linear dynamics of an operator associated to the Collatz
map*, [arXiv:2303.03203v1](https://arxiv.org/abs/2303.03203v1). Their
generating-function/Hardy/Bergman normalizations are not silently
substituted for (1). No theorem from either paper is a dependency of
the elementary proof above, and no exhaustive novelty search is claimed.

**First unsupported inference.** Neither a bound on the particular
all-source moment `D_q`, nor a regularity theorem excluding a nonzero
limit `r`, has been proved. The rigorous consequences are the compact
comparison, essential approximate spectrum, finite certificate family,
and bounded coboundary description. They do not exclude a single
nonperiodic positive orbit. They also do not exclude any additional
positive cycle; every eventual cycle has `r=0` in this normalization.
