# Direct pressure and collision attack on the retained ordinary law

Date: 2026-11-23.

**Status: new written deductions, with the finite comparison and counterexample
core separately checked in Lean. Escape exclusion remains OPEN.** The intended
contradiction is PR185's critical collision lower bound against an upper bound
for exactly the same ordinary inverse endpoint law. This note attempts that
upper bound using PR177's new finite ordinary atomic pressure measure. It
proves a genuine arithmetic off-diagonal estimate, carries out the change of
measure, and finds a quantitative obstruction to using a uniform density
comparison. It also tests the proposed alternative of turning endpoint
collisions into repeated actual gap words.

The new results are (6), (9)--(11), and the incompatibility of (15)--(15b)
with a critical estimate through this particular uniform-density argument.
The strongest version permits the pressure exponent to vary with the time
window. These results do
not establish the required upper bound for the ordinary time law. No new
closure-equivalent hypothesis is asserted as a theorem.

## 1. Frozen sources, map and exact target

The source ledger `SOURCES.json` records the paths and blob hashes actually
read. The relevant heads are:

| Source | Exact head | Material used |
|---|---|---|
| PR185 | `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d` | `COLLISION_LOGARITHMIC_GAIN.md`, Theorems 3--4 and equations (9)--(12); the actual ordinary kernel and retained masses in `SAME_SOURCE_INVERSE_ENTROPY.md`. |
| PR177 | `6de3e304bb49a93a6c5ef0e5563137e75c7defb4` | `HIGH_VARIANCE_ESCAPE.md`, HE-P3--P6, especially the ordinary atomic measure, its positive-atom tails, and its exact Green-integrability obstruction. |
| PR175 | `8870528daa6a13cc941d602e578e35c8bfa4bf4f` | The actual proofs in `risk23/HARDY_INVERSE_TREE.md` and `risk23/RENORMALIZED_FIBRE_ENTROPY_ATTACK.md`. Neither supplies the missing ordinary-law upper bound. |
| PR180 | `04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2` | `ANALYTIC_GLUING.md`, Sections 1--6: the common whole-path boundary, its actual source conditioning and the retained root cost in its routing comparison. |

Use the accelerated map

\[
 U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

on positive odd ternary units. Assume, for this attempted contradiction,
that one fixed ordinary source has an escaping orbit
\(q_j=U^j(q_0)\). In particular its states are distinct. Let \(E\) be
its entire ordinary component. Retain PR185's source-qualified positive
bounded ordinary harmonic flow

\[
 \nu(q)=\sum_{Un=q}\nu(n),\qquad
 v_j:=\nu(q_j)\uparrow C>0,
 \qquad K(q,n)=\mathbf1_{Un=q}\frac{\nu(n)}{\nu(q)}.
\]

For \(N=M+1\), the law under attack is precisely

\[
 \zeta_{M,r}=\frac1N\sum_{j=0}^{M}K^r(q_{r+j},\cdot),
 \qquad r\ge0.
 \tag{1}
\]

Ordinary endpoint uniqueness gives, for every finite inverse clock,

\[
 \zeta_{M,r}(\{q_j\})
   =\frac{v_j}{Nv_{r+j}}\ge\frac{c_0}{N},
 \qquad c_0=v_0/C>0.
 \tag{2}
\]

The new PR185 bound is

\[
 \operatorname{Col}_{3^m}(\zeta_{M,r})
 \ge c\sqrt m\,3^{-\theta m},\qquad
 \theta=0.949955527188\ldots,
 \tag{3}
\]

uniformly over \(r\), when \(m^2=O(M)\). Here
\(\operatorname{Col}_{Q}(\sigma)=\sum_{a\bmod Q}
\sigma(a+Q\mathbb Z)^2\). The intended opposing estimate is
\(O(Q^{-\theta})\) with \(Q=3^m\), on this same law. All uses of
\(\nu\) retain the analytic qualifications of the pinned construction.

## 2. A genuine arithmetic upper bound for the pressure measure

For \(s>1\), PR177 constructs on this same component

\[
 r_E(n)=\frac{\Lambda_\infty(n)}n,\qquad
 \mu_s=\sum_{n\in E}r_E(n)^s\delta_n,
 \qquad S_s=\mu_s(E)\in(0,\infty),
 \tag{4}
\]

where \(0<\Lambda_\infty(n)\le1\) is the actual infinite forward
product of \(3n/(3n+1)\). The elementary orbit count needed for its
positivity was reconstructed in that source independently of the canonical
envelope. Thus \(\mu_s(\{n\})\le n^{-s}\). Its pressure identity is
\(\mu_sP_s=\mu_s\), with

\[
 P_sf(q)=\sum_{Un=q}(3/2^{v_2(3n+1)})^s f(n).
\]

This is a conformal measure for that operator. It is not the endpoint law
(1), and \(P_s\) is not a probability kernel. Normalize only this
measure by \(\bar\mu_s=\mu_s/S_s\).

Separate ordinary diagonal atoms from modular collisions:

\[
 \mathcal O_Q(\sigma)=
 \sum_{\substack{n,k\ge1\\n\ne k,\ Q\mid n-k}}
       \sigma(\{n\})\sigma(\{k\}),\qquad
 \operatorname{Col}_Q(\sigma)=
 \sum_n\sigma(\{n\})^2+\mathcal O_Q(\sigma).
 \tag{5}
\]

For the law (1), different roots \(q_{r+j}\) have disjoint \(r\)-step
ordinary preimage supports: an endpoint has only one deterministic forward
image at that clock. Each root is chosen with mass \(1/N\), so every
ordinary atom of \(\zeta_{M,r}\) is at most \(1/N\). Together with (2),
this proves

\[
 \frac{c_0^2}{N}\le\sum_n\zeta_{M,r}(\{n\})^2\le\frac1N.
\]

Thus at scales \(Q\le C N^{1/\theta}\), an
\(O(Q^{-\theta})\) estimate for its *actual off-diagonal part* would
indeed give the required full collision upper bound. The off-diagonal
estimate, rather than the ordinary diagonal, is the unresolved part.

**Proposition 1.** For every positive integer \(Q\),

\[
 \boxed{\mathcal O_Q(\mu_s)\le2\zeta(s)^2Q^{-s},\qquad
 \mathcal O_Q(\bar\mu_s)
       \le\frac{2\zeta(s)^2}{S_s^2}Q^{-s}.}
 \tag{6}
\]

Here \(\zeta(s)=\sum_{n\ge1}n^{-s}\) denotes the convergent positive
series; no unproved statement about the Riemann zeta function is involved.

**Proof.** Extend the atom weights by zero outside \(E\). For every
ordered unequal congruent pair, exactly one of \(n<k\) and \(k<n\)
holds. Write the larger integer uniquely as \(n+\ell Q\),
\(\ell\ge1\). Positivity of the ordinary integers, followed by Tonelli,
gives

\[
\begin{aligned}
 \mathcal O_Q(\mu_s)
 &=2\sum_{n\ge1}\sum_{\ell\ge1}
     \mu_s(\{n\})\mu_s(\{n+\ell Q\})\\
 &\le2\sum_{n\ge1}n^{-s}
                  \sum_{\ell\ge1}(n+\ell Q)^{-s}\\
 &\le2\left(\sum_{n\ge1}n^{-s}\right)
              \left(\sum_{\ell\ge1}(\ell Q)^{-s}\right)
 =2\zeta(s)^2Q^{-s}.
\end{aligned}
\]

Normalization gives the second inequality. This argument uses neither
Haar measure nor a stationary substitution for the source. \(\square\)

The exponent \(s\) cannot be improved for all positive integer measures
with atom bound \(n^{-s}\): for the measure having all these weights,
the pair \(1,1+Q\) contributes \(2(1+Q)^{-s}\). This sharpness
example is not asserted to be a Collatz component measure.

For the pressure measure itself the full collision sum does not tend to
zero: it retains \(\sum_n\bar\mu_s(\{n\})^2>0\). Subtracting the
ordinary diagonal in (5) is essential even before comparing laws.

## 3. The actual change of measure has unavoidable growing norms

Every endpoint in (1) belongs to \(E\), so it is absolutely continuous
with respect to the purely atomic \(\bar\mu_s\). Write its literal
density as

\[
 f_{M,r}(n)=\frac{\zeta_{M,r}(\{n\})}
                  {\bar\mu_s(\{n\})}.
 \tag{7}
\]

This absolute continuity is on the countable ordinary support. It is not
absolute continuity with respect to Haar measure. From the single retained
source atoms (2),

\[
 f_{M,r}(q_j)\ge\frac{c_0S_s}{N}q_j^s.
 \tag{8}
\]

**Proposition 2.** For every \(p>1\), uniformly over every finite \(r\),

\[
 \boxed{\|f_{M,r}\|_{L^p(\bar\mu_s)}^p
 \ge\frac{c_0^pS_s^{p-1}}{s(p-1)+1}
             N^{(s-1)(p-1)}.}
 \tag{9}
\]

The inequality permits an infinite norm. If
\(H_M=\max_{0\le j\le M}q_j\), the corresponding pointwise bound is

\[
 \boxed{\|f_{M,r}\|_\infty
             \ge\frac{c_0S_s}{N}H_M^s.}
 \tag{10}
\]

**Proof.** Since \(\bar\mu_s(\{q_j\})\le(S_sq_j^s)^{-1}\),

\[
 \sum_n\zeta_{M,r}(\{n\})^p\bar\mu_s(\{n\})^{1-p}
 \ge\frac{c_0^pS_s^{p-1}}{N^p}
                   \sum_{j=0}^Mq_j^{s(p-1)}.
\]

After sorting these \(N\) distinct positive integers, their \(k\)-th
smallest is at least \(k\). For every \(a>0\),
\(\sum_{k=1}^{N}k^a\ge\int_0^Nx^a\,dx=N^{a+1}/(a+1)\).
Taking \(a=s(p-1)\) proves (9); (10) is (8) at a maximum-height
state. \(\square\)

Thus not even a uniform \(L^{1+\varepsilon}\) comparison is available:
it is contradicted by the unchanged original-source atoms. Taking deeper
inverse clocks does not reduce this lower bound.

There is also an information version. With relative entropy allowed to be
infinite,

\[
 \boxed{\liminf_{M\to\infty}\ \inf_{r\ge0}
 \frac{D_{\rm KL}(\zeta_{M,r}\Vert\bar\mu_s)}{\log(M+1)}
 \ge s-1.}
 \tag{11}
\]

To verify it directly, fix \(a\ge0\) and put \(c_a=v_a/C\).
On the retained atoms, (8) bounds \(\log f\) below by
\(\log(c_0S_s/N)+s\log q_j\). For large \(N\) its constant term
is negative and the total retained mass is at most one. On \(j\ge a\)
use the sharper mass lower bound \(c_a/N\). The omitted part of
\(\int f\log f\,d\bar\mu_s\) is at least \(-1/e\), because
\(x\log x\ge-1/e\). Therefore

\[
 D_{\rm KL}(\zeta_{M,r}\Vert\bar\mu_s)
 \ge\log(c_0S_s/N)+\frac{sc_a}{N}\log((N-a)!)-1/e.
\]

Use \(\log((N-a)!)=N\log N-N+o(N\log N)\), then let
\(a\to\infty\), so \(c_a\to1\). This proves (11) uniformly in
the inverse clock. No entropy-continuity claim on a moving infinite
alphabet is being made.

## 4. The literal uniform-density route cannot reach the critical scale

The tempting transfer of (6) is valid as an inequality. Put
\(D_{M,r}=\|f_{M,r}\|_\infty\). When this is finite,

\[
 \mathcal O_Q(\zeta_{M,r})
 \le D_{M,r}^2\mathcal O_Q(\bar\mu_s)
 \le B_{M,r,Q}:=\frac{2\zeta(s)^2}{S_s^2}D_{M,r}^2Q^{-s}.
 \tag{12}
\]

The coordinating root agent contributed a sharper transfer, independently
reconstructed in this lane and by the separate reviewer. It uses the total
probability mass of one factor, rather than its maximum density. From
\(\zeta_{M,r}(\{k\})\le D_{M,r}/(S_s k^s)\),

\[
\begin{aligned}
 \mathcal O_Q(\zeta_{M,r})
 &=2\sum_{n\ge1}\zeta_{M,r}(\{n\})
          \sum_{\ell\ge1}\zeta_{M,r}(\{n+\ell Q\})\\
 &\le \frac{2D_{M,r}}{S_s}
       \sum_{n\ge1}\zeta_{M,r}(\{n\})
          \sum_{\ell\ge1}(\ell Q)^{-s}\\
 &=\boxed{\frac{2\zeta(s)}{S_s}D_{M,r}Q^{-s}}
   =:B^{\rm lin}_{M,r,Q}.
\end{aligned}
 \tag{12a}
\]

Thus no squared density loss is necessary. The following calculation tests
this sharper estimate as well as (12).

The problem is quantitative, not merely the absence of a comparison
theorem. The newest PR185 height theorem implies, for all sufficiently
large \(N\),

\[
 H_M\ge c_HN^{1/\theta}(\log N)^{1/(2\theta)}.
 \tag{13}
\]

Changing \(1+H_M\) in its original statement to \(H_M\) only changes
the constant. Combining (10) and (13) gives

\[
 D_{M,r}^2\ge c_sN^{2s/\theta-2}(\log N)^{s/\theta}.
 \tag{14}
\]

Moreover, a proposed critical *full* collision bound
\(\operatorname{Col}_{Q}(\zeta_{M,r})\le A Q^{-\theta}\),
with fixed \(A\), must respect its ordinary diagonal:
\(\operatorname{Col}_{Q}(\zeta_{M,r})\ge c_0^2/N\) by (2).
Consequently every potentially useful scale satisfies
\(Q\le C_A N^{1/\theta}\).

At all such scales, since \(s>1>\theta\), (12)--(14) imply

\[
 \boxed{\frac{B_{M,r,Q}}{Q^{-\theta}}
 \ge c_{s,A}N^{s/\theta-1}(\log N)^{s/\theta}
 \longrightarrow\infty.}
 \tag{15}
\]

For the sharper one-density bound, (10), (13), and the same necessary
precision restriction give, for each fixed \(s>1\),

\[
 \frac{B^{\rm lin}_{M,r,Q}}{Q^{-\theta}}
 \ge c_{s,A}(\log N)^{s/(2\theta)}\longrightarrow\infty.
 \tag{15a}
\]

Here the logarithmic factor in the newest running-height theorem supplies
the entire divergence; its critical power alone would give only a constant
at the largest usable precision.

The root agent also observed that tuning the pressure exponent does not
avoid this obstruction. Take
\(C_A=(A/c_0^2)^{1/\theta}>0\), so \(Q\le C_A N^{1/\theta}\).
Before absorbing any constants depending on \(s\), the exact calculation
is

\[
\begin{aligned}
 \frac{B^{\rm lin}_{M,r,Q}}{Q^{-\theta}}
 &\ge 2c_0\zeta(s)\frac{H_M^s}{N}Q^{\theta-s}\\
 &\ge2c_0\zeta(s)C_A^\theta
       \left[\frac{c_H}{C_A}
                     (\log N)^{1/(2\theta)}\right]^s\\
 &\ge\boxed{2c_0c_HC_A^{\theta-1}
                        (\log N)^{1/(2\theta)}}.
\end{aligned}
 \tag{15b}
\]

The final line holds once the bracket is at least one, because
\(\zeta(s)\ge1\) and \(s>1\). The normalization \(S_s\) cancels in
the first line. The constants \(c_0,c_H,C_A\) and the required onset
are independent of \(s\). Thus (15b) holds uniformly over every choice
\(s=s_N>1\), including choices tending to one, and every inverse clock.
If the chosen density norm is infinite, it already gives no finite upper
bound. No uniformity in \(s\) of a hidden moment estimate is assumed.

**Interpretation of (15)--(15b).** Both available comparison bounds,
including the sharper \(B^{\rm lin}_{M,r,Q}\), are necessarily too large
to deliver the critical same-law upper bound. This holds even when the
pressure parameter is adapted to the window length. It is not a lower
bound on the actual
off-diagonal collision sum, and it is not a claim that every possible
pressure argument fails. A nonuniform bilinear estimate could exploit
which high-density atoms actually share a residue; the uniform maximum
in (12) and (12a) discards that information. No such estimate was proved here.

This calculation uses the fresh critical height exponent in a substantive
way. It keeps the original source, the exact inverse clock, and the
ordinary positive atoms throughout. Replacing the norm in (14) by a Haar
norm would remove precisely the retained terms that make it grow.

## 5. Endpoint collisions do not recover repeated critical-budget words

The second direct attempt was to turn the excess collisions in (3) into
repetitions, then use ordinary two-adic integrality to force an exact cycle
or an unusually strong rational approximation. The first possible inference
already needs more arithmetic information.

A length-\(m\) past gap word determines its endpoint modulo \(3^m\).
The reverse implication fails, even for different words below the critical
total-gap budget, on one actual ordinary orbit. Starting at 41, the windows
ending at clocks 21 and 28 are

\[
 167\xrightarrow{1}251\xrightarrow{1}377
       \xrightarrow{2}283\xrightarrow{1}425,
\]

\[
 719\xrightarrow{1}1079\xrightarrow{1}1619
       \xrightarrow{1}2429\xrightarrow{3}911.
\]

Both endpoints are \(20\pmod{81}\), but the actual words are
\((1,1,2,1)\) and \((1,1,1,3)\). Their total gaps are 5 and 6;
both are at most \(4\log_2 3\), since \(2^6<3^4\). All the displayed
states are positive odd units. The complete common-source prefix, not two
independent witnesses, is included in the Lean certificate.

The algebra is systematic. For \(m\ge2\), the words

\[
 w_m=(1^{m-2},2,1),\qquad v_m=(1^{m-1},3)
\]

have total gaps \(m+1,m+2\) and affine maps

\[
 F_{w_m}(x)=\frac{3^m(x+1)}{2^{m+1}}-\frac14,
 \qquad
 F_{v_m}(x)=\frac{3^m(x+1)}{2^{m+2}}-\frac14.
 \tag{16}
\]

Every integral endpoint of either map is \(-4^{-1}\pmod{3^m}\).
For \(m\ge4\), both totals are below \(m\log_2 3\): the inequality
\(2^{m+2}<3^m\) holds at 4 and persists upon multiplication by 2
and 3. Thus critical cost alone does not make the word-to-residue map
injective. The finite example above establishes that this ambiguity is
present within one actual ordinary trajectory.

The repeated-block bound below is already present mathematically in our
baseline `research/global-synthesis-20261122/ARITHMETIC_CLOSURE.md`,
Section 3, with its existing `IndependentBlockBudget.lean` consumer. It is
reused here to identify the quantitative information that the collision
argument does not provide; it is not counted as a new repetition theorem.
The present self-contained Lean core additionally derives its finite
telescope directly from a supplied list of repeated affine edges.

For an actual repeated block of length \(m\), total valuation \(A\),
and affine numerator \(B\), there is a real two-adic constraint. If the
same block repeats \(k\) times from an ordinary source \(x\), put
\(D=2^A-3^m\). Exact replay implies

\[
 2^{kA}\mid 3^{km}(Dx-B),
 \qquad\text{hence}\qquad 2^{kA}\mid Dx-B.
 \tag{17}
\]

Indeed \(D F_w(x)-B=(3^m/2^A)(Dx-B)\), and iteration yields
the first divisibility because the final state is an integer. If
\(Dx-B\ne0\), (17) forces \(2^{kA}\le|Dx-B|\). If it vanishes,
the supplied word already fixes its original ordinary source. This exact
repeat test is valid, but (3) neither supplies repeated consecutive blocks
nor removes the nonidentical-word collisions in (16). At the collision
scale \(m=O(\log M)\), a widely separated repeated word alone also
does not supply an approximation at precision comparable to a potentially
exponential source height. No Diophantine approximation theorem is invoked
without that missing quantitative premise.

## 6. Outcome of the attempted full contradiction

The pressure lane yields the arithmetic upper (6), but its actual transfer
has the unavoidable growing densities (9)--(11). Even the sharper
one-density transfer (12a) fails quantitatively by (15b), uniformly for all
varying pressure parameters \(s>1\). The repetition lane
must first distinguish the nonidentical-word collisions already present in
(16); it cannot treat residue equality as a repeated itinerary.

PR175's Hardy construction concerns signed square-summable incoming flows,
not an upper estimate for the nonnegative law (1). Its renormalized real
boundary argument computes a compact quotient coordinate whose integer-part
entropy does not become endpoint entropy. PR180's common path conditioning
does retain the source; its routing comparison still pays
\(\log(q\nu(q)/\gamma)\). PR177's pressure Green function is finite at
ordinary atoms, but \(\int Z_s\,d\mu_s=\infty\); one unchanged source
contributes a fixed amount at every distinct future vertex. None of those
exact statements removes the costs calculated here.

The first unsupported step in the remaining bilinear attempt would be an
upper bound for

\[
 \sum_{\substack{n\ne k\\n\equiv k\ (3^m)}}
 f_{M,r}(n)f_{M,r}(k)
       \bar\mu_s(\{n\})\bar\mu_s(\{k\})
\]

that uses the arithmetic locations of its large actual densities strongly
enough to beat (3). Neither boundedness of their unweighted pressure law,
Haar contraction, full topological support, nor mere word repetition proves
that estimate. It is not added as an axiom. The actual same-law upper bound,
escape exclusion and full Collatz theorem remain unresolved.

## 7. Formal scope and execution

`lean/PressureCollisionCore.lean` contains ten public theorems. Its first
three prove the finite pair-density comparison and the unavoidable cost
of a retained atom. Its next four give a self-contained finite
formalization of the reused repeated-block argument: the exact affine-word
telescope, coprime cancellation, the Collatz power specialization, and the
resulting nonzero-displacement lower bound. Its last three certify the
complete common-source prefix from 41, distinct positive unit states, and
the critical-budget collision between the two different actual past words.

The proof and its separate axiom audit compiled with Lean 4.34.1 and
Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, with
`autoImplicit=false` and warnings treated as errors. The axiom union is
`propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`, imported closure
axiom, or native proof shortcut appears. Installed dependency objects were
reused. The infinite sums, real-power estimates, KL asymptotics and
scheme obstructions (15)--(15b) remain written proofs, and the source-qualified
canonical flow is not asserted in Lean. See the exact compiler receipt
and audit in `reports/2026-11-23-global-closure/escape-lean-build.json`
and `escape-lean-audit.log`.
