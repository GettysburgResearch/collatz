# Critical odd-clock time for first entry into permanently safe ordinary seeds

Let $U(n)=(3n+1)/2^{v_2(3n+1)}$ on positive odd integers and write $E_j(n)=\sum_{i<j}v_2(3U^i n+1)$. Put $b=2-\log_2 3$ and $C_*=1/b$. Define the set of permanently safe ordinary seeds by
$$
 \mathcal P=\{x:4E_j(x)\le7j\text{ for all }j\ge1\}.
$$
Let $\tau(n)=\inf\{j\ge0:U^jn\in\mathcal P\}$ with the value $\infty$ when there is no visit. Call $n$ bad if its orbit never reaches one. Write $\Pr_k$ for the uniform probability on the $2^{k-1}$ odd integers of $[2^k,2^{k+1})$, for $k\ge1$.

**Permanent entry.** One has $\tau(n)<\infty$ exactly for the bad positive odd sources. For every fixed $\delta>0$ there are $c_\delta,C_\delta>0$ such that
$$
 \Pr_k\left(n\text{ bad},  \left|\frac{\tau(n)}{\log_2n}-C_*\right|>\delta   \text{ or }  \log_2 U^{\tau(n)}n>\delta\log_2 n\right)
 \le C_\delta e^{-c_\delta k}.                                      \tag{1}
$$
The condition $n$ bad applies to the entire parenthesized pair of exceptions. Thus both bounds concern the same first permanently safe state of the same actual positive integer. In particular their exceptional set has finite ordinary harmonic mass. The result places no lower bound on the number of bad sources.

**Sparse visitors.** Fix $0<c<C_*$ and $0<\epsilon<(1-bc)/40$. On an odd octave choose any predetermined set of $O(2^{\epsilon k})$ positive odd starting integers. Outside an exceptional fraction $O(e^{-h k})$, the tested orbit $U^jn$, $0\le j\le c\log_2n$, meets no forward state at any future time of any of those starting integers. In particular the comparison may include all odd $v\le n^\epsilon$. Here $h>0$ can depend on $c,\epsilon$. This consequence uses the uniform reciprocal packing estimate for an actual simple trajectory. The proof of (1) involves only finite elementary ordinary and geometric word estimates. It does not need packing, a ternary mixing theorem, a basin density theorem or an assumption about the existence of bad sources.

## Finite-octave short blocks

Use the large initial octave parameter $k$. Fix constants $\beta>0$ and $\eta>0$, with $0<\eta<\beta/8$. Take a starting octave $I_m=[2^m,2^{m+1})$ with $m\ge\beta k$, and a block of $\ell\le\beta k/8$ accelerated steps. It suffices to consider $k$ large in terms of these fixed constants. Put $H=\lfloor\beta k/2\rfloor$. Then $H\le m-1$ and $H\ge2\ell+\beta k/5$ for all sufficiently large $k$.

For a chronological word of $s$ positive exponents and total $h$, its exact cylinder is one odd residue modulo $2^{h+1}$. For instance the $s$-step affine recurrence fixes the source modulo $2^h$ by the terminal numerator divisibility, and the odd terminal fixes the next bit. Equivalently each next gap $e$ selects its sole exact-valuation child among the $2^e$ odd lifts. Each such complete word with $h\le H$ has odd-uniform octave probability exactly $2^{-h}$. Summing over all words of length $\ell$ and $h\le H$ also identifies the complementary overflow probability by subtraction from one. This uses the finite actual octave's complete dyadic periods.

Let $G$ be the event $E_\ell\le H$ and $|E_s-2s|\le\eta k$ for all $s\le\ell$. Its complementary probability on the original octave is $O(e^{-c_0k})$ uniformly in $m,\ell$. Under the independent law $\Pr(e=r)=2^{-r}$ the centered exponential moments exist near zero and $\log\mathbb E e^{t(e-2)}=O(t^2)$. Choosing fixed positive and negative $t$ small relative to $\eta,\beta$ bounds each deviation by $2e^{-c k}$ and the fixed overflow by $e^{-c'k}$. Sum over $s=O(k)$ and apply the complete-word identity. At every date of a good block,
$$
 y_s=U^s x\ge 3^s2^{-E_s}x\ge 2^{m-bs-\eta k}\ge2^{\beta k/2}.
$$
The logarithmic correction $L_s=\sum_{i<s}\log_2(1+1/(3y_i))$ lies between zero and $\ell 2^{-\beta k/2}/(3\ln2)$, which is at most one for large $k$. The actual forward survival $f_s(x)=\prod_{i<s}3y_i/(3y_i+1)=2^{-L_s}$ is at least $1/2$. Consequently
$$
 |\log_2 y_s-\log_2 x+bs|\le\eta k+1.                             \tag{2}
$$
For each fixed $s$ the good endpoints from a fixed starting octave occupy $O(k+1)$ consecutive possible target octaves, with the bound independent of $m$.

Write $F_s$ for the terminal affine value from zero under this word, so
$$
 2^h y=3^s x+N_s,\qquad N_s=2^h F_s
     =\sum_{i=0}^{s-1}3^{s-1-i}2^{E_i}.
$$
Under the original geometric law $F_{s+1}=2^{-e_s}(3F_s+1)$, $\mathbb E2^{-e_s}=1/3$, and independence from the past gives $\mathbb E F_s=s/3$. For $K\ge1$ the odd-uniform probability of $G$ and $F_s>K$ is at most $s/(3K)$. Indeed $G$ enforces $E_s\le H$, so summing full $s$-word cylinders gives an upper bound by the unconditioned geometric probability, to which Markov applies.

At a fixed endpoint $y$ and total $h$, the positive integers $N_s$ for sources with $F_s\le K$ obey
$$
 3^{s-1}\le N_s\le K2^h,\qquad N_s\equiv2^hy\pmod{3^s}.
$$
For fixed $h,y,N_s$ there is at most one physical source, because $x=(2^hy-N_s)/3^s$. Hence there are at most $K2^h/3^s+1$ sources. When there is at least one, $3^s2^{-h}\le3K$. Their exact transported harmonic weights satisfy $f_s(x)/x=3^s2^{-h}/y$. Thus the sum of these weights for this $(h,y)$ is at most $4K/y$, including when $y<3^s$. This argument for $s\ge1$ uses the affine intercept and actual positive-source identifiability; at $s=0$ the endpoint map is the identity.

Let $A$ be any deterministic set of odd integers whose fractions $|A\cap[Y,2Y)|/Y$ in all the target octaves of (2) are at most $d\le1$. The sum of $1/y$ over its portion of those $O(k+1)$ octaves is $O((k+1)d)$. Sum the preceding rows over $0\le h\le H$ and the target set. On $G$ the unweighted harmonic sum costs at most twice the transported one. On $I_m$ odd-uniform probability is bounded by four times the unweighted harmonic sum. This proves, for every fixed $s\le\ell$,
$$
 \Pr_{I_m}(G,\ U^s x\in A)
 \ll (k+1)^2 Kd+(k+1)/K
 \ll (k+1)^2\sqrt d                                                     \tag{3}
$$
on taking $K=d^{-1/2}$ for $d>0$. If $d=0$, the event is empty. Constants may depend on the fixed block parameters. The set $A$ may contain arbitrary prescribed future-path failures of an endpoint. No independence between two consecutive physical blocks is assumed.

## A fixed number of blocks to every subcritical clock

Fix $c<C_*$, a tolerance $a>0$, and any $0<\beta<1-bc$. Suppose that sets $A_k$ satisfy
$$
 \sup_{2^m\ge2^{\beta k},\ m\in\mathbb Z}
        2^{-m}|A_k\cap[2^m,2^{m+1})|\le C e^{-d_0 k}                 \tag{4}
$$
for fixed $d_0>0$. Then outside probability $O(e^{-h k})$, simultaneously for every $0\le s\le c\log_2 n$,
$$
 |\log_2 U^s n-\log_2 n+bs|\le ak,\qquad U^s n\notin A_k .        \tag{5}
$$
Use $J=\lfloor c(k+1)\rfloor$. Choose a fixed integer $R$ large enough that the $R$ successive nearly equal pieces with integer boundary dates $0=t_0<\cdots<t_R=J$ have lengths $\le\beta k/8$ for all large $k$. Choose fixed $\eta>0$ so $2R\eta<\min(a,1-bc-\beta)$ and $\eta<\beta/8$. For block $i$ allow incoming octaves whose lower exponents satisfy
$$
 m\ge k-b t_i-i(\eta k+3).
$$
In particular all permitted starting octaves have $m\ge\beta k$ for large $k$. A good block from any permitted octave has good terminal octaves for the next stage by (2) and flooring the endpoint logarithm. Every intermediate good endpoint lies in an octave with exponent $\ge\beta k$ as well. These estimates include the $O(1)$ difference between $J$ and $ck$.

Define the future failure set at date $t_i$ as a deterministic predicate on the integer source at that date. Failure means that some subsequent block fails its local event $G$ or some remaining date reaches $A_k$. At the last cut this predicate is membership in $A_k$. Suppose the future failure set at the next cut has fraction $O(e^{-d'k})$ in every permitted octave. The current local bad block costs $O(e^{-c_0k})$. On a good block, (3) bounds the probability of entering that next exceptional set by $O((k+1)^2e^{-d'k/2})$. Each of the present $O(k+1)$ dates meets $A_k$ with probability $O((k+1)^2 e^{-d_0k/2})$ by (3) and (4). Summing and going backward across the fixed $R$ stages preserves a positive exponential rate. The local logarithmic errors along successful consecutive blocks add to at most $R(\eta k+1)<ak$. This proves (5), also with all sets $A_k$ empty.

A simple orbit has a uniform distinct-site reciprocal tail $\sum_{y>H}1/y\ll H^{-1/40}$. For an arbitrary single visitor use the distinct state set of its full forward path, obtained by taking simple prefixes or one traverse of a cycle. A union from $O(2^{\epsilon k})$ starting integers therefore has fraction $O(2^{\epsilon k}Y^{-1/40})$ in $[Y,2Y)$. Choose $40\epsilon<\beta<1-bc$ in (4) to obtain the sparse-visitor theorem above. The horizon of the competing visitors is completely unrestricted. [Resident simple-path packing source](https://github.com/GettysburgResearch/collatz/blob/bf7d52e78631954a9fd35e4ce973acd27738fc80/research/unconventional-20261126/trace/ANNULAR_ESCAPE_CURRENT.md)

## Recognition of every bad ordinary orbit

If $n$ reaches one, its ordinary word eventually has only exponent two. No point in that orbit is permanently safe. Conversely, if $n$ never reaches one, every $y_i=U^i n$ is at least three. Let $D_j=7j/4-E_j(n)$ and $d=7/4-\log_2(10/3)>0$. From $2^{E_j}=(n/y_j)\prod_{i<j}(3+1/y_i)$ we have
$$
 D_j\ge dj-\log_2(n/3).
$$
Hence $D_j\to+\infty$, and at its earliest global minimum $t$ we have $D_t\le D_0=0$. Every future cumulative debt from $y_t$ is nonnegative, so $y_t\in\mathcal P$ with $t\le d^{-1}\log_2(n/3)$. This linear bound holds for each individual bad source. The comparison $d>0$ is the elementary integer inequality $10^4<2^7 3^4$.

Let $D$ denote the union of the least positive odd seeds of all finite accepted words $4E_j\le7j$ in PR 201. A permanently safe source eventually equals its own least seed since its total clock tends to infinity, so $\mathcal P\subset D$. The earlier principal-seed count gives $|D\cap[Y,2Y)|\ll Y^{H_2(4/7)}$ with $H_2(4/7)<1$. Indeed if $Y=2^m$ and an accepted word has least seed in this octave then $E_{\rm end}\ge m$. At the first odd clock $i$ with $E_i\ge m$, the first $m$ shortcut steps include exactly $i\ge4m/7$ odd departures. Every such binary parity prefix has one residue modulo $2^m$, giving the elementary upper binomial tail count. [Principal seeds and finite trace](https://github.com/GettysburgResearch/collatz/blob/807d67ab049f1646398d8ca8c20948cdc1d87742/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md)

Fix a small $u>0$ and take $j_0=\lfloor(C_*-u)k\rfloor$. Using $A_k=D$ and $a=u$ in (5) with $c=C_*-u$, we find that all dates through $j_0$ miss $\mathcal P$ and $\log_2 y_{j_0}\le (bu+u)k+O(1)$, on the same good octave set. If the source is bad, apply the deterministic bound just proved to the actual $y_{j_0}$. Thus the first entrance satisfies
$$
 j_0<\tau(n)\le j_0+d^{-1}\log_2 y_{j_0}.
$$
The elementary bound $U(x)+1\le(3/2)(x+1)$ also gives
$$
 \log_2 U^{\tau(n)}n\le
 \log_2(y_{j_0}+1)+(\tau(n)-j_0)\log_2(3/2).
$$
Since $u$ may be chosen arbitrarily small depending on $\delta$ and $d$, these estimates imply (1), with the bounded difference between $k$ and $\log_2 n$ absorbed for large $k$. There is also a direct lower bound for permanent entry using the known trajectory envelope alone. For a proposed permanent visit at $t\le(C_*-u)k$, extend by $L=\lfloor uk/2\rfloor$ further steps, still at a subcritical clock. Permanence forces $\log_2(y_{t+L}/y_t)\ge(\log_2 3-7/4)L$. The two-sided envelope forces this quantity to be at most $-bL+2ak$ outside the same type of power-saving exceptional set. Since $b+\log_2 3-7/4=1/4$, these bounds conflict for $a$ sufficiently small relative to $u$. Thus the permanent-entry timing can alternatively be deduced from Inselmann’s existing envelope and the coercive debt argument. The sparseness estimate actually protects the entire subcritical window against every finite-depth principal seed, including those whose later gate fails.

Inselmann, Theorem 3.8, already gives the critical odd-Syracuse trajectory envelope with a power-saving exceptional set. His Theorem 2.18 gives the corresponding shortcut result, and his proof already develops iterative transport of polynomially sparse sets. The explicit positive affine row (3) is an odd-clock proof for the particular moving endpoint sets and block restarts used here. The permanent-safe first entrance is defined by an infinite *future* test and concerns all physical sources avoiding one, including possible nontrivial cycles. Its near-critical timing gives no bound on the eventual survival of any one finite-depth principal seed. That survival is the unproved requirement for vanishing of the arithmetic trace in PR 201. [Inselmann, arXiv:2402.03276v3, Theorems 2.18 and 3.8](https://arxiv.org/pdf/2402.03276)

The exact finite controls matched 3,884 complete physical word cylinders and checked 52,480 low-offset endpoint-and-clock rows. They compared flat and backward evaluation of future failures on 16,128 ordinary sources with 4,480 shared starting states across the stages. A finite-horizon suffix-minimum check covers 16,383 true sources and 5,804 suffixes with at least five safe letters. These finite suffixes test the deterministic argument without assuming an actual permanently safe source exists.

Prepared by the independent all-height auditor, 27 November 2026 UTC.
