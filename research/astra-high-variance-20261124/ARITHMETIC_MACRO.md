# All light buffers and all pure paid-run lengths for two comparison slopes

**Written theorem.** Use the affine comparison \(H_\lambda(q)=\lambda(q+7)-7\) from [DESCENT_MACRO.md](DESCENT_MACRO.md). For each of its two slopes, a uniform reset on \(L^K P^s\), \(K\ge0,\ s\ge1\), exists exactly when
\[
                      K\ge k_0,\qquad s\in\{1,2\}.
\]
Here \(k_0=4\) for \(5583/4096\) and \(k_0=5\) for \(72873/65536\). On \(L^K P L^j P\), \(K,j\ge0\), a uniform reset exists exactly when \(K\ge k_0\) and \(j\ne3\). Thus arbitrarily many light blocks cannot rescue a run of three consecutive paid blocks for either slope. These statements classify uniform single-word resets, not all possible comparisons on one particular input.

A reset means a literal shortcut word with the same length and odd count as the source word whose affine action intertwines \(H_\lambda\) with the source affine action. Realization as an ordinary path on an infinite concatenation is a further step, supplied by the denominator argument below.

## Positive descent extension

For either header and slope specified in DESCENT_MACRO.md, retain its ordinary entrance construction. The tail can now be any infinite concatenation of
\[
 L,\quad L^K P,\quad L^K P L^j P\qquad(K\ge k_0,\ j\ge0,\ j\ne3).
\]
For the first slope this allows an outer buffer of four lights and for the second an outer buffer of five. Every macro has \(2p-A>0\), where \(p\) is its odd count and \(A\) its literal time: a light block contributes \(+1\) and a paid block \(-1\). At every boundary the comparison values are positive and have dyadic denominators dividing the fixed denominator of \(\lambda\). A nonintegral denominator at one boundary would grow by \(2^A\) at the next since the certified translated numerator is integral and \(3^p\) is odd. Hence they are ordinary integers along the one infinite source. Their target words execute literally and give unbounded cumulative excess \(2p-A\), incompatible with hitting one. The earlier entrance and size proof therefore places an actual nonconverger below the original floor under this enlarged tail hypothesis. No existence of an infinite ordinary source of this kind is presumed.

## Reducing arbitrary light buffers to the least possible buffer

Write \(M/2^d=\lambda\) in lowest terms, \(d\ge1\). The fixed centers of \(L\) and \(P\) are \(-7\) and \(5/23\), respectively. Relative to the light center, the constant for \(P\) is \(166/32\). Its fixed displacement is \(166/23\). Thus the translation of \(P^s\) in the \(q+7\) coordinate is \((166/23)(1-(9/32)^s)\). For \(L^K P^s\) the required target carry is
\[
 K_\lambda=7(3^p-2^A)+\lambda(166/23)\,8^K(32^s-9^s),
 \qquad p=2(K+s),\quad A=3K+5s.
\]
The quotient \((32^s-9^s)/23\) is an odd integer. Carry integrality requires \(3K+1\ge d\), giving \(k_0=\lceil(d-1)/3\rceil\). More generally, every nonempty suffix \(V\) starting with a paid block has centered, clock-cleared translation of exact 2-adic valuation one. The first paid contribution is 166 times an odd power of nine; all later contributions from paid blocks are divisible by \(2\cdot32\), and lights contribute zero. This gives the same necessary buffer for \(L^K V\).

The comparison commutes with \(L\). For \(K\ge k_0\), write \(b=K-k_0\). The formal affine candidate for \(L^K V\) factors as the actual target \(L^b\) followed by the candidate at \(k_0\), whose carry is an integer. Any length-\(A\), odd-count-\(p\) word with integer carry \(C\) forces its *initial* residue to be \(-C3^{-p}\pmod{2^A}\). This determines its entire chronological parity string, by iterating from that residue. In the factorization the residue modulo \(2^{3b}\) forces the actual \(L^b\) prefix: modulo \(2^{3b}\) the subsequent integral carry is multiplied by \(2^{3b}\), and the remaining factor is an odd power of three. After stripping this forced prefix, the same time, odd-count and carry comparison is exactly the candidate at \(k_0\). Conversely any certificate there extends by prepending \(L^b\). Buffer cancellation is therefore an equivalence.

## Forcing a signed rational prefix for unbounded paid lengths

At minimal buffer \(k=k_0\), evaluate the affine candidate at the unique rational input whose image under \(L^k\) is the paid fixed point. Its comparison source and target are
\[
 y=\lambda(166/23)(8/9)^k-7,\qquad B=\lambda(166/23)-7.
\]
The initial \(y\) has odd reduced denominator. Put \(h=d-1\); the terminal \(B\) has exact binary denominator \(2^h\) for the two slopes under consideration. For a candidate with \(A\ge h\), reverse its last \(h\) formal affine branches from \(B\). The inverse branches are \(2z,(2z-1)/3\), so every choice gives an odd-denominator rational after these \(h\) steps. Continuing backward from such a rational, each inverse step gives the prescribed actual parity at its input because 3 is odd. Thus the first \(A-h\) candidate bits must be the genuine signed rational shortcut itinerary from \(y\), using numerator parity in lowest terms. The remaining \(h\) bits may be relaxed to *arbitrary* affine branches; failure even after this relaxation excludes a reset.

This also gives a general rigidity statement for any fixed positive dyadic slope and sufficiently long paid runs. The point after the forced prefix belongs to the fixed finite set of all formal depth-\(h\) preimages of \(B\). Infinitely many successful \(s\) force the signed orbit from \(y\) to repeat. Its eventual cycle must have odd density \(2/5\), because the total required odd count is \(2(k+s)\), the total time is \(3k+5s\), and the remaining \(h\) clocks contribute at most \(h\) odds. Conversely if it is periodic with that density, the remaining target and odd-count tests become periodic in \(s\) after entrance to the cycle: advance by a multiple of the cycle length and five, so the required and accumulated odd counts increase identically. Thus the set of successful \(s\) is always eventually periodic (possibly finite). This is a structural statement, not an effective orbit-classification procedure for an arbitrary supplied slope. For integral slopes use \(h=0,k=0\).

## Exact finite certificates for both published slopes

With \(h,k\) fixed as above, straightforward rational iteration gives:

| \(M,d\) | \(k,h\) | signed source \(y\) | preperiod | period | first periodic value | \(23\,2^h B\) |
|---|---|---|---:|---:|---|---:|
| 5583,12 | 4,11 | \(-43181/50301\) | 12 | 43 | \(41/23\) | 133661 |
| 72873,16 | 5,15 | \(-128090/50301\) | 14 | 5 | \(14/23\) | 772811 |

For \(s\ge3\), the forced prefix \(3k+5s-h\) is already at least the preperiod in each row. For each \(z\) on the relevant cycle, start with \(D_0=\{23z\}\), a set of integers, and compute
\[
 D_{i+1}=D_i\ \cup\ \{3v+23\,2^i:v\in D_i\}.
\]
These are precisely the scaled numerators after \(i+1\) unrestricted formal steps, at scale \(23\,2^{i+1}\). Neither row has \(23\,2^h B\in D_h\) for any point of its own cycle. This one finite test excludes *all* \(s\ge3\).

For \(s=1,2\) the literal target parity certificates at the minimal buffers are respectively:
* \(5583/4096\): 11110010101000111 and 1111000010100111010011.
* \(72873/65536\): 01111110100010111100 and 0111100011110110010011100.

For a pair with \(j\ge k_0\), concatenate the two certified single-paid resets. For \(0\le j<k_0\), direct decoding at the least buffer succeeds exactly for \(j\ne3\) for both slopes. Buffer cancellation proves necessity at all larger \(K\). [arithmetic_macro.py](arithmetic_macro.py) reproduces the signed orbits, all cycle exclusions and the literal finite checks with exact rational and integer arithmetic. Normal and optimized Python runs agree. No Lean formalization of this all-length classification is asserted.

## Changing slopes

If a uniform target word uses \(u\) odd inputs in \(B'\) clocks while the source uses \(p\) in \(A\), switching from \(\lambda\) to \(\mu\) requires
\[
 \mu/\lambda=3^{u-p}2^{A-B'} .
\]
This follows by comparing the coefficients of the initial value, regardless of chosen constant translations. It persists on any infinite or any two-point family of lifts sharing the same fixed words. The odd factors outside 3 in the two published slopes are 1861 and 2699; neither cancels in their ratio. Thus no uniform switch between these two values is possible, even with asynchronous target clocks. Along a chain of arbitrary such switches the ratio between any two used slopes remains a \(\{2,3\}\)-unit. Many slope switches within one such coset are not excluded; for bounded dyadic denominators, powers of three may still grow without bound. A source-dependent choice of words is outside the uniform single-word conclusion unless the specific words are fixed on at least two inputs.

**A cost even for source-dependent switches.** Fix two rational affine comparisons \(\lambda q+b\) and \(\mu q+c\) in distinct slope cosets. Suppose one positive integer source \(q\) realizes a switch using arbitrary source and target words of lengths \(A,B'\), counts \(p,u\), and integer carries \(C,D\). The exact equality is
\[
 2^A \bigl(3^u(\lambda q+b)+D\bigr)
   =2^{B'}\bigl(\mu(3^p q+C)+2^A c\bigr).
\]
Clear the fixed rational denominators. The coefficient of \(q\) is a nonzero integer by the coset test, so its absolute value is at least one. All remaining terms have total absolute value at most \(C_0\,3^{A+B'}\), with \(C_0\) depending only on the two comparisons. Indeed a raw word of length \(a\) has carry bounded by \(3^a-2^a\), by direct induction on the branches. Consequently
\[
                 A+B'\ge(\log q-\log C_0)/\log3 .
\]
This holds even when the words were selected after inspecting the full source. Along a single nonperiodic ordinary path, distinct switching boundaries have distinct positive values. For any \(m\) disjoint switches in both executions the total combined literal clock is at least \((\log(m!)-m\log C_0)/\log3\), since their starting values have product at least \(m!\). In particular bounded-clock switches occur only finitely often. Adaptive switches between the two cosets have zero asymptotic density per combined clock; if the target clock is bounded by a fixed multiple of the source clock in total, the same holds per source clock. This budget still permits infinite switching separated by sufficiently long windows.

**Power cost along two injective ordinary arms.** The variation argument in [REWRITING_VARIATION.md](REWRITING_VARIATION.md) and the preceding coset test together give a stronger estimate for a finite fixed palette of positive rational slopes and rational additive offsets. Use nonempty switching words on both arms in disjoint time intervals on two fixed injective ordinary shortcut trajectories. Let \(\eta=\mu/\lambda\notin\langle2,3\rangle\) and \(L=1+A+B'\). The nonzero real linear form
\[
 Z=(u-p)\log3-(B'-A)\log2-\log\eta
\]
satisfies \(|Z|\ge cL^{-\kappa}\) for constants \(c,\kappa>0\) depending only on the palette. Apply Matveev, Corollary 2.3, to the three fixed positive rationals \(3,2,\eta\) in degree one with coefficients \(u-p,A-B',-1\) of magnitude at most \(L\). Their logarithms are rationally independent: a prime outside \(\{2,3\}\) has nonzero valuation on \(\eta\). The logarithmic heights and the coefficient weights in the corollary are thus fixed, and the lower bound for \(\log|Z|\) is \(-O(1+\log L)\). Take the worst constants over the finitely many pairs. [Matveev, original paper](https://www.mathnet.ru/eng/im314)

For a raw ordinary word taking \(x\) to \(x'\), write \(E\) for the sum of \(\log(1+1/(3z))\) over its odd inputs \(z\). Then \(\log(x'/x)=p\log3-A\log2+E\). Apply this identity also on the other arm with correction \(F\), initial value \(\lambda x+b\) and final value \(\mu x'+c\). Subtracting gives
\[
 Z = E-F+\log(1+c/(\mu x'))-\log(1+b/(\lambda x)).
\]
Each boundary logarithm is bounded in absolute value by \(C/x'\) or \(C/x\): this is immediate above a fixed threshold, and a finite enlargement covers the remaining positive integers giving positive targets. Each of the two full ordinary odd suborbits is injective and has finite reciprocal sum by PR193. The full shortcut trajectory has finite reciprocal sum as well: a run of even inputs ending at odd \(z\) contributes at most \(1/z\), with an initial or final partial run handled by the same geometric sum (or use PR193's direct shortcut bound). The disjoint word interiors charge each odd correction at most once per arm, and starts and ends of nonempty intervals charge each boundary at most twice. Therefore on all incompatible switches
\[
 \sum_jL_j^{-\kappa}<\infty,\qquad
 \frac{\sum_{j\le m} L_j}{m^{1+1/\kappa}}\longrightarrow\infty
 \quad\text{if infinitely many occur}.
\]
For the second claim apply convexity of \(v^{-\kappa}\) on any tail from a fixed index \(J\) through \(m\). The mean length there is at least \(((m-J+1)/\sum_{j\ge J}L_j^{-\kappa})^{1/\kappa}\). First send \(m\to\infty\), then \(J\to\infty\). This concerns the combined two-arm clock for actual repeated switches, not arbitrary independent witnesses.

Locally, regardless of injectivity, if every state on both arms including endpoints has value at least \(H\), then \(|Z|\le C L/H\) by the same exact expression. Thus \(H\le C' L^{\kappa+1}\). This can force visitation below a specified initial floor when a sufficiently short incompatible switch is actually available on two known nonconvergent arms. There is no theorem here supplying such switches on arbitrary remaining schedules.
