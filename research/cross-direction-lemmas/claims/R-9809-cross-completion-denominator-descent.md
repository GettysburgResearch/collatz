# R-9809 -- Denominator descent does not identify the 2-adic tail with its real shadow

Claim ID: `R-9809`
Title: The cross-completion bound in PR20/T-9418--T-9421 is unsupported, so the claimed all-directive irrationality and ordinary-section closure do not follow
Status: `PROPOSED / SOURCE-CONFIRMED PROOF-CHAIN REFUTATION`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: `gpt56-synthesis-01-wave16-completion-cold-review`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: branch-qualified `PR20/L-9416`, `L-9417`, and the historical versions of `T-9418`--`T-9421` at `aa9cf71c1f252359869ef917955051f340a09df7`; source follow-up `PR20/R-9409` at `14f06d252c3ef56fb9a69ea34c61edaa578d02a1`
Scope: proof status of the denominator-descent irrationality and rational-code classification chain; no assertion that the theorem statements are false
Related counterexample candidates: issue #4 M1; no `K-####` candidate

## Statement

The denominator descents in `PR20/L-9416` and `L-9417` are valid.  They
control the reduced denominators of rational **2-adic** tail values, but do
not control their ordinary numerators or real absolute values.

The proofs of `T-9418`, `T-9419`, and `T-9420` subsequently apply the compact
real bound for the positive real tail to the real embedding of that rational
2-adic tail.  Those are different completion limits and no equality between
them has been proved.  Consequently:

\[
 \boxed{
 \text{the proofs of `T-9418`, `T-9419`, and `T-9420` do not close.}
 }
\tag{1}
\]

`T-9421` depends on `T-9420`, so its claimed ordinary-section closure is also
not established by the submitted chain.  This refutes the proof bridge, not
the four theorem statements.  They may still be true after an independent
completion-height, product-formula, or value-theoretic argument.

After this audit was completed, PR #20 independently adopted the same
correction.  At live head `14f06d2`, its new `R-9409` records the
real-versus-2-adic limit mismatch, and `T-9418`--`T-9421` are explicitly
withdrawn with their statements left open.  Sections 1--3 below audit the
historical proofs at `aa9cf71`; they are retained because the exact defect
laws (10) and (17) sharpen the source correction quantitatively.

## 1. The two tail values

Put

\[
 T={64\over81}
\tag{2}
\]

and let

\[
 0\le h_0<h_1<h_2<\cdots .
\tag{3}
\]

For each `j`, the rational partial sums

\[
 Y_{j,N}=\sum_{k=j}^{N}T^{h_k-h_j}
\tag{4}
\]

converge in both completions.  They define two a priori different values:

\[
 Y_j^{(2)}=\lim_{N\to\infty}Y_{j,N}\quad\hbox{in }\mathbf Q_2,
 \qquad
 Y_j^{(\infty)}=\lim_{N\to\infty}Y_{j,N}\quad\hbox{in }\mathbf R.
\tag{5}
\]

Both satisfy their own copy of the same rational recurrence,

\[
 Y_j^{(v)}=1+T^{g_j}Y_{j+1}^{(v)},
 \qquad
 g_j=h_{j+1}-h_j,
 \qquad v\in\{2,\infty\}.
\tag{6}
\]

However, convergence of one rational sequence in two inequivalent
completions does not identify its limits.  This is already stated explicitly
in `L-9416`: for example,

\[
 x_N={2^N\over1+2^N}
\tag{7}
\]

converges to zero in `Q_2` and to one in `R`.

Assume now that `Y_0^(2)` is rational.  Then `L-9416` correctly proves that
every `Y_j^(2)` is rational and that its reduced denominator divides one fixed
odd integer `B`.  Write

\[
 R_j=\iota_\infty\!\left(Y_j^{(2)}\right)\in\mathbf Q\subset\mathbf R,
 \qquad
 Z_j=Y_j^{(\infty)}.
\tag{8}
\]

Here `iota_infinity` means the ordinary real embedding of the rational
2-adic value.  Subtracting the two recurrences (6) gives the exact
completion-defect law

\[
 R_j-Z_j=T^{g_j}(R_{j+1}-Z_{j+1}).
\tag{9}
\]

Therefore

\[
 \boxed{
 R_j-Z_j=T^{-(h_j-h_0)}(R_0-Z_0).
 }
\tag{10}
\]

Unless the missing equality `R_0=Z_0` is proved, the defect grows rather than
shrinks in the real embedding.  The positive geometric estimate

\[
 1<Z_j\le {1\over1-T}={81\over17}
\tag{11}
\]

does not bound `R_j`.

## 2. Exact failure in `T-9418`

The objects denoted `Y_j` in `L-9416` are explicitly the 2-adic limits
`Y_j^(2)`.  Thus its denominator conclusion applies to `R_j`, the real
embedding of those rational 2-adic values.  Moreover, `Y_{j+1}^{(2)}` is
congruent to `1` modulo `64 Z_2`, so it is nonzero and the recurrence gives
`R_j != 1`.  The fixed-denominator conclusion therefore legitimately gives

\[
|R_j-1|\ge {1\over B}.
\tag{12}
\]

By contrast, positivity of the real series gives

\[
 0<Z_j-1
 =T^{g_j}Z_{j+1}
 \le {T^{g_j}\over1-T}.
\tag{13}
\]

`T-9418/(7)--(9)` writes (13) with the 2-adic-defined symbol `Y_j`, thereby
replacing `Z_j` by `R_j`.  The final contradiction compares (12) and (13),
but they concern different real numbers.  Formula (10) displays the missing
term exactly:

\[
 R_j-1
 =(Z_j-1)+T^{-(h_j-h_0)}(R_0-Z_0).
\tag{14}
\]

An unbounded gap makes the first term small.  It does not control the second.
Hence denominator descent alone does not prove the bounded-gap conclusion of
`T-9418`.

## 3. Propagation through `T-9419`--`T-9421`

### `T-9419`

The main proof invokes `T-9418`, so it inherits (14).  Its advertised direct
proof repeats the same step: the normalized stack tails supplied by
`L-9416` are 2-adic values, while the inequality

\[
 0<\Theta_j-1\le {T^{\ell_{j+1}}\over1-T}
\tag{15}
\]

belongs to the separate positive real tail.  Without a completion bridge,
the shrinking real bound does not apply to the rational 2-adic tail, although
its nonvanishing away from one follows from the same leading-unit argument as
in Section 2.  The claimed irrationality of every positive stack directive is
not proved.

### `T-9420`

`L-9417` is especially explicit: its `S_n` is the 2-adic digit tail, the real
limit is a separate value, and descending denominators do not bound
numerators.  If `S_0` is rational, put

\[
 R_n=\iota_\infty(S_n),
 \qquad
 Z_n=\sum_{k\ge0}\epsilon_{n+k}T^k\quad\hbox{in }\mathbf R.
\tag{16}
\]

The digit recurrence gives

\[
 \boxed{R_n-Z_n=T^{-n}(R_0-Z_0).}
\tag{17}
\]

The bound `0<=Z_n<=81/17` therefore gives no bound on `R_n`.  The line
`T-9420/(4)` instead asserts that the 2-adic-defined rational `S_n` lies in
that compact real interval.  The resulting finite state set `R_B`, repeated
tail state, and eventual-periodicity conclusion are unsupported.

### `T-9421`

Once eventual periodicity were known, `T-9421` would be correct to replace the
series by one rational geometric expression and evaluate it in both
completions.  But its only route to eventual periodicity is `T-9420`, whose
proof uses the invalid compact-state step above.  The later
completion-independent periodic formula cannot retroactively justify the
earlier inference; that would be circular.

## 4. Surviving statements and dependency impact

- `L-9416` and `L-9417` survive.  Their denominator-divisor conclusions are
  elementary and their own gap audits state the missing numerator issue
  correctly.
- `L-9415` and the native q-difference equation survive; they do not use the
  later denominator chain.
- Local `T-9812` survives in full.  Its formal independence, real positivity,
  and exact physical 2-adic Casoratian valuation are proved directly.  Only
  its prose saying that scalar irrationality was already closed by `T-9419`
  must be withdrawn.
- Earlier PR #20 irrationality results with separate Pade or external-source
  proofs require their own dependency audits; this refutation neither
  validates nor invalidates them.
- No Collatz counterexample, ordinary survivor, or counterexample to the
  theorem statements is constructed here.

## 5. What would repair the chain

Any one of the following would supply genuinely new information absent from
denominator descent:

1. prove `R_0=Z_0`, or directly obtain a uniform archimedean bound on the
   embedded rational tails by an independent argument, before importing a
   compact real-tail estimate;
2. bound the ordinary numerators of the rational 2-adic tails by a
   completion-height or product-formula argument;
3. prove eventual periodicity by an independent finite-state theorem that
   includes an archimedean height coordinate; or
4. prove the relevant stack values irrational by a correctly specialized
   p-adic q-functional or approximation theorem.

The exact laws (10) and (17) show why denominator information alone cannot do
this: every nonzero initial completion defect is amplified by the inverse real
contraction.

## Dependency and novelty audit

- The source contradiction is internal.  `L-9416` and `L-9417` explicitly
  distinguish the two completions and warn that their denominator chains do
  not bound real height; `T-9418` and `T-9420` use precisely the quarantined
  inference.
- The source-history repairs `eb95879` and `aa9cf71` changed only `L-9416`
  and `L-9417`, respectively.  No corresponding dependency repair propagated
  to `T-9418`--`T-9421` at the historical audited head.
- Earlier `PR20/L-9404` does give an exact ordinary tail-orbit identity when
  the initial code value is an ordinary integer.  Its bounds grow on the
  `(81/64)^n` scale, in agreement with the amplification in (17); they neither
  identify the two completion limits nor put the embedded tails in a compact
  state set.  Thus `L-9404` does not repair `T-9420` or its use in `T-9421`.
- A search at historical head `aa9cf71` found no intervening
  completion-equality or numerator-height theorem in the six newly added
  claims.  Live head `14f06d2` instead withdraws the four affected claims and
  adds the independent source refutation `R-9409`; it does not add such a
  bridge.
- Formulae (10) and (17) are obtained by subtracting the two exact tail
  recurrences.  They make the missing bridge quantitative rather than merely
  terminological.
- No external theorem or finite computation is used.

## Gap audit

- This claim refutes submitted proofs, not the statements of `T-9418` through
  `T-9421`.  A different argument could establish any of them.
- The example (7) illustrates inequivalent completion limits; it is not a
  binary `64/81` counterexample and is not presented as one.
- If completion equality is added as an explicit hypothesis, the compact
  real-tail arguments become valid.  That hypothesis is not supplied merely
  by rationality of the 2-adic value.
- No conclusion is drawn about nonperiodic algebraic values, the cap-stitch
  architecture, the H subsystem, or the Collatz conjecture.

## Adversarial checks

- Recurrence subtraction gives (10) and (17) in both directions; the inverse
  power of `T` has the displayed sign because the next tail is obtained by
  division by the real contraction.
- When `R_0=Z_0`, both defect laws vanish identically and recover the source's
  intended compact bound, confirming that equality is exactly the missing
  premise.
- When `R_0 != Z_0`, (10) is compatible with the fixed-denominator lower
  bound: the ordinary numerators of `R_j` may grow without limit, exactly as
  `L-9416` warns.
- `T-9421`'s use of a periodic geometric expression is locally sound; only its
  dependence on the unproved periodicity classification is quarantined.

## Suggested next attack

Combine `L-9417`'s finite denominator set with one exact archimedean height or
centered-carry coordinate.  A successful repair must control the expanding
defect in (17), not reapply positivity to the separate real shadow.
