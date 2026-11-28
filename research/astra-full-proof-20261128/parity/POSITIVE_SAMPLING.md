# Positive sampling of a Haar-contracting inverse transfer

This calculation tests whether the sign of the ordinary source can be extracted by a positive majorant whose poles begin at the negative fixed point. It gives an exact identity and a pointwise convergence result. The estimates obtained here do not control the ordinary global sum.

On the 3-adic integers put
\[
  L_s f(y)=a f(2y)+b\,1_{y=2\bmod3} f((2y-1)/3),
  \quad a=2^{-s},\quad b=(3/2)^s,\quad 1<s<2.
\]
Normalized Haar integration multiplies by $a+b/3<1$. Indeed $1+3^{s-1}<2^s$ on $1<s<2$ by strict concavity of $x^{s-1}$ at $x=1,3$. For $b/(1-a)<B<3$ and $\Lambda\ge1$ with $\rho=\Lambda(a+b/B)<1$, the following pole expansion is available.

## Exact transport of negative poles

For a dyadic rational $z$, let $p_z(y)=B^{v_3(y-z)}$, with infinite value at $y=z$. Let $F_0z=z/2$ and $F_1z=(3z+1)/2$, now applied without a parity restriction. Then
\[
  a p_{F_0z}(y)+(b/B)p_{F_1z}(y)
  =L_s p_z(y)+(b/B)\,1_{y\ne2\bmod3}.                    \tag{1}
\]
The even term agrees since 2 is a 3-adic unit. At $y=2\bmod3$, taking the inverse odd branch lowers the valuation by one. At the other two trits, $p_{F_1z}=1$. This proves (1) pointwise in the extended nonnegative reals.

Start the poles at $-1$. For every binary word $w$ let $z_w=F_{w_t}\cdots F_{w_1}(-1)$ and give it weight $\alpha_w=(\Lambda a)^{t-q}(\Lambda b/B)^q$, $q=|w|$. Let $\Psi_N(y)$ be the sum of $\alpha_w p_{z_w}(y)$ over all words of lengths $0,\ldots,N$. Writing $J=1_{y\ne2\bmod3}$ and $Z_j=\sum_{i=0}^j\rho^i$, (1) gives
\[
 \Psi_N=p_{-1}+\Lambda L_s\Psi_{N-1}+(\Lambda b/B)Z_{N-1}J .
\]
Consequently, as an equality of extended nonnegative functions,
\[
 \Psi=\lim_N\Psi_N
     =\sum_{j\ge0}(\Lambda L_s)^j\left(p_{-1}
        +\frac{\Lambda b}{B(1-\rho)}J\right).              \tag{2}
\]
To see the equality, iterate the finite identity first. For each fixed depth $j$ the forcing coefficient tends monotonically to the indicated limit. Every $p_{z_w}$ has the same finite Haar integral, $2/(3-B)$, and the sum of weights is $1/(1-\rho)$. Thus $\Psi$ is Haar integrable.

No $z_w$ is a positive integer. Initial odd letters fix $-1$. The first even letter changes the denominator in reduced form to 2. Thereafter if $z=u/2^j$ with odd $u$ and $j\ge1$, both $F_0z,F_1z$ have denominator $2^{j+1}$ in reduced form. All individual terms are therefore finite on the positive integers. This alone establishes no bound for their sum at a positive integer.

## The diagonal selected by ordinary sources

Write $F_w(x)=(3^q x+c_w)/2^t$. For $y>0$, a reverse path following $w$ is legal over the integers iff $3^q\mid 2^t y-c_w$. This follows by peeling the last letter. The last odd letter requires $2y-1\equiv0\bmod3$, and the remaining power-of-three divisibility is exactly that for the prefix. The even letter removes no factor of three. When the path is legal its unique initial integer $x$ is positive, since the integer inverse branches preserve positivity. Since
\[
  y-z_w=3^q(x+1)/2^t,
\]
the condition is precisely $v_3(y-z_w)\ge q$. The contribution of this pole to $\Psi$ is then
\[
  \alpha_w p_{z_w}(y)
      =\Lambda^t (3^q/2^t)^s B^{v_3(x+1)}.               \tag{3}
\]
In particular the terms with unusually close negative-pole images retain the full physical positive inverse graph. No sign cancellation is available in (3).

Put $A_w=3^q/2^t$. Along the true positive forward path from $x$ to $y$,
\[
    y/x=A_w\prod_{i\ \mathrm{odd}}(1+1/(3T^ix))\ \ge A_w. \tag{4}
\]
For a nonperiodic fixed $y$, every positive $x$ can arrive at $y$ at most once. Summing (4) over all arrival times gives the unconditional bounds at $\Lambda=1$
\[
 \sum_{j\ge0}L_s^j1(y)\le y^s\zeta(s),\qquad
 \Psi(y)\le y^s\sum_{x\ge1}\frac{B^{v_3(x+1)}+b/[B(1-\rho)]}{x^s}<\infty. \tag{5}
\]
For the Dirichlet sum, the integers $x$ with $3^r\mid x+1$ are $3^r\ell-1$. For $r\ge1$ their inverse-$s$ sum is at most $(3/2)^s3^{-rs}\zeta(s)$. Summing over valuations converges because $B<3<3^s$. For a periodic $y$, partition by first arrival and repeat a lap. The extra geometric factor is $1/(1-A_{\rm lap}^s)$, finite by (4) since the positive lap contains an odd state. Thus even pointwise finiteness at **every** positive integer, with the strict Haar gap, holds regardless of the existence of escape.

The global height-weighted sum $\sum_{y\ge1}y^{-s}\Psi(y)$ is a different demand. With $\Lambda>1$, a single unbounded forward orbit forces divergence. Its distinct positive states $x_i=T^i(x)$ go to infinity, so $\sum_{i<t}1/x_i=o(t)$. Equation (4) then gives a weight at its $t$th endpoint of at least $x^{-s}\Lambda^t\exp[-o(t)]$. The same global bound would restrict any cycle of length $l$ and least value $d$ by $\log\Lambda<s\log(1+1/(3d))\le s/(3d)$, since otherwise the corresponding lap alone gives infinite mass. At $s=3/2,\Lambda=1.01,B=2.99$ one has $\rho<1$; the cycle restriction would give $d<51$, already covered by the finite base. This tilted bound is stronger than universal convergence. If it holds with a fixed $\Lambda>1$ and the cycle restriction above, then the term for the first arrival of $x$ at 1 is proportional to $x^{-s}\Lambda^{\tau_1(x)} f_{\tau_1(x)}(x)^s$, where $f_t(x)=A_w x/T^t(x)$. The sum of these terms over positive $x$ is finite. Using the uniform reciprocal packing for distinct positive orbit values gives $f_{\tau_1(x)}(x)\ge c_s>0$ before first arrival. The single term for each $x$ then gives $\tau_1(x)=O(\log(2x))$ uniformly. Thus even after eliminating extra cycles the proposed global bound demands exponential time control. [Uniform reciprocal packing and simple-arrival product](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/escape/phase4/HARMONIC_SOURCE_PHASE.md)

We found no proof of the global bound. The calculation isolates the ordinary positive diagonal that a Haar argument would need to estimate.

The cutoff, probability and signed Fourier pairing for the separate native-clock target are in [README.md](README.md). These transfer calculations are written mathematics and do not have a Lean certificate.
