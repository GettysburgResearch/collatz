# Computing the entire limiting denominator spectrum at each fixed odd grade

Let \(\mathcal S_p\) be the set of all subsequential limits of \(\log_2(q)/L\) along positive rational shortcut cycles of **least** native period \(L\to\infty\) and exactly \(p\) odd departures, with \(q\) their complete reduced denominator. The input of the following proposed theorem is an arbitrary positive integer \(p\).

**Theorem.** There is an algorithm which halts and outputs the finite set \(\mathcal S_p\) exactly, as rational numbers. It can also output, for each listed number \(\sigma\), integer coefficients in
\[
         L_n=k n+a,\qquad u_{i,n}=c_i n+b_i\quad(0\le i<p),           \tag{1}
\]
which for every sufficiently large integer \(n\) give the sorted odd dates of a primitive positive rational cycle attaining
\[
                          \log_2 q_n=\sigma L_n+O(1).                   \tag{2}
\]
With a further arithmetic progression in \(n\), the ratio \(q_n/2^{\sigma L_n}\) has a finite nonzero limit. The algorithm decides which asymptotic exponents **occur**. It gives no effective uniform threshold at which all calendars of a given grade approach this set. The underlying fixed-target gcd theorem is ineffective.

The [prime-grade and prime-power calculation](PRIME_GRADE_DENOMINATORS.md) gives explicit sharp families, and [PR212](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/MOVING_ARCS.md) already implies that the only possible fixed-grade exponents are multiples of \(1/p\). That finite list of candidates alone does not decide occurrence or construct an attaining family. We use a one-parameter realization of each occurring exponent, then reduce the consequent existence problem to linear integer arithmetic.

## Every limit has an affine-calendar realization

Start with a sequence tending to a chosen exponent. Use the affine-space reduction in the [prime-grade proof](PRIME_GRADE_DENOMINATORS.md), retaining its notation \(F=2^aX^k-3^p\), \(B=\sum_i 3^{p-1-i}2^{b_i}X^{c_i}Y^{v_i}\), \(U=\gcd(F,B)\) monic, and \(V=F/U\). That argument gives the original limit \(\deg V/k\). Write \(m\) for the integer coordinates corresponding to \(Y\); the total length is \(a+kn\) with \(X=2^n\).

Each cyclic gap between odd dates is an integer affine functional of \((n,m)\). After thinning, each gap is either fixed or tends to infinity. A fixed gap is constant on the whole chosen affine space by its minimality. We may rotate the original word at the outset so that \(u_0=0\) on every calendar, so that positivity of the cyclic gaps and of \(L\) suffices for the ordering. Take a difference \((N,\mu)\) of a sufficiently late parameter point and one earlier point, with \(N>0\) and positive linear increments simultaneously on every growing gap. This integer vector keeps all fixed gaps constant.

For the new one-parameter curves use
\[
                       X=T^N,\qquad Y_i=2^{t_i}T^{\mu_i},
                          \qquad T=2^v,\quad v\to\infty .
\]
We may also start at any fixed \(n_*\) by multiplying \(X\) by \(2^{n_*}\). Pick \(n_*,t_i\) as follows. For each nontrivial rotation of the \(p\) cyclic gaps, fix one difference of corresponding affine gaps which is not identically zero; this is possible by primitivity of the original sequence. Each such difference whose linear increment on \((N,\mu)\) vanishes must be nonzero at the chosen starting point. These finitely many proper affine hyperplanes can be avoided by first choosing \(n_*\) away from the finitely many constraints depending only on \(n_*\), then avoiding proper affine hyperplanes in \(t\). The resulting gap array has no nontrivial period for all sufficiently large \(v\).

Fix this \(n_*\) and put \(c=2^{n_*}\). For each of the finitely many roots \(\beta\) of \(V(cT^N)\), the Laurent polynomial \((B/U)(c\beta^N,Y)\) is nonzero as a polynomial in \(Y\). Otherwise the irreducible polynomial of \(c\beta^N\) over the rationals divides every coefficient, contrary to the choice of \(U\) and the squarefreeness of \(F\). Thus
\[
               (B/U)(c\beta^N,2^{t_i}\beta^{\mu_i})
\]
can be made nonzero for all these roots at once: the points \((2^{t_i})\) are Zariski dense in the torus, and the finitely many excluded affine hyperplanes on \(t\) also exclude just proper character hypersurfaces there. This works when \(m\) has no coordinates: there is then no specialization capable of introducing roots beyond \(U\). Consequently the univariate residual polynomials are coprime after these substitutions and Laurent powers can be cleared without touching the nonzero roots of \(V(cT^N)\). The positive cyclic gaps and primitivity hold eventually, so these are genuine primitive words and their positive rational cycles are the usual word fixed points.

The evaluated gcd of two coprime fixed integer polynomials divides their fixed nonzero resultant (or a nonzero integral Bézout constant). After clearing fixed denominators and Laurent powers this gives a bounded residual gcd outside two and three on the curve. The local valuations at two and three of \(V(cT^N)\) cost \(O(1)\) as in the prime-grade proof. Therefore \(\log_2 q_v=Nv\deg V+O(1)\), giving (2) with \(L_v=a+kn_*+kNv\). Moreover each residual gcd is drawn from finitely many divisors of a fixed integer. At every relevant odd prime the sequence \(2^v\) is periodic modulo the fixed prime powers needed to determine those divisors; Laurent denominators are units there outside their fixed scalar denominators, which cost only fixed additional precision. The valuation at two stabilizes, and at three it is bounded as above. Thus on a residue class all the finite local factors stabilize, while the real leading coefficient is fixed. This proves the ratio claim. The argument from an arbitrary attaining sequence is existential; the effective search for families follows next.

## At most \(2p\) characters after removing the real radical

Take an integer affine family (1), ordered and primitive for large \(n\). Here and below \(k\ge1\), \(0\le c_i\le k\), and offsets \(a,b_i\) may be negative. In the parameter \(X=2^n\) the native denominator polynomial is \(2^a X^k-3^p\) and the numerator polynomial is \(\sum_i3^{p-1-i}2^{b_i}X^{c_i}\). The same univariate resultant argument says that \(\sigma\) is exactly the fraction of the \(k\) distinct denominator roots which are not numerator roots.

Set
\[
 g=\gcd(k,a,p),\quad k'=k/g,\quad p'=p/g,\quad a'=a/g,\quad
 e=\gcd(2,k'),\quad d=k'/e,\quad t=ge\le2p,
 \qquad \lambda=(3^{p'}2^{-a'})^{1/k'}>0.
\]
Over the maximal abelian extension \(K=\mathbb Q^{\rm ab}\) we have
\[
                           [K(\lambda):K]=d.                            \tag{3}
\]
Indeed \(\mathbb Q(\lambda)\) has degree \(k'\): the constant term of its monic minimal polynomial has valuations \(r p'/k'\) and \(-r a'/k'\) at three and two when its degree is \(r\), and \(\gcd(k',a',p')=1\). The same calculation shows \(\mathbb Q(\lambda^s)\) has degree \(k'/s\) for any divisor \(s\mid k'\), with its full binomial as minimal polynomial. Over \(K\), all \(k'\)th roots of unity are present. Thus the finite extension \(K(\lambda)/K\) is Galois with its group identified by \(\lambda\mapsto\zeta\lambda\) with a subgroup of the cyclic group \(\mu_{k'}\). Write its order \(s\). Then \(\lambda^s\in K\). In the chosen embedding \(\mathbb Q(\lambda^s)\subseteq\mathbb R\), because \(\lambda\) is positive real. As a subfield of the abelian extension it is Galois over \(\mathbb Q\). If \(k'/s>2\), the irreducible binomial for this positive real radical has nonreal roots, inconsistent with normality of this real subfield. Hence \(k'/s\le2\). When \(k'\) is even, \(\lambda^{k'/2}\) is a square root of a rational number and already belongs to \(K\), giving \(s\mid k'/2\). This proves (3) for both parities.

All roots of the original denominator are \(\lambda\zeta_k^j,\ 0\le j<k\). Write
\[
       c_i=r_i+d z_i,\quad 0\le r_i<d,\quad 0\le z_i\le t,\qquad
       a'=e w+\eta,\quad 0\le\eta<e,\qquad B_i=b_i-wz_i .
\]
The coefficient of \(\lambda^{r}\zeta_k^{jr}\) in evaluating the numerator at the \(j\)th root is
\[
 \sum_{i:\,r_i=r}
  3^{p-1-i}
  \left(3^{p'/e}2^{-\eta/e}\zeta_t^{\,j}\right)^{z_i} 2^{B_i}.         \tag{4}
\]
All displayed coefficients apart from \(2^{B_i}\) lie in a fixed explicit abelian number field for each \(p,g,e,\eta\), for example \(\mathbb Q(\zeta_t,\sqrt2,\sqrt3)\). By (3), the powers \(\lambda^r,\ 0\le r<d\), are linearly independent over \(K\). Therefore a root vanishes exactly when (4) vanishes in every occupied residue class \(r_i=r\). This property depends only on \(j\bmod t\), independently of the possibly unbounded \(k\). The exponent is the fraction of the \(t\) residues which do not vanish.

## The remaining test uses integer addition and fixed congruences

For a fixed tuple of computable algebraic coefficients \(\alpha_i\), the predicate
\[
                          \sum_i\alpha_i 2^{B_i}=0                       \tag{5}
\]
on integer variables \(B_i\) is effectively definable in Presburger arithmetic. Express all coefficients in a rational basis of a number field containing them and clear fixed denominators. This gives integer vectors \(v_i\) with (5) equivalent to vector vanishing. Fix an integer \(H\) with \(2^H>p\max_i(1,\|v_i\|_\infty)\). Enumerate weak orderings of the \(B_i\). At a consecutive gap larger than \(H\), multiply by a common power of two to make all exponents nonnegative. Each coordinate of the sum of terms below the gap has absolute value smaller than the full binary place of the first exponent above the gap. If the total is zero, each lower coordinate is divisible by that binary place, and hence is zero. Thus the full sum is zero exactly when each consecutive block separated by such gaps sums to zero. Inside a block, all consecutive differences belong to \([0,H]\); enumerate these finitely many offsets and compute (5) after subtracting the smallest exponent in the block. This produces a finite Boolean combination of integer affine comparisons for (5), also valid for moving negative exponents and repeated exponents. The zero tests on algebraic coefficients use finite number-field arithmetic, e.g. cyclotomic polynomials and adjoining the two displayed square roots. Their negations are effective too.

To compute \(\mathcal S_p\), enumerate \(g\mid p,\ e\in\{1,2\},\ 0\le\eta<e\), every \(z_i\in[0,ge]\), and all partitions of the \(p\) indices by equality of their \(r_i\). All these choices are finite before any unbounded variables are introduced. For each choice, existentially quantify integer variables \(d,w,r_i,B_i\). Require \(d\ge1,\ 0\le r_i<d\), the chosen equality partition (different parts are different residues), \(ed\) odd if \(e=1\), and
\[
                        \gcd(ed,ew+\eta,p')=1 .
\]
The last requirement is a finite conjunction that no prime divisor of the fixed \(p'\) divides both of the first two quantities. Set the linear expressions
\[
 k=ged,\quad a=g(ew+\eta),\quad c_i=r_i+d z_i,\quad b_i=B_i+wz_i.
\]
Enforce \(0\le u_{0,n}<u_{1,n}<\cdots<u_{p-1,n}<kn+a\) eventually by lexicographic coefficient comparisons of these affine functions. For \(p>1\), require for each shift \(1\le s<p\) that at least one cyclic gap \(u_{i+1,n}-u_{i,n}\), with \(u_{p,n}=L_n+u_{0,n}\), differs in slope or intercept from its shift by \(s\). This is precisely primitivity for all large \(n\), since two different affine functions coincide on at most one integer and native periodicity permutes the odd dates by a cyclic shift. For \(p=1\) this condition is vacuous. All comparisons so far involve only addition and fixed coefficients.

Finally enumerate which of the \(t=ge\) residues are numerator zeros. Enforce that exact pattern using (4)–(5) for the selected partition and coefficient data. Every coefficient in (4) is fixed at this stage; neither unbounded \(d\) nor \(r_i\) occurs in it. The resulting formula is an existential Presburger sentence. [Oppen's decision-procedure theorem](https://doi.org/10.1016/0022-0000(78)90021-1) suffices to decide it; no efficiency bound is needed here. For every satisfiable sentence record the fraction of nonzero residues. An explicit satisfying tuple can be obtained by enumerating integer tuples until the decidable quantifier-free conditions hold on one, after affirmative decision. Equations (1) then supply the claimed calendars. Conversely every affine family produces one of these finite case splits with a satisfying tuple, and the first section gives such a family for every actual limit. This proves termination and exactness of the mathematical algorithm for every input \(p\). No large-grade numerical implementation or effective convergence-rate estimate is part of this assertion.

## Executable specialization

The [solver](solve_denominator_spectrum.py) builds quantifier-free linear integer formulas for the existential tests above. It represents the algebraic coefficients in the ordinary power basis of \(\mathbb Q(\zeta_{\operatorname{lcm}(24,t)})\), using \(\sqrt2=\zeta_8+\zeta_8^{-1}\), \(\sqrt3=\zeta_{12}+\zeta_{12}^{-1}\). Larger common denominators are cleared before binary gap sizes are chosen. Bounded representatives \(E_i\in[0,(p-1)(H+1)]\) preserve each nonnegative pairwise difference \(B_j-B_i\le H\) exactly and keep every larger difference greater than \(H\). They always exist by clipping sorted adjacent gaps at \(H+1\). Consequently replacing \(2^{B_i}\) by the finite lookup \(2^{E_i}\) keeps all zero predicates while leaving the original \(b_i\) for chronological order and primitivity. Shifting the integer family parameter puts \(0\le a<k\), and one native rotation puts \(u_{0,n}=0\).

By default the solver first prunes character patterns using rational conjugacy. For a cyclotomic automorphism \(u\) on the conductor \(\operatorname{lcm}(24,t)\), the real coefficient \(3^{p'/e}2^{-\eta/e}\) in (4) changes by a sign. When \(e=2\), conjugation negates \(\sqrt3\) for \(u=5,7\bmod12\) and \(\sqrt2\) for \(u=3,5\bmod8\), with only the roots present in the coefficient contributing. Thus the surviving \(j\) are unions of orbits of \(j\mapsto uj\) for a positive sign and \(j\mapsto uj+t/2\) for a negative sign. The positive root survives and the orders \(g/\gcd(g,j)\) of the surviving images have lcm \(g\) by the proper-shorter-congruence obstruction. With the optional switch \(\texttt{--no-character-pruning}\) the solver tests the theorem's formulas directly without these reductions. A satisfiable model is independently checked for chronological order, least period and the claimed degree by exact univariate polynomial gcd. An unresolved query aborts the run.

The [checked receipt](FIXED_GRADE_SPECTRUM_SOLVER.jsonl) computes \(\mathcal S_p=\{1\}\) at \(p=1,2,3,5\) and \(\mathcal S_4=\{3/4,1\}\) through the general program. Normal and optimized Python agreed. A separate time-limited run at grade six returned unresolved on one formula and furnished no grade-six spectrum. The command below reproduces the successful small-grade run and can optionally export its individual SMT-LIB inputs with \(\texttt{--dump-dir}\).

~~~sh
python -B solve_denominator_spectrum.py 1 2 3 4 5 --timeout-ms 15000
~~~
