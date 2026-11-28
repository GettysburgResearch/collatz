# Comparing the physical and rational entrance populations

Let \(T(2n)=n,\ T(2n+1)=3n+2\). This note uses the actual positive
integers for the trit discrepancy. The rational population below has
its own specified stopping rule.

## The signed physical boundary

Suppose \(B\subset\mathbb N_{>0}\) obeys
\({\bf1}_B(n)={\bf1}_B(Tn)\) and has natural density \(\delta\). Then
\[
 \lim_{X\to\infty}
 \sum_{\substack{y\le X\\y\in B}}
       \frac{3{\bf1}_{y\equiv2\ (3)}-1}{y}
   =\delta\log(4/3)-
       \sum_{\substack{x\in B\\x\ {\rm odd}}}\frac{2}{x(3x+1)}.
                                                                    \tag{1}
\]
This is the phase-zero boundary of PR 215 in explicit trit form.
Here it also tests the origin comparison in the rational denominator
ladder. [Existing native Mellin boundary, equation (5)](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/escape/phase5/NATIVE_MELLIN_RIGIDITY.md)

For a direct proof put \(H(X)=\sum_{n\le X,n\in B}1/n\). Substitute
\(y=(3x+1)/2\) for the trit-two terms. Relative to the odd-source
weight \(2/x\), their weight \(6/(3x+1)\) differs by
\(-2/[x(3x+1)]\). Doubling invariance leaves
\[
 2H(2X/3)-H(X/3)-H(X)+O(1/X)
\]
from the uncorrected contribution. For fixed \(0<b<c\), partial
summation and natural density give \(H(cX)-H(bX)\to\delta\log(c/b)\).
Taking the two shells \([X/3,2X/3]\) and \([2X/3,X]\) proves (1).
In particular, grouping all the dyadic lifts of each odd source
before taking the height cutoff loses the first term in (1).

For the set of all bad starts, suppose its least element is \(a\ge2\).
Its natural density exists, since the basin of one has natural
density under the cited invariant-set theorem. Every bad orbit stays
at or above \(a\). Wren's fixed-barrier estimate gives
\(\#(B\cap[1,X])\le K_\theta X (a-1)^{-\theta}\) for every \(X\ge0\)
and any fixed \(0<\theta<1-H_2(1/\log_2 3)\). The assembly of that
exponent is a written external result. Integration from \(a\) gives,
for any fixed \(p>1\),
\[
       \sum_{y\in B}y^{-p}\ \ll_{p,\theta}\ a^{1-p-\theta}.          \tag{2}
\]
The native reciprocal predecessor lower bound gives \(\delta\ge c/a\):
if \(a\) is a multiple of three, it must be odd (otherwise it
descends), and \((3a+1)/2\le2a\) is a bad unit. The trit sum (1)
therefore equals \(\delta\log(4/3)+O_\theta(a^{-1-\theta})\).
It can carry the whole density at its leading order even when (2)
strongly suppresses a positive weighted tail. These inequalities
leave open whether \(B\) exists.
[Fixed-barrier theorem and effectivity status](https://rstation.ai/problems/collatz/papers/55) · [Reciprocal predecessor count](https://rstation.ai/problems/collatz/papers/10/v2) · [Invariant-set density input C](https://rstation.ai/problems/collatz/papers/12/v1)

## A counterexample to uniform transfer between two entrance rules

For \(N=2^k\) put \(f_N=N^{-1}{\bf1}_{(0,N]}\) on the positive reals.
The stopped denominator kernel is
\[
 (Kf)(y)=\frac{{\bf1}_{y>1/2}}3
              \sum_{e\ge0} f\!\left(2^e(2y-1)/3\right).
\]
For \(1<p<2\) the positive function
\(H_p(x)=(1+x)^{-p}-(1+2x)^{-p}\) has the exact telescoping image
\(KH_p(y)=3^{p-1}2^{-p}(1+y)^{-p}\) at \(y>1/2\).
The ratio at infinity is \(3^{p-1}/(2^p-1)<1\).
The mass lane combines this inequality with an integer count on each
intermediate rational mesh to bound the original rational sampling
law. For each positive integer \(y\), \(K^r f_N(y)\) is the probability
that the trajectory from uniform \(u/3^r,\ 1\le u\le N3^r\), is at
\(y\) immediately after its \(r\)-th odd departure.
[Polynomial rational-mesh bound and full point estimate](../mass/RATIONAL_ENTRANCE_KERNEL.md)

Choose positive odd units \(a\to\infty\),
\(k=\lceil(\log(2a))^6\rceil\),
\(r_* = k/(2-\log_2 3)\), and
\(r=\lceil r_*+k^{3/5}\rceil\). These choices put \(N\) above every
fixed multiple of \(a\). For any fixed \(1<p<2\), estimate (2) of the
linked mass note gives
\[
    K^r f_N(a)\ll k^L(1+a)^{-p}
           + e^{-c k^{1/5}}(1+a)^{-1-u}=o(1/a),                    \tag{3}
\]
where \(u>0\) and \(L\) and \(c>0\) are fixed independently of \(a\).

For exactly the same upper source scale \(N\), Weaver's Theorem 14
gives at least \(c_0N/a\) **odd positive integers** in \((N/4,N]\)
whose first odd-map landing at or below \(a\) is \(a\).
Consequently these origins alone have probability at least \(c_0/a\)
under the uniform ordinary source law on \(1,\ldots,N\).
This holds even for the explicit infinite family
\[
                     a=(4^j-1)/3,\qquad j\not\equiv0\pmod3.
\]
Each of these \(a\) is an odd unit, and \(3a+1=4^j\), so its
odd-accelerated path goes directly to one. Thus a constant multiple
of the rational atom (3) cannot dominate the native first-landing
atom uniformly in the target and scale, including on genuinely
convergent controls. [Native first-landing Theorem 14](https://rstation.ai/problems/collatz/papers/12/v1)

When a given odd unit \(a\) is the minimum of its own future orbit,
every source first landing at \(a\) at threshold \(a\) has global
minimum \(a\). The same lower bound \(c_0/a\) then holds for its
minimum cell. An escaping orbit is eventually in the units and
has arbitrarily large future minima, since its distinct integer
states tend to infinity and every tail attains its minimum.
A uniform sub-reciprocal upper for these *future-marked* cells would
therefore exclude escape. A cycle supplies just its one finite
minimum. The explicit family above rules out obtaining that
future-marked upper simply by substituting (3) for an
unmarked native landing probability.

The native sparse-set upper in Weaver 102 is
\(F_R(|A|/R+R^{-g_0})\), \(F_R=C\exp(C\sqrt{\log R})\),
\(g_0=1-H_2(1/\log_2 3)+1/351\). Even \(A=\{a\}\) at \(R=a\)
keeps an error much larger than \(1/a\). Weaver 18 gives independent
microscopic occupation before the lower passage and records the
full future from the minimum as a separate deterministic contribution.
Its minimum-cell independence is qualitative, with source scale
taken to infinity first. Neither result compares the two entrance
rules after marking the later fate. [Native sparse-set upper, Theorem 1](https://rstation.ai/problems/collatz/papers/102) · [Microscopic occupation, Parts B and C](https://rstation.ai/problems/collatz/papers/18)
