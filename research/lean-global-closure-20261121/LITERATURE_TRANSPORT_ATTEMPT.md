# Critical transport: an exact Doob comparison and an Abel-mixture obstruction

**Status: written deductions, not new Lean formalizations. Full Collatz
remains unproved.** This note connects the canonical inverse potential
to the actual original-source transport. It also tests, and rules out,
a positive-mixture shortcut for removing the Abel discount.

## 1. Literature motivation and pinned inputs

Assani's finite-measure approach suggests preserving a positive atom for
every ordinary source, and controlling its transport by the actual map.
Theorem 1.2 of [Assani, arXiv:2208.11675v3](https://arxiv.org/html/2208.11675v3)
states the full-support power-bounded formulation with conservative part
\(\{1,2\}\). The elementary atomic implication is the part relevant
here; this note does not use that paper's separate counting-measure
claims. PR185 develops this direction into explicit source fibers at
`6d2765ef462fb575c49d4133b54286be7ffe68ec`,
`research/literature-orbit-closure-20261121/HARMONIC_TRANSPORT.md`.

For the inverse potential use PR180
`d0349de2108abb7c8fb8393c086610e3372df116`:

* `GLOBAL_RENEWAL_ATTACK.md`, under
  `research/lean-forward-band-20261121/`, supplies the uniform ordinary
  unit-predecessor density (PDU), the operator \(P\), and finite Abel
  approximants.
* `MINIMAL_ENVELOPE_ATOM_REMOVAL.md` supplies the finite canonical least
  excessive majorant \(V\) and its harmonic part \(G\), with
  \(PG=G\), \(0<G\le V\) on units, and an absolute floor
  \(G(n)\ge\gamma>0\) there. At multiples of three \(G=0\).
* `ABEL_MARKED_UPPER_ATTACK.md` proves the global sublinear bounds for
  each fixed discounted approximant and records its exact defect.

These are source-qualified written analytic inputs. They are not
silently introduced as Lean axioms. The new
`CANONICAL_POTENTIAL_SUPERLEVELS.md` proves, from those inputs and the
pinned ordinary orbit-cylinder count, the global moment bound

\[
\sum_{\substack{n>0\text{ odd unit}\\n\text{ nonperiodic}}}
                      \frac{G(n)}{n^2}\le\frac{200}{c},
\tag{1}
\]

where \(c\) is the (PDU) constant. The orbit-cylinder source is
`research/astra-three-routes/pass2/ORBIT_MELLIN.md`, Section 1, at
`2055b8a311ab87d07bffc730154a7f8546fe382c`, blob
`16c943601ce791afb1bbd5f02f3a9ea88ef38520`.

Throughout, \(U\) is the accelerated odd map. A *nonperiodic endpoint*
is an ordinary odd integer not itself on a cycle; it is allowed to
enter a cycle later. This restriction is essential in the uniform
source-transport comparison below.

## 2. An explicit, depth-independent correction on every nonperiodic path

Put

\[
                         \lambda(n)=\frac{3n}{3n+1}.
\]

If \(n_0,n_1,\ldots,n_k=q\) is an actual odd path ending at a
nonperiodic endpoint, all its states are distinct and nonperiodic.
Section 4 of `CANONICAL_POTENTIAL_SUPERLEVELS.md` gives, for any finite
chain of such states,

\[
\#\{n_i\le X:0\le i<k\}
 \le4X^{39/40}+\left\lfloor\frac35\log_2X\right\rfloor
 \le5X^{39/40}.
\]

Nonnegative Mellin integration therefore yields

\[
\sum_{i<k}\frac1{n_i}
 \le\int_1^\infty 5t^{39/40}t^{-2}\,dt=200.
\tag{2}
\]

This uses neither a bound on the largest intermediate value nor the
predecessor-density theorem. The latter is needed for (1), not for (2).
Consequently the actual multiplicative correction

\[
\Lambda_k(n_0)=\prod_{i<k}\lambda(n_i)
\]

obeys the explicit uniform bound

\[
\boxed{\kappa\le\Lambda_k(n_0)\le1,
                  \qquad\kappa=\exp(-200/3)>0.}
\tag{3}
\]

Indeed \(\log(1+x)\le x\) gives
\(-\log\Lambda_k\le\tfrac13\sum_{i<k}1/n_i\).
If all states are at least \(m\), the same argument improves the
exponent to \(-(200/3)m^{-1/40}\).

## 3. The Doob transform retains the original source mass

Let \(\mathcal U\) be the positive odd ternary units and set
\(h(n)=G(n)/n\) there. For an actual inverse edge
\(U(n)=q\), write \(3n+1=2^e q\). The exact identity

\[
\frac{(3/2^e)G(n)}{G(q)}
 =\frac{\lambda(n)h(n)}{h(q)}
\]

defines an inverse transition kernel

\[
K(q,n)=\mathbf1_{U(n)=q}
                   \frac{\lambda(n)h(n)}{h(q)},
                         \qquad q,n\in\mathcal U.
\tag{4}
\]

Harmonicity \(PG=G\), positivity of \(G(q)\), and its zero values
at nonunits give \(\sum_{n\in\mathcal U}K(q,n)=1\). Thus \(K\)
is an actual countable-state Markov kernel, oriented from a target to
its ordinary odd predecessors.

Let \(a\ge0\) be any finite original source mass on \(\mathcal U\),
and retain its true depth-\(k\) fibers

\[
b_k(q)=\sum_{\substack{n\in\mathcal U\\U^k(n)=q}}a(n).
\]

Telescoping the \(h\)-factors on each actual inverse path gives the
exact identity

\[
\boxed{h(q)\,K^k(a/h)(q)
 =\sum_{U^k(n)=q}\Lambda_k(n)a(n).}
\tag{5}
\]

All terms are nonnegative. In particular the observable is the original
\(a(n)/h(n)\), not a newly sampled endpoint weight. At a nonperiodic
endpoint every path in (5) satisfies (3). Therefore

\[
\boxed{
h(q)K^k(a/h)(q)\le b_k(q)
       \le\kappa^{-1}h(q)K^k(a/h)(q).}
\tag{6}
\]

This comparison is uniform in both the depth and the nonperiodic moving
endpoint. In particular a specified original source \(x\) with
\(U^k(x)=q\) contributes at least \(\kappa a(x)\) to the left
side of (5). A change of measure has not erased its positive atom.

### A concrete finite seed supplied by the new global moment

Let \(\mathcal N\subset\mathcal U\) be the nonperiodic states and
choose

\[
a(n)=\mathbf1_{n\in\mathcal N}\frac{G(n)}{n^2}
     =\mathbf1_{n\in\mathcal N}\frac{h(n)}n.
\tag{7}
\]

Equation (1) makes this a finite mass, positive at every nonperiodic
unit state. At a nonperiodic endpoint every inverse ancestor is again
nonperiodic, so (5) specializes to

\[
h(q)K^k(1/n)(q)=\sum_{U^k(n)=q}\Lambda_k(n)\frac{G(n)}{n^2}.
\tag{8}
\]

This converts the global moment into a source-retaining probability
representation with the explicit observable \(1/n\).

For each fixed nonperiodic \(q\), the expectation
\(K^k(1/n)(q)\) tends to zero. For any finite source bound \(M\),
each of the finitely many sources \(n\le M\) can hit that fixed
nonperiodic target at only one depth. Beyond their finitely many possible
depths, every inverse source is larger than \(M\), giving the bound
\(K^k(1/n)(q)\le1/M\).

The missing global estimate is a decay assertion that retains a moving
root, for example

\[
\sup_{q\in\mathcal N}h(q)K^k(1/n)(q)\longrightarrow0.
\tag{9}
\]

A source with an escaping odd orbit would contradict (9) by (6)--(8).
The fixed-root argument does not prove (9). Nor do the superlevel moment
bounds: a sparse forward trajectory can carry the persistent atom.

At a periodic endpoint, the correction product can contain arbitrarily
many cycle laps and tends to zero along those repetitions. Bound (3)
then fails. Thus (6) is not a cycle-exclusion claim. A clock lift cannot
restore (3), because it separates clock states while repeating the same
ordinary integers in the reciprocal sum.

### A fixed-endpoint Green sum is not total occupation

For nonperiodic \(q\), a source can hit \(q\) at only one depth, so
positive summation of (5) gives

\[
\sum_{k\ge0}h(q)K^k(a/h)(q)
 =\sum_{n\to q}\Lambda_{n\to q}a(n)
 \le\sum_na(n)<\infty.
\tag{10}
\]

This is a uniform bound for each fixed endpoint. Summing (10) over all
endpoints is a different operation: one escaping source visits infinitely
many distinct endpoints and retains at least \(\kappa a(n)\) at each.
It would make that total occupation infinite. No finite total occupation
is inferred from the pointwise Green bound.

## 4. Positive mixtures cannot remove the Abel discount

Use \(D_s=P^s1\), \(D_0=1\), and the source-pinned approximants

\[
F_\rho(q)=(1-\rho)\sum_{s\ge0}\rho^sD_s(q),
                             \qquad0<\rho<1.
\]

Their exact resolvent identity gives

\[
PF_\rho-F_\rho
              =\frac{1-\rho}{\rho}(F_\rho-1).
\tag{11}
\]

Consider a nonzero finite positive measure \(\nu\) on \((0,1)\)
and the candidate \(M_\nu(q)=\int F_\rho(q)\,d\nu(\rho)\).
Assume it is finite where an excessive majorant is intended. If
\(PM_\nu\) is infinite somewhere, it already fails excessivity.
Otherwise Tonelli and (11) give

\[
PM_\nu(q)-M_\nu(q)
 =\int\frac{1-\rho}{\rho}(F_\rho(q)-1)\,d\nu(\rho).
\tag{12}
\]

The explicit **odd unit** targets

\[
                         q_k=2\cdot3^k-1,\qquad k\ge1,
\]

have the legal inverse \(e=1\) chain

\[
m_j=2^{j+1}3^{k-j}-1,\qquad 0\le j\le k.
\]

Every \(m_j\) is positive odd, and it is a ternary unit for \(j<k\).
Consequently, using only depths \(0\le s\le k-1\),

\[
D_s(q_k)\ge(3/2)^s,\qquad
F_\rho(q_k)\ge(1-\rho)
                         \sum_{s=0}^{k-1}(3\rho/2)^s.
\tag{13}
\]

For \(0<\rho<2/3\), this implies

\[
\liminf_{k\to\infty}
\frac{1-\rho}{\rho}(F_\rho(q_k)-1)
\ge\frac{1-\rho}{2(1-3\rho/2)}\ge\frac12.
\tag{14}
\]

For \(2/3\le\rho<1\), the lower limit is infinite. Also
\(F_\rho(q)\ge1-\rho\), so the integrand in (12) is always at
least \(-(1-\rho)\ge-1\). Add one and apply Fatou against the finite
positive measure \(\nu\). Equations (12)--(14) prove

\[
\boxed{\liminf_{k\to\infty}
       (PM_\nu(q_k)-M_\nu(q_k))
          \ge\tfrac12\nu((0,1))>0.}
\tag{15}
\]

Thus no such nonzero positive mixture is excessive for the
undiscounted operator on all positive ordinary odd unit targets. This
includes finite positive mixtures. It does not rule out a signed
cancellation or a state-dependent correction, but either would need
its own positivity, transfer, and growth proof.

## 5. The remaining transfer to invariant-label energy

The new finite moments concern \(h=G/n\), which is not a
Collatz-invariant label. Taking its forward supremum does not preserve
the harmonic moment. For example, extend \(h\) by zero on periodic
states and use the known nonperiodic unit target 5. Every unit source
that eventually hits 5 has forward supremum at least \(h(5)>0\).
(PDU) makes that source set have positive lower natural density, so its
harmonic mass is infinite. This already occurs in a known convergent
basin and is not a counterexample to Collatz.

Likewise, for a Boolean component label \(f\), the harmonic numerator
\(G_f=fG\) has the same positive moment bounds on the nonperiodic
domain. Recovering \(f=G_f/G\), however, only has the floor
\(G\ge\gamma\). At a five-defect source one can bound

\[
\frac{|f(5n)-f(n)|}{n}
 \le\gamma^{-1}\left(\frac{G_f(n)}n+
                              5\frac{G_f(5n)}{5n}\right),
\]

which requires an *unweighted* sum of the normalized numerator on the
right. The proved moment is weighted by another factor \(1/n\).
Dropping that factor is not licensed by the superlevel theorem.

A genuine charging inequality from the ordinary five-defect boundary
to the finite potential moment, or a proof of the moving-root bound
(9) with cycle exclusion handled separately, would be a new closing
step. Neither has been established in this attempt.
