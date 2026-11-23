# A bounded change of harmonic flow removes the inverse-clock rate loss

23 November 2026. Author: `stationary_rigidity`.

**Status: PROPOSED written deductions from the stated ordinary-component
hypotheses. The original-source collision upper and escape exclusion remain
OPEN.** The construction below supplies a quantitative coalescence rate,
while leaving the complete inverse law at the original root unchanged.
It does not supply the still-missing arithmetic estimate on the original
orbit's residue pairs.

The preceding PR178 packet identified an actual coalescence-time rate as
a sufficient interface for transferring collision bounds. Its fixed-tilt
example showed that the enumerated flow and boundary properties alone do
not imply such a rate for an arbitrarily specified law. Here the approach
is constructive: choose one equivalent positive ordinary harmonic flow
whose joining time has an exponential tail. This is an explicit change
of law, with its preserved and lost properties recorded below.

## 1. One ordinary component and the exact source inputs

Use the accelerated map on positive odd integers prime to three,

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

Fix one hypothetical escaping ordinary orbit `q_j=U^j(q_0)`, `j>=0`,
and let `E` be its coalescence component. Every vertex of `E` eventually
reaches this forward spine. Its graph has no cycle. Assume a positive
harmonic flow with finite positive spine capacity:

\[
\nu(q)=\sum_{Un=q}\nu(n),\qquad
v_j=\nu(q_j)\uparrow C\in(0,\infty).
\tag{1}
\]

All sums are over legal ordinary unit parents. Harmonicity makes the
flow nondecreasing along every forward path, so (1) already implies
`0<nu(n)<=C` on the whole component.

The graph-only construction in Sections 2--4 needs no whole-path
probability or analytic boundary theorem. Those additional supplied
objects are used only to identify the change of path law and transfer
the previously established boundary properties in Section 5.

| Frozen source | Exact use |
| --- | --- |
| PR178, `e6ed7f1429ced4b58b85ca9006edd9a3a12ca193`, `research/profound-step-20261123/dynamics/COALESCENCE_AND_CRITICAL_COLLISIONS.md`, Sections 1--4 | Original component/kernel, exact variation identity, coalescence interpretation, and root-collision stability |
| PR180, `a436db7b85f37abafea25f42d6f34afed02a29c0`, `research/whole-source-20261123/COLLISION_CORE.md`, Sections 3--7 | Actual stationary gap lift and the strict process-dependent collision exponent; no same-limit upper is imported |
| Same PR180/head, `research/whole-source-20261123/BOUNDARY_DESCENT.md`, Sections 2--6 | Pathwise minimum, weighted occupation identity, and the retained source-height cost |
| PR180, `fcdcdbadc6172e414f7282442a8a6b85587d7e70`, `research/source-clock-20261123/EXTENSIONS.md`, (E13)--(E15), retained through the PR178 baseline | Positive lower information dimension under each fixed absolutely continuous path change; source-qualified analytic input |
| PR182, `a7fd3ac9e5bff7412858df23d776bb847e9c1371`, `research/whole-repo-round3-20261123/ACTUAL_COLLISION.md`, Theorem 2 and (15), (20)--(21) | Complete source-box injection and its actual weighted collision consumer |
| Same PR182/head, `research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`, Theorem (1) | The uniform pathwise critical count, used only as supplied in Section 5 |

The existence and analytic properties of the canonical component flow
remain source-qualified. No existence of an escaping ordinary component
is asserted by this conditional construction.

## 2. Explicit regularization on the unchanged ordinary graph

Fix `0<rho<1`. For `k>=1`, put `Delta_k=v_k-v_(k-1)>=0`, and define

\[
C_\rho=v_0+\sum_{k\ge1}\rho^k\Delta_k,
\qquad Z_\rho=C_\rho/C.
\tag{2}
\]

The nonnegative series converges because `sum Delta_k=C-v_0`. In
particular

\[
0<v_0/C\le Z_\rho\le1.
\tag{3}
\]

For a vertex `n` off the forward spine, let `k(n)` be the index of the
first spine vertex reached by its forward path. Define

\[
\boxed{
\begin{aligned}
\nu_\rho(n)&=Z_\rho^{-1}\rho^{k(n)}\nu(n)
&&\text{if }n\notin\{q_j:j\ge0\},\\
\nu_\rho(q_j)&=Z_\rho^{-1}
   \left(v_0+\sum_{k=1}^j\rho^k\Delta_k\right)
&&\text{if }j\ge0.
\end{aligned}}
\tag{4}
\]

**Theorem 1 (positive harmonic regularization).** Formula (4) is a
positive harmonic flow on exactly the same ordinary component. It has
the same spine capacity `C`, and

\[
0<\nu_\rho(n)\le C,
\qquad \nu_\rho(n)\le Z_\rho^{-1}\nu(n).
\tag{5}
\]

**Proof.** A parent of a nonspine vertex is nonspine and has the same
first-attachment index. Its harmonic equation is therefore multiplied
by one common factor. Every parent of `q_0` first attaches at `q_0`,
so its incoming sum is `v_0/Z_rho`.

For `j>=1`, the parents of `q_j` consist of `q_(j-1)` and the off-spine
parents whose first attachment is `q_j`. The latter have total old
flow `Delta_j`. Their new incoming sum is

\[
\nu_\rho(q_{j-1})+Z_\rho^{-1}\rho^j\Delta_j
=\nu_\rho(q_j).
\]

This proves harmonicity. The spine values tend to `C_rho/Z_rho=C`.
Every other vertex flows into the spine, giving the bound by `C`.
Finally the weighted partial sum in (4) is at most `v_j`; the
off-spine upper comparison is immediate. Positivity holds at every
ordinary vertex. No edge or inverse branch is deleted. `QED`.

Write `v_j^rho=nu_rho(q_j)`. The same construction gives the stronger
tail estimate

\[
\boxed{
0\le C-v_j^\rho
=Z_\rho^{-1}\sum_{k>j}\rho^k\Delta_k
\le Z_\rho^{-1}\rho^{j+1}(C-v_j)
\le C Z_\rho^{-1}\rho^{j+1}.}
\tag{6}
\]

This is the rate that was unavailable for the original specified flow.
It is obtained by an explicit new choice, not deduced for that old flow.

## 3. Fixed-root inverse laws and reciprocal floors

Let `K` and `K_rho` be the old and new ratio kernels. Their exact
relationship is

\[
K_\rho(q,n)=K(q,n)\frac{h(n)}{h(q)},
\qquad h(n)=\nu_\rho(n)/\nu(n)>0.
\tag{7}
\]

Harmonicity is precisely `sum_n K(q,n)h(n)=h(q)`. In particular:

1. **Every nonspine inverse kernel is unchanged.** All its parents have
   the same attachment factor. All its earlier inverse vertices do too,
   so its entire infinite inverse path law is unchanged.
2. **The entire inverse law at the original root `q_0` is unchanged.**
   Every ancestor of that root has attachment index zero and is scaled
   by exactly `1/Z_rho`.
3. For each fixed `j>=0`, on the whole inverse cone of `q_j`, including
   that root,

   \[
   Z_\rho^{-1}\rho^j\nu(n)
   \le\nu_\rho(n)\le Z_\rho^{-1}\nu(n).
   \tag{8}
   \]

To verify (8), an off-spine ancestor has attachment index at most `j`.
For a spine ancestor `q_i`, `i<=j`, every coefficient in its weighted
partial sum is at least `rho^i>=rho^j`. Thus every finite inverse
cylinder from `q_j` has likelihood ratio between `rho^j` and
`rho^(-j)`. The whole inverse path probabilities are consequently
equivalent, with these fixed-root bounds.

A supplied reciprocal floor `nu(n)>=gamma/n` therefore survives on
every fixed inverse cone, with a root-dependent constant. It survives
on `Pred(q_0)` with the common factor `1/Z_rho`. A single positive
reciprocal constant on the **entire** component does not follow from
these comparisons and is not asserted. Future spine roots have no
uniform-in-`j` lower comparison in
(8). Any theorem requiring that global uniform floor must retain it as
an additional hypothesis instead of applying it to (4).

## 4. Quantitative agreement at every inverse clock and every quotient

Use the original ordinary empirical law

\[
\pi_N=\frac1N\sum_{j=0}^{N-1}\delta_{q_j},\qquad N\ge1.
\]

Choose arbitrary deterministic finite clocks `r_j>=0` and put

\[
\zeta^\rho_{N,(r_j)}
=\frac1N\sum_{j=0}^{N-1}K_\rho^{r_j}(q_{j+r_j},\cdot).
\tag{9}
\]

The exact retained-spine argument from the baseline, now applied to
the positive flow (4), gives

\[
\|\zeta^\rho_{N,(r_j)}-\pi_N\|_{\rm TV}
=\frac1N\sum_{j<N}\left(1-\frac{v_j^\rho}{v_{j+r_j}^\rho}\right)
\le\frac1N\sum_{j<N}\left(1-\frac{v_j^\rho}{C}\right).
\]

Using (6) and summing the geometric progression proves

\[
\boxed{
\|\zeta^\rho_{N,(r_j)}-\pi_N\|_{\rm TV}
\le \frac{\rho(1-\rho^N)}{Z_\rho(1-\rho)N}
\le\frac{D_\rho}{N},
\qquad D_\rho=\frac{\rho}{Z_\rho(1-\rho)}.}
\tag{10}
\]

For `rho=1/2`, this is at most `1/(Z_rho N)`, with
`1/Z_rho<=C/v_0`. The law is fixed once for this source; it does not
change with `N`, the residue precision, or the selected inverse clocks.

Let `Col_Q(P)` be the sum of squared residue masses modulo an arbitrary
integer `Q>=1`. The baseline root-collision inequality gives

\[
\left|\sqrt{\operatorname{Col}_Q(\zeta^\rho)}
-\sqrt{\operatorname{Col}_Q(\pi_N)}\right|
\le \sqrt2 D_\rho/N.
\tag{11}
\]

The ordinary diagonal of `pi_N` is `1/N`, and grouping atoms into
residues only increases collision, so `Col_Q(pi_N)>=1/N`. Dividing
(11) by its positive square root proves:

**Theorem 2 (uniform relative collision equivalence).** Put
`delta_N=sqrt(2)D_rho/sqrt(N)`. Then, simultaneously for every finite
quotient and all clocks in (9),

\[
\boxed{
(1-\delta_N)_+^2\operatorname{Col}_Q(\pi_N)
\le\operatorname{Col}_Q(\zeta^\rho_{N,(r_j)})
\le(1+\delta_N)^2\operatorname{Col}_Q(\pi_N).}
\tag{12}
\]

The positive part in the lower bound handles small `N`. In particular
the ratio is `1+O_rho(N^(-1/2))` uniformly at **every** chosen precision,
not just at a prescribed relation between `Q` and `N`. The same proof
works for any finite partition of the ordinary state set.

Thus an actual inverse-endpoint collision bound can be transferred
without the earlier unresolved coalescence rate. The construction does
not produce that collision bound. In fact (12) requires the new law's
collisions to track the original ones: choosing this flow is not itself
a smoothing theorem for the original orbit.

## 5. The path-law meaning and the preserved analytic inputs

When the supplied whole-path probability `Pi` is available, let
`tau=min{j>=0:Q_j=q_j}`. Then `Pi(tau<=j)=v_j/C`, and
`Pi(tau=0)=v_0/C`, `Pi(tau=k)=Delta_k/C` for `k>=1`.
Equations (2)--(4) are exactly the fixed bounded change

\[
\boxed{d\Pi_\rho=Z_\rho^{-1}\rho^\tau d\Pi.}
\tag{13}
\]

The density is positive almost surely and bounded above by `1/Z_rho`;
the two path laws are equivalent. On the event of passing through an
off-spine vertex, the future determines its first attachment, so the
density is constant there. On the event of passing through `q_j`, the
joining time ranges from zero through `j`. This verifies every marginal
in (4) and the exact fixed-root assertions of Section 3.

All ordinary states, physical valuations, complete carry identities,
coherent scales, and pointwise path counts are unchanged. The common
real boundary is the same pathwise function. Its fixed-root law at
`q_0` is literally unchanged. At every other fixed root its path law
is unchanged or related by the bounded comparisons above. The pinned
PR180 fixed-AC theorem therefore retains its positive lower information
dimension; the stated almost-everywhere upper local dimension one
also transfers. These remain source-qualified analytic conclusions.
No new canonical-trace identity is inferred from this change of flow.

The pathwise occupation calculation also survives. If every actual
whole path obeys `# {j:Q_j<=X}<=B(X)`, Tonelli gives

\[
\sum_{n\le X}\frac{\nu_\rho(n)}C
=\mathbb E_{\Pi_\rho}\#\{j:Q_j\le X\}\le B(X).
\tag{14}
\]

The new PR182 critical bound may be used for `B`, with its stated
domain. Finite weighted occupation measures at every exponent above
that bound follow by the same nonnegative integration. The old
arithmetic upper estimates for those occupation weights retain their
normalization and their original-source density cost. In particular
the new spine values still approach `C`; their weighted-density ratio
to `pi_N` still contains the actual ordinary factor `q_j^s/N`.

The finite coherent-minimum source construction likewise applies to
the same paths under (13), with new minimum weights. It does not turn
the future of the minimum into a random orbit: that future remains
deterministic and eventually joins the original spine.

## 6. The exact source-box consumer after regularization

This was the direct attempt to use the new rate to close the stationary
gap. Fix `1<=m<N`, and retain endpoints `q_j` for `m<=j<N` with their
literal past windows. Let `A` be the total binary clock of such a window,
`C_w` its complete ordered carry, and `p=q_(j-m)` its original source.
Use PR182's exact boxes

\[
B=\left(A,\left\lfloor C_w/3^m\right\rfloor,
                \left\lfloor p/2^A\right\rfloor\right).
\tag{15}
\]

Within one box the endpoint residue determines the occurrence index.
Let `N_B` count the retained indices in box `B`; `sum_B N_B=N-m`.
Define the effective number of occupied boxes by

\[
\mathcal B_{N,m}
=\left(\sum_B\sqrt{\frac{N_B}{N-m}}\right)^2.
\tag{16}
\]

The original empirical restriction to one box has collision exactly
`N_B/N^2`. The triangle inequality for residue vectors, retaining
all cross-box terms, gives

\[
\sqrt{\operatorname{Col}_{3^m}(\pi_N)}
\le\frac{\sqrt{(N-m)\mathcal B_{N,m}}+m}{N}.
\tag{17}
\]

One may apply the same box decomposition directly to the retained
atoms of (9): their weights are at most `1/N`, their omitted first
`m` labels have mass at most `m/N`, and the entire off-spine remainder
has mass at most `D_rho/N`. Hence the slightly sharper direct consumer
than adding (11) is

\[
\boxed{
\operatorname{Col}_{3^m}(\zeta^\rho_{N,(r_j)})
\le\left(
\frac{\sqrt{(N-m)\mathcal B_{N,m}}+m+D_\rho}{N}
\right)^2.}
\tag{18}
\]

This uses the supplied source-box injection; the new part is the explicit
uniform remainder after choosing (4). No conditional independence of
the boxes is assumed. The square of the sum, not the sum of their
individual collision energies, remains.

At a compatible logarithmic precision `3^(theta m)` comparable to `N`,
a subexponential bound `mathcal B_(N,m)=exp(o(m))` would give the
critical upper with a subexponential loss. Together with PR180's finite
Shannon-deficit branch on the same source subsequence this would be
contradictory. Its geometric-iid equality branch requires its separately
stated time-limit-first order; it is not silently upgraded to a moving
precision theorem here.

No such bound on the actual occupied boxes was obtained. The global
orbit count bounds source positions in a bounded height range, but it
does not bound how many translated source boxes contribute at the late
time labels. Boundary entropy is a law of inverse paths, while those
boxes retain the original deterministic sources. Even after the rate
has been constructed, this is the remaining arithmetic estimate.

## 7. What this resolves and what remains

The new result removes a specific prospective obstruction: **a fast
source comparison can always be arranged by one equivalent positive
ordinary flow**, while keeping the original root's inverse law exact.
It supplies uniform relative collision agreement at arbitrary precision
and arbitrary deterministic label clocks. It leaves an explicit
cross-box term, or a direct original-source collision estimate, to be
controlled.

The higher-rank averaging in PR175 was also tested at its frozen head
`53ba1e1ffc46bf022433c2124a62682ad8dd4739`,
`research/lean-global-closure-20261121/risk24/literature/HIGHER_RANK_BOUNDARY_ATTACK.md`.
Its separate dyadic thickening still changes the averaging and the
compact observable. Formula (12) compares legal ordinary inverse
endpoints with original endpoints; it does not compare those endpoints
with that thickened real-fibre law. No Haar component is transferred
across an unproved identification.

All new assertions in this note are written mathematics. No new Lean
theorem, global reciprocal floor, same-limit collision upper, escape
exclusion, or unrestricted positive-cycle exclusion is claimed.
