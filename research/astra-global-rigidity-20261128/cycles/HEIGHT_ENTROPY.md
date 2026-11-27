# Positive entropy of polynomially concentrated ordinary cycle phases

**PROPOSED.** Let a primitive positive ordinary Collatz cycle have least shortcut period \(n\), distinct shortcut states \(x_i\), and cyclic word \(w_i=x_i\bmod 2\), with \(T(x)=x/2\) at even inputs and \(T(x)=(3x+1)/2\) at odd inputs. Entropies in this note are measured in bits. A limiting law is the weak limit, along periods tending to infinity, of the uniform measures on the two-sided shifts of the periodic shortcut words. Each single finite-cycle measure itself has entropy zero.

Fix \(K>0\) and \(0\le c<1\). In each cycle pick any set of states of size \(L_n\) such that each length-\(m\) word occurs on at most \(B_n\) of the selected states, where \(m=\lceil K\log_2 n\rceil\) and \(B_n\le n^{c+o(1)}\). If \(L_n/n\to\delta>0\), every limiting law \(\nu\) on that sequence has
\[
                      h(\nu)\ge \frac{\delta(1-c)}K .                 \tag{1}
\]
One can use any \(\delta\) below the lower limit. An unconditional way to meet the multiplicity condition is to cover the selected states by \(B_n\) arithmetic progressions with arbitrary odd common differences, arbitrary starting heights and at most \(2^m\) terms each. In particular \([1,n^K]\) needs just one interval. Thus a zero-entropy limiting law forces the proportion in *every* such polynomial family of short progressions to vanish. No height bound is imposed on the unselected states. A polynomial number of progressions is allowed as long as its exponent is strictly below one.

## The finite bound and passage to entropy rate

On two starts with the same \(m\) parities, iteration and subtraction give
\[
             2^m(x'_m-x_m)=3^a(x'_0-x_0),
\]
where \(a\) is their common odd count. Consequently their sources agree modulo \(2^m\). Conversely congruent sources have the same first \(m\) parities by induction on \(m\). Each of the described progressions contains at most one representative of any residue since its step is odd and its length at most \(2^m\).

Choose a uniform phase \(I\) and its outgoing \(m\)-word \(W\). Conditional on \(I\) belonging to the selected set, the phase is uniform on \(L_n\) points and every fiber of \(W\) has size at most \(B_n\). Hence
\[
             H(W)\ge (L_n/n)\log_2(L_n/B_n).                         \tag{2}
\]
Indeed conditioning on membership only decreases entropy, and the conditional entropy of the phase given its word and membership is at most \(\log_2 B_n\). A high state may share its word with a selected state. No injectivity on that larger population is used.

For every fixed positive \(k\), partition \(W\) into length-\(k\) blocks and a final shorter block. Cyclic stationarity and subadditivity bound \(H(W)\le\lfloor m/k\rfloor H_k(\nu_n)+k\). For fixed \(k\) the finite binary block law and its entropy converge. Divide by \(m\), pass to the limit along the stated subsequence, then take the infimum of \(H_k(\nu)/k\) over \(k\). This proves (1). The same proof allows \(m/\log_2 n\to K\). It also applies to \(n\) pairwise distinct phases of an ordinary nonperiodic path, using an actual continuation: the uniform block entropies at a fixed translate of the sampling interval differ by \(o(1)\) uniformly over translates of size \(O(\log n)\), by coupling the shifted uniform intervals. Any limit is shift invariant. This conditional extension leaves open an arbitrary escaping orbit's height concentration.

## A positive proportion of discrepancies from low-complexity models

For a reference cyclic binary word \(v\) of length \(n\), let \(P_v(m)\) count its distinct cyclic \(m\)-factors, and \(E\) the Hamming distance between \(w\) and \(v\) in a chosen alignment. Let \(r\) be any integer with \(0\le r<m\), and \(V(m,r)=\sum_{j=0}^r\binom mj\). The same selected population obeys the exact finite bound
\[
      L_n \le B_n P_v(m)V(m,r)+\frac{mE}{r+1}.                       \tag{3}
\]
Each mismatch occurs in precisely \(m\) cyclic windows counted with multiplicity. Thus at most \(mE/(r+1)\) starts have more than \(r\) errors. The other selected starts use words in the Hamming balls about the reference factors, each with at most \(B_n\) selected realizers. This proves (3), including wraparound.

Write \(H_2(t)=-t\log_2 t-(1-t)\log_2(1-t)\), with lower inverse on \([0,1/2]\). Suppose at the stated scale \(P_v(m)\le 2^{(h_0+o(1))m}\), where the reference word and alignment can vary arbitrarily with \(n\). If \(0<(1-c)/K-h_0\le1\), then
\[
    \liminf E/n\ \ge\ \delta\, H_2^{-1}\big((1-c)/K-h_0\big).         \tag{4}
\]
For any \(0<t<1/2\) below the inverse, put \(r=\lfloor tm\rfloor\). The binary binomial bound gives \(B_n P_v(m)V(m,r)=o(n)\). Divide (3) by \(n\) and increase \(t\) to the endpoint. If \((1-c)/K>1\), the multiplicity and cardinality assumptions with positive \(\delta\) are already impossible since there are only \(2^m\) words.

In particular, (4) permits a moving reference subshift, finite-state model, finite template or individual word. Only its actual factor count at the indicated resolution is required. An ordinary finite template with length \(n\) can also be wrapped cyclically: the seam adds at most \(m-1\) distinct factors. The sharper factor \(\delta H_2^{-1}((1-c)/K-h_0)\) uses the actual error count across the selected low starts. No statistical independence of error sites is assumed.

## Insertions and deletions at positive density

Cut the physical word at any phase and compare it by a usual edit alignment with a finite binary template of *any* length. Let \(E\) count substitutions, insertions and deletions, each at cost one. Assume all the template's factor counts satisfy \(P(j)\le 2^{h_0j+o(m)}\) uniformly for \(m-r\le j\le m+r\). An absent length has count zero. For \(r/m\to t\in(0,1/2)\), define
\[
                V_{\rm edit}(t)=t+(2+t)H_2\big(t/(2+t)\big).
\]
The limiting inequality \(\liminf E/n\ge\delta t\) holds whenever
\[
           c+K\big((1+t)h_0+V_{\rm edit}(t)\big)<1.                 \tag{5}
\]
In particular bounded odd width and a moving zero-entropy factor dictionary force a distance exceeding \(0.02n\) asymptotically, even allowing all three edit operations.

Discard the final \(m-1\) possible physical windows at the cut. In each remaining window take exactly the columns from its first to its final output letter. Each substituted or inserted output letter appears in at most \(m\) windows, and each deleted input letter lies between the extremes of at most \(m\) windows. Thus at most \(mE/(r+1)\) windows contain more than \(r\) costly columns. Every other window projects to a template factor of length \(\ell\in[m-r,m+r]\).

For a fixed input factor of length \(\ell\), the number of length-\(m\) outputs realizable with \(a\) deletions, \(b\) substitutions and \(i\) insertions is at most
\[
         \binom{\ell}{a+b}\binom{a+b}{a}\binom mi\,2^i.
\]
Choose the removed or altered input positions, distinguish the two kinds, locate the inserted output positions and assign their bits. The other substitutions in a binary alphabet are forced. For each total \(j=a+b+i\le r\), summing the middle binomial over the possible splits gives \(2^{a+b}\), and summing over \(i\) by Vandermonde gives an upper bound \(2^j\binom{\ell+m}{j}\), even on dropping the output-length consistency constraint. Hence the entire edit ball has size at most \(2^r\sum_{j=0}^r\binom{2m+r}{j}\), which is \(2^{(V_{\rm edit}(t)+o(1))m}\). Multiply by the sum of the template factor counts over the possible \(\ell\), then by \(B_n\). Under (5) this is \(o(n)\). Including the discarded and high-cost windows proves (5). The strict numerical margin follows from
\[
  V_{\rm edit}(1/50)=\frac{1+\log_2(101^{101}/100^{100})}{50}
     <25/128<1/5.116201 .
\]
Continuity allows a fixed \(t>1/50\). The Hamming estimate still gives the stronger three-percent threshold when only substitutions are permitted.

## Consequence at every fixed odd width

Suppose the greatest odd state is at most \(R\) times the least odd state \(s\), with any fixed finite \(R\), along growing ordinary cycles. If \(p\) is the odd count, the exact cycle product gives
\[
        0<n\log 2-p\log 3\le p/(3s).
\]
Theorem 1 of Bondareva, Luchin and Salikhov, p. 18, gives the lower bound \(\gg n^{-4.116201}\) on this nonzero form, since \(n\asymp p\) by the displayed product. Thus \(s\ll n^{5.116201}\). Every even shortcut state is at most the largest immediate shortcut output from an odd state, at most \((3Rs+1)/2\). Apply (1) and (4) with \(B_n=1\), \(\delta=1\), and \(m=\lceil\log_2(C_R n^{5.116201})\rceil\). Every limiting parity law has entropy at least \(1/5.116201\) bits per shortcut step, and even a moving reference with subexponential factor count at these logarithmic horizons has asymptotic Hamming distance at least
\[
                  H_2^{-1}(1/5.116201)> 0.03 .
\]
The same consequences hold under polynomial maximum height \(n^{K+o(1)}\) with \(K\) in place of \(5.116201\), for any fixed finite \(K\ge1\). This is a proportion of the *whole* primitive parity lap; it cannot be inferred from a lower bound on the number of mismatches alone. [Primary logarithmic estimate](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

Weaver 223/v1 §2 uses the individual low-state window injection and §3 counts windows meeting at least one substitution at one explicit period/count pair. The PR211 mechanical-distance theorem at `4b44cded44af5bb7c3ce67fb16a70c898ad505d5` gives square-root Levenshtein separation at unrestricted height using a real discrepancy bound. Here the Hamming-ball count accommodates positive local error rates on arbitrary model words, obtains linear separation under polynomial concentration, and gives a Shannon entropy statement independent of a reference word. These are distinct hypotheses. The finite-state avoidance and full-denominator census in the same PR concern the total periodic-state population across cycles. [Weaver 223/v1](https://rstation.ai/problems/collatz/papers/223/v1) · [Pinned mechanical-distance proof](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/cycles/spectrum/MECHANICAL_DISTANCE.md) · [Pinned full-denominator census](https://github.com/GettysburgResearch/collatz/blob/4b44cded44af5bb7c3ce67fb16a70c898ad505d5/research/astra-reciprocal-rigidity-20261127/cycles/phase8/DENOMINATOR_CENSUS.md)

Witteveen's earlier threshold argument applies a factor-count pigeonhole bound to a specific bounded-amplitude odd-valuation language, followed by an irrationality bound. This is an antecedent for the all-low counting principle. Equations (1)–(5) instead quantify selected physical populations, their limiting measure entropy, and their distance from external model words. [Witteveen, §5 at fc08547](https://github.com/kulltc/collatz-entropy-barriers/blob/fc0854799b094fa04250ce8309279609276f3c58/paper/main.tex)

## The remaining physical obstruction

An ordinary cycle with positive entropy in its *limiting* parity law meets (1). A sequence with a zero-entropy law could have almost all states above every polynomial in its period, despite one polynomially bounded minimum. The argument excludes neither possibility. The construction of invariant measures on binary windows of 2-adic Collatz dynamics does not identify the full conditional parity process with fair coins, even when its averaged window measure is Lebesgue. No measure-rigidity theorem is used in (1)–(4). [Window measures and conditional digits, §§5–6](https://rstation.ai/problems/collatz/papers/170)

## Exact antecedent

The all-low-height full-cycle entropy conclusion is already in [PR195, `PHASE_POPULATION.md`, final paragraph, at 3fa7ef4a0011b35447a70f587b400878d5ea8ebe](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/cycles/PHASE_POPULATION.md), alongside its earlier nonperiodic height-to-entropy argument. The selected positive fraction, arbitrary translated odd-step progressions, collision-aware conditioning, and Hamming/Levenshtein conclusions here are the extensions.
