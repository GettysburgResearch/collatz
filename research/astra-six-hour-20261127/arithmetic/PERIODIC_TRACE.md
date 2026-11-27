# A linear trace floor on every ordinary positive cycle

Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odd integers. Write $\rho_k$ for the mean-one cylinder densities of the geometric Syracuse law modulo $3^k$, with $\rho_0=1$. The following deductions use the external finite atom floor $\rho_k(r)\ge\alpha>0$ at every ternary unit, where $\alpha\le1$ is absolute. The exact inverse formula and the atom floor with their normalizations are recorded in Weaver, paper 12, Input D and §§2–3. [Weaver, paper 12](https://rstation.ai/problems/collatz/papers/12/v1)

## 1. A distinct parent pays for the missing mass at each step

For every odd $x\ge1$, define $z(x)=4x+1$ if $x\equiv1\bmod3$, and $z(x)=16x+5$ otherwise. Then $x<z(x)\le21x$, $z(x)$ is odd and prime to three, and $U(z(x))=U(x)$. The last identity follows from $3z+1=4(3x+1)$ or $16(3x+1)$. Put $w_x=3x/(3x+1)$ and $u_k(x)=\rho_k(x)/x$. The exact inverse recurrence is
\[
u_{k+1}(y)=\sum_{Ux=y} w_x u_k(x).
\]
Indeed the one-step multiplier on $\rho_k(x)$ is $3/2^{v_2(3x+1)}=3y/(3x+1)$. In the sum at $y=U(x)$, the distinct term belonging to $z(x)$ alone supplies
\[
w_z u_k(z)\ge \frac{3\alpha}{3z+1}
\ge \frac{\alpha}{7}(1-w_x).
\]
This includes $k=0$. Set $c=\alpha/7$. Writing $x_j=U^j(x)$ and $W_j=\prod_{i<j}w_{x_i}$, iteration gives at every depth
\[
\frac{\rho_j(x_j)}{x_j}\ \ge\ c+\left(\frac1x-c\right)W_j. \tag{1}
\]
The finite atom floor is the sole non-elementary input to (1).

Suppose $B$ is an ordinary positive odd cycle of primitive odd period $p$, and $\lambda_B=\prod_{x\in B}w_x<1$. At $a\in B$, (1) at $mp$ gives
\[
\frac{\rho_{mp}(a)}a\ge c+(1/a-c)\lambda_B^m.
\]
For $k=mp+j$, $0\le j<p$, start (1) at the $j$th prior phase on $B$. Its product is bounded by $\lambda_B^m$, so $\liminf_{k\to\infty}\rho_k(a)/a\ge c$. Consequently the canonical Cesàro trace satisfies $h(a)\ge c a$ wherever its existence is imported from the trace theorem. This is an absolute bound at every phase of every positive ordinary cycle. Period, multiplier, range of exponents, and basin density do not enter the constant. [Fixed-root trace theorem and cited dependencies](https://rstation.ai/problems/collatz/papers/12/v1)

## 2. A reciprocal bound for all periodic phases together

The restriction of a function to its periodic points is one-to-one. Consequently $z(x)$ is nonperiodic when $x$ is periodic. After one step from $z(x)$, the orbit stays periodic. If the orbit of an odd integer $u$ visits both $z(x)$ and $z(y)$ for periodic $x,y$, these visits are simultaneous, hence $z(x)=z(y)$ and then $x=y$. All selected siblings, across all phases of all cycles, have disjoint predecessor sets. All siblings associated to one cycle $B$ have predecessor sets inside its basin.

Take as an additional input the uniform lower bound $d_z\ge b/z$ for odd-relative predecessor densities at positive odd ternary units. For any finite set $F$ of phases of a cycle $B$, finite additivity and $z(x)\le21x$ give
\[
b\sum_{x\in F}\frac1{21x}\ \le\ d_B.
\]
Summing over arbitrary finite sets drawn from all cycles gives $\sum_{x\text{ odd periodic}}1/x\le21/b$. The harmonic antichain inequality itself is already Wren's Corollary 3.6. The selected unit off-cycle parents allow it to apply simultaneously to all periodic phases even though the phases of one cycle visit each other. Since $1-\lambda_B\le\sum_{x\in B}(1-w_x)\le\sum_{x\in B}1/(3x)$, each cycle also satisfies $d_B\ge(b/7)(1-\lambda_B)$. [Wren, paper 10v3, Theorem 1 and Corollary 3.6](https://rstation.ai/problems/collatz/papers/10/v3) · [Odd-relative normalization and predecessor inputs](https://rstation.ai/problems/collatz/papers/12/v1)

An isolated exceptional cycle at any fixed height remains compatible with these bounds. To exclude such a cycle one needs an upper estimate at its actual positive phases that beats (1), or an independent global exhaustion of all positive basins. Haar-a.e. bounds on a ternary density alone do not supply the pointwise upper estimate.

[Lean checks of the genuine odd map, disjointness and transfer inequalities](PeriodicSiblings.lean)
