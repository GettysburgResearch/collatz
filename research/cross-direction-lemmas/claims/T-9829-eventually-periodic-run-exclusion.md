# T-9829 -- Positive binary-chart survivors have aperiodic maximal runs

Claim ID: `T-9829`
Title: Every eventually periodic maximal-run schedule forces a nonintegral tail carry
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave16-completion-cold-review`
Reviewing agents: `gpt56-synthesis-01`, `gpt56-synthesis-01-wave14-cap-cell-hierarchy`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9827`; local `T-9823` only for the nontrivial-orbit coding setup
Scope: every positive ordinary binary expanding-chart orbit with `U=2^a<V` and `V` odd; exact `4 -> 5` specialization
Related counterexample candidates: issue #26; PR #35; no `K-####` candidate

## Setup

Let

\[
 U=2^a,
 \qquad a\ge1,
 \qquad V>U\text{ odd},
 \qquad C=V-U.
\tag{1}
\]

Suppose a nontrivial positive ordinary orbit satisfies

\[
 UM_{n+1}=VM_n-C\epsilon_n,
 \qquad M_n>1,
 \qquad \epsilon_n\in\{0,1\}.
\tag{2}
\]

Decompose its code into finite maximal runs as in `T-9827`.  Write `ell_k`
for the run lengths, `s_k` for the alternating symbols, and

\[
 \sigma_k=2s_k-1,
 \qquad \sigma_{k+1}=-\sigma_k.
\tag{3}
\]

That theorem extracts positive odd carries `q_k` obeying

\[
 \boxed{
 U^{\ell_{k+1}}q_{k+1}
 =V^{\ell_k}q_k+\sigma_k.}
\tag{4}
\]

## Theorem

The maximal-run sequence `(ell_k)` of a positive ordinary orbit (2) is not
eventually periodic.

More precisely, if a purported periodic tail starts at run `K`, then its
forced tail carry is a rational number satisfying

\[
 \operatorname{sgn}(q_K)=-\sigma_K,
 \qquad
 0<|q_K|<V^{-\ell_K}\le {1\over V}.
\tag{5}
\]

This contradicts the fact that `q_K` is a positive odd integer.

## Tail carry formula at an arbitrary run

Fix `k` and put

\[
 S_{k,0}=0,
 \qquad
 S_{k,j}=\sum_{i=1}^{j}\ell_{k+i}\qquad(j\ge1),
 \qquad r={U\over V}.
\tag{6}
\]

Composing (4) backwards through `N` transitions gives

\[
 \begin{aligned}
 q_k={}&-V^{-\ell_k}
 \sum_{j=0}^{N-1}\sigma_{k+j}r^{S_{k,j}}\\
 &+U^{S_{k,N}}
 V^{-\sum_{i=0}^{N-1}\ell_{k+i}}q_{k+N}.
 \end{aligned}
\tag{7}
\]

Every `q_(k+N)` is odd.  Since `S_(k,N)->infinity`, the last term tends to
zero 2-adically.  Therefore

\[
 \boxed{
 q_k=-V^{-\ell_k}
 \sum_{j\ge0}\sigma_{k+j}r^{S_{k,j}}
 \quad\text{in }\mathbf Q_2.}
\tag{8}
\]

This is the shifted form of `T-9827/(36)`.  In general it must not be
identified with the real sum of the displayed series.

## Periodic-tail rationalization

Assume for contradiction that some positive integer `d` satisfies

\[
 \ell_{j+d}=\ell_j
 \qquad(j\ge K).
\tag{9}
\]

Take

\[
 T=\begin{cases}
 d,&d\text{ even},\\
 2d,&d\text{ odd}.
 \end{cases}
\tag{10}
\]

Then `T` is even, and both `ell_(K+j)` and `sigma_(K+j)` are `T`-periodic.
Put

\[
 L=S_{K,T},
 \qquad
 B=\sum_{t=0}^{T-1}\sigma_{K+t}r^{S_{K,t}}.
\tag{11}
\]

For `m>=0` and `0<=t<T`, periodicity gives

\[
 S_{K,mT+t}=mL+S_{K,t}.
\tag{12}
\]

Consequently the series in (8) is a geometric series in `Q_2`:

\[
 \begin{aligned}
 A
 &:=\sum_{j\ge0}\sigma_{K+j}r^{S_{K,j}}\\
 &=B\sum_{m\ge0}r^{mL}
 ={B\over1-r^L}\in\mathbf Q.
 \end{aligned}
\tag{13}
\]

Here `v_2(r)>0`, so the 2-adic expansion is valid.  Because `0<r<1`, the
same geometric expansion converges in the real absolute value and has the
same rational value `B/(1-r^L)`.  Eventual periodicity is exactly what makes
this cross-place identification legitimate.

The signs in (13) alternate, while

\[
 1=r^{S_{K,0}}>r^{S_{K,1}}>r^{S_{K,2}}>\cdots>0.
\tag{14}
\]

The strict alternating-series estimate therefore gives

\[
 \boxed{0<\sigma_KA<1.}
\tag{15}
\]

Equation (8) is now an equality between rational numbers: the embedding
`Q -> Q_2` is injective.  Hence

\[
 q_K=-V^{-\ell_K}A,
\tag{16}
\]

and (15) proves (5).  This is incompatible with a positive odd integer
`q_K`.  The periodic tail cannot exist. **QED**

## Corollary -- phase and run-length complexity floors

Let

\[
 \epsilon=\epsilon_0\epsilon_1\epsilon_2\cdots
\tag{17}
\]

be the binary phase word and

\[
 \ell=\ell_0\ell_1\ell_2\cdots
\tag{18}
\]

its word of maximal-run lengths.  Neither word is ultimately periodic.  If

\[
 p_x(n)=\#\{x_ix_{i+1}\cdots x_{i+n-1}:i\ge0\},
\tag{19}
\]

then, for every `n>=1`,

\[
 \boxed{p_\epsilon(n)\ge n+1,\qquad p_\ell(n)\ge n+1,}
\tag{20}
\]

where `p_ell(n)` is allowed to be infinite.

First observe directly that both phase symbols occur infinitely often.  If
`epsilon_n=s` for all `n>=N`, put `X_n=M_n-s`.  Equation (2) becomes

\[
 UX_{n+1}=VX_n.
\tag{21}
\]

Iteration and `gcd(U,V)=1` force `U^t|X_N` for every `t`, hence `X_N=0`.
This would give `M_N=0` or `1`, contrary to `M_N>1`.  Thus there are
infinitely many finite maximal runs.

For any binary one-sided word with infinitely many occurrences of both
symbols, ultimate periodicity of its phase word is equivalent to eventual
periodicity of its maximal-run lengths.

For one direction, suppose the run lengths have eventual period `d`.  Choose
the even period `T` from (10), so both lengths and run symbols repeat after
`T` runs.  If `p_k` is the first position of run `k` and

\[
 P=\sum_{i=K}^{K+T-1}\ell_i,
\tag{22}
\]

then

\[
 p_{k+T}=p_k+P,
 \qquad \ell_{k+T}=\ell_k,
 \qquad s_{k+T}=s_k
\tag{23}
\]

for all late `k`.  Hence `epsilon_(n+P)=epsilon_n` after the finite prefix.

Conversely, suppose `epsilon_(n+P)=epsilon_n` for all `n>=N`.  The switch
indicator

\[
 b_n=\mathbf1_{\epsilon_n\ne\epsilon_{n-1}}
\tag{24}
\]

is `P`-periodic for `n>=N+1`.  It has a positive number `r` of switches per
period because both symbols continue to occur.  Translation by `P` therefore
advances every sufficiently late ordered run boundary by exactly `r`
boundaries:

\[
 p_{k+r}=p_k+P,
 \qquad p_{k+r+1}=p_{k+1}+P.
\tag{25}
\]

Subtracting gives `ell_(k+r)=ell_k` eventually.  The theorem rules this out,
so neither word is ultimately periodic.

For completeness, use the elementary one-sided Morse--Hedlund lemma: if an
infinite one-sided word over any alphabet has `p_x(n)<=n` for some `n>=1`,
then it is ultimately periodic.  Indeed, set `p_x(0)=1`.  The prefix map from
`(m+1)`-factors onto `m`-factors is surjective, so the complexities are
nondecreasing.  If every increase through level `n` were strict, then
`p_x(n)>=n+1`.  Otherwise some `m<n` has

\[
 p_x(m+1)=p_x(m).
\tag{26}
\]

Every `m`-factor then has a unique right extension.  Successive `m`-factors
follow a deterministic map on a finite set and eventually cycle, making the
word ultimately periodic.  The `m=0` case is the constant word.  Taking the
contrapositive proves (20).  This also covers the positive-integer alphabet
of `ell`; if infinitely many run lengths occur, its factor complexities are
already infinite.

A periodic phase tail may begin inside a run, but moving to the next boundary
changes only finitely many terms.  Factors meeting a finite preperiod can only
increase the counts.  In fact every suffix of either word is non-ultimately-
periodic and separately obeys (20).

## Why the contradiction is taken after the preperiod

It would be invalid to infer that a nonintegral forced tail carry makes the
initial carry nonintegral.  The finite backward map is affine and can cancel
denominators.  For example, in the `4 -> 5` zipper with

\[
 \ell_0=\ell_1=1,
 \qquad \sigma_0=-1,
\tag{27}
\]

the nonintegral value `q_1=7/2` maps backwards to

\[
 q_0={4q_1+1\over5}=3.
\tag{28}
\]

This is not a valid orbit because `q_1` is not an odd integer.  It shows why
the proof must contradict the carry condition directly at the first periodic
tail index `K`, rather than propagate nonintegrality through the preperiod.

## Exact `4 -> 5` consequence

For

\[
 4M_{n+1}=5M_n-\epsilon_n,
\tag{29}
\]

no positive ordinary chart survivor has an eventually periodic maximal
phase-run schedule.  If a proposed tail at `K` has run period `d`, choose `T`
by (10), let

\[
 S_t=\sum_{i=1}^{t}\ell_{K+i},
 \qquad L=S_T,
\tag{30}
\]

and its forced carry is exactly

\[
 \boxed{
 q_K=-5^{-\ell_K}
 {\displaystyle\sum_{t=0}^{T-1}
 \sigma_{K+t}(4/5)^{S_t}
 \over
 1-(4/5)^L}.}
\tag{31}
\]

It has sign `-sigma_K` and magnitude strictly below `5^(-ell_K)<=1/5`,
contradicting positivity and odd integrality.  Under the PR #35 chart
normalization `M_0=A_0+2`, an ordinary survivor therefore requires a genuinely
aperiodic maximal-run schedule.

## Dependency and novelty audit

- `T-9827` supplies the exact positive odd carries and zipper (4).  It leaves
  eventual stabilization of the initial-carry cylinders open.
- The present theorem closes one infinite family of schedules: every
  eventually periodic run-length directive has a rational tail completion,
  and the real alternating estimate places that rational strictly between
  consecutive integers.
- No external Diophantine theorem is used.  Only a finite geometric-series
  identity, injectivity of `Q -> Q_2`, and the elementary alternating-series
  estimate enter.
- PR #35 is used only for the physical `4 -> 5` crosswalk.  The general proof
  is native to (1)--(4).

## Adversarial boundary

- The sparse series in (8) converges both 2-adically and really, but those two
  limits are not equated until periodicity turns both into the same explicit
  rational expression (13).
- The run period must be made even.  If `d` is odd, the alternating signs have
  period `2d`, not `d`.
- The argument concerns eventual periodicity of maximal-run lengths.  It does
  not exclude Sturmian, automatic, morphic, bounded-aperiodic, or arbitrary
  high-complexity schedules.
- Finite prefixes of any proposed schedule remain compatible with large
  positive lifts.  The contradiction is intrinsically infinite.
- The theorem excludes a family of chart directives; it does not construct a
  positive survivor or settle the existence of survivors with aperiodic run
  schedules.

## Suggested next attack

Replace geometric rationalization by an arithmetic classification of sparse
series whose exponent gaps are automatic or substitutive.  Showing that the
2-adic carry in (8) is irrational, transcendental, or has nonintegral rational
tails for broader low-complexity run schedules would turn the exact zipper
into a hierarchy of one-root exclusions beyond eventual periodicity.
