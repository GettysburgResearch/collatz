# R-9810 -- Archimedean Hecke--Mahler transcendence does not determine the 2-adic Sturmian carry

Claim ID: `R-9810`
Title: The Sturmian maximal-run carry is a 2-adic Beatty--Hecke--Mahler value, while the available transcendence theorem controls only its real shadow
Status: `PROPOSED / SOURCE-CONFIRMED METHOD BOUNDARY`
Authoring agent: `gpt56-synthesis-01-wave16-completion-cold-review`
Reviewing agents: `gpt56-synthesis-01`, `gpt56-synthesis-01-wave16-completion-cold-review`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9827`, `T-9829`; Luca--Ouaknine--Worrell 2022, Theorem 2; Bugeaud--Laurent 2023, Theorem 1.1; Ooto 2016; Lopez--Stoll 2009
Scope: mechanical/Sturmian maximal-run tails for the binary chart `U=2^a<V`, with `V` odd
Related claims: issue #26; PR #35; local `R-9809`; no `K-####` candidate

## Statement

Let a maximal-run tail have mechanical lengths

\[
 \ell_{K+j}
 =h+\lfloor(j+1)\alpha+\rho\rfloor
    -\lfloor j\alpha+\rho\rfloor,
 \qquad j\ge0,
\tag{1}
\]

where `h>=1`, `0<alpha<1` is irrational, and `0<=rho<1`.  The exact
carry zipper of `T-9827` writes the required carry as

\[
 \boxed{
 q_K=-\sigma_KV^{-\ell_K}
 \mathcal H_{\alpha,\beta}^{(2)}(r),}
 \qquad
 r={U\over V},
 \qquad
 \beta=\{\alpha+\rho\},
\tag{2}
\]

where

\[
 \mathcal H_{\alpha,\beta}^{(2)}(r)
 =\sum_{j\ge0}(-1)^j
 r^{hj+\lfloor j\alpha+\beta\rfloor}
 \quad\hbox{in }\mathbf Q_2.
\tag{3}
\]

The same rational partial sums have a real limit.  That real limit is a
difference of two Beatty--Hecke--Mahler series and is transcendental by the
archimedean theorem of Luca--Ouaknine--Worrell.  This does **not** prove that
the 2-adic value (3) is irrational, transcendental, nonintegral, or
incompatible, through (2), with the positive odd carry required by the chart.

Thus the proposed Sturmian continuation of `T-9829` stops at a genuine
cross-place gap:

\[
 \boxed{
 \text{real Beatty--Hecke--Mahler transcendence}
 \not\Longrightarrow
 \text{2-adic carry irrationality}.}
\tag{4}
\]

This refutes the completion-transfer method, not the desired Sturmian
run-exclusion statement.

## 1. Exact mechanical carry series

Put

\[
 S_j=\ell_{K+1}+\cdots+\ell_{K+j},
 \qquad S_0=0.
\tag{5}
\]

Telescoping (1) from `1` through `j` gives

\[
 \begin{aligned}
 S_j
 &=hj+\lfloor(j+1)\alpha+\rho\rfloor
       -\lfloor\alpha+\rho\rfloor\\
 &=hj+\lfloor j\alpha+\beta\rfloor.
 \end{aligned}
\tag{6}
\]

Since `sigma_(K+j)=sigma_K(-1)^j`, the shifted carry formula
`T-9829/(8)` becomes (2)--(3).  Because `v_2(r)=a>0`, the series converges
in `Q_2`.  Because `0<r<1` and `S_j` grows strictly, the identical sequence
of partial rational sums also converges in `R`.  Denote the latter limit by

\[
 \mathcal H_{\alpha,\beta}^{(\infty)}(r).
\tag{7}
\]

Nothing in this two-place convergence identifies the limits.

## 2. Archimedean Beatty--Hecke--Mahler form

Set

\[
 b={V\over U}=r^{-1},
 \qquad
 \theta=2(h+\alpha),
 \qquad
 \gamma=h+\alpha+\beta.
\tag{8}
\]

Splitting (7) into its even and odd indices gives the exact real identity

\[
 \boxed{
 \mathcal H_{\alpha,\beta}^{(\infty)}(r)
 =\sum_{m\ge0}b^{-\lfloor m\theta+\beta\rfloor}
  -\sum_{m\ge0}b^{-\lfloor m\theta+\gamma\rfloor}.}
\tag{9}
\]

Indeed,

\[
 2hm+\lfloor2m\alpha+\beta\rfloor
 =\lfloor m\theta+\beta\rfloor,
\tag{10}
\]

while

\[
 h(2m+1)+\lfloor(2m+1)\alpha+\beta\rfloor
 =\lfloor m\theta+\gamma\rfloor.
\tag{11}
\]

The two offsets are inequivalent under the rotation lattice because

\[
 \gamma-\beta=h+\alpha={\theta\over2}
 \notin\mathbf Z\theta+\mathbf Z.
\tag{12}
\]

For if `theta/2=p theta+q` with integers `p,q`, irrationality of `theta`
would force `p=1/2`, which is impossible.

The same even/odd split is valid in `Q_2`, because its two subseries converge
there.  If

\[
 F_\delta^{(v)}(b,\theta)
 =\sum_{m\ge0}b^{-\lfloor m\theta+\delta\rfloor},
 \qquad v\in\{2,\infty\},
\tag{13}
\]

then

\[
 \mathcal H_{\alpha,\beta}^{(v)}(r)
 =F_\beta^{(v)}(b,\theta)-F_\gamma^{(v)}(b,\theta)
 \qquad(v=2,\infty).
\tag{14}
\]

It remains to map only the real copy to the available theorem.  If
`delta=k+x` with `k` integral and `0<=x<1`, then

\[
 F_\delta^{(\infty)}=b^{-k}F_x^{(\infty)}.
\tag{15}
\]

If `x=0`, shifting the index once gives

\[
 F_0^{(\infty)}
 =1+b^{-\lfloor\theta\rfloor}
 F_{\{\theta\}}^{(\infty)}.
\tag{16}
\]

Integer normalization and the zero-offset shift change an offset only by an
element of `Z theta+Z`.  Thus (12) guarantees that the two normalized offsets
remain distinct.  Equations (15)--(16) put the real value in the exact form

\[
 \mathcal H_{\alpha,\beta}^{(\infty)}(r)
 =c+\mathcal S(b,\theta,A,\mathbf v),
\tag{17}
\]

where `c` is algebraic, `A` consists of two offsets in `(0,1)`, and
`v` is a nonzero algebraic weight vector.  This explicitly covers
`beta=0` or `{gamma}=0`; the normalized weights need not remain `(1,-1)`.

Luca--Ouaknine--Worrell, Theorem 2, applies to (17).  Here `b` is algebraic
with ordinary absolute value greater than one, `theta` is irrational, and
(12) is exactly their offset-separation condition.  In their single-base
case, `k=r=1`; the singleton base is multiplicatively independent because
`|b|>1`.  The theorem makes `1` and `S` linearly independent over the
algebraic numbers.  Adding the algebraic constant `c` preserves
transcendence, so

\[
 \boxed{
 \mathcal H_{\alpha,\beta}^{(\infty)}(r)
 \text{ is transcendental}.}
\tag{18}
\]

Bugeaud--Laurent prove the corresponding transcendence theorem for
two-variable Hecke--Mahler series at algebraic points.  Both results are
complex/archimedean value theorems; neither evaluates (3) in `Q_2`.

## 3. Why the 2-adic theorem does not transfer

Let

\[
 H_N=\sum_{j=0}^{N}(-1)^j
 r^{hj+\lfloor j\alpha+\beta\rfloor}\in\mathbf Q.
\tag{19}
\]

Then

\[
 H_N\longrightarrow
 \mathcal H_{\alpha,\beta}^{(2)}(r)
 \quad\hbox{in }\mathbf Q_2,
\tag{20}
\]

and

\[
 H_N\longrightarrow
 \mathcal H_{\alpha,\beta}^{(\infty)}(r)
 \quad\hbox{in }\mathbf R.
\tag{21}
\]

An algebraic or transcendence conclusion about the limit in (21) says
nothing by itself about the limit in (20).  The rational geometric
rationalization in `T-9829` avoided this issue because eventual periodicity
made both limits equal to one explicitly displayed rational number.  The
Sturmian series has no such rationalization.

The nearest p-adic digit theorems do not fill the gap.  Ooto proves
transcendence for p-adic numbers built directly from non-ultimately-periodic
canonical digit strings that are automatic, primitive morphic, or Sturmian;
his Mahler-class theorem then classifies such irrational values.  He also
treats sparse p-adic Beatty digit sums of the form
`sum p^(floor(n theta+rho))`.  Neither statement matches (3): its terms are

\[
 2^{aS_j}V^{-S_j},
\tag{22}
\]

with varying 2-adic units and alternating signs.  No audited result identifies
the canonical binary digits of their sum with the mechanical exponent-gap
word, or reduces those units to Ooto's unweighted sparse Beatty series.

Lopez--Stoll's exact `3x+1` conjugacy study supplies a useful warning rather
than a theorem for this chart.  Its abstract explicitly records as unknown
whether an aperiodic parity word can have an eventually periodic image under
the 2-adic conjugacy map, and it studies mechanical words by a genuinely
2-adic continued fraction.  That is closely analogous to the rationality
question here, but it neither proves nor disproves it.

## 4. Exact chart example with different two-place limits

The completion problem already occurs in the elementary `2 -> 3` chart

\[
 2M_{n+1}=3M_n-\epsilon_n,
 \qquad \epsilon_n\in\{0,1\}.
\tag{23}
\]

Iteration gives

\[
 M_0=\left({2\over3}\right)^NM_N
 +{1\over3}\sum_{n=0}^{N-1}
 \epsilon_n\left({2\over3}\right)^n.
\tag{24}
\]

For an ordinary integer trajectory, the first term tends to zero in `Q_2`.
Hence, when `M_0=2`,

\[
 \boxed{
 \sum_{n\ge0}\epsilon_n(2/3)^n=6
 \quad\hbox{in }\mathbf Q_2.}
\tag{25}
\]

The real series formed from the identical rational partial sums satisfies

\[
 0\le\sum_{n\ge0}\epsilon_n(2/3)^n
 \le\sum_{n\ge0}(2/3)^n=3.
\tag{26}
\]

Thus its real limit cannot equal the rational 2-adic limit `6`.  This is an
exact chart identity, not a generic topological example, and it shows why
real bounds or real transcendence cannot be applied to a forced 2-adic carry.

## 5. Precise missing theorem

A direct Sturmian extension of `T-9829` needs the following exact target.

> Let `b=V/2^a` be rational with `V` odd and `V>2^a`, let `theta>0` be
> irrational, and let `beta` be real.  With `gamma=beta+theta/2`, prove that
> the convergent value
> `F_beta^(2)(b,theta)-F_gamma^(2)(b,theta)` is irrational in `Q_2`.

The rational base makes the `Q_2` embedding unambiguous, and both subseries
converge because `|b^(-1)|_2=2^(-a)<1`.  For the physical specialization,
`theta=2(h+alpha)`.  Equation (14), now at `v=2`, would make (3) irrational,
contradicting the rational factorization (2) with positive integral `q_K`.
The offsets are allowed to be arbitrary real numbers, as the mechanical
parameters require.  None of the audited sources supplies this statement.

## Primary-source audit

- Luca, Ouaknine, and Worrell, [*On the transcendence of a series related to
  Sturmian words*](https://arxiv.org/abs/2204.08268), especially Theorem 2,
  treat complex algebraic bases of ordinary modulus greater than one and the
  offset lattice and normalized real form used in (12)--(18).
- Bugeaud and Laurent, [*Transcendence and continued fraction expansion of
  values of Hecke--Mahler series*](https://arxiv.org/abs/2203.12901), prove
  transcendence at algebraic points satisfying their archimedean domain
  `0<|z_1|<1` and `0<|z_1 z_2^theta|<1`; this source is corroborative and is
  not used to prove (18).
- Ooto, [*Mahler's classification and a certain class of p-adic
  numbers*](https://arxiv.org/abs/1512.06511), treats canonical nonperiodic
  digit words and an unweighted sparse p-adic Beatty series, not the varying-
  unit signed series (3).
- Lopez and Stoll, [*The 3x+1 conjugacy map over a Sturmian
  word*](https://math.colgate.edu/~integers/j13/j13.pdf), state the related
  aperiodic-to-periodic conjugacy question as open and develop a 2-adic
  continued fraction instead of an archimedean transfer.

## Gap and novelty audit

- Equations (6), (9), and (14) are exact; they identify both completion values
  attached to a mechanical maximal-run tail.
- Equation (18) is an archimedean conclusion only.  It is not used as a claim
  about (3).
- Equation (25) is an explicit counterexample to completion identification,
  not a Sturmian counterexample and not a counterexample to either cited
  transcendence theorem.
- No positive Sturmian survivor is constructed.  No Sturmian schedule is
  excluded.
- The useful output is a sharp target theorem and a quarantine: future work
  must use a genuinely p-adic Beatty-series argument, not the real shadow.

## Suggested next attack

Study the canonical binary carries of (3) along convergent denominators of
`alpha`.  A viable route must either obtain p-adic rational-approximation
exponents for the Beatty series or prove that rationality would force eventual
periodicity of a carry automaton.  Both approaches would address the actual
`Q_2` value and bypass the invalid completion transfer.
