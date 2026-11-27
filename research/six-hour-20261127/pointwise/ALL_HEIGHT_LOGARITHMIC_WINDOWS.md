# Sharp all-height statistics on ordinary logarithmic source windows

Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odd integers, with $Q$ and $g$ from the all-height census. Fix $0<\alpha<1/2$ and put
$$
 M_\alpha(n)=\max_{0\le j\le\alpha\log_2 n}
                    Q(U^j n)/g(U^j n),\qquad
                      \kappa=(\log2)^{-2}.
$$
Thus the upper test controls every positive rational height at each of the same actual dates. The lower test will use the single integer anchor $1$.

**Theorem B (written).** For a uniformly sampled odd integer $n\in[2^k,2^{k+1})$, $M_\alpha(n)\to\kappa$ in probability as $k\to\infty$. For any $c>0$ one also has the sharp reciprocal-sum threshold
$$
       \sum_{\substack{n>0\ {\rm odd}\\M_\alpha(n)>c}}\frac1n<\infty
                       \quad\Longleftrightarrow\quad c>2\kappa .       \tag{B1}
$$
The once-sampled ordinary source is followed through the entire tested window. A different random variable, such as a stationary ternary sample or the last suffix of a charged ray, is not being substituted into this assertion.

## Two elementary geometric-script bounds

Give each accelerated gap the probability $2^{-e}$ independently. A word of length $d$ determines one terminal residue modulo $3^d$ because the last $d$ maps remove all earlier input digits. Write $p_d(r)$ for the resulting probability of residue $r$, and $p_0=1$. For any fixed admissible terminal the first reversed gap must have one specified parity. The total geometric probability of that parity is at most $2/3$. Iterating the reversed residue recursion gives
$$
            p_d(r)\le(2/3)^d,\qquad
            p_d(-1)\ll(d+1)^2\,2^{-d}.                            \tag{B2}
$$
Every compatible word at target $-1$ has an ordinary negative inverse lift. Its positive magnitudes satisfy $u_{\rm prev}=(2^e u_{\rm next}+1)/3$, ending at $1$. They are positive odd integers and have exactly the requested forward gaps for the signed numerator $3u-1$. Before the first arrival at 1, all magnitudes are distinct and greater than 1 by physical determinism. Every remaining gap at 1 is one. If such a word starts in magnitude $u$ and has total exponent $E$, its product telescope gives
$$
           3^d2^{-E}=\frac1u
              \prod_{\rm departures}\Big(1-\frac1{3u_i}\Big)^{-1}
                \le\frac{d+1}{u}(3/2)^d .
$$
For $s$ distinct prearrival integers greater than one, the product is at most $\prod_{t=2}^{s+1}t/(t-1)=s+1$. With $E\le6d$ all starts satisfy $u\le2^E\le2^{6d}$ by the positive inverse recurrence. Each start has only one length-$d$ forward word, so their reciprocal sum is $O(d+1)$. For $E>6d$, omit the residue restriction. The contribution to $3^d p_d(-1)$ is bounded by $9^d(2/3)^{6d}$, using $\mathbb E(3/2)^e=3$. This proves (B2). The elementary argument uses only the reflected target $-1$. Weaver's original-law maximum-density exponent would give an alternative with a subexponential error for all residues. [Weaver, Paper 9/v2, maximum density](https://rstation.ai/problems/collatz/papers/9)

## An exact transfer from a finite ordinary octave

On the odd sources in the octave, the first $k$ native shortcut parity bits are uniform conditional on their first bit being one. This follows inductively from the affine formula: the two binary lifts of an initial word have opposite next parities. Write $j_*=\lfloor\alpha(k+1)\rfloor$, choose $2\alpha<\tau<1$, and let $E_j$ be the actual sum of the first $j$ full exponents. The probability that $E_{j_*}>\lfloor\tau k\rfloor$ is $O(e^{-c_\alpha k})$. The event uses only $\lfloor\tau k\rfloor+1$ parity bits and is exactly the geometric negative-binomial upper tail on these finite octaves for large $k$. For instance an exponential Markov bound works since the geometric mean is two. Denote its complement by $G_k$.

For $0\le j\le j_*$ and any residue $r\bmod3^d$,
$$
 \Pr(G_k,\ U^j n\equiv r\bmod3^d)
 \le
 \begin{cases}
     p_d(r), &d\le j,\\
     p_j(r\bmod3^j)\,3^{-(d-j)}+2^{1-(1-\tau)k}, &d>j .
 \end{cases}                                                       \tag{B3}
$$
To verify it one may enlarge $G_k$ to $E_j\le\lfloor\tau k\rfloor$. A word with total $E$ in this range has one odd source class modulo $2^{E+1}$ and probability $2^{-E}$ exactly. For $d\le j$ only its last $d$ letters determine the residue, so summing over the enlarged unrestricted geometric law proves the first line. For $d>j$, its $2^{k-E-1}$ equally likely positive sources form a progression. Their terminal values have step $2\cdot3^j$ by the affine identity $2^E y=3^j n+A$. After matching $r\bmod3^j$, at most the fraction $3^{-(d-j)}+2^{E+1-k}$ have the full residue. Averaging the error over words costs at most the additive error in (B3). For $j=0$ the same argument is the ordinary odd progression directly.

On $G_k$ every inspected $y=U^jn$ satisfies $2^{(1-\tau)k}\le y\le (n+1)(3/2)^j$, so $g(y)=\log k+O_\alpha(1)$ uniformly. As in Theorem A, an anchor violating $c\,g(y)$ has $h\le\exp(O_{\alpha,c}(k/\log k))$. Thus summing the additive error in (B3) over all possible anchors is exponentially small. A violation at exact height $h$ forces one residue modulo $3^{d_h}$ with $d_h=\lfloor c\log(2h)(\log k-C_\alpha)\rfloor+1$. For $h=1$ use the specialized bound in (B2) and, when $d_1>j$, $(j+1)^2 2^{-j}3^{-(d_1-j)}\le(d_1+1)^2 2^{-d_1}$. For $h\ge2$ use $(2/3)^j3^{-(d_h-j)}\le(2/3)^{d_h}$ when needed. The sum over heights is bounded by a constant times its first term because at most $2h$ pairs have each exact height. We obtain
$$
 \Pr(M_\alpha(n)>c)
 \ll_{\alpha,c}
 k^{1-c(\log2)^2}(1+\log k)^2+
 k^{1-c\log4\log(3/2)}+e^{-c' k}.                                  \tag{B4}
$$
The factor $k$ pays for all actual dates in the window, and the exceptional probability of $G_k^c$ has been included. Since $\log4\log(3/2)>(\log2)^2$, the probability tends to zero for $c>\kappa$. Its sum over octaves is finite for $c>2\kappa$, giving the upper part of (B1).

## The lower bound occurs on ordinary runs of ones

Take the first $\lfloor\alpha k\rfloor$ native clocks, omit the fixed first parity bit and split the other independent bits into disjoint blocks of $d+1$ bits, where $d=c\log2(\log k+C_\alpha')+O(1)$ is an integer strictly above the displayed threshold. For every state seen within these native clocks, $g(y)\le\log k+C_\alpha'$ by the deterministic growth bound. A block entirely of ones gives $d$ actual gap-one departures and an odd endpoint $y$ at an accelerated date $j\le\alpha\log_2 n$. The exact shifted identity gives $v_3(y+1)\ge d$, so $M_\alpha(n)>c$. Independence of the disjoint ordinary parity blocks yields
$$
  \Pr(M_\alpha(n)>c)\gg_{\alpha,c}
        \min\{1,\ k^{1-c(\log2)^2}/\log k\}.                         \tag{B5}
$$
When $c<\kappa$, the expected number of successful blocks tends to infinity and their exact no-success probability tends to zero, giving the lower half of convergence in probability. When $c\le2\kappa$, (B5) has divergent sum over $k$, including the endpoint $1/(k\log k)$. Weighting an octave by $1/n$ changes its uniform probability by at most absolute constant factors in its unnormalized harmonic mass. This finishes (B1).

## Original macroscopic first-exit law

Let $1\le x<X$ range over ordinary positive starting integers with weight $0\le F_X(x)\le1/x$ and total weight at least $\delta\log X$ along an unbounded sequence. Put $n=x/2^{v_2(x)}$ and normalize the weights to a probability. The conclusions
$$
 M_\alpha(n)\longrightarrow\kappa\quad\hbox{in probability},
 \qquad \Pr(M_\alpha(n)>c)=O_{\alpha,c,\delta}(1/\log X)
                   \quad(c>2\kappa)                                 \tag{B6}
$$
hold for this law. Indeed, on each odd core $n$ the sum of source upper weights over $x=2^t n$ is at most $2/n$. Octave exceptional probabilities tending to zero have cumulative harmonic weight $o(\log X)$ by Cesàro averaging, and the exceptional set in (B1) has finite harmonic weight. This uses the actual original gate weights when $F_X=w_z(x)/x$ through the same domination.

For that first-exit application the observations in (B6) can all be read before exit with failure probability $O_\delta(1/\log X)$ (the constant may also depend on $\alpha$). On an odd octave, apart from the exponentially small event $G_k^c$, the window ends by native time $k$ for large $k$. At each native time $s\le k$, write $T^s(n)=nL_s+A_s$, with $L_s=3^{o_s}/2^s$ and $0\le A_s\le(3/2)^k$, by summing the individual translates of $1/2$. After the fixed first parity, $L_s$ is a nonnegative martingale for the remaining independent parity bits with mean $3/2$. Its finite maximal bound gives $\Pr(\max_{s\le k}L_s>z)\le(3/2)/z$ for $z\ge1$. For the full octaves $2^{k+1}\le X$, the term $(3/2)^k$ is at most $X/2$, and $n\le2^{k+1}$. Hence the octave probability of reaching $X$ by those native times is $O(2^k/X+e^{-c_\alpha k})$. Smaller threshold values in the maximal inequality are covered by the trivial bound one. The sum of these octave probabilities is $O_\alpha(1)$, as is the whole last partial octave's harmonic mass. An initial even chain is decreasing, and the factor-two odd-core estimate applies. Dividing by the macroscopic total proves the claimed pre-exit probability. No distribution or time scale after coalescence into a distinguished tail is inferred.

All clocks and full valuations are physical in (B1)–(B6). The statements allow individual exceptional ordinary starts. The family following Theorem A has arbitrarily long all-height failures at a fixed anchor. In particular the resident distinct-orbit reciprocal estimate already makes the entire state set of any escaping ray reciprocal-summable. A reciprocal-summable exceptional set can therefore contain that ray. The sharp census and the macroscopic ensemble result do not supply a universal same-source clock, a smaller merger, or a contradiction on an escaping ray. [Fixed-source escape trace and reciprocal bound at PR 200](https://github.com/GettysburgResearch/collatz/blob/bf7d52e78631954a9fd35e4ce973acd27738fc80/research/unconventional-20261126/trace/ESCAPE_TRACE_PROFILE.md)
