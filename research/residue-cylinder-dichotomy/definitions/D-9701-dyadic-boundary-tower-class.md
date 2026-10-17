# D-9701 — Dyadic boundary tower-cylinder class

**Claim ID:** `D-9701`  
**Title:** Exact direct-connector class on the four phase-`-34` dyadic tower boundaries  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** branch-qualified data from PR #3 `L-0016` and `L-0017`  
**Scope:** arbitrary infinite directives in the four phase-`-34` self-return tower types, using direct height doubling  
**Related counterexample candidates:** none

## Motivation

PR #3 proves exact finite tower replacement and a corrected supercritical 256-transition stage, but ordinary closure remains a residue-cylinder question. This definition freezes a simpler nontrivial boundary class in which the same four tower types and one scale counter remain visible while the real height becomes uniformly contracting. It is designed as a theorem-quality comparison class, not as a replacement for the 256-stage target.

## 1. Shortcut map and four finite-control types

Use the shortcut map

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\[1mm]
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

The four phase-`-34` self-return types are indexed by their source mismatch
positions

\[
\mathcal I=\{5,6,7,8\}.
\]

Their finite constants are

| type `i` | `k_(0,i)` | `r_i` | `g_(0,i)` | `b_i` |
|---:|---:|---:|---:|---:|
| 5 | 5 | 5 | 5 | 2 |
| 6 | 6 | 4 | 4 | 3 |
| 7 | 7 | 3 | 5 | 2 |
| 8 | 8 | 2 | 6 | 1 |

Every row satisfies

\[
k_{0,i}+r_i+1=11,
\qquad
g_{0,i}+b_i=7.
\tag{1}
\]

For padding height \(t\ge0\), put

\[
k_i(t)=k_{0,i}+11t,
\qquad
g_i(t)=g_{0,i}+7t.
\tag{2}
\]

Let \(\mu_i(t)\) be the unique odd residue in
\([0,2^{r_i+1})\) satisfying

\[
3^{g_i(t)}\mu_i(t)\equiv-1\pmod{2^{r_i+1}}.
\tag{3}
\]

Define

\[
A_i(t)=2^{k_i(t)}\mu_i(t),
\tag{4}
\]

\[
K_i(t)=k_i(t)+r_i+1=11(t+1),
\tag{5}
\]

\[
B_i(t)=
3^{b_i}
\frac{3^{g_i(t)}\mu_i(t)+1}{2^{r_i+1}},
\tag{6}
\]

\[
G_i(t)=g_i(t)+b_i=7(t+1).
\tag{7}
\]

The exact tower identity inherited from PR #3 `L-0016` is

\[
\boxed{
T^{K_i(t)}
\left(A_i(t)+2^{K_i(t)}h-34\right)
=
B_i(t)+3^{G_i(t)}h-34
}
\tag{8}
\]

for every ordinary integer \(h\ge0\). Algebraically the affine identity remains
valid for any integer \(h\) for which the displayed block is interpreted on its
prescribed parity cylinder.

The canonical bounds are

\[
0<A_i(t)<2^{K_i(t)},
\qquad
0<B_i(t)<3^{G_i(t)}.
\tag{9}
\]

## 2. One counter and arbitrary finite control

Fix a starting scale \(m_0\ge0\). The sole directive counter is

\[
m_n=m_0+n,
\qquad
t_n=2^{m_n}.
\tag{10}
\]

Finite control chooses a type

\[
i_n\in\mathcal I.
\]

The theorem below allows every sequence in \(\mathcal I^{\mathbb N}\), hence it
also applies to every finite directed control graph on \(\mathcal I\).

At step \(n\), use the canonical **direct connector** from the source tower
\((i_n,t_n)\) to the target tower \((i_{n+1},2t_n)\). Put

\[
N_n=3^{G_{i_n}(t_n)}=3^{7(t_n+1)},
\tag{11}
\]

\[
q_n=2^{K_{i_{n+1}}(2t_n)}
=2^{11(2t_n+1)},
\tag{12}
\]

\[
C_n=B_{i_n}(t_n)-A_{i_{n+1}}(2t_n).
\tag{13}
\]

The exact high-tail recurrence is

\[
\boxed{
h_{n+1}=\frac{N_nh_n+C_n}{q_n}.}
\tag{14}
\]

An integer \(h_n\) is locally admissible exactly when the numerator in (14) is
divisible by \(q_n\). In that case the corresponding tower output equals the
next tower input:

\[
B_{i_n}(t_n)+N_nh_n
=
A_{i_{n+1}}(2t_n)+q_nh_{n+1}.
\tag{15}
\]

Consequently the physical states

\[
x_n=A_{i_n}(t_n)+2^{K_{i_n}(t_n)}h_n-34
\tag{16}
\]

obey the exact finite replay

\[
T^{K_{i_n}(t_n)}(x_n)=x_{n+1}.
\tag{17}
\]

When every \(h_n\ge0\), all sufficiently large displayed physical states are
positive. Positivity is not used in the negative theorem; `T-9702` excludes even
signed ordinary integer high-tail trajectories.

## 3. Residue cylinders

For a finite control prefix

\[
i_0,i_1,\ldots,i_k,
\]

require (14) for \(0\le n<k\). Since every \(N_n\) is odd, `L-9701` gives one
initial residue cylinder

\[
h_0\equiv R_k\pmod{Q_k},
\qquad
Q_k=\prod_{n=0}^{k-1}q_n.
\tag{18}
\]

The cylinders are nested. Their new block is

\[
a_k=\frac{R_{k+1}-R_k}{Q_k},
\qquad0\le a_k<q_k.
\tag{19}
\]

This is the precise residue-cylinder object classified in `T-9702`.

## 4. Deliberate distinction from PR #3's 256-stage map

Equation (14) is one direct connector between dyadic boundary heights. It is
not the chronological composition of the 256 intermediate connectors in PR #3
`T-0027`.

The distinction is structural, not cosmetic. The direct boundary map has a
uniform real contraction. The composed 256-stage map has the positive residual
surplus of `T-0024`. `Q-9701` records the exact transfer gap.


## Dependency audit

- PR #3 `L-0016` supplies the four type constants, the canonical residues, and the exact tower identity (8).
- PR #3 `L-0017` supplies the direct connector interpretation. Equation (14) is also obtained directly by equating the source output with the target input.
- No result about the 256-transition composite, entropy, logarithms, or p-adic completion is used in the definition.

## Gap audit

- The class uses dyadic boundary doubling and omits the 256 chronological intermediate connectors.
- An arbitrary type directive is allowed, but the scale schedule is fixed to `t -> 2t`.
- Finite admissibility does not identify an ordinary infinite initialization. That question is answered negatively only after `L-9701`, `T-9701`, and `T-9702`.

## Adversarial tests

`X-9701` reconstructs every recovery residue independently, checks all 16 source/target pairs at six dyadic heights, and directly replays thirty positive physical tower blocks.

## Remaining uncertainty

The branch-qualified PR #3 tower formulas remain `PROPOSED` pending independent review. The packet independently checks their finite arithmetic interface but does not re-prove the original parity-template derivation of all four tower types.

## Suggested next attack

Use this class as a control case for a renormalized height or forbidden-zero-block invariant on the genuinely supercritical stage equation in `Q-9701`.
