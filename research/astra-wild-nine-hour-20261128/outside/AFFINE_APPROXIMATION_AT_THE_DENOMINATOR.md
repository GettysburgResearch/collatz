# The denominator threshold in affine real approximation

**SOURCE-QUALIFIED external approximation rate and elementary exact tests.** Javaheri's November 2026 preprint, Theorem 3.8, treats unrestricted compositions of \(u\mapsto u/a\) and \(u\mapsto bu+1\) on the positive reals. The paper's Collatz illustration uses \(a=2,b=3\), the two raw maps without parity guards. The specialization **\(a=2,b=3/2\)**, conjugated by \(u=2x\), instead yields the two shortcut maps \(F_0(x)=x/2\), \(F_1(x)=(3x+1)/2\). For positive real \(x,y\) the preprint gives infinitely many words \(w\) of increasing length \(t\) with
\[
 |F_w(x)-y|\le C_{x,y}\lambda^{-t},\qquad
 \lambda=\exp((\log2)^2/\log6).
\]
This is a statement about those real affine values. No local numerical test below is a replay of the preprint. [Javaheri, Theorem 3.8, arXiv:2611.03778](https://arxiv.org/abs/2611.03778)

For positive integers \(x,y\), if one such word *lands integrally* it is the actual parity word of \(x\). At a first wrong letter the valuation at two falls to \(-1\); both maps thereafter decrease it by exactly one at every tick. In particular if \(\ell<t\) initial letters were correct, the reduced denominator of \(F_w(x)-y\) is exactly \(2^{t-\ell}\). If \(\ell=t\) the difference is integral. This integrality property distinguishes the shortcut pair from the permitted even applications of the raw odd map in the paper's illustration. Affine-word membership and the existence of a source-to-target word were already separated in PR215. [Pinned decoder](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/phase4/AFFINE_MEMBERSHIP.md)

It follows that the original positive \(x\) reaches \(y\) if the displayed real approximation holds along words with
\[
     \ell-(1-\log_6 2)t\longrightarrow+\infty .
\]
Indeed for large \(t\) the real error is then strictly smaller than \(2^{-(t-\ell)}\). An even weaker sufficient condition uses simultaneous ternary approximation. For a proposed word take \(\ell\) as above and any \(j\ge0\) such that \(F_w(x)-y\in3^j\mathbb Z_3\). Whenever the difference is nonzero,
\[
                  2^{t-\ell}3^{-j}|F_w(x)-y|_\infty\ge1 .
\]
Multiplication by \(2^{t-\ell}\) gives an ordinary nonzero integer divisible by \(3^j\). Thus \((\ell-(1-\log_6 2)t)\log2+j\log3\to+\infty\) suffices under the stated real rate. The preprint supplies neither the true-prefix length nor this joint bound.

The constant one in the last integer test is exact even if the same fixed positive source and target are used, both the physical prefix and the replayable target suffix grow, and the real and ternary errors tend to zero. Start at \(x=y=1\). Follow any \(2j\) true ticks, returning to one. Use the wrong even branch to reach \(1/2\). Apply \(k\) copies of the true target word \(10\), whose affine map is \(v\mapsto(3v+1)/4\). The resulting difference is \(-3^k/2^{2k+1}\). Here \(t=2j+1+2k\), \(\ell=2j\), and its ternary valuation equals \(k\), so the product in the test is exactly one. Its large true prefix does not repair the intervening wrong letter. This sharpness example is for the integer test; the external exponential rate for the *total* word length is not asserted for this family.

One idea to select better approximants is to force congruences to many nearby ordinary points already known to reach one quickly. On the actual forward orbit such simultaneous tests obey the [uniform short-predecessor obstruction](CONGRUENCES_TO_SHORT_PREDECESSORS.md). Another is to use atoms of a forward empirical law to extract exact rational recurrence. The [atomic theorem](ATOMS_OF_ORDINARY_TIME_AVERAGES.md) determines the rational phase, including otherwise hidden ordinary denominator primes, but still permits diffuse components. Neither result proves that the approaching unrestricted words cross the strict denominator threshold for each fixed source.
