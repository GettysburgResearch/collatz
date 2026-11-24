# Multiplicative rank of the actual centers at a cycle minimum

**Status.** PROPOSED written theorem. Its two divisor identities and two cross-carry identities have kernel-checked cores in [DenominatorBudget.lean](DenominatorBudget.lean). The effective logarithmic estimate uses Lagarias’s explicit bound. This result tests whether repeated returns to an *ordinary* minimum could furnish a common finite prime set for a moving-target argument. For any sufficiently long putative primitive integer cycle the first $\lfloor\sqrt A/2\rfloor$ such centers are multiplicatively independent modulo sign. Conversely a dependence among the first $t$ forces $\log d\ge(A/t)\log2-O(t+\log A)$ on the complete original denominator. There is no assumption on the parity-factor complexity, runs, or selected block dictionary.

Consider a primitive positive rational shortcut cycle of length $A$, with $p$ ones and reduced denominator $d$. Rotate to its minimum, write that minimum $m/d$ in lowest terms, and let $n_j/d$ be the state after $j$ shortcut steps. Thus $m=n_0=n_A$. Write $p_j$ for the odd count through those first $j$ bits, excluding the bit at $j$. For $1\le j<A$, close the remaining word from position $j$ through position $A-1$ *by itself*. Its unique rational fixed point is its affine center, which can have either sign. Put
$$
 U_j=2^{A-j},\qquad V_j=3^{p-p_j},\qquad D_j=U_j-V_j,\qquad
 c_j=C_j/D_j,\qquad b_j=\operatorname{den}(c_j)>0 .
$$
The full positive cycle satisfies $p>0$ and $2^A>3^p$, with $d\mid 2^A-3^p$ by the fixed-point formula. Hence $\gcd(d,6)=1$. The minimum numerator $m$ must be odd, since an even numerator is halved on the following step. At any odd-to-odd return $2^g n'=3n+d$; reduction modulo three gives $3\nmid n'$, in particular $3\nmid m$. These facts use the actual reduced denominator throughout.

Here $C_j$ is the shortcut carry of the suffix. The walk uses the original physical endpoints $n_j/d$ and $m/d$. The artificial center $c_j$ need not lie on that walk. The clock gap $D_j$ is nonzero by unique factorization.

### Exact endpoints and independent clock gaps

The endpoint equation gives $dC_j=U_j m-V_j n_j=D_jn_j+U_j(m-n_j)$. Since $\gcd(U_j,D_j)=1$,
$$
 \gcd(|D_j|,dC_j)=\gcd(|D_j|,m-n_j),\qquad
 b_j\ge\frac{|D_j|}{|m-n_j|}. \tag{8}
$$
Primitivity ensures $n_j\ne m$ at every internal cut. At $d=1$, the center's reduced denominator is exactly $|D_j|/\gcd(|D_j|,m-n_j)$. This extends the exact integral-center criterion used in PR #193 C1 to the full denominator of arbitrary signed proper segments.

For $1\le i<j<A$, let $h=j-i$ and $k=p_j-p_i$. Then $D_i=2^hU_j-3^kV_j$ and hence
$$
 \gcd(b_i,b_j)\mid\gcd(|D_i|,|D_j|)\mid |2^h-3^k|<3^h .
 \tag{9}
$$
The second divisibility follows by substituting $V_j\equiv U_j\bmod D_j$ and cancelling the coprime factor $U_j$ modulo a common divisor. It covers $k=0$. The strict final inequality holds for $0\le k\le h$ and $h>0$.

### Common denominators and prime support

Let $c_0=\log(3)/1200$. For any $L\ge1$ and any integer $k\ge0$, Lagarias's Lemma 2.2(1) gives $|L\log2-k\log3|\ge c_0L^{-13.3}$. For $x=L\log2-k\log3<0$, $|1-e^{-x}|\ge|x|$. For $x>0$, $1-e^{-x}\ge\min(1,x)/2$. As $c_0<1$, this gives
$$
 |2^L-3^k|\ge (c_0/2)2^L L^{-13.3}.
$$
The odd numerator satisfies (2) of [the denominator note](README.md), so $m\le (400/\log3)d A^{14.3}$. On either shortcut branch $n_{i+1}+d\le(3/2)(n_i+d)$, hence $|m-n_j|\le(3/2)^j(m+d)$. From (8), with an absolute constant in the error,
$$
 \log b_j\ge A\log2-j\log3-\log d-O(\log(2A)). \tag{10}
$$
In particular for ordinary cycles every puncture with $j=o(A)$ leaves a center of almost maximal possible denominator. This holds separately for each cut. For the matching upper bound, $0<3^{p}<2^A$ and $U_j<2^A$, so $b_j\le |D_j|<2^A$. [Lagarias, *Ternary expansions of powers of 2*, Lemma 2.2(1)](https://arxiv.org/pdf/math/0512006)

Let $1\le t<A$ and $B_t=\operatorname{lcm}(b_1,\ldots,b_t)$. For a given prime the sum of exponents minus the largest exponent is at most the sum, over pairs, of their minimum exponents. Applying that inequality at every prime, and then (9)–(10), gives
$$
 \begin{aligned}
 \log B_t
 &\ge \sum_{j\le t}\log b_j-\sum_{1\le i<j\le t}\log\gcd(b_i,b_j)\\
 &\ge t(A\log2-\log d)-(\log3)\frac{t(t+1)}2
       -(\log3)\frac{t^3-t}{6}-O(t\log(2A)). \tag{11}
 \end{aligned}
$$
The cubic term comes from $\sum_{i<j}(j-i)=(t^3-t)/6$.

Set $t=\lfloor\sqrt A\rfloor$ for large $A$. If $\log d=o(A)$, including $d=1$, then
$$
 \log B_t\ge(\log2-\tfrac16\log3-o(1))A^{3/2}.
$$
Every maximal prime power in $B_t$ occurs in some $b_j<2^A$, so
$$
 \omega(B_t)\ge\frac{\log B_t}{A\log2}
       \ge(1-\tfrac16\log_2 3-o(1))\sqrt A .
 \tag{12}
$$
Thus these particular physical cuts force at least about $0.7358\sqrt A$ distinct primes in their reduced center denominators. This cardinality is a prime-support obstruction to using one common set $S$ for those centers. It does not by itself lower-bound the abstract multiplicative rank of the centers, since a single rational generator can have many prime divisors.

The estimate also works without a distinguished square-root cutoff. If $0<\eta<1$ and $\log d\le(1-\eta)A\log2$, choosing $t=\lfloor c_\eta\sqrt A\rfloor$ with $0<c_\eta^2<6\eta\log2/\log3$ gives $\log B_t\gg_\eta A^{3/2}$ and $\omega(B_t)\gg_\eta\sqrt A$. These bounds concern the complete **reduced** center denominators. Using raw clock gaps would lose the link to ordinary arithmetic.

### Multiplicative independence of the centers themselves

Write $c_i=a_i/b_i$ in lowest terms with $b_i>0$. Fix $1\le i,j\le t<A$, $i\ne j$, and put $h=|j-i|$, $k=|p_j-p_i|$. The following cross-carry divisibilities bound cancellations against *numerators* at other positions. If $i<j$, the earlier endpoint identity gives
$$
 d C_i=2^hU_j m-3^k V_j n_i
 \equiv U_j(2^h m-3^k n_i)\pmod {D_j}.
$$
Since $U_j$ is a unit modulo $D_j$, $\gcd(b_j,|a_i|)$ divides $|2^h m-3^k n_i|$. For $k>0$ the bracket is nonzero because $3\nmid m$. For $k=0$ the $h$ intervening steps are even, so $n_i=2^h n_j$ and equality would force $n_j=m$ at an internal position. If $i>j$, then $D_j=2^h U_i-3^k V_i$, so
$$
 2^h dC_i\equiv V_i(3^k m-2^h n_i)\pmod{D_j}.
$$
Here $V_i$ is a unit modulo $D_j$: if $V_i>1$, then $3\mid V_j$ and $3\nmid D_j$. The bracket is odd and nonzero. Thus $\gcd(b_j,|a_i|)$ divides its absolute value. Both conclusions use that $a_i$ divides $C_i$ up to sign when $C_i\ne0$; for $C_i=0$ the corresponding congruence still holds. The finite identities preceding the modular cancellations are checked as earlier_carry_residue and later_carry_residue. Both brackets are differences of positive terms and hence
$$
 \gcd(b_j,|a_i|)\le 3^h(3/2)^i(m+d). \tag{13}
$$

Suppose the first $t$ centers are nonzero and multiplicatively dependent modulo sign. Choose a nontrivial integer relation $\prod_{i\le t}|c_i|^{e_i}=1$, then choose $j$ with maximal $|e_j|$. At each prime $\ell\mid b_j$, integral valuations give
$$
 v_\ell(b_j)\le\sum_{i\ne j}|v_\ell(c_i)|=\sum_{i\ne j}v_\ell(|a_i|b_i).
$$
Truncating each summand to $v_\ell(b_j)$ preserves the inequality. Since $a_i,b_i$ are coprime,
$$
 \log b_j\le\sum_{i\ne j}\big(\log\gcd(b_j,|a_i|)+\log\gcd(b_j,b_i)\big).
$$
Put $M=\log(m+d)$. From (9) and (13), using $\sum_{i\ne j}|j-i|\le t(t-1)/2$ and $\sum_{i\le t}i=t(t+1)/2$, the right-hand side is at most
$$
 (\log3)t(t-1)+\tfrac12\log(3/2)t(t+1)+(t-1)M .
$$
But (8) and the two-log lower bound give $\log b_j\ge A\log2-j\log3-M-13.3\log A+\log(c_0/2)$. Combining and using $j\le t$ gives the entirely explicit consequence of dependence
$$
 A\log2\le tM+13.3\log A+\log(2/c_0)
       +(\log3)t^2+\tfrac12\log(3/2)t(t+1). \tag{14}
$$
If a suffix has zero carry, its $b_j=1$ and the last lower bound also implies (14) directly. This covers the case in which the multiplicative group would not be defined for that center.

Substitute $M\le\log d+\log(1+(400/\log3)A^{14.3})$ to obtain
$$
 \log d\ge \frac{A}{t}\log2-O(t+\log(2A)). \tag{15}
$$
Formula (15) holds whenever a center is zero or the first $t$ centers are dependent modulo sign. In particular, if their generated group has bounded rank $r$ through the first $r+1$ cuts, then the full original denominator is at least $2^{A/(r+1)}A^{-O_r(1)}$. This uses the actual rational centers of explicitly chosen nested arcs and allows those centers arbitrary individual height.

Conversely, if $\log d=o(\sqrt A)$ and $t=\lfloor\sqrt A/2\rfloor$, the right side of (14) is at most
$$
 \left(\tfrac14\log3+\tfrac18\log(3/2)+o(1)\right)A
 < (0.326+o(1))A.
$$
This is strictly less than $A\log2$ for all sufficiently large $A$. The first $t$ centers are therefore all nonzero and **multiplicatively independent modulo sign**. The maximal-coefficient valuation cover and its truncation are also kernel-checked in [ValuationDominance.lean](ValuationDominance.lean). This holds within each sufficiently long hypothetical primitive ordinary cycle, whatever its block and factor complexities. It is stronger than a lower bound on the number of primes in the common support. It also differs from a rank estimate across the ambient family of all possible words.

### What the near-minimum recurrence can certify

A minimum at period $A$ has a polynomially bounded numerator when $d=1$. Consequently the minimum itself and its first $O(\log A)$ iterates admit descriptions with $O(\log A)$ bits. Formula (10) shows that puncturing even at these small endpoints leaves a near-period center of exponential height. The affordability hypothesis of the growing-partition theorem therefore cannot be inferred for these long arcs from the short description of the recurrent endpoints. The many-center strengthening (11) also excludes allocating one fixed prime budget to all these cuts.

For comparison, even computability or a short description of the entire parity word would not force a cheap partition on its own. PR #192 constructs, at prescribed convergent clocks, finite families containing high rational words requiring many bounded-height windows. For $H=1$, searching these finite families and taking the lexicographically first nonintegral hard word gives a uniformly computable choice from the encoded clocks whenever the stated hard-word bound holds. One may test a threshold, for example $A/(\log A)^2$ windows at large $A$, by exact comparisons on the finite lists, using an equivalent computable integer threshold smaller than the established lower bound. The clock input needs $O(\log A)$ bits. Ordinary integrality would still have to supply additional mathematical structure.

The unconditional constraints proved here on these precise centers are (8)–(14): bounds on full denominators, cross gcds, and a necessary large multiplicative rank for small $d$. The cited moving-target, unit-equation and almost-boundedness theorems give no rank **upper bound** for these same centers. The cut centers are rational auxiliary values. An ordinary cycle need not force their prime factors to divide its minimum or any specified bounded-height global integer. Establishing such a constraint, proving a cheap partition made of *different* arcs, or obtaining a pointwise bound directly for the full period carry remains open. [PR #192, moving-window theorem and its high-complexity controls](https://github.com/GettysburgResearch/collatz/blob/d2081d1cd2410e6004eaee9f9b13c5553afaf3f4/research/astra-closure-attack-20261124/CYCLE_EXTENSION.md) [PR #193, cut criterion C1](https://github.com/GettysburgResearch/collatz/blob/c6cb5e66516a86c33a757154983bbddc822510de/research/astra-universal-descent-20261124/cycles.md)
