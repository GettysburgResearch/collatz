# A fixed-source closing test and its exact arithmetic threshold

**PROPOSED derivations; global closure remains OPEN.** The purpose of this
note is to test whether the simultaneous-approximation denominator bound
in [AR2](ADIC_REAL_DENSITY.md) can force a genuine ordinary Collatz orbit
to close. All actual iterates below come from one fixed positive ordinary
source. The calculation yields exact necessary thresholds and a failure
of one natural Subspace-Theorem architecture. It does not prove a bound
on every orbit.

## 1. The natural periodic pin of an actual finite prefix

Let T be the shortcut map, fix n>0, and write n_K=T^K(n). If its actual
length-K parity word has q odd letters, then
\[
 2^K n_K=3^q n+C,\qquad C\in\mathbb Z_{\ge0}.
\]
Take K>=1 and q>=1. The integer D=2^K-3^q is nonzero and coprime to six.
The same word has a unique rational fixed point
\[
 r_K=C/D.
\]
It need not be positive. Put
\[
 h=n_K-n,\qquad g=\gcd(C,|D|).
\]

**FS1 (exact denominator and difference).** If h!=0, then
\[
 g=\gcd(h,|D|),\qquad
 d_K=\operatorname{den}(r_K)=|D|/g,
\]
and
\[
 r_K-n=\frac{2^K h}{D},\qquad
 d_K|r_K-n|=\frac{2^K|h|}{g}.                            \tag{1}
\]
Consequently the exact local precisions are
\[
 v_2(r_K-n)=K+v_2(h),\qquad
 v_3(r_K-n)=v_3(h).                                    \tag{2}
\]
To prove the gcd identity, subtract nD from C and use
C-nD=2^K(n_K-n), with gcd(2,D)=1. The remaining claims follow immediately.

Write h=2^u3^v h_0 with gcd(h_0,6)=1. The gcd g divides h_0, so (1) becomes
\[
 \frac{d_K|r_K-n|}{2^{K+u}3^v}=\frac{|h_0|}{g}
 \in\mathbb Z_{\ge1}.                                 \tag{3}
\]
Thus the simultaneous local denominator lower bound is exact up to a
positive integer factor that is already present in the ordinary endpoint
difference. If a proof forced the left side below one, it would force
h=0, an actual return of the fixed source. No such forcing estimate has
been established here. When h=0, the pin is exactly n and this is an actual
periodic orbit; even proving a return would still require excluding every
nontrivial positive integer cycle to finish Collatz.

## 2. What the same pins do on a hypothetical escaping orbit

Normalize to a positive odd ternary unit n_0. Every arbitrary positive
integer reaches this domain after discarding its initial powers of two
and, if necessary, taking one odd step. Suppose for this section that
the accelerated odd orbit n_j=U^j(n_0) is nonperiodic. Its states are
pairwise distinct and tend to infinity.

Let
\[
 a_j=v_2(3n_j+1),\qquad A_j=\sum_{i<j}a_i,
 \qquad\lambda_j=2^{A_j}/3^j.
\]
Define the exact scaled height
\[
 L_j=\lambda_j n_j
     =n_0+\frac13\sum_{i<j}\lambda_i
     =n_0\prod_{i<j}\left(1+\frac1{3n_i}\right).         \tag{4}
\]
The uniform reciprocal bound for distinct ordinary orbit states gives
sum_i 1/n_i<infinity. Hence L_j increases to a finite number L>n_0,
lambda_j=L_j/n_j tends to zero, and
\[
 L-L_j=\frac13\sum_{i\ge j}\lambda_i
       \ge\lambda_j.                                  \tag{5}
\]
The last inequality uses a_i>=1, which gives
lambda_{j+h}/lambda_j>=(2/3)^h, and sums the geometric series.
This paragraph uses PR150, head
`ef4022fa5ae43dd943ecca0b7c84d69af624c5c9`,
`research/pointwise-closure-20261120/LOCAL_DISTORTION.md`, the shell bound
and reciprocal sum below 600. A nonperiodic accelerated orbit is a subset
of a distinct shortcut orbit, so the hypothesis applies. A sharper prior
constant is unnecessary. The existence of a limiting logarithmic phase
is already in PR145's `research/binary-run-occupancy/MELLIN_PHASE.md`;
this note makes no novelty claim for that phase.

In fact the inequality in (5) is strict on this hypothetical ordinary
orbit. Direct calculation gives
\[
 \lambda_{i+1}(n_{i+1}+1)-\lambda_i(n_i+1)
   =\frac{\lambda_i}{3}(2^{a_i}-2)\ge0.
\]
Writing s_j=v_2(n_j+1), there are exactly s_j-1 consecutive future gaps
equal to one before the first gap at least two. This follows from
n_{j+h}+1=3^h(n_j+1)/2^h through those gaps. The first positive increment
in the preceding display is at least lambda_j(2/3)^{s_j}. Passing to the
limit yields
\[
 \frac{L-L_j}{\lambda_j}
   \ge1+(2/3)^{s_j}>1.                                \tag{5a}
\]

The rational periodic pin of the j-odd-step prefix is
\[
 r_j=\frac{L_j-n_0}{\lambda_j-1}
     \longrightarrow n_0-L<-1.                         \tag{6}
\]
It therefore approaches a negative real value while its 2-adic precision
at the positive ordinary source n_0 tends to infinity. Positivity of the
source does not transfer to this limiting real coordinate.

For j large enough that lambda_j<1, FS1 gives
\[
 |r_j-n_0|=\frac{L_j-\lambda_j n_0}{1-\lambda_j}
          \longrightarrow L.                          \tag{7}
\]
An attempted ternary-precision gain illustrates the missing arithmetic
step exactly. Put h_j=n_j-n_0>0 for large j, u_j=v_2(h_j), and
v_j=v_3(h_j). Its natural denominator is at most 3^j-2^{A_j}. Using
(7), the inequality that would beat the denominator bound is
\[
 2^{A_j+u_j}3^{v_j}>
       |r_j-n_0|\,(3^j-2^{A_j})=2^{A_j}h_j.            \tag{8}
\]
After canceling 2^{A_j}, this asks for 2^{u_j}3^{v_j}>h_j, which is
impossible for a nonzero integer h_j. Using the reduced denominator
instead yields the equally exact obstruction (3). The needed gain is
therefore a theorem forcing an exact endpoint return, not a free
consequence of finite residue recurrence or real phase recurrence.

## 3. Why the simplest adelic Subspace product is at the critical scale

There is a second plausible architecture: use simultaneous real and
2-/3-adic approximation to the finite limit L in (4). First, algebraicity
of L is not established. Even if it were supplied, the natural pair does
not yield a Subspace-Theorem saving.

Put
\[
 p_j=2^{A_j}n_j,\qquad q_j=3^j,\qquad H_j=\max(p_j,q_j).
\]
These integers are coprime because n_j is a ternary unit; their 2-adic
and 3-adic local maximum norms are both one. At infinity take the two
linear forms LX-Y and X on (X,Y)=(q_j,p_j). At 2 and 3 take the coordinate
forms X,Y. The unnormalized product of their absolute values is exactly
\[
 \begin{split}
 \mathcal P_j
 &=|Lq_j-p_j|\,q_j\;2^{-A_j}\,3^{-j}\\
 &=\frac{L-L_j}{\lambda_j}
   =\frac13\sum_{h\ge0}\frac{\lambda_{j+h}}{\lambda_j}
   \ge1+(2/3)^{v_2(n_j+1)}>1.                         \tag{9}
 \end{split}
\]
The normalized product is therefore greater than H_j^{-2}. For every
fixed eta>0 and all sufficiently large j, it cannot satisfy the
Subspace-Theorem input inequality H_j^{-2-eta}. This is an exact
obstruction for this specified choice of dimension and forms. It is not
a theorem against every possible use of Diophantine approximation.

The positive future affine sum causes the floor in (9); its formal
minimum, attained by a future consisting only of valuation-one letters,
is exactly one. Such an infinite future is impossible for a positive
ordinary endpoint. Replacing j by any finite later exact endpoint leaves
the same lower bound. Subtracting a j-dependent lookahead while retaining the old
pair introduces moving coefficients; applying a theorem for fixed linear
forms would then need a separate height argument. Existing source proofs
of compressed-word descent obtain savings from bounded structural
complexity, not from the bare identity (4): see PR145, head
`dd245a712f985909f541590e3f6c179b7ba011e4`,
`research/pointwise-run-defects/COMPRESSED_DESCENT.md`, and
`research/unsafe-return-weights/VALUATION_ONE_RUNS.md`.

For the exact theorem normalization, see Evertse's
[p-adic Subspace Theorem, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf).
The arithmetic lower bound (9) is independent of that theorem; the
comparison only specifies why its standard two-coordinate small-product
hypothesis is unavailable here.

## 4. A concrete completion equation, and the remaining bridge

The density construction appends 1^b0^a to an actual prefix w of n_0.
If its fixed root were exactly n_0, equation (5) in that construction
would require
\[
 3^b(n_K+1)=2^b(n_0 2^a+1).                             \tag{10}
\]
For a>=1, the factor n_0 2^a+1 is odd, so necessarily
\[
 b=v_2(n_K+1).                                         \tag{11}
\]
This is precisely the finite run of odd shortcut inputs available at
the actual endpoint. The density construction instead sends b to
infinity while holding the finite prefix fixed, and pays for this in
its reduced denominator. It cannot be inserted as an ordinary
continuation of that fixed source.

A closure-capable improvement would have to prove, for an actual fixed
source, additional global cancellation or an exact return using its
unbounded sequence of available runs. It would have to beat the explicit
integer threshold (3), or produce a different fixed-form approximation
with a genuine power saving beyond (9). Neither follows from independent
finite approximants, a null exceptional set, limiting real rotation, or
the present calculations. These are the precise unresolved steps of this
attempt. No claim that a new name or this equivalent threshold resolves
the original problem is made.

## 5. Finite evidence

The companion checker uses actual finite prefixes of positive ordinary
sources for the exact pins and the completion equation. For a finite prefix
ending at M it can set a *formal* future valuation sequence equal to one,
giving L_formal=L_M+lambda_M. That continuation is only an algebraic
control for (9); it is not claimed to be the actual forward orbit.
The checker verifies the product identity and its weak lower bound one
exactly; it checks the stronger ordinary bound whenever the finite actual
prefix already includes the first gap greater than one from that endpoint.
Its finite success does not prove existence of an escaping orbit,
algebraicity of L, or any universal endpoint return.

The exact replay covered 31,523 nonreturn shortcut prefixes from ordinary
sources 1 through 400, with a maximum prefix length of 80, plus 80 actual
return controls. It checked 7,696 one-burst completion equations and
7,823 product identities from 333 ordinary odd ternary-unit sources up
to 1,000. Normal and `-OO` reports were byte-identical. The cycle witnesses
and these actual-prefix/formal-tail checks are identified separately in
`adic-real-density-report.json`.
