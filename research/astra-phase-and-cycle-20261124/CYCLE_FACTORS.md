# Residual cycle denominator growth on the full parity clock

**Status: PROPOSED written deductions.** The degree and size statements concern polynomial cancellation before integer evaluation. An explicitly computed reduced rational cycle denominator appears in the controls below. No unconditional exclusion of nontrivial integer cycles or escaping trajectories follows.

**Sources.** Use the shortcut map, with a binary 1 for an odd input. [PR185, degree proof](https://github.com/GettysburgResearch/collatz/blob/2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d/research/central-closure-20261123/PRIMITIVE_RESIDUAL_DEGREE.md) gives principal survival and the projected-order lcm. [Its denominator growth proof](https://github.com/GettysburgResearch/collatz/blob/2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d/research/central-closure-20261123/PRIMITIVE_DENOMINATOR_GROWTH.md) gives coefficient support and the source-qualified numerical gap via a linear-forms estimate and continued fractions. [PR191, TCP-4](https://github.com/GettysburgResearch/collatz/blob/37b3916633cd32a0c173b20bb18ec3a7ec290a63/research/two-sided-cycle-packing-20261124/README.md) identifies a component norm's vanishing with a common complex root and bounds the evaluation gcd. All claims below use one specified word. These written results do not carry a Lean kernel receipt.

## 1. Count how many roots each surviving order costs

Let a primitive length-$A$ binary word have $p\ge1$ ones at positions $0\le d_0<\cdots<d_{p-1}<A$. Primitivity means that the word has no proper cyclic period. Put
\[
g=\gcd(A,p),\quad a=A/g,\quad b=p/g,\quad e=\gcd(b,2),\quad t=b/e,
\qquad F=X^p-2^A,\quad Q=\sum_i2^{d_i}X^{p-1-i}.
\]
Let $G$ be the monic gcd in $\mathbb Q[X]$, set $F_0=F/G$, $n=\deg F_0$. For roots $\alpha$ of $F_0$, let $\mathcal H$ be the set of orders of $\eta=\alpha^b/2^a$. Each image is a $g$th root of unity. **For arbitrary signs of the real cycle denominator,**
\[
 n\ \ge\ b+t\sum_{h\in\mathcal H,\ h>1}\varphi(h),\qquad
 \sum_{q\parallel g}\varphi(q)\ \le\ 1+(n-b)/t.
\tag{1}
\]
Here and below $q\parallel g$ runs once over the maximal powers of the distinct primes dividing $g$.

For completeness, the coefficient-support input has a short proof. Every root of any monic rational factor $P\mid F$ has modulus $r=2^{a/b}$. Gauss's lemma gives integral coefficients. Its constant coefficient has modulus $r^{\deg P}$, so $b\mid\deg P$. The root pairing $\alpha\mapsto r^2/\alpha=\bar\alpha$ gives $X^{\deg P}P(r^2/X)=P(0)P(X)$. Comparing symmetric nonzero coefficients yields $b\mid2i$ for each occurring power $X^i$. Therefore $P\in\mathbb Q[X^t]$. Apply this to $F_0$. For each root $\alpha$, multiplying by each $t$th root of unity keeps a root of $F_0$ and preserves $\eta$. Each surviving image contributes at least $t$ distinct roots. Rationality gives every conjugate image of each represented order. The entire principal fibre contributes $b$ roots by PR185 (the irreducible $X^b-2^a$ survives since $Q(r)>0$). This proves the first inequality.

The lcm of $\mathcal H$ equals $g$ by PR185, Section 4, using ordinary binary primitivity. Assign each maximal prime power $q\parallel g$ to a represented $h$ divisible by $q$. At each $h$, the product of the assigned totients divides $\varphi(h)$. For integers at least two their product is at least their sum whenever there are two or more, with equality allowed; for a singleton use its value. The only possible assigned totient equal to one comes from $q=2$, and occurs at most once across the full assignment. Thus $\sum_{q\parallel g}\varphi(q)\le1+\sum_{h>1}\varphi(h)$. If $g$ is odd the additive one may be omitted. This proves (1).

## 2. Uniform superpolynomial residual denominator

Write $S=\sum_{q\parallel g}\varphi(q)$ and let $m$ count its summands. By (1), $S\le n$. Sort the distinct prime bases increasingly. The $j$th base is at least $j+1$, and its totient contribution is at least $j$, so $m(m+1)/2\le S$. Also $q\le2\varphi(q)\le2n$, hence
\[
 \log p=\log b+\log g\le\log n+\sqrt{2n}\log(2n)\le3\sqrt n\log(2n).
\tag{2}
\]
This includes $g=1$. For $p\ge3$, splitting according as $n\ge(\log p)^2$ or $n<(\log p)^2$ gives the explicit bound
\[
 n\ \ge\ \left(\frac{\log p}{3\log(2(\log p)^2)}\right)^2.
\tag{3}
\]
Thus $n/\log p\to\infty$ uniformly over all primitive words as $p\to\infty$. The order counting from PR185 alone suffices for this asymptotic consequence; the fibre multiplicity in (1) improves its clock-sensitive bound.

Suppose now $2^A>3^p$ and exclude the trivial rotations 10 and 01. PR185's source-qualified bound $|F_0(3)|>(3/2)^{n-1}$ and (3) imply that **for every fixed real $K>0$, there is $p_K$ such that $|F_0(3)|>p^K$ for every such word with $p\ge p_K$**. This strengthens the fixed exponent of PR185. It does not improve the actual reduced denominator by itself.

## 3. Exactly when a prime-power top component survives whole

Let $g=\ell^k>1$ be a prime power. The lcm statement forces image order $g$ to occur. For any $h\mid g$ write
\[
 H_h(X)=(2^a)^{\varphi(h)}\Phi_h(X^b/2^a).
\]
The following splitting criterion also holds for arbitrary $h>1$, without the prime-power assumption on $g$.

* If $b$ is odd or $v_2(h)\ne2$, then $H_h$ is irreducible over the rationals.
* If $b$ is even and $v_2(h)=2$, then $H_h$ has exactly two irreducible factors of equal degree $b\varphi(h)/2$.

Here is an elementary fibre proof. Choose a primitive $h$th root $\eta$, let $K=\mathbb Q(\eta)$, and choose $\alpha^b=2^a\eta$. Each irreducible rational factor containing such a root projects onto all conjugates of $\eta$, and the support argument of Section 1 forces at least $t$ roots above each conjugate. For odd $b$, $t=b$ exhausts the fibre. For even $b$, a proper factor must have exactly $b/2$ roots in each fibre and comprise precisely one orbit under multiplication by the $(b/2)$th roots of unity there. Consequently $\alpha^{b/2}$ is fixed by every automorphism fixing $K$, so $2^a\eta$ is a square in $K$. Conversely, if it is a square, the binomial $X^b-2^a\eta$ splits over $K$ into factors of degree $b/2$. Since $K\subseteq\mathbb Q(\alpha)$, the tower law and the preceding fibre lower bound force degree exactly $b\varphi(h)/2$ over the rationals. There are exactly two factors as asserted.

It remains to test that square. For even $b$, coprimality gives odd $a$, so test $2\eta$. Write $h=2^s m$ with $m$ odd and separate the odd-order part of $\eta$ (a square in $K$). If $s=0,1$, then $K=\mathbb Q(\zeta_m)$ and the remaining number is $2$ or $-2$. Neither square root lies in $K$: the degree identity $\varphi(8m)=\varphi(8)\varphi(m)$ gives $K\cap\mathbb Q(\zeta_8)=\mathbb Q$, and both square roots lie in $\mathbb Q(\zeta_8)$. If $s=2$, the remaining number is $\pm2i=(1\pm i)^2$, a square. If $s\ge3$, then $\sqrt2\in K$ and a square root of the primitive even-order $\eta$ would generate the larger cyclotomic field of conductor $2h$, since $\varphi(2h)=2\varphi(h)$. This proves the criterion.

For prime-power $g$ outside the exceptional pair $g=4$, $b$ even, the whole $H_g$ survives, and TCP-4's $J_g$ is nonzero. In the positive cone this gives a distinguished integer factor of $|F_0(3)|$ with
\[
 H_g(3)=\frac{2^A-3^p}{2^{A/\ell}-3^{p/\ell}}>2^{A(1-1/\ell)}.
\tag{4}
\]
The strict inequality is the geometric sum with positive lower terms. For the exception $g=4$, $b$ even, the two factors are $X^b\pm 2^{(a+1)/2}X^{b/2}+2^a$. At least one survives. Each evaluates at 3 to at least $2^{a-1}$ by completing the square. Therefore an exponential-in-$A$ residual lower bound holds for every prime-power clock gcd greater than one, including this split case.

## 4. The distinguished integer fibre still cancels

A primitive control has $A=12,p=4$ and odd positions $(0,1,2,4)$. Here $Q=X^3+2X^2+4X+16$ and $H_4=X^2+64$. Its two roots survive yet $Q(3)=73=H_4(3)$. Its complete reduced denominator is $4015/73=55$. A closer-slope control has $A=20,p=12$, odd positions $(0,1,2,3,4,5,6,8,13,14,15,16)$. Here $Q(3)=1,053,553=601\cdot1753$ and $H_4(3)=1753$. The complete denominator before numerical cancellation is $2^{20}-3^{12}=295\cdot1753$ and the reduced denominator is 295. Both words have numerical top-factor absorption despite irreducible whole-top survival. The principal-factor absorption family in [PR185](https://github.com/GettysburgResearch/collatz/blob/2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d/research/central-closure-20261123/PRINCIPAL_FIBER_CONTROL.md) covers a different component.

The first missing implication is a simultaneous restriction on the integer evaluations. In the exact notation the missing cycle statement is
\[
 |F_0(3)|\nmid (Q/G)(3)
\]
for every primitive nontrivial positive candidate. TCP-4 bounds the gcd with each component by a norm. In the two top-absorption controls $H_4(3)\mid Q(3)$ forces $H_4(3)\mid J_4$ by TCP-4 itself, so even a demonstrably nonzero norm may provide no strict saving on an exponentially large projected component. Counting its complex roots does not choose a prime at the ordinary evaluation. The recurrence also has escaping branches, which no cycle-only arithmetic argument addresses.

### A simultaneous nonzero-norm obstruction at every component

There is a stronger test of that last route. Take the primitive word with $A=28,p=16$ and odd positions
$(0,2,3,4,5,8,9,10,11,12,14,16,17,18,19,22)$.
Here $g=4,a=7,b=4$. The polynomials $F,Q$ are coprime: **all sixteen roots survive**. The ordinary evaluation gives $Q(3)=120739927$, $2^{28}-3^{16}=225388735$, with gcd 209. The fixed rational state is $577703/1078415$. Its exact trajectory realizes the word and returns, as checked by the integer numerator recurrence in the companion replay. This is a rational cycle.

Choose the PR191 discrepancy-minimizing rotation with positions
$(0,3,9,11,12,13,14,17,18,19,20,21,23,25,26,27)$. Use $u=2,v=1$, so $bu-av=1$. The full TCP-4 computation gives

| Component $h$ | $D_h$ | Signed norm $J_h$ | $\gcd(D_h,J_h)$ |
|---|---:|---:|---:|
| 1 | 47 | 2157911 | 47 |
| 2 | 209 | 9937323 | 209 |
| 4 | 22945 | 87054402105125 | 22945 |

Thus **every norm is nonzero and every entire component divides its norm**. The lower bound for the complete reduced denominator from TCP-4 equation (8) is exactly one, while the actual reduced denominator exceeds one million. This refutes a universal strict saving from these norms even after enforcing primitivity, positivity and complete polynomial survival. It leaves open methods that resolve the distinguished evaluation inside a component instead of taking the determinant across all its conjugates.

The obstruction persists after imposing the ordinary nontrivial-cycle floor above one. Keep the same clocks and use odd positions $(0,1,4,6,7,10,12,13,14,15,16,17,18,22,23,24)$. The fixed rational state is $174449/82955$ and the minimum of **all** 28 cyclic states is $88181/82955>1$. The polynomial gcd is one. At the prescribed minimum-discrepancy rotation, the three norms are respectively $-29281$, $411939$ and $16950045125$, divisible by $47$, $209$ and $22945$. This example proves the floor above one; it does not meet a stronger floor of $19/10$.

For independent reconstruction, on these two specific examples $T^4=2W$. The three rational algebras use respectively $T^4=2$, $T^4=-2$, $T^8=-4$, always with $W=T^4/2$. In each, take the determinant of multiplication by
\[
 (T-1)\sum_{i=0}^{15}T^{4d_i-7i}W^{2i-d_i}.
\]
The companion script reduces powers with these binomial equations and uses rational Gaussian elimination. This computes the same determinant in a different rational basis from TCP-4. It also replays the two smaller controls and the finite degree and component-occupancy checks. Both `python -B cycle_controls.py` and `python -O -B cycle_controls.py` ran successfully. Each checked all 8,031 primitive words with at least one odd symbol through length 12, 14,317 homogeneous components, 1,649 positive prime-power instances, four literal rational cycles and six norm saturations across two whole systems. The unbounded portions of Sections 1–3 remain written mathematics.
