# Relative first landing from one native Collatz step

Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on the positive odd integers. For $r\ge1$ let $L_r(x)$ be the first odd state at or below $r$, with a cemetery value on failure, and include an immediate landing if $x\le r$. Extend it to even inputs by stripping their initial powers of two. For each $r$ there is a probability $\mu_r$ on these labels. If $W_Y$ is uniform odd in $[Y,2Y)$ and $v=\log(Y/r)\ge2$, then, uniformly for every $0\le g\le1$ on the entire label set,
\[
 \left|\mathbb E\,g(L_r(W_Y))-\mu_r(g)\right|
       \le C\,\mu_r(g)\,v^{-1/9}+C_B v^{-B}\qquad(B>0).            \tag{1}
\]
Both constants and the large-$v$ onset are independent of $Y,r,g$. The same bound holds on the all-positive octave for the odd-part extension. Set $g(\dagger)=0$ to omit failed landings. **Source-qualified status.** This is a written deduction from the one-trit signed physical-source estimate of PR 195, whose proof invokes Paper 48 exact-clock mixing. The other inputs for first landing are elementary short-trajectory counting and the two-logarithm lower bound of Bondareva, Luchin and Salikhov. For the general sparse-exception extension below, include the finite-quotient $L^p$ estimate, $1<p<2$.

For comparison, Leen's relative landing law as quoted in Weaver's Paper 12, (15), gives any relative exponent below $5/143$ and arbitrary additive log powers at $Y\ge r^{1.001}$ in terms of $\log r$. Here the scale in (1) is the logarithmic separation itself. The input is cancellation on short ordinary trajectories with a signed initial ternary digit, and the passage can have unlimited later duration. [PR 195, MARKED_FIBRES (3) and its physical-source proof, commit 3fa7ef4a](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/MARKED_FIBRES.md) · [Weaver–Wren, Paper 48 v1, §8, Theorem 6 (66)](https://rstation.ai/problems/collatz/papers/48/v1) · [Bondareva–Luchin–Salikhov (2018), Theorem 1, p. 18](https://www.mathnet.ru/eng/cheb619) · [Weaver, Paper 12 v1, §6, (15)](https://rstation.ai/problems/collatz/papers/12/v1).

More generally the label can take values in an arbitrary countable set and may be assigned arbitrarily at odd states at or below $r$. Require $L(x)=L(Ux)$ at odd $x>r$ outside an exceptional set $E$ with
\[
 \#(E\cap[Z,2Z))\le C_A Z\,\langle\log(Z/r)\rangle^{-A}
                      \quad(Z\ge r,\ A>0),                           \tag{2}
\]
where $\langle v\rangle=1+|v|$. All estimates then depend on the indicated exception bounds but are uniform over the labels with those same bounds.

## Cancellation on a high source interval

For any fixed compact interval $S\subset(0,\infty)$, $\varphi\in C_c^1(S)$, and mean-zero $\psi$ on $\mathbb Z/3$ with $|\psi|\le1$,
\[
 \left\|Y^{-1}\sum_{x\ge1}\varphi(x/Y)\psi(x\bmod3)\delta_{L(x)}
                  \right\|_{\ell^1}\le C_{A,S}\|\varphi\|_{C^1}
                                          \langle v\rangle^{-A}.     \tag{3}
\]
Here $x$ runs through all positive integers and all labels remain in the same vector. To verify it first take odd $x$ in an arbitrary subinterval of an octave $[Z,2Z]$ at source scale $Z/r\ge c_S e^{v/2}$. Choose $t=\lfloor c v\rfloor$ with a small fixed $c>0$, so $t\le(\log_2 Z)/32$ and $Z2^{-4t}\ge r e^{v/3}$ at large $v$. The signed source input bounds the sum norm after $t$ physical odd steps, retaining the actual endpoint and total and weighting by $f_t(x)/x$, by $O_A(t^{-A})$. Its binary-cylinder tail $S_t>4t$ has unsigned reciprocal mass $O(e^{-c't}+2^{4t}/Z)$. On the good complement all intermediate states exceed $Z2^{-4t}$, and $1-f_t(x)\le Ct/(Z2^{-4t})$. For the landing label the forward labels are then identical through the whole short segment. Sending the endpoint to its label contracts the sum norm. This proves the bound for the mass $\psi(x)\delta_{L(x)}/x$ on every such odd subinterval.

With exceptional states as in (2), discarding good-total trajectories that visit $E$ costs $O_A(v^{-A})$. At each $i<t$ a visited state $y$ is between $Z2^{-4t}$ and $2^{t+1}Z$, spanning $O(1+t)$ dyadic octaves. All have bottom height $Z'\gg r e^{v/3}$ and $3^i\le Z'$ after decreasing $c$. Count each compatible ordinary word at its actual endpoint, using $1/x\le2\cdot3^i2^{-S_i}/y$ on these good trajectories. Summing over words and then $y\in E$ is bounded on each octave by $C_p(\#(E\cap[Z',2Z'))/Z')^{1-1/p}$. This is Hölder applied to the complete-period $L^p$ estimate for $\rho_i$. Choosing an arbitrarily large power in (2) covers all $O((1+t)^2)$ times and bands. [Finite-quotient count, equation (3)](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md).

Partial summation with $x\varphi(x/Z)/Z$ converts the odd-interval signed bound to the corresponding normalized smooth source estimate, costing $C_S\|\varphi\|_{C^1}$. For all positive inputs split $x=2^e u$ with $u$ odd. When $2^e\le e^{v/3}$ the odd source scale $Y/2^e$ is sufficiently high, the residue function $\psi(2^e u)$ still has mean zero, and the normalization gains $2^{-e}$. The other inputs have normalized mass $O_S(e^{-v/3}+Y^{-1})$ since they are divisible by a common power of two of size at least $e^{v/3}$. Summing proves (3). The same argument proves its unweighted subinterval version.

## The renewal equation on logarithmic size

For $u\in\mathbb R$ put
\[
 F_\varphi(u)=e^{-u}\sum_{x\ge1}\varphi(xe^{-u})\delta_{L(x)}.
\]
All values and estimates are in $\ell^1$ of the countable label set. Even inputs contribute $\frac12 F_\varphi(u-\log2)$ exactly. On the odd inputs set $y=(3x+1)/2$. This is a bijection to $y=2\bmod3$ among the positive integers. For large $v=u-\log r$ the labels at $x$ and $y$ agree except at the odd exceptional starts (2). Replacing $\varphi((2y-1)/(3e^u))$ by $\varphi(2y/(3e^u))$ costs $O_S(\|\varphi'\|_\infty e^{-u})$ after normalization. Equation (3) at scale $3e^u/2$, with $\psi=1_{2\bmod3}-1/3$, gives
\[
 F_\varphi(u)=\tfrac12F_\varphi(u-\log2)
              +\tfrac12F_\varphi(u+\log(3/2))
              +O_{A,S}\big(\|\varphi\|_{C^1}\langle v\rangle^{-A}\big).
                                                                         \tag{4}
\]
The constants include (2) if used. The coefficient of the second term is $(3/2)/3$.

Take $\varphi$ smooth, fix a smooth cutoff $\chi$ vanishing for $v\le0$ and equal to one for $v\ge2$, and let $f(v)=\chi(v)F_\varphi(\log r+v)$. Define $g_0=f-Pf$ using the two translations and their weights in (4). This cutoff removes all dependence on uncontrolled behavior far below $r$. Because $\partial_u^j F_\varphi=F_{(-1-t\partial_t)^j\varphi}$, every derivative obeys
\[
   \|g_0^{(j)}(v)\|_1\le C_{A,j,S}\|\varphi\|_{C^{j+1}}
                                   \langle v\rangle^{-A}.            \tag{5}
\]
For $v$ sufficiently negative all terms vanish. On the bounded transition interval use the elementary sum on the compact support and $r\ge1$; where $v$ is large use (4) on the differentiated weight. The constants are uniform in $r,L$ subject to (2).

## Dividing the Fourier multiplier

With Fourier convention $\widehat f(\xi)=\int e^{-i\xi v}f(v)\,dv$, the multiplier of $1-P$ is
\[
          d(\xi)=1-\tfrac12e^{-i\xi\log2}-\tfrac12e^{i\xi\log(3/2)}.
\]
Its only real zero is zero, and that zero is simple since the mean translation is $-\tfrac12\log(4/3)\ne0$. For $|\xi|\ge1$ we have
\[
                         |d(\xi)|\ge c(1+|\xi|)^{-8.5}.             \tag{6}
\]
Indeed the real part bounds below a constant times the sum of squares of the distances of $\xi\log2$ and $\xi\log(3/2)$ from $2\pi\mathbb Z$. If both are close, nearest integer multiples give a nonzero integer two-logarithm linear form with coefficients $O(1+|\xi|)$ and magnitude bounded by a constant times the larger distance. Explicitly, if $m,n$ are nearest integers to $\xi\log2/(2\pi),\xi\log(3/2)/(2\pi)$, use $m\log(3/2)-n\log2$. For large $|\xi|$ they are not both zero, and $\log2,\log(3/2)$ are linearly independent over $\mathbb Q$. Theorem 1 of Bondareva–Luchin–Salikhov bounds $|h_1\log2+h_2\log3+h|$ below by $H^{-4.116201}$ for integer coefficients and sufficiently large $H=\max(|h_1|,|h_2|)$. Set $(h_1,h_2,h)=(-m-n,m,0)$ and weaken the resulting exponent to $4.25$. This gives the required lower bound $c(1+|\xi|)^{-4.25}$ on the linear form. The compact remainder follows from absence of zeros. [Bondareva–Luchin–Salikhov, Theorem 1, p. 18](https://www.mathnet.ru/eng/cheb619).

Set $b(\xi)=i\xi/d(\xi)$ with its removable value at zero. Since all positive derivatives of $d$ are bounded, at each order $l$,
\[
                 |b^{(l)}(\xi)|\le C_l(1+|\xi|)^{8.5(l+1)+1}.
\]
Consequently $b\widehat g_0$ is Schwartz by (5). In tempered distributions the Fourier transform of $f'$ differs from $b\widehat g_0$ by a distribution annihilated by $d$. Such a distribution is supported at its unique simple zero, so is a multiple of $\delta_0$. After inverse transformation the resulting constant is zero, by sending $v\to-\infty$ where $f'=0$. These steps can be taken after scalar testing by any $\ell^\infty$ function of norm at most one; all ensuing estimates are uniform in this test.

More quantitatively, for each positive integer $j$,
\[
    \|F_\varphi(\log r+v)-\Lambda_r(\varphi)\|_1
       \le C_{j,S}\|\varphi\|_{C^{k_j}}\langle v\rangle^{-j}
                  \quad(v\ge2),\qquad k_j=\lceil8.5(j+2)+6\rceil . \tag{7}
\]
To see the derivative count, take $j+1$ frequency derivatives of $b\widehat g_0$. For the derivative of order $l\le j+1$ on $b$, integrate by parts $k_j-1$ times in the Fourier transform of $v^{j+1-l}g_0(v)$ at high frequencies. Formula (5) with sufficiently large moment weights bounds its resulting $L^1$ derivatives by $C_{j,S}\|\varphi\|_{C^{k_j}}$. The frequency integral converges absolutely since $k_j-1>8.5(j+2)+3$. Fourier inversion gives $\|f'(v)\|_1\le C_{j,S}\|\varphi\|_{C^{k_j}}\langle v\rangle^{-j-1}$. Integration gives the norm limit $\Lambda_r(\varphi)$ and (7).

The limit is shape-independent after normalization. It is a positive linear functional in $\varphi$ with values in $\ell^1$, bounded in norm by $\int|\varphi(t)|dt$ by the Riemann-sum bound. Replacing $\varphi(t)$ by $\varphi(ct)$ gives $\Lambda_r(\varphi(c\,\cdot))=c^{-1}\Lambda_r(\varphi)$ for each $c>0$ by changing $u$. For each label event its bounded scalar $L^1(dt)$ functional therefore has a dilation-invariant $L^\infty(dt)$ density, constant almost everywhere. For example, pass to $t=e^w$, where invariance under a countable dense subgroup of translations implies a constant after smoothing and then passing to Lebesgue points. Choose a nonnegative smooth shape of integral one to define $\mu_r=\Lambda_r(\varphi)$. Its masses sum to one by $\ell^1$ convergence and the ordinary scalar Riemann sum. Thus $\Lambda_r(\varphi)=\mu_r\int\varphi$ for every smooth shape.

## Recovering the actual octave

Sandwich $1_{[1,2)}$ by nonnegative smooth functions $\varphi_\eta^\pm$ supported in $[1/2,3]$, of integrals $1+O(\eta)$ and $C^k$ norms $O_k(\eta^{-k})$, by smoothing slightly enlarged or reduced intervals. At $v\ge2$ choose $\eta$ comparable to $v^{-1/9}$ and at most $1/8$. In (7), $v^{-j}\eta^{-k_j}=O_j(v^{-j(1-8.5/9)+O(1)})$, an arbitrarily large negative power after choosing $j$. Sandwiching any positive test $g\le1$ gives the all-positive form of (1); normalizing by the exact population $Y+O(1)$ makes an exponentially small change in $v$. This also proves the stronger every-order convergence in $\ell^1$ for each fixed smooth octave shape of integral one.

For an odd uniform octave, subtract the even terms before normalizing. Their normalized expectation is one half of the all-positive one at $Y/2$, up to $O(1/Y)$, since $L(2u)=L(u)$. Both all-positive estimates use the same $\mu_r$, and $\log(Y/(2r))=v-\log2$. Positivity of the original test bounds the combined relative term by an absolute constant times $\mu_r(g)v^{-1/9}$. This proves (1). Uniformity for $Y\ge r^{1.001}$ follows by $v\ge0.001\log r$. The same result identifies the natural label law through a growing bound by octave decomposition, and identifies its logarithmic law by partial summation.
