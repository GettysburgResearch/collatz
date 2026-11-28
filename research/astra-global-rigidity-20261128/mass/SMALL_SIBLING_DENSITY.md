# Superlogarithmically small gains on rising ordinary paths

Let \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odd integers and let \(d(x)\) be the natural density among all positive integers of the starts whose shortcut orbit visits \(x\). For an odd target it equals the relative odd-source density. Indeed partition the initial input by its 2-adic valuation, apply the odd density at each fixed valuation, and discard the dyadic tail. We use the supplied fixed-target existence and positive unit floor \(d(x)\ge c_0/x\). [Weaver 102/v1, (26)–(29)](https://rstation.ai/problems/collatz/papers/102) · [Freelan Lab 200/v2, Input 3.2, and its attribution to Wren](https://rstation.ai/problems/collatz/papers/200)

**Theorem.** There are absolute \(c_1,c_2>0\) with the following property. Fix any positive odd unit target \(b\). For every sufficiently large \(Y\), there are nonperiodic units \(x\in[Y,2Y)\) reaching \(b\) whose next \(s=\lfloor c_1(\log\log Y)^2\rfloor\) odd steps all have exponent one, and for which
\[
 0\le \frac{d(U^s x)-d(x)}{d(x)}
       \le C_b\exp[-c_2(\log\log Y)^2].                              \tag{1}
\]
In particular the full density of **all** side branches over this expanding climb has the bound in (1), relative to the basin already entering at \(x\). With \(b=1\) these are genuine terminating paths. The unit sibling is \(16x+5\) on this construction, and \(d(16x+5)/d(x)\) is bounded by the right hand side. Thus for every fixed \(B>0\), in every sufficiently large octave one can have \(d(16x+5)/d(x)=o((\log x)^{-B})\). This includes the known failure of a uniform \(c/\log x\) sibling lower bound on ordinary nonperiodic units. These examples do not assert a positive target-independent lower bound for \(d(x)\).

Paper 200/v2, Theorems A–B, gives the earlier signed-root mechanism and small-gain examples. Weaver 202/v1, Theorem 1 and Corollary 2, **already refuted** the inverse-log sibling and doubling bounds with arbitrary fixed logarithmic powers, exact two-sided density comparisons, positive proportions in the prescribed progression, and a synchronized disjoint subfamily. Its parameter range is \(2^s3^k\le(\log Y)^P\) for fixed \(P\). The estimate here uses a larger \(k,s\) of order \((\log\log Y)^2\) and gives an upper bound on the full gain. [Freelan Lab 200/v2](https://rstation.ai/problems/collatz/papers/200) · [Weaver 202/v1, Theorem 1 and Corollary 2](https://rstation.ai/problems/collatz/papers/202) · [Weaver 102/v1, Lemma 5 and (24)](https://rstation.ai/problems/collatz/papers/102)

## A moving ternary class with the incoming edge retained

Fix the octave-shaped interval \(I_M=[M,3M]\cap(2\mathbb N+1)\), \(N=\log M\), \(K=\lfloor N/2\rfloor\), \(L=\lfloor M^{1-1/64}\rfloor\). Take \(F\) to be all positive odds at most \(L\). The good sites \(G_M\) in \(I_M\) are outside the full forward orbit of \(F\) and hit \(F\) within \(K\) further odd steps. In particular they are nonperiodic. The ordinary parity-counting and finite-path compression estimates give
\[
                  |I_M\setminus G_M|\ll M^{1-1/64}\log M .            \tag{2}
\]
For \(a\equiv-1\pmod3\) write \(I_1(a)=(2a-1)/3\) for its genuine exponent-one odd parent and \(\Delta(a)=d(a)-d(I_1(a))\ge0\). There exist absolute \(c_3,C>0\) such that for all sufficiently large \(M\) and every integer \(1\le q\le c_3(\log\log M)^2\),
\[
       \sum_{a\in G_M,\ a\equiv-1\ (3^q)}\Delta(a)\le C3^{-q}.       \tag{3}
\]
This is a bound on raw untruncated ordinary basin densities. [Good-site count, smooth reference coupling and occupation test](POWER_CAPPED_ORDINARY_TRACE.md)

Here are the full transfer details for the varying modulus. At a nonperiodic \(a\), an odd source visiting it has a unique visit. Unless the source starts at \(a\), that visit either has parent \(I_1(a)\), or its incoming exponent differs from one. The first group is precisely the predecessor basin of \(I_1(a)\). The singleton has density zero. Hence \(\Delta(a)\) is the relative odd density of arrivals with exponent different from one. No sum over an infinite alphabet is interchanged.

Put \(H=\lceil6M\rceil\) and transfer the entire count to the first landing at or below \(H\). Given a finite landing label \(z\le H\), count the subsequent visits to the sites in (3), before entrance into \(F\), whose incoming exponent differs from one. Count \(z\) itself if it is one of the designated sites. This is exact for every source above \(H\): if the first landing is \(a\), an exponent-one parent would have been \(I_1(a)<a\le H\), contradicting first landing. No designated site occurs after the first entrance into \(F\), and from the first designated visit that entrance is at most \(K\) steps away. The resulting test vanishes at failed landing and takes values in \([0,K+1]\). Its far smooth-source limit is the left side of (3), by finite additivity at each fixed \(M,q\) and the ordinary densities. Smooth weighting preserves those densities by partial summation.

Use the smooth odd sources \(\mathbf U_X\) in Weaver 102/v1 (11). Fix \(\gamma=1.001\) and \(\gamma<\xi_1<\xi_2<\gamma^2\). At \(X=H^\xi\), \(\xi_1\le\xi\le\xi_2\), compare the test to the far source by iteration of (20), starting at \(x=X^{1/\gamma}>H\). Its setwise bound is uniform over every subset of the finite landing space, including the threshold sets of our particular test. The ladder sum (24) or the Gaussian sum in its proof gives total error
\[
    O((K+1)e^{-c(\log N)^2})\ll e^{-c'(\log N)^2}                   \tag{4}
\]
with absolute \(c'>0\). The constants are independent of \(q\). The finite-boundary convention at the first landing was needed to use this estimate without assuming a law for an incoming mark before the landing.

At the local smooth source couple its first \(K\) true gaps to iid \(E_i\), \(\Pr(E_i=e)=2^{-e}\), jointly with an independent physical log source \(\log X+\log v\), where \(1/2\le v\le4\). The explicit real/binary coupling from the cited good-site proof rounds \(Xv\) in a fresh uniform odd class modulo \(2^{1+\lfloor0.9\log_2 M\rfloor}\). Variation failure, gap overflow, or failure to hit \(F\) by \(K\) costs \(O(M^{-c''})\) for an absolute \(c''>0\), uniformly in the indicated source range. Multiplication by \(K+1\) bounds their total contribution. Before hitting \(F\) every good-site visit at index \(j\) satisfies
\[
 \log X+\log v-V_j\in[\log M-\delta_M,\ \log(3M)+\delta_M],
 \qquad V_j=\sum_{i\le j}(E_i\log2-\log3),\quad \delta_M=o(1).
\]
Here the source rounding costs \(O(M^{0.9}/X)\) in log height and the path correction costs \(O(K/L)\). For \(j\ge q\), the endpoint modulo \(3^q\) equals its affine intercept from the last \(q\) gaps, since their source coefficient is divisible by \(3^q\) in \(\mathbb Z_3\). The true incoming exponent is \(E_j\). Therefore the residue and incoming tests together have iid probability
\[
 3^{-q}\!\sum_{|w|=q,\,-1\in A_w,\ e_1(w)\ne1}3^q2^{-S_w}
       =3^{-q}\,\tfrac14\rho_q(-4)\le C3^{-q}.                        \tag{5}
\]
Words here are read outward, so the first letter is the last actual incoming gap. The equality follows by replacing the legal first letter \(e\ge3\) at \(-1\) by \(e-2\) at \(-4\), preserving every ensuing inverse state and giving the factor \(1/4\). Paper 200/v2 Corollary 4.4 gives the uniform bound. It includes arbitrary later gaps and does not condition the earlier source anew.

Average \(\log X\) uniformly over \([\xi_1\log H,\xi_2\log H]\), of length comparable to \(N\). For given \(v\) and gaps the allowed interval for \(\log X\) has length at most \(\log3+2\delta_M=O(1)\). Thus for each \(q\le j\le K\) its contribution is at most \(O(1/N)\) times (5), without assuming independence of \(V_j\) and the residue. Summing these \(O(N)\) possible times costs \(O(3^{-q})\). At the early times \(j<q\), a visit requires \(V_j\ge c_4 N-O(1)\) for a fixed \(c_4>0\) as \(\xi_1>1\). A fixed positive exponential moment of one increment bounds the union by \(O(q\exp[-c_5N+C_5q])\), uniformly for our \(q\); multiplying by \(K+1\) is harmless. Choose \(c_3\) so small that (4) is \(O(3^{-q})\) throughout the asserted range. All remaining errors are smaller still, proving (3).

## Many terminating examples in every octave

Choose a sufficiently small absolute \(\alpha>0\), and let \(k=\lfloor\alpha(\log\log Y)^2\rfloor\). Take \(s=\lfloor c_1(\log\log Y)^2\rfloor\ge1\), with \(c_1>0\) sufficiently small compared to \(\alpha\), so that \(s\log2\le k\log(3/2)/2\) and \(k+s+1\) is in the range of (3) at heights \((3/2)^i Y\), \(i\le s\). Prescribe
\[
       x=x_0=2^{s+1}3^{k+1}u-1\in[Y,2Y),\qquad
       x_i=2^{s+1-i}3^{k+1+i}u-1,\quad 0\le i\le s.
\]
The \(u\)'s form a proportional positive interval of \(J\asymp Y/(2^s3^k)\) integers. Every \(x_i\) is an odd unit. For \(i<s\), \(3x_i+1\) has valuation one and \(U(x_i)=x_{i+1}\); these values are strictly increasing. Also \(x\) has the unit ancestor \(v=(2/3)^k(x+1)-1\), rising to \(x\) by \(k\) exponent-one steps. The density floor gives
\[
                   d(x)\ge d(v)\gg(3/2)^k/Y.                         \tag{6}
\]

A positive fraction, tending to \(d(b)\), of the candidate \(u\)'s give \(x\) reaching \(b\). Indeed \(x_s=3^{k+s+1}(2u)-1\). The actual affine same-clock coupling from PR146 compares the first-hit indicator at the pair \(2u,x_s\) with mismatch proportion \(O((1+k+s)/\sqrt{\log J}+J^{-1/2})=o(1)\). To verify progression uniformity, use deadline \(h=\lfloor\frac12\log_2J\rfloor\) and the residuewise symbolic absorption event at starts \(2u\). Each tested residue mod \(2^h\) has relative frequency at most \(2^{1-h}+1/J\); the normalized failure fraction from theorem (1) with scale \(3^{k+s+1}\) and shift \(-1\) is \(O((1+k+s)/\sqrt h)\). At either end an early visit to fixed \(b\) costs at most \(O(2^h/J)\) by indegree two and injectivity in \(u\). All starts here exceed \(b\), so \(2u\) has the same first-hit indicator as \(u\); its mean tends to \(d(b)>0\) on this proportional interval. Also every prescribed ascent lies above \(b\), so the indicators at \(x\) and \(x_s\) agree. [PR146, actual affine merger estimate (1) and its residuewise event, pin 0410811](https://github.com/GettysburgResearch/collatz/blob/0410811710af2f7da71522ec67233528048adb9a/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md)

For \(1\le i\le s\), put \(M_i=(3/2)^iY\). Then \(x_i\in I_{M_i}\) for large \(Y\), and \(x_i\equiv-1\pmod{3^{k+i}}\). Omit any candidate \(u\) for which some \(x_i\notin G_{M_i}\). Each affine map \(u\mapsto x_i\) is injective. By (2), the total number omitted is \(O(s\max_i M_i^{1-1/64}\log M_i)=Y^{1-1/64+o(1)}=o(J)\). This is only a count of omitted sites. Their uncapped basin mass is never estimated. On each remaining candidate \(x_s\) is a nonperiodic good site and hence all its ancestors are nonperiodic. By injectivity at each \(i\), positivity, (3), and telescoping,
\[
 \sum_{u\ {\rm retained}}\big[d(x_s)-d(x_0)\big]
    \le \sum_{i=1}^s\sum_{a\in G_{M_i},\ a\equiv-1\ (3^{k+i})}
                         \Delta(a)
    \ll\sum_{i=1}^s3^{-k-i}\ll3^{-k}.
\]
There are at least \(d(b)J/2\) retained candidates reaching \(b\) for large \(Y\). A positive fraction of all candidates therefore both reach \(b\) and have \(d(x_s)-d(x)\ll_b2^s/Y\), by Markov's inequality on the last sum. Dividing by (6) gives \(O_b(2^s(2/3)^k)\), which is the stated stretched exponential. For \(x\equiv-1\pmod3\), the parent \(4x+1\) of \(U(x)\) is a multiple of three and \(16x+5\) is a distinct odd unit parent. Its full predecessor basin is disjoint from the one at \(x\), by nonperiodicity of \(U(x)\). Hence its density is bounded by \(d(Ux)-d(x)\), as claimed.

The argument uses a thin prescribed progression and discards a negligible fraction of its sites. A fixed escaping ray can instead lie entirely in the excluded forward orbits of small starts. In particular the construction does not decide a lower bound restricted to sites already carrying a fixed positive amount of precursor mass along a supplied infinite ray.
