# Coverage of actual smaller sources along the complete Mersenne ascent

**O10, proposed written application to the hard family.** Put
\[
 m=11+162j,\qquad z_m=(2^{m+7}-271)/81,\qquad
 Z_i=3^i2^{m-i}-1\quad (0\le i\le m).
\]
The original lower path reaches \(Z_0\) and then visits the \(Z_i\) consecutively. Suppose a positive integer \(Y<2^{-D}z_m\) reaches any one of these actual states, at any clock and with any odd count \(q\). Write \(a=H_2(\log_3 2)<1\), where \(H_2\) is binary entropy. The following statements use any constant \(C\) bounding the distortion of the first-hit paths considered below, and assume \(2^{D-1}>C\).

1. Every such ordinary index lies in a single open set of \(\mathbb Z_3\) of normalized Haar measure at most \(1944C^2 4^{-D}\). The set permits all heights, clocks, odd counts and ascent positions.
2. In any interval of \(J\) consecutive nonnegative indices, the fraction admitting such a witness with **excess odd count** \(q-i\le P\) is at most
   \[
   1944C^2 4^{-D}+O\!\left(\frac{3^{aP}}{J\sqrt{P+1}}\right).
   \]
   In particular, \(P=\lfloor a^{-1}\log_3 J\rfloor\) makes the error tend to zero. The implied constant is absolute. The index at which the lower paths meet and both ordinary endpoints can vary with \(j\).

The short independent calculation below gives \(C=512\) with no imported delay census. Nikzad, Frinkle and Bagherzadeh's finite-path four-thirds bound gives \(C=4/3\) here using their cited finite records. With the latter input and \(D=40\), the bound is \(3456\,2^{-80}<2.86\cdot10^{-21}\). The even-departure theorem below also reaches beyond \(Z_m\), giving an upper ordinary fraction below 0.033 through 32 additional even departures at the same excess-grade cutoff. An open ternary set of arbitrarily small measure can contain every nonnegative ordinary integer, so the unrestricted Haar bound alone does not exclude a prescribed ordinary witness.

The first-crossing inequality, the signed common-ascent argument and degree-wise orbit packing have precedents. Paper 100 uses the same \(4^{-D}\) crossing bound and matches inverse prefixes to a signed orbit. Papers 177, 178 and 207 present the binary maximum-gain formulation. Our application shares one cut across all ascent positions of this particular exponential family, quantifies actual source height, and counts all integral signed centers through the growing excess-grade cutoff. The earlier local signed-template count treats a leading-coefficient condition. [Paper 100, §§3 and 5](https://rstation.ai/problems/collatz/papers/100) · [Paper 207, §3 and references](https://rstation.ai/problems/collatz/papers/207) · [Local signed-template bound](../descent/SIGNED_COVERAGE.md) · [Original family and physical clocks](../descent/SIGNED_MERSENNE.md)

## Single-terminal crossing estimate

The reverse shortcut letters are \(E(x)=2x\) and \(O(x)=(2x-1)/3\). The odd inverse is legal when \(x\equiv2\bmod3\). Every legal inverse at a positive ordinary root remains a positive integer. A length-\(H\) word with \(p\) odd letters is legal on exactly one ternary class modulo \(3^p\). Indeed, if its forward offset is \(c\), its source is \((2^H x-c)/3^p\). The one final congruence suffices at all intermediate steps: at a reverse odd, divisibility of the full numerator first forces \(3\mid 2x-1\) because \(2^h\) is a ternary unit, then the remaining congruence follows by cancellation. At an even the test is the preceding congruence at \(2x\). This induction also appears in [SuffixMass.lean](SuffixMass.lean).

For \(G>1\), stop the reverse word the first time its homogeneous gain \(M=3^p/2^H\) is at least \(G\). Every word attaining this threshold begins with such a stop. The stopped words form a prefix-free family. In the binary word space give \(E,O\) independent probabilities \(1/4,3/4\). A word has probability \(\nu=3^p4^{-H}\). Its terminal legality class has Haar mass \(3^{-p}=\nu/M^2\). Summing the class masses bounds the Haar measure of their union by \(G^{-2}\). The disjoint symbolic cylinders and the possibly overlapping ternary classes live in different spaces.

The sum of ternary class masses lies between \((4/9)G^{-2}\) and \(G^{-2}\): the biased binary walk has positive mean log gain, so it stops almost surely, and each first-crossing gain is less than \(3G/2\). At strict threshold one, the stop beginning with \(O\) costs \(1/3\), while those beginning with \(E\) cost at most \(1/4\) in total. The elementary bound is \(7/12\); Paper 100 gives a stronger one by expanding the tree further. The Lean file proves the exact endpoint congruence, two finite quadratic inequalities, the integral signed ascent cut, and both shifted formal estimates used beyond the peak. Countable stopping and the physical counting applications below are written proofs.

## A signed cut independent of the ascent position

Read the actual word backwards from \(Z_i\), matching the same inverse letters at the signed integer \(-1\). At a prefix with \(e\) even and \(h\le i\) odd letters the signed value is \(-A\), where \(1\le A\le2^e\), and the difference of the two states is
\[
     2^{m+e}(3/2)^{i-h}. \tag{1}
\]
The difference is an integer because \(m\ge i\). Until the next odd letter would exceed \(i\) it is divisible by three before every odd inverse, so that inverse is legal at both values. The signed magnitude doubles at an even and changes to \((2A+1)/3\le A\) at a legal odd inverse. These facts give (1) inductively, including the empty prefix.

If the whole word has at most \(i\) odds, (1) implies \(Y\ge2^e(2^m-1)>z_m/2\), a contradiction. Otherwise cut immediately after the \(i\)-th reverse odd, using the empty cut for \(i=0\). For its \(e,A\), the actual cut value is
\[
     U=2^{m+e}-A\ \ge\ 2^e(2^m-1)>2^{e-1}z_m.
\]
The remaining word is an actual path from \(Y\) to \(U\) using exactly \(q-i\) odds. Truncate it forward at the first visit to \(U\). This leaves distinct inputs, gives the same physical ratio \(U/Y>2^{D+e-1}\), and can only decrease the odd count. With \(T\) the shortcut map, telescoping gives
\[
 \frac{U}{Y}=\frac{3^{p'}}{2^{H'}}\prod_{x\text{ odd departure}}(1+1/(3x)).
\]
Consequently its reverse word crosses \(G_e=2^{D+e-1}/C>1\). The lower source and the word producing it can change at every index.

For fixed \(e,A\), the ordinary values \(U(j)=2^{11+162j+e}-A\) extend to a map from \(\mathbb Z_3\) onto one coset modulo \(3^5\). Indeed \(v_3(2^{162}-1)=5\) and \(v_3(U(j)-U(j'))=5+v_3(j-j')\) for distinct ordinary indices. This follows from \(v_3(4-1)=1\) and lifting by successive cubes. It gives a bijection of residues at every higher precision and carries normalized Haar to conditional Haar on that coset. Thus the union of crossing classes for this pair \((e,A)\) has index mass at most \(243/G_e^2\). Sum over the at most \(2^e\) possible positive integers \(A\), then use \(\sum_{e\ge0}2^{-e}=2\), to get the stated \(1944C^2 4^{-D}\).

At a stopped grade \(p\ge1\) the crossing gain belongs to \([G_e,3G_e/2)\), so the clock has at most one integer possibility for this \(p,e\). Write \(L=\lfloor p\log_2 3\rfloor\). Its clock \(H\) is at most \(L-e\). Therefore the total number of pairs of cut centers and first-crossing words at this grade is bounded by
\[
 \sum_{e\ge0}2^e {L-e\choose p}
 \le {L\choose p}\sum_{e\ge0}\bigl(2(1-1/\log_2 3)\bigr)^e
 \ll \frac{3^{ap}}{\sqrt{p+1}}. \tag{2}
\]
Take the binomial coefficient to be zero for \(L-e<p\). The first inequality uses the successive ratio \((L-e-p)/(L-e)\le1-p/L\), and the last follows from Stirling's inequalities at \(p/L=\log_3 2+O(1/p)\). Each compatible pair gives a single index class modulo \(3^{\max(p-5,0)}\). Its count in any length-\(J\) ordinary interval exceeds \(J\) times its Haar mass by at most one. In summing these estimates use the sum of the **individual** cylinder masses, already bounded in the crossing proof, even when disks overlap. Summing (2) up to \(P\) gives the second assertion.

For the narrower exact chart \(X(j)=(2^{17+162j}-122)/27\), the same congruence calculation gives a coset of index nine, \(X\equiv8\bmod9\). Thus all ordinary words landing exactly at \(X\) with slope at least \(G\) lie above an index set of Haar measure at most \(9G^{-2}\). The same grade rounding bound follows directly without the sum over \(e\). This applies in particular to the simultaneous returns of [O9](PAIRED_GAIN.md).

## Beyond the peak, through a specified number of even departures

Let \(V_0=2^m-1\), and let \(V\) be **any** later state on its actual path reached using \(k\) odd departures and \(s\le S\) even departures. Fix integers \(m_0>S\ge0\), restrict to \(m\ge m_0\), and put
\[
 \delta=(2/3)^{m_0},\qquad
 L_0=\frac{81}{128}(1-2^{S-m_0}),\qquad L_0 2^{D-S}>C .
\]
The set of indices admitting \(Y<2^{-D}z_m\) reaching any such \(V\) lies in a ternary open envelope of normalized Haar measure at most
\[
       B=486(1+\delta)(C/L_0)^2 4^{S-D}. \tag{3}
\]
For a path from \(Y\) to \(V\) with \(q\) odd departures, imposing \(q-k\le P\) gives an ordinary upper fraction \(B+O(3^{aP}/(J\sqrt{P+1}))\) in any interval of \(J\) consecutive indices with \(m\ge m_0\). There is no upper limit on the original odd count or the number of clocks. Initial ascent states have \(s=0\), so (3) spans both sides of the peak.

For \(D=40,\ S=32,\ m_0=42,\ C=4/3\), one has \(B<0.033\). Every \(j\ge1\) satisfies this floor. Thus in long ordinary intervals, at least \(96.7\%-o(1)\) of indices admit no such actual forty-bit improvement through the first 32 even departures with excess grade at most \(\lfloor a^{-1}\log_3J\rfloor\). With the independent local constant \(C=512,\ S=24,\ m_0=34\), the bound is \(B<0.07422\). Both paths may nevertheless coalesce later. A path meeting with an arbitrarily large excess grade is outside the ordinary finite-index claim.

**Proof.** Apply the original forward parity word from \(V_0\) as a composition of real affine maps also at \(-1\), and write its formal value there as \(b\). The signed value need not follow a physical trajectory. In the shifted coordinate \(v=b+1\) the forward maps are \(v\mapsto (v+1)/2\) and \(v\mapsto3v/2\). The first \(m\) departures of \(V_0\) are odd. Thus if the word stops in that prefix then \(v=0\). Otherwise that prefix ends with \(v=0\), and the rest gives \(0\le v\le(3/2)^{k-m}\). In either case
\[
     0\le (2/3)^k(b+1)\le(2/3)^m.
\]

Now apply the reverse letters of the path from \(Y\) to \(V\) both to \(V\) and formally to \(b\). After \(e\) even and \(h\le k\) odd inverses, write the second value as \(A\). The difference of the two values is exactly
\[
       \Delta=2^{m+e-s}(3/2)^{k-h}.
\]
The shifted signed coordinate undergoes \(v\mapsto2v-1\) at an even inverse and \(v\mapsto2v/3\) at an odd inverse. Its value is \(2^e(2/3)^h(b+1)\) minus a nonnegative amount at most \(2^e-1\). This last bound follows inductively: an even doubles the accumulated subtraction and adds one, and an odd multiplies it by \(2/3\). Consequently \(A\ge-2^e\) throughout, while at \(h=k\),
\[
       -2^e\le A\le2^e(2/3)^m-1 .
\]
If the actual word ends with \(q\le k\), its source therefore satisfies
\[
 Y\ge2^{m+e-s}-2^e\ge(1-2^{S-m_0})2^{m+e-s}
   > L_0 2^{e-s} z_m>2^{-D}z_m .
\]
Here \(z_m<(128/81)2^m\), \(e-s\ge-S\), and \(C\ge1\). This contradicts the proposed height. Cut the remaining cases at precisely \(h=k\), taking the empty cut when \(k=0\). The physical value at the cut is \(U=2^{m+d}+A\) with \(d=e-s\ge-S\). Now \(A\) is an ordinary integer since \(U\) and \(2^{m+d}\) are integers. Its range is contained in
\[
      [-2^{d+S},\ \delta 2^{d+S}-1],
\]
which has at most \((1+\delta)2^{d+S}\) integers. The remaining true path has exactly \(q-k\) odd departures. The same bound on \(U\) forces its first-hit homogeneous gain to exceed \(G_d=L_0 2^{D+d}/C>1\). For the imported \(4/3\) constant the first-hit inputs are greater than one whenever \(U>2\), as in the displayed numerical specialization. More generally, a first-hit path with a departure from 1 must end at 2 and start at 1 if it has physical gain greater than one, and that one-step path has distortion exactly \(4/3\).

Each \(d,A\) gives a coset of index 243 since differences of \(2^{11+162j+d}\) have ternary valuation \(5+v_3(j-j')\), also for negative \(d\). Summing its crossing masses over the possible centers and using \(\sum_{d\ge-S}2^{d+S}4^{-d}=2\cdot4^S\) gives (3). For the rounding error write \(e'=d+S\ge0\). At grade \(p\) of the minimal crossing suffix the number of candidate centers is at most \((1+\delta)2^{e'}\), and the clock is at most \(\lfloor p\log_2 3\rfloor-e'\) since \(G_d=2^{e'}G_{-S}\) with \(G_{-S}>1\). Applying (2) again proves the finite-index bound. There is no summation over the forward words or the time to the peak.

## A short local distortion certificate

For any single positive orbit, let \(S\) be the set of its distinct odd values. The following explicit bounds use no precomputed Collatz trajectories:
\[
 \sum_{x\in S}x^{-1}<18.5,\qquad
 \sum_{x\in S,\ x\ge2^{40}} x^{-1}<6.3,\qquad
 \sum_{x\in S,\ x\ge2^{71}} x^{-1}<2.8.
\]
The idea is the parity and image-counting argument in Garcia–Tal, specialized with constants. Fix \(k\ge1\), \(N=2^k\), and consider the odd values in \([N,2N)\). Each length-\(k\) parity word has one source class modulo \(2^k\), since the two dyadic lifts of a prefix have next outputs differing by an odd power of three. The number of starting-odd words with more than \(p\) odd steps is \(\sum_{s>p}{k-1\choose s-1}\). At all other starts the image after \(k\) clocks is at most \(2\cdot3^p+(3/2)^p\): the linear part is bounded by \(2\cdot3^p\), and the offset by \((3/2)^p-1\) since moving halvings before odd branches increases their value at zero. On an injective orbit the \(k\)-th iterate is injective. On an eventually periodic orbit, discard the last at most \(k\) transient vertices before cycle entry. The other transient images are distinct and transient, while \(T^k\) permutes the cycle. This gives the same count with at most \(k\) discarded vertices. [Garcia–Tal, Lemma 3 and equation (6)](https://matwbn.icm.edu.pl/ksiazki/aa/aa90/aa9033.pdf)

Take \(B_k\) to be the minimum of \(N/2\) and all resulting bounds \(k+2\cdot3^p+\lceil(3/2)^p\rceil+\sum_{s>p}{k-1\choose s-1}\) for \(1\le p\le k\). Put \(v=B_k/N\). The odd reciprocal contribution on the shell is bounded by the sum at its \(B_k\) smallest odd integers. Convexity integrates each midpoint reciprocal over its centered interval to give at most \(\frac12\log(1+2v)\). The latter is at most \(v-v^2/(1+2v)\) by integrating \(2s/(1+2s)\ge 2s/(1+2v)\) for \(0\le s\le v\).

For the tail \(k\ge400\), split exactly at \(p=\lfloor3k/5\rfloor\). The image count before rounding is at most \(3\,3^{3k/5}\), since the offset bound was \((3/2)^p-1\). Weight high words by \((3/2)^{s-3k/5}>1\): their fraction among all \(2^k\) words, with first bit odd, is at most \((3/5)[(5/4)(3/2)^{-3/5}]^k\). Thus the shell count divided by \(2^k\) is at most
\[
  k2^{-k} + 3(27/32)^{\lfloor k/5\rfloor}
       +(3/5)(3125/3456)^{\lfloor k/5\rfloor}.
\]
Each geometric ratio is strictly below one. Summing this majorant from 400 costs less than 0.010074. The script rounds **up** to one millionth on each of the first 400 shells and also charges 1 for the possible state 1. It deliberately counts shell 400 twice. The resulting global bound is 18.465213. The product on a first-hit segment is therefore at most \(\exp(18.5/3)<512\), using \(\log2>2/3+2/81\). [Exact checker](distortion_bounds.py) · [Replay output](../../../reports/astra-unconventional-20261126/operator/distortion_bounds.txt)

For the sharper imported value, the initial-ascent cut has \(U\ge2^m-1>2\). In the two stated even-budget specializations, the general cut bound is \(U\ge2^{m-S}-1\ge1023>2\), since \(m\ge m_0=S+10\). Thus a first hit of \(U\) cannot have departed from 1. All its inputs are distinct and greater than one as required by Theorem 2.22. The cited preprint relies on its specified earlier finite computations. The local 400-shell proof above is independent of those records. Neither computation decides convergence for a new unrestricted ordinary component. [Nikzad, Frinkle and Bagherzadeh, Corollary 2.21 and Theorem 2.22](https://hexagonmath.org/pdf/2611.00033v1) · [Comparison of finite inputs, Paper 196](https://rstation.ai/problems/collatz/papers/196/v1)
