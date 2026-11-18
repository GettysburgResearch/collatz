# Target distribution of the full positive first-hit pressure

**FS-013–015: PROPOSED, pending independent review.** These are
unconditional population statements on odd positive *targets*. They rely
on the all-depth predecessor-minimum transfer in
[FS-010](PREDECESSOR_MINIMA.md). The resulting critical estimate is sharp
in its scale in probability. It is not pointwise on a prescribed
unbounded trajectory.

Let $S$ be the positive odd Syracuse map. For the first hit from odd $x$
to odd $t$, let $q$ be its Syracuse depth, $A$ the total valuation, and
$J_0(x,t)=3^q/2^A$, with the empty hit having weight one. For $s>1$ put

$$
 H_s(t)=\sum_{x\text{ odd first hits }t}J_0(x,t)^s .
$$

This is first-hit pressure (the source occurs once); repeat visits around
a positive cycle are not added. The exact inequality $J_0(x,t)\le t/x$
follows by composing affine maps with nonnegative offsets, so this sum
is finite for each positive $t$. The definitions and existing averaged
decay estimates are credited to PR #143,
`research/pressure-decay-20261031/PROOF.md`, PF-001/001b, at the source
pin given below. No simple-path sparsity estimate from that packet is
needed here.

Define the ternary random variable on $\alpha\in\mathbb Z_3$

$$
 \mathcal H_s(\alpha)=
 \sum_{\text{finite inverse valuation words legal at }\alpha}
          (3^q/2^A)^s ,
$$

with the empty word included. Haar probability is denoted by $\mu_3$.
For $1<u<2$ one has

$$
 \int\mathcal H_u\,d\mu_3=
 \sum_{q\ge0}\left(\frac{3^{u-1}}{2^u-1}\right)^q<\infty .
$$

Each word has legality probability $3^{-q}$; summing its weight over
all positive letters gives the displayed expression. The strict
inequality $3^{u-1}<2^u-1$ follows from strict convexity of
$\log(1+3^{u-1})-u\log2$, whose endpoints at 1 and 2 are zero.
For every $s>1$ choose $1<u<\min(s,2)$. Since $u/s<1$,
$\mathcal H_s^{u/s}\le\mathcal H_u$. In particular the limiting pressure
is finite almost surely even at and above the critical second moment.

## FS-013. Tight first-hit clocks for every comparable source

For every fixed $R>0$, in odd target density,

$$
 \lim_{M\to\infty}\limsup_{X\to\infty}\frac1X
 \#\big\{t\in[X,2X]\text{ odd}:
     \text{some odd }x\le Rt\text{ first hits }t
     \text{ after more than }M\text{ shortcut steps}\big\}=0.
$$

The maximum is over *all* such sources for that target. This includes
sources larger than the target. The factor $1/X$ rather than the reciprocal
of the number of odd targets only changes a constant.

Fix a small $0<\theta<1$ and discard $m(t)<\theta t$, where $m(t)$ is
the least ordinary predecessor. By FS-010 this costs at most $\theta^2$
of odd targets asymptotically. On every remaining path to $t$, *all*
states are at least $\theta t$, since each state is itself a predecessor.

We need the following extension of the late-record count in FS-010.
Allow a source $x\le BX$ to be **above** its terminal record
$r\in[aX,bX]$, with all states before $r$ at least $aX$ and strictly
larger than $r$ at interior clocks. If the segment has length greater
than $L$ and $r$ is a strict future record from $x$ (or from its first
iterate if $x<r$), the number of possible such $r$ is
$o_{L\to\infty}(X)$ in the iterated limsup along the good clocks in
FS-010, even after multiplying the relative error by any fixed power
of $L$. Constants may depend on $a,b,B$.

Indeed the initial source $x\le BX$ remains above $aX$ up to time $L$.
Hence $(3+1/(aX))^q/2^L\ge a/B$ for its odd count $q$. With fixed
$a,B$ and all sufficiently large $L$, the limiting cutoff for $q/L$
exceeds some fixed number strictly between $1/2$ and $\log_3 2$.
The parity count in FS-010 thus gives exponentially small upper density
for those starting $x$. When the final record transition has length
at most $L$, there are $O_{a,b,B}(L+1)$ possible record destinations
per starting $x$, since each drop inside $[aX,2BX]$ consumes at least
$\Delta_L/2$ in logarithmic height. When the final record transition
is long, its immediate preceding record is instead a no-descent source
to $L$, counted once globally and determining its unique next record.
A terminal record reached directly from the initial $x$ in a long
transition is also covered by this latter case. This proves the extension.

Now read a simple first-hit path $x\to t$ backwards, taking successive
strict inverse records as in FS-010. All of these are at least $\theta t$.
The first long arc, if any, ends at an upper record $r\in[\theta X,2X]$;
preceding short arcs in backward order cost $O_\theta(L^2)$ clock in
total. The late-record count and at most $O_\theta(L^2)$ forward
iterates per $r$ bound their possible $t$ by an exponentially vanishing
limsup fraction. If no such long arc occurs, consider the remaining
prefix from $x$ to the smallest reverse record $r$. This is either
empty or goes from $x>r$ to $r$ with all interior values strictly above
$r$. If it is long, apply the extended record count with
$a=\theta$, $B=2\max(R,1)$, and the same bounded multiplicity from $r$
forward to $t$. Otherwise the entire path has length
$M=O_\theta(L^2)+L$. Send $L\to\infty$ and then $\theta\downarrow0$.
This proves FS-013.

## FS-014. Whole first-hit pressure has the ternary Haar law in target density

For every $s>1$ and every bounded Lipschitz test function $f$,

$$
 \lim_{X\to\infty}\frac{1}{\#\{t\le X:\ t\ {\rm odd}\}}
 \sum_{\substack{t\le X\\t\ {\rm odd}}}f(H_s(t))
   =\int_{\mathbb Z_3}f(\mathcal H_s(\alpha))\,d\mu_3(\alpha).
$$

First truncate the ordinary sum to odd $x\le Rt$ for fixed $R\ge2$,
and the ternary sum to words with $D_w=2^A/3^q\le R$.
If the shortcut clock is also bounded by $M$, these are finite sums.
An integral word produces exactly the ordinary source $D_wt-C_w$, with
$C_w>0$ for nonempty words and $C_w=0$ for the empty word. Thus the
source-size condition agrees for all sufficiently large $t$ with the
ternary slope cutoff, including equality. Distinct words of bounded
clock that reach $t$ more than once from a given source require a
positive return of $t$ in at most $M$ steps. Each possible return word
has at most one positive fixed point by its affine formula
($3^q\ne2^A$ for nonempty odd words). Therefore for large $t$ these
finite sums coincide exactly as a function of its ternary residue.
Their laws in $[X,2X]$ converge to the Haar law by residue counting.

Remove $M$ with $R$ still fixed. On the ordinary side the probability
that any omitted first-hit source exists tends to zero by FS-013. On
the ternary side the cutoff sums increase to the stipulated truncation
of the almost surely finite $\mathcal H_s$; bounded convergence applies
to $f$. This proves convergence for each fixed-size truncation.

To remove $R$ on the ordinary side, fix $\varepsilon>0$.
FS-013 at ratio 2 supplies a *fixed* $M_\varepsilon$ such that all but a
limsup proportion at most $\varepsilon$ of odd $t$ in the shell have
every first hit from $y\le2t$ completed within $M_\varepsilon$.
Call these targets good. For each odd source $x>RX$ whose orbit ever
enters the odd interval $[1,2X]$, take its first such odd state $y$.
Every good shell target visited by that orbit satisfies $y\le2t$,
so its first visit from $y$ occurs within $M_\varepsilon$ shortcut steps.
The complete orbit of $x$ therefore visits at most $M_\varepsilon+1$
distinct good shell targets, regardless of its initial height or fate.
An orbit never entering the interval visits none. By $J_0(x,t)\le t/x$,
Tonelli bounds the total omitted pressure over good targets, divided by
the number of odd targets in the shell, by

$$
 O_s\!\left((M_\varepsilon+1)X^{s-1}\sum_{x>RX}x^{-s}\right)
 =O_s((M_\varepsilon+1)R^{1-s}).
$$

Here $x>Rt$ implies $x>RX$; enlarging the sum is legitimate. Thus the
error on test-function averages is at most this bound times the Lipschitz
constant plus $O(\varepsilon\|f\|_\infty)$ from the discarded targets.
First let $R\to\infty$ with $M_\varepsilon$ fixed, then
$\varepsilon\downarrow0$. On the ternary side monotone convergence of
the pressures and bounded convergence of $f$ remove $R$. This proves
the asserted law on shells, hence on cumulative intervals by dyadic
summation.

## FS-015. Sharp typical scale of the critical pressure observable

Writing $F(t)=H_2(t)/t^2$ as in PF-001, $t^2F(t)$ is tight in ordinary
odd target density. More precisely its limiting law is $\mathcal H_2$.
For every positive $g(t)\to\infty$, the set of odd targets on which

$$
 \frac1{t^2}\le F(t)\le\frac{g(t)}{t^2}
$$

has relative density one. The lower bound holds at every target from
the empty word. For the upper bound first use tightness at a fixed
constant, then let that constant grow. Large finite spikes and spikes
along a sparse hypothetical divergent trajectory are allowed by the
statement. No claim of convergence of the untruncated *mean* is made;
in fact $\int\mathcal H_2\,d\mu_3=\infty$.

[PF-001/PF-001b source](https://github.com/GettysburgResearch/collatz/blob/41a408e5e617fb4e65142485f6f3ff3e6ef6c408/research/pressure-decay-20261031/PROOF.md).
