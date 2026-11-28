# The lower edge of the original parity-type budget

Let \(T(2x)=x,\ T(2x+1)=3x+2\), let \(Q_t(n)\) count the odd departures at times \(0,\ldots,t-1\), and put
\[
 L=\log_2N,\quad t=\lfloor\kappa L\rfloor,\quad
 \theta=\log_2 3,\quad D=1-\theta/2,\quad p_0=(1-1/\kappa)/2.
\]
Fix any \(\kappa>1\). Count all ordinary \(1\le n\le N\) with \(Q_t(n)\le pt\), writing this count as \(A_N(p)\). For \(p_0<p<\min(1/2,(1-1/\kappa)/\theta)\), set \(r=(\kappa p-(\kappa-1)/2)/D\). Then
\[
 \limsup_N L^{-1}\log_2 A_N(p)\le G(r),\qquad
 G(r)=\inf_{0<z<1}\left[-\log_2z+
 r\log_2\frac{z^{1-\theta}(1+z^2)}{1-z^6}\right].                 \tag{1}
\]
In particular the usual fair-coin upper bound \(A_N(p)/N\le 2^{-t(1-H_2(p))}\) holds eventually, with an exponential saving, whenever
\[
                   G(r)< F_\kappa(p):=\kappa H_2(p)-(\kappa-1).       \tag{2}
\]
This condition includes a nonempty interval immediately above \(p_0\) for every \(\kappa>1\). Each interior point of that interval has exponentially many actual witnesses, even restricting to the source octave \((N/2,N]\).

More precisely, as \(r\downarrow0\) at fixed \(\kappa\), first taking the large-\(N\) limits, both lower and upper exponential counting rates satisfy
\[
 \liminf_N L^{-1}\log_2 A_N(p),\quad \limsup_N L^{-1}\log_2 A_N(p)
   =r\log_2(1/r)+r\log_2(e/3)+O(r^2).                              \tag{3}
\]
The assertion in (3) bounds both rates, without asserting their equality at a supplied positive \(r\). At \(p=p_0\) the count is at most \(2^{o(L)}\), whereas the fair allowed counting exponent is positive. For \(p<p_0\) the count is eventually zero. Thus a matching two-sided fair type law on the full range fails for every \(\kappa>1\). The book asks for the **upper bound**. Equations (1)–(2) give it on a lower-tail sector and leave the remaining nontrivial types open. [Polson–Sokolov v1.4.0, R6 at its source pin](https://github.com/VadimSokolov/collatz/blob/5840497a23fc0d64127b850aea68862d7c93f2b7/book/chapters/ch10h_ratchets.tex#L783-L785)

## A true first arrival inside the full observation

For every positive \(x\), every \(j\ge0\),
\[
 1\le T^j x=x2^{-j}\!\prod_{i<j:\,T^ix\ {\rm odd}}(3+1/T^ix)
       \le x2^{-j}4^{Q_j(x)}.                                      \tag{4}
\]
This proves the lower support bound. For \(p\) in (1), choose one fixed integer \(M>2\) with \(\kappa p\log_2(3+1/M)<\kappa-1\). Every tested path enters \([1,M]\) by time \(t\) for large \(N\), since otherwise (4) with each odd factor bounded by \(3+1/M\) contradicts the positive final height. If the first small state is even, its successive halvings lead to an odd \(y\le M\) in at most \(\lfloor\log_2M\rfloor\) more steps. Let \(h\) be the first time at any such small odd state, and \(q=Q_h(n)\). Thus \(h\le t+O_M(1)\) and \(y=T^h n\). Before that first visit the states are distinct, since a repetition in the deterministic path would prevent the later first visit. Ordering the distinct odd departures gives
\[
 0\le C_h=\sum_{i<h:\,T^in\ {\rm odd}}\log_2(1+1/(3T^in))
           \le (1+\ln(1+h))/(3\ln2).
\]
The exact height then gives \(h=\log_2(n/y)+\theta q+C_h\le L+\theta q+O_M(\log(2+t))\). For \(h\le t\), (4) at \(y\) shows \(Q_t(n)\ge q+(t-h-\log_2 y)/2\). If \(h>t\), the few intervening steps cost at most \(O_M(1)\). Thus in both cases
\[
        Q_t(n)\ge(t-L)/2+Dq-O_M(\log(2+t)),\qquad
        q\le r L+O_M(\log(2+t)).                                   \tag{5}
\]
This uses the actual suffix from the reached integer, including visits to \(2,1\) and any later motion of that integer.

## Arithmetic inverse count

Write \(n=2^k u\) with \(u\) odd. If \(q=0\), there are at most \(M(1+t+O_M(1))\) possibilities. Otherwise \(y\) is a ternary unit and the part from \(u\) to \(y\) consists of \(q\) accelerated odd steps with valuations \(e_i\ge1\) and \(k+\sum e_i=h\). Reading out from \(y\), the inverse step is \(I_e(v)=(2^ev-1)/3\). All intermediate odd sites are units modulo three, because they are actual accelerated outputs. The outermost child \(u\) can be a multiple of three. For every odd unit \(v\), in each full period of six positive exponents exactly two classes give an integral unit child. This follows from order six of two modulo nine. Both classes have the same parity, so for \(0<z<1\)
\[
  \sum_{e:\, I_e(v)\ {\rm integral\ unit}}z^e\le A(z)=\frac{z+z^3}{1-z^6}.
\]
The last unrestricted integral child costs at most \(z/(1-z^2)\), and summing \(z^k\) over initial even prefixes costs at most \((1-z)^{-1}\). Every individual exponent list and initial even clock determine at most one source at the supplied endpoint. Consequently, for fixed \(z\), the number with \(q\ge1\) fixed is bounded by
\[
  O_{M,z}\big((2+t)^{C_z} z^{-L}(z^{-\theta} A(z))^q\big).
\]
Here the cost \(z^{-h}\) uses the upper bound for \(h\) in (5). Since \(z^{-\theta}A(z)>1\), summing (5) proves (1). At \(p_0\) the same proof has \(q=O(\log t)\), hence the elementary bound \(O_M(t^{O(\log t)})\) from all choices of the \(q\) positions. As \(r\downarrow0\), one has \(G(r)\to0\), by taking \(z\uparrow1\) after the \(r\) limit. Strict concavity gives \(H_2(p_0)>2p_0\), so \(F_\kappa(p_0)>0\); (2) follows on an open sector.

The following rational test values give entire closed intervals \([p_0,p_1]\) satisfying the fair bound. For the displayed \(z\), the difference of \(F_\kappa\) and the trial expression in (1) is concave in \(p\), so checking both endpoints suffices. The fair probability rate is \(t(1-H_2(p))\) in base two. The last column is a conservative additional saving per \(L\) before polynomial factors.

| \(\kappa\) | \(p_1\) | \(z\) | certified margin |
|---:|---:|---:|---:|
| 1.01 | .0062 | .994 | .0008 |
| 1.10 | .056 | .952 | .0070 |
| 1.25 | .121 | .907 | .0060 |
| 1.50 | .195 | .870 | .0081 |
| 2 | .280 | .839 | .0135 |
| 3 | .359 | .815 | .0080 |
| 4.82 | .414 | .804 | .0225 |
| 6 | .432 | .797 | .0035 |
| 10 | .459 | .799 | .0480 |

## Matching sparse-edge count

For an upper count, an intermediate exponent has the form \(6m+d\) with \(1\le d\le6\), \(m\ge0\); enumerate the two admissible choices in ascending order at each visited state. Allow three choices at the outermost child. Thus (5) bounds the stars-and-bars count from above by a polynomial times
\[
 \sum_{q\le rL+O(\log t)}
        2^q {\left\lfloor (L+(\theta-1)q+O(\log t))/6\right\rfloor+q\choose q}.
                                                                    \tag{6}
\]
All integer rounding and the leading factor \(2^k\) cost only polynomial factors. The summands are bounded by the same expression at the largest allowed \(q\), since \(\theta>1\).

For a lower count start at \(1\). For each \(m_i\ge0\), choose either unit child with \(e_i=6m_i+d_i\), \(3\le d_i\le8\). Each odd child strictly exceeds its parent. Therefore its path back reaches \(1\) for the first time after exactly the stated \(q\) odd departures. Different choices give distinct positive odd ancestors by their deterministic forward valuations. The resulting \(u\) satisfies \(u\le2^{\sum e_i}3^{-q}\) by successive positive inverse steps. Choose
\[
 q=\lfloor rL\rfloor-O(1),\qquad
 6\sum m_i\le L+(\theta-8)q .
\]
For sufficiently small fixed \(r>0\) the budget is positive. Then \(u\le N\) and \(n=2^{\lfloor\log_2(N/u)\rfloor}u\in(N/2,N]\); distinct odd parts still give distinct starts. At first hit \(1\), \(h=\log_2 n+\theta q+C_h\). The correction is \(O(\log L)\), since the constructed \(h=O(L)\) from its displayed budget and initial halving time. Hence \(h<t\) whenever \(\theta r<\kappa-1\) with strict slack. On the alternating tail,
\[
 Q_t(n)=q+\lceil(t-h)/2\rceil\le(t-L)/2+Dq+1.
\]
Subtracting a fixed sufficiently large integer in the choice of \(q\) ensures \(Q_t(n)\le pt\), including the floor in \(t\). This gives at least
\[
            2^q {\lfloor(L+(\theta-8)q)/6\rfloor+q\choose q}         \tag{7}
\]
sources. For each fixed \(p>p_0\), taking \(q=cL+O(1)\) for sufficiently small \(c>0\) gives exponentially many eligible ordinary sources in the same octave.

By the entropy form of Stirling, the upper rate (6) and lower rate (7), near zero, respectively have the form
\[
 r+[(1+Cr)/6]\,H_2(6r/(1+Cr)),\qquad C=\theta+5,\ \theta-2 .
\]
Both expand as (3). In particular the sparse-edge count reflects the two permissible unit classes in each block of six exponents. The elementary first-arrival and counting argument uses no orbit convergence assumption or external stochastic approximation.

## Relation to existing bounds

Inselmann's Theorem 3.3 gives a power-small exceptional set for each fixed parity-fraction deviation up to the natural clock \(\kappa_* L\), \(\kappa_*=1/D\). Converting its \(\log_2 n\) to the fixed \(L\) uses a power-small bottom interval and the deterministic time Lipschitz bound. The exponent there need not equal the fair rate. PR213's source-cell bound concerns the opposite, upper tail and gives a near-fair exponent on small linear additional-clock bands, with an arbitrarily small dimension loss when the band is chosen after the loss. The critical Gaussian and supercritical parity criterion already occur in this pass and in parallel PR215. They concern concentration or central fluctuations. [Inselmann, arXiv:2402.03276v3, Theorem 3.3](https://arxiv.org/html/2402.03276v3) · [PR213, linear native source loss](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/mass/LINEAR_NATIVE_SOURCE_LOSS.md) · [Critical native count, checkpoint 8](https://github.com/GettysburgResearch/collatz/blob/f99cce768e1d5644cabd50ae277bc74cb3c60a11/research/astra-global-rigidity-20261128/mass/CRITICAL_NATIVE_COUNT.md) · [PR215, terminal windows](https://github.com/GettysburgResearch/collatz/blob/8a50018b6a861e810b18512fdd59aaf45214bba1/research/astra-nine-hour-20261128/escape/TERMINAL_WINDOWS.md).
