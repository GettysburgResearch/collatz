# Cross-direction lemma forge -- wave twenty-four resolution-first checkpoint

Date: 2026-07-22
Agent: `gpt56-synthesis-01`
Issue: #29
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
Status: six proposed exact reductions; unconditional counterexample search remains primary; no counterexample claimed

## Resolution posture

The active objective is a full unconditional Collatz resolution, with an
explicit nontrivial positive cycle as the shortest finite-certificate route
and an ordinary divergent orbit as the parallel route. Partial results are
published only when they are independently auditable and useful to those
routes.

At this checkpoint there is no candidate integer. In particular, no formal
`2`-adic path, modular cycle, powered presentation of `(2)`, negative cycle,
or changing sequence of finite roots is reported as a counterexample.

## Live reconciliation

- This branch and draft PR #34 began the wave at
  `b77a84c7e4ff15f36b59b29627671f1cb6544072`.
- Issue #9 remained the compressed positive-cycle target. Draft PR #42 and
  its claimed branch stood at `94fcd99fe7fb71e0f5a15915ba40e9d74b167a13`.
- PR #11 remained at `7950713cbb6ba0af0a424806cc36ce01ad24cf9e`.
- Issue #40 remained the proof-carrying centered-tail target; its active
  branch stood at `e0593a9f59e7a8a8ce00106581ffa24d37963173`.
- PR #37 stood at `a518db7feece37513ddcda729553e8b8c4c4d657`.
- PR #38's global cartography stood at
  `dbcf25cabba838c8c97ba9003b8216f83d92d458`.

## Result 1 -- commuting cycle grammars collapse

[`L-9906`](../../research/cross-direction-lemmas/claims/L-9906-compressed-cycle-commuting-block-collapse.md)
classifies the affine commutator of two compressed blocks.

For summaries `(p,q,c)` and `(r,s,d)`, the exact chronological defect is

\[
 \Omega=(q-p)d-(s-r)c.
\]

All translation, identity, and homothety degeneracies are handled explicitly.
For nonempty accelerated words `u,v`, none of those degeneracies occurs, and
the following are equivalent:

- their affine maps commute;
- `Omega(u,v)=0`;
- their rational fixed points agree;
- `uv=vu`; and
- `u` and `v` are powers of one unique primitive word.

If `w=uv` is an exact positive cycle and `n_u` is the state after `u`, then

\[
 \boxed{\Omega(u,v)=D_w(n_0-n_u).}
\]

Thus zero commutator is exactly an early return and a repeated smaller
certificate. Every proper cut of a primitive certificate instead satisfies

\[
 0\ne\Omega,
 \qquad D_w\mid\Omega,
 \qquad |\Omega|\ge D_w.
\]

This yields a proof-carrying grammar sieve: canonicalize zero defects, reject
nonzero defects smaller than `D_w`, and retain exact divisibility for the
survivors. It does not exclude every noncommuting primitive word.

## Result 2 -- the Smith-form route is an exact equivalence

[`L-9907`](../../research/cross-direction-lemmas/claims/L-9907-cycle-circulant-snf-equivalence.md)
records the outcome of the first resolution-focused lattice attack.

For a valuation word `w=(a_0,...,a_(k-1))`, let `M_w` have cyclic row

\[
 -3x_j+2^{a_j}x_{j+1}=1.
\]

For every `r<k`, one `r`-minor is `(-3)^r` and another is a power of two.
All lower determinantal divisors are therefore one, while

\[
 \det M_w=(-1)^{k-1}(2^A-3^k).
\]

Consequently

\[
 \boxed{
 \operatorname{SNF}(M_w)
 =\operatorname{diag}(1,\ldots,1,|D_w|).}
\]

If `C_j` are the rotated affine constants, then

\[
 M_w C=D_w\mathbf1.
\]

Cramer's rule shows that the maximal minors of `[M_w|1]` have gcd

\[
 G=\gcd(D_w,C_0,\ldots,C_{k-1}),
\]

and the class of `1` in the cyclic cokernel has exact order `|D_w|/G`.
For `D_w>0`, that class vanishes exactly when `C_j/D_w` is the full positive
integer cycle vector.

Therefore the proposed theorem `G<D_w` for every primitive word other than
`(2)` is logically equivalent to excluding all nontrivial positive cycles.
SNF and the resultant see only `(k,A)`; they do not supply the missing prime
of `D_w` that fails to divide `C_0`. This closes a tempting shortcut while
leaving the genuine divisibility problem explicit.

## Result 3 -- centered positive lassos have a finite firewall

[`L-9908`](../../research/cross-direction-lemmas/claims/L-9908-centered-forced-tail-lasso-firewall.md)
addresses issue #40's exact zero-appended-block kernel

\[
 64B_{n+1}=81B_n+e_n-e_{n+1},
 \qquad e_n\in\{0,1\}.
\]

For `B_0>=1`, integrality gives strict escape `B_(n+1)>=B_n+1`. The exact
heights `17B_n-1` and `17B_n+1` give

\[
 \left({81\over64}\right)^n
 \left(B_0-{1\over17}\right)+{1\over17}
 \le B_n\le
 \left({81\over64}\right)^n
 \left(B_0+{1\over17}\right)-{1\over17}.
\]

The normalized state has a positive real limit, while backward integrality
gives a separate `Q_2` series for `-B_0`. The two completions are not
identified.

If the bit tail has period `p` from `N`, define the finite integer

\[
 D_{N,p}=\sum_{j=0}^{p-1}
 81^{p-1-j}64^j(e_{N+j}-e_{N+j+1}).
\]

Repeated backward iteration in `Q_2`, followed only then by rational
injectivity, forces

\[
 (81^p-64^p)B_N+D_{N,p}=0,
 \qquad
 |B_N|\le {1\over17}.
\]

The only nonnegative integral periodic tails are `(B,e)=(0,0)` and `(0,1)`.
Hence an autonomous deterministic finite-state controller cannot carry a
positive survivor. The claim explicitly leaves genuinely aperiodic paths,
unbounded carry, and nondeterministic label choices open.

A final source refresh found independently overlapping live results on the
issue-#40 branch: `D-8701` gives the recurrence, `L-8701` gives strict
monotonicity, and `R-8701` gives the periodic-lasso exclusion. `L-9908` does
not claim those conclusions as novel. Its cross-direction additions are the
sharp normalized height cone, the explicit separation of real and `Q_2`
limits, and the maximal-run zipper/table inherited from the general chart.

## Result 4 -- one genuine primitive prime power can be fully silent

[`L-9909`](../../research/cross-direction-lemmas/claims/L-9909-primitive-prime-power-cycle-obstruction-boundary.md)
records the exact failure of the natural Zsigmondy obstruction.

For any `g>m>=1`, choose a primitive divisor `p` of `3^g-2^g`, let

\[
 e=\nu_p(3^g-2^g),
 \qquad H=\operatorname{ord}_{p^{e+1}}(2),
 \qquad L=1+gH,
\]

and form the primitive mixed valuation word

\[
 w=L^m1^{g-m}.
\]

Its parameters are

\[
 k=g,
 \qquad A=g(1+mH),
 \qquad D_w=\left(2^{1+mH}\right)^g-3^g>0.
\]

Modulo `p^(e+1)`, every letter looks like `1`, so the normalized numerator is
the same geometric sum as the constant word. The exact result is

\[
 \boxed{\nu_p(D_w)=e=\nu_p(C_w).}
\]

The prime remains a genuine order-`g` top-cyclotomic divisor for the new
denominator. The construction handles `e>1`, can silence any prescribed
finite set of factors simultaneously, and remains available with 92 local
minima and odd-step length above `72,000,000,000`.

This is deliberately not a cycle candidate. The new denominator may contain
additional prime factors that fail to divide `C_w`. The theorem proves that
existence, order, and lifting depth of one primitive divisor cannot be the
universal obstruction; a successful factor route must control the whole
factorization together with the prefix discrepancies.

The manuscript also proves that this specific family cannot be upgraded into
a cycle. Writing `r=g-m`, `a=2^L`, and `U=a^m`, exact composition gives

\[
 (a-3)C_w=D_w+(a-2)U(3^r-2^r).
\]

For the lifted frontier family with `m>=2`, divisibility would force

\[
 D_w\mid(a-2)(3^r-2^r),
\]

but the latter is positive and strictly smaller than `D_w`. Thus another
prime-power factor necessarily escapes. A further residue-word theorem
excludes choosing one exponent modulus containing `ord_(D_w)(2)` or
`lambda(D_w)` so that the word aliases a smaller word modulo every factor at
once. A separate identity and size bound close the `m=1` edge, so the entire
lifted family is excluded. Only genuinely prime-dependent nonconstant
cancellation patterns remain.

The residue-word theorem leaves a still sharper exact target. If an upward
alias has total valuations `A>B`, then cancellation of the odd denominator
gives

\[
 D_w\mid 2^{A-B}-1,
\]

while size forces `A=ceil(k log_2 3)` and therefore

\[
 2^A-3^k\le 2^{A-k}-1.
\]

An explicit rational specialization of Matveev's theorem gives the finite
cutoff `k<25,000,000,001`. Legendre's criterion then reduces the entire
remaining range to eleven upper convergents of `log_2 3`; exact rational
logarithm enclosures certify that list. The `8/5` convergent fails directly,
and every denominator at least `41` fails the standard two-sided convergent
bound. Thus the gap, and every upward one-global-residue-word alias, is
impossible. As a reusable consequence, for every `D=2^A-3^k>1`,

\[
 \boxed{\operatorname{ord}_D(2)>A-k.}
\]

Every letter in a positive length-`k`, total-`A` valuation word is at most
`A-k+1`, so reduction modulo the full denominator order cannot change a
single letter. This does not control the smaller, different orders of the
individual prime-power factors.

## Result 5 -- neutral valuations disappear after centering at one

[`L-9910`](../../research/cross-direction-lemmas/claims/L-9910-centered-defect-neutral-tail-collapse.md)
introduces

\[
 E_w=C_w-D_w
\]

and proves the exact sparse identity

\[
 \boxed{
 E_w=\sum_{j=0}^{k-1}
 3^{k-1-j}2^{A_j}(4-2^{a_j}).}
\]

Every valuation `2` contributes zero. The first non-2 letter gives the unique
least 2-adic summand and therefore determines `v_2(E_w)` exactly. Positive
cycle divisibility is equivalently `D_w>0` and `D_w|E_w`; outside the trivial
word `(2)^k`, exact replay also forces `E_w>=2D_w`.

For a fixed core `u` and a terminal neutral tail `w_r=u(2)^r`,

\[
 E_{w_r}=3^rE_u,
 \qquad
 D_r=2^{A_u}4^r-3^{k_u}3^r,
\]

and `gcd(D_r,3)=1`. Hence a cycle exists in this family exactly when

\[
 D_r>0,
 \qquad D_r\mid E_u.
\]

Once positive, `D_(r+1)>4D_r`, so the family reduces to a finite exact list
of divisors of the fixed integer `E_u`. A complete case split further
excludes every word with exactly one or exactly two non-2 letters. The last
case reduces to four values `t=3,4,5,6`, all rejected by explicit nonzero
remainders.

Three exceptional letters are also impossible. Deleting neutral branches
strictly increases the centered replay; every three-letter core containing a
valuation at least three is a contraction and can be classified exactly. The
only height survivor reduces to the impossible replay `3 -> 5` with next
valuation `4`. If all three exceptional letters are `1`, rotating the largest
neutral gap to the tail and maximizing the remaining numerator by adjacent
swaps gives `E_u<2D`.

Four exceptional letters are impossible as well. After deleting neutral
branches and lowering high letters to `3`, every core with at least two high
letters has fixed point below the least positive centered state. The
one-high cases reduce either to the core `(1,1,1,4)` or to a largest-gap
estimate with exact checks at `R=1,2,3`; the all-one case has the same
asymptotic collapse and six nonzero remainders at its sole boundary `R=6`.
Any nontrivial cycle word therefore has at least five exceptional valuations
before the much stronger external frontier is used.

## Result 6 -- mechanical and Sturmian run schedules are too simple

[`L-9911`](../../research/cross-direction-lemmas/claims/L-9911-sturmian-run-schedule-complexity-exclusion.md)
closes the low-complexity divergent-orbit schedule left open by `R-9810`.

If the binary phase word has run lengths between `h` and `H`, a length-`n`
phase factor is determined by its starting symbol, its offset in the first
run, and

\[
 1+\left\lceil{n-1\over h}\right\rceil
\]

successive run lengths. Therefore

\[
 \boxed{
 p_e(n)\le2H,p_\ell\!\left(
 1+\left\lceil{n-1\over h}\right\rceil\right).}
\]

Mechanical and Sturmian binary run schedules have `p_ell(m)<=m+1`; for run
lengths `h,h+1`, the resulting phase-complexity slope is at most
`2(h+1)/h<=4`. Local `T-9801` requires the strictly larger slope

\[
 {\log U\over\log(V/U)}.
\]

The two needed comparisons are exact:

\[
 64^5>81^4,
 \qquad
 4^5>5^4.
\]

Thus neither the `64 -> 81` nor `4 -> 5` chart admits a positive ordinary
survivor with an eventually mechanical or Sturmian maximal-run schedule. The
proof stays entirely in ordinary factor complexity and does not identify the
real and `Q_2` values of the Beatty carry.

## Resolution attacks that did not close

The lattice/SNF attack above was pursued as a possible universal obstruction,
not designed as a boundary lemma. Its exact endpoint is

\[
 [\mathbf1]\ne0\text{ in }\operatorname{coker}M_w
 \quad\Longleftrightarrow\quad
 D_w\nmid C_w,
\]

which is the original positive-cycle condition. Cut defects do not strengthen
it: under a certificate they are expected nonzero multiples of the odd
denominator.

Primitive-divisor, constructive CRT, and ordinary divergent-orbit attacks
remain active beyond this publication checkpoint. Any future success will be
required to supply one explicit positive integer and a finite, independently
replayable proof that its orbit is cyclic or avoids the trivial cycle forever.

## Review and validation

- `L-9906` was independently reconstructed by the integrating agent. The
  orientation, affine degeneracies, word decoder, first-mismatch valuation,
  early-return identity, connected-partition theorem, and cut sieve were
  checked separately from the authoring lane.
- `L-9907` was reconstructed from its minors rather than accepted from an SNF
  computation. The determinant sign, lower determinantal divisors, augmented
  Cramer minors, cokernel-class order, and equivalence with `D|C` were checked.
- `L-9908` received a nonauthoring cold review of every displayed formula.
  The reviewer found two scope defects but no algebraic defect: the title had
  omitted the trivial zero lassos, and one completion sentence had stated a
  conditional unboundedness consequence as unconditional existence. Both
  were corrected, and the reviewer returned `PASS` on the patched file.
- `L-9909` received a separate primitive-divisor audit and an integrating
  reconstruction. Both Zsigmondy exceptions, exact order modulo `p^e`, the
  `p^(e+1)` lifting modulus, cyclic word primitivity, the full numerator
  valuation, finite-set scope, and frontier parameters were checked. The
  concrete word `(41,1)` independently gives `v_5(D)=v_5(C)=1`. Two further
  cold audits checked the rational Matveev specialization, analytic cutoff,
  gcd-reduced Legendre step, complete upper-convergent table, exceptional
  rows, and the full-order corollary. The exact `Fraction` certificate passes.
- `L-9910` was independently reconstructed from the centered telescoping
  identity. The unique first-defect valuation, neutral-tail chronology,
  parity-height bound, denominator recurrence, mixed-sign inequality,
  centered-deletion comparison, three-core replay, four-core contraction
  tables, largest-gap bounds, and every finite boundary remainder were
  checked. Exhaustive regression over `55,986` words of length at most six
  over `{1,...,6}` agreed with the identities; a second cold review audited
  the sparse exclusions independently.
- `L-9911` received an integrating reconstruction of the one-sided factor
  encoding, circle-partition bound, finite-prefix correction, and both exact
  threshold inequalities. Independent small factor enumeration passed for
  `h=1,...,5` and lengths through 80.
- Exact bounded enumerations checked `24,025` ordered word pairs for the
  commutator and first-mismatch valuation, all `335,922` valuation words of
  length at most seven over `{1,...,6}` for the bounded cycle regression, all
  `780` words of length at most four over `{1,...,5}` for the determinant,
  lower-minor, and rotation-gcd formulas, `1,368` centered transitions, and
  all `2,046` cyclic bit words of periods at most ten. These are regression
  tests only, not proof inputs.
- `research/cross-direction-lemmas/proofs/L-9909-gap-certificate.py` used
  exact integer and rational arithmetic to enclose `log 2` and `log 3`, certify
  the required continued-fraction prefix, enumerate every upper convergent
  below the analytic cutoff, and replay all exceptional inequalities.
- Claim IDs, local links, metadata, equation/fence balance, and whitespace are
  checked before commit.

## Boundary

No result in this wave proves the Collatz conjecture or gives a counterexample.
Specifically:

- commuting grammars collapse, but primitive noncommuting words remain;
- the cyclic cokernel criterion is exactly the original cycle condition;
- deterministic periodic centered tails are impossible, but aperiodic
  unbounded-carry paths remain; and
- one or finitely many selected denominator prime powers may be silent, but
  the displayed lifted family is nevertheless excluded and arbitrary
  cross-prime cancellation remains uncontrolled; and
- neutral padding and words with at most four non-2 valuations are excluded,
  but the five-exception sparse frontier remains; and
- mechanical/Sturmian run schedules are excluded, but high-complexity
  bounded runs and subgeometrically unbounded runs remain; and
- no `K-####` candidate is proposed.

All six entries remain `PROPOSED` pending repository-independent review.
