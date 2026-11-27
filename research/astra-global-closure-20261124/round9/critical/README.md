# Cyclic order at the least bad multiple

**Written pointwise results. Collatz remains open.** At the least odd tripling disagreement, the bounded branch of PR205 has a primitive period ratio. Its odd cycle spans at least two dyadic intervals. A physical inverse path eliminates one whole ternary progression of possible minima. A fixed observation window can miss the required excursion on both sides of an ordinary source.

Use the shortcut map $T(2v)=v$, $T(2v+1)=3v+2$, and let $U(x)$ be the next odd iterate from an odd input. PR192 chooses the least positive odd $q$ for which reaching 1 differs between $q$ and $3q$. Then $q$ reaches 1, $n=3q$ does not, and all positive multiples of three below $n$ reach 1. In the bounded branch of PR205, $q=1\pmod{12}$ and $s=(n-1)/2$ is the minimum of a nontrivial cycle. The odd sites $x$ satisfy $s\le x\le (16s+7)/3$, and each $a(x)=v_2(3x+1)$ is 1 or 2. The other branch crosses $6q$ and can later escape or enter a cycle. [PR192 minimum](https://github.com/GettysburgResearch/collatz/blob/26f070c38ad9edd21ed7dac6efaab6554550c2a3/research/astra-minimum-source-20261124/minimal/MinimumFailure.lean) · [PR205 bounded branch](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/ordinary/HEIGHT_STRIP.md)

This lane independently reconstructed the three-band order, the coprimality of the full period pair and the weighted cycle congruence. The late PR192 cycle note derives the same results and gives a 41-odd-phase rational example with a proper common divisor. The earlier repository synthesis also contains the single-octave exclusion. PR193 strengthens it for sufficiently large odd period $p$, proving that more than $p/21$ odd phases exceed twice the minimum. [PR192 cycle order and denominator](https://github.com/GettysburgResearch/collatz/blob/a0d7c6e36c378bbb6c826002039aef486bbe0383/research/astra-universal-closure-20261124/cycle/README.md) · [Earlier single-octave proof, verified copy](https://github.com/GettysburgResearch/collatz/blob/fbe870ec44239e6b6c753bab9d1c7537acfff701/research/astra-global-synthesis-20261124/arithmetic/proof.md) · [PR193 cycle occupation](https://github.com/GettysburgResearch/collatz/blob/24cdd0e5471d4421716cfce6bd88916f858f994c/research/astra-universal-proof-20261124/critical/CYCLE_OCCUPATION.md)

## The full period ratio is an upper convergent

Consider any positive integer cycle with $p$ distinct odd sites $x_i$, indexed in its cyclic trajectory order, odd minimum $s$, and maximum odd site less than $8s$. Write $a_i=v_2(3x_i+1)$ and $h=\sum a_i$, the least shortcut period. Choose $k_i\in\{0,1,2\}$ uniquely so that $z_i=2^{-k_i}x_i\in[s,2s)$. These numbers are distinct because the $x_i$ are distinct and odd. Put $c_i=2^{-k_i}$. Then

$$
 z_{i+1}=(3z_i+c_i)/2^{b_i},\qquad b_i=a_i+k_{i+1}-k_i.
$$

In sorted $z$ order the values $g_i=3z_i+c_i$ increase strictly. Distinct $z$ differ by at least $1/4$ and the corrections lie in $[1/4,1]$, so the $g$'s weakly increase. Equality would give the same normalized successor because division by a power of two into $[s,2s)$ is unique. The successors are distinct. The first normalized site is $s$, where $g=3s+1$. The largest $g$ is less than $6s+1<2(3s+1)$. Consequently $b_i$ is 1 or 2. The division changes from 2 to 4 at the single cut $g=4s$. After normalization every site above the cut has image below every image from below the cut, since $\max g<2\min g$. Within each of the two blocks the order is preserved.

Let $r$ be the number of terms with $b_i=2$. On the sorted ranks $0,\ldots,p-1$ the permutation is therefore exactly $j\mapsto j+r\pmod p$. For $p>1$ its orbit is the whole set, so $\gcd(r,p)=1$. This is immediate also for $p=1$. The exponent changes telescope, giving $h=p+r$. Thus

$$
                   \gcd(h,p)=1.
$$

PR205's ceiling $(16s+7)/3$ is less than $8s$ for positive $s$. Its theorem gives $0<h/p-\log_2 3\ll p^{-100/49}$, with the reduced ratio an upper continued-fraction convergent for sufficiently large $q$. Here $p$ itself is the denominator of that convergent. In particular a nontrivial common multiple of a candidate numerator and denominator cannot be the least period data. Both the order argument and the coprimality result are unconditional. The continued-fraction conclusion uses the cited PR205 clock estimate.

## A nontrivial integer cycle must leave the first dyadic interval

If all odd sites lie in $[s,2s)$, then $k_i=0$ and $a_i=b_i$. For rank $j$, the letter $b$ is $1+\mathbf1_{j+r\ge p}$. Thus the letters along the rank orbit are the wraps of the rotation by $r$. For $p>1$ choose two starting ranks differing by one. The wrap indicators differ at just the two ranks $p-r-1$ and $p-1$, which are consecutive in the time order because adding $r$ to the first gives the second. At these two positions the two words exchange $12$ and $21$. A common cyclic rotation makes the exchange internal to the words.

For an exponent word starting at an odd site $x$, put $A_j=\sum_{i<j}a_i$. Ordinary composition gives

$$
 (2^h-3^p)x=\sum_{j=0}^{p-1}3^{p-1-j}2^{A_j}.
$$

Exchanging adjacent exponents 1 and 2 changes just one intermediate $A_j$ by one. The two right-hand sides differ by $\pm3^u2^v$. Both are divisible by the positive integer $D=2^h-3^p$, which is coprime to six. Therefore $D=1$. For $h\ge3$ this would give $3^p=7\pmod8$, impossible. For $p=1$, the equation $(2^h-3)x=1$ gives $h=2,x=1$. Hence every nontrivial integer cycle has an odd site at least $2s+1$.

The exclusion of the physical Christoffel word is classical in the current literature. The geometric conclusion comes from identifying the word by ordering the normalized physical sites. For the larger interval, only the normalized word is mechanical. The old adjacent-swap theorem does not apply directly to the physical word. [Knight, *Collatz high cycles do not exist*, Discrete Mathematics 349 (2026)](https://doi.org/10.1016/j.disc.2025.114812) · [Earlier repository treatment of perturbations](../../round3/cycles/README.md)

The obstruction already occurs in the positive rational cycle with odd sites $(283,431,653,493,373)/13$. Its actual exponent word is $(1,1,2,2,2)$, its dyadic indices are $(0,0,1,0,0)$, and its normalized exponent word is $(1,2,1,2,2)$. The latter is mechanical. The former contains both $11$ and $22$, so it is unbalanced. Its minimum $s=283/13$ also has $v_3(s-1)=3$, and the odd range ratio $653/283$ lies between 2 and $16/3$. This rational example distinguishes the two words even when the displayed range and local ternary conditions hold. It does not supply an ordinary integer counterexample.

There is an additional finite restriction on how the dyadic intervals interleave. For $p>1$, let $t$ make $rt=1\pmod p$. Let $E$ count the adjacent pairs in **sorted normalized order** at which $k$ changes, including the cyclic last pair. The two trajectories separated by $t$ have different $b$ at precisely two phases. There are at most $E+2$ phases with different $k$ or different $b$. Along $L$ consecutive agreeing phases, the difference of the two integer mantissas $4z$ is multiplied by $3^L/2^{\sum b}$. Successors remain integral, hence $2^{\sum b}$ divides a nonzero initial difference less than $4s$ in absolute value. The wrap formula gives $\sum b\ge Lh/p-1$. At least one gap has $L\ge p/(E+2)-1$. Combining gives

$$
  E+2>\frac{p}{1+(p/h)(1+\log_2(4s))}.
$$

This restriction measures changes in sorted order. It permits many such changes and does not eliminate the remaining cycles.

The normalized positions admit an explicit error at every rank. Start at $x_0=s$, write $j_i=ir\bmod p$, and put $d_i=\log_2(1+1/(3x_i))$. Their cyclic mean is $\bar d=h/p-\log_2 3$. Telescoping the normalized recurrence and the exact rotation wraps gives

$$
 \log_2(z_i/s)-j_i/p=\sum_{m<i}(d_m-\bar d),\qquad
 \left|\log_2(z_i/s)-j_i/p\right|\le\frac{p}{12s\log 2}.
$$

Indeed the partial centered sum equals $i(p-i)/p$ times the difference between the mean on the first $i$ sites and that on the others. Its absolute value is at most $p(\max d-\min d)/4$. Since $p^2/s\to0$ along any unbounded family of these candidate cycles, the error is $o(1/p)$ in logarithmic coordinate. In the normalized coordinate this gives $|z_i-s2^{j_i/p}|=O(p)$. In the ordinary coordinate it gives $|x_i-2^{k_i}s2^{j_i/p}|=O(p)$ since $k_i\le2$. This precision distinguishes the ranks but does not fix which quarter-integers or band indices occur.

## Ordinary inverse paths from the restricted minimum

For a unit odd endpoint $y$, the smallest allowable reverse odd exponent is 1 if $y=2\pmod3$ and 2 if $y=1\pmod3$. Its predecessor is $R(y)=(2^a y-1)/3$. On the restricted cycle it is the actual previous odd site. Put $v=v_3(s-1)=1+v_3(q-1)\ge2$. For $0\le j\le v$ the predecessor obtained after $j$ steps equals

$$
     R^j(s)=1+(4/3)^j(s-1).
$$

At $j=v$ the factor $(s-1)/3^v$ must be 1 modulo three, since residue 2 would put a multiple of three on the cycle. Six such steps exceed $(16s+7)/3$ for $s\ge28$. Hence $v\in\{2,3,4,5\}$ in this range, and the first nonzero ternary digit of $s-1$ is 1. These restrictions concern the actual minimum $q$, not the density of candidate words.

There is also a known good neighbor at every odd site of a restricted cycle. Set $G(x)=(x-1)/2$. On an exponent-one edge $G(x)$ is odd and $G(U(x))=T(G(x))$. On an exponent-two edge $x=8m+1$, so $G(x)=4m$ and $G(U(x))=3m$. The height ceiling gives $x<8q$, hence $0<m<q$. Minimality gives that both $m$ and $3m$ are good. Since $G(s)<q$ is good, following the cycle shows that every $G(x)$, and hence every $x-1$, is good. This does not identify any $x$ with its good neighbor.

A single extra factor of four in an inverse step cannot give a smaller bad multiple. At the first such step the rival predecessor is $4x+1$, where $x$ is the cycle predecessor. For $x=2\pmod3$ this already is a multiple of three. For $x=1\pmod3$ its next minimal predecessor is $2R(x)+1$, using $3R(x)+1=4x$. At a site of the form $2y+1$, the reverse chain stops if $y=1\pmod3$. If $y=2\pmod3$ the next minimal predecessor is $2R(y)+1$. It reaches the first case because an entire cycle of exponent 1 would strictly increase. Every odd point after the extra inverse step on this path is at least $2s+1=n$. The zero-detour path stays on the cycle. This rules out all depths under precisely this one-extra-factor restriction.

Allowing more choices gives an actual descent. For every integer $t\ge0$, set

$$
  s=116582680+129140163t,\qquad z=181749759+201326592t.
$$

Then $0<z<2s+1$, $3\mid z$, and $T^{26}z=s$. For odd $s$ the exact reverse odd exponents, read from $s$, are $(4,3,4,1,2,2,1,1,1,1,1,1,1,1,1,1)$. For even $s$ the same shortcut word stops within its final halving run. Its affine identity on both parities is $3^{16}z=2^{26}s-49385281$. Physical legality on the entire row is also obtained by translating the actual 26-step path from $181749759$ by $3\cdot2^{26}t$. It contains 16 odd inputs. Every odd $s$ on this row has odd $t$ and $q=(2s+1)/3=1\pmod{12}$. A hypothetical restricted minimum on this row would give a bad positive multiple of three below $3q$. Thus this entire progression is excluded. [Lean proof, `small_multiple`](CycleOrder.lean)

For $s\ge10^{11}$ with the required seventeen previous bounded odd sites, this is the first successful depth for the stated tests. All 7,813,124 eligible exponent compositions through depth sixteen were checked. None reaches the good interval, and the displayed ternary class is the only one reaching a smaller multiple of three. Its first such path has sixteen odd steps. The count permits arbitrarily many shortcut halvings through an explicit affine cutoff. [Derivation and complete count](SHALLOW_ANCESTORS.md)

## Arbitrarily long ordinary windows in the narrow interval

Fix $L\ge2$ and let $\theta=\log_2 3$. Prescribe the first $L$ forward odd exponents at $s$ by the prefix sums $F_j=\lfloor j\theta\rfloor$. Prescribe its $L$ reverse odd exponents by $B_j=\lceil j\theta\rceil$, starting with $B_0=0$. These specifications can hold simultaneously. The forward word is one odd binary cylinder modulo $2^{F_L+1}$, by the shortcut parity bijection with its final odd bit. The inverse word specifies one ternary cylinder modulo $3^L$, by iterating the affine odd-predecessor formula. Its first two exponents are both 2, giving $s=1\pmod9$. The Chinese remainder theorem supplies one infinite ordinary progression. Odd $s=1\pmod9$ gives $s=1\pmod{18}$ and $q=(2s+1)/3=1\pmod{12}$. The first two forward exponents are 1 and 2, so $s=16m+11$. The original $n=2s+1=32m+23$ and $s$ meet at the actual common point $T^5(n)=T^4(s)=27m+20$. This agreement holds on the entire CRT progression.

For $1\le j\le L$ the forward and reverse odd states on this progression have leading multiples of $s$ equal to $3^j/2^{F_j}$ and $2^{B_j}/3^j$, respectively. Their additive terms depend on the fixed words alone. Both leading multiples lie strictly between 1 and 2 because no positive power of 3 is a power of 2. Consequently every sufficiently large member has all $L$ odd sites on each side strictly between $s$ and $2s$. All inverse steps are positive and legal. The fixed exponent words contain only 1 and 2, so every even segment between odd sites is empty or a singleton. This is a finite-window assertion with $s$ free to grow with $L$. No fixed ordinary integer is asserted to survive all these tests.

## The remaining arithmetic step

All surviving restricted cycles must have some $k_i\ne0$. Their normalized equation is

$$
 (2^h-3^p)\,4z_0=\sum_{j=0}^{p-1}3^{p-1-j}2^{B_j}\,2^{2-k_j},\qquad B_j=\sum_{i<j}b_i.
$$

There is a modular form with a fixed ordered list of powers. For $D=2^h-3^p>1$, choose integers $A,B$ with $pA+hB=1$ and set $u=2^A3^B\pmod D$, using inverses for negative exponents. Then $u^p=2$ and $u^h=3$ modulo $D$. At the minimum phase $B_j=\lfloor jh/p\rfloor$ and $\ell_j=jh\bmod p$ runs over all ranks. Up to multiplication by one fixed unit each term $3^{p-1-j}2^{B_j}$ equals $u^{p-1-\ell_j}$ modulo $D$. Thus an actual integer cycle forces

$$
 F(u)=0\pmod D,\qquad F(X)=\sum_{\ell=0}^{p-1}c_\ell X^{p-1-\ell},\qquad c_{\ell_j}=2^{2-k_j},\quad c_0=4.
$$

A sufficient closing lemma for the bounded branch would rule out that congruence for the allowed nonconstant $k$ sequences, or find a common forward iterate with a positive multiple of three below $3q$ for every surviving least-disagreement candidate. All parameters at a given $(h,p)$ are finite, and the band transitions require $a_j=b_j+k_j-k_{j+1}\in\{1,2\}$. Constant coefficients are units times a geometric sum, and $(u-1)\sum_{i=0}^{p-1}u^i=u^p-1=1\pmod D$. For unrestricted coefficients the proposed nonvanishing is false even at the upper convergent $h/p=8/5$. Here $D=13$, $u=6$, and $(c_0,\ldots,c_4)=(4,1,2,2,2)$ gives $F(6)=5486=422\cdot13$. Its time-order indices $(0,1,2,1,1)$ give $a=(0,1,2,2,3)$, which violates the physical edge condition. This counterexample does not disprove the proposed lemma with admissible edges. The modular form is an explicit place to attack that lemma. It supplies no proof of its outstanding direction.

For admissible transitions, $B_j-k_j=\sum_{i<j}a_i$ because $k_0=0$. The polynomial expresses the complete physical cycle divisibility using sorted normalized ranks. The mechanical $b$-word and the full coprime $(h,p)$ are known. The factors $2^{2-k_j}\in\{1,2,4\}$ vary along the unknown physical cycle. They prevent subtracting neighboring rotations to obtain one pure $2,3$-power. Excluding the resulting integer cycles with the stated height, actual-edge, and least-disagreement conditions would close the bounded branch. The separate first-crossing branch still requires a smaller bad representative or a contradiction farther along its actual trajectory. The residue-avoidance conjecture that every nonconvergent ordinary trajectory meets $5\bmod8$ would exclude an all-singleton cycle but remains unproved. [Yolcu, Aaronson and Heule, *An Automated Approach to the Collatz Conjecture*, §4.5, Conjecture 4.12](https://www.cs.cmu.edu/~mheule/publications/collatz.pdf)

[Finite arithmetic control](check.py) · [Kernel-checked arithmetic and rank lemmas](CycleOrder.lean) · [Nonperiodic growth estimate](ESCAPE.md)
