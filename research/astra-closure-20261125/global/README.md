# A Fourier norm test for a second ordinary basin

**PROPOSED written equivalence. The necessary upper bound remains OPEN.** Let $T(2n)=n$, $T(2n+1)=3n+2$. Put $b(n)=1$ if the positive ordinary integer $n$ never reaches 1, and zero otherwise. Set $b(0)=0$. Write $e(t)=\exp(2\pi i t)$ and use normalized Haar measure on the circle. For $N\ge1$ define the real trigonometric polynomial

$$
K_N(t)=\sum_{|k|<N}(1-|k|/N)b(|k|)e(kt).
$$

Then the following four statements are equivalent.

1. Every positive ordinary integer reaches 1.
2. The numbers $\|K_N\|_1$ have finite lower limit as $N\to\infty$.
3. The sequence $k\mapsto b(|k|)$ is the Fourier transform of a finite complex measure on the circle.
4. Along $N=2^j$, with $A_N(t)=K_N(2t)$, $H_N(t)=K_{2N}(t)-A_N(t)$,

$$
\sum_{j\ge0}\int_{\mathbb T}\big(|H_{2^j}(t)|-|A_{2^j}(t)|\big)_+\,dt<\infty.
$$

The criterion uses a symmetric kernel. For example, a constant coefficient sequence gives a Fejér kernel with bounded integral norm. A one-sided analytic polynomial or a sharp interval truncation has different norm behavior.

## From compactness to ordinary termination

Under statement 2, take a bounded subsequence of the measures $K_N(t)\,dt$. Weak-star compactness and separability give a convergent subsequence. Each fixed Fourier coefficient tends to $b(|k|)$. Conversely, under statement 3 convolving that measure with the nonnegative Fejér kernel bounds every $\|K_N\|_1$ by its total variation.

The limit measure is convolution-idempotent by its Boolean Fourier coefficients and uniqueness. The Cohen–Helson–Rudin idempotent theorem puts its Fourier support in the coset ring of $\mathbb Z$. Each coset here is an arithmetic progression or a singleton, so any finite Boolean combination has eventually periodic positive trace. This application needs no density hypothesis on either basin. [Green and Sanders, *Annals of Mathematics* 168 (2008), introduction and Theorem 1.1](https://annals.math.princeton.edu/2008/168-3/p09)

Suppose an exactly orbit-invariant coloring of the positive integers has eventual period $d$. Positive $x,y$ congruent modulo $d$ have the same color, since $2^jx,2^jy$ are eventually in the periodic tail and doubling preserves each color. Choose the smallest positive period of this induced ordinary coloring. If $2\mid d$, equality after doubling shows $d/2$ is already a period. Thus $d$ is odd. Any residue modulo $d$ has a positive odd representative $x$, and the odd edge and doubling give $b(x)=b(3x+1)$. This identity consequently holds on every residue. If $3\mid d$, it makes $d/3$ a period. Hence $6$ is invertible modulo $d$. Applying the two color-preserving maps in opposite orders gives

$$
b(6x+1)=b(2x)=b(x)=b(3x+1)=b(6x+2).
$$

These are all adjacent residue pairs. The color is constant on the positive integers, and $b(1)=0$. This proves statement 3 implies statement 1. Statement 1 makes every $K_N$ zero.

## The actual odd transfer and the missing estimate

Doubling invariance identifies the even-frequency part of $K_{2N}$ with $A_N$ exactly. The remaining part is

$$
H_N(t)=2\operatorname{Re}\sum_{j=0}^{N-1}
 \left(1-\frac{2j+1}{2N}\right)b(3j+2)e((2j+1)t).
$$

Translation by $1/2$ fixes $A_N$ and negates $H_N$. Pairing the two values and using $(|a+h|+|a-h|)/2=\max(|a|,|h|)$ for real $a,h$ proves the exact equality

$$
\|K_{2N}\|_1-\|K_N\|_1
=\int_{\mathbb T}(|H_N|-|A_N|)_+.
$$

Thus statement 4 bounds a subsequence in statement 2, and statement 1 gives statement 4. It would suffice to bound these nonnegative increments in total across all dyadic levels for the actual globally invariant mark.

One attempted bound interpolates the two neighboring even coefficients at each odd frequency. If $a_k=(1-|k|/N)_+b(|k|)$, use $(a_k+a_{k+1})/2$ at $2k+1$. The resulting polynomial is $(1+\cos(2\pi t))A_N(t)$, whose integral norm equals $\|K_N\|_1$. The interpolation is exact wherever the three adjacent colors at $2k,2k+1,2k+2$ agree, since the triangular weights are linear on each side of zero. The remainder has bounded coefficients supported on at most a constant times the number of adjacent disagreements up to $2N$. The cited fixed-gap absorption estimate therefore gives only $O(\sqrt{N}/(\log N)^{1/4})$ for its integral norm by Parseval. In fact at a fixed unequal pair of coarse colors, the true binary midpoint differs from their arithmetic mean by $1/2$; the corresponding weighted remainder coefficient tends in magnitude to $1/2$. Summability of the unsigned interpolation-remainder norms would already exclude every such pair. The exact increments can be smaller than those remainder norms. [PR146, complete-block adjacent absorption, frozen f431078244e868dc699fad011044f0d5e7f76437](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md)

The failure persists for a single genuine ordinary edge error. Let $c(n)$ indicate that $n$ ever visits 5, and put $c(0)=0$. This mark satisfies exact doubling, and its odd edge identity fails only at input 5. Indeed $5\to8\to4\to2\to1\to2$, and a different starting point visits 5 exactly when its next state does. If its Fejér norms had a bounded subsequence, the same idempotent argument would make $c$ eventually periodic. Doubling would extend that periodicity to all positive arguments. Then $c(2j+1)-c(3j+2)$ would be a periodic function of $j\ge0$, which cannot be nonzero only at $j=2$. Thus the dyadic increments have divergent sum for this actual mark. The sole correction to the positive-frequency odd sum is the mode at frequency 5 with a uniformly bounded coefficient. Fixed-floor absorption applies to this mark above 5. A proof based on the homogeneous equation must distinguish exact equality from adding that one mode. [Companion actual-target controls](../descent/ATTEMPT.md)

The analytic fixed-point equation for $F(z)=\sum b(n)z^n$ is the Berg–Meinardus equation. It is one mixed dilation identity. The two independent pure-base Mahler equations needed by the rationality theorem of Schäfke and Singer have not been obtained. Hardy-space fixed-point rigidity does not supply the upper bound either. Every positive bad $n$ would already have $b(2^j n)=1$ for all $j$, so $F$ could not belong to $H^2$. The symmetric Fejér condition above permits a point mass in the Fourier representation. [Berg and Meinardus, analytic formulation](https://www.math.uni-rostock.de/math/pub/romako/heft48/berg2.html) · [Schäfke and Singer, Theorem 1](https://singer.math.ncsu.edu/papers/vshort2-5.pdf) · [Neklyudov, §4](https://arxiv.org/abs/2106.11859)

For the actual least bad triple $3q$, lower triples supply the exact coefficient values $b(3v)=0$ for $0<v<q$, while $b(3q)=1$. They supply neither a bound on the integral overshoot at all larger scales nor an independent pure-base equation. **The first unsupported inference** would be that the sum in statement 4 is finite for this exact ordinary coloring. This pass does not establish it.

## A test against the square-root growth ceiling

Let $V(N)$ count adjacent color changes through $N$. For the triangular coefficient sequence $a_k$ of $K_N$, summing its first differences in square gives
$\sum_k|a_k-a_{k-1}|^2\ll V(N)+1/N$. Indeed each change costs at most one and each equal-color edge costs at most $1/N^2$. Parseval bounds $\|K_N\|_2\ll\sqrt N$ and $\|(1-e(t))K_N\|_2\ll\sqrt{V(N)+1/N}$. Split the integral norm at circle distance $\eta$ from zero. Cauchy–Schwarz on the short arc and then on its complement, with $\int_{\eta\le |t|\le1/2}|1-e(t)|^{-2}\,dt\ll 1/\eta$, gives

$$
\|K_N\|_1\ll \sqrt{N\eta}+\sqrt{\frac{V(N)+1/N}{\eta}} .
$$

The cited absorption bound gives $V(N)\ll N/\sqrt{\log N}$. Taking $\eta=(\log N)^{-1/4}$ therefore gives $\|K_N\|_1\ll\sqrt N/(\log N)^{1/8}$. In particular, eventual dyadic norm amplification by at least $\sqrt 2$ on a nonconstant ordinary coloring would contradict the square-root ceiling, since the norm is positive once a nonzero frequency enters. The transfer supplies only the nonnegative overshoot identity. In fact the interpolation calculation above gives $\|H_N-\cos(2\pi t)A_N\|_2=o(\sqrt N)$, and $|\cos(2\pi t)A_N|\le |A_N|$. It gives no lower bound of $(\sqrt 2-1)\|K_N\|_1$ on the overshoot. The single-edge mark at 5 has divergent norms while obeying this improved upper bound, so divergence and the upper bound are compatible.

## Relation to the fixed-orbit test and verification

The November 25 update to PR192 tests the series $\sum_{j\ge0}(T^j x\bmod2)3^{E_j}z^j$ on the time index of one fixed start $x$, where $E_j$ counts earlier even inputs. Its source-qualified scalar Mahler condition would imply eventual periodicity of that orbit. The variable in $K_N$ is Fourier-dual to the ordinary **starting integer**. Even a periodic trajectory has its own time series without specifying the membership coefficients for other starts. The finite-dimensional fit and dyadic-to-real lifting arguments there do not bound the total variation of our Fejér approximants. Conversely our criterion, if proved for the actual indicator, would treat unexpected positive cycles and escape at once. [PR192, frozen 07d494324c7ea440d45845d725f5cebad8a67124](https://github.com/GettysburgResearch/collatz/blob/07d494324c7ea440d45845d725f5cebad8a67124/research/astra-full-proof-20261125/global/README.md)

[PeriodicColor.lean](PeriodicColor.lean) formally proves the entire eventual-periodicity implication for any color type, every positive ordinary argument and the exact two shortcut identities. Lean 4.34.1 checked it with warnings as errors and reported only the standard axioms `propext` and `Quot.sound`. The compactness, idempotent theorem application and Fourier estimates above are written mathematics.
