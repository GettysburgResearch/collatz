# PR 193 at the live-readback checkpoint

**Source.** PR 193, commit `52beff703fd3ce798c430e5af8199eb58d41bf93`, repository `GettysburgResearch/collatz`. All paths in the table start with `research/astra-universal-descent-20261124/`.

| Claim or source | Path | Exact Git blob | Narrow verdict |
|---|---|---|---|
| S1, guarded ordinary partner | shadow.md | 877caaccb0434fc13f98e86bb88fb4a07184becd | VERIFIED by reconstruction |
| §§1a–1b, finite synchronization in all translated intervals | escape.md | 1fbb615119e9d12f32dc2f33c333fafd65fd0938 | VERIFIED as a written theorem |
| C5.1, exact collision inequality on the complete denominator | cycles.md | 0a422b8d570660fe61edbed052163537f2b3e401 | VERIFIED as a written necessary condition |
| Scientific summary | README.md | cf177d43be1e622e66b3f31ed420f897cad5d155 | Qualify the scope of “every prescribed finite-clock obstruction class” as below |
| S1 Lean source | ShadowCore.lean | 67448fc4e63a1da06d6bd9d3b9c9e4f243b480fd | Source-pinned, no independent compiler replay here |
| Synchronization finite core | EscapeCore.lean | 8285420f9f5e731e79cc1b98739bc883ea7896a1 | Source-pinned, no independent compiler replay here |

## S1 and the guard's exact reach

Write $n=3^h u$, with $u$ positive odd, $d=h+4$, $3^d z=1+2\cdot4^h u$, and $m=2^{d+1}z-1$. The first $d$ shortcut steps from $m$ are odd, ending at $2\cdot3^d z-1=1+4^{h+1}u$. The physical pair odd/even sends $1+4v$ to $1+3v$, so $h+1$ pairs end at $1+3^{h+1}u=3n+1$. One halving reaches $T(n)$. The elapsed time is $d+2(h+1)+1=3h+7$. Positivity of $z$ gives $m>0$. As a function of $n$, its slope is $(64/81)(8/9)^h<1$ and the intercept is $2^{h+5}/3^{h+4}-1<0$. This gives an actual smaller partner without a convergence assumption.

The guard selects one unit class for $u$ modulo $3^{h+4}$. Simultaneously imposing any desired dyadic prefix by CRT is valid. In particular, choosing $h\ge H$ and $n\equiv-1\bmod2^H$ reaches the specific S2 obstruction cylinders $(-1,0)$ to arbitrarily high precision. The broad summary phrase about every obstruction class requires that qualification. **No S1 input is on PR 174's reverse-closure section $n\equiv1\bmod27$.** For $h>0$, three divides $n$. At $h=0$, the guard forces $n\equiv40\bmod81$, hence $n\equiv13\bmod27$. The protected unit cylinders $n\equiv1\bmod3^L,\ n\equiv-17\bmod2^L$ from CS2, $L\ge3$, are therefore disjoint from S1. This is a scope comparison, not a counterexample to S1.

Both S1 and CS1 construct shorter ordinary sources via lifts near the negative fixed point $-1$. S1 meets at the first shortcut endpoint of $n$ and obtains an unbounded parameter by increasing its original ternary height. CS1 uses the $-17$ cycle for the source, the $-1$ cycle for its partner, and a late ten-step equality forced by the other arm's low bits. Its witness-bearing CRT subfamily has original ternary height zero and preserves a lower bound on the length of every walk to a smaller integer. The two guards do not combine to cover the reverse-closure section. Beyond any forward odd step the odd core is a ternary unit, so unbounded initial $h$ is not a recurrence mechanism for escaping tails.

## The finite-clock translated interval bound

Set $k=\lfloor\log_2 L\rfloor$, $a=\log 2/\log3$ and $\theta=H_2(a)$. A $k$-step shortcut word of weight $p$ has $2^k T^k(n)=3^p n+B$ with $0\le B\le3^k-2^k$ by one-step induction. Fixing $p$ before subtracting the translated lower endpoint cancels its height: all images from $[M,M+L)$ lie in an integer interval of length at most $L_p=\lceil2\cdot3^p+(3/2)^k\rceil+2$. Parity words are in bijection with classes mod $2^k$; a class appears at most twice in this input interval.

Choose one input per distinct endpoint at odd clock $R$. Within fixed $p$, the images at shortcut clock $k$ remain distinct at residual odd clock $R-p$, since stripping the odd core of $T^k(n)$ gives exactly $U^p(\operatorname{oddcore}(n))$. Distinctness at this residual clock implies distinctness at all earlier common odd clocks. This supports induction on interval length on the same finite set of physical targets. It does not require distinctness between different $p$-classes.

Write $G(L)=L^\theta/\sqrt{\log(2L)}$. Fix a sufficiently large constant $D$. Weights greater than $\lfloor ak\rfloor-D$ contribute at most $O_D(G(L))$ by Stirling at the cutoff and a geometric binomial tail, since $a>1/2$. At the remaining weights, the separate interval widths give
$$
\sum_p L_p^\theta
\le C\,3^{-D\theta}L^\theta+O((k+1)(L^{\log_2(3/2)}+3)^\theta).
$$
The leading constant is independent of $D$ by the geometric sum. Each $L_p\ge(3/2)^k$ retains a fixed fraction of the initial log in the denominator of $G$. Thus one can choose $D$, then the base range, so that every retained $L_p\le L/2$ and $\sum_p G(L_p)\le G(L)/2$. For $R=\lceil K\log_2^2(2L)\rceil$ the reduction $L\mapsto L/2$ saves at least $K(2\log_2(2L)-1)$ prior to rounding, paying every $p\le k$. Strong induction proves the finite-clock bound with an absolute constant. The analogous cutoff $1/2<t<a$ with $H_2(t)<d$ gives $O_d(L^d)$ in $O_d(\log L)$ odd clocks for each $d>\theta$ (the case $d\ge1$ is immediate).

There is exactly one least positive source in each terminal fiber. Every other source in that fiber has a smaller ordinary partner. The estimate gives only an upper bound on the count of those minima. In particular, the least nonconverger, if it exists in an interval, must be one of them: a smaller member in its terminal fiber would converge by minimality and force it to converge. The theorem is consistent with that scenario at every interval size and does not assign a successful smaller partner to that prescribed source. The independent S1 congruence gives no relation to the minima of these fibers.

## Complete denominator and high-complexity boundary

For C5.1, scale the positive rational cycle by its common reduced denominator $d$ and let $e$ be the least integer state. The denominator is coprime to 6, since it divides $2^A-3^p$; shifts preserve negative valuations at each denominator prime. For a primitive period the states are distinct. Equal $k$-bit parity words force congruence of their scaled sources modulo $2^k$ by subtracting the two affine equations. The $s+t+1=P(k)+1$ consecutive starts around the minimum therefore include a state at least $e+2^k$ when $P(k)<A$. A backward step at most doubles the magnitude, and $z+d$ grows by at most $3/2$ per forward step. Subtracting $e$ from the two envelopes and multiplying by $2^t$ proves exactly the stated maximum inequality. It is a necessary test at a scale with $P(k)<A$. No low-complexity scale giving a contradiction is guaranteed for an arbitrary ordinary cycle. Neither this test nor synchronization excludes a divergent source.

## Independent finite controls and limits of review

Using independent Python integer recurrences, I checked 168 S1 sources (eight positive odd lifts at each $0\le h\le20$), including the strict inequality, exact common endpoint, and incompatibility with $n\equiv1\bmod27$. Over 2,760 input points from translated intervals of lengths 17, 64, 71, 255 and 513 at three starting heights, including $10^{55}+21$, I checked the odd-clock transport and the individual integer group widths. Direct evaluation gives $\theta=0.9499555271883305$. These controls are examples supporting the reconstruction; they cannot verify the universal statements by sampling. I did not audit the auxiliary high-excess density theorem, moving-law estimates, or finite-prime countermodels, and did not independently rebuild the PR's Lean code.

[PR 193 at the reviewed commit](https://github.com/GettysburgResearch/collatz/tree/52beff703fd3ce798c430e5af8199eb58d41bf93/research/astra-universal-descent-20261124)
