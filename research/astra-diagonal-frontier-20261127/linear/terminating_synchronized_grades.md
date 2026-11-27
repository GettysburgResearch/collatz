# The synchronized classes of sources reaching one

Let $C$ be the shortcut map, $J_t(x)$ its number of odd departures in $t$ steps, and $N(x)$ the first time it reaches $1$, including $N(1)=0$. For positive integers actually reaching $1$ set
\[
                  D(x)=N(x)-2J_{N(x)}(x).
\]

**Exact classification.** Two such inputs acquire the same ordinary state and the same accumulated odd count at one common shortcut clock if and only if their $D$ values agree. Indeed
\[
       D(x)=t-2J_t(x)+D(C^t x)
\]
also holds after the first arrival, since the positive cycle through $1$ has clocks $(2,1)$. Conversely, equality of defects makes the two first-arrival clock pairs differ by an integer multiple of $(2,1)$. Append the needed full laps to the earlier arrival. A positive input meeting one of these sources necessarily reaches $1$.

For $d\ge0$ the least source in defect class $d$ is exactly $2^d$. The exact product to the first hit gives
\[
 x=2^{D(x)}(4/3)^{J_{N(x)}(x)}
        \prod_{\substack{i<N(x)\\ C^i(x)\ {\rm odd}}}
                    \frac{3C^i(x)}{3C^i(x)+1}\ \ge 2^{D(x)},
\]
and $D(2^d)=d$. For negative $d$ the quantitative result below establishes nonempty classes. In particular $D$ on genuine terminating inputs is unbounded below. Its strict record lows, as these positive integers are taken in increasing order, occur at unbounded odd sources. An even $2u$ cannot set a record since $D(2u)=D(u)+1$. An odd $x>1$ with $x\equiv1\bmod4$ has $C^2x=(3x+1)/4<x$ with the same defect. Every such strict record $x>1$ is therefore $3\bmod4$ and has **no smaller positive synchronized partner at any clock**.

More generally, at any common state reached from such a record $x$ and a smaller $z$ using respective clocks $(t_x,j_x),(t_z,j_z)$, one has $(t_z-t_x)-2(j_z-j_x)=D(z)-D(x)>0$. For a finite example, the first arrival from 27 has $(70,41)$ and defect $-12$. Direct shortcut iteration on the integers $1$ through $26$ gives counts $1,4,9,7,5$ at defects $0,1,2,3,4$ respectively. Every merger with a smaller source in this example requires the displayed difference to be at least $12$. This concerns the labelled merger criterion even on an orbit that certainly descends.

## Class population on an actual octave

**Source-qualified corollary.** For all sufficiently large $X$, every integer $d$ with $|d|\le c\sqrt{\log X}$ occurs on at least $c'X/\sqrt{\log X}$ genuine sources in $[X,2X)$. Uniformly over all integers $d$, the number there is at most $C X/\sqrt{\log X}$. The lower estimate can also keep a single prescribed original CRT class. If $k+m\le\kappa\log_2X$, prescribe $x=r\bmod2^k$ and $x=v\bmod3^m$. Let $q$ be the number of odd departures determined by that binary prefix. For every integer
\[
                 |d-(k-2q)|\le c\sqrt{\log X}
\]
the lower count within this individual CRT class is $c'X/(2^k3^m\sqrt{\log X})$. All counted inputs make their first actual visit to $1$ in $O(\log X)$ steps. In the construction for the supplied class and defect, the two first-arrival clocks are themselves common. The constants are absolute on the pinned inputs and $\log$ without a base is natural.

For the upper, on a first-arrival row at odd grade $j$ write $p=2^d(4/3)^j$. The simple-path correction bound gives $c_*p\le x\le p$. At fixed $d$ an octave permits only $O(1)$ integer $j$, including initial even halvings in the native clock. Each such row has at most $C p/\sqrt{1+\log p}$ sources by the [sharp target-uniform first-arrival bound](../mass/SHARP_UNIFORM_FIRST_ARRIVAL_ROWS.md).

For the lower we use the existing [individual mixed-CRT first-landing construction](suffix_horizon.md) and fix its total at the prescribed defect before choosing its length. Take its favorable odd unit $w=(2^e-1)/3$ with $U(w)=1$, for one fixed $e$ large enough that $w>100(F+1)$, where $F$ is the selected real-offset cap. It may be chosen in the favorable fixed cylinder by the unit order of 2. Write $\zeta=2^k/3^q$ and $\Delta=d-(k-2q)-(e-2)$. Choose an integer $b$ with
\[
             1.2 X\le W:=\zeta w2^\Delta(4/3)^b\le1.8X,
             \qquad s=2b+\Delta .
\]
Such $b$ exists because one increment multiplies $W$ by $4/3$. Uniformly for small fixed $\kappa,c$, $b\asymp\log X$, $q+m\le\delta b$ and $|s-2b|\le2\sqrt b$. Here $\delta$ is the extra-depth constant in the [selected exact-total floor, equation (2)](local_first_landing.md).

Apply that floor at the same full residue as in the mixed-CRT construction. Each selected word has exact total $s$, offset $B_b\le F$, weight $2^{-s}$ and gives one positive original source
\[
             x=W(1-B_b/w)-d_0,\qquad 0\le d_0<2^k .
\]
The bounds on $w,W,2^k$ place every such $x$ in $[X,2X)$. The full congruence enforces both original residues. All odd intermediate inverse sites after $w$ exceed 1 by the selected real cap, and the initial native prefix stays above $X/2^k>1$. The first visit to 1 has clocks $(k+s+e,\ q+b+1)$ in native, odd order, giving the prescribed $D(x)=d$. At fixed $b,s$ distinct words give distinct sources. Their number is at least
\[
 \frac{c_0\,2^s}{3^{b+q+m}\sqrt b}
        \asymp\frac{X}{2^k3^m\sqrt{\log X}}.
\]
Taking $k=m=0$ gives the unmarked lower estimate. In particular every fixed integer defect is realized when $X$ is sufficiently large. The existing mixed-CRT theorem already summed over clocks to give its full first-landing floor. The choice of $s-2b$ here isolates a single all-time synchronized class.

The analytic inputs are Weaver–Wren, Paper 48 v2, Lemma 7 and (76), (79), for the lower, and the written target-uniform sharp row law for the upper. The classification and the example 27 are elementary. The existence of unbounded terminating odd records above uses the stated physical lower. It does not imply that a record for a different component converges. [Paper 48 v2](https://rstation.ai/problems/collatz/papers/48/v2)


The exact two directions above are connected to the actual native map in [TerminatingGrades.lean](TerminatingGrades.lean). Its hypotheses furnish finite visits to 1; the formal statement does not assert visits for any additional input.
