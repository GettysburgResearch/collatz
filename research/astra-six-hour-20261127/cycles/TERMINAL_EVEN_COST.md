# Exact first-hit even cost on fixed Mersenne visitors

Put \(j=11+162m\), \(N=2^j\). Grant every \(2^U N-1\), \(U\ge0\), as a possible bad lower start. A visitor uses a fixed finite word of legal ordinary forward and inverse shortcut edges from one of those starts and has the form \(y=\alpha N-b\). The offset and word are fixed on their ternary cylinder. The conjectural exceptional source supplies only some of the starting labels. The larger supply strengthens this obstruction to a fixed-word argument. [Earlier all-offset definition](../ordinary/LATER_STARTS.md)

Write \(E(3y)\) for the number of even departures up to the first ordinary visit to one. At the ternary point \(N_*=590\), among **all** visitors legal there with \(E(3y)\le j+4\) on arbitrarily large members of their cylinder, precisely two forms qualify. Both have \(U=0\), and both work on the entire \(j=11\bmod162\) progression. The first row is the unique minimum in the lexicographic order of even cost and source height for this class at that ternary point.

| Lower source \(y\) | Upper odds to first one | \(E(3y)-j\) | Lower clocks to \(N-1\) | Upper clocks to \(N/4\) |
|---|---:|---:|---:|---:|
| \((256N-623)/243\) | 4 | 4 | 8 | 10 |
| \((128N-271)/81\) | 3 | 4 | 7 | 9 |

The same two rows exhaust the class on **every** progression residue if the upper first-hit odd count is at most six. There are nine residues of \(N\bmod3^7\) with \(N=104\bmod243\). The all-grade assertion at 590 also detects a hypothetical word giving a subfloor visitor with more than six upper odds. The all-nine finite numerator check here includes only grades one through six.

## The terminal slope

Cancel backward-then-forward edges in a visitor. The word goes forward \(h\ge0\) times from \(2^U N-1\), then backwards with \(q\) odd inverses and \(A\) even inverses. For sufficiently large \(j\) all \(h\) forward inputs are odd. Put \(d=q-h\). The lower slope and signed center satisfy
\[
        \alpha=2^{A+U}(2/3)^d,\qquad 1\le b\le2^A.
\]
Indeed the reflected signed center starts at 1 before the inverse part. Even inverses double it and odd inverses send \(v\) to \((2v+1)/3\), which lies in \([1,v]\) for \(v\ge1\). The source center has odd denominator a power of three. At a ternary unit where the word is legal, \(d\le0\) implies that \(b\) is an integer. For \(d>0\), \(b\) in lowest terms has denominator exactly \(3^d\), since \(\alpha N-b\) is ternary-integral there.

Suppose \(3y\) reaches one with \(p\) odd inputs and \(E\) even inputs. Multiplying its shortcut factors gives \(3y(3/2)^p\le2^E\). Thus \(p\) is bounded on any fixed positive-slope form at cost \(E\le j+4\). There is at least one odd input because the initial positive integer is divisible by three. In particular \(\alpha\le32/9\).

For every fixed number of steps the upper parities agree, for all large \(j\), with those of the dyadic signed start \(-3b\). A uniform upper odd bound forces this signed trajectory to hit zero. Otherwise it would have infinitely many odd inputs, since a nonzero dyadic integer has finite two-adic valuation. The finite first-hit clocks of the physical starts tend to infinity because the starts do. An ordinary nonzero integer cannot reach zero, which excludes \(d\le0\).

For \(d>0\), exactly \(p=d-1\) odd steps bring \(-3b\) to zero. Its denominator initially equals \(3^{d-1}\). An odd step removes precisely one factor of three while a factor remains. Once it has become an ordinary integer, only zero itself can reach zero. Write \(\alpha=2^e/3^d\). At the signed zero clock \(H\) the physical upper is exactly \(2^{j+e-H}\). All preceding physical inputs exceed one for large \(j\), and the remaining steps are halvings. Therefore
\[
                 E(3y)=j+e-d+1=j+A+U+1.
\]
This formula uses the full first-hit terminal and permits arbitrarily long final halving runs.

## Two exact enumerations

For the all-grade result, apply the earlier signed-center clearing proof with cap \(32/9\). At \(N_*=590\), every possible positive-depth word gives an ordinary readout \(x=590\alpha-b\) between 1 and 2097. Until the signed center has cleared its denominator, the positive \(x\) has the same parities and reaches an actual integer of the form \(590\,2^{U+B}-v\), where \(v\) reaches 1 under the reflected map in exactly \(B\) even departures and \(1\le v\le2^B\). This follows by following the first \(d\) odd steps and paying the used even letters, exactly as in the cap-\(128/81\) reduction. Enumerate every first-hit orbit of the 2097 possible \(x\), and every \(U,B\) satisfying \((590\,2^U-1)2^B\le T^t x<590\,2^{U+B}\). The later two-cycle lies below 589. Reconstruct the slope \(2^{t+B+U}/3^{P_t(x)}\), test the reflected budget and retain the physical cap and signed center bound. The maximum clock is 115, the largest site is 638468 and \(U\le10\). This safe superset has 26 distinct forms. Exactly five have signed upper center reaching zero. In increasing slope their scores are \(4,4,5,6,5\), leaving the displayed rows. The checker verifies their actual lower and upper affine paths independently. [Signed-center clearing proof](../../astra-unconventional-20261126/renormalization/FINITE_COVER_BARRIER.md) · [Exact replay](check_cost_590.py) · [Receipt](../../../reports/astra-six-hour-20261127/cycles/cost-590.json)

For the nine-class check there is a direct terminal parameterization. Write \(\sigma=E(3y)-j\). For grade \(1\le p\le6\) one has \(1\le\sigma\le4\), \(0\le U<\sigma\), \(A=\sigma-1-U\), and
\[
 y={2^{p+\sigma}N-M\over3^{p+1}},
 \qquad
 1<b={M\over3^{p+1}}\le2^A,\quad 3\nmid M .
\]
The strict initial bound follows from the exact denominator. Enumerate the integers \(M\) in this finite interval satisfying \(M=2^{p+\sigma}N\bmod3^{p+1}\) on at least one of the nine classes. Retain only those for which the reflected trajectory from \(b\) reaches 1 with exactly \(A\) even inputs and the signed upper from \(-3b\) reaches zero. The reflected test ends as soon as its value exceeds \(2^{\text{remaining budget}}\). At odd steps its distance from one grows by \(3/2\), so a consecutive odd stretch away from one cannot delay this test indefinitely. The two displayed forms pass on every residue, and no others survive. This is independent of the 2097 ordinary test orbits and of a signed inverse-prefix enumeration.

The assertion concerns a fixed lower-connection word at each cylinder. A minimizing actual disagreement could be connected by words depending on the exponent, or lie in a different bad component. Its sparse upper odd positions can vary with \(j\).
