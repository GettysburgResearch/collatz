# Effective native clock bounds when long single-arm descents do not keep revisiting the same slope

Use the shortcut map on the two positive ordinary inputs \(s,3s\), \(s\) odd. Assume the two states remain distinct at every common native date through \(L\), and denote the total odd grade on the two paths by \(G\). Ignore common-even dates in forming the list of active events. Make each simultaneous-odd event a separate piece and split the remaining list into maximal runs in which only the same physical arm is odd. Let \(R\) be the number of resulting pieces. Each piece includes the consecutive common-even dates immediately following each of its events, through the next active event or the end of the prefix.

On a single-arm run the slope exponent of the moving arm relative to the even arm increases by one at each odd departure. Before equality of slopes, call the segment with the smaller slope on the moving arm **descending**; there the absolute gap \(j>0\) drops by one per odd departure. For \(j\ge1\), count the descending segments in which an event departs from gap \(j\). Let \(V\) be the maximum of these counts over \(j\), with maximum zero if no such event occurs. Thus \(V\le R\). All these quantities can be read from the two finite parity words.

**Proposed bound.** Set \(N=G+2\), and let \(k\) be any integer in \([1,N]\). There is an effective absolute \(C\) such that
\[
 L\le C\left[\frac{N^2}{k}+(R+1)kN+
       V kN\,e^{Ck^2}(N+1)^{1-\delta_k}\right],
 \qquad \delta_k^{-1}=(k-1)!\sum_{i=0}^{k-1}\frac1{i!}.                \tag{1}
\]
For example, for every fixed \(0<\alpha<1\), with \(b(N)=\log\log N/\log\log\log N\), the fully effective estimate
\[
 L\ll_\alpha \frac{N^2}{b(N)}
 \quad\text{holds if}\quad
 R\le N/b(N)^2,\qquad V\le \exp((\log N)^\alpha)                    \tag{2}
\]
for all sufficiently large \(N\) with effective onset. The same estimate holds if simply \(R\le\exp((\log N)^\alpha)\). This allows growing numbers of switches, arbitrary lengths of even coasts, and unbounded slope excursions. The conditional incidence hypotheses are explicit; a repeated common-odd periodic shadow can fail them.

## The scalar estimate at arbitrary entry heights

The [effective denominator-clearing packet theorem](../literature/EFFECTIVE_WORST_LANDING.md) provides a single exceptional set \(E_{N,k}\) of cardinality at most \(\exp(Ck^2)(N+1)^{1-\delta_k}\). We need its proof for the enlarged collection of **all** starts \(u/3^h\) with \(k\le h\le N,\ 0<u\le3^N,\ u\) odd and prime to three; some starts can have real value greater than one. The proof applies directly to this collection. Every subsequent normalized numerator is still at most \(3^N\) because its update is either halving or averaging with \(3^{h'-1}\le3^N\). The initial value \(u\) is a ternary unit. The \(k\) odd dates \(t_i\), final duration \(d\) and terminal numerator \(v\) have exactly
\[
                u+\sum_{i=1}^k3^{h-i}2^{t_i}=2^d v .
\]
The duration is at most \(k(1+N\log_2 3)\). These are all hypotheses used in the box, minor and valuation argument of that theorem; one can form its finite matrix on this entire collection at the outset. Consequently outside \(E_{N,k}\) every such packet has duration \(<2N\), including its final even coast through the next odd source, truncated at integral landing if the old denominator clears.

## Reading the actual signed lines

After the mandatory first ordinary step the states on each arm are ternary units. On orienting a nonzero slope gap as \(B=3^jA-a\), \(a\) is a nonzero integer, \(|a|\le3^N\), and \(3\nmid a\) for \(j>0\). At zero gap the translation is again nonzero as the ordinary states differ. These are the normalized [physical determinant bounds](PAIRED_SOURCE_GRADES.md). The first step leaves \(j=1,\ a=1\) in the orientation with the higher affine slope on the left, since \(T(3s)=3T(s)-1\). Common-even dates replace \(a\) by \(a/2\) and hence cost at most \(N\log_2 3\) consecutively.

Each simultaneous-odd piece costs \(O(N)\), using this last bound for the following even coast. Along a single-arm run, split at the at most one zero crossing of the relative slope. During the part in which the moving arm has the higher slope, an active step has \(2a'=3a-1\), and a common-even step has \(2a'=a\). At gap zero choose the orientation that will make the moving arm the higher one. Since every endpoint translation in this part is nonzero, multiplication of \(2|a'|\le4|a|\) on active dates and \(2|a'|=|a|\) on others bounds its whole duration by twice its grade plus \(N\log_2 3\). Extra coasts at the initial step or at a zero crossing can also be charged \(O(N)\) once per run.

On the descending segment the moving arm is \(A\), the passive arm \(B\). An active step sends \(j\) to \(j-1\) and \(2a'=a+3^{j-1}\). On common-even dates the level is unchanged and \(2a'=a\). All input dates with \(a<0\), summed across the full prefix, cost \(O(G+1)\) by the [signed physical potential](POSITIVE_DESCENDING_INTERVALS.md). Once positive, the translation stays positive on this segment. Any initial common-even coast before its first positive odd departure costs \(O(N)\). At that odd departure \(a\) is odd and prime to three. The ensuing word through the next change of moving arm or the zero crossing agrees exactly with the initial part of a scalar descent from \(a/3^j\). Indeed the passive arm is even, so the parity of the moving arm equals the parity of \(a\), and the normalized recurrence just given is the scalar one. This comparison covers truncation just before the passive arm next becomes odd. Any even dates after the zero-gap integral landing are covered by the zero-crossing coast charge.

Partition each such positive scalar segment into packets with exactly \(k\) odd departures, and a shorter terminal piece if needed. End a full packet just before the next scalar odd mark, at landing, or at the physical end of the segment. For a truncated packet its actual duration is at most the corresponding true scalar duration. Across all runs, the packets starting outside \(E_{N,k}\) cost at most \(2NG/k\). Each exceptional starting level contributes at most \(V\) full packets since the charge is at a physical decreasing event and no decreasing run uses that level twice. Those exceptional packets cost at most \(V|E_{N,k}|k(1+N\log_2 3)\). Each run's incomplete tail costs at most \(k(1+N\log_2 3)\). Together with the initial and sign costs, this proves (1).

For (2) use natural logarithms and take \(k=\lfloor c_\alpha b(N)\rfloor\) with \(0<c_\alpha<(1-\alpha)/2\). The factorial estimate yields \(\delta_k\log N\ge(\log N)^{1-c_\alpha}\) for all sufficiently large \(N\), with effective threshold. This dominates \(\log V+Ck^2+3\log(k+2)\), giving the required bound on the final term. The stipulated \(R\) bound handles the middle term.

## Why this argument distinguishes revisits

An effective bound \(K(G)\le G^2\rho(G)\) on the unrestricted maximal ordinary clock, with a computable modulus for \(\rho(G)\to0\), would already imply an effective superlinear lower bound for \(\operatorname{ord}_{2^\ell-3}3\) relative to \(\ell\). Indeed let \(j\) be that order, enter the one-odd rational center \(1/(2^\ell-3)\) by the [physical universal entrance](UNIVERSAL_RATIONAL_MERGERS.md), and realize \(j\) full laps on an unmerged positive ordinary lift. The total grade is at most \(C_0(j+1)\) and the tail alone has length \(j\ell\), with effective \(C_0\). Thus an effective bound of the specified kind yields
\[
                   \ell\le C_1(j+1)\rho(\lceil C_0(j+1)\rceil).
\]
Here \(j\ge\log_3(2^\ell-2)\) for \(\ell\ge3\), so an effective modulus in \(j\) indeed supplies one in \(\ell\). The existing [Corvaja–Zannier consequence](RATIONAL_PERIODIC_SHADOWS.md) proves \(j/\ell\to\infty\) with ineffective onset. Quantitative counts of exceptional inputs alone do not exclude one far-out repeatable input. Formula (1) uses the different situation in which the number of visits to an exceptional descending level is known. No unrestricted effective clock, logarithmic upper bound, or finite last exceptional order is asserted.
