# The scale of two Collatz arrival clocks in short ordinary intervals

Let $T(2n)=n$ and $T(2n+1)=3n+2$. Choose any set $A\subseteq[1,M]\cap\mathbb N$ of positive targets. From an ordinary positive start, record its first landing site $y\in A$, the number $\tau$ of shortcut steps to that visit, and the number $p$ of odd departures before it. Give starts never reaching $A$ one separate symbol $\partial$. For an integer modulus $m\ge1$, let $\mu_{I,m}$ be the law of $(y,\tau\bmod m,p\bmod m)$ and $\partial$ on uniformly sampled integers in an interval $I$. Write $\lambda_I$ for its landing-site marginal. For a row law $\lambda$, write $U_m\lambda$ for the law that spreads each finite row uniformly over its $m^2$ residue pairs and leaves the cemetery mass in place. Total variation is half the sum of absolute differences. Logs with a subscript 2 are in bits.

Take a real octave $[X,2X)$ and a contained half-open interval $I=[x,2^\rho x)$ of logarithmic width $0<\rho\le1$. Set
\[
 L=\min\{\log_2(X/M),\ \log_2(X\rho)\},\qquad W=\sqrt L,\qquad \alpha=\log_2 3 .
\]
We state asymptotics with $L\to\infty$. No limit assumption on the octave landing law is needed.

**Short-interval theorem.** For every denominator $q$ of a continued-fraction convergent to $\alpha$,
\[
 d_{\rm TV}(\mu_{I,m},U_m\lambda_{[X,2X)})
   \ \ll\ \frac{mq}{W}+\frac{m}{\rho q}.                              \tag{1}
\]
The constant is independent of the interval, floor, target set, landing labels and modulus. In particular, one can take any function of the landing label, including an invariant partition of paths which miss $A$ provided that partition is constant along every such edge. With no clocks, the same argument applies to any orbit label constant along all edges above $M$, with total error summed over the labels.

Let $Q\le\sqrt{W/\rho}<Q'$ be consecutive convergent denominators and put
\[
       H(W,\rho)=\max\{1,\rho Q,W/Q'\}.                               \tag{2}
\]
Using whichever of $Q,Q'$ gives the smaller bound, and the trivial bound one if necessary, (1) is $O(\min\{1,m/H(W,\rho)\})$. Thus $m=o(H)$ gives total variation tending to zero. The same holds with the actual local marginal $\lambda_I$ by contraction of total variation and the triangle inequality.

**Sharpness in actual first passages.** Fix $\alpha/2<\gamma<1$ and a finite $B\ge0$. Take $M=\lfloor X^\gamma\rfloor$, $A=[1,M]\cap\mathbb N$ and $(\log X)^{-B}\le\rho\le1$. Whenever $m/H(W,\rho)\to\infty$,
\[
                      d_{\rm TV}(\mu_{I,m},U_m\lambda_I)\longrightarrow1 .  \tag{3}
\]
The convergence is uniform over positions of the indicated windows and holds also with any comparison row law in place of $\lambda_I$. Only the ordinary parity bijection, elementary concentration and the physical step formula enter this direction. At $m$ comparable to $H$ neither limiting assertion is made.

For a full octave, $H(W,1)\le\sqrt W$. At scales $W=q^2$ for a convergent denominator $q$, it equals $q=L^{1/4}$. Rounding the logarithmic scale by $O(1)$ preserves comparability, including at an endpoint. Thus the fourth root is attained on some scales. Consecutive-denominator gaps remain in the all-scale answer. For an explicit, weaker range on every scale, Rhin's linear-forms bound implies $Q'\ll Q^{13.3}$. Minimizing $\max(\rho Q,c W Q^{-13.3})$ gives $H\gg(\rho^{13.3}W)^{1/14.3}$. This yields growing moduli and shrinking windows together whenever $\rho\ge L^{-b}$, $m\le L^a$ and $14.3a+13.3b<1/2$. [Rozier and Terracol, Proposition 6.3, quoting Rhin](https://arxiv.org/pdf/2502.00948v5#page=19)

## Integer comparisons inside a moving window

Let $g(n)$ be the point mass of the recorded mark, and let $S$ increment its shortcut residue, $P$ its odd residue. These commuting permutations fix $\partial$. Above $M$ the even edge gives $g(2n)=Sg(n)$ and the odd edge gives $g(2n+1)=SPg(3n+2)$. If two neighboring starts counted-fuse by time $k$ (their values and numbers of odd departures agree) and neither visits $A$ through that time, their full marks agree, including nonarrival.

For adjacent integer starts drawn from any length-$D$ interval, the number failing to counted-fuse by $k$ is
\[
                   O(D/\sqrt{k+1}+2^k).                                \tag{4}
\]
Indeed the Haar failure fraction is $O((k+1)^{-1/2})$ and the event depends only on the initial residue modulo $2^k$. Each full period is exact and the incomplete remainder costs at most one period. Applying this to containing intervals of twice or three times the length bounds the failures on the classes appearing below. This uses a fixed two-start result only. [Weaver, Paper 124, Theorem 1 and integer transfer](https://rstation.ai/problems/collatz/papers/124/v1) · [Leen and Weaver comparison of the pair input](https://rstation.ai/r/collatz/posts/20)

Use $k=\lfloor L/3\rfloor$. On compact exponent ranges below, every initial value is at least $X-O(1)$ and every iterate through $k$ is at least the start divided by $2^k$, hence exceeds $M$ for large $L$. Write $g_t=g(\lfloor X2^t\rfloor)$. In any subinterval $J\subseteq[0,3]$ of length at most $\rho$, (4) gives the two bounds
\[
  \int_J \|g_{t+1}-Sg_t\|_1\,dt+
  \int_J \|g_{t+\alpha}-P^{-1}g_t\|_1\,dt
            \ll |J|/W+2^k/X.                                         \tag{5}
\]
For $n=\lfloor X2^t\rfloor$, the doubled index is one of $2n,2n+1$. The tripled index is one of $3n,3n+1,3n+2$. Away from the three adjacent comparisons starting at $2n,3n,3n+1$, all available neighbors agree in each group. Substituting both true edges then gives the displayed permutations. Each integer cell has logarithmic length $O(1/X)$, and $J$ intersects $O(X|J|+1)$ cells. This accounts for the rounding in (5) even on a very short subpiece. Our choice ensures $2^k/(X\rho)\ll1/W$.

## The rotation and the two finite clocks

On a circle of circumference $m$, set $F(u+j)=S^j g_u$ for $0\le u<1$, $j=0,\ldots,m-1$. On its product with $\mathbb Z/m$ put $K(z,v)=P^vF(z)$. All values are probability measures. Haar averaging $K$ over this product gives $U_m\lambda^\log$, where $\lambda^\log$ is the logarithmically uniform landing marginal on the full octave before endpoint rounding. This follows by averaging independently over the integer part of $z$ and over $v$.

Consider $R(z,v)=(z+\alpha,v+1)$. Relative to any arc of length $\rho$, the integral error of $K\circ R-K$ is $O(\rho/W)$, uniformly in $v$. Indeed at $z=j+u$ let $d=\lfloor u+\alpha\rfloor\in\{1,2\}$. The definition gives $F(z+\alpha)=S^{j+d}g_{u+\alpha-d}$. At most two doubling comparisons in (5) replace this by $S^jg_{u+\alpha}$, then tripling replaces that by $S^jP^{-1}g_u$. Split an arc at the bounded number of relevant integer boundaries and fractional carries and apply (5) on each subpiece. The interval arguments needed there stay in $[0,3]$. The factor $P^{v+1}$ removes the last shift. The integer part $j$ never enters the error, even when $m$ grows.

Start $z$ uniformly in *ordinary real height* in the requested interval and take $v=0$. In circle coordinates this is the translated density
\[
 k_\rho(u)=\frac{(\log2)2^u}{2^\rho-1}\,\mathbf1_{[0,\rho)}(u).
\]
It integrates to one, has sup norm and total variation $O(1/\rho)$, and all its translates have the same bounds. The preceding one-step estimate and telescoping show that averaging its first $mq$ iterates of $R$ changes the initial mean of $K$ by $O(mq/W)$ in the sum norm.

For each of the $m$ vertical classes the horizontal orbit centers of this average, normalized by the circumference $m$, are a translate of $b\alpha\bmod1$, $0\le b<q$. If $a/q$ is the convergent, each center differs from its corresponding point on the regular $q$-grid by at most $1/q$. The empirical mass of every arc thus differs from its length by $O(1/q)$. Integrating a function of bounded variation against this discrepancy costs at most $O(1/q)$ times its variation, by integration by parts or by writing it as a difference of increasing functions. Apply this at each fixed horizontal location to the translated density in circumference-one variables. Its variation is $O(m/\rho)$ after multiplying by $m$ to give integral one. The resulting averaged density differs from the uniform horizontal density, pointwise relative to it, by $O(m/(q\rho))$. Every vertical coordinate had exactly $q$ samples. Integrating the probability-measure-valued $K$ costs the same total error, with no dependence on the number of rows or marks.

Real-uniform height followed by flooring changes the integer-uniform law by $O(1/(X\rho))$ at the two ends. One may therefore compare $\mu_{I,m}$ with $U_m\lambda^\log$ at the cost on the right of (1). Apply this comparison again with $m=1,\rho=1$ on the full octave to replace $\lambda^\log$ by its ordinary integer marginal. The larger full-octave $L$ only reduces that error. This proves (1), also for an arbitrary discrete set of landing labels.

## A matching obstruction before the binary digit budget runs out

Under the assumptions of (3), $L=\log_2(X/M)$ eventually. Set $d=1-\alpha/2>0$, $k_*=L/d$. Choose a constant $\eta$ strictly between $(1-\gamma)/d$ and 1, and let $J=\lfloor\eta\log_2 X\rfloor$. This choice is possible precisely because $\gamma>\alpha/2$. The parity-word bijection on a full period of length $2^J$ makes the first $J$ shortcut parities independent fair bits. The total variation error for the integer sample in the interval is $O(2^J/(X\rho))=o(1)$, uniformly over the stated positions and widths.

For any $\epsilon>0$, Kolmogorov's maximal inequality gives a constant $K_\epsilon$ such that, with probability at least $1-\epsilon-o(1)$, every partial odd count up to $J$ differs from half its clock by at most $K_\epsilon W$. Here $J=O_\gamma(W^2)$. Up to and including first landing, the exact logarithmic formula at time $j$ is
\[
 \log_2 T^j n=\log_2 n-j+\alpha p_j+D_j,\qquad
 D_j=\sum_{i<j,\ T^in\ {\rm odd}}\log_2(1+1/(3T^i n)),\quad
 0\le D_j\le C J/M\quad(j\le J).                                    \tag{6}
\]
The bound holds while all departing sites exceed $M$. If the orbit had not landed by $k_*+C_\epsilon W$ rounded up, (6) would put it below the floor at that date. A landing before $k_*-C_\epsilon W$ is excluded by the same equation using $D_j\ge0$. Both dates lie below $J$ eventually. Thus, on the good event, $|\tau-k_*|+|p-k_*/2|=O_\epsilon(W)$. Constants can depend on fixed $\gamma$.

Write $P_0/Q$ for the convergent with denominator $Q$ from (2). Its error satisfies $|Q\alpha-P_0|<1/Q'$. For each landing row $y$, all good starts in that row therefore obey
\[
 Q\tau-P_0p
  =Q\log_2(x/y)+(Q\alpha-P_0)k_*/2
          +O_\epsilon(Q\rho+QJ/M+W/Q').                              \tag{7}
\]
Indeed (6) gives $\tau=\log_2(n/y)+\alpha p+D_\tau$. The floor and width assumptions give $J/M=o(\rho)$. After reducing (7) modulo $m$, there are at most $O_\epsilon(1+Q\rho+W/Q')=O_\epsilon(H)$ allowed scalar residues in each row, even if the center crosses zero. Since $\gcd(Q,P_0)=1$, the map $(r,s)\mapsto Qr-P_0s$ from $(\mathbb Z/m)^2$ onto $\mathbb Z/m$ is surjective, with equal fibers. A distribution uniform on each row therefore assigns the union of these row-dependent windows mass at most $O_\epsilon(H/m)$, regardless of that distribution's row weights. The true law assigns it mass at least $1-\epsilon-o(1)$. Send $X$ to infinity first, then $\epsilon$ to zero. This proves (3).

On the high barrier, (3) uses only the first $J$ low bits of the ordinary sources. On the upper side, (1) permits a fixed small target and also accounts for every start which never reaches it. The count of such starts is part of the input row law, and its vanishing is still open.

## Ordinary common blocks with prescribed clocks

The same comparison can keep an entire growing block of starts. For each sampled $n\in I$ test whether $n,n+1,\ldots,n+D-1$ have equal positions and equal odd counts after $k=\lfloor L/3\rfloor$ steps. Theorem 1 of Weaver 124 bounds the fraction failing this test on a complete binary period by $C(1+\log D)^4/\sqrt{k+1}$. Transferring to $I$ adds $O(2^k/(X\rho))$. Every tested path stays above $M$ through $k$. A counted merger therefore ensures identical first landing, shortcut clock and odd clock for the entire block, or nonarrival of the whole block. The comparison in (1) holds with the additional error $O((1+\log D)^4/W)$ when failures receive a distinct error symbol. The points in a block are sampled through its left endpoint; they need not all lie in the sampling interval. Trimming the last $D-1$ endpoints costs at most $O(D/(X\rho))$ if containment is desired. [Weaver 124, Theorem 1 and Corollary 4](https://rstation.ai/problems/collatz/papers/124/v1)

For example, fix an odd ternary-unit target $a$, take $A=\{a\}$, and assume its predecessor set has positive lower natural density. Its fraction on every sufficiently large full octave has an $a$-dependent positive lower bound. To see this with only lower density, choose a fixed $e>0$ giving at least $eX$ predecessors below $X$. At least $eX/2-O(1)$ lie in $[eX/2,X]$. Double each into $[X,2X)$; the shortcut orbit of the doubled source still visits $a$, and the multiplicity is at most $2+\lceil\log_2(2/e)\rceil$. The external Mazur predecessor theorem supplies this premise for every fixed odd ternary unit, including one on a hypothetical nonconvergent path. [Mazur, *Positive lower density of Collatz predecessors*](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

Consequently, if
\[
         m^3/H(W,\rho)\to0,\qquad
         m^2(1+\log D)^4/W\to0 ,
\]
then every such interval has $\gg_a |I|/m^2$ left endpoints of blocks whose members all visit $a$ at the same actual time and with the same actual odd count, meeting any prescribed pair of residues modulo $m$. This uses a total error $o(1/m^2)$, as required for the individual pairs. The estimate holds on each sufficiently large octave. In the inverse-logarithmic shrinking windows allowed by Rhin, both $m$ and $D$ can grow. The conclusion quantifies the supply around a fixed target, conditional only on its own lower density for this last corollary. It gives no eventual destination for that target.

**Comparison.** Paper 124 already supplies the growing-block counted merger on any translated integer interval. Leen and Weaver treat stable labels and arrival laws within input progressions and prime samples. Paper 191 treats simultaneous shortcut and ordinary passage clocks into deep levels in translated intervals. Those results concern different marginal or sampling variables. The estimates here keep the entire distribution of the landing site, including nonarrival, and address the joint *output* residues with a modulus and spatial window varying simultaneously. The matching high-floor bound (3) uses the continued-fraction scale of the two clocks. [Weaver 13, prior synchronization and clock laws](https://rstation.ai/problems/collatz/papers/13/v1) · [Weaver 191, translated interval passage](https://rstation.ai/problems/collatz/papers/191/v2) · [Paper 233, prime sampling and input divisibility](https://rstation.ai/problems/collatz/papers/233) · [Weaver 175, terminal phases](https://rstation.ai/problems/collatz/papers/175)
