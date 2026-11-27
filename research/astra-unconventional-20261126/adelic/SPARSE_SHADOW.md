# Joint real and profinite records under sparse ordinary corrections

**PROPOSED written countermodel theorem.** Fix any positive odd ordinary integer \(q_0\) and any specified nondecreasing \(B:[1,\infty)\to[1,\infty)\) with \(B(x)=o(\log x)\). There is a sequence of positive odd integers from that single source satisfying
\[
  2^{e_i}q_{i+1}=3q_i+d_i,\qquad e_i\ge1,\quad d_i\ge1,\qquad
  A_n=\sum_{i<n}e_i,\quad M_n=3^n2^{-A_n},\quad D_n=\log_2 M_n .
\]
The following conclusions hold simultaneously.

1. \(D_n\asymp n/\log n\), \(q_n/M_n\to L\in(0,\infty)\), and \(q_n\) is eventually injective. In particular \(A_n/n\to\alpha=\log_2 3\).
2. Among the first \(N\) odd edges, at most \(O((\log(2+N))^3)\) have \(d_i>1\). Their mutual spacings tend to infinity. For every \(\epsilon>0\), eventually \(d_i\le q_i^\epsilon\). For **every** fixed positive integer \(m\), eventually \(d_i\equiv1\bmod m\). In addition, eventually this agreement holds simultaneously for all \(1\le m\le B(q_i)\). The native exponent \(v_2(3q_i+1)\) is \(e_i\) at every sufficiently late edge, including the exceptional ones.
3. There is \(c>0\) such that, for every sufficiently large \(i\), the window of \(R_i=\lfloor c i/(\log i)^3\rfloor\) consecutive odd edges has exactly the gap word of the first \(R_i\) native steps from \(q_i\). At all \(0\le j\le R_i\), \(q_{i+j}\equiv U^j(q_i)\bmod m\) simultaneously for all \(1\le m\le B(q_i)\), where \(U(x)=(3x+1)/2^{v_2(3x+1)}\). The same conclusion holds for any fixed modulus. The logarithmic order of the modulus cutoff is sharp for subpower nonunit corrections, as shown below.
4. Write \(\mathbb T=\mathbb R/\mathbb Z\). The set of joint accumulation points of \((\log_2 q_n\bmod1,(q_n)_p)\), over the strict record times of \(M_n\), equals
\[
   \mathbb T\times\mathbb Z_2^\times\times K_{\rm crit}
                     \times\prod_{p\ne2,3}\mathbb Z_p . \tag{1}
\]
The same equality holds over the strict record times of the **ordinary integer heights** \(q_n\). Here
\[
 K_{\rm crit}=\left\{\sum_{j\ge1}3^{j-1}2^{-B_j}\ \text{in }\mathbb Z_3:
 b_j\ge1,\ B_j=\sum_{t=1}^j b_t<j\alpha\text{ for all }j\right\}.
\]
This compact set includes the explicit positive-dimensional compact family of transcendental coordinates from [round 13](../../astra-global-closure-20261124/round13/critical/TRANSCENDENTAL_FAMILY.md). The identification of that subfamily as transcendental uses the sources pinned there. The proof of (1) below is elementary.
5. No tail of this gap sequence is the actual trajectory of any rational \(2\)-adic integer, of either sign. In particular no choice of a positive ordinary initial value turns the full itinerary into a native escaping orbit.

The theorem concerns coherent ordinary states under a changed recurrence. It exhibits exactly which joint local observations can hold when the equality \(d_i=1\) has sparse exceptions. A single true ordinary escape with these record limits remains open. The previous bounded-carry control used \(d_i\in\{1,3,5,7\}\); that bound permits persistent discrepancies at a fixed prime. [Frozen previous control](https://github.com/GettysburgResearch/collatz/blob/9adafafbb715796a090448215dde1c77eb02d5d9/research/astra-global-closure-20261124/closing/adelic/README.md)

## Finite steering with inherited agreement

For any infinite positive-gap script its native starting class at position \(i\) is the odd \(2\)-adic integer
\[
  \xi_i=-\sum_{j\ge0}\frac{2^{A_{i+j}-A_i}}{3^{j+1}} .
\]
It obeys \(2^{e_i}\xi_{i+1}=3\xi_i+1\). A finite precision in \(\xi_i\) uses only letters through the required total physical cost. A run of at least \(r\) initial ones fixes \(\xi_i\equiv-1\bmod2^r\), the class for the all-ones script.

Let \(i<b\) be consecutive corrections, encompassing one block of \(b-i\) letters, with \(H=A_b-A_i\). At least \(r_b\) ones are fixed at the next block's start. Fix an odd positive \(Q\). Choose the least \(d_i>1\) satisfying
\[
 d_i\equiv 2^{e_i}\xi_{i+1}-3q_i
       \pmod{2^{H+r_b}},\qquad d_i\equiv1\pmod Q .              \tag{2}
\]
The binary residue is odd, and CRT gives \(d_i\le 2\cdot 2^{H+r_b}Q\). Every other edge of the block has \(d=1\). The new \(q_{i+1}\) is a positive odd ordinary integer congruent to \(\xi_{i+1}\) modulo \(2^{H-e_i+r_b}\). Multiplication by three preserves dyadic precision and dividing by \(2^e\) consumes \(e\) bits. All later edges therefore have positive odd endpoints and \(q_b\equiv\xi_b\bmod2^{r_b}\). If the incoming congruence has precision \(r_i\le H+r_b\), equation (2) gives \(d_i\equiv1\bmod2^{r_i}\) as well. Each \(d_i\) uses only the current block and the preassigned initial ones of the next. The rest of the next block can depend on \(q_b\).

## Three independent finite coordinates and a record

For every positive \(m\) prime to six the unit-carry actions \(f_1(x)=(3x+1)/2\), \(f_2(x)=(3x+1)/4\) permute \(\mathbb Z/m\). Their positive semigroup equals the group they generate by finiteness. The maps \(f_1f_2\) and \(f_2f_1\) have the same slope and differ by \(1/4\). Their quotient is translation by \(1/4\), which generates every translation on this ring. Simple directed paths thus connect any input to \(-1\), and \(-1\) to any output, in at most \(m-1\) gaps each. Since \(f_1(-1)=-1\), the concatenation can have **exactly** \(2m\) gaps. This holds also for \(m=1\).

Specify a backward critical prefix \(w=(b_1,\ldots,b_r)\), a dyadic odd class \(c\bmod2^h\), a class \(a\bmod m\) for \(m\) prime to six, and a nonempty open arc \(J\subset\mathbb T\) with rational endpoints. Choose a finite native forward word \(u\) from a positive odd representative of \(c\), with total physical cost \(H(u)\ge h\). Its gap cylinder forces the starting residue modulo \(2^h\): equal words imply equal initial values modulo \(2^{H(u)}\) by the iterated affine identity. Enumerate these tuples with each occurring infinitely often, for example by successive integer bounds on their entries.

For an era \(2^k\le i<2^{k+1}\), divide its \(2^k\) odd edges into \(k^2\) blocks of lengths \(s=\lfloor2^k/k^2\rfloor\) or \(s=\lceil2^k/k^2\rceil\). Take \(k\) sufficiently large. Write \(L_k=2^k/k^2\). Each block begins at \(i\) with one correction (2). Set \(r_i=\lfloor L_k/(4k)\rfloor\); every block starts with at least \(r_i\) ones. Let \(b_i=\max(k,\lfloor B(2^{2D_i})\rfloor)\) and take \(Q\) to be the odd part of \(\operatorname{lcm}(1,\dots,b_i)\). The construction starts with a record and all later block starts are records, so the argument of \(B\) is at least one. There are two kinds of blocks.

In an ordinary block, use the next tuple once \(m, |w|,H(u)\le k\) and once some \(n\in[i+\lceil s/2\rceil,i+\lfloor3s/4\rfloor]\) has \(n\alpha\bmod1\in J\). Otherwise use the default tuple (\(m=h=1\), \(w=(1)\), \(u=(1)\), unrestricted arc, arbitrary middle index) and retry the requested tuple later. A fixed \(J\) has bounded gaps for the irrational rotation: finitely many backward translates of \(J\) cover the circle by density and compactness. There are ordinary blocks of arbitrarily large length, so every tuple is eventually served. Prescribe the chronological pieces below.

- Start with \(P=\lceil s/k\rceil\) ones. Append a route of precisely \(2m\) letters in \(\{1,2\}\), then \(8m+2\) ones.
- Fill the remaining time up to \(n-|w|\) with the reverse of the corresponding prefix of \(b_j^*=\lfloor j\alpha\rfloor-\lfloor(j-1)\alpha\rfloor\). Append the reverse of \(w\), ending at \(n\).
- Apply \(u\) at \(n\), then \(4(H(u)+|u|+1)\) ones, then a reversed mechanical prefix to fill the block.

For all sufficiently large \(k\) the lengths fit uniformly. Everything except the route is determined before the block is steered. As \(m\mid Q\), the residue after the initial \(P\) gaps is obtained from \(q_i\bmod m\) by \(P\) applications of \(f_1\), including the corrected first step. All actions from the end of the route to \(n\) are invertible modulo \(m\). Route to the inverse image of \(a\) under those actions. Then choose \(d_i\) by (2).

The end of each reversed nonempty critical prefix strictly exceeds every earlier position within that piece in \(D\): each nonempty chronological suffix of length \(t\) costs \(<t\alpha\). A reversed mechanical piece gains less than one and every intermediate level is within one of its start. A length-\(2m\) routing word has any suffix loss at most \(2m(2-\alpha)\). The next \(8m+2\) ones more than repay this loss, including from its interior maximum. Likewise the \(4(H(u)+|u|+1)\) ones repay every suffix loss of \(u\). If the block starts at a record, both \(n\) and its far endpoint are therefore strict new records. Its net gain is
\[
              (\alpha-1)P+O(k+1)\asymp L_k/k .                  \tag{3}
\]
Within any block the minimum is at least its start minus \(O(k)\), and the maximum is at its endpoint. At the selected \(n\) the unit-carry edges immediately before and after it enforce
\[
 q_n\equiv\sum_{j=1}^r3^{j-1}2^{-B_j}\pmod{3^r},\qquad
 q_n\equiv c\pmod{2^h},\qquad q_n\equiv a\pmod m .             \tag{4}
\]
The first congruence comes from the last \(r\) edges. Neither local word crosses a correction.

## Long marked climbs and growth

At the start of eras whose index \(k\) is a sufficiently large power of two, take the smallest number of full blocks whose total length \(R_k\) is at least \(2D_{2^k}+k\). Use only ones in those blocks. The remaining blocks are ordinary. Before the first era, take one finite all-ones block starting at zero, with one correction chosen by (2) for the supplied \(q_0\). Its endpoint is a record; inherited precision is needed only at subsequent corrections.

To justify that the marked run fits, the previous possible mark has era index \(k/2\). The trivial bound \(D_t\le(\alpha-1)t\) at \(t=2^{k/2+1}\), followed by (3) in the intervening eras, gives
\[
 D_{2^k}\ll 2^{k/2+1}+\sum_{j=k/2+1}^{k-1}2^j/j\ll 2^k/k .
\]
Choose the first mark late enough for the estimate from the finite initialization. Thus \(R_k=O(2^k/k)\), using \(O(k)\) of the \(k^2\) blocks. Each marked era has total gain \(O(2^k/k)\), as does every ordinary era. Every full block, including each all-ones block, gains at least \(cL_k/k\). Geometric summation and the intra-block lower bound imply, for \(2^k\le n<2^{k+1}\),
\[
                    D_n\asymp 2^k/k\asymp n/\log n .            \tag{5}
\]
Every block has physical cost \(H=O(L_k)\): the mechanical and routing letters are at most two, the cost of \(w\) is at most \(\alpha|w|\), and \(H(u)\le k\). The elementary estimate \(\log\operatorname{lcm}(1,\ldots,b)=O(b)\) and (5) give \(\log Q=o(2^k/k)\) uniformly over resets in era \(k\). Indeed \(b_i=o(D_i)\). Equation (2) gives \(\log d_i=O(L_k)+o(2^k/k)=o(2^k/k)\). The exact real identity
\[
   q_n/M_n=q_0+\tfrac13\sum_{i<n}d_i/M_i                         \tag{6}
\]
now converges to a finite positive \(L\). Charging all \(2^k\) positions of an era at its largest correction costs at most \(2^k\exp(o(2^k/k)-c2^k/k)\). Positivity and (5) yield \(\log d_i/\log q_i\to0\). The number of exceptions through \(N\) is at most a constant plus \(\sum_{j\le\log_2 N}j^2\). Their spacings grow, every prescribed odd prime power eventually divides \(Q\), and inherited dyadic precision tends to infinity. Thus \(d_i\to1\) profinitely. At a late reset \(i\), (6) gives \(q_i\le2^{2D_i}\). Also \(\log_2 b_i=O(k)\) whereas \(r_i\gg k\). This gives the simultaneous modulus conclusion in statement 2.

At a reset the planned gap is one and eventually \(q_i\equiv-1\bmod4\), giving the native valuation. Choose the absolute \(c>0\) in statement 3 small enough that every late window with length \(R_j\) meets at most one reset and, if it crosses a reset \(i\), then \(R_j\le r_i/2\). This follows uniformly from the block lengths \(\asymp2^k/k^2\), the reset precision \(\asymp2^k/k^3\), and the bounded change of these scales between adjacent eras. Edges before the reset are genuine. After it the next \(R_j\) letters are ones. The reset starts at a coefficient record, so \(M_j\le M_i\) for \(j\le i\), and (6) gives \(q_j\le L M_i\le2^{2D_i}\) at all late such resets. For every \(m\le B(q_j)\), its odd part divides \(Q\), and \(v_2(m)\le\log_2 b_i=O(k)\). Consequently
\[
                    2^{R_j+1}m\mid d_i-1
\]
at every sufficiently late crossed reset. The difference from the true output there is \((d_i-1)/2\). Repeated multiplication by three and division by two preserve the native valuations and agreement modulo \(m\) for the rest of the window. The same reasoning for an arbitrary fixed \(m\) uses \(b_i\ge k\).

The threshold follows from elementary bounds on the least common multiple \(J(b)=\operatorname{lcm}(1,\ldots,b)\). The exponent of each \(p\) in \(\binom{2a}{a}\) is a sum of at most \(\lfloor\log_p(2a)\rfloor\) terms zero or one, so this binomial divides \(J(2a)\). Thus \(\log J(b)\gg b\) by the largest binomial coefficient in row \(2\lfloor b/2\rfloor\). Conversely \(J(2a)/J(a)\) is a product of distinct primes \(p\) with a power in \((a,2a]\). For each such power the corresponding term in \(v_p\binom{2a}{a}\) is one. Hence \(J(2a)/J(a)\mid\binom{2a}{a}\le4^a\); summing over dyadic scales gives \(\log J(b)\ll b\). If a subpower defect satisfies \(d_i>1\) and \(d_i\equiv1\bmod m\) for every \(m\le c_0\log q_i\), with fixed \(c_0>0\), then
\[
 \log(d_i-1)\ge\log J(\lfloor c_0\log q_i\rfloor)\gg c_0\log q_i .
\]
This is impossible at arbitrarily late corrections. Thus simultaneous congruences through a fixed positive multiple of \(\log q_i\) force eventual unit carry, whereas every specified sublogarithmic cutoff is attained by the construction.

## Ordinary injectivity and exclusion of rational shadows

By (6), \(q_n=q_t\) with \(t>n\) requires \(|D_t-D_n|=O(1)\). For \(n\) in era \(k\), (5) gives \(t=O(n)\), so its era index differs from \(k\) by \(O(1)\). If at least one entire block lies strictly between the two containing blocks, its gain is \(\gg L_k/k\). The first endpoint dominates \(D_n\), all subsequent full blocks gain, and the last block's interior can lose at most \(O(k)\) from its start. This excludes equality for large \(k\). Hence \(h=t-n=O(L_k)\), the physical cost \(E=A_t-A_n=O(L_k)\), and \(\max_{n\le i<t}\log d_i=o(kL_k)\). Iteration gives
\[
 (2^E-3^h)q_n=\sum_{j=0}^{h-1}3^{h-1-j}2^{A_{n+j}-A_n}d_{n+j}>0 .
\]
The integer coefficient is at least one. The right side is at most \(h\,3^h2^E\max d_{n+j}=\exp(o(kL_k))\), whereas \(q_n\ge q_0 2^{D_n}=\exp(\Omega(kL_k))\). Thus the path is eventually injective.

Suppose a tail has a native rational \(2\)-adic starting point, with positive odd denominator \(b\). Its successors \(y_n\) have denominators dividing \(b\). Formula (6) on that tail with every carry one gives \(|y_n|\ll M_n\), allowing either sign. For a marked run of \(R_k\) ones starting at \(n=2^k\),
\[
 2^{R_k} b(y_{n+R_k}+1)=3^{R_k} b(y_n+1).
\]
The integer \(b(y_n+1)\) is divisible by \(2^{R_k}\) and has absolute size \(O(2^{D_n})\). By \(R_k\ge2D_n+k\), it vanishes for every sufficiently late mark. The point \(-1\) has only the constant gap-one itinerary, contradicting the gap mean \(\alpha>1\). This proves statement 5. After deleting a finite prefix the model can be an orbit of a deterministic altered map, since the remaining ordinary states never repeat.

## Exact accumulation sets

Every strict \(M\)-record is a strict \(q\)-record by (6). On any \(q\)-record sequence \(n\to\infty\), for fixed \(j\ge1\),
\[
 1<q_n/q_{n-j}
 =3^j2^{-(A_n-A_{n-j})}\frac{q_n/M_n}{q_{n-j}/M_{n-j}} .
\]
The last fraction tends to one. Since \(3^j\) is no power of two, eventually \(A_n-A_{n-j}<j\alpha\). Each fixed length of reversed gaps at late records has finitely many possibilities. Given a convergent record subsequence, take a diagonal further subsequence on which all reversed prefixes stabilize. The resulting gaps \(b_j\) obey every strict critical inequality. For fixed \(r\), iteration of the last \(r\) rows gives
\[
  q_n\equiv \sum_{j=1}^r 3^{j-1}2^{-(A_n-A_{n-j})}d_{n-j}\pmod{3^r}.
\]
All these \(d_{n-j}\) eventually equal one modulo \(3^r\). Thus the limiting ternary coordinate belongs to \(K_{\rm crit}\). The other coordinates obey the immediate constraints in (1).

Conversely (4) attains every prescribed finite neighborhood of the profinite coordinates in (1) infinitely often at strict \(M\)-records, jointly with \(n\alpha\bmod1\in J\). Any finite specification away from two and three is one residue modulo \(m\) by CRT. For the circle, \(\log_2 q_n\bmod1=n\alpha+\log_2 L+o(1)\bmod1\) by (6). Inside the desired arc shifted back by \(\log_2 L\) choose a rational-endpoint arc with closure still inside. The enumeration serves that arc infinitely often. The product is compact and metrizable, so meeting every neighborhood infinitely often is exactly accumulation. Together with the upper inclusion at all height records this proves (1) for both notions of records.
