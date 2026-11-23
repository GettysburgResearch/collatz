# Self-contained arithmetic questions for independent attacks

These are **OPEN** tasks. The statements below contain all definitions and
do not announce a larger convergence consequence. An expert may still
recognize the recurrence. Copy a task statement and its scope notes when
delegating it; the integration notes at the end explain why it matters.
None of the requested conclusions is an available theorem in this packet.

## A. Collision dimension of a single integer recurrence

Let `q_0,q_1,...` be pairwise distinct positive odd integers, none divisible
by three. Let `a_0,a_1,...` be positive integers such that

\[
 2^{a_j}q_{j+1}=3q_j+1\qquad(j\ge0).
\]

Fix one such sequence; its initial integer does not vary with the sample
length. Choose a subsequence `N_i -> infinity` along which, for every
`m>=1` and residue `r mod 3^m`, the limits

\[
 \mu_m(r)=\lim_{i\to\infty}\frac1{N_i}
 \#\{0\le j<N_i:q_j\equiv r\pmod{3^m}\}
\]

exist. These limits are compatible probability distributions. Define

\[
 \ell=\log_2 3,\qquad
 \Phi=\ell\log\ell-(\ell-1)\log(\ell-1),\qquad
 \theta=\Phi/\log3.
\]

**Question.** Prove that every such compatible limit satisfies

\[
 \liminf_{m\to\infty}
 \frac{-\log\left(\sum_{r\bmod3^m}\mu_m(r)^2\right)}{m\log3}
 \ge\theta.
 \tag{A}
\]

A sufficient form is a sequence `epsilon_m -> 0` with
`sum_r mu_m(r)^2 <= exp(epsilon_m m) 3^(-theta m)` for all sufficiently
large `m`. The sequence of errors may depend on the fixed integer orbit.

Useful exact arithmetic: for a gap from `q_i` to `q_(i+d)`, put

\[
 A=\sum_{j=i}^{i+d-1}a_j,\qquad
 C=\sum_{h=0}^{d-1}3^{d-1-h}2^{a_i+\cdots+a_{i+h-1}},
 \qquad C/(2^A-3^d)=c/b
\]

in lowest terms, with `c>0` and signed `b`. Then

\[
 q_i\equiv q_{i+d}\pmod{3^m}
 \quad\Longrightarrow\quad
 2^{A+1}3^m\mid bq_i-c.
\]

For each fixed complete gap word, its exact legal source and return
condition together form one residue class modulo `2^(A+1)3^m`.
These facts do not make the actual sequence uniformly distributed over
those source classes. All lag lengths and the actual common source
quotient have to remain in the argument.

**Quantifier guard.** Take `i -> infinity` first at each fixed `m` in
(A). A bound only when `m=floor(log N/Phi)` is a different target. It
would settle the finite-Shannon-deficit diagonal case, but does not on
its own establish (A) or handle the equality branch. A theorem for an
independent random word, an average over starting integers, or a different
source at each horizon does not answer this question.

## B. Finite synthesis for a coupled integer program

For `r>=0`, define

\[
 F(r)=\prod_{j=0}^{r-1}(1+3^j),\qquad F(0)=1.
\]

For a positive integer `n`, choose a signed integer `a` and a nonnegative
integer `r`. Put

\[
 M=n\max(1,|a|)F(r),\qquad
 E=\min\{e\in\mathbb N:M<2^e\},\qquad H=9E+1.
\]

Initialize the state `(x,w,s)=(n,a,r)`. A test passes exactly when `x`
and `w` have opposite parity. If it passes, update by the applicable rule:

| Condition | New state |
|---|---|
| `x` odd, hence `w` even | `((3x+1)/2, w/2, s)` |
| `x` even, `w` odd, `s>0` | `(x/2, (w+3^(s-1))/2, s-1)` |
| `x` even, `w` odd, `s=0` | `(x/2, (3w+1)/2, 0)` |

All divisions in a passed step are exact integer divisions, including
for negative `w`.

**Question.** Give a proved terminating construction which, for every
`n>0`, returns `a` and `r` for which the first `H` tests pass.

The horizon must be computed from the returned candidate's own height.
Merely producing a candidate passing an arbitrarily prescribed shorter
word is insufficient. Increasing its denominator or numerator changes
the required number of tests. Lowest terms are not required, and a
construction may use negative numerators.

There is no demand for a small running time. A well-founded recursive
construction is acceptable if all its descent, coverage, and eventual
success assertions are proved. An exhaustive search without a proof
that it finds an accepted candidate is not a solution.

The new finite insertion theorem bounds one restricted family of
source-changing repairs; it does not solve this synthesis problem.
In particular, requiring all partial edits to be individually integral
would discard valid joint denominator cancellations.

## C. Complete divisibility of a binary affine carry

Let `e_0,...,e_(A-1)` be a nonconstant binary word of positive length.
Write `p=sum e_i`, and define integers recursively by

\[
 C_0=0,\qquad C_{i+1}=3^{e_i}C_i+e_i2^i,
 \qquad D=2^A-3^p.
\]

Assume `D>0` and `D` divides `C_A`.

**Question.** Prove that `C_A/D` is either 1 or 2. Equivalently, prove
that the word is a repetition of `10` or of `01`.

For possible use, the complementary carry and its full reduced denominator
are

\[
 C^*_0=0,\quad
 C^*_{i+1}=3^{1-e_i}C^*_i+(1-e_i)2^i,\quad
 E=2^A-3^{A-p},\quad q=E/\gcd(E,C^*_A)
\]

when `E>0`. The original condition is divisibility by the complete
numerical `D`, not a collection of selected prime factors or a small
denominator estimate. Retain the complete carries under rotations.

The product multiplier `3/4` does not by itself add an independent
equation. With

\[
 f=DX-C_A,\qquad g=EY-C^*_A,
\]

the denominator-cleared product closure satisfies exactly

\[
 (4^A-3^A)XY-3^pC^*_AX-3^{A-p}C_AY-C_AC^*_A
 =2^AYf+2^AXg-fg.
\]

A useful new proof would therefore have to use an additional integral,
height, prime-valuation, or positivity constraint. Bounds tested only
on one-rise words, bounded numbers of runs, fixed recurrence families,
or bounded lengths do not answer the all-word question.

## Integration notes for the coordinating researcher

- **A** is the missing actual stationary collision lower-dimension bound.
  PR180's pinned strict-exponent theorem gives the opposite strict
  inequality for every escaping ordinary time-limit law. The input
  sequence in A would therefore be excluded if A were proved. This
  addresses escape; positive cycles remain separate.
- **B** is the unchanged universal candidate problem. Checkpoint 17's
  Lean theorem proves that passing this finite candidate-dependent
  horizon reaches the exact complementary standard cycle. Constructing
  a successful candidate for every positive source would close the
  full theorem. The finite recognizer is already available; existence
  is the work requested.
- **C** is the complete positive-cycle divisibility problem. The affine
  carry formulas imply literal parity legality when the full quotient
  is an integer. Excluding its nontrivial integer values addresses the
  cycle branch. The rational controls in this checkpoint show why the
  full divisibility assumption cannot be dropped.

For a focused high-variance pass, B offers a direct all-source target.
A gives a separate route through actual arithmetic mixing, and C is the
necessary cycle counterpart if the analytic route first excludes escape.
None should be replaced by verifying another finite collection of examples.
