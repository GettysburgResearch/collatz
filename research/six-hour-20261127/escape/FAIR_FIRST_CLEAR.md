# A fair initial gate gives an ordinary interval law at first denominator clearance

Let \(n=2K\), \(K\ge1\), \(Q=2^n\), \(q=3^K\). Use every reduced numerator \(Q/2\le a<13Q/2\) coprime to 6, and the usual binary shortcut on \(a/q\). Condition uniformly on the actual sources whose odd-departure counts satisfy \(2g_i\ge i\) at every \(i\le n\). Let \(\tau\) be the clock just after the \(K\)-th odd departure, \(H=n-\tau\), and \(Y=T^\tau(a/q)\). This is the first ordinary integer on the path. Each odd departure removes one denominator factor three, and the final such departure takes a reduced odd \(v/3\) to \((v+1)/2\), so \(Y\not\equiv2\pmod3\).

**Written theorem.** There is an explicit proxy for the full joint distribution of \((H,Y)\) with total-variation error at most \(\min(1,113/n)\). Draw \(H\) with its exact physical tail
\[
  \Pr(H\ge h)=A_K(h):={2^h\binom{2K-h}{K}\over\binom{2K}{K}}
       \quad(1\le h\le K),\qquad A_K(K+1)=0.                         \tag{1}
\]
Conditional on \(H=h\), draw an ordinary integer \(Y'\) uniformly among those \(y\not\equiv2\pmod3\) in
\[
                 [2^{h-1},13\cdot2^{h-1}).                            \tag{2}
\]
Then \((H,Y')\) is the proxy. In particular for every event \(A_n\) depending arbitrarily on \(H\) and the **complete ordinary forward trajectory** of the reported integer,
\[
 \left|\Pr\big((H,(T^iY)_{i\ge0})\in A_n\big)
       -\sum_{h=1}^K\Pr(H=h)
           {\#\{y\text{ in (2)},\ y\not\equiv2\ (3):
                  (h,(T^iy)_{i\ge0})\in A_n\}\over4\cdot2^h}
 \right|\le113/n.                                                     \tag{3}
\]
The events may vary with \(n\). This includes finite decisions at any later deterministic or trajectory-dependent clock as well as any specified all-time orbit property. No independence between the ordinary future and its initial integer is assumed.

## Exact finite counts

A full word passing the fair gate determines one initial dyadic residue. It starts odd. Its six lifts in the source numerator interval include exactly four nonmultiples of three. The number of passing words of length \(2K\) is \(\binom{2K}{K}\). Indeed for words ending with grade \(j\ge K\), reflection of the initial walk through its first visit to \(-1\) gives a bijection between the rejected words and all words of grade \(j+1\); summing the resulting binomial differences telescopes.

At \(t=2K-h\), a word ending with its \(K\)-th one has a preceding fair nonnegative path of length \(2K-h-1\), grade \(K-1\), ending at height \(h-1\). Necessarily \(1\le h\le K\). The same reflection gives
\[
 \binom{2K-h-1}{K-1}-\binom{2K-h-1}{K}
                 ={h\over K}\binom{2K-h-1}{K-1}
\]
possible prefixes before that final one. Every completion for the last \(h\) ticks passes the full gate, since the grade is already \(K\). Consequently
\[
 \Pr(H=h)={2^h h\binom{2K-h-1}{K-1}\over K\binom{2K}{K}}
        ={h\over 2K-h} A_K(h)=A_K(h)-A_K(h+1),
\]
which proves (1).

For a selected prefix \(w\) ending at \(t\) put
\[
 B_w=2^{-t}\sum_{i<t:e_i=1}2^i3^{K-g_{i+1}}.
\]
The genuine forward equation at first clearance is \(2^tY=a+2^tB_w\). Thus its possible reports are exactly the integers outside \(2\bmod3\) in
\[
         [2^{h-1}+B_w,13\cdot2^{h-1}+B_w).                            \tag{4}
\]
For every listed integer, the inverse affine equation produces a numerator in the required interval. Its parity is odd because the word starts odd. The last bit is one, so \(a\equiv2^{t-1}(2Y-1)\pmod3\), which gives precisely the reduced-input restriction. The inverse binary branches over odd denominators realize every indicated parity. The full positive source therefore reaches its first integer at that clock. Both (2) and (4) have length \(6\cdot2^h\) and contain exactly \(4\cdot2^h\) admissible integers. Each is equally likely within its physical prefix.

For every selected prefix, \(g_{i+1}\ge(i+1)/2\). Summing the geometric series gives the deterministic bound
\[
  0\le B_w\le3^{(h-1)/2}\sum_{j\ge1}(\sqrt3/2)^j
            =(2+\sqrt3)3^{h/2}<4\cdot3^{h/2}.
\]
The two equal-size uniform laws in (2) and (4) have total-variation distance at most \((1+B_w)/(4\cdot2^h)\), since shifting an interval to the right by \(B_w\) removes at most \(\lceil B_w\rceil\) integers. Averaging over the actual prefixes at fixed \(h\) preserves that upper bound. Using \(\Pr(H=h)\le2h/n\) from (1), the joint distance is at most
\[
 {1\over2n}\sum_{h\ge1}h\left(2^{-h}+4(\sqrt3/2)^h\right)
       \le{113\over n};
\]
here \(\sqrt3/2<7/8\) and \(\sum_{h\ge1}h(7/8)^h=56\). Applying a deterministic ordinary trajectory map to both samples cannot increase the distance. This proves (3).

## Scales of the reported integers

The factorization
\[
           A_K(h)=\prod_{i=0}^{h-1}\left(1-{i\over n-i}\right)
\]
gives \(\Pr(H/\sqrt n\ge x)\to e^{-x^2/2}\) for every fixed \(x\ge0\). For \(h=O(\sqrt n)\), expand the logarithm to obtain \(-h(h-1)/(2n)+O(h^3/n^2)\). This Rayleigh limit describes the elapsed clock from the first ordinary state to the original census. Conditional on any \(h\to\infty\), the proxy's \(Y'/2^h\) tends to the uniform real distribution on \([1/2,13/2]\) by Riemann sums on the two admissible residue classes. Its limit is independent of the Rayleigh variable, by conditioning and the fact that \(H\) tends to infinity in probability. Both conclusions transfer to the physical pair.

Consequently any fixed set of ordinary integers having relative density \(d\) among \(y\not\equiv2\pmod3\) in (2) as \(h\to\infty\) is sampled with limiting probability \(d\) at true first clearance. Converting one of these statements into extinction requires an estimate on the specified ordinary future test itself. At the earlier critical initial gate the first-clear distribution instead has summable point weights and bounded initial real source heights. Its physical calculations and survivor tests are given in [the critical first-clear law](CRITICAL_FIRST_CLEAR.md). The fair initial sources in the present note have real heights proportional to \((2/\sqrt3)^n\).

The [Lean interfaces](FairFirstClear.lean) check the exact binomial tail recursion and difference, plus automatic completion of the fair gate from the first clearance. The reflection calculation, total-variation comparison and limiting law are written proofs. The [exact control](check_fair_first_clear.py) independently scans every reduced rational source through \(n=14\), reconstructs every physical prefix-target row at its tested depths, checks their complete coverage, compares the binomial tails through \(K=128\), and executes finite post-clear tests. [Retained output](FAIR_FIRST_CLEAR_CONTROLS.json)
