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

## Evidence and predecessors

The four principal statements are `RampShadow.Postpeak.cone_iff`, `RampShadow.Postpeak.scaled_ramp`, `RampShadow.Postpeak.paid_peak`, and `RampShadow.Postpeak.protected_barrier`. They were checked on Lean 4.34.1. Each reports exactly `propext`, `Classical.choice`, and `Quot.sound`. The positive witness in the discounted criterion is constructive. Collatz convergence and unrestricted high-cost merging remain open.

PR146 at `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/THREE_RAY_SMALLER.md` and `ADJACENT_DESCENT.md`, already proves the unscaled all-clock barriers at seeds zero and one. Its `NEGATIVE_FIVE_CHECKPOINT.md` and `EXCESS_DENSITY.md` give prior signed-shift, small-seed and converse constructions on another ray. The parent packet formalizes the unscaled cases. The present scaled theorem allows any positive integral multiplier of the source's shifted height.

PR201 at `d21bac748e705a64b6b57a7996a8ad6282f0bcbf`, `research/six-hour-20261127/coupling/PEAK_RIGIDITY.md`, gives a compensated-earlier-peak classification for unit cofactor under a bound on lower postpeak clocks, a translated-carry identity, and a written proof that the corresponding Mersenne classes are finite. Its `NATIVE_EIGHT.md` classifies unrestricted lower clocks on its specific near-590 progressions at one checkpoint. The present price uses all positive cofactors and lower clocks and bounds only the number of even steps on the supplied upper arm. For every sufficiently tall Mersenne peak at the minimum of its prior compensated class, its no-cheaper alternative holds throughout this upper-even-count cone. No prescribed ternary precision for those minima follows from that statement.
