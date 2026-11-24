# Close, convergent ordinary sources with incompatible series values

**PROPOSED written theorem.** Write $S(n)=\sum_{j\ge0}A_j(n)$ as a nonnegative extended-real sum on ordinary integers. Two obstacles to local upper estimates already occur on ordinary numbers that reach one.

## Almost equal sizes in the same congruence class, along one physical segment

Given a modulus $M\ge1$, a number $\epsilon>0$, a factor $F>0$ and a floor $B$, there are positive integers $x>y>B$ such that both reach one,
\[
 x\equiv y\equiv-1\bmod M,\qquad
 1<x/y<1+\epsilon,\qquad
 T^k x=y,\qquad A_k(x)>F.
\]
Consequently every everywhere-finite nonnegative supersolution $U(n)\ge1+c(n)U(Tn)$, with $c(n)=2/3$ on evens and $4/3$ on odds, satisfies $U(x)>F U(y)$. This is already forced on the physical basin of one.

Let $L$ be a common multiple of the orders of 2 modulo the odd prime powers dividing $M$ and of 3 modulo its prime powers coprime to six. Empty lists use $L=1$. Choose $p,k\equiv1\bmod L$ with $p,k\to\infty$ and $k-p\log_2 3\to0$ from above, using irrational rotation after writing $p=1+Lj$. Eventually $k>p$. Put
\[
 r=\frac{3^p-2^p}{2^k-3^p}.
\]
Its denominator is odd and coprime to three, and it is $-1$ modulo every prime power of $M$ coprime to six. Thus the denominator is a unit modulo $3^p M$. Also $r+1=2^p(2^{k-p}-1)/(2^k-3^p)$, so $r\equiv-1\bmod M$ for sufficiently large $p$. The one-lap word $w=1^p0^{k-p}$ has forward affine map $T_w(z)=(3^p z+3^p-2^p)/2^k$ on its binary class, and $r$ is its fixed point. Its biased weight is $\beta=(2/3)^k2^p$. Since $k/p\to\log_2 3<8/5$ and $2^{13}>3^8$, $\beta$ tends to infinity. Also $2^k/3^p\to1$ from above.

For the chosen $p,k$ take an arbitrarily high ordinary $y\equiv r\bmod3^p M$ that reaches one. Existence uses K. M. Monks, 'The sufficiency of arithmetic progressions for the $3x+1$ conjecture', Proc. Amer. Math. Soc. 134 (2006), Theorem 1.1, which applies to every translated arithmetic progression of positive common difference. Apply sufficiency to the source 1 and translate the initial member of the progression beyond $\max(B,r)$. A start meeting the forward orbit of 1 reaches 1. [Author's paper, pp. 1–2](https://monks.scranton.edu/content/pubs/SufficiencyRev4.pdf)

Set $x=r+(2^k/3^p)(y-r)$. Equivalently $x=(2^k y-3^p+2^p)/3^p$; it is integral, positive, congruent to $r\bmod M$, and $x+1=2^p(2^{k-p}y+1)/3^p$ has exact binary valuation $p$. The first $p$ odd branches send it to $2^{k-p}y$, then $k-p$ halvings reach $y$. Finally $1<x/y<2^k/3^p$. Finite iteration of the supersolution inequality proves the stated ratio. It excludes fixed-modulus bounds on $U(x)/U(y)$ in sufficiently narrow multiplicative intervals. Arbitrary irregular supersolutions remain possible.

## A unit additive gap and the exact series on its known basin

There are arbitrarily large consecutive integers $n,n+1$ both reaching one, with $S(n)\to\infty$ and $S(n+1)\to3$. The number 3 is the global infimum, since $A_j\ge(2/3)^j$ and $S(2^u)=3+18(2/3)^u$.

Fix $k\ge1$ and write $n=2^k t-1$. At the common clock $k$, the two physical arms have states $3^k t-1$ and $t$. The first arm has seen $k$ consecutive odd inputs and the second $k$ consecutive even inputs. We will choose an ordinary $t$ so that the first arm also reaches one, and $S(t)$ is bounded by an absolute constant, independent of $k$.

Expose fair binary digits of a parameter $t$ in $\mathbb Z_2$. Its own shortcut parities are independent fair bits by the finite parity-word bijection modulo $2^j$. Thus
\[
 \mathbb E\left[\sum_{j\ge0}\sqrt{A_j(t)}\right]=\frac1{1-\rho},
 \quad \rho=\tfrac12\big(\sqrt{2/3}+\sqrt{4/3}\big)<1 .
\]
There is probability at least $1/2$ that $\sum A_j(t)\le C=4/(1-\rho)^2$, by Markov's inequality and $\sum A_j\le(\sum\sqrt{A_j})^2$. The terms tend to zero on this event.

For each fixed $k$, the two affine arms $(t,3^k t-1)$ almost surely reach a common **affine profile** at a finite common clock in this same filtration. This is a source-qualified use of GettysburgResearch/collatz, PR146 at `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md`, (1) and its proof on the oriented states (the absorbing state $(0,0)$ means exact affine equality on the cell). Apply it with $s=k,d=-1$, keeping $k$ fixed while the horizon tends to infinity. No independence between the arms is assumed. [Pinned proof](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md)

There is consequently a finite binary parameter prefix of some length $H$ on which the arms have merged, $\sum_{j<H} A_j(t)\le C$, and $A_H(t)\le1$. Indeed choose one realization in the intersection, and wait until after its merger and term decay. On its lifts the common endpoint is $z_0+3^q v$, where $q$ counts the odd steps of $t$ through $H$. If $q>0$, $z_0$ is a unit modulo three by the last odd step and subsequent halvings. Choose arbitrarily large $u$ with $2^u=z_0\bmod3^q$, possible because two generates the units modulo each power of three. For $q=0$ there is no congruence. The corresponding lift gives a positive ordinary $t$ and common endpoint $2^u$. Both arms now reach one, and
\[
 S(t)=\sum_{j<H}A_j(t)+A_H(t)S(2^u)\le C+21.
\]
Thus $S(n)\ge(4/3)^k$, and $3\le S(n+1)=3+(2/3)^k(S(t)-3)\le3+(2/3)^k(C+18)$. This assertion concerns the actual minimal series. It does not require an arbitrary supersolution to be small at this neighbor, because a supersolution can overestimate either source.
