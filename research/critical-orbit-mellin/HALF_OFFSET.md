# The half-grid phase counts excess valuations on an ordinary orbit

**Proposed, source-qualified.** Let $Q\ge1$ and translate the odd target grid by half its period $P=2\cdot3^Q$ in the [offset integral](OFFSET_COAREA.md). The translated targets are exactly the even integers in $(0,P]$. At a given word let $t$ be the translated even target, $J$ its slope, and $F$ its positive affine offset. Write $t=2^v y$ with $y$ odd and $v\ge1$. Keep the word if the associated odd path ending at $y$ is simple, including both its start and end. For fixed $0<\theta<1$, set
$$
 A_Q(\theta)=\sum_w \frac{J}{t}{\bf1}_{\{\theta\le F/t\le1,\ {\rm simple}\}} .
$$
Then:

- If every positive orbit is eventually periodic, $\sup_Q A_Q(\theta)<\infty$ for each $\theta$.
- If some odd unit $n$ escapes, then at $\theta=1/(3n+1)$ one has $A_Q(\theta)/\log Q\to\infty$. Universally $A_Q(\theta)=O_\theta(Q)$.
- $A_Q(\theta)=o(Q)$ for all $\theta$ precisely when every escaping odd spine, if any, has $\log U^Q(n)/Q\to\log(3/2)$. A sublinear upper bound alone would leave such a spine possible. A subsequence with $A_Q(\theta)=O_\theta(\log Q)$ at each fixed threshold would exclude every escaping orbit.

## Exact unfolding of the even target

The shift by $3^Q$ preserves the ternary residue class. The nearest reverse letter of exponent $b$ therefore gives the same integer
$$
 x=(2^b t-1)/3=(2^{b+v}y-1)/3 .
$$
It is positive and odd, and its true last valuation is $a(x)=v_2(3x+1)=b+v$. Every earlier reverse letter is physically realized at an odd target. Conversely a true length-$Q$ word ending $x\mapsto y$ gives one translated copy for each $1\le v<a(x)$ with $2^v y\le P$. The word slope and offset have both been multiplied by $2^v$, so $J/t$ and $F/t$ retain their true values at $y$. Thus the half shift counts an ordinary integral path with multiplicity at most $a(x)-1$, and counts no path with last valuation one.

At fixed depth there are finitely many even targets and countably many words. The sum is a convergent nonnegative series: the unmarked slope total at a fixed residue is bounded by $3^Q$ and the target is at least one.

## Counting along a forward spine

The simple-path reciprocal bound implies that every marked true path has some odd state $s\le R(\theta)$ strictly before its endpoint, by $F/t=1-\prod(1+1/(3u))^{-1}$. All possible last preimages $x$ therefore lie in the forward union of finitely many such $s$. For any one last step, with $y=U(x)$, the total weight before multiplicities is bounded by
$$
 g_{Q-1}(x)\frac{3\cdot 2^{-a(x)}}{y}=\frac{g_{Q-1}(x)}{x+1/3}.
$$
If every orbit eventually cycles, only a fixed finite set of $x$ occurs. The every-depth ordinary bound at those $x$, including $g_0=1$, gives the first assertion. [Fixed-target bounds](../native-pressure-20261118/ORDINARY-DENSITIES.md)

For each of the finitely many escaping components represented below $R(\theta)$, its forward union from those states lies in one chosen spine and a finite set. The portion sampled at depth $Q$ uses at most the first $Q+O_\theta(1)$ steps along those finitely many spines. On any nonperiodic target $x$, the absolute first-hit bound gives $g_{Q-1}(x)/x\ll1$, also when $Q=1$. Thus their total contribution is at most a constant times the sum of $a(x)-1$ over these portions. For $y_j=U^j n$ put $E_n(Q)=\sum_{j<Q}(a(y_j)-1)$. Exact telescoping and the bounded simple-orbit correction give
$$
 \log y_Q=Q\log(3/2)-(\log 2)E_n(Q)+O_n(1).
$$
In particular $E_n(Q)=O_n(Q)$, which proves the general upper bound. If all escaping spines have $E_n(Q)=o(Q)$, adding a fixed shift to $Q$ preserves this estimate. [Uniform first-hit bound](../unsafe-return-weights/INVERSE_AGE_LAWS.md)

Conversely, take all true inverse paths that pass through an escaping odd unit $n$ and end $j$ steps later at $y_j$, $1\le j\le Q$. They are simple. The initial factor at $n$ gives $F/t\ge1/(3n+1)$. Even their largest translated copy satisfies $2^v y_j\le(3y_{j-1}+1)/2\ll_n(3/2)^Q<P$ for all sufficiently large $Q$. Their different even endpoints or words are distinct. Write $D_j$ for the forward slope from $n$ to $y_j$. Then
$$
 A_Q(1/(3n+1))\ \ge\ \sum_{j=1}^Q (a(y_{j-1})-1)\frac{D_j}{y_j}\,g_{Q-j}(n)\ \gg_n E_n(Q).
$$
Here $D_j/y_j$ is bounded below by the reciprocal simple-orbit correction divided by $n$, and $g_k(n)$ is uniformly minorized at every unit. The [fixed-run Subspace Theorem estimate](../unsafe-return-weights/VALUATION_ONE_RUNS.md) gives $E_n(Q)/\log Q\to\infty$ on each escaping orbit. The upper and lower estimates prove all three statements. An odd nonunit can be advanced once to a unit without changing the existence or exponential rate of escape. [Integer minorization](../native-pressure-20261118/MINORIZATION.md)
