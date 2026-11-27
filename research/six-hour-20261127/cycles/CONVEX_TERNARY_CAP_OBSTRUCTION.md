# Smooth convex integer ranks in binary ternary trees below the cubic height threshold

In a fixed past mechanical calendar cell of an ordinary canonical-height-one Collatz cycle, three terminal scaled labels $u,v,w$ satisfy
$$
 u+w\equiv2v\pmod{3^k}\quad\Longrightarrow\quad u\equiv v\equiv w\pmod{3^k}
$$
whenever the past calendar is shared for $k$ steps. Indeed the common last mechanical letter makes the corresponding combination of predecessor lowbits vanish modulo three. It lies in $[-2,2]$, so all three predecessor lowbits coincide. The predecessor combination then vanishes modulo $3^{k-1}$. Induction and forward substitution give the assertion. This is the midpoint case of the ternary pair matching used in Weaver 145. For a set of labels this property at every depth up to $k$ is equivalent to every occupied prefix modulo $3^j$, $j<k$, having at most two occupied children modulo $3^{j+1}$. Three children give a counterexample at their level. Conversely, use the first differing digit. Below this is the binary subtree condition.

Put $\sigma=\log_2(3/2)=0.5849625\ldots$. Given any sufficiently large $P$ and any mask $\ell_r\in\{1,2\}$ with $\ell_0=2$, there are abstract positive integer labels $L_r$ with the following properties.

- Extend $L_{r+P}=2L_r$. Their first and second rank differences are strictly positive, including both seams. Their first differences are uniformly comparable to $X/P$.
- Every fundamental label has the prescribed lowbit $\ell_r$, is coprime to three and has a distinct odd part. The largest odd part $X$ is comparable to $P^{2+\sigma}$.
- The whole fundamental population satisfies the binary subtree condition at every depth. For some $C\asymp X$, simultaneously $L_r=C2^{r/P}+O(P^\sigma)$ throughout the fundamental range.

Thus these real-geometric and modular midpoint restrictions alone cannot force height to exceed $P^3$. The labels do not obey the Collatz chronological affine recurrence. A second construction below incorporates one common additive binary digit cube through a modulus comparable to $X/P$, with freely chosen generators and a quadratic real profile.

## Smooth exponential population

Write $d=\log_3 2$ and $p=1/d=\log_2 3$. Any set of $n$ distinct integers contains a subset of at least $n^d$ satisfying the binary subtree condition at all depths. In its least-significant-first ternary tree retain the two children of largest population at every node. For sorted child counts $n_1\ge n_2\ge n_3$, induction needs $n_1^d+n_2^d\ge(n_1+n_2+n_3)^d$. With $a=n_1^d$, $b=n_2^d$, this follows from $(a+b)^p\ge a^p+2b^p$ for $a\ge b$. Equality holds at $a=b$ because $2^p=3$, and $(a+b)^p-a^p$ is nondecreasing in $a$. It suffices to follow the finite tree until the leaves separate. Repeatedly remove a retained subtree. At each stage the potential $n^{1-d}$ drops by at least $1-d$ by concavity. Thus the set partitions into at most $n^{1-d}/(1-d)+1$ such classes.

Take $B=100P^2$, $F_r=\lfloor B2^{r/P}\rfloor$, $0\le r<P$. These $P$ different integers admit that partition. Take the least $a$ with $2^a\ge P^{1-d}/(1-d)+1$. Then $D=3^a\asymp P^{(1-d)\log_2 3}=P^\sigma$. Assign each class a distinct low code $u_r\in[0,D)$ with its $a$ ternary digits in $\{0,1\}$. Put
$$
 x_r=DF_r+u_r,\qquad L_r=12x_r+\ell_r .
$$
Extend both populations by octave doubling. The first $a$ ternary levels of $x$ use the low codes. Above each complete code its high parts form a binary subtree. For $L$, the first ternary digit separates the possible masks. In each such branch division after translation leaves $4x$, and multiplication by a ternary unit permutes the children of every prefix. Thus the whole set has the condition at every depth.

In the fundamental range $|L_r-12DB2^{r/P}|\le12D+2$. Through $r=P+1$ this error is at most $24D+4$. The smooth second differences are at least $12DB(\ln2/P)^2>500D$, while the error in each second difference is at most $96D+16$. First differences are positive and comparable to $DP$ by the same comparison. The corresponding estimates also hold before the last rescaling. Thus $x_0\le x_r<2x_0$. Mixed lowbits yield equal odd parts only if one $x$ equals twice the other, excluded by this interval. Equal lowbits use distinctness. The stated height and approximation follow. One may replace the smooth constant by $L_0$ with an additional $O(D)$ error.

## One common additive digit cube at a larger modulus

Let $q=3^b$ be the least power at least $P$. Set $S=\{\sum_{j<b}\eta_j3^j:\eta_j\in\{0,1\}\}\bmod q$. Choose shifts $v_i$ with
$$
 S+\{\textstyle\sum_{i<a}\epsilon_i v_i:\epsilon_i\in\{0,1\}\}=\mathbb Z/q .
$$
At every stage some translate reduces the uncovered fraction to at most its square, by averaging the intersection of the uncovered set with its translate. Taking the least $a$ with $2^a\ge(3/2)^b(1+\ln q)$ leaves uncovered fraction at most $(1-(2/3)^b)^{2^a}<1/q$. One may pad with zero shifts after earlier coverage. Thus $D=3^a=P^{\sigma+o(1)}$.

Set $F(j)=(12P+1)j+3j^2$, $0\le j\le P$. A difference factors as the difference of the arguments times a ternary unit, so the first $P$ values are distinct modulo $q$. Represent each $F(j)\bmod q$ by the covering shifts and $S$. With $u_j=\sum_{i<a}\epsilon_i3^i$ from that representation, $f_j=DF(j)+u_j$ belongs modulo $Dq$ to one cube with generators
$$
 3^i+Dv_i\quad(0\le i<a),\qquad D3^j\quad(0\le j<b).
$$
These generators have consecutive, distinct ternary valuations. Each prefix uniquely fixes its contributing lower bits by successive reduction, so the tree is binary to this depth. The fundamental $f_j$ are distinct modulo $Dq$ by their distinct high block indices, so every larger occupied branch contains just one of these integers.

Set $x_j=f_j+f_P-2f_0$, giving $x_P=2x_0$ exactly, and extend by doubling. Interior second differences through $j=P-2$ exceed $4D$, from the quadratic curvature $6D$ and low-code error $2(D-1)$. The final seam curvature $2(f_1-f_0)-(f_P-f_{P-1})$ is positive of order $DP$, because the two base gaps are $D(12P+4)$ and $D(18P-2)$ with errors less than $D$. All first differences are positive of order $DP$ and $x_j\asymp DP^2$. Replace fundamental $x_j$ by $L_j=12x_j+\ell_j$ and extend again by doubling. The bounded perturbation preserves both strict differences, including the seams. Lowbits and distinct odd parts follow as before. The final labels belong to one translated cube modulo $3Dq$ with the old generators multiplied by twelve and one new generator equal to one. This modulus is comparable to the height divided by $P$. The second construction does not assert the small-error exponential profile of the first. Its weights are free and differ from the specific chronological Collatz weights.

The exact replay constructs the smooth comparison via integer roots of $B^P2^j$. It checks all occupied-child trees, every first and second difference through both seams, the prescribed lowbits and distinct odd parts, and all modular cube representations in the second construction. These are controls on the formulas. The obstruction at arbitrary period follows from the two constructions.

- https://rstation.ai/problems/collatz/papers/145/v1
