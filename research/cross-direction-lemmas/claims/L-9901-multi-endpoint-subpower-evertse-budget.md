# L-9901 -- Multi-endpoint Evertse budget with subpower primitive loss

Claim ID: `L-9901`
Title: Fixed-rank zero sums remain Evertse-finite under multiple moving endpoints and subcritical primitive-height loss
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave14-cap-cell-hierarchy`
Reviewing agents: `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `L-9900`; Evertse 1984, Corollary 1
Scope: fixed-dimensional rational-integer zero sums with fixed internal prime support and possibly unbounded normalization gcd
Related claims: local `T-9828`; live PR #33

## Definitions

For a finite rational-prime set `S_0` and nonzero integer `a`, put

\[
 \operatorname{out}_{S_0}(a)
 =|a|\prod_{p\in S_0}|a|_p.
\tag{1}
\]

Fix integers `q>=1` and `r>=0`, with `q+r>=2`.  Here `q` is the fixed
number of moving endpoints and `r` is the number of internal `S_0`-unit
coordinates.

For each `m`, let

\[
 a_m=(e_{m,1},\ldots,e_{m,q},s_{m,1},\ldots,s_{m,r})
 \in(\mathbf Z\setminus\{0\})^{q+r}
\tag{2}
\]

be a zero-sum tuple.  Put

\[
 H_m=\max_k|a_{m,k}|,
 \qquad
 g_m=\gcd_k|a_{m,k}|,
 \qquad
 x_m={a_m\over g_m}.
\tag{3}
\]

Assume `H_m->infinity`.  Define the combined raw endpoint content

\[
 B_m=\prod_{i=1}^{q}\operatorname{out}_{S_0}(e_{m,i}),
\tag{4}
\]

and the two marginal exponents

\[
 \gamma=limsup_{m\to\infty}{\log g_m\over\log H_m}<1,
\tag{5}
\]

\[
 \Theta=limsup_{m\to\infty}{\log B_m\over\log H_m}.
\tag{6}
\]

## Theorem

Suppose:

1. every internal coordinate is an `S_0`-unit:

   \[
   \operatorname{out}_{S_0}(s_{m,j})=1;
   \tag{7}
   \]

2. the zero sum is nondegenerate:

   \[
   \sum_{k\in J}a_{m,k}\ne0
   \tag{8}
   \]

   for every nonempty proper coordinate set `J`; it is sufficient that
   exactly one coordinate be positive and all others negative; and

3. for some fixed `0<d<1`,

   \[
   \boxed{\Theta<d(1-\gamma).}
   \tag{9}
   \]

Then all sufficiently late primitive tuples `x_m` are `(1,d,S_0)`-admissible
in Evertse's sense.  Moreover, their primitive heights tend to infinity, so
they contain infinitely many distinct projective points.  Consequently no
infinite family satisfying these hypotheses exists.

Equivalently, there exists some usable Evertse exponent `d<1` if and only if

\[
 \boxed{\Theta<1-\gamma.}
\tag{10}
\]

## Proof

### 1. Primitive outside-prime content

The primitive tuple has

\[
 \|x_m\|={H_m\over g_m}.
\tag{11}
\]

For every coordinate,

\[
 \operatorname{out}_{S_0}(x_{m,k})
 ={\operatorname{out}_{S_0}(a_{m,k})
   \over\operatorname{out}_{S_0}(g_m)}
 \le\operatorname{out}_{S_0}(a_{m,k}).
\tag{12}
\]

If `r>=1`, then `g_m` divides an internal `S_0`-unit, so `g_m` itself is
supported on `S_0` and equality holds in (12).  In either case, normalization
cannot increase outside-`S_0` content.  Therefore

\[
 \prod_k\operatorname{out}_{S_0}(x_{m,k})\le B_m.
\tag{13}
\]

### 2. Absorb the unbounded gcd

Put

\[
 \Delta=d(1-\gamma)-\Theta>0.
\tag{14}
\]

Choose `eta>0` such that

\[
 \eta<1-\gamma,
 \qquad
 (1+d)\eta<\Delta.
\tag{15}
\]

By the definitions of `gamma` and `Theta`, for all sufficiently large `m`,

\[
 g_m\le H_m^{\gamma+\eta},
 \qquad
 B_m\le H_m^{\Theta+\eta}.
\tag{16}
\]

Hence

\[
 \|x_m\|^d
 =\left({H_m\over g_m}\right)^d
 \ge H_m^{d(1-\gamma-\eta)}.
\tag{17}
\]

Condition (15) gives

\[
 \Theta+\eta<d(1-\gamma-\eta),
\tag{18}
\]

and thus

\[
 B_m
 \le H_m^{\Theta+\eta}
 \le H_m^{d(1-\gamma-\eta)}
 \le\|x_m\|^d.
\tag{19}
\]

Combining (13) and (19),

\[
 \boxed{
 \prod_k\operatorname{out}_{S_0}(x_{m,k})
 \le\|x_m\|^d.}
\tag{20}
\]

Thus the Evertse constant is eventually exactly `c=1`, despite `g_m` being
unbounded.

### 3. Projective distinctness

Choose `eta<1-gamma` as above.  Equation (16) also gives

\[
 \|x_m\|\ge H_m^{1-\gamma-\eta}\longrightarrow\infty.
\tag{21}
\]

A rational projective point has only two primitive integer representatives,
differing by global sign, and hence has one fixed primitive height.  Therefore
(21) already forces infinitely many distinct projective points.

A separate projective-ratio certificate remains valid and may be preferable
in applications.  If fixed coordinates `u,v` have pairwise distinct ratios

\[
 {a_{m,u}\over a_{m,v}},
\tag{22}
\]

or valuations in pairwise disjoint intervals, normalization cancels from the
ratio and gives pairwise projective distinctness directly.  Under (5), this
extra separator is logically redundant.

### 4. Evertse contradiction

The rank `q+r`, dimension `n=q+r-1`, prime set `S_0`, and constants
`c=1,d<1` are fixed.  The tuples are primitive, nondegenerate zero sums
satisfying (20), and infinitely many projective points occur.  Evertse's
Corollary 1 allows only finitely many.  Contradiction. **QED**

## Existence of an admissible exponent

Since `gamma<1`, a number `d` satisfying

\[
 {\Theta\over1-\gamma}<d<1
\tag{23}
\]

exists exactly when

\[
 \Theta<1-\gamma.
\tag{24}
\]

Thus (24) is the sharp sufficient inequality expressible solely through the
two marginal limsup exponents.

For individual endpoint exponents

\[
 \theta_i=limsup
 {\log\operatorname{out}_{S_0}(e_{m,i})\over\log H_m},
\tag{25}
\]

the convenient sufficient condition is

\[
 \sum_{i=1}^{q}\theta_i<d(1-\gamma),
\tag{26}
\]

because `Theta<=sum_i theta_i`.

## Fixed constants at exponent equality

Suppose stronger uniform bounds are known:

\[
 g_m\le C_gH_m^\gamma,
 \qquad
 B_m\le C_BH_m^\Theta,
\tag{27}
\]

and

\[
 \Theta\le d(1-\gamma)
\tag{28}
\]

for one fixed `d<1`.  Then

\[
 \|x_m\|^d\ge{H_m^{d(1-\gamma)}\over C_g^d},
\tag{29}
\]

so

\[
 B_m\le C_BC_g^d\|x_m\|^d.
\tag{30}
\]

Evertse therefore applies with the fixed constant

\[
 \boxed{c=C_BC_g^d.}
\tag{31}
\]

Strict inequality in (9) is what upgrades unknown limsup constants to
eventual `c=1`.  Equality is permissible when uniform multiplicative
constants are supplied.

## Exact joint criterion

The marginal condition can be conservative if large endpoint content and
large gcd occur on different subsequences.  The exact normalized-height
invariant is

\[
 \Xi=\limsup_{m\to\infty}
 {\log B_m\over\log(H_m/g_m)}.
\tag{32}
\]

The direct criterion is

\[
 \Xi<d<1.
\tag{33}
\]

From the separate marginal exponents one always has

\[
 \Xi\le{\Theta\over1-\gamma},
\tag{34}
\]

which recovers (9).  Thus `Theta<1-gamma` is sharp given only `Theta` and
`gamma`, while (33) may prove more when their peaks are anticorrelated.

## Sharp boundary counterexample

Fix `0<=gamma_0<1`, take `S_0={2}`, and put

\[
 N_m=2^m,
 \qquad
 h_m=\left\lfloor{\gamma_0\over1-\gamma_0}m\right\rfloor,
 \qquad
 G_m=2^{h_m}.
\tag{35}
\]

Consider the three-coordinate tuple

\[
 a_m=\bigl(G_mN_m,-G_m(N_m-1),-G_m\bigr).
\tag{36}
\]

It has exactly one positive coordinate, total sum zero, no proper vanishing
subsum, two moving endpoints, one internal `{2}`-unit, gcd `g_m=G_m`, raw
height `H_m=G_mN_m`, and projective separator

\[
 {G_mN_m\over-G_m}=-N_m.
\tag{37}
\]

Its exponents are

\[
 \lim{\log g_m\over\log H_m}=\gamma_0,
\tag{38}
\]

while

\[
 \begin{aligned}
 B_m
 &=\operatorname{out}_{\{2\}}(G_mN_m)
   \operatorname{out}_{\{2\}}(G_m(N_m-1))\\
 &=N_m-1,
 \end{aligned}
\tag{39}
\]

so

\[
 \Theta=1-\gamma_0.
\tag{40}
\]

After primitive normalization,

\[
 x_m=(N_m,-(N_m-1),-1),
\tag{41}
\]

with

\[
 \|x_m\|=N_m,
 \qquad
 \prod_k\operatorname{out}_{\{2\}}(x_{m,k})=N_m-1.
\tag{42}
\]

For every fixed `c>0` and `d<1`,

\[
 N_m-1>cN_m^d
\tag{43}
\]

eventually.  Hence this is an actual infinite, nondegenerate, projectively
distinct boundary family.  No criterion using only `Theta` and `gamma` can
replace `Theta<1-gamma` by a non-strict inequality.

## Specialization at `gamma=0`

If

\[
 {\log g_m\over\log H_m}\longrightarrow0,
\tag{44}
\]

the gcd may be unbounded but is subpower in `H_m`.  The criterion becomes

\[
 \Theta<d
\tag{45}
\]

for a prescribed `d<1`, or simply

\[
 \boxed{\Theta<1}
\tag{46}
\]

for the existence of some Evertse exponent.

The bounded-gcd lemma `L-9900` is the special case `g_m<=G`, which implies
`gamma=0`.  Its finite threshold `H_m^epsilon>=G^d` is the constant version
of the absorption in (16)--(20).

For `T-9828`,

\[
 g_m\le216,
 \qquad\gamma=0,
 \qquad
 \Theta\le{6498\over346819}<{1\over50}.
\tag{47}
\]

Thus `T-9828` uses (45) with `d=1/50`.  Its 2-adic ratio intervals provide
pairwise separation, although the diverging primitive-height bound already
guarantees infinitely many distinct projective points.

## Dependency and gap audit

- Evertse's Corollary 1 is the only external input beyond `L-9900`'s notation
  and source map.
- The number of endpoints and internal coordinates must remain fixed.
- The exact invariant is `Xi`; the marginal inequality is intentionally safe
  and can lose information when endpoint content and gcd peaks are
  anticorrelated.
- The boundary example proves strictness is not a technical artifact.
- No claim is made when `gamma>=1`, because primitive height need not diverge.
