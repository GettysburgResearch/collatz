# What a physical competitor must spend after the Mersenne peak

**PROPOSED** for the elementary bounds. **SOURCE-QUALIFIED** for the quantitative excess using Yu. The source is one supplied ordinary power $3^j-1$. The visitor can have arbitrarily many clocks and can use any legal word. These are necessary conditions on physical mergers. Throughout, a signed shortcut is $T(v)=v/2$ at an even integer and $(3v+1)/2$ at an odd one. Write $P(v)=v^2$ except that $P(-2)=5$, $P(-4)=18$, and $P(-7)=50$.

## A common clock gives a small signed center

Fix positive integers $j,w$, $K\ge1$, with $w\le K2^j$. Suppose an actual visitor from $w$ reaches $T^h(3^j-1)$. Write $p$ for the native $h$-step odd count. If the visitor clock is at least $h$, cut off its last $h$ steps, of odd count $q$, and let $u$ be the initial value of that suffix. Put $N=j+p-q$ and assume $N\ge0$. Then
$$
             u=3^N+c,\qquad -2\cdot3^h\le c\le3^h.
$$
In fact $2^hT^h(v)=3^{Q_h(v)}v+B(v)$, with $0\le B(v)\le3^h-2^h$. Subtract the two equal-endpoint identities to obtain $3^qc=B(3^j-1)-3^p-B(u)$. The case $c=-1$ is *exactly* an equal-clock merger of two positive peaks with the augmented counts $N+q=j+p$. If $c=0$ and $N>0$, the head leading to $u=3^N$ consists solely of even steps: no odd shortcut has image divisible by three. Consequently $w\ge3^N$ here. If the visitor has fewer than $h$ clocks, its terminal is at most $(3/2)^h(w+1)$ by shifted-height growth, while $T^h(3^j-1)\ge(3^j-1)/2^h$. This is impossible for fixed $K$ and $h=o(j)$ at large $j$. [Kernel common-clock cut](PhysicalWindow.lean)

For any physical trajectory from $w$ to $3^N+c$, let $Q$ count its odds and $E=(Q-N)_+$. Then
$$
\begin{array}{rl}
 3^N2^E &\le c3^E(w+1) \qquad (c>0),\\
 8^N4^E &\le 4P(c)9^E(w+1)^2
       \qquad(c\le-2,\quad 2|c|\le2^N).
\end{array}                                                    \tag{1}
$$
Run the last at most $N$ odd inverse letters alongside the signed center $c$. If their number is $b$ and their duration $S$, the two backward endpoints differ by $2^S3^{N-b}$. The physical and signed inverse words agree at each legal inverse choice, since a remaining ternary digit suffices for integrality. A signed inverse word ending at $c>0$ starts at a positive integer $s$ (zero and negative inputs stay on their own sides). Its forward product gives $2^Sc\ge3^b s$. For $c\le-2$, every signed value is $\le-2$, including when $c$ itself has an eventual orbit through $-1$. The only exceptional negative center is the terminal $c=-1$. One checks at each edge $8^{v\bmod 2}P(v)\le4P(Tv)$ with $Tv\le-2$, giving $8^bP(s)\le4^SP(c)$. On a reverse word of $b$ odds the signed magnitude grows by at most $2^{S-b}$, so $|s|\le2^{S-b}|c|$. If $2|c|\le2^N$ the positive physical endpoint is at least half of $2^S3^{N-b}$. Complete the remaining $E$ reverse odds using $(v_{\rm odd\,pred}+1)=2(v+1)/3$ and the monotonicity of shifted height at an even inverse. This proves (1). The three corrections in $P$ give equality around $-5,-7,-10,-5$, so the factor 8 per odd is optimal for an all-center one-step potential with time factor 4. [Kernel signed budget](SignedBudget.lean) · [kernel finite precision](ShadowBarrier.lean) · [kernel arbitrary visitor](PhysicalWindow.lean)

For a positive center set $\mu=3$. For a negative center other than $-1$ set $\mu=\sqrt{8}$. One can also take $\mu=3$ for a *nonperiodic* negative center, since every finite signed path ending there is simple. The occupation estimate and product in [the ascent theorem](FIRST_MEETING.md) give $2^S|c|\ge c_0\,3^b|s|$ with an absolute $c_0>0$. No classification of the negative cycles is needed. Define
$$
   \kappa(\mu)=1+\frac{\log(\mu/2)}{\log(3/2)}.
$$
For fixed $h,K$ and large $j$, a visitor reaching the given postpeak point with $c\notin\{0,-1\}$ spends at least $\kappa(\mu)j-O(h+\log(2K))$ total odds. Thus the baseline is $2j$ at positive or nonperiodic negative centers, and $\bigl(1+\log 2/[2\log(3/2)]\bigr)j$ at arbitrary negative centers. The sharper statement below shows that even matching the baseline to a constant is impossible at a fixed cofactor.

## A fixed cofactor creates a further cost

For fixed $h,K$ there are absolute $c_1>0$ and an implied absolute constant such that for sufficiently large $j$, every merger as above with $c\notin\{0,-1\}$ uses at least
$$
       \kappa(\mu)j+
       c_1\,\frac{\log j}{\log\log j}-O(h+\log(2K))
                                                               \tag{2}
$$
odd inputs. Constants in the nonperiodic negative-center case can incorporate the absolute simple-path constant. The assertion concerns an ordinary visitor at the given power. It does not estimate the number of allowed starting residues. In particular, the all-cofactor attainment in the ascent theorem allows the cofactor to vary and gives no construction invalidating (2).

**Proof.** Work at large $j$. We have $|N-j|\le h$. Equation (1) excludes $Q\le N$ for the visitor's head, since $|c|\le2\cdot3^h$, $w\le K2^j$, and even $\sqrt8>2$. After exactly $N$ reverse odds on the head, at clock $S$, the physical state is $b=2^S+s$ with $s$ a nonzero signed integer, the ancestor of $c$. From the signed estimates above,
$$
   2^S\ \ge\ \mu^N |s|/A,\qquad
   b+1\ge 2^{S-1},\qquad \log A=O(1+h).                      \tag{3}
$$
For example one may take $A=c$ in the positive case, $\sqrt{P(c)}$ in the general negative case and $|c|/c_0$ in the simple negative case. In the negative case use $|s|\le2^{S-N}|c|$ and $2|c|\le2^N$. Write $k,d$ for the number of odds and evens on the remaining reversed head from $b$ back to $w$. Each even inverse increases shifted height by at least $3/2$ at a positive input. Hence
$$
 (k-d)\log(3/2)\ \ge\ (S-1)\log 2-\log(w+1).
                                                               \tag{4}
$$
Write the total odd count $N+k+q=\kappa(\mu)j+B$. Inequalities (3) and (4) imply $B\ge-C(1+h+\log(2K))$. With $D=1+\max(0,B)+h+\log(2K)$, they also imply
$$
    d+\log(1+|s|)\ll D,\qquad S\ll j+D,\qquad
    k\ge(\kappa(\mu)-1)j-O(h+\log(2K)).
                                                               \tag{5}
$$
Indeed the left side of (4) is at most $(\kappa(\mu)-1)j\log(3/2)+(B+O(h)-d)\log(3/2)$, and the right side is at least $j\log(\mu/2)+\log|s|-O(1+h+\log(2K))$. This also justifies the baseline bound.

Track the remaining actual inverse word from $b$. After $t$ inverse letters with $\ell$ odds the physical value $v$ obeys
$$
                  3^\ell(v+1)=2^{S+t}+C_t .
$$
Initially $C_0=s+1$. An odd inverse doubles $C_t$; an even inverse replaces it by $2C_t-3^\ell$. Consequently $\log(1+|C_t|)\ll D+\ell$, uniformly in $t$: use $t\le\ell+d$ and $|C_t|\le2^t(|s|+1+t3^\ell)$. Before a consecutive run of $m\ge1$ odd inverses, legality gives
$$
                   3^{\ell+m}\mid 2^{S+t}+C_t.                \tag{6}
$$
The numerator is positive. If $3\mid C_t$ then (6) is impossible, including $C_t=0$. Otherwise apply Kunrui Yu's $p$-adic logarithm estimate at $p=3$, $K_{\rm field}=\mathbb Q$, to the two units $2,-1/C_t$ with integer exponents $S+t,1$. Their product differs from one exactly because the numerator in (6) is nonzero. Negative rational units are allowed. The height of $-1/C_t$ is $\log\max(1,|C_t|)$, and $3^1=3\bmod4$ verifies condition (1.2). The consequence of Theorem 1 given in Yu's introduction yields
$$
             \ell+m\le C(D+\ell)\log(3+j+D).
$$
Here $t\le k+d=O(j+D)$. Across the even letters $\ell$ does not change. There are at most $d+1$ runs, so
$$
               k\le D\,[1+C\log(3+j+D)]^{d+1}.
$$
If $D\ge\log j$ the desired lower bound on $D$ is immediate. Otherwise take logarithms and use $k\gg j$ from (5), $\log D\le\log\log j$ and $d\ll D$ to obtain $D\gg\log j/\log\log j$. For fixed $h,K$ this eventually forces $B>0$, giving (2). [Yu, Acta Arith. 89 (1999), 337–378, Theorem 1, (1.1), (1.2), (1.5) and (1.8)](https://doi.org/10.4064/aa-89-4-337-378)

The special center $-1$ has an arbitrarily long exact all-odd inverse orbit at $-1$, so the signed budget cannot extend across it. Equal-clock augmented peak links are a real exception. Round thirteen's finiteness of each such class does not tell us where a given *asynchronous* physical visitor next meets, nor that a visitor of acceptable grade exists.

Weaver's paper 230 already uses fixed post-crest suffixes, a bounded signed comparison center, and all-clock estimates from the target's ternary depth. Equations (1) and (2) optimize a different signed-label growth estimate and retain the surplus forced by the supplied cofactor. [Weaver, paper 230, §§2–4](https://rstation.ai/problems/collatz/papers/230)
