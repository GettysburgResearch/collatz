# Full endpoint-profile entropy at the coefficient-stopping threshold

**PROPOSED, elementary orbit and word count.** Let $h,p$ be positive integers with $p\le h$ and $3^p\ge2^h$. In every aligned block of $2^h$ ordinary parameter values $u$, fix a designated arm $n=u$ or $n=3u$. There are at least

$$
 \frac{\binom hp}{h(1+h/2)}
$$

distinct exact ordered joint profiles among parameters for which the designated arm has exactly $p$ odd inputs and stays at least $n$ through **every** clock up to $h$. A joint profile records both integer endpoints and both odd counts at the same clock. All selected parameters are odd. For the additional ternary-unit condition, at least one of any three consecutive aligned blocks retains at least two thirds of the displayed lower bound. The same count applies to profiles recentered by their known block displacements.

Consequently, at $p=\lceil h\log_3 2\rceil$, the exponential rate is precisely $H_2(\log_3 2)=0.949955527\ldots$, counting before any all-time basin condition. The upper bound is the whole binomial slice. The matching entropy for *counts of source words* is recorded in the repository’s existing no-descent theorem. Here the lower bound survives projection onto the physical endpoint coordinate, after retaining the all-prefix restriction on the designated arm. [Existing source-word entropy and rotation argument](../../../integrated/exceptional-mass/README.md)

## The critical and supercritical grades

A cyclic rotation of each word of weight $p$ can arrange that every $j$-bit prefix has at least $pj/h$ odd bits. Choose the new start immediately after a minimum of the partial sums of $e_i-p/h$. Each rotation class has at most $h$ words. Its chosen representative has first bit 1 and every terminal segment of length $j$ has weight at most $pj/h$. At least $\binom hp/h$ words can therefore be used. On a complete parameter block each occurs once at the designated arm, since the ordinary parity map is bijective on residues modulo $2^h$ and multiplication by 3 is invertible there. For every positive proper or complete prefix the coefficient $3^{P_j}/2^j$ is at least $(3^{p/h}/2)^j\ge1$. All affine carries are nonnegative.

Put $d=3^{p/h}/2\ge1$. The exact endpoint $y=3^p n/2^h+\beta_w$ has normalized carry

$$
 0\le\beta_w
 =\sum_{t=1}^h e_{h-t}\frac{3^{P_{\mathrm{last}\ t-1}}}{2^t}
 \le\frac12\sum_{j=0}^{h-1}d^j
 \le \frac{h}{2}\frac{3^p}{2^h}.
$$

At fixed $y$ all designated inputs thus lie in a real interval of length at most $h/2$. There are at most $1+h/2$ admissible integers in that interval. The claimed number of distinct designated endpoints follows, and retaining the second arm and both counts can only distinguish more. For odd ternary units, take three consecutive aligned blocks. The three lifts of each word have parameters differing by $2^h$, hence exactly two are ternary units. At least one block retains two thirds of the selected words. Positivity holds on every positive block and also in the initial block because all selected starts are odd.

## Why this grade matters for a least directed failure

Suppose $u$ is the least forward or reverse failing unit for the basin of 1. The [round-seven directed paths](../../round7/head/README.md) imply that each positive bad vertex $y$ satisfies $u\le Ky$, with $K=167/27$ forward or $2351/123$ reverse. The designated bad start is $n_0=3u$ or $n_0=u$, respectively. Multiplying the exact ratios over its first $h$ steps, with $P$ odd inputs and $n_j=T^j n_0$, gives

$$
 \frac{u}{K}\le T^h n_0
  = n_0\frac{3^P}{2^h}\prod_{j<h,\ n_j\text{ odd}}
       \left(1+\frac1{3n_j}\right)
  \le n_0\frac{3^P}{2^h}\left(1+\frac{K}{3u}\right)^h .
$$

Therefore $P/h\ge\log_3 2-\log_3(Kn_0/u)/h-\log_3(1+K/(3u))$. At native clocks $h\asymp\log u$ the permitted lower deficit tends to zero as the candidate height grows. The word count at and above this threshold explains why near-central profile compression alone leaves the relevant tail. The selected words demonstrate the full finite-horizon entropy even with a prefixwise restriction stronger than the fixed floor. Whether a particular such pair carries a genuine all-time directed failure is a separate question.

## The exceptional saving in the near-central upper bound


**PROPOSED lower bound and scope check.** This uses just the first arm at clock $h$ on a complete aligned block of $2^h$ sources. Any joint profile retaining the first arm's exact endpoint and odd count refines that information. At a fixed count and aligned block a recentered endpoint differs from the ordinary endpoint by a fixed constant.

Fix $1/2<a<\log_3 2$, put $p=\lfloor ah\rfloor$, and use the binary entropy $H_2$. Among the weight-$p$ words there are at least $\binom hp/h$ whose terminal segments of every length $j$ have weight at most $pj/h$. Indeed rotate a word immediately after a minimum of the partial sums of $e_i-p/h$. Its new prefix sums are nonnegative, so its terminal sums are nonpositive. Every rotation class has at most $h$ members. At these words the first bit is 1. Every such word occurs at exactly one start per complete block by the ordinary parity bijection.

The normalized carry $\beta_w$ in $T^h x=3^p x/2^h+\beta_w$ satisfies

$$
 0\le \beta_w
 =\sum_{t=1}^h e_{h-t}3^{P_{\mathrm{last}\ t-1}}2^{-t}
 \le\sum_{t\ge1}3^{a(t-1)}2^{-t}
 =\frac1{2-3^a}.
$$

At one fixed physical endpoint the eligible starts are therefore confined to an interval containing at most $1+(2-3^a)^{-1}2^h/3^p$ integers. If at most $O(2^{(1-c)h})$ starts are discarded for a fixed $c>0$ and $H_2(a)>1-c$, Stirling's formula leaves $2^{H_2(a)h-o(h)}$ of these words. The remaining joint profiles number at least

$$
        2^{[H_2(a)-1+a\log_2 3-o(1)]h}.
$$

If one requires odd ternary-unit sources, first take any three consecutive aligned blocks. Two of the three lifts of every selected word are units, so at least one block retains the same exponential lower bound. This suffices to test bounds asserted uniformly over aligned blocks.

The displayed exponent exceeds $(\log_2 3)/2$ for all $a$ sufficiently close to $1/2$ from above. Its derivative there is $\log_2 3$, and $H_2(1/2)=1$. Hence a profile bound of $2^{[(\log_2 3)/2+o(1)]h}$ cannot hold alongside a fixed positive saving $c$ on the exceptional exponent. An upper bound with an arbitrary fixed error $\epsilon>0$ and a saving $c(\epsilon)>0$ retains its quantifiers. The [finite controls](../../../../reports/astra-global-closure-20261124/round8/unit/binary_controls.json) at $a=3/5$ enumerate all aligned inputs at clocks 5, 10 and 15, check the rotation counts and the carry ceiling, and report 2, 23 and 377 retained distinct endpoints.


At the critical and supercritical test grades $(h,p)=(8,6),(12,8),(15,10)$, the separate control tracked both choices of designated arm over three aligned parameter blocks. Each recorded word stayed above its designated start at every prefix. The smallest numbers of distinct selected endpoints across the three blocks were 4, 55 and 273 for either arm. [Exact control output](../../../../reports/astra-global-closure-20261124/round8/unit/binary_controls.json)
