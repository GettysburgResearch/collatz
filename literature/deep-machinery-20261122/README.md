# Deep machinery for Collatz: an agent field guide

**Literature deep dive and research handoff — 22 November 2026.**
**Project status: OPEN.** This guide contains established literature,
source-qualified recent work, proposed deductions, and unproved research
targets. It does not claim a proof of Collatz or independent replay of the
cited Lean projects. The accepted baseline is main at
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; exploratory source heads are
frozen separately in [REPO_SOURCES.json](REPO_SOURCES.json).

**Scope:** six detailed chapters, 57 distinct primary works or explicitly
qualified primary-source leads, and fourteen task cards. The full guide and
bibliography are about 27,000 words; the tables and reading paths below are
intended to make selective reading practical.

## The main finding

There are serious connections to deep mathematics here. The strongest
connections have a particular shape: a powerful theorem can organize or
classify an object that the repository already nearly constructs, but a
specific source-preserving estimate or finite-complexity representation is
still missing.

The most direct analytic route is to control the **actual distribution left
after repeated failed returns**, or to make its survivor count smaller than
a rigorously constructed predecessor population. The most concrete
arithmetic route is to improve the quantitative band-entry theorem or
classify a fixed family of complete cycle denominators. The most useful
termination route is to combine locally decreasing resources while proving
that every required ordinary source is covered.

The high-risk opportunities are also real: entropy inverse theorems,
higher-rank measure rigidity, countable-state pressure, and simultaneous
Mahler equations can impose remarkable structure. They require an exact
representation that is presently absent. This guide gives an early test
for that representation instead of suggesting months of reading on the
strength of the symbols 2 and 3.

## Read it at the right depth

| Time / role | Reading path | Outcome |
|---|---|---|
| Ten-minute triage | This page, then [task queue](06_agent_tasks.md) | Choose a task with a stated output and stop rule |
| Starting work on the repo | [Problem interfaces](01_problem_interfaces.md) | Fix maps, clocks, source weights, quantifiers, and exact open obligations |
| Analysis / probability agent | [Analysis and entropy](02_analysis_and_entropy.md), then [return operators](04_returns_operators_and_termination.md) §§1–7 | Translate mixing or drift into a claim about retained ordinary sources |
| Number theory / logic agent | [Arithmetic and logic](03_arithmetic_and_logic.md) | Find a fixed-dimensional arithmetic target; retain the full denominator |
| Formalization / automated reasoning agent | [Return operators and termination](04_returns_operators_and_termination.md) §§8–12, then the tasks | Build sound compositional certificates and expose coverage failures |
| Dynamics specialist | [Rigidity and long shots](05_rigidity_and_long_shots.md) | Test whether an invariant action, joining, or algebraic interpolation can actually be built |
| Auditing a citation | [Human source index](SOURCES.md) and [machine source manifest](SOURCES.json) | Find exact version, theorem location, inspected scope, and caveat |

Each substantial machinery discussion follows the same pattern: what it
does in plain language; the actual theorem and hypotheses; a proposed
translation; the first missing lemma; a useful initial deliverable; and a
condition under which that implementation should stop.

## Ranked machinery map

Priority reflects expected usefulness **for the current repository**, not
the depth or importance of the subject. “High” can mean a valuable bounded
result, rather than a high probability of solving Collatz.

| Machinery | Concrete possible payoff | The load-bearing missing input | Priority / chapter |
|---|---|---|---|
| Tao's Fourier mixing, collision estimates, and two-dimensional renewal | A checked joint clock/offset population theorem; a foundation for stronger survivor estimates | Correct law after clock conditioning and every source selection; later transport is separate | Very high; [02](02_analysis_and_entropy.md) §§2–3 |
| Quantitative predecessor density plus a fixed-floor tail | Turn one failed orbit's ancestor population into a contradiction | A uniform upper bound in the fixed floor, with the right rate and limit order | Very high target; [02](02_analysis_and_entropy.md) §3 |
| Weighted collision energy and operator renewal | Control repeated marked returns while keeping every original atom | The stated near-square-root $L^2$ growth bound, or the corresponding retained-atom envelope | High target; [04](04_returns_operators_and_termination.md) §§3–4 |
| Foster–Lyapunov / occupation potentials | Charge a finite budget to every surviving return, including cycles | A finite nonnegative potential satisfying the actual killed-operator inequality | High target; [04](04_returns_operators_and_termination.md) §5 |
| Matveev / linear forms in logarithms | A proposed entry clock polynomial in input bit length | Explicit constants and a careful transplant into the existing grid argument | High bounded task; [03](03_arithmetic_and_logic.md) §B |
| Corvaja–Zannier recurrence quotients | Classify entire parametric cycle families using the whole denominator | Derive a fixed recurrence schema, then classify possible quotient recurrences | High family task; [03](03_arithmetic_and_logic.md) §E |
| Size-change, transition invariants, multiset ranks | Let different local resources cooperate in a termination proof | Sound composed constraints and universal coverage of ordinary sources | High; [04](04_returns_operators_and_termination.md) §§8–10 |
| Krasikov–Lagarias inequality certificates | An exact finite certificate, or a dual obstruction explaining missing state | A faithful survivor abstraction retaining overflow, guards, and collisions | High experiment; [02](02_analysis_and_entropy.md) §5 |
| Original-source first-passage counting | Avoid replacing transported packets by a fresh population | A pullback bound stable under previous failures | High comparison; [02](02_analysis_and_entropy.md) §4 |
| Hochman entropy inverse theory | Classify why selected packets fail to spread | A genuine convolution or quantitative decoupling theorem in the correct ambient space | Medium / speculative; [02](02_analysis_and_entropy.md) §6 |
| Subspace, moving-target and S-unit theorems | Rigidity of a bounded-complexity carry architecture | A genuine arithmetic saving after the complete local product is simplified | Medium with a new invariant; [03](03_arithmetic_and_logic.md) §§C–D |
| GCD estimates on algebraic tori | Force an integral cycle family onto exceptional multiplicative relations | Fixed polynomial expressions and an independently required large common divisor | Medium family task; [03](03_arithmetic_and_logic.md) §F |
| Cobham–Semenov / simultaneous Mahler equations | Rationality or eventual periodicity from two finite descriptions | One finite system closed under both scales for the all-time object | Medium representation task; [03](03_arithmetic_and_logic.md) §G |
| Young towers and countable-state pressure | Keep long excursions and diagnose loss of mass at infinity | Faithful ordinary coding, appropriate invariant law, and tail/recurrence estimates | Medium / long shot; [04](04_returns_operators_and_termination.md) §§2,6 |
| Path-complete Lyapunov functions | A family of compatible local potentials for guarded macrosteps | Correct guard language; affine drift rather than impossible full-vector contraction | Medium restricted task; [04](04_returns_operators_and_termination.md) §11 |
| Furstenberg–Rudolph and solenoid rigidity | Convert extra invariance and positive entropy into a rigid measure | Two genuine commuting actions preserving failure information and ordinary realization | Long shot; [05](05_rigidity_and_long_shots.md) §§1–2 |
| Dynamical Mordell–Lang / p-adic interpolation | Structure repeated exact coincidences in a fixed macro-word family | A fixed admissible map, invariant domain, and algebraic target | Family-level long shot; [05](05_rigidity_and_long_shots.md) §4 |
| Entropy decrement / sum–product | An information budget or structural obstruction for leading/trailing dependence | Stationarity, covariance, legal branching, or prime-power structure not yet supplied | Long shot; [02](02_analysis_and_entropy.md) §§7–8 |
| Benoist–Quint / random matrices | A new action on packets or histories | The direct affine action is reducible; random sampling is not actual parity | Low for the direct encoding; [05](05_rigidity_and_long_shots.md) §3 |
| GRH / Chebotarev | Small arithmetic representatives for an independently valid certificate | A source-preserving ordinary merger and a size saving after conductor costs | Low without a new encoding; [05](05_rigidity_and_long_shots.md) §5 |

The underlying papers are identified by stable aliases in the chapters and
the [bibliography](SOURCES.md). The broadest speculative topics, including
automorphic and spectral-determinant ideas, are kept in
[05 §7](05_rigidity_and_long_shots.md#7-further-long-shots-demand-a-representation-before-investing)
as representation questions, not cited theorem applications.

## Four additional deductions worth separating from the literature

These are written arguments in this guide, checked by a second researcher.
They have not been formalized here, and no claim of historical priority is
made. The hypotheses remain part of each statement.

### 1. A faster visit theorem may be within reach

The existing band proof uses rational approximation to the rotation by
$\alpha=\log_2 3$. An effective inequality
$|q\alpha-a|\ge c q^{-\kappa}$ can force the useful rational denominator
to be large while keeping it polynomial in $\log n$. The proof sketch in
[03 §B](03_arithmetic_and_logic.md#b-linear-forms-in-logarithms-a-plausible-upgrade-to-the-band-clock)
then gives a conservative proposed entry time
$O((1+\log n)^{\kappa+1})$.

The effect is quantitative: reach the same marked section much sooner.
It does not prove that the visit is below the source, that the next return
contracts, or that cumulative valuations have favorable drift. Explicit
constants, a valid threshold, rounding, and formal integration are the
remaining bounded implementation work.

### 2. An average square bound could replace pointwise domination

Let $\rho$ keep the original source weights after first entrance, and let
$Q$ be the marked return operator killed at 1. The existing packet has a
finite fourth logarithmic moment. For
$f_j=(Q^j\rho)/\rho$, the sufficient target

$$
\|f_j\|_{L^2(\rho)}
=O\!\left(\sqrt{j+1}\,(1+\log(j+2))^{5/2}\right)
$$

would exclude a survivor that is **not eventually periodic**. A retained
positive atom visiting distinct endpoints would force a divergent total
fourth logarithmic moment. [04 §4](04_returns_operators_and_termination.md#4-a-new-lp-interface-for-the-retained-atom-budget)
gives the $L^p$ statement and the dyadic divergence argument.

This estimate is **OPEN**. It is useful because collision energy may be
more accessible to mixing methods than a uniform density ratio. Cycles
need a separate argument; the occupation-potential alternative in the
next section of that chapter is cycle-sensitive.

### 3. The predecessor/survivor comparison has an explicit exponent target

A least failed source $m$ would force every predecessor of a suitable
ternary-unit $q$ between $m$ and $2m$ to stay above $m$. The source-qualified
Lau v2 estimate would give this fixed-floor survivor set lower density at
least $D_A^{-1}(2m)^{-25/11}$. A uniform logarithmic upper-density estimate
$C m^{-\beta}$ with $\beta>25/11$ would therefore exclude all sufficiently
large least failures. Under the stronger uniform population statement
written in #180, the required threshold would instead be $\beta>1$.

[02 §3](02_analysis_and_entropy.md#3-what-the-2026-predecessor-density-results-change)
preserves the source qualification, enormous constant, finite remaining
range, and order of limits. The required power-saving fixed-floor estimate
is **OPEN**. It is substantially stronger than simply showing that the
minimum is small relative to the starting input.

### 4. Recurrence integrality can attack the complete denominator

For a fixed block schema
$W(k)=V_1^{a_1k+b_1}\cdots V_r^{a_rk+b_r}$, the full cycle candidate is
$C(k)/(2^{|W(k)|}-3^{\#1(W(k))})$. Both numerator and denominator are
fixed recurrences with roots in the positive rational group generated by
2 and 3. Corvaja–Zannier's theorem, together with the elementary fact that
a simple nonzero recurrence cannot have a nonconstant polynomial factor
and still leave a recurrence, implies a useful necessary condition:
**infinitely many integral candidates force the entire quotient to be a
linear recurrence**.

[03 §E](03_arithmetic_and_logic.md#e-integrality-of-recurrence-quotients-a-stronger-route-for-parametric-cycles)
gives the exact theorem, proof sketch, and source-access limitation.
Classifying those quotients, retaining trivial-cycle repetitions, obtaining
effective cutoffs, and covering arbitrary words are separate obligations.
This is a family-level opportunity, not a reduction of all Collatz words
to one finite list.

## Results that save agents from repeating failed approaches

- **Uniform unweighted spectral contraction is impossible.** Powers of
  two can survive arbitrarily long before entering the terminal cycle, so
  the killed shortcut operator has $\|K^t\|_{1\to1}=1$ for every $t$.
  Convergence for each fixed full-support summable law is a different goal.
- **Finite spectral success can be pure cutoff leakage.** Every finite
  killed truncation of $n\mapsto n+1$ is nilpotent, while the infinite map
  never absorbs. Keep escape mass separate from mass reaching 1.
- **The natural Subspace product already cancels the tempting saving.**
  #183 computes a nonzero integer residual after all places are included.
  A new application needs new arithmetic information, not a stronger
  citation to the same forms.
- **Positive entropy alone does not force favorable Collatz parity.**
  The 2-adic conjugacy admits biased Bernoulli invariant laws. Ordinary
  atoms and additional invariance cannot be dropped.
- **The direct affine matrices have a common invariant line.** Their
  triangular form defeats the strong-irreducibility hypothesis of the
  quoted random-matrix theorem. Independent branch sampling is also a
  different process.
- **Termination and coverage are separate.** A rewrite subsystem can
  terminate by becoming stuck. The stuck ordinary sources still need
  smaller valid partners or another convergence implication.
- **A tiny error is not an absent counterexample.** Small total residual
  mass can retain one ordinary atom indefinitely; the relevant norm or
  occupation estimate must exclude that possibility.
- **A finite witness at every depth need not have one ordinary source.**
  The accepted extraction and completion-ghost results should be used as
  adversarial tests for compactness, automata, and p-adic arguments.

Proofs, source pins, and scope limits for these points are in the linked
chapters. These are objections to specified implementations, not claims
that their entire mathematical fields are irrelevant.

## Assigning the next round of agents

The [fourteen task cards](06_agent_tasks.md) give exact outputs and stop
rules. A balanced first wave is:

1. **Analytic audit:** freeze and reconstruct the #180 joint clock/offset
   implication, then write the weakest useful fixed-floor survivor target.
2. **Arithmetic implementation:** instantiate the logarithmic separation
   theorem and formalize the proposed band-clock upgrade conditionally.
3. **Transport:** derive the exact weighted collision identity for repeated
   returns and determine what arithmetic estimate would control its tail.
4. **Certificates:** choose one blocked normal-form family, prove actual
   ordinary merger semantics, and test composed size-change constraints.

A second wave can tackle one full-denominator recurrence family and one
high-risk representation problem. The deliverable from a failed attempt
should be a preserved counterexample, a precise missing hypothesis, or a
no-go theorem for that representation. “The calculation became hard” is
less useful than identifying the invariant or source information it lost.

## Evidence and maintenance

| Label | Meaning in this guide |
|---|---|
| Literature theorem | A cited primary theorem, used only within the stated hypotheses and inspected scope |
| SOURCE-QUALIFIED | A recent manuscript, repository argument, or statement verified through a narrower access route; acceptance/replay is not silently upgraded |
| PROPOSED deduction | An argument supplied here for independent proof checking or formalization |
| OPEN target | A named estimate or structural bridge that has not been established |
| Long shot | A potentially useful representation project with substantial missing prerequisites |
| Refuted implementation | A specified inference contradicted by an exact obstruction; not a universal impossibility statement |

The source manifest distinguishes full-text theorem inspection, indexed
primary statements, author expositions, and abstract-only leads. It also
retains corrections and version dates. This is a deep research map, not a
complete independent proof audit of every cited paper.

Refresh source PRs before extending them. Preserve full SHAs and narrow
declaration scope in the follow-up. In particular, #183's newest four Lean
scripts were pending compiler replay at the frozen head; earlier successful
replays do not certify that continuation. The main errata and integration
boundaries continue to govern accepted repository claims.
