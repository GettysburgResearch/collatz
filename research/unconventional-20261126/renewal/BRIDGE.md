# Simultaneous dyadic–ternary precision and record-return spacing

**Status — PROPOSED.** These are deterministic inequalities for any
finite positive ordinary trajectory with the stated record endpoints.
No bound on interrecord gaps or orbit sampling assumption enters.

A chronological word of $m$ positive gaps, native clock $s$ and
partial clocks $S_j$ acts by $F(t)=(3^m t+C)/2^s$, with

$$
 C=\sum_{j=0}^{m-1}3^{m-1-j}2^{S_j}>0.
$$

If its two endpoints are strict coefficient records, $2^s<3^m$.
This includes segments containing intermediate records. Since
$s-S_j\ge m-j$, summing a geometric progression gives

$$
 C\le 2^s((3/2)^m-1)<(9/2)^m.                                    \tag{B1}
$$

For the drawdown $D=\max_{0\le j<m}(S_j-j\log_2 3)$ we also have
$C\le (m/3)3^m2^D$ directly from the sum. All bounds retain the
full integer carry.

## One block with different rational shadows at its two ends

Write $u=A/d\in\mathbb Q\cap\mathbb Z_2$ and
$v=B/e\in\mathbb Q\cap\mathbb Z_3$ in lowest terms with positive
denominators. For an ordinary segment from $q$ to $q'$, put

$$
 a=\min(v_2(q-u),s),\qquad b=\min(v_3(q'-v),m),\qquad
 N=3^m A e+de C-2^s B d.
$$

The value $+\infty$ for an exact match is allowed before truncating.
Subtract the exact endpoint equation to get

$$
              N=3^m e(A-dq)+2^s d(e q'-B).                         \tag{B2}
$$

Thus $2^a3^b\mid N$. For a single first-ladder block of length
$m>3(\max(v,0)-u)$ this integer is nonzero. In fact
$F(t)=r(t+h_w)$, $r>1$ and $h_w\ge m/3$ from the proper-prefix
inequalities, so $F(u)=v$ would require
$m/3\le v/r-u\le\max(v,0)-u$.

**Theorem B.** Every such single block satisfies

$$
 a\log2+b\log3\le
 \min\!\left\{m\log(9/2)+O_{u,v}(1),\
 m\log3+D\log2+\log(m+1)+O_{u,v}(1)\right\}.                      \tag{B3}
$$

Indeed the left side is at most $\log|N|$. The first bound uses
(B1) and $2^s<3^m$ on the other two terms. For the second use
$C\le (m/3)3^m2^D$. In particular $s=\lfloor m\log_2 3\rfloor$
for a first-ladder block gives

$$
 \frac{a}{s}+\frac{b}{m}\le 2-\log_3 2+O_{u,v}(1/m).
$$

If $D=o(m)$ along a sequence with $m\to\infty$, its upper limit
is at most one. The two independent local precisions are measured
at the **start** and **end** of the same word. Without the real
sign/length obstruction to $N=0$, the product bound would have an
exception for exact signed affine bridges. The divisibility (B2)
also applies to multiblock segments whenever $N\ne0$.

## Returns to an algebraic ternary neighborhood

Let $q_i,q_j$ be two ordinary coefficient record values, separated
by $m>0$ odd steps. Put $w$ equal to their entire intervening
chronological word. The rational fixed point

$$
              z_w=-\frac{C}{3^m-2^s}                               \tag{B4}
$$

has negative sign, odd numerator and odd denominator prime to
three. It is a genuine periodic point of the signed rational odd
map: replay the word from (B4). A nongenuine first gap either
gives negative dyadic valuation at once, or gives positive valuation
which cannot persist to an odd target; any subsequent gap then
gives negative valuation. Negative valuations can never return to
zero. Hence all its gaps are genuine. The first-ladder blocks in
this word are its successive strict coefficient record phases on
periodic replay, because each block crosses strictly above its start
only at the end. If $q_i\equiv q_j\equiv z\bmod 3^b$, then

$$
                       z_w\equiv z\bmod3^b.                          \tag{B5}
$$

Indeed $F(q_i)=q_j$ and $F$ contracts ternary differences by $3^{-m}$.
Thus $F(z)-z$ is divisible by $3^b$ in $\mathbb Z_3$. The factor
$3^m/2^s-1$ has valuation zero at three, so the same is true of
$z-z_w$.

**Theorem B.1.** Suppose $z\in\mathbb Z_3$ is algebraic over
$\mathbb Q$ of degree $d$ and is not a negative signed periodic
record phase. Let $P\in\mathbb Z[X]$ be an irreducible polynomial
for $z$, and put $\|P\|_1=\sum|P_i|$. Each pair of record visits
to $z+3^b\mathbb Z_3$ is separated by at least

$$
             \frac{b-\log_3\|P\|_1}{d\log_3(9/2)}                  \tag{B6}
$$

odd steps, whenever the right side is positive. Consequently the
number through odd time $n$ is at most one plus $n$ divided by that
positive bound. This includes rational $z$ with $d=1$.

Write (B4) as $A/B$ with the possibly unreduced
$A=-C$ and $B=3^m-2^s>0$. By (B1) both absolute values are at
most $(9/2)^m$. The integer $B^dP(A/B)$ is nonzero by hypothesis:
an irreducible polynomial having a rational root is linear.
The congruence (B5) and $3\nmid B$ make it divisible by $3^b$.
Its absolute value is at most $\|P\|_1(9/2)^{dm}$. Taking
logarithms gives (B6). For a periodic rational target, the same
bound holds for every pair whose intervening word *does not*
fix that target. This allows exceptional exact cycles to be
identified by their true word.

For an arbitrary nonperiodic ternary $z$ there is also a qualitative
spacing law independent of measure theory. For any time threshold
$T$ the set of words with $m\le T$ and $2^s<3^m$ is finite.
Their rational fixed points (B4) form a finite set missing $z$
if one restricts to concatenations of ladder words. At a sufficiently
large ternary precision $b$ none can share $z\bmod3^b$. By (B5)
all returns are then more than $T$ odd steps apart. This proves
the ternary conclusion (F3) of [the stationary-flow theorem](RECORD_FLOW.md)
by a direct finite argument.
