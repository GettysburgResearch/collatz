# A subquadratic native clock for two unmatched ordinary sources

**PROPOSED written theorem, using the rational $p$-adic Subspace Theorem.** Use the ordinary shortcut map. Take an odd positive integer $s$, a nonnegative integer $r$, and a native prefix of length $k$ on $s$ and $3^rs$ with distinct states at every common clock through $k$. Let $G$ be their total number of odd departures. Uniformly along such families with $G\to\infty$,

$$
                         k=o\big(G(G+r)\big).                        \tag{1}
$$

In particular $k=o(G^2)$ when $r$ is fixed. For fixed positive forward-incomparable targets $a,b$, along **any** odd sources $s\to\infty$ reaching them from $s,3^rs$ at independent clocks with total grade $G$ and $r$ fixed,

$$
                \frac{G}{\sqrt{\log_2 s}}\longrightarrow\infty.       \tag{2}
$$

The explicit elementary bound in [PAIRED_SOURCE_GRADES.md](PAIRED_SOURCE_GRADES.md) remains available at a specified grade. The argument for (1) gives no effective modulus of convergence or fixed power improvement.

## An ordered integer sum with two exceptional factors

Fix a finite set of primes $P$ containing 2 and 3, a nonnegative integer $m$, and $\kappa>1$. Write $b_P(z)$ for the positive part of $|z|$ coprime to every prime in $P$. Use base-two logarithms. There is a constant $C_{m,P,\kappa}$ with this property.

Consider a finite signed sum of nonzero integers indexed by native exponents $e\in[0,L]$. It has two **distinguished** terms, at $e=0$ and $e=L$, each of the form $2^e w d$ with $w$ an odd positive integer supported on $P$ and $d=d_0,d_L$ a nonzero signed integer, respectively. There are at most $m$ further terms $\pm 2^e w$ of the same odd-supported type. Exponents can coincide. Assume the total is zero, and for every integer $1\le t\le L$ the sum of **all** terms with $e<t$ is nonzero. Then

$$
 L+v_2(d_L)-v_2(d_0)
 \le \kappa\big(\log b_P(d_0)+\log b_P(d_L)\big)+C_{m,P,\kappa}.     \tag{3}
$$

In particular $L\le\kappa(\log|d_0|+\log|d_L|)+C_{m,P,\kappa}$. The coefficient of the endpoint cost in (3) is independent of $m$. Without that point, partition into blocks would not prove (1).

**External theorem.** For $n\ge2$ primitive integral variables and $n+1$ fixed rational forms in general position at each place in $S=\{\infty\}\cup P$, the tuples on which the product of all these absolute values is at most $C\|x\|_\infty^{1-\delta}$ lie in finitely many proper rational subspaces, for fixed $\delta>0,C>0$. We use the usual normalization $|p|_p=p^{-1}$. This is the $r=n+1$ case of Schlickewei's theorem. [Schlickewei, 1977, Journal of Number Theory](https://doi.org/10.1016/0022-314X(77)90073-7) · [Evertse, Theorem 1.1 and the $n+1$-form application on p. 6](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

**Stable rational relations.** Suppose that no constant in (3) exists. Take examples along which left minus right, excluding the additive constant, tends to infinity. Pass to a fixed number and indexing of terms, with the two distinguished positions labelled. Across the sequence regard the $i$th signed term as a nonzero rational vector $Y_i$ with one coordinate per example. Among infinite subsequences choose one maximizing the dimension of the space of fixed rational relations on this finite list. No further infinite subsequence can acquire a new fixed rational relation.

A circuit is a minimal linearly dependent sublist of the $Y_i$ over $\mathbb Q$. Its unique relation up to scale has fixed nonzero integer coefficients $c_i$. There are finitely many circuits in this fixed sublist. At each example consider the primitive tuple
$$
                 z_i=c_i Y_i/\gcd_{j\text{ in circuit}} |c_jY_j|.
$$
Here $Y_i$ denotes its integer value at that example inside the formula. These nonzero integers sum to zero. Let $H=\max |z_i|$ and $B$ be the product of the $b_P(d)$ for distinguished indices in this particular circuit, an empty product being one. Then on the chosen subsequence
$$
                               H\le C_{\rm circ} B^\kappa.            \tag{4}
$$

For two terms this holds because the primitive tuple has coordinates $\pm1$. For a circuit with $n+1\ge3$ entries, the first $n$ coordinates form a primitive tuple since the last is minus their sum. Their maximum is between $H/n$ and $H$. Use the first $n$ coordinate forms and the negative of their sum at every place of $S$. They are in general position. For a nonzero integer $v$, the product of its norms over $S$ is $b_P(v)$. The product of forms is therefore at most $C'_{\rm circ}B$, since integer gcd division only reduces the prime-to-$P$ parts. If (4) fails by arbitrarily large factors along a further subsequence then $H\to\infty$ there. Taking $\delta=1-1/\kappa$ puts those examples under the displayed Subspace Theorem inequality. An infinite subsequence then has a fixed nonzero relation on its first $n$ coordinates. Reversing the fixed coordinate multipliers and common gcd introduces an additional relation on a *proper* sublist of the circuit. This contradicts stability and minimality. This proves (4), including bounded $B$. No linear-independence or nondegeneracy premise on the full original list has been inserted.

For any two coordinates in a circuit, (4) gives
$$
 |v_2(Y_i)-v_2(Y_j)|\le\kappa\log B+O_{\rm circ}(1).
$$
Indeed one cancels the common gcd in the valuation difference, pays the fixed valuations of $c_i,c_j$, and uses $0\le v_2(z_i)\le\log H$. In particular a circuit with only pure terms spans a bounded interval of raw exponents $e$ on the chosen subsequence. This bound follows from genuine rational minimality and (4); it is not inferred from finite symbolic support alone.

**Chronological cuts.** Every rational relation on a finite list is a rational linear combination of circuit relations supported in its own support. To see this, choose a minimal dependent sublist of the support, subtract a multiple of its relation to eliminate one coordinate and induct. Apply this once to the all-ones relation expressing the full signed sum. At each example draw the interval between the least and greatest raw exponent in each circuit used in this decomposition. Their union covers $[0,L]$. Otherwise there is a gap between two consecutive occupied exponents in which no circuit crosses. Cutting there, every circuit is entirely on one side or the other. The restricted all-ones relation on the earlier terms is a sum of whole circuit relations, so its numerical sum is zero. This contradicts the strict chronological-cut hypothesis. Endpoints occur in some circuit because their coefficients in the all-ones relation are nonzero. Integer exponents ensure that a cut between two distinct occupied exponents is among the stated tests.

If a circuit contains both distinguished terms then the difference of their 2-adic valuations is $L+v_2(d_L)-v_2(d_0)$ and (4) gives (3) directly. Otherwise all circuits through the first endpoint together cover an interval from zero of length at most
$$
                   v_2(d_0)+\kappa\log b_P(d_0)+O(1).
$$
For each such circuit use its greatest raw exponent among the pure terms. There are finitely many fixed circuit constants, and every interval has the *same* left endpoint. Similarly all circuits through the last endpoint together cover an interval ending at $L$ of length at most
$$
                   \kappa\log b_P(d_L)-v_2(d_L)+O(1).
$$
Use the least pure exponent and the terminal valuation $L+v_2(d_L)$. The remaining pure intervals have bounded total length on this subsequence. Adding the three bounds and using coverage contradicts the choice of sequence. The individual constants in this contradiction may depend on the chosen subsequence; a sequence violating every common constant cannot exist. This proves (3).

## From integer sums to the two physical trajectories

Write $A_t=T^t s$, $B_t=T^t(3^r s)$, with cumulative grades $g_t,h_t$. Use the **signed** determinant
$$
                  d_t=3^{g_t}B_t-3^{h_t+r} A_t .
$$
The [elementary clock proof](PAIRED_SOURCE_GRADES.md) gives $|d_t|\le 3^{g_t+h_t+r}$ and $d_t\ne0$ at every unmatched $t\ge1$. At time zero $d_0=0$. Thus all block arguments start at physical time one. With $a_t=A_t\bmod2$, $b_t=B_t\bmod2$, direct substitution gives
$$
             2d_{t+1}=3^{a_t+b_t}d_t
                  +3^{g_t+a_t} b_t -3^{h_t+r+b_t}a_t .             \tag{5}
$$

Take a block of $L$ *steps* beginning at native time $u\ge1$. Write $Q_j=\sum_{i<j}(a_{u+i}+b_{u+i})$. Unroll (5). The initial term is $3^{Q_L}d_u$, the terminal term is $-2^Ld_{u+L}$. At exponent $j$, the individual pure terms are $2^j3^{Q_L-Q_{j+1}}$ times the two signed contributions after the first term in (5), omitting literally zero contributions. Thus there are exactly $Q_L$ pure terms, including two on a date with two odd departures even if they cancel. At a cut $1\le t\le L$ the sum of all terms whose raw exponent is less than $t$ equals
$$
                       2^t3^{Q_L-Q_t}d_{u+t}\ne0.
$$
The full sum is zero. Consequently (3) applies with the two *actual* endpoint determinants. Its valuation terms telescope between consecutive blocks.

For any fixed integer $m\ge1$, partition the dates from 1 through $k-1$ into consecutive blocks by closing a block as soon as its cumulative grade reaches $m$. Each completed block has $m$ or $m+1$ pure terms, and there is at most one final incomplete block. Hence there are at most $G/m+1$ blocks, each covered by $C_{m+1,P,\kappa}$. Each $\log|d_t|\le (G+r)\log_2 3$. The coarser consequence of (3) gives
$$
 k-1\le (G/m+1)\,\big[2\kappa(G+r)\log_2 3+C_{m+1,P,\kappa}\big].
$$
Divide by $G(G+r)$, first take a limsup as $G\to\infty$ and then let the previously fixed $m\to\infty$. This proves (1). The empty prefix and $k\le1$ create no limiting case.

For (2) take $k$ to be the earlier of the two marked visits. They cannot have met by that date, since both targets would then lie on the future of one state. Every step retains at least half the input; hence $k\ge\log_2(s/\max(a,b))$. The elementary bound forces the grade through $k$ to infinity. Apply (1) at that grade and increase it to the full marked grade to obtain (2).

## A prime-factor condition when one asks for a linear clock

For fixed $r\ge1$, (5) gives $d_1=3(1-3^r)/2$, independently of the odd source. Taking the preceding partition with $m=1$ and summing the full estimate (3) gives a stronger obstruction than the size bound alone. If $k/G\to\infty$ along unmatched prefixes, for *every* fixed finite prime set $P\supset\{2,3\}$ the sum of $\log_2 b_P(d_t)$ over block boundaries, divided by $G$, tends to infinity. Count a shared interior boundary at most twice. The summed terminal valuation is nonnegative and the initial valuation is fixed. In particular a family whose boundary determinants are all supported on a fixed finite set of primes satisfies a linear native-clock bound with a constant depending on that set and $r$. No such support condition has been proved for all genuine pairs.

This circuit estimate uses the same classical Subspace Theorem as the [powered-word source-height proof](../literature/POWERED_WORD_HEIGHT.md). Here there are two exceptional integer factors, signed chronological cuts, and a limit over fixed block sizes. A general local block can contain rational subrelations involving neither endpoint. The circuit decomposition is what prevents their number from multiplying the endpoint-height coefficient. The chronology and true unit condition are needed before applying it to ordinary sources.

## Physical replay

The [finite checker](check_discrepancy_blocks.py) tested 51,400 signed native recurrences for 1,285 ordinary pairs and reconstructed 87,952 strictly nonzero chronological cuts in 14,848 unmatched blocks, keeping both terms at each tied exponent. A separate positive grade-five control already met at time five and had 61 consecutive zero cuts afterward. The ordinary and optimized Python executions produced identical [integer receipts](DISCREPANCY_BLOCK_CONTROLS.json). The replay checks equation (5), its finite expansion and the need for the unmatched condition; no computation here tests the uniform assertion of the Subspace Theorem or certifies an asymptotic onset.
