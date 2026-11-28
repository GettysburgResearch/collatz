# Most odd steps cannot lie in runs comparable to the current bit length

**PROPOSED, written proof using Evertse's 1984 theorem on sums of $S$-integers.** Let $x_t$ be a positive, non-eventually-periodic shortcut orbit. For each maximal nonempty run of odd inputs, including a possible initial one, let $g$ be its length and $B=\log_2(x+1)$ at its first state. For fixed $\delta>0$, call an odd input *marked* if it lies in a run with $g\ge\delta B$. Let $M(t)$ and $U(t)$ count marked and unmarked odd inputs in the first $t$ steps. Set $\gamma=\log_2 3$ and $c=\log_2(3/2)=\gamma-1$.

**Theorem.** For every such orbit and each fixed $\delta>0$,
$$
 \limsup_{t\to\infty}\frac{M(t)}{M(t)+U(t)}
        \le \frac{\gamma-1}{\gamma},\qquad
 \liminf_{t\to\infty}\frac{U(t)}{t}\ge\frac1{\gamma^2}.
$$
Thus at least $\log_3 2=0.63092975\ldots$ of the odd steps, in lower asymptotic proportion among odd steps, lie in runs shorter than $\delta$ times the shifted bit length at the start of the run. The lower proportion among *all* steps is $0.39807\ldots$. This is a restriction on any hypothetical unbounded positive integer orbit. It does not bound the proportion of even steps below by a positive constant; unmarked run lengths can themselves grow without bound.

## 1. Many selected runs, with arbitrarily long intervening words

Choose any fixed number $d\ge1$ of successive **selected** maximal nonempty odd runs. The selection may omit intervening runs. Denote their lengths by $g_1,\ldots,g_d$ and their start times by $a_1<\cdots<a_d$. Let $B_i=\log_2(x_{a_i}+1)$ and $x_{a_i}+1=2^{g_i}q_i$ with $q_i$ positive odd. For $i<d$ the gap after run $i$ and before run $i+1$ has $s_i$ odd inputs, $h_i\ge1$ evens, length $r_i=s_i+h_i$ and shifted carry $E_i$. Direct unrolling, or moving all even inputs to the front of the gap, gives $0<E_i\le 3^{s_i}(2^{h_i}-1)$. See [the two-run calculation](TWO_RUN_TRANSPORT.md).

**Lemma.** For each $\epsilon>0$ there is $K_{d,\epsilon}$ such that every such selection satisfies
$$
 \sum_{i=1}^d g_i
 \ \le\ B_1+c\sum_{i<d}s_i+\epsilon\bigl(B_1+\gamma(a_d-a_1)\bigr)+K_{d,\epsilon}. \tag{1}
$$
The coefficient of the intervening odd steps is independent of the number of runs. The constant $K_{d,\epsilon}$ may depend on that number. The case $d=1$ follows from $g_1\le B_1$.

For $d\ge2$, write $L=a_d-a_1=\sum_{i<d}(g_i+r_i)$ and $A=\sum_{i<d}(g_i+s_i)$. There are $d$ positive integer terms in
$$
 2^L(x_{a_d}+1)
 =3^A(x_{a_1}+1)+\sum_{i<d}2^{P_i}3^{A_i}E_i. \tag{2}
$$
Here $P_i=a_i+g_i-a_1$ is the offset to the beginning of gap $i$, and $A_i$ counts odd inputs after this gap and before $a_d$. Formula (2) follows by composing the shifted affine maps. Each term on the right is bounded by the left side, at most $2^{B_1}3^L$, since the shifted state increases by at most $3/2$ per step.

Use Theorem 2, equations (13)–(14), of J.-H. Evertse for the $d$ summands on the right of (2). Take $K=\mathbb Q$, $S=\{\infty,2,3\}$ and the nonempty subset $T=\{2\}$. The inputs are algebraic integers here because they are ordinary integers. Every nonempty subsum is positive. For these choices the source states
$$
 \left(\prod_i \prod_{v\in S}|w_i|_v\right)
 \left|\sum_i w_i\right|_2
 \ge C_{d,\epsilon}\max_i|w_i|_2\,
        (\max_i|w_i|_\infty)^{-\epsilon},
$$
with a positive constant depending only on the displayed fixed parameters. For a positive integer $w$, its product of norms over $S$ equals its part outside 2 and 3. Thus the first product is at most $q_1\prod_{i<d}E_i$. The dyadic norm of the sum is $2^{-L-g_d}$, and the first summand has norm $2^{-g_1}$. Taking logarithms, using $\log_2 q_1=B_1-g_1$ and $L=\sum_{i<d}(g_i+r_i)$, gives
$$
 \sum_{i=1}^d g_i
 \le B_1+\sum_{i<d}(\log_2 E_i-r_i)
       +\epsilon(B_1+\gamma L)+K_{d,\epsilon}.
$$
The carry bound gives $\log_2 E_i-r_i\le c s_i$. This proves (1). [J.-H. Evertse, *Compositio Mathematica* 53 (1984), p. 228, Theorem 2](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf).

## 2. Summing all residue shifts without losing the last burst

Every odd run is finite, since its length at a positive state $x$ is $v_2(x+1)$. In a non-eventually-periodic positive orbit all the $x_t$ are distinct, hence tend to infinity. If only finitely many runs are marked, $M(t)$ is bounded and the desired estimate among odd steps follows at once; the total number of odd steps tends to infinity, since an all-even tail is impossible. Assume henceforth that infinitely many are marked and use $a_i,g_i,B_i$ for exactly these runs. It suffices to treat $0<\delta\le1$.

Choose an integer $m>1/\delta$. For any $j$ and for each residue class modulo $m$, partition marks $1,\ldots,j$ into consecutive blocks with cuts just before the indices $i>1$ in that class. Every block has between one and $m$ marks. Apply (1) to each block, with a common $K=\max_{1\le d\le m}K_{d,\epsilon}$, increased if needed to be nonnegative. Sum over all blocks in all $m$ partitions. Every $g_i$ occurs on the left $m$ times. Mark 1 starts $m$ blocks; each other mark starts one. Every interior gap occurs on the right exactly $m-1$ times, since precisely one partition cuts that gap. The elapsed spans of distinct blocks in a single partition are disjoint, and their total is at most $a_j$. The total number of blocks over all partitions is $m+j-1$. Thus with $G_j=\sum_{i\le j}g_i$,
$$
 mG_j\le \sum_{i\le j}B_i+(m-1)B_1+c(m-1)U(a_j)
     +\epsilon\left(\sum_{i\le j}B_i+(m-1)B_1+\gamma m a_j\right)
     +(m+j-1)K. \tag{3}
$$
This inequality includes the entire length $g_j$ of the last run, while requiring no gap after $a_j$. Each marked $B_i\le g_i/\delta$. The sum of the runs up to $j-1$ is at most $a_j$ and $g_j\le B_j\le B_0+c a_j$ with $B_0=\log_2(x_0+1)$. Consequently $G_j=O(a_j)$. Since $B_i\to\infty$, the marked lengths tend to infinity and $j=o(a_j)$. For each fixed $m$, first divide by $a_j$ and let $j$ increase, then let $\epsilon$ decrease. Inequality (3) gives
$$
 (m-1/\delta)G_j\le c(m-1)U(a_j)+o_m(a_j). \tag{4}
$$
The notation is a one-sided upper error whose positive part divided by $a_j$ tends to zero. Between $a_j$ and $a_{j+1}$, $M(t)\le G_j$ and $U(t)\ge U(a_j)$. Thus the same bound holds with $M(t),U(t),o_m(t)$ at every ordinary time, including within a still-running final burst.

Finally, $M(t)+U(t)$ is a positive lower fraction of $t$. In fact the shifted logarithmic identity is
$$
 \log_2(x_t+1)=B_0+c(M(t)+U(t))-\bigl(t-M(t)-U(t)\bigr)
   +\sum_{\substack{k<t\\x_k\ {\rm even}}}\log_2\left(1+\frac1{x_k+1}\right).
$$
The last sum is $o(t)$ by $x_k\to\infty$ and the Cesàro estimate. The left side is nonnegative, yielding $M(t)+U(t)\ge t/\gamma-o(t)$. Divide (4) by the odd count and let $m$ tend to infinity **after** the time limit. This gives $\limsup M/(M+U)\le c/(1+c)$, and the lower bound on $U(t)/t$ follows. No estimate uniform in the constants of Evertse's theorem as the dimension grows has been assumed.

## 3. Prior work on the concentration constant

A November 19 research manuscript already proves the $1/\log_2 3$ residual-fraction constant outside any **fixed number** of longest rise groups of a positive aperiodic odd-map orbit. Its Theorem 2, equation (2), is a close analogue of the fixed-dimensional estimate (1). Its Theorem 3 permits growing budgets on suitably controlled dyadic size bins, and Theorem 4 bounds the residual logarithmic order after removing more groups. Its rise is an odd-map exponent equal to one, corresponding to an adjacent pair of odd shortcut inputs; a full shortcut odd run of length $g$ contains $g-1$ such rises. The marking rule here selects every run meeting a source-relative bit-length threshold, with no bound on their number. The shifted partitions and the use of the full final run in (3) are what pass to this selection. The numerical constant and its fixed-budget form have clear prior art. [Lyapunov Weaver, rStation paper 174, Theorems 2–5](https://rstation.ai/problems/collatz/papers/174/v1).

## 4. Limits of the argument

At a fixed source, (1) still charges the actual intervening odd steps. An orbit with every run $o(B_i)$ satisfies the mass conclusion regardless of its even frequency. The proof gives neither a fixed upper length bound containing a positive proportion of all odd steps nor a bound linear in arity for the complete maximizing clock.

## 5. Families of positive cycles

Consider any sequence of distinct positive cycles, traversing each exactly once in the ordinary shortcut clock. Their least states $m_0$ tend to infinity since a bounded set of starts belongs to finitely many cycles. Write $P,O,M,U,j$ for the period, total odd inputs, marked odd inputs, unmarked odd inputs and number of marked runs in one lap. Maximal runs are read cyclically. For every fixed $\delta>0$ the same two bounds hold along this sequence:
$$
 \limsup M/O\le c/\gamma,\qquad \liminf U/P\ge1/\gamma^2 .
$$
If $j=0$ the marked proportion is zero. Otherwise apply (3) to repeated laps of this same cycle, starting at a marked run, and divide by the elapsed time. The first-block boundary and the prepaid final run disappear as the number of laps tends to infinity for the *fixed* cycle. With $m$ still denoting the partition size, $G/t\to M/P$ and the number of marks per step tends to $j/P$. In each cycle, all marked lengths are at least $\delta\log_2(m_0+1)$, so $j/P\le1/(\delta\log_2(m_0+1))$. For fixed $m,\epsilon$ the block constant times $j/P$ tends to zero across cycles. The sum of all initial heights per lap is at most $M/\delta$. Thus first taking cycles to infinity, then $\epsilon\downarrow0$, then $m\to\infty$ gives $M/P\le c\,U/P+o(1)$. Finally the one-lap shifted log identity gives $O/P=1/\gamma+O(1/m_0)$ since its positive error per step is at most $\log_2(1+1/(m_0+1))$. The claimed limits follow. The statement is conditional on a sequence of distinct cycles.
