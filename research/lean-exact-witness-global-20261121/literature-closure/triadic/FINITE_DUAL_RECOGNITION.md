# The paid finite test recognizes the exact complementary point

23 November 2026. **A positive finite recognition theorem; the universal
existence of a successful candidate remains open.** The same horizon as
PR176's finite convergence certificate actually forces joint arrival at
the standard complementary cycle. Thus a successful candidate is exactly
the complementary 2-adic point, rather than only a sufficiently long
approximation to it.

This note is a written deduction from the literal paired transitions and
weighted product of PR176 at
`fb402404deb810bd8e32e596993739bb5a6967d1`,
`research/lean-global-resolvent-20261121/overview/triadic-height/TRIADIC_AMORTIZED_BUDGET.md`.
It does not add a Lean declaration or enlarge the formal scope of
`SourceTailPullback.lean`. The three earlier files in this directory
remain unchanged.

## 1. The exact finite statement

Let \(n>0\) be an ordinary integer, \(a\in\mathbb Z\), and \(r\ge0\).
The presentation \(a/3^r\) need **not** be reduced. Define

\[
F(0)=1,\qquad F(r)=\prod_{j=0}^{r-1}(1+3^j),
\]

\[
B=n\max(1,|a|)F(r),\qquad
E=\operatorname{bl}(B),\qquad H=9E+1.                 \tag{1}
\]

Here \(\operatorname{bl}(B)\) is the least positive integer \(E\) with
\(B<2^E\). In particular \(B\ge1\) and \(E\ge1\).

Start the paired state at \((x_0,w_0,r_0)=(n,a,r)\). At clock \(i\),
the compatibility test is that \(x_i\) and \(w_i\) have opposite parity.
When it passes, apply the literal rules

\[
\begin{array}{c|ccc}
\text{case}&x_{i+1}&w_{i+1}&r_{i+1}\\ \hline
x_i\text{ odd}&(3x_i+1)/2&w_i/2&r_i\\
x_i\text{ even},\ r_i>0&x_i/2&(w_i+3^{r_i-1})/2&r_i-1\\
x_i\text{ even},\ r_i=0&x_i/2&(3w_i+1)/2&0.
\end{array}                                               \tag{2}
\]

The represented dual \(y_i=w_i/3^{r_i}\) therefore follows its actual
shortcut map, and the displayed denominator exponent never increases.

**Finite exact-recognition theorem.** If all tests at clocks
\(0,\ldots,H-1\) pass, then there is a clock \(J\le8E\) such that

\[
\boxed{x_J=1,\qquad w_J=2\cdot3^{r_J}.}                \tag{3}
\]

One may take \(J\) to be the first hit of \(1\). Consequently the two
represented trajectories continue forever as the complementary cycle
\((1,2),(2,1)\), and

\[
\boxed{\frac a{3^r}=\Omega(n).}                        \tag{4}
\]

Here \(\Omega(n)\) is the unique 2-adic point with parity itinerary
complementary to that of \(n\), in the framework of Monks--Yazinski,
Section 1 and Theorem 2.1
([primary author PDF](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf)).
The finite joint-arrival assertion (3) can be stated without introducing
an infinite conjugacy.

## 2. A globally nonincreasing product before zero

At a state with \(w_i\ne0\), put

\[
                     P_i=x_i|w_i|F(r_i).                \tag{5}
\]

Every original state is a positive integer. At an odd original input,

\[
\frac{P_{i+1}}{P_i}=\frac{3x_i+1}{4x_i}\le1.          \tag{6}
\]

The ratio is one at \(x_i=1\), and at most \(5/6\) when \(x_i>1\).
An original-even input at positive exponent satisfies

\[
\begin{aligned}
2|w_{i+1}|&\le |w_i|+3^{r_i-1}
                    \le |w_i|(1+3^{r_i-1}),\\
P_{i+1}&\le P_i/4.                                    \tag{7}
\end{aligned}
\]

At exponent zero, an original-even input gives

\[
\frac{P_{i+1}}{P_i}=\frac{|3w_i+1|}{4|w_i|}\le1.      \tag{8}
\]

For negative \(w_i\) this ratio is at most \(3/4\); for positive odd
\(w_i\ge3\) it is at most \(5/6\). Its only tie is \(w_i=1\).
Thus \(P\) is nonincreasing at every compatible nonzero step, including
steps after the original trajectory has reached \(1\). No
nonconvergence hypothesis is used for this monotonicity.

## 3. Exclude zero entry before locating the first hit

The order of these two arguments is essential: the first-hit bound must
not be inferred from a sufficient horizon that only promises a hit by
\(H\).

**Initial zero.** If \(a=0\), every passed test forces an original odd
input and keeps the dual numerator zero. For \(L\) such steps,

\[
2^L(x_L+1)=3^L(n+1),\qquad 2^L\mid n+1.              \tag{9}
\]

But \(n+1\le B+1\le2^E\), while \(L=H>E\). This is impossible.
Hence \(a\ne0\), and \(P_0=B\).

**First zero at a positive clock.** Suppose its first occurrence is at
\(j\le8E\). The only branch that can create it from a nonzero integer
numerator is the positive-denominator even branch. Immediately before
entry, \(w_{j-1}=-3^{r_{j-1}-1}\), and therefore

\[
0<x_j+1=\frac{x_{j-1}}2+1
       \le x_{j-1}\le P_{j-1}\le B<2^E.               \tag{10}
\]

This includes \(x_j=1\). The inequalities use (6)--(8), which hold
without any assumption about whether \(1\) has already been reached.

There are \(H-j\ge E+1\) further passed tests. All of their original
inputs must be odd because the zero numerator persists. Applying (9)
at clock \(j\) gives \(2^{H-j}\mid x_j+1\), contradicting (10).

We have proved, independently of any first-hit assertion,

\[
                  w_i\ne0\quad(0\le i\le8E).         \tag{11}
\]

## 4. The original first hit occurs by \(8E\)

Suppose \(x_i>1\) at every clock \(i\le8E\). By (11), all associated
products are positive integers. At every step except a possible
exponent-zero tie \(w_i=1\), the factor is at most \(5/6\). In that tie,
\(w_{i+1}=2\); compatibility makes \(x_{i+1}\) odd, and under the current
assumption it is at least three. The following step contracts by at least
\(5/6\).

Every pair of steps therefore gives
\(P_{i+2}\le(5/6)P_i\), and every eight steps strictly halve the product,
because \(2\cdot5^4<6^4\). Iterating through clock \(8E\) yields

\[
              0<P_{8E}\le(5/6)^{4E}B<2^{-E}B<1,
\]

which is impossible. There is a first hit \(J\le8E\). Equations
(6)--(8) and (11) give

\[
 x_J=1,\qquad w_J\ne0,\qquad
                P_J=|w_J|F(r_J)\le B.                 \tag{12}
\]

Compatibility at clock \(J\) says \(w_J\) is even, so
\(|w_J|\ge2\).

## 5. The remaining bits force exact equality

First record an elementary bound on the same denominator weight:

\[
                         3^q+1\le2F(q)\quad(q\ge0).  \tag{13}
\]

At \(q=0\) this is equality. If it holds at \(q\), then
\(2F(q+1)\ge(1+3^q)^2\ge1+3^{q+1}\), since
\((1+v)^2-(1+3v)=v(v-1)\ge0\) for \(v=3^q\ge1\).

For any integer \(w\) with \(|w|=m\ge2\), (13) gives

\[
\begin{aligned}
|w-2\cdot3^q|
 &\le m+2\cdot3^q\\
 &\le m+4F(q)-2\\
 &\le 2mF(q).
\end{aligned}                                           \tag{14}
\]

The last difference is exactly
\((m-2)(2F(q)-1)\ge0\). Applying (14) at the first-hit state gives

\[
             |w_J-2\cdot3^{r_J}|\le2P_J\le2B<2^{E+1}.\tag{15}
\]

Let \(L=H-J\ge E+1\). From clock \(J\), the original states are
\(1,2,1,2,\ldots\). The candidate and the standard complementary orbit
starting at \(2\) follow the same \(L\) dual branches, because all
remaining tests pass. Thus

\[
                         2^L\mid w_J-2\cdot3^{r_J}.  \tag{16}
\]

Here is a finite integer justification that retains unreduced
denominators. Let \(q\) count odd **dual** branches in these \(L\) steps,
and let \(c_L\in\{1,2\}\) be the corresponding standard complementary
terminal value. Subtracting the two finite affine recurrences gives

\[
3^q(w_J-2\cdot3^{r_J})
=2^L\left(3^{r_J-r_H}w_H-3^{r_J}c_L\right).           \tag{17}
\]

The expression on the right is an integer because (2) gives
\(r_H\le r_J\). Since three is odd, (17) implies (16). This argument
does not assume that any displayed fraction is reduced, and it does not
identify a real limit with a 2-adic limit.

Equations (15)--(16), together with \(L\ge E+1\), force
\(w_J-2\cdot3^{r_J}=0\). This proves (3). The represented dual value at
\(J\) is exactly \(2\), so the two trajectories remain complementary
forever. Uniqueness of the complementary parity point proves (4).

## 6. Consequences and the remaining construction

### An endpoint congruence recognizes the exact dual

For the actual first \(H\) original bits, define \(b_H,D_H\) by (3) of
[SOURCE_TAIL_TRANSPORT.md](SOURCE_TAIL_TRANSPORT.md). Then the single
finite integer condition

\[
                  2^H\mid3^{b_H}a+3^rD_H              \tag{18}
\]

forces the theorem's literal \(H\) compatibility tests. Indeed the forced
terminal value is

\[
\frac{3^{b_H}a+3^rD_H}{3^r2^H},
\]

which has an odd denominator under (18). Pulling it back through the
literal complementary word selects the required parity at every step;
the affine identity recovers the initial \(a/3^r\). Thus (18), with its
own horizon (1), implies both joint arrival (3) and exact equality (4).

Conversely, if \(a/3^r=\Omega(n)\), every finite complementary test
passes by definition, so (18) holds. Therefore, for each specified
positive \(n\) and specified triadic fraction, this is a finite exact
recognition criterion:

\[
\boxed{
2^H\mid3^{b_H}a+3^rD_H
\quad\Longleftrightarrow\quad a/3^r=\Omega(n).
}                                                       \tag{19}
\]

This decides equality for a **supplied candidate**. It does not provide a
bound on the search for a candidate, nor assert that one exists for every
positive \(n\).

### Accepted rational values are unique

Two candidates passing their respective horizons for the same \(n\)
represent the same rational value. Their numerator/exponent presentations
may differ by powers of three; uniqueness is of the represented value.

### The exact reduced denominator records a source clock

If \(n>2\) and an accepted candidate is reduced, write its first-hit clock
as \(J\) and its number of original-even inputs before that hit as
\(b_J\). The denominator computation in Proposition 1 of
[SOURCE_TAIL_TRANSPORT.md](SOURCE_TAIL_TRANSPORT.md) now applies to the
convergence just proved, and gives

\[
                    \operatorname{den}_3(\Omega(n))=b_J-1>0.
                                                               \tag{20}
\]

In particular, an integer candidate can pass its own horizon only for
\(n=1\) or \(n=2\), with represented values \(2\) and \(1\), respectively.
No integer candidate certifies a different positive source through this
criterion. Reduced or unreduced triadic presentations remain permitted.

The new theorem strengthens what a successful finite candidate certifies.
Constructing that candidate from an arbitrary positive input, or from the
complete witness for the original \(x\) while targeting \((x+1)/2\), is
still the missing universal step. No such construction is assumed in
(3), (19), or (20).
