# The actual coalescence clock behind inverse smoothing

Date: 23 November 2026.

**Status: written deductions and an attempted escape contradiction.
The same-orbit collision upper and full Collatz remain OPEN.**

The attack was to combine PR180's new real-boundary regularity with
coupling and merging methods to smooth the original orbit at the critical
ternary precision. The exact calculation identifies the entire distance
from the original time law with a truncated coalescence clock. It gives
the correct scale for a collision comparison. A fixed absolutely continuous
reweighting on the **same ordinary path space** then shows that the
enumerated harmonic, path, and dimension properties alone cannot supply
a rate for that clock.

The last construction changes the harmonic law. It is not a claim that
the distinguished canonical law has the slow rate constructed below,
and it is not a Collatz counterexample. It identifies an additional
property of that canonical construction which a closing proof would
have to use.

## 1. Actual component and exact source qualifications

Use the accelerated map on positive odd integers prime to three,
\[
 U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]
Assume one fixed ordinary source has an escaping orbit
\(q_j=U^j(q_0)\), so its states are distinct. Let \(E\) be its ordinary
coalescence component. Retain the source-qualified positive bounded
harmonic flow
\[
 \nu(q)=\sum_{Un=q}\nu(n),\qquad
 K(q,n)=\mathbf1_{Un=q}\frac{\nu(n)}{\nu(q)},\qquad
 v_j=\nu(q_j)\uparrow C>0.                                      \tag{1}
\]
All states and edges are ordinary and legal.

The supplied whole-path construction has an integer component clock
\(\ell(Un)=\ell(n)+1\), normalized by \(\ell(q_0)=0\), and a probability
\(\Pi\) on two-sided actual paths satisfying
\[
 \Pi(Q_j=n)=\nu(n)/C\quad(\ell(n)=j).                            \tag{2}
\]
Its future is deterministic. The events \(E_j=\{Q_j=q_j\}\) increase,
\(\Pi(E_j)=v_j/C\uparrow1\), and the complete inverse law from \(q_j\)
is \(\Pi(\cdot\mid E_j)\).

| Exact source | Material used |
|---|---|
| PR180, 04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2, research/high-variance-20261123/ANALYTIC_GLUING.md, Sections 1–4 | Actual component law, real coordinate, bounded comparisons of ordinary and critical path laws |
| Same PR/head, research/high-variance-20261123/ENTROPY_RIGIDITY.md, Sections 2–3 | Increasing coalescence events and whole-path conditioning; the already established boundary/time decoupling |
| PR180, fcdcdbadc6172e414f7282442a8a6b85587d7e70, research/source-clock-20261123/BOUNDARY_OVERLAP.md, Sections 4–5 | Arbitrary-reference upper-local-dimension conclusion |
| Same PR/head, research/source-clock-20261123/EXTENSIONS.md, (E13)–(E15) | Positive lower information dimension under every fixed absolutely continuous path reweighting |
| Same PR/head, research/source-clock-20261123/COLLISION_TRANSFER.md | Separate model-law and actual-high-profile cautions; no collision upper imported |
| PR178, 4e204f54136c79cf8c9393b34e3330594f99ae0a, research/global-closure-20261123/escape/PRESSURE_COLLISION_ATTACK.md, Sections 1–4 | The specified inverse-time law, retained atoms, ordinary diagonal, and the preceding maximum-density comparison boundary |

PR185's critical lower bound at 2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d,
research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md, is reused
through the pinned PR178 argument, rather than independently re-audited
here. Its exponent is \(\theta=0.949955527188\ldots\).

The harmonic-flow construction, population estimates, and recent
manuscript inputs remain source-qualified. The new results below are
written deductions from the displayed hypotheses, not Lean declarations.

## 2. Exact variation distance from the unchanged spine

For \(N\ge1\), put
\[
 \eta_N=\frac1N\sum_{j=0}^{N-1}\delta_{q_j},\qquad
 \zeta_{N,r}=\frac1N\sum_{j=0}^{N-1}K^r(q_{j+r},\cdot).          \tag{3}
\]
Here \(N=M+1\) in the preceding notation. Use
\(\|P-Q\|_{\rm TV}=\sup_A|P(A)-Q(A)|\).

**Theorem 1 (exact spine defect).** For every finite \(N,r\),
\[
 \boxed{\|\zeta_{N,r}-\eta_N\|_{\rm TV}
 =\frac1N\sum_{j=0}^{N-1}\left(1-\frac{v_j}{v_{j+r}}\right).}     \tag{4}
\]

**Proof.** A legal inverse cylinder has probability equal to its endpoint
flow divided by its root flow. Injectivity of the original orbit gives
\(U^r(q_i)=q_{i+r}=q_{j+r}\) exactly when \(i=j\). Therefore
\[
 \zeta_{N,r}(\{q_j\})=\frac{v_j}{Nv_{j+r}}\le\frac1N,\quad j<N.
\]
The signed difference \(\eta_N-\zeta_{N,r}\) is nonnegative on the
finite set \(\{q_0,\ldots,q_{N-1}\}\) and nonpositive outside it.
Its positive mass is exactly the right side of (4). \(\square\)

Every summand increases with \(r\), so
\[
 \boxed{\sup_{r\ge0}\|\zeta_{N,r}-\eta_N\|_{\rm TV}
 =\varepsilon_N:=\frac1N\sum_{j=0}^{N-1}
             \left(1-\frac{v_j}{C}\right)\longrightarrow0.}     \tag{5}
\]
Only finite inverse clocks occur in the supremum; its value is their
increasing limit. The convergence is ordinary Cesaro convergence.

Thus for every sequence of finite clocks \(r_N\), the inverse laws and
the unchanged forward empirical laws have the same weak subsequential
limits on the compact ternary space. All bounded residue observations
are controlled by the same variation error, at any chosen precision.
Deepening the inverse clock does not itself supply a new limiting
distribution of the original source.

### The low-profile part has vanishing whole mass

For the supplied trace profile \(F=h_{\rm tr}\), PR180's
COLLISION_TRANSFER, (7)--(8), gives
\(F(q_j)\ge c q_j\), where \(c=\eta\delta v_0>0\) is fixed.
The \(q_j\)'s are distinct positive integers. Hence for every real
\(B\ge0\), at most \(\lfloor B/c\rfloor\) of them can satisfy
\(F(q_j)\le B\). Equation (5) therefore gives
\[
 \sup_{r\ge0}\zeta_{N,r}\{F\le B\}
 \le\frac{\lfloor B/c\rfloor}{N}+\varepsilon_N.             \tag{5a}
\]
In particular, for every nonnegative sequence \(B_N=o(N)\),
\[
 \boxed{\inf_{r\ge0}\zeta_{N,r}\{F>B_N\}\longrightarrow1.} \tag{5b}
\]
The same conclusion holds for the unequal clocks below. This strengthens
the earlier positive retained high-profile fraction to asymptotically
the entire probability, uniformly over inverse clocks. It concerns the
actual endpoint law, not the fixed-root full-path boundary. Thus a
concentration bound restricted to fixed low-profile endpoints controls
an asymptotically vanishing part of this target law. It does not estimate
the collision of the remaining mass.

### Unequal clocks and the early-clock bound

Choose arbitrary deterministic finite clocks \(r_j\ge0\), one for each
original time label, and replace the \(j\)-th term in (3) by
\(K^{r_j}(q_{j+r_j},\cdot)\). The same proof gives (4) with \(r_j\)
in its \(j\)-th summand and the same upper bound \(\varepsilon_N\).
This is clock selection by the original label, not a claim about stopping
rules depending on a sampled inverse path.

If every \(r_j\le R\), monotonicity reduces the defect to the common
clock \(R\). The exact finite telescope
\[
 \sum_{j=0}^{N-1}(v_{j+R}-v_j)
 =\sum_{k=0}^{R-1}(v_{N+k}-v_k)\le R(C-v_0)
\]
then gives
\[
 \boxed{\|\zeta_{N,(r_j)}-\eta_N\|_{\rm TV}
 \le\min\left\{\varepsilon_N,\frac{R(C-v_0)}{Nv_0}\right\}.}      \tag{6}
\]
The constant belongs to the one original source and its supplied flow.
No bound on \(C-v_j\) was assumed.

## 3. The missing rate is a literal coalescence-time moment

Define
\[
 \tau(\omega)=\min\{j\ge0:Q_j(\omega)=q_j\}.                     \tag{7}
\]
This is finite almost surely. It is not asserted to be a stopping time
for the inverse filtration. Since
\(\Pi(\tau>j)=1-v_j/C\), the finite tail-sum identity gives
\[
 \boxed{N\varepsilon_N=\mathbb E_\Pi\min\{\tau,N\}.}             \tag{8}
\]
Finite mean coalescence would give \(\varepsilon_N=O(1/N)\).
Almost-sure finite coalescence supplies only \(o(1)\).

This is the motivation taken from coupling theory. Aldous–Fill's author
manuscript, Chapter 12, Sections 12.1.1–12.1.2, equation (12.3), separates
construction of a faithful coupling from analysis of its coupling time.
Here the actual graph gives the stronger exact formulas (4) and (8).
No finite-state or reversible-chain mixing estimate is imported.

## 4. A collision comparison at the square-root scale

For a probability \(\sigma\) on ordinary integers, put
\[
 \operatorname{Col}_Q(\sigma)
 =\sum_{a\bmod Q}\sigma(a+Q\mathbb Z)^2.
\]

**Theorem 2 (collision stability).** If
\(\|\sigma-\eta\|_{\rm TV}\le d\), then
\[
 \boxed{\left|\sqrt{\operatorname{Col}_Q(\sigma)}
       -\sqrt{\operatorname{Col}_Q(\eta)}\right|
       \le\sqrt2\,d.}                                        \tag{9}
\]

**Proof.** Push both laws to the finite quotient. Their variation
distance can only decrease. The positive and negative parts of the
difference vector each sum to at most \(d\), since the vector sums to
zero. Its squared Euclidean norm is consequently at most \(2d^2\).
Apply the reverse triangle inequality. \(\square\)

In particular,
\[
 \operatorname{Col}_Q(\zeta_{N,r})
 \le\left(\sqrt{\operatorname{Col}_Q(\eta_N)}
                         +\sqrt2\,\varepsilon_N\right)^2,       \tag{10}
\]
and likewise with the two laws exchanged. A sufficient uniform rate
for preserving a bound \(O(Q^{-\theta})\) with asymptotically negligible
root-collision error is
\[
 \varepsilon_N=o(Q^{-\theta/2}).                              \tag{11}
\]
The square root matters; asking for \(o(Q^{-\theta})\) would be
unnecessarily strong. At the largest ordinary-diagonal-compatible
scale \(Q\asymp N^{1/\theta}\), (11) becomes
\[
 \mathbb E\min\{\tau,N\}=o(\sqrt N).                            \tag{12}
\]
For clocks bounded by \(R_N=o(\sqrt N)\), (6) already supplies this
comparison scale. The analogous sufficient error for the weaker target
\(o(\sqrt m\,3^{-\theta m})\) is
\(o(m^{1/4}3^{-\theta m/2})\).

None of these comparisons proves an upper bound for \(\eta_N\).
At \(r=0\), that law is already the exact target. The result identifies
what an inverse smoothing argument must actually control.

## 5. Arbitrarily slow coalescence on the same ordinary component

The next construction preserves the component and original forward
source while changing the path law. Every \(q_k\) has a legal unit
parent other than \(q_{k-1}\); positivity of the flow gives
\(v_k>v_{k-1}\) for \(k\ge1\). Thus the disjoint events
\[
 A_k=E_k\setminus E_{k-1}=\{\tau=k\},\qquad
 a_k=\Pi(A_k)>0
\]
all have positive probability.

**Theorem 3 (one fixed tilt with a prescribed tail).** For any probability
weights \((w_k)_{k\ge1}\), define
\[
 \widetilde\Pi
 =\frac12\Pi+\frac12\sum_{k\ge1}w_k\Pi(\cdot\mid A_k).            \tag{13}
\]
It has the fixed density
\[
 F:=\frac{d\widetilde\Pi}{d\Pi}
 =\frac12+\frac12\sum_{k\ge1}\frac{w_k}{a_k}\mathbf1_{A_k}.       \tag{14}
\]
The events are disjoint, so \(F\) is finite almost surely and has
integral one. It is bounded below by \(1/2\), but need not be bounded
above. The two path laws are mutually absolutely continuous.

Define
\(\widetilde\nu(n)=C\widetilde\Pi(Q_{\ell(n)}=n)\). Then:

1. \(0<\nu(n)/2\le\widetilde\nu(n)\le C\).
2. \(\widetilde\nu(q)=\sum_{Un=q}\widetilde\nu(n)\), and its inverse
   kernel is the actual ratio
   \(\widetilde K(q,n)=\mathbf1_{Un=q}\widetilde\nu(n)/
      \widetilde\nu(q)\).
3. Every path, integer, valuation and physical edge is unchanged.
4. The floor \(\nu(n)\ge\gamma/n\), when supplied, becomes
   \(\widetilde\nu(n)\ge\gamma/(2n)\).
5. Its coalescence tail is exactly
\[
 \boxed{1-\frac{\widetilde\nu(q_j)}C
 =\frac12\left(1-\frac{v_j}C\right)+\frac12\sum_{k>j}w_k.}        \tag{15}
\]

**Proof.** At each fixed level the events \(Q_j=n\) partition the
path space. The event \(Q_j=q\) is the disjoint union of \(Q_{j-1}=n\)
over its actual parents. This gives harmonicity and the inverse ratios.
Longer cylinders telescope because the forward future is deterministic.
The retained half of \(\Pi\) supplies the lower bound. Finally
\(A_k\subset E_j\) holds precisely for \(k\le j\), giving (15).
All pointwise path-count and correction-product bounds are preserved.
\(\square\)

The optional fixed-basin sublinearity is preserved too. Suppose
\[
 \sup\{\nu(n):n\in\operatorname{Pred}(q),\ n\ge H\}\to0
\]
for every fixed nonperiodic target. For any event \(B\) and \(L>0\),
\[
 \widetilde\Pi(B)\le L\Pi(B)+\int_{F>L}F\,d\Pi.
\]
Use \(B=\{Q_{\ell(n)}=n\}\), let \(H\to\infty\) first and then
\(L\to\infty\). This proves the corresponding uniform sublinearity
for \(\widetilde\nu\) in each fixed basin.

### An explicit slow law

Choose
\[
 w_k=\log2\left(\frac1{\log(k+1)}-\frac1{\log(k+2)}\right),
 \qquad k\ge1.
\]
These weights are positive and sum to one, with
\(\sum_{k>j}w_k=\log2/\log(j+2)\). Formulas (5), (8), and (15) give
\[
 \boxed{\sup_{r\ge0}
 \|\widetilde\zeta_{N,r}-\eta_N\|_{\rm TV}
 \ge\frac{\log2}{2\log(N+1)}.}                                 \tag{16}
\]
For each \(N\), a sufficiently large finite inverse clock achieves at
least half this lower bound. More generally, any decreasing probability
tail tending to zero can be substituted to prescribe an arbitrarily
slow contribution with one fixed law.

Equation (16) does not claim that the original canonical law has this
rate. It also does not give a lower bound for the difference between
the collision probabilities. It shows that the uniform rate needed by
the specific comparison (11) cannot follow from properties preserved
by (13).

## 6. PR180's new real-boundary regularity survives the test

The common real coordinate \(Z\) is a pathwise object on this same
graph, and is unchanged by (13). The new real marginal is mutually
absolutely continuous with the old one and remains nonatomic.

More specifically, apply PR180 BOUNDARY_OVERLAP (21) with the new real
marginal as its fixed reference. Condition at a clock-zero ordinary
root and use the supplied equivalence of its ordinary and trace path
laws. The arbitrary-reference statement gives upper local dimension
at least one at the new sampled boundary almost surely. The universal
upper bound for real probability measures gives equality.

The positive lower Shannon information dimension follows directly from
PR180 EXTENSIONS (E13)–(E15): those statements allow every fixed
absolutely continuous reweighting of the path law, with an integrable
unbounded density. Formula (14) is exactly such a density. The same
positive coefficient \(d_B\) remains available, subject to the original
source qualifications.

Thus the combination of positive bounded harmonic flow, the original
ordinary paths, the pointwise product bounds, fixed-basin sublinearity,
upper local dimension one, and the positive information-dimension bound
does not force the uniform coalescence rate (12). A theorem using only
those properties must also apply to the slow law (13).

This is not a claim that every defining identity of the distinguished
canonical trace has been preserved as a new canonical construction.
The changed law is identified throughout. A proof of a rate for the
distinguished law must use a feature not invariant under this tilt,
or bypass the variation comparison and control the actual residue pairs.

## 7. The attempted closing step and what remains

The literature-inspired attempt had three stages: construct a faithful
coupling, obtain its rate from the actual boundary theory, and transfer
it at the critical residue scale. The first and third have exact
formulas, (4), (8), and (9). The second is not supplied by the enumerated
properties, as the same-component construction demonstrates.

PR182 at b78819e95ee7d39f02022de991b42217821e7590,
research/closure-round2-20261123/SOURCE_CLOSURE.md, Sections 2–4,
was also inspected. Its single ordinary pressure maximum obeys every
forward coefficient inequality \(3^h/2^A>1\) and every incoming
coefficient inequality \(3^h/2^A<1\). These restrict actual paths and
survive a change of law on those paths. They do not specify a
coalescence-time tail. The companion ESCAPE_CLOSURE.md retains the
pressure residual in its exact loss summation and does not supply
the missing rate here.

The first unsupported inference would be quantitative control of
\(\mathbb E\min\{\tau,N\}\) for the distinguished law, or a direct
bound on the original source's residue pairs strong enough to oppose
the critical collision lower bound. Neither was proved. No closing
hypothesis is added as an axiom, and no numerical census is offered
as evidence for it.

## Primary literature consulted

David Aldous and James Allen Fill, *Reversible Markov Chains and Random
Walks on Graphs*, author manuscript, Chapter 12, Sections 12.1.1–12.1.2,
especially (12.3):

<https://www.stat.berkeley.edu/users/aldous/RWG/Book_Ralph/Ch12.S1.html>.

The coupling inequality and method discussion were read directly.
The proofs in this note are self-contained and do not import the
finite-state or reversibility assumptions of the surrounding examples.
The broader representation alternatives were checked against PR186,
1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493,
literature/deep-machinery-20261122/05_rigidity_and_long_shots.md.
No independent-base invariance or stationary-law hypothesis was added.
