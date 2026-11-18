# Sharp power exponent of the least-predecessor density

**PROPOSED.** Let $d(\theta)$ be the limiting relative density among odd positive targets $t$ whose least positive predecessor is strictly below $\theta t$. The [ordinary-to-ternary transfer](../fixed-floor-shells/PREDECESSOR_MINIMA.md), FS-010 at commit `f222e4d`, proves existence and $d(\theta)\le\theta^2$. For an absolute $c>0$,
\[
 c\frac{\theta^2}{\sqrt{1+\log(1/\theta)}}\le d(\theta)\le\theta^2
 \qquad (0<\theta\le1).
\]
In particular the logarithmic slope equals 2 as $\theta\downarrow0$. The lower bound already holds with witnesses of one prescribed odd depth and total valuation, depending on $\theta$.

For a word of positive inverse valuation letters $a_1,\dots,a_q$ write $A_j=\sum_{i\le j}a_i$, $A=A_q$. Its source is $(2^A t-C)/3^q$, with
\[
 C=\sum_{j=1}^q 3^{j-1}2^{A-A_j}.
\]
The legality cylinder is $2^At\equiv C\pmod{3^q}$. Indeed reducing this congruence successively modulo $3^j$ recovers every prefix integrality condition, since each suffix power of 2 is a unit. For fixed $q,A$, distinct words give distinct integers $C$. For $q\ge2$, $C-3^{q-1}=2^{a_q}C_{q-1}$ with odd $C_{q-1}$. Extract the last letter by its 2-adic valuation and repeat. The fixed total recovers $a_1$.

Consider independent letters with probabilities $3\,4^{-a}$ for $a\ge1$, and write $S_m$ for the sum of $m$ letters. Conditional on $S_q=A=\lfloor4q/3\rfloor$, the compositions are uniform. The local estimates
\[
 \sup_n\Pr(S_m=n)\le K/\sqrt m,\qquad
 \Pr(S_q=\lfloor4q/3\rfloor)\ge k/\sqrt q
\]
hold with absolute constants. Indeed the mass at $n\ge m$ is $\binom{n-1}{m-1}3^m4^{-n}$, the ratio of successive masses is $n/[4(n-m+1)]$, and Stirling's formula applies at its mode $4m/3+O(1)$ and at the displayed central value.

A positive fraction of these compositions have $C\le B3^q$ for an absolute $B$. To see this let $Y=2^a/3$; then $\mathbb E Y=1$ and $r=\mathbb E\sqrt Y<1$ by strict concavity. The scaled numerator $C/3^q$ is one third of the sum over suffix lengths $0\le l<q$ of the products of the corresponding $Y$'s. The square root of each suffix product has conditional expectation at most
\[
 r^l\frac{\sup_n\Pr(S_{q-l}=n)}{\Pr(S_q=A)}
 \le K' r^l\sqrt{q/(q-l)} .
\]
This follows by conditioning on the suffix and applying independence to the complementary prefix. Sum through $l\le q/2$ by a geometric series and bound the remainder by $O(\sqrt q\,r^{q/2}/(1-r))$. Subadditivity of the square root now bounds the conditional mean of $\sqrt{C/3^q}$ absolutely. Markov's inequality gives the asserted positive fraction.

On this fraction each ternary residue has at most $1+\lfloor B\rfloor$ representatives, by distinctness of $C$. Writing $D=2^A/3^q$, the union measure of their cylinders is consequently at least
\[
 c_0\binom{A-1}{q-1}3^{-q}
 =c_0\Pr(S_q=A)D^2\ge c_1D^2/\sqrt q .
\]
When $D\le\theta$, each cylinder is in the FS-010 crossing event. Equivalently, at every sufficiently large odd representative the integral source is positive, strictly below $\theta t$, and reaches $t$. Set $b=2^{4/3}/3<1$ and $q=\max(1,\lceil\log(\theta)/\log(b)\rceil)$; then $b\theta/2\le D\le\theta$ and $q\ll1+\log(1/\theta)$. This gives the claimed bound. The exact order between the two bounds remains open.
