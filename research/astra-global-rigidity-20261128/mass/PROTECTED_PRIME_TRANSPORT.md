# Globally fresh prime factors on increasing ordinary prefixes

Fix a finite set of primes \(S\) containing 2 and 3. Write \(D=24\prod_{p\in S\setminus\{2,3\}}p\). For any \(t\ge1\) and positive multiple \(n\) of \(D\), define
\[
 x_i=9^i8^{t-i}n-5,\qquad \beta_i=(x_i+1)/4,\qquad 0\le i\le t .
\]
Every \(\beta_i\) is a positive integer prime to all of \(S\). On the actual shortcut map \(T(2u)=u,\ T(2u+1)=3u+2\), the consecutive three-step blocks from \(x_i\) to \(x_{i+1}\) all have parity word \(110\). In fact \(x_i\equiv3\pmod8\), the second step reaches \((9x_i+5)/4=2x_{i+1}\), and the third halves it. Every state throughout is at least \(x_0\). The starting valuations in the ramp notation are \(s_i=2,\ h_i=0\). The outside-\(S\) prime-power mass acquired across *all* these ramp starts, counting each prime only to its maximum attained exponent, is
\[
 L_t=\log\operatorname{lcm}(\beta_0,\ldots,\beta_t).
\]
Thus the examples also control the total outside-\(S\) valuation increments, which dominate this maximum-exponent statistic when initial mass is included. The ramp notation agrees with the reduced-core transport formulation.

## A deterministic least-common-multiple bound

For \(0\le i<i+d\le t\),
\[
 8^d\beta_{i+d}-9^d\beta_i=9^d-8^d .
\]
In particular successive cores are coprime. For every prime power \(p^e\) dividing the product of the cores, \(p\notin S\). Put \(d_e=\operatorname{ord}_{p^e}(9/8)\). All indices with \(p^e\mid\beta_i\) lie in one class modulo \(d_e\), by the displayed identity. Their number after the first is at most \(\lfloor t/d_e\rfloor\), exactly the number of \(1\le k\le t\) for which \(p^e\mid9^k-8^k\). Sum this inequality over all \(e\) for each \(p\). It proves the integer divisibility
\[
 \frac{\prod_{i=0}^t\beta_i}{\operatorname{lcm}_{0\le i\le t}\beta_i}
      \ \biggm|\ \prod_{k=1}^t(9^k-8^k).
\]
Since \(\beta_i=(9/8)^i(\beta_0+1)-1\ge(9/8)^i\beta_0\), taking logarithms gives
\[
          L_t\ge(t+1)\bigl(\log\beta_0-\tfrac12t\log8\bigr).       \tag{1}
\]
Take \(n=D\) fixed and let \(t\to\infty\). There is then \(c_S>0\) such that \(L_t\ge c_S(\log x_0)^2\) on these true protected prefixes. This statement about the displayed single-parameter family uses no assumption about its eventual fate.

## Positive proportions of known convergent sources

Let \(B_5\) consist of all ordinary starts which eventually visit 5. Its natural density \(d_5>0\) is a named fixed-basin input. Every such source continues through \(5,8,4,2,1\). For \(x_0\in[X,2X)\) in the prescribed class \(x_0\equiv-5\pmod{D8^t}\), the conditional fraction in \(B_5\) is
\[
 d_5+O_S\bigl((1+t)/\sqrt{\log X}\bigr)+o_S(1),
               \qquad 0\le t\le\sqrt{\log X}.                         \tag{2}
\]
In particular for all sufficiently small fixed \(c=c(S,d_5)>0\), at \(t=\lfloor c\sqrt{\log X}\rfloor\) a positive fraction of the progression consists of genuinely convergent starts. On each of them (1) gives \(L_t\gg_S(\log X)^{3/2}\). These are conditional proportions in the given progression, whose relative width in the full octave tends to zero. [Fixed-basin source and frozen dependencies](FIXED_BASIN_NATIVE_WINDOW.md) · [Finite actual coupling and first-hit defect](ORDINARY_BASIN_WINDOWS.md)

Here are the progression details in (2). Write \(f={\bf1}_{B_5}\). For \(k\) ranging over an interval of \(K\) consecutive integers, consider two positive starts \(z=uk+b\) and \(3^j z+l\). For positive integral \(u\), integer \(l\), and \(j\ge0\), their first-hit mismatch proportion is at most
\[
 C\,2^{v_2(u)}\frac{1+j+\sqrt{\log(2+|l|/3^j)}}{\sqrt{\log(2K)}}+ CK^{-1/2}.   \tag{3}
\]
This follows directly from the *affine two-ray* version of the upper-bit merger theorem: its symbolic equal-slope and equal-intercept absorption by deadline \(H=\lfloor\tfrac12\log_2 K\rfloor\) is determined by the starting residue of \(z\bmod 2^H\). Its failure proportion on a complete block is at most \(C(1+j+\sqrt{\log(2+|l|/3^j)})/\sqrt{H}\). An isolated equality of differently sloped trajectories in a residue is unnecessary. Each residue hit by the progression has relative frequency at most \(2^{v_2(u)-H}+1/K\). A possible visit to 5 before the symbolic meeting costs \(O(2^H/K)\) for each trajectory, by indegree two and injectivity as functions of \(k\). On the other pairs the two first-hit labels agree. This proves (3), including the trivial case \(v_2(u)>H\). [PR146, normalized affine two-ray theorem (1) and residuewise proof](https://github.com/GettysburgResearch/collatz/blob/0410811710af2f7da71522ec67233528048adb9a/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md)

Now put \(n=Dk\), so \(k\) ranges over a proportional interval of \(K\asymp X/(D8^t)\) integers and \(\log K\sim\log X\) in (2). The initial strictly protected block lies above 5, giving \(f(x_0)=f(9^tDk-5)\). Take \(u=D,b=0,j=2t,l=-5\) in (3) to compare directly to \(f(Dk)\) at cost \(O((1+t)/\sqrt{\log K})\), since \(v_2(D)=3\). The genuine exceptional departure at 5 was included in the early-visit count in (3). This direct affine comparison uses all \(k\), with no truncation by their individual 2-adic valuations. Finally, \(f(Dk)\) has mean \(d_5+o_S(1)\) on proportional \(k\)-intervals: average \(f(Dk+l)\) over \(0\le l<D\), use (3) separately at each fixed gap with \(j=0\), then apply natural density to the consecutive interval so obtained. This proves (2).

## Pairwise coprimality can also hold throughout

For the stronger conclusion \(\gcd(\beta_i,\beta_j)=1\) for every \(i\ne j\), additionally require \(n\) divisible by the product of all distinct primes dividing \(\prod_{k\le t}(9^k-8^k)\). Each such prime is outside \(\{2,3\}\); reducing \(\beta_i=9^i8^{t-i}n/4-1\) modulo it gives \(-1\). The pair identity excludes all remaining shared primes. If \(M\) denotes the resulting modulus for \(x_0\), then
\[
                 \log M\le \tfrac12(\log9)t(t+1)+O_S(t).
\]
This stronger progression still has conditional \(B_5\) density \(d_5+o(1)\) whenever \(M\sqrt{\log(2M)/\log X}\to0\). To see it, compare its count on \([X,2X)\) to each translate by \(j=0,\ldots,M-1\). The total number of mismatches for any one shift, even without the residue restriction, is \(O(X\sqrt{\log(2M)/\log X}+\sqrt X)\) by the ordinary interval estimate. The average of the translated counts is the unrestricted octave count divided by \(M\), up to \(O(1)\) from the two endpoints. Division by the progression length proves the claim. In particular one can take \(t=\lfloor c\sqrt{\log\log X}\rfloor\) for any fixed \(0<c<1/\sqrt{\log9}\). Here \(L_t=\sum_i\log\beta_i=(1+o(1))(t+1)\log X\).

The examples preclude a uniform \(o((\log x_0)^2)\) budget for this statistic over all protected ordinary finite prefixes. They preclude a uniform \(o((\log x_0)^{3/2})\) budget even if the prefix must be part of a certified convergent orbit. Any hypothesis restricted to an entire infinite escape, or allowing an unrestricted finite constant depending on each individual starting value, needs a different argument.
