# Which ordinary targets can repay a prescribed inverse route?

**PROPOSED written theorems.** The visible-prefix theorem below allows the routing depth, binary clock, intermediate heights and path to depend on the target. It gives a natural-density bound for ordinary targets after taking the union over *all* routing depths. It also gives an exact obstruction to spending the currently available ternary digits to descend from a critical arm. No pointwise resolution of Collatz is obtained.

Write \(T(n)=n/2\) on even positive integers and \(T(n)=(3n+1)/2\) on odds. On odd integers \(U(x)=(3x+1)/2^{v_2(3x+1)}\). An odd word \(a=(a_1,\ldots,a_d)\) lists positive halving exponents in **forward** order, has length \(d\), and total \(|a|=\sum a_i\). A genuine ordinary realization takes \(|a|\) shortcut steps. All densities of odd targets below are relative to positive odd integers.

## A sharp finite floor obstruction on the actual three-step arms

Let \(m\) precede \(z\) by any \(d\) odd steps. Each edge \(3u+1=2^e v\) gives \(3(u+1)\ge2(v+1)\). Thus
\[
  3^d(m+1)\ge 2^d(z+1).
\]
When \(z\equiv-1\pmod{3^d}\), the inverse word consisting of \(d\) ones is legal at every step and realizes equality, including the exact additive terms. Its output is positive and odd since \(z+1\) is an even positive multiple of \(3^d\). Consequently it minimizes the source among **all** inverse words of this odd length. To remain a ternary unit at the very last source one may need a further prescribed ternary digit.

Take any of the ordinary critical arms from PR193 at the base head of this packet. They satisfy \(|2^{-r}z-x|<13\), where \(x\) is the actual class minimum and \(r=e+2\cdot3^{b+2}+5\). For every \(x\ge52\), every arm and every \(1\le d\le b\), **every** \(d\)-step inverse predecessor \(m\) of \(z\) satisfies \(m\ge x\). Indeed \(z\ge2^d(x-13)\) and
\[
  2^d(z+1)>4^d(x-13)\ge3^d x.
\]
The last inequality follows from \(4(x-13)\ge3x\) and \(4^{d-1}\ge3^{d-1}\). No routing, residue or clock selection within that inverse depth can lower the chosen arm below even its moving minimum. Since \(x\) lies above the least nonconvergent floor, this also rules out repayment to that floor by these steps.

There is an absolute restriction if the final reverse operation uses only ones. Suppose it starts at \(y\) and pays down to \(0<m<F\). The equality above gives \(2^d\mid m+1\), hence \(2^d\le F\). It also gives
\[
   y+1=(3/2)^d(m+1)\le F^{\log_2 3}.
\]
In particular increasing precision at ever later phases cannot make this last operation alone return to a *fixed* original floor. A preceding route from arbitrarily large marks must first get inside this specific ordinary interval. For a mixed word the uniform arbitrary-length substitute below concerns density, not every target. [Critical theorem at the base](../../astra-heavy-machinery-20261124/ergodic/critical.md)

### Arbitrarily late mergers with a bounded competing source

The actual critical construction starts at a future-tail record \(i\), with \(m_i\) the unrestricted minimum of its synchronous class and \(m_i\le m_k\) for every \(k\ge i\). The produced mark \(z\) belongs to \(C_{i+s}\) for some \(s\ge0\). Thus **every** future odd image \(U^j(z)\) is at least \(m_i\), for all \(j\) with no bound. If a positive odd source \(v<F\) meets any such image after \(h\) odd steps, the exact inverse inequality gives
\[
       (3/2)^h F\ge m_i+1 .
\]
The competing arm alone has to pay this clock; waiting on the marked arm does not decrease it.

There is a stronger restriction on the number \(R\) of maximal constant-parity runs of the *shortcut itinerary on the competing arm*. For arbitrary positive integer paths from \(v<F\) to \(Y\), as \(Q=\log(Y+6)/\log(F+6)\to\infty\),
\[
               R/\log Q\longrightarrow\infty .
\]
In particular one may substitute \(m_i\) for \(Y\) in this necessary condition for the merger. This consequence of PR192 applies to any clock and changing floors. On a hypothetical escape it applies also to its original bounded seed whenever that seed reaches the common main-orbit continuation, so the comparison has actual instances under the hypothesis.

For the proof, fix an arbitrary integer \(m\ge1\) and group runs in batches of at most \(m\). PR192's fixed-window estimate (2) applies to each batch from its current integer \(u\), because a monochromatic nonempty positive window has center 0 or \(-1\) and never fixes its positive entry. It bounds its shortcut length by \(L\le 2\log_2(u+6)+C_m\) (choose \(\epsilon=1\)). Each step increases \(u+6\) by a factor at most \(3/2\). For \(Z=\log_2(u+6)\) the next boundary therefore satisfies \(Z'\le BZ+c_m\), where \(B=1+2\log_2(3/2)\) is independent of \(m\). Iterating over at most \(\lceil R/m\rceil\) batches yields \(Q\le C'_m B^{\lceil R/m\rceil}\), uniformly in \(F,Y\), since \(\log_2(F+6)\ge1\). Hence \(\liminf R/\log Q\ge m/\log B\) for each fixed \(m\). Let \(m\) increase only after this limit. This is the noncyclic application of PR192's grouping argument; it does not require uniformity of its Evertse constant in dimension. No estimate forces a successful arm of smaller run complexity. [PR192, fixed-window estimate and grouping at d2081d1](https://github.com/GettysburgResearch/collatz/blob/d2081d1cd2410e6004eaee9f9b13c5553afaf3f4/research/astra-closure-attack-20261124/CYCLE_EXTENSION.md) · [Evertse, Corollary 1](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

## An all-depth ordinary visibility theorem

Fix a real \(K>0\) and a finite or countable family \(\mathcal W\) of finite positive odd words. Let \(V_K(\mathcal W)\) consist of odd targets \(q\) for which some positive odd \(z\le Kq\) follows a complete initial word \(a\in\mathcal W\) and subsequently hits \(q\) after any number of further odd steps, including zero. Every intervening source, carry and merger is ordinary. Repeated visits to cyclic targets are allowed.

**Theorem.** The natural density of \(V_K(\mathcal W)\) exists, and for an absolute finite constant \(C\),
\[
   \operatorname{dens}_{\rm odd} V_K(\mathcal W)
      \le C K\sum_{a\in\mathcal W}2^{-|a|}.
   \tag{1}
\]
Redundant extensions may be removed before applying the bound. For a prefix-free family the sum is its actual binary probability conditional on an odd source. Equality in (1) is not claimed.

In particular, after *any* preparatory inverse route from an ordinary target, steering to \(-1\bmod 3^b\) and then spending \(b\) inverse ones can produce a source \(z\le Kq\) on a set of upper relative density at most \(C K2^{-b}\). The statement includes free choice of the clock and depth of the preparatory route, as well as the affine-carry case where the real homogeneous slope equals \(K\). It is stronger than a count at prescribed routing length and total.

**1. A tail bound for actual visitors.** For a finite integer interval \(I\), the union \(D\) of the complete forward orbits of \(N\) positive seeds has
\[
  |D\cap I|\le |T^l(I)|+Nl,\qquad l\ge1.
  \tag{2}
\]
Add the orbits one at a time. Each new piece is an injective infinite path, an injective finite path entering the old set, or a finite tail followed by a disjoint cycle. On a finite path or tail omit its last \(l\) states (all of them if shorter). The \(l\)-step images of the remaining states stay on that same piece and are distinct. The cycle points also map bijectively onto their cycle. Distinct pieces contribute disjoint images. This is the complete-orbit counting argument in Weaver's work, including the periodic case. [Weaver, paper 178 v1, §5](https://rstation.ai/problems/collatz/papers/178/v1)

Uniformly for each fixed integer \(j\ge1\), there are absolute \(C_0,c>0\) with
\[
 \limsup_{X\to\infty}X^{-1}|T^j([1,X]\cap\mathbb Z)|\le C_0 e^{-cj}.
 \tag{3}
\]
Indeed fix \(1/2<t<\log_3 2\). Binary parity words of length \(j\) biject the residues modulo \(2^j\). The number of sources with more than \(tj\) odd steps has limiting proportion at most \(e^{-c_1j}\) by the binomial bound. All other outputs are at most \(X(3^t/2)^j+(3/2)^j\), by the affine word formula. The last term is fixed when taking the indicated limit. This needs no mixing theorem.

Any \(q\le X\) reached by any \(z\le Kq\) after at least \(J\) shortcut steps belongs to an orbit from \(T^J([1,KX])\). Apply (2) with \(I=[1,X]\) and \(l=J\), followed by (3) on both source and target intervals. The resulting upper density amongst **all** positive targets is at most
\[
 C_0 (1+KJ)e^{-cJ}.
 \tag{4}
\]
For relative odd density multiply by two. This controls all larger clocks simultaneously, permits arbitrary path-dependent prefixes, and supplies the order of the two limits used next.

**2. The exact ternary law.** For each complete finite word \(w\) of \(n\) positive gaps and total \(S\), its reverse branch at \(q\) has the affine expression
\[
       z=\lambda_w q-c_w,\qquad \lambda_w=2^S/3^n,
       \quad c_w\ge0 .
\]
The empty word has \(c_w=0\). There is exactly one legality class modulo \(3^n\), by the full denominator \(3^n\) in the inverse equation and invertibility of \(2^S\). Composite integrality gives integrality at every intermediate step by reducing at successive powers of three. Each integral reverse step from a positive odd state gives a positive odd state, so every large odd target in that class realizes the word. For any fixed word and all sufficiently large targets, \(z\le Kq\) holds precisely when \(\lambda_w\le K\). If \(\lambda_w>K\) the fixed affine offset eventually loses, and when \(\lambda_w=K\) the offset is nonnegative.

Let \(H_K(\mathcal W)\) be the union in \(\mathbb Z_3\) of those legality cylinders with \(\lambda_w\le K\) and \(w\) starting in \(\mathcal W\). At a fixed shortcut deadline \(J\) this is a finite union and its normalized Haar measure equals the relative odd natural density of its physical counterpart, since removing finitely many small targets does not affect natural density. As \(J\to\infty\) the finite unions increase to \(H_K\). By (4) the corresponding ordinary error goes to zero. Thus the literal, untruncated physical density exists and equals \(\pi(H_K(\mathcal W))\). No identification of a particular ordinary target with a Haar-typical point has been used.

**3. Renewal of the homogeneous cost.** Fix one prescribed initial word \(a\) of length \(d\) and total \(G\). For each following free word \(v\) of length \(h\) and total \(s\), the combined legality cylinder has measure \(3^{-d-h}\). The terminal ternary-unit restriction is unnecessary for this upper bound. The homogeneous slope condition is \(2^s/3^h\le D:=K3^d/2^G\).

Let \(E_i\) be independent with \(\mathbb P(E_i=e)=2^{-e}\) for \(e\ge1\), and \(W_h=\sum_{i=1}^h(E_i\log 2-\log 3)\), \(W_0=0\). The cylinder union bound for this one initial word is at most
\[
  3^{-d}\sum_{h\ge0}\mathbb E\!
        \left[e^{W_h}\mathbf1_{W_h\le \log D}\right].
 \tag{5}
\]
Indeed the chosen free word has probability \(2^{-s}\) and \(2^{-s}e^{W_h}=3^{-h}\). There is an absolute \(A\) such that the expected number of visits by this walk to any interval of length one is at most \(A\). To see this, start the walk at its first entry into the interval. At lag \(n\ge1\) another visit requires the independent increment to be at most one. For \(r=\mathbb E e^{-W_1/2}=\sqrt3/(2\sqrt2-1)<1\) its probability is at most \(e^{1/2}r^n\). Thus \(A=1+e^{1/2}r/(1-r)\) suffices, including the first visit. Decompose \(( -\infty,\log D]\) into the unit strips ending at \(\log D-j\). Equation (5) is bounded by
\[
  3^{-d} A D\sum_{j\ge0}e^{-j}
    =\frac{A}{1-e^{-1}}K2^{-G}.
\]
Sum over \(a\) in the prefix family to obtain (1). The probabilities in this computation count algebraic words. Their use for ordinary targets was established by the independent deadline argument.

**Adaptive codes and a fixed component.** Suppose the proof chooses *any* of the length-\(b\) odd words with total at most \(\gamma b\), with fixed \(1<\gamma<2\). Their combined binary mass is \(\mathbb P(\sum_{i\le b} E_i\le\gamma b)\le e^{-c_\gamma b}\) by the exponential Markov inequality. This includes every homogeneous unexpanded inverse repayment word of length \(b\), taking \(\gamma=\log_2 3\). Allowing every length \(h\ge b\) subject to the same bound still gives \(O_\gamma(e^{-c_\gamma b})\) by summing over \(h\). Endpoints choose the code and all remaining clocks themselves. The estimate forces failure at a positive density of ordinary targets even with this freedom.

If a fixed set \(A\) of odd targets has lower relative density \(\delta>0\), then \(A\setminus V_K(\mathcal W)\) has lower relative density at least \(\delta-CK\sum 2^{-|a|}\). In particular it applies to the odd ancestor population of *one specified* positive unit target under the external fixed-target positive-density input M used in PR199. Positive lower density of all shortcut ancestors gives positive lower density of their odd parts by discarding large powers of two, since stripping all initial twos from an ancestor of an odd target still leaves an ancestor of that target. Thus a cheap prefix family can fail on many actual ancestors even in a fixed component. Conversely, a fixed divergent forward ray could itself lie in every exceptional set (4) beyond finitely many steps, because its original source eventually lies below its targets. No positive density of forward states on that ray follows from positive density of its predecessors. [PR199, input M](https://github.com/GettysburgResearch/collatz/blob/d868f8e8405c08b8c501236853bea495ca593824/research/optimal-critical-ancestors-20261124/README.md)

## A competing arm of unlimited depth and a moving meeting point

Give the original odd target \(q\) up to \(J\) shortcut steps of its own, choose any odd meeting point \(y\) along that portion of its orbit, and let a positive odd \(z\le Kq\) follow a word of \(\mathcal W\) and meet \(y\) after arbitrarily many more odd steps. The successful original starts have relative upper density at most
\[
        C K\,2^J\sum_{a\in\mathcal W}2^{-|a|}. \tag{6}
\]
The arrival clocks can differ. Indeed, for one fixed original gap word \(f\) through \(y\), write \(y=\lambda q+c\), where \(\lambda=3^{\ell(f)}/2^{|f|}>0\) and \(c\ge0\). The map from these starts to \(y\) is injective. Each qualifying meeting endpoint is in \(V_{K/\lambda}(\mathcal W)\) and is at most \(\lambda X+c\) for \(q\le X\). Equation (1) bounds the asymptotic number of such odd endpoints by \((\lambda X/2) C(K/\lambda)\sum_a2^{-|a|}+o_f(X)\). The two scale factors cancel. The empty original word and the positive compositions of every integer through \(J\) give exactly \(2^J\) possible original words. At fixed \(J\) their error sum is still \(o(X)\), proving (6).

For \(b\) required ones on the competing arm, (6) gives \(CK2^{J-b}\). Paying \(b\) ternary digits in this fashion therefore requires at least \(b-O_K(1)\) shortcut clocks on the original side for any proposed all-target guarantee, even granting unrestricted further time on the competing side. Every deadline \(J\le(1-\varepsilon)b\) permits success only at an exponentially small fraction of odd starts. One may instead give the original side \(\lfloor(1/2-\varepsilon)b\rfloor\) *odd* steps for fixed \(0<\varepsilon<1/2\): except on a set of relative density \(O_\varepsilon(e^{-c_\varepsilon b})\), their actual shortcut total is at most \(\lfloor(1-\varepsilon)b\rfloor\). This is the upper tail of the sum of independent geometric letters under binary parity coding, applied to the full starting population at each fixed \(b\). The positive-density component conclusion above also applies after these original-arm choices. The argument leaves open targeted comparisons on a particular scarce starting set and routes using more original time.

## A legal alternative and what it costs

A route with longer merging horizon does achieve new ordinary residue control. Assume the source-qualified fixed-total router of Weaver and Wren, Theorem 8: at modulus \(3^k\) there is a common \(h=O(k+1)\) such that every unit target routes by \(h\) inverse odd steps of total exactly \(2h\) to every unit residue. Fix an odd ternary unit \(x\), a positive gap prefix \(a\) of length \(p\), total \(G\) and carry \(C_a\), and a unit \(u\bmod 3^b\). Take the router for \(k=b+p\), and its actual target \(y=U^{p+h}(x)\). Require its output \(v\) to satisfy
\[
 v\equiv 2^{-G}(3^p u+C_a)\pmod{3^{b+p}}.
\]
This is a unit, since for \(p>0\) the final carry summand is a power of two; for \(p=0\) the requested class is \(u\). The reverse prefix then gives the ordinary \(z=(2^Gv-C_a)/3^p\equiv u\pmod{3^b}\). Its full path has exactly the requested initial gaps, ends at \(y\) and has total \(G+2h\), with common excess rank
\[
    r=G+2h-E_{p+h}(x)
\]
for all \(u\). In the late escaping-minimum class the native inequality \(E_{p+h}(x)\le4(p+h)\) gives \(|r-G|=O(b+p+1)\), while least corrected height gives \(r\ge0\). This replaces exponential precision overhead by linear overhead when the merger horizon may grow linearly. It gives a specific excess rank, as opposed to arbitrary prescribed ranks. The source-independent router operates near free-word mean two. Changing to every linearly contracting repayment prefix encounters (1), and a single late divergent target could lie in its exceptional population. A route from a chosen actual least source that overcomes this mismatch, or a different comparison covering its entire complement, remains missing. [Weaver and Wren, paper 48 v1, Theorem 8](https://rstation.ai/problems/collatz/papers/48/v1) · [Native clock optimality, §4](../../astra-global-synthesis-20261124/section/proof.md)

## Formal boundary

[Repayment.lean](Repayment.lean) checks the exact arbitrary-word inverse inequality, the pure-ones identity with its floor divisibility, the no-repayment implication on the critical arms, the exact source-ratio transport on the original side of a two-arm merger, and the fixed-clock factorization for all later physical hits. The natural-density theorem, complete-orbit counting, renewal estimate and source-qualified routing application are written proofs. The finite formalization imports only `Std`. It does not assume Collatz convergence or any of the external density results. The independent finite [control](check.py) compares 16 deadline, scale and prefix choices over whole ternary periods with direct forward iteration of all eligible positive odd starts. Both nontrivial cycles and escape remain open.
