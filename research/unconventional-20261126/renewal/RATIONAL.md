# Rational points force a deep interrecord excursion

**Status — PROPOSED.** Use the first-ladder word $w$ and drawdown
$D=D(w)$ from [the record conventions](README.md). Let $q,q'$ be its
actual initial and terminal positive odd integers, $m$ its odd length
and $s$ its shortcut clock. Valuations of zero are $+\infty$.
Constants with a subscript $z$ can depend on that fixed rational.

**Theorem R.** For every rational $z_2\in\mathbb Z_2$ and
$z_3\in\mathbb Z_3$, every such ordinary record block satisfies

$$
 \min\{v_2(q-z_2),s\}\le C_{z_2}(1+D),                            \tag{R2}
$$


$$
 \min\{v_3(q'-z_3),m\}\le C_{z_3}\,2^{(39/40)D}.                 \tag{R3}
$$

In particular, on any sequence of record blocks with lengths tending
to infinity and drawdowns bounded, every subsequential limit of their
starts in $\mathbb Z_2$ and every subsequential limit of their ends in
$\mathbb Z_3$ is irrational. If all such terminal limit points are
rational, the drawdowns of the long blocks must tend to infinity.
The first conclusion takes its two coordinates on the *same actual
blocks*. Neither finite sections of a 2-adic word nor a probability
measure supplies an ordinary infinite realization.

## Forward shadows and the dyadic bound

Even $z_2$ are immediate. Start at an odd rational with fixed positive
odd denominator $d$. Follow its genuine shortcut map, which is
defined on $\mathbb Z_2$, including any future zero. Up to a
singularity $3z+1=0$, the odd map uses literal positive integer
gaps. The following possibilities exhaust its future:

1. Its odd-time coefficient crosses strictly above one at a finite
   odd time.
2. Its shortcut path reaches zero.
3. Its genuine odd path is eventually periodic on a positive rational
   cycle, and its coefficients never crossed above one.

To verify this, assume that there is neither a crossing nor a hit of
zero. Fixed odd denominator numerators $a_j$ are integers under the
exact gaps. With $P_j=3^j/2^{S_j}\le1$,

$$
 a_j=P_j\left(a_0+\frac d3\sum_{i<j}P_i^{-1}\right).
$$

Thus $a_j$ is eventually positive. If its positive tail is injective,
the signed positive simple-path count from PR210, section 2, gives
$\sum 1/a_j<\infty$: its count up to $X$ is $O_d(X^{39/40})$.
On that positive tail the product of $1+d/(3a_j)$ is bounded. Its
exact multiplier therefore tends to infinity with the distinct
positive integers $a_j$, contradicting $P_j\le1$. A repeat instead
gives an eventual positive cycle. Its product of forward coefficients
per lap is strictly less than one, since the product of the positive
distortion factors on a lap is strictly greater than one. The
fixed-denominator counting proof works also when $3\mid d$; it uses
the odd coefficient modulo powers of two. Alternatively, after each
nonzero odd step a factor 3 of a reduced denominator cancels until the
denominator is prime to three.

In the first case, agreement through the finite crossing and its odd
endpoint bit makes it the first crossing for $q$ too. Thus the minimum
in (R2) is bounded by a constant depending on the crossing clock
even if $D$ is large. In the other two cases the *native-clock*
coefficient $C_t$ of the rational shortcut path satisfies
$C_t\le A_{z_2}2^{-b_{z_2}t}$ for all $t$, with $b_{z_2}>0$.
For zero this is its eventual all-even tail; for a positive cycle it
follows from its strict per-lap multiplier. If
$t=\min\{v_2(q-z_2),s\}$, the first $t$ shortcut parity bits match
by the exact parity congruence. On the supplied first-ladder block its
native coefficient never falls below $2^{-D}$: within a gap it first
rises by $3/2$, then falls through halvings to its next odd endpoint.
Consequently $2^{-D}\le A_{z_2}2^{-b_{z_2}t}$, proving (R2).

## Backward shadows and the ternary bound

Read the block gaps backwards from $q'$. The inverse prefix multiplier
is $A_j=P_{m-j}/P_m$, and thus

$$
              \eta=(2/3)2^{-D}\le A_j<1,\qquad 1\le j\le m.
$$

Put $A_0=1$. For $b=\min\{v_3(q'-z_3),m\}$ the same backwards
prefix through $b$ steps lifts exactly as rational inverses from
$z_3$, since the difference after $j$ steps is $A_j(q'-z_3)$.
Write $z_3=a/d$ reduced, $d>0$, $3\nmid d$. All inverse numerators
over $d$ are integers. If $d$ is even, each inverse
$3a_j=2^{e_j}a_{j-1}-d$ increases divisibility of the numerator by
two until the full power of two in $d$ can be cancelled. One more
inverse gives odd numerator. For odd $d$ the same single inverse
suffices if its original numerator is even. The finitely many prefix
possibilities through $h=1+v_2(d)$ have bounded clocks because
$2^{S_j}<3^j$ in this backwards convention. Thus after at most $h$
steps the numerator and remaining denominator are odd, the possible
starting rational values there are finite, and $1/A_h\le(3/2)^h$.
If $b\le h$, (R3) is immediate. Nongenuine denominators at 3 were
never inverted.

Use the following source-qualified finite signed-path lemma from PR210,
sections 2--3: a distinct integral inverse-numerator chain with odd
initial numerator $u$, fixed positive odd denominator $d'$, $3\nmid d'$,
and all relative inverse coefficient multipliers bounded by $H\ge1$,
has at most $C_{d'}(H|u|)^{39/40}$ vertices. Its proof applies signed
simple-path counting and the product distortion bound separately on
the positive and negative portions. With relative slack $1/A_h$, it
bounds the entire remaining chain by a constant depending on $z_3$
if that chain is distinct.

Otherwise a repeated numerator puts the one at index $h$ on a
genuine rational odd cycle: reading edges forwards is deterministic.
While the backwards path follows that cycle it has only one cycle
predecessor at each phase. Its inverse multiplier over one primitive
lap is a rational $\lambda=2^v/3^p\ne1$. As long as the path remains
on it the prefix products stay in $[\eta,1]$, so at most
$C_{z_3}(1+|\log\eta|)$ steps can agree with the cycle. For
$\lambda>1$ use the upper bound and the fixed $A_h$; for
$\lambda<1$ use the lower bound. There are only finitely many possible
initial cycle phases after the normalization above.

Suppose the first off-cycle numerator is $u_j$, after an on-cycle
numerator $u_{j-1}$. All numerators from $j$ onward are distinct:
a repeat makes that repeated vertex periodic and its forward iterate
$u_j$ periodic on this same cycle, contrary to the departure. The
complete relative inverse multipliers of the distinct tail are at
most $1/A_j$. The one-step identity gives

$$
 |u_j|/A_j \le |u_{j-1}|/A_{j-1}+d'/(3A_j)\le C_{z_3}/\eta .
$$

The finite signed lemma bounds its length by
$C_{z_3}\eta^{-39/40}$. This absorbs the initial finite piece
and $1+|\log\eta|$, proving (R3). This argument quantifies how an
actual long first-ladder block loses a rational endpoint when its
drawdown is held fixed. PR210 classified the entire rational trace
without this two-ended drawdown condition.

## A stronger cap for the signed rational shadow

The last power in (R3) can be replaced by
[the bounded-height estimate](HEIGHT.md) on the *reflected signed
numerator path*. More precisely, with the same actual block and fixed
rational terminal,
$$
 \min\{v_3(q'-z_3),m\} \le
 C_{z_3}2^{\theta D}\exp[-c_{z_3}D^{1/3}].                     \tag{R3+}
$$
For this application use the height part of the finite signed lemma
in PR210, section 3: every numerator on a distinct inverse tail with
initial $u$ and relative slack $H$ satisfies
$|u_i|\le C_{d'}H|u|$. The proof controls the distortion separately
until a sign change and on the negative tail. In the departure case
above, $H|u|=|u_j|/A_j\le C_{z_3}/\eta$; in the entirely distinct
case it is bounded just in terms of $z_3$. The backward sign can
switch only once, from positive to negative. Read each constant-sign
piece forwards. Its distinct positive magnitudes follow the
odd-to-odd map with numerator $3x+c$, $c=d'$ or $c=-d'$, and every
displayed step has positive output. All intermediate shortcut values
are positive and at most $(3C_{z_3}/\eta+d')/2$ or $C_{z_3}/\eta$.
A repeated even value would force the following odd endpoint to
repeat; the odd magnitudes are distinct.

For fixed odd signed $c$, the proof of (H1) runs on these positive
simple shortcut pieces with constants depending on $|c|$. Indeed
the low-odd-count affine remainder is at most
$|c|((3/2)^p-1)$ in absolute value, leaving the eventual contraction
to $Y/2$ in (H3). On a high band with floor $Y>2|c|$ the absolute
logarithmic distortion per odd step is at most
$2|c|/(3Y\log2)$. Exact native parity cylinders still have modulus
$2^t$ since $3$ and $c$ are odd. The same elementary word count and
fourth-moment estimate now prove (H1) on each signed piece. Applying
it at the height $C_{z_3}/\eta$, and reintroducing the
$O_{z_3}(1+D)$ periodic portion, proves (R3+). This step does not
extend a theorem stated only for positive $3x+1$ to signed
numerators by citation.

**Sources.** PR210 at
[592328fecf8ea2cf41736294856d95f890a1ba98](https://github.com/GettysburgResearch/collatz/blob/592328fecf8ea2cf41736294856d95f890a1ba98/research/critical-record-rational-rigidity-20261125/README.md),
sections 2--4, supplies the finite signed estimate and predecessor
rigidity. The signed bound was checked at that fixed head. The
covariation of the two rational approximations is a necessary
condition on actual record blocks, not an impossibility of escape.
