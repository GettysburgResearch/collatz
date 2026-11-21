# The precise problems the machinery must solve

**Snapshot:** main at ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a, with
the exploratory heads listed below. The project remains unsolved.
This guide is a source-qualified research synthesis. It does not promote
open PRs into the accepted baseline, and it does not claim a new Lean replay.

## 1. Fix the map and the clocks

The repository uses the shortcut map

$$
T(n)=
\begin{cases}
n/2,&n\ \text{even},\\
(3n+1)/2,&n\ \text{odd}.
\end{cases}
$$

Its terminal cycle is 1 → 2 → 1. The unaccelerated map used in several
papers sends an odd n to 3n+1; its clock is different, although convergence
to 1 is equivalent. On odd positive integers use

$$
U(x)=\frac{3x+1}{2^{a(x)}},\qquad a(x)=v_2(3x+1).
$$

One U-step takes a(x) shortcut steps and a(x)+1 unaccelerated steps.
For j odd steps, A_j is the sum of the actual valuations; it is not a
fresh random variable unless a probability model has explicitly been defined.

An odd positive x is **marked** when

$$
(d+1)(x-2^d)\le70\,2^d,\qquad d=\lfloor\log_2x\rfloor.
$$

Call this set M. There is no condition modulo three in this definition.
“Ternary unit” means 3 does not divide the integer; that is a separate
condition used in inverse-population results.

For d<=69, the band contains every odd integer in that octave. Small
examples can test algebra or merger mechanisms but do not test the
asymptotically narrowing geometry.

## 2. What the band proof already accomplishes

At the pinned #173 head, the source theorem states that every positive
ordinary n has a marked iterate at a shortcut clock

$$
0\le t<4\lfloor\sqrt n\rfloor+\lfloor\log_2n\rfloor.
$$

The set M has natural density zero. The argument works on each actual
orbit: logarithmic phase is a perturbed rotation; a rational approximation
provides a finite grid; either the orbit drops below a quarter of the
current input, or the accumulated perturbation is small enough to force a
band hit. Strong induction handles the drop case.

This is why Diophantine approximation is a real connection. It is already
inside the proof, rather than being suggested because Collatz contains powers
of 2 and 3. The arithmetic chapter proposes a stronger quantitative
replacement for the elementary separation bound.

What the theorem does not establish is equally specific. A band hit can
lie above the original input. A first positive return can expand by an
arbitrarily large factor. Reducing the logarithmic identity modulo one
discards the integer valuation sum that governs height drift:

$$
\log_2 U(x)-\log_2x
=\log_2 3-a(x)+\log_2\!\left(1+\frac1{3x}\right).
$$

Therefore leading-phase equidistribution is compatible with insufficient
division by two. A successful next argument must recover this information,
find a smaller merger partner, or eliminate the entire survivor population.

**Source:** [#173 README](https://github.com/GettysburgResearch/collatz/blob/fa0c9e2a2851e6324391e39c17afcb5913185aec/research/lean-shell-cover/README.md),
with the declarations identified below.

## 3. Five exact interfaces

These are alternatives and partial research targets, not five obligations
that every proof must satisfy.

### I1 — eventual descent under the actual return map

Let E(n) be first entrance into M, allowing time zero. Let R(m) be the
first **strictly positive** marked return from m. The entry theorem makes
R total.

The repository proves the equivalence

$$
\mathrm{Collatz}\iff
\forall m\in M,\ m>1,\ \exists k\ge1:\ R^k(m)<m.
$$

This concerns some later return, not necessarily the first. A theorem about
arbitrarily large contracting examples does not cover each prescribed m.
A theorem about a freely selected inverse ancestor does not automatically
control R.

**Best machinery candidates:** source-aware block drift, occupation
potentials, and valuation/phase coupling. Better entry clocks are useful
infrastructure but do not directly settle I1.

### I2 — a lower ordinary component representative

The marked version in #184 is

$$
\forall m\in M,\ m>1,\quad
\exists y\in M,\ 0<y<m,\ \exists a,b\ge0:
T^a(y)=T^b(m).
$$

This is again equivalent to full convergence. The smaller y need not occur
on the forward trajectory of m; the two trajectories may merge later.
Strong induction on marked values is what makes the comparison useful.

An original-source version starts from arbitrary n>1 and its first mark
q=E(n). It requires a positive x<n whose forward trajectory merges with q.
The inequality must be below **n**, because q can be much larger.
A saving only below q is not enough for induction on n.

The exact splice machinery already constructs partners from alternative
inverse histories. The unresolved step is universal selection of a legal
history meeting the strict saving inequality.

**Best machinery candidates:** complete guarded rewrite systems,
size-change and multiset ranks, restricted S-unit/recurrence families,
and arithmetic constructions that preserve the supplied source.

**Source:** [#184, sections 2 and 5](https://github.com/GettysburgResearch/collatz/blob/366dab89ee9548084ab9b5e4e90ff82abf287a20/research/lean-band-coupling-20261121/README.md).

### I3 — beat a known predecessor population

In #176, call Q>=16 admissible if some integer a coprime to Q satisfies

$$
|Q\log_2 3-a|\le1/Q.
$$

Admissible scales are cofinal. Each positive ternary-unit target q<=2^Q
has at least 2^Q distinct marked odd predecessors x with

$$
2^Q\le x<2^{10Q},\qquad
T^{k_x}(x)=q,\qquad 7Q-5\le k_x<11Q.
$$

The clocks k_x vary. Define S_Q(t) to be the marked positive inputs below
2^(10Q) which have not hit 1 through shortcut clock t. The exact sufficient
finite certificate is |S_Q(t)|<2^Q, and the packet proves

$$
\mathrm{Collatz}\iff
\forall K\ \exists Q\ge K\text{ admissible}\ \exists t:
|S_Q(t)|<2^Q.
$$

The upper survivor count is open. This route handles hypothetical cycles
as well as escaping orbits.

The analytic #180 alternative uses much denser predecessor populations
inside selected octaves. Under its explicit analytic population input,
with V_d(t) counting unresolved marked starts in octave d, its criterion is

$$
\exists d_0\ \forall d\ge d_0\ \exists t:
(d+1)^3 V_d(t)<2^d.
$$

Here the survivor upper bound must hold on **every sufficiently large
octave**. An arbitrary unbounded subsequence does not necessarily meet the
target-dependent octaves supporting the lower bound.

**Best machinery candidates:** selected-law Fourier estimates,
original-source first-passage inequalities, and exact inequality
certificates with overflow retained.

**Sources:** [#176 section packet](https://github.com/GettysburgResearch/collatz/blob/3dbe5542fd6a5a1d63b354225d92391471c17002/research/lean-global-resolvent-20261121/section/README.md);
[#180 population criterion](https://github.com/GettysburgResearch/collatz/blob/cf91e46fa9fbadba3df7942202a5197c134d0ce0/research/lean-forward-band-20261121/README.md).
The latter analytic population theorem is a written, source-qualified
argument, not a theorem this review has compiled in Lean.

### I4 — make a full-support source law lose all surviving mass

Use

$$
\mu=\sum_{n\ge1}n^{-4}\delta_n,\qquad \rho=E_*\mu.
$$

The weight belongs to the original n. If many inputs share E(n), their
weights add; they are not replaced by the endpoint's fourth inverse power.

Let Q push marked mass along R and kill it at 1. Then

$$
\|Q^j\rho\|_1\longrightarrow0
$$

would imply full convergence: every failed original source would retain
its own strictly positive mass forever. The converse follows by dominated
convergence. This elementary equivalence explains why a measure argument
can prove an all-input statement when its reference law contains every
ordinary atom.

The newest #183 continuation obtains an entrance moment and studies
retained transport. Its displayed inequality Qρ<=8ρ+ε has a small total
residual, but its factor 8 is expansive, and no suitable pointwise control
of ε/ρ is supplied. A small total residual is not zero and can contain a
hypothetical exceptional source.

Its recurrence envelope controls survivors that are **not eventually periodic**; a cycle needs
another argument. The dynamics chapter supplies two further conditional
interfaces: an L^p retained-atom bound and a cycle-sensitive occupation
potential. Neither required estimate is established here.

**Best machinery candidates:** operator renewal on a preserved weighted
space, collision-energy estimates, and exact occupation certificates.

**Source:** [#183 latest transport note](https://github.com/GettysburgResearch/collatz/blob/cc046e189366e7e876fc283b80459e64faa9c486/research/literature-closing-20261121/transport/RETURN_TRANSPORT.md).
At this exact checkpoint the four new Lean scripts are reported as
**pending compiler replay**. The earlier successful replay does not certify
them. Written deductions and source-reported proofs retain that boundary.

### I5 — ordinary realization and full denominators

The older research programs remain relevant. A compatible infinite parity
history determines a 2-adic point, but not necessarily one positive
ordinary integer. In the accepted extraction result, nested nonempty
positive survivor sets have a common ordinary element exactly when their
least elements remain bounded. Finite witnesses can change with depth.

For a periodic shortcut parity word w of length L and odd weight s,

$$
T^L(x)=\frac{3^s x+C_w}{2^L},\qquad
x=\frac{C_w}{2^L-3^s}.
$$

The whole denominator, sign, positivity, and physical parity replay must
be retained. Eliminating proper factors or proving arbitrarily many finite
congruence conditions is insufficient.

**Best machinery candidates:** fixed-rank S-unit equations,
recurrence-quotient integrality, torus gcd bounds, restricted
p-adic interpolation, and exact symbolic language classification.

**Sources:** [ordinary extraction](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/integrated/ordinary-extraction/README.md);
[periodic tails](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/integrated/periodic-tails/README.md).
The main errata keep the combined periodic-synthesis review boundary
separate from its exact component identities.

## 4. A translation table that prevents expensive wrong turns

| A source establishes | An agent must not silently substitute |
|---|---|
| Almost every input under Haar measure on the 2-adics | Every positive ordinary integer |
| Almost every input reaches a threshold tending to infinity | Almost every input reaches 1 |
| A predecessor population lower bound | A forward survivor upper bound |
| A fresh-source tail or drift estimate | The same estimate after arbitrary failed returns |
| Leading logarithmic phase equidistribution | A favorable average of v_2(3x+1) |
| A selected contracting family | A partner for each prescribed source |
| A finite legal word at every depth | One ordinary integer realizing all depths |
| A fixed-dimensional Diophantine theorem | A theorem uniform in the number of carry terms |
| A well-founded rank on covered rules | Coverage of every required comparison |
| A negative average random-matrix exponent | Decrease on every legal deterministic product |
| A spectral gap in a finite truncation | A gap for the infinite operator with escape retained |
| A compiler or repository integrity pass | Independent mathematical acceptance |

## 5. Source pins and read-first files

All links below are frozen. The machine-readable companion lists the
inspection and evidence limits.

| Source | Full head | Read first / named interface |
|---|---|---|
| Main | ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a | AGENTS; research map; integrated index; scoped errata; source/extraction/transport packets |
| #173 | fa0c9e2a2851e6324391e39c17afcb5913185aec | ForwardSection.bounded_visit; SectionDynamics.collatz_iff_return_descent; RisingReturns |
| #175 | 06215e69346c4d32bf970af9c846a6894586c1e7 | BAND_ATTACK: limits of ranks using exponent and trailing-one depth |
| #176 | 3dbe5542fd6a5a1d63b354225d92391471c17002 | section/README; BandCriterion; CountCriterion |
| #177 | 00a611094043afeb256d6532b477c0709e8ed270 | UNBOUNDED_GAP_REWRITES; CollatzGapComparison.Complete remains open |
| #180 | cf91e46fa9fbadba3df7942202a5197c134d0ce0 | JOINT_CLOCK_MIXING; GLOBAL_RENEWAL_ATTACK; analytic population bounds |
| #181 | 5f03d809b4495802971211ef13ff905f741d700d | lean-global-target: nonpaying-exit families and guarded repayment |
| #182 | 8372e302041a55057742a9e6ee9b4fa600c88fdb | InfiniteDescent; PHASE_FREQUENCY |
| #183 | cc046e189366e7e876fc283b80459e64faa9c486 | literature-closing continuation: transport, arithmetic product audit, blocked normal form |
| #184 | 366dab89ee9548084ab9b5e4e90ff82abf287a20 | ClockSteering; SourceBoundedMerge; LowerMarkedMerger |
| #166 | 5996b9f525ca50978bc34f423192c36a87765bf3 | GRH_INTERFACES: representative selection versus source-preserving descent |

A future agent should refresh a source PR before extending it, preserve the
full head used in its own note, and review any changed claim at the narrow
file/declaration level. Do not copy “latest” from this dated guide.
