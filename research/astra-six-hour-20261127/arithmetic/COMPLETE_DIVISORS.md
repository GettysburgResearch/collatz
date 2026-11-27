# Complete-divisor tails for unrestricted near-critical cycle words

**PROPOSED written theorem.** Fix $L>0$. Pick uniformly from **all** rooted binary shortcut words of length $h$ with $p$ odd departures, where $0<h\log 2-p\log 3\le L$. There is no upper bound on an odd-to-odd division exponent, no strip condition on the heights, and no factorization assumption on the clocks. Write $D=2^h-3^p$, let $C$ be the literal affine carry, and put $G=\gcd(C,D)$. The actual reduced denominator is $D/G$. With $\beta=\log_3 2$ and $H=-\beta\log_2\beta-(1-\beta)\log_2(1-\beta)$, every divisor $g\mid D$ satisfies
\[
          \Pr(g\mid C)\ll_L h^{5/2}g^{-H}.                         \tag{1}
\]
For every $0<\epsilon<H$, as $h\to\infty$ in this strip,
\[
 \Pr\left(\log G\ge h^{1-H+\epsilon}\right)
       \le \exp(-c_\epsilon h^{1-H+\epsilon}).                     \tag{2}
\]
In particular the denominator loses at most a stretched-sublinear logarithmic term outside that exceptional proportion. These are bounds for words drawn from the stated finite population. They do not give an upper bound below one on the number of exceptional primitive ordinary cycles.

## The exact short prefix at the minimum

Use $T(x)=x/2$ at even 2-adic residue and $T(x)=(3x+1)/2$ at odd residue on positive odd-denominator rationals. If $b_i\in\{0,1\}$, $k_i=\sum_{j<i}b_j$, then the fixed point at this cut is $C/D$, with
\[
              C=\sum_{i:\,b_i=1}2^i3^{p-k_i-1}.
\]
All cyclic rotations give the successive positive rational phases. Indeed their odd determinant is prime to three, and the affine rotation identity is $2C_{i+1}=3^{b_i}C_i+b_iD$. Reducing the full carry at its first bit modulo two gives its prescribed parity. Common gcd with $D$ is unchanged by the unit multipliers. This is the classical rational-cycle correspondence. [Halbeisen and Hungerbühler, *Optimal bounds for the length of rational Collatz cycles*](https://user.math.uzh.ch/halbeisen/publications/pdf/collatz.pdf)

Rotate to a least physical phase $x_0$. At each cut $i\le h$, the suffix from $x_i\ge x_0>0$ to $x_0$ has nonnegative affine carry. Thus
\[
     2^{h-i}x_0\ge 3^{p-k_i}x_i\ge 3^{p-k_i}x_0,\qquad
     3^{p-k_i}\le 2^{h-i}.                                        \tag{3}
\]
At each odd cut this bounds three times its carry summand by $2^h$, giving the exact integer cap $3C\le p2^h$ at the minimum. If $g\mid C,D$, write the minimum as $A/d$ over the common, possibly unreduced denominator $d=D/g$. Then
\[
        A=C/g\le p2^h/(3g).
\]
For any fixed odd $d$, a binary prefix of length $n$ determines $A\bmod 2^n$. In fact the affine equation for two numerators sharing it gives $3^{k_n}(A-A')=2^n(B-B')$. Hence the first $n$ bits at the minimum determine the **whole** word rooted there whenever $2^n>p2^h/(3g)$. This is an actual decoder: solve the prefix affine congruence for $A$ in $[0,2^n)$, then iterate $T$ on $A/d$. The concentration estimate imposes one residue condition on the complete lift, including every prime power of $g$.

## Counting the codes

If $g\le p$, the right side of (1) after enlarging the constant exceeds one. Otherwise choose $n=\lceil\log_2(p2^h/g)\rceil$; then $0\le n\le h$. All possible prefixes at the minimum have
\[
                k_n\ge p-(h-n)\beta\ge \beta n -L/\log 3.
\]
Put $v=\beta/(1-\beta)>1$. The number of such words is at most
\[
 v^{L/\log 3}v^{-\beta n}(1+v)^n\ll_L 2^{Hn}.
\]
There are at most $h$ rootings for each cycle word rooted at its minimum, including for an imprimitive presentation. Consequently the number of successful rooted words is $\ll_L h(p2^h/g)^H$. Stirling's formula and $p=\beta h+O_L(1)$ give $\binom hp\gg_L 2^{Hh}/\sqrt h$. This yields (1), in fact with the slightly smaller factor $O_L(h^{3/2+H})$. The proof only used $0<h\log2-p\log3\le L$. No irrationality-measure input is needed for (1) or (2).

For (2), take $t=\epsilon/2$, $s=H-t\in(0,1)$. Since $G\mid D$,
\[
 \mathbb E[G^t]\le\sum_{g\mid D}g^t\Pr(g\mid C)
        \ll_Lh^{5/2}\prod_{\ell\mid D}(1-\ell^{-s})^{-1}.
\]
There are at most $h$ distinct prime divisors. Ordering them increasingly gives $\ell_j\ge j+1$, so the logarithm of this Euler product is $O_s(\sum_{j\le h}(j+1)^{-s})=O_s(h^{1-s})$. Markov's inequality at the displayed threshold gives (2), since $1-s=1-H+\epsilon/2$. If desired, along clocks with $\log D\asymp h$ this puts the actual denominator at $D^{1-o(1)}$ outside the exceptional proportion. The estimate controls the **complete** canceled factor even when the set of primes dividing it grows.

The principal finite arithmetic steps are checked in [MinimumCode.lean](MinimumCode.lean). The entropy and divisor-product steps above are written deductions. The [bounded-mask divisor distribution](https://github.com/GettysburgResearch/collatz/blob/f192322f70073ba44bc9f98785a51c27a4da9ee5/research/astra-global-closure-20261124/round13/cycle/DISTRIBUTION.md) concerns a different probability space and estimates modular mixing there. Here the minimum cut and dyadic decoding apply to the entire fixed-weight population.

## Pointwise boundary

For $g=D$ the count still allows a polynomial number of words on ordinary near-critical clocks with polynomial inverse clock gap. Rotating one primitive ordinary cycle supplies $h$ rooted words; this does not contradict (1). Small nonordinary denominators really do permit exceptional words. For example the gap word $1,3$ realizes $5/7,11/7$, and repetitions keep denominator seven even as their unreduced determinant grows. Those repeated clocks eventually leave each fixed near-critical strip, so the example is not an asymptotic counterexample inside the theorem. To exclude ordinary cycles one must still show that no primitive nontrivial word realizes the exceptional full cancellation $G=D$. The prefix reconstruction and the tail estimate do not settle that individual case.
