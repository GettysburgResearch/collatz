# T-9816 -- Rational binary values have a sharp relative support-gap ceiling

Claim ID: `T-9816`
Title: A rational 2-adic binary 64/81 series can have no support gap exceeding the critical relative slope by an unbounded amount
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: `gpt56-synthesis-01-wave14-period-ten`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: elementary product-formula height; local `R-9809` and branch-qualified `PR20/R-9409` and `T-9411` at `14f06d252c3ef56fb9a69ea34c61edaa578d02a1` only for source-chain comparison
Scope: every binary `64/81` series with infinite support; sparse-stack specialization included
Related counterexample candidates: issue #4 M1 and periodic stack frontiers; no `K-####` candidate

## Statement

Put

\[
 T={64\over81}
\tag{1}
\]

and let

\[
 0\le h_0<h_1<h_2<\cdots
\tag{2}
\]

be the support of an infinite binary series

\[
 \Psi=\sum_{j\ge0}T^{h_j}\qquad\hbox{in }\mathbf Q_2.
\tag{3}
\]

Assume that its 2-adic value is rational and write

\[
 \Psi={A\over B},
 \qquad
 A\in\mathbf Z,
 \quad B\in\mathbf Z_{>0},
 \quad \gcd(A,B)=1.
\tag{4}
\]

Then `B` is odd and, for every `j>=0`,

\[
 \boxed{
 2^{6h_{j+1}}
 \le
 \left(|A|+{81\over17}B\right)81^{h_j}.
 }
\tag{5}
\]

Define the critical relative-gap slope

\[
 \delta
 =\log_{64}{81\over64}
 ={\log_2 81\over6}-1
 =0.056641667147437458\ldots
\tag{6}
\]

and put `g_j=h_(j+1)-h_j`.  Taking logarithms in (5) gives

\[
 \boxed{
 g_j
 \le
 \delta h_j
 +{1\over6}\log_2\left(|A|+{81\over17}B\right).
 }
\tag{7}
\]

Consequently,

\[
 \boxed{
 \sup_j\{g_j-\delta h_j\}=+\infty
 \quad\Longrightarrow\quad
 \Psi\notin\mathbf Q.
 }
\tag{8}
\]

The same criterion holds for the standard scaled code
`Phi=(17/81)Psi`, because multiplication by a nonzero rational preserves
rationality.

## Proof

Let

\[
S_j=\sum_{k=0}^{j}T^{h_k}.
\tag{9}
\]

Every partial sum belongs to `Z_2`, and the sequence converges there because
`h_j` tends to infinity.  Hence `Psi` belongs to `Z_2`.  A rational element
`A/B` in lowest terms belongs to `Z_2` only if `B` is odd, proving the first
assertion.

Its ordinary denominator divides `81^(h_j)`.  In `Q_2`, the tail error is

\[
 \begin{aligned}
 E_j
 &=\Psi-S_j\\
 &=T^{h_{j+1}}
 \left(
 1+\sum_{k\ge j+2}T^{h_k-h_{j+1}}
 \right).
 \end{aligned}
\tag{10}
\]

Every exponent in the sum inside parentheses is at least one.  Since
`v_2(T)=6`, that parenthesis belongs to `1+64 Z_2` and is a 2-adic unit.
Therefore

\[
 \boxed{v_2(E_j)=6h_{j+1}.}
\tag{11}
\]

In particular `E_j` is nonzero.  Write it in lowest terms as `N_j/D_j` with
`D_j>0`.  Both `B` and `81^(h_j)` are odd, and subtraction in (4), (9) gives

\[
 D_j\mid B81^{h_j}.
\tag{12}
\]

Equation (11) then says

\[
 2^{6h_{j+1}}\mid N_j.
\tag{13}
\]

Use only the ordinary real embedding of the rational number `E_j`.  From
(12)--(13),

\[
 |E_j|
 ={ |N_j|\over D_j}
 \ge {2^{6h_{j+1}}\over B81^{h_j}}.
\tag{14}
\]

On the other hand, this same rational difference is `A/B-S_j`.  Every term
of the finite sum `S_j` is a positive real number, so

\[
 0<S_j<{1\over1-T}={81\over17},
\tag{15}
\]

and hence

\[
 |E_j|
 \le {|A|\over B}+{81\over17}.
\tag{16}
\]

Combining (14) and (16) proves (5).  Divide its base-two logarithm by six and
subtract `h_j`; equations (6)--(7) follow.  The contrapositive proves (8).
**QED**

## Sparse-stack specialization

For the positive stack notation of PR #20, let

\[
 m_0\ge0,
 \qquad
 m_t=m_0+\sum_{i=1}^{t}d_i,
 \qquad d_i\ge1,
\tag{17}
\]

\[
 \ell_t=9m_t+1,
 \qquad
 H_0=0,
 \qquad
 H_j=\sum_{i=1}^{j}\ell_i.
\tag{18}
\]

The stack series has support `h_j=H_j` and gap
`g_j=ell_(j+1)`.  Therefore

\[
 \boxed{
 \sup_j\{\ell_{j+1}-\delta H_j\}=+\infty
 \quad\Longrightarrow\quad
 \sum_{j\ge0}T^{H_j}\notin\mathbf Q\text{ in }\mathbf Q_2.
 }
\tag{19}
\]

Equivalently, a sufficient condition in the increment variables is

\[
 \sup_j
 \left\{
 9m_{j+1}+1
 -\delta\left(9\sum_{i=1}^{j}m_i+j\right)
 \right\}
 =+\infty.
\tag{20}
\]

This rigorously excludes superlacunary positive directives whose next height
repeatedly dominates the accumulated prior height beyond the critical slope.
It does not exclude bounded or periodic increment words: there
`ell_(j+1)=O(j)` while `H_j=Theta(j^2)`, so the left side of (19) tends to
minus infinity.

## What this repairs and advances

- Local `R-9809` and live `PR20/R-9409` show why unbounded **absolute** gaps do
  not follow from denominator descent: rational 2-adic tails and their bounded
  positive real shadows need not agree.  The present proof never identifies
  those two infinite limits.
- Instead it uses one finite rational partial sum.  The exact 2-adic tail
  valuation and the ordinary height of that same rational difference meet in
  (14), so the product-formula comparison is legitimate.
- The result supplies a direct valid gap statement from this one-coordinate
  height: gaps may be unbounded, but only below the relative line
  `delta h+O(1)`.
- The constant is the same critical slope appearing in the `64 -> 81`
  completion-height/repetition wedge, now applied directly to sparse support.

## Dependency and novelty audit

- No PR #20 denominator-descent claim is used in the proof.  Rationality of
  `Psi`, the exact first omitted exponent, and the finite partial-sum
  denominator suffice.
- Local `L-9803` records the abstract product-formula wedge with the reciprocal
  critical slopes.  The present theorem supplies a new direct support-gap
  specialization and the exact rational-height constant in (5).
- `PR20/T-9411` already computes the exact reduced denominator and 2-adic
  error of bounded-increment stack truncations, then observes their limiting
  exponent is subcritical.  The present theorem extends the finite
  truncation comparison to arbitrary binary support under a hypothetical
  rational value and extracts the pointwise relative-gap ceiling (5)--(8).
- `PR20/T-9401` contains the same slope in a repeated-factor theorem for an
  ordinary integer code.  It neither states the arbitrary-rational
  support-gap criterion nor supplies the missing cross-completion step in
  `T-9418`.
- Live `PR20/R-9409` independently records the completion-limit mismatch and
  explicitly calls for a numerator/height bound.  It supplies no such bound.
  The present cross-multiplied rational difference is exactly that additional
  height coordinate.
- At live head `14f06d2`, `PR20/T-9418`--`T-9421` are explicitly withdrawn.
  The former `T-9418` bounded-absolute-gap statement remains open; (7) is a
  valid weaker replacement obtained without a completion identification.
- A live-head search at `14f06d2` found no displayed relative-gap inequality
  (5), (7), or stack criterion (19), including in the new `R-9409`.
- No external theorem or finite computation is used.

## Gap and scope audit

- Relative control `g_j<=delta h_j+O(1)` does not imply bounded gaps.
- The constant in (7) depends on the numerator and denominator of the assumed
  rational value.  It is fixed along one code but is not uniform over all
  rational codes.
- The binary positive alphabet is used only for the finite real bound (15).
  Signed or unbounded digits require a different height estimate.
- Periodic positive stack increments lie below the relative-gap threshold, so
  this theorem does not settle the periodic q-difference frontier of
  `T-9812`.
- The theorem proves irrationality only under (8) or (19).  It constructs no
  ordinary survivor, Collatz orbit, or `K-####` candidate.

## Adversarial checks

- The tail unit in (10) is proved 2-adically from its residue `1 mod64`; no
  positivity or real convergence is used for (11).
- The real bound is applied only to the finite rational `S_j` and the fixed
  rational `A/B`, not to the real shadow of an infinite 2-adic tail.
- Possible cancellation in the ordinary fraction can only decrease `D_j`;
  the divisibility `D_j|B81^(h_j)` therefore has the correct direction for
  the lower bound (14).
- The exponent in (11) is `6h_(j+1)`, not `6g_j`: the unnormalized tail begins
  at the absolute support position.
- At the critical line `g_j=delta h_j+O(1)`, the argument is sharp at the
  exponent level and gives no contradiction.

## Suggested next attack

Add one centered-carry or archimedean numerator recurrence to (5).  Any
subcritical bound on the right side along all rational tails would lower the
relative slope and could begin to reach periodic or balanced stack supports.
