# A lower bound for all smaller ancestors at the negative-five cycle

**PROPOSED, unconditional.** Write $T(x)=x/2$ for even $x$ and $T(x)=(3x+1)/2$ for odd $x$. Write $s_i(x)$ for the number of odd inputs in the first $i$ steps. The starting values and both clocks in the theorem are ordinary nonnegative integers, with positive starting values.

**Theorem.** Let $k\ge1$, $A\ge0$, $3^A\mid n$ and $8^k\mid n+5$. If $0<m<n$ and $T^j(m)=T^i(n)$ for some $0\le i\le3k$, then

$$
s_j(m)\ \ge\ s_i(n)+A+1. \tag{1}
$$

The competing clock $j$ is unrestricted. For $A\ge6$ the sharper bound is $s_j(m)\ge s_i(n)+A+2$, as proved below. In particular, for $n=3^a$ the cost is at least $a+1$ **additional odd steps** over the part of the orbit covered by the theorem. Already $k=1$ applies to every odd $a$. Arbitrarily long covered segments occur among powers of three.

## The signed path controls the last odd steps

Under the integer extension of $T$, the cycle is $-5\to-7\to-10\to-5$. A positive start $n=8^k t-5$ has the same parities for $3k$ steps, and

$$
Y=T^{3k}(n)=9^k t-5,\qquad s_{3k}(n)=2k. \tag{2}
$$

Every meeting in (1) can be continued to $Y$ along the common orbit. Both odd counts increase by the same amount. It suffices to prove that reaching $Y$ from below $n$ costs more than $2k+A$ odd inputs.

The positive map $S$ obtained by applying $T$ to $-x$ and changing the sign back is $x/2$ on evens and $(3x-1)/2$ on odds. Suppose $S^L(M)=5$ with $q$ odd inputs. Then $M\ge5$, since $\{1,2,3,4\}$ is invariant. In fact

$$
 2^L\ \ge\ (M/5)\,8^{q/2}. \tag{3}
$$

Set $W(8)=50$ and $W(x)=x^2$ elsewhere. On every step of this path, $4W(Sx)\ge8^{x\bmod2}W(x)$. This follows immediately for an even input. At 5 and 7 there is equality. At odd $x\ge9$ use $(3x-1)^2\ge8x^2$. Multiplying the inequalities and using $W(5)=25$ proves (3).

Take any length-$L$ path from a positive $z$ to $Y$ with $q\le2k$ odd inputs. Write its affine numerator as $3^q z+B=2^L Y$. The same word run backwards from $-5$ produces the signed integer $-M$, where

$$
 M=\frac{5\cdot2^L+B}{3^q},\qquad
 z+M=2^L3^{2k-q}t. \tag{4}
$$

For integrality, the second formula gives an integer for $M$ by subtraction. To verify the word at every intermediate step, undo each step simultaneously from $Y$ and $-5$. Their difference starts at $3^{2k}t$. An even inverse doubles it, and an odd inverse multiplies it by $2/3$. Before each of the $q$ odd inverses a factor of three is still available, so both inverse values are integers. An even inverse gives an even preimage, and an integral odd inverse gives an odd preimage. The signed inverse values stay at most $-1$, so $S^L(M)=5$ with precisely these parities.

Combining (3) and (4) gives

$$
 z+M\ \ge\ \frac M5 (9/8)^{k-q/2}(n+5).
$$

It follows that $z\ge n$ for $q\le2k$. If $q=2k$, the formulas give more. There is an integer $b=L-3k\ge0$ such that

$$
 z=2^b n+c,\qquad c=5\cdot2^b-M\ge0. \tag{5}
$$

Here (3) implies $2^b\ge M/5\ge1$.

## The first odd steps can also be controlled

Suppose a smaller $m$ reaches $Y$ with $2k+d$ odd inputs, where $1\le d\le A$. Split its path just after the $d$th odd input. The initial segment has length $J$ and ends at $z$. Its remaining $2k$ odd inputs give (5).

Run the initial word backwards from **both** $z$ and $c$. Their difference $2^b n$ is divisible by $3^d$, so the same inverse argument makes the second path integral at every step. If $c=0$, backwards halving steps only give zero, and an odd inverse at zero would give $-1/3$. Thus $c>0$. Every integral inverse from a positive integer is positive. The second path starts at a positive integer $\beta$ and satisfies

$$
  T^J(\beta)=c,\qquad s_J(\beta)=d,\qquad
  m=\alpha n+\beta,\qquad \alpha=2^{J+b}/3^d. \tag{6}
$$

In particular $\alpha<1$. Evaluate the same inverse affine word at $-M$ over the rationals, using its prescribed branches. Both inverse branches $y\mapsto2y$ and $y\mapsto(2y-1)/3$ preserve $y<-1$. Because $c+M=5\cdot2^b$, the resulting rational value is $\beta-5\alpha<-1$. Together with $\alpha<1$, this leaves only $\beta=1,2,3$.

The positive orbits of these three integers determine the last inequality. For every $J$, $3^{s_J(\beta)}/2^J\le2$ except at $\beta=3,J=2$, where the ratio is $9/4$ and $T^2(3)=8$. Indeed 1 and 2 alternate, with ratio $3/4$ per full cycle, and $3\to5\to8\to4\to2\to1$ supplies the only extra prefix. By (6), $2^b<3^d/2^J$. If $b=0$, then $M\ge5$ forces $c=0$ in (5). If $b\ge1$, the only possibility is the exceptional prefix, with $b=1$ and $c=8$. Equation (5) would give $M=2$. Both cases are impossible. This proves (1).

## What a near-minimal merger would imply

There is also information just beyond (1). Suppose $A\ge1$ and a smaller start meets the initial segment with exactly $A+e$ extra odd inputs, $e\ge1$. Then there is a positive ordinary integer $\beta$ and a clock $J$ satisfying

$$
 \beta+1<5(3/2)^e,\qquad s_J(\beta)=A,\qquad
 \frac{3^A}{2^J}>(2/3)^e. \tag{7}
$$

Extend the meeting to $Y$ and split off the first $e$ odd inputs of the smaller start, ending at $v$. At an odd step $T(x)+1=3(x+1)/2$, and at an even step $T(x)+1\le x+1$. Hence $v+1\le(3/2)^e(m+1)\le(3/2)^e n$. Split the rest just after the next $A$ odd inputs. Its last $2k$ odd inputs give (5). Applying the inverse construction in (6) to the middle segment, using $3^A\mid n$, gives $v=\alpha n+\beta$ with $\alpha=2^{J+b}/3^A$ and $\beta>0$. The signed evaluation again gives $\beta+1<5\alpha$. Since $\alpha<(3/2)^e$, (7) follows.

In particular, fixing $e$ and producing such ordinary mergers for unbounded $A$ would **disprove Collatz and force a divergent positive trajectory**. There are only finitely many choices of $\beta$ in (7), so one would realize unbounded clocks with multipliers bounded away from zero. For any eventually periodic positive orbit, a full period with $s$ odd inputs and length $h$ has $3^s/2^h<1$. Indeed its affine constant is positive because every positive cycle contains an odd input, and its starting value is positive. Repeating the period drives all prefix multipliers to zero. Thus the selected orbit cannot repeat a value. A positive integer orbit without repetitions tends to infinity. The construction of mergers for unbounded $A$ at a fixed $e$ is an open hypothesis.

There is a finite consequence in the other direction. If $\beta$ reaches 1 with $s$ odd steps before time $J$, its multiplier up to 1 is at most $1/\beta$. Any continuation from 1 with $A-s$ odd steps has multiplier at most $2(3/4)^{A-s}$. Thus $(4/3)^{A-s}<2(3/2)^e$. For $e=1$, (7) leaves only $1\le\beta\le6$, all of which reach 1 within two odd steps. If $A\ge6$ their hit must occur before $J$, and $(4/3)^4>3$ gives a contradiction. Consequently (1) improves to **at least $A+2$ extra odd steps whenever $A\ge6$**. This last numerical threshold follows from the six explicit orbits, for all admissible $n,k$ and both arbitrary clocks.

## The first possible time for direct descent is attained

For $k\ge1$ let $r$ be the least integer with $2^r8^k>9^k$. For every positive $n=8^k t-5$, its first strict descent below $n$ takes at least $3k+r$ shortcut steps, if it occurs. Along each three-step block the intermediate slopes relative to its starting value are $3/2$, $9/4$ and $9/8$, with positive offsets. After the blocks, $Y>(9/8)^k n$. Every additional step is at least division by two.

For **each** $k$, infinitely many powers of three attain that first possible time exactly. Prescribe $t\equiv5(9^k)^{-1}\pmod{2^r}$. Then $2^r\mid Y$, so the next $r$ steps are all halvings. Since $2^r8^k-9^k>0$, all $n$ with

$$
 (2^r8^k-9^k)n>5(9^k-8^k)
$$

have $Y/2^r<n$. The prescription fixes one residue for $n$ modulo $2^{3k+r}$, congruent to $3$ modulo 8. The powers of three run through exactly the residues $1,3\pmod8$ modulo $2^h$ for $h\ge3$. Indeed $v_2(9^{2^j}-1)=j+3$ by repeated difference of squares, so the order is $2^{h-2}$ and these two classes have that many elements. Thus the desired exponents form one complete residue class modulo $2^{3k+r-2}$, with at most finitely many initial terms below the size threshold. For $k=1$ this includes every sufficiently large $a\equiv1\pmod4$. For example $3^9=19683$ has the path $19683\to29525\to44288\to22144\to11072$. Any smaller start reaching 22144 must have spent at least thirteen odd steps. One more halving nevertheless gives the first strict descent of 19683.

For a fixed $k$, any power with $8^k\mid 3^a+5$ is eligible for (1). Choosing $a$ in $[2^{3k-2},2^{3k-1})$ in the unique prescribed class gives an unbounded sequence for which the covered time $3k$ is within an absolute constant of $\log_2 a$. The signed cycle supplies finite parity words for these positive integers.

### A smaller partner four steps after the checkpoint

There is a uniform way through the initial obstruction even when direct descent is still arbitrarily far away. Write $n=8^k t-5$ and prescribe just four more binary digits by $9^k t\equiv15\pmod{16}$. Then $m=n-2>0$ and $n$ have the **same endpoint and the same odd count** at time $3k+4$.

Indeed the lower start $8^k t-7$ follows the signed cycle starting at $-7$, a different phase of the same cycle. Its endpoint at $3k$ is $9^k t-7$ with $2k$ odd steps. Put $9^k t=16u+15$. The two endpoints are $16u+10$ and $16u+8$. Both halve, and then $8u+5$ and $8u+4$ both reach $3u+2$ in three steps with one odd input. Thus the smaller source gives a certificate of convergence if all smaller integers converge.

For each $k\ge1$ the prescription holds on exactly one sixteenth of the exponent lifts satisfying $8^k\mid3^a+5$. It also allows $3^A\mid n$ for any $A$, by the Chinese remainder theorem. When $k\ge24$, $9^k>16\cdot8^k$, so the bound above rules out direct descent throughout these four additional steps. The proof therefore excludes an explicit infinite class of powers from being least counterexamples while their individual orbits are still above their starting values. As $k$ grows, the proven minimum wait for direct descent exceeds the time of this merger by an unbounded amount. [Lean identity](HighBit.lean)

**Why these three signed phases do not cover every exit at a bounded clock.** Allow all prospective smaller sources $c8^{k-1}t-s$ with $1\le c\le8$ and $s\in\{5,7,10\}$, excluding the original pair $(c,s)=(8,5)$. After $3(k-1)$ steps they have values $cX-s$, where $X=9^{k-1}t$, while the upper source is $8X-5$. Fix any clock bound $H\ge1$ for the two paths from these values. For every fixed $k$, infinitely many powers $n=3^a$ with odd $t$ have **no** such meeting within those clocks.

Impose $X\equiv1\pmod{2^H}$. This fixes one exponent class by the power-of-three order calculation above and allows arbitrarily large $X$. Each permitted word is affine in $X$ and has the same parities as at the signed test value $X=1$. For a pair of words to represent identical affine functions, their slopes must agree. This forces $c$ to have no prime factors other than 2 and 3. At $X=1$ the upper source is 3. Nonpositive integer test sources stay nonpositive under the signed map. Among the remaining allowed pairs, the only positive test sources are $6-5=1$ and $8-7=1$. For $c=8$, equal slopes force equal clocks $i=j$. For $c=6$, they force $i=j+2$, where $i$ is the upper clock. Neither offset permits a meeting of 3 and 1. Check $3\to5\to8\to4\to2\to1$ against $1\to2\to1$; on the cycle the two paths have opposite phases for either of these even clock offsets. Thus each pair of the finitely many affine functions agrees at most at one $X$. Removing those finitely many values proves the assertion. This restriction concerns these prospective smaller sources and their clocks after the common blocks. Other smaller sources remain available.

### Reaching a prescribed target

The obstruction also occurs on orbits known to reach 1. More generally fix $k\ge1$, $A\ge0$ and any positive target $u$ coprime to three. Choose $L$ satisfying

$$
 8^k u\,2^L\equiv 5(9^k-8^k)\pmod{3^{2k+A}}. \tag{8}
$$

Both sides are units. The powers of two run through all units modulo $3^m$ since $v_3(4^{3^j}-1)=j+1$ by induction from the difference of cubes. Thus (8) gives a full arithmetic progression of $L$. For every sufficiently large such $L$ the integer

$$
 n=8^k\frac{2^L u+5}{9^k}-5
$$

is positive, divisible by $3^A$, and has $Y=2^Lu$ in (2). Indeed (8) makes $8^k(2^Lu+5)-5\cdot9^k$ a multiple of $3^{2k+A}$. These starts attain the earliest direct descent time $3k+r$ and then continue by halving until they reach $u$. Taking $u=1$ proves convergence for all the starts so constructed. Prescribing a target in this construction does not require $n$ itself to be a power of three.

In particular, fix *any* $k,A$ and take the set of positive starts satisfying the divisibilities of the theorem that first descend at the earliest time by these consecutive halvings. The full Collatz conjecture is equivalent to convergence for every member of this set. For the reverse implication, any positive start reaches a positive unit $u$ modulo three. If needed, strip off powers of two and take one odd step. Equation (8) gives a member of the set whose orbit reaches that particular $u$. If the member reaches 1, so does $u$, since 1 lies on the cycle $1\to2\to1$. Thus even an orbit with a proven, optimally early first descent can carry any possible subsequent behavior.

## First descent after the checkpoint for a typical power

There is an exact finite counting law for what happens after an arbitrarily long prescribed prefix. Let $D_k(J)$ be the relative natural density, among exponents $a\ge1$ with $8^k\mid3^a+5$, of powers that have fallen below their start by time $3k+J$. Put $\lambda=\log_2 3$ and $H_k=k\log_2(9/8)$. For independent fair bits $e_1,\ldots,e_J$, set $X_0=0$ and $X_j=j-\lambda\sum_{v=1}^j e_v$. Then

$$
 D_k(J)=\Pr\!\left(\max_{0\le j\le J}X_j>H_k\right). \tag{9}
$$

To verify (9), lift the exponent class from modulus $2^{3k-2}$ to $2^{3k+J-2}$. The powers run through all $2^J$ lifts of the prescribed starting residue. The corresponding $t$ run through all residues modulo $2^J$, as do $Y=9^k t-5$. A length-$J$ parity word for $Y$ specifies exactly one such residue. This follows inductively since changing its next binary digit changes the next endpoint by an odd number. At additional time $j$ the iterate is an affine function of $n$ with slope $(9/8)^k3^{\sum e_v}/2^j$ and nonnegative constant term. The slope cannot equal 1 because $k\ge1$. On each finite word, all sufficiently large powers have crossed below their starting value by the deadline precisely when one of those slopes is less than 1. Finite initial exceptions do not affect the exponent density.

For example, (9) has a sharp large-$k$ transition. Write $\mu=1-\lambda/2$, $\sigma=\lambda/2$ and $c=\log_2(9/8)/\mu=0.818841679\ldots$. For every real $x$, with $\Phi$ the standard normal distribution function,

$$
 \lim_{k\to\infty} D_k(\lfloor ck+x\sqrt{k}\rfloor)
   = \Phi\!\left(\frac{\mu x}{\sigma\sqrt c}\right). \tag{10}
$$

Indeed the increments of $X$ have mean $\mu>0$ and variance $\sigma^2$. Reversing the order of the increments shows that $\max_{s\le J}X_s-X_J$ has the law of $\max_{s\le J}(-X_s)$. Choose $\theta>0$ small enough that $b=\mathbb E\exp(-\theta X_1)<1$. For $v>0$ the probability of the latter maximum exceeding $v$ is at most $e^{-\theta v}\sum_{s\ge1}b^s$. Thus replacing the maximum by $X_J$ costs a quantity bounded in probability, uniformly in $J$. The binomial central limit theorem at $J=\lfloor ck+x\sqrt{k}\rfloor$ proves (10). The density in $a$ is taken first for each fixed $k,J$. At any fixed $k$ the density of exponents that never descend is zero, by (9) and the positive drift. A density statement still leaves individual exponents undecided.

## Where this leaves the conjecture

The checkpoint theorem limits every smaller ancestor of every point in this initial segment. A smaller source can still meet the trajectory later. The exact descent classes exhibit one way this happens. For an arbitrary exit, the quotient $(9^k t-5)/2^r$ need not be integral, and (1) gives no later meeting or descent. Proving such a meeting for every remaining start is open here.

Earlier work analyzes smaller companions for specified exits from the same negative cycle. The estimates above use its positive signed preimages and the divisibility of the ordinary start by three. [Earlier exit calculations and their provenance](https://github.com/GettysburgResearch/collatz/blob/65c91ecea97d9ebf931eb1d9284b7950182a298e/research/astra-exit-merging/PROOF.md)

## Verification

Lean 4.34.1 checks (1), the stronger bound for $A\ge6$, the small ordinary witness in (7) at the continued checkpoint, and the four-step equal-count exit. The direct-descent time, prescribed-target construction, divergence implication and density statements are written proofs. The separate checker replays 9,068 initial positions, including 4,325 with a smaller source on the tested clocks. It also reconstructs 74 small ordinary witnesses, replays 56 four-step equal-count exits and 54 prescribed-target paths, and checks 1,533 exponent lifts against the finite first-passage law. Run `python -B research/upper-bit-mergers/check_checkpoint.py` from the repository root. [Lean proof](HighBit.lean) · [Exact checker](check_checkpoint.py)
