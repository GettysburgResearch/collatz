# Simultaneous physical parity tests through a polylogarithmic first passage

Use the ordinary positive shortcut map `T`. Write $p_b(z)$ for its odd-input count over the first $b$ steps, $a=\log_2(2/\sqrt3)$, $d=\log_2 R$ and $\tau_Y(n)=\inf\{t\ge0:T^t n<Y\}$. An infinite hitting time is allowed. Sources run through any fixed interval $[cR,CR]$ with $0<c<C$. All error counts are absolute counts of original sources and therefore still bound an arbitrary source selection by intersection.

**Theorem.** Fix $A>0$ and $0<\eta<a$. There are constants $K,D>0$ such that with $b=\lceil K\log_2 d\rceil$ and $M=d^D$, apart from $O_{A,\eta,c,C}(R d^{-A})$ original sources, one has
\[
 \tau_M(n)\le \frac{d+O_{c,C}(1)}{a-\eta},\qquad
 |p_b(T^s n)-b/2|<b/40\quad(0\le s\le\tau_M(n)+b).
 \tag{1}
\]
In particular these sliding tests extend $b$ clocks past the first passage. The assertion concerns the entire listed range of starting clocks, including choices made after seeing the future. It supplies absolute source-count bounds through this range. It puts no bound on a later mark, on the time to reach one from the landing integer, or on a fixed-floor hitting time.

## First-entrance fibers

If $n\ge Y$ and $t=\tau_Y(n)\le H$, write $z=T^t n$. Every earlier input is at least $Y$ and $Y/2\le z<Y$ because one shortcut step decreases a positive input by at most a factor of two. With $p=p_t(n)$ and $F=3^p2^{-t}$, multiplication of the exact odd-step corrections gives
\[
 1\le z/(Fn)\le(1+1/(3Y))^t .                                  \tag{2}
\]
For fixed $(t,p,z)$ any two possible sources $n_1\le n_2$ obey $n_2\le (1+1/(3Y))^t n_1$. For $1\le H\le Y$ and $n_i\le CR$ the fiber size is $O_C(1+HR/Y)$. There are at most $(H+1)^2$ possible $(t,p)$. If $Y\ll R$, $B\subset\mathbb Z/2^L\mathbb Z$ has mass $\rho$ and $2^L\le Y$, complete-period covering gives $O(Y\rho)$ possible integers $z$ in the entry band. Thus
\[
 \#\{n\in[cR,CR]: n\ge Y,\ \tau_Y(n)\le H,\ T^{\tau_Y(n)}n\bmod 2^L\in B\}
       \ll_{c,C} (H+1)^3 R\rho .                              \tag{3}
\]
The implicit bound on $Y/R$ can be any fixed constant, absorbed into the implied constant. Tests can depend on the threshold, or even on $t,p$ if they have the same uniform mass bound and the cover is taken separately for each $(t,p)$. No uniformity of the stopped distribution is assumed. The ordinary prefix and exact fixed-fiber comparisons behind (2) are in `PostDescentFibers.lean`. For integer $Y>0$, $t≤3Y$, and sources at most $U$, `FirstPassageMarks.lean` proves the exact cardinal bound $1+\lfloor tU/(3Y)\rfloor$ for each $(t,p,z)$ fiber. Indeed $K=3Y$ satisfies $(K+1)^t(K-t)\le K^{t+1}$. Combining it with $K^tn_2\le (K+1)^tn_1$ gives $K(n_2-n_1)\le tn_2\le tU$. The module also checks the entry band. The residue-covering estimate, multistage schedule and sliding-window conclusion are written proofs.

## Descent and all sliding tests in one sample

Let $Y_0=(C+1)R$, $\lambda=1-(a-\eta)/2$, $Y_{i+1}=Y_i^\lambda$, $L_i=\log_2Y_i$, $k_i=\lfloor L_i/2\rfloor$. Stop the schedule at the first $J$ with $Y_J\le M$. Then $J=O_\eta(\log d)$, $Y_i>M$ for $i<J$, and
\[
 \sum_{i<J} k_i\le \frac{\log_2Y_0}{a-\eta} .                 \tag{4}
\]
Take $H$ to be the ceiling on the right. Large $R$ ensures $Y_1<cR$ and $M>H$. At $i=0$ take the actual source $z=n$ at time zero; thereafter use its first entrance to $Y_i$. All the latter thresholds are below the original source.

Choose $\epsilon=\eta/(2\log_2 3)$. A length-$k_i+3b$ parity word is declared exceptional if its first $k_i$ bits contain more than $(1/2+\epsilon)k_i$ odd bits, or if some length-$b$ subword starting at $0\le l\le k_i+b$ differs from $b/2$ by at least $b/40$. (The unused final bits are harmless.) Parity coding on a full $2^{k_i+3b}$ grid is bijective: after any fixed prefix the two next binary lifts have opposite next parities, by the affine formula with odd high-quotient coefficient. Hoeffding and a union bound give grid mass
\[
 \rho_i\le e^{-2\epsilon^2 k_i}+2(k_i+b+1)e^{-b/800}.         \tag{5}
\]
Choose $K$ so large that $e^{-b/800}\le d^{-A-7}$ for large $R$. Choose $D>7K+7$ sufficiently large that $k_i+3b\le L_i$ and $e^{-2\epsilon^2 k_i}\le d^{-A-6}$ for every $i<J$. The first condition allows exactly this *entire* set of bad words to be tested in (3). At $i=0$ ordinary complete-period covering directly costs $O_{c,C}(R\rho_0)$. At later stages apply (3) to sources with $\tau_{Y_i}\le H$, costing $O(d^3R\rho_i)$ at each stage. Taking the union over all these events costs $O(R d^{-A})$, by (4), (5), $k_i\ll d$, and $J=O(\log d)$.

For verification that the good blocks force timely entry, the ordinary affine identity gives $T^k z\le 3^{p_k(z)}(2^{-k}z+1/3)$. Indeed, in $T^kz/3^{p_k(z)}$, the additive term from an odd input at clock $j$ is $2^{j-k}/3^{p_{j+1}(z)}$. Their sum is less than $1/3$. At the $i$-th entry $z\le Y_i$. A good word gives
\[
 T^{k_i}z\le Y_i 2^{-(a-\eta/2)k_i}(1+2^{k_i}/(3Y_i))< Y_i^\lambda
\]
for large $R$, uniformly in $i<J$ since $L_i>\log_2M\to\infty$. The strict margin $\eta L_i/4$ in the exponent absorbs the floor and the multiplicative constant. Thus, inductively, every first entrance to $Y_{i+1}$ occurs within $k_i$ more clocks, and by (4) occurs by $H$. The starting intervals $[\tau_{Y_i},\tau_{Y_{i+1}}+b]$, taking $\tau_{Y_0}=0$, cover $[0,\tau_M+b]$ because $Y_J\le M$. The sliding tests in the corresponding good word cover all those clocks. This proves (1), using the actual sum (4) for its exact upper time bound.

## The two actual head arms and the remaining low-entrance law

Set $R=81^j$, $7R\le x<8R$, $m=\lfloor x/81\rfloor$. Applying (1) to both arms costs $O(Rd^{-A})$ original children, since each parent occurs at most 81 times. Outside this exception, for every $s\le\min(\tau_M(x),\tau_M(m))+b$,
\[
 |p_b(T^s x)-p_b(T^s m)|< b/20 < b/16 .                        \tag{6}
\]
Neither signed all-future Pliss mark can start in this range. Furthermore, if one arm has already reached the $1,2$ cycle by $s$ and $s\le \tau_M(\text{other arm})+b$, that cycle's $b$-block differs from $b/2$ by at most $1/2$. Its excess with the other arm is at most $b/40+1/2<b/16$ for large $R$. This locates the obstruction on actual sources with summable relative exceptional counts for $A>1$. A discordant pair can still have all its positive-density marks later.

There is an exact finite reduction at each scale. On timely entrance of both arms retain the ordered pair of actual first-entrance integers $(v,w)\in[M/2,M)^2$. Let $W_j(v,w)$ be the number of these original children, counting only those with both entrance times at most $H$. If $f$ is the basin-of-one color, then its number of discordant head edges differs from $\sum_{v,w}W_j(v,w)\mathbf1_{f(v)\ne f(w)}$ by $O(Rd^{-A})$. This follows from invariance along each physical arm; weights count their joint law. Consequently summability over $j$ of this weighted discordance divided by $81^j$ suffices under the fixed-target positive-density input in `HEAD_EDGE_RIGIDITY.md` and `MACROSCOPIC_PAIR_CLOSURE.md`. Summability follows likewise if an upper bound counts all as-yet uncertified entrance pairs with these actual multiplicities. No comparable estimate for the joint entrance weights on discordant pairs has been established.

## Relation to existing first-passage results

Idris Ali Shaik's 2026 preprint [Polylogarithmic Descent for Almost All Collatz Orbits in Natural Density](https://shaikidris.github.io/polylog/paper/) uses original-source first-passage counts at descending thresholds. Theorem 1.1 and Corollary 1.2 supply sharper stand-alone landing exponents and two-sided clocks. The application here is to simultaneous short sliding windows and anticipative two-arm marks, with the elementary coarse fiber bound (3). Lech Mazur's [2026 natural-density log-time preprint](https://www.proofatlas.ai/papers/natural-density-log-time-collatz/Mazur_Natural_Density_Collatz_Orbits_in_Logarithmic_Time_v2.pdf) gives an ordinary-map hitting statement at any prescribed diverging height. Neither landing statement identifies the eventual colors of the two physical landing values. Universal convergence is open.
