# A positive small cycle expression with vanishing dyadic and ternary contractions

**PROPOSED written theorem.** Use the rationalized symbol boundary and the real Rogers function of [P5](PELL.md) and [U5–U7](LOCAL_UNITS.md). All algebraic quantities lie in one finite totally real multiquadratic field. On a complete ordinary odd cycle let $m$ be its length, $N$ its least state, $a_i=v_2(3x_i+1)$, $A=\sum a_i$, $q_i=3/2^{a_i}$, $X_i=E_{x_i}^{-1}$, $Y_i=X_{i+1}$ and $s_i^2=X_iY_i/q_i$. Assume the states are distinct when using the bound in terms of $N$ independent of the period. The local computations also apply to repeated traversals.

## R1. A two-place correction with bounded coefficient denominator

Start with P5's positive expression
$$C=\sum_i(\tfrac12\{X_i^2\}+\tfrac12\{s_i^2\}-\{-X_iY_i\}).$$
Put
$$R=\prod_i\frac{Y_i}{q_i(1-s_i^2)},\quad H=1+R^6+R^{12},\quad
S=\prod_i (E_{x_i}(1-s_i^2))^{a_i},\quad z=(S H^A)^{-1}.$$
Define
$$\Psi_3(R)=\tfrac16\{R^6\}-\tfrac1{18}\{R^{18}\},\qquad
\Psi_2(z)=\tfrac1{24}\{z^{24}\}-\tfrac1{48}\{z^{48}\},\qquad
C^*=C-\tfrac12\Psi_3(R)+\tfrac12\Psi_2(z).$$

Then **all** contractions of $\partial C^*$ at finite places above 2 or 3 vanish. Its raw real Rogers value is strictly positive. For a simple cycle this value is $O(\log(2N)/N)$ with an absolute constant. Its coefficients have common denominator **288**, independent of the cycle and of the field degree.

Write square brackets for additive vectors in the rationalized multiplicative group. The two correction boundaries simplify without any analytic input:
$$\partial\Psi_3(R)=-[R]\wedge[H],\qquad
\partial\Psi_2(z)=-[z]\wedge[1+z^{24}].$$

At every ternary place, U6 gives $2\iota_3\partial C=[R]$. All $X_i,Y_i$ reduce to one there. Since $q_i(1-s_i^2)=q_i-X_iY_i$, the residue of $R$ is $(-1)^m$. The ramification index in a multiquadratic completion over three is at most two: adjoining square roots of units gives at most the unramified quadratic extension, and one square root of a uniformizer suffices afterwards. Hence $v_3(R^2-1)\ge1/2$ unless the difference is zero, and cubing gives $v_3(R^6-1)\ge3/2$. From $H=3+3(R^6-1)+(R^6-1)^2$ one obtains $v_3(H)=1$. Therefore $\iota_3\partial\Psi_3=[R]$, which clears every ternary contraction at once.

At every dyadic place $v_2(1-X_i^2)=2+a_i/2$: its factors $1-X_i$ and $1+X_i$ have valuations one and $1+a_i/2$. Also $v_2(s_i^2)=a_i$ and $v_2(1+X_iY_i)=1$ since $X_i$ and $Y_i$ differ from $-1$ by elements of valuation greater than one. Direct contraction gives
$$2\iota_2\partial C_i=-(2+a_i)[X_i]+2[Y_i]+a_i[1-s_i^2].$$
Summation yields $2\iota_2\partial C=[S]$. Moreover $v_2(R)=A$, $v_2(H)=v_2(S)=0$, while $v_3(S)=-A$. It follows that $z$ is a unit at every place above 2 and 3, and the remaining dyadic contraction of $2C-\Psi_3$ is $[S H^A]=-[z]$.

A multiquadratic completion at two has residue degree at most two and ramification index at most four: the squareclass group of the dyadic rationals has order eight (odd unit modulo eight and uniformizer parity), and its elementary unramified quotient has degree at most two. If the local compositum has degree eight it contains the unramified quadratic extension. Hence $z^3$ reduces to one, with $v_2(z^3-1)\ge1/4$; three successive squarings give $v_2(z^{24}-1)>1$. Thus $v_2(1+z^{24})=1$ and $\iota_2\partial\Psi_2=[z]$. At three the residue degree is at most two; since $8\mid24$, one has $z^{24}\equiv1$ and $v_3(1+z^{24})=0$. This leaves the ternary cancellation intact.

For positivity, U6 gives $0<R<(8N)^{-m}$. Also $0<z<(10N)^{-m}$ since $E_{x_i}>12N$, $1-s_i^2>8/9$, $H>1$ and $A\ge m$. At a state attaining $N$, $X_i>1/(14N)$; hence $L(C)>1/(392N^2)$ since $L(t)\ge t$ for $0<t<1$. On $0<t\le1/2$ the Taylor series give $L(t)\le3\sqrt t$: use $\mathrm{Li}_2(t)\le2t$, $-\log(1-t)\le2t$ and $-t\log t\le(2/e)\sqrt t$. The ternary subtraction costs at most $L(R^6)/12\le R^3/4<1/(2048N^2)$. The dyadic addition is positive by monotonicity and is bounded above by $L(z^{24})/48$. These bounds prove both claims about the real value.

At places outside three where $R$ is a unit and $H$ is not a unit, its reduction has order 9 or 18 because $R^6$ is a primitive cube root. The rational prime is therefore congruent to $\pm1\pmod9$: the residue degree is at most two in an elementary abelian two-extension. New finite factors can occur even when the two chosen contractions vanish exactly.

## R2. A clock-supported alternative

Another positive, square-small cycle expression is $Z=-\sum_i(\{-s_i\}+\{v_i\})$, with $v_i=q_i s_i$. P5 gives real value $\frac12\sum L(X_i^2)-\sum L(-X_iY_i)>0$. All arguments and complements are units outside primes over 2, 3 and the clock integers $K_i=2^{a_i}+3$. The equality $1+s=(1-v)/\theta$ and U2 establish the complement claim. On a cycle the product of these clock integers is at most $10^m$ because $K_i\le(5/2)2^{a_i}$ and $2^A=\prod(3+1/x_i)\le4^m$.

With the U5 notation $E=[E_x],Y=[E_y^{-1}],Q=[q],P=[1+q],B=[\beta]$, one edge has
$$-2\partial Z_i=(Y-E)\wedge(P+B)+Q\wedge Y.$$
For a normalized valuation over $p\ge5$ this gives $2\iota_p\partial Z_i=(v(P)+v(B))(Y-E)$. The coefficient is nonnegative since $(1+q)\beta=(1-v)^2/Y_i$ is integral away from 2 and 3. It vanishes away from the clock primes. Every nontrivial cycle has a growth edge with nontrivial third field, by A6. At such an edge $p=5$ divides its clock integer; some place above five satisfies $v(P)+v(B)>0$, since conjugate valuations of $\beta$ are opposite. All other terms there have nonpositive real logarithm. Thus $Z$ cannot be boundary-free on that cycle. Its full Galois average on a nondegenerate edge loses the varying real correction, since $-s$ is the reciprocal of a conjugate of $v$ and the Rogers sum on a pair of reciprocal arguments is constant on each sign branch.

## R3. An exact surviving defect and a positive Galois projection

On the actual cycle $x=y=1$, take $q=3/4$ and $X=7-4\sqrt3$. Seven is inert in $\mathbb Q(\sqrt3)$. The identity $X^2-14X+1=0$ shows that $1+X^2=14X$ has valuation one and $q-X^2=7(1-8X)/4$ also has valuation one: the residue of $X$ squares to $-1$ and so is not one. Writing $J=1+z^{24}$, the respective valuations of $(R,S,H,z,J)$ at seven are $(-1,2,-12,22,0)$. Also $v_7(1-X^2)=0$. Direct substitution into the R1 symbol gives
$$2\iota_7\partial C^*=[qX^2 R^{12}/(H J^{22})].$$
The distinguished real value inside the brackets is strictly between zero and one. This is an explicit remaining finite defect on a genuine integral cycle after exact cancellation at all places over 2 and 3.

Let $\tau$ be the nontrivial inertia element above three in the multiquadratic field. Every ordinary odd cycle state is a ternary unit. Inertia fixes square roots of ternary units and negates a square root of three. It follows that the **same** involution sends every $U_{x_i}$ to its inverse, every $v_i$ to $-1/s_i$, and every $s_i$ to $-1/v_i$. It fixes all third-field $\beta_i$, whose labels are sums of two ternary-ramified squareclasses. In particular even the two-element average of the R2 expression removes its variation, because $L(Z_i)+L(\tau Z_i)=-c$ at every edge, with $c=\pi^2/6$.

The R1 expression behaves differently. For any simple ordinary cycle with $N\ge2$ the **centered inertia sum**
$$L(C^*)+L(\tau C^*)-3mc$$
is strictly positive and is $O(\log(2N)/N)$. Its symbol boundary is inertia-invariant and all its contractions at places over 2 and 3 vanish. The centering constant is Rogers torsion (or one may work modulo $c$).

Indeed on the standard real branch $L(t)+L(1/t)=2c$ for positive $t$ and $-c$ for negative $t$. Thus
$$L(C_i)+L(\tau C_i)-3c=\tfrac12(L(s_i^2)-L(v_i^2)).$$
On the cycle $s_i>Y_i$ and $v_i<X_i$. By adding and subtracting the telescoping sum of $L(X_i^2)$ and $L(Y_i^2)$, all resulting differences are positive. At a minimum state, one of these differences is at least $X_i^2(1-\theta_i^2)$, since $L'(t)\ge1$ for $0<t<1$ (the derivative of the defining integral, or $-\log(1-t)\ge t$ and $-\log t\ge1-t$). Here $X_i>1/(14N)$ and $1-\theta_i>Y_i>1/(28N)$, using $y_i\le2N$. The centered sum before the global corrections exceeds $1/(10976N^3)$.

The conjugate corrections remain small as well:
$$|\tau R|=\prod_i X_i/(1-v_i^2)<(11N)^{-m},\qquad
|\tau S|=\prod_i (E_{x_{i+1}}(1-v_i^2)/q_i)^{a_i}>(7N)^m.$$
Consequently $|\tau z|<(7N)^{-m}$. For $t\le1/2$, the same Taylor estimate as R1 gives $L(t)\le4t^{2/3}$ since $-t\log t\le(3/e)t^{2/3}$. The two ternary subtractions together are at most $(8^{-4}+11^{-4})/(3N^4)<1/(10976N^3)$ for $N\ge2$. The dyadic additions are positive since only even powers occur. Summing the original upper bounds for the positive $L(s_i^2)$, plus the exponentially small corrections, proves the claimed upper estimate.

## R4. Full Galois averaging does not preserve that sign on rational controls

There are exact positive rational cycles of arbitrarily large minimum and wide real spacing on which the centered **full** Galois mean of $C^*$ has either sign. This tests sign arguments based on real sizes and clock statistics; it makes no assertion that the rational states are ordinary integers.

Fix $B=2$ or $3$. Take a sequence of reduced rationals $b/m$ above $(\log_2 3-1)/(B-1)$ with $m$ odd and $\delta=m+(B-1)b-m\log_2 3\longrightarrow0^+$. Such approximants exist by density of the irrational rotation along odd denominators, followed by reduction (which preserves oddness and divides the error by the gcd). Take clocks
$$a_i=1+(B-1)(\lfloor(i+1)b/m\rfloor-\lfloor ib/m\rfloor).$$
Their partial clock discrepancy is bounded by $B-1$, so the P6 affine construction gives real states between positive constant multiples of $m/\delta$, all with exact prescribed dyadic clocks. The rotation numerators over $D=2^{m+(B-1)b}-3^m$ jump in phase order by $(2^{B-1}-1)2^u3^v$, with the underlying $2^u3^v$ bounded below by a fixed multiple of $3^m$. Since $2^{B-1}-1$ is one or three and $D$ is prime to six, all state numerators are coprime to $D$: any common divisor of one and $D$ divides every rotated numerator by the recurrence and hence every phase jump. Also $D\equiv5\pmod8$ for all large odd $m$.

On each growth edge the first numerator is $3\pmod4$. Equality of the two adjacent Pell fields would force the first and third ordinary numerators to have the same squareclass and their two-clock sum to be even, by the U2 label. Their gcd divides five on a growth edge by the exact two-clock relation and coprimality to $D$. A numerator $3\pmod4$ has a prime $3\pmod4$ to odd order, ruling this out. On each clock-two edge the first rational state is $1\pmod8$, so its numerator is $5\pmod8$. Here the first/third numerator gcd divides seven. Neither a square nor seven times a square is $5\pmod8$, ruling out equal Pell fields there as well. Thus all edges are nondegenerate for $B=2$, and all growth edges are nondegenerate for $B=3$. Every individual quadratic field is nontrivial since its discriminant squareclass has odd ternary valuation.

For distinct adjacent fields, summing the four conjugate contributions gives
$$\sum_\sigma L(\sigma C_i)-6c
=\tfrac12\{L(s_i^2)-L(v_i^2)+L((\theta_i/q_i)^2)-L(\theta_i^2)\},$$
where braces group real numbers. This follows by applying the positive and negative reciprocal identities. In the limit the centered **mean** contribution tends uniformly to $f(a_i)/8$, where $f(a)=L((2^a/3)^2)-c$. For a coincident pair its two conjugates give centered mean tending to zero by R3. The four global R1 correction terms have total bounded real value in every embedding: all their arguments are positive even powers and $0<L(t)<2c$ for every real $t>0$. Their contribution divided by $m$ tends to zero even if some conjugate argument is large.

One has $-.901<f(1)<-.898$, $.734<f(2)<.737$ and $f(3)<c<1.65$. The frequency of clocks $B$ tends to $(\log_2 3-1)/(B-1)$, with $1.58<\log_2 3<1.59$. The resulting centered mean per edge is strictly positive for $B=2$, strictly negative for $B=3$, even allowing all non-growth edges in the latter family their maximal positive contribution. The stated numeric enclosures can be certified by the positive power series for $\mathrm{Li}_2(t)$ and $-\log(1-t)$ at $t=4/9,9/16,1/2$ and their complementary arguments, with $c=2L(1/2)$.

The common inertia involution in R3 therefore has a sign property that full symmetrization does not share on these controls. Extending the positive, two-place-cleared expression to a torsion class for *ordinary* integer states still requires control of other finite places and of the exterior square of global units. Full Galois averaging kills the latter invariant component by the multiplicity-one character decomposition of the totally real unit group, but the two families above demonstrate the missing sign condition under that operation.
