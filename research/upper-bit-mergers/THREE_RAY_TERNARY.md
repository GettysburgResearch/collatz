# The ternary digits occupied by failed tripling pairs

**PROPOSED.** Write $P(x)$ when the positive Collatz orbits of $x$ and $3x$ meet. Let $E$ consist of the odd failures and put
$$
 S=\{x\in E:x\equiv1\pmod {16},\ 3\nmid x\}.
$$
For a set $A$ of integers, let $N_h(A)$ be the number of residues modulo $3^h$ represented in $A$. If Collatz fails, then
$$
 \limsup_{h\to\infty} \frac{N_h(S)}{3^{0.84h}}>0. \tag{1}
$$
The witnesses in different residues may occur at different heights. In particular, eventual success on the two ternary-unit classes in the class $1\bmod16$ suffices for full Collatz. One may discard any set with $N_h=o(3^{0.84h})$ from those required tests. The exponent comes from the [dyadic-limit counting theorem and its published predecessor input](THREE_RAY_DENSITY.md).

## Two elementary facts about ternary projections

Call $A$ small in this proof if $N_h(A)=o(b^h)$, where $b=3^{0.84}>2$. Finite unions of small sets are small. For any fixed nonconstant rational affine map $L$ with denominator a power of three, the integer-domain preimage $\{x:L(x)\in A\}$ of a small set is small. In fact, for $L=(a x+c)/3^v$ and $d=v_3(a)$, membership fixes $ax+c$ modulo $3^{h+v}$ in at most $N_h(A)$ ways. Any such congruence has at most $3^d$ solutions modulo $3^h$, since two solutions differ by a multiple of $3^{h+v-d}$ if that exponent is positive. The bound still holds if $h+v\le d$.

Suppose every member of $A$ belongs to $U$ or has one of $m$ integer images in $A$ under maps $(a_i x+c_i)/3$ with $3\nmid a_i$. For $h\ge1$,
$$
 N_h(A)\le N_h(U)+mN_{h-1}(A).
$$
Indeed a permissible image modulo $3^{h-1}$ specifies exactly one source residue modulo $3^h$. If $U$ is small and $m<b$, iteration of the inequality shows $A$ is small: after division by $b^h$ its forcing term tends to zero and its memory is bounded by the geometric series of ratio $m/b$. This argument concerns actual ordinary parameters; it only uses residue sets to bound their number.

## Transporting a small tested set to all odd starts

Assume $S$ is small. Let $E_0$ denote odd failures divisible by three, and $A_j=\{x\in E:x\equiv j\pmod{16}\}$. A failed $x\in E_0$ forces a failure at $16x/3+1$ or $32x/3+1$. Both are $1\bmod16$. If the failed successor is a ternary unit, it belongs to $S$. If it is a multiple of three, it belongs to $E_0$. Thus the preceding recurrence for $E_0$ has $m=2$ and small $U$ consisting of two affine preimages of $S$. As $2<b$, both $E_0$ and $A_1\subset E_0\cup S$ are small. [Ordinary two-successor identity](THREE_RAY_WINDOWS.md#when-three-divides-the-defect)

Here are details for the other needed residues. For a ternary unit $x$, take $L=2$ if $x\equiv1\bmod3$ and $L=3$ otherwise. Put $z=(2^L x-1)/3$ and $g(y)=f(y-1)$, where $f$ denotes the true component. The elementary window proof states that $P(z)$ gives $f(x)=g(3^Lx)$, and $P(8x-1)$ gives $g(9x)=g(27x)$. If $3^jx$ is 3 modulo 16 or 5 modulo 8, its orbit meets that of $3^jx-1$. Therefore for $j,L\in\{2,3\}$ the only possible failing tests needed here are $z$, the multiples $3^a x$ for $1\le a<j$, and $8x-1$ if $L\ne j$. [Proof of these identities](THREE_RAY_WINDOWS.md#when-three-does-not-divide-the-defect)

- For $x\equiv13\bmod16$ take $j=2$. If $L=2$, then $z\equiv1\bmod16$. If $L=3$, then $8x-1$ is a multiple of three and $z\equiv13\bmod16$. Apart from preimages of $E_0$ and $A_1$, each failure can therefore continue only from $x$ to $(8x-1)/3$ in $A_{13}$. The recurrence with $m=1$ shows $A_{13}$ is small.
- For $x\equiv7\bmod16$ take $j=3$. Here $8x-1\equiv23\bmod32$ passes unconditionally. The two starts $23,69$ both reach 20 in five steps, with three and two odd inputs respectively. Shifting the parameter by $32w$ shifts both endpoints by $27w$. Apart from the multiple-of-three tests, $L=3$ leads to $z\in A_{13}$ if the test fails, and $L=2$ leads to $z\in A_9$.
- For $x\equiv9\bmod16$ take $j=3$. If $L=3$ the only possible failure apart from the multiple-of-three tests is at $z\equiv13\bmod16$. If $L=2$, then $z\equiv1\bmod16$, and $8x-1$ belongs to $7\bmod16$ and $1\bmod3$. Apply the preceding bullet to that number: apart from multiples of three the only continuing test is at $(4(8x-1)-1)/3=(32x-5)/3\equiv9\bmod16$. Thus $A_9$ is included in finitely many fixed affine preimages of already small sets, together with a single denominator-three continuation into $A_9$. Again $m=1$, so $A_9$ is small. The preceding bullet now gives smallness of $A_7$.

For a general odd failure the window theorem gives either a failed multiple-of-three test, a failure at $8x-1$ or $24x-1$ (both 7 modulo 16), or a failure at $z$ (one of 1, 9 or 13 modulo 16). The integer 1 passes directly. Thus $E$ is small. The interval $[1,3^h]$ contains one representative per residue, so $D(3^h)\le N_h(E)=o(3^{0.84h})$. Monotonicity and the fixed factor between consecutive powers imply $D(X)=o(X^{0.84})$. This contradicts the counting theorem in a counterexample, proving (1).

## Removing deeply even shifts from an eventual test

There is a further ordinary reduction. For $x\equiv1\pmod{16}$ and $x\equiv1\pmod3$, put $z=(4x-1)/3$. Then $f(z)=f(x)$ since $T(z)=2x$. Moreover
$$
 f(3z)=g(4x)=g(9x)=g(6x)=f(6x)=f(3x).
$$
Here $g(2u)=g(3u)$ is native, and $6x-1$ meets $6x$ after five steps as in the window proof. Thus $P(x)$ and $P(z)$ agree without any assumption about other pairs.

In particular every $z\equiv1\bmod64$, $z>1$, may be replaced by $(3z+1)/4$ while preserving the truth of its test. For a ternary-unit parameter $z\equiv1\bmod16$, repeat until the new parameter $w$ has $v_2(w-1)=4$ or 5. Each reduction produces a ternary unit and keeps the parameter 1 modulo 16. Setting $a$ equal to the number of reductions gives $w-1=(3/4)^a(z-1)\ge(z-1)^{\log_4 3}$ because $4^a\le z-1$. Hence the new parameters go to infinity with the old ones. Full Collatz is consequently equivalent to eventual success on just the six residues
$$
 17,49,97,113,145,161\pmod {192}.
$$
Here 97 and 161 have $v_2(w-1)=5$, the other four have valuation 4, and none is divisible by three. The pointwise reduction to these six residues need not preserve the quantitative residue-count conclusion (1). Whether every required ordinary pair meets remains open.

## Ordinary heights of tested failures

Let $T_*(X)$ be the number of actual failed comparisons in the six displayed residues up to $X$, and $T_S(X)=|S\cap[1,X]|$. A counterexample forces
$$
 \limsup_{X\to\infty}\frac{\log(1+T_*(X))}{\log X}
 \ \ge\ \gamma_0=\frac{0.84}{1+\displaystyle\frac{1-0.84}{1-\log_3 2}\log_3(32/3)}
 \ >0.4343. \tag{2}
$$
This statement keeps heights finite by tracking both the input ternary digits and the size of each new parameter.

In the preceding reduction, first route a failure to $A_7,A_9,A_{13},A_1$ or $E_0$ with one of the finitely many initial affine maps. Follow $A_7$ to $A_9,A_{13}$ or $E_0$. At $A_9$ the only repeat is $(32x-5)/3$; the fixed intermediate $8x-1$ in that repeat has been included in the formula. All other exits from $A_9$ go to $A_{13},A_1$ or $E_0$. At $A_{13}$ the only repeat is $(8x-1)/3$, with other exits going to $A_1$ or $E_0$. Split $A_1$ into $S$ and $E_0$. At $E_0$ each application of $(cx+3)/3$ for $c=16$ or 32 either ends in $S$ or continues at $E_0$. Include that final application as an $E_0$ step. At any stage a multiple of three may be sent directly to $E_0$. Thus apart from an absolutely bounded number of maps from a fixed finite list, the path consists, in order, of at most three runs of the three types just listed. In particular the two alternatives at $E_0$ are the only binary choices within a run. Only a single actual continuation is needed per source.

Truncate at a total of $h$ run steps or arrival in $S$, whichever occurs first. There is an absolute constant $C$ with
$$
 D(X)\ll (1+h)^C\left[T_S(C(32/3)^h X)+2^h(X/3^h+1)\right]. \tag{3}
$$
For the paths attaining $h$ steps, there are at most $O((1+h)^C2^h)$ words: fix the bounded external maps and the three run lengths, then choose the binary $E_0$ word. Each fixed word requires its last output to be integral. Its rational affine slope has ternary valuation at most $-h+C$ since every run step divides by three and has ternary-unit numerator in its slope. The external maps have bounded ternary valuations. Two valid input integers therefore differ by a multiple of $3^{\max(0,h-C)}$, proving the second count in (3).

For a path terminated in $S$, all intermediate heights are at most $C(32/3)^h X$. Indeed a run of $k$ steps, each of slope at most $32/3$ and bounded additive constant, increases the height to at most $(32/3)^k$ times the incoming height plus a fixed multiple of $(32/3)^k$. Only boundedly many runs and external maps occur. Given the terminal input, the lengths of the runs and the external maps determine at most one initial positive odd failure. The two choices at each $E_0$ step are distinguished in reverse by $v_2(y-1)$ at its output $y$, since $y-1=c(x/3)$ and $x/3$ is odd. Every other map is injective. Thus the first term in (3) costs only a polynomial in $h$ for multiplicity.

Set $d=\log_3 2$, $a=0.84$, and take $h=\lfloor k\log_3 X\rfloor$ for fixed $(1-a)/(1-d)<k<1$. The second term including its logarithmic factors is $o(X^a)$. By the truth-preserving binary reduction, $T_S(Y)\ll(1+\log Y)(1+T_*(Y))$: a terminal value and the number of binary reductions determine the initial parameter, and the number of reductions is at most $\log_4 Y$. If $T_*(Y)\ll Y^\gamma$ for $\gamma<a/(1+k\log_3(32/3))$, the first term of (3) is also $o(X^a)$. That violates the dyadic-limit lower bound for $D$ in a counterexample. Letting $k$ decrease to $(1-a)/(1-d)$ proves (2).
