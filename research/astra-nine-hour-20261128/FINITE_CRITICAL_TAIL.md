# A finite parity deficit certifies a positive cycle

**PROPOSED, unconditional finite theorem.** Let
\(T(n)=n/2\) for even \(n\), and \(T(n)=(3n+1)/2\) for odd \(n\).
For a positive integer \(n\le X\), let \(q=F_t(n)\) be the number of odd
departures in the first \(t\) shortcut steps. Suppose that integers
\(d\ge1\) and \(t\ge0\) satisfy

\[
 t=2q+d,\qquad t\le d^2,\qquad X^2 3^{t+1}<4^{t+1}.                 \tag{1}
\]

Then two states among \(n,Tn,\ldots,T^{t-1}n\) are equal. In particular
the actual positive orbit has already entered a positive cycle.

Every test in (1) uses integer arithmetic. There is no asymptotic
population input, probabilistic assumption, or hypothesis that all
orbits converge. The conclusion does not identify the cycle as
\(1\to2\to1\). The proposed Lean kernel is
`FiniteCriticalTail.lean`; its exact replay status belongs in the
checkpoint evidence, independently of this written proof.

## A simple path cannot accumulate enough correction

Define the exact multiplicative correction

\[
 R_t(n)=\frac{2^tT^t(n)}{3^{F_t(n)}n}
       =\prod_{\substack{0\le i<t\\T^i(n)\text{ odd}}}
          \left(1+\frac1{3T^i(n)}\right).                         \tag{2}
\]

For every integer \(x\ge1\),

\[
 \left(1+\frac1{3x}\right)^2\le1+\frac1x.
\]

An even departure has correction one and obeys the same upper bound.
If the first \(t\) states are distinct, write them in increasing order
\(x_1<\cdots<x_t\). Then \(x_j\ge j\), so

\[
 R_t(n)^2\le\prod_{j=1}^t\left(1+\frac1{x_j}\right)
      \le\prod_{j=1}^t\left(1+\frac1j\right)=t+1.                 \tag{3}
\]

The Lean implementation uses the equivalent induction removing the
largest element of a finite set. Positivity of every ordinary state is
proved from the actual update, and the affine identity is proved by
induction on the actual trajectory.

On the other hand \(T^t(n)\ge1\), \(n\le X\), and (2) imply

\[
 4^t\le9^q X^2 R_t(n)^2\le9^qX^2(t+1).                          \tag{4}
\]

For every integer \(d\ge1\), elementary induction gives

\[
 3^{d+1}\ge4(d^2+1)\ge4(t+1).                                  \tag{5}
\]

The base \(d=1\) is \(9\ge8\); multiplying its induction hypothesis
by three leaves the nonnegative polynomial
\(4(2d^2-2d+1)\) at the next step. Multiply (4) by four and apply (5):

\[
 4^{t+1}\le9^qX^2\,3^{d+1}=X^2 3^{t+1},
\]

contrary to (1). Thus the initial states are not all distinct. If
\(T^i(n)=T^j(n)\), \(i<j<t\), determinism gives a positive periodic
future of period dividing \(j-i\).

## The critical count has an exact finite interpretation

Let

\[
 t_X=\max\{t\in\mathbb N:4^t\le X^2 3^t\},\qquad
 a_X=\lceil\sqrt{t_X}\rceil.
\]

For \(t_X\ge1\), every source counted by

\[
 B(X)=\#\{1\le n\le X:2F_{t_X}(n)\le t_X-a_X\}                \tag{6}
\]

has a repeated positive state before the observation ends. Indeed take
\(d=t_X-2F_{t_X}(n)\); maximality of \(t_X\) gives the strict clock
inequality in (1), while \(d\ge a_X\) gives \(d^2\ge t_X\).

The critical population law in
[the companion note](escape/CRITICAL_CORRECTION.md) says, under its
explicit external inputs, that the limit of \(B(X)/X\) is a mixture of
cycle contributions. Escaping components contribute zero to this strict
lower tail. The finite theorem proves the exclusion of a simple
trajectory directly, without those inputs. Establishing the specified
Gaussian limit value remains a global problem; counting many finite
instances does not establish that value.

## Exact bounded computation

`critical_tail_probe.cpp` evaluates both literal shortcut iteration and
an independent version grouping consecutive even steps. The driver
`check_critical_probe.py` decides the logarithmic clock by integer
powers, checks each source's two odd counts, and compares a literal
Python control through 4,096. Arithmetic overflow is checked before
every native multiplication by three.

The initial replay reached \(X=2^{24}\):

| \(X\) | \(t_X\) | \(a_X\) | \(B(X)\) |
|---:|---:|---:|---:|
| 16 | 19 | 5 | 0 |
| 256 | 38 | 7 | 1 |
| 4,096 | 57 | 8 | 287 |
| 65,536 | 77 | 9 | 11,372 |
| 262,144 | 86 | 10 | 39,222 |
| 1,048,576 | 96 | 10 | 183,065 |
| 4,194,304 | 106 | 11 | 487,859 |
| 16,777,216 | 115 | 11 | 2,864,542 |

These are counts at the stated deterministic clocks. The ratios are
not monotone, and their finite oscillations must not be interpreted as
a proven limiting normalization. The checkpoint receipt records the
exact source hashes, compiler, commands and comparison coverage.
