# Exact canonical run-weight commutator and its surviving component

Date: 2026-11-22. **Status: complete written deduction from frozen canonical-energy and arithmetic inputs; not Lean formalized.**

The boundary-drift term in current PR177's commutator tends to zero uniformly in the finite Green depth, for each fixed truncated run weight. The remaining term has an exact asymptotic, including the supremum over Green depth. Its coefficient is the surviving canonical component charge. This proves no uniform bound in the run cutoff when that charge is positive, and does not eliminate escape.

## 1. Frozen inputs and notation

The target is PR177 at commit

`e4ca639326bac73da8c2a698dec8a749e5efbe68`,

`research/lean-exact-witness-global-20261121/LITERATURE_CANONICAL_ENERGY.md`, Section 8, equations (38)–(49). The precise arithmetic input is the same commit's `LITERATURE_ARITHMETIC_RETURN.md`, Section 6, Theorem 3: for every escaping ordinary orbit and every fixed S, its times with at most S binary runs have upper Banach density zero. In particular, the density assertion is uniform in the starting time of the interval. That theorem imports Evertse–Schlickewei–Schmidt, *Linear equations in variables which lie in a multiplicative group*, Theorem 1.1; this note imports the repository's arithmetic deduction rather than replaying that literature argument.

Use the actual retained ordinary forest, killed upon entry into a periodic vertex. Write

- C for killed forward composition: Cφ(x)=φ(Ux) on a retained edge and zero otherwise;
- L for forward transport of ordinary measures, the counting-measure adjoint of C;
- ν for the positive ordinary harmonic flow, Lν=ν;
- Kφ=ν^(−1)L(νφ), the ν-adjoint of C;
- d for the actual canonical charge and g=d/ν;
- R_M=∑_{i=0}^{M−1}K^i g and R=∑_{i≥0}K^i g.

The frozen canonical construction gives

\[
0\le R_M\uparrow R\le1,\qquad
(I-K)R_M=g-K^Mg.
\tag{1}
\]

Fix 0<α<1/40, ρ=4^α, and a positive integer cutoff L₀. To keep the transport operator L distinct from the cutoff, put

\[
w(x)=w_{\rho,L_0}(x)=\min(\rho^{r(x)},W),
\qquad W=\rho^{L_0}.
\]

Here r(x) counts binary runs. PR177's equation (44) proves

\[
D:=\sum_xd(x)<\infty,\qquad
\sum_x d(x)w(x)\le B_\alpha<\infty,
\tag{2}
\]

with B_α independent of L₀. The first inequality follows also from the second because w≥1. All source weights below remain these same d(x).

For an escaping component E, write

\[
c_E=\lim_{k\to\infty}\nu(U^kp)>0,\quad
D_E=\sum_{x\in E}d(x),\quad
F_E=D_E/c_E\in(0,1].
\tag{3}
\]

These quantities do not depend on the choice of p in that component. The frozen canonical-energy component identification is

\[
b_\infty=\sum_{E\text{ escaping}}c_EF_E^2
=\sum_{E\text{ escaping}}F_ED_E.
\tag{4}
\]

In particular, this series is at most D. Equation (4) is the existing identification of the escape coefficient in PR177's equations (40)–(41); it is retained as a canonical-energy input here.

## 2. The uniform Green-depth commutator theorem

Let A_{N,M}(w) be the first line of PR177's (47), and T_{N,M}(w) its second line:

\[
A_{N,M}(w)=\frac2N\sum_{j<N}\sum_xd(x)
\left[C^j(wR_M)(x)-w(x)C^jR_M(x)\right],
\tag{5}
\]
\[
T_{N,M}(w)=\frac1N\sum_x\nu(x)R_M(x)^2
\left[C^Nw(x)-w(x)\right].
\tag{6}
\]

Thus the exact canonical commutator is A_{N,M}+T_{N,M}.

**Theorem.** For every fixed truncated weight above,

\[
\boxed{\lim_{N\to\infty}\sup_{M\ge1}|T_{N,M}(w)|=0,}
\tag{7}
\]

and

\[
\boxed{
\lim_{N\to\infty}\sup_{M\ge1}
\mathfrak C_{N,M}(w)
=2Wb_\infty-
2\sum_{E\text{ escaping}}F_E\sum_{x\in E}d(x)w(x).}
\tag{8}
\]

The right side is nonnegative because w≤W. It is an exact asymptotic of the supremum in Green depth; it does not assert a limit for every choice of M as N grows.

### All signed expressions are integrable

Put f=R_M and a_M=νf². Since 0≤f≤1,

\[
\sum_xa_M(x)\le\sum_x\nu(x)f(x)
=\sum_{i<M}\sum_x\nu(x)K^ig(x)
\le MD.
\tag{9}
\]

The last inequality uses killed forward transport, which cannot increase the total charge. Thus a_M and L a_M are finite measures; their difference is an absolutely summable signed measure. Every function used below is bounded by W. This justifies all adjoint pairings and finite telescoping identities, including those with future suprema or infima that need not belong to L²(ν).

## 3. The boundary drift is uniformly negligible

Let

\[
\lambda_M=L a_M-a_M.
\]

Its negative part satisfies the source-preserving domination

\[
\boxed{\lambda_M^-\le2d.}
\tag{10}
\]

Indeed K is a Markov kernel and Jensen gives Kf²≥(Kf)². Using (1), 0≤f,Kf≤1, and g≥0,

\[
\begin{aligned}
(a_M-L a_M)_+
&=\nu(f^2-Kf^2)_+\\
&\le\nu\bigl[(f-Kf)(f+Kf)\bigr]_+\\
&\le2\nu g=2d.
\end{aligned}
\]

Define the killed forward average

\[
H_N=\frac1N\sum_{j<N}C^jw.
\tag{11}
\]

A finite telescoping sum and adjointness give precisely

\[
T_{N,M}(w)=\langle H_N,\lambda_M\rangle.
\tag{12}
\]

The pairing in (12) is counting-measure pairing with the signed measure λ_M. Define its future upper and lower envelopes

\[
H_N^+(x)=\sup_{t\ge0}(C^tH_N)(x),\qquad
H_N^-(x)=\inf_{t\ge0}(C^tH_N)(x).
\tag{13}
\]

Killed future values are zero. Consequently

\[
0\le H_N^-\le H_N\le H_N^+\le W,
\qquad CH_N^+\le H_N^+,\quad CH_N^-\ge H_N^-.
\]

Since a_M≥0,

\[
\langle H_N^+,\lambda_M\rangle
=\langle CH_N^+-H_N^+,a_M\rangle\le0,
\]

and the corresponding pairing for H_N^- is nonnegative. Subtract H_N from these two inequalities and use (10):

\[
-2\sum_xd(x)(H_N-H_N^-)(x)
\le T_{N,M}(w)
\le2\sum_xd(x)(H_N^+-H_N)(x).
\tag{14}
\]

In particular,

\[
|T_{N,M}(w)|\le\varepsilon_{N,L_0}
:=2\sum_xd(x)(H_N^+-H_N^-)(x),
\tag{15}
\]

independently of M.

On an escaping orbit, the upper Banach density input implies

\[
\sup_{t\ge0}\left|\frac1N\sum_{j<N}
w(U^{t+j}x)-W\right|\longrightarrow0.
\tag{16}
\]

Indeed W−w vanishes whenever r≥L₀ and is bounded by W everywhere. Thus both envelopes in (13) tend to W at this fixed original x.

If x is killed after τ(x)<∞ retained times, then H_N^-(x)=0 and every future average is bounded by

\[
H_N^+(x)\le W\min(1,\tau(x)/N)\longrightarrow0.
\tag{17}
\]

Every original source therefore has H_N^+−H_N^- tending to zero. Domination by W and the finite original charge in (2) give ε_{N,L₀}→0. This proves (7), including all killed components.

The one-sided upper bound in (14) requires only the ordinary fixed-orbit Cesàro convergence H_N(x)→W on escape, not the upper Banach strengthening. The stronger input is what also makes the lower bound vanish and establishes absolute uniform convergence in (7).

## 4. The surviving component in the transport term

First identify the ordinary forward limit of the canonical potential. Its exact inverse-tree representation is

\[
\nu(q)R(q)=\sum_{i\ge0}\sum_{U^ix=q}d(x).
\tag{18}
\]

There is no repeated counting of a source: repetition at different depths would make q periodic, and periodic vertices are excluded. Along an escaping forward ray q_k, these predecessor trees increase and exhaust its ordinary component E. Hence their charge tends to D_E. Together with ν(q_k)→c_E, this gives

\[
R(U^kx)\longrightarrow F_E\qquad(x\in E).
\tag{19}
\]

At each fixed N, bounded convergence against d and R_M↑R give

\[
A_{N,M}(w)\longrightarrow A_{N,\infty}(w)
\quad(M\to\infty),
\tag{20}
\]

where the latter expression uses R in (5). No signed infinite-moment exchange is involved: the absolute value is bounded by 2W d(x) after time averaging.

For an escaping original source x in E, the source's contribution to (20) is

\[
\frac2N d(x)\sum_{j<N}
\bigl(w(U^jx)-w(x)\bigr)R(U^jx).
\]

By (19), bounded weights, and the fixed-orbit consequence of (16), its limit is

\[
2d(x)F_E\bigl(W-w(x)\bigr).
\tag{21}
\]

For a killed source only finitely many retained terms occur, so the contribution tends to zero. Domination by 2W d(x) now gives

\[
A_{N,\infty}(w)\longrightarrow
2\sum_{E\text{ escaping}}F_E
\left(WD_E-\sum_{x\in E}d(x)w(x)\right).
\tag{22}
\]

Equation (4) identifies this with the right side of (8).

### Taking the supremum over every finite Green depth

The supremum in (8) is also controlled, despite possible negative coefficients in (5). Because 0≤R_M≤R,

\[
A_{N,M}(w)\le A_{N,\infty}(w)+\eta_{N,L_0},
\tag{23}
\]

where

\[
\eta_{N,L_0}:=\frac2N\sum_xd(x)
\sum_{\substack{j<N\\j<\tau(x)}}
\bigl(w(x)-w(U^jx)\bigr)_+.
\tag{24}
\]

Here τ(x)=∞ on escape. For an escaping fixed x, its averaged positive part tends to zero: w(x)≤W, while w(U^jx) has Cesàro mean W and never exceeds W. For a killed x there are only finitely many retained terms. Bounded convergence against the original d gives η_{N,L₀}→0.

The reverse bound

\[
A_{N,\infty}(w)\le\sup_{M\ge1}A_{N,M}(w)
\]

follows from (20). Combining (15) and (23) therefore sandwiches the full supremum:

\[
A_{N,\infty}(w)-\varepsilon_{N,L_0}
\le\sup_{M\ge1}\mathfrak C_{N,M}(w)
\le A_{N,\infty}(w)+\eta_{N,L_0}+\varepsilon_{N,L_0}.
\tag{25}
\]

Equations (22) and (25) prove (8).

## 5. What the exact result pays, and what survives

The subtraction in (8) is bounded independently of the cutoff:

\[
0\le\sum_{E\text{ escaping}}F_E
\sum_{x\in E}d(x)w_{\rho,L_0}(x)
\le\sum_xd(x)\rho^{r(x)}\le B_\alpha.
\tag{26}
\]

Consequently

\[
2\rho^{L_0}b_\infty-2B_\alpha
\le\lim_{N\to\infty}\sup_{M\ge1}
\mathfrak C_{N,M}(w_{\rho,L_0})
\le2\rho^{L_0}b_\infty.
\tag{27}
\]

If an escaping component has positive canonical charge, this grows without bound as the run cutoff increases. Its leading coefficient is exactly 2b_∞. The positive term comes from transporting the original charge along the actual escaping component; it has not been created by changing root, using Haar-typical points, or assigning a fresh source distribution.

This calculation resolves the signed boundary-drift issue and identifies the entire surviving term in the current commutator. It does not prove the uniform cutoff bound required to close the argument. Such a bound would have to eliminate the same b_∞ appearing in the canonical escape energy, rather than follow from the finite static forcing estimate alone.

The result is compatible with the independent adaptive inverse-word attempt in `ADAPTIVE_SIBLING_AND_HARNACK_ATTEMPT.md`: its finite-depth 16^(−r) comparison does not control this transported run-weight correlation. The reversible recurrence calculation in that earlier note overlaps the symmetrization result already present in the newly refreshed PR177; that overlap is not a new advance over this frozen upstream commit.

## Review scope

All new deductions in this note are equations (7)–(27), conditional on the explicit frozen inputs in Section 1. The ordinary arithmetic upper Banach theorem, the canonical construction, the component identity (4), and the original weighted-forcing estimate are imported. No old build, broad repository audit, numerical experiment, generic Harnack application, or replacement stationary measure is a premise. No full Collatz theorem or new Lean formalization is claimed.
