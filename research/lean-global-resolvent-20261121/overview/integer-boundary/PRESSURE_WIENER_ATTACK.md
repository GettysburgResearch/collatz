# The ordinary pressure operator in the Wiener algebra

Date: 2026-11-23. **Written deductions; escape exclusion remains open.**

This attack starts from PR177's ordinary atomic pressure measure and asks
whether its extra Archimedean Fourier regularity forces it to vanish. The
answer obtained here is not a closing theorem. It is an exact finite analytic
equation and an obstruction to proving its uniqueness by a spectral gap:
positive approximate fixed vectors already exist wholly inside the known
basin of 1, even in the weighted Wiener norms automatically available to an
escaping component. The true kernel, rather than its approximate spectrum,
is the remaining issue.

The source is PR177 at `6de3e304bb49a93a6c5ef0e5563137e75c7defb4`,
`research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ESCAPE.md`, especially
HE-P3--HE-P6. Its elementary positive path-product proof and ordinary
eigenmeasure classification are used, not claimed new. PR175 at
`8870528daa6a13cc941d602e578e35c8bfa4bf4f`,
`research/lean-global-closure-20261121/risk23/FOURIER_IDEMPOTENT_CLOSURE_ATTEMPT.md`
and `HARDY_INVERSE_TREE.md`, was read to distinguish this attempt from its
basin-indicator Fourier-measure criterion and its unweighted pushforward
operators. The operator below is the weighted ordinary pullback, not those
operators.

## 1. The actual ordinary operator

Let O be the positive odd integers coprime to 3. Write

\[
 a(n)=v_2(3n+1),\qquad U(n)=(3n+1)/2^{a(n)},
 \qquad (A_s h)(n)=(3/2^{a(n)})^s h(U(n)).                 \tag{W1}
\]

For real s>1, the coefficient space is

\[
 \mathcal A_t=\{h:O\to\mathbb C:\quad
       \|h\|_t=\sum_{n\in O}n^t|h(n)|<\infty\},
       \qquad 0\le t<s-1.                               \tag{W2}
\]

At t=0 this is the analytic Wiener algebra with coefficient support O.
All operators and norms here retain the ordinary integer index.

The operator is bounded. For q in O, its predecessors are exactly
`n=(2^e q-1)/3` for e>=1 for which that value is an integer unit. Thus

\[
 \sum_{Un=q}n^t(3/2^{a(n)})^s
 \le q^t\,\frac{3^{s-t}}{2^{s-t}-1}.                    \tag{W3}
\]

Tonelli applied to absolute values proves the bound. For t=0 the exact
operator norm is

\[
 \|A_s\|_0=
 \frac{3^s(2^{-s}+2^{-3s})}{1-2^{-6s}},                  \tag{W4}
\]

attained at columns q=2 mod 9: their legal gaps are 1 and 3 modulo 6.
The other five unit residues have the legal gap pairs listed in Section 4.

PR177 proves that an escaping ordinary component E supplies

\[
 h_{E,s}(n)=1_E(n)\left(\frac{\Lambda_\infty(n)}n\right)^s,
 \qquad 0<\Lambda_\infty(n)\le1,
 \qquad A_sh_{E,s}=h_{E,s}.                             \tag{W5}
\]

In particular h belongs to every space (W2), with h(n)<=n^(-s).
Taking its real Fourier series therefore supplies an absolutely convergent
function, and weighted absolute convergence supplies the indicated additional
regularity. This is actual regularity of the hypothetical ordinary measure;
it does not identify that measure with ternary Haar measure.

## 2. Positive approximate fixed vectors inside the known basin of 1

### Theorem W-Q

For every s>1 and every 0<=t<s-1, there are nonnegative vectors f_k in
the space (W2), all supported on integers that provably reach 1, with

\[
 \|f_k\|_t=1,\qquad
 \|(I-A_s)f_k\|_t
 \le 2^t(2/3)^{(s-t)k}\longrightarrow0.                 \tag{W6}
\]

Moreover every exact fixed vector of A_s is zero on this known basin.
Consequently

\[
 \operatorname{dist}_{\mathcal A_t}
       (f_k,\ker(I-A_s))=1.                            \tag{W7}
\]

The range of I-A_s is not closed, and I-A_s is not Fredholm, in every one
of these spaces. The vectors can also be replaced by nonnegative finitely
supported coefficient vectors, with residual tending to zero and unchanged
support qualification.

### Proof: an explicit family of actual convergent trajectories

For k>=1 set

\[
 e_k=3^{k+1}+1,\qquad
 q_k=(2^{e_k}-1)/3,\qquad
 p_k=2^k(q_k+1)/3^k-1.                                 \tag{W8}
\]

The elementary divisibility

\[
 3^{m+1}\mid 2^{3^m}+1\quad(m\ge0)                    \tag{W9}
\]

follows by induction. The case m=0 is immediate; if x=2^(3^m), then
`x^3+1=(x+1)(x^2-x+1)`, and the second factor is divisible by 3 because
x=-1 mod 3. Thus q_k+1 is divisible by 2*3^(k+1).

The actual successive states from p_k to q_k are

\[
 n_j=2^{k-j}3^j\frac{q_k+1}{3^k}-1,
       \qquad 0\le j\le k.                            \tag{W10}
\]

They are positive odd integers congruent to -1 modulo 3. For j<k,
`3 n_j+1=2 n_(j+1)` and n_(j+1) is odd, so the exact gap is one.
At the last state `3 q_k+1=2^(e_k)`, so its next odd state is 1.
This is a literal trajectory, with no residue-class surrogate or unproved
convergence premise.

For example, k=1 gives `227 -> 341 -> 1`, at odd gaps 1 and 10.
For k=2 the states are `39768215 -> 59652323 -> 89478485 -> 1`,
at odd gaps 1, 1 and 28. These examples illustrate the all-k formula;
finite verification is not its proof.

### Proof: the whole ancestor resolvent is summable

Fix one of the nonperiodic roots q=q_k. For n in O define

\[
 h_q(n)=
 \begin{cases}
 (3^j/2^{a(n)+\cdots+a(U^{j-1}n)})^s,&U^j(n)=q,\\
 0,&\text{no such }j.
 \end{cases}                                          \tag{W11}
\]

The empty path has value 1. The hitting depth is unique because q is not
periodic: q goes to 1 and q>1. The edge telescope gives

\[
 h_q(n)=q^s\Lambda(n,q)^s n^{-s}\le q^s n^{-s}.         \tag{W12}
\]

Consequently h_q is in (W2), since s-t>1. Every nonzero coefficient is
at an actual ancestor of q and hence reaches 1. Its exact defect is

\[
 (I-A_s)h_q=\delta_q.                                  \tag{W13}
\]

At an ancestor other than q this is the edge recurrence. At q, h_q(Uq)
is zero because 1 cannot reach q. Outside the ancestor set both terms
are zero. No omitted terminal branch is being treated as harmless.

The actual source p_k contributes

\[
 \|h_{q_k}\|_t\ge p_k^t(3/2)^{sk}.                    \tag{W14}
\]

Also q_k/p_k <= 2(3/2)^k. Indeed
`p_k=(2/3)^k(q_k+1)-1`, and `(2/3)^k q_k>=2` for k>=1.
For the last bound, `e_k>=3k+2` gives
`q_k>2^(3k)` and hence `(2/3)^k q_k>(16/3)^k`.
Dividing (W13) by the norm and using (W14) proves (W6).

For an exact fixed vector h, its coefficient at 1 obeys
`h(1)=(3/4)^s h(1)`, so h(1)=0. Every ordinary predecessor in that
basin then has coefficient zero by (W1), without needing any sign
assumption. Disjoint support proves (W7). A bounded operator with closed
range is bounded below modulo its kernel, so (W6)--(W7) prove the range
claim. Fredholm operators have closed range.

Finally, finite coefficient truncations of h_q converge in (W2).
Boundedness (W3) makes their defects converge as well. Choose each
truncation accurate enough relative to its h_q norm, and then normalize.
All surviving coefficients still lie in the same explicitly convergent
basin. This proves the finite-support variant, without asserting an
uncomputed finite truncation depth or rate.

## 3. What this does and does not rule out

The obstruction is stronger than an abundance of signed square-summable
flows: the vectors in (W6) are nonnegative, absolutely summable, and can
have any of the additional weighted absolute convergence in (W2). It is
also independent of hypothetical escaping components.

It rules out a uniform estimate
`dist(h,ker(I-A_s)) <= C ||(I-A_s)h||_t` in these spaces and hence the
proposed closed-range or Fredholm route to uniqueness. It does not show
that an exact nonzero fixed vector exists. The unilateral-shift analogy
is pertinent only in this precise respect: lack of closed range does not
decide whether the kernel is zero.

The fixed envelope in (W5) is not satisfied uniformly by our normalized
approximate vectors. In fact they eventually vanish at every fixed
ordinary index. A fixed n that reaches one can meet only finitely many
of the distinct roots q_k; a fixed n outside that basin meets none.
Thus, after normalization, their entire unit norm moves to larger indices.
If they also obeyed a uniform bound `C n^(-s)` with C independent of k,
dominated convergence in (W2) would contradict their unit norm.

This distinction leaves a concrete potential route: prove true-kernel
uniqueness using the fixed absolute coefficient envelope, rather than
claiming a norm spectral gap. No such uniqueness proof was obtained.

## 4. A finite equation for the actual analytic function

For a coefficient series H(z)=sum_(n in O) h(n) z^n, let R_e retain the
indices in the following two residue classes modulo 9:

| e modulo 6 | retained q modulo 9 |
|---|---|
| 1 | 2, 8 |
| 2 | 1, 4 |
| 3 | 2, 5 |
| 4 | 1, 7 |
| 5 | 5, 8 |
| 0 | 4, 7 |

These are exactly the classes for which `(2^e q-1)/3` is integral and
not divisible by 3. Each R_e can equivalently be expressed by a finite
filter using ninth roots of unity. It is bounded on the Wiener spaces.

For an exact fixed vector, coefficient comparison gives

\[
 zH(z^3)=3^s\sum_{e\ge1}2^{-es}(R_eH)(z^{2^e}).        \tag{W15}
\]

Grouping the period-six filters yields the finite equation

\[
 zH(z^3)-2^{-6s}z^{64}H(z^{192})
 =3^s\sum_{e=1}^6 2^{-es}(R_eH)(z^{2^e}).              \tag{W16}
\]

Conversely, (W16) for a power series supported on O implies (W15):
iterate the substitution z->z^64 in the missing tail; every fixed
coefficient eventually lies below the tail's first possible exponent.
At coefficient `3n+1`, there is exactly one term on the right of (W15),
at e=v_2(3n+1), and its remaining index is U(n). Thus (W16) recovers
exactly (W1), with no added or discarded ordinary solutions.

At s=2 all displayed constants are rational. Multiplication by 4096 gives

\[
\begin{split}
4096zH(z^3)-z^{64}H(z^{192})={}&
9216(R_1H)(z^2)+2304(R_2H)(z^4)\\
&+576(R_3H)(z^8)+144(R_4H)(z^{16})\\
&+36(R_5H)(z^{32})+9(R_6H)(z^{64}).                    \tag{W17}
\end{split}
\]

The exact kernel question can therefore be passed on without importing
the dynamical language: must a series supported on positive indices
coprime to 6, with `0<=h(n)<=n^(-2)`, satisfying (W17), vanish?
PR177's component construction and classification make a positive answer
equivalent to absence of escaping components, not to absence of positive
nontrivial cycles. The finite equation itself is a reformulation; no
reduction in mathematical difficulty is claimed for it.

## 5. The attempted analytic closure and its remaining step

The hoped-for implication was that absolute Fourier convergence on the
real circle, combined with the ternary conformal relation and strict Haar
mass contraction, would force h=0. Absolute convergence is indeed present,
but (W6) defeats the direct bounded-inverse argument. It also defeats
repairing that argument with the finite coefficient moments automatic
from h(n)<=n^(-s).

Varying s does not create a second independent dilation equation. For a
single putative escaping component, the series
`H_s(z)=sum_(n in E) exp(s log(Lambda_infinity(n)/n)) z^n`
is entire in s at each |z|<1. The positive uniform path-product bound in
PR177 bounds the coefficients on compact s-sets by a constant times a
power of n, which justifies that assertion. Its value at s=0 is the
component indicator series. Thus parameter continuation returns the
original component at zero; no additional coefficient rigidity has been
derived from it.

The inspected primary literature does not directly close (W17):

* Schaefke--Singer, *Mahler equations and rationality*, Theorem 1,
  <https://singer.math.ncsu.edu/papers/vshort2-5.pdf>, requires separate
  finite 2-Mahler and 3-Mahler equations. Equation (W16) is one mixed
  equation, with residue filters. Neither separate equation was obtained.
* Siegel, *Conservation of Singularities in Functional Equations Associated
  to Collatz-Type Dynamical Systems; or, Dreamcatchers for Hydra Maps*,
  <https://arxiv.org/abs/1909.09733>, describes its finite-support
  singularity classification. Only the primary abstract was inspected in
  this pass. No applicable finite singularity-support theorem for (W17)
  is asserted, and a Wiener function by itself does not supply one.

The next mathematical step is true-kernel uniqueness within the specified
positive coefficient envelope, or an estimate retaining the same original
atom that implies it. This note proves neither that step nor escape
exclusion. The new spectral obstruction is a constructive diagnosis of
the attempted method, not evidence that an escaping component exists.

## Verification scope

The companion `check_pressure_wiener.py` checks the actual trajectories
(W8)--(W10), the six exact branch filters, and the finite equation for the
operator on arbitrary test coefficient polynomials, all using integer or
Fraction arithmetic. It does not calculate the full ancestor resolvent,
an escaping component, or an infinite norm. The infinite arguments above
are written proofs and have no Lean-verification claim.
