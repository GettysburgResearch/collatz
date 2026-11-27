# Primitive positive rational cycles with small complete denominators

The following are actual ordinary-shortcut **rational** cycles. Their least periods tend to infinity and their full reduced denominators \(q\) have \(\log q=o(h)\). One choice gives the stronger bound
\[
 \log q=O\!\left(\frac{(\log h)^3}{(\log\log h)^2}\right).              \tag{1}
\]
Another choice retains a nearcritical clock \(0<h-p\log_2 3<h^{-1+o(1)}\), a minimum at least \(h^{2-o(1)}\), and a universally bounded maximum-to-minimum ratio. The estimates do not exhibit denominator one. They show why a global exponential denominator lower bound cannot follow from least period, positivity, nearcriticality and bounded physical amplitude by themselves.

## The cell construction

Choose distinct primes \(\ell_1,\ldots,\ell_s\ge5\) and let \(N=\prod_i\ell_i\). A template is a binary word of length \(n\) with \(b>0\) ones and \(s\) marked disjoint occurrences of \(10\), with neither endpoint wrapping around the template. We require \(A=2^n>B=3^b\) and \(\gcd(n,b)=1\). In cell \(j\), \(0\le j<N\), swap marker \(i\) to \(01\) precisely when \(\ell_i\mid j\). Read the \(N\) cells in order. The length is \(h=Nn\), its odd count is \(p=Nb\), and \(\gcd(h,p)=N\).

At a fixed marker, swapping transfers one odd letter one place forward. Its carry contribution changes from \(2^{t_i}3^{u_i}\) to \(2^{t_i+1}3^{u_i}\), where \(u_i\) is the number of ones strictly after this marker. Other disjoint swaps preserve those counts. Thus the exact carry of cell \(j\) is
\[
 c_j=c_*+\sum_{i=1}^s d_i\,{\boldsymbol 1}_{\ell_i\mid j},
 \qquad d_i=2^{t_i}3^{u_i}>0.                                          \tag{2}
\]
Every cell has the same homogeneous multiplier \(B/A\). The actual rational fixed point at cut zero is
\[
 x=\frac{C(A)}{A^N-B^N},\qquad
 C(T)=\sum_{j=0}^{N-1} c_j B^{N-1-j}T^j.                              \tag{3}
\]
This fraction is positive and its denominator is coprime to six. Rotating its affine fixed point to each cut gives the true shortcut parities, by reducing the literal carry modulo two. The correspondence between binary cyclic words and rational cycles is classical. [Lagarias, *The set of rational cycles for the 3x+1 problem*](https://doi.org/10.4064/aa-56-1-33-53)

Suppose the full bit word were a \(k\)-fold repetition with \(k>1\). Then \(k\mid\gcd(h,p)=N\), so advancing \((N/k)n\) bits must preserve the word. At the fixed marker slots this advances each indicator in (2) by \(N/k\) cells, hence \(\ell_i\mid N/k\) for every \(i\), an impossibility. Distinct parities of the deterministic rational map distinguish phases. Thus \(h\) is the **least** period.

Let \(\Phi_\ell(T,B)=\sum_{j=0}^{\ell-1}T^jB^{\ell-1-j}\) for prime \(\ell\). Then
\[
 q\ \mid\ P(A),\qquad
 P(T)=(T-B)\prod_{i=1}^s\Phi_{\ell_i}(T,B),\qquad
 J=\deg P=1+\sum_{i=1}^s(\ell_i-1).                                    \tag{4}
\]
Indeed, at a root \(T=B\zeta\) of \(T^N-B^N\), the remaining sum after removing \(B^{N-1}\) is \(\sum c_j\zeta^j\). At \(\zeta=1\) it is positive. For a nontrivial \(\zeta\) of order dividing \(N\), the indicator at \(\ell_i\) sums to \(N/\ell_i\) if \(\zeta^{\ell_i}=1\), and to zero otherwise, by a finite geometric sum. Distinct prime orders are disjoint outside one. Thus the exact common roots have all orders other than \(1,\ell_1,\ldots,\ell_s\). The monic quotient \((T^N-B^N)/P(T)\) divides \(C(T)\) in \(\mathbb Z[T]\), by monic polynomial division. The residual numerator is coprime to \(P(T)\) over \(\mathbb Q[T]\). Evaluation at \(T=A\) proves (4). Equivalently, every periodic forcing term in (2) has an individual determinant \(A^{\ell_i}-B^{\ell_i}\), and (4) is a common multiple including the mean forcing. The finite identity says that a periodic forcing keeps its individual determinant under a common return, and that equal-length forcings add. The [Lean periodic-forcing identities](IndependentClocks.lean) formalize this finite calculation.

There is also an **exact full numerical denominator**, even when all parameters vary. Set \(F_i=\Phi_{\ell_i}(A,B)\) and \(M_0=Nc_*+\sum_i(N/\ell_i)d_i=\sum_{j<N}c_j\). Summing the periodic impulses in (2) gives
\[
 x=\frac{c_*}{A-B}+
    \sum_i\frac{d_i B^{\ell_i-1}}{(A-B)F_i},\qquad
 \boxed{\quad q=
 \frac{A-B}{\gcd(A-B,M_0)}\prod_i F_i .\quad}                          \tag{5}
\]
To prove the denominator formula, first \(F_i\) and \(F_j\) are coprime for \(i\ne j\). Any common prime \(l\nmid A-B\) would make the nontrivial multiplicative order of \(A/B\bmod l\) divide both \(\ell_i\) and \(\ell_j\). A prime \(l\mid A-B\) dividing \(F_i\) must equal \(\ell_i\) by the geometric sum modulo \(A-B\), and cannot also equal \(\ell_j\). Each \(F_i\) is coprime to six. Modulo \(F_i\), \(P(A)x\) is \(d_iB^{\ell_i-1}\prod_{j\ne i}F_j\), a unit because \(d_i\) has only prime divisors two and three. Hence a canceled prime cannot divide any \(F_i\). Modulo \(A-B\) one has \(P(A)x\equiv B^{J-1}M_0\), proving (5). In particular **every constructed cycle has \(q>1\)**. The proof is elementary and requires no uniform bound for a resultant or for individual prime factors.

For **fixed** primes and a fixed marked prefix, append an arbitrarily long all-zero tail, keeping \(b\) fixed and \(n\) coprime to \(b\). The cell carries and \(M_0\) remain fixed, so (5) gives \(\log_2 q/h\to J/N\) exactly. For example \(\ell=(5,7,11)\) gives \(J=21,\ N=385\), hence rate \(3/55\); more primes can make the rate arbitrarily small with genuine least period. For variable primes one always has
\[
 (J-1)n\le\log_2 q\le Jn+\log_2 N,
\]
since \(A^{\ell_i-1}\le F_i\le\ell_i A^{\ell_i-1}\). Thus the order of the right-hand side in (1) is attained for the stated first diagonal, by the prime number theorem.

## Nearcritical physical cycles

Choose upper continued-fraction convergents \(n/b>\gamma=\log_2 3\) with \(0<n-b\gamma<1/b\); infinitely many exist. Put \(a_t=\lfloor(t+1)b/n\rfloor-\lfloor tb/n\rfloor\), \(0\le t<n\). There are \(\gg n\) nonwrapping disjoint occurrences of \(10\) for all sufficiently large convergents. Since \(b/n>1/2\), this mechanical word has no consecutive zeros, and all but possibly one zero therefore ends such a pair. There are \(n-b\) zeros. Use any \(s\) of the available markers.

Any interval **inside a cell** has odd count within three of its length times \(b/n\). In the base word the deviation is strictly less than one, and at most two swaps can cross its endpoints. Consequently every homogeneous multiplier \(3^u/2^v\) for an interval of length \(v\le n\) and weight \(u\) lies between two absolute positive constants. For instance \(1/54\le3^u/2^v\le27\) follows from \(0<n-b\gamma<1/b\) and \(b\ge1\). The cell's normalized carry \(c_j/A\) is one-half the sum over its \(b\) odd departures of the homogeneous multiplier of the interval after that departure. Thus
\[
 b/108\le c_j/A\le 27b/2 .
\]
The actual cell boundaries follow \(x_{j+1}=(B/A)x_j+c_j/A\). Periodicity and the geometric series place every \(x_j\) between the minimum and maximum of \(c_j/A\), each divided by \(1-B/A\). The same interval bounds control every within-cell state: a positive homogeneous multiple of \(x_j\) plus a nonnegative carry at most \(27b/2\). The odd and even shortcut states all lie in an interval \([M,K M]\) with absolute \(K\), and \(M\gg b/(1-B/A)\gg b^2\). These are bounds on the actual cycle states.

First let \(s=\lfloor (n-b)/2\rfloor\) and use the first \(s\) primes at least five. The prime number theorem gives \(\log N=\Theta(s\log s)\), \(\sum_i \ell_i=O(s^2\log s)\). Since \(A>B\), (4) gives \(P(A)\le N A^J\), hence \(\log q=O(n s^2\log s)\). Now \(n=\Theta(s)\), \(h=nN\), proving (1). This sequence also has \(M\gg(\log h/\log\log h)^2\).

For a different diagonal, take \(s\to\infty\), take the same first primes, and subsequently pick an upper convergent with \(n>N^s\). This ensures enough available markers. Then \(N=h^{o(1)}\), \(J/N\to0\), \(M\gg b^2=h^{2-o(1)}\) and
\[
 0<h-p\gamma=N(n-b\gamma)<N/b=h^{-1+o(1)}.
\]
From \(q\le N A^J\) again, \(\log q/h=o(1)\). The stronger numerical denominator bound (1) belongs to the first choice; the very small total clock defect belongs to this second one. Both are positive primitive rational sequences.

## The strong diagonal fits arbitrarily close to one odd octave

Mark the \(s\) copies of \(10\) whose second site \(t\) has \(f_t=\{tb/n\}\) equal to \(1/n,\ldots,s/n\). These sites exist since \(\gcd(b,n)=1\). For \(s/n<\min(b/n,1-b/n)\) and \(t\ne0\), the preceding bit is one and the base bit at \(t\) is zero. For the prefix ending just before site \(t\) in cell \(j\), the odd count is \(\lfloor tb/n\rfloor-\epsilon_{j,t}\), with \(\epsilon_{j,t}=1\) exactly at a newly odd site shifted by a chosen marker. At any unchanged odd site \(f_t\ge1-b/n\). At any new odd site \(f_t+\epsilon_{j,t}\le1+s/n\). Thus all actual odd cuts satisfy
\[
 1-b/n\le f_t+\epsilon_{j,t}\le1+s/n .
\]
Put \(\delta=n\log2-b\log3\). Multiplying the exact physical branch law up to any cut gives
\[
 \frac{x_{j,t}}{x_{0,0}}
 =3^{-f_t-\epsilon_{j,t}}
   \exp\!\left(-(j+t/n)\delta+E_{j,t}\right),
 \qquad 0\le E_{j,t}\le N\delta .
\]
Indeed \(E_{j,t}\) is the partial sum of \(\log(1+1/(3x))\) over actual odd departures. All summands are positive and the complete sum is exactly \(N\delta\). On \(n>N^s\) this proves
\[
 \frac{\max_{\rm odd}x}{\min_{\rm odd}x}
 \le 3^{\,b/n+s/n}e^{2N\delta}
 =2+O((s+N)/b)=2+h^{-1+o(1)} .
\]
For \(s/n<\min(1-b/n,2b/n-1)\), each marked triple \(t-2,t-1,t\) is \(110\) in the base template: \(f_{t-2}=f_t+2(1-b/n)\) without reduction and \(f_{t-1}=f_t+1-b/n\). The swap produces \(101\). Its new zero has ones on both sides. A distinct marked pair cannot change the preceding bit to zero because this would require an overlapping \(10\) pair. The base has no consecutive zeros, including across the cell boundary. Consequently **every actual odd-to-odd exponent is one or two**. The displayed smallness condition holds eventually in both parameter choices when their markers are selected by these phases.

For the strong diagonal, an odd state greater than twice the true odd minimum must have \(f_t+\epsilon_{j,t}\le1-\log_3 2+s/n+2N\delta/\log 3\). Eventually no shifted odd site meets this condition. An unchanged odd site already has \(f_t\ge1-b/n\), and the phases form the \(1/n\) grid. Hence the proportion of actual odd states exceeding twice the odd minimum is \(O((1+s+N)/b)=h^{-1+o(1)}\). This is a genuinely rational contrast with the reported integral odd-occupation obstruction. [Wren, *Odd heights of positive Collatz cycles*](https://rstation.ai/problems/collatz/papers/210/v1)

All shortcut states have ratio at most \(3+h^{-1+o(1)}\) by the same formula. Eventually the odd ratio is **strictly greater than two**: a primitive cycle fitting one odd octave has \(q=D\) by the adjacent-gap argument, whereas here \(\log q=o(h)\) and \(D=A^N-B^N\ge A^{N-1}\) since \(A-B\ge1\). Thus any fixed positive enlargement of the one-octave band admits these small-complete-denominator rational examples. [Prior one-octave deduction and sources](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-global-synthesis-20261124/arithmetic/proof.md)

Prior repository work applied cyclotomic selectors, resultants and Parseval to arbitrary arrangements of two equal-clock words. The present construction uses independently editable marker slots within each cell, realizes multiple prime cell clocks at once, and computes the entire numerical denominator (5). [Prior two-block cyclotomic analysis, §4](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-ordinary-boundary-20261124/arithmetic/README.md)

Lagarias' Theorem 3.2 proves that infinitely many fixed candidate denominators \(k\) either support no primitive generalized cycle or all such cycles have \(k\le(\log D)^3\). His disjunction does not construct a nonempty family with that polynomial bound. Here the constructed cycles exist, with quasi-polynomial \(q\) in (1); polynomial \(q\) and bounded \(q\) are stronger. Fixed-width rank arguments and fixed-complexity denominator estimates do not assert a universal exponent. [Original theorem](https://matwbn.icm.edu.pl/ksiazki/aa/aa56/aa5614.pdf)


[Exact replay](check_independent_clocks.py) checks the complete reduced fraction, not merely its cyclotomic upper bound. Four small cases replay every true parity and certify the least period through \(25{,}025\). Two factored cases compute (5) without expanding the full word, including a period \(2{,}103{,}896{,}795\) instance of full denominator bit length \(1{,}211{,}624\). The small physical ratios are diagnostic values. [Archived integer-arithmetic output](../../../reports/astra-infinite-descent-20261127/cycles/INDEPENDENT_CLOCKS.json)

[Lean affine kernel](IndependentClocks.lean) proves carry concatenation, additive superposition, the division-free periodic-denominator identity for arbitrary repeated cell forcings, and addition of rational coordinates over a common denominator. Formula (5), native primitivity, and the growing parameter estimates are written proofs.
