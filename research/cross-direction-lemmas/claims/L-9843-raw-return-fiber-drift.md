# L-9843 — Positive affine-fiber drift over the raw H return rotation

Claim ID: `L-9843`  
Title: The `30/(60 or 70)` raw return has a positive additive fiber cocycle, exact mean drift, and zero Lyapunov exponent  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9841`  
Scope: the real affine skew product of the raw multiplier return architecture  
Related counterexample candidates: none

## Definitions

For the completed H suffix `r0`, put

\[
\mu_r=\frac{3^{2r+2}}{2^{3r+4}},
\qquad
q\longmapsto\mu_rq+\frac7{16}.
\tag{1}
\]

Use the exact constants from `L-9841`

\[
L=\frac98,
\qquad
\xi=\mu_3\mu_6=\frac{3^{22}}{2^{35}},
\qquad
\frac1L<\xi<1,
\tag{2}
\]

and let

\[
\mathcal I= (1,L].
\tag{3}
\]

One raw return consists of appending `30` and then appending `70` or `60`
according to

\[
r(R)=
\begin{cases}
7,&1<R\le\xi^{-1},\\
6,&\xi^{-1}<R\le L.
\end{cases}
\tag{4}
\]

Define

\[
a_r=\mu_3\mu_r,
\qquad
b_r=\frac7{16}(1+\mu_r).
\tag{5}
\]

Thus

\[
a_6=\xi,
\qquad
a_7=L\xi.
\tag{6}
\]

## Statement

### 1. Exact two-step affine skew product

On the raw affine state `(R,q) in I times R`, one down-return pair acts by

\[
\boxed{
\mathcal T(R,q)
=\left(P(R),a_{r(R)}q+b_{r(R)}\right),
\qquad
P(R)=a_{r(R)}R.
}
\tag{7}
\]

The base map `P:I->I` is the irrational rotation of `L-9841`. In logarithmic
coordinates its invariant probability measure is

\[
\boxed{
d\nu(R)=\frac{dR}{\ell R},
\qquad
\ell=\log L.
}
\tag{8}
\]

### 2. Positive additive cocycle in the normalized fiber

Put

\[
\boxed{w=\frac qR.}
\tag{9}
\]

Then (7) becomes

\[
\boxed{
\begin{aligned}
R'&=P(R),\\
w'&=w+\phi(R),
\end{aligned}
\qquad
\phi(R)=\frac{b_{r(R)}}{P(R)}>0.
}
\tag{10}
\]

Thus the multiplicative affine fiber is exactly conjugate to a strictly
positive additive cocycle over the irrational phase rotation.

Put

\[
\sigma=L\xi\in(1,L).
\tag{11}
\]

The branchwise ranges are exact:

\[
\boxed{
\begin{array}{c|c|c}
\text{return suffix}&R'\text{ range}&\phi(R)\text{ range}\\ \hline
70&(\sigma,L]&[b_7/L,b_7/\sigma),\\
60&(1,\sigma]&[b_6/\sigma,b_6).
\end{array}
}
\tag{12}
\]

In particular, with

\[
c_-=\min\!\left(\frac{b_7}{L},\frac{b_6}{\sigma}\right),
\qquad
c_+=\max\!\left(\frac{b_7}{\sigma},b_6\right),
\tag{13}
\]

one has the uniform bounds

\[
\boxed{0<c_-\le\phi(R)<c_+<\infty.}
\tag{14}
\]

Consequently every forward orbit satisfies

\[
\boxed{
w_0+nc_-
\le w_n
<w_0+nc_+
\qquad(n\ge1).
}
\tag{15}
\]

### 3. Exact ergodic drift

The cocycle has the exact invariant mean

\[
\boxed{
\begin{aligned}
\overline\phi
&=\int_{\mathcal I}\phi\,d\nu\\
&=\frac1\ell
\left[
\frac{b_7}{L\xi}(1-\xi)
+\frac{b_6}{\xi}\left(\xi-\frac1L\right)
\right]\\[1mm]
&=\frac7{144\log(9/8)}
\left(1+\frac1{\mu_3}\right)\\[1mm]
&=\frac{103271}{944784\log(9/8)}.
\end{aligned}
}
\tag{16}
\]

For every initial phase and every initial real fiber coordinate,

\[
\boxed{
\lim_{n\to\infty}\frac{w_n-w_0}{n}
=\overline\phi>0.
}
\tag{17}
\]

The drift is therefore deterministic and phase-independent, not merely an
almost-everywhere average.

### 4. Zero fiber Lyapunov exponent

For two points over the same phase, the normalized fiber difference is
preserved exactly:

\[
\boxed{w_n-\widetilde w_n=w_0-\widetilde w_0.}
\tag{18}
\]

In the original `q` coordinate,

\[
\boxed{
q_n-\widetilde q_n
=\frac{R_n}{R_0}(q_0-\widetilde q_0).
}
\tag{19}
\]

Equivalently, the derivative of the `n`-step fiber map telescopes:

\[
\boxed{
\frac{\partial q_n}{\partial q_0}
=\prod_{k=0}^{n-1}a_{r(R_k)}
=\frac{R_n}{R_0}.
}
\tag{20}
\]

Since `R_n,R_0 in (1,L]`,

\[
L^{-1}
<\left|\frac{\partial q_n}{\partial q_0}\right|
<L,
\tag{21}
\]

and hence the fiber Lyapunov exponent is

\[
\boxed{
\lim_{n\to\infty}
\frac1n\log
\left|\frac{\partial q_n}{\partial q_0}\right|
=0.
}
\tag{22}
\]

The raw affine return is neutral in its fiber: it neither contracts away nor
exponentially amplifies retained offset information.

### 5. No bounded invariant graph, orbit, or cycle

There is no bounded function `G:I->R` whose graph is invariant under (7).
Indeed, if `q=G(R)` were invariant, then

\[
H(R)=\frac{G(R)}R
\tag{23}
\]

would be bounded and would satisfy

\[
H(P(R))=H(R)+\phi(R).
\tag{24}
\]

Iteration and (14) would give

\[
H(P^n(R))\ge H(R)+nc_-,
\]

contradicting boundedness. More generally, (24) has no `nu`-integrable
solution, because integrating it would give `0=bar(phi)>0`.

Every real fiber orbit is unbounded above in `w`, and hence also in `q`
because `R` stays in `I`. There is no periodic full affine state and no
compact invariant set with bounded fibers.

### 6. Interpretation boundary

This theorem concerns the raw real affine skew product of exact H word maps.
It proves that the finite multiplier return of `L-9841` retains a neutral
fiber with unavoidable positive drift. It does not identify the normalized
fiber `w=q/R` with the 2-adic endpoint tail, prove eventual vanishing of
canonical interface blocks, or produce an ordinary nonnegative Collatz seed.

## Proof

Appending `30` sends

\[
(R,q)\longmapsto
\left(\mu_3R,\mu_3q+\frac7{16}\right).
\]

Appending the selected return suffix `r0` next gives

\[
\begin{aligned}
R'&=\mu_r\mu_3R=a_rR,\\
q'&=\mu_r\left(\mu_3q+\frac7{16}\right)+\frac7{16}
=a_rq+b_r,
\end{aligned}
\]

proving (7). Divide the second identity by `R'=a_rR` to obtain

\[
\frac{q'}{R'}
=\frac qR+\frac{b_r}{R'},
\]

which is (10).

On the `70` branch, `R in (1,xi^(-1)]` and
`R'=L xi R in (sigma,L]`. On the `60` branch,
`R in (xi^(-1),L]` and `R'=xi R in (1,sigma]`. Since `b_r/R'` decreases in
`R'`, this proves (12)--(15).

For the mean drift, integrate against (8):

\[
\begin{aligned}
\overline\phi
&=\frac1\ell
\int_1^{\xi^{-1}}
\frac{b_7}{L\xi R}\frac{dR}{R}
+\frac1\ell
\int_{\xi^{-1}}^L
\frac{b_6}{\xi R}\frac{dR}{R}\\
&=\frac1\ell
\left[
\frac{b_7}{L\xi}(1-\xi)
+\frac{b_6}{\xi}\left(\xi-\frac1L\right)
\right].
\end{aligned}
\tag{25}
\]

Put `m=mu_6`. Then `mu_7=Lm`, `xi=mu_3m`, and
`b_r=(7/16)(1+mu_r)`. The bracket in (25), divided by `7/16`, simplifies to

\[
\begin{aligned}
&\frac{1+Lm}{L\xi}(1-\xi)
+\frac{1+m}{\xi}\left(\xi-\frac1L\right)\\
&=\left(1-\frac1L\right)
\left(1+\frac m\xi\right)
=\frac19\left(1+\frac1{\mu_3}\right).
\end{aligned}
\tag{26}
\]

This proves (16). The base is an irrational rotation, so every orbit is
equidistributed. The function `phi` is bounded and Riemann integrable with
two circle discontinuities: the return-branch cut and the identified interval
seam. Weyl equidistribution therefore gives (17) for every initial phase.

For two fibers over the same base orbit, equation (10) cancels the common
cocycle and proves (18). Multiplying back by `R_n` proves (19). Alternatively,
the product of the affine slopes telescopes because

\[
a_{r(R_k)}=\frac{R_{k+1}}{R_k},
\]

which proves (20)--(22).

Finally, invariance of a graph `G` under (7), divided by the new base
coordinate, gives (24). Its positive lower drift proves the bounded-graph and
bounded-orbit obstructions. Invariance of `nu` and (16) rule out an integrable
solution as well. A periodic full state would force a zero sum of positive
cocycle increments, so no cycle exists. ∎

## Motivation

`L-9841` closes the raw multiplier phase with the finite suffix family
`{30,60,70}`. Multiplier closure alone could still conceal contraction or a
synchronizing graph in the affine offset. The normalized coordinate `w=q/R`
shows the opposite: offset information is neutral, while every return adds a
uniformly positive amount.

The exact mean (16) quantifies the resulting secular drift. Its simplification
also shows that switching between `60` and `70` changes the pointwise
increments but not the final closed-form average forced by the phase
partition.

## Dependency audit

- `L-9841` supplies the raw base rotation, branch cut, and exact completed
  suffix multipliers.
- The affine offset law is recomposed directly in the proof.
- Weyl equidistribution for irrational rotations is used for the every-orbit
  drift limit.
- No 2-adic carry distribution or ordinary-seed assumption is used.

## Gap audit

- Positive real affine drift is not a statement about the sign or size of the
  canonical 2-adic interface blocks.
- Zero Lyapunov exponent means retained fiber differences persist; it does not
  imply statistical independence or recurrence.
- No bounded invariant affine graph exists, so any full-state return must use
  an additional coordinate or a different renormalization.
- The theorem does not establish an ordinary nested point or a marked Collatz
  orbit.

## Adversarial tests

- The cocycle increment is `b_r/R'`, not `b_r/R`; dividing by the old phase
  gives the wrong drift integral.
- The `70` branch includes its upper cut and the `60` branch excludes its
  lower cut. These conventions produce the half-open ranges in (12).
- Unique ergodicity alone is normally stated for continuous observables;
  the every-orbit conclusion here uses Weyl equidistribution and the fact
  that `phi` is bounded and Riemann integrable.
- A zero fiber Lyapunov exponent does not contradict linear additive drift:
  derivatives measure differences between fibers, while `phi` translates all
  fibers together.

## Remaining uncertainty

The interaction between this real affine drift and the exact 2-adic reset
residues of `L-9837` is unknown. In particular, no theorem yet decides whether
the unique canonical carry path for the alternating architecture can
stabilize to an ordinary nonnegative seed.

## Suggested next attack

Compose the endpoint-tail maps for `30` followed by `60` or `70`, then compare
their dyadic reset residues with the branch rotation. A useful next result
would be an exact congruence showing whether positive real `w` drift forces or
forbids recurring zero interface blocks in the physical 2-adic fiber.
