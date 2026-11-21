# Sparse failures on the five-ray

**PROPOSED, unconditional.** For the positive shortcut map $T$, write $f(n)$ for the merger component of $n$. Thus $f(n)=f(m)$ means that their orbits have a common value at two possibly different finite clocks. Let
$$
 \mathcal B=\{t\ge1:f(5t+1)\ne f(t)\},\qquad B(X)=|\mathcal B\cap[1,X]|.
$$

**Theorem.** If the Collatz conjecture is false, then for all large $X$,
$$
 B(X)\ \ge\ \log_2 X-O(1).
$$
Consequently eventual validity of $t\sim5t+1$, or even $\liminf_{X\to\infty} B(X)/\log_2 X<1$, is equivalent to the full conjecture. A still weaker equivalent condition is that $B(X)-\log_2 X$ be unbounded below. In the other direction full convergence gives $B(X)=0$ identically. Lean verifies the equivalence with eventual merger in `collatz_iff_eventual_five_ray`. The quantitative lower bound is a written proof about permanent failures at unrestricted clocks. [Formal source](HighBit.lean) · [All-parameter five-ray criterion](AFFINE_RAYS.md)

A further written argument proves $B(X)/\log X\to\infty$ if a counterexample exists. Its proof also gives an equivalent single family with compatible slopes. [Multiplication by three and removal of the remaining exceptions](THREE_RAY.md)

## Lifting a failed multiplication by three

Always $f(2x)=f(x)$. There is an exact two-step identity $T^2(4u+1)=3u+1$. Suppose $f(3x)\ne f(x)$ for some $x$. For each integer $a\ge2$ at least one of
$$
 t_1=2^a x,\qquad t_2=3\cdot2^{a-2}x
$$
is in $\mathcal B$. Indeed $T^2(5t_1+1)=5t_2+1$, whereas $f(t_1)=f(x)$ and $f(t_2)=f(3x)$. All these pairs are disjoint by unique factorization. Each pair with $2^a x\le X$ contributes a distinct failure. This gives $B(X)\ge\lfloor\log_2(X/x)\rfloor-1$.

## A two-parameter obstruction for multiplication by five

Now assume $f(3x)=f(x)$ for every $x$. If $f(5x)\ne f(x)$ anywhere, stripping factors of two gives an odd witness $x$. For all $i,j\ge0$ with $i+j\ge1$, put $t=4^i3^j x$. Then $f(t)=f(x)$ and
$$
 T^{2i}(5t+1)=5\cdot3^{i+j}x+1.
$$
The right side is $3z+1$ for the odd integer $z=5\cdot3^{i+j-1}x$, so its component equals $f(z)=f(5x)$. Thus all these $t$ are bad. They are distinct and give $B(X)\gg_x (\log X)^2$. For instance, independently restrict $i\le\log(X/x)/(2\log4)$ and $j\le\log(X/x)/(2\log3)$.

## Propagating a one-unit gap

Assume now $f(2x)=f(3x)=f(5x)=f(x)$ on all positive integers. Write $g(y)=f(y-1)$ for integers $y\ge2$. Two exact ordinary paths give
$$
 g(2h)=g(3h),\qquad g(8h)=g(9h)\qquad(h\ge1).
$$
The first is $T(2h-1)=3h-1$. For the second, the odd input $3(8h-1)$ has shortcut image $4(9h-1)$, and the multipliers 3 and 4 preserve the component.

In particular $g(4h)=g(6h)=g(9h)=g(8h)$. Iterating the resulting doubling relation, and exchanging factors 2 and 3 one at a time with the first identity, gives
$$
 g(2^i3^j h)=g(4h)\qquad(i,j\ge0,\ i+j\ge2).
$$
Suppose $5\nmid h$ and $f(4h-1)\ne f(4h)$. For every such $i,j$ with $y=2^i3^j h\equiv1\pmod5$, $y>1$, the positive parameter $t=(y-1)/5$ then satisfies
$$
 f(t)=f(y-1)=g(4h)\ne f(4h)=f(y)=f(5t+1).
$$
These parameters are distinct. One may take $j\equiv0\pmod4$ and $i$ in the single residue class modulo four with $2^ih\equiv1\pmod5$. Independent ranges $2^i,3^j\le\sqrt{X/h}$ give $B(X)\gg_h (\log X)^2$ for large $X$.

## Descent once the obstructions are absent

In the remaining case $f(4h-1)=f(4h)$ for every $h$ prime to five. Strong induction proves full convergence. Even starts halve. Odd $n>1$ with $n\equiv1\pmod4$ reach $(3n+1)/4<n$ in two steps. If $n\equiv3\pmod4$ and $5\nmid n+1$, apply the gap equality at $4h=n+1$ to get $f(n)=f((n+1)/4)$. Finally, if $5\mid n+1$, apply it at $4h=4n$. Now $f(n)=f(4n-1)=f((4n-1)/5)$, with integral positive argument strictly below $n$. A start in the component of 1 reaches 1 because $1$ and $2$ alternate. This exhausts the cases and proves the theorem.

If there is a second component, some fixed $x$ or $h$ in the three displays above forces an unbounded family of failures. Under the two exact multiplication invariances, the remaining family has two independent exponents and an explicitly fixed pair of residue classes modulo four. Establishing sufficiently many actual successful meetings remains open.


The counting condition also has a finite-certificate formulation. At a chosen scale $X$, exhibit a pair of finite orbit prefixes with a common endpoint for every parameter up to $X$ except for at most $U(X)$ parameters. This establishes $B(X)\le U(X)$ without deciding whether the remaining pairs ever meet. A sequence of such certificates with $U(X)-\log_2 X$ unbounded below would suffice for full Collatz. Conversely, if all starts reach 1, at each finite scale the largest of their finitely many hitting times supplies such a certificate with $U(X)=0$. No sequence achieving the required bound has been constructed here.
