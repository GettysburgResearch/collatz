# Randomized finite controllers have exponentially small chances of tracking the native optimum

Let the positive iid geometric gaps have mean $1<b\le a_*$, parameter $\theta=1/b$, gap probabilities $p_e=\theta(1-\theta)^{e-1}$, entropy $H=H(b)$, and put $t=-\log(1-\theta)$ and $r=p_5$. Write $\mu_b$ for the distribution of the original ternary source, and $C_n(x)$ for its unrestricted minimum total cost through $n$ unit-legal inverse gaps. With probability one the same source defeats **all** fixed-size randomized controllers, even if one chooses the controller and its initial hidden state separately for each supplied source and horizon.

A controller reads the current $W$-trit row and has at most $M$ internal states. A time-homogeneous probability kernel selects a legal label from the row and hidden state. After the actual transition the updated hidden state may also use the new row and the executed label. Conditional kernels use fresh randomness. A fixed shared seed that selects one such controller initially is also covered by convexity. Additional persistent state, an externally supplied clock, and an oracle that changes the kernel during the path are separate resource models. All statements below apply also to smaller numbers of states or trits by padding.

For fixed $W\ge2$ and $M\ge1$, there are constants $c,d>0$ for which, for $\mu_b$-almost every $x$, eventually for every $n$,
$$
  \sup_\pi \Pr_\pi\{T_n(\pi,x)\le C_n(x)+dn\}\le e^{-cn}.       \tag{1}
$$
In particular conditional mean regret is linear, uniformly over those controllers, because every executed path costs at least $C_n(x)$. The critical source $\mu_{a_*}$ has full Shannon dimension. The result transfers to $X^{H/\log3+o(1)}$ odd positive roots in each sufficiently large octave, simultaneously at all sufficiently large depths through $\log_3 X-O(1)$, with the low-cost witness specified below.

## The hidden-state waiting bound

Use the native $W$-word $B_5$ from `UNIVERSAL_WINDOW_REGRET.md`. Its first gap is five, the others are at most four, and it starts at row $-1\bmod3^W$. The packet $P=1^M B_5$ has length $M+W$. Along any compatible native path all of its first $M+1$ decision rows are the same row $-1$. This follows either by the fixed inverse point at gap one or by the source formula for the remaining prefix ending with the complete $B_5$. The first $M$ successor rows are also $-1$, so the hidden transition conditional on executing a one in this part is identical at each step.

Write $A_{ij}$ for the probability of executing one and updating from $i$ to $j$, with both current and following row $-1$, and $v_i$ for the probability of selecting five there. Thus $A$ is nonnegative substochastic and $0\le v\le {\bf1}-A{\bf1}$. For any starting distribution $\lambda$ of total mass at most one let $p=\lambda A^M v$. For every $0\le j\le M$, all coordinates of $\lambda A^j$ lie in $[0,1]$, so
$$
 p=(\lambda A^j)(A^{M-j}v)\le \sum_i(A^{M-j}v)_i.
$$
Sum these inequalities. Since $\sum_{k=0}^M A^k v\le {\bf1}-A^{M+1}{\bf1}\le{\bf1}$, it follows that $(M+1)p\le M$. This is uniform for arbitrary transition probabilities. For a fixed legal word at a fixed root, every displacement through other symbols is substochastic. Conditioning at each of $K$ disjoint complete occurrences of $P$ bounds the probability of that exact word by $(M/(M+1))^K$. This argument retains the same controller only within the tested path and places no cardinality restriction on the set of controllers.

The same bound applies to a time-homogeneous controller with quantum memory of dimension $M$, classical observed rows and output gaps, and no persistent ancillary memory beyond this dimension. On identical current and successor rows let $T$ be the completely positive trace-nonincreasing update for gap one. Let $E$ be the positive effect for selecting gap five, so $E\le I-T^*(I)$. Before conditioning on the label the trace of the one-symbol update is its selection probability, including when its postprocessing reads the next row. For any initial density $\rho$, each $T^j\rho$ is positive with trace at most one, thus $T^j\rho\le I$. For any $u\ge0$,
$$
 (u+1)\operatorname{tr}[\rho(T^*)^uE]
 \le \sum_{j=0}^u \operatorname{tr}[(T^*)^{u-j}E]
 \le \operatorname{tr} I=M .
$$
The first inequality splits the update after $j$ labels and uses positivity; the second telescopes using the exit-effect bound. Taking $u=M$ yields the same native packet estimate. All later arguments use only this probability bound, so (1) and (3) include these controllers. The analogous repeated-output test is studied as the *one-tick sequence* in finite-state clock theory; our bound $M/(u+1)$ suffices without an optimality claim. [Weilenmann, Budroni and Navascués, Sections IV.A and VI.A](https://doi.org/10.1103/PRXQuantum.5.020351).

## A common upper envelope of success probabilities

Partition the first $n$ letters into $m=\lfloor n/(M+W)\rfloor$ aligned packets. Let $K(w)$ be their number of matches with $P$, and put $z=M/(M+1)$, $\tau=m\theta^M r^W/(M+1)$. Under the iid geometric law $K$ is binomial and
$$
  \mathbb E z^K=(1-p_P/(M+1))^m\le e^{-\tau}.
$$
For words of total at most $bn+\tau/(4t)$, each iid word probability is at least $\exp(-nH-\tau/4)$. Consequently
$$
 \sum_{w\,\mathrm{cheap}}z^{K(w)}\le \exp(nH-3\tau/4).            \tag{2}
$$
Such a word determines one original depth-$n$ residue $[w]$. For an actual root $x$, define
$$
 F_n(x)=\min\{1,\sum_{w\,\mathrm{cheap}}z^{K(w)}{\bf1}_{[w]}(x)\}.
$$
It bounds the conditional probability of an actual cheap word under *every* controller. Terminal legality can only remove terms. Also $0\le F_n\le1$ and the sum of $F_n$ over depth-$n$ residues is bounded by (2).

The finite-block Rényi bound in `UNIVERSAL_WINDOW_REGRET.md` gives, for every fixed $\epsilon>0$, some $q>1$ with $\sum_v\mu_b(v)^q\le C e^{-(q-1)(H-\epsilon)n}$. Indeed successive blocks of source trits, conditional on the prior trits, have laws that are mixtures of permutations of the iid suffix source law. Convexity gives submultiplicativity of those power sums, and Leen's Theorem C gives their finite-block entropy input. By Hölder and $F_n^{q/(q-1)}\le F_n$,
$$
 \int F_n\,d\mu_b\le C^{1/q}
 \exp\big[(q-1)(\epsilon n-3\tau/4)/q\big].
$$
At fixed $M,W$, $\lim\tau/n=\theta^Mr^W/((M+1)(M+W))>0$. Choose $\epsilon$ smaller than one fourth this limit. Markov's inequality and Borel–Cantelli give $F_n(x)\le e^{-cn}$ eventually, for some $c>0$. The sampled true path has $S_n=bn+o(n)$ and $C_n\le S_n$. Thus (1) follows with any $d$ strictly below $\lim\tau/(4tn)$, decreasing $c$ as needed. These statements hold on one common full-measure set for all fixed memory and width bounds.

## Growing both resources on the same ordinary roots

Suppose $1<b\le\log_2 3$, $W=W_n\ge2$, $M=M_n\ge1$ and for some fixed $\kappa>0$ eventually $\tau\ge n^{1/2+\kappa}$. For instance take $W_n\le\max(2,c_W\log n)$ and $M_n\le\max(1,c_M\log n)$ with $c_W|\log r|+c_M|\log\theta|<1/2$. There is $c_b>0$ such that for almost every $x$ eventually
$$
 \sup_\pi\Pr_\pi\{T_n(\pi,x)\le C_n(x)+\tau/(8t)\}
       \le \exp(-c_b\tau^2/n).                                   \tag{3}
$$
For any fixed small $u>0$, exponential moments of the centered geometric law and a union bound give
$\Pr(\max_{j\le n}|S_j-bj|>u\tau)\le 2n\exp(-c_{b,u}\tau^2/n)$.
Here $\tau\le n$ ensures a uniform choice of the moment parameter proportional to $u\tau/n$. On the complement the integer numerator $C(w)=\sum_{j=1}^n3^{j-1}2^{S_n-S_j}$ has size at most $n3^n e^{O_b(u\tau)}$. At fixed total and residue it belongs to one class modulo $3^n$ and determines the word. Each typical word has probability at most $\exp[-nH+tu\tau]$. Summing over $O_b(n)$ totals bounds the typical mass of every cell by $\exp[-nH+O_b(u\tau+\log n)]$. Multiply this by (2) and choose $u$ sufficiently small; the exceptional part contributes at most its total probability. Therefore $\int F_n\,d\mu_b\le\exp(-2c_b\tau^2/n)$ for large $n$. Markov and Borel–Cantelli bound $F_n$ as in (3). The actual iid path satisfies $S_n\le bn+O_b(\sqrt{n\log n})$ eventually, which is at most $bn+\tau/(8t)$ eventually.

Both (1) and (3) have the stated integer realizations. Restrict the full-measure set of sampled paths to a positive-mass subset with a common onset, retaining also the uniform $S_j\le bj+O_b(\sqrt{j\log j})$ at all later dates. The Rényi estimate gives at least $\exp(nH-o(n))$ prefixes of $n+1$ source trits for this set. Each of those classes has a positive odd representative in every octave $[X,2X)$ with $2\cdot3^{n+1}\le X$. All the upper witness costs for $j\le n$ remain valid at this representative because the chosen labels and terminal trit agree. Each $F_j$ depends only on the first $j$ trits, so the conditional-probability lower-cost exclusions persist even if the controller has access to $W_j$ trits at every later departure, beyond the last trit fixed on the representative. The terminal cost upper bound confines the count to at most $\exp(nH+o(n))$ cells by composition counting when $n$ is the largest allowed value. The octave conclusions concern finite prefixes on supplied actual roots. The typical source probability is $\mu_b$, which is singular relative to ternary Haar at the critical point.

The stationary inverse optimum $L$ and the universal behavioral lower bound here have different quantifiers. The latter applies even if one redesigns a finite-state randomized transducer for each individual supplied source and depth; almost every source separately experiences the stated exponentially small success probability. [Leen, *Tilted 3-adic Syracuse laws*, Theorem C](https://doi.org/10.5281/zenodo.23268832) · [Tao, Lemma 6.2](https://arxiv.org/abs/1909.03562).
