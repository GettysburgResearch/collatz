# Unrestricted closing attempts and ordinary descent comparisons

24 November 2026. **Collatz remains OPEN.** The latest pass targets a globally
least nonconverger and a universal weighted inverse-word estimate. It did not
prove the strict descent or moment decay needed to close the conjecture.
The earlier work in this checkpoint develops actual smaller ordinary
nonconvergers for infinite L/P languages, including all sixteen initial paid
headers followed by unbounded paid runs with seven-light buffers. Those
restrictions remain; these comparison theorems are not a universal solution.
The precise written and Lean boundaries are stated below.

The work continues PR192 at `d2081d1cd2410e6004eaee9f9b13c5553afaf3f4`.
Three GPT-6.2 Astra workers developed the descent, rewriting and arithmetic
lanes. They cross-reviewed the resulting arguments. The coordinating agent
reconstructed the main algebra and quantifiers, added a generic Lean proof of
delayed-transversal soundness, and incorporated PR182's new
`f5e65dbad5eaf2a5f85cde8916e91fe6e5102e67` checkpoint. Exact dependencies are
in [SOURCES.json](SOURCES.json); review scope is in [ROOT_REVIEW.md](ROOT_REVIEW.md).

## 0. The direct closing attack

The objective is to start from the globally least positive odd nonconverger m
and produce an actual positive odd nonconverger below m, with no assumption on
its future gap word. The three lanes were redirected to that objective after
the restricted comparison constructions. They also inspected the newer
PR193 `d35bdfd9d0c75effda50bbb8040c136482431e24`, PR197
`9ed095c3b3386d66c1dba103117e8dda0268b7aa`, and PR188
`f0e3cd96bab2d23791998bb92a86bf7ff2d51d4d`.

The forward-anchor route gives an actual forward value y that is the image of
a critical mark. Its least one-step odd predecessor is below m exactly when
y is 2 modulo 3 and y<(3m+1)/2. Phase steering does not supply this simultaneous
residue and absolute-height bound. The critical lift can reduce exactly back
to the original minimum, so its power-sized reduction cannot be counted as a
second gain. [Direct return attack](CENTRAL_RETURN.md).

The inverse-path route tests every ordinary inverse word, permitting arbitrary
gaps and offsets. Its exact cost inequalities retain the original floor.
For the L/P sector an explicit reciprocal budget makes these conditions hold
at every horizon of a least escaping input. The attempted classification of
all such optimal paths is incomplete. This is a necessary condition, not a
proof of descent or a reduction of all possible Collatz itineraries to L/P.
[Inverse optimization attack](CENTRAL_DESCENT.md).

The analytic route expresses the full nonconvergent mass through an explicit
shifted negative moment of independent inverse-word data. It includes cycles
as well as escape and requires no favorable language. The remaining assertion
is decay of that moment. A single fixed ordinary source has a constant exact
contribution while it survives, even when its word is exponentially rare in
the independent distribution. An average contraction or a bulk mixing theorem
therefore does not establish the required bound.
[Universal moment and attempted estimates](CENTRAL_CLOSURE.md).

## 1. A smaller start can support an expanding comparison

Use the shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd},\end{cases}
\]

and the accelerated odd map \(U(q)=(3q+1)/2^{v_2(3q+1)}\).
The two source blocks \(L=(2,1)\), \(P=(1,4)\) list successive odd-map
gaps. Their boundary equations are \(8q'=9q+7\) and \(32q'=9q+5\).
A “paid run” means consecutive P blocks in this particular alphabet.

The previous packet's finite prefix code covered thirteen of the sixteen
five-letter headers beginning with P. The residual headers were PPLLL, PLLPP
and PLLPL. The new comparison does not need to meet the original future:
it starts below the original floor and then enters a different positive
ordinary trajectory. Its later multiplier may exceed one.

For \(q_0\) followed by an initial \(L^r\), write
\(q_0+7=2^{3r+1}v\). The small start has the form
\(m=M2^{2r+\ell}v-1\). The three headers feed comparisons
\(Y=\lambda(q+7)-7\) as follows.

| Header | \(\lambda\) | \(\ell\) | Allowed tail |
|---|---:|---:|---|
| PPLLL or PLLPL | \(5583/4096>1\) | −6 | Infinite concatenations of L, \(L^K P\), and \(L^K P L^j P\), with \(K\ge4\), \(j\ne3\) |
| PLLPP | \(72873/65536>1\) | −9 | The same form, with \(K\ge5\), \(j\ne3\) |

Here \(j\ge0\) and K can change from macro to macro. For every initial
\(r\), the construction or an earlier actual paid endpoint gives a positive
odd nonconverger below \(q_0\) and, when relevant, below the first light
intermediate \((3q_0+1)/4\). Infinitely many close paid pairs are allowed.
The result rules out the globally least odd counterexample in these specified
positions and languages. It does **not** prove convergence of every source in
the language: the smaller nonconverger need not remain in that language.

The fixed five-macro core, with outer buffer six, has a Lean proof of
infinite integrality, actual target iteration, nonconvergence and original-floor
descent for \(r\ge7\). Lean also checks the direct inequalities for
\(r\le6\). The sharper buffers and all internal separations above are written
extensions with exact arithmetic certificates.
[Core theorem](DESCENT_MACRO.md) · [all-length extension](ARITHMETIC_MACRO.md)
· [Lean source](descent_macro.lean).

### Unbounded paid clusters

The strongest header result permits **every** five-letter word W beginning
with P:

\[
 L^r W\{L,\ L^7P^h\ (h\ge1)\}^{\omega},\qquad r\ge0.
\]

Every such actual infinite ordinary input yields a positive odd nonconverger
below its original boundary and, when present, its first light intermediate.
The thirteen earlier headers need no condition on their future. Three new
two-state comparisons handle the remaining headers and arbitrary paid-run
lengths. Their multipliers are 2442741/2097152, 103789/131072 and 5367/4096;
the middle one is below one. All intermediate comparisons are forced to be
ordinary integers on the given infinite source. This is an independently
reviewed written proof with exact finite arithmetic certificates. The
seven-light separation condition in the displayed tail remains.
[All-header proof](DESCENT_ALL_HEADERS.md) · [certificates](descent_all_headers.py).

A separate construction uses a shorter four-light buffer after a more
restricted initial word. It proves original-floor descent for every actual infinite
input with word

\[
 L^r PP L^sP^t\{L,\ L^4P^h\ (h\ge1)\}^{\omega},
 \qquad r\ge0,\quad s\ge6,\quad t\ge3.
\]

It uses one multiplier \(5367/4096\) and two offsets:

\[
F(q)=\frac{5367q+8897}{4096},\qquad
I(q)=\frac{5367q+2395}{4096}.
\]

An entrance, an interior P loop and a three-P exit handle every paid-run
length. Infinitely many runs can have unbounded lengths. All intermediate
comparison values are forced to be ordinary integers along the single given
infinite source. Their positive boundary values stay above two, which excludes
the \(1,2\) cycle even when long paid runs defeat an odd-count argument.
The original-floor entrance uses a different signed phase, −10, reached after
a fully specified rational calculation. This theorem is a written proof with
nine exact ordinary-word certificates, not a newly Lean-checked theorem.
[Complete proof](DESCENT_PAID_RUNS.md) · [exact controls](descent_paid_runs.py).

## 2. The sparse residual set now has a physical return dynamics

PR182 defines a decidable set S of minima of synchronized marked fibers.
It already proves, in written mathematics, that convergence on S is equivalent
to Collatz and that \(\sum_{s\in S}s^{-\theta}<\infty\), where
\(\theta=H_2(\log2/\log3)=0.9499555\ldots\). The count depends on PR193's
written translated-interval synchronization theorem. Those inputs retain
their original evidence levels.

The new equal-odd-clock calculation sharpens the mixed half-partner merger.
Both arms use exactly the same number of odd inputs. All smaller-partner
reductions of a mark in octave d can therefore be composed at the single
horizon \(R_d=(d+2)^3\), using the maximum of horizons rather than their sum.
The least marked \(s\le n\) with
\(U^{R_d}(s)=U^{R_d}(n)\) belongs to S.

Use states \((s,L)\), with settled value \(U^L(s)\). Follow that actual value
to its next positive-time mark, replace it by the canonical residual
representative, and record the new settlement delay. Successive settled
values advance strictly on **one original ordinary orbit**. Repetition of the
return state is equivalent to eventual periodicity of that source. Convergence
to one remains a separate obligation; other positive cycles are not excluded.
[Return construction](ARITHMETIC_RETURN.md) · [literal half-script counts](arithmetic_equal_clock.lean)
· [formal transversal transport](root_delayed_transversal.lean).

### A finite total cost, including every replacement path

In a nonperiodic component, assign an integer level to a source by its odd
clock relative to the original orbit, and let \(m_i\) be the smallest source
at level i. Distinct levels cannot merge at a common odd clock. PR193 therefore
applies to their entire transversal, yielding

\[
\sum_i\frac1{m_i}<\infty.
\]

Settlement intervals of the generated return process are disjoint in those
levels. For its selected mark \(n_j\), residual \(s_j\), and octaves
\(d_j,e_j\), sufficiently late replacements satisfy the exact identity

\[
A_j-B_j=d_j-e_j,
\]

where A and B are the total binary divisions on the two equal-odd-clock arms.
Moreover,

\[
\sum_j\left|\log\frac{n_j}{2^{d_j-e_j}s_j}\right|<\infty.
\]

After dyadic padding the arms thus synchronize in literal shortcut time too.
This is one total budget for the actual source and all its replacements; the
delays do not appear as a multiplying loss. The missing lower bound is real:
valid marked pairs \(2^d+3\) and \(2^{d-1}+1\) differ by just one after
padding, giving errors of order \(2^{-d}\).
[Component argument](ARITHMETIC_COST.md) · [whole-path argument](REWRITING_RETURN.md).

### The latest fixed-floor synthesis

Every member of the **entire** residual set S has \(v_2(3s+1)\le2\).
If a mark n has a larger gap, the even neighbor \(n-1\) is in its same
octave interval and same synchronized fiber, so the fiber is discarded.
Repeated quarter deletion preserves markedness and the next odd endpoint.
At a PR197 critical mark of octave d this supplies a residual representative
of size less than \(8n^{4/5}\), saving at least \((d+1)/5-2\) octaves.
No theorem yet forces a fixed forward return chain to select such critical
marks. Cofinal predecessors do not supply those visits.
[Exact deduction and new source pin](ARITHMETIC_FLOOR.md).

## 3. Effective visitation and the two ends of a rewrite

Every positive odd n reaches the marked section within

\[
O\bigl((1+\log n)^{17/4}\bigr)
\]

odd steps, and also within that order of ordinary shortcut steps. The constants
are effective but are not evaluated. This is an asymptotic visitation theorem,
not an implementation with a calibrated stopping bound. On N consecutive
states of an injective orbit, or one primitive periodic lap, the leading-phase
interval discrepancy is \(O(N^{-4/25})\), uniformly over starting sources.
Both estimates use Wu and Wang's published linear-form theorem and the stated
ordinary correction bounds. They are written proofs.

At odd macro-rewrite times on a nonperiodic positive ordinary orbit, the
limiting leading-boundary block law is the coding of an irrational rotation.
Its three boundary-rule frequencies are
\(\log_2(4/3),\log_2(5/4),\log_2(6/5)\); its positive-frequency length-r
language has at most \(3r\) words. Yet any fixed open leading-phase interval
and any prescribed finite trailing gap list occur together at arbitrarily
large sources reaching one. The construction preserves the upper and lower
logarithmic counting exponents of every eventual-intersection component.
Convergence on **any** such fixed nonempty joint cylinder would already imply
universal convergence. It does not follow that an arbitrary component admits
a specified infinite trailing language.
[Rewrite factor and cylinder theorem](REWRITING_FRONT.md) ·
[quantitative proof](REWRITING_RETURN.md) · [finite suffix kernel](rewriting_front.lean).

## 4. What the further closure attacks established

- The isolated PP ramp cannot rejoin the original endpoint after **any** number
  of following light blocks through a uniform affine word. The positive descent
  above succeeds by entering another ordinary comparison instead.
  [All-length proof](DESCENT_PAIR.md).
- For the two fixed-intercept multipliers, all pure paid-run reset lengths are
  classified: only one and two paid blocks work, regardless of light buffer.
  The two-intercept controller handles unbounded runs by changing the
  comparison's offset. [Classification and switch costs](ARITHMETIC_MACRO.md).
- Along two injective ordinary comparisons with matching odd and raw clocks,
  the logarithms of their affine multipliers have finite total variation.
  A finite palette eventually becomes constant. With arbitrary clocks, a short
  switch incompatible with the exact \(\{2,3\}\)-unit slope relation forces
  an actual small state on one segment, possibly an endpoint, by a
  three-logarithm bound. Constructing
  such a switch on two certified bad arms for every candidate remains open.
  [Source budget and local consequence](REWRITING_VARIATION.md).
- Positive inverse-basin density, rapid interval synchronization and summable
  level minima can coexist with escape for a separate explicit integer map.
  Thus those combinatorial properties alone do not prove residual recurrence.
  [Countermodel](ARITHMETIC_DENSITY.md).
- Genuine inverse ordinary paths ending at a single specified ternary-unit
  root give incoming real amplitudes of Hausdorff dimension at least one
  quarter. A unique incoming constant cannot be inferred from summability.
  [Fixed-root construction](ARITHMETIC_INVERSE.md).

## Verification and remaining target

Five new Std-only Lean files check the expanding-shadow core, literal equal-odd
clock mergers, arbitrary binary-suffix carry, generic delayed transversals,
and the exact strong-induction meeting criterion with its finite lift algebra.
The source-specific execution record identifies the fresh compiled files,
named axiom reports and exact normal/optimized arithmetic replays. Analytic
counting, equidistribution, Diophantine estimates, Hausdorff dimension and the
unbounded paid-run extension remain written mathematics. Repository validation
checks the complete checkout, not the truth of these mathematical claims.
[Execution record](../../reports/astra-high-variance-20261124/README.md).

The closing problem remains a universal one. The unrestricted shifted-moment
decay and the least-source meeting premise are both unproved. The new descent languages still
leave arbitrary overlapping clusters and short intercluster gaps. The residual
return construction has no proven recurrent finite region or universally
strict rank. The switch theorem needs a construction of its two ordinary
nonconverging arms and the requisite short incompatible switch. An escaping
source argument also cannot replace the separate obligation to exclude every
nonstandard positive cycle. No missing premise is installed as an axiom.
