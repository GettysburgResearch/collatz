# Arithmetic and logic: powerful theorems, exact interfaces, and useful limits

**Status: literature synthesis and proposed research tasks; no new Collatz theorem is asserted.** Checked 2026-11-22. This chapter uses the shortcut map `T(n)=n/2` for even `n`, `(3n+1)/2` for odd `n`, and the odd map `U(x)=(3x+1)/2^{v_2(3x+1)}`. A *marked* integer is positive, odd, and satisfies `(d+1)(n-2^d)≤70·2^d`, where `d=floor(log_2 n)`. Markedness has no mod-3 condition.

Read this chapter in two passes. The plain-language paragraphs identify the mechanism; the displayed conditions tell an implementing agent what must actually be proved. Statements labeled **literature** come from the cited sources. **Proposed bridge** means a deduction or research direction suggested here, not a theorem imported from a paper. **Stop rule** identifies a concrete reason to abandon that implementation without abandoning the whole theory.

## A. The arithmetic triage

| Machinery | What it could buy here | What it does not supply | Priority |
|---|---|---|---|
| Effective linear forms in logarithms | Much faster quantitative entry into the band; strong bounds for restricted cycle patterns | A favorable sign of return drift | High for a bounded technical task |
| Integrality of ratios of recurrences | Classify or exclude entire parametric families of full cycle denominators | A finite menu covering arbitrary parity words | High for a specific family |
| Subspace/S-unit theorems | Rigidity once a fixed-dimensional genuine arithmetic saving is available | A saving from the current band alone | Medium, only after an exact product audit |
| GCD estimates on algebraic tori | Limit unusually large common factors in structured carry identities | Divisibility control for unrestricted carries | Medium/long shot |
| Simultaneous 2- and 3-Mahler equations | Turn a genuine finite functional closure into rationality and eventual periodicity | That finite closure itself | Medium as an obstruction/search tool |
| Cobham–Semenov and Christol | Certify limits of finite-state descriptions; test proposed symbolic models | Automaticity of the all-time basin | Medium as a method screen |
| Arithmetic complexity/transcendence | Exclude specific low-complexity encodings when algebraicity is known | Algebraicity of a Collatz parity encoding | Low as a direct closing route |
| Dynamical Mordell–Lang and p-adic interpolation | Classify intersections for fixed algebraic dynamics; possibly fixed macro-word families | A theorem for arbitrary parity-dependent switching | Long shot |

The useful organizing distinction is **unbounded complexity versus fixed algebraic structure**. The deepest arithmetic theorems are often spectacularly effective after the number of variables, generators, functional equations, or recurrence roots has been fixed. A Collatz trajectory generates new carry information indefinitely. Naming the theorem does not control that information. The first job is to find a representation that stays fixed while the orbit length grows.

## B. Linear forms in logarithms: a plausible upgrade to the band clock

### Plain-language mechanism

Two powers, `2^a` and `3^q`, cannot be equal. The existing proof uses an elementary quantitative version of this fact. Transcendence theory says much more: the logarithms of two fixed multiplicatively independent algebraic numbers cannot have an integer linear combination that is *too* small relative to its coefficients. This controls near-resonances of the rotation by `α=log_2 3`.

**Literature.** Matveev’s explicit theorem bounds nonzero linear forms in logarithms in terms of the number-field degree, heights of the algebraic numbers, and sizes of the integer coefficients. For fixed bases 2 and 3, Corollary 2.3 yields constants `c>0`, `κ>0` for an inequality of the form

$$
|q\alpha-a|\ge c q^{-\kappa}
$$

for integers `q≥1` and `a` in the relevant range `a=O(q)`. Laurent’s two-logarithm estimates and specialized Padé estimates are the natural place to improve the constants. The general Matveev estimate is a reliable existence route, not a claim of numerically competitive constants. [AR01, AR02]

### Proposed bridge: replace a square-root search scale by a power of the logarithm

This is an original proposed consequence of the repository proof architecture, with a proof sketch. It should be formalized as a conditional theorem first.

Let `n` be the current odd source, `H=1+log_2 n`, and suppose the displayed Diophantine bound has been instantiated with explicit constants. Choose

$$
N=\left\lceil c^{-1}(2H)^\kappa\right\rceil.
$$

Dirichlet gives a reduced `a/q` with `q≤N` and `|qα−a|≤1/(N+1)`. The lower bound then forces `q^κ≥c(N+1)`, hence `q≥2H`. The important point is that the rational-grid steering uses fewer than `q` actual odd steps, not necessarily `N` steps.

On the branch where no iterate drops below `n/4`, the cumulative perturbation of logarithmic phase is bounded by `4j/n` at odd clock `j`. The existing grid argument chooses `j<q`, giving a total phase error of order

$$
3/q+4q/n.
$$

For `n` above an explicit threshold with `4N^2≤n`, this is at most `4/q`. Meanwhile `U(x)≤2x` gives endpoint binary height `d+1≤H+j≤H+q≤2q`. Thus `(d+1)×phase_error≤8`, comfortably below the existing logarithmic-phase constant 35. That is precisely the interface used to convert a near-integer logarithmic phase into the marked-band inequality.

If the other branch drops below `n/4`, restart at the smaller integer. At most `O(log n)` such drops occur before a finite base region. Summing costs gives the conservative proposed bound

$$
\text{odd entry clock}=O((1+\log n)^{\kappa+1}).
$$

The repository’s ordinary-clock identity converts a total of `J` odd steps to at most `2J+floor(log_2 n)` shortcut steps. The same polylogarithmic order should therefore survive. Below the threshold, the existing unconditional `bounded_visit` theorem supplies a finite additive bound; no finite verification of Collatz is needed. Rounding, constants, the initial even prefix, and the threshold must all be stated; none has been replaced here by a numerical experiment.

**Why this is interesting.** It would replace an enormous input-size-dependent entry estimate with a bound polynomial in the input’s bit length. It could shorten the forced-visit part of merger certificates and improve quantitative comparisons between source size and marked-partner size. It would also show that the elementary separation estimate is quantitatively expensive rather than conceptually indispensable.

**Why it may not matter to the final conjecture.** Entry into the band is already universal. Faster entry neither makes the endpoint smaller nor proves the valuation average needed for descent. A source can reach a mark above itself. If a proposed global argument only needs existence of entry, improving this clock alone changes no quantifier.

**Agent task.** Refactor `steer` into a theorem taking a quantitative nonresonance hypothesis. Prove the large-`n` clock result with symbolic `c,κ`, then insert one correctly transcribed published bound. Retain the old elementary theorem as the small-range fallback. Record whether the improvement changes a downstream merger inequality.

**Stop rule.** Stop presenting the improvement as a route to closure if it supplies only a shorter clock and no new source-relative saving. Also reject any exponent borrowed from an irrationality bound for `log 3` alone: the needed quantity is a linear form in *both* `log 2` and `log 3`. A bound for one logarithm does not automatically control their ratio.

### Restricted cycle bounds remain a separate use

For an odd cycle `x_0,…,x_{k-1}`, let `A=Σv_2(3x_i+1)`. Multiplying the odd-step identities gives

$$
A\log2-k\log3
=\sum_{i=0}^{k-1}\log\left(1+\frac1{3x_i}\right)>0.
$$

This exact identity is the natural place to compare a transcendence lower bound with a dynamical upper bound. The right side becomes small if the cycle elements are large. The missing global ingredient is not positivity of the left side; it is enough uniform control to defeat cycles of arbitrary combinatorial complexity.

**Literature.** Simons–de Weger combine such estimates with continued fractions/lattice reduction for cycles having a specified number of local minima. Their author revision explicitly states that the upper bounds grow exponentially with that number. Hercher’s later paper continues this program; its publisher now supplies a June 2026 corrigendum to the proof of Theorem 21. The parameter counting local minima must not be confused with total odd steps. [AR03, AR04]

**Useful outcome.** A new band-based upper bound for the sum of reciprocal cycle values could strengthen this method. Merely observing that a cycle has a marked point does not supply that sum: a band condition describes leading binary digits, not the distribution of all cycle values.

## C. The Subspace Theorem: first audit the entire arithmetic budget

### What the theorem is trying to detect

In elementary language, a large integer vector cannot repeatedly make several independent algebraic linear expressions unusually small in the real and p-adic senses unless the vectors lie in a special lower-dimensional family. Real smallness and divisibility by prime powers can cooperate. The theorem requires a fixed positive power saving in height after *all* normalization factors are included.

**Literature.** The p-adic Subspace Theorem, in the normalization used in Adamczewski–Bugeaud’s Theorem E, concerns a fixed number of variables, a fixed finite set of places, and full-rank algebraic linear forms. Its conclusion is confinement of sufficiently good approximants to finitely many proper subspaces. It is not a general statement that a relative error tending to zero forces degeneracy. [AR05]

### The repository already tested the most tempting application

The latest arithmetic note on #183 is essential prior work, not an idea to rediscover. Write the actual odd orbit as

$$
2^{A_j}x_j=3^j n+B_j,
\qquad x_j=2^d+u.
$$

For its natural vector `(3^j,2^{A_j+d},B_j)` and specified full-rank forms at `∞,2,3`, the complete unnormalized product of local factors is **exactly `u`**. At a nontrivial odd endpoint, `u≥1`. After projective normalization, the extra negative power required by the theorem is absent. Repeating the same construction at finitely many visits gives a product of offsets, still at least one. Coupled two-return elimination leaves an odd nonzero integer residual; the tested three-return gcd need not grow. These are precise obstructions to those form systems, not a universal impossibility theorem about Diophantine approximation.

**Proposed bridge worth looking for.** Find an additional relation that eliminates more than the monomial factors already canceled. Examples would be a uniformly bounded set of carry types, an actual common divisor that grows faster than the surviving residual, or a low-dimensional dependency among *several* carries that does not merely restate the orbit recurrence. Any such relation must concern the same fixed ordinary source along unbounded times.

**Agent task.** Before citing a Subspace theorem, write a table with: coordinates; all places; every linear form; determinant; vector content; exact height; exact product; and the resulting exponent. Reduce the entire product symbolically. A proof that only bounds one attractive factor should not proceed to the theorem-import stage.

**Stop rule.** If the normalized expression is `H^{-m}×integer` with the integer nonzero, the desired `H^{-m-ε}` inequality is impossible. If the number of coordinates grows with time, the fixed-dimension theorem has not been applied. If coefficients are chosen anew to fit each point, their heights and motion must be paid for.

### Do moving-target theorems rescue moving bands?

**Literature.** Ru–Vojta’s moving-hyperplane extension permits changing targets under specific nondegeneracy and slow-motion hypotheses. Vojta’s author exposition, Theorems 7.6–7.7, includes `h(H_j(i))=o(h(x(i)))`, together with independence over the field of moving coefficients. [AR06]

**Assessment.** This addresses a real limitation of a fixed-form theorem, but it does not create an arithmetic saving. Reanchoring a form at each new marked source may violate slow motion because the source height can be comparable to the point height. Selecting very separated times might make the coefficient-height ratio smaller, but the exact product cancellation still has to be overcome. A target changing slowly is not the same thing as a point approximating that target unusually well.

**Small experiment.** For a proposed coupled construction, report both `h(coefficients)/h(point)` and the complete local product. This separates two independent failures that are easily conflated. Pursue moving targets only if the first ratio tends to zero *and* the second expression exhibits a genuine negative power.

## D. S-unit equations: excellent for bounded complexity, not arbitrary carries

An *S-unit* is a rational or algebraic number whose prime factors lie in a fixed finite list, allowing negative exponents. Powers of 2 and 3 are the model example. A striking theorem says that a fixed linear equation cannot have too many essentially different solutions made from a multiplicative group of fixed rank.

**Literature.** Evertse–Schlickewei–Schmidt, Theorem 1.1, bounds the number of nondegenerate solutions to

$$
a_1z_1+\cdots+a_rz_r=1,
$$

with fixed nonzero coefficients and `(z_1,…,z_r)` in a multiplicative subgroup of finite rank `s`. Their bound depends only on `r,s`; a nondegenerate solution has no vanishing proper subsum. This is a finiteness/count theorem, not automatically an algorithm listing every solution. [AR07]

**Repo interface.** A fixed macro-pattern can give an equation with a bounded number of monomials `2^a3^b`. The corrected 256-stage architecture already demonstrates the value of this type of rigidity. The natural next question is whether some other architecture of unresolved returns can be compressed into a fixed number of such terms.

The full affine carry is

$$
B_j=\sum_{i=0}^{j-1}3^{j-1-i}2^{A_i}.
$$

There are `j` terms. Calling each term an S-unit does not put the *sum* in a bounded-rank multiplicative group; calling `B_j` a new variable does not make it an S-unit. This is the main applicability barrier. It is not repaired by the fact that all coefficients of the original recurrence are small.

**Concrete next task.** Search for an exact compression of a *restricted* class of return words into at most `r` geometric blocks, with `r` independent of the return time. Derive the resulting S-unit equation, list degenerate subsum cases, and compare them with actual positive ordinary trajectories. A uniform theorem for that class could eliminate an infinite obstruction family even if it does not cover all sources.

**Stop rule.** If `r` grows with the input or a newly introduced carry has unrestricted prime factors, report a failed interface. Do not hide the dependence in a notation such as “a bounded equation” when the bound depends on the trajectory length. If degenerate subsums survive, they are mathematical cases to classify, not noise to discard.

## E. Integrality of recurrence quotients: a stronger route for parametric cycles

### Why this deserves an agent

The difficult issue in a periodic parity word is the **complete denominator**. A local obstruction at one prime may disappear after cancellation with the numerator. There is a substantial arithmetic theory that studies when a ratio of two exponential-polynomial sequences is integral infinitely often. This is much closer to a full-denominator question than a sequence of unrelated modular sieves.

**Literature: exact usable statement.** Corvaja–Zannier’s Theorem 2 assumes that the characteristic roots of two linear recurrences `F,G` together generate a torsion-free multiplicative group. Let `R` be a finitely generated subring of the complex numbers. If `G(k)≠0` and `F(k)/G(k)∈R` for infinitely many natural numbers `k`, there is a nonzero polynomial `P` for which both `PF/G` and `G/P` are linear recurrences. Theorem 1 gives a version without the root-group assumption after restriction to an arithmetic progression. The polynomial factor cannot be omitted in general; the appendix explains difficult residual polynomial-denominator cases. [AR08]

**Verification scope.** The complete statements of Theorems 1–2 were recovered from indexed text of the primary author-hosted PDF, together with its abstract and appendix. Direct PDF retrieval returned HTTP 503; the publisher supplied a paywalled landing page. The theorem statements are checked, but the complete proof was not read in this pass.

### Proposed bridge to full cycle denominators

Fix finitely many legal parity blocks `V_1,…,V_r` and consider a one-parameter family

$$
W(k)=V_1^{a_1k+b_1}\cdots V_r^{a_rk+b_r},
$$

where the coefficients are integers and the repetition exponents are nonnegative on the domain. The number of blocks is fixed; their lengths grow. The corresponding affine map can be computed using geometric sums. Both the complete cycle numerator `C(k)` and denominator

$$
D(k)=2^{|W(k)|}-3^{\#1(W(k))}
$$

are exponential-polynomial sequences after clearing fixed denominators. Thus a prospective ordinary cycle has `x(k)=C(k)/D(k)`. For fixed blocks, the affine multiplier of every nonempty block is a power of 3 divided by a power of 2, hence differs from 1. Its iterated translation is therefore a geometric sum. Expanding finitely many such sums makes `C(k)` a finite sum of constant coefficients times positive rational bases raised to `k`; those bases belong to the multiplicative group generated by 2 and 3. The same holds for `D(k)`. This group is torsion-free. Exclude an identically zero denominator and shift the parameter if necessary so all retained denominators are nonzero.

**Proposed corollary, with an elementary proof.** In this interface `D(k)` is a *simple* recurrence: its exponential terms have constant coefficients, rather than nonconstant polynomial coefficients. If `D=P H` for a polynomial `P` and a recurrence `H`, uniqueness of the exponential-polynomial representation forces `P` to be constant. Indeed, write `H(k)=Σ p_i(k)λ_i^k` using distinct nonzero roots and polynomial coefficients. The coefficient of each surviving root in `D` is `P(k)p_i(k)`, which must be a nonzero constant for at least one root. Both polynomial factors must then be constant. Eventual identities suffice; finitely many initial indices do not affect the argument. Consequently, Theorem 2 implies that infinitely many integral values of `C(k)/D(k)` force that quotient itself to be a linear recurrence. This deduction is proposed here for independent checking; it is not a repository theorem.

The intended proof pattern is now sharper: derive the fixed recurrence family; apply the preceding necessary condition; classify when a recurrence quotient can occur; then test positive ordinary realizability and minimal period. Do not assume without proof that the quotient's roots lie in the original root group. A constant quotient from repeating the trivial cycle must survive the algebraic classification and then be explicitly recognized. Negative or rational realizers are also legitimate algebraic outputs and must be separated from positive ordinary ones.

**Why useful even without closure.** The result could exclude a whole parametric family at once, retain the full denominator, and explain *why* a modular search keeps finding finite witnesses. It may generalize the repository’s fixed-architecture exclusion without pretending to cover arbitrary infinite directives.

**Main missing bridge.** No theorem currently says every nontrivial Collatz cycle or exceptional return has a word in finitely many such schemas. An arbitrary word is not a member of a fixed recurrence family merely because its individual letters come from a two-letter alphabet.

**Agent task.** Pick one existing cycle/stack schema whose parameters already have arithmetic meaning. Derive `C(k),D(k)` symbolically and verify the simple-denominator corollary. Classify recurrence-quotient possibilities; a group-ring divisibility approach additionally needs its root-group reduction proved. Deliver a classification with a precise exception set or an explicit obstruction to applying the theorem before doing long numerical searches.

**Stop rule.** If each new candidate requires a new root set or more geometric blocks, the proposed uniform family has not been found. Also distinguish ineffective finiteness from a certified finite search: the former is a mathematical result but does not justify claiming that all remaining cases were computationally checked.

## F. Deep gcd estimates: structured common factors, not generic carry cancellation

**Literature.** Bugeaud–Corvaja–Zannier show that for multiplicatively independent positive integers `a,b`, `gcd(a^k−1,b^k−1)<exp(εk)` for all sufficiently large `k`, for each `ε>0`. Corvaja–Zannier extend this viewpoint to heights of fixed rational functions at points of a finitely generated subgroup of the two-dimensional multiplicative group. Their Theorem 1 tracks exceptional translates of subtori for fixed coprime polynomial pairs. [AR09, AR10]

**Plain language.** Two unrelated exponential mechanisms cannot repeatedly share an unexpectedly large common arithmetic factor unless they satisfy a special multiplicative relation. The exceptional algebraic relations are part of the answer.

**Potential interface.** A cycle candidate requires `D(k)|C(k)`. If a restricted family turns this divisibility into an abnormally large gcd of two fixed polynomial expressions in `2^k,3^k`, a torus gcd theorem may force the family onto an exceptional subtorus. Those exceptional relations could then be classified explicitly.

This is a more concrete long shot than “use algebraic geometry.” The exact object to search for is a pair of fixed polynomials and a fixed finitely generated group; the payoff is a height lower bound or small-gcd statement that conflicts with full divisibility.

**Why the direct version fails.** General `B_j` is not a fixed polynomial in `2^j,3^j`; it remembers the intermediate valuation sums. Also, the repository’s coupled-return residuals can already be coprime. Small gcd is no contradiction there. The contradiction would have to arise from a *separate* requirement that the same gcd be large. Neither band membership nor close leading phase provides that requirement.

**Agent task.** For one recurrence family from section E, factor the numerator and denominator symbolically and test whether a known torus gcd theorem controls their common part. Explicitly compute the exceptional multiplicative relations and verify whether they include legitimate trivial-cycle repetitions.

**Stop rule.** Do not replace the theorem’s fixed polynomial by a polynomial whose degree grows with the word length. Do not replace two independently varying exponents by the common exponent `k` without a derivation. An “unlikely intersection” slogan is not an input until the algebraic variety and orbit are specified.

## G. Cobham, Mahler, and finite closure under two scales

### The deep result behind a useful question

Finite automata can recognize many complicated-looking sets of integers in one base. Requiring a finite description in two multiplicatively independent bases is much more rigid.

**Literature.** Cobham’s theorem says a set of nonnegative integers recognizable by finite automata in two multiplicatively independent bases is ultimately periodic. Semenov extends this phenomenon to multidimensional predicates and Presburger definability. A functional-equation extension is Adamczewski–Bell’s Theorem 1.3: over a field of characteristic zero, a formal power series that is both `k`-Mahler and `l`-Mahler for multiplicatively independent `k,l` is rational. A Mahler equation is a finite linear relation, with polynomial coefficients, among `1,F(z),F(z^k),F(z^{k^2}),…`. [AR11, AR12, AR13]

### A precise candidate for the repo

Let `b(n)` indicate membership in the basin of 1, and consider the formal series `F(z)=Σb(n)z^n`, with a stated convention for `b(0)`. The orbit identities relate `b(2n)` to `b(n)` and `b(2n+1)` to `b(3n+2)`. These are exact but do **not** immediately give independent finite 2-Mahler and 3-Mahler systems for `F`.

The natural attempt is to add a vector of residue-subsequence generating functions until substitution and residue extraction close in a fixed dimension. If this succeeds for both scales, simultaneous-Mahler rigidity could force rationality. A rational power series with a finite coefficient alphabet has an eventually periodic coefficient sequence. That would put the basin or its complement into a much more restrictive class, after which its actual Collatz invariance would still need to be used.

The crucial sentence is “if this succeeds.” Repeatedly adding residue classes at larger moduli may make the vector grow forever. A finite-state description of **one step** does not imply a finite-state description of **unbounded reachability**. Taking transitive closure is exactly where the unknown dynamics enters.

**Relation to existing rigidity.** This could be used as a method screen rather than a global proof. If a proposed finite functional architecture would force the basin indicator into a class already shown too rigid by the repository’s finite-section or semilinear arguments, one can reject that architecture before investing in it. Conversely, identifying the precise operation that destroys finite closure may isolate what an enriched representation must retain.

**Agent task.** Start with finite-time basin approximants `b_t(n)` and compute their 2- and 3-kernel growth. Record exact linear dependencies over a specified coefficient field, not just similar plots. Try to prove an upper bound on the dimension independent of `t`; failing that, prove a lower-bound obstruction for the chosen representation. Do not infer all-time stabilization from a finite plateau.

**Stop rule.** A finite system whose coefficients or number of states depend on the input height is not a single Mahler system. A relation mixing `z↦z^2` and residue extraction at 3 is not automatically two separate Mahler equations. If the only way to close the system is to assume all numbers reach 1, the representation has encoded the conclusion.

## H. Christol and arithmetic complexity: attractive but easy to misapply

**Literature.** Christol–Kamae–Mendès France–Rauzy characterize algebraic formal power series over a finite field by automatic coefficient sequences. Adamczewski–Bugeaud prove that the digit expansion of an irrational algebraic real number, and likewise the Hensel expansion of an irrational algebraic p-adic number, cannot have bounded linear factor complexity: `liminf p(L)/L=∞`. Their p-adic repetition criterion concerns the actual digits of the algebraic number being approximated. [AR14, AR05]

**Useful interpretation.** Christol gives a testable dictionary between algebraicity and finite automata in positive characteristic. The complexity theorem gives a strong obstruction to a low-complexity digit pattern representing an algebraic irrational. Both can turn a representation theorem into a rigorous impossibility result.

**The Collatz encoding mismatch.** If `Q(n)=Σ(T^j(n) mod2)2^j`, then `Q(n)` records parity, while `n` is the ordinary source. Bernstein–Lagarias construct the inverse conjugacy and explicitly distinguish proved forward rationality preservation from the unproved reverse Periodicity Conjecture. Rationality of `n` does not establish algebraicity of `Q(n)`. A sequence obtained from an integer by an arbitrary continuous 2-adic map need not retain algebraicity. [AR15]

The latest repository note already makes this distinction and constructs close marked returns whose next parity behavior differs immediately. Thus a proposal cannot infer repeated low-bit blocks merely from close leading phases. Likewise, every prescribed finite odd-start parity word occurs at sufficiently high marked inputs; such witnesses vary with their required horizon.

**Possible narrow use.** Study an explicitly defined auxiliary generating series of a restricted certificate family, prove a functional equation or algebraicity independently, and then apply automatic/complexity restrictions to that auxiliary object. This can rule out a family of certificates or give exact recurrences for counting them. It does not classify the full basin unless a separate coverage theorem exists.

**Agent task.** Put two columns in the proof: “number whose digits are analyzed” and “number known to be algebraic.” Prove they agree or state the exact algebraicity-preserving map between them. If working modulo a prime, add a third column specifying what information survives reduction and what must be lifted back to ordinary integers.

**Stop rule.** Do not apply a finite-field theorem to a real or 2-adic value by analogy. Do not infer a characteristic-zero recurrence from recurrence modulo one prime. Do not infer an upper bound on orbit-word complexity from the literature’s necessary lower bound. These are different directions of implication.

## I. Dynamical Mordell–Lang and p-adic interpolation: a disciplined long shot

**Literature.** Bell–Ghioca–Tucker prove a dynamical Mordell–Lang theorem for étale endomorphisms of quasiprojective varieties in characteristic zero. Intersections of an orbit with a subvariety decompose into finitely many appropriate suborbits. Their proof constructs p-adic analytic parametrizations along arithmetic progressions and uses the rigidity of zeros of analytic functions. [AR16]

**Plain language.** For a fixed sufficiently regular algebraic evolution, repeatedly landing on an algebraic constraint often forces a repeating algebraic reason. This is much stronger than counting a finite set of coincidences.

**Why it sounds relevant.** Band returns, mergers, and periodic shadows are all repeated encounters with special sets. Exact affine maps for fixed parity blocks are simple algebraic maps. One might hope to interpolate a carefully chosen induced evolution and force repeated encounters to have structure.

**Why there is no direct application.** The global Collatz map switches branches by parity. That is not one algebraic endomorphism of the affine line over the complex numbers. The marked set additionally uses a floor logarithm and an inequality, rather than being a fixed algebraic subvariety. A finite list of affine branch maps is a semigroup of possible maps, not the iteration of one fixed étale map. Lifting the branch choice to an auxiliary coordinate must be done in fixed finite dimension and preserve actual ordinary legality; an infinite itinerary tape does not satisfy those requirements.

**Possible use.** Restrict to a macro-word family in which one fixed transformation is iterated, or to an independently proved finite algebraic model of a certificate transition. The theorem could then classify repeated exact merger conditions or divisibility equalities. Such a result would concern that model, with a separate theorem needed to connect its orbits to all Collatz sources.

**Agent task.** Before reading further arithmetic dynamics, write down the proposed variety `X`, map `Φ`, subvariety `V`, and ordinary-source embedding. Check that `Φ` is genuinely fixed, that it preserves the model, and that the target is algebraic. If this cannot be done on one page, report the missing construction rather than invoke the theorem.

**Stop rule.** Do not apply results for degree-at-least-two rational maps and canonical heights to a switching affine system without proving a compatible height theory. Choosing a favorable prime may make branch coefficients integral, but it does not remove the parity switch or prove the required analytic interpolation.

## J. Recommended arithmetic handoff order

1. **Conditional clock improvement.** A clear, bounded theorem-engineering task with a genuine deep input. It has the highest confidence of producing a useful new quantitative result, but a limited direct relationship to closure.
2. **One full-denominator recurrence family.** Use the existing fixed-architecture exclusions as a model; choose a different concrete schema and derive its exact exponential-polynomial quotient. Seek a family theorem, not a global slogan.
3. **Exact finite functional closure or a no-go theorem.** Try the two-scale generating-series interface with an explicit stopping rule on dimension growth. Either outcome can guide later agents.
4. **New coupled arithmetic saving.** Revisit Subspace/gcd machinery only after identifying an invariant that escapes the already computed product cancellation. This is potentially powerful but currently has the largest missing conceptual input.

A useful output from any of these tasks is a theorem of the form: “Under these exact structural hypotheses, this family is impossible; here is the first source of unbounded complexity that prevents extension.” That is more durable than a long list of deep theories whose hypotheses have never been translated.

## Primary-source index

- **AR01 — Matveev (2000)**, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, Corollary 2.3. [Publisher](https://www.mathnet.ru/eng/im314).
- **AR02 — Laurent (1994)**, *Linear forms in two logarithms and interpolation determinants*, Theorems 1–3. [Publisher](https://doi.org/10.4064/aa-66-2-181-199). The 1995 Laurent–Mignotte–Nesterenko refinement is a further reading lead, not a separately instantiated bound here.
- **AR03 — Simons–de Weger (2005; author revision 2007)**, *Theoretical and computational bounds for m-cycles of the 3n+1 problem*, especially §§5–6. [Author PDF](https://www.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.43%5B2007%5D.pdf).
- **AR04 — Hercher (2023; corrigendum 2026)**, *There are no Collatz m-Cycles with m≤91*. [Publisher and correction links](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html).
- **AR05 — Adamczewski–Bugeaud (2007)**, *On the complexity of algebraic numbers I. Expansions in integer bases*, Theorems 1, E, 1B and 6. [Author PDF](https://adamczewski.perso.math.cnrs.fr/ComplexityI.pdf).
- **AR06 — Ru–Vojta (1997)**, *Schmidt’s Subspace Theorem with moving targets*. Precise formulation checked in Vojta’s author exposition, Theorems 7.6–7.7. [Exposition PDF](https://library.slmath.org/books/Book37/files/vojta.pdf), [author bibliography](https://math.berkeley.edu/~vojta/bib.html).
- **AR07 — Evertse–Schlickewei–Schmidt (2002)**, *Linear equations in variables which lie in a multiplicative group*, Theorem 1.1. [Full paper](https://arxiv.org/pdf/math/0409604), [publisher](https://annals.math.princeton.edu/2002/155-3/p04).
- **AR08 — Corvaja–Zannier (2002)**, *Finiteness of integral values for the ratio of two linear recurrences*, Theorems 1–2 and Appendix 4. [DOI](https://doi.org/10.1007/s002220200221), [author-hosted PDF, intermittent 503](https://oerior.uniud.it/wp-content/uploads/2018/12/CorvajaZannier2002.pdf). Complete theorem statements checked in indexed primary PDF text; full proof not read.
- **AR09 — Bugeaud–Corvaja–Zannier (2003)**, *An upper bound for the G.C.D. of a^n−1 and b^n−1*. [Publisher](https://doi.org/10.1007/s00209-002-0449-z). Its statement is also explicitly recorded in AR10 by the same authors of the subsequent generalization.
- **AR10 — Corvaja–Zannier (2005; preprint revision 2004)**, *A lower bound for the height of a rational function at S-unit points*, Theorem 1 and Corollary 1. [Full paper](https://arxiv.org/pdf/math/0311030).
- **AR11 — Cobham (1969)**, *On the base-dependence of sets of numbers recognizable by finite automata*. [Author institution record](https://research.ibm.com/publications/on-the-base-dependence-of-sets-of-numbers-recognizable-by-finite-automata). Exact classical statement also checked in AR13, Theorem 2.1.
- **AR12 — Semenov (1977)**, *The Presburger nature of predicates that are regular in two number systems*. [Publisher record](https://www.mathnet.ru/php/archive.phtml?jrnid=smj&option_lang=eng&paperid=3937&wshow=paper). Bibliographic/extension lead; no untranscribed quantitative variant is used.
- **AR13 — Adamczewski–Bell (2017)**, *A problem about Mahler functions*, Definition 1.1 and Theorem 1.3. [Publisher PDF](https://journals.sns.it/index.php/annaliscienze/article/download/574/560).
- **AR14 — Christol–Kamae–Mendès France–Rauzy (1980)**, *Suites algébriques, automates et substitutions*, Theorem 1. [Primary archive](https://www.numdam.org/articles/10.24033/bsmf.1926/).
- **AR15 — Bernstein–Lagarias (1996)**, *The 3x+1 conjugacy map*, §1, formulas (1.5)–(1.6), Periodicity Conjecture. [Publisher](https://doi.org/10.4153/CJM-1996-060-x).
- **AR16 — Bell–Ghioca–Tucker (2010)**, *The dynamical Mordell–Lang problem for étale maps*, Theorem 1.3. [Author preprint](https://arxiv.org/pdf/0808.3266).

Repository-specific barriers in sections C and H refer to PR #183 at `cc046e189366e7e876fc283b80459e64faa9c486`, `research/literature-closing-20261121/arithmetic/ARITHMETIC_CLOSURE.md`, especially AR-2 through AR-5. The clock proposal uses PR #173 at `fa0c9e2a2851e6324391e39c17afcb5913185aec`, `research/lean-shell-cover/ForwardSection.lean`. These are source inspections and proposed deductions, not independent Lean replays.
