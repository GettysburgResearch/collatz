# Focused forward attempt: exact root bounds and merger return guards

**Outcome: Collatz remains OPEN.** This follow-up pursued a full ordinary-source
argument through the three-ray merger, five-ray merger, and all-word inverse
potential routes. It obtained the scoped results below, but no universal
forward descent, unrestricted merger theorem, or exclusion of every escaping
orbit. The unresolved implications are stated next to the results.

This packet is additive to [the preceding investigation](../2026-11-20-ordinary-bridge/README.md).
Its scientific content was published at
`8f50cd6f61d59ff2cf5547604dd6a28349bd19af`, following the frozen starting
head `6ff18e4f63be8f3bece76215fcfe44d83b001d7f`. Earlier proofs, certificate bytes,
and review hashes have not been revised by this follow-up. Publication and
execution details are recorded separately in [VALIDATION.md](VALIDATION.md).

## 1. All legal inverse words through depth 2,000

For positive odd integers prime to three, use the odd map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

and every legal inverse letter \(I_a(z)=(2^az-1)/3\), with unit states at
every stage. A word of length \(k\) and exponent sum \(A\) has score
\(8k-5A\). Let \(W_N(1)\) be the maximum of zero and the scores of all
such words from `1` of length at most \(N\).

The new elementary height theorem H1 gives the exact finite formula

\[
W_N(1)=\max\left(\{0\}\cup
\{8h(m)-5A_*(m):m\le H_N,\ m\text{ an odd unit},\ h(m)\le N\}\right),
\]

where \(h(m)\) is the first odd hitting time of `1`, \(A_*(m)\) is its
actual division-exponent sum, and

\[
H_N=\left\lfloor\sqrt[5]{\left\lfloor
\frac{256^N-1}{2\cdot243^N}\right\rfloor}\right\rfloor.
\]

There is **no imposed inverse-exponent cap**. A positive-score word must
satisfy \(3^km<2^A\) and \(5A\le8k-1\); these force the displayed ordinary
height bound. Reversing a word gives its actual first-hit path followed,
possibly, by root loops of score `-2`. Removing those loops cannot lower the
score. This proves the exact reduction, rather than extrapolating it from
sample paths.

The completed depth-2,000 run has:

| Quantity | Exact result |
| --- | ---: |
| Ordinary height cutoff | 984,624,609 |
| Odd unit candidates | 328,208,203 |
| Candidates reaching `1` within the horizon | 328,208,203 |
| Maximum first-hit odd depth | 364 |
| Maximum first-hit division-exponent sum | 607 |
| Maximum score, including zero | 0 |
| Maximum nonroot score | -12, at 5 |

Thus the certificate establishes **\(W_{2000}(1)=0\)**. It does not assert a
new record for the largest Collatz starting value verified. The original
large run is preserved in a JSON receipt; an independent reviewer rebuilt
the matching executable, checked the cutoff by a separate integer-root
method, and compared the C++ implementation with uncached arbitrary-integer
Python on smaller scopes. Those are distinct execution events.

H2 transfers a finite root certificate along an actual terminating path,
with the horizon reduced by the path length. H3 identifies the additional
content of a hypothetical infinite root bound: if \(W(1)\le B\), then every
terminating odd unit obeys a uniform logarithmic first-hit bound

\[
h(m)\le\frac5\delta\log_2m+
\frac5{9\delta}\log_2(1+\log_2m)+O_B(1),
\qquad \delta=8-5\log_2 3>0.
\]

The cutoff grows with \(N\). There is no bound here on the later finite
maxima, so \(W(1)<\infty\) remains unproved. Even root finiteness would
need an additional argument covering any hypothetical component outside the
basin of `1`.

[Proof and reproduction](../../research/focused-forward-20261120/pressure/README.md)
· [Independent audit](../../research/focused-forward-20261120/pressure/AUDIT.md).

## 2. A finite all-action potential must oscillate at every large scale

Suppose a finite nonnegative function \(V\) on all positive odd units satisfies
**every** legal inverse inequality

\[
V(z)\ge8-5a+V(I_a z).
\]

Define the largest downward change between arguments within a factor of 16:

\[
D_{V,16}(X)=\max_{u\le v\le\min(16u,X)}(V(u)-V(v)),
\]

where both arguments are odd units. The elementary O1-local and O2 arguments
prove

\[
\limsup_{X\to\infty}\frac{D_{V,16}(X)}{\log_2X}
\ge\frac8{\log_2 3}-5\approx0.047438,
\]

and the stronger frequency statement

\[
D_{V,16}(X)\ge\beta_{12}\log_2X-O_V(1),
\qquad
\beta_{12}=\frac{3\sum_{j=1}^{12}(\log_2 3)^{-j}-5}{13}
\approx0.00831750>\frac1{125}.
\]

The two coefficients have different quantifiers: the larger one is a limsup;
the smaller one holds at every sufficiently large height. The proof compares
long inverse exponent-one words with one-step ancestors of `1`, using only
ordinary integers and exact legal edges.

This excludes nearly monotone potentials and potentials with sublogarithmic
downward variation. It does not rule out irregular potentials under a
logarithmic upper envelope, construct a finite potential, or establish
finiteness of \(W\) at a fixed ordinary input.

[Full proof and precise hypotheses](../../research/focused-forward-20261120/pressure/PROOF.md).

## 3. Three-ray mergers: genuine smaller obligations and exact repetition limits

Write \(C(n)\) for the assertion that \(n\) and \(3n\) eventually meet, with
independent clocks, under the ordinary shortcut map. The pinned PR #146
reduces full Collatz to universal \(C(n)\). The new return proofs themselves
use only actual ordinary paths.

For \(n=2^ku-1\), \(k\ge3\), \(u\) odd, set \(R=3^{k-1}u\). At clock \(k\),
the two endpoints are \(3R-1\) and \(R-1\). If \(R\equiv3\pmod4\), they merge
two steps later. If

\[
\frac{R-1}{4}=2^{2r+1}m,\qquad m\text{ odd},
\]

explicit further paths instead give

\[
C(n)\quad\Longleftrightarrow\quad m\sim3^{r+1}m.
\]

Whenever \(3^rm<n\), this reduces the source to the smaller obligations
\(C(m),C(3m),\ldots,C(3^rm)\). These are concrete arithmetic guards.
The condition is not presumed for a class where it fails.

In the special return \(m=(R-1)/8\), valuations `3` through `7` always
decrease the source, whereas valuations at least `8` always increase it.
For every prescribed periodic block of expanding valuations, TR-004 gives
an exact formula for the maximum number of complete repetitions from a
fixed ordinary source. Therefore an infinite expanding run cannot have an
eventually periodic valuation schedule. A bounded alphabet also forces an
explicit linear lower bound on its factor complexity.

Every finite valuation list is nevertheless realizable by some positive
ordinary source. The source changes with the list. Finite admissibility,
periodic exclusions, and negative rational fixed completions cannot identify
one positive integer realizing or avoiding an infinite variable schedule.

Two separate interface results explain failed shortcuts: a fixed binary
cylinder merger for a convergent pair `(n,3n)` requires a precise grade
difference, and an aligned ray-to-ray inverse diagram can only preserve the
odd part by doubling. Neither result excludes a more general merger diagram.

[Proofs and checker](../../research/focused-forward-20261120/three-ray/README.md)
· [Independent review](THREE_RAY_REVIEW.md).

## 4. Five-ray mergers: the counting and return gaps are explicit

For the pair \((t,5t+1)\), compressing many parameters into a small number of
joint endpoint labels counts distinct questions. The count of parameters
whose endpoints never meet is the sum of the **sizes of the failed fibers**.
A bound on the number of labels does not supply that weighted sum.

FR-001 gives a fully ordinary interval of `N` parameters for which none of
the pairs has met by the compression clock. FR-002 strengthens this on
natural dyadic shells: for each fixed \(\varepsilon>0\) in its stated range,
almost every parameter remains unresolved through both clocks up to
\((1+\tfrac12\log_2 3-\varepsilon)h\). Its proof uses the published
Baker--Wüstholz logarithmic-form bound, with the field degree, heights,
nonvanishing, and an explicit sufficient threshold checked. It concerns
finite clocks and provides no permanently nonmerging pair.

The paired-return investigation also gives an ordinary arithmetic progression
on which the first balanced return expands:

\[
t=512u+287\quad\longmapsto\quad729u+410>t\qquad(u\ge0),
\]

at common clock `9`. The paired endpoint is again `5` times the lower
endpoint plus `1`. The two arms have no meeting at any independent clocks
through `9`; this is checked by all 100 exact affine intersection equations,
not by sampling the parameter. Thus waiting for the first such return does
not furnish a universal decreasing rank.

Uniform physical paired inverse returns also have a ternary target-residue
restriction. The accompanying descending guards and this target restriction
are stated with their direction: a backward branching obstruction is not a
proof that forward return coverage is impossible. The uncovered all-time
obligation remains explicit.

[Five-ray packet](../../research/focused-forward-20261120/five-ray/README.md)
· [Finite-clock argument](../../research/focused-forward-20261120/five-ray/FINITE_CLOCK_BARRIER.md)
· [Physical paired returns](../../research/focused-forward-20261120/five-ray/PAIRED_RETURNS.md)
· [Parent reconstruction](FIVE_RAY_REVIEW.md).

## What would actually finish the argument

The investigation did not establish any of the following sufficient closures:

- A complete well-founded ordinary selector proving \(C(n)\) for every input,
  including all residue classes and every variable expanding return schedule.
- A theorem bounding the weighted mass of permanent five-ray failures tightly
  enough to apply the source's full-convergence criterion.
- A global ordinary upper bound on the all-word inverse potential that rules
  out both other cycles and escape; finite root computations alone do not
  provide this.

These are mathematical gaps, not implementation tasks hidden by successful
checkers. The new proofs are independently reconstructed elementary arguments,
with the explicitly identified analytic input for FR-002. They are not formal
proof-assistant certifications or claims of external mathematical acceptance.

## Frozen sources

| Source | Full commit and relevant paths |
| --- | --- |
| Main | `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` |
| Previous PR #148 packet | `6ff18e4f63be8f3bece76215fcfe44d83b001d7f`; `research/forward-bridge-20261120/PROOF.md` and the earlier report |
| PR #146 | `561d48a4d3a793a59b1cdf0406062ae1a6d47515`; `research/upper-bit-mergers/THREE_RAY.md`, `AFFINE_RAYS.md`, `PREFIX_COMPRESSION.md` |
| PR #149 | `92c0129e794dde3ec55ceec470a12d51ba3f7e2f`; `research/forward-inverse-defect/PROOF.md`, `CLOSURE_BOUNDARY.md` |

The source pins do not endorse every neighboring claim or later head. Current
publication receipts identify the exact reviewed content and commands actually
executed for this additive packet.
