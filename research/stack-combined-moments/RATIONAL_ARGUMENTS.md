# Few rational-value orbits at every period

**PROPOSED.** Fix an arbitrary positive periodic native increment word of length $r$ and sum $S$. Use initial height zero to define the series
$$
F(Y)=\sum_{j\ge0}T^{E_j}Y^j,\qquad T=64/81,\quad Q=T^{9S}.
$$
In $\mathbb Q_2$, the set of $z\in\mathbb Q^\times$ with $F(z)\in\mathbb Q$ is a union of at most $\lfloor11r/6467\rfloor$ multiplicative orbits $zQ^{\mathbb Z}$. In particular for **every** period at most $\lfloor11r/6467\rfloor$ of the $S$ initial-height classes modulo $S$ have rational native values. The fraction of such classes is at most $11r/(6467S)\le11/6467$. Through period 587 there are none, and through period 1175 there is at most one. This includes negative rational arguments for $F$.

We use the determinantal bound and nonzero scalar shift residual in the [period-587 proof](https://github.com/gfreund123/collatz/blob/52b98238146d1784fa8aef378cbc9f7ed762dd51/research/stack-shift-residual/PROOF.md), and their arbitrary row-center estimates in [the parameter calculation](PARAMETER_CEILING.md). We give the specialization and counting details since the auxiliary polynomials must be independent of the exceptional arguments.

Let $a=9S/r$, $d=1033/1000$, $\theta=47/100$, $D=M=dn$ and $\mu=M+\theta n$, with $n$ a multiple of 1000. Take one nonzero $V(Y)=\sum_{k=0}^D c_kT^{g_k}Y^k$, $g_k=\lfloor a(\mu k-k^2/2)\rfloor$, and $U=[VF]_{<M}$ by the cited construction. The formal residual $VF-U$ has order at least $M+n$ and $\log_{81}\max |c_k|\le an^2(h+o(1))$ for $h=(d/4-1/12)/(d-1)+(\theta-1/2)^2$. These polynomials depend on the increment word and $n$ only.

Fix $z\in\mathbb Q^\times$ with $\xi_z=F(z)\in\mathbb Q$. For $s\ge0$ a multiple of $r$ write $P_s(Y)=\sum_{j<s}T^{E_j}Y^j$, $y=zT^{as}$. The formal shift identity gives
$$
\xi_z=P_s(z)+T^{E_s}z^sF(y).
$$
On the window $6921/1000\le s/n\le26322/1000$, the rational identity
$$
(\xi_z-P_s(z))V(y)=T^{E_s}z^sU(y)
$$
is forced exactly as for $z=1$. On the rational side the powers of $z$ have exponents between zero and $s+M+D$, so their denominators and real absolute values incur only $O_z(n)$ in logarithmic height. In the 2-adic tail at degree $j\ge M+n$, the factor $z^{s+j}$ changes the valuation by $O_z(s+j)$, absorbed in the linear error of the lower quadratic bound, which is increasing on that whole range for large $n$. The fixed denominator of $\xi_z$ incurs a constant at both places. Thus the same leading margin applies. With $t=s/n+d$ and $\rho=\log_{81}64$, it equals
$$
-(1-\rho)t^2/2+\rho t+\rho/2-(\rho+(1-\rho)\theta)d-h.
$$
It is concave in $t$ and increasing in $\rho$ on the stated window. Substitution of the lower bound $9463946/10^7$ for $\rho$ gives endpoint margins $1874534921/30937500000000$ and $81394567343/198000000000000$, both positive. For any fixed finite list of $z$ take the largest of their thresholds.

The common polynomial
$$
R=U(Y)V(QY)-P_r(Y)V(Y)V(QY)-T^{E_r}Y^rV(Y)U(QY)
$$
is nonzero, divisible by $Y^{M+n}$, and has degree at most $2D+r-1$, by the cited scalar shift argument. Each adjacent forced pair at $s,s+r$ gives $R(zT^{as})=0$ using $V(y)F(y)=U(y)$ even if $V(y)=0$. Each orbit of a rational seed therefore gives at least $(19401/1000)n/r-O(1)$ distinct nonzero roots. Two seeds in distinct $Q^{\mathbb Z}$-orbits give disjoint roots. For any finite list of $b$ inequivalent seeds the polynomial degree yields
$$
b\,(19401/1000)n/r-O_b(1)\le D-n+r-1.
$$
Letting $n$ tend to infinity gives $b\le 33r/19401=11r/6467$. Rationality is invariant in both directions along each orbit by the affine shift equation since $z\ne0$. Finally the native value at height $m$ is $F(T^{9m})$, and these arguments are equivalent precisely when their heights are congruent modulo $S$.

The theorem bounds the number of possible exceptional classes for each fixed word. When the bound is positive it does not identify their representatives.
