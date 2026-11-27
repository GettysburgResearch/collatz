# Signed word offsets and the odd-step cost of a postpeak merger

Let $T(2x)=x$ and $T(2x+1)=3x+2$. Count each departure from an odd input. Take a positive cofactor $v$, a ramp length $H$, the original source $n=2^Hv-1$, and its peak $P=3^Hv-1$. Reading a native upper word $w$ from $P$ produces $Y=T^tP$. Write $t=|w|$, $f=Q(w)$, and $q=t-f$. The cofactor may be even if the stated ramp is shorter than the maximal one.

For each binary word, define its unsigned intercept $A_w$ by $2^tT_w(x)=3^f x+A_w$, where $T_w$ denotes the composition of its indicated branch formulas. Its signed offset $C_w=A_w-3^f$ satisfies

\[
                    2^tY=3^{H+f}v+C_w .
\]

The finite criterion below optimizes over every smaller positive source and every lower native clock. Both bounds concern a finite prefix of the upper orbit.

## Exact discounted grades

Suppose $21q+3\le H$, and prescribe a nonnegative saving $d$ with $k+d=H+f$. There is a smaller positive $m<n$ with $T^e m=Y$ and $Q_e(m)=k$ for some $e$ if and only if a word $β$ of length $t$, weight $u$, satisfies both

\[
          C_β=C_w,\qquad 3^d2^f<2^{u+d}.
\]

The strict inequality forces $u>f$. If $M$ is the largest weight in the same-offset fibre and $M>f$, the least lower grade over all starts and clocks is therefore $H+f-\lfloor(M-f)\log_{3/2}2\rfloor$. If $M=f$, every lower grade exceeds $H+f$.

For sufficiency take $p=H+f-u-d$ and $m=2^p3^dv-1$. The price makes this positive source smaller. Its first $p$ odd departures reach $3^{p+d}v-1$. The affine identity for $β$ gives integral endpoint $Y$, which forces every intervening branch to be physical.

For necessity let $\ell=e-k$ be the total lower even count. A positive even departure decreases shifted height by a factor at most $2/3$. An odd departure multiplies it by exactly $3/2$. The two endpoint equations imply $(3/2)^{\ell+d}<2^q$, so $\ell+d<2q$. The lower clock is long enough to split off a final $t$-word $β$. Its preceding prefix has clock $h=e-t$, weight $p=k-u$, and endpoint $z$. Translate this prefix by the integral amount $3^dv$. The new initial point $x_0=m-2^h3^dv$ and endpoint $z_0=z-3^p3^dv$ follow a genuine signed native walk. Only the final $β$ is used affinely. It gives $3^uz_0+A_β=C_w$, so $|z_0|\le2\cdot3^{t-u}$ and $t-u\le\ell$.

Every signed native odd step away from the fixed point $-1$ increases absolute magnitude by at least $4/3$. Even steps halve it. A nonzero prefix with at least $9s+3$ odds, at most $2s$ evens and terminal magnitude at most $2\cdot3^s$ must therefore end at $-1$. Take $s=2q$. Zero cannot make a positive odd count. This gives $z_0=-1$ and $C_β=C_w$. Moreover $|x_0|\le2^{h-p}$, because every signed odd step weakly increases magnitude. Therefore $m\ge2^{h-p}(2^p3^dv-1)$, so $2^p3^d<2^H$. Multiplication by $2^{u+d}$ gives the stated price.

## Protection after a peak

Let $s\in\{0,1\}$, and assume $3^K\mid n-s$. First, for **any integer scale** $c\ge1$, a target with $2^j(Y+1)=3^jc(n+1)$ costs every positive smaller visitor more than $K+j$ odd departures. Indeed its virtual all-odd source $N=c(n+1)-1\ge n$ forces lower clock $e\ge j$. Under the opposite cost assumption take the integral $a=3^{j-k}c(n-s)$. Translating the first $e-j$ lower steps gives $m_0=m-2^{e-j}a$, with translated endpoint $z_0$ satisfying $3^uz_0+A=3^jc(s+1)-2^j$. The upper bound $A\le3^j-2^j$ gives $z_0\ge s$, and the signed prefix gives $m_0\ge s$. A second elementary bound $A_{\rm full}+2^e\ge3^k$ holds for every word. It yields $3^k(m_0+1)\le2^{e-j}3^jc(s+1)$, so $2^{e-j}3^jc\ge3^k$, hence $m\ge n$.

Call $w$ maximal if no word of the same length and offset has more odds. Under $H\ge21q+9K+3$, every smaller visitor to $Y$ then spends **more than $H+f+K$ odds**. Discounted grades are already excluded. For a proposed overspend $0\le b\le K$, the shifted-height bound implies $\ell\le2q+b$. Strip off the first $b$ lower odd departures. Of the remaining $H+f$, the last $t$-word uses $u$, and the signed prefix has at least $H-q$ odds. The same trap with $s=2q+b$ forces an actual pre-tail visit to $3^{H+f-u}v-1$ with matching offset. Maximality gives $δ=f-u\ge0$. This is the scaled-ramp target for $j=H+δ$, $c=2^δ$. Its preceding cost $H+δ+b$ violates the scaled barrier.

## Arbitrarily long residual odd phases

Let the upper word begin with an even departure and then $r\ge1$ consecutive odd departures. The word $EO^rE^s$ has offset $3^r-2^{r+1}$, regardless of $s$. A word matching this odd offset must also start even, since the unsigned intercept is odd exactly when the first letter is odd. Every word of weight $u$ has $A\ge3^u-2^u$. Removing the leading even forces $C\ge3^u-2^{u+1}$, which increases strictly from $u=1$ onwards. Therefore $u\le r$ and the word is maximal. Taking $r$ arbitrarily large leaves the upper even count $s+1$ fixed.

For arbitrary subsequent letters, write $B=C+2^t$. If $r_i$ counts odds before upper even $i$, indexed from zero, repeated native updates give $B/3^f=\sum_{i<q}2^i(2/3)^{r_i}$. This is the translated carry from PR201. Equal-length equal-offset words share $B$. For an alternative gain Δ, its first even contributes one, so $B/3^f\ge3^Δ\ge3$. Since $r_i\ge r$ for every $i\ge1$, any gain requires $(3/2)^r\le2^{q-1}-1$. With precisely two upper evens, an $EO$ start remains maximal through arbitrarily many further odds.

## Exact residual even threshold

With the first two upper letters $EO$, no same-clock equal-offset word may gain an odd departure through five upper evens, even if the total clock is unbounded. Six upper evens suffice. At clock eight use $EOEEEEEO$ against $EOEOOOEE$, whose weights are 2 and 4.

For fixed upper even count $q$ and proposed grade gain Δ, the lower must have $q' = q-Δ$ evens. At synchronized clock $j$ let $A,B$ be consumed even counts and $D$ the past upper-minus-$3^Δ$-times-lower normalized carry divided by $(2/3)^j$. One step with respective even indicators $i,h\in\{0,1\}$ gives

\[
 A'=A+i,\quad B'=B+h,\quad D'=\tfrac32(D+i3^A-h3^{Δ+B}).
\]

At a successful completion $D_j$ is an integer: its past expression has dyadic denominator; its future expression, from the equal total carries, has ternary denominator. More explicitly, if $w',b'$ are the remaining equal-length words of length $l$, then $3^lD=3^q(B_{b'}-B_{w'})$. The elementary bounds $0\le2B_{w'}\le3^l-3^{Q(w')}$ imply

\[
      -(3^q-3^A)\le2D\le3^Δ(3^{q'}-3^B).
\]

There are finitely many integer states even though arbitrarily many consecutive odd steps are allowed. Both words start even, and the second upper letter is odd. The reproduction script explores every terminally feasible state reachable under these two constraints. For $q\le5$, none of the terminal states $(q,q',0)$ is reachable. At most thirteen states survive at any such $(q,Δ)$ after the mandatory first two upper letters. The independent odd-coordinate implementation agrees on the six-even threshold.

## Source comparison and scope

PR201 at `d21bac748e705a64b6b57a7996a8ad6282f0bcbf`, `research/six-hour-20261127/coupling/PEAK_RIGIDITY.md`, gives the $v=1$ compensated earlier-peak classification under a restriction on lower postpeak clocks. Its translated-carry sum and its paper argument that compensated Mersenne classes are finite are prior work. The new odd-grade formulation allows every lower clock, every positive cofactor, and a condition depending only on the upper even count. Its application to class-minimal Mersennes supplies no prescribed ternary precision. The same PR's `NATIVE_EIGHT.md` classifies all clocks for a different specific source progression near $2^H=590$ ternarily. Its `POST_VALUATION_WINDOW.md` gives a typical delay for its special cofactor-one native branch.

PR192 at `ae48a04cca29abe5fc8273bcda45e7eee0874896`, `research/astra-minimum-source-20261124/renewal/README.md`, already supplies the positive eight-clock example. The threshold here excludes every finite clock with fewer residual evens. The exact price also distinguishes the best smaller source from the original neighbour. Earlier PR192 and PR197 signed-offset barriers are reviewed in the parent packet.

These results decide the near-optimal pair question in a nonuniform region and exhibit both positive and protected ordinary families. They leave unrestricted higher-grade mergers and universal Collatz convergence open.
