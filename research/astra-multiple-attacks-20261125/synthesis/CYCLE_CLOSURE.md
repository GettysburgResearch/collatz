# Full-cycle factors and proper-arc carries

**PROPOSED written deductions.** On a bounded ordinary cycle every proper arc between distinct odd phases has very small gcd with the **complete** lap determinant, although the full lap carry must be divisible by that determinant. This gives a check for rational candidates independently of the degree or factorization of their rank polynomial. It does not prove that no such ordinary cycle exists. The last two sections exhibit genuine rational shortcut cycles testing the large-factor and all-cuts arguments separately.

## A proper chronological arc

Let $h,p$ be the shortcut length and odd count of a positive rational cycle and $D=2^h-3^p>0$. All phases have the same reduced denominator $d\mid D$: the complete affine equation at each cyclic cut gives a denominator dividing $D$, and the two affine branches preserve a negative valuation outside 2 and 3. For two **distinct odd phases**, write their reduced numerators as $A,B>0$. Both are odd ternary units since the rational cycle follows an odd departure and subsequent halvings modulo 3. The chronological arc from the first to the second has length $n\le h$, odd count $k$, and literal nonnegative carry $C$:
$$
             d C=2^n B-3^k A.
$$
Write $t=\gcd(A,B)$, $A'=A/t$, $B'=B/t$. Define $M=1+\log(2\max(A,B))$ and $E=|k-np/h|$. For $1\le J\le h$, uniformly in the arc,
$$
 \log\gcd(D,C)\ \ll\ \log t+1+\frac hJ+J(M+E).                     \tag{1}
$$

**Proof.** Set $G=\gcd(D,2^n B'-3^k A')$. Since $\gcd(D,C)\mid\gcd(D,dC)$, the left side is at most $\log t+\log G$. The modulus $G$ is prime to $6A'B'$: it divides $D$, and $A',B'$ are coprime. In its unit group,
$$
          2^h3^{-p}=1,\qquad 2^n3^{-k}B'/A'=1 .
$$
By Dirichlet's box argument on $0,n/h,\ldots,Jn/h$ modulo one, some $1\le j\le J$ and $i\in\mathbb Z$ satisfy $|ih+jn|\le h/J$. Then $|ip+jk|\le(p/h)|ih+jn|+jE\le h/J+JE$. The positive rational number
$$
          W=(B'/A')^j\, 2^{ih+jn}\,3^{-ip-jk}
$$
equals one modulo $G$ and differs from one over $\mathbb Q$. Indeed $B'/A'\ne1$ is a ratio of distinct coprime integers prime to six, so its valuation at some prime outside $\{2,3\}$ is nonzero. After clearing denominators, $G$ divides a nonzero difference of two positive integers, each of logarithm $O(h/J+J(M+E))$. This proves (1), including prime powers of arbitrary multiplicity in $D$. The proof uses no irreducibility, coprimality of $h,p$, asymptotic factor distribution, or independence assumption about successive cuts.

**Bounded branch.** Suppose all odd phases lie in $[m,C_0m]$, with $C_0$ fixed, and their real sizes are at most $h^{A_0}$. In the bounded least-disagreement branch the referenced bound on odd width is $(16m+7)/(3m)$, and the real two-log estimate gives a polynomial bound for $m$ from the lap identity. [PR195, bounded branch and rank order](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round9/critical/README.md) · [Concentration and two-log input](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round12/cycle/README.md)

For a primitive ordinary lap, $E=O_{C_0}(1)$: the real logarithmic correction along each arc is bounded by that on the whole lap, which is $O(1)$ by the uniform finite-simple-path reciprocal estimate. The endpoint log ratio is bounded by $\log C_0$. Subtract $n/h$ times the lap log equation from the arc log equation. For repeated ordinary lap clocks one first discards any complete primitive laps from the arc: the density $p/h$ and the discrepancy $k-np/h$ are unchanged. Thus $M=O_{A_0}(\log(2h))$, giving
$$
         \log\gcd(D,C) = O_{A_0,C_0}(\sqrt{h\log(2h)}) .             \tag{2}
$$
The same conclusion holds when only these two ordinary endpoint heights are polynomial: their log ratio and hence $E$ are then $O_{A_0}(\log(2h))$. Bound the total correction by the stated simple-path estimate as before. Choosing any fixed finite prime set $S\supseteq\{2,3\}$ and a fixed positive integer $v$, [the uniform carry theorem (1)](../arithmetic/README.md) further gives, along **every** such macroscopic proper arc $n\ge ch$, $c>0$,
$$
   H_S\left(\frac{C}{\gcd(C,D^v)}\right)\ \ge\ 2^{n-o(h)}.         \tag{3}
$$
Indeed $\gcd(C,D^v)\le\gcd(C,D)^v$, the original start has polynomial size, and the onset in the one-window bound is uniform in that start. Formula (3) removes the overlap up to the multiplicities present in $D^v$; primes occurring in both numbers can remain with higher multiplicity in the quotient.

For a **rational** candidate with polynomial real phase heights, the numerator cost is instead $M=O(\log d+\log(2h))$. On the near-critical bounded clocks of PR195, $h\log2-p\log3=O(1)$; this equals the full sum of positive log corrections on the rational cycle and bounds every partial sum. The same subtraction gives $E=O_{C_0}(1)$ without invoking ordinary simple-path sparsity for rational phases. Since $d\le D<2^h$, optimizing (1) gives
$$
 \log\gcd(D,C) \ll_{A_0,C_0}
 \log d+\log(2h)+\sqrt{h(\log d+\log(2h))}.
$$
In particular a single proper arc whose carry shares $\exp(\eta h)$ with $D$, for fixed $\eta>0$, forces $d\ge\exp(c_\eta h)$ at large $h$, with other constants fixed. One can compute this test from the word. No bounded-degree factor of the complete rank polynomial has to be exhibited.

## Where the all-cuts argument stops

For the complementary arc with carry $C'$ the exact full-lap equation at the first phase is
$$
              3^{p-k}C+2^n C'=(A/d)D .
$$
In an ordinary cycle the right side is zero modulo $D$; both multipliers on the left are units there. In fact $\gcd(C,D)=\gcd(C',D)$ in that case. Thus the small gcd for each proper part does not upper-bound the gcd of the **sum**. All choices of cuts in one full cyclic word are coupled by the affine equations. If the full carry is zero modulo $D$ at one cut then so are all cyclically rotated full carries, since the clock multipliers are units modulo $D$. Applying PR195's resultant bound to low-degree factors of the full polynomial does not constrain this additive cancellation at the high-degree factors. Conversely the large mass in (3) can lie in both complementary carries and disappear in their weighted sum modulo $D$.

A genuine rational example separates these facts. The odd phases $5/7$ and $11/7$ have successive exact division exponents $1,3$. Traverse the two-phase cycle $t$ times. Then $(h,p)=(4t,2t)$, $D_t=16^t-9^t$, and the full carry from $5/7$ is $5D_t/7$, cancelling $D_t/7$ exactly in the gcd. In every arc between distinct odd phases, $k-n/2$ is $1/2$ or $-1/2$, and $A,B$ are $5,11$ in one order. Bound (1) gives $\log\gcd(D_t,C)=O(\sqrt h)$ simultaneously for all these arcs. The carries from either fixed start on long arcs also have $H_S(C)\ge2^{n-o(n)}$: the one-window two-coordinate proof uses only positivity and the integrality of the endpoint at two, and clearing the fixed denominator seven changes its height bound and local factors by at most a constant. Equivalently take the two coordinates $(A,7C/3^k)$, whose sum has dyadic size at most $2^{-n}$ by the integer numerator endpoint, and repeat the fixed-source line argument. This is a legal cycle of **reduced denominator seven**; the growing lap clocks repeat its primitive period and the density $1/2$ is not the near-critical density. It refutes an inference from the proper-arc gcd and mass bounds alone, not an inference that additionally proves an obstruction from coprime near-critical clocks.

## Physical positive words with large undilated factors

Here we test the opposite end of PR195's proposed bridge, on **primitive near-critical** clocks. Take coprime $h,p$ with $0<h-p\log_2 3=O(1/p)$, put $d_0=h-p$ and $r_i=ih\bmod p$. Set one octave bit $j_R=1$ at a chosen nonzero rank $R$ and all others to zero. Prescribe the chronological odd exponents
$$
  a_i=\left\lfloor\frac{r_i+h}{p}\right\rfloor+j_{r_i}-j_{r_{i+1}} .
$$
For $R=\lfloor p/4\rfloor$ and all sufficiently large clocks, the entering edge wraps since $R<d_0$, and the departing edge does not wrap since $R<p-d_0$. Thus the modification interchanges adjacent exponents 2 and 1 and all gaps are 1 or 2. For odd $p$ and center $R=(p-1)/2$, the entrance and exit both wrap: the incoming exponent becomes 1 and the outgoing becomes 3. These center words are legitimate in the full positive rational cycle problem, outside the all-1-or-2 bounded branch. Every prescribed gap is realized at the rational affine fixed point: at each odd cut both its numerator and $D$ are odd, and the rotated affine identities give its indicated valuation. The fixed point is positive since $D>0$, and a repetition count would have to divide both $p,h$. The labels here are an algebraically specified rank construction; no least-disagreement or ancestor optimality is claimed.

The quarter construction may use every sufficiently late upper convergent. For arbitrarily large primitive upper approximants with $p$ odd, use an upper convergent if its denominator is odd. Otherwise subtract its preceding lower convergent from twice the upper convergent, in numerator and denominator. The new denominator is odd and comparable to the upper one, the determinant with the upper pair is $\pm1$, and its signed clock discrepancy is positive and $O(1/p)$ by the two consecutive convergent errors. This supplies the claimed center family without assuming a parity pattern among convergents.

Put $s=p-1-R$ and
$$
             Q(X)=2(1+X+\cdots+X^{p-1})-X^s .
$$
Up to the content 2, this is the polynomial with the PR195 coefficients $2^{2-j_r}$ presented in reverse rank order. To check the numerical divisor directly, let $u$ be the unit modulo $D$ with $u^p=2,u^h=3$, obtained using $\gcd(p,h)=1$. Write $A_i=\sum_{\nu<i}a_\nu=\lfloor ih/p\rfloor-j_{r_i}$. The chronological full carry at the zero rank is $\sum_{i<p}3^{p-1-i}2^{A_i}$. Multiplying it by 2 and substituting $2^{\lfloor ih/p\rfloor}=u^{ih-r_i}$ gives a fixed unit times $Q(u)$, since the ranks run over all residues. Therefore its reduced denominator is exactly $D/\gcd(D,Q(u))$.

Each rational irreducible factor of $Q$ has degree at least $\min(s,p-1-s)$, and there are at most two factors with multiplicity. To see this, reduce a primitive integral factorization modulo 2: $Q\bmod2=X^s$. Every factor therefore reduces to a nonzero monomial. No positive-degree factor can have both leading and constant coefficients odd, since both corresponding terms would survive. The leading and constant coefficients of $Q$ are each 2, so each can supply an even coefficient to only one occurrence. In a nontrivial factorization there must consequently be exactly two occurrences. The factor with odd leading coefficient reduces to a monomial of its full degree, the other to a nonzero constant. The first degree is $s$, the second $p-1-s$. No cyclotomic polynomial is a factor since its endpoints have absolute value one.

All factors are undilated. Suppose a nonconstant $H(X^t)$ divided $Q$ with $t>1$. Its nonzero root $\alpha$ comes with every $\zeta\alpha$, $\zeta^t=1$. The four nonzero terms of
$$
           (X-1)Q(X)=2X^p-X^{s+1}+X^s-2
$$
therefore cancel separately in each exponent class modulo $t$, by orthogonality on the $t$-th roots of unity. No singleton class is possible, and $s,s+1$ are distinct modulo $t$. The pairs $(0,s),(p,s+1)$ would require $|\alpha|^s=2$ and $|\alpha|^{p-s-1}=1/2$. The pairs $(0,s+1),(p,s)$ would require $|\alpha|^{s+1}=2$ and $|\alpha|^{p-s}=1/2$. Both are impossible. This proves the claim for the displayed orientation of the polynomial.

In fact **$Q$ is irreducible at every interior rank**, including the quarter family with only gaps 1 and 2. Each of the only two possible nonconstant factors would have a leading or constant coefficient of absolute value 2. The multiplicative Mahler measure of each would therefore be at least 2, by its root formula or reversal. But Jensen's inequality and Parseval give
$$
 M(Q)=M((X-1)Q)\le \|(X-1)Q\|_2=\sqrt{2^2+1+1+2^2}=\sqrt{10}<4.
$$
The four exponents here are distinct. Multiplicativity excludes the factorization.

Nevertheless on both families
$$
                       \log\gcd(D,Q(u))=O(\sqrt p).                  \tag{4}
$$
Put $g=\gcd(D,Q(u))$. In $\mathbb Z/g$, multiplication by $u-1$ gives $(u-1)u^s=2$, since $u^p=2$. In the quarter case $4s=3p+c-4$ with $c=p\bmod4$, so the unit $u$ satisfies $(u-1)^4=2u^{4-c}$. At the center $2s=p-1$ instead gives $(u-1)^2=2u$. In either case there is a polynomial $H$ from a fixed finite list, of degree at most four, with constant and leading coefficients prime to 3.

Use Dirichlet with $J=\lfloor\sqrt p\rfloor$ to choose $1\le j\le J$ and $i,k$ such that $ip+jh+k=0$, $|k|\le p/J$, $|i|=O(\sqrt p)$. For large coprime clocks $k\ne0$. Clearing negative powers in $2^i3^jX^k-1$ produces an integer binomial $P$ vanishing at $u$ modulo $g$, of degree $O(\sqrt p)$ and coefficient absolute sum $\exp(O(\sqrt p))$. Its reduction modulo 3 is one nonzero monomial because $j>0$. Any primitive integral nonconstant divisor of $H$ has both endpoints prime to 3 and its reduction preserves its degree and nonzero constant. Thus $H$ and $P$ have no common complex root. Their nonzero integer resultant is divisible by $g$, via the integral Bézout identity for the resultant evaluated at the modular root. Its absolute value is at most $\|P\|_1^{\deg H} M(H)^{\deg P}$ by the complex product formula for resultants, with $M$ the multiplicative Mahler measure. This gives (4) uniformly over the finite list. The usual two-log lower bound at these clocks yields $\log D=p\log 3+O(\log p)$, so the reduced denominators have full leading exponential size.

These legal examples distinguish the two assertions at large compressed degree: the presence of such factors and the divisibility of their evaluation by most of $D$. The quarter family has only one elevated rank, so it is not a control for the positive-density occupation or all-rank mismatch conditions on a purported bounded ordinary counterexample. The center family also has a 3-gap. Neither purports to satisfy ordinary realization. [A second proof](SINGLE_RANK_RESULTANT.md) treats an arbitrary moving single rank, independently of its rational position. Both subexponential gcd arguments use the special one-site perturbation; for general physically legal masks $(u-1)Q(u)$ has many terms. No fixed-degree auxiliary polynomial $H$ for those masks has been obtained. That is the first unsupported step in this proposed use of the resultant, and the partial-arc bound (2) does not supply it.
