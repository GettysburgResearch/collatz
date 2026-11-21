# Task cards for the next agents

**Status: OPEN research targets, not a proof program whose missing steps are routine.** These cards specify bounded deliverables, useful negative outcomes, and the additional coverage needed for a global conclusion. Priority measures fit to the present repository and clarity of the first output; it makes no claim of historical novelty or likelihood of solving Collatz.

Start with [the precise interfaces and frozen source heads](01_problem_interfaces.md). Use its shortcut map, marked set, actual first entrance $E$, first positive return $R$, and killed pushforward $Q$. Preserve original-source weights $\mu=\sum n^{-4}\delta_n$, $\rho=E_*\mu$.

**Evidence boundary.** PR180's joint-clock and uniform predecessor arguments are written analytic claims at the pinned head, not independently replayed Lean theorems. PR183's newest four scripts are reported pending compiler replay. The recent Mazur, Lau, and Shaik papers retain the version and verification qualifications in the analytic chapter; this guide did not rebuild their reported formalizations. An agent importing any result must record its exact statement, version, clock, measure, and evidence status.

## T01 — Audit the existing joint-clock population argument

**Priority: immediate audit. Input:** PR180 at the pinned head, Tao v7, and the joint distribution of total valuation $A$ and Syracuse offset. Read [analysis §2](02_analysis_and_entropy.md).

**Deliverable:** a theorem dependency ledger for the claimed uniform lower count $cX/q$ when $X\ge Cq$, $3\nmid q$. Track central-clock probabilities, Fourier summation, inverse integrality, source-height windows, and removal of duplicate ordinary sources. Check the stronger renewal estimate actually used; do not substitute an objection to marginal mixing for review of the joint argument.

**Stop rule:** name the first estimate whose available error exceeds the selected clock cell or whose probability law changes without justification.

**Payoff/failure:** success supplies a reusable, source-qualified population input. Failure identifies one repairable lemma. Neither outcome supplies the survivor upper bound, and this audit must not be advertised as inventing joint-clock mixing.

## T02 — State and attack the fixed-floor tail contract

**Priority: immediate specification, difficult estimate. Input:** $E_M=\{n:\min_jT^j(n)\ge M\}$, plus either Lau v2 or an audited T01. Read [analysis §3](02_analysis_and_entropy.md).

**Deliverable:** an explicit conditional theorem comparing $\overline d_{\log}(E_M)\le C M^{-\beta}$ with a least failed source $m$. Its orbit supplies a ternary-unit odd target $q\in[m,2m]$. A strict exponent advantage suffices: $\beta>25/11$ using Lau, or $\beta>1$ using PR180's stronger uniform claim. Compute the resulting finite cutoff with every constant retained.

**Stop rule:** no moving floor $M=M(X)$, changed order of limits, or uncontrolled floor-dependent constant.

**Payoff/failure:** a proved uniform upper tail beyond the threshold would exclude sufficiently large least failures, leaving an explicit finite obligation. A weaker bound quantifies exactly the exponent or constant gap; almost-all descent to a diverging threshold does not fill it.

## T03 — Build one survivor inequality certificate with overflow

**Priority: high. Input:** interface I3, the finite inequalities architecture of Krasikov–Lagarias, and original-source first-passage bookkeeping. Read [analysis §§4–5](02_analysis_and_entropy.md).

**Deliverable:** one small rational certificate for marked survivors, retaining residue, height, clock, collision multiplicity, and an explicit overflow state. State whether its output targets the cofinal admissible scales of #176 or every sufficiently large octave required by #180. Export a checker independent of the optimizer.

**Stop rule:** restore all omitted transitions before accepting contraction; do not normalize away escaped mass.

**Payoff/failure:** success proves an upper bound on exactly the represented population. It closes I3 only with the required scales and universal coverage. An infeasible system or dual obstruction should identify which carry, history, or boundary coordinate prevents this abstraction from paying for survivors.

## T04 — Compute retained-source collision energy

**Priority: high. Input:** $\rho$, its finite fourth logarithmic moment, and $f_j=(Q^j\rho)/\rho$. Read [operators §4](04_returns_operators_and_termination.md).

**Deliverable:** exact one- and two-return formulas for
$$
\|f_j\|_2^2=\sum_m\frac{(Q^j\rho)(m)^2}{\rho(m)},
$$
with source pairs, collisions, and a certified infinite-tail remainder. The OPEN all-time target is $\|f_j\|_2=O(\sqrt{j+1}(1+\log(j+2))^{5/2})$.

**Stop rule:** no independent-sample replacement, dropped small denominators, or tail estimated from fresh endpoint weights.

**Payoff/failure:** the all-time target excludes survivors whose return endpoints are all distinct, by the retained-atom budget. It does not exclude eventual cycles. A failed one-step or preserved-norm inequality refutes that particular estimate. A proved persistent lower bound exceeding the target would rule out this asymptotic approach; large early finite values alone do not. Preserve the collision mechanism to show what extra arithmetic information is missing.

## T05 — Seek a cycle-sensitive occupation certificate

**Priority: high, strong hypothesis. Input:** the killed operator and an exact guarded state space. Read [operators §5](04_returns_operators_and_termination.md).

**Deliverable:** a finite nonnegative potential $V$ with a proved positive cost per completed block. The global target is $Q^*V\le V-1$ off $1$, with $\langle V,\rho\rangle<\infty$. For a restricted first result, identify uncovered exits and charge them explicitly.

**Stop rule:** average residue drift is insufficient; a block cannot assume the future absorption it is meant to prove.

**Payoff/failure:** a universal certificate rules out cycles and escaping survivors. Its occupation bound includes initial mass at $1$: $\sum_j\|Q^j\rho\|_1\le\rho(\{1\})+\langle V,\rho|_{m\ne1}\rangle$. A failed template locates a genuine positive-debt transition; it does not disprove existence of another potential.

## T06 — Preserve the unsafe residual through composition

**Priority: high. Input:** #183's $Q\rho\le8\rho+\varepsilon$, actual clock-resolved operators $Q_k$, and endpoint fiber weights. Read [operators §§2–3](04_returns_operators_and_termination.md).

**Deliverable:** a cone or weighted norm in which one nontrivial safe/unsafe composition has a verified bound, including its residual and logarithmic moment. State all closure hypotheses before using renewal or spectral results.

**Stop rule:** a small $\|\varepsilon\|_1$ is not a bound on $\varepsilon(m)/\rho(m)$; geometric resummation with factor $8$ does not establish a useful recurrence envelope.

**Payoff/failure:** success produces infrastructure for T04 or T05 rather than absorption by itself. Failure identifies whether endpoint concentration, moment growth, or lack of invariance prevents iteration. Keep the offending packet as a reproducible counterexample.

## T07 — Make the improved band clock explicit

**Priority: high bounded theorem. Input:** the actual steering proof and an explicit lower bound $|q\log_2 3-a|\ge c q^{-\kappa}$. Read [arithmetic §B](03_arithmetic_and_logic.md).

**Deliverable:** first prove a conditional entry theorem with symbolic $c,\kappa$, then instantiate a correctly transcribed two-logarithm estimate. Track the grid denominator, accumulated phase error, threshold $4N^2\le n$, decreasing restarts, even prefix, and conversion to shortcut clocks. The proposed conservative target is $O((1+\log n)^{\kappa+1})$.

**Stop rule:** do not call this logarithmic time without a stronger argument, or import an irrationality estimate for only one logarithm.

**Payoff/failure:** success upgrades entry to a polynomial in bit length and may sharpen merger budgets. It does not make the endpoint smaller. Report whether constants and downstream source-relative inequalities make the improvement useful; an enormous effective threshold remains legitimate but limited.

## T08 — Classify one fixed-block recurrence quotient

**Priority: high bounded family. Input:** fixed legal blocks $V_i$ and $W(k)=\prod_i V_i^{a_i k+b_i}$. Read [arithmetic §E](03_arithmetic_and_logic.md).

**Deliverable:** exact complete cycle numerator $C(k)$, denominator $D(k)=2^{|W(k)|}-3^{\#1(W(k))}$, and their recurrence roots. Independently check the proposed simple-denominator corollary of Corvaja–Zannier, then classify possible recurrence quotients, signs, integrality, physical parity, and trivial-cycle repetitions.

**Stop rule:** do not assume quotient roots remain in the original root group. The source statements were inspected with restricted full-proof access; obtain the needed proof before relying on a delicate extension.

**Payoff/failure:** success handles an infinite specified family with the whole denominator retained. It gives no finite family covering all cycles. Ineffective finiteness must remain distinct from an exhaustive computable search.

## T09 — Compress a restricted carry into fixed-rank arithmetic

**Priority: medium, after selecting a family. Input:** exact affine carries and finitely many geometric blocks. Read [arithmetic §§C–F](03_arithmetic_and_logic.md).

**Deliverable:** an S-unit equation with fixed term count and group rank, or a pair of fixed torus polynomials yielding a genuine divisibility contradiction. List every vanishing-subsum or exceptional-subtorus case and its ordinary interpretation. For any Subspace application, include all places, heights, determinants, and the fully simplified product.

**Stop rule:** stop if term count grows with orbit length, a carry with unrestricted prime factors is called an S-unit, or the normalized local product is merely a nonzero integer times the baseline height power.

**Payoff/failure:** success classifies the chosen architecture. Failure documents the exact source of unbounded complexity; it does not refute S-unit or Subspace methods in different representations.

## T10 — Connect size-change termination to source-bounded mergers

**Priority: high. Input:** #177 guarded gap rules, #183 blocked normal forms, and #184's source-bounded merger interface. Read [operators §§8–12](04_returns_operators_and_termination.md).

**Deliverable:** one finite compositional constraint system with an unbounded context parameter, a sound size-change or transition-invariant certificate, and ordinary merger witnesses for its terminal cases. Preserve the inequality $x<n$ for original input $n$, not merely $x<E(n)$.

**Stop rule:** finite unions of well-founded relations must cover the required transitive closure; termination by becoming stuck is not successful coverage.

**Payoff/failure:** success settles a guarded comparison family. Global closure additionally needs every required source to enter a covered successful case. A failure should return the shortest blocked grammar pattern or an abstract cycle together with exact arithmetic realizability obligations.

## T11 — Give entropy inverse theory an executable interface

**Priority: medium exploratory. Input:** two blocks of selected inverse words, their joint law, multiplier, and offset. Read [analysis §6](02_analysis_and_entropy.md).

**Deliverable:** specify the ambient real or residue space, scales, actual convolution, and a quantitative dependence error. Compute one exact finite example where low entropy growth can be classified as a carry relation, concentration cylinder, or repeated affine map. State how either outcome would affect T02 or T03.

**Stop rule:** correlated sums are not independent convolution; a real-line theorem is not automatically a theorem modulo $3^r$.

**Payoff/failure:** success establishes a usable expansion-or-structure lemma for its stated law. It does not classify all survivors. Failure is valuable if it isolates the conditioning cost or missing nonconcentration hypothesis rather than simply reporting that histograms look structured.

## T12 — Construct a genuine rigidity factor, or prove this encoding cannot

**Priority: disciplined long shot. Input:** accepted centered/adelic charts and their errata. Read [rigidity §§1–3](05_rigidity_and_long_shots.md).

**Deliverable:** a compact connected abelian solenoid with finite-rank dual, two explicit commuting automorphisms, an ordinary-source map, and the proposed invariant joining. Check the chosen theorem's exact irreducibility and non-virtually-cyclic hypotheses, entropy, and the meaning of any zero-entropy factor.

**Stop rule:** the two direct Collatz branches do not commute; their triangular matrices are reducible. An added generator needs a source-preserving interpretation.

**Payoff/failure:** one rigorous factor or invariance lemma would justify further specialist work. A no-go theorem for the chosen encoding prevents misuse. Include the biased Bernoulli 2-adic law as a control: positive entropy alone neither forces fair parity nor gives mass to ordinary integers.

## T13 — Certify the infinite tail before interpreting finite spectra

**Priority: mandatory for operator experiments. Input:** an exact cutoff operator, norm, killed set, and original atoms. Read [operators §§1, 6–7](04_returns_operators_and_termination.md).

**Deliverable:** separately account for absorption at $1$, retained mass, and mass crossing the upper cutoff; prove the tail estimate uniform in the required cutoff/time regime. Run the nilpotent truncated shift and the surviving point-mass controls.

**Stop rule:** neither tiny finite eigenvalues nor a stable normalized survivor profile proves vanishing total survivor mass.

**Payoff/failure:** success validates a particular limiting operator argument. Failure proves only that this truncation or norm cannot support the proposed inference. Record whether the obstacle is genuine outward transport, lack of uniformity, or omission of ordinary atoms.

## T14 — Test finite closure under the two arithmetic scales

**Priority: medium bounded representation test. Input:** finite-time basin indicators and their residue-subsequence generating functions. Read [arithmetic §§G–H](03_arithmetic_and_logic.md).

**Deliverable:** exact dependencies over a specified field for a candidate finite $2$- and $3$-Mahler system, or a proved lower bound on the dimension required by this representation. Track which information is lost under reduction modulo a prime.

**Stop rule:** finite-time plateaus do not establish all-time closure; a mixed substitution identity is not two separate Mahler equations.

**Payoff/failure:** finite closure could permit rigidity and eventual periodicity, followed by a separate Collatz-invariance argument. Growing dimension identifies a missing unbounded resource. Neither outcome follows merely from one-step finite-state computability.

## Recommended dependency order and reporting contract

Run T01 and T07 first; they have narrowly identifiable inputs. T02 can use Lau independently of T01, while its stronger threshold depends on a successful T01 audit. T13 precedes any numerical claim in T03, T04, or T06. T04 and T06 can inform T05, but a useful occupation certificate need not use them.

Run T08 and T10 in parallel on explicitly selected families; T09 should inherit such a family instead of beginning with arbitrary trajectories. T11, T12, and T14 are representation experiments: give them bounded milestones before commissioning a larger theorem import.

Each report should contain: the frozen inputs; one precise claim; exact covered sources; proof or checked certificate; first unsupported extension; and a preserved counterexample if the approach fails. Distinguish a refuted template, an ineffective family theorem, a finite verified range, and universal coverage. A failed bounded task is useful when it tells the next agent what additional arithmetic information is necessary.
