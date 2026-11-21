# A bounded number of odd steps cannot reduce every Mersenne exponent

**Proposed theorem.** Use the positive shortcut Collatz map $T$, and write $U_n=3^n-1$ for $n\ge1$. For every $H\ge4$ there is an entire arithmetic progression of exponents $n\equiv1\pmod6$ such that, whenever $n\ge4H$ belongs to that progression,

$$
 T^i(U_n)\ne T^j(U_m)\qquad(1\le m<n,\quad 0\le i,j\le H).
$$

These same $n$ have a stronger property. If $B\ge0$ is an integer and $3B+3\le H$, no two paths from $U_n$ and any $U_m$ with $1\le m<n$ can meet using at most $B$ odd steps on each arm, even when both clocks count arbitrarily many even steps. One can choose such $n$ with $H\ge\log_2 n-O(1)$. The conclusions apply simultaneously to **all** smaller positive exponents.

These are ordinary checkpoints in the one-sided Collatz criterion. Write $n=6r+1$, $r\ge1$, and take $k=(2^{6r}-1)/9$. Four steps take $16k+1$ to $2^{6r}$ with two odd inputs, and the remaining halvings reach 1. The same four steps from $32k+1$ give $2^n-1$. Its next $n$ inputs are odd and its endpoint is $U_n$, since its $i$th iterate is $3^i2^{n-i}-1$ for $0\le i\le n$. The theorem concerns the search for an earlier exponent after this forced segment. Whether all these targets reach 1 remains open. [One-sided criterion](THREE_RAY_ONE_SIDED.md)

## Selecting the exponent

Impose $3^n\equiv-5\pmod{2^H}$. As $n=6r+1$ varies, $3^n$ runs through every residue congruent to 3 modulo 8 at precision $2^H$. Indeed $v_2(3^6-1)=3$, and successive squaring increases this valuation by exactly one because $3^6\equiv1\pmod8$. Thus $3^6$ has order $2^{H-3}$ modulo $2^H$, and its powers give the entire subgroup congruent to 1 modulo 8. The required $r$ form one class modulo $2^{H-3}$. A qualifying $n$ lies in $[4H,4H+6\cdot2^{H-3})$, proving the asserted logarithmic relation.

## A common endpoint would have to match the two affine slopes

Suppose $i,j\le H$, and write $p,q$ for the odd counts on the two arms. For any length-$i$ parity word the endpoint is $(3^p x+a)/2^i$, where $0\le a\le3^i-2^i$. An even step leaves the numerator offset fixed and an odd step replaces it by $3a+2^i$, proving the bound by induction. Use $b$ for the other offset and $d=n-m$. Endpoint equality would give

$$
 3^m(2^j3^{p+d}-2^i3^q)=2^i(b-3^q)-2^j(a-3^p).
$$

The right-hand side has magnitude at most $2\cdot6^H$. For $m>2H$, $3^m$ is larger than this, so the integer in parentheses vanishes. Unique factorization then forces $i=j$ and $q-p=d$. For $m\le2H$ the inputs already differ too much in size: $U_n/U_m>3^{n-m}\ge9^H>4^H$. Each positive step multiplies size by a factor in $[1/2,2]$. Hence the two segments through clock $H$ are disjoint in this case.

## The required odd counts cannot occur

The first $H$ parities of $U_n$ agree with those of $-6$, since $U_n\equiv-6\pmod{2^H}$. For tracing parities only, the two shortcut formulas also apply to rationals with odd denominator. Congruence modulo $2^e$ fixes the parity and implies congruence of the two outputs modulo $2^{e-1}$. The comparison can therefore use rational representatives for the first $H$ parities of each positive input.

The representative of the upper arm runs $-6,-3,-4,-2,-1,-1,\ldots$. Its first four parities are $E,O,E,E$, followed entirely by odd inputs. Thus $p\ge i-3$. At equal clocks the difference $q-p$ is at most three, leaving only $d=1,2,3$. For these values, $U_m\equiv-5/3^d-1\pmod{2^H}$. The following table lists the actual inputs of each representative through its first four steps.

| $d$ | First four inputs of the lower representative | Largest $q-p$ at clocks 0 through 4 |
|---:|:---|---:|
| 1 | $-8/3,-4/3,-2/3,-1/3$ | 0 |
| 2 | $-14/9,-7/9,-2/3,-1/3$ | 1 |
| 3 | $-32/27,-16/27,-8/27,-4/27$ | 0 |

For every subsequent step through $H$, the upper odd count increases by one, so $q-p$ cannot increase. In every case $q-p<d$, excluding the required equal-slope event and proving the clock assertion.

Finally suppose an arbitrary meeting uses at most $B$ odd inputs on each arm, where $3B+3\le H$. The upper arm must stop at $i\le B+3$: at clock $B+4\le H$ it would already have at least $B+1$ odd inputs. An even step halves its input and an odd step increases it by a factor of at most two. Consequently

$$
 2^{-i}U_n\le T^i(U_n)=T^j(U_m)\le 2^{2B-j} U_m < 2^{2B-j} U_n.
$$

This forces $j<i+2B\le3B+3\le H$. The meeting would therefore be within the already excluded clocks on both arms. This proves the odd-count assertion.

## A short upper path forces a linear odd count on the lower path

Keep the same exponents $n$, the same $H$, and any earlier exponent $1\le m<n$. Suppose a meeting $T^i(U_n)=T^j(U_m)$ exists with $0\le i\le H$. Now impose **no upper bound on $j$**. If $q$ is the odd count on the lower path, then

$$
 q>\frac{m+(n-m)\log_2 3}{2}-i>\frac n2-i. \tag{1}
$$

In particular, at $n\ge4H$, any earlier exponent needs more than $n/4$ odd steps on its own arm to reach *any* of the first $H+1$ states of the upper orbit. This also bounds the number of ordinary steps, since $j\ge q$. On the exponents chosen with $H$ of order $\log n$, the two clock budgets differ by an exponential factor.

To prove (1), the integer $2^j3^{p+n-m}-2^i3^q$ in the endpoint identity is nonzero. Its vanishing would force $i=j$, bringing the lower clock back within $H$. The parity argument at the signed center already excluded the resulting odd-count equality for every $m<n$. Hence the other side of the identity is a nonzero multiple of $3^m$. The length-$i$ offset bound gives $|a-3^p|\le3^i$, and likewise $|b-3^q|\le3^j$, so

$$
 3^m\le 2^i3^j+2^j3^i\le2\cdot3^{i+j}<3^{i+j+1}.
$$

It follows that $m\le i+j$. Each odd step multiplies a positive input by at most two, while each even step halves it. A meeting therefore requires

$$
 2^{-i}U_n\le 2^{2q-j}U_m,\qquad U_n/U_m>3^{n-m}.
$$

Together these inequalities give $m\le i+j<2i+2q-(n-m)\log_2 3$, proving (1).

## How far a chain of short exponent comparisons can move

There is also a bound for **every** exponent $n>5H$, without a residue restriction. On the positive exponents join $e$ and $f$ if $U_e$ and $U_f$ meet with both clocks at most $H$. The entire connected component of $n$ in this graph lies in $[n-H,n+H]$. All its members $e$ have the same ordinary endpoint at clock $H$, and the same value of $e+s_H(U_e)$, where $s_H$ counts odd inputs in those $H$ steps. This allows arbitrarily many links, in either direction and through any positive exponents.

Indeed any edge with $e,f>2H$ has equal meeting clocks by the affine-slope calculation above. At the meeting the exponent plus the odd count agrees on its two arms. Both paths have exactly the same suffix to clock $H$, so both equalities persist there. They therefore persist along any chain made entirely of exponents greater than $2H$. Since an odd count through clock $H$ lies between zero and $H$, each exponent in such a chain from $n$ is within $H$ of $n$. In particular it exceeds $4H$. It cannot be joined to any exponent $m\le2H$, by the size bound $U_e/U_m>4^H$ used above. Thus a chain cannot leave the asserted range even by first passing through a small exponent.

For example, any chain from $U_n$ to $U_1$ must have an edge requiring a clock of at least $n/5$ for $n\ge3$. This conclusion concerns chains whose vertices are all shifted ternary powers. Allowing unrelated intermediate ordinary starts is a different proof problem.

## Positive descent from the Mersenne start to an unrelated smaller integer

For every $L\ge2$ there is an explicit arithmetic progression of exponents $e\equiv1\pmod6$ on which $M=2^e-1$ has an odd positive predecessor

$$
 w=\frac{2^{L+1}(2^{e+3}-7)}{3^{L+2}}-1
 < \frac{16}{9}(2/3)^L M.
$$

Choose $2^{e+3}\equiv7\pmod{3^{L+2}}$. The powers of 2 generate the units of this modulus, by $v_3(2^{2\cdot3^j}-1)=j+1$. Reduction modulo 9 gives $e\equiv1\pmod6$, and the indices $j=(e-1)/6$ form one residue modulo $3^L$. Starting at $M$, use the odd predecessor $(4n-1)/3$ twice. Both moves are legal since $M\equiv1\pmod9$. The second result $u=(16M-7)/9$ satisfies $3^L\mid u+1$. Taking the odd predecessor $(2n-1)/3$ another $L$ times multiplies $u+1$ by $(2/3)^L$ and gives $w$. It is positive since $u+1\ge3^L$. Reversing the word proves that $w$ reaches $M$ by ordinary steps. Taking $L=2$ gives the strict factor $64/81$ on one ninth of the rank-two exponents. For any fixed $0<\theta<1$, take $L=\lfloor\theta\log_3 N\rfloor$. Every interval of $N$ consecutive nonnegative indices $j$ contains $\gg N^{1-\theta}$ such exponents, each admitting $w\ll M/N^{\theta(1-\log_3 2)}$. These are genuine smaller positive witnesses. Their own convergence remains open.

There are also many *distinct odd ternary units* below $M$ whose paths reach it on these progressions. Stop one move early at $z=(2/3)^{L-1}(u+1)-1$. Then $z\equiv-1\pmod3$ and $z\ll (2/3)^L M$. Given an odd ternary unit $b$, among $1\le v\le6$ exactly three exponents have $2^v b\equiv1\pmod3$, and just one of these has $2^v b\equiv1\pmod9$. The other two yield distinct odd ternary-unit predecessors, each at most $(64/3)b$. At any fixed depth $d$ the resulting $2^d$ nodes are distinct, since each start determines its sequence of odd iterates and its intervening powers of two. For sufficiently large $L$, take $d=\lfloor\log(M/(2z))/\log(64/3)\rfloor$. All these starts are at most $M/2$, and all reach $M$ through $z$. Their number is $\gg (3/2)^{L\log 2/\log(64/3)}$. In particular choose $e$ on the indicated progression in $[3^{L+2},3^{L+3}]$, which is possible by its period $2\cdot3^{L+1}$. This gives infinitely many $e$ with $\gg e^\beta$ distinct such smaller predecessors, where $\beta=(1-\log_3 2)\log 2/\log(64/3)>0.0835$.

## A positive fraction require more inverse odd steps

For every sufficiently large $N$, in **every** interval of $N$ consecutive nonnegative indices $j$, at least $0.30N$ starts $M=2^{6j+1}-1$ have no smaller positive predecessor reaching $M$ with at most $\lfloor\log_3 N\rfloor$ odd steps. This bound allows arbitrarily many even steps. It concerns a path ending at $M$ itself. The forward apex $3^{6j+1}-1$ and arbitrary later points are different targets.

It suffices to consider odd predecessors, by initially stripping powers of two from any smaller positive start. In reverse, an accelerated odd word has exponents $v_i\ge1$ for moves $n\mapsto(2^{v_i}n-1)/3$. Write $V_i=\sum_{a=1}^i v_a$. After $\ell$ moves its output is

$$
 \frac{2^{V_\ell}}{3^\ell}\left(M-\sum_{i=1}^\ell3^{i-1}2^{-V_i}\right).
$$

If $M\ge3^\ell(3^\ell+1)$ and this output is smaller than $M$, then $2^{V_\ell}<3^\ell$. Indeed the parenthesized subtraction is less than $3^\ell$, and $2^{V_\ell}\ge3^\ell+1$ makes the output at least $M$. The size hypothesis for every $\ell\le\lfloor\log_3 N\rfloor$ removes only $O(\log N)$ small $j$. Each contraction therefore has an initial word that first attains $2^{V_\ell}<3^\ell$ at its last letter.

Let $f_\ell$ count these first words. Their total residue mass satisfies $\sum_{\ell\ge1} f_\ell/3^\ell<0.520$. Here are exact verification details. At length $l$, the number of candidate words of weight $v$ is the sum of the surviving counts at all previous weights less than $v$, since the new letter is positive. Remove and count the candidates with $2^v<3^l$; all other candidates survive. The row before the first letter has one word of weight zero. Through length 200 it suffices to keep weights at most $\lfloor\log_2 3^{200}\rfloor$, since larger weights cannot contribute within those lengths. The [exact integer and rational replay](check_mersenne_predecessors.py) gives $\sum_{\ell=1}^{200}f_\ell/3^\ell<0.518$. For the infinite tail, give the letters independent probabilities $2\cdot3^{-v}$. A first word has probability $2^\ell3^{-V_\ell}$ and $3^{-\ell}$ is at most this probability times $r^\ell$, where $r=3^{3/5}/2<1$ since $\log_2 3<8/5$. First words are prefix-free, so their probabilities sum to at most one. The tail is bounded by $r^{200}=(27/32)^{40}<0.002$. This also gives $f_\ell\le(3r)^\ell$ individually.

The first two word counts are $f_1=f_2=1$, from the words $(1)$ and $(2,1)$. Neither is legal for $M\equiv1\pmod9$. Every other word of length $\ell$ specifies at most one ternary class of $M$ modulo $3^\ell$ by integrality of its output. Since $2^{6j+1}-1$ samples all the classes $1\pmod9$ equally modulo $3^\ell$, this costs at most $N/3^{\ell-2}+1$ indices per word. The total rounding error through $H=\lfloor\log_3 N\rfloor$ is $O((3r)^H)=o(N)$. Removing the two impossible short words leaves at most $9(0.520-1/3-1/9)N+o(N)=0.68N+o(N)$ eligible exponents. This proves the asserted lower bound on the number requiring longer paths, with all errors uniform in the location of the interval.
