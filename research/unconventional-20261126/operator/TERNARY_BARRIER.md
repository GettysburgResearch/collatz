# A weak-square tail for the actual ternary inverse maximum

**Status.** PROPOSED written theorem. The bounds use the actual congruence overlaps of inverse words on $\mathbb Z_3$. The random walk in the proof is a counting device for scripts; the branches over a Haar root need no independence assumption.

Let $B(y)$ be the supremum of incoming slopes $C_w$ in [OP-T1](TERNARY_TRANSFER.md), and $m_3$ normalized Haar measure on $\mathbb Z_3$.

## OP-B1. The endpoint of the moment range

For $t\ge2$ there are absolute constants $c>0$ such that
$$
 \frac{c}{t^2\sqrt{1+\log t}}
       \ \le\ m_3\{y:B(y)>t\}\ \le\ \frac1{t^2}.
$$
In particular $B$ belongs to weak $L^2$, belongs to $L^p$ for all $0<p<2$, and does not belong to $L^2$ (hence to no $L^p$ with $p>2$). The exponent is exact. The displayed inequalities do not identify a possible logarithmic factor in the true tail.

**Scripts and their cylinders.** Take a word of $k$ inverse letters, with odd letters at $i_1<\cdots<i_q$. Write $C_i=3^{q_i}/2^i$ for its prefix slope. Repeated affine substitution gives
$$
  C_k x=y-A',\qquad
  A'=\tfrac12\sum_{j=1}^q C_{i_j-1},\qquad
  A=2^k A'=\sum_{j=1}^q3^{j-1}2^{k-i_j},
$$
where $x$ is the inverse endpoint. The full script is legal at $y$ exactly when $2^k y\equiv A\bmod3^q$, a cylinder of mass $3^{-q}$. Final integrality implies all prefix guards: running the affine maps forward from $x\in\mathbb Z_3$ keeps every intermediate state integral there, and a forward odd letter lands in $2\bmod3$. At fixed $k,q$, the integer $A$ determines the entire word. Its binary valuation recovers $k-i_q$, subtracting the final summand removes that letter, and induction recovers the rest. Empty-odd words require no decoding.

**A tilted first-passage count.** Let $\mathcal F_t$ consist of the words with $C_k>t$ and all proper prefixes $C_i\le t$. These are prefix-free in the binary script alphabet and cover exactly the event $B>t$ by their actual ternary cylinders. They satisfy $t<C_k\le3t/2$. Assign iid word probabilities $1/4$ for $E$ and $3/4$ for $O$. The probability of each script is then exactly $C_k^2\,3^{-q}$. Its log slope $S_k=\log C_k$ has positive drift $d=(3/4)\log3-\log2>0$. The first-passage time $\tau=\min\{k:S_k>\log t\}$ is finite almost surely. Consequently
$$
 \frac4{9t^2}\le \sum_{w\in\mathcal F_t}3^{-q(w)}
                \le \frac1{t^2}.
$$
The last inequality bounds the Haar union from above. For an elementary lower bound take only $k\le K\asymp\log t$ keeping a fixed positive fraction of the tilted mass. On first passage $A'/C_k\le k/2$. At fixed $k$, $q$ is unique when it exists since the overshoot factor $3/2$ is less than 3. Each given cylinder has at most $1+k/2$ representatives by the injectivity of $A$ within $0\le A\le (k/2)3^q$. Summation over the possible $k$ bounds the total overlap by $O((1+\log t)^2)$ and gives a preliminary lower bound with that denominator.

**Uniform carry control at first passage.** Set $L=\log t$. For the tilted walk, for every interval $I$ of length one the expected total number of visits to $I$ is uniformly bounded by a finite $M$, independently of $I$. Indeed condition at the first visit. From its entrance position $x\in I$, a further visit after $j$ steps forces the new increment sum $S_j\le1$. For sufficiently small $b>0$, $\mathbb E e^{-b S_1}<1$ by positive drift. Therefore $\sum_{j\ge1}\Pr(S_j\le1)\le e^b\sum_{j\ge1}(\mathbb E e^{-b S_1})^j<\infty$. The strong Markov property gives the uniform assertion, also for intervals the walk can skip.

Before $\tau$ the walk is below $L$. Divide this region into slabs $(L-r-1,L-r]$, $r\ge0$. Since $C_\tau>e^L$,
$$
 \mathbb E[A'/C_\tau]
 \le \tfrac12\mathbb E\sum_{j<\tau}e^{S_j-L}
 \le \tfrac M2\sum_{r\ge0}e^{-r}<\infty
$$
uniformly in $t$. Hence choosing a fixed $K_0$ retains at least $7/8$ of the tilted first-passage mass with $A'/C_\tau\le K_0$.

**Concentration of the crossing length.** For all large $L$, at least $7/8$ of the tilted mass lies in $|\tau-L/d|\le D\sqrt L$ for a sufficiently large constant $D$. At $n_-=\lfloor L/d-D\sqrt L\rfloor$, an earlier crossing implies
$\max_{j\le n_-}|S_j-dj|\ge L-dn_-$. Kolmogorov's maximal inequality bounds its probability by $\operatorname{Var}(S_1)n_-/(L-dn_-)^2=O(D^{-2})$. At $n_+=\lceil L/d+D\sqrt L\rceil$ a later crossing implies $S_{n_+}\le L$, with probability $O(D^{-2})$ by Chebyshev. Rounding the window ends by one has no effect and can be absorbed in $D$.

On the intersection of these two restricted families the tilted mass is at least $3/4$. Its sum of cylinder masses is at least a constant times $t^{-2}$. At each of $O(\sqrt L)$ possible lengths the recovered integer $A$ is at most $K_0 3^q$, so a fixed target belongs to at most $1+\lfloor K_0\rfloor$ such scripts at that length. Dividing by the total overlap proves the lower bound for large $t$. For bounded $t\ge2$ one can reduce the constant using any sufficiently long all-odd cylinder. The layer-cake formula now gives divergence of $\int B^2$ since $\int^{\infty}dt/(t\sqrt{\log t})=\infty$.

The same lower bound holds for the lower natural density of ordinary positive targets with $B(y)>t$ for each *fixed* $t$: the restricted first-passage union above uses finitely many congruence cylinders. It also gives the same lower bound for the full ordinary union from its finite subunions. Haar upper bounds on an infinite union of cylinders give no matching upper natural density without additional control. Nothing here implies sublinear $B(y)$ at a specified ordinary target as its height tends to infinity.
