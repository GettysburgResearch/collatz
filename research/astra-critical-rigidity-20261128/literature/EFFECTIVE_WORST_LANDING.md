# An effective subquadratic worst-case clock for first integer landing

For \(N\ge1\), take any integer \(1\le M\le3^N\) with \(3\nmid M\). Start the shortcut Collatz map at the actual positive rational \(M/3^N\) and let \(J(N)\) be the greatest first integral landing time over all such \(M\). There is an effective absolute \(C\) such that for every sufficiently large \(N\), with effective onset,
\[
              J(N)\ \le\ C N^2
                    \frac{\log\log\log N}{\log\log N}.              \tag{1}
\]
The prior [worst-case result](../ordinary/POSITIVE_DESCENDING_INTERVALS.md) gives \(J(N)=o(N^2)\) by a chronological Subspace Theorem estimate. Here (1) follows by integer determinants and a count of distinct ternary valuations. It concerns the maximum over the entire positive numerator grid. The [typical source-grid law](../ordinary/TYPICAL_INTEGER_LANDING.md) describes a different quantifier.

There is also a uniform assertion about starting denominator levels, including arbitrary positions on all these orbits. For a fixed packet size \(k\), there is a set \(E_{N,k}\subseteq\{k,\ldots,N\}\) of size
\[
           |E_{N,k}|\le \exp(Ck^2)(N+1)^{1-\delta_k},
       \qquad \delta_k^{-1}=(k-1)!\sum_{i=0}^{k-1}1/i!,             \tag{2}
\]
such that every packet of \(k\) consecutive odd departures starting from an odd numerator at level \(h\notin E_{N,k}\) costs less than \(2N\) native dates. For the last departure, the packet includes the following even steps through the next odd source, or stops at the first integral landing, whichever comes first. One set works simultaneously for **all** \(M\) at the fixed initial height \(N\). The estimates below prove (2) for \(N\ge64(k+1)\log_2(k+2)\); enlarging \(C\) covers the complementary range. All constants here can be computed. A fixed threshold \((\log_2 3+\varepsilon)N\) is also possible by taking correspondingly narrower boxes, with a constant in (2) depending on \(\varepsilon>0\).

## Complete numerator transport

Before landing, write the current reduced state as \(u/3^h\). An even letter gives the new numerator \(u/2\) at the same level. An odd letter gives \((u+3^{h-1})/2\) at level \(h-1\). Before the last such decrease the numerator remains prime to three. In either update the positive numerator is at most \(3^N\), as the odd update is the average of two numbers bounded by \(3^N\). Thus the first odd date costs at most \(\lfloor N\log_2 3\rfloor\) initial even steps, and the time from any odd date through the next one, or to landing, is at most \(1+\lfloor N\log_2 3\rfloor\).

Consider any of the packets above, with \(k\le h\). Let \(u\) be its initial integer numerator, let \(d\) be its native duration and let \(0=t_1<t_2<\cdots<t_k<d\) be its odd dates relative to the initial mark. Iterating the numerator update gives the exact equation
\[
          u+\sum_{i=1}^k3^{h-i}2^{t_i}=2^d v,                       \tag{3}
\]
where \(v\) is the actual final numerator. It also holds when the final state is the first integer landing. Each gap is bounded as above, so \(d,t_i\le k(1+N\log_2 3)\). The valuation \(v_3(u)=0\) is essential.

## A rational span from both the height and the clock

Use all actual packets at the fixed \(N,k\) with \(d\ge2N\). Work first with \(N\ge64(k+1)\log_2(k+2)\). Put \(B=\lfloor N/(64k)\rfloor\); then \(B\ge N/(128k)\). Box the level \(h\in[k,N]\) by consecutive intervals of \(B\) integers starting at \(k\), and each \(t_i\) by the same width starting at zero. The first date \(t_1=0\) is fixed. There are at most
\[
 (1+N/B)\big(1+k(1+N\log_2 3)/B\big)^{k-1}\le(C_0k^2)^k           \tag{4}
\]
product boxes. Fix a nonempty box. Its lower level endpoint \(H\) satisfies \(H\ge k\), and write \(T_i\) for its lower clock endpoints. On the box define the integer row columns
\[
       z_i=3^{h-H}2^{t_i-T_i},\qquad 1\le z_i\le 6^B.
\]
The original pure term at index \(i\) is \(a_i z_i\), with the single nonnegative integer \(a_i=3^{H-i}2^{T_i}\) common to all rows. These \(a_i\) may be large.

Let the matrix of the \(k\) pure columns on all these rows have rational rank \(r\), with \(1\le r\le k\). Choose a column basis with index set \(J\) and a nonzero \(r\)-row minor \(\Delta\) of that basis. Then \(|\Delta|\le r!6^{rB}\). Cramer's rule expresses \(\Delta\) times each original pure column as an **integer** linear combination of the basis columns on every row. Thus after multiplying (3) by \(\Delta\), there are fixed integers \(c_j\) with
\[
                \Delta u+\sum_{j\in J} c_j z_j\equiv0\pmod{2^{2N}}
                                                                    \tag{5}
\]
on every row in this box. This statement does not require any bound on the heights of the \(c_j\).

Add the numerator column \(u\) to the chosen basis. For every \((r+1)\)-row minor \(D\) of this augmented matrix, (5) shows \(2^{2N}\mid\Delta D\), by replacing \(\Delta u\) by the left side of (5) in the determinant. Meanwhile
\[
     |\Delta D|\le r!(r+1)!\,3^N6^{2rB}<2^{2N}.                     \tag{6}
\]
Indeed \(\log_2[r!(r+1)!]\le 2(k+1)\log_2(k+2)\le N/32\), while \(2rB\log_2 6\le N\log_2(6)/32\), and \(\log_2 3+(1+\log_2 6)/32<2\). Thus every \(D\) is zero, including the vacuous case of only \(r\) rows. Since the basis has rank \(r\), the numerator itself is an exact rational linear combination of its columns. For coefficients \(b_j\in\mathbb Q\) common on this box,
\[
         u=3^{h-H}\sum_{j\in J} b_j2^{t_j-T_j}.
\]
Here \(u>0\) and \(3\nmid u\). Consequently the sum on the right, after removal of \(3^{h-H}\), has **exactly** valuation \(H-h\). Distinct starting levels \(h\) in the box give distinct finite valuations. Apply [the uniform short-power valuation bound](POWER_VALUATION_LEVELS.md) to at most \(k\) powers with exponents in \([0,B)\) and arbitrary rational coefficients. This bounds the number of levels in this box by \(\exp(C_1k^2) B^{1-\delta_k}\). Multiplying by (4) proves (2). For smaller \(N\) use \(|E_{N,k}|\le N\) and \(N^{\delta_k}\le64(k+1)\log_2(k+2)\) in that range.

To obtain the optional threshold with \(\varepsilon>0\), choose a box width at most \(c_\varepsilon N/k\) with \(2c_\varepsilon\log_2 6<\varepsilon/3\), and require \(2(k+1)\log_2(k+2)<\varepsilon N/3\). Then the logarithm in (6) is strictly smaller than \((\log_2 3+\varepsilon)N\). For integer \(d\) round this lower bound up when writing the dyadic modulus. The remaining proof is identical.

## Charging the whole positive descent

Split any one full path into its initial even coast, consecutive full \(k\)-odd packets, and a final shorter packet if needed. Each start level occurs at most once because each odd departure drops the level by one. There are at most \(N/k\) full packets of duration less than \(2N\), and at most \(|E_{N,k}|\) full packets of duration at least \(2N\). Every full or partial packet lasts at most \(k(1+N\log_2 3)\). It follows for \(1\le k\le N\) that
\[
 J(N)\le \frac{2N^2}{k}+C_2 k N+
                  kN\,\exp(C_3 k^2)(N+1)^{1-\delta_k}.             \tag{7}
\]
The term \(C_2kN\) covers both boundary pieces. The uniform exceptional level set (2) is substantially more than is needed for this summation.

For large \(N\) take \(k=\lfloor\log\log N/(4\log\log\log N)\rfloor\), with natural logs. Then \(k!\le k^k\le(\log N)^{1/4}\) and \(\delta_k\ge1/k!\). Hence \(\delta_k\log N\ge(\log N)^{3/4}\), which dominates \(C_3 k^2+3\log(k+2)\) effectively. The last term in (7) is \(O(N^2/k)\), yielding (1). The quantitatively open scale for the complete positive test remains \(O(N\log N)\). The arbitrary positive integer pair problem can include several sign and level excursions, whereas (1) controls a complete positive denominator-clearing test.
