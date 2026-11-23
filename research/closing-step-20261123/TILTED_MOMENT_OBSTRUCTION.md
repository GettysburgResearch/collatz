# A bounded stationary law with exponentially bad tilted carry moments

Status: proved counterexample to an abstract moment upgrade. This is **not**
an actual fixed-source Collatz orbit, and it is not asserted to be one.

The exact carry inequality in [COLLISION_CLOSURE.md](COLLISION_CLOSURE.md)
requires a moment under the squared-word law, not only a first-moment or
uniform-integrability statement under the original stationary law. The
construction below separates those conditions even for an ergodic process
whose gaps take only the values \(1\) and \(2\), with mean strictly below
\(\log_2 3\).

In particular, the missing original-source arithmetic cannot be replaced
by bounded gaps, stationarity, ergodicity, or a sublinear expected
logarithmic carry budget.

## 1. An explicit stationary regenerative process

Let \(R\) be a positive integer with distribution

\[
 {\mathbb P}(R=r)=\frac{4}{r(r+1)(r+2)},\qquad r\ge1.                 \tag{1}
\]

The telescoping identity

\[
 \frac{4}{r(r+1)(r+2)}
 =2\left(\frac1{r(r+1)}-\frac1{(r+1)(r+2)}\right)
\]

gives

\[
 {\mathbb P}(R\ge r)=\frac{2}{r(r+1)},\qquad
 {\mathbb E}R=\sum_{r\ge1}\frac{2}{r(r+1)}=2.                      \tag{2}
\]

A cycle of length \(2R\) consists of \(R\) consecutive gaps equal to \(2\),
followed by \(R\) consecutive gaps equal to \(1\):

\[
                         2^R1^R.                                \tag{3}
\]

Here (3) denotes a word, not exponentiation.

To specify the stationary law without a renewal-origin ambiguity, let
\((\Omega_0,\mathbb P_0,\sigma)\) be the two-sided iid shift of variables
\((R_j)_{j\in\mathbb Z}\) with law (1). Define the integer suspension

\[
 \Omega=\{(\omega,u):0\le u<2R_0(\omega)\}
\]

with probability measure

\[
 \mu(B)=\frac14
 {\mathbb E}_0\sum_{u=0}^{2R_0-1}{\bf1}_B(\omega,u).                \tag{4}
\]

The factor \(1/4\) is \(1/{\mathbb E}(2R)\). Let \(T\) advance \(u\) by one
within a cycle, and send its last point to \((\sigma\omega,0)\). Explicitly,

\[
 T(\omega,u)=
 \begin{cases}
  (\omega,u+1),&u<2R_0-1,\\
  (\sigma\omega,0),&u=2R_0-1.
 \end{cases}                                                     \tag{5}
\]

For any bounded test function \(F\), summing \(F\circ T\) over a fibre in
(4) replaces the term \(F(\omega,0)\) with \(F(\sigma\omega,0)\).
Their expectations are equal by shift invariance of \(\mathbb P_0\);
therefore \(T\) preserves \(\mu\).

The suspension is ergodic. Indeed, a \(T\)-invariant indicator is constant
along each suspension fibre, and its restriction to \(u=0\) is
\(\sigma\)-invariant. Ergodicity of the iid shift makes it almost surely
constant. The cycle lengths being even does not affect this invariant-set
argument.

Set

\[
 G(\omega,u)=
 \begin{cases}
  2,&0\le u<R_0,\\
  1,&R_0\le u<2R_0,
 \end{cases}
 \qquad G_j=G\circ T^{j-1}.                                      \tag{6}
\]

This is a stationary ergodic process with bounded gaps and

\[
 {\mathbb E}_\mu G
 =\frac{{\mathbb E}_0(3R)}4
 =\frac32<\log_2 3,                                               \tag{7}
\]

where the strict inequality follows from \(2^{3/2}=\sqrt8<3\).

## 2. Exact probability of the collision-favored words

For every \(m\ge1\), an \(m\)-letter all-\(2\) block can start at exactly
\((R-m+1)_+\) positions in a cycle. It cannot cross the intervening
all-\(1\) block. Hence (2) and (4) give the exact identity

\[
 \begin{aligned}
 {\mathbb P}_\mu(G_1=\cdots=G_m=2)
 &=\frac14{\mathbb E}(R-m+1)_+\\
 &=\frac14\sum_{r=m}^{\infty}{\mathbb P}(R\ge r)\\
 &=\frac14\sum_{r=m}^{\infty}\frac{2}{r(r+1)}
 =\frac1{2m}.                                                     \tag{8}
 \end{aligned}
\]

The all-\(1\) word has the same probability.

Write \(P_m(w)\) for the actual \(m\)-word law of this process, and put

\[
 Z_m=\sum_w P_m(w)^2,\qquad
 \widetilde P_m(w)=\frac{P_m(w)^2}{Z_m}.                            \tag{9}
\]

The sum is finite because the alphabet is \(\{1,2\}\), and

\[
             0<Z_m\le1,\qquad
 \widetilde P_m(2,\ldots,2)\ge\frac1{4m^2}.                        \tag{10}
\]

The latter bound uses the full normalizing constant \(Z_m\), not a
replacement law. In fact (8) also implies \(Z_m\ge1/(2m^2)\), because the
two constant words are distinct.

## 3. The complete carry on the all-\(2\) word

Use exactly the chronological carry convention of
[COLLISION_CLOSURE.md](COLLISION_CLOSURE.md):

\[
 a_i=\sum_{j=1}^i g_j,\qquad
 C_m(w)=\sum_{i=0}^{m-1}3^{m-1-i}2^{a_i},\qquad
 K_m(w)=\left\lfloor\frac{C_m(w)}{3^m}\right\rfloor.                \tag{11}
\]

For \(w=(2,\ldots,2)\), the elementary geometric-sum identity yields

\[
 C_m=4^m-3^m,\qquad
 K_m+1=\left\lfloor(4/3)^m\right\rfloor
       \ge\frac12(4/3)^m.                                        \tag{12}
\]

Combining (10) and (12), for **every fixed \(t>0\)**,

\[
 {\mathbb E}_{\widetilde P_m}(K_m+1)^t
 \ge \frac{2^{-t}}{4m^2}(4/3)^{tm}.                               \tag{13}
\]

Consequently,

\[
 \liminf_{m\to\infty}\frac1m
 \log{\mathbb E}_{\widetilde P_m}(K_m+1)^t
 \ge t\log(4/3)>0.                                                \tag{14}
\]

Thus the needed carry moment is exponentially large even before adding
any total-clock penalty. This remains true for every positive power;
it is not an issue restricted to the requirement \(t>1\).

The same phenomenon occurs under any \(q\)-word tilt, \(q>1\). Since
\(Z_{q,m}=\sum_wP_m(w)^q\le1\), replacing (9) with
\(P_m(w)^q/Z_{q,m}\) gives

\[
 {\mathbb E}_{P_m^q/Z_{q,m}}(K_m+1)^t
 \ge (2m)^{-q}\,2^{-t}(4/3)^{tm}.                                 \tag{15}
\]

## 4. The original logarithmic carry budget still vanishes

For completeness, this process satisfies the original-law conclusion
used in the Shannon bridge. Put

\[
 S_i=(G_1+\cdots+G_i)\log2-i\log3,\qquad
 M_m=\max_{0\le i<m}S_i.
\]

By ergodicity and (7),

\[
 \frac{S_i}{i}\longrightarrow
 \frac32\log2-\log3<0
 \quad\hbox{almost surely}.
\]

Therefore \(S_i\to-\infty\), its running maximum has a finite almost
sure limit, and \(M_m/m\to0\) almost surely. Also

\[
 0\le \frac{M_m}{m}\le 2\log2,
\]

so dominated convergence gives \({\mathbb E}M_m/m\to0\).
From (11),

\[
 \frac{C_m}{3^m}=\frac13\sum_{i=0}^{m-1}e^{S_i},
 \qquad
 0\le\log(K_m+1)\le M_m+\log(m+1).
\]

It follows that

\[
       \frac{{\mathbb E}_{P_m}\log(K_m+1)}{m}\longrightarrow0.       \tag{16}
\]

The normalized logarithmic carries are themselves uniformly bounded
up to the vanishing term \(\log(m+1)/m\), so there is no hidden
uniform-integrability defect in (16). Equations (13) and (16) hold for
the same stationary process.

## 5. What this does and does not settle

The process provides an exact separation:

- The original gap law is stationary, ergodic, bounded, and has mean
  \(3/2<\log_2 3\).
- Its original expected logarithmic carry is sublinear.
- Every positive carry moment under its squared-word law has an
  exponential lower bound.

The long all-\(2\) blocks have only polynomially small stationary
probability, so squaring word probabilities does not remove their
exponentially large complete carries. Bounded gap values do not control
the lengths of correlated excursions.

This is an obstruction to deriving the required tilted carry estimate
from the listed probabilistic hypotheses alone. It is **not** a
counterexample to a theorem imposing additional ordinary-source
arithmetic, and no claim is made that one fixed positive integer
realizes this stationary law along its Collatz orbit. Any closure
argument that excludes this behavior for the actual original source
must use that additional arithmetic explicitly.
