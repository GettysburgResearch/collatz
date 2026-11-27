# A sharp one-sided obstruction with an actual floor and a certified upper arm

**Proposed written theorem.** Put \(\alpha=\log_3 2\) and
\(\theta=H_2(\alpha)\). For all large \(H\) there are at least
\(2^{\theta H}/H^C\) distinct \(H\)-clock lower words with all of the
following properties. The absolute constant \(C\) is independent of
the source's prescribed ternary cylinder.

* The lower path has exactly \(\lceil\alpha H\rceil\) odds, and
  \(3^{a_t}\ge2^t\) at every clock \(0\le t\le H\).
* For each prescribed \(A>0\) the words can be chosen so that their
  **native** positive representatives \(2^H\le Y<2^{H+1}\) obey
  \(T^H(3Y-1)\le Y/H^A\) and \(Y\le T^H Y\le4Y\). The counting
  constant \(C\) may depend on \(A\). Both ordinary paths are distinct
  through all these clocks.
* The paired paths \((Y,3Y-1)\) have distinct affine germs throughout.
  They admit arbitrarily large positive ordinary realizations in **any**
  prescribed ternary source class, with genuinely distinct ordinary
  states at every common clock.
* In those realizations every lower state through \(H\) is at least
  its own original \(Y\), and the upper state at clock \(H\) is a
  power of two. The complete upper orbit therefore reaches 1. For
  each word the terminal lower height divided by \(Y\) tends to
  \(3^{\lceil\alpha H\rceil}/2^H\in[1,3)\) as its lifts grow.

Consequently a superpolynomial improvement on \(2^{\theta H}\)
requires more than this single arm's full native-time floor and the
other arm's true convergence certificate. The [two-arm estimate](HELLINGER.md)
does obtain such an improvement when both arms meet the critical
odd-frequency threshold. The unconstrained heights of the positive
lifts and the finite lower time horizon are essential qualifiers here.

## Steering to negative rank at logarithmic cost

Use the signed affine rank \(r=1+b-a\) and integral carry \(c\).
Start with two lower odd bits. The states after them are \((0,-1)\)
and \((-1,-2)\), respectively. At the latter state any further common
odd bit fixes the state. Each of these initial lower odds adds
\(\log(3/2)>0\) to \(\log(3^{a_t}/2^t)\).

Fix \(R\ge2\). From rank \(-j\), if the carry is even, expose a mismatch
within at most \(e_j+1\) common clocks, where
\(e_j=v_2(3^j-1)\). In fact each step below valuation \(e_j\) removes
one factor of two; at or above it one of the bits gives valuation
\(e_j-1\). With an odd carry choose lower bit 1, upper bit 0 to
reach rank \(-j-1\). The carry cannot vanish at a nonzero rank in
this physical chart. The whole steering word to rank \(-R\) uses
at most \(\sum_{1\le j<R}(e_j+2)\ll R\) clocks. Here \(e_j=1\) for
odd \(j\); for even \(j\), \(e_j=2+v_2(j)\). The bound follows by
summing the powers of two dividing the integers up through \(R\).

Prepend \(O(R)\) stationary lower odds at \((-1,-2)\) to pay for the
worst possible loss of \(\log2\) per steering clock. The complete
initial prefix of length \(L=O(R)\) then has nonnegative homogeneous
log-gain at **every** prefix, including all of the prescribed descent
in rank. No merger occurs in this prefix.

## A prescribed grade and the physical floor

Now use independent lower bits of probability \(\alpha\) on the
remaining \(n=H-L\) clocks. At each mismatch the rank increases with
probability \(1-\alpha\), decreases with probability \(\alpha\).
Mismatch selection occurs before revealing its bit, so an independent
mismatch-bit stream yields an ordinary biased simple walk, continuing
the stream even if the observed pair stops. The probability of ever
reaching zero from \(-R\) is at most
\(\eta^R\), \(\eta=(1-\alpha)/\alpha<1\). More generally the
probability of coming within \(R/2\) of zero is at most
\(\eta^{\lfloor R/2\rfloor}\). This is the usual
finite-interval gambler's-ruin probability in the increasing-interval
limit. Avoidance of zero precludes an affine merger on the remaining
segment.

Write \(a_*\) for the initial prefix odd count and prescribe the
remaining count \(p=\lceil\alpha H\rceil-a_*=\alpha n+O(R)\). Take
\(R=\lceil K\log H\rceil\) with \(K\) fixed sufficiently large that
\(\eta^{\lfloor R/2\rfloor}\le H^{-3}\) and
\(3^{R/2}\ge 20 H^A\). For all sufficiently large \(H\), \(0<p<n\);
Stirling gives \(\Pr(\operatorname{Bin}(n,\alpha)=p)\gg n^{-1/2}\)
uniformly in this \(O(\log H)\) neighborhood.

Among such words at least a fraction \(1/n\) of the words have all
their prefix log-gains at least \(\min(0,T)\), where
\(T=p\log3-n\log2\) is their common total. To see this, rotate any
word immediately after a minimum of the prefix sums at the indices
\(0,\ldots,n-1\). Before wrapping the sums are nonnegative, except
possibly the segment ending exactly at the original word's endpoint,
whose sum is at least \(T\); after wrapping they are at least \(T\).
Counting rotation pairs gives the fraction bound even for periodic
words. The previous buffer is nonnegative and its sum with \(T\) is
nonnegative by the prescribed total grade. Thus every such concatenated
word retains the full homogeneous lower floor.

The resulting tail event has probability \(\gg n^{-3/2}\). Subtract
the probability \(H^{-3}\) of approaching rank zero within \(R/2\). Independence
of these two events is unnecessary. All retained tails have the same
individual probability
\(\alpha^p(1-\alpha)^{n-p}=2^{-\theta n}H^{O(1)}\); and
\(H-n=O(\log H)\). This proves the claimed polynomial-loss lower count.
The exact one-arm binomial count gives the matching exponential upper
rate.

For the native representative, the final upper grade satisfies
\(b\le a-R/2\) since \(1+b-a\le-R/2\). The elementary affine offset
bound used in [the first-passage calculation](CRITICAL_FLOOR.md) gives
\[
 T^H(3Y-1)\le 3^b(2^{-H}3Y+1/3)
 \le 10\,3^{-R/2}Y,\qquad
 T^H Y\le 3^a(2^{-H}Y+1/3)\le4Y
\]
as \(Y\ge2^H\) and \(3^a<3\cdot2^H\). The lower floor and the terminal
separation disallow any earlier ordinary meeting. Each lower word has
one distinct representative in this native octave. One can also impose
a fixed ternary source class by taking a representative between
\(2^H\) and \((1+3^L)2^H\) for a modulus \(3^L\), preserving both bounds.
At native height this certifies a strict upper descent. The next
paragraph provides actual eventual upper convergence on other lifts.

## Ordinary lifts with an upper hitting certificate

Fix any resulting pair of parity words. Let \(b\) be the upper grade
and \(A_u\) its affine numerator, so the upper terminal is
\((3^b(3Y-1)+A_u)/2^H\). To obtain terminal \(2^j\), it suffices to take
\[
         Y=\frac{2^{H+j}-A_u+3^b}{3^{b+1}} .
\]
For \(b>0\), \(A_u\) is a ternary unit by its last odd contribution;
for \(b=0\), \(A_u=0\). In either case \(A_u-3^b\) is a unit modulo
\(3^{b+1}\). Powers of two run through all these units by
\(v_3(4^k-1)=1+v_3(k)\). Thus suitable \(j\ge0\) exist in one class
modulo \(2\cdot3^b\). Integrality certifies every parity bit of the
upper word since the affine congruence modulo \(2^H\) fixes its unique
binary entrance class. Multiplication by three and translation by
minus one are invertible modulo \(2^H\), so the lower word is the
given one as well.

As \(j=j_0+2\cdot3^b k\) varies, the valuation of the difference
of two \(Y\)'s is exactly \(v_3(k-k')\), again by the same elementary
lifting formula. The \(Y\)'s cover every ternary cylinder and do so
at arbitrarily large positive heights. The affine lower value at
each clock is \(3^{a_t}2^{-t}Y+A_{\ell,t}2^{-t}\), with
\(A_{\ell,t}\ge0\). This proves the lower floor and terminal ratio.
Distinct affine germs at each of the finitely many clocks can
coincide on at most one source each; increasing the lift beyond
these finitely many accidental meetings ensures literal separation.
