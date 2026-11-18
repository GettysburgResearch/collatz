# A component-local Stieltjes identity and convergent finite witnesses

**PROPOSED, source-qualified.** Use the odd Syracuse map
$U(x)=(3x+1)/2^{v_2(3x+1)}$, the unnormalized real fibre $F_t$ of
mass $b(t)=\lim_q L^q1(t)$, and
$K_z(t)=\int(z+B)^{-1} F_t(dB)$ for $z>0$. Nonunit fibres have
mass zero. The following results isolate two limits involved in the
[logarithmic escape test](STIELTJES_ESCAPE_FLOOR.md).

## Exactly retaining the predecessor component

Write $P(s)=\{n:U^j(n)=s\text{ for some }j\ge0\}$ for odd positive
$n$ and a fixed nonperiodic odd unit $s$. Write $p$ for normalized
odd logarithmic density and $\delta=\log(4/3)/2$. For $c>0$,
$$
\sum_{t\in P(s)}\int\left(\frac1{t+cB}-
\frac1{t+cB+(1+c)/3}\right)F_t(dB)
=\delta p(P(s))-\int\frac{F_s(dB)}{s+1/3+c(B+1/3)}.                 \tag{1}
$$
Indeed let $V_i$ be the product of $(1+1/(3U^j n))^{-1}$ for $j<i$.
Along an edge out of $t$ the mark is $B=t(1-V_i)$ and
$V_{i+1}=V_i t/(t+1/3)$. The two terms under the sum are the
[weighted source occupation formula](MOVING_ORDINARY_FIBRES.md)
applied to the consecutive values of $V/(1+c(1-V))$.
A source entering $P(s)$ belongs to $P(s)$ itself. Its visits there
are exactly its initial segment up to and including $s$, with no
repeats. The telescoping sum leaves the initial value 1 and the value
after departing $s$. The sum over fixed targets may be passed through
the source mean: the increment at $t$ is at most $(1+c)/(3t)$, and
the [simple-orbit reciprocal tail](../terminal-residue/SUPPORT.md)
above any fixed cutoff tends uniformly to zero on all such segments.
The density of $P(s)$ exists by the fixed-target first-hit law.
In particular the boundary term on the right is at most $3b(s)/c$.

Now fix an escaping spine $y_i=U^i(y_0)$ in a component $C$. Put
$R_i=V_\infty(y_i)>0$, $Y_i=y_i/R_i$, and $T_i=Y_i-y_i>0$. If
$J_i=3/2^{v_2(3y_i+1)}$, then
$Y_{i+1}=J_iY_i$ and $T_{i+1}=J_i(T_i-1/3)$.
For the unnormalized [ordinary distortion measure](HARMONIC_OFFSET_CONE.md)
restricted to this component, write
$L_C(c)=\int(1+cr)^{-1}\,d\mu_C(r)$. Then
$$
 cL_C(c)=\lim_{i\to\infty}K_{T_i+Y_i/c}(y_i),                       \tag{2}
$$
and this limit is increasing in $i$. Indeed the component measure is
$\delta E[V_\infty(n)\mathbf1_C\,\delta_{1-V_\infty(n)}]$ with the
ordinary limiting source law. On first reaching $y_i$ one has
$V_\infty=R_i(1-B/y_i)$.
Applying the weighted occupation formula shows that the restriction
through $P(y_i)$ is $F_{y_i}/Y_i$ pushed by
$B\mapsto (T_i+B)/Y_i$. These nested predecessor sets exhaust $C$.
For the limiting-law exhaustion one may first restrict to sources whose
ordinary minimum is at most $M$. All such sources in $C$ reach one
of the finitely many integers up to $M$ in $C$, each of which reaches
some $y_i$. The mass of sources with minimum above $M$ tends to zero by
the [minimum law](../fixed-floor-shells/FIRST_MOMENT.md).

The underlying exact identity on finite-trace phases is
$$
 K_z(t)=\sum_{a\ \mathrm{legal}} K_{(2^a z+1)/3}((2^at-1)/3).
$$
It follows from the canonical fibre recursion by cancellation of its
weight $3/2^a$ with the real dilation. Thus the branch back to $y_i$
at the next stage of (2) reproduces the preceding term exactly.
Every other branch makes a nonnegative addition. Fixed-root bounds
at $c\to\infty$ are insufficient to control this increasing limit:
the [disjoint sibling floor](STIELTJES_ESCAPE_FLOOR.md) already implies
$\liminf cL_C(c)/\log c>0$ if this one component exists.

## Logarithmic finite-clock behaviour within the basin of 1

For each large integer $k$ there is a segment $y_0,\ldots,y_k=t$ of
positive odd integers, all in the basin of 1, with $U(y_j)=y_{j+1}$,
$y_j\equiv-1\pmod{3^j}$ and $\log y_j\asymp k$ for $k/2\le j\le k$.
The entire segment and its continuation to 1 use $O(k)$ odd steps.
To obtain $t$, choose a large $q\asymp k$ with $k\le d(q-1)$ in
the [oversampled fixed-total floor, equation (3)](../native-pressure-20261118/EVERY-DEPTH.md)
from [paper 48, Lemma 7](https://rstation.ai/problems/collatz/papers/48/v2).
Take total $A=2q$ and prescribe
$\beta_w\equiv1+3^q2^{-A}\pmod{3^{q+k}}$.
There is a compatible length-$q$ word to target 1 with that
offset, and its ordinary inverse source
$t=2^A(1-\beta_w)/3^q$ is odd, positive, and $-1$ modulo $3^k$.
Positivity follows stepwise since a legal inverse of a positive odd
integer is again a positive odd integer. Thus
$2\cdot3^k-1\le t\le(4/3)^q$.
Set $y_j=2^{k-j}(t+1)/3^{k-j}-1$ for $0\le j\le k$.
These are positive odd integers, with valuation one at each step
before $t$, and $y_j+1\ge 2^{k-j+1}3^j$.

At depth $j$ define the truncated transform
$R_{j,z}(t)=\sum_w J_w/(z+\beta_w)$ over compatible length-$j$
words at $t$. It depends on $t$ modulo $3^j$. On the segment just
constructed,
$$
 R_{j,1}(y_j)=R_{j,1}(-1)=1+\sum_{m=1}^j R_{m,2}(-2)\asymp 1+j.      \tag{3}
$$
To verify this, remove all initial inverse letters 1 at $-1$.
Each such letter keeps the phase fixed, multiplies the weight by
$3/2$ and sends $B+1$ to $(3/2)(B+1)$, cancelling from the quotient.
There is one all-ones word. With $m\ge1$ letters remaining the first
letter exceeds 1. Subtracting 1 from it bijects these words to all
length-$m$ words at $-2$, doubles both the offset and weight, and
changes the denominator as in (3). The [rational trace classification](RATIONAL_PHASE_TRACE.md)
gives $\sup_m g_m(-2)<\infty$, hence the summands are bounded above.
Their uniform positive lower bound for large $m$ follows from the
[bounded-offset finite-word floor at every unit](STIELTJES_ESCAPE_FLOOR.md).
The full transforms on the same points satisfy
$K_1(y_j)\gg j$: their legal prefix of $j$ ones has offset
$(3/2)^j-1$, so the physical-target estimate in the same reference applies.

In particular a positive logarithmic lower bound at every clock of a
growing interval of order logarithmic height is compatible with reaching
1 shortly afterwards, all inside a single fixed ordinary component.
Even the exact finite-clock transform has matching logarithmic order
there. These finite witnesses vary with $k$; they do not exhibit an
infinite ordinary escaping spine. Excluding that fixed-source case,
or finding an upper estimate on its component transform in (2),
remains open.

## Joint finite source and Stieltjes scales on a fixed escaping component

Let $0<\eta<1$ be a [uniform orbit packing exponent](PRIOR_WORK.md):
a simple odd orbit visits $[H,2H]$ at most $O(H^\eta)$ times.
If the component $C$ escapes, there are absolute $A,b>0$ (for fixed
packing constants) and an onset $R_C$ such that
$$
 \frac1X\#\{X/4<n\le X:\ n\text{ odd in }C,       0<1-V_\infty(n)\le R^{-1}\}\ge b/R                          \tag{4}
$$
whenever $R\ge R_C$ and $X\ge A R^{1/(1-\eta)}$.
This controls finite shell counts at shrinking distortion radii.

Indeed put $S_i=\sum_{l\ge i}1/y_l$, and at each $i$ use the unit
sibling $s_i$ between $y_i$ and $21y_i$ from the
[disjoint entrant construction](STIELTJES_ESCAPE_FLOOR.md).
For $X\ge C s_i$, applying the [controlled first-landing estimate](../terminal-residue/SUPPORT.md)
at $a=M=s_i$ gives at least $b_1 X/s_i$ odd sources entering that
sibling with total pre-entry logarithmic correction $O(1/s_i)$.
The proof of that estimate controls the correction **up to entry**
regardless of the eventual minimum. The remaining correction, from
$s_i$ along the spine, is at most $C_1 S_i$. Thus the entire
relative distortion is at most $C_2 S_i$ for all these sources.
The selected families are disjoint in $i$.

Take the first $j$ with $C_2 S_j\le1/R$. As $S_{j-1}\le3S_j$,
one has $S_j\gg1/R$ for large $R$. The subset of the tail at heights
$y_i>H$ contributes at most $C_3 H^{\eta-1}$ by dyadic summation.
Choose $H$ a sufficiently large constant times $R^{1/(1-\eta)}$.
The retained $y_i\le H$ then contribute at least $S_j/2$. All
the chosen siblings have $s_i\le21H$. Summing the simultaneous
first-landing counts proves (4).

For $r(n)=1-V_\infty(n)$, set
$$
 L_{C,X}(c)=X^{-1}\sum_{X/4<n\le X,\ n\text{ odd in }C}
             \frac{V_\infty(n)}{1+c r(n)} .
$$
Integrating (4) on $1/c\le r\le1/R_C$ by the layer-cake identity
gives $L_{C,X}(c)\gg(\log c)/c$ uniformly for large $c$ and
$X\ge A c^{1/(1-\eta)}$ (increase $R_C$ to ensure $V_\infty\ge1/2$
in the retained events). Consequently one joint sequence of shell
averages over **all** odd sources below this rate in that range
would exclude escape. Periodic sources have $V_\infty=0$ and incur
no contribution. The proof supplies the lower estimate under escape;
an unconditional upper estimate of that order remains unavailable.
