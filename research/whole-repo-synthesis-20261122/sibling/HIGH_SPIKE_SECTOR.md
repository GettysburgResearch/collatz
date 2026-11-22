# Finite ordinary anchors for the entire high-spike sector

**22 November 2026. Status: SOURCE-QUALIFIED written deductions;
the direct sibling-current closing attempt remains OPEN.**

The new moving-root trace theorem is uniform along each fixed ordinary
source. **The finite-spine structure is already prior PR185 work**, not
a new discovery here. This note reconstructs its harmonic-flow version
and combines it with the new trace theorem: at any fixed positive
capacity threshold, finitely many actual sources cover the entire target
sector, so the trace becomes uniform across that sector with their
original clocks retained. The attempted next step was to remove those
clocks and transport a substantial stopping-antichain mass to arithmetic
siblings. That step did not succeed.

## 1. Frozen ordinary inputs

The domain \(N\) consists of nonperiodic positive odd ternary units.
Forward transport is killed on entering a periodic vertex. Use the
accelerated map \(U\), the canonical unit obstacle envelope \(V\),
its critical harmonicization \(G\), and the ordinary harmonic flow
\(\nu\). The inputs are

\[
 L\nu=\nu,\qquad
 0<\delta\nu(n)\le G(n)/n\le\nu(n)\le A,
 \tag{1}
\]

and, for every finite reachability antichain \(F\subset N\),

\[
 \sum_{n\in F}\nu(n)\le A.
 \tag{2}
\]

Here \(V\ge G\), and the first inverse contact with
\(C_2=\{n:V(n)\le2\}\) is almost surely finite under the actual
critical Doob law \(\mathbb P_n^G\), at every ordinary root.
The full ordinary inverse law \(\mathbb P_n^\nu\), with kernel

\[
 K_\nu(q,z)=1_{Uz=q}\frac{\nu(z)}{\nu(q)},
\]

is uniformly equivalent to \(\mathbb P_n^G\):

\[
 \delta\mathbb P_n^G\le\mathbb P_n^\nu
      \le\delta^{-1}\mathbb P_n^G.
 \tag{3}
\]

The exact source pins are:

- PR185 `4b0c2c27812db555061f5d9006de82a87e7e364f`,
  [CANONICAL_FINITE_SPINE_CONCENTRATION.md](https://github.com/GettysburgResearch/collatz/blob/4b0c2c27812db555061f5d9006de82a87e7e364f/research/literature-orbit-closure-20261121/CANONICAL_FINITE_SPINE_CONCENTRATION.md),
  Section 5, equation (10): prior global finite-forward-trajectory
  concentration for every positive superlevel of \(V(n)/n\).
  Since \(\nu\le\delta^{-1}V(n)/n\), this already supplies
  finite forward-trajectory coverage for the sector considered here.
- PR185 `53f01ca5b443ef57ef2160b4996dbb2cc87f7395`,
  [ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md](https://github.com/GettysburgResearch/collatz/blob/53f01ca5b443ef57ef2160b4996dbb2cc87f7395/research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md),
  equations (12), (14), (15), (18), and (23)--(24): harmonic comparison,
  antichain bound, and full path-law comparison. The displayed
  Radon--Nikodym derivative there lies in \([\delta,\delta^{-1}]\),
  giving (3).
- PR175 `08fe1388ad63c758680b3695249aca319515c47d`,
  [MOVING_CESARO_FIBRES.md](https://github.com/GettysburgResearch/collatz/blob/08fe1388ad63c758680b3695249aca319515c47d/research/lean-global-closure-20261121/machinery/MOVING_CESARO_FIBRES.md),
  Sections 2--3 and Theorems 1--2: ordinary inverse contact and the
  sourcewise uniform moving traces, with its pinned contact and external
  ordinary-trace dependencies retained.
- PR180 `a9f471543d7fed0a76f348e6d97a9d6d44fa369e`,
  [CRITICAL_BOUNDARY.md](https://github.com/GettysburgResearch/collatz/blob/a9f471543d7fed0a76f348e6d97a9d6d44fa369e/research/central-step-20261122/CRITICAL_BOUNDARY.md),
  Section 6: the actual sibling budget and OPEN-S/OPEN-F.

No new proof of those analytic inputs, uniform ordinary density limit,
or periodic-orbit exclusion is asserted.

## 2. The existing finite-spine structure in harmonic-flow form

For \(\eta>0\), define the actual high-capacity sector

\[
 S_\eta=\{n\in N:\nu(n)\ge\eta\}.
\]

This sector contains every canonical linear spike
\(G(n)\ge\eta n\). Conversely, every point of \(S_\eta\)
satisfies \(G(n)\ge\delta\eta n\).

**Harmonic-flow specialization.** There is an ordinary finite set \(A_\eta\subset
S_\eta\), with \(\#A_\eta\le A/\eta\), such that

\[
 \boxed{
 S_\eta=\bigcup_{p\in A_\eta}
       \{U^kp:k\ge0,\ U^kp\text{ retained}\}.
 }
 \tag{4}
\]

The set \(A_\eta\) consists precisely of the vertices in
\(S_\eta\) with no immediate parent in \(S_\eta\).
In particular, each high vertex has only finitely many high ancestors.
The following contact proof reconstructs this specialization. The prior
fixed-basin sublinearity proof also gives finite high ancestry directly.

**Proof.** Stationarity gives \(\nu(Uz)\ge\nu(z)\) on every
retained edge, so \(S_\eta\) is forward closed until killing.
At any vertex, the number of high immediate parents is at most
\(\nu(q)/\eta\le A/\eta\). Its high inverse tree is therefore
finitely branching.

There is no infinite high inverse ray. Suppose one were
\(x_0,x_1,\ldots\), with \(Ux_{j+1}=x_j\) and all
\(\nu(x_j)\ge\eta\). Its states are distinct: a repetition would
make the root periodic. The probability under \(\mathbb P_{x_0}^\nu\)
of following its first \(r\) edges is exactly

\[
 \frac{\nu(x_r)}{\nu(x_0)}\ge\frac\eta{\nu(x_0)}.
\]

Continuity from above gives a positive probability of following the
whole ray. But a high vertex in \(C_2\) satisfies

\[
 \delta\eta\le G(n)/n\le V(n)/n\le2/n,
 \qquad n\le2/(\delta\eta).
 \tag{5}
\]

Only finitely many distinct states of the ray can satisfy (5). Start
after its last contact. The entire remaining ray still has positive
\(\mathbb P^\nu\)-probability, hence positive
\(\mathbb P^G\)-probability by (3), but never hits \(C_2\).
This contradicts the actual almost sure inverse-contact theorem.

König's lemma now makes each finitely branching high inverse tree
finite. Every high vertex therefore has an ancestral high vertex with
no high parent. Distinct such minimal vertices are incomparable:
otherwise forward monotonicity would supply a high immediate parent
to the later one. They form an antichain. Equation (2) implies that
there are at most \(A/\eta\) of them. Following their actual
forward paths proves (4). \(\square\)

The anchors are actual positive integers, not points of a compact
completion or resampled initial values. Their number is bounded; this
argument supplies no effective height bound or algorithm for finding
them.

## 3. Uniform trace on the whole spike sector

To avoid a normalization collision, write \(h_{\rm tr}\) for
PR175's arithmetic Cesàro trace; it is not \(G(n)/n\). That source
has \(\alpha G\le h_{\rm tr}\le2G\). Let \(D_j=P^j1\),
and keep its measures \(\Phi_j^n\) and
\(\widehat\mu_n^{h_{\rm tr}}\), including their original mass
normalization and the bounded-Lipschitz metric.

For every \(n\in S_\eta\), choose an anchor \(a(n)\in
A_\eta\) and its actual clock \(k(n)\ge0\), so that
\(U^{k(n)}a(n)=n\). Then the sourcewise theorems imply

\[
 \boxed{
 \lim_{R\to\infty}\sup_{n\in S_\eta}
 \frac1R\sum_{r<R}
 \left|\frac{D_{k(n)+r+1}(n)}{h_{\rm tr}(n)}-1\right|=0,
 }
 \tag{6}
\]

and

\[
 \boxed{
 \lim_{R\to\infty}\sup_{n\in S_\eta}
 \frac1R\sum_{r<R}
 d_{\rm BL}\left(\Phi_{k(n)+r+1}^n,
                 \widehat\mu_n^{h_{\rm tr}}\right)=0.
 }
 \tag{7}
\]

Indeed each left side before taking the limit is bounded by the maximum
of the finitely many sourcewise error functions at \(p\in A_\eta\).
Those functions tend to zero individually. The same reasoning gives
one finite dominating contact measure for all these roots: take the
largest of the finitely many constants attached to their anchors.
No moving source or changed weight is introduced.

Equations (6)--(7) apply in particular to **every** ordinary linear
spike \(G(n)\ge\eta n\), rather than only to a previously selected
orbit. They retain the actual anchor clock \(k(n)\). They provide
neither an unshifted precision nor a quantitative convergence rate.

## 4. The attempted passage to sibling transport

The hoped-for completion was to use the common high-sector contact
reference to choose a uniformly adequate stopping antichain, then
transport that whole antichain to the roots \(B^j n\). The ordinary
clock cannot be discarded in doing this. There is an exact obstruction
on the same hypothetical escaping source being tested.

Suppose an escaping tail lies in \(S_\eta\). Its distinct states
eventually exceed \(2/(\delta\eta)\), so by (5) choose a retained
point \(p\) after the last visit to \(C_2\). Write
\(q_k=U^kp\). All of this forward tail avoids \(C_2\). From
\(q_k\), following its actual inverse prefix back to \(p\) has
probability

\[
 \mathbb P_{q_k}^\nu[\text{this prefix}]
   =\frac{\nu(p)}{\nu(q_k)}\ge\frac\eta A.
\]

On this event the inverse contact time \(\tau\) is greater than
\(k\). By (3), for every fixed \(R\) and every \(k\ge R\),

\[
 \boxed{\mathbb P_{q_k}^G(\tau>R)\ge\delta\eta/A.}
 \tag{8}
\]

Thus the finite-anchor theorem and the uniform **centered** estimates
(6)--(7) do not create an unshifted tight stopping policy on that
escaping tail. The surviving event in (8) is the unchanged actual
source prefix, not a constructed countermodel.

Moreover, the sibling roots themselves need not belong to
\(S_\eta\). Along an escaping spine their total relative ordinary
side current is summable. Uniformity on the high sector therefore
cannot be applied to them as though their capacities already had the
lower bound being sought.

The two latest direct attempts were also inspected at their new heads:

- PR175 `08fe1388ad63c758680b3695249aca319515c47d`,
  [ADAPTIVE_SIBLING_AND_HARNACK_ATTEMPT.md](https://github.com/GettysburgResearch/collatz/blob/08fe1388ad63c758680b3695249aca319515c47d/research/lean-global-closure-20261121/machinery/ADAPTIVE_SIBLING_AND_HARNACK_ATTEMPT.md):
  changing inverse words leaves the terminal-height distortion to be
  paid on precisely these stopping trees.
- PR180 `a66a44c9bf058cd7efe1018827ddda9a13297a21`,
  [RENEWAL_TRANSPORT.md](https://github.com/GettysburgResearch/collatz/blob/a66a44c9bf058cd7efe1018827ddda9a13297a21/research/deep-machinery-20261122/RENEWAL_TRANSPORT.md):
  renewal comparison preserves the diagonal source, and full boundary
  quasi-invariance under \(B\) is false. It leaves the restricted
  ordinary high-spike comparison open.

Neither result supplies the missing weighted lower transport to the
low-capacity siblings. No estimate
\(\mathscr L_G(n)\ge c_\eta/\log(2+n)\) was obtained here.

## Outcome

Combining the prior finite-spine structure with the new moving trace
resolves source-finiteness for that trace on the whole fixed-threshold
spike sector, yielding (6)--(7). No priority is claimed for finite-spine
concentration. The next proposed inference, a uniform unshifted stopping
policy feeding the arithmetic sibling transport, fails to follow: the
actual retained prefix has the positive lower mass (8).

These are written source-qualified deductions, not Lean declarations.
They do not prove OPEN-S, OPEN-F, escape exclusion, nontrivial-cycle
exclusion, or the full Collatz conjecture.
