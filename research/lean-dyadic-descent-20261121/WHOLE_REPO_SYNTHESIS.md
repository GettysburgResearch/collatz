# Whole-repository reassessment and the next checked attacks

**Full Collatz remains open.** The broader pass changes the immediate work
from adding another selected band family to connecting the repository's
complete-certificate, ordinary-counting, and source-preserving analytic
programs. It produces two new finite Lean developments, a written
periodic-approximation rigidity argument, and a separate adversarial audit
of the strongest new analytic input.

## Scope of the reassessment

[WHOLE_REPO_INVENTORY.json](WHOLE_REPO_INVENTORY.json) records all **145 pull
requests** returned by GitHub's two all-state pages, through PR186, with
their exact heads, bases, titles and update times. This is a complete
metadata inventory at that observation, not a claim that every line of
every branch received a fresh mathematical review.

The integrated baseline was read at main
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, including the cumulative
[results catalog](../RESULTS_CATALOG.md), [research map](../../docs/RESEARCH_MAP.md),
[resident proofs](../integrated/README.md), [errata](../integrated/ERRATA.md),
and [open obligations](../open-obligations/README.md). The three parallel
source-level tracks then examined certificate/rank composition; population,
renewal and invariant-component arguments; and coefficient stopping,
ordinary extraction, cycle algebra and symbolic rigidity. Exact source
claims below retain their prior review scope. Merely appearing in this
table does not promote an exploratory branch to an accepted global proof.

The [new literature field guide, PR186](https://github.com/GettysburgResearch/collatz/blob/1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493/literature/deep-machinery-20261122/README.md)
was discovered during the inventory. Its T01 population audit and T10
compositional certificate task closely match two of the concrete
developments below. Its proposed quantitative consequences remain
source-qualified; they are not imported as Lean facts.

## 1. What can actually be connected

| Program and exact source | What is available | What a full closing argument still needs |
|---|---|---|
| [Forced ordinary band, PR173](https://github.com/GettysburgResearch/collatz/blob/fa0c9e2a2851e6324391e39c17afcb5913185aec/research/lean-shell-cover/ForwardSection.lean) | Every positive ordinary orbit enters the marked dyadic band; the positive return map is total. | Eventual strict return descent for every marked source, or another universal closing mechanism. |
| [Return obstructions, PR175](https://github.com/GettysburgResearch/collatz/tree/2055b8a311ab87d07bffc730154a7f8546fe382c) and the previous PR182 checkpoint | Actual expanding returns, equal-feature collisions, selected contracting blocks, and a first-hit offset larger than its original source. | A comparison with the original induction source, with all guards preserved. Size, binary exponent and trailing-one depth alone do not supply the missing every-return rank. |
| [Complete-certificate rank, PR177](https://github.com/GettysburgResearch/collatz/tree/a0a0d76f91b4e3846c1b1f0706cad56cb6098317) | One common highest-multiplicity rank reduces the remaining supplied certificate language to initial even runs 1--3 and odd gaps at most four. | Successful rules for every residual source/target query; a finite alphabet still permits arbitrary word length. |
| [Marked prefixes, PR178](https://github.com/GettysburgResearch/collatz/blob/e5de8da89b3aab3cae98db3157977165f4467e3e/research/reframe-20261121/README.md) and [physical erasure, PR185](https://github.com/GettysburgResearch/collatz/blob/6d2765ef462fb575c49d4133b54286be7ffe68ec/research/literature-orbit-closure-20261121/README.md) | Suitable binary prefixes remain marked. Exact endpoint diamonds give actual smaller marked common-future sources on unbounded guarded classes, including some with no native-horizon descent. | An exhaustive physical partner selection. A smaller binary prefix is a candidate until its common future is established. |
| [Coefficient and first-crossing programs](../integrated/coefficient-stopping/README.md), [PR92 orbit-Mellin](https://github.com/GettysburgResearch/collatz/blob/7bb6d36d3bc37dd09b52aa9a23c8e33973032359/research/astra-three-routes/pass2/ORBIT_MELLIN.md) | Exact affine corrections, supercritical-tail reductions and stronger qualitative coefficient escape on nonperiodic ordinary paths. | Exclusion of the all-supercritical alternative and the full first-crossing displacement obstruction. Coefficient contraction alone need not be ordinary descent. |
| [Uniform predecessor populations, PR180](https://github.com/GettysburgResearch/collatz/blob/d0349de2108abb7c8fb8393c086610e3372df116/research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md) | A written joint-clock derivation of a uniform lower bound `cX/a` for actual predecessors of a ternary-unit target. | An upper bound on actual eternal survivors or an invariant-component regularity estimate. A population lower bound is not a survivor-mass loss. |
| [Entrance renewal, PR183](https://github.com/GettysburgResearch/collatz/blob/907a540943090968bc683b1b9246208e9053c1f8/research/literature-closing-20261121/README.md) and PR185's original survivor fibers | Exact first-entrance accounting, retained source atoms, finite resolvent budgets and conditional absorption statements. | A repeated-return estimate for the transported source law; fresh endpoint weights cannot replace it. Distinct-endpoint arguments also leave the cycle alternative. |
| [Canonical inverse envelope, PR180](https://github.com/GettysburgResearch/collatz/blob/d0349de2108abb7c8fb8393c086610e3372df116/research/lean-forward-band-20261121/MINIMAL_ENVELOPE_ATOM_REMOVAL.md) and PR178's compact Green analysis | Written sublinearity on every fixed predecessor basin, and exact distinctions between ordinary and compact-state Green values. | Uniform sublinearity as the marked target changes. A forward orbit does not remain in the predecessor basin of its initial point. |
| [Ordinary extraction](../integrated/ordinary-extraction/README.md), [periodic tails](../integrated/periodic-tails/README.md), [factor complexity](../integrated/factor-complexity/README.md), and the catalog's Padé/rigidity families | Precise ordinary-realization criteria, whole-denominator cycle conditions, and exclusions for specified symbolic architectures. | An all-source upper-complexity or height input, or an all-word denominator obstruction. Finite compatible prefixes do not extract one positive ordinary source. |
| [Mixed-base normal forms, PR183](https://github.com/GettysburgResearch/collatz/blob/907a540943090968bc683b1b9246208e9053c1f8/research/literature-closing-20261121/README.md) | A terminating subsystem, a common normalization rank and explicit blocked forms, with some actual erasure mergers. | Every blocked form needs a valid component-preserving erasure. Becoming stuck is not convergence. |

## 2. A finite coefficient theorem from exact parity counts and ordinary packing

The new [CoefficientCounting.lean](CoefficientCounting.lean) proves

\[
\sum_{0\le r<2^k}2^{q_k(r)}=3^k,
\]

where `q_k` counts the actual odd shortcut inputs. The proof pairs residues
`r` and `r+2^k`: their first `k` odd counts agree, while their next parities
are opposite because their endpoints differ by an odd power of three.
This is an exact identity on a full residue system. It makes no claim of
independence along an individual ordinary orbit.

For `B>=1`, set

\[
k=70(\lfloor\log_2B\rfloor+3),\qquad M=2^k.
\]

Two kernel-checked integer comparisons yield

\[
4B\,\#\{0\le r<M:2^k\le B3^{q_k(r)}\}\le M.
\]

Quotient--residue injection then shows that `N` distinct ordinary values
at most `X`, each with that same finite coefficient lower bound, satisfy
`4BN<=X+M`. The final full period is paid explicitly; there is no density
limit or hidden boundary error.

[CoefficientPeaks.lean](CoefficientPeaks.lean) supplies the dynamical
hypotheses from a provisional coefficient strip. Write
`C_t=3^(q_t(n))/2^t`, and let

\[
N=n+M+1,\qquad H=6B^2(n+N)+1.
\]

It proves the unconditional finite alternative

\[
\boxed{\exists t\le H:\quad C_t<1\ \text{or}\ C_t>B.}
\]

The proof retains the affine corrections and derives both
`T^t(n)<=B(n+t)` and `t<=6B T^t(n)` under the strip hypothesis. If the
first `N` states repeated, determinism would bound all later states by
`B(n+N)`, contradicting the second inequality at `H`. Thus the required
finite injectivity is proved inside the argument. Exact coefficient
composition supplies the finite block lower bound, and the residue
packing becomes impossible.

The same module proves the explicit polynomial upper bound

\[
H\le12B^2n+6\,2^{210}B^{72}+6B^2+1.
\]

These constants are conservative. The contribution is the **finite,
elementary integer certificate and displayed horizon in Lean**. The older
orbit-Mellin program already has qualitative coefficient escape under its
nonperiodicity hypothesis. That earlier result is credited and is not
presented as new. See [COEFFICIENT_PEAKS.md](COEFFICIENT_PEAKS.md) for the
full derivation and exact prior-source comparison.

This does not prove coefficient stopping. A hypothetical supercritical
path can leave every bounded strip through its upper boundary. It also
does not discard the affine remainder when the lower boundary is crossed.

## 3. A new rule inside the complete-certificate residual language

[CertificateBoundary.lean](CertificateBoundary.lean) uses an inductive
complete odd-gap certificate with checked ordinary-orbit semantics. Its
grade list and comparison reproduce the two source-pinned PR177
definitions: the initial even run contributes grade `2e+1`, an odd gap
`a` contributes `2a`, and the highest changed multiplicity must decrease.

Consider the residual source

\[
S=4(4p+1),
\]

whose supplied odd certificate begins with gap four and then an arbitrary
complete suffix `tail`. That first edge yields a complete sibling
certificate for `p` beginning with gap two, with the **same literal suffix**.
Under the retained-even-reset guards

\[
3\nmid p,\qquad p\ne1,\qquad p\not\equiv7\pmod9,
\qquad p\not\equiv19\pmod{27},
\]

the module constructs a certified predecessor `z>=2p` with a prefix of
gaps at most three. Since a complete odd certificate makes `z` odd,
actually `z>=2p+1`. Consequently the child source

\[
S'=8z\ge S+4
\]

covers the entire old target interval without moving its target.

The grade replacement is exact:

\[
\{5,8\}+\operatorname{grades}(\text{tail})
\quad\longrightarrow\quad
\{7\}+\operatorname{grades}(\text{front})+\{4\}
 +\operatorname{grades}(\text{tail}).
\]

Every front grade is at most six. Grade eight decreases once, and all
higher counts remain equal. The module checks this comparison for an
arbitrary suffix and proves the local interval rule under the explicitly
stated lower-rank induction hypothesis. It does not replace that hypothesis
by a global axiom or claim an exhaustive dispatcher.

The source certificate can grow while its certificate rank decreases.
That is legitimate in the stated certificate induction and must not be
misreported as ordinary value descent of the target. The module also
retains separate exact physical boundary identities discovered during the
attempt, but the final main rewrite needs no boundary excursion.

Direct integration into PR177's implementation is still a source-qualified
interface task: this packet proves the same local grade comparison and
ordinary complete-certificate semantics in a small independent module.
The remaining guarded complement is not covered.

The [guard-composition audit](GUARD_COMPOSITION_AUDIT.md) makes that
comparison concrete. The entire family `768r+295` escapes several listed
static guards yet has the checked physical descent
`T^8(768r+295)=729r+281`. A nearby query uses the complete source certificate
`133 -> 25 -> 19 -> 29 -> 11 -> 17 -> 13 -> 5 -> 1` and wanted target
`1055`. It escapes those short direct tests but first descends at clock
80 to 628, as independently replayed with exact integers. The latter is a
bounded calculation, not another Lean theorem or a counterexample. The
two examples prevent a failed guard from being mistaken for an orbit
obstruction and identify the extra coverage still needed.

## 4. Audit the strongest analytic input before using it

[PREDECESSOR_POPULATION_AUDIT.md](PREDECESSOR_POPULATION_AUDIT.md) records
an independent adversarial reconstruction of the written PR180 implication

\[
X\ge Ca\quad\Longrightarrow\quad
\#\{0<n\le X:n\text{ odd},\ n\to a\}\ge cX/a
\qquad(3\nmid a).
\]

The critical point is not a direct conversion of a polynomial total-variation
error to an exponentially small point probability. A bounded-real-offset,
fixed-total counting operator converts the error to a supremum over final
residues. The review checked that operator's normalization, conservation of
the complete clock, the early/late negative-binomial convolution errors,
every intermediate depth, and distinctness of actual inverse sources. It
also checked Tao's version-seven primary statement at the exact imported
nonnegative renewal estimate.

No unsupported step was found in those specified interfaces. This is a
substantial **source-qualified written result**, with exact file hashes and
external theorem dependence. It is not a Lean theorem, not a review of all
of PR180, and not a new population argument invented by this packet.
None of the Lean results above depends on it.

If available, a linear predecessor lower bound improves the fixed-floor
counting target from beating a particular exponent below one to proving
an `o(X)` upper bound for the actual surviving set. That is a useful change
in the required estimate. It does not supply the estimate: the repository's
native-horizon no-descent roots and its temporal marked visits are different
sets. The fixed original source and all its transported mass must survive
the comparison.

## 5. Qualitative periodic approximation already forces constancy

[PROFINITE_LABEL_RIGIDITY.md](PROFINITE_LABEL_RIGIDITY.md) supplies a new
written route through the earlier stationary-density work. Its input is
Tao's marginal fine-scale mixing together with the earlier selected atom
floor and logarithmic predecessor mass. It does **not** depend on the new
joint-clock natural-density claim audited in Section 4.

Let `f` be a nonconstant Boolean label on the positive ordinary integers
satisfying `f(Tn)=f(n)`. The new result gives one `epsilon_f>0` such that
every `[0,1]`-valued periodic function `p` of period `2^a 3^b` satisfies

\[
\liminf_{X\to\infty}\frac1{H_X}
 \sum_{1\le n\le X}\frac{|f(n)-p(n)|}{n}\ge\epsilon_f.
\]

The same positive constant works for every conductor and every choice of
the approximating values. Thus qualitative approximation in logarithmic
mean would force the label to be constant; the stronger approximation
rate required by the earlier finite-conductor estimate is unnecessary.
A corresponding obstruction holds for the natural upper mean.

The proof constructs measures from the actual ordinary sources using
finite periodic stationary densities. It never evaluates an arbitrary
almost-everywhere density at an ordinary integer. Total-variation coherence
and exact changes of variables along both ordinary branches give an
invariant dominated measure on `Z_2 x Z_3`. A direct coupling proves mixing
there, so that measure is a scalar multiple of the stationary probability.
Logarithmic unit-predecessor mass bounds that scalar away from zero and one
for a separating pair of components. One fixed finite density approximation
then supplies the uniform error floor, independent of the conductor.

This is a source-qualified written measure-theoretic proof, separately
reviewed and outside the Lean theorem count. Its remaining global premise
is substantial: the basin-of-one label has not been shown to admit the
required ordinary-mean approximations. Density of cylinder functions on
the compact space does not supply them. The ordinary integers have compact
measure zero, and the scalar component projection need not be zero or one.

## 6. What still prevents the full theorem

The reassessment did not reveal a missing invocation that completes Collatz.
The remaining alternatives persist at precise points:

1. **Certificate route:** the new gap-four rule reduces one unbounded
   guarded class in the same rank, but sources outside its reset guards
   and other residual queries still need successful rules.
2. **Coefficient route:** the finite theorem forces a lower exit or a
   high peak. It does not rule out repeated upper exits. A first lower
   coefficient crossing still needs its complete displacement conditions.
3. **Population/transport route:** a positive predecessor population,
   summable reciprocal occupation, phase estimates and fixed-basin
   sublinearity do not imply the required moving-target upper bound or
   repeated-return loss for one original surviving atom.
4. **Symbolic/cycle route:** existing exclusions retain their word-family,
   complexity, source-height and whole-denominator hypotheses. They cannot
   be promoted to all positive ordinary itineraries by finite compatibility
   or statistical regularity alone.
5. **Regularity route:** the new theorem removes the rate requirement from
   periodic approximation. It does not construct qualitative approximants
   for the actual basin label. That is still a possible full-theorem target,
   not a conclusion of compact mixing.

The new checked work therefore advances concrete interfaces while keeping
the universal closure obligations visible. Its execution evidence is in
the [reassessment report](../../reports/2026-11-21-dyadic-descent/reassessment/README.md).
