# A sufficient family of semiprimes whose factors are easy to find

**PROPOSED, SOURCE-QUALIFIED written theorem.** This is a reduction of universal Collatz convergence to an explicit sparse family. It does not prove convergence on that family. The proof uses the stated uniform pair-fusion theorem and positive-predecessor theorem as external Collatz inputs. Its number-theoretic input is unconditional; no Riemann hypothesis is assumed.

Throughout, use the shortcut map
\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
\qquad n\in\mathbb N_{>0},
\]
and natural logarithms. Define the fixed set
\[
\mathcal S=\{pq:p<q\text{ are primes},\quad \log(pq)<p\le(\log(pq))^2\}.
\tag{S}
\]
All sufficiently large members are odd and squarefree. Their smaller factor can be found by trial division through \((\log n)^2\), in a number of bit operations polynomial in the bit length of \(n\).

## Claims

There are absolute constants \(c,C>0\) and a function \(r(X)\to0\) with the following property. For **every** union \(A\) of ordinary forward components, even one chosen separately at each scale,
\[
\#(A\cap\mathcal S\cap(X,2X])
\ge {c\over\log X}\#(A\cap(X,2X])
       -r(X){X\over\log X}.
\tag{1}
\]
The constants and error are uniform in \(A\). The same conclusion holds for the set of predecessors of a specified target \(v\le X^{1/2}\), uniformly in that target, and for its visit indicator before any common shortcut deadline \(L\ge\lfloor\tfrac14\log_2X\rfloor\).

Consequently, with Mazur's positive-predecessor theorem as stated below:

1. Every fixed target \(v\) prime to three has at least \(c_vX/\log X\) predecessors in \(\mathcal S\cap[1,X]\), for all sufficiently large \(X\), where \(c_v>0\).
2. If any positive source fails to reach 1, at least \(c_*X/\log X\) members of \(\mathcal S\cap[1,X]\) fail to reach 1, for all sufficiently large \(X\), for some \(c_*>0\).
3. Universal convergence is equivalent to convergence of every member of \(\mathcal S\). It is also equivalent to an **upper relative natural density of one** for convergence within \(\mathcal S\).

The last assertion uses \(\#(\mathcal S\cap[1,X])\le CX/\log X\). In fact the prime number theorem gives \(\#(\mathcal S\cap[1,X])\sim(\log2)X/\log X\), but that asymptotic is unnecessary for the reduction.

## Exact external inputs

**Short-interval supply.** Matomäki and Teräväinen, Theorem 1.1 of *Almost primes in almost all short intervals II*, arXiv:2207.05038v2 (2023), give constants \(c_0,\delta>0\): outside \(O(X/(\log X)^\delta)\) integer exceptions through \(X\), the interval \((x,x+(\log x)^{2.1}]\) contains at least \(c_0(\log x)^{1.1}\) products \(p_1p_2\) with \((\log x)^{1.09}<p_1\le(\log x)^{1.1}\). These products lie in (S) for all sufficiently large \(x\). This is a lower bound, not an assertion of asymptotic equidistribution in every short interval. [Original paper, Theorem 1.1](https://arxiv.org/pdf/2207.05038v2) · [Journal version](https://doi.org/10.1090/tran/8869).

**Uniform, actual pair fusion.** Leen's exact binary-cylinder lemma, balanced-shortcut dictionary and uniform pair-absorption theorem give an absolute \(B\): for every integer \(j\) and \(t\ge1\), at most
\[
B2^t\sqrt{{1+\log(1+|j|)\over t}}
\tag{2}
\]
residues modulo \(2^t\) fail to guarantee \(T^t n=T^t(n+j)\) for **every ordinary lift** of that residue. The extra equal-odd-count condition in the cited theorem is precisely what makes the cylinder valid for all lifts. We use its upper bound, not a uniform asymptotic. [Leen, original source, labels `pair:cylinders`, `pair:dictionary`, `pair:uniform-tail`](https://doi.org/10.5281/zenodo.23268751).

**Positive predecessors.** Mazur's theorem gives positive lower natural density for ordinary-map predecessors of each fixed positive target not divisible by three. For a shortcut target \(v\), apply it to the ordinary target \(2v\): the subsequent halving guarantees a shortcut visit to \(v\), even when \(2v\) itself was skipped by a shortcut. Its corollary gives positive lower density of nonconvergence if there is any counterexample; ordinary and shortcut convergence coincide. No density-one convergence premise is supplied by this input. [Original Theorem 1.1 and Corollary 1.2](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf).

We also use the classical Brun–Titchmarsh inequality and the bounded reciprocal prime sum between \(\log X\) and \((\log(3X))^2\). Only an absolute-constant upper bound is needed. [Montgomery–Vaughan, *The large sieve*, Mathematika 20 (1973), 119–134](https://doi.org/10.1112/S0025579300004708).

## Weighted failures: the essential arithmetic step

Set
\[
t=\lfloor\tfrac14\log_2X\rfloor,\quad Q=2^t,
\quad H=\lceil(\log(2X))^{2.1}\rceil.
\]
For every odd residue \(a\bmod Q\),
\[
\#\{m\in\mathcal S\cap(X,3X]:m\equiv a\pmod Q\}
        \le C{X\over Q\log X}.
\tag{3}
\]
Indeed, write \(m=pq\) with the smaller factor \(p\). Its permitted range is contained in
\(\log X<p\le(\log(3X))^2\), whose reciprocal prime sum is bounded by an absolute constant. Each \(p\) is odd and invertible modulo \(Q\). The other prime must satisfy \(q\equiv ap^{-1}\pmod Q\) and \(q\le3X/p\). Brun–Titchmarsh bounds its count by
\[
{2(3X/p)\over\varphi(Q)\log(3X/(pQ))}
      \le C{X\over pQ\log X},
\]
since \(Q\le X^{1/4}\), \(p\ll(\log X)^2\), and \(\varphi(Q)=Q/2\). Summing proves (3). Even residues contain no sufficiently large elements of \(\mathcal S\).

For each \(1\le j\le H\), let \(E_j\) be the failing residue set in (2). Translating the residue class from \(n\) to \(m=n+j\), (3) gives
\[
\#\{X<n\le2X:n+j\in\mathcal S,\ n\bmod Q\in E_j\}
 \le C{X\over\log X}
       \sqrt{{1+\log(1+H)\over t}}.
\tag{4}
\]
Thus the failure cost is small **relative to the sparse semiprime population**. Using the unweighted estimate \(O(X/\sqrt{\log X})\) here would fail. No independence between primality and fusion is assumed: the bound is valid separately in each failing binary residue.

## Double counting the windows

Write \(I=(X,2X]\cap\mathbb N\). The short-interval theorem, applied through \(2X\), and the definition of \(H\) show that for all but \(O(X/(\log X)^\delta)\) sources \(n\in I\),
\[
\sum_{j=1}^{H}\mathbf1_{\mathcal S}(n+j)
       \ge c_1 H/\log X
\tag{5}
\]
for an absolute \(c_1>0\). The small change from \(\log n\) to \(\log X\) is uniform on this octave.

Sum (5) over \(n\in A\cap I\). The result is at least
\[
{c_1H\over\log X}
  \left[\#(A\cap I)-O\bigl(X/(\log X)^\delta\bigr)\right].
\tag{6}
\]
On every pair outside the failing residues, an actual merger occurs by time \(t\), so \(n\in A\) forces \(n+j\in A\). Summing (4) over \(j\) bounds the discarded incidences by
\[
C{HX\over\log X}\sqrt{{1+\log(1+H)\over t}}.
\]
Each retained target \(m\) has at most \(H\) source incidences. Dividing (6) by \(H\) therefore gives (1), after trimming the at most \(H\) targets beyond \(2X\). For example one may take
\[
r(X)=O\!\left((\log X)^{-\delta}
       +\sqrt{{\log\log X\over\log X}}
       +{H\log X\over X}\right).
\tag{7}
\]
All bounds are independent of \(A\), proving the stated uniformity.

For a visit to \(v\le X^{1/2}\), neither source can visit \(v\) before fusion: at every date \(i\le t\), the actual value is at least \(X/2^t\ge X^{3/4}>v\). The two future paths then agree. This proves the predecessor and common-deadline variants as well. A finite deadline requires \(L\ge t\); an earlier deadline is outside this proof.

## Passing from an octave to a fixed exceptional source

Suppose a set \(A\) of one of the preceding types has lower natural density \(d>0\). Choose a fixed integer \(K\) with \(2^{-K}<d/4\). For all sufficiently large \(X\),
\[
\#(A\cap(X/2^K,X])\ge(d/2-2^{-K})X\ge dX/4.
\]
Apply (1) to the \(K\) disjoint dyadic octaves filling this interval. Because \(K\) is fixed, the combined error is \(o(X/\log X)\); each denominator is at most \(\log X\). It follows that
\[
\#(A\cap\mathcal S\cap[1,X])\ge c_dX/\log X
\tag{8}
\]
eventually, for some \(c_d>0\). Positive lower density alone need not give positive mass in every individual octave, which is why this step is included.

The same elementary prime upper bound used in (3), with modulus one, gives \(\#(\mathcal S\cap[1,X])\ll X/\log X\), after dyadic summation and a negligible initial range. Hence (8) is a positive lower **relative** density within \(\mathcal S\).

Apply this first to the predecessors of a fixed eligible target, and then to the invariant set of nonconvergent starts. Alternatively, a counterexample orbit contains an integer prime to three: divide off its powers of two, and if its odd state is divisible by three, its next shortcut state is 2 modulo 3. All predecessors of that target are counterexamples. Mazur's theorem supplies the positive-density premise in either formulation. This proves the three claims.

## Relation to the requested proof routes

The family (S) is much smaller than all semiprimes, whose counting function has an additional \(\log\log X\) factor. The result does **not** assert that an arbitrary density-one subset of all semiprimes is sufficient. It identifies a particular family and proves the required relative transfer there.

Paper 233, *Prime factors of Collatz predecessors*, uses ordinary RH to sample primes at a variable multiplier and derive independence of marks on ordered partial products. The present argument does not establish that prime-sampling or product-independence theorem without RH. It uses an unconditional semiprime minorant to obtain a one-sided, uniformly positive transfer, which suffices for the universal reduction above. [Paper 233, sections 3–4](https://rstation.ai/problems/collatz/papers/233).

This addresses a necessary bridge for the factoring project: proving convergence throughout (S) would settle Collatz. However, factor recovery is already polynomial-time on (S). The missing statement is dynamical, such as a terminating descent or a genuine merger certificate for every such product. Factoring a product, or obtaining a dense family of easily factored products by arbitrary residue permutations, does not prove that statement.

The median statistic remains
\(\tfrac14\sum_C d_C^2/P_C\). This reduction would force its value to \(1/8\) if convergence on (S), or relative upper density one there, were proved. Neither is inferred from the short-interval supply theorem.
