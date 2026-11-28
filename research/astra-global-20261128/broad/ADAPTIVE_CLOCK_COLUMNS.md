# A finite signed auxiliary for arbitrary selected clock translates

**Written proof.** Take the $M+1$ even inputs at actual times $0=t_0<\dots<t_M$ in a positive or zero even ordinary source $x$. Put $u_j=t_j-j$, $p_j=2^{t_j}/3^{u_j}$, $S_j=\sum_{i<j}p_i$, and $y=-(x+1)$. The native identity gives $v_2(y-S_M)=t_M$.

Choose $0\le h<M-1$ and distinct indices $0\le k_1<\cdots<k_m\le h$, with $m>r=M-h-1$. Choose nonnegative integer artificial exponents $v_k$ at the selected indices and weights $w_k=2^{k+v_k}/3^{v_k}$. The selected columns and their exponents may be chosen after examining the finite path. All bounds below involve finite rational or integer data.

For each interpolation row $h<\ell<M$, put
$$
 R_\ell=\max_{k}(v_k+u_{\ell-k})-\min_{k}(v_k+u_{\ell-k}),\qquad
 H=3^{\max_\ell R_\ell}.
$$
Choose an integer $B\ge1$ with
$$ (B+1)^m>(mHB+1)^r . \tag{1}$$
Assume the selected weights satisfy $4B w_{k_{i+1}}\le w_{k_i}$ for all $i<m$. Define the exponents
$$
 A=\max_k (v_k+u_{h-k}),\qquad
 \Theta=\min\left\{t_M+\min_k(k+v_k),\quad
                 \min_k(k+v_k+t_{M-k})\right\}.
$$
Then the following inequality holds:
$$
 \boxed{\quad 2^\Theta\le3^A\,2B w_{k_1}(x+1+S_{h+1}).\quad} \tag{2}
$$
Here $A$ also clears the head weights, since all $u_j\ge0$. The weights need not be the native $p_k$.

**Proof.** Write $b_\ell=\min_k(v_k+u_{\ell-k})$. In row $\ell$, divide all $w_k p_{\ell-k}$ by the common positive rational $2^\ell(2/3)^{b_\ell}/3^{R_\ell}$. The resulting integer entry equals
$$2^{v_k+u_{\ell-k}-b_\ell}3^{R_\ell-(v_k+u_{\ell-k}-b_\ell)}\in[1,H].$$
By (1), differences in the integer box $\{0,\ldots,B\}^m$ yield nonzero integers $q_k$ as a vector, $|q_k|\le B$, with $\sum_kq_kw_kp_{\ell-k}=0$ in every high row. Set
$$ Q=\sum_k q_k w_k,\qquad P=\sum_k q_k w_k S_{h-k+1}. $$
If $k_i$ is the first nonzero position of $q$, then $|q_{k_i}|\ge1$ while
$$\sum_{j>i}|q_{k_j}|w_{k_j}\le 2B w_{k_{i+1}}\le w_{k_i}/2$$
with an empty sum at the last index. The partial sums $S_{h-k+1}$ are positive and nonincreasing as $k$ increases. Consequently $Q,P$ have the same nonzero sign and $F=Qy-P\ne0$.

In $Q S_M$, terms with $k+j\le h$ give $P$. Terms with $h<k+j<M$ cancel exactly. For each remaining term, $j\ge M-k$ and $v_2(w_kp_j)=k+v_k+t_j\ge k+v_k+t_{M-k}$. The difference $Q(y-S_M)$ has valuation at least $t_M+\min_k(k+v_k)$, with the zero case automatic. Hence $2^\Theta$ divides the nonzero integer $I=3^A F$. Geometric decay gives $\sum_k w_k\le2w_{k_1}$, so $|F|\le2B w_{k_1}(x+1+S_{h+1})$. This proves (2).

**Reflected weights.** Fix any $a\ge h$ with $a\le M$. Taking $v_k=u_a-u_{a-k}$ makes the row $\ell=a$ constant. Its other row spreads equal the spread of $u_{\ell-k}-u_{a-k}$ across the selected columns. Thus the coefficient height depends on translated **short increments** near the interpolation rows and need not reflect the full initial discrepancy. The leading-weight ratios for consecutive columns equal $2(2/3)^{g_{a-k-1}}$; skipping a column multiplies through the skipped ratios. In particular the sign condition can tolerate unused positions whose individual gaps are small.

For the simplest dense choice $k=0,\ldots,h$, $h=4s,M=7s$, one may take $B=(2mH)^3$. Taking $v_k$ equal to the native $u_k$ gives an intrinsic test; choosing another profile can shrink the finite row spreads or improve the source exponent. Equation (2) is an arithmetic restriction on any such chosen finite configuration. A general theorem producing a configuration with a prohibitive right-hand side from every escaping trajectory remains open.

## A limitation across all choices of columns and artificial exponents

Take an integer $J\ge1$. Suppose throughout the finite observed window that
$$
 1\le g_{i+1}-g_i\le J\qquad(0\le i<M-1).
$$
Constants in the following estimate may depend on $J$. For **every** permitted choice of columns and exponents, a positive value of $\Theta-\log_2(3^A\,2B w_{k_1})$ requires, after the first-column normalization below,
$$
 M\ll_J \sqrt{g_0+1}. \tag{3}
$$
The test is insensitive to a long part of a window that is removed by this normalization.

To normalize, let $k_1=k_0$. The sign condition forces $v_k$ to increase strictly along the selected columns. Subtract $k_0$ from every index, $v_{k_0}$ from every selected exponent, and $k_0$ from both $h$ and $M$. All row spreads and the number of rows stay the same. The exponents $\Theta$ and $A$ drop by $k_0+v_{k_0}$ and $v_{k_0}$ respectively. For $\Theta$, the term from the first column is $k_0+v_{k_0}+t_{M-k_0}$, so the separate lower constraint from $t_M$ is redundant. The factor $w_{k_0}=2^{k_0+v_{k_0}}/3^{v_{k_0}}$ cancels these exponent changes exactly. The new head weight is one. In (3), $M$ denotes this effective horizon and $g_0$ is still the first observed gap of the input. Equivalently, a certificate omitting the first $k_0$ columns tests the same normalized product against a shorter **initial** prefix of length $M-k_0$ in event time.

After normalization assume $k_1=v_{k_1}=0$. Positive payoff entails $\gamma A<\Theta$ for $\gamma=\log_2 3$. The first column gives $A\ge u_h$ and $\Theta\le t_M=M+u_M$. Also
$$
 u_M\ge Mg_0+\binom M2,\qquad
 u_M-u_h\le (r+1)(g_0+JM).
$$
It follows that $(\gamma-1)u_M-M<\gamma(r+1)(g_0+JM)$. For sufficiently large $M$, this forces $r\gg_J M$, uniformly in $g_0$. Indeed the left side is at least a positive constant times $M(g_0+M)$.

Let $k=k_m\ge m-1$ be the last active index. As the row index runs from $h+1$ through $M-1$, the quantity $u_\ell-u_{\ell-k}$ increases by at least $k$ per step. This follows by summing $g_{i+k}-g_i\ge k$. At both extreme rows, $v_k+u_{\ell-k}-u_\ell$ lies within $R=\max_\ell R_\ell$ of zero, since the first and last columns occur in the same row. Thus $2R\ge k(r-1)\ge(m-1)(r-1)$. The box hypothesis (1) implies $m\log_2(2B)>r\log_2 H=\gamma rR$. Since $m>r\gg_J M$, we obtain $\log_2(2B)\gg_J M^2$.

Multiplying all the neighboring weight-decay inequalities shows
$$
 (\gamma-1)v_{k_m}\ge k_m+(m-1)\log_2(4B)\gg_J M^3.
$$
But $A\ge v_{k_m}$ and $\Theta\le M(1+g_0)+JM^2$. A positive payoff therefore implies $M^3\ll_J M(1+g_0)+JM^2$, which proves (3), including bounded $M$ by enlarging the constant.

For an infinite hypothetical integer orbit with $1\le g_{i+1}-g_i\le J$, the shifted source $x_j=T^{t_j}x$ satisfies
$$
 \log_2(x_j+1)\ge\log_2(x+1)+(\gamma-1)u_j-j\gg j^2 .
$$
This follows from the positive finite native calibration $p_j(x_j+1)=x+1+S_j$. Here $g_j=O(j+1)$. At any sufficiently late source, (3) limits an informative translate to $O_J(\sqrt{g_j+1})$ effective events with total physical length $O_J((g_j+1)^{3/2})$, smaller than that source's bit length. Since the payoff is at most the effective $t_M$, (2) cannot yield an asymptotic contradiction on these translates.

This limitation applies to the box bound and uniform geometric sign hypothesis in (1)–(2). A specially constructed smaller integer vector, a sharper nonvanishing proof or additional arithmetic information can evade it. Exact constant curvature is already handled by the independent finite $q$-Padé construction. No existence theorem for a positive integer orbit with the displayed curved profile is asserted.
