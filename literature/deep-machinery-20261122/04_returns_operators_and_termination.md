# Dynamical, operator, and termination machinery: a guide for the Collatz agents

**Status:** literature-backed research design, with explicitly labeled deductions and open bridges. No Collatz closure is claimed. The source-level statements below were checked against primary papers or author-hosted versions; the one original size-change reference and the transition-invariants reference have narrower access notes in [SOURCES.json](SOURCES.json). The proposed applications are our analysis, not claims made by those authors.

## Executive recommendation

The best immediate uses of deep dynamics are **to design the correct norm and return operator, and to diagnose missing recurrence assumptions**. The best immediate use of termination theory is **to replace a single numerical rank by a sound, compositional family of ranks with a complete coverage argument**. Neither field turns a forced visit into a forced descent for free.

| Machinery | Plain-language contribution | Best repo interface | Priority |
|---|---|---|---|
| Operator renewal / inducing | Keep the entire excursion, including how it changes the incoming distribution | Actual first-return packets, especially #183's residual | High for a narrowly stated transfer lemma; medium for a full theory |
| Weighted drift and occupation bounds | Make each surviving source spend a finite budget | Cycle-sensitive strengthening of return transport | High as a theorem target; difficult to establish |
| Size-change / transition invariants | Different quantities may decrease on different parts of a run | Guarded comparison certificates and blocked normal forms | High for compositional certification |
| Multiset and nested ranks | A large object may split into many smaller obligations without losing termination | #177's unbounded gap pumps | High, but most of this basic mechanism is already present |
| Abstract interpretation | Overapproximate all reachable states while retaining enough arithmetic | Residues plus unbounded counters and exact merger witnesses | High for counterexample-guided refinement |
| Countable-state thermodynamic formalism | Distinguish recurrence, null recurrence, and escape of weighted mass | A genuinely faithful countable return coding | Medium / long shot |
| Path-complete Lyapunov functions | Several local energy functions can jointly control all allowed products | Guarded affine macrosteps or certificate transformations | Medium after the guards are represented correctly |
| Quasi-stationarity / small-hole perturbation | Analyze the distribution of long-lived survivors | Diagnostics for exact finite truncations and a future faithful operator | Low as a direct proof route; high as a warning against normalization errors |

### The current interface, including the newer #183 continuation

The shortcut map is $T(n)=n/2$ for even $n$, and $T(n)=(3n+1)/2$ for odd $n$. The marked band is

$$
D=\{n>0:\ n\text{ odd},\ (d+1)(n-2^d)\le70\,2^d,\ d=\lfloor\log_2n\rfloor\}.
$$

The pinned #173 input supplies a visit to $D$ from every positive ordinary source. It makes the first positive return $R:D\to D$ total. It does not make $R(n)<n$; arbitrarily large first-return expansion is among the repo's obstructions. #184's useful alternatives are eventual strict return descent and a smaller ordinary or marked partner in the same forward-merger component, with the correct source-relative inequality.

Read the newer #183 continuation at `cc046e189366e7e876fc283b80459e64faa9c486`, specifically `research/literature-closing-20261121/transport/RETURN_TRANSPORT.md`, before starting another measure argument. It retains original weights:

$$
\mu=\sum_{n\ge1}n^{-4}\delta_n,\qquad \rho=E_*\mu,
$$

where $E$ is first entrance, and $Q$ is the pushforward by $R$ killed at 1. Its entrance moment is finite, $\sum_m\rho(m)(1+\lfloor\log_2m\rfloor)^4<\infty$. Its paper calculation gives $Q\rho\le8\rho+\varepsilon$, with a very small total residual mass. It explicitly does **not** bound $\sup_m\varepsilon(m)/\rho(m)$. Its distinct-atom budget rules out survivors that are not eventually periodic under an actual domination $Q^j\rho\le C_j\rho$ with $C_j=O(j\log^5j)$; repeated endpoints in a cycle need another argument. These are precise existing written interfaces, not results supplied by the outside papers below. At this exact #183 head, the four new Lean scripts are reported as pending compiler replay; the earlier replay does not certify them.

## 1. First choose what the operator must remember

**Our elementary diagnostic, before importing any spectral theorem.** Let $A=\{1,2\}$, and let $K$ push measures forward by the ordinary shortcut map while killing an orbit as soon as it enters $A$. For any positive summable weights $w_n$, put $\eta_0=\sum_{n\notin A}w_n\delta_n$. Then

$$
\|K^t\eta_0\|_1=\sum_{n\notin A}w_n\mathbf1_{\{\tau_A(n)>t\}}.
$$

The limit is zero **if and only if every positive integer enters $A$**. One direction is dominated convergence; in the other direction, a surviving source $s$ contributes its fixed positive weight $w_s$ forever. This is a legitimate route from a measure statement to all inputs because the measure gives every ordinary integer positive mass. Haar measure on the 2-adic integers does not have this property: every individual ordinary integer has mass zero there.

But a uniform spectral gap on unweighted $\ell^1$ is the wrong target. For every $t$, the source $2^{t+2}$ survives the first $t$ steps. Therefore $\|K^t\|_{1\to1}=1$, even if every source eventually converges. Pointwise or strong convergence on each initial measure can coexist with no uniform rate over all initial point masses. A weighted norm might provide a rate with a source-dependent prefactor, but it has to be justified and must include the atoms of interest.

Another exact diagnostic: the shift $F(n)=n+1$, truncated by killing above $N$, has a nilpotent finite matrix and spectral radius zero for every $N$. The untruncated shift never absorbs a source. Finite spectra by themselves do not control escape through the truncation boundary.

**Agent task:** write the transfer operator's domain, killed set, weight, and action on a singleton before calculating its spectrum. Require a uniform tail-error estimate before interpreting a family of finite matrices. Reject a “proof” whose Banach space excludes every $\delta_n$, unless there is a separate rigorous transfer from that space to these atoms.

## 2. Young towers: organizing long excursions without pretending they mix

**Mechanism.** Instead of observing every clock tick, observe returns to a chosen base. Record each excursion's duration as the height of a tower. A complicated map can then be studied through simpler return branches and the distribution of their lengths.

**Literature.** Young's 1999 construction uses a Markov tower, a reference measure, nonsingular return branches, and a uniform distortion bound expressed in separation time. Under integrability of the return time and the tower's mixing assumptions, it constructs an absolutely continuous invariant probability. Its convergence estimates apply to specified regular densities; polynomial or exponential tower-tail estimates give corresponding mixing estimates. See Sections 1.1–1.2 and Theorems 1–3, not just the paper's title. [D02](https://math.nyu.edu/~lsy/papers/mixingrate.pdf)

**Repo translation, our proposal.** The band provides a natural base and an everywhere-defined return time. A return branch can be labeled by its actual parity word, affine coefficient, correction term, source congruence, and first-return exclusion conditions. This supplies the raw excursion decomposition. It does not supply a Gibbs–Markov return map: an affine formula on a residue cell does not itself imply a full-image branch, bounded distortion of the source-weighted density, or a suitable invariant reference law.

The tempting shortcut is to combine the entry-clock bound $O(\sqrt n+\log n)$ with $n^{-4}$ source weights. That does yield a rapidly decreasing **fresh-source** entrance-time tail; for large $n$, the stated clock bound is below $5\sqrt n$, so the source mass with entrance time above $t$ is $O(t^{-6})$. This elementary observation does not provide the same tail for $Q^j\rho$, and the tail after an arbitrary number of unsafe excursions is the important one.

**Small first task:** partition actual first returns into a tractable family of congruence branches; prove a distortion estimate for the entire fiber weight of each branch, including branches omitted by the finite menu. Test whether the proposed class of densities is preserved under composition. **Stop condition:** if the proof uses the initial $n^{-4}$ tail again after a return without showing preservation of that law, the tower argument has silently restarted the source distribution.

## 3. Operator renewal: a particularly good language for #183's residual

**Mechanism.** Scalar renewal theory describes repeated waiting times. Operator renewal theory additionally remembers where each excursion ends and how it reshapes the incoming density. That extra memory is exactly what a scalar “most excursions are good” estimate loses.

**Literature.** Gouëzel's Theorem 1.1 starts with bounded operators satisfying the renewal equation $T(z)=(I-R(z))^{-1}$, summable return operators, a simple isolated eigenvalue at 1, the nondegeneracy condition $PR'(1)P\ne0$ for its spectral projection $P$, an aperiodicity condition, and a polynomial operator-tail bound with exponent greater than 1. It derives sharp asymptotics. The dynamical application additionally assumes a mixing probability-preserving Markov map, Hölder distortion, and a big-image property. These assumptions are inputs, not consequences of writing a renewal equation. [D03](https://gouezel.pages.math.cnrs.fr/webpage/articles/decay.pdf)

Melbourne–Terhesiu develop renewal theory in an infinite-measure setting. In their stated AFN-map application, regular variation of the return-time tail and a suitable invariant measure are explicit; the strongest individual-iterate limit in Theorem 1.1(a) requires tail exponent $\beta>1/2$. Their corrected version is the right source to use. [D04](https://math-ianmelbourne.github.io/papers/oprenew_corrected.pdf)

**Repo translation, our proposal.** Let $Q_k$ carry the actual original-source packets whose next marked return takes $k$ ordinary clocks. Then $Q=\sum_kQ_k$. Try to keep the two distinctions that existing estimates blur: marked fresh mass versus transported entrance mass, and safe excursions versus the residual unsafe excursions. A two-component or countably graded operator can record both without replacing the residual by fresh mass.

This is promising if exact arithmetic can establish a preserved cone or a weighted operator tail. It is less promising if the only available input is a small scalar $\|\varepsilon\|_1$: a small positive amount concentrated at a very light reference atom can have an arbitrarily large density ratio. Renewal machinery cannot repair that by summing a geometric series unless the growth factor and norm already control it.

**First target:** prove one nontrivial composition estimate for $Q_kQ_\ell$, retaining endpoint fibers and source weights, on a norm that includes the finite logarithmic moment. **Stop condition:** no spectral-gap assertion before specifying the Banach space and proving the return-operator assumptions there. A bounded first entrance and a formal resolvent identity are not that proof.

## 4. A new $L^p$ interface for the retained-atom budget

**This subsection is our elementary deduction, not an imported theorem.** It offers a potentially easier bridge to Hilbert-space estimates than pointwise domination.

Write $L(m)=1+\lfloor\log_2m\rfloor$, and retain the finite reference moment $\sum_m\rho(m)L(m)^4=K_0<\infty$. Because $\rho(m)>0$ on every marked $m$, define

$$
f_j(m)=\frac{(Q^j\rho)(m)}{\rho(m)}.
$$

Suppose one surviving source that is not eventually periodic contributes an unchanged atom $a>0$ at distinct marked endpoints $z_j$. For $1<p<\infty$, with $p'=p/(p-1)$,

$$
\|f_j\|_{L^p(\rho)}^p\ge a^p\rho(z_j)^{1-p},
\qquad
\rho(z_j)\ge\left(\frac{a}{\|f_j\|_{L^p(\rho)}}\right)^{p'}.
$$

Consequently every finite set of indices satisfies

$$
a^{p'}\sum_j\frac{L(z_j)^4}{\|f_j\|_{L^p(\rho)}^{p'}}\le K_0.
$$

The same dyadic counting argument used by the repo then excludes distinct survivors if the running maximum of $\|f_j\|_{L^p(\rho)}^{p'}$ is $O((j+1)(1+\log(j+2))^5)$. To verify the divergence explicitly, let $C_j$ be the running maximum of $\|f_j\|_{L^p(\rho)}^{p'}$ and split the indices into disjoint blocks $2^k\le j<2^{k+1}$. At least $2^{k-1}$ endpoints in each block exceed $2^{k-1}$, since all endpoints are distinct, so $L(z_j)\ge k$ there and the finite-atom inequality bounds the sum of the block contributions $a^{p'}2^{k-1}k^4/C_{2^{k+1}}$ by $K_0$. Under the stated growth envelope these contributions dominate a positive constant times $1/k$, contradicting finiteness as the number of blocks grows.

For $p=2$, the desired bound becomes

$$
\|f_j\|_{L^2(\rho)}=O\bigl(\sqrt{j+1}\,(1+\log(j+2))^{5/2}\bigr).
$$

This is not known from the present packet. It changes the analytic object worth investigating: weighted collision energy of transported packets. It allows some concentrated fibers, but demands a controlled global square sum. The operator on densities is explicit:

$$
(\mathcal Lf)(m)=\frac{\mathbf1_{m\ne1}}{\rho(m)}
\sum_{\substack{r\ne1\\R(r)=m}}\rho(r)f(r).
$$

**Why potentially useful:** arithmetic mixing techniques often provide $L^2$ information more naturally than a supremum density ratio. **Why not solved:** collisions are real, source-weighted small denominators remain, and ordinary exceptional atoms must stay in the norm. Cycles also remain outside the distinct-endpoint contradiction.

**First task:** derive exact finite-prefix collision identities for $\|\mathcal L^j1\|_2^2$, with a rigorous uncomputed-tail bound. Do not estimate this by replacing transported packets with independent samples. A bound exponential in $j$ misses the required growth scale even when its one-step constant looks modest.

## 5. Harris and Foster–Lyapunov theory: powerful, but the small set is the missing theorem

**Mechanism.** A Lyapunov function makes excursions spend energy, while a small-set condition prevents different regions from evolving as permanently separate worlds. Both ingredients are needed for the usual strong recurrence and convergence conclusions.

**Literature.** Hairer–Mattingly's Theorem 1.2 assumes $PV\le\gamma V+K$, with $\gamma<1$, and a common minorizing probability law on a sufficiently large sublevel set of $V$. It then gives a unique invariant measure and geometric convergence in a weighted supremum norm. Their assumptions and the norm are explicit in Section 1. [D01](https://www.hairer.org/papers/harris.pdf)

**Deterministic obstruction, our analysis.** For $P(x,\cdot)=\delta_{R(x)}$, a nonzero common one-step minorization over a set with several points requires their return images to agree. Randomly sampling return times changes the statement but still requires shared accessible support. The repo's newer #183 note already shows why declaring the whole marked band petite, including its fixed point 1, would force a uniform return-index bound to 1 under the proposed sampling. That would be much stronger than the available band-entry theorem.

The useful adaptation is a drift inequality for the **killed** operator. If a finite nonnegative $V$ satisfies

$$
Q^*V(m)\le V(m)-1\quad(m\in D\setminus\{1\}),
$$

then summing along a surviving orbit rules out endless survival. For $\rho^\circ=\rho|_{D\setminus\{1\}}$, integrating and telescoping gives $\sum_{j\ge0}\|Q^j\rho^\circ\|_1\le\langle V,\rho^\circ\rangle$; using the full $\rho$ adds exactly $\rho(\{1\})$ to the sum. Thus finite $\langle V,\rho\rangle$ gives a finite total occupation budget. Unlike a distinct-atom argument, this also rules out nontrivial cycles. This is an elementary conditional certificate, not a newly constructed function. Its existence may encode essentially the whole difficulty; adding integrability makes the desired packet estimate stronger still.

**First task:** seek a blockwise or piecewise $V$ on an exact enlarged state, allowing expansion inside a block but charging a verified positive cost at block completion. Permit positive defects only with a proved finite total budget. **Stop condition:** empirical negative average drift over residues does not verify the inequality along each actual source, nor after conditioning on repeated failed returns.

## 6. Countable-state thermodynamic formalism: the right vocabulary for escape, not an automatic escape exclusion

**Mechanism.** Pressure balances the number of allowed paths against their weights. With infinitely many states, mass can flee to larger and larger states. A finite-state eigenvector calculation can miss this completely.

**Literature.** Sarig's generalized Ruelle–Perron–Frobenius theory distinguishes positive recurrence, null recurrence, and transience. In the formulation of his author survey, Theorem 4.9 assumes a topologically mixing countable Markov shift, summable variations, and finite Gurevich pressure. Positive recurrence is equivalent to an eigenfunction/eigenmeasure pair with a finite normalized product; transience has a different conclusion. [D05](https://www.weizmann.ac.il/math/sarigo/sites/math.sarigo/files/uploads/tdf-survey.pdf)

Cyr–Sarig's Theorem 2.1 identifies strong positive recurrence as exactly the spectral-gap condition for weakly Hölder potentials of finite Gurevich pressure on a topologically mixing countable Markov shift, in their specified rich Banach-space sense. Thus a spectral gap is not a generic consequence of having a countable Markov description. [D06](https://www.weizmann.ac.il/math/sarigo/sites/math.sarigo/files/uploads/stability8.pdf)

A recent precise refinement is Velozo's *Pressure at infinity on countable Markov shifts* (2026). Theorem 1.3 bounds the limiting free energy of invariant probabilities converging on cylinders to a subprobability: retained mass is charged its limiting free energy, and escaped mass is charged pressure at infinity. The hypotheses include a transitive countable shift, uniform continuity, finite second variation and pressure, and an additional integrability or pressure-scaling condition. [D16](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/pressure-at-infinity-on-countable-markov-shifts/A430E984BC7C678A70FA395B9740C1BC)

**Long-shot use, our analysis:** a proved pressure gap could prevent near-maximizing invariant measures in a faithful Collatz coding from losing all their mass. But a hypothetical escaping integer orbit is not automatically a near-maximizing invariant measure. An agent would first have to turn that orbit into the required sequence of invariant measures with controlled energy. That conversion is a substantive new bridge, not a formal consequence of orbit equidistribution.

**Repo translation, our proposal.** A useful state might retain band height, a congruence cylinder, and a debt or gap parameter. A potential might charge both duration and coefficient growth. The difficult preliminary task is constructing an exact coding of the ordinary positive trajectories, not merely all finite legal parity words or their 2-adic completions. Weighting the return diagram by a convenient potential changes the equilibrium measure; it does not change which exceptional ordinary trajectories exist.

There is an additional trap: periodic-orbit pressure measures weighted returns. An infinite directed ray with no returns still supports an escaping path. Lack of cycles, low pressure on recurrent components, or a small equilibrium mass on high states therefore does not alone exclude escape. One needs control of the transient part and a transfer to each ordinary source.

**First task:** identify an induced countable graph whose edges carry exact ordinary realization data, and state the precise equivalence between its paths and integer trajectories. Then test strong positive recurrence for one explicit potential. **Stop condition:** if the graph admits spurious infinite 2-adic paths, or the useful spectral space ignores the integer atoms, the formalism has not reached the repo's all-input obligation. **Assessment:** technically deep and structurally relevant, but a long shot until the coding and weights pass these tests.

## 7. Quasi-stationarity and escape-rate perturbation: useful for survivors, dangerous as an absorption argument

**Literature.** Champagnat–Villemonais study general almost-surely absorbed Markov processes. Their Theorem 1.1 obtains uniform exponential convergence of the law conditioned on survival from two assumptions: a conditional minorization and a comparison of survival probabilities. The standing assumptions include almost-sure absorption and positive survival probability at each finite time. [D07](https://arxiv.org/pdf/1404.1349)

Keller–Liverani's small-hole theory gives first-order changes in escape rates under explicit spectral decomposition, uniform summability, and perturbation hypotheses. Theorem 2.1 assumes these hypotheses; its applications verify Lasota–Yorke-type control for specified expanding systems. [D08](https://carlangelo-liverani.github.io/Lavori/live0802.pdf)

**Repo assessment, our analysis.** A normalized survivor profile can settle down while its total surviving mass behaves quite differently. The object $Q^j\rho/\|Q^j\rho\|_1$ discards exactly the scalar that must vanish in an absorption proof. The fixed-source deterministic Collatz map also fails the probabilistic standing condition of positive survival probability at all finite times for a source known to terminate. An added noise model is a new model, not a proof about the original integers.

These theories are nevertheless good diagnostics for an exact family of truncated operators. They tell an agent to inspect long-lived conditional states, nearly invariant components, and escape through the upper boundary rather than just the leading eigenvalue. A rigorous truncation theorem would need control uniform in the cutoff and a norm that retains the relevant source atoms. The nilpotent-shift example in Section 1 should be a mandatory sanity check for any proposed limiting argument.

**First task:** report three quantities separately: mass absorbed at 1, mass still within the retained domain, and mass leaving the computational cutoff. Validate proposed norm bounds on all three channels. **Stop condition:** never classify cutoff loss as convergence to 1, and never import an almost-sure-absorption theorem whose absorption hypothesis is precisely what is being sought. **Priority:** low as direct closure, useful for preventing misleading operator experiments.

## 8. Multiset and ordinal ranks: precisely why large numerical growth need not defeat a proof

**Mechanism.** Replace a large obligation by finitely many strictly smaller obligations. The number of pieces may increase, and a naive sum may increase, while the whole collection still decreases in a well-founded ordering.

**Literature.** Dershowitz–Manna prove that the multiset extension of a well-founded order is well founded; they also treat nested multisets. The basic order permits replacing elements by finitely many smaller ones. Section 2 states and proves the theorem, and the paper applies it to rewrite-system termination. [D09](https://www.cs.tau.ac.il/~nachumd/term/ProvingTerminationWithMultisets.pdf)

**Repo translation, our assessment.** This is already close to #177's gap-multiset mechanism. It explains why a pump may increase the integer source dramatically and still be legitimate progress. The next productive step is therefore not simply to announce a larger ordinal: it is to show that every reachable unresolved comparison has an enabled move that decreases the same well-founded object, preserves ordinary legality, and transfers convergence in the required direction.

There are two separate tasks: termination of a selected rewrite policy, and completeness of the reduction from an arbitrary Collatz source to that policy. A total function returning `UNRESOLVED` proves neither successful coverage nor convergence. A theorem about all rewrites of an auxiliary term system is useful only if each arithmetic source admits the required legal representation and the normal forms have an adequate arithmetic meaning.

Nested ranks might help if an unsafe return creates a new collection of lower-level debts while strictly decreasing a higher-level resource. The higher resource must be an actual well-founded parameter; calling a phase “higher” or adding a symbolic ordinal without a verified transition inequality changes nothing.

**First task:** export the existing guarded pumps into a small proof-producing rewrite checker, with an explicit theorem for every guard and tail substitution. Identify the shortest reachable normal form where all legal rules fail. **Stop condition:** if the remaining problem is that no rule is enabled, stronger termination machinery is solving the wrong half of the problem. The useful result is the uncovered grammar and its arithmetic condition.

## 9. Size-change termination and transition invariants: alternate decreasing quantities can cooperate

**Literature.** Lee–Jones–Ben-Amram's size-change principle proves termination when every abstract infinite call sequence would force infinite descent in well-founded data. The original work supplies a graph-based analysis. Ben-Amram's corrected 2010 treatment extends this to monotonicity constraints; Theorem 4.12 reduces termination of that finite abstract system to a local test on its finite closure of cyclic constraints. Its proof uses infinite Ramsey theory to extract a repeating composite pattern. [D10](https://researchprofiles.ku.dk/en/publications/the-size-change-principle-for-program-termination/) [D11](https://arxiv.org/pdf/1005.0253)

Podelski–Rybalchenko's transition-invariant rule uses a finite union of well-founded relations containing the **transitive closure** of reachable program transitions. This gives a termination/liveness characterization and a basis for abstraction. Merely covering the individual edges by several terminating relations is insufficient. [D12](https://lics.siglog.org/2004/PodelskiRybalchenko-TransitionInvariant.html)

The underlying argument can be checked directly. For a hypothetical infinite execution, color each pair of times $i<j$ by one of the finitely many relations containing the pair of reached states. Infinite Ramsey theory gives an infinite subsequence with one color. Consecutive states of that subsequence form an infinite descending chain in a single well-founded relation, a contradiction. Covering only consecutive original times would not let us color all pairs. This explains the transitive-closure requirement without treating it as technical decoration.

**Repo translation, our proposal.** These methods can accommodate a decrease in one feature followed by an increase, provided the composed constraints force some infinite descending thread on any purported infinite execution. That is more flexible than demanding every marked return decrease one function of binary exponent and trailing-one depth. It does not contradict the repo's obstruction to those particular features: a sound abstraction using only those features may simply fail the termination test.

For #177, use variables for genuinely well-founded gap resources. For the newer #183 normalizer, use separate control locations for normalization, blocked exchange, and candidate-merger verification. Preserve an unbounded parameter for the blocked context; do not cap its length. If the certificate includes a smaller partner rather than a forward descent, the transition relation must encode the proof dependency, not pretend the partner lies on the forward orbit.

**First task:** compute composition constraints for a small verified macro-rule family and test every idempotent or cyclic abstract summary, including summaries created by alternating different families. On failure, produce the abstract cycle and determine whether it is arithmetically realizable. **Stop condition:** a Ramsey or automata theorem proves the global consequence of the correct local summaries; it does not prove those summaries or eliminate spurious behavior admitted by an imprecise abstraction.

## 10. Abstract interpretation: make the failed abstraction teach the next agent something

**Mechanism and literature.** Abstract interpretation replaces a large concrete state space by a simpler domain with sound transfer operations. Its foundational lattice/fixpoint framework is Cousot–Cousot's 1977 paper. Soundness is the essential one-way guarantee: a proved universal property of a safe overapproximation transfers to the concrete system. Failure of an analysis can arise from loss of precision. [D13](https://cs.nyu.edu/~pcousot/COUSOTpapers/POPL77.shtml)

**Repo proposal.** Combine finite residues with unbounded exact resources, rather than using only a large finite modulus. A candidate domain could store: control location; source residue modulo a selected power of 2 and 3; symbolic bit length; one or more gap variables; accumulated affine coefficient/correction; and proof obligations for merger or return guards. There is no claim that this domain is complete. Its virtue is that every approximation can be inspected.

A computed abstract cycle should be converted back into a system of exact congruences and inequalities. If inconsistent, refine the domain by the missing relation. If finitely realizable at all depths but not by one ordinary integer, retain that distinction and ask what additional boundedness invariant is required. The existing ghost examples are excellent adversarial fixtures for this refinement process.

For agents, “try a larger modulus” is not a sufficiently informative next step. Record the specific arithmetic relation the current modulus forgot. A quotient that creates false expanding cycles may need a high-bit/low-bit dependency, not more bits independently. Conversely, if arbitrarily large ordinary sources realize every finite abstract cycle prefix, a finite local refinement may be unable to close it without a new global rank.

**First task:** choose one failed certificate cell, derive its concrete transition relation, and perform one justified refinement that eliminates a demonstrably spurious cycle or proves a new guarded family. **Stop condition:** neither testing all states up to a cutoff nor saturating the abstract graph proves the abstraction is exact. The final certificate must state the inclusion direction, the reachable domain, and the bound or invariant that handles the omitted infinite tail.

## 11. Path-complete Lyapunov functions and joint spectral radius: a guarded, medium-priority experiment

**Literature.** Ahmadi–Jungers–Parrilo–Roozbehani attach multiple Lyapunov functions to the nodes of a labeled graph. Their Theorem 2.4 shows that, for a finite family of matrices, a path-complete graph and the corresponding positive continuous homogeneous Lyapunov inequalities bound the joint spectral radius. The graph must cover all relevant products; checking only a convenient collection of cycles does not suffice. [D14](https://arxiv.org/pdf/1111.3427)

**Repo proposal.** Guarded affine macrosteps can be homogenized as matrices, and different congruence or certificate states can carry different candidate potentials. This suggests exact rational or semidefinite searches for **local** certificates that an independent checker later verifies. It may discover a useful multicomponent potential even where a scalar logarithmic height fails.

There are two immediate traps. First, unconstrained switching includes impossible arithmetic sequences; in particular, the expanding odd branch can be applied forever in the matrix model even when that sequence does not represent a positive ordinary all-time source. Second, standard homogenization of $x\mapsto ax+b$ introduces a permanent last coordinate 1. The resulting matrices have eigenvalue 1, so proving their entire homogeneous vector contracts to zero is incompatible with the representation. One needs an appropriate affine/sublevel drift statement, a quotient or cone argument, or a certificate rank on a different state—not blind application of a homogeneous stability solver.

The [#181 nonpaying-exit family](https://github.com/GettysburgResearch/collatz/blob/5f03d809b4495802971211ef13ff905f741d700d/research/lean-global-target-20261121/README.md) is an especially good mandatory test. A proposed potential must handle many expanding blocks followed by an exit whose numerical source remains larger. A numerical fit that only sees easy exits provides little evidence.

**First task:** select one exact macro-rule sublanguage, make its guard automaton explicit, and search for a rational multiple-potential certificate on that restricted domain. **Stop condition:** an infeasible quadratic search refutes only that template, and a feasible search proves only the guarded language actually checked. Full coverage is an independent obligation.

## 12. Mixed-base rewriting: a published Collatz interface already close to the repo

**Literature.** Yolcu–Aaronson–Heule construct a mixed binary–ternary string-rewriting system whose termination is equivalent to Collatz; Theorem 3.17 gives that equivalence in the expanded preprint. They obtain automated termination proofs of weakened systems and prove limitations of natural matrix interpretations for a particular unary representation, even with dependency pairs. Those limitations do not exclude every mixed-base or higher-order proof method. [D15](https://arxiv.org/pdf/2105.14697) [journal version](https://link.springer.com/article/10.1007/s10817-022-09658-8)

**Repo assessment.** The newer #183 continuation already uses this connection: deleting the exchange `f1 -> 0t` permits a terminating normalizer, but a blocked erasure still needs an actual ordinary merger. Restoring the blocked exchange does not always decrease the existing rank after normalization; the packet records the small counterexample. Therefore rerunning a prover on the already solved subsystem adds less value than studying its exact blocked grammar.

Three concrete extensions remain worth trying. A dependency-pair formulation might isolate the troublesome recurring contexts. A size-change abstraction might find a descending thread across several normalizations. A richer term representation could preserve a tree of arithmetic obligations that a flat string loses. All three require a semantics theorem: an erasure that lowers a syntactic rank is not automatically a physical arithmetic edge or a valid convergence implication.

**First task:** map the complete blocked-normal-form grammar to dependency pairs with exact source-value formulas. Attach a proof of ordinary merger to each successfully discharged family. Feed failed patterns back as preserved counterexamples. **Stop condition:** no rule removal may silently drop a case required by the original source, and a reduction system that terminates by becoming stuck is useful only after its stuck forms are classified and linked to the desired arithmetic conclusion.

## Handoff: six sharply scoped tasks worth assigning

| Task | Concrete deliverable | What success would establish | What it would not establish |
|---|---|---|---|
| D-A: weighted collision energy | Exact $L^2(\rho)$ identity and finite/infinite-tail split for one or two returns | A defensible route toward the new $L^p$ transport target | The required all-$j$ growth bound |
| D-B: residual-preserving renewal | A cone or norm closed under a verified safe/unsafe macrostep composition | A reusable actual-packet estimate | Fresh-density mixing after arbitrary returns |
| D-C: occupation drift | A guarded blockwise positive-cost inequality, with summable defects proved | Cycle-sensitive absorption for its covered sources | Universal coverage without the guard theorem |
| D-D: size-change closure | Complete compositional constraint closure for one existing certificate language | Termination of that sound abstract language | Ordinary realization or coverage of every source |
| D-E: blocked grammar analysis | Exact dependency pairs and merger obligations for normal forms | A sharper algebraic description of the remaining rewrite obstruction | Merger from mere syntactic erasure |
| D-F: spectral sanity suite | Explicit shift/truncation, preserved-atom, and nonpaying-exit countermodels | Rejection of several tempting false inferences | Any empirical claim about all Collatz trajectories |

The strongest long shot here is a faithful countable return model whose arithmetic controls both distortion and escape of mass. The most practical next advance is likely smaller: a composition theorem that retains the residual, an $L^2$ estimate with source weights intact, or a new complete family in the blocked comparison grammar. These deliverables expose the exact unsupported step and remain useful even if the larger architecture ultimately fails.
