# The ternary cost of following a native inverse lap

Use $U(z)=(3z+1)/2^{v_2(3z+1)}$ on positive odd integers. A native block consists of $r\ge1$ reverse edges with exponents $a_1,\ldots,a_r$ from $x$ to $u$. Suppose $x$ is a ternary unit. A candidate reset from another odd ternary unit $y$ uses the same block except for adding an integer $t\ge0$ to its first exponent. The endpoint of this reset is allowed to float.

## One padded entrance to any native block

The entire path is physically legal if and only if
$$3^r\mid 2^t y-x.\tag{1}$$
Indeed the first reverse exponent does not contribute to the carry of the block. Subtract the two affine equations, with $A=\sum a_i$, to find $3^r(z-u)=2^A(2^t y-x)$. This proves necessity. For sufficiency (1) makes $z$ integral and the resulting whole equation gives every intermediate division as in the carry proof. Each ordinary integral inverse step from a positive odd value is positive and odd.

There is an absolute effective $C$ such that, whenever $x,y\le H$ and $2^t y\ne x$, (1) implies
$$r\le C\log(2H)\log(3+t).\tag{2}$$
Apply the consequence of Yu's Theorem 1 printed immediately after equation (1.1), with number field $K=\mathbb Q$, prime ideal $(3)$, $n=2$, $\alpha_1=2,\alpha_2=y/x$, $b_1=t,b_2=1$ and $B=\max(3,t)$. The field degree, residue degree and ramification index are one. The prime 3 satisfies the paper's condition (1.2) through $3\equiv3\pmod4$. Both inputs are 3-adic units as required by (1.9), and $2^t y/x-1\ne0$. The rational logarithmic heights are $\log 2$ and at most $\log H$; (1.8) allows the chosen $B$. Since $x$ is a ternary unit the valuation of the linear form is the valuation needed in (1). These substitutions give (2) with an absolute constant. No multiplicative independence hypothesis occurs in the theorem. [Kunrui Yu, *p-adic logarithmic forms and group varieties II*, Acta Arith. 89 (1999), 337–378](https://doi.org/10.4064/aa-89-4-337-378)

For positive odd $x,y$ the exact exception $2^t y=x$ means $t=0,y=x$. When $y=x$ and $t>0$, (1) more explicitly requires $2\cdot3^{r-1}\mid t$: odd $t$ gives valuation zero, and $v_3(2^t-1)=1+v_3(t)$ for even $t$. When $t=0$ and $x\ne y$, direct size already bounds $r\le\log_3 H$.

In particular a $p$-edge native lap on a bounded ordinary candidate cannot be attached by a polynomial first padding from a different odd ternary-unit terminal of polynomial height. If $x,y\le p^A$ with fixed $A$, any nonidentity such reset costs $t\ge\exp(c_A p/\log p)$ for all sufficiently large $p$. This applies to every phase and every such incoming integer, with no height assumption on the resulting source. Repeating the same native lap $m$ times as one block replaces $r$ by $mp$. The congruence $2^h\equiv3^p\pmod{2^h-3^p}$ does not remove this separate ternary guard.

## A sparse-edit bound with a small source at the other end

Let $x_0,\ldots,x_p$ be a native reversed lap with $s\le x_i\le C_0s$ and all exponents $a_i\in\{1,2\}$. Consider a second positive ordinary inverse path $y_0,\ldots,y_p$ with exponents $e_i\ge1$ at the same indexed sites, and write $z=y_p$. The total clocks may differ. Let $m$ be the number of positions with $a_i\ne e_i$, and let $n$ count those with $e_i<a_i$.

A site at which $y_i\ne x_i$ can never subsequently equal the native site at the same index. Equality at a later site would give equality under the deterministic forward odd map at all earlier sites. Likewise, if both paths first differ in their edge exponent at index $i$, they have different next sites: the valuation of $3y_{i+1}+1$ uniquely recovers the edge. Let $N$ count the edges after the first different **site** (including edges starting at that differing site). Thus $N=p$ if $y_0\ne x_0$.

With $F=C_0\max(s,z)$ one has
$$
N\le m+(m+1)\frac{\log F+n\log2}{\log3}.\tag{3}
$$
For the real bound, put $R_i=y_i/x_i$, and set $c=1/(3x_{i+1})$. The two exact edges give
$$R_i=2^{a_i-e_i}\frac{R_{i+1}+c}{1+c},\qquad
\max(1,R_i)\le 2^{(a_i-e_i)_+}\max(1,R_{i+1}).$$
The negative defects save only one clock each. Iterating backwards gives $y_i\le C_0 2^n\max(s,z)=2^n F$ for every site, including sites before the first divergence. In any consecutive run of $l$ equal exponents starting at a differing site, the affine equation forces $3^l\mid y_i-x_i$. This is a nonzero integer of absolute value at most $2^nF$. There are at most $m+1$ such runs, interrupted by at most $m$ changed edges. Summing their upper bounds proves (3).

For the bounded candidate branch the earlier ordinary estimates give $s\le p^{O(1)}$ and a bounded $C_0$. Thus a complete transfer from a different terminal into a source $z\le p^A$ requires $m\gg_A\sqrt p$ as $p\to\infty$. If the changes only add clocks, then $n=0$ and $m\gg_A p/\log p$. More generally the same conclusions hold for an unmatched suffix with $N\gg p$. Edits confined to the far end after a long exact initial agreement need not satisfy a bound with $p$ in place of $N$. These assertions leave open dense changes and paths whose source is large, both of which the complete inverse basin permits.

[Physical divisibility and one-edge ratio kernels](NativeReset.lean) · [Prior bounded cycle and height hypotheses](../../astra-global-closure-20261124/round13/cycle/README.md)
