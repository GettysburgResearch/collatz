# A recurrent network on the actual escaping component

Date: 2026-11-23.

**Status: unconditional written construction from the hypothesis of an
escaping ordinary component, and a direct closure attempt.
The theorem is about an auxiliary reversible walk on the actual ordinary
component. It does not assert recurrence of the deterministic Collatz map,
and does not prove Collatz.** The main construction uses only an elementary
orbit count and the actual binary inverse tree already proved in this PR.
It requires no predecessor-density theorem, canonical-envelope hypothesis,
replacement of ordinary vertices by completion points, or independent
random parity assumption.

The proposed closing move was to combine recurrence with a bounded,
strictly increasing physical coordinate. Recurrence is proved here. The
coordinate's exact drift changes sign; the uniform inequality that would
close this route has not been established. A finite, explicitly specified
measure accounts for the cancellation rather than discarding the original
source.

## 1. Exact objects and the two different measures

Write

\[
U(n)=(3n+1)/2^{a(n)},\quad a(n)=v_2(3n+1),\quad
w(n)=3/2^{a(n)},\quad \lambda(n)=3n/(3n+1).
\]

Let \(E\) be one hypothetical escaping component of positive odd integers
coprime to three. Every two vertices have a common forward endpoint; no
forward orbit repeats. All edges below are actual integral Collatz edges.

The elementary positive-product calculation in PR177,
`6de3e304bb49a93a6c5ef0e5563137e75c7defb4`,
`research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md`,
(HE2), (HE18)--(HE24a), supplies the following notation and theorem. Its
short orbit-count proof is reconstructed in Section 8 rather than treated
as an analytic premise:

\[
\Lambda(n)=\prod_{j\ge0}\lambda(U^jn)\in(0,1),\qquad
r(n)=\Lambda(n)/n,\qquad r(n)=w(n)r(Un).                 \tag{1}
\]

It also supplies, for \(s>1\), the finite positive conformal measure
\(\mu_s=\sum_{n\in E}r(n)^s\delta_n\), satisfying
\(\mu_sP_s=\mu_s\), where

\[
(P_sf)(q)=\sum_{Un=q}w(n)^sf(n).                         \tag{2}
\]

We will construct a positive harmonic function satisfying

\[
P_1G=G,\qquad 0<G(n),\qquad G(n)/n\le C.                \tag{3}
\]

The previously existing canonical function also satisfies (3), as stated
in PR180,
`04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`,
`research/high-variance-20261123/ANALYTIC_GLUING.md`, Sections 1 and 4,
with its population and finite-envelope qualifications retained. That
canonical function is **not** the deliberately chosen function constructed
next. For the new function we will prove directly

\[
\sum_{n\in E}G(n)/n^2<\infty.                            \tag{4}
\]

The critical inverse probability kernel and its invariant mass are

\[
K(q,n)=\mathbf1_{Un=q}\frac{w(n)G(n)}{G(q)},\qquad
\pi(n)=r(n)G(n).                                        \tag{5}
\]

This is the critical normalization used for PR180's \(K_h\), with our
new choice of \(G\); it is not an identification with either of PR180's
canonical kernels. It has row sum one by (3).
The finite conformal measure \(\mu_s\) and the infinite invariant mass
\(\pi\) must not be identified.

## 2. Constructing a full-support flow without analytic hypotheses

Fix \(p\in E\). There is a well-defined integer level \(h\) with
\(h(p)=0\), \(h(Un)=h(n)+1\): if \(U^kn=U^jp\), put
\(h(n)=j-k\). Extending a meeting adds the same amount to both clocks,
and acyclicity prevents two different values. The component is an
undirected tree.

Enumerate its countably many vertices as \(v_1,v_2,\ldots\). At every
odd unit there are two strictly larger legal unit parents with exponents
between 3 and 8. This exact ordinary construction is proved in
`../risk23/HARDY_INVERSE_TREE.md`, Section 2, and its arithmetic is checked
in `../risk23/InverseBranching.lean`, at our published commit
`8870528daa6a13cc941d602e578e35c8bfa4bf4f`.

From \(v_i\), choose each of those two parents with probability one half,
indefinitely into the past, and extend forward by the actual deterministic
map \(U\). This is a probability \(\Pi_i\) on bi-infinite actual paths
\((Q_t)_{t\in\mathbb Z}\), with \(h(Q_t)=t\). Distinct selected
binary paths have distinct ordinary labels, so \(\Pi_i\) has no atoms
on the space of whole paths. Let

\[
\Pi=\sum_{i\ge1}2^{-i}\Pi_i,\qquad
\pi(n)=\Pi(Q_{h(n)}=n).                                 \tag{6a}
\]

Every vertex has positive mass, since \(\pi(v_i)\ge2^{-i}\), and
\(\pi(n)\le1\). Deterministic forward motion implies

\[
\sum_{Un=q}\pi(n)=\pi(q),\qquad
\sum_{h(n)=t}\pi(n)=1\quad(t\in\mathbb Z).              \tag{6b}
\]

The mixture still has no whole-path atoms. Its backwards conditional law
is Markov with probabilities \(\pi(n)/\pi(q)\): given the current
state, every later state is already determined. This deterministic-future
property justifies the reverse Markov assertion even for the mixture.

Section 8 proves the uniform bound \(\sum_{n\text{ on a path}}1/n
\le160\) for each of these bi-infinite actual paths. Tonelli gives

\[
\sum_{n\in E}\pi(n)/n\le160.                            \tag{6c}
\]

Now define \(G(n)=\pi(n)/r(n)\). Equation (1) and (6b) give
\(P_1G=G\). The same orbit count gives
\(\Lambda(n)\ge\delta:=e^{-160/3}>0\), uniformly on \(E\), hence

\[
0<G(n)/n=\pi(n)/\Lambda(n)\le\delta^{-1},\qquad
\sum_nG(n)/n^2\le160\delta^{-1}.                        \tag{6d}
\]

Thus (3)--(4) have been constructed without importing the canonical
population or envelope theory. The resulting \(K\) in (5) is exactly
the backward law in (6b), and \(\pi=rG\) exactly as in (5).
No uniform lower bound \(G(n)\ge\gamma>0\) is claimed; arbitrary
enumeration weights do not supply one. This missing comparison is one
reason the new \(G\) must not be substituted for the canonical function.

More generally, the recurrence proof below applies to **any** positive
flow satisfying (1)--(3). The next paragraph reconstructs the level mass
in that generality; in the mixture construction its value is simply one.

### General finite level mass

Equations (1), (3), and (5) give

\[
\pi(q)K(q,n)=\pi(n)\quad(Un=q),\qquad
\sum_{Un=q}\pi(n)=\pi(q).                               \tag{6}
\]

Thus \(\pi\) is invariant under both deterministic forward motion and
the inverse kernel. It obeys \(0<\pi(n)\le C\).

Write \(q_j=U^jp\), using the level already constructed.

The sequence \(\pi(q_j)\) is nondecreasing by (6), and bounded above by
\(C\). Put \(L=\lim_j\pi(q_j)\in(0,C]\). At fixed level \(t\),
the sets

\[
A_{j,t}=\{n:U^{j-t}n=q_j\},\qquad j\ge\max(0,t),
\]

increase to the whole level \(h^{-1}(t)\). Iterating (6), with only
nonnegative sums, gives \(\sum_{A_{j,t}}\pi(n)=\pi(q_j)\).
Consequently

\[
\boxed{\sum_{h(n)=t}\pi(n)=L\quad(t\in\mathbb Z).}       \tag{7}
\]

The stationary-level construction and common path space already occur
in PR180 for its base flow. Formula (7) reconstructs the corresponding
critical tilted flow; it is not a priority claim for the level method.
The reversible-walk consequence below is the new consumer.

## 3. The symmetrized actual walk is null recurrent

Define

\[
S(q,n)=\tfrac12\mathbf1_{n=Uq}+\tfrac12K(q,n).           \tag{8}
\]

This is an irreducible Markov chain on \(E\). Its conductance on the
undirected edge \(\{n,Un\}\) is

\[
c(n,Un)=\pi(n)/2.                                      \tag{9}
\]

Indeed \(\pi(n)S(n,Un)=\pi(n)/2=\pi(Un)S(Un,n)\).
Each vertex has finite total conductance \(\pi(n)\), even though
it has infinitely many inverse neighbors.

### Theorem RN1

Under (1)--(3), \(S\) is recurrent and its mean return time to every
state is infinite.

**Proof.** For integer \(M\ge1\), take the level tent

\[
f_M(n)=\max(1-|h(n)|/M,0).
\]

Its support may be infinite, but it has finite \(\ell^2(\pi)\) norm:
there are fewer than \(2M+1\) nonzero levels, each of mass \(L\).
There are exactly \(2M\) level interfaces at which its increment has
absolute value \(1/M\). The total conductance across every interface
is \(L/2\), by (7) and (9). Therefore its Dirichlet energy is exactly

\[
\mathcal E_S(f_M)
=\frac12\sum_{q,n}\pi(q)S(q,n)(f_M(q)-f_M(n))^2
=\frac LM.                                             \tag{10}
\]

To justify the finite-support capacity test, exhaust the support by
finite sets containing \(p\) and truncate \(f_M\) to those sets.
The truncations converge in \(\ell^2(\pi)\). Since \(S\) is a
stationary Markov contraction on that space,
\(\mathcal E_S(v)=\langle v,(I-S)v\rangle_\pi
\le2\|v\|_2^2\); hence the truncated energies converge to (10).
All truncations equal one at \(p\). The finite-support Dirichlet
principle gives \(\operatorname{Cap}_S(p)\le L/M\) for every \(M\),
so \(\operatorname{Cap}_S(p)=0\). This is recurrence.

The capacity principle applies to countable networks with finite total
conductance at each vertex; finite graph degree is not required. An
explicit primary reference is Benjamini--Hermon, *Recurrence of Markov
chain traces*, arXiv:1711.03479v4, the network conventions on pages 1--2
and (2.3)--(2.4) on page 8:
<https://api.repository.cam.ac.uk/server/api/core/bitstreams/bde96264-63d8-45ff-b05d-1fedc4eff84b/content>.
Only that standard capacity principle is imported, not their trace theorem.

At every state, the level of the next step rises or falls by one with
probability exactly one half. Thus the level process is simple symmetric
random walk on \(\mathbb Z\). A return to \(p\) cannot precede its
level's first positive return to zero. The latter has infinite mean.
For example, from level 1 the expected time to hit \(\{0,N\}\) is
\(N-1\), so the expected time to hit zero is at least \(N-1\) for
every \(N\). Conditioning on the first level step proves the claim.
Irreducibility transfers it to every starting vertex. \(\square\)

The deterministic map \(U\) still escapes under the hypothesis defining
\(E\). The additional inverse choices in (8) are essential. Recurrence
of \(S\) is not recurrence of \(U\).

## 4. The physical coordinate and the attempted maximum principle

Use the bounded coordinate

\[
Y(n)=\Lambda(n)\in(0,1).
\]

It is PR180's \(y(n)/b_E\). Directly from (1),

\[
Y(Un)-Y(n)=r(n)/3,\qquad
Y(q)-Y(n)=2^{-a(n)}r(q)\quad(Un=q).                     \tag{11}
\]

In particular it is nonconstant and strictly increasing under every
forward edge. Set

\[
A(q)=\sum_{Un=q}K(q,n)2^{-a(n)}.
\]

The exact drift of (8) is

\[
\boxed{SY(q)-Y(q)=\frac{r(q)}2\left(\frac13-A(q)\right).}\tag{12}
\]

A positive superharmonic function on an irreducible recurrent chain is
constant: stop its nonnegative supermartingale at the almost-sure hitting
time of another vertex and apply Fatou; this gives \(f(x)\ge f(y)\),
and reversal gives equality. Thus the tempting uniform inequality
\(A(q)\ge1/3\) would contradict (11). The opposite uniform inequality
also fails, by applying the same argument to \(1-Y\).

The conclusion is precise:

\[
\boxed{\text{If such an escaping component exists, some actual vertices
have }A(q)<1/3\text{ and others have }A(q)>1/3.}           \tag{13}
\]

An actual-orbit average above \(1/3\) does not establish either
pointwise inequality. The forward drift includes the changing factor
\(r(q)\), and \(\sum_jr(q_j)\le\sum_j1/q_j<\infty\).
No invalid averaging is needed to explain its compatibility with a
bounded coordinate.

## 5. A finite measure that accounts for the drift cancellation

Now also use (4). The total mass

\[
Z_2=\sum_{q\in E}\pi(q)r(q)=\sum_{q\in E}G(q)r(q)^2
\]

is positive and finite. Define the probability
\(\eta_2(q)=G(q)r(q)^2/Z_2\). Then

\[
\boxed{\sum_q\eta_2(q)A(q)=\frac13.}                   \tag{14}
\]

To check this without exchanging signed divergent sums, use only positive
terms and (6):

\[
\begin{aligned}
\sum_q\pi(q)r(q)A(q)
&=\sum_{n\in E}\pi(n)r(Un)2^{-a(n)}\\
&=\frac13\sum_{n\in E}\pi(n)r(n).
\end{aligned}
\]

The last equality is (1). Both sides are finite by (4). This also proves
the integrated drift is zero with absolute convergence.

The new finite ordinary conformal measure is doing actual work here:
\(\eta_2\) is the normalized measure \(G\,d\mu_2\). It is not the
uniform time law along an escape, and not a claim that \(\eta_2\) is
stationary for \(K\) or \(S\). Its weights on the forward spine are
summable. Formula (14) therefore cannot be compared directly with the
strict unweighted actual-gap surplus in PR177 (HE13).

## 6. Why pointwise inverse dissipation also did not close the proof

For a fixed root and \(s>1\), (2) and (5) give the exact identity

\[
\frac{P_s^k(G^s)(q)}{G(q)^s}
=\sum_{U^kn=q}K^{(k)}(q,n)^s\le1.                       \tag{15}
\]

On an acyclic component each endpoint corresponds to just one path.
If the chosen inverse path measure is atomless, its largest
depth-\(k\) cylinder mass tends to zero. This also holds for countable
branching: if masses at least \(\varepsilon\) persisted, their
prefix tree would have finitely many such children at each node and an
infinite nested path of mass at least \(\varepsilon\). Consequently
the right side of (15) tends to zero, bounded by the largest cylinder
mass to the power \(s-1\). For the function constructed in Section 2,
atomlessness holds after conditioning the atomless \(\Pi\) on any
positive-mass vertex event. For a separately chosen canonical function,
atomlessness retains that source's qualifications. It is unnecessary
for RN1--(14).

The attempted closure was to integrate that pointwise decay against
\(\mu_s\). It has no integrable majorant of the displayed form:

\[
\int G^s\,d\mu_s=\sum_{q\in E}\pi(q)^s=\infty,         \tag{16}
\]

because \(\pi(q_j)\ge\pi(p)>0\) at infinitely many distinct actual
forward states. This failure retains the fixed source explicitly. In
fact, the one reversed prefix from \(q_j\) to \(p\) has probability
\(\pi(p)/\pi(q_j)\ge\pi(p)/L\); (15) at \(q=q_j,k=j\) is bounded
below by \((\pi(p)/L)^s\). Hence the pointwise dissipation is not
uniform over precisely the moving roots needed for the argument.

## 7. Remaining proof obligation

This attempt has constructed and classified the recurrence of a faithful
auxiliary walk, and calculated its exact physical drift and finite drift
average. It has not produced an arithmetic inequality that contradicts
those identities. A new argument would have to control the actual
state-dependent drift or supply a different positive excessive function
for (8), with all ordinary inverse branches retained. A uniform sign for
the drift in (12), canonical row comparability, or an integrated decay
estimate is not supplied by Haar contraction, a time average, or the
finite measure alone.

The deliberately constructed law can give any prescribed actual path
through \(p\) arbitrarily large retained forward-prefix probability:
give \(\Pi_p\) weight \(1-\varepsilon\) and use total weight
\(\varepsilon\) for the full-support enumeration mixture. All the
properties proved above survive, and \(\pi(p)\ge1-\varepsilon\).
Thus atomlessness, a positive harmonic function, bounded \(G/n\), finite
reciprocal moments, and recurrence of the symmetrized chain are compatible
with almost complete concentration on the actual reversed spine from
moving future roots. This is a construction conditional on an actual
escaping component; it neither creates such a component nor substitutes
a nonordinary model for it.

RN1 and the infinite analysis are written proofs. No Lean formalization
or computational verification of an infinite escaping component is claimed.
The previously compiled Lean arithmetic input proves the two legal larger
parents, not the new probability and recurrence assertions.

## 8. Elementary uniform count used in the construction

This is the PR177 (HE2) argument, itself crediting the PR92 orbit-cylinder
method and its PR175 consumers. The only extension is to the full
bi-infinite path, for which the same proof applies verbatim: \(U^k\) is
injective on its state set for every fixed \(k\), and all forward
valuations are actual positive integer valuations.

Let \(S\) be the distinct states of one such path and \(X\ge1\).
Set \(k=\lfloor(3/5)\log_2X\rfloor\) and
\(m=\lfloor5k/3\rfloor\). A word of \(k\) positive gaps of total
\(A\) selects one odd residue modulo \(2^{A+1}\). There are
\(\binom{A-1}{k-1}\) such words. Its endpoint formula is

\[
U^k(n)=(3^kn+B)/2^A,\qquad
0<B/2^A\le(3/2)^k-1.
\]

For \(k\ge1\), the lane \(A\le m\) has at most

\[
\frac32X\sum_{A\le m}\binom{A-1}{k-1}2^{-A}
\le\frac32X\rho^k,\qquad \rho^3=3125/3456<1.
\]

Indeed \(2^m\le X\), so a cylinder contains at most
\(X/2^{A+1}+1\le(3/2)X2^{-A}\) sources; inserting \(z=4/5\)
in \(\sum_{A\ge k}\binom{A-1}{k-1}(z/2)^A
=(z/(2-z))^k\) gives the stated \(\rho\).

In the other lane, \(A\ge m+1>5k/3\). Its endpoints are distinct
positive odd integers below
\(\sigma^kX+(3/2)^k-1\), where \(\sigma^3=27/32<\rho^3\).
Thus the number of sources in this lane is at most
\((\sigma^kX+(3/2)^k)/2\). Combining both lanes gives

\[
\#(S\cap[1,X])\le2X\rho^k+\tfrac12(3/2)^k
\le4X^{39/40}.                                         \tag{17}
\]

For the final loose margin, \(\rho>2/3\) and
\(8\,3125^{24}<3456^{24}\) imply \(\rho<2^{-1/24}\);
rounding \(k\) loses less than the displayed constant. Also
\((3/5)\log_2(3/2)<39/40\). If \(k=0\), the elementary bound
\(\#(S\cap[1,X])\le X\) suffices because \(X<2^{5/3}\).
No predecessor-basin injectivity is asserted: \(S\) is one path.

Nonnegative summation now gives

\[
\sum_{n\in S}\frac1n
=\int_1^\infty\#(S\cap[1,t])t^{-2}\,dt\le160.
\]

Applied to a forward subpath this also gives
\(\prod_j\lambda(U^jn)\ge e^{-160/3}\), using
\(\log(1+1/(3n))\le1/(3n)\). These are the only orbit-size
inputs needed in the new full-support mixture construction.
