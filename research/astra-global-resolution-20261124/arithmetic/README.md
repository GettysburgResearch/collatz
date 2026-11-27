# Rational approximation to the dyadic companion at one ordinary source

**PROPOSED written theorem.** For the shortcut map \(T\), let \(x_i=T^i(n)\), \(e_i=x_i\bmod 2\), \(P_i=\sum_{j<i}e_j\), \(A_i=2^{i+P_i}/3^i\), and \(D(n)=\sum_{i\ge0}e_iA_i\in\mathbb Z_2\). Write an arbitrary reduced rational as \(a/b\) with \(b=3^h m>0\) odd and \(3\nmid m\). Put
\[
 \alpha=\log_2 3-1,\quad s=\frac{-\alpha\log\alpha-(1-\alpha)\log(1-\alpha)}{\log3}
 =0.6177244\ldots,\quad F(m)=m^s/\sqrt{\log(2m)} .
\]
There is an absolute constant \(C\) such that for *every positive ordinary* \(n\) and every incorrect candidate \(a/b\ne D(n)\),
\[
 \boxed{\quad v_2(D(n)-a/b)\ \le\
 C\big(1+\log(n+1)+\log(|a|+2)+\log b+F(m)\big).\quad} \tag{1}
\]
All constants can be obtained from the proof; no numerical value of \(C\) is claimed. A reduced even denominator gives negative agreement valuation immediately. At \(m=1\), the explicit \(10^6\) inequality in PR182 is preferable. The new term controls unbounded denominators with unrestricted prime factors. The same packing result forces superlinear growth of the **companion denominator** on every sufficiently long putative primitive integer cycle and on every sufficiently long periodically closed prefix of a fixed escape. [PR182, dyadic signs and rationality](https://github.com/GettysburgResearch/collatz/blob/4f226f3b278ffe4559110a6ca952ff4a7c56ceba/research/high-variance-closure-20261124/ordinary-arithmetic/DYADIC_COMPANION.md) · [PR182, triadic separation](https://github.com/GettysburgResearch/collatz/blob/4f226f3b278ffe4559110a6ca952ff4a7c56ceba/research/high-variance-closure-20261124/ordinary-arithmetic/TRIADIC_SEPARATION.md)

## From dyadic agreement to positive real phases

Write \(B_i=\sum_{j<i}e_j A_j\) and start the rational trial at \(w_0=-a/(3b)\). The companion branches, driven by the physical bits, are
\[
 2^{1+e_i}w_{i+1}=3w_i+e_i,\qquad
 w_i=(B_i-a/b)/(3A_i).
\]
A trial with \(v_2(D(n)-a/b)\ge2K\) stays dyadically integral through time \(K\). Indeed the difference from \(-D(x_i)/3\) loses exactly \(i+P_i\le2i\) dyadic bits. Before each of the first \(K\) steps the trial agrees modulo four with that genuine phase. At even physical input \(w_i\) is even; at odd input \(w_i\equiv1\bmod4\). Hence the trial phase determines the next branch uniquely. Its reduced denominator divides \(m\) after \(h+1\) steps, since division by two is dyadically legal, and multiplication by three before addition clears a factor of three whenever one is present. No other odd prime factor is introduced.

Set \(N=1+h+\log(n+1)+\log(|a|+2)+\log b\), using natural logarithms unless a base is indicated. Suppose first that all physical inputs up to a horizon are at least 20. For each prefix of length \(i\) within it, \(2^ix_i\le n(61/20)^{P_i}\), by the physical product formula. Since \((61/20)^3<2^5\) and \(x_i\ge1\), this gives \(P_i\ge(3/5)(i-\log_2 n)\) and
\[
 \log A_i\ge\delta i-(3/5)\log n,\qquad
 \delta=\tfrac15\log(256/243)>0.                                  \tag{2}
\]
The identity \(2B_i=3A_i-3+\sum_{j<i}A_j\) follows by telescoping \(3(A_{j+1}-A_j)=(2e_j-1)A_j\). Choose \(J=O(N)\), \(J\ge h+1\), so (2) gives \(A_i\ge 4(3+2|a|)/3\) for all \(i\ge J\) in the given horizon. Then \(w_i\ge1/4\) by the displayed formula. Also \(|w_i|+1\le(3/2)^i(|w_0|+1)\), so \(\log w_J=O(N)\) as an upper bound.

For \(t>J\) within this horizon, multiply the positive companion steps to obtain
\[
 \sum_{J\le i<t,\ e_i=1}\log(1+1/(3w_i))
 =\log(A_t/A_J)+\log(w_t/w_J)\ge\delta t-O(N).                  \tag{3}
\]
Here \(A_J\le(4/3)^J\). The terms are at most \(\log(7/3)\). Fix an absolute \(B>1\) large enough that \(\log(1+1/(3B))<\delta/2\). At least \(c t-O(N)\) indices \(J\le i<t\) have \(1/4\le w_i\le B\), for an absolute \(c>0\).

## The number of bounded trials with a legal past

Put \(k=\lceil\log_3(2Bm)\rceil\). Discard the first \(k\) indices after \(J\). Any remaining bounded endpoint \(w_i\) has a legal \(k\)-bit past with \(u\) ones. The unrolled recurrence reads
\[
 2^{k+u}w_i=3^k w_{i-k}+C_{\rm past},\qquad C_{\rm past}\ge0.
\]
The carry depends only on the ordered past word. Since both endpoints are on the \(1/m\) grid, this fixes \(mw_i\bmod 3^k\), because \(2^{k+u}\) is a ternary unit. Its positive numerator is at most \(Bm<3^k\), hence each past word specifies at most one bounded endpoint. Furthermore \(B\ge w_i\ge 3^k/(4\,2^{k+u})\) forces \(u\ge\alpha k-\log_2(4B)\). Therefore these bounded endpoints have at most
\[
 \sum_{u\ge\alpha k-\log_2(4B)}{k\choose u}
 \ \ll_B\ \frac{\exp(k[-\alpha\log\alpha-(1-\alpha)\log(1-\alpha)])}
                  {\sqrt{1+k}}
 \ \ll_B F(m)                                                     \tag{4}
\]
distinct values. Here \(\alpha>1/2\). For large \(k\) the successive coefficients starting at the first permitted index have ratio at most a constant strictly smaller than one; Stirling at \(\alpha k+O_B(1)\) bounds the first coefficient as displayed. The bounded smaller \(k\) are absorbed in the constant. The count uses a past already lying in the \(1/m\) grid. Counting fresh residues from the original physical source would not supply this restriction.

## A repeat either proves equality or bounds the agreement

Take \(t=\lceil C_0(N+F(m))\rceil\), with \(C_0\) large enough that (3), after discarding \(k=O(N)\) indices, exceeds (4). We can suppose \(K\ge t\); otherwise \(2K\) is already on the asserted scale. If a physical state below 20 occurs before \(t\), it reaches 1 within an absolute number of steps by direct iteration of the nineteen possible values. Consequently \(T^\ell n=1\) for some \(\ell\le t+O(1)\). As \(D(1)=9\), the splitting identity expresses \(D(n)=B_\ell+9A_\ell\) with denominator dividing \(3^\ell\) and numerator over \(3^\ell\) of absolute value at most \((\ell+9)4^\ell\). For unequal rationals, the valuation of their difference is at most the base-two logarithm of the absolute cross numerator. This proves (1) in this case.

Otherwise (3)–(4) give two identical trial phases \(w_i=w_j\), \(J\le i<j<t\). The trial then repeats the legal block from \(i\) to \(j\) forever by determinism of the allowed branch on dyadically integral phases. The **actual physical** bits at \(i\) and \(j\) consequently agree for the next \(K-j\) steps. If \(x_i=x_j\), the physical orbit itself cycles with that block, and the trial agrees with the genuine companion forever. Indeed iterating the splitting identity to arbitrarily large times forces \(D(n)-a/b\) divisible by arbitrarily high powers of two. This contradicts the wrong-candidate hypothesis. If \(x_i\ne x_j\), subtract the common affine physical prefixes to give \(2^{K-j}\mid x_j-x_i\). Since \(x_\ell+1\le(3/2)^\ell(n+1)\), this implies
\[
 K\le j+j\log_2(3/2)+\log_2(n+1).
\]
Choosing \(K=\lfloor v_2(D(n)-a/b)/2\rfloor\) when this valuation is positive proves (1), including all cases of short agreement.

The same argument gives a terminating comparison algorithm for a supplied rational of any denominator. Run the ordinary and trial branches together. A trial residue incompatible with the next physical bit disproves equality. If a physical state below 20 occurs, evaluate the exact triadic value by finite iteration to 1. If both states of a pair \((x_i,w_i)\) recur together, their common legal cycle proves equality by dyadic splitting. The preceding count bounds the number of steps by \(O(N+F(m))\) even for a *correct* candidate: by time \(t\) there is a trial repeat or the small physical state intervenes. In the repeat case \(x_i\ne x_j\) cannot allow more than \(O(t+\log(n+1))\) total matching steps. Thus any correct rational input also bounds the actual physical preperiod and period by this quantity. When doing the comparison directly, any nonintegral trial at time zero or failure at a later step is already decided. This algorithm decides the equality question for each specified rational.

## A denominator forced on individual cycles and escaping prefixes

For a primitive length-\(L\) bit word of weight \(p>0\) with
\(\Gamma=(L+p)\log2-L\log3\ge\eta L\) for fixed \(\eta>0\), close its companion branches around the word. The fixed point \(w=B_L/[3(A_L-1)]\) is positive, as are all rotations. The full raw companion divisor is \(E=2^{L+p}-3^L>0\); explicitly \(Ew=\sum_{j<L}e_j2^{j+P_j}3^{L-1-j}\). Thus its reduced denominator \(b_*\) is a divisor of \(E\), is coprime to six, and is the same at every phase. Each phase is in \(\mathbb Z_2\), as is the next one. Hence the recurrence forces one of the two legal residues and the word is literal for this companion. The minimum is at least one: a predecessor using the even branch strictly increases a positive value, and the odd branch forces \(4w_{\min}\ge3w_{\min}+1\) at a minimum. Distinct phases have distinct values by least period and deterministic legal branches.

Multiplying through the cycle gives \(\sum_{e_i=1}\log(1+1/(3w_i))=\Gamma\). Since every \(w_i\ge1\), at least \(c_\eta L\) phases lie in \([1,B_\eta]\) for a sufficiently large fixed \(B_\eta\). Formula (4) applies to *every* such phase by periodic extension, with grid \(1/b_*\). Consequently
\[
 L\ll_\eta F(b_*),\qquad
 b_*\gg_\eta L^{1/s}(\log(2L))^{1/(2s)}.                         \tag{5}
\]
More generally the sum of the least periods of **all distinct primitive companion cycles with this same reduced denominator** satisfying \(\Gamma\ge\eta L\) is \(O_\eta(F(b_*))\). Their bounded phases occupy disjoint grid points because the permitted companion branch is deterministic. Apply the same past count to their union and sum the positive-fraction lower bounds. For the inversion first deduce \(\log(2b_*)\gg_\eta\log(2L)\). Every hypothetical nontrivial primitive positive ordinary cycle has all phases at least 20. Applying the closed product estimate \(2^L\le(61/20)^p\) gives \(\Gamma\ge\delta L\), so (5) applies individually.

For one fixed positive escaping source, (2) gives \(\Gamma\ge(\delta/2)L\) on every sufficiently long prefix. All sufficiently long such prefixes are primitive: if a length-\(L\) prefix is a proper power of a length-\(r\) word, then \(r\le L/2\) and \(2^{L-r}\mid x_r-n\). Those states are different on an escape and \(|x_r-n|<(3/2)^r(n+1)\), which is incompatible with \(L-r\ge r\) at large \(L\); in fact \(2^{L-r}\le(3/2)^r(n+1)\) bounds \(L\) directly. This proves (5) for the periodized companion of every sufficiently long prefix of that same ray. It does not identify this auxiliary rational with the actual \(D(n)\).

The fresh PR182 equivalence would give universal convergence if \(D(n)\in\mathbb Z[1/3]\) for all \(n>0\). Formula (1) bounds agreement with every wrong rational. It neither produces a correct rational at a prescribed \(n\) nor bounds the height of one for all \(n\). Formula (5) leaves room for growing denominators of auxiliary periodic companions of an irrational dyadic limit. Both full divisors attain their respective leading exponents outside an exponentially small fraction at every fixed interior clock density. Their raw gcd is uniformly subexponential by the Subspace Theorem. These statements are proved in [CLOCK_FIBERS.md](CLOCK_FIBERS.md).

## Formal and replay scope

[CompanionPacking.lean](CompanionPacking.lean) proves the arbitrary-word affine equation for two companion branches, uniqueness of a bounded ternary endpoint on a fixed denominator grid, the integer clock inequality underlying the odd-weight cutoff, and the physical size consequence once a trial repeat has supplied a shared dyadic congruence. Lean 4.34.1 with Std compiled the four declarations with warnings as errors. The counting, analytic bounds, selection of repeated phases and the passage to the genuine dyadic scalar are written arguments.

[check.py](check.py) enumerates marked representatives of binary necklaces through length 12. Normal and optimized Python each checked 608 positive and 169 negative physical necklaces, 2,256 dyadic minimum encodings, 417 ternary minimum encodings, 973 companion stopping-prefix minimum encodings, 1,241 companion ternary minimum encodings, 1,320 bounded companion phases, and 50,814 literal agreement steps at specified ordinary sources. These checks exercise finite identities and are independent of the asymptotic claims.
