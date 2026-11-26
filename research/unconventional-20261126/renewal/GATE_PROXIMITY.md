# Critical-trace proximity of heavy ordinary gates and sharp leakage through exponent two

**Status — PROPOSED ordinary gate theorem.** Use the physical cutoff
$X$, its first-exit gate $y=(3p+1)/2$ and its mass $J_{s,X}(y)$
from [OP-G1–G4](../operator/GATE_ARITHMETIC.md). Here $p$ is the
immediately preceding positive odd integer. Let $\mathcal R_b$
be the union of ternary depth-$b$ cells of strict critical
backward odd-gap prefixes, and let $\mathcal R$ denote the
infinite critical trace. Every such finite prefix can be
periodically extended, so these are exactly the depth-$b$
neighborhoods of $\mathcal R$. Put
$\gamma=\log3/\log(3/2)=2.70951\ldots$.

**Theorem P.** For fixed $s>1$ and $\varepsilon>0$, every physical
gate with $J_{s,X}(y)\ge\varepsilon$ satisfies, uniformly for
$X$ sufficiently large,
$$
             \operatorname{dist}_3(p,\mathcal R)
                   \ll_{s,\varepsilon} p^{-\gamma}(\log p)^C.       \tag{G1}
$$
The finite exponent $C$ is absolute and effective using a real
two-logarithm estimate. Since $p\asymp X$, this quantifies
proximity in terms of the *ordinary* size of the positive pre-gate.

For a fully specified power-thin finite sieve, set
$b=\lceil\log_3 X\rceil$, and keep the gates $y$ whose pre-gate
$p$ lies in $\mathcal R_b$. Write this set as $E'_X$, and let
$D_s(X)=\sum_{y\notin E'_X}J_{s,X}(y)$. With
$\theta=H_2(\log_3 2)$, one has
$$
 |E'_X|\ll X^\theta(1+\log X)^{-3/2},\qquad
 D_s(X)\begin{cases}
 \asymp_s X^{1-s}, &1<s<2,\\
 \asymp X^{-1}\log X, &s=2,\\
 \ll_s X^{-\log_3(2^s-1)}, &s>2 .
 \end{cases}                                                       \tag{G2}
$$
The lower bounds through $s=2$ hold after deleting *any*
collection of $O(X^{1-\eta})$ gate sites at each threshold,
for fixed $\eta>0$ (with constants allowed to depend on the
deletion bound). The upper bounds concern the particular sieve
$E'_X$. They sharpen the leakage estimate in OP-G3. The
matching-order assertion in (G2) stops at $s=2$.

## First failure of a critical suffix

In any first exit from below, its pre-gate $p$ is strictly larger
than every previous odd state on that source's path: an earlier
odd $u\ge p$ would already have successor $(3u+1)/2\ge y\ge X$.
Read a suffix of $j$ valid odd gaps ending at $p$, of total native
clock $S$. If its incoming slope $r=3^j/2^S$ is less than one,
let $u<p$ be its initial ordinary odd. Its positive normalized
affine carry is at most $(3/2)^j-1$, since each odd-to-odd
operation divides by at least two and the all-gap-one composition
maximizes the carry. Therefore
$$
                        p(1-r)\le (3/2)^j.                          \tag{G3}
$$
The exact product identity for the odds $x_h$ traversed there gives
$2^S/3^j=(u/p)\prod_{h<j}(1+1/(3x_h))\le(4/3)^j$, so $S\le2j$.
The two-logarithm lower bound for the nonzero
$S\log2-j\log3>0$ yields $1-r\gg (2j)^{-A}$ for an effective
absolute $A$. For $S\log2-j\log3\ge1$ this inequality is immediate.
Hence every failing suffix has
$$
              j\ge\log_{3/2}p-O(\log\log(3p)).                     \tag{G4}
$$
Take logarithms in (G3), separating off $j>2\log_{3/2}p$ first.
Ties $r=1$ at $j>0$ are impossible. The argument is a
paradoxical-sequence height bound applied to each possible
backwards suffix, with its full positive carry and both endpoint
inequalities. [Real two-log bound, Lagarias, proof of Theorem 3.2](https://matwbn.icm.edu.pl/ksiazki/aa/aa56/aa5614.pdf)
· [Paradoxical Collatz lengths and related height bounds](https://rstation.ai/problems/collatz/papers/231)

Given a heavy gate, choose $H$ so that $\sum_{x>H}x^{-s}<\varepsilon$.
Some actual source $x\le H$ contributes. Its first odd $u$ is at
most $H$. If the path to $p$ has no failing suffix, it is entirely
critical backwards, and contains at least
$\log_{3/2}((p+1)/(H+1))$ odd-to-odd steps by the shifted-height
bound. Otherwise all depths before its first failure are critical,
which by (G4) gives at least $\log_{3/2}p-O(\log\log(3p))-1$
such odd gaps. In either case periodic extension of this very
prefix gives (G1). Every rational point $a/d$ of the trace in that
matching cell, written with $d>0$, $3\nmid d$, must have ordinary
height $\max(|a|,d)\gg_{s,\varepsilon}p^{\gamma-1}/(\log p)^C$.
Indeed $p\notin\mathcal R$ by positive integer rigidity and
$3^j\mid dp-a\ne0$, whereas $|dp-a|\le(p+1)\max(|a|,d)$.
This is a height requirement on its rational witnesses.

## Summing exact short paths

The [critical word count](GAUGE.md) is
$O(3^{\theta b}(1+b)^{-3/2})$. Each depth-$b$ cell contains
$O(1)$ candidate integers $p\asymp X$ because $3^b\ge X$.
This proves the cardinality in (G2). By (G4), for all large $X$
each actual path reaching some $y\notin E'_X$ has *fewer than*
$b$ completed odd gaps before $p$; otherwise its critical suffix
through $b$ would put $p\in\mathcal R_b$. Thus its entire binary
word, including the final odd departure from $p$, has grade
$j\le b$. Any initial even steps before the first odd are included
in its native clock $k$ and do not increase $j$.

For one native word of grade $j$, clock $k$, each matched shell
endpoint solves a single congruence modulo $3^j$. There are
$O(X/3^j+1)=O(X/3^j)$ such integers because $3^j\le3^b<3X$
(up to equality at powers of three). Each endpoint fixes at most
one integer source for that word by the affine identity, and its
retained mass equals exactly
$(3^j/(2^k y))^s$. Summation over *all* words only increases the
positive bound. The resulting series is
$$
 \begin{aligned}
 D_s(X)&\ll_s X^{1-s}\sum_{j=0}^b 3^{(s-1)j}
               \sum_{k\ge j}\binom{k}{j}2^{-sk}\\
       &\ll_s X^{1-s}\sum_{j=0}^b
                     \left(\frac{3^{s-1}}{2^s-1}\right)^j .
 \end{aligned}                                                     \tag{G5}
$$
The ratio is below one for $1<s<2$, equals one at $s=2$ and
exceeds one for $s>2$: equivalently
$2^{-s}+3^{s-1}2^{-s}$ is strictly convex, equals one at $1,2$
and increases thereafter. This proves all upper estimates.
For $1<s<2$, deleting a power-thin set leaves order $X$ shell
gates. Each has mass at least $(3/(2y))^s$ from its direct odd
predecessor, yielding the required lower bound.

## Why the logarithm at two is necessary

Fix a deletion set of size $O(X^{1-\eta})$. Give backwards native
letters the sole counting law $\Pr(O)=3/4$ and $\Pr(E)=1/4$.
For a word of length $k$ and grade $j$, write $C_i$ for its incoming
prefix slope. Its probability is exactly $C_k^2 3^{-j}$. This
walk in $\log C_i$ has strictly positive drift. For some fixed
$0<\xi<1/4$, the event $C_i\ge1+\xi$ for all $1\le i\le k$
has probability bounded below independently of $k$. For example
start with $N$ odd letters and then use the positive-drift
walk from that height. For small $t>0$, $\mathbb E[C_1^{-t}]<1$;
a union bound over the negative excursions of the fresh sums
gives post-initial failure at most
$(1+\xi)^t(3/2)^{-Nt}\sum_{j\ge1}(\mathbb E[C_1^{-t}])^j$.
Choose $N$ large and absorb the finitely many shorter clocks.

For $1\le k\le c_\eta\log X$, choose $c_\eta>0$ sufficiently
small that $3^k\le X^{\eta/2}$ and
$k(3/2)^k=o(X)$. For every retained word its terminal congruence
class supplies $\gg X/3^j$ integers
$X\le y\le(1+\xi/2)X$, even after deleting the entire specified
set since $X/3^j\ge X^{1-\eta/2}$. The first backwards letter
must be $O$, so these ordinary $y$ satisfy the physical exit's
residue condition. All backwards intermediate states are integral:
the full terminal residue implies every intermediate ternary guard
as in [OP-B1](../operator/TERNARY_BARRIER.md). They are positive
since their real form is $(y-A'_i)/C_i$ with
$A'_i=\frac12\sum_{h\le i:\,O}C_{h-1}\ll k(3/2)^k=o(X)$.
They are strictly below $X$ at every nonempty prefix because
$C_i\ge1+\xi$ and $y\le(1+\xi/2)X$. Thus each resulting pair
is a genuine ordinary first-exit path, with positive integer
source and exact retention. Distinct triples of clock, word and
terminal have distinct sources, by the uniqueness of a first exit
and the deterministic forward parity word.

At each such $k$ their total mass is consequently at least
$cX^{-1}\sum_w C_k^2 3^{-j}\gg X^{-1}$, the sum over the
retained words. Summing all these disjoint clocks gives
$\gg_\eta(\log X)/X$. This argument identifies the unavoidable
short-clock leakage even if every ordinary component eventually
cycles. It requires no assertion about a heavy gate actually
existing for unbounded cutoffs.
