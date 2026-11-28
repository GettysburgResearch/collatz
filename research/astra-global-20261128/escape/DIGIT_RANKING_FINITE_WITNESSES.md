# A finite balanced certificate for every fixed digit window, degree and radix

**Written theorem.** This proof uses the digit-score rigidity established in the companion manuscript, including its classical Hochman–Host equidistribution input. All finite witnesses here use actual positive Collatz steps. The argument proves their existence and gives a terminating search without a size or runtime bound. Its certificate question comes from Paper 189, which gives explicit ternary witnesses at widths one and three above every floor, and at width five above 64. Its current version two, dated 23 November 2026, leaves width five above larger floors and all widths from seven open. [Companion polynomial-digit rigidity proof](../root/DIGIT_POLYNOMIAL_RANKING.md) · [Paper 189, current version two, §§1 and 6](https://rstation.ai/problems/collatz/papers/189) · [Paper 189, version one](https://rstation.ai/problems/collatz/papers/189/v1).

Fix any integer radix $p\ge2$, window radius $r\ge0$, polynomial degree $D\ge0$, and any input floor $X_0$. For every window $w$ of the terminating base-$p$ numeral with the two distinct end sentinels and $0\le j\le D$, define the integer feature
\[
             \Phi_{w,j}(n)=\sum_{i:\,w_i(n)=w}i^j ,
\]
with $i^0=1$. Write $\Phi(n)$ for their finite vector, $d(n)=\Phi(Tn)-\Phi(n)$, and $e(n)=n\bmod2$, where $T$ is the ordinary shortcut map. Then there are finitely many positive integers $n_s>X_0$, **all prime to three**, and positive integers $b_s$ with
\[
       \boxed{\ \sum_s b_s d(n_s)=0,\qquad
          \frac{\sum_s b_s e(n_s)}{\sum_s b_s}>\log_3 2.\ }            \tag{1}
\]
Consequently every finite local score $\theta\cdot\Phi$ fails a parity price $a-b e(n)$ with $b>0$ and $a/b\le\log_3 2$, regardless of any lower bound on the score. Adding $c\log n$ with $c\ge0$ still fails: the weighted sum of log increments is strictly positive since each even step has increment $-\log 2$ and each odd step has increment greater than $\log(3/2)$. The same single certificate works for the entire indicated price range at the specified width and floor. These conclusions concern finite integer feature sums. With a completely arbitrary bounded correction, $-\log_3 n$ attains the critical price, as in the companion theorem.

## Bare rigidity on the positive unit core

Call a score *bare* if it is exactly $\theta\cdot\Phi(n)$, with no separate bounded term. Suppose its increments are bounded above by finite constants on both parities at all sufficiently high inputs satisfying $3\nmid n$. The proof of the companion theorem gives, for all sufficiently long canonical numerals,
\[
     \theta\cdot\Phi(n)=\gamma L(n)+
        V(\operatorname{lead}_K(n),n\bmod p^K),                      \tag{2}
\]
where $V$ is a real function on finitely many leading and trailing digit words. Here $\operatorname{lead}_K$ records the first $K$ most significant digits. Both $K$ and the length from which (2) holds can be chosen in terms of $p,r,D$ alone; $\gamma,V$ may depend on the coefficients. Equation (2) holds on all sufficiently large integers, even though the increment hypotheses are only imposed on unit inputs. We give the needed modifications explicitly.

In the invariant-measure limit the bounded addition to $\lfloor p^L U\rfloor$ may depend on that integer. The carry proof bounds the chance of any modification with the prescribed absolute bound so it applies without independence. In the repeated even inequality choose $x$ at bounded distance from $\lfloor p^L U\rfloor$ with $3\nmid x$. Then $2^j x$ stays a unit throughout the comparison. In the alternate power-of-two-radix argument choose $x$ within bounded distance so $2x+1\not\equiv0\bmod3$ before comparing $2x+1$ and $3x+2$. Multiplication by any of the fixed factors still gives a bounded perturbation at that step of the proof. This supplies the same top-degree invariant-measure comparison and the same finite de Bruijn coboundary.

At the mantissa comparison of degree $D\ge1$, for the odd edge one may take $n=6m+1$ and $Tn=9m+2$. For the even edge take $n=6m+2$ and $Tn=3m+1$. The variable $m$ spans an interval of length comparable to $p^L$. The fixed strides $3,6,9$ have greatest common divisor with $p^{i+r'+1}$ dividing $p^{i-r'}$ for all sufficiently large $i-r'$, where $r'$ is the fixed current radius. Indeed only primes dividing $p$ can divide this common divisor and their powers in the strides are bounded. Thus every specified interior digit block contains equally many of the accessible residues in a full period, and the remaining error is $O(p^{i+r'+1-L})$ for bounded window coefficients. The finitely many lower positions and geometrically summed partial periods have exactly the same cost as in the companion argument. The odd and even inequalities give, after Haar averaging in logarithmic mantissa, respectively $\beta\log_p(3/2)\le0$ and $-\beta\log_p2\le0$. Hence the top interior constant is zero. The top boundary is constant by the odd irrational rotation, and its constant times $L^D$ reduces exactly to degree at most $D-1$.

The reduction also preserves the asserted finite boundary form. The originally absent bounded correction starts at zero. Discrete summation by parts leaves at the low end a function of finitely many low digits, since the indices there are bounded. At the high end each lower power of $L$ times a fixed leading function is represented exactly by the uniquely marked top sentinel window at the reduced degree. Contributions from numerals too short for these identities are supported on a finite set of lengths. Iterating to degree zero leaves only the constant interior weight times $L$ and finitely many fixed endpoint functions from the top, bottom and final coboundary. All radii can be enlarged by fixed amounts sufficient for the windows in the previous degree, independently of coefficient values. The original interval of degrees is finite. This gives (2) with a common structural cutoff and a common $K$. Increase $K$ as needed to include the common short-length cutoff. At fixed length the leading words correspond to half-open cells in $u=\log_p n-(L-1)\in[0,1)$.

If the even and odd upper allowances are $A,E$, then consecutive even steps from $2^Jz$ down to a fixed unit $z$ above the floor yield
\[
                        -\gamma\log_p2\le A .
\]
The positive path beginning at $2^J-1$ has $J$ odd steps to $3^J-1$. Take $J$ odd so the starting site is a unit; every later site in the segment is $-1\bmod3$. Its length change gives
\[
                         \gamma\log_p(3/2)\le E .                      \tag{3}
\]
Both inequalities follow by summing the actual increments, using (2) with a bounded remainder, dividing by $J$, and letting $J$ increase.

## The critical bare score is impossible

Put $\alpha=\log_3 2$. Suppose $\theta\cdot d(n)\le\alpha-e(n)$ at all sufficiently high unit sources. Applying (3) with $A=\alpha$ and $E=\alpha-1$ pins
\[
                          \gamma=-\log p/\log3 .
\]
Along odd sources $n\equiv-1\bmod 2p^K$, the target $(3n+1)/2$ has the same residue $-1\bmod p^K$. We can take $n\equiv-1$ also modulo $3$, so all sources are units. In any open mantissa interval and at arbitrarily large lengths such sources exist, by ordinary progression counting. Put $v=\log_p(3/2)$ and
\[
               W(u)=V(\operatorname{lead}_K(u),-1)+\gamma(1-u).
\]
Here the leading tuple is read from $p^u\in[1,p)$. For every $u$ away from the finitely many leading and length boundaries before and after rotation, choose a sequence of such sources whose mantissas tend to $u$ within its cell. The odd additive correction $1/2$ has vanishing relative size. In the ideal step the log contribution $\gamma v=\alpha-1$ exhausts the allowance. Equation (2) therefore gives $W(\{u+v\})\le W(u)$ for almost every $u$. The two Haar integrals are equal, giving equality almost everywhere. Since $(3/2)^j$ is never an integer power of the integer $p$ for $j>0$, $v$ is irrational, so $W$ is constant almost everywhere. On the interior of each nonempty leading cell $W$ has slope $-\gamma\ne0$. This contradiction uses only actual high odd unit inputs. In particular the full infinite system is infeasible at the exact critical price.

## Every nonincreasing bare boundary score is neutral

Choose an integer $N>X_0$ large enough that (2) is valid at both ends of every edge with source $n>N$, and every leading-digit or length threshold in the two ranges is an integer. This is possible using the common $K$. Consider any vector $\theta$ with $\theta\cdot d(n)\le0$ for every $n>N$ prime to three. Now (3) forces $\gamma=0$. The score is precisely the bounded boundary function in (2) at both ends of each tested edge. We show
\[
              \theta\cdot d(n)=0\quad
                  \text{for every }n>N,\ 3\nmid n .                  \tag{4}
\]

For this purpose write $p^K=2^c3^a m$, $\gcd(m,6)=1$, and use $a'=\max(a,1)$. Consider the space of a logarithmic mantissa $u\in\mathbb R/\mathbb Z$, a binary integer $z_2\in\mathbb Z_2$, a unit residue $z_3\bmod3^{a'}$, and a residue $z_m\bmod m$. These specify the leading and trailing score at all points off the finite mantissa boundaries. The parity of $z_2$ determines one ideal shortcut. The mantissa translates by $-\log_p2$ on an even input and by $\log_p(3/2)$ on an odd input. On the binary coordinate apply the corresponding shortcut branch. On the two odd-modulus coordinates apply $t_0(z)=z/2$ or $t_1(z)=(3z+1)/2$ in the indicated residue rings. Both branches preserve ternary units.

This ideal system has an invariant probability of full support. Take the product of Haar probabilities on the mantissa and binary coordinates, uniform probability on the $m$-residues, and any stationary probability for the fair two-branch finite Markov chain on the ternary units. That stationary probability is strictly positive on every unit: the even map $z\mapsto z/2$ permutes the units in a single cycle (the order of $2$ modulo $3^{a'}$ is $2\cdot3^{a'-1}$, by $v_3(4^h-1)=1+v_3(h)$). The identity for the order follows also by expanding $(1+3)^h$ first for $3\nmid h$ and then cubing successively. Conditional on either parity, the binary output is Haar since each shortcut branch maps its parity coset bijectively with the normalized Haar law onto $\mathbb Z_2$. Each branch preserves uniformity modulo $m$ and on the circle. Hence these three output marginals have the same product conditional on either branch and are independent of the ternary coordinate; stationarity of its fair-branch law proves invariance of the full product. Trivial modulus factors cause no change.

Every ideal transition with $u$ and its image in the interiors of their leading and length cells, and with specified finite lower residues determining both endpoint digits, is realized by arbitrarily large true unit inputs. Indeed fix the input binary class through $c+1$ bits so the output is fixed through $c$ bits, and fix the indicated odd-modulus residues. The Chinese remainder theorem gives one integer progression. A nonempty open mantissa interval about $u$, whose ideal image stays in the chosen cell, has length growing proportionally to $p^L$ at high lengths. It contains true representatives, and their relative odd correction tends to zero. Thus the boundary increment is nonpositive almost everywhere for the full-support invariant measure. Its integral is zero by invariance. Each such open transition with its residue cylinder has positive measure, on which the increment is constant, so every one has increment zero.

Conversely every true $n>N$ with $3\nmid n$ realizes one of these open types, including possible exact leading thresholds. For an odd $n$ use the real source $x=n+1/3+\varepsilon$ with $0<\varepsilon<1/6$. It has the same canonical leading tuple and length as $n$ because $n<x<n+1$, and the ideal odd output $(3/2)x=T(n)+(3/2)\varepsilon$ lies strictly between the integer $T(n)$ and $T(n)+1$. The integer leading thresholds at these lengths ensure an open neighborhood with both same leading tuples. For even $n$ take $x=n+\varepsilon$. Independently use precisely the lower residue cylinder of $n$, which gives the true lower output digits. The two corrected leading and low labels in this open type are therefore the actual ones at $n,T(n)$. This proves (4).

## Compactness and exact integer separation

Let $S$ be the finite-dimensional real span of the integer vectors $d(n)$ for $n>N$, $3\nmid n$. Their common annihilator may be discarded by projecting any potential vector orthogonally to $S$. By (4), every nonzero $\theta\in S$ has some tested row $d(n)$ with $\theta\cdot d(n)>0$. Cover the unit sphere of $S$ by these open positivity sets and take a finite subcover. On the sphere the maximum of the selected finitely many linear forms has a strictly positive minimum $c$. Consequently, if $\theta\in S$ satisfies just those finitely many critical-price inequalities, then $c\|\theta\|\le\max(\alpha,\alpha-1)=\alpha$. If $S=\{0\}$, a single high odd unit is already a certificate.

Inside that compact coefficient ball, the closed half-spaces from all tested rows have empty joint intersection by critical bare infeasibility. The finite intersection property supplies a finite subfamily already having empty intersection in the ball. Adjoining the coercive subcover rows gives a finite infeasible family in the entire coefficient space. The coercivity argument is essential: infeasibility of a general infinite system of linear inequalities need not have a finite witness.

The finite Farkas alternative now gives nonnegative weights on those rows, of sum one after normalization, with $\sum b_s d(n_s)=0$ and $\sum b_s e(n_s)>\alpha$. The normalized set cut out by the balance equalities and nonnegativity is a bounded rational polytope. Some rational vertex attains the maximum of the odd fraction, so the strict inequality persists with rational weights. Drop zero weights and clear denominators to obtain (1).

For an exhaustive search one can enumerate the high unit rows and the finite lists of nonnegative integer weights, test balance by integer arithmetic and check the strict comparison by $3^{\sum b_s e(n_s)}>2^{\sum b_s}$. The theorem supplies termination for each fixed radix, width, degree and floor. No bound on the first successful search range follows here. This proof gives certificates specific to the chosen width; Paper 189's obstruction to using one fixed witness for unbounded widths is unaffected.
