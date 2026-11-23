# Can actual boundary entropy force ordinary escape to disappear?

Date: 2026-11-23. Status: a direct literature-based closing attempt, with
two explicit corollaries of the existing retained-source identities. No
escape exclusion, new unconditional real regularity theorem, or cycle
exclusion is obtained here. The corollaries below are not presented as a
new global reduction or as substitutes for the requested missing bound.

## 1. The new input and the target

PR180 at `fcdcdbadc6172e414f7282442a8a6b85587d7e70` proves, subject to its
listed canonical-trace inputs, that the actual common real boundary law
has upper local dimension one almost everywhere, is nonatomic, and has a
strictly positive lower Shannon information dimension at every fine scale.
The last lower bound persists after every fixed absolutely continuous
reweighting of the original path probability. Its files
`research/source-clock-20261123/BOUNDARY_OVERLAP.md`, `EXTENSIONS.md` and
`COLLISION_TRANSFER.md` were read in full for this attempt.

The exact requested conclusion is still an upper bound on the *ordinary
ternary inverse endpoint law*, not on a convenient measure with the same
real support. In the notation of PR185 at
`2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`, let

\[
q_j=U^j(q_0),\qquad v_j=\nu(q_j)\uparrow C>0,\qquad
K(q,x)=\mathbf1_{Ux=q}\frac{\nu(x)}{\nu(q)},
\]

\[
\pi_M=\frac1{M+1}\sum_{j=0}^M\delta_{q_j},\qquad
\zeta_{M,r}=K^r_*\left(\frac1{M+1}
                         \sum_{j=0}^M\delta_{q_{r+j}}\right).
\tag{1}
\]

The source is one hypothetical escaping positive odd unit orbit and the
harmonic flow is exactly the source-qualified ordinary flow in that PR.
For each fixed positive finite T, its exact-word argument gives

\[
\inf_{r\ge0}\operatorname{Col}_m(\zeta_{M,r})
\ge c\sqrt m\,3^{-\theta m},\qquad
m^2\le TM,
\quad\theta=0.949955527188\ldots.
\tag{2}
\]

Thus an upper bound `O(3^(-theta*m))` along one compatible sequence would
exclude escape. PR180 already gives a model showing why even exact local
dimension one and full Shannon information dimension do not imply this
collision estimate. That model is not repeated as a new result.

The attack here was to supply the missing structural input using
entropy-growth and measure-rigidity machinery, with the new real entropy
as the nondegenerate factor. The computation below keeps both factors and
the original inverse clock.

## 2. The actual branching equation is graph-directed

For the trace kernel, write `F` for its critical harmonic function and

\[
K_F(q,x)=\mathbf1_{Ux=q}\frac3{2^e}\frac{F(x)}{F(q)},
\qquad x=\frac{2^e q-1}{3}.
\]

Let `mu_q` be the law of the real inverse series R at that ordinary root.
The exact first-step identity gives

\[
\mu_q=\sum_{e\text{ legal at }q}
 K_F(q,I_eq)\,(\psi_e)_*\mu_{I_eq},
\quad
I_eq=\frac{2^e q-1}{3},\quad
\psi_e(t)=\frac{1+3t}{2^e}.
\tag{3}
\]

More generally, for every actual complete prefix w of odd depth r, let
`a_w=3^r/2^{A_w}`, `R_w` be its finite real sum, and n its ordinary
endpoint. Then

\[
\widehat\mu_q(t)=
\sum_w a_w\frac{F(n)}{F(q)}
 e^{itR_w}\widehat\mu_n(a_wt).
\tag{4}
\]

No independence is used in (3)--(4). They follow by conditioning the same
Markov path law on its actual first edge or prefix. The residual law is
`mu_n`; its label n depends on that prefix, and the available coefficients
also depend on n. Replacing all residual laws by one common independent
factor is an additional assertion. The exact affine formulas do not make
that assertion true.

This matters for the cited inverse entropy theorem. Hochman,
*On self-similar sets with overlaps and inverse theorems for entropy*,
arXiv:1212.1873v6, Theorems 2.7--2.8 (PDF pp. 14--15), treats an actual
convolution of two probability measures. Its self-similar applications
also require the specified fixed IFS and fixed probability vector.
Equation (3) is a countable graph-directed system with varying laws and
weights; the step e=1 is even expansive as a real affine map. A block or
stopping construction could address expansion, but does not remove the
conditional dependence in (4).

The distinct theorem of Hochman--Shmerkin, *Local entropy averages and
projections of fractal measures*, Theorem 1.3 (printed p. 1005), starts with
two probability measures invariant under the separate multiplication maps
`T_m` and `T_n`. Their CP-chain results likewise assume the stated scenery
process. No separate multiplication invariance of the actual `mu_q`, its
common component boundary, or the ordinary time marginal is supplied by
(3). Irrationality of `log(2)/log(3)` does not itself supply that missing
invariance.

Primary statement pages inspected:

- <https://arxiv.org/pdf/1212.1873>, Theorems 2.7--2.8 and the defining
  self-similar equation in Section 1.1.
- <https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n3-p01-p.pdf>,
  Theorem 1.3 and the CP-chain hypotheses around Theorems 1.10--1.13.

These are a hypothesis check at the relevant theorem statements, not a
claim to have reconstructed the complete proofs of either paper.

## 3. The retained high-profile part actually has mass tending to one

PR180's collision-transfer note proves a fixed positive high-profile mass
using `c_0=v_0/C`. Keeping the exact retracing coefficients gives the
following sharpened corollary. It uses no new population or regularity
input beyond those already needed for (1).

**Corollary 1.** Suppose `F(q_j) >= c*q_j` for a fixed c>0, as in the
pinned trace comparison. Then, for every fixed B,

\[
\boxed{\lim_{M\to\infty}\inf_{r\ge0}
        \zeta_{M,r}\{F>B\}=1.}
\tag{5}
\]

**Proof.** Choose J such that `F(q_j)>B` for every j>=J; this is possible
because the ordinary positive states of an escaping orbit are distinct.
The exact retracing word from `q_(r+j)` to `q_j` has probability
`v_j/v_(r+j) >= v_j/C`. Its atoms at the distinct q_j give

\[
\zeta_{M,r}\{F>B\}
\ge \frac1{M+1}\sum_{j=J}^M\frac{v_j}{C}.
\]

The right side tends to one by Cesaro convergence, independently of r.
The probability is at most one. This proves (5).

This is a direct corollary of older exact retracing, not an independent
anti-concentration theorem. It shows precisely why improving only the
low-profile portion of PR180's real-boundary argument cannot close (2):
that portion has vanishing mass for the moving source law (1).

In particular, the selection theorem's fixed-root qualification cannot be
removed by choosing a much longer r in (1). The root moves by the same
clock, and (5) is uniform over every finite r.

## 4. A nondegenerate independent reference costs linear information

Here is a general exact consequence explaining why introducing fresh
independent branch noise changes the law substantially. Let `P_(j,r)`
be the actual ordinary inverse word law at root `q_(j+r)`, with word
length r, and let `w_(j,r)` be its literal retracing word to q_j. Write

\[
p_{j,r}=P_{j,r}\{w_{j,r}\}=\frac{v_j}{v_{j+r}}\ge\frac{v_j}{C}.
\tag{6}
\]

Let `Q_(j,r)` be any reference word law whose mass at this word is at
most `exp(-h*r)`, with h>0. This includes a fixed nondegenerate Bernoulli
word law with largest letter probability at most `exp(-h)`, and a Markov
reference with the same uniform one-step bound.

**Corollary 2.** With natural logarithms,

\[
\boxed{D_{\rm KL}(P_{j,r}\Vert Q_{j,r})
       \ge p_{j,r}hr-h_b(p_{j,r})
       \ge\frac{v_j}{C}hr-\log2.}
\tag{7}
\]

If the reference gives zero mass to the retracing word, the divergence is
infinite and the inequality has the same interpretation.

**Proof.** Project both laws to the indicator of that single word. Put
`b=Q_(j,r){w_(j,r)}`. Convexity of `t log t`, separately on the word
event and its complement, gives the binary lower bound

\[
D_{\rm KL}(P\Vert Q)
\ge p\log\frac p b+(1-p)\log\frac{1-p}{1-b}
=-h_b(p)+p\log\frac1b+(1-p)\log\frac1{1-b}.
\]

Drop the last nonnegative term and use `b<=exp(-hr)`. Finally
`h_b(p)<=log 2` and (6) prove (7).

Consequently, along any `j_i -> infinity`, `r_i -> infinity`,

\[
\liminf_i\frac1{r_i}
D_{\rm KL}(P_{j_i,r_i}\Vert Q_{j_i,r_i})\ge h.
\tag{8}
\]

This does not rule out entropy methods with dependent or singular
references. It rules out treating these particular independent-reference
replacements as a vanishing-cost perturbation of the retained ordinary
path law. Related memory costs and the exact radial total-variation
theorem already occur in PR178 and PR175; (7) is a direct reusable binary
form, not a claim of priority for that underlying obstruction.

The rich real tail is consistent with (6). In the common coherent chart
of PR180, let `y(q_j) -> b_E`. On the retracing event, the normalized real
boundary obeys exactly

\[
T_{j+r}=\varepsilon_{j,r}+(1-\varepsilon_{j,r})T_j,
\qquad
\varepsilon_{j,r}=1-\frac{y(q_j)}{y(q_{j+r})},
\]

\[
0\le\varepsilon_{j,r}\le1-\frac{y(q_j)}{b_E}\longrightarrow0
\quad\text{uniformly in }r.
\tag{9}
\]

Thus a high-entropy real boundary can pass almost unchanged through an
arbitrarily long retained prefix. It need not generate independent
ordinary residue entropy at each inverse step. PR175's
`risk23/RENORMALIZED_FIBRE_ENTROPY_ATTACK.md` already proves a stronger
exactly renormalized whole-law total-variation statement; (9) is credited
to that existing transport, not counted as new progress.

## 5. The selection-weight cancellation attempt

The most promising additional calculation was to weight by
`g(X_r)=D_1(X_r)/F(X_r)`. On a prefix ending at n the trace cylinder weight
becomes exactly

\[
\left(a_r\frac{F(n)}{F(q)}\right)g(n)
=\frac{a_rD_1(n)}{F(q)}\le\frac{2a_r}{F(q)}.
\tag{10}
\]

For a fixed odd depth r and total valuation A, integer endpoint
separation then controls real cells. This removes the endpoint's large
F-value from that one finite cylinder weight. It is useful algebra, but
the real tail from n is not uniformly small unless a cone-floor estimate
is retained. PR180 supplies that estimate at low-profile n; on the moving
law its complement has mass tending to one by (5).

There is a second independent issue: summing the per-total cell estimate
over the possible totals has an r-dependent effective multiplicity.
Changing to a first-crossing scale makes the depth itself vary, and no
bounded multiplicity or stationary CP-chain identification was proved for
that stopping construction. Equation (10) alone therefore gives neither
a uniform real Frostman estimate nor the required ternary estimate (2).
This is the first unsupported uniform estimate in that attempted
regularization, rather than a reason to relabel the same real entropy as
ordinary time entropy.

## 6. Outcome and next exact problem

The new source makes an entropy-growth approach worth pursuing: the real
factor now has positive mean information at every fine scale under its
actual law. The literature theorems inspected require an additional
convolution, scenery, or invariance structure. The exact law currently
retains dependent conditional tails, and (5)--(9) quantify the original
spine that those tails can carry.

No closing upper bound was obtained. A usable next theorem must do at
least one of the following with the same original law:

- Control collision of the high-profile ordinary endpoints in (1), at
  the precision range of (2), directly.
- Produce a genuine convolution/scenery structure for the graph-directed
  equation (3), then prove a quantitative transfer to those endpoints
  that keeps the original clock and pays the law comparison.

Neither proposal is asserted here. No Lean module was added merely to
formalize the already known transport identities or the binary KL
inequality; that would not resolve their missing arithmetic input.
