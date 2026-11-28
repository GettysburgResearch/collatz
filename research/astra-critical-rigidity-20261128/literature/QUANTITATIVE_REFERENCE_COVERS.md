# A uniform quantitative height bound for arbitrary reference arcs

**Status: PROPOSED written theorem.** Let $n>0$ be an ordinary integer, let its actual shortcut prefix have duration $D\ge1$, and partition it into $K\ge1$ nonempty arcs. On each arc take two rational references of height at most $H$ satisfying its affine endpoint equation, with the initial reference different from the physical initial state. No restrictions are imposed on the word within an arc. There is an absolute effectively computable constant $A$ such that

$$
 D\le \exp\!\left(A\frac{K+1}{\ln(K+2)}\right)
       [1+\log_2(n+1)+\log_2 H].                                    \tag{1}
$$

The same upper bound holds for the base-two logarithm of every physical boundary height, after an absolute change in $A$. In particular, on any one fixed ordinary source, every separated cover with $\log_2 H\le D^\theta$, for fixed $\theta<1$, costs $\gg_\theta\ln D\,\ln\ln D$ arcs for all sufficiently large $D$. The implicit constant is effective and the onset may depend on the source. More generally replace $\ln D$ in this inversion by $\ln(D/U)$, where $U=1+\log_2(n+1)+\log_2H$ and $D/U\to\infty$. There is no input asserting the existence of a small cover.

The proof adapts the boundary-record and ordered-exponent argument of [Weaver, Paper 15/v2, Theorem 9, (A1)–(A13)](https://rstation.ai/problems/collatz/papers/15/v2). That theorem assumes an actual periodic odd-exponent dictionary and charges the sum of its literal division budgets. In (1) arbitrary signed endpoint references may change on each arc. Their denominators may be even or divisible by three. The proof clears denominators locally, uses distortion at physical **boundaries** only, and retains the original-source coordinate. The external quantitative input is [Evertse and Ferretti, *Annals of Mathematics* 177 (2013), Corollary 1.3 and Lemma 15.3](https://doi.org/10.4007/annals.2013.177.2.4).

## A packet of $m$ consecutive arcs

Replace $H$ by $\max(H,2)$. For an integer physical state $x$, write $Y(x)=x+2H+2$ and $h(x)=\log_2Y(x)$. For a single arc of duration $d$ with references $\xi,\eta$, clear their denominators by $C_1\le H^2$. If its grade is $a$ and its endpoint $y$, then

$$
  2^d C_1(y-\eta)=3^a C_1(x-\xi).
$$

The two powers are coprime and the integer on the right after removing $3^a$ is nonzero. Hence $2^d\le H^2(x+H)$ and $d\le3h(x)$. Since $Y(Tx)\le(3/2)Y(x)$, we also have $h(y)\le3h(x)$. A packet of at most $m$ arcs from $s$ therefore has duration $d\le2\cdot 3^m h(s)$ and terminal logarithmic height at most $3^m h(s)$.

Group consecutive arcs into packets of at most $m$. A packet may be truncated at a boundary where it attains its largest new boundary record. Write $s,e$ for the initial and terminal physical states of this truncated packet, $R$ for the largest previous value of $Y$, and $r=\log_2 R$. A **fast increase** means $h(e)>2r$. Fix the cutoff

$$
    h_* = 10^7 (m+2)^5\,3^m\,\log_2(2H).                              \tag{2}
$$

Consider only a fast increase with $r\ge h_*$. Every boundary $x$ within its truncated packet exceeds $W=10(m+1)3^m H$: otherwise $h(e)\le3^m\log_2(W+2H+2)<h_*$. Put $c=\log_2(3/2)<3/5$. From $h(e)-h(s)\le cd$ and $h(s)\le r<h(e)/2$,

$$
        h(s)<cd,\qquad d>h(e)/(2c)>5h(e)/6.                          \tag{3}
$$

For a one-arc slope $\lambda=3^a/2^l$ at these high boundaries,
$y/(\lambda x)=(1-\xi/x)/(1-\eta/y)\in[1/2,2]$. Thus distortion over any part ending at an arc boundary costs at most $2^m$. There is no assumption on intermediate physical heights within the arcs.

## The fixed forms and the exact primitive normalization

Let there be $j\le m$ arcs in the truncated packet. Write $d_i,g_i$ for time and odd count through boundary $i$, starting from $(d_0,g_0)=(0,0)$ and ending at $(d,g)$. Let $C$ be the common multiple obtained by multiplying the reduced denominators of its $2j$ reference endpoints, so $C\le H^{2m}$. Put $P=2CH$. The centered telescope gives the integer coordinates

$$
 \begin{aligned}
 z_0&=C3^g(s-\xi_1),\\
 z_i&=C(\eta_i-\xi_{i+1})\,2^{d_i}3^{g-g_i}\quad(1\le i<j),\\
 Z=\sum z_i&=C2^d(e-\eta_j).
 \end{aligned}                                                       \tag{4}
$$

The root $z_0$ exceeds the sum of the absolute values of the other coordinates. Indeed, $2^{d_i}3^{-g_i}\le 2^m s/x_i$ by boundary distortion, $s-\xi_1\ge s/2$, and $|\eta_i-\xi_{i+1}|\le2H$. The sum of the ratios is at most $m\,2^{m+2}H/W<1$. Discard zero coordinates and delete nonempty zero subsums repeatedly. The positive root survives, the total $Z$ is unchanged, and every nonempty subsum of the retained tuple is nonzero. If only the root remained then $2^d\mid C(s-\xi_1)$, hence $d\le h(s)+\log_2C$, impossible by (2)–(3). Write $l$, $2\le l\le m$, for the retained dimension, and $T=\max|z_i|/G=z_0/G$ for the height of the primitive tuple after dividing by its positive gcd $G$.

Use coordinate forms at infinity and at three. At two replace the root coordinate by the sum of the coordinates. At each place this is a basis of forms, all drawn from coordinates and their sum. Let $Q$ be the product of their absolute values on the **primitive** tuple, without projective norm denominators. For an integer $t\ne0$ let $\operatorname{rough}(t)$ remove the powers of two and three from $|t|$. Replacing the root form at two multiplies the raw coordinate product by $|Z|_2/|z_0|_2$. Dividing every coordinate by $G$ divides that product by $\operatorname{rough}(G)^l$. In particular

$$
    Q\le C(s+H)\,P^m\,2^{-d}.                                        \tag{5}
$$

Here $|Z|_2\le2^{-d}$, the root contributes $\operatorname{rough}(z_0)/|z_0|_2\le C(s+H)$, and each remaining prime-to-six part is bounded by its integer coefficient $|C(\eta_i-\xi_{i+1})|\le P$. This accounting permits $C$ divisible by either two or three.

The dyadic part of $G$ is at most $C(s+H)$, using $z_0$. Its ternary part is at most $C(e+H)$, using $Z$. Its prime-to-six part is at most $P$, using any retained nonroot. From $Z\le lGT$ and $e\ge3H$ it follows that

$$
      T\ge\frac{2^d}{2mCP(s+H)}.                                    \tag{6}
$$

The harmless coefficients in (5)–(6) obey
$$
  \log_2\max(CP^m,\,2mCP)\le(2m+4)^2\log_2(2H)<d/20
$$
by (2)–(3). Also $\log_2T\le\log_2[C3^g(s+H)]<3d$ since $g\le d$. Equations (3), (5), and (6) therefore yield

$$
   Q<T^{-1/100},\qquad
   h(e)/5\le\log_2T\le 6\cdot3^m h(s).                              \tag{7}
$$

Thus a fast record creates strict excess in the Subspace Theorem inequality. The second comparison locates the actual progress relative to the height of the primitive vector.

## How many height intervals can pay for a fast increase?

The following details ensure uniformity as the packet size and endpoint budget change. Put $N=4000l$ and write $G=2^u3^vG'$ with $(G',6)=1$. Each primitive nonroot can be expressed

$$
  t_i=b_i\,2^{(d_i-u)^+}3^{(g-g_i-v)^+},\qquad 0<|b_i|\le P.
$$

Indeed $G'$ divides the raw coefficient, as do the powers needed to offset any negative residual dyadic or ternary exponent. In the chronological order of the retained nonroots the first exponent is nondecreasing and the second is nonincreasing. Equation (2) and the lower bound in (7) ensure $\log_2 T>N\log_2P$ and $T>l^{200l}$.

For these nonroots round down
$$
 \frac{(d_i-u)^+\ln2}{\ln T},\qquad
 \frac{(g-g_i-v)^+\ln3}{\ln T}
$$
to multiples $a_i,b'_i$ of $1/N$ in $[0,1]$. Their ranges follow from $1\le |b_i|$ and $|t_i|\le T$. The normalized exponents for the two nonarchimedean coordinate forms are bounded above by $-a_i,-b'_i$. The exponent at infinity is bounded above by $\min(0,a_i+b'_i+3/N-1)$. The total excess of these rounded upper exponents over the three true exponents is at most $7/N$ per nonroot, since the logarithm of each coefficient is at most $(\ln T)/N$. The root's real normalized exponent is zero. Round down its ternary valuation times $\ln3/\ln T$ on $[0,1]$ and the dyadic valuation of the primitive sum times $\ln2/\ln T$ on $[0,2]$; the primitive sum has magnitude at most $lT\le T^2$. This adds at most $2/N$ more excess.

Finite-place norms of the primitive vector are one, and its infinite-place norm is $T$. The true sum of all projective exponents is less than $-l-1/100$ by (7), so the rounded sum is at most $-l-1/200$. All rounded exponents are nonpositive. Scale them toward zero to make their sum exactly $-l-1/200$, keeping all necessary inequalities. The number of resulting systems is bounded by

$$
   (N+1)(2N+1)\binom{N+l-1}{l-1}^{\!2}\le \exp(C_1l)              \tag{8}
$$

with an effective absolute $C_1$. The binomial coefficients count the oppositely ordered rounded tuples. They are the reason an absolute exponential in $l$ suffices.

Apply Evertse–Ferretti, Corollary 1.3, with $\varepsilon=1/200$ and $S=\{\infty,2,3\}$. Above $l^{200l}$, the primitive heights for each system lie either on the exceptional subspace or in at most $\lceil10^6\,2^{2l}l^{12}200^2\ln(1200l)\rceil$ intervals $[V,V^\omega)$ with $\omega=400l\ln(6l)$. By their Lemma 15.3 the exceptional subspace requires a nonempty zero subsum of the coordinates. Pruning excluded every such subsum. These intervals and the systems (8) depend only on $l$, with no reference data or orbit parameters. Their locations need not be effective. Their number and logarithmic widths are effective.

## Charging disjoint record increases

On the scale $y=\ln h$, every packet that fails to double the previous record in $h$ adds at most $\ln2$. All fast increases whose old logarithmic height is below (2) end below $3^m h_*$, by the elementary packet bound. Their **total** charge beyond the initial record is $O(m+1)$ since $h(n)\ge\log_2(2H)$ and their progress intervals have disjoint interiors.

For a remaining fast packet put $v=\ln\log_2 V$ for its assigned interval. From (7) and $h(s)\le r$, its whole progress interval $[\ln r,\ln h(e)]$ lies within
$$
 [\,v-\ln(6\cdot3^m),\,v+\ln\omega+\ln5\,].
$$
The actual progress intervals again have disjoint interiors. Sum these enlarged widths over dimensions $2\le l\le m$, over the systems (8), and over their allowed height intervals. The total is at most $\exp(C_2m)$ for an effective absolute $C_2$, because all counts grow at most exponentially and each width is $O(m+\ln(m+2))$. If $m=1$ the large fast-packet case was already excluded by its one-coordinate divisibility. We have proved, with $h_{\max}$ the greatest logarithmic height at any boundary,

$$
 \ln(h_{\max}/h(n))\le \lceil K/m\rceil\ln2+\exp(C_3m).              \tag{9}
$$

Finally $D\le3K h_{\max}$ from the individual duration bound. For large $K$ take $m=\lfloor\ln(K+2)/(2C_3)\rfloor$, and take $m=1$ in the remaining finite range. This gives (1) after adjusting an absolute effective constant, using $h(n)\le2[1+\log_2(n+1)+\log_2H]$. Monotone inversion gives the stated $\ln(D/U)\ln\ln(D/U)$ lower order. No numerical claim about the usefulness of the resulting onset is made.

## Positive rationals with their full starting denominator

Let the initial physical point be $a/q>0$ in lowest terms with odd $q$, and let the reference height bound remain $H$. On an actual rational trajectory only factors of three can be removed from the odd reduced denominator, so $A_i=q x_i$ is an integer at every clock. Scale each reference endpoint to $q\xi_i,q\eta_i$ and use $H_0=\max(2,qH)$. Both scaled heights are at most $H_0$. Equations for differences, dyadic divisibility, and separation are unchanged in the integer coordinates. At odd departures the affine offset in one scaled step is $q/2$, and at even ones it is zero. Hence $Y(A)=A+2H_0+2$ still satisfies $Y(A_{\rm next})\le(3/2)Y(A)$. This is the sole one-step size estimate needed above. The remaining arguments use the integer coordinates at boundaries, their scaled references, and their difference transport. Thus the entire proof gives, after an absolute change in the same effective constant,

$$
 D\le\exp\!\left(A\frac{K+1}{\ln(K+2)}\right)
       [\,1+\log_2\max(a,q)+\log_2H\,].                              \tag{10}
$$

The factor $q$ used to scale the reference data contributes only the displayed $\log_2 q$ inside this estimate. An initial denominator divisible by three is allowed; no fixed-denominator property after reduction is assumed.

## Full denominator on a closed orbit

For a positive primitive rational cycle of least shortcut period $D$, let $q$ be its full reduced denominator and $g$ its odd count. Cyclicity makes $q$ constant and prime to six, and the positive cycle product gives $\rho=3^g/2^D<1$. Use $K$ nonempty separated reference arcs of endpoint height at most $H$ around the full circle. Write $M$ for the least physical boundary value. If $M>H$, multiplying the relative transports about the cycle gives

$$
  \rho=\prod_i\frac{x_i-\eta_{i-1}}{x_i-\xi_i}
       \ \ge\ \left(\frac{M-H}{M+H}\right)^K
       \ \ge\ 1-\frac{2KH}{M+H}.
$$

Thus $M\le2KH/(1-\rho)$, also true if $M\le H$. This small-boundary step is prior work. Theorem 1 of Bondareva, Luchin and Salikhov, at $(h_1,h_2,h)=(D,-g,0)$, gives $D\ln2-g\ln3>D^{-4.116201}$ for all sufficiently large $D$. Since $1-e^{-v}\ge \min(v/2,1/2)$ for $v>0$, this gives $\log_2(1/(1-\rho))=O(\log(D+1))$. Cut at $M$ in (10) and use $K\le D$. For an absolute constant $c_0>0$,

$$
   1+\log_2 q+\log_2H+\log_2(D+1)
       \ \ge\ c_0 D\exp\!\left(-A\frac{K+1}{\ln(K+2)}\right).       \tag{11}
$$

In particular, if $q$ is polynomial in $D$ and $\log_2H\le D^\theta$ for fixed $\theta<1$, then $K\gg_\theta\ln D\,\ln\ln D$. The fixed-$K$ sharp denominator-rate and clock-spectrum results for these closed arcs remain those of PR212. The different conclusion in (11) controls growing numbers of arbitrary reference arcs and permits growing reference height. [PR212, effective small-boundary argument](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/ARC_HEIGHT.md) · [Bondareva, Luchin and Salikhov, Theorem 1, printed p. 18](https://www.mathnet.ru/eng/cheb619)

The [exact normalization checker](check_quantitative_reference.py) tests 560 ordinary packets with differing signed rational endpoints, including 450 common reference scales divisible by six. It directly multiplies the local norms after primitive scaling and checks (5), the gcd component bounds, rooted height bounds on the 397 high-boundary examples, and the ordered monomial coefficient normalization. In 304 cases the scaling gcd has a nontrivial prime-to-six part. Proper zero subsums remove 440 nonzero coordinates. Another 168 positive rational packets check the full scaled integer argument, including 96 which lose factors of three from their reduced denominator. These finite computations check the algebraic inputs. They do not validate the external interval theorem or its asymptotic record charge.
