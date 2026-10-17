# Iteration 14: Tao--surplus rigidity for all-time supercritical Collatz orbits

All theorem-level claims remain `PROPOSED` pending independent reconstruction.
This iteration attacks one of the two exhaustive lanes left by the positive
coefficient-gate program.  It introduces no new symbolic architecture and no
bounded computation.

The result combines the exact shortcut affine identity with Tao's
almost-bounded-orbit theorem to eliminate the entire bounded-surplus face of the
all-time coefficient-supercritical lane.  More generally, any such ordinary
orbit must spend logarithmic density one of its times outside every fixed
surplus band.

## 1. Setup

Let

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\[1mm]
(3x+1)/2,&x\equiv1\pmod2
\end{cases}
\tag{1}
\]

be the shortcut Collatz map.  For a positive orbit put

\[
x_k=T^k(x_0),\qquad
v_k=x_k\bmod2,\qquad
q_k=\sum_{j=0}^{k-1}v_j.
\tag{2}
\]

Write

\[
\alpha={\log2\over\log3},\qquad
D_k=q_k-\alpha k.
\tag{3}
\]

Then

\[
{3^{q_k}\over2^k}=3^{D_k}.
\tag{4}
\]

The orbit is **all-time coefficient-supercritical** when

\[
D_k\ge0\qquad(k\ge0).
\tag{5}
\]

The exact affine expansion is

\[
\boxed{
 x_k
 =3^{D_k}x_0
 +{1\over2}\sum_{m=1}^k
 v_{m-1}3^{D_k-D_m}.
}
\tag{6}
\]

This follows by induction from

\[
x_{j+1}={3^{v_j}x_j+v_j\over2}.
\tag{7}
\]

## L-9532: bounded surplus gives two-sided linear orbit growth

**Claim ID:** `L-9532`  
**Title:** A bounded all-time supercritical surplus forces a linear-size orbit  
**Status:** `PROPOSED`  
**Dependencies:** the exact identity (6)  
**Scope:** positive ordinary shortcut-Collatz orbits

Assume that for some finite `B`,

\[
0\le D_k\le B\qquad(k\ge0).
\tag{8}
\]

Because `q_k>=alpha k`, equation (6) gives

\[
\begin{aligned}
x_k
&\ge {1\over2}\sum_{m=1}^k
  v_{m-1}3^{-B}\\
&={q_k\over2\,3^B}\\
&\ge {\alpha\over2\,3^B}k.
\end{aligned}
\tag{9}
\]

Likewise `D_k<=B` and `D_m>=0` give

\[
\begin{aligned}
x_k
&\le 3^Bx_0+{1\over2}\sum_{m=1}^k3^B\\
&\le 3^B\left(x_0+{k\over2}\right).
\end{aligned}
\tag{10}
\]

Hence there are positive constants `c,C`, depending only on `x_0,B`, such that

\[
\boxed{ck\le x_k\le C(k+1).}
\tag{11}
\]

In particular `x_k -> infinity`.  The orbit states are therefore distinct: a
repeated state would make the deterministic orbit periodic, contradicting
(11).

## 2. The ordinary exceptional set attached to one divergent orbit

For any shortcut orbit tending to infinity define its future minimum

\[
m_k=\min_{j\ge k}x_j.
\tag{12}
\]

Then `m_k -> infinity`.  Define a function on the positive integers by

\[
\boxed{
 f(N)={1\over2}
 \min\{m_k:x_k\ge N\}.
}
\tag{13}
\]

The set in (13) is nonempty for every `N`, because `x_k -> infinity`.
Furthermore `f(N)->infinity`: for fixed `K`, once `N` exceeds
`max_{k<K}x_k`, every index in (13) is at least `K`, and its future minimum is
at least `m_K`.

For each orbit state,

\[
f(x_k)\le {m_k\over2}<m_k.
\tag{14}
\]

Let `Col` denote the unshortened Collatz map, with odd step `3x+1`.  The
intermediate value `3x+1` is larger than both `x` and `(3x+1)/2`, so the minimum
of the unshortened orbit beginning at `x_k` equals the minimum of the shortcut
tail:

\[
\operatorname{Col}_{\min}(x_k)=m_k.
\tag{15}
\]

Consequently every `x_k` lies in the exceptional set

\[
\mathcal E_f=
\{N\ge1:\operatorname{Col}_{\min}(N)>f(N)\}.
\tag{16}
\]

Tao's theorem says that for every function `f(N)->infinity`, this exceptional
set has logarithmic density zero.

## T-9521: bounded-surplus all-time supercritical orbits do not exist

**Claim ID:** `T-9521`  
**Title:** Tao's almost-bounded theorem excludes every bounded-surplus all-time supercritical ordinary orbit  
**Status:** `PROPOSED / SOURCE-DEPENDENT`  
**Dependencies:** `L-9532`; Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), Theorem 1.3  
**Scope:** positive ordinary shortcut-Collatz orbits

Assume (8).  Put

\[
C_0=3^B\left(x_0+{1\over2}\right).
\tag{17}
\]

Then (10) implies

\[
x_k\le C_0(k+1).
\tag{18}
\]

For

\[
X_N=C_0(N+1),
\tag{19}
\]

the distinct states `x_0,...,x_N` all lie below `X_N`.  Therefore

\[
\begin{aligned}
\sum_{\substack{n\le X_N\\n\in\mathcal E_f}}{1\over n}
&\ge
\sum_{k=0}^N{1\over x_k}\\
&\ge {1\over C_0}\sum_{k=0}^N{1\over k+1}\\
&={1\over C_0}\log N+O(1).
\end{aligned}
\tag{20}
\]

Since `log X_N=log N+O(1)`, the exceptional set has positive upper logarithmic
density.  This contradicts Tao's theorem.  Hence

\[
\boxed{
\text{no positive ordinary orbit satisfies }
0\le D_k\le B\text{ for all }k.
}
\tag{21}
\]

In particular, any all-time coefficient-supercritical ordinary orbit must have

\[
\boxed{\sup_kD_k=+\infty.}
\tag{22}
\]

This eliminates the full bounded-bank regime, not merely periodic, automatic,
Sturmian, or finite-state examples within it.

## 3. Full divergence and logarithmic sparsity of every low-surplus band

For completeness, the elementary low-band argument is included here rather
than imported from a neighboring branch.

Put

\[
a=1-\alpha.
\tag{23}
\]

Fix `H>0`.  If `D_k<H` infinitely often, then there are infinitely many odd
endpoints `m` with

\[
v_{m-1}=1,\qquad D_m<H+a.
\tag{24}
\]

Indeed, after any sufficiently late visit below `H`, some future odd step must
occur, or repeated even steps would force `D` below zero.  The first such odd
step ends below `H+a`.

At a later time `k` with `D_k<H`, every endpoint counted in (24) contributes at
least

\[
{1\over2}3^{-(H+a)}
\tag{25}
\]

to (6).  Thus repeated returns to the low band force the low-band orbit values
to infinity.  If returns below `H` stop, the multiplicative term
`3^(D_k)x_0` remains above `3^H x_0`.  Letting `H` grow proves

\[
\boxed{
D_k\ge0\text{ for every }k
\quad\Longrightarrow\quad
x_k\longrightarrow+\infty.
}
\tag{26}
\]

Now fix `B>=0` and let

\[
I_B(N)=\{0\le k\le N:D_k\le B\}.
\tag{27}
\]

For `k in I_B(N)`, equation (6) gives the same upper bound

\[
x_k\le C_B(k+1),
\qquad
C_B=3^B\left(x_0+{1\over2}\right).
\tag{28}
\]

The function `f` from (13) is available by (26), and every orbit state remains
in `E_f`.  Therefore

\[
\sum_{\substack{n\le C_B(N+1)\\n\in\mathcal E_f}}{1\over n}
\ge
{1\over C_B}
\sum_{k\in I_B(N)}{1\over k+1}.
\tag{29}
\]

Tao's logarithmic-density-zero conclusion forces

\[
\boxed{
\sum_{\substack{0\le k\le N\\D_k\le B}}
{1\over k+1}
=o(\log N)
\qquad(N\to\infty).
}
\tag{30}
\]

## T-9522: surplus escape in logarithmic time density

**Claim ID:** `T-9522`  
**Title:** Every all-time supercritical ordinary orbit escapes each fixed surplus band in logarithmic time density  
**Status:** `PROPOSED / SOURCE-DEPENDENT`  
**Dependencies:** (6), (26), Tao's Theorem 1.3  
**Scope:** positive ordinary shortcut-Collatz orbits

Equation (30) says precisely that for every fixed `B`, the times with
`D_k<=B` have logarithmic density zero in the time variable.  Equivalently,

\[
\boxed{
D_k\longrightarrow+\infty
\quad\text{in logarithmic density.}
}
\tag{31}
\]

This is stronger than mere unboundedness.  It rules out every uniformly
supercritical candidate whose capital is recurrent in any bounded strip with
positive logarithmic frequency.

## R-9512: sharpened least-counterexample dichotomy

**Claim ID:** `R-9512`  
**Title:** A least counterexample's all-time supercritical lane must be high-surplus and logarithmically transient  
**Status:** `PROPOSED / CROSS-BRANCH`  
**Dependencies:** `T-9521`, `T-9522`; the coefficient-stopping gate in PR #76 only for the numerical delayed-crossing alternative

For a least positive Collatz counterexample, define the first coefficient
crossing

\[
\tau=\min\{k\ge1:3^{q_k}<2^k\},
\tag{32}
\]

with `tau=infinity` when no crossing occurs.

The positive coefficient-gate packet proposes

\[
\tau=\infty
\quad\text{or}\quad
\tau\ge217\,976\,794\,617.
\tag{33}
\]

The present theorem sharpens the first lane.  If `tau=infinity`, then the orbit
must satisfy all of

\[
\boxed{
\begin{aligned}
&x_k\to+\infty,\\
&\sup_kD_k=+\infty,\\
&\sum_{\substack{k\le N\\D_k\le B}}{1\over k+1}=o(\log N)
\quad\text{for every fixed }B.
\end{aligned}}
\tag{34}
\]

Thus the critical bounded-surplus mechanical regime is eliminated
architecture-independently.  The only remaining no-crossing candidate is a
genuinely high-surplus ordinary divergent orbit whose returns to every bounded
capital band are logarithmically negligible.

## Q-9516: next global offense

**Claim ID:** `Q-9516`  
**Title:** Exclude high-surplus all-time supercritical ordinary extraction  
**Status:** `IDEA`

The remaining `tau=infinity` theorem is now:

\[
\boxed{
\text{No positive ordinary orbit can satisfy (5) and (31).}
}
\tag{35}
\]

A closing argument must use information unavailable to the bounded-surplus
proof, for example:

1. an architecture-specific least-root lower bound in the high-surplus tree;
2. an inverse-basin harmonic expansion contradicting Tao's logarithmic-density
   theorem even when the spine itself is sparse;
3. a derived `2`-adic approximant whose height saves a fixed factor beyond the
   exponent-one product-formula threshold;
4. a global return theorem forcing bounded-surplus visits with positive
   logarithmic time density.

Another proof that a legal no-crossing orbit grows does not advance (35): growth
is already part of the conclusion.

## Dependency and scope audit

- The only external theorem is Tao's logarithmic-density theorem.
- The function `f` in (13) may depend on the hypothetical orbit; Tao's statement
  applies to every function tending to infinity and imposes no computability or
  monotonicity requirement.
- Shortcut and unshortened orbit minima agree because an odd unshortened
  intermediate value is `3x+1`, larger than the following shortcut value.
- Positive upper logarithmic density in (20) is enough to contradict logarithmic
  density zero.
- No ordinary root is extracted and no proof of Collatz is claimed.
- The theorem closes a complete dynamical subregime of the all-time
  supercritical lane, and is therefore strictly weaker than Collatz.