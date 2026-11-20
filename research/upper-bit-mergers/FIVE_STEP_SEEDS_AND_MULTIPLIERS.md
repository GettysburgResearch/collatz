# A single residue class suffices for multiplication by five

**PROPOSED.** All statements concern ordinary positive integers. Let $T$ be the shortcut Collatz map, $U$ its odd-to-odd acceleration, and $C$ the integers reaching 1. Write $X(k)=128k+1$, $Y(k)=64k+1$, with $k>0$ and $4\nmid k$. Rank counts odd inputs before first arrival at 1. We also study the directed adjacent implication $X(k)\in C\Rightarrow Y(k)\in C$. Its universal validity remains open. [Adjacent criterion](DEEP_REVERSE_BASIN.md)

## Transport both orbits into one residue class

For a fixed positive odd integer $q$ coprime to three, the physical five comparison asks whether $q\in C$ implies $5q\in C$. PR 157 proves that validity for every such $q$ is equivalent to Collatz. PR 166 gives pairs of ordinary prefixes that commute with multiplication by five. The observation here is that a single suitable pair transports **every supplied comparison**, with bounded multiplicative cost and with both endpoints prescribed. [Global equivalence, GCM-002](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/merger.md) · [Physical ladder, FL1–FL3](https://github.com/GettysburgResearch/collatz/blob/5996b9f525ca50978bc34f423192c36a87765bf3/research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md)

PR 160 already gives a same-clock proportional return for which the odd endpoint increases. The lifting theorem below applies to its 21-clock PC-002 example as well. The 71-clock choice gives the long initial valuation pattern used here. [PC-002 and its scope](https://github.com/GettysburgResearch/collatz/blob/6d877e718f5ef9d57fe1830912c444359718747a/research/closure-attacks-20261120/merger/PHYSICAL_CERTIFICATE_BOUNDARY.md)

**One explicit sufficient test.** It suffices to prove $x\in C\Rightarrow5x\in C$ just for positive $x\equiv6\,375\,551\,795\pmod{2^{71}}$ coprime to three. Every such $x$ starts with accelerated exponents $(1,3,3,3,3,3,3)$, outside the published ladder compiler. The criterion persists on an explicit single subprogression of arbitrarily high binary and ternary precision.

Here is the finite datum, reproducible by 71 applications of the defining map on each starting integer. Both starts encounter 37 odd inputs. The accelerated prefix in the preceding paragraph consumes 19 clocks, so it is fixed on the stated residue class.

| Start | Endpoint after 71 shortcut steps |
|---:|---:|
| $a=6\,375\,551\,795$ | $v=1\,215\,835$ |
| $5a=31\,877\,758\,975$ | $5v=6\,079\,175$ |

**Proof for all inputs.** More generally, suppose $a$ is a positive odd ternary unit, $L\ge1$, and the paths of $a,5a$ have the same odd count $p\ge1$ through clock $L$, ending at $v,5v$ with $3\nmid v$. Fix integers $D\ge0$, $d\ge1$ and any residue $t$ coprime to three. Define the single progression $S$ by
$$
 x\equiv a-2^L v(3^p)^{-1}\pmod{2^{L+D}},\qquad x\equiv t\pmod{3^d}.
$$
The inverse in this formula is modulo $2^{L+D}$. For every positive odd ternary unit $q$ there are infinitely many positive $x\in S$ and $b\ge0$ with
$$
                 T^{L+b}(x)=q,\qquad T^{L+b}(5x)=5q.
$$
Choose $\kappa$ with $2^L\kappa\equiv t-a\pmod{3^d}$. Then $v+3^p\kappa$ is a unit modulo three. Choose $b\ge D$ sufficiently large with $2^bq\equiv v+3^p\kappa\pmod{3^{p+d}}$. Such exponents form a full progression modulo $2\cdot3^{p+d-1}$ because $2$ generates the units modulo each power of three. This order follows from $v_3(4^{3^j}-1)=j+1$ by cubing. Set
$$
             k=(2^bq-v)/3^p,\qquad x=a+2^L k.
$$
Then $k\ge0$, $k\equiv\kappa\pmod{3^d}$, and the formula puts $x$ in the required binary class. The length-$L$ parity words are unchanged. Their affine slopes give $T^L(x)=v+3^pk=2^bq$ and $T^L(5x)=5v+5\cdot3^pk=2^b5q$. Halving $b$ times proves both endpoint identities. For a failed comparison at $q$, every such $x$ is an actual failed comparison. Applying PR 157 gives the stated equivalence. Each fixed $D,d$ gives a separate ordinary criterion.

**Counting and weighted consequence.** The lift can be chosen injectively with $x\le Kq$ for a constant depending only on $a,L,p,v,D,d$. Take $B=\max(D,\lceil\log_2 v\rceil)$, and choose the unique allowed $b$ in $[B,B+2\cdot3^{p+d-1})$. For instance $K=a+2^{L+B+2\cdot3^{p+d-1}}$ suffices. The odd part of $T^L(x)$ recovers $q$, proving injectivity. Consequently for any nonnegative weight $w(q)$ depending only on the ordered pair of ordinary orbit components of $(q,5q)$, and every $s\ge0$,
$$
 \sum_{q\le X}\frac{w(q)}{q^s}
 \ \le\ K^s\sum_{\substack{x\in S\\ x\le KX}}\frac{w(x)}{x^s}.
$$
Both sums are over positive odd ternary units. At $s=0$ this counts failed comparisons by using their indicator. At $s>0$ the full energy is finite if and only if it is finite on this one progression, by nonnegativity and inclusion in the reverse direction.

Taking $t=1$ also locates any hypothetical failure where bounded reverse descent is impossible. For every $x>1$ with $x\equiv1\pmod{3^d}$, every positive ordinary ancestor $z$ reaching $x$ with at most $d$ odd inputs obeys $z\ge x$, however many even inputs it uses. Reverse its actual word from 1 as well as from $x$. Each reversal doubles its argument or sends $y$ to $(2y-1)/3$. Starting with a difference divisible by $3^d$, each odd reversal consumes at most one power of three, so every division at the reference point is integral. The reference path stays positive. The reverse affine function $G(y)=Ay-B$ has $B\ge0$ and $G(1)\ge1$, whence $A\ge1$ and $z=G(x)\ge x$. For each $d$ the lifting theorem places every failed comparison at such an $x$ with the same prescribed seven initial exponents. In fact fix a failed $q$, take $D=d$, and choose $b$ as in the counting proof. Then $x$ tends to infinity and $\log_2 x=O_q(3^d)$. Infinitely many resulting failed sources require at least $\log_3\log_2 x-O_q(1)$ odd inputs in any path from a smaller ancestor.

A much smaller explicit constant applies to the **covered** ladder class $H_1=\{x\equiv49\pmod{64}:3\nmid x\}$. Given $q$, choose $L_0\in[6,11]$ with $2^{L_0}q\equiv7\pmod9$. At $L=L_0,L_0+6$, both candidates $x=(2^Lq-7)/9$ are integers, and their difference $7\cdot2^{L_0}q$ is a unit modulo three. Choose a unit candidate. It is positive, is 49 modulo 64, and satisfies $x<(2^{17}/9)q$. Its source word is $(2,L-2)$: the first odd successor is $(2^{L-2}q-1)/3$ and the next is $q$. FL1 at $r=1$ sends $5x$ to $5q$ at the same clock $L$. The endpoint $q=U^2(x)$ again makes the selection injective. Thus the displayed inequality also holds with $S=H_1$ and $K=2^{17}/9$. This gives a lower bound on the portion of energy carried by the covered class at a larger cutoff, complementing PR 166's upper bound on its contribution at a smaller cutoff. Neither estimate supplies an absolute finite bound. In particular the open step is proving five-closure on one sufficient progression, or obtaining an independent estimate for its defect. [Ladder renewal and the uncovered energy, PR 166](https://github.com/GettysburgResearch/collatz/blob/5996b9f525ca50978bc34f423192c36a87765bf3/research/grh-certificate-closure-20261120/LADDER_RENEWAL.md)

## A finite test over all certified base pairs

The W512-060 theorem lifts from a positive eligible base $b$ with certificates for both $X(b)$ and $Y(b)$ to $k=b+2^K u$, $u>0$ odd. If their total shortcut clocks and odd counts are $(A_s,r_s),(A_t,r_t)$, put $H_s=A_s-2r_s$, $H_t=A_t-2r_t$. Its sufficient conditions are $1-H_s+H_t\ge0$ and $K\ge\max(2,A_s-6,A_t-5,H_t,5-4H_s)$. The following test decides the applicability of this specific theorem when the upper witness at $k$ is supplied. [W512-060, PR 164](https://github.com/GettysburgResearch/collatz/blob/ae595a48afaf327e979034b1d0e477170d6f4d86/research/witness-closure-512-2026-11-20/continuation-descent.md)

Truncate the supplied witness at its first hit. If its rank is $s$, there are at most $s-1$ candidate bases. For each $1\le i<s$, let $z_i=U^i(X(k))$ and $A_i$ be the shortcut clock there. Test the single candidate
$$
 b_i=k-\frac{2^{A_i}(z_i-1)}{128\,3^i}.
$$
Keep positive integral eligible candidates with $b_i<k$. Put $K=v_2(k-b_i)$. Check the upper prefix at $b_i$ and compute the lower first-hit certificate by running at most $K+5$ shortcut steps. If that budget expires, discard the candidate. Otherwise check the two W512-060 inequalities with the first-hit data.

Indeed any admissible base can use its first-hit certificates. Removing terminal loops at 1 preserves both heights and only decreases the clock requirements. Exact lifting follows the base word on the larger input. At the base upper's first hit, the transported difference is $128\,3^i(k-b)/2^{A_i}$, giving the formula for $b_i$. The base hits strictly earlier in odd-step count than the larger upper: until the base hit, the larger upper follows the same branches with strictly positive difference. Thus the loop omits no possible first-hit base. Conversely every accepted candidate explicitly satisfies the source theorem. The lower clock budget makes the search finite even when convergence of that base's lower arm is unknown.

**No rank-five upper input satisfies W512-060 at any positive smaller base.** Its odd exponent word is $(2,2,2,c,a)$, with $a\ge4$ even, and its fourth odd endpoint is $z=(2^a-1)/3$. Any eligible base must have rank at least four, so only $i=4$ can contribute. A rank-four base with fourth exponent $c$ exists only for $c=54j+2$, $j\ge1$. In that case $A_4=c+6$, and $v_2(z-1)=2$ gives $K=A_4+2-7=c+1$ if the candidate is integral. But at clock $c+5$ the lower arm of this very base reaches $3^{27j}+1$, with all earlier states above 1. At $c+6=K+5$ its value is still $(3^{27j}+1)/2>1$. Its certificate cannot fit the required budget. Other transfer rules, including explicit mergers at rank five, retain their own domains. [Rank-four clocks](DEEP_REVERSE_BASIN.md#what-the-first-nonempty-rank-would-settle) · [Rank-five parameterization K3](https://github.com/GettysburgResearch/collatz/blob/051237135a34ae7d4b973ee5fcf5da04ded6f0fc/research/deep-reverse-closure-20261120/REVERSE_CERTIFICATE_KERNEL.md)

## A smaller multiplication-by-five comparison for every surviving Mersenne exponent

Take $e=119+162j$, $P=2^e$, $M=P-1$, $X=(1024P-2573)/243$, and $Y=(X+1)/2$. The certified upper $X$ has rank five and $Y$ shares an ordinary forward iterate with $M$. Write $v\sim w$ for such a meeting. Choose $h=e+1$ and $r=2$ for even $j$, $r=1$ for odd $j$. Define
$$
             B=3^r2^{h-r},\qquad q=(B-1)/5.
$$
For every $j\ge0$, $q$ is an odd ternary unit, $q<X/4$, and $5q\sim Y$. Both $q$ and $5U(q)$ have explicit ordinary representatives below $X/176106$. Thus if $X$ were the globally least failure of the adjacent implication, it would force
$$
             q\in C,\qquad 5U(q)\in C,\qquad 5q\notin C.
$$
In particular the full adjacent implication **on this family** follows from the smaller adjacent comparisons needed for $q$, together with just the physical five-closure call $q\in C\Rightarrow5q\in C$. The new ladder compiler handles source words beginning with a valuation two. This particular source starts with valuation one. [Least-failure height and constructive smaller comparisons](LEAST_FAILURE_SIEVE.md) · [Physical five-closure, PR 157](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/merger.md) · [Five-closure compiler and its domain, PR 166](https://github.com/GettysburgResearch/collatz/blob/5996b9f525ca50978bc34f423192c36a87765bf3/research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md)

The latest PR 164 update adds two negative-template contractions and three broadened rules. None applies directly to this family. Here $k=2m$ with $m=(4P-11)/243\equiv7\pmod{16}$. Both negative-template domains and the broadened adjacent domain W512-082 require an odd index $k$. The directed comparison at an even index is $P(m)$ in PR 164's notation. W512-080 concerns $Q$, while W512-081 needs $m\equiv1215\equiv15\pmod{16}$. This checks the stated domains only. [W512-070 and W512-072](https://github.com/GettysburgResearch/collatz/blob/6fa6b429870a9cd53cde0fc77ad64a3c3956199f/research/witness-closure-512-2026-11-20/continuation-negative.md) · [W512-080–082](https://github.com/GettysburgResearch/collatz/blob/6fa6b429870a9cd53cde0fc77ad64a3c3956199f/research/witness-closure-512-2026-11-20/continuation-j.md)

**The ordinary paths.** For any $d\ge1$, $T^d(2^d-1)=3^d-1$. Since $e$ is odd, two steps from $3^e-1$ reach $(3^{e+1}-1)/4$. Two halvings from $3^h-1$ reach the same number. Consequently $M\sim2^h-1$, whose first $r$ steps reach $B-1$. Modulo five, $B\equiv(-1)^{h/2+r}=1$. Also $3\nmid(B-1)$ and $B-1$ is odd. The bound $q<9P/10<X/4$ follows from $X>4P$.

Set $s=e-r$, $A=3^{r+1}$. The first odd step gives $u=U(q)=(A2^s+1)/5$. Write $m=\lfloor s/3\rfloor$. Three shortcut steps take $(F2^l+1)/5$ to $(3F2^{l-3}+1)/5$ whenever the start is integral and $l\ge3$: it is $5\bmod8$ and its first step is followed by two halvings. This yields
$$
       T^{3m}(u)=w=(2^{s\bmod3}A3^m+1)/5.
$$
Meanwhile each pair of steps on $5u=A2^s+1$ exchanges a factor of four for a factor of three in $5u-1$. After $2\lfloor s/2\rfloor$ steps it reaches
$$
       v=2^{s\bmod2}3^{r+1+\lfloor s/2\rfloor}+1 .
$$
We have $w<22\,3^{e/3}$ and $v<55\,3^{e/2}$. Both are below $P/176106$: the integer inequality $(55\cdot176106)^2 3^{119}<4^{119}$ suffices at $e=119$, and $3/4<1$ gives every larger exponent. Under the least-failure hypothesis, the established height bound now gives $w,v\in C$. Without that hypothesis, the directed descent constructs $O(e)$ sufficient smaller adjacent comparisons for $w$, each with upper start below $176106w=O(P^{\log_8 3})$. These arguments use the actual $e$ supplied and require no hypothesis on primes.

The same orbit connection $5q\sim 2^e-1$ works for every odd $e\ge3$ by choosing $r\in\{1,2\}$ of the same parity as $(e+1)/2$. The least-failure conclusion above uses the specified rank-five family and its known upper antecedent.

## An exact link to the rank-four powers

PR 165 identifies the pure-power component on the lower side of the rank-four problem. A second choice of $r$ puts that component and the rank-five Mersenne component on opposite sides of the following comparison. [Rank-four source and its two-transfer interpretation, PR 165](https://github.com/GettysburgResearch/collatz/blob/78bdb31ccba608de3d089b751a0ab59a52007408/research/certificate-transfer-intake-20261120/EXCEPTIONAL_FAMILY.md)

Use the same $h$ and choose $r=20$ for even $j$ and $r=101$ for odd $j$. The five-divisibility condition still holds, $0<r<h$, and $h-r-1$ is a multiple of three. Put $q'=(3^r2^{h-r}-1)/5$. The same paths give
$$
 5q'\sim M,\qquad q'\sim v'=(3^b+1)/10,\qquad 5v'\sim3^{b-1},
$$
with $b=54(j+1)$ or $54(j+2)$ respectively. In fact the clock-three blocks terminate exactly at $(3^b+1)/5$, which halves to $v'$. In both cases $b\equiv2\pmod4$, so $v'$ is an odd ternary unit. Its multiple $5v'$ is $T(3^{b-1})$. Hence the final pure power is literally of the rank-four form $3^{27t-1}$. If convergence of the pure power is the input, transferring it to $M$ by these two pairs requires reverse five-closure at $v'$ and forward five-closure at $q'$. A forward-only compiler does not supply the first implication. The three ordinary component identities are unconditional.

## Exact replay

Run `python -B research/upper-bit-mergers/check_five_step_seeds.py` from the repository root. It verifies the two 71-step paths, their odd counts and exponents, the small-constant lift on all ternary unit residues modulo 27, and examples for the seed recognizer and both Mersenne constructions. The all-input claims follow from the proofs above.
