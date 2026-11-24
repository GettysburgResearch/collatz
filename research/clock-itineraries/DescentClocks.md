# Which inverse clocks can lower an ordinary root?

Consider a positive odd source $y$ reaching a positive odd root $q>2$ in $b>0$ odd gaps at total shortcut clock $s$. If $y\le q$, then

\[
                         5s\le8b .
\]

Indeed the sharp distortion inequality gives $59049\,2^{5s}q^5\le100000\,2^{8b}y^5$. Cancel $q^5$ after replacing $y$ by $q$ on the right. Because $100000/59049<2$ and both exponents are integers, $5s\le8b$. In particular all central clocks $|s-2b|\le\sqrt b$ force $y>q$ at every $b\ge7$. [Lean proof](DescentClocks.lean) and [sharp constant](FixedGate.md)

## A root class with no descent at any clock

For any nonempty exact word of $b$ odd gaps, its affine equation is $2^s q=3^b y+C$, where $C>0$ depends only on the ordered gaps. All odd roots compatible with that word belong to one residue modulo $3^b$. Suppose a word is legal at $q=z+2\cdot3^b d$, with $z$ positive and odd and $d>0$. Successively peeling inverse steps at $z$ gives a legal positive source $y_0$ satisfying $y=y_0+2\cdot2^s d$. Positivity follows at each peeling because an exact inverse gap of positive length has numerator $2^e u-1>0$ at each positive odd target $u$.

If $y_0\ge z$, the affine identity at $z$ forces $2^s>3^b$. Hence $y>q$. Equivalently, any weak descent at the higher root forces strict descent by the same word at every smaller positive odd representative. In particular, if $q>1$ and $q\equiv1\pmod{3^b}$, **every legal ancestor at odd depth $b$ exceeds $q$**, at every possible total clock. A smaller positive ancestor of one is impossible.

These root classes occur on ordinary converging examples at every finite depth. For any $B\ge0$ take $e=2+2\cdot3^B$ and $q=(2^e-1)/3$. Then $q>1$ is odd, reaches one in one odd gap, and $q\equiv1\pmod{3^B}$. It has no weakly smaller positive ancestor at any odd depth from one through $B$. [Theorems `downward_descent`, `no_descent_at_one_cylinder` and `converging_obstruction`](DescentClocks.lean)

## Total mass at the central and descent clocks

The external input called F in PRs #203 and #205 concerns independent positive gap lengths with probability $2^{-j}$ for length $j$. Lemma 7, equation (76), states a joint lower bound on a fixed unit cylinder modulo $3^{b+K}$, near $s=2b$, with $K\le\delta b$ and $\delta\le1/1000$. The subsequent bounded prepending step is used to cover unit residues. This audit uses only the stated range and the exact number of words. [Weaver and Wren, paper 48 v2, Lemma 7 and Theorem 8](https://rstation.ai/problems/collatz/papers/48/v2)

At $s=2b$ there are $\binom{2b-1}{b-1}\sim4^b/(2\sqrt{\pi b})$ positive words, each of mass $4^{-b}$. There are $2\cdot3^{b+K-1}$ unit residue classes. Even one word in every class requires $K\le(\log_3 4-1)b-\tfrac12\log_3 b+O(1)$. The stated extra depth is well inside that necessary capacity. The proposed central lower bound of order $4^b/(3^{b+K}\sqrt b)$ per class sums to the correct total order. This comparison checks compatibility with counting, without proving the analytic floor.

The comparison reverses when a construction needs an ancestor no larger than its root. Pool **all** clocks permitted by $5s\le8b$ at a fixed odd depth $b$. Partial sums of the positive gaps identify a word with a $b$-element subset of $\{1,\ldots,\lfloor8b/5\rfloor\}$. The number of words is exactly $\binom{\lfloor8b/5\rfloor}{b}$. Each word supplies at most one ternary root class modulo $3^b$, since $2^s q\equiv C\pmod{3^b}$ and $2^s$ is invertible. For $L=\lfloor8b/5\rfloor$ the binomial theorem gives

\[
  \binom Lb\,(5/3)^b\le(8/3)^L,
  \qquad
  \binom Lb\le\Lambda^b,
  \qquad
  \Lambda=\left(\frac{8^8}{5^5\,3^3}\right)^{1/5}<3 .
\]

Consequently, the proportion of unit classes that can admit even one word at a descent-compatible clock is at most $\tfrac32(\Lambda/3)^b$, with $\Lambda/3\approx0.960683$. A positive word count in every unit class is impossible in this range, even after pooling all the totals. The geometric bound also implies that Haar-almost every ternary unit belongs to only finitely many of these sets of classes. The count and the measure statement are written deductions. The clock cap and the exact ordinary obstruction above are checked in Lean.

## A positive fraction misses at every depth simultaneously

At any finite horizon $B\ge1$, **more than one eighth** of the unit classes modulo $3^B$ admit no legal inverse word with $5s\le8b$ at any depth $1\le b\le B$. The same bound holds for the Haar measure of units that avoid these words at every positive depth. This includes a different quantifier from the fixed-depth estimate.

Read an inverse word outwards from its root. Write $s_j$ for the partial clock and $h_j=5s_j-8j$. Stop the first time after the root that $h_j\le0$. These first-crossing words form a prefix-free set. Each word of length $j$ allows one residue cylinder of ternary Haar mass $3^{-j}$ before conditioning on units. If a root has any candidate at any depth, it belongs to one of these first-crossing cylinders.

Take $r=7/9$ and assign to an edge of gap $e$ the weight $r^{5e-8}/3$. Their sum is

\[
    \Phi=\frac{r^{-3}}{3(1-r^5)}
        =\frac{14348907}{14489006}<1 .
\]

Thus at every node the total outgoing weight is at most the incoming weight. Starting at positive surplus $h$, the sum of the raw weights $3^{-j}$ over all first-crossing continuations is at most $r^h$. Indeed at each stopped word the terminal factor $r^{h_j}$ is at least one, and the sum of the weighted masses of a prefix-free collection is bounded by its initial mass. Apply this first on finite trees and take increasing depth and letter cutoffs.

The first gap $e=1$ stops immediately. Gap $e=2$ leaves surplus $2$. From there a second gap one stops, and a second gap at least two leaves surplus $4+5k$, $k\ge0$. A first gap at least three leaves surplus $7+5k$. Summing these cases and conditioning on units of Haar mass $2/3$ bounds the covered fraction by

\[
 \frac12\left(1+\frac13+
       \frac{r^4}{3(1-r^5)}+\frac{r^7}{1-r^5}\right)
       =1-\frac{437041}{3421602}<\frac78 .
\]

At finite $B$ each word cylinder of depth $j\le B$ has exactly $3^{B-j}$ lifts, so the same proof applies directly to counting residues. Every excluded cylinder has ordinary converging representatives by the one-gap cylinder theorem. The infinite Haar statement does not itself identify the natural density of ordinary integers avoiding all depths. [One-gap cylinder construction](SynchronousShadow.lean)

For a hypothetical least nonconverging gate $a$, its particular forward endpoints can lie in the exceptional classes. The estimates give no deterministic visit outside them and no descent below $a$. Proving such a visit would require information about the residues of that very orbit.
