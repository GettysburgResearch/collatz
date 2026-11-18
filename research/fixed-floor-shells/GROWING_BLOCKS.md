# Prescribing the final height and allowing block length to grow

**Status: PROPOSED, pending independent review.** The map, basin $B_b$,
gate $(M,A,B,e,D,L,Q,t_0)$, and predecessor hypothesis $P(\gamma)$ are
as in [the shell theorem](PROOF.md). Sections FS-004/005 track the cost of
growing consecutive blocks. The resulting lower counts do not supply any
survivor upper estimate.

## FS-004. A terminal inverse step that absorbs the ternary phase

Let $A=3^Q$, $Q\ge1$, $P=2\cdot3^{Q-1}$, and $y$ be any positive odd
ternary unit. Given any **prescribed integer** $E\ge3P$, there is an
integer $0\le k<E$ with $1\le l=E-k\le3P$ such that

$$
 z=(2^l y-1)/3\quad\hbox{is odd positive},\qquad
 2^k z=e\pmod A,\qquad
 2^k z=\frac{2^E y}{3}\left(1-\frac1{2^l y}\right).
$$

Indeed $2^E y-3e$ is a unit modulo $3A$. Powers of two at the $3P$
consecutive exponents $E-3P,\ldots,E-1$ exhaust all units modulo $3A$.
Choose the exponent with $2^k=2^E y-3e\bmod 3A$. Reduction modulo three
gives $2^l y=1\bmod3$; the full congruence proves the claim. From $2^kz$,
one odd core recovers $z$, then the odd core of $3z+1$ recovers $y$.
There is no fiber loss proportional to $P$. For $y=1$ a possible integral
inverse has $z=1$, still a valid ordinary witness.

This permits the real-height selection to use the fixed circle
$\mathbb R/\mathbb Z$, whatever the ternary precision of the gate.
Indeed, first recode $n$ to $U$ by FS-001. Choose the unique
$p\in\{2,\dots,7\}$ satisfying $2^pU=4\bmod9$. Then
$y_0=(2^pU-1)/3$ is odd, a unit, and reaches $U$ in $p$ steps.
Repeat the same inverse instruction on $y_0,y_1,\ldots$.
Writing $S_j$ for the sum of the last $j$ selected exponents gives

$$
 y_0-1\le 3^j 2^{-S_j}y_j\le y_0 .
$$

This follows as in FS-002 since every multiplier is at least $4/3$.
Thus $\log_2 y_j$ differs modulo one from $\log_2 y_0-j\log_2 3$ by
at most $-\log_2(1-1/y_0)$ for $y_0>1$. Also $y_j\le 2^{7(j+1)}5n$,
and $y_j\ge y_0$ since the positive integral inverse with $p\ge2$
does not decrease its input.

Fix $0<\epsilon<1$. Put $\delta=\log_2(1+\epsilon)/12$ and take
$J=J_\epsilon$ such that $0\le j\le J$ give a $\delta$-net on the
unit circle. Choose $N_\epsilon$ so that for $n>N_\epsilon$ both
$-\log_2(1-1/y_0)$ and $-\log_2(1-1/(2y_0))$ are below $\delta$.
For the center $X\sqrt{1+\epsilon}$, choose $j\le J$ and an integer $E$
with $(M/(3A))2^E y_j$ within $2\delta$ of the center on the
base-two log scale (ordinary real distance). We can use any
$n\in B_b$ with $N_\epsilon<n\le aX$, where

$$
 a=\min(1,A/M)\,2^{-3P-7(J+1)-4}.
$$

Indeed $E\ge3P$ follows from the upper bound on $y_j$ and the lower
margin above $X$. Apply the terminal inverse step. Its extra logarithmic
error is at most $\delta$. The gate parameter $t=(2^kz-e)/A$ is integral,
and the outputs $x+d=(M/A)2^kz+B-Me/A+d$ lie in the claimed shell once
the fixed offsets have been absorbed. A sufficient threshold is that
$\max_{d\in D}|B-Me/A+d|\le c_\epsilon X$ and $Mt_0+|Me/A|\le c_\epsilon X$
for a sufficiently small positive $c_\epsilon$ depending only on
$\epsilon$. These follow from the positive lower and upper margins after
$3\delta$ of errors. Every output reaches the same $b$ as in FS-002.

Decode the anchor to $y_j$ using the two odd cores above. At most $J+1$
choices of $j$ recover $y_0$. There are at most six choices of $p$ and
two choices in the unit recoding. Therefore at least

$$
 \frac{A_b(aX)-A_b(N_\epsilon)}{12(J+1)|D-D|}
$$

disjoint gate translates occur. The only part of the exponential scale
loss involving $P$ is now $2^{3P}$. Both the rotation budget and the
fiber bound before disjoint thinning are independent of $Q$.

## FS-005. One explicit lower bound with growing block length

Write $\log^{(j)}$ for the $j$-fold iterated natural logarithm. Under
$P(\gamma)$, for every fixed $0<\epsilon<1$, all sufficiently large $X$
admit $X^{\gamma-o(1)}$ pairwise disjoint blocks of consecutive members
of $B_b$ in $[X,(1+\epsilon)X]$, each of length at least

$$
 K(X)=\lfloor\tfrac12\log^{(4)} X\rfloor .
$$

The small constant and four iterated logarithms give a safe elementary
rate. We do not claim optimal compiler complexity. The following upper
bound on a specific gate uses the equal-length two-chart compiler of
PR #132, frozen at
`7687eec1ac364009d644cb8d015f1fe3b28730cc`,
`research/astra-exit-merging/affine-completeness/PROOF.md`, ACS-002
(equation 8). That statement supplies a pair merge of length at most
$d(R+2)+6R+3$ for $(3^d y+b,y)$, with
$R=\mathrm{bitlength}(|b|+3^d)$. Its physical instructions impose
successive residues of the lower input $y$. The argument below accounts
for all $K$ original arms on their one common parameter.

After $L$ prescribed bits, write the initial sources as $B+2^L t+i$
for $0\le i<K$, $0\le B<2^L$. Each current arm is
$3^{q_i}t+c_i$ where $0\le q_i\le L$ and $c_i=T^L(B+i)$; use $T(0)=0$
only to compute the intercept at $t=0$. Positivity of the actual sources
holds for $t\ge1$ throughout. Since $T(n)+1\le(3/2)(n+1)$,
$0\le c_i\le(K+1)3^L$. Order the current representative and the next
unmerged arm by slope; their chart has $d=|q_i-q_j|\le L$ and
$|b|\le 2(K+1)3^{2L}$. The specified chart word extends the *same*
initial gate because the lower slope $3^{q_j}$ is invertible at two.
Previously joined arms stay joined.

Set $S=L+\lceil\log_2(K+2)\rceil+10$. Then $R\le 4S$ and
$S_{\rm next}\le 10S^2$ by the displayed pair bound. At most $K-1$ joins
yield $L\le(10S_0)^{2^K}$, with $S_0=\lceil\log_2(K+2)\rceil+10$.
The final common slope has $1\le Q\le L$ when $K\ge2$: pure halving
on two distinct arms of the same length could not merge them. Its
intercept satisfies $0\le e\le(K+1)3^L$ and is a unit modulo three
by the last odd step. We may take $t_0=1$.

For clarity about the slow rate, let $u=\log^{(4)}X$. With
$K\le u/2$, one has
$\log L\le 2^K\log(10S_0)=o(e^u)=o(\log^{(3)}X)$.
Consequently $L=(\log\log X)^{o(1)}$,
$P\le 2\cdot3^L=(\log X)^{o(1)}$,
and $\log(a^{-1})=O_\epsilon(P+L+1)=o(\log X)$.
Likewise $\max_{d\in D}|B-Me/A+d|+Mt_0+|Me/A|=X^{o(1)}$, since
$\log M=O(L)$ and $\log(e+1)=O(L+\log K)$.
All gate thresholds therefore hold uniformly for large $X$.
Now $aX=X^{1-o(1)}$ passes the one fixed target cutoff in $P(\gamma)$,
whereas $|D-D|=2K-1=X^{o(1)}$. Substitution in FS-004 proves the result.
