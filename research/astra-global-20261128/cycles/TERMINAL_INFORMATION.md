# Ordinary endpoint information at critical time and the escape-density coefficient

Let $U_X$ be uniform on $1,\ldots,\lfloor X\rfloor$, $L=\log X$, $a=\log(4/3)/2$, $\mu=1/a$, and $b=\log3/2$. For a deterministic native shortcut date $t$ set $Y=T^t U_X$, write $P_{X,t}$ for its ordinary endpoint law and
\[
           I_{X,t}=-\log P_{X,t}(Y).
\]
This is the log reciprocal mass of the *actual* equal-date ordinary fibre of the sampled source. Let $d_E$ be the total natural density of the escaping components, and $d_P=1-d_E$ the bounded-component density, under the source-qualified component law below.

At the critical clocks $t=\mu L+u\sqrt L+o(\sqrt L)$ for fixed real $u$,
\[
         I_{X,t}/\sqrt L\ \Longrightarrow                   (b\sqrt\mu\,G-au)_+,\qquad G\sim N(0,1).             \tag{1}
\]
In particular $H(Y)/\sqrt L$ tends to the expectation of this positive part. The clipped Gaussian law quantifies the size of the true endpoint fibre even on a path whose later component is unknown.

At every supercritical clock $g=t-\mu L\gg\sqrt L$ in the sense $g/\sqrt L\to+\infty$, the two endpoint regimes split in probability:
\[
     I_{X,t}/(\tfrac12\log L)-\mathbf1_{\{Y\text{ nonperiodic}\}}
               \ \longrightarrow 0 \quad\text{in probability}.          \tag{2}
\]
The nonperiodic flag has limiting mass $d_E$. For the **Shannon entropy** one has the sharper numerical coefficient whenever $g/\sqrt{L\log L}\to+\infty$, with no upper bound on $t$,
\[
              \boxed{\displaystyle
                 \frac{H(T^t U_X)}{\tfrac12\log\log X}\longrightarrow d_E.}       \tag{3}
\]
Under the separate positive predecessor-density input, any actual escaping integer produces a positive-density escaping component. Thus for example $H(T^{\lceil(\log X)^2\rceil}U_X)=o(\log\log X)$ is equivalent to absence of escaping integer orbits, allowing arbitrary finite cycles. Equation (3) supplies the genuine global coefficient. It does not provide an independent reason for $d_E$ to vanish.

The source inputs are [PR 215, stopped full native endpoint and grade, equation (1)](https://github.com/GettysburgResearch/collatz/blob/7902faf17d50851b46cdcd420ae479d19f0c845c/research/astra-nine-hour-20261128/escape/phase2/NATIVE_BINOMIAL_TRANSFER.md) and [PR 213, all-clock nonperiodic atom upper and total-variation law on periodic sites, equations (1)–(3)](https://github.com/GettysburgResearch/collatz/blob/87be3aa8837ecc64e83075d7571c6ab9e1646c2b/research/astra-global-rigidity-20261128/mass/NATIVE_ENDPOINT_ATOMS.md). The first uses signed exact native endpoint/clock transport. The periodic part of the second uses the fixed-basin density and finite-coverage statements it identifies. PR 213 also already detects escape with a normalized $q$-collision sum for $q>1$, bounding a specified escaping ray's terminal support on a clock band of width $O(\sqrt L)$. Here the complete source's Shannon entropy includes small atoms and requires an integrated tail estimate.

## Information in a stopped fresh-size mixture

In the stopped input the fair size walk is $L_j=L-aj+b(2B_j-j)$ with iid fair odd indicators and their count $B_j$. Put $\tau=\inf\{j:L_j\le H\}$, $J=\min(t-d,\tau)$. For $L>H\ge2$ and $t\ge d\ge2$, the actual endpoint law is within
\[
                      C_A(H^{-A}+d^{-A})                                \tag{4}
\]
in total variation of $Y'=T^{t-J}m$, conditional on the fair path choosing a fresh uniform integer $1\le m\le e^{L_J}$. All terminal points of this approximating law are also genuine positive-integer states. If $J=\tau$, its input has at most $e^H$ possibilities. If $J=t-d<\tau$, it has the same law as $T^d m$ given the grade $B_{t-d}$ and survival of the size walk.

For a finite latent label $Q$ and any discrete variable $V$, writing $i=-\log\Pr(V)$ and $i_Q=-\log\Pr(V\mid Q)$ at a sample, one has $i-i_Q\le-\log\Pr(Q)$ and
$\Pr(i_Q-i>z)\le e^{-z}$. The latter follows by conditioning on $Q$ and summing the unconditioned atom probabilities over that conditional support. Thus a latent variable with at most $M$ possibilities changes sampled information by $O_{\Pr}(\log(2M))$, since $\Pr(-\log\Pr(Q)>\log M+z)\le e^{-z}$. Likewise two laws tending together in total variation admit a coupling with the same sample off $o(1)$, on which their self-information difference is tight. For instance the mass under either law of atoms where the other is smaller by a factor below $e^{-z}$ is at most $\mathrm{TV}/(1-e^{-z})$ measured in the larger law; use this twice for each fixed $z>0$. No entropy continuity with growing support is assumed.

For (1) take $H=d=\lfloor L^{1/8}\rfloor$. Use the label $Q=(J,B_J,\mathbf1_{J=\tau})$ with $O((1+t)^2)$ values. On the crossing branch $i_Q=O_{\Pr}(H+1)$ by the support bound. On the other branch put $M=\lfloor e^{L_J}\rfloor$. Every point has at most $2^d$ length-$d$ predecessors (each shortcut state has at most two positive-integer parents), and the output range of $T^d[1,M]$ has at most $2^d(M+1)$ points, since $Tz\le2z$ for positive $z$. Hence $i_Q=L_J+O_{\Pr}(d+1)$ by maximum conditional atom mass and support. Consequently the sampled information, divided by $\sqrt L$, is within $o_{\Pr}(1)$ of $L_{t-d}\mathbf1_{\tau>t-d}/\sqrt L$. On the event of a crossing before $t-d$ the future increments have negative drift. The probability that the size walk returns upward by at least $v$ after its first crossing is $O(e^{-c v})$ uniformly by its positive exponential supermartingale at a small parameter. Thus the latter variable is within $o_{\Pr}(1)$ of $(L_{t-d})_+/\sqrt L$. The ordinary binomial CLT at $t-d$ and (4) prove (1).

For its expectation one may use the concentration estimate below, including the missing-crossing term when $g=O(\sqrt L)$. It gives uniform integrability at scale $\sqrt L$.

## Small sets of genuine endpoints, uniformly in a late clock

Here is a tail bound that can be integrated even far beyond any deterministic function of $X$. There are absolute positive $c,C$ such that for $u_0\le u\le L+1$, $t\ge\mu L-C_0\sqrt L$ (with constants allowed to depend on fixed $C_0$), the genuine mass satisfies
\[
 \Pr\{I_{X,t}>\tfrac12\log L+u\}
  \le C_Au^{-A}+Ce^{-cu}
        + C\exp[-c\min(((g+c_1u)_+)^2/L,(g+c_1u)_+)].                 \tag{5}
\]
Here $u_0$ is a sufficiently large absolute constant and $c_1>0$. If the positive part in the last term vanishes its contribution is a constant, as required. To prove the bound put $H=d=\lfloor u/C_1\rfloor$ with $C_1$ a fixed sufficiently large constant, using (4) with any desired power. Then $H<L/2$ and $d<t$. The central crossing time is $t_*=(L-H)/a$. Except for probability $Ce^{-cu}$, $\tau$ lies in an integer band of length $O(\sqrt{L u}+u+1)$ around $t_*$. For an early crossing use the exponential maximal Hoeffding bound for the centred bounded-increment size walk to time $t_*-K(\sqrt{L u}+u)$, which is empty if negative. For a late crossing, no crossing by $t_*+K(\sqrt{Lu}+u)$ forces the size walk still above $H$ there, bounded by fixed-time Hoeffding. The bound is uniform for the indicated $u$, since $t_*=O(L)$ and the tested upper time is $O(L+u)$. If $\tau>t-d$, fixed-time Hoeffding similarly gives the last term in (5): the distance of $t-d$ above $t_*$ equals $g+(1/a-1)H$, and $(g+cH)^2/(t-d)$ bounds a fixed constant times $\min((g+c'H)^2/L,\,g+c'H)$ when the latter argument is positive, after absorbing integer roundings. This works even when $t\gg L$.

On all remaining fair paths the source integer $m$ is at most $e^H$ and the residual date $t-\tau$ ranges over only that same band. All these true terminal labels therefore belong to a set of at most $Ce^H(\sqrt{Lu}+u+1)$ ordinary integers. Its log cardinality is at most $\tfrac12\log L+u/2$ for large $u_0$ by the choice of $C_1$ and $u\le L+1$. Transfer the retained mass to the actual endpoint by (4). Inside this set the mass of atoms having information above $\frac12\log L+u$ is at most its cardinality times $L^{-1/2}e^{-u}\le e^{-u/2}$. This proves (5).

The actual endpoint law has $0\le I_{X,t}\le\log\lfloor X\rfloor\le L$ pointwise, for all $t$. When $g=O(\sqrt L)$, substituting $u=v\sqrt L$ in (5) bounds the tail for large $v$ by $O_A((v\sqrt L)^{-A})+O(e^{-cv\sqrt L})+O(e^{-c'v^2})$ throughout its nonempty support, with constants for the fixed scaled clock interval. This proves the claimed uniform integrability in (1). When $g\gg\sqrt L$, (5) at large fixed $u$, followed by $u\to\infty$, gives $I_{X,t}\le\frac12\log L+O_{\Pr}(1)$. For $g\gg\sqrt{L\log L}$ its last term additionally has integral $o(1)$ in $u\in[u_0,L+1]$: one may use $L\exp[-c\min(g^2/L,g)]\to0$. Integrating (5) proves
\[
                 \mathbb E(I_{X,t}-\tfrac12\log L)_+=O(1)                \tag{6}
\]
at these delayed clocks. It also proves uniform integrability of $I_{X,t}/(\tfrac12\log L)$ there, since that normalized excess has expectation vanishing.

By the cited PR 213 union law, on periodic endpoints the samples converge in total variation as subprobabilities to the fixed discrete cycle-phase distribution of mass $d_P$. Thus the information on the periodic event is tight in subprobability: truncate to finitely many positive limiting atoms, whose own masses stay positive. On nonperiodic endpoints the all-time row bound gives $I_{X,t}\ge\frac12\log L-O(1)$ deterministically. Combining this with (5) proves (2). Together with (6) and the limiting nonperiodic mass $d_E$ it gives (3). The stronger timing assumption in (3) disposes of tiny surviving, not-yet-descended sources in the Shannon integral. Those sources can have much larger information than the typical postcritical value.

[The exact finite control](check_native_fibres.py) also checks the latent-label information inequalities on a mixture of genuine shortcut endpoint laws with three different source sizes and physical dates. [Recorded output](../../../reports/astra-global-20261128/cycles/NATIVE_FIBRES.json)
