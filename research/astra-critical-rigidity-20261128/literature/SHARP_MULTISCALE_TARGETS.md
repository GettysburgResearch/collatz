# One computable sparse set visited by almost every early ordinary trajectory

**Proposed written theorem.** There is a single computable set \(F\) of positive odd integers such that
\[
  2^{-j}|F\cap[2^j,2^{j+1})|\ll \frac{(\log j)^{12}}{j^2}
                                                                  \tag{1}
\]
for large \(j\), and yet almost every positive integer \(n\), in natural density, has a true shortcut visit to \(F\) strictly before its global minimum date, within \(O(\log n/(\log\log n)^2)\) native steps. Every such early visit is at a value \(n^{1+o(1)}\). In particular, for \(U_X\) uniform through \(X\) and \(R=\lfloor X^{1/2}\rfloor\), the probability of a preminimum visit to \(F\cap[R,\infty)\) tends to one. Its dyadic square-root costs satisfy
\[
 \left(\sum_{i\ge0}
  \left(\frac{|F\cap[2^iR,2^{i+1}R)|}{2^iR}\right)^{q/2}\right)^{1/q}
                  \longrightarrow 0\qquad\text{for every }q>1 .         \tag{2}
\]
Thus the \(\ell^1\) cost across shells in [All high targets](ALL_HIGH_TARGETS.md) cannot be replaced by any \(\ell^q,\ q>1\), even for one fixed integer set and all ordinary source cutoffs. The construction and its lower hitting bound use finite counting and elementary Bernoulli concentration only.

More generally fix rational \(0<a\le1\). There is an explicit \(F_a\) with octave density \(O_a(j^{-2a}(\log j)^{12})\) and typical first visit by \(K_j=\lfloor j^a/(\log(j+2))^2\rfloor\) steps on the source octave \([2^j,2^{j+1})\). The assertion holds uniformly on **every subinterval of that octave containing at least \(2^{20K_j}\) consecutive sources**. This is a positive integer experiment with no clearing or conditioning on a prescribed later orbit. For \(a=1\), \(F=F_1\) gives (1).

## A family of short ternary residue tests

Let \(\gamma=\log_2 3\), \(\lambda=\gamma-4/3>0\). For \(k\) a positive multiple of three, let \(A_k\subset\mathbb Z/3^k\mathbb Z\) be the terminal residues of the \(k\)-odd-gap words of total \(4k/3\). Specifically, for the reversed list of positive gaps \(a_1,\ldots,a_k\) and \(s_i=\sum_{h\le i}a_h\), include \(\sum_{i=1}^k3^{i-1}2^{-s_i}\bmod3^k\). Expansion of the actual odd maps \(y\mapsto(3y+1)/2^{a}\) shows that every genuine chronological list with that total ends in \(A_k\), regardless of its starting odd state. Residue collisions are allowed. There are
\[
 N_k=\binom{4k/3-1}{k-1}\asymp k^{-1/2}2^{(8/3-\gamma)k}
\]
such lists, by Stirling's formula. The probability that \(k\) independent positive geometric gaps of masses \(2^{-v}\) have that total is exactly \(N_k2^{-4k/3}\). Therefore
\[
 \frac{|A_k|}{3^k}\le C k^{-1/2}2^{-2\lambda k},
 \qquad
 \Pr\big(\text{total gap }=4k/3\big)
                \ge c k^{-1/2}2^{-\lambda k}.                           \tag{3}
\]
The chosen total gives the square of the exponential probability scale in the cardinality bound. Previous arithmetic treatments of the Syracuse stationary density likewise use words of prescribed total and tilted word distributions. This use constructs a fixed set in all physical octaves and tests many disjoint true chronological blocks. It needs neither injectivity of the residue map nor an infinite stationary-density theorem. [Valbuena, native word formula and word counting](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/main/paper/quadratic-cylinder-energy.tex) · [Weaver, stationary endpoint and tilted words](https://rstation.ai/problems/collatz/papers/146/v1)

Set \(\ell=\lfloor\log_2 j\rfloor\) for large \(j\). Choose \(k(j)=3b\), with \(b\) the largest integer satisfying
\[
                         (27/16)^b\,\ell^6\le2^{\lfloor a\ell\rfloor}.
\]
Use \(k=3\) at small \(j\) if necessary. This is a finite rational comparison for the stated rational \(a\). Since \(2^{3\lambda}=27/16\), it gives \(k(j)\asymp_a\log j\) and \(2^{-\lambda k(j)}\asymp_a (\log j)^6 j^{-a}\). For large \(j\) and \(j/2\le j'\le 2j\), one has \(|k(j')-k(j)|\le18\): the two \(\ell\)'s differ by at most one, their right sides after division by \(\ell^6\) differ by a factor at most four, and rounding the base-\(27/16\) logarithm changes the difference by at most one.

On \([2^j,2^{j+1})\), retain a positive odd integer \(y\) if \(y\bmod3^k\in A_k\) for any positive multiple of three \(k\) with \(|k-k(j)|\le18\). This defines \(F_a\). Only boundedly many depths occur per octave. Each congruence class supplies at most \(1+2^j/3^k\) integers there, and \(3^k=2^{O_a(\log j)}=o(2^j)\). Equation (3) yields the claimed density bound. The restriction to odd targets can only decrease this count.

## An actual early hit on each long enough interval

Let \(j\) be large, \(K=K_j\) and \(k=k(j)\), and sample an integer in any interval as in the theorem. The first \(16K\) native parity bits on the complete residue grid modulo \(2^{16K}\) are iid fair bits, by the ordinary parity-word bijection. Uniform interval sampling changes their joint law in total variation by at most \(O(2^{-4K})\). The event in the next paragraph is determined by this prefix. There is no claim of iid behavior after this many native steps.

In an independent infinite fair tape, begin at its first one. The gaps to further ones are independent positive geometric variables of masses \(2^{-v}\). Test the first \(b'=\lfloor K/(4k)\rfloor\) disjoint blocks of \(k\) such gaps. The probability that all fail is at most
\[
 (1-N_k2^{-4k/3})^{b'}
                \le \exp[-c_a(\log j)^{5/2}],
\]
by (3) and the definition of \(K\). With probability \(1-O(e^{-cK})\) these blocks all end by native date \(K\), since this needs only \(b'k+1\) ones among the first \(K+1\) bits. Subtracting the two failure probabilities gives a lower bound for an event measurable through date \(K\). Transfer it to the real interval by the parity dictionary. The final one of a successful block marks an actual odd state \(y\) with \(y\bmod3^k\in A_k\). Every positive shortcut step changes \(\log_2\) height by at most one. Therefore its octave index \(j'\) is between \(j-K-1\) and \(j+K+1\), inside \([j/2,2j]\) eventually. The mask at its actual height includes the tested depth \(k\), so \(y\in F_a\).

It remains to check that the true global minimum occurs later. Among the first \(16K\) departures the number \(g\) of odd ones is at most \(9(16K)/16\) with probability \(1-O(e^{-cK})\) under the same fair tape. No independence from the successful block is needed. All true input heights through these steps are at least \(n2^{-16K}\). The exact shortcut product then gives
\[
 \log_2(T^{16K}n/n)
   \le 16K\big((9/16)\gamma-1\big)+
                    O(K2^{16K}/n) < -K
\]
eventually, because \((9/16)\gamma-1<-1/16\) and \(K=o(j)\). Every state through date \(K\) is at least \(n2^{-K}\). Hence its global minimum date lies strictly after \(K\) on this event. Altogether the exceptional fraction tends to zero uniformly on the asserted source intervals. Combining complete octaves and the incomplete top octave gives natural density one: an incomplete top interval shorter than \(2^{20K_j}=o(2^j)\) has negligible total sample mass. Independently, \(U_X\ge X^{3/4}\) with probability tending to one, and then all the early marked values exceed \(X^{1/2}\). For \(a=1\), (2) follows since \(\sum_{j\ge J}j^{-q}(\log j)^{6q}\to0\) for each \(q>1\); a shell on a shifted dyadic grid overlaps at most two ordinary dyadic octaves of comparable size.

## Optimal power of the observation time

For any deterministic mask with octave densities at most \(j^{-2a+o(1)}\), a uniform ordinary start on \([2^j,2^{j+1})\) has probability \(o(1)\) of visiting it both by \(j^{a-\epsilon}\) native steps and through its true minimum, for each \(0<\epsilon<a\). Indeed all such states lie in \(O(j^{a-\epsilon}+1)\) octaves of indices \(j+O(j^{a-\epsilon}+1)\). Use [All high targets](ALL_HIGH_TARGETS.md) on only these shells, conditioning the uniform sample through \(2^{j+1}\) on the octave at a bounded factor. Their sum of square-root densities is \(j^{-\epsilon+o(1)}\). Thus the power \(a\) of the logarithmic height in the construction cannot be reduced at this density scale. The logarithmic corrections, and the best possible norm between \(\ell^1\) and all the \(\ell^q\), are not determined here.
