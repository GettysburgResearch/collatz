# Prime parts of the literal carry on one ordinary orbit and its completions

**PROPOSED written theorems.** Use the shortcut map \(T(2a)=a\) and \(T(2a+1)=3a+2\). Fix an ordinary integer \(n>0\). Write \(x=T^kn\) and let \(p\) count the odd inputs in these \(k\) steps. Fix a finite set \(S\) of primes containing 2 and 3. For a positive integer \(v\), write \(v_{S'}\) for its complete part outside \(S\) and \(v_S=v/v_{S'}\).

## The actual prefix

Let \(A=2^kx-3^pn\) be the carry of the original orbit. Once the path has an odd input, \(A>0\). At every sufficiently large clock,

\[
 \log A_{S'}\ \ge\ k\log 2+\log x_S-o(k),\qquad
 \log A_S\ \le\ \log x_{S'}+o(k).                                      \tag{1}
\]

In particular, along **any** sequence of clocks with \(\log x=o(k)\), the outside part of this actual integer carry has \(\log A_{S'}/k\to\log 2\), and \(\log A_S/k\to0\). This includes any subexponential-return subsequence of a putative escaping orbit. The existence of such a subsequence is not presumed.

Indeed \(2^kx=3^pn+A\) is a nondegenerate positive row. Its common content \(g\) divides \(n\), since every iterate after the first odd branch is a ternary unit. Put \(H=2^kx/g\). For every \(0<\epsilon<1\), Evertse's Corollary 1 gives

\[
 c_{S,\epsilon} H^{1-\epsilon}\le n_{S'}x_{S'} A_{S'}.
\]

This is the integer version for glued signs and collective gcd one. The signed coordinates sum to zero, and a proper nonempty subsum cannot vanish since the positive summands exhaust the sole negative coordinate. Apply the published result with its threshold constant one and absorb its finitely many exceptional primitive tuples in \(c_{S,\epsilon}>0\). Dividing every coordinate by \(g\) may only reduce the product of its outside parts. The physical bound \(2^kx\le4^pn\le4^kn\) controls \(H\) exponentially in \(k\). Thus \(A_{S'}\ge c_{n,S,\epsilon}\,2^kx_S(4^kn)^{-\epsilon}\). Let \(\epsilon\) decrease after taking limits. The upper bound on \(A_S\) follows from \(A\le2^kx\).

A direct test for the critical case would seek a prime \(q\ge5\) and a constant \(\eta>0\) with \(2^kx\equiv3^pn\pmod{q^{\lceil\eta k\rceil}}\) at arbitrarily large subexponential-return clocks of a hypothetical escape. Equation (1) excludes that event. Ordinary integrality and a height-return hypothesis alone do not establish it. At \(n=1\), for example, \(A_{2j}=4^j-3^j\); every fixed prime outside six has valuation \(O_q(\log j)\) by its multiplicative order and the lifting-the-exponent identity.

## A four-coordinate row for every positive completion

Suppose \(m=n+2^kt\), \(t\ge1\), and a genuine suffix of length \(l\) with \(h>0\) odd inputs takes \(y=x+3^pt\) to 1. Let \(C>0\) be the **entire literal suffix carry**. For every \(0<\epsilon<1\) there is a constant \(c=c(S,\epsilon)>0\), independent of the source, word, depth and clocks, such that

\[
                 x_{S'} C_{S'}\ \ge\ c\,3^{p+h}2^{-\epsilon l}.           \tag{2}
\]

The number of odd inputs, transitions, periodic blocks or signed atoms can be arbitrary. The proof uses four coordinates in every case. The complete integer row is

\[
                  2^l=3^{p+h}t+3^hx+C.
\]

Its positive form rules out all proper zero subsums even if some entries coincide. Its content \(g\mid2^l\) is a power of 2, and \(g\mid3^{p+h}t\) gives \(g\mid t\). The maximum primitive coordinate is \(H=2^l/g\). The product of the four primitive outside parts is **exactly** \(t_{S'}x_{S'}C_{S'}\). Since \(g\mid t_S\), we have \(H\ge3^{p+h}t_{S'}\). Evertse gives \(t_{S'}x_{S'}C_{S'}\ge cH^{1-\epsilon}\), proving (2). If \(h=0\), use the three-coordinate row without \(C\). It gives \(x_{S'}\ge c3^p2^{-\epsilon l}\), incompatible with \(x/3^p\le n(2/3)^k\) at large \(k\) when \(l\le Bk\) for fixed \(B\).

In particular, for **all** such distinct lifts with \(l\le Bk\), uniformly as \(k\to\infty\),

\[
 \log C_{S'}\ \ge\ (p+h)\log3-\log x_{S'}-o(k)
             \ \ge\ k\log(3/2)+h\log3-o(k).                             \tag{3}
\]

At a subexponential-return clock the first bound is \((p+h)\log3-o(k)\). The proof works unchanged with a uniformly bounded number of contiguous physical blocks in place of the whole suffix. In the row, each nonzero block carry acquires only a power of two and a power of three. The product of their outside parts replaces \(C_{S'}\). The dimension of this extension depends on the bound for the number of blocks. Formula (2) itself has no such condition.

There is also a pointwise consequence for the smallest odd input **strictly before the first hit of 1** from \(y\). Truncate the given suffix at that first hit, with length \(l_0\le l\), odd count \(h_0\le h\) and carry \(C_0\). When \(h_0=0\) the truncated suffix consists entirely of halving steps and has no such minimum. The preceding three-coordinate argument excludes that case for all sufficiently large \(k\) if \(l\le Bk\). Suppose \(h_0>0\) and write \(M\) for this minimum. Multiplying the actual factors on the truncated path gives

\[
 1+\frac{C_0}{3^{h_0} y}
   =\prod_{z\text{ odd input before the first hit}}\left(1+\frac{1}{3z}\right)
   \le \exp\!\left(\frac{h_0}{3M}\right).
\]

Taking \(c\le1\) in (2) for the truncated path, the left side is at least \(1+b_0\), where \(b_0=c2^{-\epsilon l_0}/(x_{S'}(t+x/3^p))\le1\). Since \(\log(1+b_0)\ge b_0/2\), this gives the finite, ineffective inequality

\[
 M\ \le\ \frac{2h_0}{3c}\,2^{\epsilon l_0} x_{S'}(t+x/3^p)
   \ \le\ \frac{2h}{3c}\,2^{\epsilon l} x_{S'}(t+x/3^p).
\]

When \(l\le Bk\) it implies \(\log M\le\log t+\log x_{S'}+o(k)\), even though the suffix began at \(x+3^pt\). A suffix ending at a power \(2^a\) may be completed by \(a\) halving steps and then truncated at its first 1; the asymptotic statement uses \(l+a\le Bk\). The forced small odd value belongs to the competitor's path.

The failure of a dimension-independent bound is already unconditional on the actual orbit of 1. For its first \(2j\) steps, the expanded positive row is
\[
             4^j=3^j+\sum_{i=0}^{j-1}4^i3^{j-1-i}.
\]
It has collective gcd one, no vanishing proper subsum, and every coordinate is supported on \(\{2,3\}\). Its outside product equals 1 while its height is \(4^j\). PR192 already identifies this increasing-dimension obstruction. In (1) the single carry \(4^j-3^j\) is retained as a coordinate; its outside factor supplies the required mass. [PR192, fixed-source analysis, §6](https://github.com/GettysburgResearch/collatz/blob/26f070c38ad9edd21ed7dac6efaab6554550c2a3/research/astra-closure-attack-20261124/FIXED_SOURCE.md).

The imported Diophantine input in (1)–(3) is [J.-H. Evertse, *On sums of S-units and linear recurrences*, Corollary 1, printed p. 227, (9)–(12)](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf). It fixes the dimension. Quantitative Subspace Theorems bound exceptional *subspaces* for a stated dimension and height system; they do not turn an unbounded literal list of odd positions into a fixed-dimensional tuple. The estimates here absorb the entire uncompressed carry as one coordinate and explicitly retain its outside part. [J.-H. Evertse and R. G. Ferretti, *A further improvement of the Quantitative Subspace Theorem*, 2013](https://doi.org/10.4007/annals.2013.177.2.4).

## An arbitrary number of powered blocks on the paired witness family

This counting statement applies to any fixed prefix and any family of at least \(e^{ck}\) distinct lifts reaching 1 with first-hit suffix length at most \(L=\lfloor Bk\rfloor\). Round eight obtains such a family simultaneously on both arms under its explicitly named analytic input F. Fix one arm. At a prescribed prefix the map from a suffix word ending at 1 to its displacement is single-valued by the exact integer row. Thus an upper bound on word counts is also an upper bound on distinct lifts.

Suppose a word admits a factorization \(u_1^{d_1}\cdots u_s^{d_s}\) of positive powers of nonempty binary words with total root length \(r=\sum |u_i|\). The root letters have \(2^r\) choices, their boundaries have at most \(2^{r-1}\) choices, and the positive exponents have sum at most \(L\). For a given \(s\) the last condition gives \(\binom{L}{s}\) choices by summing the composition counts. If \(R\le L/2\), at most

\[
            (R+1)4^R\binom{L}{R}
\]

words of length at most \(L\) have some representation with \(r\le R\), including the empty word. For \(R=\lfloor\delta k\rfloor\), \(0<\delta<B/2\), its logarithm divided by \(k\) is at most \(\delta\log4 + B H(\delta/B)+o(1)\), with \(H(s)=-s\log s-(1-s)\log(1-s)\). This tends to zero with \(\delta\). An initial segment of any represented word still admits a representation of cost at most \(2r\): split its last, possibly incomplete power into full copies and at most one proper root prefix.

Choose \(\delta\) so the exponent bound is strictly below \(c/2\). Apart from at most \(2 e^{ck/2}\) of the simultaneously supplied pairs at large \(k\), **each arm and every stopping continuation**, even one taking extra laps after the first 1, requires total root length at least \(\delta k/2\) under *any number* of powered blocks. In this conclusion the number of blocks can grow freely, while an exponentially smaller exceptional family is retained. Round eight's different arithmetic statement applies to every witness with a fixed block budget. [Round-eight paired construction and its quantifiers](../../round8/paired/CROSS_ROUTE.md).

A stronger-looking replacement by ordinary program-description length fails in this setting. Under F, fix \(n\), an integer witness-octave exponent \(D\) from the paired construction and an integer time multiplier large enough for its two hit bounds. Given \(k\), exhaust the finite octave in increasing order, check the two congruences, both hit times and a common clock \(j\le40(k+1)\) with \(T^j m=T^j(3m)\) by direct simulation, and output the first qualifying lift's actual first-hit suffix. This one fixed program succeeds at every sufficiently large \(k\). Its output has conditional plain Kolmogorov complexity \(O_n(1)\) given \(k\), despite the strict displacement, exponential source scale, and the round-eight fixed-block linear lower bound. In particular, replacing the arithmetic description requirement by unrestricted computability does not force the lift to equal the positive anchor. The construction already applies at \(n=1\) under the same external F.

## Repetition on the same critical trajectory

Let \(x_i=T^i n\) on an injective positive orbit, and let \(P(L)\) count its distinct length-\(L\) factors in the binary parity word. Equal length-\(L\) words force the starting values to agree modulo \(2^L\). Consequently **all** distinct orbit states below \(2^L\) give different length-\(L\) factors. Dubickas's Theorem 5 gives the unconditional eventual bound \(P(L)>1.70951129L\) on a divergent positive orbit. [A. Dubickas, *On integer sequences generated by linear maps*, Glasgow Math. J. 51 (2009), pp. 243–252, Theorem 5](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C40C0C07FEC20797475BB2899C436C9A/S0017089508004655a.pdf/on_integer_sequences_generated_by_linear_maps.pdf).

If \(\log x_i=o(i)\), then for every fixed \(B\), all states through \(\lfloor BL\rfloor\) lie below \(2^L\) once \(L\) is sufficiently large. Thus even the length-\(L\) words at the first \(\lfloor BL\rfloor+1\) positions are all distinct and \(P(L)/L\to\infty\). Critical *limiting* odd frequency \(p_i/i\to\log_3 2\) implies this subexponential height: the exact logarithmic step product has correction at most \(\tfrac13\sum_{j<i}1/x_j\le(1+\log i)/3\) by injectivity. This direction gives a restriction opposite to the desired recurring-prefix compression.

A single sequence of subexponential returns, \(\log x_{k_j}=o(k_j)\), already gives \(\limsup P(L)/L\ge 1+2/\log_2(3/2)=4.4190\ldots\). Choose integers \(L=L_j\to\infty\) with \(\log_2(x_{k_j}+1)=o(L)\) and \(L=o(k_j)\), for instance by rounding the geometric mean of \(k_j\) and \(1+\log_2(x_{k_j}+1)\). Put \(d=\log_2(3/2)\) and fix \(0<\eta<1\). From \(x_{i+1}+1\le (3/2)(x_i+1)\), the initial interval of length \(\lfloor(1-\eta)L/d\rfloor\) and the same number of clocks immediately following \(k_j\) lie below \(2^L\) eventually. From \(x_i\le2x_{i+1}\), another \(\lfloor(1-\eta)L\rfloor\) preceding clocks at \(k_j\) do as well. Choose the index ranges without repeating \(k_j\); the two groups around 0 and \(k_j\) are disjoint since \(L=o(k_j)\). Each of these states contributes a distinct word. Divide by \(L\) and let \(\eta\downarrow0\). A sparse return subsequence gives this limsup statement, not the preceding all-\(L\) limit.

## Relation to other work and verification

PR192's FS2 studies the outside parts of the **two moving endpoints at a fixed odd clock**. Its FS4–FS5 study signed or unsigned presentations of a forward carry over proportional windows. PR205's periodic companion denominator is a different integer. PR206's sparse-defect theorem groups exceptional gaps on balanced rows; its conclusion concerns the number of unit gaps. None of those results is used as a pointwise upper bound on \(C_{S'}\). [PR192 fixed-source analysis](https://github.com/GettysburgResearch/collatz/blob/26f070c38ad9edd21ed7dac6efaab6554550c2a3/research/astra-closure-attack-20261124/FIXED_SOURCE.md) · [PR205 arithmetic packet](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/arithmetic/README.md) · [PR206 sparse-defect theorem](https://github.com/GettysburgResearch/collatz/blob/37d2b5d644664a746891042c199e58cfb06f1176/research/clock-itineraries/SparseDefects.md).

[LiteralCarry.lean](LiteralCarry.lean) checks positivity-based nondegeneracy, preservation of ternary units after an odd step, the original and lifted content estimates, the primitive height gain, uniqueness of the lift for a fixed word, the physical correction-product bound, and injectivity of parity words on the first binary block. It imports the ordinary map and parity reader from PR206's pinned `TernaryItinerary`. Evertse, the limiting estimates and the coding argument are written mathematics. [Exact finite controls](check.py) · [Control output](../../../../reports/astra-global-closure-20261124/round9/arithmetic/controls.json).

**Open.** A critical fixed source can have a carry whose entire logarithmic mass lies outside every fixed finite prime set, and its short convergent competitors can do the same. No argument forces an injective exceptional source to have the high fixed-prime divisibility forbidden by (1), or forces any of its competitors to return to its own component. Replacing the carry by one coordinate identifies what the fourth coordinate pays; it does not settle Collatz.
