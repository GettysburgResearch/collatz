# T-9822 -- Every positive `4/5` chart survivor is logarithmically oscillatory

Claim ID: `T-9822`
Title: Same-symbol returns have an exact dyadic valuation, forcing both phase supports and the switch set at every multiplicative scale
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave16-completion-cold-review`
Reviewing agents: `gpt56-synthesis-01`; `gpt56-synthesis-01-wave18-cap-joint-carry`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9819`; branch-qualified `PR35/T-8802`, `T-8803`, `T-8805`, `T-8806`, and `T-8807` at `6bb647ad13507d8b478ae990d3e1d1b95aea1f17`; branch-qualified `PR20/T-9403` and `T-9405` at `14f06d252c3ef56fb9a69ea34c61edaa578d02a1` for comparison only
Scope: every hypothetical positive ordinary orbit remaining forever in the exact two-phase `5x+1` `4 -> 5` chart
Related counterexample candidates: issue #26; no `K-####` candidate

## Setup

Let `A_0>0` remain forever in the exact chart of `PR35/T-8802`, and let
`A_n` be its successive two-step chart states.  Put

\[
 M_n=A_n+2.
\tag{1}
\]

Then `M_n>=4`, and the chart code and recurrence are

\[
 \epsilon_n=[M_n]_4\in\{0,1\},
 \qquad
 M_{n+1}={5M_n-\epsilon_n\over4}.
\tag{2}
\]

Define

\[
 \alpha=\log_4 5
 =1.160964047443681\ldots,
 \qquad
 \delta=\alpha-1=\log_4(5/4),
\tag{3}
\]

\[
 C=\log_4(5M_0),
 \qquad
 \rho={C\over\delta}.
\tag{4}
\]

For `s in {0,1}`, enumerate the occurrence positions of the symbol `s` as

\[
 0\le h^{(s)}_0<h^{(s)}_1<h^{(s)}_2<\cdots
\tag{5}
\]

and put

\[
 N_s(Y)=\#\{j:h^{(s)}_j\le Y\}.
\tag{6}
\]

Finally, let

\[
 S(Y)=\#\{n\in\mathbf Z_{\ge0}:n<Y,
 \ \epsilon_n\ne\epsilon_{n+1}\}
\tag{7}
\]

count phase switches before the real position `Y`.

## Theorem 1 -- exact physical gap valuation

Both symbols occur infinitely often.  If `h<h'` are consecutive occurrence
positions of `s`, then

\[
 \boxed{
 v_2(5M_h-4+3s)=2(h'-h).
 }
\tag{8}
\]

Consequently every same-symbol gap `g=h'-h` satisfies the strict bound

\[
 \boxed{
 g<\delta h+C.
 }
\tag{9}
\]

The same constant works for both symbols.

### Proof

First suppose that the code were eventually all zero, beginning at position
`n`.  Iterating (2) would give

\[
 M_{n+k}={5^kM_n\over4^k}\in\mathbf Z
 \qquad(k\ge0).
\tag{10}
\]

Thus `4^k` would divide the fixed positive integer `M_n` for every `k`, which
is impossible.  If the code were eventually all one, then

\[
 M_{n+k}-1={5^k(M_n-1)\over4^k}\in\mathbf Z
 \qquad(k\ge0),
\tag{11}
\]

forcing `M_n=1`, contrary to `M_n>=4`.  Hence both occurrence sequences in
(5) are infinite.

Fix consecutive occurrences `h<h'` of `s`, and put `g=h'-h`.  Every intervening
symbol is `1-s`.  Use the coordinate

\[
 Z_n=M_n-(1-s).
\tag{12}
\]

The transition at the first occurrence gives

\[
 4Z_{h+1}=5M_h-4+3s.
\tag{13}
\]

At each of the following `g-1` positions, the emitted symbol is `1-s`, so

\[
 4Z_{n+1}=5Z_n
 \qquad(h+1\le n<h').
\tag{14}
\]

At the final occurrence,

\[
 Z_{h'}\equiv s-(1-s)=2s-1\pmod4,
\tag{15}
\]

so `Z_(h')` is odd.  Equations (14)--(15) therefore give

\[
 v_2(Z_{h+1})=2(g-1).
\tag{16}
\]

Equation (13) proves (8).

The recurrence (2) also gives

\[
 M_h\le M_0(5/4)^h.
\tag{17}
\]

The integer in (8) is positive: if `s=0`, then `M_h` is a positive multiple
of four; if `s=1`, then `M_h>=5`.  Hence

\[
 4^g
 \le 5M_h-4+3s
 <5M_h
 \le5M_0(5/4)^h.
\tag{18}
\]

Taking logarithms base four proves the strict inequality (9). **QED**

## Theorem 2 -- two-symbol support and switch floors

For either `s in {0,1}` and all real `Y>=X>=h_0^(s)`, one has

\[
 \boxed{
 N_s(Y)-N_s(X)
 \ge
 \left\lfloor
 \log_\alpha{Y+\rho\over X+\rho}
 \right\rfloor.
 }
\tag{19}
\]

In particular,

\[
 \boxed{
 N_s(Y)
 \ge
 1+\left\lfloor
 \log_\alpha{Y+\rho\over h_0^{(s)}+\rho}
 \right\rfloor
 }
 \qquad(Y\ge h_0^{(s)}),
\tag{20}
\]

and

\[
 \boxed{
 \liminf_{Y\to\infty}{N_s(Y)\over\log Y}
 \ge {1\over\log\alpha}
 =6.70013449289\ldots .
 }
\tag{21}
\]

This is also a shell-by-shell oscillation statement.  Put

\[
 H=\max\{h_0^{(0)},h_0^{(1)}\},
 \qquad
 x_k=\alpha^k(H+\rho)-\rho.
\tag{22}
\]

Every open shell

\[
 \boxed{(x_k,x_{k+1})}
\tag{23}
\]

contains at least one occurrence of each symbol and at least one phase switch.
The switches obtained from different shells are distinct.  Therefore, for
every real `Y>=H`,

\[
 \boxed{
 S(Y)
 \ge
 \left\lfloor
 \log_\alpha{Y+\rho\over H+\rho}
 \right\rfloor,
 }
\tag{24}
\]

and

\[
 \boxed{
 \liminf_{Y\to\infty}{S(Y)\over\log Y}
 \ge {1\over\log\alpha}
 =6.70013449289\ldots .
 }
\tag{25}
\]

If

\[
 0\le r_0<r_1<r_2<\cdots
\tag{26}
\]

are the switch positions, then for every `k>=1`,

\[
 \boxed{r_{k-1}<x_k,}
\tag{27}
\]

and consequently

\[
 \boxed{
 \limsup_{k\to\infty}r_k^{1/k}\le\alpha=\log_4 5.
 }
\tag{28}
\]

### Proof

Equation (9) is

\[
 h^{(s)}_{j+1}<\alpha h^{(s)}_j+C.
\tag{29}
\]

Since `C=delta*rho` and `alpha=1+delta`, exact induction gives

\[
 h^{(s)}_{j+n}+\rho
 <\alpha^n(h^{(s)}_j+\rho)
 \qquad(n\ge1).
\tag{30}
\]

For `X>=h_0^(s)`, choose the last occurrence `h_j^(s)<=X`.  If

\[
 1\le n\le
 \left\lfloor
 \log_\alpha{Y+\rho\over X+\rho}
 \right\rfloor,
\tag{31}
\]

then (30) places `h_(j+n)^(s)` strictly below
`alpha^n(X+rho)-rho`, which is at most `Y`.  These are distinct occurrences
in `(X,Y]`, proving (19).  Notice that the strict inequality handles the case
where the logarithm in (31) is an integer; the floor endpoint is valid.
Equations (20)--(21) follow.

For any real `X>=h_0^(s)`, the next occurrence of `s` after `X` belongs to

\[
 (X,\alpha X+C).
\tag{32}
\]

Apply this separately to `s=0,1` with `X=x_k`.  Because

\[
 x_{k+1}=\alpha x_k+C,
\tag{33}
\]

the shell (23) contains positions carrying both symbols.  Between two such
positions there is a switch whose index also lies strictly inside that shell.
The open shells are pairwise disjoint, so no switch is counted for two shells.

If

\[
 K=\left\lfloor
 \log_\alpha{Y+\rho\over H+\rho}
 \right\rfloor,
\tag{34}
\]

then `x_K<=Y`.  The first `K` shells therefore contribute `K` distinct
switches with indices below `Y`, proving (24).  Taking `Y=x_k` proves (27),
and (25), (28) follow by taking logarithms. **QED**

## Theorem 3 -- the finite physical phase language is full

Every finite binary word occurs as the initial phase word of infinitely many
positive physical chart segments.

More precisely, fix

\[
 w=\epsilon_0\epsilon_1\cdots\epsilon_{L-1}
 \in\{0,1\}^L
\tag{35}
\]

and define

\[
 D_k=\sum_{j=0}^{k-1}\epsilon_j4^j5^{k-1-j}
 \qquad(1\le k\le L),
 \qquad D_0=0.
\tag{36}
\]

There is one residue class

\[
 \boxed{
 M_0\equiv5^{-L}D_L\pmod {4^L}
 }
\tag{37}
\]

whose sufficiently large positive representatives all generate the word `w`
for their first `L` chart steps.

### Proof

Choose `M_0` in (37).  For every `k<=L`, reduction of `D_L` modulo `4^k`
gives

\[
 D_L\equiv5^{L-k}D_k\pmod {4^k}.
\tag{38}
\]

Since five is a unit modulo every power of four, (37)--(38) imply

\[
 5^kM_0\equiv D_k\pmod {4^k}.
\tag{39}
\]

Thus

\[
 M_k={5^kM_0-D_k\over4^k}
\tag{40}
\]

is an integer.  The identity

\[
 D_{k+1}=5D_k+\epsilon_k4^k
\tag{41}
\]

and integrality at level `k+1` give

\[
 5M_k\equiv\epsilon_k\pmod4.
\tag{42}
\]

As `5` is congruent to one modulo four,

\[
 M_k\equiv\epsilon_k\pmod4,
 \qquad
 M_{k+1}={5M_k-\epsilon_k\over4}.
\tag{43}
\]

Hence the first `L` emitted symbols are exactly `w`.  Replacing `M_0` by
`M_0+t4^L` changes every `M_k` by the positive integer
`t5^k4^(L-k)`.  All `M_k` are therefore at least four for every sufficiently
large `t`.  Then `A_k=M_k-2>0`, and (43) is a positive physical chart segment.
There are infinitely many such `t`. **QED**

## Quantitative grammar criterion

Theorems 1--2 give output-statistic tests for any proposed exact connector or
representation grammar.  No infinite output word can be a positive chart
survivor if it satisfies any of the following:

\[
 \sup_j\{h^{(s)}_{j+1}-h^{(s)}_j-\delta h^{(s)}_j\}=+\infty
 \quad\hbox{for either }s,
\tag{44}
\]

\[
 \liminf_{Y\to\infty}{N_s(Y)\over\log Y}
 <{1\over\log\alpha}
 \quad\hbox{for either }s,
\tag{45}
\]

\[
 \liminf_{Y\to\infty}{S(Y)\over\log Y}
 <{1\over\log\alpha},
\tag{46}
\]

or

\[
 \limsup_{k\to\infty}r_k^{1/k}>\alpha.
\tag{47}
\]

For example, a run-length grammar whose successive switch locations satisfy

\[
 r_k\ge K\lambda^k
 \quad\hbox{eventually for some }K>0,
 \quad\lambda>\log_4 5,
\tag{48}
\]

cannot encode a positive survivor.  These hypotheses are native, checkable
properties of the emitted physical phase word; they do not require comparing
an infinite real limit with a `2`-adic limit.

Theorem 3 states the complementary no-go precisely.  No fixed forbidden
finite phase block can supply one of these asymptotic upper bounds, because
the physical language obtained while the positive root is allowed to vary is
the full binary language at every finite depth.  A successful grammar bound
must use coherence of all prefixes for one fixed ordinary root, or retain
root/carry information that grows with the depth.  Theorem 3 does **not** say
that one positive root realizes every prefix of an arbitrary infinite word.

## Dependency and novelty audit

- `PR35/T-8802` supplies exactly (1)--(2) and the physical interpretation.
  The valuation identity (8) and the common two-symbol constant in (9) are
  derived directly from that recurrence.
- Local `T-9819` gives multiplicative support floors for a rational completion.
  Applied to the `1` support of a chart survivor, its constant is
  `log_4(5(M_0+1))`; applied to the complement it is `log_4(5M_0)`.
  The physical valuation proof improves the first constant to the same
  `log_4(5M_0)` used for the complement, then couples the two floors into the
  switch-shell theorem (23)--(28).
- `PR35/T-8803` gives a factor-complexity slope
  `1/log_4(5/4)=6.212567...`.  The support/switch coefficient here is the
  different constant
  `1/log(log_4 5)=6.700134...`; the two theorems measure different axes.
- `PR35/T-8805` proves that phase-only connector gain is a coboundary.  It
  supplies no upper bound on phase switches.  Equations (44)--(48) identify
  the quantitative upper bound that a richer connector grammar would need.
- Under `PR35/T-8806`, the bottom digit is `1-epsilon_n`.  Thus Theorems 1--2
  apply equally to the low-digit bottom word, exchanging the names of the two
  supports.  The finite-prefix construction (37) is the explicit positive
  cylinder form of that tree interface.
- `PR35/T-8807` concerns the `2`-adic dimension of all completions.  It gives
  no ordinary-section support or switch bound.
- `PR20/T-9403` and `T-9405` give copy-overlap and factor-complexity
  restrictions for ordinary expanding-chart codes.  They do not bound the
  number or placement of occurrences of either individual digit.
- No external theorem or finite computation is used.

## Gap and adversarial audit

- The strict sign in (9) comes from the strict inequality
  `5M_h-4+3s<5M_h`.  The count floors remain valid at exact logarithmic
  endpoints because the iterated support bound is also strict.
- Both symbols are proved infinite before their occurrence sequences are used.
  Eventual constancy is not silently excluded by an aperiodicity assumption.
- The switch proof first finds both symbols inside one open shell and only then
  selects a switch between them.  Disjoint open shells prevent double counting.
- Logarithmic oscillation is necessary, not sufficient.  A word may easily
  satisfy (21) and (25) without representing any ordinary root.
- The full finite language is compatible with failure of infinite ordinary
  coherence: the realizing residue class changes with the requested word and
  depth.
- A small bounded search can find a longest prefix only relative to its root
  cutoff.  Theorem 3 explains why no bounded prefix length is a universal
  obstruction.
- Nothing here proves that a positive chart survivor exists or that every
  possible unbounded-state grammar fails.

## Suggested next attack

Attach to a proposed connector grammar the cumulative locations of its phase
changes.  Prove either a super-`log_4(5)` growth base for those locations, or a
minority-symbol/switch count below `1/log(log_4 5)` per logarithmic scale.
Theorem 3 shows that this estimate must transport one-root residue or carry
coherence across depths; a finite forbidden-block census cannot provide it.
