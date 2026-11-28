# Whole valuation classes attain the first possible earlier-peak clock

For each row below, every canonical exponent \(m=11+162j\) with \(v_2(3^{m+1}-1)=J\) has its **first possible meeting with any earlier peak exactly at postpeak deadline \(J+1\)**. The particular peak \(3^{m-d}-1\) and \(3^m-1\) meet then at equal clocks, with the earlier arm accumulating exactly \(d\) additional odd departures. Every earlier exponent misses *every* independent pair of clocks through \(J\). These conclusions concern each original input in a full residue class of \(j\).

In the thirteen paid rows, the original \(z=(2^{m+7}-271)/81\) meets a strictly smaller canonical \(Y\equiv17\bmod48\), with \(2^{d-c}Y<z\). Its triple reaches one with three odd departures at a clock of at most \(m-(d-c)\). The two small rows also attain the first possible peak clock. Their indicated earlier exponents cost more than their gaps under the price table. [PR206 ordinary canonical return and actual price](https://github.com/GettysburgResearch/collatz/blob/640bf7e511831a0ffc4f00462f12df81f8a8a619/research/clock-itineraries/ReturnDescentRows.lean)

| \(J\) | Earlier gap \(d\) | Price \(c\) | Proved height saving, bits | Cofactor residue \(a\) |
|---:|---:|---:|---:|---:|
| 28 | 12 | 1060 | — | 19 |
| 70 | 36 | 432 | — | 37 |
| 856 | 420 | 19 | 401 | 19 |
| 926 | 448 | 30 | 418 | 49 |
| 1018 | 504 | 185 | 319 | 19 |
| 1736 | 886 | 10 | 876 | 49 |
| 1990 | 1038 | 245 | 793 | 19 |
| 3310 | 1648 | 12 | 1636 | 37 |
| 3592 | 1810 | 12 | 1798 | 19 |
| 8882 | 4450 | 10 | 4440 | 49 |
| 9172 | 4570 | 35 | 4535 | 19 |
| 15280 | 7614 | 7 | 7607 | 37 |
| 24346 | 12226 | 10 | 12216 | 19 |
| 31132 | 15676 | 30 | 15646 | 19 |
| 34048 | 17038 | 12 | 17026 | 19 |

**Why each row covers the whole class.** A hard exponent has \(6\mid m+1\). For even \(m+1\), successive squaring gives \(v_2(3^{m+1}-1)=2+v_2(m+1)\). Thus valuation \(J\) is equivalently \(m=12\cdot2^{J-4}r-1\) with \(r\) odd. Its canonical congruence says \(2^{J-4}r\equiv1\bmod27\). Consequently the complete family is \(r=a+54n\), \(n\ge0\), for the indicated least positive odd residue \(a\). In the row-index variable, \(m_j+1=6(2+27j)\), so exact valuation \(J\) specifies one residue class of \(j\bmod2^{J-2}\).

**The symbolic edge.** Let \(U=(3^{m+1}-1)/2^J\), an ordinary positive odd integer. The first \(J\) parities of the upper peak match those of \(-2/3\), whose initial even and odd departures reach zero, followed by even departures. Changing the initial value by \(2^JU/3\) adds exactly \(U\) at the endpoint. Thus the actual upper arm reaches \(U\) at \(J\) with one odd departure. For the lower signed seed \(\gamma_d=3^{-d-1}-1\), each table row has
\[
                        T^J\gamma_d=1,\qquad p_J(\gamma_d)=d+2.
\]
The actual earlier peak differs from this seed by \(2^JU/3^{d+1}\). It follows exactly the same \(J\) parities and has endpoint \(1+3U\). At the next shortcut, \(U\) is odd and \(3U+1\) even. Both reach \((3U+1)/2\). Their final grades are 2 and \(d+2\), so the counted ordinary identity applies to all allowed cofactors. The finite verifier follows the signed numerator through all \(J\) departures and checks its denominator and grade exactly. No assumption about an unbounded signed orbit is used. [Finite arithmetic and canonical prices](check_valuation_returns.py)

**Why the deadline is optimal.** PR192 proves a general independent-clock exclusion: if \(3^{m+1}=1+2^J U\) and \(2\cdot2^J3^J<U\), all earlier peaks miss all pairs of clocks through \(J\). Its `special_width` proof establishes the inequality at \(m+1=12\cdot2^{J-4}\). Multiplying this exponent by any positive cofactor preserves the inequality, since \(((1+2^J U)^r-1)/2^J\ge U\). The earlier theorem's original cofactor-one application and its general width hypothesis are distinct. The argument here uses the general result on every member of each class. [PR192 general SignedPeakDelay.all_earlier, Git blob 4c3acddc493159c42c5b47633c1d4cdecbf0c552](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/descent/SignedDelay.lean)

These favorable classes have \(J\equiv8,10,16\bmod18\). The 192 preassigned cofactor-one exponents have \(J=18k+4\). Their original supplied-input paid returns and the delayed cofactor progressions at those same fixed valuations are separate theorems. Convergence of every resulting smaller canonical lower source remains open. [The 192 original inputs](FIXED_MERSENNE.md) · [Unbounded delays at their fixed valuations](FIXED_VALUATION.md)

**Kernel proofs and independent arithmetic.** The theorem `Collatz.ValuationDictionary.sharp_classes` quantifies over every positive cofactor in each of the thirteen paid families. It proves the exact common deadline, the full independent-clock exclusion up to the preceding step, the smaller canonical return and the displayed saving. Its finite certificate stores the least positive binary residue of the lower affine base. Lean checks its defining modular equation, both parity counts and both endpoints with the accelerated ordinary iterator. The proof cancels the odd coefficient modulo the full clock precision and lifts the equality to every cofactor. The independent scalar verifier follows the signed trajectories instead and covers all fifteen rows, including the two unpriced rows. [Finite certified rows](ValuationRows.lean) · [Universal realization and optimality](ValuationDictionary.lean) · [All-cofactor width and earlier-clock exclusion](ValuationSharp.lean) · [Ordinary lifting and periodic prices](ValuationReturns.lean) · [Scalar replay](check_valuation_returns.py)
