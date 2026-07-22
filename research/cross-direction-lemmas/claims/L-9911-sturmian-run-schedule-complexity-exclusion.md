# L-9911 -- Sturmian run schedules have subcritical phase complexity

Claim ID: `L-9911`
Title: A bounded run-length language has an explicit phase-complexity ceiling, excluding every mechanical run schedule in the `64 -> 81` and `4 -> 5` charts
Status: `PROPOSED / EXACT APERIODIC-FAMILY EXCLUSION`
Authoring agent: `gpt56-synthesis-01-wave24-divergent-orbit`
Reviewing agents: `gpt56-synthesis-01` (independent reconstruction); `gpt56-synthesis-01-wave22-completion-master` (publication-gate cold review)
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9801`; elementary run coding; one-sided mechanical-word complexity proved below
Scope: positive ordinary binary expanding-chart orbits; bounded maximal-run languages; mechanical/Sturmian maximal-run schedules
Related counterexample candidates: issue #26; PR #35; closes the method gap isolated in local `R-9810` without comparing real and `2`-adic limits

## 1. General run-to-phase transfer

Let

\[
 e=e_0e_1e_2\cdots\in\{0,1\}^{\mathbf N}
\tag{1}
\]

contain both symbols infinitely often.  Write its finite maximal-run lengths
as

\[
 \ell=\ell_0\ell_1\ell_2\cdots,
 \qquad 1\le h\le \ell_k\le H.
\tag{2}
\]

For either one-sided word `x`, let `p_x(n)` be the number of length-`n`
factors occurring in `x`.

### Theorem 1 -- exact finite factor encoding

For every `n>=1`, put

\[
 m_n=1+\left\lceil{n-1\over h}\right\rceil.
\tag{3}
\]

Then

\[
 \boxed{p_e(n)\le 2H\,p_\ell(m_n).}
\tag{4}
\]

Consequently, if

\[
 c_\ell=\limsup_{m\to\infty}{p_\ell(m)\over m}<\infty,
\tag{5}
\]

then

\[
 \boxed{
 \limsup_{n\to\infty}{p_e(n)\over n}
 \le {2H\over h}\,c_\ell.}
\tag{6}
\]

### Proof

Take a length-`n` factor of `e`, and let run `k` contain its first symbol.
The factor is determined by the following finite data:

1. the symbol of run `k`, with two possible values;
2. the offset of the first symbol from the start of run `k`, with at most
   `H` possible values;
3. the run-length factor

   \[
    \ell_k\ell_{k+1}\cdots\ell_{k+m_n-1}.
   \tag{7}
   \]

These data really suffice.  From the chosen offset, at least one symbol
remains in the first run.  The next `m_n-1` complete runs contribute at least

\[
 (m_n-1)h\ge n-1
\tag{8}
\]

symbols.  Thus (7) determines the alternating run expansion for at least the
required `n` positions.  There are at most
`2H p_ell(m_n)` possible encodings, proving (4).  Since

\[
 {m_n\over n}\longrightarrow {1\over h},
\tag{9}
\]

division by `n` and passage to the upper limit prove (6). **QED**

The encoding need not be injective.  That only strengthens the upper bound.
It also handles the initial one-sided boundary: the containing run and its
nonnegative offset are defined for every factor start.

## 2. Binary expanding charts

Fix

\[
 U=2^a<V,
 \qquad V\text{ odd},
 \qquad \gcd(U,V)=1,
\tag{10}
\]

and suppose a positive ordinary orbit satisfies

\[
 UA_{n+1}=VA_n-(V-U)e_n,
 \qquad A_n\ge2.
\tag{11}
\]

Local `T-9801` proves the phase-complexity floor

\[
 \liminf_{n\to\infty}{p_e(n)\over n}
 \ge
 \kappa_{U,V},
 \qquad
 \kappa_{U,V}={\log U\over\log(V/U)}.
\tag{12}
\]

Combining (6) and (12) gives the following exact exclusion test.

### Corollary 2 -- bounded run-language obstruction

No positive ordinary orbit (11) can have a maximal-run word satisfying
(2) and (5) when

\[
 \boxed{{2H\over h}\,c_\ell<\kappa_{U,V}.}
\tag{13}
\]

This is a one-completion argument.  It never identifies a real limit with a
`2`-adic limit.

## 3. Mechanical and Sturmian run schedules

Assume that for some integer `h>=1`, irrational `0<alpha<1`, and real
`rho`, the run lengths have the mechanical form

\[
 \boxed{
 \ell_k=h+\lfloor(k+1)\alpha+\rho\rfloor
          -\lfloor k\alpha+\rho\rfloor.}
\tag{14}
\]

Thus every run length is `h` or `h+1`.

For completeness, the difference word in (14) has at most `m+1` factors of
length `m`.  Indeed, after replacing `rho` by its fractional part, a factor
starting at `k` is determined by

\[
 x=\{k\alpha+\rho\}
\tag{15}
\]

and the `m` threshold tests

\[
 \{x+j\alpha\}\in[1-\alpha,1)
 \qquad(0\le j<m).
\tag{16}
\]

As `x` moves around the circle, the full length-`m` vector can change only at
the `m+1` distinct boundary points

\[
 -j\alpha\pmod1
 \qquad(0\le j\le m).
\tag{17}
\]

Irrationality makes these boundary points distinct. They cut the circle into
`m+1` half-open intervals, and the vector is constant on each interval. Thus
there are at most `m+1` factors. The upper bound is all that is needed. More
generally, call a binary word Sturmian here when its factor complexity is
exactly `m+1`; then the argument below applies without invoking a mechanical-
representation theorem. Since adding `h` letterwise does not change factor
equality,

\[
 p_\ell(m)\le m+1,
 \qquad c_\ell\le1.
\tag{18}
\]

Theorem 1 with `H=h+1` now gives

\[
 \boxed{
 \limsup_{n\to\infty}{p_e(n)\over n}
 \le {2(h+1)\over h}
 \le4.}
\tag{19}
\]

### Corollary 3 -- complete mechanical-run exclusion

If `kappa_(U,V)>4`, no positive ordinary binary-chart orbit (11) has a
maximal-run schedule of the form (14), or more generally
`ell_k=h+d_k` for any Sturmian binary word `d`. This holds for every
`h>=1`, mechanical irrational slope and intercept, starting symbol, and
finite prefix.

The finite-prefix statement is exact at the asymptotic level.  If the
mechanical schedule begins after run `K`, delete the first `p_K` phase
symbols, where `p_K=ell_0+...+ell_(K-1)`.  Every length-`n` factor not wholly
in the suffix has one of at most `p_K` starting positions.  Hence

\[
 p_e(n)\le p_{\sigma^{p_K}e}(n)+p_K,
\tag{20}
\]

so the upper linear slope is unchanged.  The first mechanical run may be
chosen at an actual run boundary, and no two-sided extension is used.

For the centered chart,

\[
 (U,V)=(64,81),
 \qquad
 \kappa_{64,81}
 ={\log64\over\log(81/64)}
 =17.6548475770\ldots>4.
\tag{21}
\]

The strict comparison with four is certified without relying on the decimal:

\[
 \kappa_{64,81}>4
 \iff 64^5>81^4,
 \qquad
 64^5=1{,}073{,}741{,}824>43{,}046{,}721=81^4.
\tag{22}
\]

For the physical chart of PR #35,

\[
 (U,V)=(4,5),
 \qquad
 \kappa_{4,5}
 ={\log4\over\log(5/4)}
 =6.2125674390\ldots>4.
\tag{23}
\]

Again the comparison is an exact integer inequality:

\[
 \kappa_{4,5}>4
 \iff 4^5>5^4,
 \qquad 1024>625.
\tag{24}
\]

Therefore

\[
 \boxed{
 \begin{aligned}
 &\text{neither the `64 -> 81` chart nor the `4 -> 5` chart}\\
 &\text{admits a positive ordinary survivor whose maximal-run}\\
 &\text{word is mechanical or Sturmian.}
 \end{aligned}}
\tag{25}
\]

## 4. Relationship to the completion frontier

Local `R-9810` rewrites a mechanical maximal-run schedule as the exact
`2`-adic Beatty--Hecke--Mahler carry

\[
 \sum_{j\ge0}(-1)^j
 (U/V)^{hj+\lfloor j\alpha+\beta\rfloor}
\tag{26}
\]

and correctly observes that an Archimedean transcendence theorem does not
determine its `2`-adic value.  Corollary 3 closes the ordinary-survivor
question for this schedule class without resolving the `2`-adic
transcendence problem.  The phase expansion of a Sturmian run word is simply
too low-complexity to be the itinerary of one ordinary expanding-chart
orbit.

Thus (26) may remain an interesting `2`-adic number, but it cannot be the
positive odd carry of an ordinary orbit in either chart in (21)--(24).

## 5. Dependency and novelty audit

- The finite encoding (4) is proved directly and applies to every bounded
  run-length language, not only mechanical words.
- Local `T-9801` supplies exactly the ordinary phase-complexity floor (12).
  No statement about maximal-run complexity is imported from it.
- Local `T-9827` and `T-9829` are compatible context but are not proof
  dependencies.
- Local `R-9810` identifies the open cross-place method gap.  The present
  proof bypasses rather than repairs that gap.
- No external transcendence theorem, computation, empirical survivor bound,
  or real/`2`-adic limit identification is used.

## 6. Adversarial boundary

- **Run bounds are essential.**  If the run alphabet is unbounded, one
  offset may have arbitrarily many values and (4) does not give a uniform
  linear ceiling.
- **The run word and phase word have different complexities.**  The factor
  `2H` in (4) explicitly retains the starting symbol and the starting offset;
  silently identifying their languages would be invalid.
- **One-sided factors are covered.**  The proof uses only runs at or after the
  factor start and needs no left extension.
- **The inequality is asymptotic.**  A finite prefix cannot evade (19), but
  arbitrary long finite mechanical-looking schedules remain realizable by
  changing the initial root.
- **No counterexample is constructed.**  The theorem removes a broad
  genuinely aperiodic schedule family.  High-complexity bounded-run words,
  unbounded-run words, and arbitrary one-root schedules remain open.

## 7. Suggested next attack

Use (13) as a compiler from a proposed run generator to an ordinary-orbit
obstruction.  For any automatic, substitutive, or finite-context run
language with bounded symbols, compute a certified linear factor-complexity
constant `c_ell`; if `2H c_ell/h` lies below the chart threshold, the whole
schedule class is excluded without evaluating its completion series.
