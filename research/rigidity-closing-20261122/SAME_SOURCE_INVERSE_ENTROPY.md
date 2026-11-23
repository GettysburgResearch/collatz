# The actual entropy ceiling survives arbitrary moving inverse clocks

Date: 2026-11-22. Baseline: PR185,
`980d40fc4afeaaf8f2a9256f322acf3e4568e013`.

**Status: new written deduction, conditional on the repository's existing
ordinary harmonic flow; no full Collatz conclusion.** The finite coupling
below transfers the actual-orbit entropy ceiling to a canonical inverse
law while keeping the original ordinary source. It works uniformly at
every inverse depth, including depths much larger than the averaging
window. It avoids a weak-limit interchange for a discontinuous kernel.
It does not supply the opposite entropy inequality needed to exclude
escape.

The inputs are the ordinary harmonic flow used in
`MOVING_INVERSE_WINDOW.md` and the elementary finite actual-orbit bound in
`research/deep-closing-20261122/ACTUAL_ORBIT_ENTROPY.md`. The construction
of the flow retains its external analytic dependencies. The finite
probability and entropy arguments here are written proofs, not a claim of
Lean verification of probability theory or of those external inputs.

## 1. One actual source, one exact kernel

Suppose one fixed positive odd ternary-unit source has a non-eventually-
periodic orbit

\[
q_j=U^j(q_0),\qquad 2^{g_j}q_j=3q_{j-1}+1\quad(j\ge1).
\]

The existing source-qualified ordinary flow satisfies

\[
0<\nu(q)\le A,\qquad \nu(q)=\sum_{Ux=q}\nu(x).
\]

Write

\[
v_j=\nu(q_j),\qquad v_j\uparrow C\in(0,A],\qquad
K(q,x)=\frac{\nu(x)}{\nu(q)}\mathbf1_{\{Ux=q\}}.
\tag{1}
\]

This is the ordinary harmonic-flow kernel. It is not silently identified
with a geometric inverse policy or the other canonical transforms in the
repository.

For integers \(M,r\ge0\), define two occupation measures

\[
\pi_M=\frac1{M+1}\sum_{j=0}^M\delta_{q_j},\qquad
\pi_{M,r}=\frac1{M+1}\sum_{j=0}^M\delta_{q_{r+j}}.
\tag{2}
\]

To sample the moving inverse law, choose \(J\) uniformly from
\(\{0,\ldots,M\}\), keep that label, and run \(r\) inverse steps of
\(K\) from \(q_{r+J}\). Its endpoint law is
\(\zeta_{M,r}=(K^r)_*\pi_{M,r}\). The comparison path uses that same label
and the same source orbit, and outputs
\((q_{r+J},q_{r+J-1},\ldots,q_J)\).

## 2. Uniformity in every inverse depth

The probability of this exact path, conditional on \(J=j\), telescopes:

\[
\Pr\{\text{exact retracing}\mid J=j\}
=\prod_{i=j+1}^{r+j}\frac{v_{i-1}}{v_i}
=\frac{v_j}{v_{r+j}}.
\tag{3}
\]

Each comparison law, conditional on its retained label, is a point mass.
Consequently the total variation distance of the **labelled complete
path laws** is exactly

\[
\varepsilon_{M,r}
=\frac1{M+1}\sum_{j=0}^M\left(1-\frac{v_j}{v_{r+j}}\right).
\tag{4}
\]

Since \(v_{r+j}\le C\), set

\[
\eta_M=1-\frac1{C(M+1)}\sum_{j=0}^M v_j.
\]

Then

\[
\boxed{\sup_{r\ge0}\varepsilon_{M,r}=\eta_M\longrightarrow0.}
\tag{5}
\]

For fixed \(M\), the summands in (4) increase as \(r\) increases and
converge to \(1-v_j/C\), proving the equality in (5). The subsequent
limit is simply Cesaro convergence of \(v_j\) to \(C\). There is no
relation required between \(r\) and \(M\). For a quantitative expression
in terms of the as yet unbounded capacity tail, every \(0\le L\le M\)
gives

\[
\eta_M\le\frac{L}{M+1}+1-\frac{v_L}{C}.
\tag{6}
\]

In this ordinary state space, endpoint projection in fact preserves the
exact distance. If an \(r\)-step endpoint from \(q_{r+j}\) is some
forward-ray state \(q_k\), deterministic forward iteration gives
\(q_{r+k}=q_{r+j}\). The actual ray is injective, so \(k=j\). The only
inverse path to that endpoint is its actual forward history reversed.
Consequently

\[
\zeta_{M,r}(q_j)=\frac{v_j}{(M+1)v_{r+j}}\quad(0\le j\le M),
\qquad \zeta_{M,r}(q_k)=0\quad(k>M).
\tag{7a}
\]

On the support of \(\pi_M\) the difference \(\pi_M-\zeta_{M,r}\) is
nonnegative and has mass \(\varepsilon_{M,r}\). All the remaining mass
of \(\zeta_{M,r}\) lies outside the actual forward ray. Thus

\[
\|\zeta_{M,r}-\pi_M\|_{\rm TV}
=\zeta_{M,r}(\{q_j:j\ge0\}^{\mathsf c})
=\varepsilon_{M,r},\qquad
\boxed{\sup_{r\ge0}
\|\zeta_{M,r}-\pi_M\|_{\rm TV}=\eta_M\to0.}
\tag{7}
\]

These are probabilities on the ordinary integers themselves. The source
does not vary with \(M\) or \(r\). The root distribution does vary, but
it is exactly the stated time window of this one source. This is stronger
than a statement about two independently constructed boundary laws.

The per-root estimate in `MOVING_INVERSE_WINDOW.md` remains useful and is
sharper when all endpoints lie beyond a specified \(L\). Equation (5)
instead allows the early endpoints because their proportion tends to zero.

## 3. Finite ternary entropy, before taking any limit

Let \(H_m\) denote entropy of reduction modulo \(3^m\), with natural
logarithms. Couple an inverse endpoint \(Y\) and the actual endpoint
\(Z=q_J\) using the paths above. They agree on successful retracing.
Let \(E\) be its failure indicator. The chain rule gives

\[
H(Y\bmod3^m\mid Z\bmod3^m)
\le h_b(\varepsilon_{M,r})+\varepsilon_{M,r}m\log3,
\]

and the same estimate holds with \(Y,Z\) interchanged. Subtracting the
two entropy chain rules yields the elementary finite-alphabet continuity
bound

\[
\boxed{
|H_m(\zeta_{M,r})-H_m(\pi_M)|
\le h_b(\varepsilon_{M,r})+
       \varepsilon_{M,r}m\log3.}
\tag{8}
\]

This proof is valid even when a failed complete path has the correct
ternary endpoint. It uses the full-path failure probability as a coupling
bound, without asserting that it equals ternary-projected endpoint total
variation. Its equality with ordinary endpoint total variation was
proved separately in Section 2.

Keeping the ordinary root label gives, separately,

\[
H(Y\bmod3^m\mid J)
\le h_b(\varepsilon_{M,r})+
       \varepsilon_{M,r}m\log3.
\tag{9}
\]

Thus the small conditional randomness does not imply that a weak ternary
limit has zero entropy. Forgetting the label can retain information in the
distribution of actual roots. Equations (8)--(9) state exactly which
entropies have been compared.

For all sufficiently large \(M\), \(\eta_M\le1/2\), so binary entropy is
increasing on the relevant range and (8) is at most
\(h_b(\eta_M)+\eta_M m\log3\), uniformly in \(r\) and \(m\).

## 4. The actual entropy ceiling transfers at growing precision

Put

\[
A_M=\sum_{i=1}^M g_i,\quad
\ell=\log_2 3,\quad
\Phi(a)=a\log a-(a-1)\log(a-1),\quad
\theta=\frac{\Phi(\ell)}{\log3}<1.
\]

The baseline finite actual-source proof states that, for \(1\le m\le M\),
the endpoint law selected uniformly from \(\{q_m,\ldots,q_M\}\) has
entropy at most

\[
m\Phi\left(\frac{A_M}{M-m+1}\right).
\]

Splitting \(\pi_M\) into the first \(m\) times and the remaining times,
and adjoining the indicator of that split, gives the explicit boundary
correction, with \(t=m/(M+1)\):

\[
H_m(\pi_M)
\le h_b(t)+t m\log3+
(1-t)m\Phi\left(\frac{A_M}{M-m+1}\right).
\tag{10}
\]

Combining (8) and (10), for every \(r\ge0\),

\[
\begin{aligned}
H_m(\zeta_{M,r})\le{}&
h_b(t)+t m\log3+
(1-t)m\Phi\left(\frac{A_M}{M-m+1}\right)\\
&+h_b(\varepsilon_{M,r})+
\varepsilon_{M,r}m\log3.
\end{aligned}
\tag{11}
\]

Real positivity and distinctness imply the already proved bound
\(\limsup A_M/M\le\ell\). Therefore for **any** positive integer
sequence \(m_M=o(M)\), including a fixed precision, (5), continuity and
monotonicity of \(\Phi\) on \([1,\infty)\), and (11) imply

\[
\boxed{
\limsup_{M\to\infty}\ \sup_{r\ge0}
\frac{H_{m_M}(\zeta_{M,r})}{m_M\log3}
\le\theta.}
\tag{12}
\]

No Feller property, compact-kernel limit, unbounded-gap entropy continuity,
or exchange of weak convergence and a Markov operator has been used.
The assertion holds at finite precision first and only then takes the
displayed single limit. It is conditional on the existence of the one
escaping source used throughout, as is the original entropy ceiling.

## 5. What a genuine rigidity import would still have to prove

To close this route one could establish, for the very measures
\(\zeta_{M,r}\) above, a lower bound exceeding (12) at some allowable
precision and inverse clock. None of the sources checked supplies that
bound.

One explicit quantitative sufficient condition is the following: on each
hypothetical escaping source, find \(\delta>0\), integers
\(M_k\to\infty\), \(m_k\to\infty\) with \(m_k=o(M_k)\), and clocks
\(r_k\ge0\), such that the **same** moving-root inverse endpoint laws obey

\[
\sum_{a\bmod3^{m_k}}
  \zeta_{M_k,r_k}(a+3^{m_k}\mathbb Z_3)^2
\le 3^{-(\theta+\delta)m_k}.
\tag{13}
\]

Shannon entropy is at least minus the logarithm of this collision sum,
so (13) contradicts (12). Here the root law is exactly
\(\pi_{M_k,r_k}\) from (2). No assertion about a fixed-root limiting law,
an independent inverse source, or an almost-everywhere stationary fibre
can replace (13) without a further comparison. Equation (13) is a precise
unproved closing target, not a new theorem.

**Higher-rank measure rigidity.** Rudolph's theorem for the commuting
\(\times2,\times3\) maps requires invariance under both maps, the relevant
ergodicity hypothesis, and positive entropy. The newer solenoid version,
Einsiedler--Lindenstrauss, Theorem 1.2, assumes a totally irreducible,
non-virtually-cyclic action by commuting automorphisms and invariance under
that action. Its conclusion is a Haar-or-zero-entropy alternative. The
actual Collatz recurrence provides one adaptively selected affine map;
(7) does not manufacture either separate dilation invariance or the
required positive entropy. The first unsupported line would be to declare
the actual time law invariant under those extra actions.

Primary statements inspected:

- Rudolph, *Times 2 and times 3 invariant measures and entropy*:
  <https://doi.org/10.1017/S0143385700005629>.
- Einsiedler--Lindenstrauss, *Rigidity properties for commuting
  automorphisms on tori and solenoids*, Theorems 1.2--1.3:
  <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B5B7471AB9A282B5B179E35040809159/S0143385721000742a.pdf/div-class-title-rigidity-properties-for-commuting-automorphisms-on-tori-and-solenoids-div.pdf>.

**Local entropy averages.** Hochman--Shmerkin, Theorem 10.5, again assumes
simultaneous invariance under multiplicatively independent integer
multiplications, together with positive entropy of the relevant ergodic
components. Their conditional-measure processes are generated by
rescaling a measure with its actual mass weights. Replacing such a process
by the chosen-time Collatz process is an extra hypothesis. The checked
theorem does not turn (9) into a lower bound for (12).

Primary statement and its local-entropy setup inspected:
<https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n3-p01-p.pdf>.

**Canonical inverse frequencies.** Paper 12, Sections 8--10, obtains
fixed-root selection from a Cesaro trace, then positive upper word
frequencies from visits to bounded profile levels. Its coefficient is
independent of the root; the onset is not. Section 18 explicitly supplies
no root-uniform waiting time. Its least-ancestor entropy control also does
not bound physical parent heights. These statements cannot be inserted
as an early inverse-clock entropy lower bound.
<https://rstation.ai/problems/collatz/papers/12>.

**Newest source-retaining moving fibres.** PR175 at
`08fe1388ad63c758680b3695249aca319515c47d`,
`machinery/MOVING_CESARO_FIBRES.md`, Sections 7--9, compares moving ordinary
fibres at precision \(k+r+1\), after the source clock \(k\), and preserves
a positive original-source submeasure in equation (32). Its kernel
transforms also require the stated comparisons before being identified
with (1). That result is consistent with (12); it asserts neither a
uniform early onset nor a full-entropy classification of these fibres.

The inspected higher-rank statements are the primary theorem statements
and their hypotheses, not a fresh verification of their complete proofs.
The newer Collatz manuscripts remain source-qualified. GRH supplies no
missing invariance or onset estimate in any of these deductions.

## 6. Review of the companion clock criterion

The labelled-path TV identity (5), window budget (6), per-root
linear-depth estimate (7)--(8), and conditional capped-word entropy (10)
in `MOVING_INVERSE_WINDOW.md` are valid. Its largest-complete-path-atom
clock satisfies

\[
\tau_\varepsilon(q_N)>N-J
\]

once \(v_J>(1-\varepsilon)C\). Therefore a proved bound
\(\tau_\varepsilon(q)\le a\log(q+2)+b\) would force
\(\liminf_N\log(q_N+2)/N\ge1/a\), excluding zero-exponential-speed
escape. The inequality is a valid conditional consequence; the bound on
\(\tau_\varepsilon\) is not proved by fixed-root atomlessness, inverse
word frequencies, or the post-source-clock result in PR175.

The new entropy transfer does not bypass that missing arithmetic input.
It shows that the canonical inverse law and the actual low-entropy time
law can be compared directly, at all moving clocks, while retaining the
source. The central task is now an opposite estimate for those same
finite laws, not a change to a more regular source distribution.
