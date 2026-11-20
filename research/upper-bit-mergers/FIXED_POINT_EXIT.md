# A smaller partner from the signed fixed point

**PROPOSED, unconditional.** Use the positive shortcut map $T(x)=x/2$ on even inputs and $(3x+1)/2$ on odd inputs. Write $s_i(x)$ for the number of odd inputs before clock $i$. Consider the starts $n=8^k t-5$, where $k,t\ge1$, and put $W=9^k t$. The [negative-five checkpoint](NEGATIVE_FIVE_CHECKPOINT.md) gives $T^{3k}(n)=W-5$ with $2k$ odd inputs.

## A comparison outside the three cycle phases

If $W\equiv9\pmod{128}$ and $k\ge2$, let $m=2\cdot4^k t-1$. Then $0<m<n$. Writing $W=128u+9$ gives the exact endpoints and odd counts below.

$$
 T^{3k+7}(n)=T^{2k+8}(m)=27u+2,\qquad
 s_{3k+7}(n)=s_{2k+8}(m)=2k+3.
$$

The smaller arm comes from the signed fixed point $-1$. On an odd input $T(x)+1=3(x+1)/2$. Thus $2^b t-1$ takes $b$ consecutive odd steps to $3^b t-1$, including when $t$ is even. With $b=2k+1$ its endpoint is $3W-1$. The two intermediate values are $128u+4$ and $384u+26$. At $u=0$ the upper path is $4,2,1,2,1,2,1,2$ and the lower path is $26,13,20,10,5,8,4,2$. Their odd counts are three and two. Adding $2^7 v$ to a source adds $3^{s_7}v$ to its seventh iterate and preserves its seven parities. Taking $v=u$ and $v=3u$ gives exactly the displayed endpoint. Finally $n-m=4^k(2^k-2)t-4>0$ for $k\ge2$. At $k=1$ the same residue condition makes $t$ odd and $n=16v+3$ for $v=(t-1)/2$. Then $T^4(n)=9v+2<n$.

For $k\ge4$, $m/n\le2^{1-k}$ by multiplying both sides by $2^k n$. For $k\ge17$ the whole upper path through the meeting stays strictly above $n$ after time zero. The initial three-step blocks increase their starting value at each of the three checkpoints inside the block. At their end $W-5>(9/8)^k n$. In the next seven steps the smallest prefix multiplier is $9/64$ (at the sixth step), and every additive offset is nonnegative. Since $9^{18}>64\cdot8^{17}$, the claimed strict inequality follows. Thus the upper orbit can still be above its initial value when it joins a source smaller by an arbitrarily large factor.

For each fixed $k$, precisely one of the 128 binary lifts of $n\equiv-5\pmod{8^k}$ satisfies the stated congruence. This lift is attained by an arithmetic progression of exponents $a$ with $n=3^a$, by the order of 3 modulo powers of two. These powers are excluded as least counterexamples. In particular this handles every sufficiently deep cylinder used in the previous bounded-comparison obstruction. There the test variable was $X=9^{k-1}t\equiv1\pmod{2^H}$, and $H\ge7$ implies $W=9X\equiv9\pmod{128}$. The previous impossibility concerned smaller candidates obtained from the three phases of the cycle through $-5$.

## Prescribing the subsequent target

For any $k\ge2$, $A\ge0$ and positive $q$ coprime to three, there are infinitely many examples with $3^A\mid n$ whose common endpoint subsequently reaches $q$ by halvings. Choose $L$ from

$$
 128\cdot8^k q\,2^L\equiv135\cdot9^k+13\cdot8^k
 \pmod {3^{2k+3+A}}.
$$

Both coefficients of this discrete logarithm are units. The powers of two generate the units modulo $3^h$, as shown in the [checkpoint proof](NEGATIVE_FIVE_CHECKPOINT.md). Thus the congruence admits an arithmetic progression of $L$. For large such $L$ put $t=(128q2^L-13)/(27\cdot9^k)$. The congruence gives a positive integral $t$ and $3^A\mid8^k t-5$. The equation $27W+13=128q2^L$ implies $W\equiv9\pmod{128}$ and the common endpoint is $q2^L$. This construction permits arbitrary $q$ without requiring $n$ to be a power of three.

The result supplies an actual reduction for the indicated residue class. Extending it to all exits, or proving convergence of all smaller partners, remains open.

## A gap of four and a uniform bound for powers of three

Use the same fixed point, now taking $m_0=4^k t-1$. After $2k$ odd steps it reaches $W-1$, exactly four above the upper endpoint $Y=W-5$. At $k\ge2$ it is smaller than $n$, and at $k\ge3$ it satisfies $m_0/n\le2^{-k}$ since $2^k m_0=n+5-2^k$. At $k=1$ it is smaller for $t>1$. The remaining start $n=3$ reaches 1.

An unconditional cylinder is $W=32v+21$. The endpoints $Y=32v+16$ and $Y+4=32v+20$ reach $3v+2$ after five steps, each with one odd input. Indeed the base starts 16 and 20 both reach 2 at that clock with one odd input, and adding $32v$ preserves the word. This gives a smaller partner on one thirty-second of the eligible exponent lifts.

**SOURCE-QUALIFIED quantitative conclusion.** David Leen’s public preprint *Quantitative synchronization of Collatz trajectories* (version 1, 9 October 2026) states the following theorem, “Uniform pair absorption.” For initial level zero and offset $D$, the fraction of dyadic classes surviving without symbolic absorption to depth $H$ is at most $C\sqrt{(1+\log(1+|D|))/H}$. Its “Fresh labels and exact cylinders” and “Clock and halving-count realization” lemmas identify absorption with a sufficient certificate of equal endpoints and equal odd counts at the same shortcut clock. These are results about the pair of actual maps driven by the same starting residue. The paper credits Said Duran for the earlier qualitative coalescence conclusion. We use the stated estimate as an external input. [Primary source, including full TeX](https://doi.org/10.5281/zenodo.23268755)

Fix $k\ge1$ and sample exponents $a$ conditionally on $8^k\mid3^a+5$. The $2^H$ exponent lifts of that class correspond bijectively to every residue of $t=(3^a+5)/8^k$ modulo $2^H$. Multiplication by $9^k$ and subtraction of 5 send these lifts bijectively to the residues of $Y$. Leen’s estimate at $D=4$ therefore leaves at most $O(H^{-1/2})$ of these exponent lifts without the certificate, with an absolute constant **independent of $k$**. Every good lift has $T^{3k+H}(n)=T^{2k+H}(m_0)$ and equal total odd counts at those two clocks. A certificate at an earlier time can be advanced to $H$ along the common future. Thus for every $\epsilon>0$ one common additional horizon $H=O(\epsilon^{-2})$ works for a proportion at least $1-\epsilon$ at every $k$. The limit in the exponent is taken at each fixed $k,H$.

In particular choose $H=\lfloor k\log_2(9/8)\rfloor$. As $k\to\infty$, at least a proportion $1-O(k^{-1/2})$ of the eligible exponents have a partner $m_0\le2^{-k}n$ at this deadline. Throughout the upper path the starting value has yet to be undercut. After the initial blocks its value exceeds $(9/8)^k n$ and even $H$ successive halvings could not take it below $n$. The estimate controls a relative density and leaves open individual exponents.

## Which periodic template can save these steps?

Among integer cycles of the signed shortcut map, only the fixed point $-1$ can have more than two odd inputs per three steps on average. The zero cycle has none. Any positive cycle of length $L$ and odd count $q$ has $3^q<2^L$ by the positive affine offset along the period, giving $q/L<\log_3 2<2/3$. For a negative cycle pass to the mirror map $S$. The magnitudes 1 through 4 all reach 1, so every other negative cycle has magnitudes at least 5. For the weight $F(7)=50$ and $F(x)=x^2$ elsewhere, the [checkpoint proof](NEGATIVE_FIVE_CHECKPOINT.md#the-signed-path-controls-the-last-odd-steps) gives $4F(Sx)\ge8^{x\bmod2}F(x)$. Telescoping one full cycle gives $4^L\ge8^q$ and hence $q/L\le2/3$. If the cycle contains 5 or 7, it is the known cycle through 5, 7 and 10 and equality holds. Every other such cycle contains an odd magnitude at least 9, where $(3x-1)^2>8x^2$ makes the inequality strict. Thus within the method of repeating complete integer cycles to supply $2k$ odd steps, the uniquely faster baseline is $-1$, whether or not other integer cycles exist.
