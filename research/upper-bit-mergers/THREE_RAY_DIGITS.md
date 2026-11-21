# Leading binary digits of failed tripling comparisons

**PROPOSED, unconditional.** For the ordinary positive shortcut map, call an odd $q$ a defect when the orbits of $q$ and $3q$ never meet. Write $S$ for the set of defects, $\ell(n)=\log_2 n\bmod1$ and $\theta=\log_2 3\bmod1$. Let $K$ be the set of limits of $\ell(q_i)$ along defects $q_i\to\infty$. If Collatz is false, then
$$
 \mathbb R/\mathbb Z=\bigcup_{j=0}^5(K-j\theta). \tag{1}
$$
In particular $K$ has normalized Lebesgue measure at least $1/6$ and contains an interval. There is a leading binary word $P$ beginning with 1 for which **every** finite binary word $w$ occurs as the next digits of infinitely many defects beginning with $Pw$. In fact $P$ can be chosen so that for **each** continuation $Pw$, its defect count divided by $X^{0.84}$ is unbounded along arbitrarily large cutoffs. The cutoffs can depend on $w$.

Consequently any regular language containing all defective binary representations has positive upper natural density as a set of integers, if Collatz is false. In particular, proving that a finite automaton recognizes precisely the defects would settle the conjecture. The proof uses only finite comparison identities and the constructive synchronization of compatible affine pairs.

## Component changes at every logarithmic position

Every ordinary merger component contains positive odd integers $y$ coprime to three, by removing factors of two and taking an odd step if needed. Let $L$ be the closure of $\ell(y)$ for such $y$ in one component. The odd inverse $(2^v y-1)/3$ is a positive odd unit modulo three for arbitrarily large $v$. Indeed there are exponents with $2^v y\equiv1\pmod3$ but $2^v y\not\equiv1\pmod9$, repeating modulo six. The inverse reaches $y$, and its logarithmic position tends to $\ell(y)-\theta$. It follows by closure that $L-\theta\subseteq L$. Irrationality of $\theta$ now gives $L=\mathbb R/\mathbb Z$.

Let $f$ label the merger component of its positive integer argument. If there are two components, choose in each one a point with its logarithmic position in any specified open subinterval of $(0,1)$. Exact doubling preserves $f$ and $\ell$. Hence for **every** sufficiently large $k$ both labels occur between $2^k$ times the two ends of the associated interval of significands in $(1,2)$. Between these points is an integer $n$ with $f(n)\ne f(n+1)$. Shrinking intervals shows every circle point is a limit of $\ell(n)$ for such changes with $n\to\infty$. The same reasoning works with any nonconstant labeling that is constant along ordinary steps.

## Keeping the powers of three in the finite chain

We use the 17-step chain from $288n$ to $288(n+1)$. Its proof supplies the following pointwise statement. If $f(n)\ne f(n+1)$, some positive odd defect $q$ satisfies
$$
 q-e=2^{-v} A(an+b),\qquad v\ge0,\qquad e\in\{-1,0,1\}, \tag{2}
$$
where $A,a>0$ are smooth with prime factors 2 and 3, $b$ is fixed for its row, and $(e,A,a,b)$ comes from a finite list. The integer $j=v_3(Aa)$ is between zero and five. Here are the details of the list bounds. [Offset chain and comparison identities](TRIPLING_VARIATION.md)

- Removing a factor $s=2^d3^t$ from $288n+p$ costs tests at the odd parts of $3^i(288n+p)/s$ for $0\le i<t$. Their slope has ternary exponent $2-t+i\le1$. The endpoint normalizations at $n,n+1$ satisfy the same bound.
- A comparison at $h=an+b$ in the chain has $a=288/(s k)$ for $k=4,16$ or 3. In each row $a$ is an integer and $v_3(a)\le2$. The ordinary odd rows use a single test at $h$ itself.
- In a minus row $f(4h-1)=f(h)$, write $h=2^v w$ with $w$ odd. Removing twos from the comparison tests $8\cdot 2^i w-1$ with $0\le i<v$, of the form (2) with exponent $v-i$ in place of $v$. At odd $w$, the reduced 27-window proof uses only $8w-1,24w-1$ to transport $g(4w)=g(9w)$ to $g(3^j w)$, where $g(y)=f(y-1)$ and $2\le j\le4$. Unless $w\equiv1\pmod{16}$, some such $3^jw$ is 3 modulo 16 or 5 modulo 8, where the adjacent pair meets. Removing the factors of three then tests $3^i w$ with $0\le i\le3$. For $w\equiv1\pmod{16}$ use $g(9w)=g(6w)$ and the five-step meeting of $6w-1$ and $6w$; only the test at $w$ is needed to identify $f(6w)$ with $f(w)$. Thus $v_3(A)\le3$. [Residue and path identities](THREE_RAY_WINDOWS.md#when-three-does-not-divide-the-defect)
- In a plus row $f(16h+1)=f(h)$, the twos are removed by testing $16\cdot2^i w+1$ with $0\le i<v$. For odd $w$ there is a shorter last comparison. The ordinary two-step identity gives $f(16w+1)=f(12w+1)$. Since $12w\equiv4\pmod8$, the pair $12w,12w+1$ meets in three steps, by the lifted base pair $4,5$. Thus $f(16w+1)=f(12w)=f(3w)$ and only $w$ itself needs testing. Here $v_3(A)=0$.

These comparisons prove (2) with $q-e>0$. They only charge an actual defect when some adjacent labels differ.

## Covering the circle

At every such witness (2) gives the exact identity $\ell(n+b/a)=\ell(q-e)-j\theta$ on the circle. For any sequence $n\to\infty$ of changes approaching a prescribed position, pass to a subsequence with the same row constants. If $q\to\infty$ on a further subsequence, the bounded additive shifts change the two logarithms by $o(1)$, giving a limit in $K-j\theta$. Otherwise pass to a subsequence with $q$ fixed. That limit is the single position $\ell(q-e)-j\theta$. All fixed-$q$ exceptions together give at most a countable set. Thus the complement of the finite closed union on the right of (1) is both open and at most countable. It must be empty. Subadditivity of measure gives $|K|\ge1/6$. A finite union of closed sets with empty interiors has empty interior, so $K$ contains a nonempty open interval.

Passing from $\ell(n)$ to the significand $2^{\ell(n)}$ yields an interval strictly inside $(1,2)$. Choose inside it a binary prefix cylinder determined by $P$. For every extension $Pw$, the interior of that cylinder contains limit positions of arbitrarily large defects, giving the stated prefix conclusion. This permits arbitrary additional digits between $P$ and any prescribed block as well.

## A finite-automaton criterion

Suppose a regular language $\mathcal L$ of canonical binary integers contains all the defect representations. Use a deterministic automaton reading the most significant bit first, with $s$ states. Every word $Pw$ above can reach an accepting state. From its last state there is an accepting continuation of length at most $s-1$, by erasing loops from a shortest path. For all $2^k$ words $w$ of length $k$, these accepted continuations produce distinct integers below $2^{|P|+k+s}$. This gives positive upper density; in fact the same bound at successive $k$ gives positive lower density. A regular set of zero lower density therefore cannot contain all defects of a counterexample.

If $S$ itself were regular, a second property would give a contradiction. Reverse its regular language to read digits from the least significant end. Every fixed initial binary class has a subclass on which $n$ and $3n$ merge for all positive lifts, by the equal prime-to-six parts of the slopes 1 and 3. Thus from every reachable state of the reversed automaton there is a path to a dead state (one with no accepting continuation). This applies also to the empty prefix, and does not require accepting binary representations with leading zeros. For a complete automaton with $s'$ states the path has length at most $s'$, including zero if already dead. Conditional on any still live history, at least one in $2^{s'}$ blocks of $s'$ fair bits therefore enters the dead set. The number of accepted words of length $m$ is at most $2^m(1-2^{-s'})^{\lfloor m/s'\rfloor}$, which gives zero upper natural density after summing lengths. This contradicts the prefix conclusion if Collatz is false. Conversely full convergence gives the empty regular language. [Constructive binary subclass theorem](AFFINE_RAYS.md#classification-and-a-constructive-bound)

The argument neither supplies an automaton nor bounds the shortest defect with a given initial word. Whether the defective language is empty remains open.

## Component counts inside any prescribed arc

The numerical exponent below comes from the published theorem of Krasikov and Lagarias. For each fixed positive ternary unit $y$, at least $X^{0.84}$ positive starts up to $X$ reach $y$, for every sufficiently large $X$. Arbitrarily many pairwise incomparable ternary-unit targets can be chosen in each component, with disjoint predecessor sets. Applying the theorem to that finite collection shows that the count in each component divided by $X^{0.84}$ tends to infinity. The proof below works with any $0<\alpha<1$ for which two component counts have this property. [Krasikov–Lagarias, Theorem 6.1](https://arxiv.org/abs/math/0205002) · [Disjoint predecessor construction](TWO_SCALE_TRIPLING.md#arbitrarily-large-predecessor-coefficients)

The cumulative count of each component retains its power in *every* fixed open arc $I$ of logarithmic positions. Given an ordinary start $n=2^v w$, $w$ odd, replace $w$ by $w_0=4w+1$ if $3\mid w$ and by $w_0=w$ otherwise. The output is a ternary unit in the same component since $T^2(4w+1)=3w+1$ and odd $w$ shares the component of $3w+1$. The input power of two $2^v$ will be restored at the end.

From an odd ternary unit $y$ choose the least $a\in[4,9]$ with $(2^ay-1)/3$ an odd ternary unit. Such a choice exists by the powers of two modulo nine. The ordinary accelerated odd map sends this inverse back to $y$. Its size is between $5y$ and $171y$, and its logarithmic position differs from $\ell(y)-\theta$ by $O(1/y)$. Hence at step $k$ the accumulated error relative to $\ell(w_0)-k\theta$ is $O(1/w_0)$ uniformly in $k$, by the geometric growth. There exists $H_I$ such that the first $H_I$ translates by $-\theta$ of every starting position include a point in an arc compactly inside $I$, by density of irrational rotation and compactness. For $w_0$ sufficiently large in terms of $I$, some inverse among the first $H_I$ therefore has position in $I$. For smaller $w_0$, first take a bounded number of the same growing inverse steps to exceed that threshold, then apply the argument from the new starting point.

This produces $n'=2^v y'$ in the same component with $\ell(n')\in I$ and $n'\le C_I n$. Each $n'$ has only boundedly many antecedents in this construction: it records $v$ in its binary valuation, and for each possible bounded number of inverse steps the odd part $y'$ determines $w_0$ by forward odd iteration. At most two original odd parts give the same $w_0$. Applying this map to component members up to $X/C_I$ gives $\gg_I X^\alpha$ members with position in $I$ up to $X$ whenever the component has the original $\gg X^\alpha$ count. The multiplicity and dilation constants are fixed for $I$, so a ratio tending to infinity before transport still tends to infinity in $I$.

## Local convergence on one arc forces a constant global limit

Let $f$ now indicate the component of 1. For $R=2^k$ put $g_R(t)=f(\lfloor R2^t\rfloor)$ on $[0,1)$, extended periodically. Suppose $g_R$ converges in $L^1$ on every compact subarc of a nonempty open arc $I$. Then it converges globally in $L^1$ to a constant in $\{0,1\}$. We include the local propagation argument since it requires no global bound on the number of defects.

First, local convergence implies $o(R)$ changes $f(m)\ne f(m+1)$ with $R\le m<2R$ and $\ell(m)$ in any compact subarc of $I$. In a fixed coordinate chart away from the cut at zero, shift $x=R2^t$ to $x+1$. The induced change of variable in $t$ tends uniformly to the identity and has Jacobian bounded above and below. Approximate the local $L^1$ limit by a continuous function on a slightly larger arc. Local convergence, the Jacobian bound and uniform continuity give $o(1)$ for the integrated difference of the two step functions. Each integer change contributes $\gg1/R$, since the integer parts of $x$ and $x+1$ change together. Arcs meeting the cut can be split into charts away from it, discarding first a fixed interval of width $\epsilon$ around zero. That interval contributes $O(\epsilon R+1)$ candidate changes, and then $\epsilon$ tends to zero. This also proves the same $o(R)$ bound in any constant number of neighboring dyadic shells.

Next fix a compact subarc inside $I-\theta$, with image under rotation contained strictly in $I$. For $R\le x<2R$ write $n=\lfloor x\rfloor=2^v u$, with $u$ odd. We have $f(n)=f(u)=f(3u+1)$ and $f(3n)=f(3u)$. At each fixed $v$, discrepancies therefore cost adjacent changes at $3u$ with logarithmic positions in $I$, in a bounded number of shells at scales comparable to $R/2^v$. Taken over $v\le V$ for fixed $V$, there are $o_V(R)$ such $n$; the remaining $n$ are multiples of $2^{V+1}$ and number $O(R/2^V+1)$. Taking $R$ to infinity and then $V$ to infinity gives $o(R)$ disagreements. The rotation of $\ell(x)$ sends $x$ to $3x/2^j\in[R,2R)$ with $j=1$ or 2. The integer $2^j\lfloor3x/2^j\rfloor$ differs from $3n$ by at most four, so the same local adjacent-change bound pays for any mismatch there. The former integer shares the label of $\lfloor3x/2^j\rfloor$ by exact doubling. Every exceptional $n$ occupies only $O(1/R)$ logarithmic measure. We have proved
$$
 \|g_R(t)-g_R(t+\theta)\|_{L^1(J)}\longrightarrow0
 \qquad (J\text{ any compact subarc of }I-\theta).
$$
Thus the local convergence extends to $I-\theta$, to the translated limit. Iterate this argument. Finitely many rotated arcs cover the circle, and compact subarcs inside them can still be chosen to cover it. The local limits agree almost everywhere on overlaps since they are limits of the same sequence. The resulting global $L^1$ limit is binary and invariant under rotation by $\theta$, hence constant by irrationality (all Fourier coefficients except the constant coefficient vanish).

## The power 0.84 persists in the leading digits

For an arc $I$ put $D_I(X)=|\{q\le X:q\in S,\ \ell(q)\in I\}|$. Define $K_\alpha$ to contain those $t$ for which every open neighborhood $I$ has $\limsup_{X\to\infty}D_I(X)/X^\alpha=\infty$. This is a closed set. Under the two component lower bounds above,
$$
 \mathbb R/\mathbb Z=\bigcup_{j=0}^5(K_\alpha-j\theta). \tag{3}
$$
Suppose otherwise. Choose an open arc $U$ whose closure misses this finite union. For every $j$ a fixed open neighborhood of $\overline U+j\theta$ has $D_I(X)=O(X^\alpha)$, using a finite subcover of neighborhoods witnessing exclusion from $K_\alpha$ (one may take a finite union of arcs). For all sufficiently large $q$ and $n$ in (2) with $\ell(n)\in U$, its $\ell(q)$ is in one of these neighborhoods. This follows from the exact identity after (2) and the uniformly bounded additive shifts. The remaining bounded $q$ cost only $O(1)$ per fixed-ratio shell: for each row and $q$, (2) puts $2^v$ in a fixed-ratio interval and then determines $n$. This multiplicity bound also holds for every unbounded $q$, all of which satisfy $q\le CR$ on $R\le n\le2R$. Thus
$$
 \#\{R\le n\le2R:\ell(n)\in U,\ f(n)\ne f(n+1)\}=O(R^\alpha).
$$

For each compact subarc inside $U$, it follows that the local $L^1$ difference between $g_{2R}$ and $g_R$ is $O(R^{\alpha-1})$: a discrepancy at $n=\lfloor R2^t\rfloor$ requires an adjacent change at $2n$. These dyadic differences are summable, so the functions converge locally on $U$. The preceding propagation argument makes the common global limit constant. Summing the geometric tail of successive differences on the compact subarc now gives distance $O(R^{\alpha-1})$ from that constant there. On any smaller fixed open arc $I$ compactly inside the subarc, each integer of the minority color on $[R,2R)$ contributes $\gg1/R$ to the local distance. Thus the minority color contributes $O(R^\alpha)$ starts in $I$ per shell and $O(X^\alpha)$ cumulatively in $I$. This contradicts the transported component lower bound. Equation (3) follows.

In particular $K_{0.84}$ has measure at least $1/6$ and nonempty interior. The prefix argument applied inside this interior proves the unbounded normalized count for every continuation. It also strengthens the regular-cover criterion. If $A$ is any regular set of zero lower density, its set $K_A$ of limiting logarithmic positions has empty interior, since an interval of limits would force positive lower density by the bounded-continuation argument. Choose an open subarc whose closure lies in the interior of $K_{0.84}$ and misses $K_A$. Then only finitely many members of $A$ have their logarithmic positions in this subarc. It follows that
$$
 \limsup_{X\to\infty}\frac{|(S\setminus A)\cap[1,X]|}{X^{0.84}}=\infty.
$$
Thus a regular sparse candidate set cannot absorb the forced power of failures.
