# T-9819 -- Rational completion supports are multiplicatively syndetic

Claim ID: `T-9819`
Title: A rational bounded-digit completion has logarithmically many support points at every multiplicative scale
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave16-completion-cold-review`
Reviewing agents: `gpt56-synthesis-01-wave14-period-ten`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `T-9816` for the binary `64/81` precursor; elementary finite-rational height; branch-qualified `PR35/T-8802`, `T-8803`, and `T-8807` at `6bb647ad13507d8b478ae990d3e1d1b95aea1f17` only for the `4/5` chart translation and novelty audit
Scope: bounded integral digits of a common narrow `p`-adic order band for every contracting completion ratio `p^a/Q`; explicit `64/81`, positive-stack, and `4/5` consequences
Related counterexample candidates: issue #4 M1 and issue #26 `5x+1` chart survivors; no `K-####` candidate

## General theorem

Let `p` be a prime, let `a>=1`, and put

\[
 R=p^a,
 \qquad
 Q>R,
 \qquad
 p\nmid Q,
 \qquad
 T={R\over Q}.
\tag{1}
\]

Let

\[
 0\le h_0<h_1<h_2<\cdots
\tag{2}
\]

and let `c_j` be nonzero integers satisfying

\[
 |c_j|\le D,
 \qquad
 \nu_-\le v_p(c_j)\le\nu_+,
 \qquad
 \nu_+-\nu_-<a.
\tag{3}
\]

Consider the convergent `p`-adic series

\[
 \Psi=\sum_{j\ge0}c_jT^{h_j}.
\tag{4}
\]

Assume that its `p`-adic value is rational, and write it in lowest terms as

\[
 \Psi={A\over B},
 \qquad
 A\in\mathbf Z,
 \quad B\in\mathbf Z_{>0}.
\tag{5}
\]

Then `p` does not divide `B`.  Define

\[
 K=|A|+{DBQ\over Q-R},
 \qquad
 \nu_j=v_p(c_j).
\tag{6}
\]

For every `j>=0`, one has the exact first-omitted-term height inequality

\[
 \boxed{
 p^{ah_{j+1}+\nu_{j+1}}
 \le KQ^{h_j}.
 }
\tag{7}
\]

Put

\[
 \alpha=\log_R Q>1,
 \qquad
 \delta=\alpha-1=\log_R{Q\over R},
\tag{8}
\]

and `g_j=h_(j+1)-h_j`.  The digit-sensitive and uniform gap bounds are

\[
 \boxed{
 g_j\le\delta h_j+C_j,
 \qquad
 C_j={\log_pK-\nu_{j+1}\over a},
 }
\tag{9}
\]

and

\[
 \boxed{
 g_j\le\delta h_j+C,
 \qquad
 C={\log_pK-\nu_-\over a}.
 }
\tag{10}
\]

The exact induction retaining the individual digit orders is

\[
 h_{j+n}
 \le
 \alpha^nh_j+
 \sum_{r=0}^{n-1}\alpha^{n-1-r}C_{j+r}.
\tag{11}
\]

In particular, with

\[
 \rho={C\over\delta},
\tag{12}
\]

the closed uniform form is

\[
 \boxed{
 h_{j+n}\le
 \alpha^n(h_j+\rho)-\rho
 }
 \qquad(j,n\ge0).
\tag{13}
\]

The constant `C` is positive; in fact `C>h_0`, so `rho` is well-defined and
positive.

Let

\[
 N(X)=\#\{j:h_j\le X\}.
\tag{14}
\]

Then the support is multiplicatively syndetic in the following exact sense.
For every real `Y>=X>=h_0`,

\[
 \boxed{
 N(Y)-N(X)
 \ge
 \left\lfloor
 \log_\alpha {Y+\rho\over X+\rho}
 \right\rfloor.
 }
\tag{15}
\]

Equivalently, every interval

\[
 \boxed{(X,\alpha X+C]}
\tag{16}
\]

with `X>=h_0` contains a support point.  Taking `X=h_0` in (15) gives

\[
 \boxed{
 N(Y)\ge
 1+\left\lfloor
 \log_\alpha {Y+\rho\over h_0+\rho}
 \right\rfloor
 }
 \qquad(Y\ge h_0).
\tag{17}
\]

Consequently,

\[
 \boxed{
 \liminf_{Y\to\infty}{N(Y)\over\log Y}
 \ge {1\over\log\alpha},
 }
\tag{18}
\]

where the logarithms in (18) are natural, and

\[
 \boxed{
 \limsup_{j\to\infty}h_j^{1/j}\le\alpha,
 \qquad
 \limsup_{j\to\infty}{h_{j+1}\over h_j}\le\alpha.
 }
\tag{19}
\]

Consequently, each of

\[
 \sup_j\{g_j-\delta h_j\}=+\infty,
 \qquad
 \limsup_{j\to\infty}h_j^{1/j}>\alpha,
 \qquad
 \limsup_{j\to\infty}{h_{j+1}\over h_j}>\alpha
\tag{20}
\]

is a rational-value-independent irrationality criterion.  The same is true
if

\[
 \liminf_{Y\to\infty}{N(Y)\over\log Y}
 <{1\over\log\alpha}
\tag{20a}
\]

holds.  If a particular rational value `A/B` is proposed, a single violation
of (7), (13), or (15) with its explicit constant already refutes it.

## Proof

The series belongs to `Z_p`, since its term valuations tend to infinity.
Thus a rational value in lowest terms has `p` prime to `B`.

Let

\[
 S_j=\sum_{k=0}^{j}c_kT^{h_k},
 \qquad
 E_j=\Psi-S_j.
\tag{21}
\]

The first term of `E_j` has valuation

\[
 v_p(c_{j+1}T^{h_{j+1}})=\nu_{j+1}+ah_{j+1}.
\tag{22}
\]

For every `k>=j+2`, strict increase of the support and (3) give

\[
 \begin{aligned}
 v_p(c_kT^{h_k})
 &\ge \nu_-+a(h_{j+1}+1)\\
 &>\nu_++ah_{j+1}\\
 &\ge\nu_{j+1}+ah_{j+1}.
 \end{aligned}
\tag{23}
\]

The first omitted term is therefore the unique term of least valuation in the
tail.  The ultrametric inequality is exact, so

\[
 \boxed{v_p(E_j)=ah_{j+1}+\nu_{j+1}.}
\tag{24}
\]

In particular, `E_j` is nonzero.  The same unique-minimum argument applied to
the whole series below also shows that `Psi` is nonzero.  The ordinary
denominator of `S_j` divides `Q^(h_j)`.  If `E_j=N_j/D_j` in lowest terms with
`D_j>0`, then

\[
 D_j\mid BQ^{h_j}.
\tag{25}
\]

Equations (24)--(25) imply

\[
 |E_j|
 ={ |N_j|\over D_j}
 \ge {p^{ah_{j+1}+\nu_{j+1}}\over BQ^{h_j}}
\tag{26}
\]

in the ordinary real absolute value.  On the other hand, only the finite
rational sum `S_j` is estimated in the real embedding:

\[
 |S_j|
 \le D\sum_{n\ge0}T^n
 ={DQ\over Q-R}.
\tag{27}
\]

Since `E_j=A/B-S_j`,

\[
 |E_j|\le {|A|\over B}+{DQ\over Q-R}.
\tag{28}
\]

Combining (26) and (28) proves (7).  Taking its base-`p` logarithm, dividing
by `a`, and subtracting `h_j` proves (9); (10) follows from
`nu_(j+1)>=nu_-`.

The same unique-minimum argument at the first term of the whole series gives

\[
 v_p(A)=v_p(\Psi)=ah_0+\nu_0.
\tag{29}
\]

Thus `|A|>=p^(ah_0+nu_0)`, while `K>|A|`.  It follows that

\[
 C={\log_pK-\nu_-\over a}>h_0,
\tag{30}
\]

as claimed.

Equation (10) is the affine recurrence

\[
 h_{j+1}\le\alpha h_j+C.
\tag{31}
\]

Direct induction gives both the weighted form (11) and

\[
 h_{j+n}+\rho\le\alpha^n(h_j+\rho),
\tag{32}
\]

which is (13).

For (15), choose the last support point `h_r<=X`.  Formula (13) gives

\[
 h_{r+n}\le\alpha^n(X+\rho)-\rho.
\tag{33}
\]

Every integer

\[
 1\le n\le
 \left\lfloor
 \log_\alpha{Y+\rho\over X+\rho}
 \right\rfloor
\tag{34}
\]

therefore supplies a distinct support point in `(X,Y]`.  This proves (15),
and its case `Y=alpha*X+C` proves (16).  Equations (17)--(19) follow from
(13), (15), `N(h_0)=1`, and elementary logarithms.  **QED**

## The `64/81` binary and odd-digit consequences

Take

\[
 p=2,
 \quad a=6,
 \quad R=64,
 \quad Q=81.
\tag{35}
\]

For binary digits, `D=1` and `nu_-=nu_+=0`.  Then

\[
 \alpha_{64/81}=\log_{64}81
 =1.056641667147437458\ldots,
\tag{36}
\]

\[
 \delta_{64/81}=\log_{64}{81\over64}
 =0.056641667147437458\ldots,
\tag{37}
\]

and

\[
 C_{64/81}
 ={1\over6}\log_2\left(|A|+{81\over17}B\right).
\tag{38}
\]

Equation (7) is exactly the height inequality of `T-9816`, while (13)--(19)
are its global quantitative closure.  In particular,

\[
 \boxed{
 \liminf_{Y\to\infty}{N(Y)\over\log Y}
 \ge
 {1\over\log(\log_{64}81)}
 =18.1502565060\ldots .
 }
\tag{39}
\]

More generally, if every nonzero `64/81` digit is odd and has absolute value
at most `D`, all conclusions remain valid with the exact constant

\[
 \boxed{
 C_D={1\over6}\log_2
 \left(|A|+{81D\over17}B\right).
 }
\tag{40}
\]

The signs may be arbitrary.  Positivity of the infinite real shadow is never
used.

## Positive-stack increment directives

Use the standard positive-stack notation

\[
 m_0\ge0,
 \qquad
 m_t=m_0+\sum_{i=1}^{t}d_i,
 \qquad d_i\ge1,
\tag{41}
\]

\[
 \ell_t=9m_t+1,
 \qquad
 H_0=0,
 \qquad
 H_j=\sum_{i=1}^{j}\ell_i.
\tag{42}
\]

Suppose the binary stack value `sum_(j>=0)T^(H_j)=A/B` is rational, and let
`C=C_(64/81)` be (38).  Since the support starts at `H_0=0`, (13) and the
one-step bound give

\[
 \boxed{
 H_j\le {C\over\delta}(\alpha^j-1),
 \qquad
 \ell_{j+1}\le C\alpha^j,
 }
\tag{43}
\]

where `alpha=alpha_(64/81)` and `delta=delta_(64/81)`.  Hence

\[
 \boxed{
 m_{j+1}\le {C\alpha^j-1\over9},
 \qquad
 \sum_{i=1}^{j+1}d_i
 \le {C\alpha^j-1\over9}-m_0.
 }
\tag{44}
\]

There is also a history-sensitive directive ceiling.  Substituting

\[
 H_j=9\sum_{i=1}^{j}m_i+j,
 \qquad
 \ell_{j+1}=9m_{j+1}+1
\tag{45}
\]

in (10) gives

\[
 \boxed{
 d_{j+1}
 \le
 \delta\sum_{i=1}^{j}m_i-m_j
 +{\delta j+C-1\over9}.
 }
\tag{46}
\]

Since positivity gives `m_j>=m_0+j`, (44) also yields the purely indexed
bound

\[
 \boxed{
 d_{j+1}
 \le {C\alpha^j-1\over9}-m_0-j.
 }
\tag{47}
\]

Thus each of

\[
 \sup_j{d_{j+1}\over\alpha^j}=+\infty,
 \qquad
 \limsup_{j\to\infty}d_j^{1/j}>\alpha,
\tag{48}
\]

is a sufficient irrationality condition for the stack value.  These are
directive-growth criteria rather than a restatement in the cumulative heights.

## Exact `4/5` chart corollary

Take

\[
 p=2,
 \quad a=2,
 \quad R=4,
 \quad Q=5,
 \quad D=1,
 \quad \nu_-=\nu_+=0.
\tag{49}
\]

If

\[
 \Psi_{4/5}=\sum_{j\ge0}(4/5)^{h_j}={A\over B}
\tag{50}
\]

has infinite binary support and is rational in `Q_2`, then

\[
 \boxed{
 4^{h_{j+1}}
 \le (|A|+5B)5^{h_j},
 }
\tag{51}
\]

and

\[
 \boxed{
 g_j
 \le
 \log_4(5/4)h_j+\log_4(|A|+5B).
 }
\tag{52}
\]

Here

\[
 \alpha_{4/5}=\log_4 5
 =1.160964047443681\ldots,
 \qquad
 \delta_{4/5}=0.160964047443681\ldots .
\tag{53}
\]

Equations (13)--(19) apply with
`C=log_4(|A|+5B)`.  In particular,

\[
 \boxed{
 \liminf_{Y\to\infty}{N(Y)\over\log Y}
 \ge
 {1\over\log(\log_4 5)}
 =6.70013449289\ldots .
 }
\tag{54}
\]

At live PR #35 head `6bb647a`, `T-8802` proves that an ordinary positive seed
`x` remaining forever in the exact `4 -> 5` chart has

\[
 M=x+2={1\over5}\sum_{j\ge0}\epsilon_j(4/5)^j.
\tag{55}
\]

Such a directive necessarily has infinite support.  Indeed, if its last `1`
were at `h`, the numerator of (55) over `5^(h+1)` would be congruent to
`4^h` modulo `5`, so it could not be the integer `M`; the empty support gives
`M=0`, not `x>0`.

For the support `h_j` of its `1` digits, (51)--(52) specialize further to

\[
 \boxed{
 4^{h_{j+1}}
 \le 5(M+1)5^{h_j},
 \qquad
 g_j\le\log_4(5/4)h_j+\log_4(5(x+3)).
 }
\tag{56}
\]

Therefore every ordinary positive `4 -> 5` chart survivor obeys the same
multiplicative-syndeticity and support-count bounds with
`C=log_4(5(x+3))`.

## Dependency and novelty audit

- `T-9816` proves the binary `64/81` one-step inequality (7).  The new content
  here is the exact affine induction, support points in every multiplicative
  interval, the local count (15), the asymptotic density constant (18), the
  directive ceilings (43)--(48), and the bounded signed digit theorem.
- Local `L-9803` supplies an abstract one-step product-formula wedge.  It does
  not iterate that wedge into local support counts, nor treat the digit-order
  condition that makes every omitted tail exact.
- Live `PR20/T-9411` at `14f06d252c3ef56fb9a69ea34c61edaa578d02a1`
  treats direct truncations for bounded-increment sparse stacks and finds a
  subcritical limiting exponent.  It gives neither arbitrary-support count
  bounds nor the exponential directive ceilings above.
- Live `PR20/R-9409` at the same head forbids identifying an ordinary limit
  with a `2`-adic limit without an additional height bound.  The proof here
  uses only the finite rational `S_j` and the fixed rational difference
  `A/B-S_j`; it makes no cross-completion identification.
- `PR35/T-8802` supplies exactly the normalization (55).  The factor-complexity
  theorem `PR35/T-8803` already has the same critical slope
  `log_4(5/4)` in a repeated-factor inequality.  Applying it to two shifted
  all-zero blocks also gives a relative support-gap bound with a larger
  additive constant.  Thus the slope in (52) is corroboration, not claimed as
  wholly new.  Equations (51), (54), and (56) give the sharper
  first-omitted-tail constant and the new support-count formulation.
- `PR35/T-8807` computes prefix-cylinder dimension for all `4/5` directives,
  including arbitrarily sparse ones.  It neither implies nor is implied by the
  rational-section support-density bound here.
- No external theorem or computation is used in the proof.  The displayed
  decimals are informational only.

## Sharpness, adversarial examples, and scope

- The order-band threshold in (3) is sharp for this mechanism.  At width
  exactly `a`, the two adjacent digits

  \[
  R T^H-QT^{H+1}=0
  \tag{57}
  \]

  cancel exactly.  Choosing arbitrarily separated blocks with coefficient
  `R` at `H_n` and `-Q` at `H_n+1` gives a bounded-digit infinite series equal
  to zero with arbitrarily large support gaps.  For `64/81` these digits are
  `64,-81`; for `4/5` they are `4,-5`.  Some control on leading digit order is
  therefore essential.
- The affine iteration constant is exact as a consequence of (10).  Real
  sequences satisfying `u_(j+1)=alpha*u_j+C`, and integer sequences obtained
  by flooring after a sufficiently large start, have growth base `alpha` and
  counting order `log_alpha Y`.  Hence neither the base in (13) nor the
  coefficient in (18) can be improved using the one-step recurrence alone.
  This does **not** assert that a rational digit series attains the boundary.
- Dense rational examples exist: `h_j=j`, `c_j=1` gives
  `Psi=Q/(Q-R)`.  Thus logarithmic support density is necessary, not
  sufficient, for rationality.
- Infinite support is essential.  A finite digit polynomial is rational and
  has no next support point after its last digit.
- The rational-height constant depends on the fixed value `A/B`; no uniform
  constant over all rational values is asserted.
- The stack bounds allow bounded and periodic positive directives, whose
  cumulative heights grow only quadratically.  They do not settle that
  frontier.
- Nothing here constructs an ordinary survivor, a divergent orbit, or a
  `K-####` candidate.

## Suggested next attack

Combine the local support count (15) with an independent finite-state or
factor-complexity upper bound for the physical output code.  For the `4/5`
chart, a connector grammar forcing fewer than
`1/log(log_4 5)` support points per logarithmic scale would rule out every
positive ordinary survivor without any comparison of infinite real and
`2`-adic limits.
