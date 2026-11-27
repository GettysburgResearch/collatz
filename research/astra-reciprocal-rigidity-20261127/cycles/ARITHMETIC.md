# Complete denominators, translated products, and ordinary path controls

**Status.** The two-shift obstruction and finite endpoint reconstruction are Lean-checked. A larger obstruction at three shifts has an exact integer valuation certificate. The stated two-run construction has a written elementary proof. All three questions concern ordinary finite paths or positive rational cycles of the shortcut map, as specified separately.

## What every translated product knows

For a finite union of ordinary accelerated paths, discard their interior states in the flow balance. Suppose their remaining initial and final multisets are $A$ and $B$ of equal cardinality $r$, with multiplicities. Define
$$P_A(t)=\prod_{a\in A}(t+a),\qquad P_B(t)=\prod_{b\in B}(t+b).$$
A genuine cycle has $A=B$ and all shifted products agree. Conversely, agreement at $r$ distinct integer shifts suffices for $A=B$: the difference of these two monic degree-$r$ polynomials has degree at most $r-1$ unless zero. The polynomial identity recovers every root with multiplicity. For $r=0$ both multisets are empty. This degree counts open path endpoints after cancellation and can be much smaller than the edge count. The theorem recover_endpoints in [ShiftBalance.lean](ShiftBalance.lean) works over multisets of signed integer roots. Use roots $-a$ and $-b$ for the displayed convention.

PR178 identified a finite exact prime-balance control for an arbitrary completely additive potential on the ordinary odd map. Adding a second independent prime weight at a translated coordinate does not repair global strict descent. The following three positive ordinary paths, all states at least seven, have complete odd exponents certified in Lean.

| Initial | Remaining successive odd states |
|---:|---|
| 7 | 11 |
| 65 | 49, 37, 7, 11, 17, 13 |
| 55 | 83, 125, 47, 71, 107, 161, 121, 91, 137, 103, 155, 233, 175 |

The exact endpoint defect polynomial is
$$
(t+7)(t+55)(t+65)-(t+11)(t+13)(t+175)=-72t(t-1).
$$
At shifts zero and one the respective common products are 25,025 and 29,568. At shift two the defect is $-144$. This is a minimal number of open paths for two distinct evaluations, by the reconstruction theorem. It rules out strict decrease on every such genuine edge of any potential $F(n)+G(n+1)$ for arbitrary, independently chosen real-valued completely additive functions $F,G$. Telescoping the strict inequalities along the three paths would contradict the two product equalities. The same calculation implies that if all the edge changes in the certificate are nonpositive, they must all vanish. It makes no assertion for unbounded floors.

The three-shift certificate [three_shifts.tsv](three_shifts.tsv) gives 248 distinct ordinary accelerated edges with positive integer multiplicities, of total mass 944,819,606,987,064. All states are at least five. At each $t=0,1,2$, and every prime $p$, the weighted difference of valuations $v_p(x+t)-v_p(U(x)+t)$ sums to zero. There are 205 distinct vertices with nonzero state-flow balance. At $t=3$, prime 2 gives the signed difference $-127991939519124$. Thus even three independently chosen completely additive functions at the three consecutive translates cannot strictly decrease on all ordinary edges in this domain. The standard-library verifier factors every individual positive state and its three translates, checks the physical transitions and all positive weights, and sums exactly. Floating-point linear programming was used only to locate a possible support, followed by an exact integer nullspace and full verification. The certificate proves nothing for an arbitrary fourth translate, arbitrarily high floors, or a different family of functions.

Taken over arbitrarily many shifts, the evaluation criterion recovers actual state closure. This identifies the gap in using a few prime-product balances as a full-cycle criterion: an all-shift identity is equivalent to the very permutation of ordinary states one needs to establish.

## Shifted reciprocal balances on a true cycle

For a positive shortcut cycle of length $L$ and odd count $s$ put $E$ and $O$ for its even and odd physical phase multisets. Since the actual states permute under the map, for every real $t\ge0$,
$$
\frac{2^L}{3^s}=
  \prod_{e\in E}\frac{e+2t}{e+t}\,
  \prod_{o\in O}\frac{o+(1+2t)/3}{o+t}.
$$
The same proof works for positive rational cycles with their actual parity coding. At $t=0$ and $t=1$ this yields the dual products
$$
\prod_{o\in O}(1+1/(3o))=2^L/3^s=\prod_{e\in E}(1+1/(e+1)).
$$
The derivative of the logarithm at zero yields
$$
\sum_{e\in E}1/e=\sum_{o\in O}(o+1)/(o(3o+1)).
$$
These exact finite identities retain cross-parity information but also hold for nonordinary positive rational cycles. The identity for a variable $t$, cleared of denominators, records permutation of the entire phase multiset.

## Prescribed prime powers really dividing the lap determinant

Let $Q\ge1$ be any integer coprime to six, let $\mathcal P$ be a finite set of primes at least five containing its prime divisors, and fix a bounded open real interval $I\subset(0,\infty)$ with positive length. There are primitive positive rational shortcut cycles of form $1^s0^z$, with arbitrarily large $s$, satisfying **all** of the following.

* The minimum lies in $I$.
* $Q$ divides the unreduced lap determinant $D=2^{s+z}-3^s$ and every rotated affine numerator.
* No prime in $\mathcal P$ divides the reduced denominator $d$ of any phase. This includes every exponent actually occurring in $D$ at those primes.
* The reduced denominator grows at least as $2^s/(1+\sup I)$.

Indeed, for the origin at the first one let $C_s=3^s-2^s$. The minimum and full cancellation are
$$
x=C_s/D,\qquad \gcd(C_s,D)=\gcd(C_s,2^z-1).
$$
The gcd follows by adding $C_s$ to $D$, obtaining $2^s(2^z-1)$, and using oddness. The affine solution has $x+1=2^s(2^z-1)/D$. In lowest terms $x=n/d$, the denominator $d$ is odd and $2^s\mid n+d$, hence $d(x+1)\ge2^s$. Exact parity follows at all rotations by the periodic affine cylinder or by iterating the $s$ odd steps from $x+1$ and then the $z$ halvings. The initial odd run increases the real coordinate and the halving run decreases it back to $x$, making $x$ the minimum. There is just one cyclic change from zero to one, so the word is primitive when $s,z>0$.

Choose $h\ge1$ with $2^h\equiv3^h\equiv1$ modulo $Q\prod_{p\in\mathcal P}p$ (when this modulus is one, $h=1$ works). For each $p\in\mathcal P$ put $e_p=v_p(C_h)$ and set $M=\prod_{p\in\mathcal P}p^{e_p+1}$. Choose $k$ divisible by the orders of both 2 and 3 modulo $M$; take $k=1$ when $M=1$. Take $s=h+ku$ and $z=kv$, with $u,v$ positive integers. Then $C_s\equiv C_h\pmod M$, $2^z\equiv1\pmod M$ and $D\equiv-C_h\pmod M$. Consequently $v_p(C_s)=v_p(D)=e_p$ for every selected prime, and $Q\mid\gcd(D,C_s)$. The recurrence $2C_{\rm next}=3^{w_0}C_{\rm current}+w_0D$ and invertibility of 2 and 3 modulo $D$ preserve the entire gcd at every rotation.

Write $\alpha=\log_2(3/2)$ and $\delta=z-s\alpha$. Then
$$
x=\frac{1-(2/3)^s}{2^\delta-1}.
$$
Choose a positive real $\delta_0$ with $1/(2^{\delta_0}-1)$ interior to $I$. By irrationality of $\alpha$, the fractional parts of $u\alpha+h\alpha/k$ visit every circle interval infinitely often. Choosing the integer $v$ gives a sequence $\delta\to\delta_0$, with $u,v\to\infty$. Thus $D>0$ and eventually $x\in I$. The integer-grid bound forces $d\to\infty$.

PR200 already gives much stronger adelic approximation and rough-denominator constructions in other rational families. Here the prescribed prime powers divide the **unreduced** determinant and are genuinely cancelled throughout; avoiding those primes in $D$ would give a weaker proper-factor test. No all-word prime upper bound or ordinary cycle follows.
