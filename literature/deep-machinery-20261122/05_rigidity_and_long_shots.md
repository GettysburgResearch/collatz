# Rigidity, arithmetic dynamics, and carefully bounded long shots

**Status: literature map and proposed applications, 22 November 2026.**
These are candidates for new representations or restricted-family results.
None currently supplies the missing universal Collatz implication. The
assessments below are our analysis of the interfaces, not claims made by the
cited authors.

Read the [problem interfaces](01_problem_interfaces.md) first. “Useful” means
that a theorem could produce a concrete estimate, exclusion, or certificate
once a named additional lemma is proved. It does not mean that the remaining
lemma is likely to be easy.

## At a glance

| Machinery | What makes it tempting | First missing input | Present recommendation |
|---|---|---|---|
| Furstenberg–Rudolph rigidity | Two multiplicatively independent scales often destroy structured exceptional measures | Invariance under two commuting actions, and usually positive entropy | A representation project, with early rejection tests |
| Higher-rank solenoid rigidity | Handles real and non-Archimedean coordinates together | Genuine higher-rank algebraic action and the required invariant probability | Long shot; inspect the existing centered/adelic chart |
| Benoist–Quint random walks | Classifies stationary measures and orbit distributions | An appropriate irreducible group action and a justified sampling law | Direct affine-matrix application fails |
| Dynamical Mordell–Lang / p-adic interpolation | Converts infinitely many algebraic coincidences into structured return times | One fixed algebraic or analytic map preserving actual branch legality | More plausible on a fixed macro-word family |
| GRH / Chebotarev | Finds arithmetic representatives with quantitative size bounds | A source-preserving conversion from the representative to a smaller merger partner | Existing repo obstruction should be read first |
| Computability and incompleteness | Explain why generic termination procedures can fail | A theorem about this particular map, not a class of programs | Useful for method design, not evidence that Collatz is unprovable |
| Spectral or generating-function reformulations | Could package all ordinary survivors in a positive analytic object | Faithful encoding plus an independently provable analytic estimate | Require an explicit space, norm, and retained-atom statement |

## 1. Furstenberg and Rudolph: could two scales force the right distribution?

### The idea in ordinary language

A set can be highly structured when viewed at one scale. Requiring that the
same set or probability law be compatible with two unrelated magnifications
can leave much less freedom. Collatz visibly contains 2 and 3, so this is an
attractive source of rigidity.

**Actual literature.** Furstenberg's 1967 Theorem IV.1 proves density of the
orbit of an irrational circle point under a nonlacunary multiplicative
semigroup, including multiplication by powers of 2 and 3. His final paragraph
explicitly warns that density does not imply equidistribution for the
increasingly ordered semigroup. Rudolph's 1990 result says that a probability
measure on the circle, invariant and ergodic for the joint action of
multiplication by relatively prime integers at least 2, is Lebesgue if one action has
positive entropy. The zero-entropy alternative remains. [F67] [R90]

### The Collatz interface is not automatic

For the shortcut map, the formal affine branch functions are

$$
A_0(x)=x/2,\qquad A_1(x)=(3x+1)/2.
$$

They do not commute:

$$
A_0(A_1(x))=(3x+1)/4,\qquad
A_1(A_0(x))=(3x+2)/4.
$$

Moreover, only the branch selected by the parity of the current ordinary
integer is legal. A Collatz trajectory therefore does not provide a freely
available two-parameter multiplication action. A distribution invariant
under the selected map need not be invariant under either branch separately.

Nor is the band phase a multiplication-by-2/3 orbit. Its evolution is an
approximately additive rotation by log-base-2 of 3, with an actual carry
and a positive perturbation. Those are different dynamical systems.

### A useful countermodel for a proposed entropy shortcut

Bernstein–Lagarias give a homeomorphism between the shortcut map on the
2-adic integers and the one-sided binary shift. [BL96] Here is an elementary
consequence of that representation.

Take independent binary symbols with probability p of a one, where
0<p<1. The resulting Bernoulli law is shift-invariant and has positive
entropy. Transport it through the conjugacy. This produces an invariant
2-adic Collatz law whose typical trajectory has odd-step frequency p almost surely. In particular p can exceed
log(2)/log(3), the affine coefficient-growth threshold. This concerns symbolic frequency and the coefficient product, not real escape of an ordinary positive orbit.

Thus “invariant Collatz law with positive entropy” does **not** force fair
parity. These nonatomic measures give zero mass to the countable set of
ordinary integers, so they are not counterexamples to Collatz either.
The example identifies the missing condition: ordinary-source information
and the extra invariance cannot be discarded.

### A concrete experiment worth doing

Try to construct from a failed ordinary component a measure on a compact
group carrying *two explicitly defined commuting transformations*. Before
estimating entropy, establish:

1. The transformations preserve the relevant failure information.
2. A limiting measure exists without losing the ordinary-source constraint.
3. It is invariant under both transformations; invariance under their
   selected composition is insufficient.
4. The entropy is positive for the action to which the rigidity theorem applies.
5. A Haar conclusion actually contradicts the original failure property.

The first three items are already meaningful mathematical tasks. A proof of
one of them would be a useful contribution even without the remaining two.

**Stop rule.** If the construction only averages over freely chosen inverse
branches and thereby replaces the fixed original orbit, it has not supplied
this interface. If all one gets is a zero-entropy invariant measure, the
positive-entropy theorem has not classified it.

**Priority:** long shot, with a specific algebraic-invariance test. The
appearance of the integers 2 and 3 alone is weak evidence of applicability.

## 2. Higher-rank adelic and solenoid rigidity

### Why this is more than a superficial analogy

The repo already studies real size together with binary and ternary
arithmetic information. Here a solenoid is a compact connected abelian group whose dual has finite rank; it can retain several such local views in one space. The disconnected group of 2-adic integers alone is not such a solenoid. Deep measure-rigidity results on
solenoids are consequently better candidates than applying a circle theorem
after throwing away the carries.

**Actual literature.** Einsiedler–Lindenstrauss, Theorem 1.2, classify invariant
ergodic probability measures for a totally irreducible, not virtually cyclic
action by commuting automorphisms of a solenoid: either Haar measure or zero
entropy for every action element. Their more general Theorem 1.3 assumes no
virtually cyclic factors and, after restriction to a finite-index subgroup
and a finite ergodic decomposition, gives subgroup translation invariance
together with zero-entropy factors, rather than universal Haar measure. [EL21]

### What must be built in this repository

The relevant object would need an actual higher-rank action, not just a
single noninvertible return map decorated with several coordinates. Adding
the coordinates log(x), x modulo powers of 2, and x modulo powers of 3 does
not prove that the resulting evolution is algebraic or that its components
commute.

A productive starting point is the accepted
[centered/adelic and factor-complexity material](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/RESULTS_CATALOG.md).
Record the exact chart, branch laws, integer embedding, and endpoint
exceptions before modifying it. The
[scoped errata](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/integrated/ERRATA.md)
matter here: closed strips, open cylinders, constant codes, and ordinary
realization have already caused incorrect strengthening attempts.

A possible new direction is a *joining*: a probability distribution recording
two views of the same trajectory, rather than two unrelated marginals.
One might hope to prove that any failure joining has both an arithmetic
restriction and enough entropy to trigger rigidity. This is a research
proposal. Neither the existence of that joining with the needed properties,
nor the entropy bound, is currently available.

**First deliverable:** a two-page exact representation and hypothesis table.
Include a concrete nonordinary 2-adic point and show what the representation
does to it. If the candidate theorem treats that point identically to an
ordinary integer, identify what additional test will separate them.

**Stop rule:** do not invoke the general theorem after proving only the
simpler theorem's hypotheses on a quotient. A nontrivial zero-entropy factor
can contain precisely the unresolved dynamics.

**Priority:** valuable for experts in homogeneous dynamics or arithmetic
dynamics; expensive as a generic first task.

## 3. Benoist–Quint and random matrix products

### Why it is tempting

A finite parity history is an affine map, so an orbit can be encoded by a
product of small matrices. Random matrix theory has powerful results about
stationary measures, Lyapunov exponents, and equidistribution.

**Actual literature.** Benoist–Quint's *Random walks on projective spaces*
studies products sampled from a probability law on a linear group. Its
Theorem 1.1 assumes strong irreducibility and gives a Cesàro limiting law
from each projective starting point; other classification statements retain
their reductivity or algebraic-group hypotheses. Their homogeneous-space
orbit-closure theorem assumes a semisimple Zariski closure of the adjoint
action without compact factors. [BQ14] [BQ13]

### The direct Collatz encoding fails a visible hypothesis

Projective matrices for the two shortcut branches are

$$
M_0=\begin{pmatrix}1&0\\0&2\end{pmatrix},\qquad
M_1=\begin{pmatrix}3&1\\0&2\end{pmatrix}.
$$

Both preserve the line spanned by (1,0). Their products remain upper
triangular. Thus this action is reducible; it does not meet strong
irreducibility. The natural affine group is also solvable, so a semisimple
classification theorem is not available by merely changing notation.

There is a second obstruction: actual parity is chosen by the current
integer. Sampling M_0 and M_1 independently defines another process.
A negative random Lyapunov exponent does not prove that every legal
ordinary product has negative drift.

### Where pieces of the method might still help

One could search for a more informative action on a space of residue
packets or inverse histories. This would have to preserve the exact
endpoint relation and the mass assigned to the original source. An
inverse-branch random walk is a legitimate mathematical object; its
conclusions become relevant only through a proved comparison with
ordinary survivors.

The right first calculation is a group and support audit:

- Write the actual generators, including every affine carry.
- Determine common invariant subspaces and algebraic closure.
- State the sampling measure, its dependence on the input, and its support.
- State the observable connecting a sampled path to a smaller ordinary merger.
- Check that the comparison does not lose rare sources.

**Stop rule:** a measured or simulated negative exponent under independent
parity is a heuristic. An irreducible action manufactured by adding unrelated
generators proves facts about those generators, unless every new move has
an ordinary-orbit interpretation.

**Priority:** low for the direct 2-by-2 representation; a disciplined long
shot for a new packet representation.

## 4. Dynamical Mordell–Lang and p-adic analytic interpolation

### What these tools can do

They replace a sequence of iterates by algebraic or analytic structure.
That can make infinitely many exact coincidences accessible to powerful
zero-set theorems.

**Actual literature.** Bell–Ghioca–Tucker's Theorem 1.3 for étale
endomorphisms of complex quasiprojective varieties describes intersections
of a forward orbit with a subvariety as finitely many arithmetic-progression
orbits, with singleton cases included. Poonen's Theorem 1 interpolates
iterates of a p-adic analytic self-map on a closed unit polydisk when the map
is coefficientwise congruent to the identity modulo p^c for c>1/(p-1).
These are structural theorems under specific map hypotheses, not general
termination theorems. [BGT10] [P14]

### Three different obstacles in the global Collatz application

**The map.** Collatz is selected by parity; it is not one polynomial or
rational morphism on the affine line. A fixed finite parity word has one
affine formula, but changing words changes the formula.

**The local analytic domain.** At p=2, the derivative of a shortcut branch
has 2-adic absolute value 2. A word of length L has derivative 3^s/2^L,
whose 2-adic absolute value is 2^L. The forward branch expands binary
balls. This is not Poonen's near-identity self-map of a fixed polydisk.

At an odd prime the affine formulas have a different local behavior, but
parity is not a continuous function of the p-adic coordinate: even and odd
ordinary integers are both dense. Interpolating a chosen affine formula
therefore does not establish that its infinite iteration follows the legal
ordinary parity branches.

**The target.** Membership in the shrinking band is an inequality involving
binary size. It is not membership in a fixed algebraic subvariety. Even an
exact description of hitting times would not assert that the target is hit.

### A realistic restricted use

Take a fixed macro-word or a fixed finite collection of macro-words with
one integer repetition parameter. Prove all legality guards first.
Then investigate whether the endpoint equation, or an equation for a
candidate partner, lies in a fixed linear recurrence or algebraic dynamical
system. A Skolem–Mahler–Lech or dynamical Mordell–Lang conclusion could
classify repeated coincidences inside that family.

This complements the arithmetic chapter's recurrence-ratio approach.
It might produce an infinite merger family or exclude a fixed family of
cycles. It would not cover arbitrary words whose description length grows
with the source.

**First deliverable:** one explicit guarded family with a fixed algebraic
map and a specified target subvariety. State how each algebraic orbit
element corresponds to an ordinary Collatz computation.

**Stop rule:** if the alleged self-map domain is invariant only after
assuming all future parity choices, the crucial hypothesis is the unresolved
orbit statement itself.

**Priority:** moderate for structured families; low for direct global use.

## 5. GRH, Chebotarev, and conductor costs

### The useful part

Prime-distribution theorems can find numbers meeting congruence conditions
and can bound their size. They may therefore help construct auxiliary
certificates, provided those congruence conditions really imply the needed
ordinary endpoint identity.

**Actual literature.** Bach–Sorenson obtain, under ERH, a least prime in
a reduced residue class modulo q, with q>=2, below 2(q log q)^2. Later work of
Lamzouri–Li–Soundararajan and Carneiro–Milinovich–Quesada-Herrera–Ramos
sharpens conditional least-prime bounds. These theorems concern reduced
residue classes or specified Frobenius data. [BS96] [LLS16] [CMQR24]

### The relevant repository work already exists

Read the complete
[PR166 interface analysis](https://github.com/GettysburgResearch/collatz/blob/5996b9f525ca50978bc34f423192c36a87765bf3/research/grh-certificate-closure-20261120/GRH_INTERFACES.md).
It distinguishes selecting a prime with a prescribed *finite parity prefix*
from preserving membership in a fixed target's *entire predecessor basin*.

One particularly sharp obstruction is elementary. At a prescribed ternary
level e, a decreasing core of the form (2^a n-1)/3^e needs
a<e log-base-2 of 3. For n congruent to -1 modulo 3^e, divisibility instead
forces a congruent to 3^(e-1) modulo 2·3^(e-1). These demands are incompatible
for e>=3. Better prime-selection constants cannot change this arithmetic.

The scope is narrow: adaptive multistep paths, different levels, and larger
actual stripping can behave differently. The repo does not prove that GRH
could never help Collatz.

### The correct task for a number theorist

Find a *new* congruence or Frobenius encoding whose solutions are actual
ordinary partners of the supplied source. Then track:

- whether the class is reduced and nonempty;
- the field degree and discriminant, or the modulus;
- the resulting size bound;
- positivity and every inverse division;
- the strict saving relative to the original source.

A representation by a Dirichlet series also needs a real analytic theorem.
A component-weighted series does not acquire an Euler product, a functional
equation, or a GRH statement merely because it resembles a classical
L-function.

**Stop rule:** finding a well-behaved new source in the same residue class
does not prove the given source behaves well after its shared finite prefix.

**Priority:** low without a new encoding; useful as a constructor after an
independent source-preserving bridge.

## 6. Undecidability, finite abstractions, and what a negative result means

**Actual literature.** Kurtz–Simon prove a generalized Collatz decision
problem is Pi-zero-two complete. Their result ranges over a family of
generalized maps; it is not an independence theorem for the fixed 3x+1
conjecture. The publisher statement was checked; the full author PDF was
not accessible in this retrieval, so no finer proof claim is used. [KS07]

For this project the practical implication is methodological: a universal
black-box termination algorithm for sufficiently expressive arithmetic
programs is too much to expect. It remains possible that this particular
map has a short structural proof.

The same scope discipline applies to finite-state impossibility results.
Failure of a rank built from two features rules out that feature family.
It does not rule out additional state, an unbounded counter, ordinal
ranks, certificate-dependent induction, or an arithmetic proof that never
uses such a rank.

A finite-state overapproximation can be sound for proving termination if
every ordinary run is represented and every abstract run terminates.
But the converse need not hold. An abstract loop can arise by joining
successive transitions that no single ordinary source can follow.
Such a loop is a request for refinement or an arithmetic realizability
proof, not an ordinary counterexample.

**Useful first task:** for each surviving abstract loop, compute its exact
affine composition and congruence guards. Ask whether it has a positive
integer fixed point or an indefinitely realizable ordinary path. Preserve
the complete denominator and sign. The repo's completion ghost is a
mandatory control example.

**Priority:** high as a safeguard for automated search; no evidence here
for unprovability of Collatz.

## 7. Further long shots: demand a representation before investing

These are intentionally less developed than the main chapters. They are
included because a specialist may see a representation the present review
does not.

| Possible machinery | A meaningful first object | Why we do not recommend a theorem citation alone |
|---|---|---|
| Spectral determinants and analytic continuation | A positive survivor-generating function with a proved relation to each original integer atom | A zero-free or meromorphic region must imply a survivor estimate in the correct norm |
| Automorphic or trace-formula methods | An arithmetic quotient and an orbit/certificate correspondence, with a test function representing the required event | No such source-preserving correspondence is supplied by the inspected packets |
| Arithmetic geometry beyond S-units | A fixed-dimensional family of endpoint equations with controlled height and coefficients | Encoding all parity words by growing dimension loses the uniformity a finiteness theorem needs |
| Renormalization of valuation blocks | A closed class of actual return packets with a quantitative error and tail budget | Similar-looking small-scale histograms do not prove closure under repeated transport |
| Computer-assisted operator inequalities | Rational interval bounds for a specific retained-mass norm, including the infinite tail | Eigenvalues of a finite truncation can change when unobserved escape channels are restored |

The investment rule is simple: an ambitious theorem can be worth exploring
even when its relevance is uncertain, but its first task should expose the
missing representation or estimate. “Use deep machinery” is not yet a
research task. “Construct this invariant joining,” “prove this weighted
density bound,” or “classify this one recurrence quotient” is.

## Primary reading

- **[F67]** H. Furstenberg, *Disjointness in ergodic theory, minimal sets,
  and a problem in Diophantine approximation* (1967), Part IV, Theorem IV.1
  and the following equidistribution warning.
  [Paper](https://mathweb.ucsd.edu/~asalehig/F_Disjointness.pdf).
- **[R90]** D. J. Rudolph, *×2 and ×3 invariant measures and entropy*
  (1990). [Publisher statement](https://doi.org/10.1017/S0143385700005629).
  The statement was checked, not the complete proof.
- **[EL21]** M. Einsiedler and E. Lindenstrauss, *Rigidity properties for
  commuting automorphisms on tori and solenoids*, journal publication 2022, online 2021,
  Theorems 1.2–1.3 and Section 4.
  [Full text](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/rigidity-properties-for-commuting-automorphisms-on-tori-and-solenoids/B5B7471AB9A282B5B179E35040809159).
- **[BL96]** D. J. Bernstein and J. C. Lagarias, *The 3x+1 Conjugacy Map*
  (1996), Section 1.
  [Publisher](https://doi.org/10.4153/CJM-1996-060-x).
- **[BQ14]** Y. Benoist and J.-F. Quint, *Random walks on projective spaces*,
  Theorem 1.1 and the introductory hypotheses.
  [Author paper](https://www.math.u-bordeaux.fr/~jquint/publications/projectivespace.pdf).
- **[BQ13]** Y. Benoist and J.-F. Quint, *Stationary measures and invariant
  subsets of homogeneous spaces (III)* (2013).
  [Publisher](https://annals.math.princeton.edu/2013/178-3/p05).
- **[BGT10]** J. P. Bell, D. Ghioca and T. J. Tucker, *The dynamical
  Mordell–Lang problem for étale maps* (2010), Theorem 1.3.
  [Author preprint](https://arxiv.org/pdf/0808.3266).
- **[P14]** B. Poonen, *p-adic interpolation of iterates* (2014), Theorem 1.
  [Author paper](https://math.mit.edu/~poonen/papers/p-iteration.pdf).
- **[BS96]** E. Bach and J. Sorenson, *Explicit bounds for primes in residue
  classes* (1996).
  [Author bibliographic record](https://digitalcommons.butler.edu/facsch_papers/1121/);
  [DOI](https://doi.org/10.1090/S0025-5718-96-00763-6).
- **[LLS16]** Y. Lamzouri, X. Li and K. Soundararajan, *Conditional bounds
  for the least quadratic non-residue and related problems*, corrected v3.
  [Versioned record](https://arxiv.org/abs/1309.3595v3).
- **[CMQR24]** E. Carneiro, M. B. Milinovich, E. Quesada-Herrera and
  A. Ramos, *Fourier optimization, the least quadratic non-residue, and the
  least prime in an arithmetic progression*, v2 dated 12 August 2025 (initial preprint 2024), Section 1.2.
  [Full text](https://arxiv.org/html/2404.08380v2).
- **[KS07]** S. A. Kurtz and J. Simon, *The Undecidability of the Generalized
  Collatz Problem* (2007).
  [Publisher](https://doi.org/10.1007/978-3-540-72504-6_49).
