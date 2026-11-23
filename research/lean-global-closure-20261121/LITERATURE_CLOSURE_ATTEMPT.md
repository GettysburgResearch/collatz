# Literature continuation: global potential control and a typed induction

**Status: Collatz remains OPEN.** This continuation pursued the full closing
step after the core Lean checkpoint. Its strongest new analytic result is
a weighted upper bound over **all nonperiodic odd unit targets**, conditional
on the explicitly pinned population and canonical-potential inputs below.
Its strongest constructive result is a uniform interval continuation and
fusion rule. Neither result supplies the remaining universal conclusion.

The new mathematics in this continuation is written and independently
reviewed where indicated. It is not included in the 16-unit Lean count.

## 1. New repository inputs during this pass

The starting inventory recorded 143 PRs. A live refresh then found new
commits and a new PR. The following heads were frozen for targeted source
inspection; the earlier compiled dependency copies were left unchanged.

| Source | Frozen head | Relevant input |
|---|---|---|
| PR177 | `a0a0d76f91b4e3846c1b1f0706cad56cb6098317` | Cofinal certified predecessors over gaps 1--4; high-gap/even-run interval reduction; low-interval refinements. |
| PR180 | `d0349de2108abb7c8fb8393c086610e3372df116` | Uniform natural predecessor density, canonical least excessive majorant, fixed-basin sublinearity, and subcritical bounds. |
| PR183 | `907a540943090968bc683b1b9246208e9053c1f8` | One matrix rank for ordinary mixed-base normalization and blocked erasure; general erasure merger remains a premise. |
| PR185 | `6d2765ef462fb575c49d4133b54286be7ffe68ec` | Ordinary source-fiber transport and a quantitative resolvent saving target; no universal saving is supplied. |

The [refresh record](../../reports/lean-global-closure-20261121/wide/live-refresh.json)
keeps the observation boundaries. The detailed notes give inspected paths,
exact statements, and source qualifications. This is not a blanket replay
of every branch's compiler receipts.

## 2. A new global weighted estimate for the canonical potential

Use the accelerated odd map `U` and the actual inverse operator

\[
(Pf)(q)=\sum_{\substack{a\ge1\\2^a q\equiv1\pmod3}}
 \frac3{2^a}f\!\left(\frac{2^a q-1}{3}\right).
\]

Let `g` be the unit indicator and let
`V_0=g`, `V_(j+1)=max(g,PV_j)`, `V=sup_j V_j` be the finite canonical
least excessive majorant described in the pinned PR180 input. Set
`H(n)=V(n)/n`.

The population input is kept explicit: for some absolute `c,C>0`, every
positive odd ternary-unit target `a` has at least `cX/a` odd unit ordinary
predecessors up to `X`, whenever `X>=Ca`. This is the written PDU theorem
claimed and reviewed in PR180, not a new Lean axiom or a numerical estimate
for `c`.

On the set `N` of positive odd ternary units which are **not themselves on
a cycle**, the new deduction proves, for every `X>=1`,

\[
\boxed{\sum_{\substack{n\in N\\n\le X}}\frac{V(n)}n
 \le \frac{4X^{39/40}+\lfloor(3/5)\log_2X\rfloor}{c}
 \le\frac5c X^{39/40}.}
\]

Nonperiodic here includes convergent preperiods; it does not mean that an
orbit diverges. No cycle classification is assumed. For every `p>=1` and
`s>39/40`, the corresponding global moment estimate is

\[
\boxed{\sum_{n\in N}\frac{(V(n)/n)^p}{n^s}
 \le\frac{5s}{c^p(s-39/40)}.}
\]

In particular,

\[
\sum_{n\in N}\frac{V(n)}{n^2}\le\frac{200}{c},
\qquad
\sum_{n\in N}\frac{V(n)^2}{n^3}\le\frac{200}{c^2}.
\]

The same upper bounds hold for the pinned harmonic minorant `G<=V`.

### Why this controls all targets in the displayed domain

Unfold the actual inverse tree at a nonperiodic root. The value `V(q)` is
the supremum of finite stopping-cutset weights. Each cutset leaf is a
positive ordinary source `m`, and its actual Jacobian weight is at most
`q/m`. Distinct prefix-free leaves have disjoint entire predecessor basins:
determinism would otherwise make their inverse words comparable.

The uniform population lower bound therefore gives
`lower_density(Pred(q)) >= c*H(q)`. If a finite family of roots is an
antichain under forward reachability, its predecessor basins are disjoint
too, so

\[
\sum_{q\text{ in an antichain}} H(q)\le1/c.
\]

Now order the nonperiodic targets up to `X` by reachability and assign to
each the length of a longest chain ending there. Equal-rank sets are
antichains. The resident orbit-cylinder proof bounds each chain's length
by `4X^(39/40)+O(log X)`; the logarithmic term covers the final preperiod
states which could otherwise merge in a cycle. Summing the antichain
budget over the rank layers gives the weighted estimate directly. This
avoids the logarithmic loss of a superlevel-only layer-cake argument.

The full proof, including the selected-depth injectivity and all constants,
is in [CANONICAL_POTENTIAL_SUPERLEVELS.md](CANONICAL_POTENTIAL_SUPERLEVELS.md).
Its [separate review](../../reports/lean-global-closure-20261121/wide/CANONICAL_POTENTIAL_REVIEW.md)
is recorded at the exact source hash. The population
and finite-envelope hypotheses remain part of its evidence boundary.

### The full-theorem step still needed

The estimate permits a sparse escaping forward trajectory on which `H`
stays positive, while `H` decays through that trajectory's many incoming
predecessors. It consequently does not prove uniform marked sublinearity.

The resident finite-five-energy rigidity criterion instead concerns an
orbit-invariant component label `f` and the multiplicative defect

\[
\sum_{\substack{n>0\\n\text{ odd},\ 3\nmid n}}
 \frac{d(f(5n),f(n))}{n}.
\]

`H` is not such a label. A complete application would need an actual
transfer or charging inequality from those label defects to the new
finite potential moments, preserving original source weights and
controlling incoming multiplicity. This pass did not obtain that
inequality. Periodic targets are also outside the displayed moment domain.

### An exact transform preserves each original source atom

The same finite-chain count gives a uniform correction bound on every
actual odd path ending at a nonperiodic target:

\[
\kappa\le\prod_{i<k}\frac{3n_i}{3n_i+1}\le1,
\qquad\kappa=\exp(-200/3).
\]

This path bound does not need PDU. Given the source-qualified positive
harmonic `G`, set `h=G/n` and define the actual inverse Doob kernel
`K(q,n)=1_(U(n)=q)*[3n/(3n+1)]*h(n)/h(q)` on odd units. For any finite
original source mass `a`, its true depth-`k` fiber mass `b_k(q)` satisfies

\[
h(q)K^k(a/h)(q)\le b_k(q)
 \le\kappa^{-1}h(q)K^k(a/h)(q)
\]

at every nonperiodic endpoint. This holds uniformly in the depth and the
moving endpoint. The new global moment supplies the concrete finite seed
`a(n)=G(n)/n^2` on nonperiodic units, giving the observable `a/h=1/n`.

Decay of the resulting expectation is established for each fixed root;
the moving-root supremum needed to exclude escape is still unproved.
A separate exact argument shows that no nonzero finite positive mixture
of the stated Abel approximants is an excessive function for the
undiscounted operator on all ordinary odd unit targets. It uses the
actual inverse chains above `2*3^k-1` and retains their positivity.

[LITERATURE_TRANSPORT_ATTEMPT.md](LITERATURE_TRANSPORT_ATTEMPT.md) gives
the full identities, source hypotheses, mixture proof, and a direct test
showing why a forward supremum cannot transfer the new finite moment to
component-label energy. These deductions preserve the fixed source; they
do not assume the remaining uniform transport estimate.

## 3. Termination theory suggests keeping pending calls typed

Yolcu--Aaronson--Heule study Collatz through mixed-base rewriting and
relative termination. Their result for every one-rule deletion does not
prove relative termination of the deleted rule against the full system.
That distinction motivated a direct attempt to keep recursively produced
certificates as unevaluated, typed requests.

Write `O_a(C)` for an actual odd certificate with first gap `a`, and
`F_e(C)` for the pending psi target of its powered source. The exact
infinite schemas are

\[
F_e(O_a(C))\longrightarrow
 O_1(F_{e-1}(F_{a-1}(C)))\quad(e,a\ge1),
\]

\[
F_0(O_a(C))\longrightarrow O_2(F_{a-2}(C))\quad(a\ge2).
\]

A token multiset, together with a commuting-rule inversion count, orients
these schemas before evaluation. The larger interval request `I_e(C)`
also admits the exact continuation fusion

\[
I_e(F_d(C))\quad\Leftarrow\quad I_{e+d+1}(C).
\]

It follows from the inequality between their actual interval ceilings;
it does not extract and reuse an uncontrolled output certificate. Combined
with the actual source step, it gives the uniform macro

\[
I_e(O_a(C))\longrightarrow I_{e+a-1}(C),
\]

which reduces the complete source clock by exactly one. The retained even
exponent can nevertheless increase. At the empty source tail it leaves
an unbounded power-of-two interval, so the terminal case still contains
the full convergence problem. The terminal reset and this clock decrease
have not been combined into one well-founded order.

[PROVENANCE_TERMINATION_ATTEMPT.md](PROVENANCE_TERMINATION_ATTEMPT.md)
records the typed semantics, rank calculations, predecessor branch,
terminal outputs, even-run fusion, and the exact remaining condition.
The older
[NONTERMINAL_DISPATCH_ATTEMPT.md](NONTERMINAL_DISPATCH_ATTEMPT.md)
keeps the underlying ordinary offset identities.

## 4. Semigroup membership must be realized by ordinary paths

Applegate--Lagarias prove a complete multiplicative semigroup theorem.
Their modified process can multiply a state by a suitable wild integer
before further Collatz steps. We tried to replace those multiplications
by actual ordinary merger paths while preserving PR183's word rank.

The resulting written proposition covers every bounded repair scheme:
if a fixed integer multiplier `m` has a prime factor other than 2 or 3,
then for fixed clocks `H,K` at most
`(2^(H+1)-1)(2^(K+1)-1)` positive sources can satisfy
`T^h(x)=T^t(m*x)` with `h<=H,t<=K`. Fixed parity words give affine
formulas; two different sources for the same word pair would force an
impossible equality of slopes. A successful physical repair must therefore
be unbounded and depend on the actual source.

This limits the proposed multiplier repair, not arbitrary mergers or
Collatz proofs. The full proof and the attempted ancestor/divisibility
repair are in [LITERATURE_MERGER_ATTEMPT.md](LITERATURE_MERGER_ATTEMPT.md).
[LATE_MERGER_REFRESH.md](LATE_MERGER_REFRESH.md) identifies exactly what
the newest PR183 normalization and erasure theorems supply.

## Primary literature consulted

- E. Yolcu, S. Aaronson, M. J. H. Heule, *An Automated Approach to the
  Collatz Conjecture*, Journal of Automated Reasoning 67 (2023), article 15;
  [arXiv:2105.14697v3](https://arxiv.org/html/2105.14697v3), especially
  Theorems 2.6 and 2.15, Lemma 3.18, and Section 4.3.
- D. Applegate, J. C. Lagarias, *The 3x+1 Semigroup*, Journal of Number
  Theory 117 (2006), 146--159;
  [arXiv:math/0411140v2](https://arxiv.org/pdf/math/0411140), especially
  Theorem 1.1 and Section 2.
- I. Assani, *Collatz map as a non-singular transformation*, Studia
  Mathematica 275 (2024), 249--261;
  [arXiv:2208.11675v3](https://arxiv.org/pdf/2208.11675), Theorem 1.2.
  Its finite full-support power-boundedness criterion motivates preserving
  original source atoms; endpointwise Green finiteness alone is weaker.

No external theorem or proposed repository completion is imported as a
Lean axiom. The separately
[recorded fresh build](../../reports/lean-global-closure-20261121/wide/VALIDATION.md)
checks the earlier core Lean packet. The new written estimates above have
their stated analytic hypotheses and exact remaining implications.
