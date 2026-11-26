# Many finite ordinary records already have large closings on both sides

**Status.** Proposed written finite-family result. The binomial comparison in the proof is checked by the exact Python control. This counts changing sources and quantifies their necessary growth.

Let \(L=1536\), \(n=tL\), and \(X=3^n\). For all sufficiently large \(t\), there are at least \(cX^{0.94}\) distinct odd integers \(q\in[X,3X)\) with the following two properties, where \(c>0\) is independent of \(t\).

* Each \(q\) ends an actual positive path of \(n\) odd steps as a strict upper record of its coefficient multiplier.
* **Every** past closing with \(0.95\log_3q\le b\le\log_3q\) and every future closing with \(0.95\log_2q\le h\le\log_2q\) on that path has reduced denominator greater than \(q^{0.26}\). The clocks are integers, and the two types of closing are the physical ones in [FORCED_CLOSINGS.md](FORCED_CLOSINGS.md).

### An elementary supply of distinct record integers

Set \(S=\lfloor L\log_2 3\rfloor=2434\). There are \(\binom{S-1}{L-1}\) positive compositions of \(S\) into \(L\) gaps. Partition them into rotation classes, each of size at most \(L\). In each class one can rotate the word so that every running sum \(S_j\) satisfies \(S_j-j\log_2 3<0\): start immediately after a maximum of the unrotated sums at times \(0,\ldots,L-1\). The sums at different times are distinct by irrationality; a wrapped prefix acquires the strictly negative total increment. Select one such reversed critical word per class. This supplies at least \(N=\lfloor\binom{2433}{1535}/1536\rfloor\) distinct words, and the exact inequality \(N^{50}>3^{47L}\) gives \(N>3^{0.94L}\).

Read these words in the inverse direction, beginning at the eventual terminal. Every concatenation of \(t\) selected words is a critical script of length \(n\). Its total inverse slope is \(\lambda^t\), where \(\lambda=2^S/3^L<1\). The inverse map of a single selected block has the shape \(y\mapsto\lambda y-B\), with \(B\ge0\) bounded by a finite \(B_L\) on this finite collection. The composed inverse map is \(y\mapsto\lambda^ty-C/3^n\), where \(0\le C/3^n\le B_L/(1-\lambda)\). Its ternary residue condition is \(2^{tS}q\equiv C\pmod {3^n}\).

At a fixed admissible residue there is exactly one odd representative \(q\in[X,3X)\). Inverting the script from this integer gives integral odd values at each step: full divisibility by \(3^n\) implies every intermediate inverse divisibility by the chronological affine identities. Explicitly, at inverse depth \(j\) the state is \(2^{S_j}3^{-j}(q-\beta_j)\), where \(\beta_j=\sum_{i=1}^j3^{i-1}2^{-S_i}\). Every such state is positive since \(\beta_j\le (3/2)^j-1<X\). All these inverse gaps are therefore exact, and following the resulting ordinary source forward gives the prescribed path. The reversed strict prefix inequalities make its terminal an actual strict coefficient record relative to its starting time.

If two scripts in this fixed residue had the same carry \(C\), their initial states would coincide by the affine formula at the common clocks. The ordinary forward map from that state is deterministic, so the scripts would be equal. Distinct scripts therefore give distinct carries in one residue class modulo \(3^n\), in an interval of length \((B_L/(1-\lambda))3^n\). Each residue has at most \(1+\lfloor B_L/(1-\lambda)\rfloor\) scripts. Consequently the resulting collection of distinct ordinary \(q\)'s has size \(\gg_L N^t\gg X^{0.94}\). This is the equal-length special case of the earlier bounded-overlap mechanism, and the above proof provides its full finite inputs. [PR201, record renewal, Sections 2.1–2.3](https://github.com/GettysburgResearch/collatz/blob/94ce06ccbd312ccd0ce4450b567cc514a2f0b54a/research/killed-green-head-closure-20261124/record-renewal/README.md)

### Counting all possible small rational closings

Put \(\theta=0.95\), \(\delta=0.26\), \(\rho=\log_3 2\). Uniformly over the two indicated clock ranges and \(q\in[X,3X)\), the real bounds of [FORCED_CLOSINGS.md](FORCED_CLOSINGS.md) give \(|\zeta|\le X^{1-\rho+o(1)}\). All possible reduced rationals with this real bound and denominator at most \((3X)^\delta\) number \(O(X^{2\delta+1-\rho+o(1)})\), by summing over the denominators. At a prescribed past or future clock, one such phase forces \(q\) into one residue class modulo respectively \(3^b\) or \(2^h\), of size at least \(X^\theta\). At most \(O(X^{1-\theta})\) integers of the interval can belong to this class. There are \(O(\log X)\) clocks in total. Thus the number of ordinary integers in the entire interval admitting *any* such small closing, even after allowing all compatible past paths, is
\[
 O\left(X^{1-\theta+2\delta+1-\rho+o(1)}\right)=o(X^{0.94}).
\]
The strict gap follows from \(2^{100}>3^{63}\), which gives \(\rho>0.63\). Subtract this bound from the constructed population.

If \(u\) is any of the constructed initial integers, the upper growth per odd step gives
\[
 u+1\ge (2/3)^n(q+1)>2^n .
\]
The same starting value also satisfies \(u\le\lambda^t q\) by positivity of the inverse carry. These are genuine growing ordinary sources with substantial height gain. The construction samples exactly \(n=\lfloor\log_3q\rfloor\) past odd steps; a sufficiently late actual escape record generally has a deeper earlier history anchored at one fixed integer.

### Large denominators can be created by one exceptional bit

Consider any shortcut word of \(h\ge2\) bits containing exactly one zero, with \(r\) ones after that zero. The odd affine branch fixes \(-1\). The exceptional even branch creates displacement \(1/2\), and the remaining ones multiply it by \((3/2)^r\). Therefore the rational closing satisfies
\[
 \zeta+1=\frac{2^{h-r-1}3^r}{2^h-3^{h-1}}.
\]
The numerator and denominator are coprime, so the reduced closing denominator equals the entire raw denominator. Across a nested family of prefixes that each contain the same sole exceptional zero, every such closing already has this maximal denominator. Any prescribed finite parity word is realizable at a positive integer by the ordinary parity congruence. This example addresses the inference from a large denominator to a large number of local parity defects.
