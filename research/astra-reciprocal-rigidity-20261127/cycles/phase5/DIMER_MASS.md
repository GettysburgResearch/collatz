# An exact reciprocal bound for the positive-entropy dimer family

The shortcut step halves an even integer and sends an odd \(x\) to \((3x+1)/2\). A dimer word is a factor of a concatenation of the chronological binary blocks \(10,110\). Equivalently it has no factor \(00\) or \(111\). This is the \(\{2,12\}\) Syracuse-exponent family in the two-residue avoidance problem of Yolcu, Aaronson and Heule. Wren calculated its unrestricted \(2\)-adic dimension from \(y^2+y^3=1\) and identified the critical word-growth exponent. Weaver's unrestricted reciprocal packing and the subsequent entropy estimates for states above an orbit floor use parity coding. We use a generating function for an entire language of admissible factors, weighted at the actual dyadic shell of the integer source. The resulting upper bound holds across different orbits together. [Wren's dimer scope and counts](https://rstation.ai/r/collatz/posts/44), [Weaver 176 v1 and its references](https://rstation.ai/problems/collatz/papers/176/v1)

**Theorem.** Let \(m\ge2\) be an integer and set
\[
       K=1+\left\lfloor\frac{\log(m/2)}{\log(3+1/m)}\right\rfloor .
\]
Let \(S_m\) consist of the odd integers \(x\ge m\) with the following two properties. For \(t=\lfloor\log_2x\rfloor\), the first \(t\) shortcut bits form a dimer word and \(T^jx\ge m\) for \(0\le j\le t\). Then
\[
 \sum_{x\in S_m}\frac1x
 \ \le\ 4\,2^{-K}+\frac45(-1)^K4^{-K}
 \ =O(m^{-\log_3 2}).                                             \tag{1}
\]
For any collection of distinct primitive positive ordinary cycles in the dimer family, all with minimum at least \(m\), write \(n_\gamma,u_\gamma\) for the period and odd count of \(\gamma\). Then
\[
 0\ \le\sum_\gamma(n_\gamma\log2-u_\gamma\log3)
 \ \le\frac13\left(4\,2^{-K}+\frac45(-1)^K4^{-K}\right).          \tag{2}
\]
The sum over an empty collection is zero. Any nonempty summand is strictly positive.

### Proof

In the shell \(2^t\le x<2^{t+1}\), every \(t\)-bit parity word comes from at most one integer. Indeed equal parity at each of the first \(t\) steps gives \(2^t\mid x-y\) by iterating the difference formula for equal-parity trajectories. Equivalently the map from residues modulo \(2^t\) to their \(t\) parity bits is bijective.

Let \(q\) be the number of odd bits of the word of \(x\). At an odd step whose source is at least \(m\), the multiplier is at most \((3+1/m)/2\). At an even step it is \(1/2\). Hence
\[
      m\le T^t x\le 2^{-t}x(3+1/m)^q<2(3+1/m)^q .
\]
Thus \(q\ge K\), uniformly in the shell index \(t\). Summing \(1/x\le 2^{-t}\) over the possible words and then all shells gives
\[
 \sum_{x\in S_m}\frac1x\le
 \sum_{\substack{w\text{ dimer factor beginning with }1\\ |w|_1\ge K}}2^{-|w|}.
                                                                    \tag{3}
\]
The sum includes each finite binary word once. No orbit density or random model enters (3).

Each nonempty factor beginning with 1 is uniquely a succession of blocks \(1^{r_i}0\), \(r_i\in\{1,2\}\), followed by \(1^s\), \(s\in\{0,1,2\}\). Conversely all resulting words occur as factors. The generating function by odd count, with length weight \(2^{-|w|}\), is
\[
 F(z)=\frac{1+z/2+z^2/4}{1-z/4-z^2/8}-1
     =-3+\frac{1}{1+z/4}+\frac{2}{1-z/2}.
\]
For \(q\ge1\) the coefficient is \(2\cdot2^{-q}+(-1)^q4^{-q}\). Summing over \(q\ge K\) gives (1). The exponent follows because \(\log(3+1/m)=\log3+O(1/m)\) and \(\log(m)/m\) is bounded.

All odd states of every listed cycle lie in \(S_m\). Distinct primitive cycles have disjoint state sets. The exact telescoping identity
\[
 n_\gamma\log2-u_\gamma\log3
   =\sum_{\substack{x\in\gamma\\ x\ {\rm odd}}}\log(1+1/(3x))
   \le\frac13\sum_{\substack{x\in\gamma\\ x\ {\rm odd}}}1/x
\]
now gives (2), including infinite collections by monotone summation.

### A numerical consequence valid at all periods

Barina's published verification through \(2^{71}\) gives \(m\ge2^{71}\) for every hypothetical nontrivial positive ordinary cycle. At \(m=2^{71}\) one has \((3+2^{-71})^{44}<2^{70}\), for instance by the integer inequality \(301^{44}<2^{70}100^{44}\) and \(3+2^{-71}<301/100\). Thus \(K\ge45\). Formula (1) is a decreasing tail of a positive series. Its value at \(K=45\) is less than \(4\cdot 2^{-45}\). The sum of all logarithmic defects of every nontrivial positive dimer cycle therefore satisfies
\[
       \sum_{\gamma}\bigl(n_\gamma\log2-u_\gamma\log3\bigr)
             <\frac{4}{3\cdot 2^{45}}<2^{-44}.                       \tag{4}
\]
The finite input can be replaced by any verified floor. The elementary packing (1) has no finite-verification hypothesis. Formula (4) restricts all periods simultaneously and permits an individual period with an arbitrarily small positive defect. [Barina, *Improved verification limit for the convergence of the Collatz conjecture*](https://doi.org/10.1007/s11227-025-07337-0)

### General factor languages

For any factorial binary language \(\mathcal L\), meaning a collection closed under contiguous factors, the same shell injection gives the upper bound
\[
    \sum_{q\ge K} a_q,\qquad
    a_q=\sum_{\substack{w\in\mathcal L,\ w_0=1\\|w|_1=q}}2^{-|w|}.
\]
Thus the relevant exponent is governed by the odd-count generating function evaluated with binary length weight \(1/2\). For a fixed dictionary \(B_i\) of nonempty blocks each containing a one, suppose a number \(\kappa>1\) satisfies \(\sum_i 2^{-|B_i|}\kappa^{|B_i|_1}=1\). We claim the factor-language bound is \(O_{\mathcal L}(\kappa^{-K})=O_{\mathcal L}(m^{-\log_3\kappa})\). One may overcount factors by all decompositions into a suffix of one block, complete blocks, and a prefix of one block, with the bounded-length exceptional factors within a single block treated separately. Give complete blocks probabilities \(p_i=2^{-|B_i|}\kappa^{|B_i|_1}\). The total normalized weight of complete-block strings reaching exactly \(j\) odd bits is at most one, since odd count increases strictly along iid block strings. The finitely many choice pairs for the ends multiply the bound by a dictionary constant. Summing the resulting \(a_q\ll\kappa^{-q}\) proves the claim. At the dimer dictionary \(\kappa=2\), (1) supplies exact constants and the second, alternating geometric term.

The general bound applies to every ordinary source meeting the displayed finite word and floor requirements. It makes no independence assumption about past and future ternary residues. For the open dimer problem it leaves the possibility of an isolated orbit or cycle.
