# Independent pair-word frequencies through the full physical critical time

Put $a=\log(4/3)/2$ and $\mu=1/a$. Fix positive odd $A,B$ with $B/A\notin3^{\mathbb Z}$ and arbitrary integer $b_1,b_2$. Give $n\in[X,2X)$ the uniform counting law. For $x_1=An+b_1$, $x_2=Bn+b_2$, any fixed pair $w_1,w_2$ of length-$k$ parity words and any deterministic $t=t(X)\to\infty$ satisfying $\limsup t/\log X\le\mu$,
\[
   \frac{1}{t}\#\{0\le j<t: \text{ the actual parities from }T^jx_i
        \text{ begin }w_i\ (i=1,2)\}\longrightarrow 4^{-k}
                       \quad\text{in probability}.                        \tag{1}
\]
The same holds at every pair in a fixed pairwise nonsmooth finite family. In particular the actual unequal-parity fraction converges to $1/2$ all the way to the physical critical clock $\mu\log X$, while the direct binary prefix has only $\log_2 X$ reliable random positions. The observation times may also be random with $t_X/\log X\to\mu$ in probability, since replacing them by $\lfloor\mu\log X\rfloor$ changes a bounded time average by $o_{\Pr}(1)$. Thus the source-qualified scalar true first-minimum clock law transfers this conclusion through that actual clock, or on any chosen positive-density conditioning event where a specified first-visit clock divided by $\log X$ tends to $\mu$. No limit on a three-or-more-way complete parity word is asserted. The joint Brownian invariance principle from the [earlier joining](MULTIPLIER_BERNOULLI_JOINING.md) was proved directly through the binary horizon only.

The probability proof of (1) uses that joining's native two-adic line representation and its fixed Bugeaud–Laurent logarithm bound. It does not invoke a signed first-landing kernel, a target-density theorem or an assumption on eventual fate. The time exponent $\mu$ comes from the positive fair logarithmic loss $a$.

## Quantitative binary block estimate with uniform moving coefficients

Fix a desired word length $k$, error $\epsilon>0$, and exponent bound $D<\infty$. Take a Haar two-adic common source $u$ and odd slopes $A3^{e_1},B3^{e_2}$, where $|e_2-e_1|\le M^D$ for a block of length $M$. The slopes may be interpreted as two-adic units; the application has nonnegative exponents. Both coordinate offsets may be arbitrary. For constants depending on the fixed data, uniformly in these moving parameters,
\[
  \Pr\{|\text{paired empirical word frequency}-4^{-k}|>\epsilon\}
         \le C\exp[-cM/(\log(2+M))^{C'}].                                \tag{2}
\]
Here windows whose final digits extend past the block can be omitted at an $O(k/M)$ cost. We give the details needed for the high probability and the uniformity; almost-sure genericity without a rate would not justify the transfer.

After any binary prefix, the actual state pair is Haar uniform on a line $Y=\alpha X+\beta$, with $\alpha=(B/A)3^d$. At the successive mixed departures $d=d_0+S_j$, $d_0=e_2-e_1$, and $S_j$ is an ordinary simple symmetric walk. The physical holding length $W_j$ through its next mixed departure is either deterministic and at most $1+v(d)$, or equal to $1+v(d)+G$ for a fresh geometric valuation $G$ of mean one. Here $v(d)=v_2(B3^d-A)$, finite for every exponent. These are the conditional native affine identities in [the Hamming proof](MULTIPLIER_PARITY_SEPARATION.md), at the beginning of each holding interval. In particular for any predictable indicator $I_j$ the centered increments $I_j(W_j-\mathbb E_jW_j)$ have uniformly bounded conditional exponential moments near the origin, in the form $\mathbb E_j e^{hI_j(W_j-\mathbb E_j W_j)}\le e^{C h^2}$ for $|h|\le h_0$. This follows directly from the centered geometric generating function or from Taylor's formula and its fixed exponential moment. Their sum over $j<M$ exceeds $\delta M$ with probability at most $e^{-c_\delta M}$.

For any fixed level $l\ge3$ and direction cell modulo $2^l$, the possible $d$ form an empty set or one class $J$ modulo $2^{l-2}$. Its occupation among the first $M$ **physical dates** is at most $\sum_{j<M}1_J(d_0+S_j)W_j$ since $W_j\ge1$; the nonnegative sum includes the unfinished interval if any. We need bound this sum divided by $M$. Uniformly over $|d-d_0|\le M$, the logarithmic-form estimate gives $v(d)\le C_{A,B,D}\log^2(2+M)$. Set $K=\lceil5\log_2\log(3+M)\rceil$, $q=2^{K-2}$. For large $M$, both $f=(2+\min(v,K))1_J$ and the indicator $g=1_{v\ge K}$ are periodic modulo $q$. An empty high-valuation class is allowed. Their uniform means obey
\[
       \bar f\le C_0(l+3)2^{-l},\qquad
       \bar g\le 1/q.
\]
Indeed at levels above $l$, inside a compatible class the frequencies fall by $1/2$ per further level; below $l$ charge at most $l$ per representative. The order of three modulo $2^s$ is $2^{s-2}$ for $s\ge3$. Small levels are absorbed in $C_0$.

For a periodic test $b$ on this $q$-cycle the finite difference Poisson equation $(I-P)U=b-\bar b$ has $\|U\|_\infty\le Cq^2\|b\|_\infty$, by summing discrete differences twice as in the cited Hamming proof. Along the walk, the centered sum is the difference of two such endpoint potentials plus a martingale of increments bounded by $2\|U\|_\infty$, uniformly in $d_0$. Azuma applied to $f$ with tolerance $\delta$ and to $g$ with tolerance $\delta/(C_{A,B,D}\log^2(2+M))$ fails with total probability $O_\delta(\exp[-c_\delta M/(\log(2+M))^{C'}])$. The potential endpoint errors are polylogarithmic. The high excess contributes at most
$C_{A,B,D}\log^2(2+M)(\bar g+\delta/(C_{A,B,D}\log^2(2+M)))\le 2\delta$ for large $M$. Adding the centered holding estimate proves the empirical physical direction bound $C_0(l+3)2^{-l}+4\delta$. This holds at every one of any fixed finite list of levels and cells with the stated failure bound.

For completeness fix a large level $K_0$, to be chosen in terms of $k,\epsilon$ and independent of $M$. For every pair-state cylinder at depth $K_0$ its empirical mass differs from the time average of its conditional uniform-line probability by at most $\delta$ except with probability $O_{K_0}(e^{-c_{\delta,K_0}M})$: split dates into their $K_0$ residue classes so each test minus its conditional expectation is a bounded martingale difference. The finite mixture of all observed line parameters has, by the preceding direction bounds through $K_0$, the depth-$K_0$ collision estimate
\[
       4^{-K_0}\bigl(C(K_0+1)^2+C2^{K_0}\delta\bigr).
\]
This is the exact line intersection count from the [dyadic incidence proof](MULTIPLIER_BERNOULLI_JOINING.md): two independent directions agree modulo $2^l$ with probability at most the maximum cell mass there. Choose $\delta$ small enough at this fixed level that both the extra collision term and the change of finite entropy from the empirical cylinder approximation are bounded by an absolute constant. The entropy of the empirical paired $K_0$-block distribution is then at least $K_0\log4-O(\log(2+K_0))$. State residues and corresponding parity words are bijective at each coordinate.

Choose $K_0$ a multiple of $k$. The marginal empirical distribution of a $k$-block beginning at a fixed offset $a\le K_0-k$ inside that $K_0$-block differs in total variation by at most $K_0/M$ from the one beginning at date zero within the block. This follows by shifting the time-average index and dropping only its two boundary regions. Entropy subadditivity and continuity on the fixed $4^k$ alphabet bound the entropy of the long block above by $(K_0/k)(H_k+o_M(1))$, where $H_k$ is the empirical $k$-block entropy. Thus $k\log4-H_k\le C k\log(2+K_0)/K_0+o_M(1)$. Choose $K_0$ sufficiently large first, then $\delta$ sufficiently small. Pinsker's inequality gives the desired $\epsilon$ proximity to the uniform paired $k$-block law. This proves (2) with constants uniform in all the stated moving parameters. Fixed additional terminal digits in the ordinary reading merely increase the binary prefix length by $K_0$.

## Physical epochs from a shared ordinary source

Write $L=\log X$. It suffices first to handle $t=\lfloor\lambda L\rfloor$ for fixed $0<\lambda<\mu$. Choose a fixed integer $m$ so large that each of the $m$ consecutive epochs of approximately $\lambda L/m$ dates has length $M$ satisfying
\[
           M\log2 < \tfrac12(1-a\lambda)L .
\]
Round the epoch boundaries to integers, fixing their sum. We establish inductively that outside an $o(1)$ exceptional fraction the grades of both actual paths at every date $j$ up to an epoch's end are $j/2+O(L^\beta)$ for some fixed $\beta<1$ that may increase at each of these finitely many epochs. In the first epoch the full binary prefix is sampled with bounded relative density compared to Haar on each cell because $2^{M+K_0}=o(X)$. Hence (2) gives the word conclusion there, and the fair marginal Hoeffding bound plus a union over the prefixes gives the grade estimate for any $\beta>1/2$.

At the beginning $s$ of a later epoch let $k_i=k_s(x_i)$ and $l=\min_i k_i$, and retain the good roots just described. Their absolute forward corrections at date $s$ satisfy
\[
        0\le D_i=3^{k_i}R_{i,s}/2^s\le \exp(C L^\beta).
\]
In fact a summand is bounded by $\exp(S_{i,j}-S_{i,s})$ for $j<s$, where $S_{i,j}=j\log2-k_j(x_i)\log3$. The uniform past grade bounds give $S_{i,j}-S_{i,s}=a(j-s)+O(L^\beta)$. Here $R$ is the positive finite sum in [the native fibre formula](ORDINARY_SOURCE_FIBRES.md). Define the *same* new ordinary source for both true states by
\[
        u=\left\lfloor 3^l n/2^s\right\rfloor .
\]
The exact real affine formulas, using $0\le 3^l n/2^s-u<1$, give
\[
       T^s x_i=A_i3^{k_i-l}u+e_i,\qquad
       e_i\in\mathbb Z,\quad |e_i|\le \exp(C' L^\beta).                \tag{3}
\]
Indeed the remaining terms are $A_i3^{k_i-l}$ times that fractional part, $3^{k_i} b_i/2^s$, and $D_i$. The fixed-offset term is bounded here because $k_i=s/2+O(L^\beta)$ and $s$ is a positive constant times $L$ beyond the first epoch. The finitely many slopes $A_i$ are fixed in the initial data. The powers $k_i-l$ are at most $O(L^\beta)$, and the total number of possible tag tuples $(k_1,k_2,e_1,e_2)$ is at most $\exp(C'' L^\beta)$, including the possible $l$. The tags may be arbitrary functions of $n$; we do not condition the common $u$ to be fresh.

For each admissible tag bound its bad roots from above by dropping the tag restrictions and using the full original octave under $n\mapsto\lfloor c n\rfloor$, $c=3^l/2^s$. Here $c=e^{-as+O(L^\beta)}<1$, and every resulting integer $u$ has at most $1+1/c$ preimages in the octave. Its range is an interval of length $cX+O(1)=\exp(L-as+O(L^\beta))$, larger than $2^{M+K_0}$ by an exponential factor. Consequently for any binary-prefix exceptional event of probability $q$ under a Haar $u$, the unconditional original fraction with this tag and that exception is at most $Cq$, since each residue modulo $2^{M+K_0}$ occurs at most $1+(cX+O(1))/2^{M+K_0}$ times in the common parameter interval. The estimate is relative even for very rare events. It is valid for moving offsets of either sign and preserves both true orbit paths in (3).

Now (2) has $q\le\exp[-cL/(\log L)^{C'}]$ for this epoch, uniformly in all tags, including $d_0=k_2-k_1$. The sum over the subexponential family of tags is $o(1)$. For the grade control in every future prefix take $\beta'<1$ with $2\beta'-1>\beta$. Under Haar for each fixed tag the individual future grade is binomial at every prefix, since the coefficients are odd. Hoeffding and summation bound the probability that either path ever deviates by $L^{\beta'}$ from half its new date by $O(M\exp[-cL^{2\beta'-1}])$. This too beats all the tags. Add the initial $O(L^\beta)$ errors to get the new cumulative grade bound. This closes the induction for finitely many epochs. Summing the correct frequencies, with errors chosen within the requested tolerance and a fixed number of word windows straddling boundaries, proves (1) at $t=\lfloor\lambda L\rfloor$.

For an arbitrary $t(X)$ use subsequences on which $t/L$ converges. A zero limiting ratio lies inside the direct binary horizon. At a positive ratio below $\mu$, replacing $t$ by its fixed-proportion limit changes at most $o(t)$ terms. At limiting ratio $\mu$, use $t'=(\mu-\delta)L$ and bound the leftover fraction by $O(\delta)$, then send $\delta$ to zero. The same deterministic comparison in probability gives the random-clock assertion. The typical integer source here can belong to any finite or escaping component. No individual high cycle or escaping ray has been sampled uniformly by this ordinary density argument.

[Paper 13, especially its selected killed-excursion estimates](https://rstation.ai/problems/collatz/papers/13/v1) already derives strong physical-duration concentration for smooth-multiplier interior excursions and credits Leen's earlier affine-line occupation argument. The estimate (2) here concerns every prescribed short pair word at nonsmooth base slopes, uniformly through a changing initial power of three. Its ordinary common-parameter substitution (3) is needed to extend the physical law past the binary source horizon.
