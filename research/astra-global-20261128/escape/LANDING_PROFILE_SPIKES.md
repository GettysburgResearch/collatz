# Unbounded first-landing profiles on a critical ternary set

**Source-qualified written theorem.** Use the density $G$ and the maximum-multiplier recursion (6) of [the local first-landing law](LOCAL_LANDING_PROFILE.md). Weaver, Paper 12, Theorem 15 already constructs individual ordinary thresholds with first-landing atoms $\gg(\log B)/B$ by exits from a balanced reverse word. The theorem below counts the ternary addresses supporting such prefixes and gives lower bounds on positive-volume neighborhoods in the continuum profile. Weaver, Paper 146, §2 gives the older fixed-cap approximation and every finite moment. [Ordinary balanced peaks](https://rstation.ai/problems/collatz/papers/12) · [Fixed-cap estimates](https://rstation.ai/problems/collatz/papers/146).

For an infinite sequence of positive integers $e_i$ in inverse order, put
\[
 D_i=\sum_{j\le i}e_j,\quad A_i=3^i2^{-D_i},\quad B_i=\tfrac13\sum_{j\le i}A_j,
 \quad z=\lim_iB_i\in\mathbb Z_3.
\]
The limit is in the ternary metric; $A_0=1$ and $B_0=0$. Let $\mathcal B$ contain the addresses $z$ admitting at least one such code with $0<a\le A_i\le b<1$ for all $i\ge1$, for some constants $a,b$ depending on the code. In the usual ternary metric,
\[
                 \dim_H\mathcal B=H_2(\log_3 2).                       \tag{1}
\]
For every $z_*\in\mathcal B$, fix one of its codes and constants. For $b<u<1$ and $z\equiv z_*\pmod{3^{n+1}}$, with respect to the product reference measure almost everywhere on that rectangle,
\[
                          G(u,z)\ge c_a n \qquad(n\ge1).              \tag{2}
\]
In particular $G$ is essentially unbounded, its superlevel sets have reference volume at least $c e^{-C t}$ for all large $t$, and $\|G\|_p\gg p$ for all sufficiently large $p$. There is no positive ordinary integer in $\mathcal B$. The lower bound on positive-volume ternary cylinders in (2) does not require a value for $G$ at the particular address itself.

## Distinct exits give the local lower bound

After $i$ prescribed letters, a compatible $z$ has residual ternary state $z_i=(z-B_i)/A_i$ and residual cap $u/A_i$. Along the prescribed prefix every product $A_j$ for $1\le j\le i$ is less than $u$, so repeated use of (6) permits it. For $1\le i<n$, the residual $z_i$ is a unit, as the original code continues for at least one letter. Indeed the original residual is the image of $z_{i+1}$ under an affine ternary map with nonzero unit output, and the imposed depth $n+1$ fixes $z_i$ modulo at least nine.

Choose a new eligible letter $f_i$ in $\{3,4,\ldots,14\}$ distinct from $e_{i+1}$ such that the new residual $(2^{f_i}z_i-1)/3$ is a unit. For each unit class modulo nine, out of six consecutive exponents two have the correct divisibility by three and give a unit quotient, since the order of two modulo nine is six. The displayed interval contains two such periods. The choice can be fixed on the entire cylinder. Its multiplier $A_i3/2^{f_i}$ is less than $u$, since $A_i\le b<u$ and $f_i\ge3$. On the innermost branch the cap is $u/(A_i3/2^{f_i})>1$. The unit floor $G(v,\cdot)\ge c$ almost everywhere for almost every $v\in[1/2,1]$ and monotonicity of the cap measures imply a common lower bound $h_1\ge c'$ almost everywhere on unit trits. Images and inverse images by the fixed eligible ternary affine maps preserve null sets there. Thus each branch supplies at least $c'a\,3/2^{14}$ to $h_u$ when $i\ge1$. The words exiting for different $i$ are prefix-free, hence their contributions sum by nonnegativity and (6). For $n\ge2$, keeping $1\le i<n$ gives a linear bound after changing the constant. For $n=1$, the unit floor for $G$ itself gives (2) directly, with a smaller constant. Equivalently the unit floor on $[1/2,1]$ extends to almost every height by $G(u/2,z)=G(u,2z)$, since multiplication by two preserves unit trits and their Haar measure. Equation (6) then proves (2), since $D u\le D$.

For an explicit fixed address choose $0<\theta<2-\log_23$ and $D_i=\lceil i\log_23+\theta\rceil$ for $i\ge1$. Its positive letters have $2^{-1-\theta}\le A_i\le2^{-\theta}<1$. Thus (2) holds on a fixed positive height interval and ternary cylinders of volume $3^{-(n+1)}$. Choosing $n$ proportional to $t$ gives the superlevel lower bound; choosing $n=\lceil p\rceil$ in the $p$-norm gives the claimed linear growth. Finally, were $z_*=y$ a positive odd ordinary integer, each successive residual of its legal inverse word would be a positive odd integer and $y=A_ix_i+B_i>B_i\ge ai/3$ for every $i$. For a positive even ordinary $y$, the first legal inverse is an odd positive integer too: $2^{e_1}y-1$ is positive odd and division by three preserves oddness. The same contradiction applies.

## Dimension of the balanced addresses

Write $\alpha=\log_2 3$. A bounded-multiplier code has $D_i=\alpha i+O(1)$. For a fixed bound on this error, cover by the depth-$n$ ternary cylinders of all words with totals in that bounded interval. At total $d$ the number is $\binom{d-1}{n-1}$. Stirling's formula gives logarithmic count per letter tending to $\alpha H_2(1/\alpha)\log 2$, or $H_2(\log_3 2)$ after division by $\log3$. The countable union over integer error bounds gives the upper bound in (1).

For the opposite direction fix a large block size $k$. After one initial large exponent, choose the next $k$-letter block at stage $l$ uniformly among all compositions of
\[
     d_l=\lfloor l k\alpha\rfloor-\lfloor(l-1)k\alpha\rfloor
\]
into $k$ positive integers, independently over blocks. Every block has total either $\lfloor k\alpha\rfloor$ or $\lceil k\alpha\rceil$. At block boundaries the cumulative clock differs from $lk\alpha$ by at most one; within a block it differs from its critical value by $O(k)$ uniformly over all choices. Choose the fixed initial exponent large enough that every nonempty prefix multiplier lies in $[a_k,b_k]$ with $a_k>0$ and $b_k<1$. Thus the pushforward law of the resulting address is supported on $\mathcal B$.

At depth $n=1+lk$ the total $d$ is deterministic. For the integer numerator $C_w=2^d B_n$, the pair $(d,C_w)$ determines the entire word: $C_w-3^{n-1}=2^{e_n}C_{w^-}$, where the previous numerator is odd, and iteration recovers all letters using $d$ for the first. This is the numerator argument of Weaver, Paper 146, §2. In any fixed residue cylinder $B_n\bmod3^n$, the integers $C_w$ lie in a single residue class modulo $3^n$. Since $B_n\le n/3$ and $2^d/3^n=1/A_n\le1/a_k$, there are $O_k(n)$ possibilities. Each word has probability at most $M_k^{-l}$, where
\[
             M_k=\min_{d\in\{\lfloor k\alpha\rfloor,\lceil k\alpha\rceil\}}
                         \binom{d-1}{k-1}.
\]
Hence each depth-$n$ cylinder has mass $O_k(n)M_k^{-l}$. Intermediate depths differ by at most $k$, so the mass distribution principle gives dimension at least $(\log M_k)/(k\log3)$. As $k\to\infty$ these bounds tend to $H_2(\log_3 2)$, proving (1). The same real constant also appears in previous binary counts of permanently positive-drift paths; (1) describes ternary addresses of restricted inverse words and does not assume an ordinary positive path with that behaviour.
