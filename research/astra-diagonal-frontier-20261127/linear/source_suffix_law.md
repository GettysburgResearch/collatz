# Joint binary and ternary source digits at a physical first landing

Let $V_Y$ be uniform on all positive integers in $[Y,2Y)$, and let $L_r$ be the first odd landing at or below $r$ after stripping initial powers of two. Include a cemetery state and immediate landings. The same result holds for any countable shortcut-invariant orbit label, using $r=1$. Put $v=\log(Y/r)$ and let $\mu_r$ be the limiting label law in the [relative renewal theorem](renewal_landing.md). For every $A>0$ there are $c_A,C_A>0$ such that, for $v$ sufficiently large and integers $b,m\ge0$ satisfying
\[
                       b+m\le c_A v ,
\]
the following relative comparison holds. Let $\Pi$ be the product of the uniform law on residues modulo $2^b3^m$ and $\mu_r$. For every test $0\le H\le1$ on the full residue and label spaces,
\[
 \left|\mathbb E H(V_Y\bmod2^b3^m,L_r(V_Y))-\Pi(H)\right|
                \le C v^{-1/9}\Pi(H)+C_A v^{-A}.                    \tag{1}
\]
All constants are independent of $r,Y$ and the test. In a fixed smooth source window of integral one, the first term on the right may be omitted, with constants depending on the smooth shape. Restricting to odd uniform starts gives the same conclusions with the uniform law on the odd residue classes if $b>0$; at $b=0$ use one initial parity bit. The allowable $c_A$ can shrink with $A$. This written deduction uses the extra-depth estimate (66) of Paper 48, the finite-quotient moment bound below and the source-qualified relative renewal theorem.

Relative to the actual unconditioned octave label marginal, the **ternary-only** comparison has arbitrarily small inverse-logarithmic errors even on sharp octaves. For joint suffixes the corresponding sharp every-order comparison retains the number of odd departures of the prescribed initial parity word, as in (5) below. These are joint sum-norm bounds. At a cell of exponentially small baseline mass the additive term can exceed that mass; a guarantee for each individually supplied binary cell is given separately by the [local first-landing count](local_first_landing.md). The fixed-modulus independence of predecessor labels was already known from Duran and Leen; Weaver's Paper 12, §3, explicitly distinguishes that statement from a growing fine modulus. [Weaver, Paper 12 v1, §3](https://rstation.ai/problems/collatz/papers/12/v1) · [Weaver–Wren, Paper 48 v1, Theorem 6, (65)–(66)](https://rstation.ai/problems/collatz/papers/48/v1).

## Ternary digits of the actual source and its joint clock

Let $t$ be an odd clock, $q=3^t$, $M=3^m$, and let $P_s(z)$ be the fair mass of the outward affine offset $F\bmod qM$ and exact total $s$. Average on each $q$-fibre with $P_s^*(z)=M^{-1}\sum_{z'=z\bmod q}P_s(z')$. Paper 48 gives
\[
                 \sum_s\|P_s-P_s^*\|_{\ell^1(\mathbb Z/qM)}
                    \le C_B t^{-B}\quad(m\le\delta_B t).            \tag{2}
\]
As in PR 195's one-trit physical-source argument, start with odd inputs $x$ in any subinterval $I$ of $[X,2X)$ with $1\le t\le(\log_2 X)/32$, weight $f_t(x)/x$, and retain the actual positive endpoint $y=U^t x$ and total $s$. The earlier theorem used a mean-zero test modulo three. Here retain *all* $M$ input-residue rows in the sum norm.

Discarding $s>4t$ and replacing the source filter by $y\in3^t2^{-s}I$ on the remaining words costs $O(e^{-ct}+2^{4t}/X)$ in total unsigned mass, unchanged upon adding the actual input residue as a mark. In fact a discrepant original input is within $O(2^{4t})$ of an interval boundary and has a unique word. The high-total tail is decided within $4t$ shortcuts and is bounded by the ordinary binary-cylinder count. For fixed $s,y$, a compatible word has $x=2^s(y-F)/q$. Thus the residual coefficient at input residue $j\bmod M$ after the filter replacement is
\[
       \frac qy 1_{\{y\in q2^{-s}I\}}
            P_s(y-q2^{-s}j\bmod qM).                                \tag{3}
\]
Replacing $P_s$ by $P_s^*$ makes this exactly the marginal coefficient divided by $M$. As $j$ runs over all residues, the arguments run once through the whole fibre over $y\bmod q$. Its sum of absolute errors depends only on $y\bmod q$. In the output interval each such class occurs at most $1+q2^{-s}X/q=1+X2^{-s}$ times (enlarging by an absolute endpoint constant). Since $X2^{-s}\gg1$ and $q/y\ll2^s/X$, summing over the **actual positive** $y$ and all $j$ costs $O(\|P_s-P_s^*\|_1)$. In particular the extra factor $M$ never appears. Summing (2) proves total-variation independence of the input residue from the joint physical endpoint and native count, with error $O_B(t^{-B})$ for this unnormalized reciprocal source measure. [PR 195, PHYSICAL_SOURCE and MARKED_FIBRES (3), commit 3fa7ef4a](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/PHYSICAL_SOURCE.md).

Choose $t=\lfloor c\log(X/r)\rfloor$ with $c>0$ small. On the good short trajectories the actual label agrees with the endpoint label, since all departures exceed $X2^{-4t}>r$. Remove $f_t$, apply partial summation, and strip the initial powers of two for an all-positive sample, exactly as in the renewal theorem's proof of its signed ternary estimate (3). The residue transformation under stripping is a permutation on $\mathbb Z/M$. Each error was an unsigned source mass bound or a sum norm, so all input residues still participate at once. For the sharp octave and also for any fixed nonnegative smooth source weight $\varphi(x/X)/X$, let $P_X(j,l)$ be the resulting measure on the residue $j\bmod M$ and label $l$, with marginal $p_X(l)$. On an actual sharp octave one may take weight $1/X$ before the harmless final normalization. We have shown
\[
       \sum_{j,l}|P_X(j,l)-M^{-1}p_X(l)|
               \ll_{B,\varphi}(\log(X/r))^{-B}
                         \quad(m\le c_B\log(X/r)).                   \tag{4}
\]

## Passing a prescribed binary suffix to its true ternary progression

Use the native shortcut $T(x)=x/2$ at even $x$ and $(3x+1)/2$ at odd $x$. Its first $b$ parities are a bijection on the binary input residues modulo $2^b$: each additional binary digit selects the next parity, since changing the starting point by $2^k$ shifts its time-$k$ endpoint by the odd number $3^{d_k}$ when its first $k$ parities are held fixed. For a particular binary class $w$, let $d=d(w)$ be the number of odd departures through time $b$, and write
\[
                 y=T^b x=3^d2^{-b}x+F_w,\qquad 0\le F_w<3^d .
\]
If its odd positions are $0\le i_1<\cdots<i_d<b$, then $F_w=\sum_{j=1}^d3^{j-1}2^{-(b-i_{d+1-j})}$; the empty sum is zero. The affine progression for this binary class has step $3^d$ in $y$ and residue $r_w=F_w\bmod3^d$. Fixing in addition $x\bmod3^m$ singles out one of the $3^m$ finer residues modulo $3^{d+m}$ above $r_w$. The map from the original trit vector to that finer residue is a bijection, by the unit $2^b$ in the affine equation.

Put $Y_d=Y3^d2^{-b}$. The images for $Y\le x<2Y$ occupy $[Y_d+F_w,2Y_d+F_w)$ within the stated progression. Replacing this interval by $[Y_d,2Y_d)$ changes at most two outputs per binary class because $F_w<3^d$. After summing every additional ternary mark the normalized error is $O(2^b/Y)$. With smooth weights, shifting the shape by $F_w/Y_d$ gives the same order times a fixed $C^1$ norm; each actual input determines only one mark. All intermediate native states are $\ge x2^{-b}>r$ on the sharp or fixed compact positive support for small enough $c_A$, so their actual labels agree.

For $d\ge1$ let $N_d(s)$ count the binary classes with odd count $d$ and $r_w=s\bmod3^d$. Reverse the gaps from the terminal time: their successive cumulative sums are $b-i_d,\ldots,b-i_1$. Thus $w$ gives a distinct positive gap word of total $A=b-i_1\le b$ at that residue. Conversely its remaining $b-A$ initial halvings fix the binary pattern. It follows that
\[
                   3^d2^{-b}N_d(s)\le \rho_d(s).
\]
Indeed its weight is its fair ternary density contribution $3^d2^{-A}$ times $2^{-(b-A)}\le1$. For $d=0$ use $\rho_0=1$ and the single all-even word.

At scale $Y_d$ apply (4) to the full $3^{d+m}$ residues. Denote the sum of absolute errors above each coarse residue $s$ by $e_s$. Then $\sum_s e_s=O_B(v^{-B})$ since $\log(Y_d/r)\ge v-b\log2\ge v/2$ and $d+m\le c_B\log(Y_d/r)$. Also $3^d e_s=O_\varphi(1)$: its row mass is bounded by counting the complete coarse progression in the original interval, since $Y_d/3^d=Y/2^b\gg1$. The errors after lifting back to the binary classes are at most
\[
 \sum_d\sum_s3^d2^{-b}N_d(s)e_s
   \le\sum_d \langle\rho_d\,3^d e_\cdot\rangle
       \ll_{p,\varphi}(b+1)v^{-B(1-1/p)} .
\]
Here $\rho_d$ has bounded whole-quotient Haar $L^p$ norm for any fixed $1<p<2$, and the last step is Hölder and the two preceding bounds on $e_s$. Choose $B$ large for the requested $A$, then choose $c_A$ accordingly. [Ordinary finite-quotient moment input, commit aa686899](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md).

Consequently, in joint sum norm the actual law of $(w,j,l)$ is within $O_{A,\varphi}(v^{-A})$ of the array
\[
                           2^{-b}3^{-m}p_{Y_{d(w)}}(l).               \tag{5}
\]
This is the stated sharp-window comparison retaining only the odd count from the binary suffix. Applying the relative renewal theorem to each positive test $l\mapsto H(w,j,l)$ at $Y_d$ gives (1), because all its logarithmic separations are comparable to $v$. In a fixed smooth window its estimate (7) instead gives every-order errors in the full label norm. All steps sum over genuine ordinary starts before applying the analytic mixing bound. The omitted individual-cell inference would require absolute error smaller than that cell's own mass.
